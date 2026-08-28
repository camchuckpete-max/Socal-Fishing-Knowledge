---
type: location
tags: [regions, vocabulary, gating, day-plan, baja, socal]
sources: [cameron]
confidence: high
regions: [socal-bight, baja-pacific-north, baja-pacific-south, cortez-north, cortez-south]
waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]
layout: v2
parent: unknown
structure_type: unknown — this note defines the region/waters vocabulary itself rather than sitting on one structure; see Structure & bathymetry below
depth_band: unknown — a fixed reference vocabulary, not a depth-banded spot
distance_nm: unknown — universal reference list, not measured from one launch point
---

# Regions & Waters — the gating vocabulary

**The closed vocabulary every note tags itself with, so a day plan can never
offer a fish or a technique that doesn't exist where the angler is going.**
This note is to region what [gear classes](../tackle/gear-classes.md) is to
tackle: the controlled list that makes resolution a lookup instead of a
judgment call. Two axes gate every applicable note: `regions` (geography) and
`waters` (structure type).

## Why this exists

The knowledgebase covers fisheries that share a coastline and not much else —
cabrilla live in the Sea of Cortez, calico bass run from the Bight down the
Pacific side of Baja, spotted bay bass live in SoCal bays. Before these fields
existed, nothing in the KB distinguished those cases: notes carried a `baja`
tag that meant "this note contains Baja content," not "this fish only lives in
Baja," so it over-selected (nine dual-region species carried it) and
under-selected (thirty notes with substantial Baja content didn't); `socal`
appeared as a tag exactly once in the whole repository (cameron).

The concrete failure that motivated the fix: a day plan for a Mission Bay
jetty could route to [cabrilla](../species/cabrilla.md), whose situation table
opens with "low light, tight to shoreline structure → jerkbaits, cast tight to
the rock" — a read that fits a SoCal jetty at dawn perfectly. The fish is 400
miles away (cameron).

## Getting there

This is a universal vocabulary note, not a single spot — it carries no launch
point or transit leg of its own. Getting-there detail lives on the zone and
spot pages this vocabulary gates, e.g.
[Southern California Bight](socal-bight.md) and
[Cortez North](cortez-north.md).

⚠ Flagged gap — no corpus source: transit/launch detail (not applicable — this
note defines the region/waters vocabulary, not a spot to fish).

## Structure & bathymetry

This entry is the vocabulary itself, not one structure — each zone/spot's own
bathymetry lives on its own page.

### `regions` — five broad areas

Species and techniques are assigned at this broad-area level, not per spot
(cameron); finer grain is deliberately not modeled because a spot-level split
would mean re-deciding every note against boundaries nobody fishes by — a
finer tier can be added later if one is actually needed. The north/south
split is the Baja California / Baja California Sur state line at 28°N — a
checkable boundary, not a judgment call.

| term | covers |
| --- | --- |
| `socal-bight` | The Southern California Bight — Point Conception to the US border, including the Channel Islands, Catalina, San Clemente, the nearshore banks and the outer banks (Tanner, Cortez Bank) |
| `baja-pacific-north` | Pacific side, US border to 28°N — Ensenada, Punta Banda, Santo Tomás, Colonet, San Quintín, Cedros, the San Benitos, Guadalupe |
| `baja-pacific-south` | Pacific side below 28°N — Bahía Asunción, Magdalena Bay, Alijos Rocks, round to Cabo San Lucas |
| `cortez-north` | Sea of Cortez above 28°N — San Felipe, Gonzaga, Bahía de los Ángeles, the Midriff islands |
| `cortez-south` | Sea of Cortez below 28°N — Loreto, La Paz, the East Cape |

A note lists every region it applies to; "only in" needs no separate field —
it is set membership:

```yaml
regions: [cortez-north, cortez-south]              # species/cabrilla.md
regions: [socal-bight, baja-pacific-north]         # species/white-seabass.md
regions: [socal-bight]                             # species/spotted-bay-bass.md
```

The Cortez is split from the Pacific rather than lumped as "Baja" because they
are different oceans as far as the fish are concerned — cabrilla and pargo are
Cortez, white seabass and calico run the Pacific side; a single `baja` term
would have let a Cedros trip offer a Sea-of-Cortez program (cameron).

### `waters` — the structure axis

The axis `regions` cannot cover: it stops an offshore-bank tactic surfacing
for a bay trip, and both can be `socal-bight`. A note may list several waters
terms — a species that lives on the coast and at the islands gets
`[nearshore-coast, island]`.

| term | covers |
| --- | --- |
| `bay-harbor` | Inside bays and harbours — San Diego Bay, Mission Bay, Alamitos, Newport, Huntington Harbour |
| `nearshore-coast` | The coastal strip — kelp lines, breakwalls, jetties, riprap, coastal reef |
| `island` | Island shorelines, boiler rocks, island ridges and their kelp |
| `bank` | Offshore high spots and hard bottom fished over structure |
| `open-ocean` | Blue water with no bottom relationship — paddies, foamers, the troll, the DSL |

## What's there

⚠ Flagged gap — no corpus source: not applicable — this note defines the
gating vocabulary, not species presence at a spot. Species-by-region
assignment lives in each species note's `regions` field; see the species
routers.

## How it fishes

### How a plan uses these

[The day-plan protocol](../planning/day-plan-protocol.md) derives the day's
`{regions, waters}` envelope from the launch point and the boat's range, then
filters the species and technique notes to those that match before routing. A
note that does not match is never offered; if nothing in the envelope fits the
conditions, the plan says so rather than substituting something out-of-region.

### Rules

- Every note of type `species`, `technique`, `lure`, `rig`, `location`,
  `seasonal`, `bait`, or `decision` carries `regions` and `waters`;
  `scripts/link-maintenance.py` exits nonzero if one is missing or uses a term
  off these lists, so the backfill can't rot.
- Terms are closed — adding one means editing this note first.
- A Baja limit differing from a CDFW limit is two jurisdictions, not a
  conflict — see [regulatory claims](../sources/regulatory-claims.md).
- These fields describe where the knowledge applies, not where the video was
  filmed — a Cabo-filmed video teaching a universal knot applies everywhere.

<!-- backlinks:start -->
## Linked from

- [Baja Pacific — North](baja-pacific-north.md)
- [Baja Pacific — South](baja-pacific-south.md)
- [Coronado Islands](coronado-islands.md)
- [Cortez North](cortez-north.md)
- [Cortez South](cortez-south.md)
- [Davis Knoll / San Miguel Gap / Rodriguez Seamount](davis-knoll-san-miguel-gap-rodriguez-seamount.md)
- [Day-Plan Protocol](../planning/day-plan-protocol.md)
- [E. Butterfly / San Salvador Knoll](e-butterfly-san-salvador-knoll.md)
- [Mexican waters](mexican-waters.md)
- [North 9 Mile Bank / 178](north-9-mile-bank-178.md)
- [Source Registry](../sources/source-registry.md)
- [Southern California Bight](socal-bight.md)
<!-- backlinks:end -->
