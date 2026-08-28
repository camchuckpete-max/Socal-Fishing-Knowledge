---
type: planning
tags: [day-plan, protocol, workflow]
sources: [cameron]
confidence: high
---

# Day-Plan Protocol

The procedure chat and the boat-day skill follow to turn **conditions** +
**priors** into a gear'd-up plan. It degrades gracefully: with no profile it
returns class-term recommendations; with a profile it returns owned gear and
respects the boat envelope (range, sea-state, holder geometry). A session that
fetches only this note plus the folder [README](../README.md) indexes can
navigate the whole KB.

## The five steps

1. **Pull conditions.** Per fishing zone and along the transit route, observed
   **and** forecast: per-spot SST + chlorophyll, wind/swell/current. Endpoints,
   the fallback ladder, and the source-validity rules live in
   [conditions endpoints](../config/endpoints.md) — read that before any pull.

1b. **Set the day's envelope — do this before you open any species note.**
   From the launch point and the boat's range, derive the trip's
   **`{regions, waters}`** using the
   [regions & waters vocabulary](../locations/regions.md):

   - **`regions`** — one or more of `socal-bight`, `baja-pacific-north`,
     `baja-pacific-south`, `cortez-north`, `cortez-south`. Where you are
     actually fishing.
   - **`waters`** — which of `bay-harbor` / `nearshore-coast` / `island` /
     `bank` / `open-ocean` are reachable, given the profile's `range_nm` and
     `sea_state_max_ft` against the day's forecast. With no profile, ask.
   - Then read the matching [locations](../locations/) note(s) for the
     structure you'll actually be fishing — bays and harbors, breakwalls and
     riprap, island structure, bass structure, the zone lexicon.

   **This filter is binding for the rest of the plan.** A species or technique
   note whose `regions` doesn't contain the day's region, or whose `waters`
   doesn't intersect the day's waters, is **never offered** — not ranked
   lower, not offered with a caveat. If nothing in the envelope fits the
   conditions, say so and stop; do not substitute something out of region.

   *Why this step exists:* without it a Mission Bay day plan can route to
   [cabrilla](../species/cabrilla.md), whose situation table opens with "low
   light, tight to shoreline structure → jerkbaits, cast tight to the rock."
   That reads perfectly for a SoCal jetty at dawn, and the fish lives 400
   miles away in the Sea of Cortez.
2. **Apply priors + interpretation layers.** Weight zones and set timing (moon,
   tide windows) using the [seasonal priors](../seasonal/README.md) calendar and the
   [conditions layers](../conditions/README.md) — especially
   [sea-state](../conditions/sea-state.md), [moon](../conditions/moon.md),
   [tide & slack](../conditions/tide-and-slack.md),
   [current-structure](../conditions/current-structure.md), and
   [water color](../conditions/water-color.md) /
   [temperature](../conditions/water-temperature.md). Age the intel with
   [report reading & forecasting](report-reading-and-forecasting.md) (report
   aging, advection, coverage bias).
3. **Resolve species + technique.** Enter through the [species routers](../species/README.md)
   — **filtered to the step-1b envelope** — each mapping the day's situation →
   ranked technique(s) → gear class. The generated `species/` index badges the
   cases you can get wrong (`**[Baja only]**`, `**[SoCal only]**`); the full
   `regions`/`waters` values are in each note's front matter.
4. **Resolve gear + spread** against the active [profile](../profiles/README.md). No
   profile → class terms per the [gear-class lexicon](../tackle/gear-classes.md);
   with one → owned gear within the boat envelope. **Never recommend gear the
   angler has not said they own**, and when a class the plan calls for has no
   match in their inventory, **name the gap** — "the 40-fathom stop wants a heavy
   yo-yo iron and I don't see one in your box" — rather than substituting
   something that doesn't fish the same way.

## Conditions sources

- **Role:** [BightSST](https://bightai-api.onrender.com) is the system of record
  for *conditions*; this KB *references* it and never duplicates it.
- **Where endpoint detail lives:** [`config/endpoints.md`](../config/endpoints.md)
  — endpoint table, fallback ladder, source-validity rules, last-verified date.
  Stated there and nowhere else; an endpoint fact repeated here is a fact that
  survives a fix.
- **Doctrine — an empty layer is missing data, not a zero.** Chlorophyll is
  reported every run, or its absence is named.
- **Doctrine — distrust single-source SST extremes; cross-check models.** A
  known `goes_west_composite` window discrepancy and a cloud-contaminated NRT
  max (96.6 °F) mean single-source SST outliers are treated with suspicion.

## Supporting notes

- [Trip-length selection](trip-length-selection.md) — the upstream "which
  trip do I book" call (one-day vs. multi-day), before this protocol starts.
- [Search & glassing](search-and-glassing.md) — how to run the day and read sign.
- [Electronics & sounder](electronics-and-sounder.md) — finding fish on the meter.
- [Report reading & forecasting](report-reading-and-forecasting.md) — aging
  reports, advection, coverage bias.
- [Fleet intelligence](fleet-intelligence.md) — reading VHF chatter and
  fleet/AIS activity, and why they carry different trust.
- [Species routers](../species/README.md) — enter here to map situation → technique → gear.


<!-- backlinks:start -->
## Linked from

- [<Your Boat>](../profiles/_template/boat.md)
- [<Your> Spots](../profiles/_template/spots.md)
- [April](../seasonal/april.md)
- [August](../seasonal/august.md)
- [Current Diagnostics](../conditions/current-diagnostics.md)
- [ENTRY — SoCal Boat-Day Skill](../skills/socal-boat-day/ENTRY.md)
- [February–March](../seasonal/february-march.md)
- [Fleet Intelligence](fleet-intelligence.md)
- [June–July](../seasonal/june-july.md)
- [May](../seasonal/may.md)
- [Moon](../conditions/moon.md)
- [November–December](../seasonal/november-december.md)
- [October](../seasonal/october.md)
- [Regions & Waters — the gating vocabulary](../locations/regions.md)
- [Report Reading and Forecasting](report-reading-and-forecasting.md)
- [Sea State](../conditions/sea-state.md)
- [September](../seasonal/september.md)
- [Southern California Bight](../locations/socal-bight.md)
- [Tide and Slack](../conditions/tide-and-slack.md)
- [Trip-Length Selection — One-Day vs. Multi-Day Offshore Trips](trip-length-selection.md)
- [Upwelling and Turnover](../conditions/upwelling-and-turnover.md)
- [Water Color](../conditions/water-color.md)
- [Water Regimes](../conditions/water-regimes.md)
- [Water Temperature](../conditions/water-temperature.md)
- [Year-Anniversary Prior](../seasonal/year-anniversary-prior.md)
<!-- backlinks:end -->
