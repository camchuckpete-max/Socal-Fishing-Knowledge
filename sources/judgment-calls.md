# Judgment calls

Decisions the review made that a human should see.

## Zone groupings — provenance (2026-08-24)

The zone carve-up was shaped by a FishDope daily report Cameron supplied on
2026-08-24, used as a STRUCTURAL reference only: how the fishery groups spots
into run-sized zones. Per his instruction, FishDope is **not** registered in
`sources/source-registry.md`, none of its report content was mined, and no
conditions or bite information from it entered the KB (BightSST is the system
of record for conditions; a day's bite is not knowledge).

The groupings are therefore attributed `(cameron)` — an editorial carve-up,
not a sourced claim. Zones were then derived primarily from the coordinates in
`sources/spot-lists.md`; see `scripts/review/build-geo-worklist.py`.


## Coverage summary and the merge recommendation (2026-09-09)

The run's coverage summary is
[`review-coverage-summary.md`](review-coverage-summary.md). Its judgment calls,
each of which needs Cameron:

- **Do not merge as-is.** The ladder, evidence layer and v2 skeletons are sound
  and conserved pre-existing content (500/500 router cites, all four
  adjudications, all 23 routers). The new zone/region prose is not: 813 of the
  1,000 location fact-check flags sit on 77 pages, ~10 per zone page, and a
  40-row sample found 39 of 40 over-claims were introduced by the review.
- **The rewrite pass dropped numeric specifics** — 166 of 2,974 across 205
  notes (5.6%); `lures/knife-jigs.md` lost 45%. The guard does not conserve
  parameters. Decide whether to restore from the pre-review notes and extend
  the guard before GATE B.
- **`verify-external.yml` has never run**; 299 ledger rows are tagged and
  waiting.
- **74 escalations are genuine judgment calls** (of 135; the rest are guard
  reverts already handled and infra noise).
- The Tanner/Cortez "90 vs 110 mi" resolution was overturned by the verifier
  and is escalated; Cameron to rule.


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
