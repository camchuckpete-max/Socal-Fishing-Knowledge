#!/usr/bin/env python3
"""Scope-rule tests for scripts/review/guard.py.

Both cases below are real regressions that reached the branch. Each would
have cost the whole geographic phase, and neither is visible without running
a commit through the guard — the fleet just quietly loses work.

  1. A geo page links itself into its parent by setting `parent:`, and
     link-maintenance then rewrites the PARENT's generated child list. The
     scope rule stripped only the backlinks block before comparing, so the
     parent read as an out-of-scope edit and every zone under a region would
     have been reverted.

  2. The checkpoint step runs build-spot-pages.py, which CREATES the
     mechanical minimum spot pages. Checkpoint scope allowed only logs and
     README files, so the first checkpoint after a zone landed would have
     been reverted whole — undoing the mechanical gazetteer and rolling the
     worklist back with it.

Each test builds a throwaway git repo, makes the commit the fleet would make,
and asserts what the guard says about it.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "guard", ROOT / "scripts" / "review" / "guard.py")
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)

failures: list[str] = []


def check(label: str, got, want) -> None:
    if got != want:
        failures.append(f"{label}: got {got!r}, want {want!r}")


def run(*args: str, cwd: Path) -> None:
    subprocess.run(args, cwd=cwd, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


AUTHOR = "41898282+claude[bot]@users.noreply.github.com"

ZONE = """---
type: zone
parent: region.md
---

# Zone

## Spots

Curated prose.

<!-- children:start -->
<!-- children:end -->
"""

REGION = """---
type: region
---

# Region

## Zones

Character prose.

<!-- children:start -->
{}<!-- children:end -->
"""


def commit(repo: Path, subject: str) -> str:
    run("git", "add", "-A", cwd=repo)
    env = dict(os.environ, GIT_AUTHOR_EMAIL=AUTHOR, GIT_COMMITTER_EMAIL=AUTHOR,
               GIT_AUTHOR_NAME="kb-review[bot]",
               GIT_COMMITTER_NAME="kb-review[bot]")
    subprocess.run(["git", "commit", "-q", "-m", subject], cwd=repo, check=True,
                   env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, check=True,
                          capture_output=True, text=True).stdout.strip()


def new_repo(stack) -> Path:
    repo = Path(stack.enter_context(tempfile.TemporaryDirectory()))
    run("git", "init", "-q", cwd=repo)
    run("git", "config", "user.email", AUTHOR, cwd=repo)
    run("git", "config", "user.name", "kb-review[bot]", cwd=repo)
    (repo / "locations").mkdir()
    (repo / "sources").mkdir()
    (repo / "locations" / "region.md").write_text(REGION.format(""))
    (repo / "sources" / "review-worklist.md").write_text("| x |\n")
    commit(repo, "seed")
    return repo


def with_repo(fn):
    """Run fn against a fresh repo with guard pointed at it."""
    import contextlib
    with contextlib.ExitStack() as stack:
        repo = new_repo(stack)
        # guard runs every git call with cwd=ROOT; point it at the fixture.
        real_root = guard.ROOT
        guard.ROOT = repo
        try:
            fn(repo)
        finally:
            guard.ROOT = real_root


def test_geo_unit_may_regenerate_its_parents_child_list() -> None:
    def body(repo: Path) -> None:
        (repo / "locations" / "newzone.md").write_text(ZONE)
        # what link-maintenance does in the same breath:
        (repo / "locations" / "region.md").write_text(
            REGION.format("- [Zone](newzone.md)\n"))
        (repo / "sources" / "review-worklist.md").write_text("| y |\n")
        sha = commit(repo, "review: locations/newzone.md — geo")
        check("a geo unit regenerating its parent's child list is in scope",
              guard.violations(sha), [])
    with_repo(body)


def test_geo_unit_may_not_edit_its_parents_prose() -> None:
    def body(repo: Path) -> None:
        (repo / "locations" / "newzone.md").write_text(ZONE)
        (repo / "locations" / "region.md").write_text(
            REGION.format("- [Zone](newzone.md)\n")
            .replace("Character prose.", "Rewritten by the worker."))
        sha = commit(repo, "review: locations/newzone.md — geo")
        probs = " ".join(guard.violations(sha))
        check("a geo unit editing its parent's PROSE is still out of scope",
              "out of scope" in probs, True)
    with_repo(body)


def test_checkpoint_may_create_mechanical_pages() -> None:
    def body(repo: Path) -> None:
        (repo / "locations" / "probe-spot.md").write_text(
            "---\ntype: location\nparent: region.md\n---\n\n# Probe Spot\n")
        (repo / "sources" / "review-worklist.md").write_text("| z |\n")
        sha = commit(repo, "review: progress checkpoint")
        check("a checkpoint creating a mechanical spot page is allowed",
              guard.violations(sha), [])
    with_repo(body)


def test_checkpoint_may_not_rewrite_an_existing_note() -> None:
    def body(repo: Path) -> None:
        (repo / "locations" / "region.md").write_text(
            REGION.format("").replace("Character prose.", "Overwritten."))
        sha = commit(repo, "review: progress checkpoint")
        probs = " ".join(guard.violations(sha))
        check("a checkpoint rewriting an existing note is still a violation",
              "non-log path" in probs, True)
    with_repo(body)


# --- the commit wrapper's subject line -------------------------------------
# The subject is `review: <unit> — <phase>` and the guard's scope rule parses
# the unit out of it, so the shape matters. An orchestrator that passes the
# whole subject as --message instead of a bare phase word produced
# `review: <unit> — review: <unit> — geo` in the history Cameron reads at the
# gate. Policing exact string discipline through a prompt across hundreds of
# units is not reliable; normalising here is.

def test_phase_word_strips_a_subject_passed_as_the_message() -> None:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "commit_note", ROOT / "scripts" / "review" / "commit-note.py")
    cn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cn)
    check("a bare phase word is left alone", cn.phase_word("geo"), "geo")
    check("a full subject collapses to its phase",
          cn.phase_word("review: locations/a.md — geo"), "geo")
    check("a doubled subject collapses too",
          cn.phase_word("review: locations/a.md — review: locations/a.md — geo"),
          "geo")
    check("an escalation reason survives intact",
          cn.phase_word("escalated (guard violation)"),
          "escalated (guard violation)")
    check("empty stays empty so --status is used", cn.phase_word(""), "")


def main() -> int:
    for fn in (test_geo_unit_may_regenerate_its_parents_child_list,
               test_geo_unit_may_not_edit_its_parents_prose,
               test_checkpoint_may_create_mechanical_pages,
               test_checkpoint_may_not_rewrite_an_existing_note,
               test_phase_word_strips_a_subject_passed_as_the_message):
        fn()
    if failures:
        print(f"FAILED ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("guard scope tests: 5 check groups OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
