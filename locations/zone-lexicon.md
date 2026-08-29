---
type: location
tags: [zones, search-box, naming, geography, planning]
sources: [cameron, Blh2BA-7Ono, Rf1HKJG-SDg, 5to3Q5P7w90, OYOda6T3f-8]
confidence: high
regions: [socal-bight]
waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]
layout: v2
parent: unknown
structure_type: search-box sizing, bank/spot-file naming conventions, and sub-pixel waypoint clustering — vocabulary and scale, not one structure
depth_band: unknown — universal vocabulary, not tied to one depth
distance_nm: unknown — universal knowledge, not measured from one launch point
---

# Zone Lexicon

The vocabulary of SoCal fishing zones: how to name a spot, how to think about a
spot as a *box* rather than a pin, and how big that box is. This is universal
structure/planning knowledge; it holds no coordinates. For the physical
typology of the structure itself see [island structure](island-structure.md)
and [bass structure](bass-structure.md); for where the big weather and water
bands sit see [bight geography](bight-geography.md).

## Getting there

This is universal naming and sizing vocabulary, not a single spot — it has no
launch point or transit leg of its own. Getting-there detail belongs to the
zone and spot pages this note supports, e.g. any of the below-Clemente bank
pages.

⚠ Flagged gap — no corpus source: transit/launch detail (not applicable —
this note is universal, not spot-scoped).

## Structure & bathymetry

**A "spot" is a search box, not a pin.** Some named spots are a pin you idle
onto; others are a region you look through for hours. Sizing the box
correctly is the difference between a plan that works and one that spends the
day driving.

- **A complex** — the below-Clemente group of banks (43, 181, 182, 289,
  Clemente Ridge up to Mackerel Bank) — reads as **one ~50–60 square-mile
  search box** (`Blh2BA-7Ono`). You do not "check 43"; you plan **hours of
  looking** across the whole box, glassing and running contour between
  features, treating the named banks inside it as reference points within a
  single hunting zone.
- **A compact spot** — 302, 371, west-of-Catalina — is the opposite: a small,
  definable piece of structure you idle up to, grade the meter, and either
  commit or leave. A spot-check, not an expedition.

Budget time by box size: a complex is a half-day commitment, a compact spot is
a 20–30 minute read. See [search and glassing](../planning/search-and-glassing.md)
for the glassing protocol that fills those hours, and
[BightSST eval targets](bightsst-eval-targets.md) for the modeling-spot list.

**Bank naming runs on a fathom-depth convention.** Most of the inshore
mainland water — a mile to a mile-and-a-half off the beach from Dana Point
through Newport and Marina del Rey out to Catalina — is already **2,000–3,000
ft deep**; Huntington is the one stretch that stays shallower longer because
of the flats there (`Rf1HKJG-SDg`). Against that deep, mostly featureless
bottom, a bank is an isolated high spot — a submerged mountain rising out of
the surrounding depth — and bait stages on it for shelter while gamefish
follow the bait; structure is the constant across every fishery region (SoCal,
Cabo, Florida, Alaska, the Gulf), even though current, tide, and water
temperature also matter (`Rf1HKJG-SDg`).

- **The convention:** a bank is named for the **fathom depth of its
  shallowest (highest) point**, as read on the sounder — "182" tops out at
  182 fathoms before the bottom falls away to the surrounding depth; "209"
  tops out at 209 fathoms; "43" tops out at 43 fathoms (`Rf1HKJG-SDg`). A
  depth only earns "bank" status when it's an isolated high spot rising out
  of otherwise deep water — other places read the same fathom figure without
  being "a bank."
- **The exception — named for distance, not depth.** Nine Mile Bank is named
  for sitting **9 (statute) miles off the coast**, not for a 9-fathom depth;
  it carries many closely spaced high spots of similar depth rather than one
  dominant peak — in places it comes up to roughly 600 ft (`Rf1HKJG-SDg`) ⚠
  asr-uncertain: the exact figure is unclear in the source audio. "The 14"
  follows the same distance-naming pattern, sitting **14 miles off the beach**
  (`Rf1HKJG-SDg`).
- **Six feet to a fathom.** This is also why the sounder itself is
  historically called a "fathometer" (`Rf1HKJG-SDg`) — see
  [electronics and sounder](../planning/electronics-and-sounder.md).

This is the naming layer behind the below-Clemente complex above — most named
spots really are just their fathom number.

**Spot-file naming conventions** keep a personal spot library navigable once
names start colliding — dozens of banks are just numbers (cameron):

- **Landmass-prefix collision rule.** When two spots share a name, prefix
  with the **closest landmass** — "Catalina - X", "Baja - X", "San Diego - X"
  (cameron).
- **The "400" exception.** The two "400" banks are named **"East 400" /
  "West 400"** instead — both are Baja offshore, roughly 44 km apart
  east–west at the same latitude, so a landmass prefix cannot separate them
  (cameron).
- **Distinct, not collisions.** Similar-looking names that are genuinely
  different spots are kept as-is, not merged: "475" vs "475 Knuckle"; "300"
  vs "Bell Bank (300)" vs "300 (The Rampart)"; "179" vs "Tuna Hole (179)";
  "220" vs "Double 220". Colloquially ambiguous but distinct: "Kidney Bank
  (63)" vs "302 (Kidney Bank)" (cameron).
- **Unresolved collision.** "The Slide" ×2 — one Catalina front-side
  shoreline spot, one offshore bank ~6 km away; both are closest to Catalina,
  so the landmass rule cannot separate them. Open item, awaiting Cameron —
  not doctrine.

**Sub-pixel clusters.** Some "spots" are really a cluster of numbered
waypoints packed tighter than a single satellite pixel. For **modeling**
(SST/chlorophyll lookups) collapse the cluster to ~1 MUR pixel; for
**navigation** keep every waypoint distinct (cameron). Known clusters:
Carlsbad AR 1–12, Oceanside AR 1A–1H / 2A–2L, Pendleton 1–7, International
Reef A–F, Torrey Pines 1–2 (cameron). The lesson generalizes: artificial
reefs and permit-line structures come as numbered series that are one *water
cell* but many *drops*.

## What's there

| species | season | what the box concept does for them |
| --- | --- | --- |
| [Bluefin Tuna](../species/bluefin-tuna.md) | September (`5to3Q5P7w90`) | the **volume square** — SBI (Santa Barbara Island) – San Nicolas – San Clemente – Catalina — is the region that holds the bigger fish that month; work it as a region, not a point (`5to3Q5P7w90`). As the coast cools and fragments in fall, the fish condense outward toward Tanner and Cortez (`OYOda6T3f-8`) — that migration is tracked in [bight geography](bight-geography.md) |

⚠ Flagged gap — no corpus source: species-by-zone presence beyond the volume
square example. This is a naming/sizing vocabulary note, not a
species-presence note; species presence and season timing live in the species
routers and the zone/spot pages.

## How it fishes

⚠ Flagged gap — no corpus source: current/wind/tide behavior (not applicable
— this is a naming and box-sizing vocabulary note, not a conditions note;
conditions behavior lives in [conditions/](../conditions/) and on the
zone/spot pages this note supports).

<!-- backlinks:start -->
## Linked from

- [101 / 425](101-425.md)
- [1010 Trench / 378 / 213](1010-trench-378-213.md)
- [1140 Finger / 450](1140-finger-450.md)
- [12 Mile Reef](12-mile-reef.md)
- [14 Mile Bank](14-mile-bank.md)
- [172 / 125](172-125.md)
- [179 / 220](179-220.md)
- [209 / 312](209-312.md)
- [279 / 267 / 14 Mile Bank](279-267-14-mile-bank.md)
- [289 / 284](289-284.md)
- [311 (Trask Knoll)](311.md)
- [372 / 245 / 250](372-245-250.md)
- [380](380.md)
- [385 / 238 / 475](385-238-475.md)
- [43 / 91 / 300](43-91-300.md)
- [474 / 711](474-711.md)
- [475 Knuckle / Upper Finger Bank](475-knuckle-upper-finger-bank.md)
- [483/500 / 437](483-500-437.md)
- [51 / 181 / 138](51-181-138.md)
- [81 / 381](81-381.md)
- [<Your> Spots](../profiles/_template/spots.md)
- [Baja - 230 / Peanut Bank / 60](baja-230-peanut-bank-60.md)
- [Baja - 270 / Double 220 / 295](baja-270-double-220-295.md)
- [Baja Pacific — North](baja-pacific-north.md)
- [Banda Bank / Todos Santos Island](banda-bank-todos-santos-island.md)
- [Bluefin Tuna](../species/bluefin-tuna.md)
- [California Sheephead](../species/sheephead.md)
- [Cameron's Spots](../profiles/cameron/spots.md)
- [Catalina Island — Front Side](catalina-island-front-side.md)
- [Colonet](colonet.md)
- [Coronados - 230 / 302 (Kidney Bank) / 226](coronados-230-302-226.md)
- [Davis Knoll / San Miguel Gap / Rodriguez Seamount](davis-knoll-san-miguel-gap-rodriguez-seamount.md)
- [E. Butterfly / San Salvador Knoll](e-butterfly-san-salvador-knoll.md)
- [Electronics and Sounder](../planning/electronics-and-sounder.md)
- [Evidence — 209 / 312](evidence/209-312.md)
- [Evidence — 289 / 284](evidence/289-284.md)
- [Evidence — Dana Point](evidence/dana-point.md)
- [Finger Bank rockfish](finger-bank-rockfish.md)
- [Hancock Bank](hancock-bank.md)
- [Hidden Reef / 170](hidden-reef-170.md)
- [International Artificial Reef](international-artificial-reef.md)
- [Kidney Bank (63) / 175](kidney-bank-63-175.md)
- [LA - 270 / 286](la-270-286.md)
- [La Fonda / Bajamar / Salsipuedes](la-fonda-bajamar-salsipuedes.md)
- [Lower Cross](lower-cross.md)
- [North 9 Mile Bank / 178](north-9-mile-bank-178.md)
- [North County Artificial Reefs](north-county-artificial-reefs.md)
- [Ocean Whitefish](../species/ocean-whitefish.md)
- [Punta Banda / Santo Tomas](punta-banda-santo-tomas.md)
- [Rockfish & Lingcod](../species/rockfish-lingcod.md)
- [San Clemente Island — Front Side](san-clemente-island-front-side.md)
- [San Diego Artificial Reefs](san-diego-artificial-reefs.md)
- [San Juan Seamount](san-juan-seamount.md)
- [San Nicolas Island](san-nicolas-island.md)
- [San Quintin](san-quintin.md)
- [Santa Barbara Island](santa-barbara-island.md)
- [Skipjack Tuna](../species/skipjack-tuna.md)
- [Sniffer / West 400 / 300 (The Rampart)](sniffer-west-400-300.md)
- [South 9 Mile Bank / 439](south-9-mile-bank-439.md)
- [Southern California Bight](socal-bight.md)
- [Striped Marlin](../species/striped-marlin.md)
- [Sverdrup Bank (126)](sverdrup-bank-126.md)
- [Swordfish (Broadbill)](../species/swordfish.md)
- [Tanner Bank](tanner-bank.md)
- [The Boot (504) / 307](boot-504-307.md)
- [The Bumps](bumps.md)
- [The Corner / 140 / 182](corner-140-182.md)
- [The Pistol / Bell Bank (300)](pistol-bell-bank-300.md)
- [The Slide / 152 / 277](slide-152-277.md)
- [Upper 500 / Hidden Bank](upper-500-hidden-bank.md)
- [Upper Cross / 421 / 390](upper-cross-421-390.md)
- [W. Butterfly / 157](w-butterfly-157.md)
- [Yellowfin Tuna](../species/yellowfin-tuna.md)
<!-- backlinks:end -->
