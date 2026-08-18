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

**Last verified: 2026-08-17.** Re-verify before trusting any row below; the
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
| `/api/v1/context` | Combined context payload. |
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
- **An empty `values` object is missing data, not a zero.** Requesting a layer
  the pipeline doesn't have returns `{}` with a 200 status. Silent.
- **Check `chlorophyll_coverage_pct` before reporting chlorophyll.** It was 0.0
  on 2026-08-17 and the overlay 404'd. Chlorophyll is a standing requirement of
  every plan, so when BightSST has none, go to the fallback rather than dropping
  the layer.
- **Cold starts.** Free-tier hosting sleeps. First call can take 30–60 s. Retry
  once with a long timeout before calling it down.

### Known upstream failure

BightSST's ingest of `coastwatch.pfeg.noaa.gov` was failing on 2026-08-17,
which is what knocked out MUR and chlorophyll. That ERDDAP host was reachable
from elsewhere at the same time, so the fault was on the pipeline's side, not
NOAA's. Practical consequence: **the fallback below is not a backup for those
layers right now — it is the only working path.**

## Fallback ladder

Work down. All hosts verified reachable and keyless on 2026-08-17.

| Layer | Primary | Fallback |
| --- | --- | --- |
| SST | BightSST `point-value` | NOAA ERDDAP — `coastwatch.pfeg.noaa.gov/erddap`, then `coastwatch.noaa.gov/erddap` |
| Chlorophyll | BightSST `point-value` | NOAA ERDDAP (VIIRS ocean color) |
| Breaks / frontness | BightSST `frontness/*` | Compute from an ERDDAP SST grid — sample a ring and a transect, difference in °F per nautical mile |
| Wind & swell forecast, per coordinate | `marine-api.open-meteo.com` | `api.weather.gov` marine zones |
| Wind & swell observed | `www.ndbc.noaa.gov` realtime station text | `api.weather.gov` observations |
| Tides & tidal current | NOAA CO-OPS | — |
| Coastal warnings | `api.weather.gov` | — |

Confirm dataset and parameter names from each service's own documentation at
request time. ERDDAP dataset IDs change; a URL remembered from a previous run is
a guess.

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
