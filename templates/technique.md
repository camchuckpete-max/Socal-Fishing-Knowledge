# Template: technique note (`type: technique`, STANDARD tier)

Technique notes own execution ONLY — mechanics, retrieves, gear-class detail,
common failures — plus the short "reach for this when" list. They never
restate species patterns; the generated `## Linked from` plus that list is
the reverse map (CLAUDE.md, unchanged).

## Front matter

```yaml
---
type: technique
tags: [surface-iron, ...]
sources: [<video_id>, ...]
confidence: high
regions: [socal-bight, ...]
waters: [island, nearshore-coast, ...]
layout: v2
gear_classes: [jig-stick]
depth_band: surface to 2 fathoms
retrieve_speed: slow-medium, steady   # `unknown` if the corpus never says
---
```

## Skeleton (canonical order — extras allowed between)

```
# <Technique name>

<Lead: what the method is and the one-line case for it.>

## Reach for this when
Short bullet list of the situations that call for it.

<free sections: mechanics, the cast, retrieve & cadence, size/colour
selection, variations — whatever the method needs, in whatever order.
Source-named headings are not allowed: merge a new voice's material into the
section where it belongs, cited; disagreements go to a Doctrine & conflicts
section.>

## Gear class
Class terms, linking tackle/gear-classes.md, with the WHY (e.g. why a
high-ratio reel is wrong here).

## Common failures
What goes wrong and how to tell. Every technique note has this section even
if it starts as a single flagged gap.

## Evidence
One line linking evidence/<note>.md (only when observations exist).

## Linked from   (machine-generated)
```
