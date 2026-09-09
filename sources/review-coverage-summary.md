# Review coverage summary — did the editorial run improve the knowledgebase?

The GATE B coverage summary for the 2026-08 editorial review
(`sources/plan-review.md`). Written 2026-09-09 after the worklist drained on
2026-09-02. Every figure below was measured against three commits — batch 2
`540ea4a`, batch 3 / pre-review `1e66a92`, and the review branch tip — with
the scripts in `scripts/review/` and one-off read-only checks; nothing here
is estimated. The judgment calls it raises are listed in
`sources/judgment-calls.md`.

Comparison points: **batch 2** merged at `540ea4a` (08-17); **batch 3** merged at
`5ff787b` and the review branched from `1e66a92` (08-23), so batch 3 is the
pre-review state; **the review** ran 08-23 → 09-02 and is at HEAD. Everything
below was measured read-only against those three commits.

## Verdict

**Yes on structure and coverage, decisively. No on the accuracy of what it
added.** The run built the geographic ladder, the evidence layer, and the v2
skeletons, and it preserved pre-existing content almost perfectly. But it also
wrote roughly 1,500 claims its own sources do not support — nearly all on the
new zone and region pages — and then flagged every one of them. A new angler
gets far better navigation and a far more honest KB than before; per-claim,
the new prose is less trustworthy than the old.

It should not merge as-is. The structure is worth keeping; the zone/region prose
needs a correction pass first.

## The three states

| | batch 2 | batch 3 (pre-review) | post-review |
|---|---|---|---|
| knowledge notes | 116 | 259 | **732** + 272 evidence |
| lines | 24.9K | 59.3K | **143.9K** |
| species | 21 | 24 | 53 (23 routers + 28 species-technique + 1 zone-guide + 1 merged away) |
| locations | 7 | 13 | **454** |
| tackle | 5 | 86 | 86 |
| techniques | 21 | 49 | 50 |

Batch 3 was the tackle-heavy ingest (5 → 86). The review was the geography and
structure pass: of its +473 notes, **441 are `locations/`**.

## What it built

- **The ladder:** 2 jurisdictions, 5 regions, 76 zones, **371 spot pages**, every
  spot with a charted position traced to `sources/spot-lists.md` (1,282
  positions, 0 unsourced).
- **The evidence layer:** 272 files. `species/evidence/yellowtail.md` has 83
  one-line entries citing 89 distinct videos, each with channel, date and place.
  This did not exist before.
- **Layout v2:** 738 notes with infoboxes and CI-validated skeletons.
- **Regulations sections:** 0 → 23 species routers, real ones — jurisdiction,
  as-of stamp, verify-current — 17–33 lines each.
- **Sonar guidance:** species notes carrying fathom/sounder terms 24 → 42.
- 28 species-technique spin-outs; 58 relocations executed.

## What it preserved

- **Cites: 500 of 500** on the original routers, counted across the note +
  evidence pair. `bluefin-trolling.md` is gone because you asked for the merge;
  all 14 of its cites are in `bluefin-tuna-trolling.md`. KB-wide distinct cite
  tokens rose 8,097 → 10,301.
- **All 23 surviving routers** keep Situations→techniques, Finding them, Gear
  summary.
- **All four adjudications** survived their rewrites verbatim, markers intact.
- **The 156 gazetteer skips are all legitimate** — 53 bare-number spots, 4
  no-ops, and 99 individually-reasoned aliases, duplicates, area-level names
  and linear features ("the Ridge crosses five built zones"). No coverage lost.

## What it got wrong

**1. It manufactured its own over-claims.** 1,536 `contradicted-by-source`
flags. In a 40-row sample, **1 predates the review; 39 were introduced by it**
(26 on new pages, 13 on rewrites — three hand-checked, all confirmed).

Where they land, per page:

| new page type | pages | flags | flags / page |
|---|---|---|---|
| region | 5 | 91 | **18.2** |
| zone | 72 | 722 | **10.0** |
| jurisdiction | 2 | 7 | 3.5 |
| spot (mostly mechanical stubs) | 362 | 180 | 0.5 |

Plus 222 on rewritten species routers and ~110 on rewritten technique/rig/lure
notes. **813 of the 1,000 location flags are on 77 prose pages.** The spot stubs
are clean because they say almost nothing.

**2. The mechanism is cite-stretching, not fabrication.** Three sampled rewrite
flags, all with cites that were already in the old note:
- `dorado.md` — a tactic cited to three videos; the third never states it.
- `wahoo.md` — "wire on every presentation"; the source wires two of three.
- `striped-marlin.md` — "finning" added to a list the source gives as
  "sleeping, tailing, slashing."
The pilot shows it in miniature: the rewrite added a bait-"shattering" read to
yellowtail's Finding-them section, cited to a La Paz video — Sea of Cortez,
not offshore SoCal. Flagged.

**3. It dropped specifics.** CLAUDE.md: *"Preserve specifics exactly… never
smooth numbers into generalities."* Across 205 rewritten notes, **166 of 2,974
distinct numeric parameters are gone** from the note + evidence pair (5.6%).
110 notes lost none; `lures/knife-jigs.md` lost **45%** (53 → 29 — gram
ranges like 100–150g / 120–160g collapsed), `hoop-netting.md` 28% (depth
bands), `sliding-sinker.md` 26% (line classes, sinker weights). **The guard
does not check this** — it conserves cites and observations, not parameters.

**4. 203 stale anchors** (cosmetic; the link lands on the right note).

## Prompt tests — what a new angler actually gets

| question | before (batch 3) | after (review) | |
|---|---|---|---|
| *How do I catch yellowtail at the Coronados?* | no zone page; 11 lines in the router | 173-line zone page + a zone-guide: Mexican-waters gate, the program, reading the day, rigs & gear, how it differs from neighbours | **win** |
| *Blowing 20 kt outside — where can I still fish?* | "inner SD banks / tuna grounds (5/26/22)" | your adjudicated lee — everything east of Catalina/San Clemente, with the north-wind mechanism and the 425 | **win** |
| *How do I find bluefin on my sounder?* | depths buried in prose beside ASR-garbled names | clean depth table (30–50 fm sounded, 50–80 fm bank nights) — **but 3 of 5 rows flagged** | mixed |
| *How far is Tanner Bank, what's there?* | no page; three passing mentions | 533-line page with charted position — **33 flags** | exists; trust carefully |
| *Gear for surface iron?* | 653 lines | 606 lines, `gear_classes` infobox added, content unchanged | fine — was already good |

## The one I got wrong

I closed the Tanner/Cortez "90 vs 110 mi" row as the two ends of an 18-mile
complex. The verifier read the transcript: `nQvJnfb5jQ4` says "90 Mi off the
coast of Long Beach" **about Cortez by name**, inverting my assignment. It's
escalated to you, correctly. The pipeline caught me the same way it caught the
other 1,535.

## What GATE B actually needs from you

- **74 real judgment calls** (of 135 escalations; 38 are guard reverts already
  handled, 16 are infra noise).
- **The ledger cannot be reviewed raw.** 2,126 live rows. Triage by page type is
  the only workable approach — 813 flags on 77 zone/region pages is a
  correction job, not an adjudication job.
- **`verify-external.yml` has never run.** 299 rows tagged, 0 verified.
- `judgment-calls.md` has two entries. This document is the coverage summary
  CLAUDE.md asks for at GATE B.

## Recommendation

Do not merge yet. Two paths:

- **A (recommended):** merge the ladder, the evidence layer and the v2 skeletons
  — they are sound — but run a **correction pass over the 77 zone/region pages
  and the 23 routers**: each flagged claim rewritten to what the source actually
  says, the guard extended to conserve numeric specifics so the knife-jigs
  failure cannot recur, and the 166 dropped parameters restored from the old
  notes. Then GATE B on a KB whose new prose is as trustworthy as its old.
- **B:** merge now with all 1,536 flags in place. Honest, but every zone page
  reads with ten warnings on it, and a day plan built on one inherits them.


<!-- backlinks:start -->
## Linked from

- [Judgment calls](judgment-calls.md)
<!-- backlinks:end -->
