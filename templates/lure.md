# Template: lure note (`type: lure`, STANDARD tier)

Implementation layer: per-lure or per-class specs, rigging, running
parameters. Decision logic (WHEN to pull this lure vs another) lives at
species/decision level and links here (CLAUDE.md, unchanged).

## Front matter

```yaml
---
type: lure
tags: [mad-mac, trolling, ...]
sources: [<video_id>, ..., cameron]
confidence: high
regions: [socal-bight, ...]
waters: [open-ocean, bank, ...]
layout: v2
lure_class: bullet-jet trolling lure
weights: 9oz / 12oz / 16oz
depth_band: surface wake to 6 ft
run_speed: 9-14 kt                 # `unknown` where the corpus is silent
---
```

## Skeleton (canonical order — extras allowed between)

```
# <Lure / class name>

<Lead: what it is and the job it does.>

## Specs
The parameter block: sizes, weights, hooks, rigging, running speed/depth —
tables before prose. Conflicting parameter bands stay side-by-side with the
overlap and the decision frame stated (the mad-mac speed-band treatment).

<free sections: rigging detail, how to run it, colour selection, model
comparison — as needed.>

## When to choose it
Short list routing BACK to the species/decision notes that pull this lure —
one line per situation with the link. No species patterns restated here.

## Evidence
One line linking evidence/<note>.md (only when observations exist).

## Linked from   (machine-generated)
```
