# Template: area page (`type: area`)

Third rung, and the only OPTIONAL one: an area page exists where the corpus can
actually say something about ports, bait and range (>= 6 differentiated
mentions, or an existing page, or >= 3 harvested spots naming it). Where it
cannot, the region links its zones directly. Answers one question: *I am
launching here — what can I reach, and what do I need before I go?*

## Front matter

```yaml
---
type: area
tags: [<area>, ports, launches]
sources: [<video_id>, cameron]
confidence: high|medium|low
regions: [<parent region term>]
waters: [<waters reachable from here>]
layout: v2
parent: [<Region>](<region>.md)
ports: [<port>, <port>]
range_nm: <typical day-trip radius, or unknown>
---
```

## Skeleton (canonical order — extras allowed between)

```


# <Area name>

**The launch rung, and it only exists where it earns its keep** — an area page
is created when the corpus can actually say something about ports, bait and
range. Where it cannot, the region links its zones directly.

Answers one question: *I am launching here — what can I reach and what do I need
before I go?*

## Ports & launches

Ramps, harbours, hoists, parking and fuel where the corpus knows them.

## Bait

Where bait comes from here — barges, receivers, making your own — and what is
typically available. Live bait availability is a real constraint on which
programs are possible, so it belongs beside the ports rather than in tactics.

## What's in range

Zones and spots by distance band from this area, so range shapes the plan.
Links each zone page.

## Zones

The child zones this area reaches, one line each.

## Evidence

One line linking `locations/evidence/<note>.md`.

## Linked from   (machine-generated)
```
