#!/usr/bin/env python3
"""Mechanical post-commit guard for the unattended EDITORIAL REVIEW fleet.

Adapted from scripts/batch2/guard.py (same CLI, same revert mechanics) with
the rules the review needs: the batch-2 deletion rule reads legitimate
compression as vandalism (the observation split deliberately removes hundreds
of lines per note), so it is replaced by SCOPE and CONSERVATION rules that
check where a commit reached and whether information survived, not how many
lines moved.

  guard.py check <sha>          exit 0 clean / 3 violations (printed)
  guard.py sweep --base <sha>   re-check every commit in base..HEAD authored
                                by the pipeline identity, revert violators,
                                fix worklist rows, append escalations; exit 0

Commit-subject grammar the rules key off:

  review: <note-path> — <phase>        one note (+ its evidence file)
  review: relocate <src> → <dst>       a relocation-queue move (paired scope)
  review: progress checkpoint          checkpoint step (logs only)
  review: guard sweep fixups           the sweep's own bookkeeping

Rules per pipeline commit:
  - PROTECTED PATHS (unchanged from batch 2, plus templates/): the fleet can
    never touch CLAUDE.md, STOP, sources/source-registry.md,
    sources/batch-2-analysis.md, sources/transcripts/, scripts/, profiles/,
    skills/, prompts/, .claude/, .github/, templates/.
  - SCOPE: the touch-set must stay inside the subject's named note(s), their
    evidence files, README.md files (generated indexes), and the exempt logs.
  - CONSERVATION (named notes): a note or evidence file is never deleted;
    every source id cited in the note before must appear in the note or its
    evidence file after; every `**Observed**` block removed from the note
    must be matched by at least as many evidence entries added. A relocate
    commit checks the same over the src+dst pair as a unit.

Revert commits carry the trailer  Review-Guard: revert-of <sha>  and are
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
    "profiles/", "skills/", "prompts/", ".claude/", ".github/", "templates/",
)
# Append-only / regenerated bookkeeping the fleet may always touch.
EXEMPT_LOGS = {
    "sources/review-worklist.md", "sources/fact-check-ledger.md",
    "sources/review-progress.md", "sources/gap-report.md",
    "sources/spot-harvest.md", "sources/relocation-queue.md",
    "sources/regulatory-claims.md", "sources/escalations.md",
    "sources/extraction-log.md",
}
TRAILER = "Review-Guard: revert-of"

# Sweep polices only unattended-pipeline commits (see batch2/guard.py for why:
# applying it to supervised commits reverted reviewed work twice).
PIPELINE_AUTHORS = {"41898282+claude[bot]@users.noreply.github.com"}

SUBJ_NOTE_RE = re.compile(r"^review: (\S+\.md) [—-] ")
SUBJ_RELOCATE_RE = re.compile(r"^review: relocate (\S+\.md) (?:→|->) (\S+\.md)$")
SUBJ_CLUSTER_RE = re.compile(r"^review: (cluster:\S+) [—-] ")
SUBJ_EXEMPT_RE = re.compile(r"^review: (progress checkpoint|guard sweep fixups)")

# Observed blocks appear bare, as bullets, indented, and blockquoted.
OBSERVED_RE = re.compile(r"^[ \t>-]*\*\*Observed\*\*", re.M)
# Evidence entries are one-line bullets carrying a backticked source id.
EVIDENCE_ENTRY_RE = re.compile(r"^- .*`[A-Za-z0-9_-]{11}`", re.M)
# Cited-source tokens: front-matter sources entries, backticked ids, and bare
# ids in parens (legacy — resolve-cites retires them, but conservation still
# protects them if one survives).
BACKTICK_ID_RE = re.compile(r"`([A-Za-z0-9_-]{11})`")
PAREN_ID_RE = re.compile(r"\(([A-Za-z0-9_-]{11})\)")
FM_SOURCES_RE = re.compile(r"^sources:\s*\[(.*?)\]", re.M | re.S)


def git(*args: str, check: bool = True) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def show(sha: str, path: str) -> str | None:
    """File content at <sha>, or None when it did not exist there."""
    r = subprocess.run(["git", "show", f"{sha}:{path}"], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def is_protected(path: str) -> bool:
    return any(path == p or path.startswith(p) for p in PROTECTED)


def evidence_path(note: str) -> str:
    p = Path(note)
    return str(p.parent / "evidence" / p.name)


BACKLINK_START = "<!-- backlinks:start -->"
BACKLINK_END = "<!-- backlinks:end -->"


def _strip_backlinks(text: str) -> str:
    si, ei = text.find(BACKLINK_START), text.find(BACKLINK_END)
    if si != -1 and ei != -1 and ei > si:
        return text[:si] + text[ei + len(BACKLINK_END):]
    return text


def only_backlinks_changed(sha: str, path: str) -> bool:
    """True when a file's change is confined to its machine-generated
    `## Linked from` block. Every transform regenerates backlink blocks in
    the notes that link (or linked) to it — inherent link-maintenance churn,
    not an out-of-scope edit. Outside the markers the file must be
    byte-identical."""
    before, after = show(f"{sha}^", path), show(sha, path)
    if before is None or after is None:
        return False
    return _strip_backlinks(before) == _strip_backlinks(after)


def _plausible_id(tok: str) -> bool:
    """An 11-char English word ('temperature') is not a video id: require a
    digit/underscore/hyphen or mixed case, so prose in parens/backticks never
    trips cite conservation."""
    return bool(re.search(r"[0-9_-]", tok)
                or (tok != tok.lower() and tok != tok.upper()))


def cited_ids(text: str) -> set[str]:
    ids: set[str] = set()
    m = FM_SOURCES_RE.search(text)
    if m:
        for tok in m.group(1).replace("\n", " ").split(","):
            tok = tok.split("#", 1)[0].strip().strip("'\"")
            if re.fullmatch(r"[A-Za-z0-9_-]{11}", tok):
                ids.add(tok)
    ids.update(t for t in BACKTICK_ID_RE.findall(text) if _plausible_id(t))
    ids.update(t for t in PAREN_ID_RE.findall(text) if _plausible_id(t))
    return ids


def touched_paths(sha: str) -> list[tuple[int, int, str, list[str]]]:
    """(added, deleted, dest, all_sides) per numstat row of the commit."""
    out = git("show", "-m", "--first-parent", "--numstat", "--format=", sha)
    rows = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, deleted, path = parts
        sides = [s.strip() for s in
                 re.split(r"\s=>\s", path.replace("{", "").replace("}", ""))
                 if s.strip()]
        dest = sides[-1] if sides else path
        a = int(added) if added.isdigit() else 0
        d = int(deleted) if deleted.isdigit() else 0
        rows.append((a, d, dest, sides))
    return rows


def conservation_problems(sha: str, notes: list[str]) -> list[str]:
    """Cite + observation conservation over the named note set as a unit."""
    probs: list[str] = []
    pool = list(notes) + [evidence_path(n) for n in notes]
    before = {p: show(f"{sha}^", p) for p in pool}
    after = {p: show(sha, p) for p in pool}

    for n in notes:
        if before[n] is not None and after[n] is None:
            probs.append(f"note deleted: {n}")
    ev_deleted = [p for p in pool if p not in notes
                  and before[p] is not None and after[p] is None]
    for p in ev_deleted:
        probs.append(f"evidence file deleted: {p}")
    if probs:
        return probs

    before_ids = set().union(*(cited_ids(t) for t in before.values() if t)) \
        if any(before.values()) else set()
    after_ids = set().union(*(cited_ids(t) for t in after.values() if t)) \
        if any(after.values()) else set()
    lost = before_ids - after_ids
    if lost:
        probs.append(
            f"cite conservation: {len(lost)} source id(s) cited before are "
            f"gone from the note+evidence pair: {', '.join(sorted(lost)[:5])}"
            + (" …" if len(lost) > 5 else ""))

    obs_removed = ev_added = 0
    for n in notes:
        b = len(OBSERVED_RE.findall(before[n] or ""))
        a = len(OBSERVED_RE.findall(after[n] or ""))
        obs_removed += max(0, b - a)
    for n in notes:
        e = evidence_path(n)
        b = len(EVIDENCE_ENTRY_RE.findall(before[e] or ""))
        a = len(EVIDENCE_ENTRY_RE.findall(after[e] or ""))
        ev_added += max(0, a - b)
    if obs_removed > ev_added:
        probs.append(
            f"observation conservation: {obs_removed} **Observed** block(s) "
            f"removed but only {ev_added} evidence entrie(s) added")
    return probs


def cluster_members(key: str) -> list[str]:
    """Router + members of a cluster row, read from the worklist row's result
    cell (`members: a.md; b.md; …`) so scope follows what the builder wrote."""
    wl = ROOT / "sources" / "review-worklist.md"
    if not wl.exists():
        return []
    m = re.search(rf"^\| {re.escape(key)} \| [^|]+\| [^|]+\| [^|]*\| ([^|]*)\|$",
                  wl.read_text(encoding="utf-8"), re.M)
    if not m:
        return []
    stem = key.split(":", 1)[1]
    members = [f"species/{stem}.md"]
    cell = m.group(1)
    if "members:" in cell:
        for part in cell.split("members:", 1)[1].split(";"):
            part = part.strip().rstrip("…").strip()
            if part.endswith(".md"):
                members.append(part)
    return members


def violations(sha: str) -> list[str]:
    subj = git("log", "-1", "--format=%s", sha).strip()
    probs: list[str] = []

    if SUBJ_EXEMPT_RE.match(subj):
        named: list[str] = []
        scope_free = True
    elif (m := SUBJ_RELOCATE_RE.match(subj)):
        named = [m.group(1), m.group(2)]
        scope_free = False
    elif (m := SUBJ_CLUSTER_RE.match(subj)):
        named = cluster_members(m.group(1))
        if not named:
            return [f"cluster commit with no resolvable worklist row: {subj!r}"]
        scope_free = False
    elif (m := SUBJ_NOTE_RE.match(subj)):
        named = [m.group(1)]
        scope_free = False
    else:
        return [f"unparseable review commit subject: {subj!r}"]

    allowed = set(named) | {evidence_path(n) for n in named} | EXEMPT_LOGS

    for _a, _d, dest, sides in touched_paths(sha):
        for s in sides:
            if is_protected(s):
                # A note's outbound-link change regenerates `## Linked from`
                # blocks even inside protected paths (profiles/, skills/) —
                # machine churn, not an edit, as long as the file is
                # byte-identical outside the markers.
                if (s == dest and s.endswith(".md")
                        and only_backlinks_changed(sha, s)):
                    continue
                probs.append(f"protected path touched: {s}")
        if scope_free:
            if not (dest in EXEMPT_LOGS or os.path.basename(dest) == "README.md"):
                probs.append(f"checkpoint commit touched non-log path: {dest}")
            continue
        if dest in allowed or os.path.basename(dest) == "README.md":
            continue
        if dest.endswith(".md") and only_backlinks_changed(sha, dest):
            continue  # machine-generated backlink churn — see the helper
        probs.append(f"out of scope for {subj.split(' — ')[0]!r}: {dest}")

    if named and not probs:
        probs += conservation_problems(sha, named)
    return probs


def append_escalation(unit: str, etype: str, reason: str) -> None:
    esc = ROOT / "sources" / "escalations.md"
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    run = os.environ.get("GITHUB_RUN_ID", "local")
    with esc.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {ts} — {unit} — {etype}\n- run: {run}\n- reason: {reason}\n")


RESULT_MAX = 600


def _fit(s: str, limit: int = RESULT_MAX) -> str:
    s = s.strip()
    if len(s) <= limit:
        return s
    cut = s[: limit - 1]
    sp = cut.rfind(" ")
    if sp > limit * 0.6:
        cut = cut[:sp]
    return cut.rstrip(" ,;:-") + "…"


def set_row_status(note: str, status: str, result: str,
                   flags: str | None = None) -> bool:
    """Rewrite one review-worklist row (columns: note|tier|status|flags|result)."""
    log = ROOT / "sources" / "review-worklist.md"
    text = log.read_text(encoding="utf-8")
    pat = re.compile(
        rf"^\| {re.escape(note)} \| ([^|]+)\| ([^|]+)\| ([^|]*)\| ([^|]*)\|$",
        re.M)
    m = pat.search(text)
    if not m:
        return False
    clean = _fit(result.replace("|", "/").replace("\n", " "))
    fl = (flags if flags is not None else m.group(3).strip())
    new = f"| {note} | {m.group(1)}| {status} | {fl} | {clean} |"
    log.write_text(text[: m.start()] + new + text[m.end():], encoding="utf-8")
    return True


def unit_of(sha: str) -> str | None:
    subj = git("log", "-1", "--format=%s", sha).strip()
    m = (SUBJ_NOTE_RE.match(subj) or SUBJ_RELOCATE_RE.match(subj)
         or SUBJ_CLUSTER_RE.match(subj))
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
        if (TRAILER in body or s in reverted_targets
                or any(s.startswith(t) or t.startswith(s)
                       for t in reverted_targets)):
            continue
        if git("log", "-1", "--format=%ae", s).strip() not in PIPELINE_AUTHORS:
            continue  # supervised commit — not the sweep's business
        probs = violations(s)
        if not probs:
            continue
        print(f"SWEEP: reverting {s[:9]}: {probs[0]}")
        r = subprocess.run(["git", "revert", "--no-edit", s], cwd=ROOT,
                           capture_output=True, text=True)
        unit = unit_of(s) or "unknown"
        if r.returncode != 0:
            subprocess.run(["git", "revert", "--abort"], cwd=ROOT,
                           capture_output=True)
            append_escalation(unit, "guard-violation",
                              f"sweep found violation in {s} but revert "
                              f"conflicted — MANUAL ATTENTION: {probs[0]}")
            continue
        git("commit", "--amend", "-m",
            git("log", "-1", "--format=%B", "HEAD").strip() + f"\n\n{TRAILER} {s}")
        append_escalation(unit, "guard-violation",
                          f"sweep reverted {s}: " + "; ".join(probs))
        if unit != "unknown":
            set_row_status(unit, "reverted", f"reverted: guard: {probs[0]}")
        fixed += 1
    if fixed:
        subprocess.run(["python", "scripts/link-maintenance.py"], cwd=ROOT)
        git("add", "-A")
        if git("status", "--porcelain").strip():
            git("commit", "-m", "review: guard sweep fixups")
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
