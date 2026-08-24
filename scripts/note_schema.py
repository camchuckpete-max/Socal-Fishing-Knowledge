#!/usr/bin/env python3
"""note_schema.py — the machine layer of the layout spec (see templates/).

Single source of truth for the per-type note skeletons, infobox front-matter
fields, cite forms, and flag grammar introduced by the 2026-08 editorial
review (sources/plan-review.md). `templates/` is the human mirror of this
module; a change to one is a change to both, in the same commit.

All new validation is OPT-IN via the front-matter key `layout: v2`, written
by the review transform when a note is migrated. Notes without the key are
untouched by these rules, so CI stays green while the KB is mid-migration.

Consumed by: scripts/link-maintenance.py (validation), scripts/review/
check-note.py (per-note acceptance), scripts/review/gap-report.py.
"""
from __future__ import annotations

import re

LAYOUT_KEY = "layout"
LAYOUT_CURRENT = "v2"
FM_LAYOUT_RE = re.compile(r"^layout:\s*(\S+)", re.M)

# --- section skeletons --------------------------------------------------------
# Required `##` headings per type, in canonical relative order. Matching is by
# PREFIX: a heading passes when it starts with the canonical text, so
# "## Finding them (sign & sonar)" satisfies "## Finding them". Extra sections
# are allowed anywhere between required ones; required ones must all be present
# and in this order. `## Evidence` is governed by the pairing rule below, and
# `## Linked from` is machine-generated — neither is listed here.
REQUIRED_SECTIONS: dict[str, list[str]] = {
    "species": [
        "## Where & when",
        "## Presence & forage",
        "## Spawning",
        "## Feeding triggers",
        "## Finding them",
        "## Situations → techniques",
        "## Gear summary",
        "## Regulations",
        "## Doctrine & conflicts",
        "## Landing & handling",
    ],
    "technique": [
        "## Reach for this when",
        "## Gear class",
        "## Common failures",
    ],
    "lure": [
        "## Specs",
        "## When to choose it",
    ],
    "rig": [
        "## When to use",
        "## Parameters",
    ],
    "conditions": [
        "## How to use it in planning",
    ],
    "location": [
        "## Getting there",
        "## Structure & bathymetry",
        "## What's there",
        "## How it fishes",
    ],
    "decision": [
        "## Situations → techniques",
    ],
    "zone-guide": [
        "## The program",
        "## Reading the day",
        "## Rigs & gear",
        "## Differs from nearby zones",
    ],
    # Types with no mandated sections beyond lead + Evidence/Linked from:
    "seasonal": [],
    "bait": [],
    "tackle": [],
    "fish-care": [],
    "planning": [],
    "profile": [],
    "evidence": [],
}

# --- infobox front matter -----------------------------------------------------
# Required keys per type on `layout: v2` notes, in addition to the universal
# type/tags/sources/confidence (+ regions/waters on gated types). Values are
# scalars or one-line flow lists — the KB's YAML subset (export-site-index.py
# parses nothing richer). The literal string `unknown` is a legal value and is
# what the gap report counts; omitting a required key is a validation failure.
INFOBOX_FIELDS: dict[str, list[str]] = {
    "species": ["scientific_name", "season_peak", "sst_band_f", "depth_band",
                "gear_classes", "sonar_depth"],
    "technique": ["gear_classes", "depth_band", "retrieve_speed"],
    "lure": ["lure_class", "weights", "depth_band", "run_speed"],
    "rig": ["line_class", "hook_sizes"],
    "location": ["parent_zone", "structure_type", "depth_band", "distance_nm"],
    "seasonal": ["regime"],
    "zone-guide": ["species", "zone", "season_window", "run"],
    "evidence": ["parent"],
}
# Optional, never required (a location may legitimately omit it; charted/public
# positions only — personal waypoints stay in profiles/):
LOCATION_OPTIONAL_FIELDS = ["coordinates"]

# Front-matter keys whose value is a RELATIVE MARKDOWN PATH that must resolve
# from the note's directory (validated like a link). `unknown` is not legal
# here — omit `parent_zone` on a top-level zone instead. (`zone` on a
# zone-guide may be plain text until the gazetteer page exists, so it is not
# listed.)
PATH_FIELDS = {"parent_zone", "parent", "species"}

# --- cites --------------------------------------------------------------------
# Canonical inline cite forms: a backticked 11-char YouTube video id, or the
# literal token (cameron). Everything else is legacy and is normalized by
# scripts/review/resolve-cites.py.
VIDEO_ID_RE = re.compile(r"[A-Za-z0-9_-]{11}")
CITE_RE = re.compile(r"\(`[A-Za-z0-9_-]{11}`(?:, `[A-Za-z0-9_-]{11}`)*\)"
                     r"|\(cameron\)")
# Legacy forms the review retires (matched for detection, never for writing):
LEGACY_BARE_DATE_RE = re.compile(r"\((\d{1,2}/\d{1,2}/\d{2})\)")

# --- flag grammar -------------------------------------------------------------
# Inline markers. Every fact-check flag also gets a ledger row in
# sources/fact-check-ledger.md; every gap line is aggregated by
# scripts/review/gap-report.py into sources/gap-report.md.
FLAG_GAP = "⚠ Flagged gap — no corpus source"
FLAG_STUB = "⚠ Flagged stub — no corpus source yet"  # router rows; pre-dates v2
FACTCHECK_CATEGORIES = ("single-source", "contradicted-by-source",
                        "contradicted-internal", "external-mismatch",
                        "unverifiable")
FLAG_FACTCHECK_RE = re.compile(
    r"⚠ Fact-check \((" + "|".join(FACTCHECK_CATEGORIES) + r")\):")
FLAG_CITE_UNRESOLVED = "⚠ cite-unresolved"
FLAG_MISPLACED = "⚠ misplaced-content"


def front_matter_block(text: str) -> str:
    """The raw front-matter block (between the --- fences), or ''."""
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def layout_of(text: str) -> str | None:
    m = FM_LAYOUT_RE.search(front_matter_block(text))
    return m.group(1) if m else None


def fm_keys(text: str) -> set[str]:
    """Top-level front-matter key names (wrapped flow-list continuations are
    not keys — same joining rule as export-site-index.py)."""
    keys = set()
    for line in front_matter_block(text).splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):", line)
        if m:
            keys.add(m.group(1))
    return keys


def fm_value(text: str, key: str) -> str:
    """Scalar value of a front-matter key (first line only), '' if absent."""
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", front_matter_block(text), re.M)
    return m.group(1).split("#", 1)[0].strip().strip("'\"") if m else ""


def headings_of(text: str) -> list[str]:
    """All `## ` headings in body order (front matter and code stripped by the
    caller when needed — headings inside fences are rare enough that
    link-maintenance strips code first)."""
    return [ln.rstrip() for ln in text.splitlines() if ln.startswith("## ")]


def section_problems(note_type: str, text: str) -> list[str]:
    """Required-section presence + relative order for one note's body text."""
    required = REQUIRED_SECTIONS.get(note_type)
    if not required:
        return []
    heads = headings_of(text)
    idx: list[tuple[str, int]] = []
    problems: list[str] = []
    for canon in required:
        pos = next((i for i, h in enumerate(heads) if h.startswith(canon)), None)
        if pos is None:
            problems.append(f"missing required section {canon!r} (type {note_type})")
        else:
            idx.append((canon, pos))
    for (a, pa), (b, pb) in zip(idx, idx[1:]):
        if pb < pa:
            problems.append(f"section {b!r} appears before {a!r} "
                            f"(canonical order in templates/{note_type}.md)")
    return problems


def infobox_problems(note_type: str, text: str) -> list[str]:
    required = INFOBOX_FIELDS.get(note_type)
    if not required:
        return []
    present = fm_keys(text)
    return [f"missing infobox field `{k}:` (type {note_type}; "
            f"the literal value `unknown` is legal)"
            for k in required if k not in present]
