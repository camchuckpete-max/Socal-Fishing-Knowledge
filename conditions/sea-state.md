---
type: conditions
tags: [sea-state, wind, swell, forecasting, planning, santa-ana]
sources: [zKmZ4zql2ws, DnSqw4r7A1s, S2L3KLSQ6Is, OYOda6T3f-8, Z3rZqy2Pi8E, HzE4FHHcvTk, NC3-3pJDEgo, dS0YUOyqN6g, cameron]
confidence: high
---

# Sea State

A raw wind + swell pull (height, period, direction) is not a fishability read on
its own. These rules turn the numbers into a go / bail / route decision, and flag
where a clean-looking forecast will lie to you. Pull observed **and** forecast
wind/swell per fishing zone and along the transit route, then apply the layers
below. Doctrine here is mostly Erik Landesfeind / SoCal Bight Fishing Academy
Ep. 6 (marine forecasts) unless a specific report is cited.

## Steepness rule — period matters more than height

Swell **period** (seconds) drives how a swell feels far more than its height.
- **10 ft @ 15 s** from the south is barely felt in open water.
- **3–4 ft @ 4–5 s** is brutal.

Flag any zone or route segment where the period in seconds approaches the height
in feet — that is a steep, close-interval sea even when the height number looks
small.

## Current-vs-swell opposition

Summer uphill (counter)current running **against** the NW swell compresses the
interval and stands the swell up. A forecast of **4 ft @ 10 s** fishes like
**6 ft @ 7–8 s** when the current opposes it. Wind/NWS point forecasts will not
show this. Compute the opposition (current vector vs swell direction) along the
route from the HF-radar / WCOFS current field and **degrade the forecast where
they oppose**.

## Bathymetric slop hotspots

Where current accelerates over a ridge or shoal, the swell stands up **locally**.
Landesfeind's example: the ridge off the **east end of Catalina** is horrible for
a few miles, then lays down 3–4 mi past it. Mark bathymetric features on the
transit where the current field accelerates and annotate "expect locally worse
seas here; usually improves beyond" — do not let one rough patch imply the whole
outer zone is blown.

## Wind history, not just wind forecast (12–24 h hindcast)

A calm-morning forecast hides overnight wind. Landesfeind got beat up by leftover
chop from a south wind that had blown all night against an otherwise calm morning
read. **Conception-area corollary:** NW blows at *night* up there and stops by
morning, so a calm 6 a.m. reading is a trap — he wants **2+ consecutive days** of
no-wind or Santa Anas before a Santa Rosa / San Miguel crossing (Ep. 6; 11/23/22).
Add a **12–24 h wind hindcast** for the route and zones to every conditions pull,
not just the forward forecast.

## Upstream fetch check (swell arrives after the wind that made it)

Swell shows up later than the wind that generated it, and from far away. San
Nicolas example: calm locally all weekend, then **4 ft → 12 ft** swell by Monday
from a system off **Oregon** days earlier. Scan the synoptic wind field up-coast
over the prior **48–72 h** for swell-arrival risk the point forecast under-explains.

## Unforecast-wind heuristics

- **Inland heat → afternoon W wind.** Extreme inland heat (100 °F+) can break down
  into unforecast afternoon W wind on the water. If it is windier than forecast in
  the morning, assume it **builds all day** — a small boat bails early (`DnSqw4r7A1s`).
- **Forecast error is asymmetric.** Assume the forecast errs on the worse side,
  and that afternoon W at the islands **strengthens** rather than eases (Ep. 6).
- **Catalina Eddy shielding.** The Catalina Eddy can shield the inner SD banks /
  tuna grounds while it blows outside. Check eddy state when the outer forecast
  looks bad before writing off the inside (`S2L3KLSQ6Is`).

## Go/no-go wind & swell thresholds (`dave-hansen`)

Working-captain rule of thumb for a straight go/bail call, not just a
steepness read (dave-hansen is a registered voice, but this specific set of
thresholds is a single-mention claim, not yet repeated elsewhere in the
corpus — **medium** confidence pending repetition):

- **Wind is the ocean's driver.** Near-zero wind correlates with flat/glassy
  water; **wind above ~12 kt is what raises whitecaps**, and Hansen's personal
  cutoff is to not run when wind is blowing over 12 kt (NC3-3pJDEgo, 2020-11-18).
- **Swell interval under 10 seconds is a hard bad-sea flag** — he calls
  sub-10-second intervals "absolutely horrible," independent of height
  (`NC3-3pJDEgo`).
- **Named unfishable combo:** **12–15 kt wind with 4–8 ft swell at a 9-second
  interval** — "you can't go out there... you just cannot be caught out
  there," a dire situation even for bigger boats; he holds larger boats he
  runs at the dock in that combo too, not just small-boat caution
  (NC3-3pJDEgo, 2020-11-18).
- **Forecast tools named:** Buoy Weather, Windy, and iWindy for pulling
  current wind/swell numbers before a trip (`NC3-3pJDEgo`).
- **Captain's-call framing:** treat a big-red-flag forecast (his example: 25–45
  kt out of the NE) as a "we are not going" call, not a "let's see" call —
  weigher-of-risk responsibility sits with whoever is running the boat,
  especially with passengers aboard (NC3-3pJDEgo, 2020-11-18).

## Santa Ana = northern-islands window

Santa Ana events flatten the NW outer islands. A Santa Ana is the trigger to run
**Santa Rosa / San Miguel** for shallow rockfish and lingcod (`OYOda6T3f-8`, `Z3rZqy2Pi8E`).
See [November–December](../seasonal/november-december.md).

### Santa Ana mechanics and Catalina return-trip risk (dave-hansen, single mention — medium confidence)

A Santa Ana is an offshore-blowing **northeast** wind pattern, a normal
recurring SoCal event (not an anomaly) that runs from around this time of
year (the video was published 2020-11-18) **through Thanksgiving** in a
typical year — the timing is a seasonal norm, not a one-off (NC3-3pJDEgo,
2020-11-18).

- **Observed** (your-saltwater-guide, NC3-3pJDEgo, 2020-11-18, Avalon/Catalina):
  during an active Santa Ana, wind at Avalon was running **25–45 kt**, blowing
  straight into Avalon harbor with waves breaking over the breakwater rocks.
- **Mechanism — why the return leg from Catalina is dangerous in a Santa Ana:**
  swell/water normally moves *toward* the SoCal mainland beaches; an offshore
  (NE) Santa Ana wind pushes water back *out* against that prevailing motion,
  and the opposition stacks the sea into large, fast-building swells
  (`NC3-3pJDEgo`).
- **Return-trip risk:** a boat caught at Avalon in a Santa Ana faces a
  multi-hour beat back to mainland ports (Newport, Dana Point named) fighting
  swell the whole way — an outbound run downwind can feel fine, but the crew
  still has to turn around and come home into it (NC3-3pJDEgo, 2020-11-18).
  This is a distinct mechanism from the "Homebound wind" afternoon-W-build
  case below — here the danger window is the Santa Ana itself, not a diurnal
  build.

## Homebound wind

Runs **south** into Mexican paddy water put a W wind on the return leg = uphill
misery. Plan return timing **against** the afternoon W build, not just the outbound
conditions (`HzE4FHHcvTk`).

## Cameron's SD Bay entrance swell exposure

**Cameron** (own chart work): the San Diego Bay entrance is open to swell from
roughly **160°–186°**. The measured channel seaward axis is **186°**. **Baja
blocks** swell coming from **east of ~160°**; **Point Loma blocks** swell from
**west of the channel axis (186°)**. Use this to judge whether a given swell
direction will make the launch/return through the channel rough or protected.

## Wind mechanism: Coriolis effect and global wind belts (background, generic)

Background mechanism from an oceanography lecture (Crust to Coast, "Oceans and
Climate," `dS0YUOyqN6g`, 2022-10-14; registered mechanism source — global
textbook physics, not a SoCal measurement, and not fishing doctrine): wind is
air moving from high pressure to low pressure, and Earth's rotation deflects
that moving air (and moving water) — to the **right** in the Northern
Hemisphere, to the **left** in the Southern Hemisphere — because the Earth's
surface moves much faster at the equator (~600 km/h) than near the poles
(~0 km/h). This deflection is the **Coriolis effect**.

On a non-rotating Earth, the equator-to-pole heating difference alone would
drive one large convection cell per hemisphere. The Coriolis effect splits
each hemisphere's circulation into three cells instead: the **Hadley cell**
(0°–30°), the **Ferrel cell** (30°–60°), and the **polar cell** (60°–90°).
The boundaries between them produce the Northern Hemisphere's (SoCal's)
prevailing surface-wind bands: calm **doldrums** at the equator (0°) and calm
**horse latitudes** near 30°, bracketing the **trade winds** between them; the
lecture also names the **polar easterlies** at the 60°–90° boundary (the
30°–60° band's name was shown on an on-screen table the auto-generated
captions did not transcribe, so it is not asserted here).

This is the mechanism reason large-scale wind — and the swell it generates —
has a consistent directional tendency rather than a random distribution. It
is upstream background for the wind/swell layers above, not a SoCal-specific
parameter and not a substitute for the observed/forecast pull.

## Related

- [Current structure](current-structure.md) — how the current field that opposes
  swell and accelerates over structure is built.
- [Current diagnostics](current-diagnostics.md) — reading current strength off
  observables once you are on the water.
- [Report reading and forecasting](../planning/report-reading-and-forecasting.md)
- [Day-plan protocol](../planning/day-plan-protocol.md)


<!-- backlinks:start -->
## Linked from

- [43 / 91 / 300](../locations/43-91-300.md)
- [51 / 181 / 138](../locations/51-181-138.md)
- [April](../seasonal/april.md)
- [Baja Pacific — South](../locations/baja-pacific-south.md)
- [Bight Geography](../locations/bight-geography.md)
- [Catalina Island — Backside](../locations/catalina-island-backside.md)
- [Coronados - 230 / 302 (Kidney Bank) / 226](../locations/coronados-230-302-226.md)
- [Cortez South](../locations/cortez-south.md)
- [Current Diagnostics](current-diagnostics.md)
- [Dana Point](../locations/dana-point.md)
- [Davis Knoll / San Miguel Gap / Rodriguez Seamount](../locations/davis-knoll-san-miguel-gap-rodriguez-seamount.md)
- [Day-Plan Protocol](../planning/day-plan-protocol.md)
- [Evidence — Dana Point](../locations/evidence/dana-point.md)
- [Evidence — LA - 270 / 286](../locations/evidence/la-270-286.md)
- [Hidden Reef / 170](../locations/hidden-reef-170.md)
- [Island Structure](../locations/island-structure.md)
- [Kidney Bank (63) / 175](../locations/kidney-bank-63-175.md)
- [LA - 270 / 286](../locations/la-270-286.md)
- [Magdalena Bay (Mag Bay / Lopez Mateos)](../locations/bahia-magdalena-lopez-mateos.md)
- [November–December](../seasonal/november-december.md)
- [Point Loma](../locations/point-loma.md)
- [Report Reading and Forecasting](../planning/report-reading-and-forecasting.md)
- [San Clemente Island — Back Side](../locations/san-clemente-island-back-side.md)
- [San Clemente Island — Front Side](../locations/san-clemente-island-front-side.md)
- [San Nicolas Island](../locations/san-nicolas-island.md)
- [Santa Barbara Island](../locations/santa-barbara-island.md)
- [South Orange County — Crystal Cove](../locations/south-orange-county-crystal-cove.md)
- [Southern California Bight](../locations/socal-bight.md)
- [Swordfish (Broadbill)](../species/swordfish.md)
- [Targeting yellowtail — Coronado Islands](../species/yellowtail-coronado-islands.md)
- [The Corner / 140 / 182](../locations/corner-140-182.md)
- [The Slide / 152 / 277](../locations/slide-152-277.md)
- [Water Regimes](water-regimes.md)
<!-- backlinks:end -->
