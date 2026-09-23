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

A design agent is still refining the prompt wording and the guard regex; those
are implementation details. The shape below is settled and evidenced.

- **A new prompt and a new authority.** `prompts/factcheck-note.md` says
  explicitly *"You flag; you never delete, reword, or 'correct' a claim."* The
  corrector is a different job and needs its own prompt, not an edit to that one.
- **Scope: `contradicted-by-source` only.** Never `single-source` — CLAUDE.md
  pins *"Single-source ≠ wrong (Cameron, 2026-08-23) — flag, never delete"*, and
  that rule stands. A `contradicted-by-source` flag is a different animal: the
  cited transcript does not support the claim, so rewriting it restores fidelity
  rather than overriding a judgment call.
- **Adjudicated passages are untouchable.** `⚠ adjudicated (Cameron, <date>)` is
  final per `prompts/review-note.md` rule 3a, and the guard already conserves it.
- **The cheap part, now verified.** Each `contradicted-by-source` ledger row's
  detail cell already records what the transcript actually says, quoted, with
  timestamps, plus the precise nature of the mismatch. A four-row sample was
  sufficient to write the correction without opening a transcript in every case:

  | note | what the fix is |
  |---|---|
  | `locations/cabo-san-lucas.md` | restore two hedges the rewrite hardened — the source says "**usually** an early morning bite" and these fish "**seem to** bite the best" |
  | `locations/loreto.md` | "trolls one up before lunch" is wrong in both cited sources; one is explicitly an afternoon fish, the other says only "early on on that Halco" |
  | `species/calico-bass.md` | "boiler" in the seminar means a boiler **rock**, not fish boiling on bait; and a July–August passage was re-scoped from spotted bay bass onto calico |
  | `species/spotted-bay-bass.md` | the source self-flags its own mechanism as speculation ("all you spotty experts are probably going to hold my feet to the fire"); the note states it flatly as doctrine |

  The pattern is consistent and narrow: **hedge-hardening and sense-drift**,
  which matches the coverage summary's "cite-stretching, not fabrication"
  diagnosis. That is what makes the pass affordable against the original 913
  units — and it also means a corrector that cannot find its fix in the detail
  cell should escalate rather than improvise.
- **Real scope: 1,536 rows across 249 distinct notes**, not the 104 the coverage
  summary's zone/region-plus-routers framing implies. The distribution suggests
  the worklist tiering:

  | flags per note | notes | unit shape |
  |---:|---:|---|
  | 20 or more | 12 | one unit each, heaviest first |
  | 10 to 19 | 48 | one unit each |
  | 5 to 9 | 52 | one unit each |
  | 1 to 4 | 137 | batch ~4 notes per unit |

  That is roughly 150 units. The heaviest are exactly where the coverage summary
  predicted: `locations/east-cape.md` (33), `species/yellowfin-tuna.md` (26),
  `locations/la-paz.md` (25), `ensenada.md` and `cedros-island.md` (24 each).
- **Reuse the existing scheduler rather than building one.** `commit-note.py`
  keys off a worklist row and fails if none exists, so the correction pass needs
  rows. The cheapest route follows the pattern `cluster:<name>` already
  establishes: append **new** rows with tier `correct` and unit ids
  `correct:<note path>` at status `pending`, add a `correct` mode to
  `scripts/review/next-note.py` alongside the existing transform/geo/gazetteer/
  cluster modes, and leave `commit-note.py`, `guard.py`, `progress.py` and the
  dashboard untouched. Appending rather than re-opening the old rows keeps the
  review run's history intact.
- **Operational risk.** This is another unattended multi-day fleet run, with the
  same failure modes as the last one: a trampoline that died on a SIGPIPE and
  stalled the chain for nine hours, and watchers that died with their containers.
  Land the guard rule and the correction prompt first, pilot three notes by hand
  for Cameron before dispatching, and keep the kill switch (`STOP` at branch root)
  documented in the same place.

## Phase 2b — restore the dropped numeric specifics

A different job from correcting over-claims, and it should be its own pass. The
review dropped **166 of 2,974** distinct numeric parameters across 205 rewritten
notes (5.6%); `lures/knife-jigs.md` lost 45% (53 → 29, collapsing gram ranges
like 100–150g and 120–160g), `hoop-netting.md` 28%, `sliding-sinker.md` 26%.

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
  `1e66a92` for all 205 rewritten notes; `lures/knife-jigs.md` is back to 53; the
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
