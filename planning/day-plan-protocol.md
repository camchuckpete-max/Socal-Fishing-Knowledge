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

> **Build status:** this is the navigation spine (step 0). Step 1 enriches each
> step with direct links to the specific `conditions/`, `seasonal/`, and
> species router notes as they land.

## The four steps

1. **Pull conditions.** From [BightSST](https://bightai-api.onrender.com), per
   fishing zone and along the transit route, observed **and** forecast: per-spot
   SST + chlorophyll, wind/swell/current. (BightSST read endpoints are open /
   no-auth; expect Render free-tier cold starts of 30–60 s.)
2. **Apply priors + interpretation layers.** Weight zones and set timing (moon,
   tide windows) using the [seasonal priors](../seasonal/) calendar and the
   [conditions layers](../conditions/). Age the intel with report-reading &
   forecasting (advection, coverage bias — added in step 1).
3. **Resolve species + technique.** Enter through the [species routers](../species/):
   each maps the day's situation → ranked technique(s) → gear class.
4. **Resolve gear + spread** against the active [profile](../profiles/). No
   profile → class terms; with one → owned gear within the boat envelope.

## Conditions sources (BightSST)

- **Role:** BightSST is the system of record for *conditions*; this KB
  *references* it and never duplicates it.
- **Endpoints:** read endpoints open/no-auth; admin behind a Bearer key.
- **Cold-start caveat:** Render free tier, 30–60 s cold starts.
- **Doctrine — distrust single-source SST extremes; cross-check models.** A
  known `goes_west_composite` window discrepancy and a cloud-contaminated NRT
  max (96.6 °F) mean single-source SST outliers are treated with suspicion.

## Supporting notes

Added in step 1: search & glassing, electronics & sounder, and report reading &
forecasting (all under [planning/](../planning/)).


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
