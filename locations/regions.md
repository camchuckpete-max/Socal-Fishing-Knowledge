---
type: location
tags: [regions, vocabulary, gating, day-plan, baja, socal]
sources: [cameron]
confidence: high
regions: [socal-bight, baja-pacific-north, baja-pacific-south, cortez-north, cortez-south]
waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]
---

# Regions & Waters — the gating vocabulary

**The closed vocabulary every note tags itself with, so a day plan can never
offer you a fish or a technique that doesn't exist where you're going.**

This note is to region what
[gear classes](../tackle/gear-classes.md) is to tackle: the controlled list
that makes resolution a lookup instead of a judgment call.

## Why this exists

The knowledgebase covers fisheries that share a coastline and not much else.
Cabrilla live in the Sea of Cortez; calico bass live from the Bight down the
Pacific side of Baja; spotted bay bass live in SoCal bays. Before these
fields existed, nothing in the KB could tell those cases apart. Notes carried
a `baja` **tag**, but it meant "this note contains Baja content" — not "this
fish only lives in Baja" — so it over-selected (nine dual-region species
carried it) and under-selected (thirty notes with substantial Baja content
didn't). `socal` appeared as a tag exactly once in the whole repository.

The concrete failure that motivated this: a day plan for a Mission Bay jetty
could route to [cabrilla](../species/cabrilla.md), whose situation table opens
with "low light, tight to shoreline structure → jerkbaits, cast tight to the
rock." That reads perfectly for a SoCal jetty at dawn. The fish is 400 miles
away.

## `regions` — five broad areas

**Broad areas, not spots** (Cameron, 2026-08-17). Species and techniques are
assigned at this level. Spot-level grain is deliberately *not* modelled — a
finer tier can be added later if something actually needs it, and adding it
prematurely would mean re-deciding every note against boundaries nobody
fishes by.

The north/south split is the **Baja California / Baja California Sur state
line at 28°N** — a real, checkable boundary rather than a vibe.

| term | covers |
| --- | --- |
| `socal-bight` | The Southern California Bight — Point Conception to the US border, including the Channel Islands, Catalina, San Clemente, the nearshore banks and the outer banks (Tanner, Cortez Bank) |
| `baja-pacific-north` | Pacific side, US border to 28°N — Ensenada, Punta Banda, Santo Tomás, Colonet, San Quintín, Cedros, the San Benitos, Guadalupe |
| `baja-pacific-south` | Pacific side below 28°N — Bahía Asunción, Magdalena Bay, Alijos Rocks, round to Cabo San Lucas |
| `cortez-north` | Sea of Cortez above 28°N — San Felipe, Gonzaga, Bahía de los Ángeles, the Midriff islands |
| `cortez-south` | Sea of Cortez below 28°N — Loreto, La Paz, the East Cape |

A note lists **every region it applies to**. "Only in" needs no separate
field — it is set membership:

```yaml
regions: [cortez-north, cortez-south]              # species/cabrilla.md
regions: [socal-bight, baja-pacific-north]         # species/white-seabass.md
regions: [socal-bight]                             # species/spotted-bay-bass.md
```

**Why the Cortez is split from the Pacific rather than lumped as "Baja":**
they are different oceans as far as the fish are concerned. Cabrilla and
pargo are Cortez; white seabass and calico run the Pacific side. A single
`baja` term would have let a Cedros trip offer a Sea-of-Cortez program.

## `waters` — the structure axis

What kind of water the note applies to. This is the axis `regions` cannot
cover: it stops an offshore-bank tactic surfacing for a bay trip, and both
can be `socal-bight`.

| term | covers |
| --- | --- |
| `bay-harbor` | Inside bays and harbours — San Diego Bay, Mission Bay, Alamitos, Newport, Huntington Harbour |
| `nearshore-coast` | The coastal strip — kelp lines, breakwalls, jetties, riprap, coastal reef |
| `island` | Island shorelines, boiler rocks, island ridges and their kelp |
| `bank` | Offshore high spots and hard bottom fished over structure |
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
  `seasonal`, `bait`, or `decision` carries `regions` and `waters`.
  `scripts/link-maintenance.py` exits nonzero if one is missing or uses a term
  that isn't on these lists — so the backfill can't rot.
- Terms are **closed**. Adding one means editing this note first.
- A Baja limit differing from a CDFW limit is **two jurisdictions, not a
  conflict** — see [regulatory claims](../sources/regulatory-claims.md).
- These fields describe **where the knowledge applies**, not where the video
  was filmed. A Cabo-filmed video teaching a universal knot applies
  everywhere.

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
- [Hook Assortment by Trip Length — Overnight Through 5–6 Day](../tackle/hook-assortment-by-trip-length.md)
- [Mexican waters](mexican-waters.md)
- [North 9 Mile Bank / 178](north-9-mile-bank-178.md)
- [Source Registry](../sources/source-registry.md)
- [Southern California Bight](socal-bight.md)
<!-- backlinks:end -->
