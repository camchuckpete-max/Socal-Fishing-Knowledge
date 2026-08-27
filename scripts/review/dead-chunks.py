#!/usr/bin/env python3
"""dead-chunks.py — how many chunks in a row produced nothing.

Prints the number of consecutive `review: progress checkpoint` commits at
HEAD. Real work breaks the streak, so a long one means the fleet is running
but nothing is coming out — in practice the subscription limit, where the
agent dies on its first API call and the chunk still writes a checkpoint.
review-trampoline.yml uses the count to back off instead of bouncing every
two hours into a wall.

WHY THIS IS A SCRIPT AND NOT A SHELL PIPELINE (2026-08-27): it used to be

    dead=$(git log --format='%s' -60 \
           | awk '/^review: progress checkpoint$/{n++; next} {exit} END{...}')

inside a `set -euo pipefail` step. With a non-checkpoint commit at the tip —
i.e. exactly when the fleet HAS been producing work — awk hits `{exit}` on
the first line and closes the pipe while git log is still writing. On the
runner's cold shallow clone that races into SIGPIPE, git log exits 141,
pipefail propagates it, and set -e kills the step before it can dispatch
anything. The trampoline died silently for 9 hours. No pipe, no race.

This is an optimisation, never a gate: any failure prints 0 (meaning "no
backoff, go ahead and bounce") and exits 0. It must never be the reason a
bounce does not happen.

Usage: dead-chunks.py [-n N]     # N commits to look back over (default 60)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

CHECKPOINT = "review: progress checkpoint"


def subjects(limit: int, cwd: Path | str | None = None) -> list[str]:
    """Commit subjects newest-first, or [] if git cannot answer.

    Runs in `cwd` (the process working directory by default) rather than a
    path derived from this file, so it reads the repository it is invoked
    in — the way git itself does. The trampoline runs it from the checked-out
    branch root; the tests point it at a throwaway repo.
    """
    try:
        r = subprocess.run(
            ["git", "log", "--format=%s", f"-{limit}"],
            cwd=cwd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return []
    if r.returncode != 0:
        return []
    return r.stdout.splitlines()


def dead_chunks(limit: int = 60, cwd: Path | str | None = None) -> int:
    n = 0
    for subject in subjects(limit, cwd):
        if subject.strip() != CHECKPOINT:
            break
        n += 1
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=60,
                    help="commits to look back over (default 60)")
    args = ap.parse_args()
    try:
        print(dead_chunks(args.n))
    except Exception:            # never block a bounce
        print(0)
    return 0


if __name__ == "__main__":
    sys.exit(main())
