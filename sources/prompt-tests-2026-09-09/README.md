# Head-to-head prompt tests — 2026-09-09

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.24 | 11.57 | 11.95 |
| found | 1.86 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.86 | 1.81 | 1.95 |
| honest | 1.9 | 1.86 | 2 |
| actionable | 1.62 | 1.9 | 2 |
| **wins** | 0 | 3 | 18 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 1 | 3 | 1 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | 11.4 | 11.6 | 12 |
| Gear | 11 | 11.5 | 11.75 |
| Technique | 11 | 11.75 | 12 |
| Finding fish | 11.5 | 11.5 | 12 |
| Conditions & season | 11.5 | 10.5 | 12 |
| Rigging, bait, care | 11 | 12 | 12 |
| Honesty | 11.5 | 12 | 12 |

**Browsable version:** [Head-to-Head Prompt Tests](https://claude.ai/code/artifact/7a59971f-3762-4857-ba9c-e85b7c8ef68e) — the same record with all three answers side by side per prompt.

## Verdict

**The review won 18 of 21 prompts. Batch 3 won 3. Batch 2 won none.** More
telling than the wins: the review's answer **never scored below the top mark in
any of the 21 prompts**, and it took a perfect 12/12 in 20 of them. All three of
its losses were point-ties (12–12, 12–12, 11–11) that the judge broke on a
narrow stated edge, not defeats.

The mean totals point the same way — B2 11.24, B3 11.57, NOW 11.95 — but they
are nearly useless on their own: **352 of 378 criterion scores (93%) were a full
2/2**, so the rubric sat at its ceiling. Where a rubric ceilings, count wins.

### A correction on the record

An earlier version of this document reported 13/6/2 and a headline finding that
Tanner Bank was a case of page growth without answer quality. That was drawn
from an **incomplete first pass** of this run: one agent (the review's answer to
prompt 18) failed, the workflow restarted the whole graph, and the judge for
prompt 18 in that first pass recorded "A returned nothing and cannot be scored."
The numbers here come from the complete pass — 84 agents, no failures. **The
Tanner finding does not survive it**; the review won that prompt outright.

### What batch 3 did, and what the review did

Separating them was the point of running three columns.

**Batch 3 (the ingest) fixed reach.** Batch 2's weaknesses are absences: 1.86 on
`found`, 1.62 on `actionable`, and 16 of the 26 sub-2 scores in the test. It is
the only version a judge said had *nothing* to answer with — no standalone
slow-trolling note (#11), nothing connecting a rail rod's name to the
rail-fighting mechanic (#9). Batch 3 closed those, and on `found`, `specific`
and `sourced` it is already perfect.

**The review fixed geography, provenance and honesty.** That is where it
separates from batch 3, and it shows in what the sessions could reach:

| per answer | B2 | B3 | NOW |
|---|---:|---:|---:|
| notes cited | 21.8 | 21.7 | 23.0 |
| video ids cited | 19.8 | 25.0 | 29.4 |
| gaps admitted | 9.7 | 10.1 | 13.8 |
| answer length (chars) | 16,296 | 16,254 | 16,491 |

| across all 21 answers | B2 | B3 | NOW |
|---|---:|---:|---:|
| `locations/` notes cited | 29 | 41 | 91 |
| `evidence/` files cited | 0 | 0 | 17 |

The location layer is the largest single gain — 91 citations against 41, because
the geo tier gave the KB spot and zone pages where batch 3 had a lexicon. The
evidence layer is a step change of a different kind: 17 citations against a
structural zero, because the split did not exist before.

The review is alone at 2.00 on both `honest` and `actionable`, which is the
finding that matters most. Being more careful did not cost it usability. Across
all 63 answers and all three versions there were **zero `fabricated_specifics`
and zero `bluffed` flags** — no version invents. The separation is self-audit:
on #10 the judge credited the review for surfacing the source's own hedge and
naming an internal conflict, moves only possible because the review wrote the
flags in.

### Where the review is weakest

**One sub-2 score in 126.** On #8 it states the US two-hook jig cap as a bare
legal claim with no jurisdiction, no as-of and no verify-current — exactly what
the content rules exist to prevent. Worth noting before treating it as a review
regression: the judge recorded that **all three versions made that same miss**,
so it is a standing gap in the KB's regulatory register, not damage the review
did.

The three losses are worth reading rather than counting. On cabrilla (#5) and
slow-trolling (#11) the review tied batch 3 at 12–12 and lost on the judge's
stated edge — batch 3 gave the decision half of the question a tighter frame. On
#8 the tie was 11–11.

The one raw count that runs against the review is small and mixed:
`regulation_without_asof` fired once for batch 2, **three times for batch 3**,
and once for the review.

### The five prompts that overlap the coverage summary

| coverage-summary test | its verdict | blind prompt | blind winner |
|---|---|---|---|
| yellowtail at the Coronados | win | #1 | NOW |
| blowing 20 kt — where can I still fish | win | #16 | NOW |
| finding bluefin on the sounder | mixed | #14 | NOW |
| how far is Tanner Bank, what's there | exists; trust carefully | #4 | NOW |
| gear for surface iron | already good | #6 | NOW |

All five agree in direction, and two — the sounder and Tanner Bank — come back
better than the diff-reading predicted. The eddy row checks out on the text, not
just the score: only the review's answer carries your adjudication, "everything
east of Catalina and San Clemente," framed as "a lee, not a list of banks."
Batch 2 and batch 3 both still answer "the inner San Diego banks and tuna
grounds."

### What this does not settle

The judge scored answers, not truth. It cannot see the 39-in-40 over-claim rate
the coverage summary found by reading diffs, and a fluent, well-cited over-claim
scores 2/2 here. **This test says the review made the KB reach further, cite
harder, admit more, and stay just as usable; it does not say the review made the
KB more correct.** The coverage summary is still the document that speaks to
correctness, and it is the one that should drive the GATE B decision.


## How this record was derived

The run failed one agent partway (the review's answer to prompt 18), restarted
the whole graph, and finished clean on the second pass — 84 agents, no failures.
Every number here is taken from that complete pass, read back out of the
workflow journal rather than from any summary. Where a label carries two
results, the later (complete-pass) one is used, and each judge's verdict stays
paired with the answers that judge actually saw.

## The record, by category

Every prompt, all three answers verbatim, the judge's scores, reasons and the A/B/C mapping. Split by category because a single file of the whole record is too large for GitHub to render.

| file | prompts | winners |
|---|---|---|
| [Trip planning](trip.md) | #1, #2, #3, #4, #5 | #1 **NOW**, #2 **NOW**, #3 **NOW**, #4 **NOW**, #5 **B3** |
| [Gear](gear.md) | #6, #7, #8, #9 | #6 **NOW**, #7 **NOW**, #8 **B3**, #9 **NOW** |
| [Technique](technique.md) | #10, #11, #12, #13 | #10 **NOW**, #11 **B3**, #12 **NOW**, #13 **NOW** |
| [Finding fish](finding.md) | #14, #15 | #14 **NOW**, #15 **NOW** |
| [Conditions & season](conditions.md) | #16, #17 | #16 **NOW**, #17 **NOW** |
| [Rigging, bait, care](rigging.md) | #18, #19 | #18 **NOW**, #19 **NOW** |
| [Honesty](honesty.md) | #20, #21 | #20 **NOW**, #21 **NOW** |
