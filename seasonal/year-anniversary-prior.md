---
type: seasonal
tags: [prior, bluefin, yellowtail, historical, advection, water-state]
sources: [XLVUhV8DW64, cameron, Blh2BA-7Ono]
confidence: high
regions: [socal-bight]
waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]
layout: v2
regime: cooling
---

# Year-Anniversary Prior

**Regime: [fall fragmentation](../conditions/water-regimes.md)** — a location
prior WITHIN the regime, not a calendar rule (cameron); it is strongest while
that regime holds and weakens outside it.

**This is a prior — a pattern-layer heuristic, not current intel.** It sets
where to start looking, refined the moment you pull live
[BightSST](../planning/day-plan-protocol.md) conditions. The
[fall fragmentation regime](../conditions/water-regimes.md) recurs on roughly
the same schedule every year, and the bluefin route through it repeats with
it, so the same calendar week in prior years is a usable starting box. The
prior is only as good as the regime match: if the current year's water is
running early or late, shift the prior with the regime instead of reading the
calendar date literally.

## The prior — the bluefin route repeats year over year

The [bluefin](../species/bluefin-tuna.md) migration route repeats year over
year: "go back to this date last year and the year before — pretty close to
where they'll be" (`XLVUhV8DW64`). The same calendar week in prior years is
therefore a usable prior for where the fish are now.

- **Strongest in the fall fragmentation regime.** The route's repeatability
  tracks the [warm band's predictable retreat path](../conditions/water-regimes.md)
  as the coast cools — weight the anniversary prior most heavily during fall,
  least outside it.
- **Project the travel line rather than anchoring one point.** Line up recent
  catch positions and extrapolate the trend forward instead of treating a
  single same-date-last-year position as the answer, updating the projection
  day to day as new positions come in. ⚠ cite-unresolved: attributed to Capt.
  Duane Diego Mellor in the source note; no matching transcript found in the
  corpus.
- **Pair it with the advection model when projecting forward.** Open-water
  bluefin not holding structure move 10–15 nm overnight (`Blh2BA-7Ono`); see
  [report reading and forecasting](../planning/report-reading-and-forecasting.md).

This is a same-week historical prior, not a promise. After a full moon, or
late in the season when thinning boat coverage makes reports look like the
fish vanished, widen the search toward the same-date prior-year locations
rather than trusting report persistence — the fish relocate, they don't
disappear (`XLVUhV8DW64`).

## Water state vs the calendar — the decision rule

This prior is scoped to the fall bluefin route; it does not extend to
[yellowtail](../species/yellowtail.md). For yellowtail, water state — not the
calendar — is the decision variable: date and month don't predict them, they
follow water temperature and bait, and the bait follows temperature and
current, so any calendar pattern visible in a season's catch data is
downstream of water state, not a driver of it (cameron). See yellowtail's own
[water-state-vs-calendar decision rule](../species/yellowtail.md) for the full
framing.

The two stand unreconciled because they cover different fish and different
evidence: this prior is a bluefin-route heuristic from the corpus
(`XLVUhV8DW64`); the yellowtail model is Cameron's own read of his catch data
(cameron). The yellowtail model is attributed doctrine here, not a gate — let
live water state — [SST](../conditions/water-temperature.md),
[chlorophyll](../conditions/water-color.md),
[current structure](../conditions/current-structure.md), and
[upwelling / turnover](../conditions/upwelling-and-turnover.md) — always
override this prior as a starting box, for either species.

## Evidence

Trip reports and per-source provenance: [evidence file](evidence/year-anniversary-prior.md).


<!-- backlinks:start -->
## Linked from

- [Bluefin Tuna](../species/bluefin-tuna.md)
- [Evidence — Year-Anniversary Prior](evidence/year-anniversary-prior.md)
- [Evidence — Yellowtail](../species/evidence/yellowtail.md)
- [Moon](../conditions/moon.md)
- [Report Reading and Forecasting](../planning/report-reading-and-forecasting.md)
- [Southern California Bight](../locations/socal-bight.md)
- [Water Regimes](../conditions/water-regimes.md)
- [Yellowtail](../species/yellowtail.md)
<!-- backlinks:end -->
