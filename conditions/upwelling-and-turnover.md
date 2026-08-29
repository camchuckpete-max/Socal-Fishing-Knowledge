---
type: conditions
tags: [upwelling, turnover, chlorophyll, bloom-age, bightsst, SST, ekman, enso, primary-productivity]
sources: [h3PTupup17I, cameron, 32TQdFJKIlI, zvU45nkhhuE]
confidence: high
layout: v2
---

# Upwelling and Turnover

Chlorophyll is not a yes/no signal — it has an **age**. This note is about
reading that age: telling **fresh cold upwelled water** (bad now, productive
later) from a **mature bloom edge** (fish now), and about **turnover** — the
sharp regime flip that the timing model below treats as the single most
useful thing to forecast (cameron).

## Bloom age — the freshness interpretation

Upwelling is the front end of the food chain (mechanism in
[current structure](current-structure.md)): current forced over structure lifts
cold, nutrient-rich water, which greens up as phytoplankton bloom. But it takes
time to climb the chain to gamefish, so **freshly upwelled water is cold, green,
and bad *now*** (`h3PTupup17I`):

- **New cold bloom → avoid.** An overnight ~5 °F drop plus green water after an
  afternoon NW wind is a local upwelling event. Short-term negative — but **mark
  it for the recovery**, because that same water will be productive once the
  chain catches up.
- **Mature bloom edge → fish.** The edges of an established bloom, where green
  meets blue, are where the bait (and the gamefish on it) have stacked up.

So every chlorophyll pull needs the age question attached: *is this a new bloom
(post-wind, cold, freshly green — leave it) or a mature bloom edge (fish it)?*
Pair with [water color](water-color.md) and
[water temperature](water-temperature.md).

## Turnover

The turnover model built on BightSST sharpens the timing (cameron):

> **Fishing is best right *before* turnover** — the point where you get the sharp
> SST drop and the chlorophyll spike. **The key model output is
> time-to-turnover / the approach to it — not the turnover event itself.**
> (cameron)

In other words, the value is in forecasting *when* a spot is about to flip and
being there in the window just ahead of it, rather than reacting after the SST
has already crashed and the water has gone green. This runs the same direction
as the bloom-age rule above — the pre-turnover window is the mature-edge
opportunity just before the water resets to a fresh cold bloom — and states it
as a **timing target** the plan can aim at.

### BightSST upwelling / turnover model (reference, do not duplicate)

[BightSST](../locations/bightsst-eval-targets.md) (`bightai-api.onrender.com`)
is the system of record for the live signal — this KB references it, it does
not reproduce it (cameron):

- **Automated upwelling detection** and break detection (Canny/Sobel) on NOAA
  satellite SST, with multi-model SST per spot and frontness-vs-daily-stats.
- **Eval spots:** originally **8** (La Jolla NW corner, 302 Bank, Coronado
  Islands, Mexican rockpile, Pyramid Cove, 9 Mile Bank SD, 14 Mile Bank LA,
  Cortes Bank), **expanding to ~14** by splitting each of the 6 Coronado spots
  into its own eval location (conditions vary a lot across the group). A ~125-bank
  list is the training universe.
- **Known data quirk (`goes_west`):** a composite-window discrepancy
  (self-reported ~23 h vs. stated 12 h) and a cloud-contaminated `goes_west` NRT
  max (96.6 °F) — **treat single-source SST extremes with suspicion.** This is
  an open data-quality item, not settled doctrine (cameron).

## Wind-driven upwelling mechanism — Ekman transport (mechanism, generic — not SoCal-measured)

Wind dragging on the surface layer is transmitted down through the water
column, and the Coriolis effect turns each successively deeper layer (the
**Ekman spiral**), producing a net surface-water transport rotated **90° to
the right of the wind direction** in the Northern Hemisphere (**Ekman
transport**; 90° left in the Southern Hemisphere) (`32TQdFJKIlI`). This is the
mechanism behind the NW-wind → upwelling link above. On a Northern-Hemisphere
west coast like SoCal, a wind blowing **alongshore, north to south**, deflects
90° to its right — i.e. **offshore** — creating divergence at the coast that
draws cold, nutrient-rich water up from below: coastal upwelling. Reverse the
alongshore wind (south to north) and the same 90°-right deflection pushes
surface water **into** the coast instead: downwelling, water piles up,
productivity drops. This is the textbook mechanism underneath the
afternoon-NW-wind upwelling event described above. (**Geostrophic currents** —
the rotational flow set up where Ekman transport piles water into a bulge and
gravity pulls it back down-slope — is the same family of mechanism; noted for
vocabulary only, no SoCal-specific parameter attaches to it here.)
(`32TQdFJKIlI`)

## ENSO — El Niño / La Niña as a basin-scale upwelling modulator (mechanism, generic — not SoCal-measured)

Background mechanism from an oceanography lecture (`32TQdFJKIlI`):

- **Baseline (Walker circulation):** trade winds pile warm water in the western
  Pacific; the eastern Pacific, including the SoCal/Baja coast, sits under a
  comparatively shallow thermocline that supports upwelling.
- **El Niño:** trade winds weaken, the warm-water pool and its low-pressure cell
  shift east, the eastern Pacific thermocline deepens → **downwelling
  dominates → lower biological productivity on this coast**, even as warm water
  intrudes. This is the productivity mechanism underneath the
  tropical-species-range-extension pattern documented elsewhere (e.g.
  [Pacific crevalle jack](../species/pacific-crevalle-jack.md),
  [yellowfin tuna](../species/yellowfin-tuna.md),
  [yellowtail](../species/yellowtail.md)) — those notes describe warm water
  pulling species range north; this note adds that the same event is
  simultaneously suppressing local upwelling-driven productivity underneath it.
- **La Niña:** trade winds strengthen, the warm pool retreats west, the eastern
  Pacific thermocline shoals, water cools → **upwelling dominates → higher
  biological productivity on this coast.**
- **Irregularity:** ENSO recurs roughly every **2–10 years**; individual phases
  last **12–18 months**. The lecture notes it may nest inside a longer
  **~20–30 year Pacific Decadal Oscillation (PDO)** — flagged there as an open
  research question, not settled science.

This operates on a basin-scale, multi-month-to-multi-year timescale — the
long-range backdrop conditions sit within, distinct from and not a substitute
for the day-to-day turnover model above or the live BightSST signal.

## Why nutrients (not just warmth) trigger the bloom — primary production mechanism (mechanism, generic — not SoCal-measured)

The biology underneath "upwelled water greens up as phytoplankton bloom" above:
photosynthesis (phytoplankton using sunlight + CO2 + water to produce energy and
oxygen) is the base of most marine food webs — plants/algae eaten by consumers,
consumers eaten by consumers, up the chain. Two things drive **primary
productivity**; **temperature and salinity are explicitly not the drivers**
(ocean temperature is comparatively stable) (`zvU45nkhhuE`) — it is:

- **Light** — photosynthesis only runs in the sunlit euphotic zone; the rate
  falls with depth until the **compensation depth**, where respiration equals
  photosynthesis and there is no more net productivity below it. **Net
  production = gross production − respiration** (gross is total photosynthetic
  output before subtracting what the organisms themselves burn).
- **Nutrients** — chiefly **nitrates** (also phosphates), plus **silica** for
  diatom shells and **calcium carbonate** for coccolithophore shells. This is
  the nutrient half of the chlorophyll signal above: **upwelling is what
  delivers these nutrients** to the lit surface layer, which is why coastal
  upwelling zones (west coasts of continents, SoCal/Baja included) carry the
  world's highest net primary productivity.
- **Seasonality** follows light + nutrient availability by latitude: tropical
  productivity runs low and roughly constant year-round (stratified mix
  layer/thermocline chokes nutrient supply despite steady light); temperate
  latitudes (SoCal's band) get **two blooms — a spring bloom and an autumn
  bloom**; polar latitudes get one large **spring/summer bloom** when six
  months of darkness give way to light over nutrient-rich water.

**Chemosynthesis — the non-photosynthetic alternate base of the food web:** at
deep-sea hydrothermal vents ("black smokers," too deep for light), distinct
microbial communities run **chemosynthesis** — using hydrogen sulfide instead
of sunlight to produce sugars that feed a separate deep food web (`zvU45nkhhuE`).
Noted for vocabulary/completeness; it is a different mechanism from the
photosynthesis-driven, upwelling-fed chlorophyll signal this note and
[water color](water-color.md) track, and no SoCal fishery parameter attaches to
it here.

## How to use it in planning

- Attach the age question to every chlorophyll pull: a new post-wind cold-green
  bloom (an overnight ~5 °F drop plus green water) is a **later** asset — mark
  it and come back; a mature bloom edge, where green meets blue, is a **now**
  asset (`h3PTupup17I`).
- Aim for the pre-turnover window — the approach to the SST-drop /
  chlorophyll-spike flip — rather than reacting after the water has already
  turned over; time-to-turnover is the model output that matters, not the
  turnover event itself (cameron).
- Treat a single-source SST extreme (e.g. a cloud-contaminated `goes_west` NRT
  read) with suspicion; cross-check another model before trusting an outlier
  (cameron).
- Read ENSO phase as the season's multi-month backdrop (El Niño → suppressed
  coastal productivity, La Niña → elevated) — it sets the baseline the
  day's BightSST read sits on top of, not a substitute for it.

Pull the live upwelling/turnover state from [BightSST](../planning/day-plan-protocol.md)
at plan time; use this note for how to interpret bloom age and how to aim for
the pre-turnover window.


<!-- backlinks:start -->
## Linked from

- [12 Mile Reef](../locations/12-mile-reef.md)
- [14 Mile Bank](../locations/14-mile-bank.md)
- [279 / 267 / 14 Mile Bank](../locations/279-267-14-mile-bank.md)
- [289 / 284](../locations/289-284.md)
- [311 (Trask Knoll)](../locations/311.md)
- [474 / 711](../locations/474-711.md)
- [<Your> Spots](../profiles/_template/spots.md)
- [Anacapa Island](../locations/anacapa-island.md)
- [April](../seasonal/april.md)
- [Barred Sand Bass](../species/sand-bass.md)
- [Bight Geography](../locations/bight-geography.md)
- [BightSST Eval Targets](../locations/bightsst-eval-targets.md)
- [Cameron's Spots](../profiles/cameron/spots.md)
- [Channel Islands](../locations/channel-islands.md)
- [Coronados - 230 / 302 (Kidney Bank) / 226](../locations/coronados-230-302-226.md)
- [Current Structure](current-structure.md)
- [Davis Knoll / San Miguel Gap / Rodriguez Seamount](../locations/davis-knoll-san-miguel-gap-rodriguez-seamount.md)
- [E. Butterfly / San Salvador Knoll](../locations/e-butterfly-san-salvador-knoll.md)
- [Hancock Bank](../locations/hancock-bank.md)
- [Hidden Reef / 170](../locations/hidden-reef-170.md)
- [June–July](../seasonal/june-july.md)
- [Kidney Bank (63) / 175](../locations/kidney-bank-63-175.md)
- [LA - 270 / 286](../locations/la-270-286.md)
- [La Jolla](../locations/la-jolla.md)
- [North 9 Mile Bank / 178](../locations/north-9-mile-bank-178.md)
- [Report Reading and Forecasting](../planning/report-reading-and-forecasting.md)
- [San Juan Seamount](../locations/san-juan-seamount.md)
- [San Miguel Island](../locations/san-miguel-island.md)
- [South 9 Mile Bank / 439](../locations/south-9-mile-bank-439.md)
- [Striped Marlin](../species/striped-marlin.md)
- [Sverdrup Bank (126)](../locations/sverdrup-bank-126.md)
- [The Boot (504) / 307](../locations/boot-504-307.md)
- [Wahoo](../species/wahoo.md)
- [Water Color](water-color.md)
- [Water Regimes](water-regimes.md)
- [Water Temperature](water-temperature.md)
- [Year-Anniversary Prior](../seasonal/year-anniversary-prior.md)
<!-- backlinks:end -->
