# Plan: correction pass, external verification, then GATE B

> **Provenance:** governing plan document for the post-review correction work,
> committed as `sources/plan-correction-pass.md` per the repo convention that
> the governing spec lives beside the work it governs (pattern:
> `sources/plan.md` 2026-08-12, `sources/plan-review.md` 2026-08-23). Scope was
> settled with Cameron on 2026-09-23, when he asked whether the review branch
> was ready to merge and chose, of the three options put to him, **the
> correction pass first, with the external verification run before it**.

**Status (2026-09-23): GATE A LOCKED.** Phase 0 (accounting repair) is ordinary
document repair and is proceeding — it fixes errors in the documents GATE B is
decided against, and is needed whichever path is taken. **Phases 1, 2, 2b and 3
need `PLAN APPROVED` against this document before any fleet dispatch.** Per
CLAUDE.md, no conversational phrasing unlocks GATE A, and approving a plan in
the session's own planning UI is conversational.

Kill switch unchanged: a `STOP` file at the branch root.

---

## Context

Cameron asked whether the editorial-review branch is ready to merge to `main`.
It is not, and he has chosen the two things that must happen first: **run the
external verification pass**, then **run a correction pass** over the prose the
review introduced. This plan covers both, plus the repair and merge mechanics
that surfaced while checking.

Three things prompted this:

1. **What he reviewed is not the GATE B surface.** He reviewed the blind
   head-to-head prompt tests, which measure reach, citation and honesty.
   CLAUDE.md gates the merge on the coverage summary plus the judgment-calls
   list. The coverage summary's own verdict is *"It should not merge as-is"* —
   the run wrote ~1,500 claims its sources do not support and flagged every one.
   In a 40-row sample, **39 of 40 over-claims were introduced by the review.**

2. **Two mechanical blockers nobody had noticed.** `validate.yml` has never run
   against this branch — it triggers on push-to-main and on pull requests, and
   no pull request exists, so all 1,440 commits are unvalidated by the gate meant
   to enforce the link-maintenance no-diff contract. And the branch is 15 commits
   behind `main` with two add/add workflow conflicts.

3. **The accounting in my own coverage summary is wrong in three places.** It is
   the GATE B document, so it has to be right before it can be approved against.

Intended outcome: a branch whose new prose is as trustworthy as its old, whose
regulatory claims have actually been checked, whose GATE B surfaces are accurate,
and which has passed CI at least once — then Cameron merges.

## What is actually open (measured 2026-09-23, not quoted from summaries)

| surface | state |
|---|---|
| escalations needing a ruling | **83** of 137 (61 name Cameron explicitly) |
| ledger live rows | **2,126** (+351 Standing, 17 Resolved) |
| of those, `contradicted-by-source` | **1,536** |
| ledger rows tagged `ext-verify` | **299**, of which **0** verified |
| notes carrying a `contradicted-by-source` flag | **278** |
| region + zone pages among them | **81** |
| species routers among them | **23** |
| worklist rows not at a terminal status | **246** (all at `fact-checked`, 0 `pending`) |
| relocation rows contested | **3** (0 pending, 57 executed) |
| `judgment-calls.md` | 2 entries — a pointer, not an enumeration |
| coordinate conservation | **clean** — 1,321 positions, 0 unsourced |
| ladder | 2 jurisdictions, 5 regions, 76 zones, 371 spots |

Clean and not at issue: the ladder, the evidence layer, coordinate conservation,
cite conservation (500 of 500 on the original routers), and the working tree.

## Phase 0 — repair the accounting before anything is approved against it

These are small, and they gate everything because they are the documents Cameron
signs off on.

1. **Fix `sources/review-coverage-summary.md`.** Three figures are wrong:
   escalations are **137**, not 135; **83** are genuine by category (61 by the
   narrower "names Cameron" test), and the stated **74** reconciles with neither;
   relocations executed are **57**, not 58.
2. **Resolve the Tanner/Cortez contradiction.** `sources/fact-check-ledger.md`
   has the Long Beach 90-vs-110 mi row in its **Resolved** section reading
   *"resolved by geometry… no figure was wrong"*, while
   `sources/escalations.md:528` records the verifier overturning exactly that on
   2026-09-02: `nQvJnfb5jQ4` states the 90 mi figure **of Cortez by name**,
   inverting the near/far assignment. Move the row back out of Resolved into the
   live table. A reader of the ledger alone currently concludes this is closed.
3. **Give `sources/escalations.md` a status column.** 134 of 137 entries carry no
   disposition, so "open" is unrecoverable from the file — it can only be
   inferred from category. Append a `- status:` line to the schema and backfill
   the 54 noise entries (38 guard-reverts, 11 check-note-failed, 5
   subagent-failure) as closed, leaving the 83 genuine ones open.
4. **Populate `sources/judgment-calls.md` as a real enumeration** of those 83,
   grouped for triage rather than listed flat. Right now it is 2 entries that
   point at other documents, one of which repeats the wrong 74/135 figure.
   CLAUDE.md names it as a GATE B surface; it cannot serve as one in this state.
5. **Settle the 246 `fact-checked` rows.** Per
   `prompts/orchestrate-review-chunk.md:55` the fact-check step sets `done` for
   standard and gazetteer tiers, so the 138 standard + 1 gazetteer rows sitting at
   `fact-checked` are mislabelled. For `geo` and `full` tiers (107 rows) no later
   pass exists — `next-note.py` only ever selects `pending` — so `fact-checked`
   is their real terminal state. A five-row sample confirms the work was done
   (`layout: v2` present, evidence files written, ledger rows produced). Relabel
   to `done` and log it, or restate the GATE B criterion; do not re-run 246 units.
6. **Fix two malformed ledger rows** whose unescaped `|` shifts their columns
   (they parse as category `45–50 mi out"` and `42–43 mi"`), and the stray blank
   line inside the live table at line 1587 that breaks naive row-walkers.

## Phase 1 — external verification (299 rows)

`verify-external.yml` is the only workflow with web access and has **never run**.
Its 299 queued rows are mostly regulatory and biology claims, the
highest-consequence content in the KB to have wrong.

- **It does not self-re-dispatch.** Unlike `review-chunk.yml`, it is
  `workflow_dispatch`-only with a default `chunk_size` of 30, so 299 rows is
  ~10 dispatches. Port the self-re-dispatch block from
  `.github/workflows/review-chunk.yml:214-243` — the STOP check, the
  zero-progress guard, the chain cap and the retry ladder — gating on remaining
  `ext-verify` rows instead of `next-note.py --count`. One dispatch then drains
  the queue.
- **I may not be able to start it.** `actions_run_trigger` returned 403 earlier
  in this session. `gh` is available inside the runner but not in my session, so
  the chain is self-sustaining once started; the first dispatch may have to be
  Cameron clicking *Run workflow*. Verify the 403 at execution time before
  asking him.
- Results append `— verified-current <date> (<source>)` or `— external-mismatch: …`
  to each row's detail cell. **Any `external-mismatch` becomes a correction-pass
  input**, so Phase 1 must finish before Phase 2's worklist is built.

## Phase 2 — the correction pass

### The unit is a note, not a ledger row

214 units, after folding the 35 evidence-file ledger rows into their parent
notes. A note-shaped unit reuses the existing machinery untouched: `guard.py`'s
`SUBJ_NOTE_RE` already parses `review: locations/tanner-bank.md — correct`,
SCOPE already permits the note plus its evidence file plus the exempt logs, and
`commit-note.py --note` already rewrites one worklist row. Nothing in the scope
machinery changes.

### The corrector reads the note first, the ledger second

The inline flag sits beside the claim it indicts, and **1,598 of 1,666 inline
flags (96%) carry a verbatim quote of what the source actually says**, median
535 characters. That solves "where in a 533-line note is this claim?" for free.
The ledger row is worth reading for the 28% of cases where it names a *different*
video id — the correct cite — and little else.

Across the live ledger, **1,510 of 1,539 `contradicted-by-source` rows (98.1%)
carry at least one verbatim quoted span**, and roughly **91% are correctable
from the row and note alone**. Transcripts are local and median 2.2 KB, so the
escape hatch is cheap; the point is that it is the exception. The builder tags
the ~9% in advance: 23 rows whose detail carries no quote and names no
alternative source get `needs-transcript` and 100% transcript verification.

### Five legal moves, and no sixth

Ranked; the corrector picks the highest that fits.

1. **Narrow** — keep the claim, restore the source's hedge, scope or condition.
2. **Restate** — replace the wording with what the transcript actually says.
3. **Re-cite** — the claim is right and the cite is wrong; fix it and append the
   correct id to front-matter `sources` (append-only).
4. **Split** — one sentence welded two sources' facts; separate them, each with
   its own cite.
5. **Demote** — nothing supports it as doctrine; move it to the evidence file as
   a one-line cited observation.

**Deletion is not a correction.** It is the cheapest way to make a flag go away
and the pass's defining failure mode, so it is excluded by construction rather
than by instruction. A corrector whose honest answer is "remove this" marks the
row `correction-blocked: needs-cameron` and leaves the claim standing.

### What the corrector may never touch

Enforced in the builder and the guard, not merely requested in the prompt — a
rule that depends on a worker reading a marker correctly 1,539 times will fail
some of the time.

- **`single-source` claims and flags, ever.** CLAUDE.md pins the reason and it
  stands. Guard invariant: the `single-source` inline-flag count across the
  note-plus-evidence pair is **non-decreasing**.
- **`⚠ adjudicated (Cameron, <date>)` passages** — already guarded.
- **The 27 rows carrying `**stands**`** and **the 106 tagged `ext-verify`** —
  excluded by the builder. Correcting an `ext-verify` row pre-empts Phase 1,
  which may overturn the correction.
- **`contradicted-internal` (228 rows)** — deferred. Those span two notes and
  need the cluster-pass authority, which already exists as its own tier.
- **Any second note.** A correction implying a move appends a relocation-queue
  row and leaves the content in place.

### The ledger closure that makes deletion mechanically detectable

Each closed row moves out of the live table into a new `## Corrected` section
below the end markers, mirroring the existing `## Standing` and `## Resolved`
grammar, in this shape:

```
| <note> | <claim, unchanged> | corrected | <final cite> | **corrected** (<date>,
correct pass): was: "<verbatim old sentence>" — now: "<verbatim new sentence>"
— <one line: what the source actually says> |
```

`was:` and `now:` are verbatim single sentences, and that is the keystone. The
guard asserts the `now:` string is **literally present** in the post-commit note
and the `was:` string **literally absent**. A deletion cannot satisfy it: there
is no `now:` text to point at. It also catches a corrector rewriting the ledger
to describe an edit it did not make.

Paired with it: **flag-closure accounting** — the count of
`contradicted-by-source` flags removed from the note must equal the count of
rows moved into `## Corrected` naming that note. A flag deleted without a ledger
closure is a violation, and so is the reverse. The two surfaces cannot drift
apart.

### The tier must be `correct` — a trap worth naming

`guard.py`'s `set_row_status` coerces `done` back to `transformed` for tiers
`full`, `standard` and `geo`, so the fact-check phase cannot be skipped. A
correction unit landing `done` on a `geo`-tier row would be **silently** coerced
and re-enter fact-check. A distinct `correct` tier sidesteps it entirely.

Wiring is four small edits: `correct` added to `next-note.py`'s tiers, model map
and a bucket placed **last** in `buckets()`; a `cost_of()` that reads `cbs:<n>`
out of the flags cell; `corrected` added to `commit-note.py`'s status choices.
`review-chunk.yml` needs no change — the phase is derived from worklist state,
which is the whole design of the self-re-dispatching chain.

### The verifier needs its own prompt

`prompts/verify-review.md` rule 5 currently reads *"Fact-check units: flags
only — any reworded/deleted claim → reject"*, which would reject every
correction unit. A correction verifier checks: every `now:` string is literally
in the note; every `was:` string is literally absent; the new text is entailed
by the ledger detail's quoted wording; **at least three corrections per unit
spot-checked against the actual transcript** with timestamps quoted, the bar
`verify-review.md` already sets; no `single-source` flag lost; no second note
touched.

### Phasing and sizing

Unit cost by flag count: 1–4 rows = 2 points, 5–9 = 3, 10–19 = 5, 20+ = 8.
Ordering is region-first with `socal-bight` ahead of Baja, then worst pages
first, so a budget cut lands on the cleanest pages rather than on the mission
scope. The three worst pages in the KB are all Baja and must not front-run
Point Loma and Catalina.

| phase | scope | units | rows | chunks |
|---|---|---:|---:|---:|
| supervised setup | prompts, guard rules, builder, `## Corrected` section, wiring | — | — | 1 PR |
| 1a | SoCal zone, region, jurisdiction pages | 42 | 517 | ~12 |
| 1b | species routers | 21 | 224 | ~6 |
| 1c | Baja and Cortez zone and region pages | 44 | 561 | ~13 |
| 2 | techniques, rigs, lures, conditions, seasonal, bait | 77 | 166 | ~10 |
| 2b | spot pages | 33 | 191 | ~6 |
| 4 | adversarial re-sample of 40 rows, scored the way the original 40 were | — | 40 | ~2 |
| | **total** | **217** | **1,539** | **~50** |

Phase 4 matters: the pass's claim of success gets measured the same way the
review's failure was measured, by an independent adversarial sample, not by the
correctors' own reports.

### Pre-flight the builder must do

- Parse the ledger `\|`-aware. Six rows carry escaped pipes inside cells and
  read as 9 to 11 columns under a naive split.
- Normalise one malformed note cell,
  `techniques/slow-pitch-jigging.md (evidence file)`, to
  `techniques/evidence/slow-pitch-jigging.md`.
- Fold the 35 evidence-file rows into their parent units: 248 note paths → 214.
- Emit a `--dry-run` census the way `build-geo-worklist.py` does. **That census
  is the gate artifact Cameron approves before any unit runs.**

### Operational risk

Another unattended multi-day fleet run, with the same failure modes as the last
one: a trampoline that died on a SIGPIPE and stalled the chain for nine hours,
and watchers that died with their containers. Land the guard rules and the
prompts first, pilot three notes by hand for Cameron, and keep the kill switch
(`STOP` at the branch root) documented in the same place.

## Phase 2b — restore the dropped numeric specifics

A different job from correcting over-claims, and it should be its own pass. The
review dropped numeric parameters at an aggregate rate near **4–6%** of roughly
3,000 across the rewritten notes.

**Re-derive the list before restoring anything.** The figure this plan first
carried — "166 of 2,974, `knife-jigs.md` lost 45%" — does not survive checking:
that note holds **19 distinct gram parameters before and 31 after**, and the two
ranges named as casualties are present now and absent before. Most apparent loss
is the 57 relocations and 28 spin-outs carrying parameters to notes the
extraction was not searching. The genuinely-lost residue is small, order a
couple of dozen, and mixed in kind — `35–37 lb` on a Cedros session is gone from
the KB entirely, while `50–150 yards` for boiling bluefin now reads
`100–150 yards`, a narrowed range rather than a deletion.

`scripts/review/guard.py` conserves cites and observations but not parameters, so
nothing stops a recurrence. Two pieces:

1. **A numeric-conservation rule in the guard**, mirroring the existing cite and
   observation conservation in `conservation_problems()`: extract numeric
   parameters from the note-plus-evidence pair before and after, and fail when
   the after-set is smaller. The false-positive list matters — dates, charted
   coordinates, video ids, fathom-named banks ("43", "181", "the 425") and line
   numbers must not count as parameters.
2. **A restore pass** against the pre-review commit `1e66a92`, diffing each of
   the 205 rewritten notes for parameters present then and absent now, and
   putting them back. The guard rule must land first, or the restore pass can
   undo itself.

## Phase 3 — merge mechanics

Only after Phases 1, 2 and 2b are green.

1. **Merge `origin/main` into the branch.** It is 15 commits behind, all CI and
   publishing plumbing, no knowledge content. Two add/add conflicts, on
   `.github/workflows/review-chunk.yml` and `review-trampoline.yml`, from the
   registered-copy scheme drifting. `verify-external.yml` is still identical.
2. **Retire the review workflows** per `sources/plan-review.md:460-467` —
   `review-chunk`, `verify-external`, the `main` trampoline and the registration
   copies. This dissolves both conflicts rather than resolving them. Do it
   **after** Phase 2, which needs the chunk runner.
3. **Open a pull request** so `validate.yml` fires for the first time: the four
   unit test scripts, `link-maintenance.py` passing *and leaving no diff*, and
   the `export-site-index.py` dry run.
4. **Regenerate the Review Watch surface** (`scripts/build-review-watch.py`; the
   HTML is gitignored) so Cameron reviews against current state.
5. Cameron merges. Per CLAUDE.md, GATE B is his action, not mine. Note that
   merging fires `notify-site.yml`, which dispatches to the BightSST repo — this
   is not an inert merge.

## Governance

**This re-opens GATE A.** A correction pass is new work, and CLAUDE.md is
explicit that any plan amendment re-opens GATE A and approval must be re-given
with a `PLAN APPROVED` token. Two items additionally need Cameron's sign-off
because they change the rules rather than apply them:

- **A scoped CLAUDE.md amendment.** The content rule at line 265 reads
  *"Fact-check flags never touch the claim."* The corrector needs a narrow
  carve-out for `contradicted-by-source`, leaving the `single-source` rule
  untouched. CLAUDE.md is guard-protected — a human-in-the-loop edit.
- **The three contested relocation rows** (`banda-bank-todos-santos-island.md`
  split, the white-seabass hatchery-program spin-out, the cabrilla sliding-sinker
  destination), which are destination classification calls only he can make.


## Appendix — the exact CLAUDE.md amendment being asked for

The corrector needs one carve-out. CLAUDE.md is guard-protected, so this is a
human-in-the-loop edit and it is quoted here in full rather than described, so
approving the plan and approving the rule change are one read.

**Current** (CLAUDE.md, "Content rules"):

> - **Fact-check flags never touch the claim.** The `⚠` flag grammar
>   (`templates/style-guide.md`) sits beside a claim and queues it in
>   `sources/fact-check-ledger.md` for Cameron. **Single-source ≠ wrong**
>   (Cameron, 2026-08-23) — flag, never delete.

**Proposed** — the existing sentences unchanged, one paragraph added:

> - **Fact-check flags never touch the claim.** The `⚠` flag grammar
>   (`templates/style-guide.md`) sits beside a claim and queues it in
>   `sources/fact-check-ledger.md` for Cameron. **Single-source ≠ wrong**
>   (Cameron, 2026-08-23) — flag, never delete.
>   **One exception, for `contradicted-by-source` only** (Cameron, 2026-09-DD):
>   a sanctioned correction pass may rewrite a claim its own cited transcript
>   does not support, to what that transcript actually says, and close the
>   ledger row. That is restoring fidelity to a source, not adjudicating a
>   judgment call — which is why it does not reach `single-source`,
>   `unverifiable` or `contradicted-internal`, never touches an
>   `⚠ adjudicated` passage, and requires a corrector that cannot ground its
>   fix in the ledger row's recorded source wording to escalate rather than
>   improvise.

Why the carve-out is narrow rather than general: the rule's stated reason is
that a single source is not a wrong source, and that stands. A
`contradicted-by-source` flag says something different — the cited transcript
does not support the claim, because the review hardened a hedge or drifted a
sense. Leaving those standing under a warning label is the only option the
current rule allows, and it is the option that makes every zone page read with
ten warnings on it.

## What has already been done under this plan

**Phase 0 is complete** (2026-09-23), before GATE A, because it is document
repair rather than a build and it was needed whichever path was chosen:

- Ledger: one row that was invisible to every row-walker un-fused; the
  Tanner/Cortez row moved out of Resolved and re-opened for a ruling; a stray
  blank line removed. Every live row now parses at five cells. Counts moved to
  2,128 live and 1,537 `contradicted-by-source`.
- Coverage summary: escalations corrected to 137 total and 83 genuine (the
  stated "74 of 135" reconciled with no cut of the file); relocations to 57
  executed with 3 contested.
- Escalations: a `- status:` field added to the schema, backfilled across all
  137 entries, and written by `guard.py`'s appender from now on.
- Judgment calls: rewritten from two pointer entries into the actual decision
  list — all 83 open calls grouped by area.
- Worklist: 246 rows were stuck at `fact-checked`, one step short of terminal,
  with 0 pending — the chain had reported itself drained with a quarter of its
  rows open. Verified complete by sampling every affected tier, then relabelled
  `done`. Every row is now terminal.

## Verification

- **Phase 0:** every figure in the coverage summary reproduces from a command in
  the document; `judgment-calls.md` enumerates 83 entries; no worklist row sits
  at a non-terminal status; the ledger parses cleanly row-by-row.
- **Phase 1:** 0 of 299 `ext-verify` rows lack a verdict string; every
  `external-mismatch` has a correction worklist row.
- **Phase 2:** `contradicted-by-source` live rows fall to near zero; every
  correction cites the ledger row it closes; `single-source` row count is
  **unchanged** (proof the corrector stayed in scope); the numeric-parameter
  count per note is `>=` its pre-correction value under the new guard rule; a
  hand-audit of ~15 corrections against the transcripts confirms each matches.
- **Phase 2b:** the per-note numeric-parameter count is `>=` its value at
  `1e66a92` for every note on the re-derived list; the
  guard rejects a deliberate parameter deletion in a test fixture.
- **Phase 3:** `validate.yml` green on the pull request; `check-coordinates.py`
  still clean; `link-maintenance.py` leaves no diff; the ladder still reconciles
  at 391 spots = pages + AR rows + excluded.
- **End to end:** re-run a subset of the 21 blind prompt tests against the
  corrected branch and confirm the honesty and actionability scores hold. The
  harness is in the scratchpad and the pinned batch-2 and batch-3 worktrees still
  exist, so this is cheap and it is the only check that reads the KB the way a
  user does.


<!-- backlinks:start -->
## Linked from

- [Judgment calls — the GATE B decision list](judgment-calls.md)
<!-- backlinks:end -->
