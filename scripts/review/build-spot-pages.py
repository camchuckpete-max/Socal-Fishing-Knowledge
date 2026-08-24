#!/usr/bin/env python3
"""build-spot-pages.py — write the minimum spot pages MECHANICALLY.

Cameron, 2026-08-24. Of the 344 spot pages the ladder calls for, only a
handful have any corpus material; the rest carry a coordinate and a parent
zone and nothing else. Handing those to the fleet meant Opus writing ~331
pages from a template at two subagent calls each — half the entire remaining
job — and, worse, retyping 391 coordinate pairs. A wrong waypoint on a
fishing page is a real-world hazard, not a typo.

So the minimum pages are generated here: deterministic, coordinates copied
from the parsed source digit-for-digit, passing check-note by construction.
The fleet then writes only the spots that actually have something to say.

    python scripts/review/build-spot-pages.py --dry-run   # decisions + plan
    python scripts/review/build-spot-pages.py             # write pages

Idempotent and non-destructive: an existing page is never touched, so a
re-run as the harvest grows only adds what is missing and can never clobber
fleet enrichment or a hand-written page.
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from geo_slug import slugify  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "build_geo_worklist", HERE / "build-geo-worklist.py")
_geo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_geo)

LOCATIONS = ROOT / "locations"
WORKLIST = ROOT / "sources" / "review-worklist.md"
WL_END = "<!-- review:worklist:end -->"
HARVEST = ROOT / "sources" / "spot-harvest.md"

# `waters` is a gated closed vocabulary — it cannot be `unknown` — so it is
# decided per ZONE and inherited by that zone's spots: 76 reviewable calls
# instead of 344 guesses. Everything offshore defaults to `bank`; the
# exceptions are listed. --dry-run prints the whole assignment.
WATERS_BY_SLUG = {
    # island chains
    "catalina-island-front-side": ["island"],
    "catalina-island-backside": ["island"],
    "san-clemente-island-front-side": ["island"],
    "san-clemente-island-back-side": ["island"],
    "coronado-islands": ["island"],
    "san-nicolas-island": ["island"],
    "santa-barbara-island": ["island"],
    # coastal strips
    "la-jolla": ["nearshore-coast"],
    "point-loma": ["nearshore-coast"],
    "dana-point": ["nearshore-coast"],
    "oceanside-north-county": ["nearshore-coast"],
    "imperial-beach": ["nearshore-coast"],
    "south-orange-county-crystal-cove": ["nearshore-coast"],
    "rosarito-descanso": ["nearshore-coast"],
    "la-fonda-bajamar-salsipuedes": ["nearshore-coast"],
    "ensenada": ["nearshore-coast"],
    "colonet": ["nearshore-coast"],
    "punta-banda-santo-tomas": ["nearshore-coast"],
    "san-quintin": ["island", "nearshore-coast"],   # San Martin sits in it
    # man-made structure on the coastal shelf
    "north-county-artificial-reefs": ["nearshore-coast"],
    "san-diego-artificial-reefs": ["nearshore-coast"],
    "international-artificial-reef": ["nearshore-coast"],
    # named bank complexes
    "finger-bank-rockfish": ["bank"],
}
DEFAULT_WATERS = ["bank"]        # every cluster / isolated offshore bank


def waters_for(zone: dict) -> list[str]:
    return WATERS_BY_SLUG.get(zone["slug"], DEFAULT_WATERS)


def coord_text(raw: tuple[str, str, str, str]) -> str:
    """Publish the source's own digits. No float ever reaches this string."""
    d_lat, m_lat, d_lon, m_lon = raw
    return f"{d_lat}°{m_lat}'N {d_lon}°{m_lon}'W"


def tags_for(name: str, zone: dict) -> list[str]:
    out = [t for t in slugify(name).split("-") if t and not t.isdigit()][:3]
    out.append(zone["slug"])
    seen, uniq = set(), []
    for t in out:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq[:5]


GAP = "⚠ Flagged gap — no corpus source"


def page_text(name: str, zone: dict, raw, waters: list[str],
              ar_rows: list[tuple[str, tuple]] | None = None) -> str:
    parent = f"{zone['slug']}.md"
    kind = ("artificial-reef complex" if ar_rows else "spot")
    fm = [
        "---", "type: location",
        f"tags: [{', '.join(tags_for(name, zone))}]",
        "sources: [cameron]", "confidence: medium",
        f"regions: [{zone['region']}]",
        f"waters: [{', '.join(waters)}]",
        "layout: v2", f"parent: {parent}",
        "structure_type: unknown", "depth_band: unknown",
        "distance_nm: unknown",
    ]
    if not ar_rows:
        fm.append(f"coordinates: {coord_text(raw)}")
    fm.append("---")

    zname = zone["display"]
    if ar_rows:
        lead = (
            f"The **{name}** series — {len(ar_rows)} charted waypoints on one "
            f"artificial-reef complex, in the [{zname}]({parent}) zone. The "
            f"numbered waypoints have no fishing identity apart from each "
            f"other, so they share this page; every position is in the table "
            f"below.")
    else:
        lead = (
            f"A charted {kind} at **{coord_text(raw)}** (cameron), in the "
            f"[{zname}]({parent}) zone.")

    body = [
        "", f"# {name}", "", lead, "",
        "**This is a minimum page.** The corpus carries the position and the "
        "parent zone and nothing further yet; the flagged gaps below are what "
        "a source would fill, and they are aggregated into "
        "[the gap report](../sources/gap-report.md).", "",
        "## Getting there", "",
        f"{GAP}: the run, the approach, and where to start.", "",
        "## Structure & bathymetry", "",
        f"{GAP}: depth, bottom composition, and how it sits relative to the "
        f"rest of the zone.", "",
    ]
    if ar_rows:
        body += ["Charted waypoints, as published in "
                 "[the spot library](../sources/spot-lists.md):", "",
                 "| waypoint | position |", "| --- | --- |"]
        body += [f"| {n} | {coord_text(r)} |" for n, r in ar_rows]
        body += [""]
    body += [
        "## What's there", "",
        "| species | season | what this spot does for them |",
        "| --- | --- | --- |",
        f"| {GAP} | — | — |", "",
        "## How it fishes", "",
        f"{GAP}. The zone-level program is on "
        f"[{zname}]({parent}).", "",
        "<!-- backlinks:start -->", "## Linked from", "<!-- backlinks:end -->",
        "",
    ]
    return "\n".join(fm + body)


def harvested_slugs() -> set[str]:
    if not HARVEST.exists():
        return set()
    text = HARVEST.read_text(encoding="utf-8")
    if "<!-- review:harvest:start -->" not in text:
        return set()
    block = text.split("<!-- review:harvest:start -->", 1)[1] \
                .split("<!-- review:harvest:end -->", 1)[0]
    out = set()
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) == 5 and cells[0] not in ("spot", "") \
                    and set(cells[0]) - {"-", " "}:
                out.add(slugify(cells[0]))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    spots = _geo.parse_spot_lists()
    zones, spot_rows, ar_series, non_spot, _un = _geo.build_zones(spots, None)
    by_name = {s["name"]: s for s in spots}
    harvest = harvested_slugs()
    zone_slugs = {z["slug"] for z in zones}

    print("## `waters` by zone (inherited by its spots)")
    for z in sorted(zones, key=lambda z: z["slug"]):
        if not z["spots"]:
            continue
        mark = "" if z["slug"] in WATERS_BY_SLUG else "   (default)"
        print(f"  {z['slug']:<46} {','.join(waters_for(z)):<26}{mark}")

    plan, skip_exists, collide, enrich, waiting = [], [], [], [], []
    for r in spot_rows:
        slug, zone = r["slug"], r["zone"]
        src = by_name.get(r["display"])
        if src is None:
            continue
        if slug in zone_slugs:
            # e.g. the spot "Tanner Bank" inside the zone "Tanner Bank" — the
            # zone page IS that place; a second file would collide with it.
            collide.append((r["display"], zone["display"]))
            continue
        if slug in harvest:
            enrich.append(r["display"])         # the fleet writes this one
            continue
        path = LOCATIONS / f"{slug}.md"
        if path.exists():
            skip_exists.append(slug)
            continue
        if not (LOCATIONS / f"{zone['slug']}.md").exists():
            waiting.append((r["display"], zone["slug"]))
            continue
        plan.append((path, r["display"], zone, src["raw"]))

    ar_plan = []
    for key, a in ar_series.items():
        path = LOCATIONS / f"{key}.md"
        rows = [(s["name"], s["raw"]) for s in a["zone"]["spots"]
                if _geo.AR_SERIES.match(s["name"])
                and slugify((_geo.AR_SERIES.match(s["name"]).group(1)
                             or _geo.AR_SERIES.match(s["name"]).group(2)
                             ).strip()) == key]
        if path.exists():
            skip_exists.append(key)
            continue
        if not (LOCATIONS / f"{a['zone']['slug']}.md").exists():
            waiting.append((a["display"], a["zone"]["slug"]))
            continue
        ar_plan.append((path, a["display"], a["zone"], rows))

    print(f"\n## Plan\n  {len(plan)} minimum spot pages"
          f"\n  {len(ar_plan)} AR complex pages"
          f" (covering {sum(len(r[3]) for r in ar_plan)} waypoints)"
          f"\n  {len(enrich)} left to the FLEET (corpus material exists)"
          f"\n  {len(skip_exists)} already exist — untouched"
          f"\n  {len(collide)} spot/zone name collisions — the zone page is"
          f" that place"
          f"\n  {len(non_spot)} excluded (not fishing spots)"
          f"\n  {len(waiting)} WAITING on their zone page — the geo phase"
          f" writes those first, then the next checkpoint picks these up")
    for n, z in collide:
        print(f"    collision: {n}  ==  zone {z}")
    if enrich:
        print("  fleet writes: " + ", ".join(sorted(enrich)[:12])
              + (" …" if len(enrich) > 12 else ""))

    if args.dry_run:
        print("\n--dry-run: nothing written.")
        return 0

    written = []
    for path, name, zone, raw in plan:
        path.write_text(page_text(name, zone, raw, waters_for(zone)),
                        encoding="utf-8")
        written.append(path.name)
    for path, name, zone, rows in ar_plan:
        path.write_text(page_text(name, zone, None, waters_for(zone),
                                  ar_rows=rows), encoding="utf-8")
        written.append(path.name)

    # The worklist stays a COMPLETE inventory: a mechanical page is `done`
    # (real work, just not the fleet's), an enrichable one is `pending`.
    wl = WORKLIST.read_text(encoding="utf-8")
    rows = []
    for path, name, _z, _r in plan:
        rows.append(f"| locations/{path.name} | gazetteer | done |  | "
                    f"mechanical: coordinates + parent zone |")
    for path, name, _z, rr in ar_plan:
        rows.append(f"| locations/{path.name} | gazetteer | done |  | "
                    f"mechanical: AR complex, {len(rr)} waypoints |")
    for name in enrich:
        s = slugify(name)
        rows.append(f"| locations/{s}.md | gazetteer | pending |  | "
                    f"corpus material harvested — fleet writes this one |")
    fresh = [r for r in rows if f"| {r.split('|')[1].strip()} |" not in wl]
    if fresh:
        WORKLIST.write_text(wl.replace(WL_END, "\n".join(fresh) + "\n" + WL_END),
                            encoding="utf-8")
    print(f"\nwrote {len(written)} page(s); appended {len(fresh)} worklist row(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
