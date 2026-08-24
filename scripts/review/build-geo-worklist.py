#!/usr/bin/env python3
"""build-geo-worklist.py — derive the geographic ladder and queue it.

Amendment v2.2 (sources/plan-review.md). Emits worklist rows for
jurisdiction -> region -> area -> zone -> spot, TOP-DOWN, because every rung's
`parent` must resolve before the rung below it can be written.

    python scripts/review/build-geo-worklist.py --dry-run   # the CENSUS
    python scripts/review/build-geo-worklist.py             # append rows

`--dry-run` is the GATE ARTIFACT: it prints every page it would create with
its rung, parent, differentiated mention count and which clause of the
existence bar it passed, plus every candidate it would flag as a stub and why,
plus per-spot parent + distance so a mis-parented spot is visible on the page.
It writes nothing.

Zones come from COORDINATES, not mention counts (Cameron, 2026-08-24):

  1. the `##` sections of sources/spot-lists.md ARE the zone skeleton — a
     fisherman's carve-up outranks anything a script infers;
  2. constrained clustering subdivides the one catch-all section (`Offshore
     banks (N->S)` is 125 spots in latitude order, a list not a zone).
     COMPLETE-linkage with a max diameter: single-linkage chains the whole
     coast into one 309-spot, 192-nm blob;
  3. corpus mention counts survive only as a CONTENT-DEPTH signal — how much a
     zone page can say, never whether it exists.
"""
from __future__ import annotations

import argparse
import math
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from geo_slug import slugify, dedupe_key  # noqa: E402

SPOT_LISTS = ROOT / "sources" / "spot-lists.md"
WORKLIST = ROOT / "sources" / "review-worklist.md"
WL_END = "<!-- review:worklist:end -->"

MAX_ZONE_DIAMETER_NM = 12.0     # complete-linkage cap; see module docstring
AREA_BAR_NOTES = 6              # the existence bar, stated as a number

KNOWLEDGE_DIRS = ["species", "techniques", "lures", "rigging", "tackle", "bait",
                  "fish-care", "conditions", "seasonal", "locations", "planning",
                  "profiles"]

# The catch-all section that is a sorted list rather than a zone.
CATCHALL = "Offshore banks"

# Sections that are species FILTERS over a place already sectioned elsewhere,
# not places of their own — they merge into their geographic parent so a spot
# is never claimed by two zones.
FILTER_SECTIONS = {
    "Catalina Island — Rockfish spots": "Catalina Island — Front Side (W→E)",
    "Rockfish areas (Coronados vicinity)": "Coronado Islands",
}

# Sections that are one heading but more than one run. Split BY NAME so the
# carve-up is auditable in review rather than emerging from a threshold.
#
# "Northern Baja" (Cameron, 2026-08-24) was the case that forced this: a single
# 33-nm heading from the border (Bull Ring, 32.525N) to Punta Salsipuedes
# (31.973N). It is genuinely the northernmost Baja COASTAL zone — only the
# Coronado Islands share its latitudes and those are offshore — but the name
# collided with the `baja-pacific-north` REGION term, and its own ends were
# three of the census's parent-distance outliers.
SECTION_SPLITS = {
    "Northern Baja": [
        ("Rosarito / Descanso", {
            "Bull Ring", "Rosarito Flats (big area)", "Punta Descanso",
            "Descanso rockfish 1", "Descanso rockfish 2", "Sugarloaf Rock"}),
        ("La Fonda / Bajamar / Salsipuedes", {
            "Punta Mesquite", "La Fonda", "Bajamar", "Punta Salsipuedes"}),
    ],
}

# A lone offshore bank is a spot, not a zone, when it sits within reach of a
# real zone. Beyond this it is its own single-spot zone — an isolated seamount
# genuinely is a destination.
ORPHAN_ATTACH_NM = 25.0

# Numbered artificial-reef series collapse to one complex page carrying a
# coordinate table (Cameron, 2026-08-24) — "Carlsbad AR 7" has no fishing
# identity apart from "Carlsbad AR 6", and spot-lists already treats the
# series as one pixel. Every coordinate stays published, on that table.
AR_SERIES = re.compile(r"^(.*?\bAR|International Reef|.*?Artificial Reef)\s+"
                       r"[0-9]+[A-Za-z]?$|^(.*?\bAR)\s+[A-Z]$")

# Entries the library carries that are not fishing spots — surfaced for
# Cameron's call rather than silently minted as pages.
# ONLY a live-fire/security area is not a fishing spot. An MPA advisory in the
# label ("stay W of MPA at 118 29.300") marks a REAL spot with a boundary to
# respect — Ship Rock, Bird Rock, Long Point and Windansea are all real, and
# excluding them would have silently dropped 12 pages. The advisory becomes
# content on the page.
NON_SPOT = re.compile(r"naval security zone", re.I)
ADVISORY = re.compile(r"\bMPA\b|big area|caution", re.I)

JURISDICTIONS = {
    "us-waters": ("US waters", ["socal-bight"]),
    "mexican-waters": ("Mexican waters", ["baja-pacific-north",
                                          "baja-pacific-south",
                                          "cortez-north", "cortez-south"]),
}

# Zones with no coordinates in the library (it stops at northern Baja) but real
# corpus depth. Without these the Baja fishery would have no pages at all.
CORPUS_ZONES = {
    "cedros-island": ("Cedros / San Benitos", "baja-pacific-north"),
    "guadalupe": ("Guadalupe", "baja-pacific-north"),
    "alijos-rocks": ("Alijos Rocks", "baja-pacific-south"),
    "bahia-magdalena-lopez-mateos": ("Magdalena Bay", "baja-pacific-south"),
    "cabo-san-lucas": ("Cabo San Lucas", "baja-pacific-south"),
    "bahia-de-los-angeles": ("Bahia de los Angeles", "cortez-north"),
    "loreto": ("Loreto", "cortez-south"),
    "la-paz": ("La Paz", "cortez-south"),
    "east-cape": ("East Cape", "cortez-south"),
}

# Which region a spot-lists section belongs to.
def bank_region(spot: dict) -> str:
    """US/Mexico for an offshore bank.

    The maritime boundary runs SW from the coastal border at ~32 32'N, so a
    bare latitude test mislabels banks that sit west and south of it. This
    approximates the line rather than pretending a single parallel is it.
    """
    boundary_lat = 32.5333 - 0.36 * (abs(spot["lon"]) - 117.124)
    return "socal-bight" if spot["lat"] > boundary_lat else "baja-pacific-north"


SECTION_REGION = [
    # Islas Los Coronados are Mexican territory ~8 nm off Tijuana — the
    # default-to-socal-bight fallback had them in US waters, which the map
    # made obvious and which contradicted locations/coronado-islands.md.
    (re.compile(r"punta banda|santo tomas|ensenada|san quintin|colonet|"
                r"northern baja|finger bank|coronado", re.I),
     "baja-pacific-north"),
    (re.compile(r".", re.I), "socal-bight"),
]

# Fixture: this script re-implements the scan that produced the plan's table.
# Two independent implementations must agree or one of them is wrong, and we
# want to know BEFORE reading 200 census rows.
# Verified 2026-08-24: Catalina and Cedros sit BELOW the plan's published
# 54/41 because that throwaway scan double-counted three species notes against
# their own evidence files (barracuda, bluefin-tuna, yellowtail all mention
# Catalina in both). Folding evidence into its parent is the correct rule and
# is what this script does, so the fixture carries the folded numbers and the
# plan's table is the stale one. Guadalupe (no evidence file yet) is unmoved,
# and both poison cases still read 2 and 1.
# Bands, not exact counts. The point of this check is that two independent
# scan implementations agree on the SHAPE of the answer — it caught a
# too-strict place matcher and the plan's own double-counted table. Exact
# equality would additionally fire on every legitimate corpus change the
# fleet makes, which is noise, not signal. The bands are tight enough that
# the bug class this exists to catch (105/150 scoring 54 on gear prose,
# Catalina scoring 0 on a heading mismatch) still blows them open.
FIXTURE = {"Catalina": (40, 70), "Cedros / San Benitos": (30, 55),
           "Guadalupe": (22, 45), "105 / 150": (0, 8),
           "Middle Grounds": (0, 5)}


# --------------------------------------------------------------- coordinates
def parse_spot_lists() -> list[dict]:
    spots, section = [], None
    for line in SPOT_LISTS.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^## (.+)$", line)
        if h:
            section = h.group(1).strip()
            continue
        m = re.match(r"^- (.+?) — (\d+) ([\d.]+) / (\d+) ([\d.]+)\s*$", line)
        if m and section:
            spots.append({
                "name": m.group(1).strip(),
                "lat": int(m.group(2)) + float(m.group(3)) / 60,
                "lon": -(int(m.group(4)) + float(m.group(5)) / 60),
                "section": section,
            })
    return spots


def nm(a: dict, b: dict) -> float:
    dlat = (a["lat"] - b["lat"]) * 60
    dlon = ((a["lon"] - b["lon"]) * 60
            * math.cos(math.radians((a["lat"] + b["lat"]) / 2)))
    return math.hypot(dlat, dlon)


def complete_linkage(items: list[dict], max_diam: float) -> list[list[dict]]:
    """Agglomerative clustering that REFUSES a merge exceeding max_diam.

    Single-linkage would chain: each spot within the threshold of the next,
    and the entire coast fuses into one cluster. Capping the diameter is what
    keeps 9 Mile Bank (54 nm from 14 Mile) out of its neighbour's zone.
    """
    clusters = [[it] for it in items]
    while True:
        best, bi, bj = None, -1, -1
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                diam = max(nm(a, b)
                           for a in clusters[i] + clusters[j]
                           for b in clusters[i] + clusters[j])
                if diam <= max_diam and (best is None or diam < best):
                    best, bi, bj = diam, i, j
        if best is None:
            return clusters
        clusters[bi] += clusters[bj]
        clusters.pop(bj)


def centre(cluster: list[dict]) -> dict:
    return {"lat": sum(s["lat"] for s in cluster) / len(cluster),
            "lon": sum(s["lon"] for s in cluster) / len(cluster)}


def name_cluster(cluster: list[dict]) -> str:
    """Name a bank cluster after its members, longest-known names first."""
    names = sorted((s["name"] for s in cluster),
                   key=lambda n: (n.isdigit(), len(n)))
    return " / ".join(names[:3]) + ("" if len(names) <= 3 else " …")


# ------------------------------------------------------------- corpus depth
def load_notes() -> dict[str, str]:
    """Knowledge notes, evidence folded into their parent, FM+backlinks off."""
    docs: dict[str, str] = {}
    for d in KNOWLEDGE_DIRS:
        for p in (ROOT / d).rglob("*.md"):
            if p.name == "README.md":
                continue
            t = p.read_text(encoding="utf-8", errors="replace")
            # Skip pages this ladder GENERATES. A zone page naming its own
            # spots would inflate the depth count with the census's own
            # output — "Middle Grounds" jumped 1 -> 2 the moment
            # locations/coronado-islands.md was written. Depth must measure
            # what the KNOWLEDGE notes say about a place.
            if re.search(r"^type:\s*(zone|region|area|jurisdiction|location)"
                         r"\s*$", t, re.M):
                continue
            if t.startswith("---"):
                e = t.find("\n---", 3)
                if e != -1:
                    t = t[e + 4:]
            a, b = (t.find("<!-- backlinks:start -->"),
                    t.find("<!-- backlinks:end -->"))
            if a != -1 and b != -1:
                t = t[:a] + t[b:]
            t = unicodedata.normalize("NFKD", t).encode("ascii",
                                                        "ignore").decode()
            key = str(p.relative_to(ROOT)).replace("/evidence/", "/")
            docs[key] = docs.get(key, "") + "\n" + t
    return docs


def anchored_number(n: str) -> str:
    """A numbered spot NEVER counts on the bare number.

    "105"/"150" scored 54 notes on line-test pounds and jig grams. A context
    anchor is required: "the 425", "425 Bank/Spot/Fathom", "181/182".
    """
    n = re.escape(n)
    return (rf"\bthe\s+{n}\b"
            rf"|\b{n}\s*(?:bank|spot|fathom|ridge|reef|hi(?:gh)?\s*spot|"
            rf"line|hole|kelp)\b"
            rf"|\b{n}\s*/\s*\d")


# Terms with a non-geographic sense in the fishery. These match CASE-SENSITIVELY
# and without plural flex: the corpus writes the spot as "Middle Grounds" and
# the gear term as "7:1 middle ground", so case is what separates them. Without
# this rule "Middle Grounds" scores 4 notes, none of them about the place.
AMBIGUOUS = {"Middle Ground", "Middle Grounds", "Rockpile", "Horseshoe",
             "East Cape", "The Slide", "Corner"}


def depth_regex(display: str) -> re.Pattern:
    parts, strict = [], False
    for token in [t.strip() for t in display.split("/")]:
        if not token:
            continue
        if token in AMBIGUOUS:
            parts.append(rf"\b{re.escape(token)}\b")
            strict = True
        elif re.fullmatch(r"\d+", token):
            parts.append(anchored_number(token))
        else:
            # Fold accents, and make the trailing plural optional: the corpus
            # writes both "the San Benitos" and "San Benito Island", and a
            # strict \bSan Benitos\b silently missed 10 notes.
            ascii_tok = unicodedata.normalize("NFKD", token).encode(
                "ascii", "ignore").decode()
            stem = ascii_tok[:-1] if ascii_tok.endswith("s") else ascii_tok
            parts.append(rf"\b{re.escape(stem)}s?\b")
    pattern = "|".join(parts) or r"(?!x)x"
    return re.compile(pattern) if strict else re.compile(pattern, re.I)


def depth_term(display: str) -> str:
    """The searchable place name inside a section heading.

    "Catalina Island — Front Side (W→E)" is a heading, not a phrase the corpus
    ever writes; counting it literally returned 0 notes for the single richest
    zone in the KB. Strip directional qualifiers after a dash and any
    parenthetical aside, then count the place itself.
    """
    core = re.split(r"\s+[—–-]\s+", display)[0]
    core = re.sub(r"\s*\([^)]*\)", "", core).strip()
    # Do NOT strip "artificial reefs" — that leaves the bare city name, and
    # "San Diego" scored 85 notes as a port and a place people live. A reef
    # complex is counted by its full name or not at all.
    return core or display


def depth_count(display: str, docs: dict[str, str]) -> int:
    rx = depth_regex(display)
    return sum(1 for t in docs.values() if rx.search(t))


def fixture_drift(docs: dict[str, str]) -> dict:
    out = {}
    for k, (lo, hi) in FIXTURE.items():
        got = depth_count(k, docs)
        if not lo <= got <= hi:
            out[k] = ((lo, hi), got)
    return out


def build_zones(spots: list[dict], docs: dict[str, str] | None = None):
    """The single source of truth for the ladder's rungs 4 and 5.

    Returns (zones, spot_rows, ar_series, non_spot, unassigned). The census
    formats it; Review Watch's map draws it. Two implementations of zoning is
    the bug class this project keeps hitting, so there is exactly one.
    """
    zones: list[dict] = []
    by_section: dict[str, list[dict]] = {}
    for s in spots:
        by_section.setdefault(s["section"], []).append(s)

    unassigned: list[tuple[str, str]] = []
    for section, members in by_section.items():
        if section.startswith(CATCHALL):
            continue                       # subdivided below
        if section in FILTER_SECTIONS:
            continue                       # merged into its parent below
        region = next(r for rx, r in SECTION_REGION if rx.search(section))
        extra = [m for filt, parent in FILTER_SECTIONS.items()
                 if parent == section for m in by_section.get(filt, [])]
        pool = members + extra

        if section in SECTION_SPLITS:
            claimed: set[str] = set()
            for display, names in SECTION_SPLITS[section]:
                part = [m for m in pool if m["name"] in names]
                claimed |= {m["name"] for m in part}
                if part:
                    zones.append({"display": display, "slug": slugify(display),
                                  "region": region, "spots": part,
                                  "src": "split"})
            # A member the split forgot is REPORTED, never dropped — the
            # coordinate-conservation assert would catch the loss, but this
            # names the cause.
            for m in pool:
                if m["name"] not in claimed:
                    unassigned.append((m["name"], section))
            continue

        zones.append({"display": section, "slug": slugify(section),
                      "region": region, "spots": pool, "src": "section"})

    banks = by_section.get(
        next((k for k in by_section if k.startswith(CATCHALL)), ""), [])
    orphans = []
    for cluster in complete_linkage(banks, MAX_ZONE_DIAMETER_NM):
        if len(cluster) == 1:
            orphans.append(cluster[0])
            continue
        display = name_cluster(cluster)
        zones.append({"display": display, "slug": slugify(display),
                      "region": bank_region(cluster[0]),
                      "spots": cluster, "src": "cluster"})
    # A lone bank joins the nearest zone it can actually be fished with;
    # only a genuinely isolated one earns a zone of its own.
    for o in orphans:
        near = min(((z, nm(o, centre(z["spots"]))) for z in zones if z["spots"]),
                   key=lambda t: t[1], default=(None, 1e9))
        if near[0] is not None and near[1] <= ORPHAN_ATTACH_NM:
            near[0]["spots"].append(o)
        else:
            zones.append({"display": o["name"], "slug": slugify(o["name"]),
                          "region": bank_region(o), "spots": [o],
                          "src": "isolated bank"})

    for slug, (display, region) in CORPUS_ZONES.items():
        if any(z["slug"] == slug for z in zones):
            continue
        zones.append({"display": display, "slug": slug, "region": region,
                      "spots": [], "src": "corpus"})

    if docs is not None:
        for z in zones:
            z["notes"] = depth_count(depth_term(z["display"]), docs)
    else:
        for z in zones:
            z["notes"] = 0

    # -- rung 5: spots ------------------------------------------------------
    spot_rows, ar_series, non_spot = [], {}, []
    for z in zones:
        for s in z["spots"]:
            if NON_SPOT.search(s["name"]):
                non_spot.append((s["name"], z["display"]))
                continue
            m = AR_SERIES.match(s["name"])
            if m:
                base = (m.group(1) or m.group(2)).strip()
                ar_series.setdefault(slugify(base), {"display": base,
                                                     "zone": z, "n": 0})
                ar_series[slugify(base)]["n"] += 1
                continue
            spot_rows.append({"slug": slugify(s["name"]), "display": s["name"],
                              "zone": z, "dist": nm(s, centre(z["spots"]))})


    return zones, spot_rows, ar_series, non_spot, unassigned


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="print the census; write nothing (the gate artifact)")
    args = ap.parse_args()

    spots = parse_spot_lists()
    docs = load_notes()

    drift = fixture_drift(docs)
    if drift:
        print("FIXTURE DRIFT — the two scan implementations disagree:",
              file=sys.stderr)
        for k, ((lo, hi), got) in drift.items():
            print(f"  {k}: expected {lo}-{hi}, this script says {got}",
                  file=sys.stderr)
        print("Refusing to emit a census built on a differently-wrong scan.\n"
              "Fix the implementation, or update FIXTURE in the same commit.",
              file=sys.stderr)
        return 2
    print(f"fixture OK ({len(FIXTURE)} anchors agree)\n")

    zones, spot_rows, ar_series, non_spot, unassigned = build_zones(spots, docs)

    # ---------------------------------------------------------------- census
    print("=" * 78)
    print("GEO CENSUS — every page this would create, and every stub it flags")
    print("=" * 78)
    print(f"\n## Rung 1 — jurisdiction ({len(JURISDICTIONS)})")
    for slug, (display, regs) in JURISDICTIONS.items():
        print(f"  locations/{slug}.md   {display}  <- covers {', '.join(regs)}")

    print("\n## Rung 2 — region (5, closed vocabulary, unchanged)")
    for r in ["socal-bight", "baja-pacific-north", "baja-pacific-south",
              "cortez-north", "cortez-south"]:
        j = "us-waters" if r == "socal-bight" else "mexican-waters"
        nz = sum(1 for z in zones if z["region"] == r)
        print(f"  locations/{r}.md   parent={j}   zones={nz}")

    print(f"\n## Rung 4 — zone ({len(zones)})")
    print(f"  {'page':<40} {'parent':<20} {'spots':>5} {'notes':>6}  origin")
    for z in sorted(zones, key=lambda z: (-len(z["spots"]), -z["notes"])):
        print(f"  locations/{z['slug']+'.md':<30} {z['region']:<20} "
              f"{len(z['spots']):>5} {z['notes']:>6}  {z['src']}")

    print(f"\n## Rung 5 — spot ({len(spot_rows)} individual"
          f" + {len(ar_series)} AR complex pages"
          f" = {len(spot_rows)+len(ar_series)})")
    far = [s for s in spot_rows if s["dist"] > MAX_ZONE_DIAMETER_NM]
    print(f"  {len(spot_rows)} spot pages assigned; "
          f"{len(far)} sit further than {MAX_ZONE_DIAMETER_NM:.0f} nm from "
          f"their zone centre (listed below)")
    for a in ar_series.values():
        print(f"  locations/{slugify(a['display'])+'.md':<32} "
              f"AR complex, {a['n']} waypoints in a coordinate table "
              f"<- {a['zone']['display']}")
    if far:
        print("\n  ! parent-distance outliers — check these before generating:")
        for s in sorted(far, key=lambda s: -s["dist"])[:15]:
            print(f"    {s['display']:<38} {s['dist']:>6.1f} nm from "
                  f"{s['zone']['display']}")

    if unassigned:
        print(f"\n## !! UNASSIGNED by a section split ({len(unassigned)}) — "
              f"these would be LOST")
        for name, section in unassigned:
            print(f"  {name:<52} (was in: {section})")
        print("  Fix: add each to a SECTION_SPLITS group, or remove the "
              "section from FILTER_SECTIONS.")

    if non_spot:
        print(f"\n## Not minted as pages — YOUR CALL ({len(non_spot)})")
        for name, zone in non_spot:
            print(f"  {name:<52} ({zone})")

    adv = [s for s in spot_rows if ADVISORY.search(s["display"])]
    if adv:
        print(f"\n## Minted, but carry an advisory to surface on the page "
              f"({len(adv)})")
        for s_ in adv[:12]:
            print(f"  {s_['display'][:70]}")
        if len(adv) > 12:
            print(f"  … and {len(adv) - 12} more")

    thin = [z for z in zones if z["notes"] < AREA_BAR_NOTES and not z["spots"]]
    if thin:
        print(f"\n## Flagged stubs — no coordinates and thin corpus ({len(thin)})")
        for z in thin:
            print(f"  {z['display']:<40} {z['notes']} notes")

    # ---- coordinate conservation -----------------------------------------
    # Every coordinate in the library must land on exactly one page: its own
    # spot page, or its complex page's table. This is the check that stops the
    # AR collapse or a slug fix silently dropping a waypoint.
    accounted = (len(spot_rows) + sum(a["n"] for a in ar_series.values())
                 + len(non_spot))
    if accounted != len(spots):
        print(f"\n!! COORDINATE LOSS: {len(spots)} spots in the library, "
              f"{accounted} accounted for "
              f"({len(spot_rows)} pages + "
              f"{sum(a['n'] for a in ar_series.values())} AR table rows + "
              f"{len(non_spot)} excluded)", file=sys.stderr)
        return 3
    print(f"\ncoordinate conservation OK: {len(spots)} spots = "
          f"{len(spot_rows)} pages + {sum(a['n'] for a in ar_series.values())}"
          f" AR table rows + {len(non_spot)} excluded")

    total = (len(JURISDICTIONS) + 5 + len(zones) + len(spot_rows)
             + len(ar_series))
    print(f"\n{'=' * 78}\nTOTAL PAGES: {total}"
          f"  (2 jurisdiction + 5 region + {len(zones)} zone"
          f" + {len(spot_rows) + len(ar_series)} spot)")
    print("=" * 78)

    if args.dry_run:
        print("\n--dry-run: nothing written.")
        return 0

    rows = []
    for slug in JURISDICTIONS:
        rows.append(f"| locations/{slug}.md | geo | pending |  | jurisdiction |")
    for r in ["socal-bight", "baja-pacific-north", "baja-pacific-south",
              "cortez-north", "cortez-south"]:
        rows.append(f"| locations/{r}.md | geo | pending |  | region |")
    for z in sorted(zones, key=lambda z: -len(z["spots"])):
        rows.append(f"| locations/{z['slug']}.md | geo | pending |  | "
                    f"zone: {len(z['spots'])} spots, {z['notes']} notes |")
    for a in ar_series.values():
        rows.append(f"| locations/{slugify(a['display'])}.md | gazetteer | "
                    f"pending |  | AR complex: {a['n']} waypoints |")
    for s in sorted(spot_rows, key=lambda s: s["slug"]):
        rows.append(f"| locations/{s['slug']}.md | gazetteer | pending |  | "
                    f"spot in {s['zone']['display']} |")

    wl = WORKLIST.read_text(encoding="utf-8")
    fresh = [r for r in rows if f"| {r.split('|')[1].strip()} |" not in wl]
    wl = wl.replace(WL_END, "\n".join(fresh) + "\n" + WL_END)
    WORKLIST.write_text(wl, encoding="utf-8")
    print(f"\nappended {len(fresh)} row(s) to the worklist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
