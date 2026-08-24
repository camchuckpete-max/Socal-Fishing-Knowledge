# Template: zone page (`type: zone`)

Fourth rung, and the load-bearing one — every spot below re-parents if a zone
is drawn wrong. **A zone is a run grouping**: the set of spots realistically
fished in one trip, named the way the fishery names them.

Zones are derived from COORDINATES, not mention counts (Cameron, 2026-08-24):
the `##` sections of `sources/spot-lists.md` are the skeleton, and constrained
coordinate clustering subdivides the offshore-banks catch-all. Corpus depth
decides how much a zone page can SAY, never whether it exists.

## Front matter

```yaml
---
type: zone
tags: [<zone>, <structure tags>]
sources: [<video_id>, cameron]
confidence: high|medium|low
regions: [<parent region term>]
waters: [<island|bank|nearshore-coast|bay-harbor|open-ocean>]
layout: v2
parent: <parent>.md
structure_type: <island | offshore bank | coastal reef | canyon | artificial reef>
depth_band: <e.g. 15-60 fathoms, or unknown>
distance_nm: <from the nearest common port, or unknown>
coordinates: <charted/public centre position, or omit>
---
```

## Skeleton (canonical order — extras allowed between)

```


# <Zone display name>

**A zone is a run grouping** — the set of spots you would realistically fish in
one trip, named the way the fishery names them. The lead says what this zone is
and why anyone points a boat at it.

A zone page exists when it HAS SPOTS (a `##` section of the spot library, or a
constrained coordinate cluster) or when the corpus carries it. Depth of content
varies; existence does not depend on it — a real zone with a thin corpus is a
real page with flagged gaps.

## Getting there

Run from the usual ports, crossing character, what the transit itself demands
(sea state, fuel, timing). Zone-wide access and legal notes that are facts about
THIS place — Navy closures, MPA boundaries, restricted areas — live here, not on
the jurisdiction page.

## Structure & bathymetry

What the bottom does: ridges, high spots, drop-offs, kelp, canyon edges, the
depth bands that matter and why. This is the part that explains the fishing.

## What's there

Species by season, each linking its router:

| species | season | what this zone does for them |
| --- | --- | --- |
| [<species>](../species/<species>.md) | <months> | <why they are here> |

## How it fishes

The zone's program at zone level — current, tide, light, where you start and how
you move. Trip-level species detail belongs in a
[zone guide](../species/<species>-<zone>.md); per-spot depth belongs on the spot
pages. Link both rather than absorbing them.

## Spots

The child spot pages, with a one-line character note each. Named sub-spots that
have not earned their own page are lines inside their spot page, not here.

## Evidence

One line linking `locations/evidence/<note>.md`.

## Linked from   (machine-generated)
```
