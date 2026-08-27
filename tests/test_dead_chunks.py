#!/usr/bin/env python3
"""Tests for scripts/review/dead-chunks.py and the trampoline snippet.

This file exists because of a real 9-hour outage on 2026-08-27. The
dead-fleet backoff in review-trampoline.yml was a shell pipeline:

    dead=$(git log --format='%s' -60 \
           | awk '/^review: progress checkpoint$/{n++; next} {exit} END{...}')

run under `set -euo pipefail`. When the branch tip is NOT a checkpoint
commit, awk exits on the first line and closes the pipe while git log is
still writing; on a cold shallow clone that races into SIGPIPE, git log
exits 141, pipefail propagates, and set -e kills the step BEFORE it
dispatches. The trampoline had been fine for 31 runs only because the tip
was always a checkpoint commit, so awk read to the end.

The bug was invisible to every existing test and did not reproduce on a
warm full clone. test_a_normal_tip_does_not_kill_the_step is the check
that was missing: it runs the real snippet under the real shell flags
against the exact repo shape that broke it.
"""
from __future__ import annotations

import contextlib
import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "review" / "dead-chunks.py"
spec = importlib.util.spec_from_file_location("dc", SCRIPT)
dc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dc)

CHECKPOINT = "review: progress checkpoint"
failures: list[str] = []


def check(label: str, got, want) -> None:
    if got != want:
        failures.append(f"{label}: got {got!r}, want {want!r}")


def run(*args: str, cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def repo_with(stack, subjects: list[str]) -> Path:
    """A repo whose commit subjects are `subjects`, oldest first."""
    repo = Path(stack.enter_context(tempfile.TemporaryDirectory()))
    run("git", "init", "-q", cwd=repo)
    run("git", "config", "user.email", "kb@example.com", cwd=repo)
    run("git", "config", "user.name", "kb-review[bot]", cwd=repo)
    for i, subject in enumerate(subjects):
        (repo / f"f{i}.md").write_text(f"{i}\n")
        run("git", "add", "-A", cwd=repo)
        run("git", "commit", "-q", "-m", subject, cwd=repo)
    return repo


def count_in(repo: Path) -> int:
    return dc.dead_chunks(cwd=repo)


# The snippet as the workflow actually runs it, with the shell flags the
# workflow actually sets.
SNIPPET = (
    "set -euo pipefail\n"
    f'dead=$(python {SCRIPT}) || dead=0\n'
    'echo "dead=$dead"\n'
)


def test_a_normal_tip_does_not_kill_the_step() -> None:
    """THE regression: a non-checkpoint tip must not abort the bounce."""
    with contextlib.ExitStack() as stack:
        repo = repo_with(stack, [CHECKPOINT] * 5 + ["review: locations/x.md — geo"])
        r = subprocess.run(["bash", "-c", SNIPPET], cwd=repo,
                           capture_output=True, text=True)
        check("step exits 0 with a normal commit at the tip", r.returncode, 0)
        check("and reports no dead chunks", r.stdout.strip(), "dead=0")


def test_a_checkpoint_tip_still_counts_the_streak() -> None:
    with contextlib.ExitStack() as stack:
        repo = repo_with(stack, ["review: species/a.md — full"] + [CHECKPOINT] * 3)
        r = subprocess.run(["bash", "-c", SNIPPET], cwd=repo,
                           capture_output=True, text=True)
        check("step exits 0 with a checkpoint tip", r.returncode, 0)
        check("counts the streak", r.stdout.strip(), "dead=3")


def test_counts_only_the_streak_at_head() -> None:
    """Checkpoints below a real commit are history, not a stall."""
    with contextlib.ExitStack() as stack:
        repo = repo_with(stack, [CHECKPOINT] * 9
                         + ["review: species/a.md — full"] + [CHECKPOINT] * 2)
        check("streak stops at the first real commit", count_in(repo), 2)


def test_empty_and_broken_repos_report_zero() -> None:
    """Never block a bounce: no git, no answer -> 0, not a crash."""
    with contextlib.ExitStack() as stack:
        empty = repo_with(stack, [])
        check("a repo with no commits", count_in(empty), 0)
        notrepo = Path(stack.enter_context(tempfile.TemporaryDirectory()))
        check("a directory that is not a repo", count_in(notrepo), 0)


def test_every_commit_a_checkpoint() -> None:
    with contextlib.ExitStack() as stack:
        repo = repo_with(stack, [CHECKPOINT] * 4)
        check("all-checkpoint history", count_in(repo), 4)


def main() -> int:
    for fn in (test_a_normal_tip_does_not_kill_the_step,
               test_a_checkpoint_tip_still_counts_the_streak,
               test_counts_only_the_streak_at_head,
               test_empty_and_broken_repos_report_zero,
               test_every_commit_a_checkpoint):
        fn()
    if failures:
        print(f"FAILED ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("dead-chunks tests: 5 check groups OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
