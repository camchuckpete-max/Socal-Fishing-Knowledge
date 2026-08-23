# Template: location / spot page (`type: location`, STANDARD tier)

The gazetteer layer (RS-wiki location-page model, Cameron 2026-08-23):
containment hierarchy region → zone/complex → named spot, an infobox, and a
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
parent_zone: coronado-islands.md    # relative path; MUST resolve; omit on a
                                    # top-level zone
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

A zone/complex page (Catalina, the Coronados) uses the same skeleton with its
children linked from `## What's there` or a short child list in the lead.
