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


# --- worklist status by tier -----------------------------------------------
# The fact-check phase selects rows whose status is `transformed`. A tier that
# produces cited prose but lands on `done` is skipped silently — never checked,
# never reported. Four geo rows needed hand-fixing during the geo phase before
# this was enforced.

def test_cited_prose_tiers_cannot_park_on_done(tmp_dir=None) -> None:
    import tempfile, shutil
    tmp = Path(tempfile.mkdtemp())
    try:
        (tmp / "sources").mkdir()
        (tmp / "sources" / "review-worklist.md").write_text(
            "| locations/a.md | geo | pending |  |  |\n"
            "| species/b.md | full | pending |  |  |\n"
            "| tackle/c.md | light | pending |  |  |\n"
            "| locations/d.md | gazetteer | pending |  |  |\n")
        real_root = guard.ROOT
        guard.ROOT = tmp
        try:
            for note in ("locations/a.md", "species/b.md",
                         "tackle/c.md", "locations/d.md"):
                guard.set_row_status(note, "done", "x")
        finally:
            guard.ROOT = real_root
        out = (tmp / "sources" / "review-worklist.md").read_text()
        check("a geo row is coerced to transformed",
              "| locations/a.md | geo | transformed |" in out, True)
        check("a full row is coerced too",
              "| species/b.md | full | transformed |" in out, True)
        check("a light row legitimately stays done",
              "| tackle/c.md | light | done |" in out, True)
        check("a mechanical gazetteer row stays done",
              "| locations/d.md | gazetteer | done |" in out, True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- per-tier model selection ----------------------------------------------
# The workflow sets --model once per run, so a chunk that mixed tiers would
# silently run some units on the wrong model — Sonnet on a species router, or
# Opus on the light tail Cameron deliberately moved off it. Neither shows up
# in the output: the note still gets written, just by the wrong model.

def test_chunks_never_mix_models() -> None:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "next_note", ROOT / "scripts" / "review" / "next-note.py")
    nn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nn)

    check("the species routers stay on Opus",
          nn.MODEL_BY_TIER["full"], "claude-opus-5")
    check("the ladder stays on Opus",
          nn.MODEL_BY_TIER["geo"], "claude-opus-5")
    check("the formulaic tail moves to Sonnet",
          (nn.MODEL_BY_TIER["standard"], nn.MODEL_BY_TIER["light"]),
          ("claude-sonnet-5", "claude-sonnet-5"))

    rows = [{"note": f"n{i}.md", "tier": t} for i, t in
            enumerate(["full", "full", "standard", "light", "standard", "full"])]

    def chunk(rs, budget=16):
        out, spent, model = [], 0, nn.model_of(rs[0], "transform")
        for r in rs:
            if nn.model_of(r, "transform") != model and out:
                break
            c = nn.COST[r["tier"]]
            if spent + c > budget and out:
                break
            out.append(r)
            spent += c
        return out, model

    seen, remaining = [], rows[:]
    while remaining:
        c, model = chunk(remaining)
        check(f"chunk of {[r['tier'] for r in c]} is model-homogeneous",
              {nn.model_of(r, "transform") for r in c}, {model})
        seen.append((tuple(r["tier"] for r in c), model))
        remaining = remaining[len(c):]

    check("every unit is still emitted, none dropped at a boundary",
          sum(len(t) for t, _m in seen), len(rows))
    check("a full-tier unit stranded after the Sonnet tail still gets Opus",
          seen[-1], (("full",), "claude-opus-5"))


NOTE_CAMERON = """---
type: conditions
sources: [S2L3KLSQ6Is, cameron]
---

# Sea state

- **Catalina Eddy shielding.** The eddy shields everything east of Catalina
  and San Clemente; the 425 is often shielded despite sitting far south of
  it (`S2L3KLSQ6Is`, cameron).
"""

# Same note with Cameron's adjudication reworded back toward the corpus and
# the attribution dropped. The video id survives, so the {11}-only matcher
# saw nothing missing.
NOTE_CAMERON_STRIPPED = """---
type: conditions
sources: [S2L3KLSQ6Is]
---

# Sea state

- **Catalina Eddy shielding.** The eddy can shield the inner SD banks while
  it blows outside (`S2L3KLSQ6Is`).
"""


def test_dropping_a_cameron_attribution_trips_conservation() -> None:
    """CLAUDE.md: a cite is "`cameron` or the YouTube video_id". Matching only
    the 11-char id half left every cameron-attributed claim unprotected."""
    def body(repo: Path) -> None:
        note = repo / "conditions" / "sea-state.md"
        note.parent.mkdir(exist_ok=True)
        note.write_text(NOTE_CAMERON)
        commit(repo, "seed sea-state")
        note.write_text(NOTE_CAMERON_STRIPPED)
        sha = commit(repo, "review: conditions/sea-state.md — standard")
        probs = guard.conservation_problems(sha, ["conditions/sea-state.md"])
        check("dropping (cameron) is a conservation violation",
              any("cite conservation" in p for p in probs), True)
    with_repo(body)


def test_keeping_the_cameron_attribution_passes() -> None:
    """The rule must not fire on a legitimate rewrite that keeps the cite."""
    def body(repo: Path) -> None:
        note = repo / "conditions" / "sea-state.md"
        note.parent.mkdir(exist_ok=True)
        note.write_text(NOTE_CAMERON)
        commit(repo, "seed sea-state")
        note.write_text(NOTE_CAMERON.replace(
            "The eddy shields", "The eddy reliably shields"))
        sha = commit(repo, "review: conditions/sea-state.md — standard")
        check("a reword that keeps (cameron) is clean",
              guard.conservation_problems(sha, ["conditions/sea-state.md"]), [])
    with_repo(body)


def test_prose_that_looks_like_a_video_id_is_not_conserved() -> None:
    """`speed-troll` and `Baja-scoped` are 11 chars with a hyphen. Counting
    them as cites made conservation demand a worker preserve ordinary prose,
    which reverts the unit and costs its work."""
    def body(repo: Path) -> None:
        (repo / "sources" / "transcripts").mkdir(parents=True)
        (repo / "sources" / "transcripts" / "_manifest.csv").write_text(
            "video_id,title,status,caption_type,failure_reason,channel,upload_date\n"
            "S2L3KLSQ6Is,A real video,ok,auto-generated,,BDOutdoors,2024-01-01\n")
        note = repo / "lures" / "mad-mac.md"
        note.parent.mkdir(exist_ok=True)
        note.write_text("# Mad Mac\n\nRun it as a (speed-troll) lure.\n")
        commit(repo, "seed mad-mac")
        note.write_text("# Mad Mac\n\nRun it fast, on the troll.\n")
        sha = commit(repo, "review: lures/mad-mac.md — standard")
        check("rewording (speed-troll) is not a cite loss",
              guard.conservation_problems(sha, ["lures/mad-mac.md"]), [])
    with_repo(body)


ADJ_NOTE = """---
type: conditions
sources: [S2L3KLSQ6Is, cameron]
---

# Sea state

- **Catalina Eddy shielding — east of Catalina and San Clemente.**
  ⚠ adjudicated (Cameron, 2026-08-26).
  The prevailing wind outside SoCal comes from the north, so the islands
  shadow the water behind them; the 425 is shielded despite sitting well
  south of San Clemente (`S2L3KLSQ6Is`, cameron).
"""


def test_dropping_an_adjudicated_marker_trips_conservation() -> None:
    """Rule 3a is an instruction to a Sonnet worker; this makes it enforced.

    Conservation protects the `cameron` cite token, not the wording — a
    rewrite can keep the citation, drop the marker, and re-flag the passage
    as an ordinary fact-check. Nothing caught that before.
    """
    def body(repo: Path) -> None:
        note = repo / "conditions" / "sea-state.md"
        note.parent.mkdir(exist_ok=True)
        note.write_text(ADJ_NOTE)
        commit(repo, "seed sea-state")
        note.write_text(ADJ_NOTE.replace(
            "  ⚠ adjudicated (Cameron, 2026-08-26).\n", ""))
        sha = commit(repo, "review: conditions/sea-state.md — standard")
        probs = guard.conservation_problems(sha, ["conditions/sea-state.md"])
        check("dropping the marker is a conservation violation",
              any("adjudication conservation" in p for p in probs), True)
    with_repo(body)


def test_reflowing_an_adjudicated_passage_is_allowed() -> None:
    """The marker is conserved; the prose around it may legitimately change."""
    def body(repo: Path) -> None:
        note = repo / "conditions" / "sea-state.md"
        note.parent.mkdir(exist_ok=True)
        note.write_text(ADJ_NOTE)
        commit(repo, "seed sea-state")
        note.write_text(ADJ_NOTE
                        .replace("The prevailing wind outside SoCal comes",
                                 "Outside SoCal the prevailing wind comes")
                        .replace("shadow the water behind them;",
                                 "shadow the water behind them, and"))
        sha = commit(repo, "review: conditions/sea-state.md — standard")
        check("a reword that keeps the marker is clean",
              guard.conservation_problems(sha, ["conditions/sea-state.md"]), [])
    with_repo(body)


def test_moving_a_marker_within_the_note_is_allowed() -> None:
    """It is a count, not a position — restructuring a note must not trip it."""
    def body(repo: Path) -> None:
        note = repo / "conditions" / "sea-state.md"
        note.parent.mkdir(exist_ok=True)
        note.write_text(ADJ_NOTE)
        commit(repo, "seed sea-state")
        moved = (ADJ_NOTE.replace("  ⚠ adjudicated (Cameron, 2026-08-26).\n", "")
                 .rstrip() + "\n\n⚠ adjudicated (Cameron, 2026-08-26).\n")
        note.write_text(moved)
        sha = commit(repo, "review: conditions/sea-state.md — standard")
        check("relocating the marker in the same note is clean",
              guard.conservation_problems(sha, ["conditions/sea-state.md"]), [])
    with_repo(body)


def main() -> int:
    for fn in (test_geo_unit_may_regenerate_its_parents_child_list,
               test_geo_unit_may_not_edit_its_parents_prose,
               test_checkpoint_may_create_mechanical_pages,
               test_checkpoint_may_not_rewrite_an_existing_note,
               test_phase_word_strips_a_subject_passed_as_the_message,
               test_cited_prose_tiers_cannot_park_on_done,
               test_chunks_never_mix_models,
               test_dropping_a_cameron_attribution_trips_conservation,
               test_keeping_the_cameron_attribution_passes,
               test_prose_that_looks_like_a_video_id_is_not_conserved,
               test_dropping_an_adjudicated_marker_trips_conservation,
               test_reflowing_an_adjudicated_passage_is_allowed,
               test_moving_a_marker_within_the_note_is_allowed):
        fn()
    if failures:
        print(f"FAILED ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("guard scope tests: 13 check groups OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
