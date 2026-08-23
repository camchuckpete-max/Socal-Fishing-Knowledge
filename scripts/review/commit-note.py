#!/usr/bin/env python3
"""The ONLY sanctioned commit path for the unattended editorial-review fleet.

Per unit: rewrite the worklist (or relocation-queue) row mechanically,
optionally append an escalation, gate on check-note + link-maintenance,
commit everything as ONE commit, run the mechanical guard (revert on
violation), push with rebase-retry. Clone of scripts/batch2/commit-video.py
with the review's row schema and guard.

Modes:
  --note <path>                    ordinary unit (transform/factcheck/
                                   gazetteer/cluster) — updates the worklist
  --relocate-src X --relocate-dst Y  relocation unit — updates the
                                   relocation-queue row for X

Exit codes (unchanged contract):
  0  committed + pushed
  2  link-maintenance failed (unit escalated; minimal commit pushed) —
     or pre-existing breakage (nothing committed; printed loudly)
  3  guard violation (commit reverted, escalation pushed)
  4  push failed after retries (orchestrator must STOP the chunk)
  5  row not found / ambiguous (nothing committed)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402  (same directory)


def _current_branch() -> str:
    r = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                       cwd=ROOT, capture_output=True, text=True, check=True)
    return r.stdout.strip()


BRANCH = _current_branch()


def sh(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    r = subprocess.run(list(args), cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"FATAL: {' '.join(args)}: {r.stderr.strip()}", file=sys.stderr)
        sys.exit(5)
    return r


def reset_tree() -> None:
    sh("git", "checkout", "--", ".")
    sh("git", "clean", "-fd")


def run_link_maintenance() -> bool:
    r = subprocess.run(["python", "scripts/link-maintenance.py"], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout + r.stderr, file=sys.stderr)
    return r.returncode == 0


def run_check_note(note: str) -> tuple[bool, str]:
    r = subprocess.run(["python", "scripts/review/check-note.py", note],
                       cwd=ROOT, capture_output=True, text=True)
    return r.returncode == 0, (r.stdout + r.stderr).strip()


def commit(msg: str) -> str:
    sh("git", "add", "-A")
    sh("git", "commit", "-m", msg)
    return sh("git", "rev-parse", "HEAD").stdout.strip()


def push() -> bool:
    for i, delay in enumerate((0, 10, 30, 90)):
        if delay:
            time.sleep(delay)
            subprocess.run(["git", "pull", "--rebase", "origin", BRANCH],
                           cwd=ROOT, capture_output=True, text=True)
        r = subprocess.run(["git", "push", "origin", f"HEAD:{BRANCH}"],
                           cwd=ROOT, capture_output=True, text=True)
        if r.returncode == 0:
            return True
        print(f"push attempt {i + 1} failed: {r.stderr.strip()}",
              file=sys.stderr)
    return False


def set_relocation_status(src: str, status: str) -> bool:
    path = ROOT / "sources" / "relocation-queue.md"
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    pat = re.compile(
        rf"^(\| {re.escape(src)} \| [^|]+\| [^|]+\| [^|]+\| [^|]+\|) ([^|]+)\|$",
        re.M)
    m = pat.search(text)
    if not m:
        return False
    path.write_text(text[: m.start()] + f"{m.group(1)} {status} |"
                    + text[m.end():], encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--note", default=None)
    ap.add_argument("--relocate-src", default=None)
    ap.add_argument("--relocate-dst", default=None)
    ap.add_argument("--status", required=True,
                    choices=["transformed", "fact-checked", "done", "skipped",
                             "escalated"])
    ap.add_argument("--result", required=True)
    ap.add_argument("--flags", default=None,
                    help="worklist flags cell (e.g. 'gaps:3 fc:2 reloc:1')")
    ap.add_argument("--message", default="")
    ap.add_argument("--escalation", default=None,
                    help="'<unit> | <type> | <reason>' for escalations.md")
    args = ap.parse_args()

    relocate = args.relocate_src is not None
    if relocate == (args.note is not None):
        print("FATAL: pass exactly one of --note or --relocate-src/--relocate-dst",
              file=sys.stderr)
        return 5
    if relocate and not args.relocate_dst:
        print("FATAL: --relocate-src needs --relocate-dst", file=sys.stderr)
        return 5

    unit = args.note or args.relocate_src
    if relocate:
        if not set_relocation_status(args.relocate_src,
                                     args.status if args.status != "transformed"
                                     else "done"):
            print(f"FATAL: relocation row for {args.relocate_src} not found",
                  file=sys.stderr)
            return 5
        subject = f"review: relocate {args.relocate_src} → {args.relocate_dst}"
        check_targets = [args.relocate_src, args.relocate_dst]
    else:
        if not guard.set_row_status(unit, args.status, args.result, args.flags):
            print(f"FATAL: worklist row for {unit} not found — nothing "
                  f"committed", file=sys.stderr)
            return 5
        subject = f"review: {unit} — {args.message or args.status}"
        check_targets = [unit]

    if args.escalation:
        parts = [p.strip() for p in args.escalation.split("|", 2)]
        while len(parts) < 3:
            parts.append("")
        guard.append_escalation(parts[0] or unit,
                                parts[1] or "verify-escalate", parts[2])

    # Machine acceptance BEFORE the tree-wide gate — but only when the unit
    # produced/kept a real note edit (a skip/escalate row-only commit has
    # nothing to check).
    if args.status in ("transformed", "fact-checked", "done"):
        for tgt in check_targets:
            if not (ROOT / tgt).exists():
                continue
            ok, report = run_check_note(tgt)
            if not ok:
                print(report, file=sys.stderr)
                reset_tree()
                if relocate:
                    set_relocation_status(args.relocate_src, "escalated")
                else:
                    guard.set_row_status(unit, "escalated",
                                         "escalated: check-note failed")
                guard.append_escalation(unit, "check-note-failed",
                                        report.splitlines()[0] if report
                                        else "check-note failed")
                run_link_maintenance()
                commit(f"review: {unit} — escalated (check-note failed)")
                return 2 if push() else 4

    if not run_link_maintenance():
        reset_tree()
        if relocate:
            set_relocation_status(args.relocate_src, "escalated")
        else:
            guard.set_row_status(unit, "escalated",
                                 "escalated: link-maintenance failed")
        guard.append_escalation(unit, "link-maintenance-failed",
                                "link-maintenance exited nonzero on this "
                                "unit's patch; tree reset, edit discarded")
        if not run_link_maintenance():
            print("FATAL: link-maintenance fails even on the minimal row edit "
                  "— breakage predates this unit; NOT committing. Manual "
                  "attention needed on the branch.", file=sys.stderr)
            reset_tree()
            return 2
        commit(f"review: {unit} — escalated (link-maintenance failed)")
        return 2 if push() else 4

    sha = commit(subject)

    if guard.cmd_check(sha) != 0:
        probs = guard.violations(sha)
        sh("git", "revert", "--no-edit", sha)
        body = sh("git", "log", "-1", "--format=%B", "HEAD").stdout.strip()
        sh("git", "commit", "--amend", "-m", body + f"\n\n{guard.TRAILER} {sha}")
        if relocate:
            set_relocation_status(args.relocate_src, "escalated")
        else:
            guard.set_row_status(unit, "escalated",
                                 f"escalated: guard: {probs[0]}")
        guard.append_escalation(unit, "guard-violation",
                                f"commit {sha} reverted: " + "; ".join(probs))
        run_link_maintenance()
        commit(f"review: {unit} — escalated (guard violation)")
        push()
        return 3

    return 0 if push() else 4


if __name__ == "__main__":
    sys.exit(main())
