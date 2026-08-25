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


GATED_FM = ("---\ntype: species\ntags: [x]\nsources: [cameron]\n"
            "confidence: high\n{extra}---\n\n# T\n\nBody.\n")


def test_region_gating_accepts_valid(tmp: Path) -> None:
    p = write(tmp, "ok.md", GATED_FM.format(
        extra="regions: [socal-bight, cortez-north]\nwaters: [island, bank]\n"))
    check("valid gating passes", lm.region_problems(p), [])


def test_region_gating_requires_fields(tmp: Path) -> None:
    p = write(tmp, "missing.md", GATED_FM.format(extra=""))
    probs = " ".join(lm.region_problems(p))
    check("missing regions is reported", "missing `regions:`" in probs, True)
    check("missing waters is reported", "missing `waters:`" in probs, True)


def test_region_gating_rejects_off_vocabulary(tmp: Path) -> None:
    p = write(tmp, "bad.md", GATED_FM.format(
        extra="regions: [socal-bight, atlantic]\nwaters: [island]\n"))
    probs = " ".join(lm.region_problems(p))
    check("off-vocabulary region rejected", "'atlantic'" in probs, True)


def test_region_gating_skips_ungated_types(tmp: Path) -> None:
    p = write(tmp, "profile.md",
              "---\ntype: profile\ntags: [x]\nsources: []\n"
              "confidence: high\n---\n\n# T\n\nBody.\n")
    check("ungated type needs no region fields", lm.region_problems(p), [])


def test_subregions_are_retired(tmp: Path) -> None:
    """Assignment is at region level only (Cameron, 2026-08-17)."""
    p = write(tmp, "sub.md", GATED_FM.format(
        extra="regions: [cortez-north]\nsubregions: [bola]\nwaters: [island]\n"))
    check("a leftover subregions field is reported",
          "retired" in " ".join(lm.region_problems(p)), True)


V2_SPECIES_FM = ("---\ntype: species\ntags: [x]\nsources: [cameron]\n"
                 "confidence: high\nregions: [socal-bight]\nwaters: [island]\n"
                 "layout: v2\nscientific_name: unknown\nseason_peak: [jun]\n"
                 "sst_band_f: 62-74\ndepth_band: unknown\ngear_classes: [jig-stick]\n"
                 "sonar_depth: unknown\n---\n\n")

V2_SPECIES_BODY_OK = (
    "# Testfish\n\nLead.\n\n"
    "## Where & when\nx\n\n## Presence & forage\nx\n\n## Spawning\nx\n\n"
    "## Feeding triggers\nx\n\n## Finding them (sign & sonar)\nx\n\n"
    "## Situations → techniques\nx\n\n## Gear summary (class terms)\nx\n\n"
    "## Zone guides\nx\n\n"
    "## Regulations\nx\n\n## Doctrine & conflicts\nx\n\n"
    "## Landing & handling\nx\n")


# --- container rungs: the child list is generated, never hand-kept ----------
# Both regressions below cost real fleet units. A zone page shipped without
# the markers left its spot list hand-written, which no worker is allowed to
# update (guard scope) — so it would have silently decayed. And the geo worker
# PROMPT, which only quotes the marker while explaining it, had a spot list
# appended to it because the check was "does the text contain the marker"
# rather than "is this a container rung".

V2_ZONE_FM = ("---\ntype: zone\ntags: [x]\nsources: [cameron]\n"
              "confidence: high\nregions: [socal-bight]\nwaters: [island]\n"
              "layout: v2\nparent: unknown\nstructure_type: island\n"
              "depth_band: unknown\ndistance_nm: unknown\n---\n\n")

V2_ZONE_BODY = (
    "# Testzone\n\nLead.\n\n"
    "## Getting there\nx\n\n## Structure & bathymetry\nx\n\n"
    "## What's there\nx\n\n## How it fishes\nx\n\n"
    "## Spots\n\nCurated character prose.\n\n"
    "<!-- children:start -->\n<!-- children:end -->\n")


def test_container_rung_with_markers_passes(tmp: Path) -> None:
    p = write(tmp, "zoneok.md", V2_ZONE_FM + V2_ZONE_BODY)
    check("a zone carrying the children markers passes",
          lm.layout_problems(p), [])


def test_container_rung_without_markers_is_reported(tmp: Path) -> None:
    body = V2_ZONE_BODY.replace(
        "<!-- children:start -->\n<!-- children:end -->\n", "- hand list\n")
    p = write(tmp, "zonebad.md", V2_ZONE_FM + body)
    probs = " ".join(lm.layout_problems(p))
    check("a container rung with a hand-kept child list is reported",
          "container rung" in probs, True)


def test_child_list_generated_and_placeholder_when_empty(tmp: Path) -> None:
    check("an empty rung says so rather than rendering nothing",
          "no pages under this rung yet" in lm.CHILD_EMPTY, True)
    check("the generated block is the list only — the heading is authored",
          "##" in lm.CHILD_EMPTY, False)


def test_layout_v2_valid_species_passes(tmp: Path) -> None:
    p = write(tmp, "v2ok.md", V2_SPECIES_FM + V2_SPECIES_BODY_OK)
    check("valid v2 species skeleton passes", lm.layout_problems(p), [])


def test_layout_v2_missing_section(tmp: Path) -> None:
    body = V2_SPECIES_BODY_OK.replace("## Spawning\nx\n\n", "")
    p = write(tmp, "v2miss.md", V2_SPECIES_FM + body)
    probs = " ".join(lm.layout_problems(p))
    check("missing required section reported", "'## Spawning'" in probs, True)


def test_layout_v2_section_order(tmp: Path) -> None:
    body = V2_SPECIES_BODY_OK.replace(
        "## Where & when\nx\n\n## Presence & forage\nx\n\n",
        "## Presence & forage\nx\n\n## Where & when\nx\n\n")
    p = write(tmp, "v2order.md", V2_SPECIES_FM + body)
    probs = " ".join(lm.layout_problems(p))
    check("out-of-order section reported", "appears before" in probs, True)


def test_layout_v2_missing_infobox_field(tmp: Path) -> None:
    fm = V2_SPECIES_FM.replace("sonar_depth: unknown\n", "")
    p = write(tmp, "v2info.md", fm + V2_SPECIES_BODY_OK)
    probs = " ".join(lm.layout_problems(p))
    check("missing infobox field reported", "`sonar_depth:`" in probs, True)


def test_layout_v1_note_is_untouched(tmp: Path) -> None:
    fm = V2_SPECIES_FM.replace("layout: v2\n", "")
    p = write(tmp, "v1.md", fm + "# Old\n\nNo sections at all.\n")
    check("non-migrated note has no layout problems", lm.layout_problems(p), [])


def test_layout_evidence_pairing(tmp: Path) -> None:
    (tmp / "evidence").mkdir(exist_ok=True)
    parent = write(tmp, "fish.md", V2_SPECIES_FM + V2_SPECIES_BODY_OK
                   + "\n## Evidence\n\n[evidence file](evidence/fish.md)\n")
    ev = write(tmp / "evidence", "fish.md",
               "---\ntype: evidence\nparent: ../fish.md\ntags: [x]\n"
               "sources: []\nconfidence: medium\n---\n\n# Evidence — fish\n")
    check("paired evidence file passes", lm.layout_problems(ev), [])
    check("parent with linked evidence passes", lm.layout_problems(parent), [])
    unlinked = write(tmp, "nofish.md", V2_SPECIES_FM + V2_SPECIES_BODY_OK)
    (tmp / "evidence" / "nofish.md").write_text(
        "---\ntype: evidence\nparent: ../nofish.md\ntags: [x]\nsources: []\n"
        "confidence: medium\n---\n\n# E\n", encoding="utf-8")
    probs = " ".join(lm.layout_problems(unlinked))
    check("evidence file without a `## Evidence` section is reported",
          "no `## Evidence` section" in probs, True)


def test_region_badge(tmp: Path) -> None:
    baja = write(tmp, "b.md", GATED_FM.format(
        extra="regions: [cortez-north, cortez-south]\nwaters: [island]\n"))
    socal = write(tmp, "s.md", GATED_FM.format(
        extra="regions: [socal-bight]\nwaters: [island]\n"))
    both = write(tmp, "d.md", GATED_FM.format(
        extra="regions: [socal-bight, baja-pacific-north]\nwaters: [island]\n"))
    check("Baja-only note is badged", lm.region_badge(baja), " **[Baja only]**")
    check("SoCal-only note is badged", lm.region_badge(socal), " **[SoCal only]**")
    check("spanning note is not badged", lm.region_badge(both), "")


def main() -> int:
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        for fn in (test_summary_keeps_bold_lead,
                   test_summary_still_skips_real_bullets,
                   test_summary_skips_thematic_break,
                   test_backlink_block_stripped,
                   test_strip_backlinks_block_is_noop_without_markers,
                   test_code_stripping_still_works,
                   test_region_gating_accepts_valid,
                   test_region_gating_requires_fields,
                   test_region_gating_rejects_off_vocabulary,
                   test_region_gating_skips_ungated_types,
                   test_subregions_are_retired,
                   test_layout_v2_valid_species_passes,
                   test_layout_v2_missing_section,
                   test_layout_v2_section_order,
                   test_layout_v2_missing_infobox_field,
                   test_layout_v1_note_is_untouched,
                   test_layout_evidence_pairing,
                   test_region_badge,
                   test_container_rung_with_markers_passes,
                   test_container_rung_without_markers_is_reported,
                   test_child_list_generated_and_placeholder_when_empty):
            fn(tmp)
    if failures:
        print(f"FAILED ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("link-maintenance tests: 21 check groups OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
