---
type: conditions
tags: [upwelling, turnover, chlorophyll, bloom-age, bightsst, SST, ekman, enso, primary-productivity]
sources: [h3PTupup17I, cameron, 32TQdFJKIlI, zvU45nkhhuE]
confidence: high
---

# Upwelling and Turnover

Chlorophyll is not a yes/no signal — it has an **age**. This note is about
reading that age: telling **fresh cold upwelled water** (bad now, productive
later) from a **mature bloom edge** (fish now), and about **turnover** — the
sharp regime flip that Cameron's model treats as the single most useful thing to
forecast.

## Bloom age — the freshness interpretation

Upwelling is the front end of the food chain (mechanism in
[current structure](current-structure.md)): current forced over structure lifts
cold, nutrient-rich water, which greens up as phytoplankton bloom. But it takes
time to climb the chain to gamefish, so **freshly upwelled water is cold, green,
and bad *now*** (Landesfeind, Academy Ep. 1):

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

## Turnover — Cameron's doctrine (source `cameron`)

Cameron's turnover model, built from his BightSST work, sharpens the timing:

> **Fishing is best right *before* turnover** — the point where you get the sharp
> SST drop and the chlorophyll spike. **The key model output is
> time-to-turnover / the approach to it — not the turnover event itself.**

In other words, the value is in forecasting *when* a spot is about to flip and
being there in the window just ahead of it, rather than reacting after the SST
has already crashed and the water has gone green. This runs in the same direction
as the corpus bloom-age rule — the pre-turnover window is the mature-edge
opportunity just before the water resets to a fresh cold bloom — and states it
as a **timing target** the plan can aim at.

### Cameron's BightSST upwelling / turnover model (reference, do not duplicate)

His platform ([BightSST](../locations/bightsst-eval-targets.md),
`bightai-api.onrender.com`) is the system of record for the live signal — this KB
references it, it does not reproduce it:

- **Automated upwelling detection** and break detection (Canny/Sobel) on NOAA
  satellite SST, with multi-model SST per spot and frontness-vs-daily-stats.
- **Eval spots:** originally **8** (La Jolla NW corner, 302 Bank, Coronado
  Islands, Mexican rockpile, Pyramid Cove, 9 Mile Bank SD, 14 Mile Bank LA,
  Cortes Bank), **expanding to ~14** by splitting each of the 6 Coronado spots
  into its own eval location (conditions vary a lot across the group). A ~125-bank
  list is the training universe.
- **Known data quirk (`goes_west`):** a composite-window discrepancy
  (self-reported ~23 h vs. stated 12 h) and a cloud-contaminated `goes_west` NRT
  max (96.6 °F) — **treat single-source SST extremes with suspicion.** This is an
  open data-quality item Cameron flagged, not settled doctrine.

## Wind-driven upwelling mechanism — Ekman transport (Crust to Coast, `32TQdFJKIlI`, 2022-10-05; registered mechanism source — global/textbook physics, not fishing doctrine)

The "why" behind the NW-wind → upwelling link above: wind dragging on the
surface layer is transmitted down through the water column, and the Coriolis
effect turns each successively deeper layer (the **Ekman spiral**), producing a
net surface-water transport rotated **90° to the right of the wind direction**
in the Northern Hemisphere (**Ekman transport**; 90° left in the Southern
Hemisphere). On a Northern-Hemisphere west coast like SoCal, a wind blowing
**alongshore, north to south**, deflects 90° to its right — i.e. **offshore** —
creating divergence at the coast that draws cold, nutrient-rich water up from
below: coastal upwelling. Reverse the alongshore wind (south to north) and the
same 90°-right deflection pushes surface water **into** the coast instead:
downwelling, water piles up, productivity drops. This is the textbook mechanism
underneath the corpus's afternoon-NW-wind upwelling event described above.
(**Geostrophic currents** — the rotational flow set up where Ekman transport
piles water into a bulge and gravity pulls it back down-slope — is the same
family of mechanism; noted for vocabulary only, no SoCal-specific parameter
attaches to it here.)

## ENSO — El Niño / La Niña as a basin-scale upwelling modulator (Crust to Coast, `32TQdFJKIlI`, 2022-10-05; registered mechanism source, not fishing doctrine)

- **Baseline (Walker circulation):** trade winds pile warm water in the western
  Pacific; the eastern Pacific, including the SoCal/Baja coast, sits under a
  comparatively shallow thermocline that supports upwelling.
- **El Niño:** trade winds weaken, the warm-water pool and its low-pressure cell
  shift east, the eastern Pacific thermocline deepens → **downwelling
  dominates → lower biological productivity on this coast**, even as warm water
  intrudes. This is the productivity mechanism underneath the corpus's
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
for Cameron's day-to-day turnover model above or the live BightSST signal.

## Why nutrients (not just warmth) trigger the bloom — primary production mechanism (Crust to Coast, "Geology 5 — Primary Productivity," `zvU45nkhhuE`, 2022-11-02; registered mechanism source — global/textbook biology, not fishing doctrine)

The biology underneath "upwelled water greens up as phytoplankton bloom" above:
photosynthesis (phytoplankton using sunlight + CO2 + water to produce energy and
oxygen) is the base of most marine food webs — plants/algae eaten by consumers,
consumers eaten by consumers, up the chain. Two things drive **primary
productivity**, and per the lecture **temperature and salinity are explicitly
not the drivers** (ocean temperature is comparatively stable) — it is:

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
of sunlight to produce sugars that feed a separate deep food web. Noted for
vocabulary/completeness; it is a different mechanism from the photosynthesis-
driven, upwelling-fed chlorophyll signal this note and
[water color](water-color.md) track, and no SoCal fishery parameter attaches to
it here.

Pull the live upwelling/turnover state from BightSST at plan time; use *this*
note for how to interpret bloom age and how to aim for the pre-turnover window.


<!-- backlinks:start -->
## Linked from

- [<Your> Spots](../profiles/_template/spots.md)
- [April](../seasonal/april.md)
- [Bight Geography](../locations/bight-geography.md)
- [BightSST Eval Targets](../locations/bightsst-eval-targets.md)
- [Cameron's Spots](../profiles/cameron/spots.md)
- [Current Structure](current-structure.md)
- [June–July](../seasonal/june-july.md)
- [Pacific Crevalle Jack (Toro)](../species/pacific-crevalle-jack.md)
- [Report Reading and Forecasting](../planning/report-reading-and-forecasting.md)
- [Water Color](water-color.md)
- [Water Regimes](water-regimes.md)
- [Water Temperature](water-temperature.md)
- [Year-Anniversary Prior](../seasonal/year-anniversary-prior.md)
- [Yellowfin Tuna](../species/yellowfin-tuna.md)
- [Yellowtail](../species/yellowtail.md)
<!-- backlinks:end -->
