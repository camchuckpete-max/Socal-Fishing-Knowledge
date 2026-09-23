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
- 28 species-technique spin-outs; 57 relocations executed, 3 contested.

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

**1. It manufactured its own over-claims.** 1,537 `contradicted-by-source`
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
other 1,536.

## Ledger repairs, 2026-09-23

Three structural defects were fixed before this document could be approved
against. They move the headline counts by two rows.

- **One ledger row was invisible.** A lost newline had fused
  `locations/hidden-reef-170.md`'s MPA row onto the front of
  `locations/la-270-286.md`'s overnight-boat row, so every row-walker read them
  as one. Split. That is where the extra `contradicted-by-source` comes from.
- **The Tanner/Cortez row is re-opened.** It sat in **Resolved** reading
  "resolved by geometry… no figure was wrong" while the verifier had overturned
  exactly that on 2026-09-02: `nQvJnfb5jQ4` states the 90 mi figure **of Cortez
  by name**, inverting the near-end/far-end assignment the resolution rested on.
  A reader of the ledger alone would have concluded it was closed. Moved back to
  the live table, marked for a ruling.
- **A stray blank line** inside the live table split it into two blocks for
  naive parsers. Removed. Every live row now parses at exactly five cells.

## What GATE B actually needs from you

- **83 real judgment calls** of 137 escalations. The other 54 are noise: 38
  guard-reverts already handled, 11 check-note failures, 5 subagent failures.
  A narrower cut — entries whose text names you explicitly — gives 61.
  (Corrected 2026-09-23: this line previously read "74 of 135", which
  reconciled with no cut of the file. `grep -c '^## ' sources/escalations.md`
  is 137; the category histogram is in `sources/judgment-calls.md`.)
- **The ledger cannot be reviewed raw.** 2,128 live rows. Triage by page type is
  the only workable approach — 813 flags on 77 zone/region pages is a
  correction job, not an adjudication job.
- **`verify-external.yml` has never run.** 299 rows tagged, 0 verified.
- `judgment-calls.md` now enumerates all 83 open calls by category. This
  document is the coverage summary CLAUDE.md asks for at GATE B; that one is
  the judgment-calls list it asks for alongside.

## Recommendation

Do not merge yet. Two paths:

- **A (recommended):** merge the ladder, the evidence layer and the v2 skeletons
  — they are sound — but run a **correction pass over the 77 zone/region pages
  and the 23 routers**: each flagged claim rewritten to what the source actually
  says, the guard extended to conserve numeric specifics so the knife-jigs
  failure cannot recur, and the 166 dropped parameters restored from the old
  notes. Then GATE B on a KB whose new prose is as trustworthy as its old.
- **B:** merge now with all 1,537 flags in place. Honest, but every zone page
  reads with ten warnings on it, and a day plan built on one inherits them.

## The blind head-to-head

The five prompt tests above were run by hand against the diffs. They were then
re-run blind — 21 prompts, answered by a planning session confined to each of
three pinned checkouts (batch 2, batch 3, the review), scored by a judge that
never saw which version it was reading. The full record and the verdict are in
[Head-to-head prompt tests](prompt-tests-2026-09-09/README.md), and the
browsable side-by-side version is
[here](https://claude.ai/code/artifact/7a59971f-3762-4857-ba9c-e85b7c8ef68e).

The headline: **the review won 18 of 21, batch 3 won 3, batch 2 won none**, and
the review's answer never scored below the top mark in any prompt — all three of
its losses were point-ties broken on a narrow stated edge. The rubric ceilinged
(352 of 378 scores were a full 2/2), so read the wins rather than the means.
**All five tests above agree in direction with their blind counterparts**, and
two — the sounder and Tanner Bank — come back better than the diff-reading
predicted.

The review is alone at a perfect 2.00 on both `honest` and `actionable`: being
more careful did not cost it usability. Its one sub-2 score in 126 is #8's bare
two-hook cap with no jurisdiction or as-of — a miss **all three versions** made,
so it is a standing gap in the regulatory register, not damage the review did.


<!-- backlinks:start -->
## Linked from

- [Judgment calls](judgment-calls.md)
<!-- backlinks:end -->
