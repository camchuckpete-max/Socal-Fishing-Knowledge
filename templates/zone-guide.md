# Template: zone guide (`type: zone-guide`, lives in `species/`)

The species×zone targeting guide (pilot feedback, 2026-08-24 — Nate's ask):
"what a trip to this zone looks like" for one species, at **region/zone
level, never spot level** (Cameron: "targeting yellowtail, Bahía de Los
Ángeles" — a zone, not a waypoint). This is the trip-story layer the router
can't hold: the router's situations table says which technique fits which
read; the zone guide says how the DAY actually runs here.

Filename: `species/<species>-<zone>.md` (e.g.
`species/yellowtail-coronado-islands.md`). The species router links it from
`## Zone guides`; the guide links back to the router, the techniques it
names, and the zone's `locations/` page.

## Front matter

```yaml
---
type: zone-guide
tags: [yellowtail, coronado-islands, ...]
sources: [<video_id>, ..., cameron, nate]
confidence: high
regions: [socal-bight]          # gated
waters: [island]                # gated
layout: v2
species: yellowtail.md          # relative link to the router; MUST resolve
zone: ../locations/coronado-islands.md   # relative link when a page exists,
                                         # else the zone name as text
season_window: mar-jun peak     # `unknown` legal
run: ~13 nm from San Diego bay entrance  # `unknown` legal
---
```

## Skeleton (canonical order — extras allowed between)

```
# Targeting <species> — <zone>

<Lead: what a trip here looks like, one breath — the zone's character for
this species.>

## The program
The day, start to finish, as locals actually run it: the search pattern
(e.g. troll pink/purple Halco 190s as the fish-finder, do 8s around the
islands, work the middle grounds), when to commit (anchor/drift/bait), when
to switch presentations, when to leave. Numbered where order matters.

## Reading the day
Zone-specific conditions logic: the tide/current/light windows that matter
HERE, what good and bad water look like here, the local bite pattern
(seeing-not-biting cycles, gray-light windows). Links conditions/ notes.

## Rigs & gear for this zone
What to actually rig for this zone's grade and structure — classes + the
zone-specific numbers (line classes, jig sizes/colors, hook sizes),
linking technique/lure/rigging notes for execution.

## Differs from nearby zones
The contrast that makes the guide worth reading: how this trip differs from
the adjacent zones' trips for the same species (LJ vs the Coronados), one
bullet per contrast.

## Evidence
Only when observations exist.

## Linked from   (machine-generated)
```

Rules: corpus + registered sources only, gaps flagged; all style-guide v2.1
rules apply (no filler, mechanism or gap, scope, presence ≠ catchability,
single observation → evidence). A zone with fishery relevance but no corpus
program yet gets a stub guide with flagged gaps OR a flagged stub row in the
router's `## Zone guides` — never silence.
