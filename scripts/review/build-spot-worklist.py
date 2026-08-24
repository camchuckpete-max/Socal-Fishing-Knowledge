#!/usr/bin/env python3
"""build-spot-worklist.py — turn the spot harvest into gazetteer worklist rows.

Reads sources/spot-harvest.md (rows `| spot | note | section | claim | cite |`
appended by the transform pass), normalizes spot names to kebab slugs,
deduplicates, drops spots that already have a locations/ page, and APPENDS
`| locations/<slug>.md | gazetteer | pending |  | harvest: N mention(s) |`
rows to the review worklist for the rest. Append-if-absent: idempotent, safe
to run at every checkpoint.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
HARVEST = ROOT / "sources" / "spot-harvest.md"
WORKLIST = ROOT / "sources" / "review-worklist.md"
H_START, H_END = "<!-- review:harvest:start -->", "<!-- review:harvest:end -->"
WL_END = "<!-- review:worklist:end -->"

# Slugging lives in geo_slug.py — ONE implementation for the whole ladder.
# Two of them is how the accented Bahia duplicates got queued (see that module).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from geo_slug import slugify, dedupe_key  # noqa: E402


def existing_page_keys() -> dict[str, str]:
    """Normalized identity -> path, for every locations/ page that exists."""
    out = {}
    for p in (ROOT / "locations").glob("*.md"):
        if p.name != "README.md":
            out[dedupe_key(p.stem)] = p.name
    return out


def main() -> int:
    if not HARVEST.exists():
        print("build-spot-worklist: no harvest file yet")
        return 0
    text = HARVEST.read_text(encoding="utf-8")
    if H_START not in text:
        print("build-spot-worklist: harvest markers missing")
        return 0
    block = text.split(H_START, 1)[1].split(H_END, 1)[0]
    counts: dict[str, int] = {}
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 5 or cells[0] in ("spot", "") \
                or set(cells[0]) <= {"-", " "}:
            continue
        slug = slugify(cells[0])
        if slug:
            counts[slug] = counts.get(slug, 0) + 1

    # Drop anything whose folded identity already has a page (this is the
    # check the old raw-slug comparison failed).
    have = existing_page_keys()
    for slug in [k for k in counts if dedupe_key(k) in have]:
        print(f"build-spot-worklist: {slug} -> existing {have[dedupe_key(slug)]}")
        counts.pop(slug)

    wl = WORKLIST.read_text(encoding="utf-8")
    added = skipped = 0
    new_rows = []
    for slug in sorted(counts):
        rel = f"locations/{slug}.md"
        if (ROOT / rel).exists():
            skipped += 1  # existing page; its worklist row already covers it
            continue
        if f"| {rel} |" in wl:
            continue  # row already appended by an earlier run
        new_rows.append(f"| {rel} | gazetteer | pending |  | "
                        f"harvest: {counts[slug]} mention(s) |")
        added += 1
    if new_rows:
        wl = wl.replace(WL_END, "\n".join(new_rows) + "\n" + WL_END)
        WORKLIST.write_text(wl, encoding="utf-8")
    print(f"build-spot-worklist: {len(counts)} distinct spots harvested, "
          f"{added} gazetteer rows appended, {skipped} already have pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
