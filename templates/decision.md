# Template: decision spin-out (`type: decision`)

A species router's Situations → techniques table that outgrew its section —
spun out into `species/` (never `techniques/`), with the router keeping a
summary + link (CLAUDE.md, unchanged). `species/bluefin-trolling.md` is the
canonical example.

## Front matter

```yaml
---
type: decision
tags: [bluefin, trolling, ...]
sources: [<video_id>, ..., cameron]
confidence: high
regions: [socal-bight, ...]
waters: [open-ocean, ...]
layout: v2
---
```

## Skeleton

```
# <Decision domain>

<Lead: what decision this note makes and for whom.>

## Situations → techniques
The full decision table (same format as a species router row: conditions →
ranked choices → gear class → links; footnoted conditions).

<free sections: the mechanism behind the branch points, doctrine conflicts
with decision frames — as needed.>

## Evidence
Only when observations exist.

## Linked from   (machine-generated)
```
