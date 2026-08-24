# Template: species technique page (`type: species-technique`)

The middle rung Cameron asked for (2026-08-24): "a technique called bluefin
tuna - trolling, yellowtail - surface iron fishing". One species x one
technique, so the species router stays a router and the technique note stays
universal — "it makes where the species pages aren't carrying the full weight
of different techniques, the techniques pages aren't trying to explain every
variation of each technique for every species."

Filename: `species/<species>-<technique>.md`; a zone variant is
`species/<species>-<technique>-<zone>.md` and exists ONLY where the technique
itself differs there — **"if it's just using heavier gear it shouldn't have its
own article"** (Cameron). Earned when the parent notes hold >= 2 distinct cited
execution parameters specific to the pairing.

## Front matter

```yaml
---
type: species-technique
tags: [<species>, <technique>, <region-ish tags>]
sources: [<video_id>, cameron]
confidence: high|medium|low
regions: [<from locations/regions.md>]
waters: [<from locations/regions.md>]
layout: v2
species: <species>.md
technique: ../techniques/<technique>.md
zone: ../locations/<zone>.md     # OPTIONAL — zone variants only
gear_classes: [<class>, <class>]
conditions_window: <the conditions that make this the call, or unknown>
---
```

## Skeleton (canonical order — extras allowed between)

```


# <Species> — <technique>

**One species, one technique.** The lead says in two or three sentences what
this program is and when an angler would reach for it, so the page answers its
own question before the reader scrolls.

## When this is the call

The decision layer. Conditions, season, water state, what the fish are doing —
the things that make THIS pairing right rather than the species' other options.
Links back to the router's Situations → techniques row. Never restates the
general technique's "Reach for this when": that is about the method in general,
this is about the method *for this fish*.

## How <species> changes the execution

The mechanics that differ because of this species: retrieve, depth, speed, bite
handling, hookset, how the fish tells you it is there. Parameters carry cites.
This is the section that justifies the page existing — if it can only be filled
with general mechanics, the page should not exist and the content belongs in the
router row.

## Rigs & gear

Class terms, linking [gear classes](../tackle/gear-classes.md). Specific line
classes, weights and hook sizes with their cites. Profile resolution stays a
lookup.

## Differs from the general method

The explicit delta list against [the technique note](../techniques/<technique>.md)
— the reader who already knows the method reads only this. A bullet that merely
restates the general method is a defect, not content; the cluster-consistency
phase re-checks these against the parent technique whenever it changes.

## Evidence

One line linking `<folder>/evidence/<note>.md`.

## Linked from   (machine-generated)
```
