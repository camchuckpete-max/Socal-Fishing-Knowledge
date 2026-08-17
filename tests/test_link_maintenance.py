#!/usr/bin/env python3
"""Unit tests for scripts/link-maintenance.py.

Run: python tests/test_link_maintenance.py   (exit 0 = pass)

Covers the two defects found in the batch-3 Phase 1 audit, both of which had
silently corrupted the KB for the whole of batch 2:

  1. summary_of() skipped any line starting with a bare "*", so a
     "**Bold lead:** ..." opening line was dropped from the generated index.
     That erased the region line from species/cabrilla.md's index entry — the
     KB's only machine-visible region marker — along with all nine seasonal
     regime labels and a flagged-stub warning.

  2. parse_links() did not strip the generated "## Linked from" block, so
     every backlink was re-parsed as an outbound link and bred a reciprocal
     one. 32% of the backlink graph was phantom, and the writes into
     guard-protected paths reverted four clean extractions.
"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "lm", ROOT / "scripts" / "link-maintenance.py")
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)

failures: list[str] = []


def check(label: str, got, want) -> None:
    if got != want:
        failures.append(f"{label}\n     got:  {got!r}\n     want: {want!r}")


def write(tmp: Path, name: str, body: str) -> Path:
    p = tmp / name
    p.write_text(body, encoding="utf-8")
    return p


FM = "---\ntype: species\ntags: [x]\nsources: [cameron]\nconfidence: high\n---\n\n"


def test_summary_keeps_bold_lead(tmp: Path) -> None:
    p = write(tmp, "bold.md", FM + (
        "# Cabrilla\n\n"
        "**Region: Baja — Sea of Cortez.** Cabrilla are a structure-ambush\n"
        "fish that sit tight to rock.\n"))
    got = lm.summary_of(p)
    check("bold lead line survives into the summary",
          got.startswith("Region: Baja"), True)


def test_summary_still_skips_real_bullets(tmp: Path) -> None:
    p = write(tmp, "bullets.md", FM + (
        "# Note\n\n"
        "- a bullet that is not the summary\n"
        "* another bullet\n\n"
        "The real opening paragraph starts here.\n"))
    check("'- ' and '* ' bullets are still skipped",
          lm.summary_of(p), "The real opening paragraph starts here.")


def test_summary_skips_thematic_break(tmp: Path) -> None:
    p = write(tmp, "rule.md", FM + "# Note\n\n---\n\nReal text after a rule.\n")
    check("a lone thematic break is skipped",
          lm.summary_of(p), "Real text after a rule.")


def test_backlink_block_stripped(tmp: Path) -> None:
    p = write(tmp, "note.md", FM + (
        "# Note\n\n"
        "A real outbound link to [gear classes](../tackle/gear-classes.md).\n\n"
        f"{lm.BACKLINK_START}\n"
        "## Linked from\n\n"
        "- [Some Router](../species/yellowtail.md)\n"
        f"{lm.BACKLINK_END}\n"))
    targets = [fp for _t, fp, _r in lm.parse_links(p)]
    check("outbound link is still parsed",
          "../tackle/gear-classes.md" in targets, True)
    check("backlink-block entry is NOT parsed as outbound",
          "../species/yellowtail.md" in targets, False)


def test_strip_backlinks_block_is_noop_without_markers(tmp: Path) -> None:
    body = "# Note\n\nNo markers here at all.\n"
    check("strip is a no-op when markers are absent",
          lm.strip_backlinks_block(body), body)


def test_code_stripping_still_works(tmp: Path) -> None:
    """The pre-existing guarantee (tests/link-fixture.md) must not regress."""
    p = write(tmp, "code.md", FM + (
        "# Note\n\n"
        "```\n[fake](../nope/void.md)\n```\n\n"
        "Inline `[fake2](../nope/void2.md)` too.\n\n"
        "Real: [index](../README.md).\n"))
    targets = [fp for _t, fp, _r in lm.parse_links(p)]
    check("fenced-code link ignored", "../nope/void.md" in targets, False)
    check("inline-code link ignored", "../nope/void2.md" in targets, False)
    check("real link parsed", "../README.md" in targets, True)


def main() -> int:
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        for fn in (test_summary_keeps_bold_lead,
                   test_summary_still_skips_real_bullets,
                   test_summary_skips_thematic_break,
                   test_backlink_block_stripped,
                   test_strip_backlinks_block_is_noop_without_markers,
                   test_code_stripping_still_works):
            fn(tmp)
    if failures:
        print(f"FAILED ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("link-maintenance tests: 6 checks groups OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
