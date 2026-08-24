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


def main() -> int:
    text = (ROOT / "sources" / "spot-lists.md").read_text(encoding="utf-8")
    known = {m.groups()[1:] for m in SRC.finditer(text)}
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
