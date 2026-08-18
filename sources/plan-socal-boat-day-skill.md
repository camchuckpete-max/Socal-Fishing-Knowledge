---
type: planning
tags: [plan, skill, socal-boat-day, config, endpoints, multi-user]
sources: [cameron]
confidence: high
---

# Plan: distributed `socal-boat-day` skill + `config/` endpoint layer

The governing plan for shipping the multi-user boat-day skill: a thin packaged
bootstrap plus a live, editable endpoint layer in the repo. Produced from the
`HANDOFF-socal-boat-day.md` bundle Cameron delivered 2026-08-18.

> **STATUS — GATE A IS OPEN (not approved).** This document is a proposal.
> Nothing in it has been executed; the only file written to the branch is this
> plan. Per CLAUDE.md, execution unlocks only when Cameron sends a message
> containing exactly `PLAN APPROVED` for *this* document, and any amendment
> re-opens the gate. The handoff bundle is **not** an approval and says so
> itself. GATE B (merge to `main`) remains separate and later.

## Branch state

`claude/new-session-3obq33` is at `540ea4a`, byte-identical to `origin/main`
(0 ahead / 0 behind). Batch 2 is already merged, so this work starts from
canonical state and stacks cleanly.

## Context

Two constraints from the handoff drive every decision:

1. **A packaged skill cannot be edited after it ships.** It goes out over
   iMessage — no update channel, no recall. Anything that can change must live
   in the repo and be fetched at plan time.
2. **The KB changes constantly.** Ingestion batches land regularly, so a skill
   carrying a snapshot of the decision layer is stale the day it is packaged.

Therefore the skill hardcodes exactly two things — the repo raw base and one
entry path — and fetches procedure, doctrine, and endpoints live from `main`.
This supersedes the bundling design in `skills/boat-day/` (which generates a
snapshot via `scripts/build-skill-resources.py`). Per the handoff, `boat-day/`
is **flagged, not deleted** — see W6 and the open questions.

The endpoint layer has to leave the skill because BightSST provably lies in
ways that need a same-day fix: on 2026-08-17 `/sst-sources` reported MUR
available while serving GOES under the MUR label, `point-value` defaulted to a
source that errors, and chlorophyll returned `{}` with a 200 status. A fix to a
file in the repo reaches every installed copy on its next run; a fix to a
packaged skill reaches nobody.

## What ships

Four new files, authored in the handoff bundle, plus edits to three existing
files. The packaged `.skill` archive itself is **not** committed (see open
question 1).

| Path | Kind | What it owns |
| --- | --- | --- |
| `skills/socal-boat-day/ENTRY.md` | new note | The stable entry point every distributed copy fetches. Read order, the profile contract, plan requirements, reasoning discipline. **Path is a contract — never rename or move.** |
| `skills/socal-boat-day/README.md` | new index | Human-facing explanation of the thin-skill split and the relationship to `boat-day/`. |
| `config/endpoints.md` | new note | Endpoint table, fallback ladder, source-validity rules, last-verified date. The single place endpoint facts are stated. |
| `config/README.md` | new index | Folder index for the new `config/` branch. |
| `README.md` (root) | edit | Branch-map rows — add `config/`, fix the now-wrong `skills/` row. |
| `planning/day-plan-protocol.md` | edit | Remove inline endpoint facts; link `config/endpoints.md` instead. |
| `CLAUDE.md` | edit (needs explicit OK) | Repository-layout block and the `skills/` line. |

## Work items

### W1 — Add the four files

Committed as delivered, with the two corrections in "Defects found" below
applied. All four conform to the format rules: YAML front matter, relative
markdown links with human text, no wikilinks, backlink markers present for the
maintenance script to fill.

`config/` is a **new top-level branch**. It is not a knowledge branch — it holds
runtime configuration the distributed skill reads at plan time, and it exists
because values that change must live where they can be edited.

### W2 — Root README branch map

The root branch map is hand-maintained (the script does not touch the root
README). Two rows change. Proposed text:

```text
| [config/](config/) | Runtime config the distributed skill reads at plan time — conditions endpoints, fallback ladder, source-validity rules |
| [skills/](skills/) | Deployable skills — `socal-boat-day` (distributed, fetches the KB live) and `boat-day` (earlier bundled design) |
```

`config/` is placed after `sources/` and before `skills/`, keeping the existing
run of rows otherwise untouched.

### W3 — CLAUDE.md (requires an explicit yes)

CLAUDE.md is the spec document, so this is called out separately rather than
folded into W2. Two stale statements:

- The **Repository layout** block has no `config/` line. Proposed insert:
  `config/       runtime config read by the distributed skill: conditions endpoints, fallback ladder`
- The `skills/` line reads `the boat-day skill (built FROM KB notes + a profile)`.
  That description is now wrong for the distributed skill, which is built from
  nothing and fetches everything. Proposed: `skills/       socal-boat-day (distributed, live-fetch) + boat-day (bundled, earlier design)`

Both are inside a fenced block, so neither affects link validation. **If Cameron
prefers CLAUDE.md untouched in this pass, W3 is dropped and the layout block
knowingly lags the tree** — that is the trade, and it should be a deliberate
choice rather than an oversight.

### W4 — Reconcile `planning/day-plan-protocol.md` with `config/endpoints.md`

This is the work item that actually prevents a stale endpoint from surviving a
fix. The protocol currently states endpoint facts inline in two places. Both are
duplicated in `config/endpoints.md`, which is the file the skill reads.

Step 1 of the four steps becomes:

```text
1. **Pull conditions.** Per fishing zone and along the transit route, observed
   **and** forecast: per-spot SST + chlorophyll, wind/swell/current. Endpoints,
   the fallback ladder, and the source-validity rules live in
   [conditions endpoints](../config/endpoints.md) — read that before any pull.
```

The `## Conditions sources (BightSST)` section becomes `## Conditions sources`:

```text
- **Role:** [BightSST](https://bightai-api.onrender.com) is the system of record
  for *conditions*; this KB *references* it and never duplicates it.
- **Where endpoint detail lives:** [`config/endpoints.md`](../config/endpoints.md)
  — endpoint table, fallback ladder, source-validity rules, last-verified date.
  Stated there and nowhere else; an endpoint fact repeated here is a fact that
  survives a fix.
- **Doctrine — an empty layer is missing data, not a zero.** Chlorophyll is
  reported every run, or its absence is named.
- **Doctrine — distrust single-source SST extremes; cross-check models.** A
  known `goes_west_composite` window discrepancy and a cloud-contaminated NRT
  max (96.6 °F) mean single-source SST outliers are treated with suspicion.
```

What leaves the protocol: "read endpoints open/no-auth; admin behind a Bearer
key" and the Render cold-start caveat — both are endpoint facts and both already
live in `config/endpoints.md`. What stays: the role statement and the
single-source-extreme doctrine, which are knowledge, not configuration. What is
**added**: the empty-layer-is-not-a-zero line, promoted from the skill and the
endpoint file into the protocol because it is a planning rule the protocol
should state on its own. That addition is a judgment call — see J3.

Two other files mention the BightSST host and are **deliberately left alone**:
`conditions/upwelling-and-turnover.md` (states the `goes_west` data quirk as
doctrine — knowledge, not config) and `locations/bightsst-eval-targets.md` (a
link to the service, not an endpoint fact). `skills/boat-day/SKILL.md` also
names the host; it is left untouched pending the W6 decision.

### W5 — Run `scripts/link-maintenance.py` and verify

Before the commit, per the hard habit. See "Dry-run results" for exactly what it
does and what it touches.

### W6 — Flag the `boat-day/` overlap, do not resolve it

Two live definitions of the planning procedure will drift. The handoff is
explicit that Cameron decides whether `boat-day/` survives as a self-use variant
or retires, so this pass **flags and stops**. Proposal: add a short paragraph to
the curated prose in `skills/README.md` (above the auto-generated index markers,
which the script preserves) naming both skills, the difference between bundled
and live-fetch, and that the overlap is an open decision. No file in
`skills/boat-day/` is edited or deleted.

### W7 — Commit and push, then stop

One commit on `claude/new-session-3obq33`, pushed with `git push -u origin`.
**Do not merge and do not open a PR** — `main` is canonical, nothing is
canonical until merged, and the merge is GATE B: Cameron's post-build review of
the coverage summary and the judgment-calls list.

## Dry-run results (verified, not predicted)

The four files were placed in a throwaway copy of the repo at `540ea4a` and
`scripts/link-maintenance.py` was run against it. Result:

```text
OK: 132 notes, 20 indexes, 0 dead links.
```

Every relative link in the new files resolves, including the ones the handoff
called out: `ENTRY.md` → `config/endpoints.md`, `planning/day-plan-protocol.md`,
`profiles/README.md`, `profiles/cameron/README.md`, `profiles/cameron/boat.md`,
`tackle/gear-classes.md`, `planning/report-reading-and-forecasting.md`; and
`config/endpoints.md` → `skills/socal-boat-day/ENTRY.md`.

The script's writes, in full — five pre-existing files change, each by exactly
one generated line:

| File | Change |
| --- | --- |
| `skills/README.md` | index gains `socal-boat-day/` |
| `planning/day-plan-protocol.md` | backlink from `ENTRY.md` |
| `planning/report-reading-and-forecasting.md` | backlink from `ENTRY.md` |
| `profiles/cameron/boat.md` | backlink from `ENTRY.md` |
| `tackle/gear-classes.md` | backlink from `ENTRY.md` |

And on the new files: `skills/socal-boat-day/README.md` gains generated index +
map blocks; `config/README.md` gains a map block and has its hand-written index
line replaced by the generated summary. Nothing else in the tree moves. The
run with the W4 protocol edits applied is also clean — same counts, 0 dead
links, and `config/endpoints.md` picks up the protocol backlink.

## Defects found in the handoff files

**D1 — `ENTRY.md` generates a broken index summary.** The auto-index takes the
first prose paragraph, and it skips lines starting with `*`. `ENTRY.md`'s first
paragraph opens with `**This path is a contract...**`, so the generator skipped
that line and produced a fragment starting mid-sentence:

```text
- [ENTRY — SoCal Boat-Day Skill](ENTRY.md) — socal-boat-day skill are distributed as packaged files that cannot be edited after they're sent; every one of them fetches this exact path.
```

Proposed fix — a plain lead paragraph before the contract paragraph, which
leaves the contract text itself untouched:

```text
The live entry point every distributed `socal-boat-day` skill copy fetches
first. It owns the read order, the profile contract, and what a plan must
state.
```

Verified: the index line becomes
`— The live entry point every distributed socal-boat-day skill copy fetches first.`

**D2 — `config/README.md`'s hand-written index line is not what the script
generates.** It reads "where conditions data comes from, and what to do when a
source lies or dies"; the generator replaces it with the first sentence of
`endpoints.md` ("The single source of truth for where conditions data comes
from."). Not a bug — the index is generated by design — but the hand-written
line should not be committed as if it will survive. It is dropped, and the
better phrasing is preserved where it can live: in the curated prose above the
markers, which the script does preserve.

## Judgment calls

- **J1 — `config/` as a new top-level branch rather than a subfolder of
  `planning/`.** The endpoint layer is configuration, not knowledge, and the
  distributed skill hardcodes a path to it. Burying it under `planning/` would
  put a contract path inside a branch that gets reorganized as knowledge grows.
  Cost: one more top-level folder, and the branch map / layout block have to
  learn about it (W2, W3).
- **J2 — `type: planning` front matter on both new files.** Neither is a
  knowledge note. `planning` is the closest existing type, and adding a `config`
  type to the CLAUDE.md enum is a spec change this pass does not need. Flagged
  in case Cameron wants the enum extended later.
- **J3 — promoting "an empty layer is missing data, not a zero" into the
  protocol** (W4). It exists in the skill and in `endpoints.md`; the protocol is
  the surface a chat session actually follows, and a silent `{}` is the exact
  failure mode that produced this work. Stated as doctrine, not as an endpoint
  fact, so it does not re-create the duplication W4 removes.
- **J4 — the BightSST failures are recorded, not fixed.** `endpoints.md` carries
  them as dated observations with a "re-verify before trusting" instruction.
  Fixing BightSST's ERDDAP ingest is separate work in a different repo.
- **J5 — no stub is needed for the `boat-day` overlap.** The flagged-stub rule
  covers species routers and real-fishery methods absent from the corpus, not
  tooling decisions. The overlap is flagged in prose (W6) and in the open
  questions below.

## Open questions for Cameron

1. **Should the packaged skill's source be committed?** The handoff says the
   `.skill` package is delivered separately and not committed. The consequence:
   the repo has no record of what actually shipped to people's phones, and when
   a friend reports odd behavior there is no way to tell which version they
   have. Recommendation — commit `skills/socal-boat-day/SKILL.md` plus its three
   reference files as the source of record, and add `SKILL.md` to the script's
   `VALIDATE_ONLY` set the way `boat-day/SKILL.md` already is, so it is
   link-validated but never gains a backlinks block. This is **not** in the plan
   above; say the word and it becomes W8.
2. **Does `skills/boat-day/` survive or retire?** (Handoff question, unchanged.)
   Two definitions of the procedure will drift. If it retires,
   `scripts/build-skill-resources.py` and the `resources/` exclusion in
   `link-maintenance.py` go with it.
3. **Should `config/` hold anything else currently hardcoded where it cannot be
   fixed?** (Handoff question.) Nothing else was found hardcoded in a packaged
   artifact during this pass, but the search was scoped to endpoints.
4. **The uninstalled forecasting-layer and convergence-layer patches** from
   earlier sessions still are not in the repo. They belong in `planning/` or
   `conditions/`, not in a skill bundle. Separate work item; needs a sequencing
   call.
5. **W3 (CLAUDE.md) — in or out of this pass?**

## Out of scope

- Fixing BightSST's ERDDAP ingest, MUR, or chlorophyll.
- Deleting or editing anything under `skills/boat-day/`.
- Adding any user's inventory to the repo. Profiles are opt-in; the skill keeps
  each angler's gear in their own chat memory.
- Adding coordinates for any user other than Cameron. His waiver is personal and
  specific.
- Merging to `main`, or opening a PR.

## Verification checklist (run at the end of execution, before the commit)

- [ ] `python scripts/link-maintenance.py` exits 0 with 0 dead links.
- [ ] A second run produces no diff (the script is idempotent).
- [ ] `skills/socal-boat-day/ENTRY.md` exists at exactly that path and its
```text
  generated index summary is a complete sentence (D1).
```
- [ ] `config/endpoints.md` is the only file in the repo stating an endpoint
```text
  path, a fallback host, or a source-validity rule.
```
- [ ] The root branch map lists `config/` and describes both skills.
- [ ] `git diff` touches only: the four new files, the three edited files, and
```text
  the five generated one-line backlink/index updates.
```
- [ ] No user inventory, no non-Cameron coordinates, nothing under
```text
  `skills/boat-day/` modified.
```

## Execution order

One commit, in this order: add the four files (with D1 and D2 applied) → W2 root
README → W3 CLAUDE.md if approved → W4 protocol reconciliation → W6 flag in
`skills/README.md` → run `link-maintenance.py` → commit → push to
`claude/new-session-3obq33` → **stop at GATE B.**


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
