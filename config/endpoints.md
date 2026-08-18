---
type: planning
tags: [endpoints, bightsst, conditions, fallback, api, config]
sources: [cameron]
confidence: high
---

# Conditions Endpoints & Fallback Ladder

The single source of truth for **where conditions data comes from**. The
distributed [`socal-boat-day`](../skills/socal-boat-day/ENTRY.md) skill cannot be
edited after it ships, so it carries no endpoints — it reads them here. Fix a
broken endpoint in this file and every installed copy picks up the fix on its
next run.

**Last verified: 2026-08-18.** Re-verify before trusting any row below; the
verification commands are at the bottom.

## BightSST — primary

Frontend `bightsst-frontend.onrender.com` is backed by:

    https://bightai-api.onrender.com

Read endpoints are open, no auth. Admin endpoints require a Bearer key and
correctly return 401. Live machine-readable spec: `/openapi.json`.

| Endpoint | Use |
| --- | --- |
| `/api/v1/metadata` | Run status, `sources_available`, `chlorophyll_coverage_pct`. **Read this first every run.** |
| `/api/v1/available-dates` | Which dates have data. Gaps happen. |
| `/api/v1/point-value?lat=&lon=&layers=&source=` | Per-spot SST / chlorophyll. `layers` is comma-separated. |
| `/api/v1/frontness/value?lat=&lon=` | Break strength at a point (°F/nmi) with a coherence figure. |
| `/api/v1/frontness/stats`, `/api/v1/sst-stats` | Field-wide statistics. |
| `/api/v1/breaks` | Detected breaks. |
| `/api/v1/upwelling` | Upwelling zones. |
| `/api/v1/named-features` | Named feature lookup. |
| `/api/v1/bathymetry-contours` | Depth contours. |
| `/api/v1/acspo-fronts` | ACSPO front product. |
| `/api/v1/context` | Combined context payload — moon, tide predictions, per-source stats. **Its wind is field-wide and it carries no swell:** it returns the same wind and the same tide station whatever lat/lon you pass (verified 2026-08-18 at two points 130 nmi apart). Never use it for per-spot wind. |
| `/api/v1/goes-west-meta` | Composite-window detail for the GOES field. |
| `/api/v1/manifest` | Run manifest. |
| `/api/v1/health` | Liveness. |

Overlay endpoints (`/sst-overlay`, `/chlorophyll-overlay`,
`/bathymetry-overlay`) serve map imagery — not useful for numeric planning.

### Rules that keep this from lying to you

These are not hypotheticals. Each was observed live on 2026-08-17.

- **Trust `/metadata` → `sources_available` over `/sst-sources`.** The two
  contradict each other. `/sst-sources` reported MUR as available while carrying
  an upstream connection error, with statistics identical to the GOES field
  including a 0.4555 valid-pixel fraction — a gap-filled L4 product cannot be 45%
  valid. It was serving GOES data under the MUR label.
- **Always pass `source` explicitly to `point-value`.** It defaults to `mur`,
  and when MUR hasn't ingested, the default errors outright. Read
  `sources_available` and pass an ID that is actually true.
- **Source IDs in the parameter documentation are not the real IDs.** The docs
  list `mur, acspo, viirs, geopolar, goes_west`; the working ID on 2026-08-17 was
  `goes_west_composite`. Discover IDs from `/metadata`, never from the docs.
- **Missing data arrives dressed as success, in at least five shapes.** All were
  observed live; none of them is a reading:
  1. `{"values":{}}` — the requested layer simply isn't there (BightSST chlorophyll).
  2. A **partial** payload: `layers=sst,chlorophyll` returns only `sst`, with no
     error. This is the dangerous one — the response looks complete. Check that
     every layer you asked for came back by name.
  3. `null` fields plus a friendly note: `"frontness":null … "note":"No data at
     this location"`.
  4. A well-formed series that is entirely `null` with units `"undefined"` —
     what `marine-api.open-meteo.com` returns if you ask it for wind.
  5. `MM` — NDBC's own missing marker in the realtime text files.
- **Check `chlorophyll_coverage_pct` before reporting chlorophyll.** It was 0.0
  on 2026-08-17 and the overlay 404'd. Chlorophyll is a standing requirement of
  every plan, so when BightSST has none, go to the fallback rather than dropping
  the layer.
- **Check the run date before anything else.** `/metadata` carries `date` and
  `run_finished_utc`. The pipeline can stall: on 2026-08-18 both still pointed at
  the 2026-08-17 run serving 2026-08-16 data, so a plan built that day was using
  two-day-old satellite data. Compare `date` to today and **say the age out loud
  in the plan** whenever it is more than a day behind.
- **`frontness/value` mislabels its source.** With no `source` parameter it
  returns `"source":"mur"` — an id `point-value` rejects as unknown — while
  serving numbers identical to an explicit `goes_west_composite` request
  (verified 2026-08-18). Pass `source` here too, and never quote its default
  label as provenance.
- **Cold starts.** Free-tier hosting sleeps, and the first call after it sleeps
  can take 30–60 s. It is not the usual case — a warm instance answered in 0.78 s
  on 2026-08-18. Retry once with a long timeout before calling it down.

### Known upstream failure

BightSST's ingest of `coastwatch.pfeg.noaa.gov` was failing on 2026-08-17,
which is what knocked out MUR and chlorophyll. That ERDDAP host was reachable
from elsewhere at the same time, so the fault was on the pipeline's side, not
NOAA's. Practical consequence: **the fallback below is not a backup for those
layers right now — it is the only working path.**

Re-confirmed 2026-08-18: that ERDDAP host answered normally from outside while
BightSST still reported `Network is unreachable` for it. The fault stays on the
pipeline's side.

This also makes the fallback **mandatory for the cross-check doctrine**, not
optional. With a single SST source available, BightSST cannot cross-check
itself — the second opinion has to come from ERDDAP. On 2026-08-18 the two
agreed within 1.19 °F at the same point and date, while the field max sat
15.63 °F above p98: the cloud-contamination signature the doctrine warns about,
live in that day's data.

## Fallback ladder

Work down. All hosts verified reachable and keyless on 2026-08-18.

| Layer | Primary | Fallback |
| --- | --- | --- |
| SST | BightSST `point-value` | NOAA ERDDAP — `coastwatch.pfeg.noaa.gov/erddap`, then `coastwatch.noaa.gov/erddap` |
| Chlorophyll | BightSST `point-value` | NOAA ERDDAP VIIRS ocean colour — **check each candidate's last time step before choosing.** On 2026-08-18 `nesdisVHNSQchlaDaily` (science quality) was freshest at 10 days old and returned a value; `nesdisVHNchlaDaily` (near-real-time — the obvious pick) was 40 days stale and `null` at the same point; `nesdisVHNnoaa20chlaDaily` was 59 days stale. |
| Breaks / frontness | BightSST `frontness/*` | Compute from an ERDDAP SST grid — sample a ring and a transect, difference in °F per nautical mile |
| **Wind** forecast, per coordinate | `api.open-meteo.com/v1/forecast` — `wind_speed_10m`, `wind_gusts_10m`, `wind_direction_10m` | `api.weather.gov` marine zones |
| **Swell / waves** forecast, per coordinate | `marine-api.open-meteo.com/v1/marine` — `wave_height`, `wave_period`, `swell_wave_height`, `wind_wave_height` | `api.weather.gov` marine zones |
| Wind & swell observed | `www.ndbc.noaa.gov` realtime station text | `api.weather.gov` observations |
| Tides & tidal current | NOAA CO-OPS | — |
| Coastal warnings | `api.weather.gov` | — |

Confirm dataset and parameter names from each service's own documentation at
request time. ERDDAP dataset IDs change; a URL remembered from a previous run is
a guess — the IDs named above are a starting point, not a promise.

ERDDAP discovery takes three calls and no guessing:
`/erddap/search/index.json?searchFor=…` to find the dataset,
`/erddap/info/<id>/index.json` for its dimensions and variables, then
`/erddap/griddap/<id>.json?<var>[(last)][(lat)][(lon)]` for the value. **Follow
redirects** — ERDDAP answers with a 302 to its own canonical paginated URL, and
a client that doesn't follow it sees an empty body and reads the host as down.

**`(last)` does not mean recent.** It is the newest time step that dataset
holds, which can be weeks old. Read the timestamp that comes back and report
it alongside the value.

**Per-spot resolution is required.** Wind and swell get queried at every
candidate spot and at points along the route out and back. A single coastal
station cannot describe a trip that crosses 40 miles of open water.

## Verifying this file

```bash
curl -s https://bightai-api.onrender.com/openapi.json | python3 -c \
  "import json,sys; d=json.load(sys.stdin); [print(p) for p in d['paths']]"

curl -s https://bightai-api.onrender.com/api/v1/metadata
```

`/metadata` answers the two questions that matter before any plan: which SST
sources are real today, and whether chlorophyll exists.

<!-- backlinks:start -->
## Linked from

- [Day-Plan Protocol](../planning/day-plan-protocol.md)
- [ENTRY — SoCal Boat-Day Skill](../skills/socal-boat-day/ENTRY.md)
<!-- backlinks:end -->
