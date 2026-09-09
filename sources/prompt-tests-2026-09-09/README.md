# Head-to-head prompt tests — 2026-09-09

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.1 | 11.81 | 11.81 |
| found | 1.86 | 2 | 2 |
| specific | 1.95 | 2 | 2 |
| sourced | 1.95 | 2 | 2 |
| scoped | 1.67 | 1.9 | 1.9 |
| honest | 1.95 | 1.95 | 2 |
| actionable | 1.71 | 1.95 | 1.9 |
| **wins** | 2 | 6 | 13 |  (ties: 0)
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 2 | 2 | 1 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | 11.4 | 11.8 | 11.6 |
| Gear | 11.25 | 12 | 11.75 |
| Technique | 11 | 11.75 | 12 |
| Finding fish | 11 | 12 | 11.5 |
| Conditions & season | 11 | 11.5 | 12 |
| Rigging, bait, care | 10.5 | 12 | 12 |
| Honesty | 11 | 11.5 | 12 |

## Verdict

**The review earned its keep, but the rubric could not see how much.** NOW won
13 of 21 prompts, batch 3 won 6, batch 2 won 2. The mean totals say something
different — B2 11.10, B3 11.81, NOW 11.81 — and that dead tie is an artifact,
not a result: **92% of the 378 criterion scores were 2/2**, so the rubric hit
its ceiling and stopped discriminating. Read the wins, not the means.

### What batch 3 did, and what the review did

Separating the two was the point of running three columns.

**Batch 3 (the ingest) fixed reach.** Every one of B2's weaknesses is an
absence: it scores 1.86 on `found` against a flat 2.00 for both later versions,
and it takes 19 of the 27 sub-2 scores in the whole test. B2 is the only version a judge
ever said had *nothing* to answer with — no standalone slow-trolling note (#11),
nothing connecting a rail rod's name to the rail-fighting mechanic (#9), no
small-boat translation for fish care (#19). Batch 3 closed those and closed them
completely; on `found`, `specific` and `sourced` it is already perfect and the
review cannot improve it.

**The review fixed geography, provenance and honesty.** This is where NOW
separates from B3, and it shows in what the sessions could actually reach:

| per answer | B2 | B3 | NOW |
|---|---:|---:|---:|
| notes cited | 20.9 | 20.4 | 23.9 |
| video ids cited | 20.0 | 21.9 | 26.5 |
| gaps admitted | 10.3 | 10.6 | 12.5 |
| answer length (chars) | 15,872 | 16,802 | 15,437 |

| across all 21 answers | B2 | B3 | NOW |
|---|---:|---:|---:|
| `locations/` notes cited | 25 | 42 | 106 |
| `evidence/` files cited | 0 | 0 | 20 |

NOW cites more notes, more sources and more of its own gaps in *fewer*
characters. The location layer is the largest single gain: 106 citations against
42, because the geo tier gave the KB spot and zone pages where B3 had a lexicon.
The judge saw it directly on #1 — NOW was "the only answer working from an
actual zone layer," while B2 "never names a single spot within a 13-mile island
chain." The evidence layer is a step change of a different kind: 20 citations
against a structural zero, because the split simply did not exist before.

`honest` is the one criterion where NOW is alone at 2.00. Across all 63 answers
and all three versions there were **zero `fabricated_specifics` and zero
`bluffed` flags** — the KB does not invent, in any version. The separation is in
self-audit. On #10 the judge singled out NOW for surfacing "the source's own
hedge," flagging a fathom figure "as absent from the transcript," and naming an
internal conflict — three moves that are only possible because the review wrote
the flags in.

### Where NOW is worse than B3

Eight losses, and they fall into two honest patterns.

**Carefulness crowding out execution (#2, #5, #10).** NOW took `actionable` = 1
twice. On the Dana Point blow-out (#2) the judge credited NOW with "the sharpest
epistemics" and then said plainly that "discipline costs it execution detail on
halibut, rockfish and the harbor fallback." On cabrilla (#5) NOW nailed the
region gate and then gave "almost no cabrilla execution — no depth ladder, no
reel ratio/line spec, no drag doctrine." The review taught the KB to say what it
does not know, and in these three answers that displaced saying what it does.

**Scope statements dropped (#8, #14).** NOW took `scoped` = 1 twice, and one is
a real defect: on #8 it asserts "US waters cap a jig at two hooks" with no
jurisdiction, no as-of and no verify-current — exactly the failure the content
rules exist to prevent, and B3 avoided it. On #14 the miss is softer: NOW gave
geographic context but never stated the notes' `regions`/`waters` gating, so a
judge could not tell an inshore day from an offshore one. Both are fixable in
the correction pass.

The regulation flag is the one place the raw counts favour the review anyway:
`regulation_without_asof` fired twice for B2, twice for B3, once for NOW.

### The five prompts that overlap the coverage summary

The coverage summary ran five prompts by hand, reading diffs. Four of the five
agree in direction with their blind-judged counterparts here.

| coverage-summary test | its verdict | blind prompt | blind winner | agrees |
|---|---|---|---:|---|
| yellowtail at the Coronados | win | #1 | NOW | yes |
| blowing 20 kt — where can I still fish | win | #16 | NOW | yes |
| finding bluefin on the sounder | mixed | #14 | B3 | yes |
| how far is Tanner Bank, what's there | exists; trust carefully | #4 | B2 | **no** |
| gear for surface iron | already good | #6 | NOW | yes |

The eddy row checks out on the text, not just the score: only NOW's answer
carries your adjudication — "everything east of Catalina and San Clemente,"
framed as "a lee, not a list of banks." B2 and B3 both still answer "the inner
SD banks and tuna grounds."

The exception is **#4 (Tanner/Cortez), the only prompt where the oldest version
beat both successors.** The coverage summary called that page a gain carrying 33
flags. The blind test is harsher: all three reached the same correct no-go, and
B2 won the second half by teaching the bank programs, while NOW "names the
night-jig and kite gaps and stops rather than teaching what happens out there."
A 533-line page did not produce a better answer than three passing mentions.
That gap between page growth and answer quality is the finding the diff-reading
could not surface.

### What this does not settle

The judge scored answers, not truth. It cannot see the 39-in-40 over-claim rate
the coverage summary found by reading diffs, and a fluent, well-cited over-claim
scores 2/2 here. **This test says the review made the KB reach further, cite
harder and admit more; it does not say the review made the KB more correct.**
The coverage summary is still the document that speaks to correctness, and it is
the one that should drive the GATE B decision.


## The record, by category

Every prompt, all three answers verbatim, the judge's scores, reasons and the A/B/C mapping. Split by category because a single file of the whole record is too large for GitHub to render.

| file | prompts | winners |
|---|---|---|
| [Trip planning](trip.md) | #1, #2, #3, #4, #5 | #1 **NOW**, #2 **B3**, #3 **NOW**, #4 **B2**, #5 **B3** |
| [Gear](gear.md) | #6, #7, #8, #9 | #6 **NOW**, #7 **NOW**, #8 **B3**, #9 **NOW** |
| [Technique](technique.md) | #10, #11, #12, #13 | #10 **B2**, #11 **B3**, #12 **NOW**, #13 **NOW** |
| [Finding fish](finding.md) | #14, #15 | #14 **B3**, #15 **NOW** |
| [Conditions & season](conditions.md) | #16, #17 | #16 **NOW**, #17 **NOW** |
| [Rigging, bait, care](rigging.md) | #18, #19 | #18 **NOW**, #19 **B3** |
| [Honesty](honesty.md) | #20, #21 | #20 **NOW**, #21 **NOW** |
