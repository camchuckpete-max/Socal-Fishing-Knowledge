# Template: SPOT page (`type: location`, STANDARD tier)

The bottom rung of the gazetteer (RS-wiki location-page model, Cameron
2026-08-23). The full ladder is jurisdiction → region → area → zone → **spot**,
one type per rung since amendment v2.2 — a zone is `type: zone`
(`templates/zone.md`), not this template. This page is an infobox and a
species-by-season "what's there" table linking the species routers. Universal
pages cover publicly-known/charted spots; **personal waypoints stay in
`profiles/`** — the coordinates rule is "no PERSONAL coordinates", charted
public positions are fine.

## Front matter

```yaml
---
type: location
tags: [rockpile, coronados, ...]
sources: [<video_id>, ..., cameron]
confidence: high
regions: [socal-bight]
waters: [island]
layout: v2
parent: coronado-islands.md         # relative path to the ZONE; MUST resolve.
                                    # Renamed from parent_zone in v2.2 so one
                                    # field carries the whole ladder.
structure_type: high spot / rocky ridge
depth_band: 12-40 fathoms
distance_nm: 18 nm from San Diego bay entrance
coordinates: 32°24.9'N 117°15.7'W   # optional; charted/public only
---
```

## Skeleton (canonical order — extras allowed between)

```
# <Spot / zone name>

<Lead: what and where it is, in one breath.>

## Getting there
Transit, range and sea-state considerations, launch points.

## Structure & bathymetry
What the spot IS underwater — the reason it holds fish.

## What's there
Species-by-season table, each species linking its router:
| species | season | what the spot does for them |

## How it fishes
Conditions behavior at this spot: current, wind, tide, the read.

## Evidence
One line linking evidence/<note>.md (only when observations exist).

## Linked from   (machine-generated)
```

**Every spot in `sources/spot-lists.md` gets a page** (Cameron, 2026-08-24) —
"even if it's just: this spot is at these coordinates and is a member of this
zone." A minimum spot page is legitimate: infobox, a lead naming what it is and
its zone, and flagged gaps where the corpus is silent. The existence bar does
not apply to this rung.

ONE exception: numbered artificial-reef series (Oceanside AR 1A–2L, Carlsbad
AR 1–12, Pacific Beach AR, Pendleton AR, International Reef A–F) collapse to a
single complex page carrying a coordinate TABLE of all its waypoints — a
numbered waypoint has no fishing identity of its own, and `spot-lists.md`
already treats the series as one pixel. Every coordinate stays published.

A zone/complex page is now its own type — see `templates/zone.md`.
