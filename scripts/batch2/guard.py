#!/usr/bin/env python3
"""Mechanical post-commit guard for the batch-2 unattended pipeline.

NOT model judgment: pure path/line rules over commit diffs.

  guard.py check <sha>          exit 0 clean / 3 violations (printed)
  guard.py sweep --base <sha>   re-check every commit in base..HEAD,
                                revert unguarded violators, fix worklist
                                rows, append escalations; exit 0

Rules per commit:
  - PROTECTED PATHS: any touched path equal to / under:
      CLAUDE.md, STOP, sources/source-registry.md,
      sources/batch-2-analysis.md, sources/transcripts/, scripts/,
      profiles/, skills/, prompts/, .claude/, .github/
  - DELETION RULE: >10 lines deleted from any curated note — any *.md
    outside sources/transcripts/, excluding sources/extraction-log.md,
    sources/escalations.md, sources/batch-2-progress.md, and README.md
    files (generated indexes; a legitimate mermaid-cap collapse deletes
    ~35 lines).

Revert commits carry the trailer  Batch2-Guard: revert-of <sha>  and are
skipped by the sweep (as are commits already covered by such a revert).
"""
from __future__ import annotations

import datetime
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PROTECTED = (
    "CLAUDE.md", "STOP", "sources/source-registry.md",
    "sources/batch-2-analysis.md", "sources/transcripts/", "scripts/",
    "profiles/", "skills/", "prompts/", ".claude/", ".github/",
)
DELETION_EXEMPT = {
    "sources/extraction-log.md", "sources/escalations.md",
    "sources/batch-2-progress.md",
}
TRAILER = "Batch2-Guard: revert-of"


def git(*args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def is_protected(path: str) -> bool:
    return any(path == p or path.startswith(p) for p in PROTECTED)


def violations(sha: str) -> list[str]:
    out = git("show", "-m", "--first-parent", "--numstat", "--format=", sha)
    probs = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, deleted, path = parts
        # rename syntax "old => new" — check both sides
        for p in re.split(r"\s=>\s", path.replace("{", "").replace("}", "")):
            p = p.strip()
            if not p:
                continue
            if is_protected(p):
                probs.append(f"protected path touched: {p}")
        if (path.endswith(".md") and not path.startswith("sources/transcripts/")
                and path not in DELETION_EXEMPT
                and os.path.basename(path) != "README.md"
                and deleted.isdigit() and int(deleted) > 10):
            probs.append(f"deleted {deleted} lines from curated note: {path}")
    return probs


def append_escalation(video_id: str, etype: str, reason: str) -> None:
    esc = ROOT / "sources" / "escalations.md"
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    run = os.environ.get("GITHUB_RUN_ID", "local")
    with esc.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {ts} — {video_id} — {etype}\n- run: {run}\n- reason: {reason}\n")


RESULT_MAX = 600


def _fit(s: str, limit: int = RESULT_MAX) -> str:
    """Trim a worklist result cell to `limit`, on a word boundary, marked.

    The old cap was a bare [:200], which cut mid-word and left rows reading as
    though the pipeline had crashed ("...the only calico-specif"). Truncating
    visibly means a reader can tell the difference between a short result and
    a clipped one.
    """
    s = s.strip()
    if len(s) <= limit:
        return s
    cut = s[: limit - 1]
    sp = cut.rfind(" ")
    if sp > limit * 0.6:  # only back up to a space if it isn't a huge loss
        cut = cut[:sp]
    return cut.rstrip(" ,;:-") + "…"


def set_row_status(video_id: str, status: str, result: str) -> bool:
    log = ROOT / "sources" / "extraction-log.md"
    text = log.read_text(encoding="utf-8")
    pat = re.compile(rf"^\| {re.escape(video_id)} \| ([^|]+)\| ([^|]+)\| ([^|]+)\| ([^|]+)\| ([^|]*)\|$", re.M)
    m = pat.search(text)
    if not m:
        return False
    clean = _fit(result.replace("|", "/").replace("\n", " "))
    new = f"| {video_id} | {m.group(1)}| {m.group(2)}| {m.group(3)}| {status} | {clean} |"
    log.write_text(text[: m.start()] + new + text[m.end():], encoding="utf-8")
    return True


def video_id_of(sha: str) -> str | None:
    subj = git("log", "-1", "--format=%s", sha).strip()
    m = re.match(r"batch2: (\S+) —", subj) or re.match(r"batch2: (\S+) -", subj)
    return m.group(1) if m else None


def cmd_check(sha: str) -> int:
    probs = violations(sha)
    for p in probs:
        print(f"GUARD VIOLATION [{sha[:9]}]: {p}")
    return 3 if probs else 0


def cmd_sweep(base: str) -> int:
    shas = git("rev-list", "--first-parent", "--reverse", f"{base}..HEAD").split()
    reverted_targets: set[str] = set()
    for s in shas:
        body = git("log", "-1", "--format=%B", s)
        m = re.search(rf"{TRAILER} (\S+)", body)
        if m:
            reverted_targets.add(m.group(1))
    fixed = 0
    for s in reversed(shas):  # newest first so reverts apply cleanly
        body = git("log", "-1", "--format=%B", s)
        if TRAILER in body or s in reverted_targets or any(s.startswith(t) or t.startswith(s) for t in reverted_targets):
            continue
        probs = violations(s)
        if not probs:
            continue
        print(f"SWEEP: reverting {s[:9]}: {probs[0]}")
        r = subprocess.run(["git", "revert", "--no-edit", s], cwd=ROOT,
                           capture_output=True, text=True)
        vid = video_id_of(s) or "unknown"
        if r.returncode != 0:
            subprocess.run(["git", "revert", "--abort"], cwd=ROOT, capture_output=True)
            append_escalation(vid, "guard-violation",
                              f"sweep found violation in {s} but revert conflicted — "
                              f"MANUAL ATTENTION: {probs[0]}")
            continue
        git("commit", "--amend", "-m",
            git("log", "-1", "--format=%B", "HEAD").strip()
            + f"\n\n{TRAILER} {s}")
        append_escalation(vid, "guard-violation",
                          f"sweep reverted {s}: " + "; ".join(probs))
        if vid != "unknown":
            set_row_status(vid, "escalated", f"escalated: guard: {probs[0]}")
        fixed += 1
    if fixed:
        subprocess.run(["python", "scripts/link-maintenance.py"], cwd=ROOT)
        git("add", "-A")
        if git("status", "--porcelain").strip():
            git("commit", "-m", "batch2: guard sweep fixups (worklist rows + escalations)")
    print(f"sweep complete: {fixed} commit(s) reverted")
    return 0


def main() -> int:
    if len(sys.argv) >= 3 and sys.argv[1] == "check":
        return cmd_check(sys.argv[2])
    if len(sys.argv) >= 4 and sys.argv[1] == "sweep" and sys.argv[2] == "--base":
        return cmd_sweep(sys.argv[3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
