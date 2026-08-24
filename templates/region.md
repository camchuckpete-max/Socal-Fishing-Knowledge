# Template: region page (`type: region`)

Second rung. The five terms are the closed vocabulary in
`locations/regions.md` — this template is the PAGE for one of them, not a new
axis. Carries the region's character and the shape of its year, enough that an
angler who has never fished it knows what they are walking into before picking
a zone.

## Front matter

```yaml
---
type: region
tags: [<region>, <shape tags>]
sources: [<video_id>, cameron]
confidence: high|medium|low
regions: [<this region term from locations/regions.md>]
waters: [<the waters this region actually offers>]
layout: v2
parent: [<US | Mexican> waters](<jurisdiction>.md)
season_peak: [<months>]
---
```

## Skeleton (canonical order — extras allowed between)

```


# <Region display name>

**The character rung.** What makes this stretch of ocean different from the one
next door, and how its year runs — enough that an angler who has never fished it
knows roughly what they are walking into before they pick a zone.

## The fishery

What this region is: its water, its structure, the species mix it actually
offers, what it is known for. Boundaries are the ones in
[regions & waters](regions.md) — a real, checkable line, not a vibe.

## Season shape

How the year runs here, linking the `seasonal/` notes. The pattern layer, not
current intel.

## Zones

The child zones, generated or hand-listed with a one-line character note each.
A zone the corpus cannot yet support carries a `⚠ Flagged stub` line rather than
silence — silence reads as "nothing there."

## Access & range

How anglers reach this region — ports, crossings, typical run distances,
what a day trip versus a multi-day covers. Paperwork lives on the jurisdiction
page above; this is about distance and access.

## Evidence

One line linking `locations/evidence/<note>.md`.

## Linked from   (machine-generated)
```
