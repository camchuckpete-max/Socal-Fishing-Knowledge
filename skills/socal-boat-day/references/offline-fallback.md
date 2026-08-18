# Offline Fallback

Use only when the knowledgebase repo can't be fetched. **Tell the user the plan
is reduced and why.** This file is a floor, not a substitute — it has no
seasonal priors, no species routers, and no local knowledge.

## Sources that need no key

- **Buoys (observed wind, swell, water temp)** — `www.ndbc.noaa.gov`, realtime
  text files per station. Nearest-station data, so it describes the buoy's
  location, not the spot.
- **Wind forecast by coordinate** — `api.open-meteo.com/v1/forecast`
  (`wind_speed_10m`, `wind_gusts_10m`, `wind_direction_10m`). **Not** the marine
  host: asking that one for wind returns a well-formed response whose values are
  all `null`, which reads as success. Query per spot and along the route.
- **Swell and waves by coordinate** — `marine-api.open-meteo.com/v1/marine`
  (`wave_height`, `wave_period`, `swell_wave_height`, `wind_wave_height`).
- **Coastal forecast and warnings** — `api.weather.gov`.
- **Satellite SST and chlorophyll** — NOAA ERDDAP servers at
  `coastwatch.pfeg.noaa.gov` and `coastwatch.noaa.gov`.
- **Tides and tidal currents** — NOAA CO-OPS.

Confirm exact dataset and parameter names from each service's own documentation
at request time rather than assuming a URL shape from memory.

## Reduced procedure

1. Ask which spots or general area they're considering, and their departure and
   return times.
2. Pull wind and swell — forecast and observed — **for each spot and along the
   transit route**. Say plainly whether the day is fishable for their boat and
   where the ride gets bad.
3. Pull SST and chlorophyll at each spot. Report values with their observation
   date and note gaps from cloud cover.
4. Note tide and current timing.
5. Stop before doctrine. Do not improvise seasonal patterns, species behavior,
   or technique selection to fill the hole where the knowledgebase should be.
   Give conditions and the sea-state call, resolve gear only in broad class
   terms against what they own, and say the rest needs the repo.

Then retry the repo — and before you call it unreachable, try **both** hosts:
`github.com/camchuckpete-max/Socal-Fishing-Knowledge/blob/main/<path>` and the
raw mirror `raw.githubusercontent.com/camchuckpete-max/Socal-Fishing-Knowledge/main/<path>`.
One of them failing is not the repo being down. Outages are usually short.
