---
type: location
tags: [regions, vocabulary, gating, day-plan, baja, socal]
sources: [cameron]
confidence: high
regions: [socal, baja]
waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]
---

# Regions & Waters — the gating vocabulary

**The closed vocabulary every note tags itself with, so a day plan can never
offer you a fish or a technique that doesn't exist where you're going.**

This note is to region what
[gear classes](../tackle/gear-classes.md) is to tackle: the controlled list
that makes resolution a lookup instead of a judgment call.

## Why this exists

The knowledgebase covers two fisheries that share a coastline and almost
nothing else. Cabrilla live in the Sea of Cortez; calico bass live in both
SoCal and Baja; spotted bay bass live in SoCal bays. Before these fields
existed, nothing in the KB could tell those three cases apart. Notes carried
a `baja` **tag**, but that tag meant "this note contains Baja content" — not
"this fish only lives in Baja" — so it over-selected (nine dual-region
species carried it) and under-selected (thirty notes with substantial Baja
content didn't). `socal` appeared as a tag exactly once in the whole
repository.

The concrete failure that motivated this: a day plan for a Mission Bay jetty
could route to [cabrilla](../species/cabrilla.md), whose situation table opens
with "low light, tight to shoreline structure → jerkbaits, cast tight to the
rock." That reads perfectly for a SoCal jetty at dawn. The fish is 400 miles
away.

## `regions` — the safety gate

**Two terms, deliberately.** A coarse gate is one you cannot get subtly wrong,
and this is the field that prevents the failure above.

| term | covers |
| --- | --- |
| `socal` | The Southern California Bight — Point Conception south to the border, including the Channel Islands, Catalina, San Clemente, the offshore banks, and the outer banks (Tanner, Cortez). |
| `baja` | Mexican waters — the Pacific side from Ensenada south, and the whole Sea of Cortez. |

A note lists **every region it applies to**. "Only in" needs no separate
field — it is set membership:

```yaml
regions: [baja]           # species/cabrilla.md — excluded from a socal trip
regions: [socal, baja]    # species/calico-bass.md — survives either filter
regions: [socal]          # locations/bays-and-harbors.md
```

## `subregions` — trip-planning grain

Optional, and never the gate. Use it when a note's content really is
specific to one place; omit it when the note applies region-wide.

| term | covers |
| --- | --- |
| `bight-coast` | Mainland coast, Point Conception to the border |
| `channel-islands` | Santa Cruz, Santa Rosa, San Miguel, Anacapa, Santa Barbara Island |
| `catalina` | Santa Catalina Island |
| `san-clemente` | San Clemente Island and its ridges |
| `coronados` | Coronado Islands |
| `offshore-banks` | The nearer SD/LA banks — 9 Mile, 14 Mile, 43, 302, 371 |
| `outer-banks` | Tanner and Cortez — overnight-run offshore high spots |
| `northern-baja` | The border south to Punta Banda |
| `ensenada` | Ensenada and its immediate grounds |
| `baja-pacific` | Pacific-side Baja below Ensenada — Colonet, San Quintín, Cedros, San Benito, Guadalupe, Alijos, Mag Bay |
| `sea-of-cortez` | The Cortez side generally, where a note isn't specific to one bay |
| `bola` | Bahía de los Ángeles |
| `san-felipe` | San Felipe and the northern Midriff — the mothership panga fishery |
| `loreto` | Loreto and Puerto Escondido — a different species mix from BOLA, ~250 mi south |
| `cabo` | Cabo San Lucas and the East Cape |

**BOLA, San Felipe, and Loreto are three different places.** They get
separate terms because their seasons and species differ, and because a
mothership trip out of San Felipe is not a panga day out of Bahía. A video
titled "Bahía de los Ángeles" that opens "aboard the Tony Reyes out of San
Felipe" is a San Felipe video.

## `waters` — the structure axis

What kind of water the note applies to. This is the axis `regions` cannot
cover: it stops a Cortez Bank tactic surfacing for a bay trip, and both are
`socal`.

| term | covers |
| --- | --- |
| `bay-harbor` | Inside bays and harbours — San Diego Bay, Mission Bay, Alamitos, Newport, Huntington Harbour |
| `nearshore-coast` | The coastal strip — kelp lines, breakwalls, jetties, riprap, coastal reef, surf-adjacent structure |
| `island` | Island shorelines, boiler rocks, island ridges and their kelp |
| `bank` | Offshore high spots and hard bottom fished from a boat over structure |
| `open-ocean` | Blue water with no bottom relationship — paddies, foamers, the troll, the DSL |

A note may list several. A species that lives on the coast and at the islands
gets `[nearshore-coast, island]`.

## How a plan uses these

[The day-plan protocol](../planning/day-plan-protocol.md) derives the day's
`{regions, waters}` envelope from the launch point and the boat's range, then
**filters the species and technique notes to those that match before routing.**
A note that does not match is never offered. If nothing in the envelope fits
the conditions, the plan says so rather than substituting something
out-of-region.

## Rules

- **Every** note of type `species`, `technique`, `lure`, `rig`, `location`,
  `seasonal`, or `bait` carries `regions` and `waters`.
  `scripts/link-maintenance.py` exits nonzero if one is missing or uses a term
  that isn't on these lists — so the backfill can't rot.
- Terms are **closed**. Adding one means editing this note first.
- A Baja limit differing from a CDFW limit is **two jurisdictions, not a
  conflict** — see [regulatory claims](../sources/regulatory-claims.md).
- These fields describe **where the knowledge applies**, not where the video
  was filmed. A Cabo-filmed video teaching a universal knot is `[socal, baja]`.

<!-- backlinks:start -->
## Linked from

- [Day-Plan Protocol](../planning/day-plan-protocol.md)
<!-- backlinks:end -->
