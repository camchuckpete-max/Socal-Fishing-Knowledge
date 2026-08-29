---
type: conditions
tags: [sea-state, wind, swell, forecasting, planning, santa-ana]
sources: [zKmZ4zql2ws, DnSqw4r7A1s, S2L3KLSQ6Is, OYOda6T3f-8, Z3rZqy2Pi8E, HzE4FHHcvTk, NC3-3pJDEgo, dS0YUOyqN6g, cameron]
confidence: high
layout: v2
---

# Sea State

A raw wind + swell pull (height, period, direction) is not a fishability read on
its own. These rules turn the numbers into a go / bail / route decision, and flag
where a clean-looking forecast will lie to you. Pull observed **and** forecast
wind/swell per fishing zone and along the transit route, then apply the layers
below.

## Steepness rule — period matters more than height

Swell **period** (seconds) drives how a swell feels far more than its height
(`zKmZ4zql2ws`):
- **10 ft @ 15 s** from the south is barely felt in open water.
- **3–4 ft @ 4–5 s** is brutal.

Flag any zone or route segment where the period in seconds approaches the height
in feet — that is a steep, close-interval sea even when the height number looks
small.

## Current-vs-swell opposition

Summer uphill (counter)current running **against** the NW swell compresses the
interval and stands the swell up: a forecast of **4 ft @ 10 s** fishes like
**6 ft @ 7–8 s** when the current opposes it, and wind/NWS point forecasts will
not show it (`zKmZ4zql2ws`). Compute the opposition (current vector vs swell
direction) along the route from the HF-radar / WCOFS current field and
**degrade the forecast where they oppose**.

## Bathymetric slop hotspots

Where current accelerates over a ridge or shoal, the swell stands up **locally**:
the ridge off the **east end of Catalina** is horrible for a few miles, then lays
down 3–4 mi past it (`zKmZ4zql2ws`). Mark bathymetric features on the transit
where the current field accelerates and annotate "expect locally worse seas
here; usually improves beyond" — do not let one rough patch imply the whole
outer zone is blown.

## Wind history, not just wind forecast (12–24 h hindcast)

A calm-morning forecast can hide overnight wind that already built chop before
dawn (`zKmZ4zql2ws`). **Conception-area corollary:** west/NW wind blows at
*night* up there and stops by morning, so a calm dawn reading is a trap — plan a
Santa Rosa / San Miguel crossing only after **2+ consecutive days** of no wind or
Santa Ana conditions (`Z3rZqy2Pi8E`). Add a **12–24 h wind hindcast** for the
route and zones to every conditions pull, not just the forward forecast.

## Upstream fetch check (swell arrives after the wind that made it)

Swell shows up later than the wind that generated it, and from far away: a San
Nicolas Island example ran calm locally all weekend, then jumped **4 ft → 12 ft**
swell by Monday from a system off **Oregon** days earlier (`zKmZ4zql2ws`). Scan
the synoptic wind field up-coast over the prior **48–72 h** for swell-arrival
risk the point forecast under-explains.

## Unforecast-wind heuristics

- **Inland heat → afternoon W wind.** Extreme inland heat (100 °F+) can break down
  into unforecast afternoon W wind on the water. If it is windier than forecast in
  the morning, assume it **builds all day** — a small boat bails early (`DnSqw4r7A1s`).
- **Forecast error is asymmetric.** Assume the forecast errs on the worse side,
  and that afternoon W at the islands **strengthens** rather than eases (`zKmZ4zql2ws`).
- **Catalina Eddy shielding — everything east of Catalina and San Clemente.**
  ⚠ adjudicated (Cameron, 2026-08-26).
  The shielded water is a lee, not a list of banks: the prevailing wind down
  the California coast outside SoCal comes from the **north**, so the islands
  shadow the water behind them and marks well to the south still sit in that
  shadow. The **425** is often shielded despite being far south of San
  Clemente (cameron). Check eddy state when the outer forecast looks bad
  before writing off the inside (`S2L3KLSQ6Is`, cameron).

## Go/no-go wind & swell thresholds

A working-captain rule of thumb for a straight go/bail call, not just a
steepness read (`NC3-3pJDEgo`):

- **Wind is the ocean's driver.** Near-zero wind correlates with flat/glassy
  water; **wind above ~12 kt is what raises whitecaps**, and 12 kt is the
  personal cutoff for not running (`NC3-3pJDEgo`).
- **Swell interval under 10 seconds is a hard bad-sea flag** — sub-10-second
  intervals are "absolutely horrible," independent of height (`NC3-3pJDEgo`).
- **Named unfishable combo:** **12–15 kt wind with 4–8 ft swell at a 9-second
  interval** — "you can't go out there... you just cannot be caught out
  there," a dire situation even for bigger boats; boats in that combo stay at
  the dock regardless of size, not just small-boat caution (`NC3-3pJDEgo`).
- **Forecast tools named:** Buoy Weather, Windy, and iWindy for pulling
  current wind/swell numbers before a trip (`NC3-3pJDEgo`).
- **Captain's-call framing:** treat a big-red-flag forecast (25–45 kt out of
  the NE, for example) as a "we are not going" call, not a "let's see" call —
  the risk call sits with whoever is running the boat, especially with
  passengers aboard (`NC3-3pJDEgo`).

## Santa Ana = northern-islands window

Santa Ana events flatten the NW outer islands. A Santa Ana is the trigger to run
**Santa Rosa / San Miguel** for shallow rockfish and lingcod (`OYOda6T3f-8`, `Z3rZqy2Pi8E`).
See [November–December](../seasonal/november-december.md).

### Santa Ana mechanics and Catalina return-trip risk

A Santa Ana is an offshore-blowing **northeast** wind pattern, a normal
recurring SoCal event (not an anomaly) that starts by mid-November and runs
**through Thanksgiving** in a typical year — the timing is a seasonal norm,
not a one-off (`NC3-3pJDEgo`).

- **Mechanism — why the return leg from Catalina is dangerous in a Santa Ana:**
  swell/water normally moves *toward* the SoCal mainland beaches; an offshore
  (NE) Santa Ana wind pushes water back *out* against that prevailing motion,
  and the opposition stacks the sea into large, fast-building swells
  (`NC3-3pJDEgo`).
- **Return-trip risk:** a boat caught at Avalon in a Santa Ana faces a
  multi-hour beat back to mainland ports (Newport, Dana Point named) fighting
  swell the whole way — an outbound run downwind can feel fine, but the crew
  still has to turn around and come home into it (`NC3-3pJDEgo`). This is a
  distinct mechanism from the "Homebound wind" afternoon-W-build case below —
  here the danger window is the Santa Ana itself, not a diurnal build.

## Homebound wind

A run **south** into Mexican paddy water puts a W wind on the return leg —
uphill misery. Plan return timing **against** the afternoon W build, not just
the outbound conditions (`HzE4FHHcvTk`).

## SD Bay entrance swell exposure

The San Diego Bay entrance is open to swell from roughly **160°–186°**; the
measured channel seaward axis is **186°**. **Baja blocks** swell coming from
**east of ~160°**; **Point Loma blocks** swell from **west of the channel
axis (186°)**. Use this to judge whether a given swell direction will make
the launch/return through the channel rough or protected (cameron).

## Wind mechanism — Coriolis effect and global wind belts (generic, not SoCal-measured)

Wind is air moving from high pressure to low pressure, and Earth's rotation
deflects that moving air (and moving water) — to the **right** in the Northern
Hemisphere, to the **left** in the Southern Hemisphere — because the Earth's
surface moves much faster at the equator (~600 km/h) than near the poles
(~0 km/h). This deflection is the **Coriolis effect** (`dS0YUOyqN6g`).

On a non-rotating Earth, the equator-to-pole heating difference alone would
drive one large convection cell per hemisphere. The Coriolis effect splits
each hemisphere's circulation into three cells instead: the **Hadley cell**
(0°–30°), the **Ferrel cell** (30°–60°), and the **polar cell** (60°–90°).
The boundaries between them produce the Northern Hemisphere's (SoCal's)
prevailing surface-wind bands: calm **doldrums** at the equator (0°) and calm
**horse latitudes** near 30°, bracketing the **trade winds** between them,
plus the **polar easterlies** at the 60°–90° boundary (`dS0YUOyqN6g`).

This is the mechanism reason large-scale wind — and the swell it generates —
has a consistent directional tendency rather than a random distribution. It
is upstream background for the wind/swell layers above, not a SoCal-specific
parameter and not a substitute for the observed/forecast pull.

## How to use it in planning

- Pull both height and period; treat any zone or route segment where the
  period (seconds) approaches the height (feet) as steep regardless of what
  the height number alone suggests.
- Where summer uphill current opposes the NW swell, degrade the forecast —
  expect it to fish rougher than the raw numbers — using the current vector
  from the HF-radar / WCOFS field along the whole route, not just the
  destination.
- Expect isolated bad patches over accelerating current at ridges/shoals
  (e.g., the east end of Catalina) to lay back down a few miles past them;
  don't write off a whole outer zone from one rough stretch.
- Pull a 12–24 h wind hindcast, not just the forward forecast, to catch
  overnight wind a calm morning reading would hide; hold a Santa Rosa / San
  Miguel crossing for 2+ consecutive days of no wind or Santa Ana conditions.
- Scan the synoptic wind field up-coast over the prior 48–72 h — a distant
  system can send swell days later even when it is calm locally.
- On 100 °F+ inland-heat days, assume an unforecast afternoon W wind that
  builds all day and plan a small-boat bail-out window.
- Run the go/no-go thresholds: hold at the dock above ~12 kt wind, treat a
  sub-10-second interval as a hard flag, and never run a 12–15 kt / 4–8 ft /
  9-second combo.
- Check Catalina Eddy shielding before writing off water east of Catalina /
  San Clemente on a bad outer forecast.
- During a Santa Ana, expect the northern islands to flatten while the
  Catalina return leg turns dangerous — plan crossings and return timing
  around that split, not just the outbound conditions.
- On a run south into Mexican paddy water, plan the return leg against the
  afternoon W build; check the SD Bay entrance swell direction against the
  160°–186° exposure window before the harbor transit.

## Related

- [Current structure](current-structure.md) — how the current field that opposes
  swell and accelerates over structure is built.
- [Current diagnostics](current-diagnostics.md) — reading current strength off
  observables once you are on the water.
- [Report reading and forecasting](../planning/report-reading-and-forecasting.md)
- [Day-plan protocol](../planning/day-plan-protocol.md)

## Evidence

Trip reports and per-source provenance: [evidence file](evidence/sea-state.md).

<!-- backlinks:start -->
## Linked from

- [12 Mile Reef](../locations/12-mile-reef.md)
- [14 Mile Bank](../locations/14-mile-bank.md)
- [209 / 312](../locations/209-312.md)
- [279 / 267 / 14 Mile Bank](../locations/279-267-14-mile-bank.md)
- [289 / 284](../locations/289-284.md)
- [311 (Trask Knoll)](../locations/311.md)
- [380](../locations/380.md)
- [43 / 91 / 300](../locations/43-91-300.md)
- [474 / 711](../locations/474-711.md)
- [51 / 181 / 138](../locations/51-181-138.md)
- [Anacapa Island](../locations/anacapa-island.md)
- [April](../seasonal/april.md)
- [Baja Pacific — South](../locations/baja-pacific-south.md)
- [Barred Sand Bass](../species/sand-bass.md)
- [Bight Geography](../locations/bight-geography.md)
- [Catalina Island — Backside](../locations/catalina-island-backside.md)
- [Channel Islands](../locations/channel-islands.md)
- [Chester's Rock](../locations/chester-s-rock.md)
- [Coronados - 230 / 302 (Kidney Bank) / 226](../locations/coronados-230-302-226.md)
- [Cortez South](../locations/cortez-south.md)
- [Current Diagnostics](current-diagnostics.md)
- [Dana Point](../locations/dana-point.md)
- [Davis Knoll / San Miguel Gap / Rodriguez Seamount](../locations/davis-knoll-san-miguel-gap-rodriguez-seamount.md)
- [Day-Plan Protocol](../planning/day-plan-protocol.md)
- [E. Butterfly / San Salvador Knoll](../locations/e-butterfly-san-salvador-knoll.md)
- [Evidence — Dana Point](../locations/evidence/dana-point.md)
- [Evidence — LA - 270 / 286](../locations/evidence/la-270-286.md)
- [Evidence — Sea State](evidence/sea-state.md)
- [Hancock Bank](../locations/hancock-bank.md)
- [Hidden Reef / 170](../locations/hidden-reef-170.md)
- [Isla Espíritu Santo](../locations/isla-espiritu-santo.md)
- [Island Structure](../locations/island-structure.md)
- [Kidney Bank (63) / 175](../locations/kidney-bank-63-175.md)
- [LA - 270 / 286](../locations/la-270-286.md)
- [La Paz](../locations/la-paz.md)
- [Magdalena Bay (Mag Bay / Lopez Mateos)](../locations/bahia-magdalena-lopez-mateos.md)
- [North 9 Mile Bank / 178](../locations/north-9-mile-bank-178.md)
- [November–December](../seasonal/november-december.md)
- [Point Loma](../locations/point-loma.md)
- [Report Reading and Forecasting](../planning/report-reading-and-forecasting.md)
- [Rockfish & Lingcod](../species/rockfish-lingcod.md)
- [San Clemente Island — Back Side](../locations/san-clemente-island-back-side.md)
- [San Clemente Island — Front Side](../locations/san-clemente-island-front-side.md)
- [San Juan Seamount](../locations/san-juan-seamount.md)
- [San Miguel Island](../locations/san-miguel-island.md)
- [San Nicolas Island](../locations/san-nicolas-island.md)
- [Santa Barbara Island](../locations/santa-barbara-island.md)
- [South 9 Mile Bank / 439](../locations/south-9-mile-bank-439.md)
- [South Orange County — Crystal Cove](../locations/south-orange-county-crystal-cove.md)
- [Southern California Bight](../locations/socal-bight.md)
- [Sverdrup Bank (126)](../locations/sverdrup-bank-126.md)
- [Swordfish (Broadbill)](../species/swordfish.md)
- [Tanner Bank](../locations/tanner-bank.md)
- [Targeting yellowtail — Coronado Islands](../species/yellowtail-coronado-islands.md)
- [The 43](../locations/43.md)
- [The Bumps](../locations/bumps.md)
- [The Corner / 140 / 182](../locations/corner-140-182.md)
- [The Slide / 152 / 277](../locations/slide-152-277.md)
- [Water Regimes](water-regimes.md)
<!-- backlinks:end -->
