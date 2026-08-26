#!/usr/bin/env python3
"""check-coordinates.py — every published position must trace to the source.

The gazetteer publishes hundreds of coordinates. A wrong waypoint on a
fishing page is a real-world hazard, not a typo, so this asserts rather than
trusts: each `DD°MM.mmm'N DDD°MM.mmm'W` string appearing anywhere in
`locations/` must match, digit for digit, an entry in
`sources/spot-lists.md`.

It has already earned its place — it caught a hand-typed zone-CENTRE
coordinate on `locations/coronado-islands.md` that existed in no source.

Exit 0 clean, 1 on any mismatch. Run before every commit that touches
`locations/`, and at the chunk checkpoint.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
COORD = re.compile(r"(\d+)°([\d.]+)'N (\d+)°([\d.]+)'W")
SRC = re.compile(r"^- (.+?) — (\d+) ([\d.]+) / (\d+) ([\d.]+)\s*$", re.M)


def known_positions() -> set[tuple[str, ...]]:
    text = (ROOT / "sources" / "spot-lists.md").read_text(encoding="utf-8")
    return {m.groups()[1:] for m in SRC.finditer(text)}


def unsourced_in(text: str, known: set[tuple[str, ...]] | None = None
                 ) -> list[str]:
    """Positions in `text` that appear in no spot-library entry.

    Exposed so check-note.py can run the same assertion on ONE note before it
    is committed. The whole-tree sweep catches these too, but only after the
    fact: it reddens the run, aborts the sweep step before its push, and says
    nothing about which unit is responsible. Per-unit, the offending unit
    escalates itself and the chain stays green.
    """
    if known is None:
        known = known_positions()
    return [m.group(0) for m in COORD.finditer(text) if m.groups() not in known]


def main() -> int:
    known = known_positions()
    if not known:
        print("check-coordinates: no source coordinates parsed", file=sys.stderr)
        return 1

    ok, bad = 0, []
    for p in sorted((ROOT / "locations").rglob("*.md")):
        for m in COORD.finditer(p.read_text(encoding="utf-8")):
            if m.groups() in known:
                ok += 1
            else:
                bad.append((p.relative_to(ROOT), m.group(0)))

    for path, coord in bad:
        print(f"UNSOURCED COORDINATE  {path}: {coord}", file=sys.stderr)
    print(f"check-coordinates: {ok} published position(s) match "
          f"sources/spot-lists.md exactly, {len(bad)} unsourced")
    if bad:
        print("A published position must be copied from the spot library, "
              "never computed or typed from memory.", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
