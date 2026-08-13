#!/usr/bin/env python3
"""The ONLY sanctioned commit path for the batch-2 unattended pipeline.

Per video: rewrite the worklist row mechanically, optionally append an
escalation, gate on link-maintenance, commit everything as ONE commit,
run the mechanical guard (revert on violation), push with rebase-retry.

Exit codes:
  0  committed + pushed
  2  link-maintenance failed (video escalated; minimal commit pushed) —
     or pre-existing breakage (nothing committed; printed loudly)
  3  guard violation (commit reverted, escalation pushed)
  4  push failed after retries (orchestrator must STOP the chunk)
  5  worklist row not found / ambiguous (nothing committed)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402  (same directory)

BRANCH = "claude/batch2-ingestion-rb0v4i"


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
        print(f"push attempt {i + 1} failed: {r.stderr.strip()}", file=sys.stderr)
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video-id", required=True)
    ap.add_argument("--status", required=True,
                    choices=["done", "skipped", "escalated"])
    ap.add_argument("--result", required=True)
    ap.add_argument("--message", default="")
    ap.add_argument("--escalation", default=None,
                    help="'<video_id> | <type> | <reason>' to append to escalations.md")
    args = ap.parse_args()
    vid = args.video_id

    if not guard.set_row_status(vid, args.status, args.result):
        print(f"FATAL: worklist row for {vid} not found — nothing committed",
              file=sys.stderr)
        return 5

    if args.escalation:
        parts = [p.strip() for p in args.escalation.split("|", 2)]
        while len(parts) < 3:
            parts.append("")
        guard.append_escalation(parts[0] or vid, parts[1] or "evaluator-escalate",
                                parts[2])

    if not run_link_maintenance():
        # discard this video's tree changes; escalate the row minimally
        reset_tree()
        guard.set_row_status(vid, "escalated", "escalated: link-maintenance failed")
        guard.append_escalation(vid, "link-maintenance-failed",
                                "link-maintenance exited nonzero on this video's patch; "
                                "tree reset, extraction discarded")
        if not run_link_maintenance():
            print("FATAL: link-maintenance fails even on the minimal row edit — "
                  "breakage predates this video; NOT committing. Manual attention "
                  "needed on the branch.", file=sys.stderr)
            reset_tree()
            return 2
        commit(f"batch2: {vid} — escalated (link-maintenance failed)")
        return 2 if push() else 4

    sha = commit(f"batch2: {vid} — {args.message or args.status}")

    if guard.cmd_check(sha) != 0:
        probs = guard.violations(sha)
        sh("git", "revert", "--no-edit", sha)
        body = sh("git", "log", "-1", "--format=%B", "HEAD").stdout.strip()
        sh("git", "commit", "--amend", "-m", body + f"\n\n{guard.TRAILER} {sha}")
        guard.set_row_status(vid, "escalated", f"escalated: guard: {probs[0]}")
        guard.append_escalation(vid, "guard-violation",
                                f"commit {sha} reverted: " + "; ".join(probs))
        run_link_maintenance()
        commit(f"batch2: {vid} — guard escalation")
        push()
        return 3

    return 0 if push() else 4


if __name__ == "__main__":
    sys.exit(main())
