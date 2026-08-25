# Plan: Full KB Editorial Review — structure, rewrite, evidence split, fact check, gazetteer

> **Provenance:** governing plan document for the full editorial review of the
> knowledgebase, committed as `sources/plan-review.md` per the repo convention
> that the governing spec lives beside the work it governs (pattern:
> `sources/plan.md`, 2026-08-12). Scope and decisions were worked out with
> Cameron in conversation on 2026-08-23.

**Status (2026-08-24, current): GATE A UNLOCKED — RUNNING.** Cameron re-gave
`PLAN APPROVED` for amendment v2.2 after reviewing both gate artifacts. `STOP`
removed; the fleet is working the ladder.

Running order is **geo first**: jurisdiction (2) → regions (5) → zones (76),
then the note transforms, then relocations, the enrichable spots, fact-check
and cluster consistency. ~351 actionable units, ~661 points, ~41 chunks. The
~327 minimum spot pages are generated mechanically outside the fleet and
self-sequence at each chunk checkpoint as their zone pages land.

Kill switch unchanged: a `STOP` file at the branch root. Model lever:
`MODEL_OVERRIDE` in `.github/workflows/review-chunk.yml`.

The two gate artifacts Cameron reviewed to give that approval:

1. **Five exemplars** — `species/bluefin-tuna-trolling.md`,
   `species/yellowtail-surface-iron.md`, `locations/mexican-waters.md`,
   `locations/coronado-islands.md`, `locations/pukey-point.md`.
2. **The census** — `sources/geo-census.txt`, regenerated from
   `scripts/review/build-geo-worklist.py --dry-run`.

History: GATE A was first unlocked 2026-08-24 for the v2.1 + fleet-dispatch
plan; the chain ran two chunks (yellowtail, surface-iron, barracuda,
bluefin-trolling, bluefin-tuna, bonito) before Cameron paused it against his
weekly limit. GATE B (merge to `main`) has never been open and remains locked
behind his post-build review.

> **Dispatch note (2026-08-24 18:58 UTC):** the trampoline's first dispatch
> 404'd — `gh workflow run` resolves workflow names against the
> default-branch registry, and `review-chunk.yml` existed only on this
> branch. Fixed by registering byte-identical, `workflow_dispatch`-only
> copies of `review-chunk.yml` and `verify-external.yml` on `main`
> (inert there; every dispatch targets `--ref` this branch — the batch-3
> `batch2-ingest-chunk` precedent). This widened the approved "sole main
> push" (trampoline) to three registration files, all retiring together at
> GATE B. Chain confirmed started: review-chunk run #1 in progress.

## Amendment v2.2 — the sub-article ladder (2026-08-24, cameron)

**GATE A was RE-OPENED by this amendment and re-given 2026-08-24** after
Cameron reviewed the two gate artifacts below. Kept as the record of why the
gate re-opened; the live state is the status block at the top of this file.

Cameron's two asks, which turned out to be one gap — the KB had no middle
rung, so depth either bloated a top-level page or had nowhere to live:

1. **Species x technique sub-articles.** `species/bluefin-trolling.md` read
   like a separate species when it was bluefin's *trolling program*. New gated
   type `species-technique` (`species/<species>-<technique>.md`, optional zone
   variant); the `decision` type is retired. Routers keep routing and link the
   sub-article first; technique notes keep universal mechanics and carry a
   **generated** `## Species applications` list. Bar: **>= 2 distinct cited
   execution parameters** for the pairing — *"if it's just using heavier gear
   it shouldn't have its own article."*
2. **The geographic ladder.** jurisdiction → region → area → zone → spot, one
   type per rung, flat in `locations/` with a `parent` path field. Cameron's
   three example paths conflicted because water type (Islands / Inshore /
   Offshore) was being used as a tree level; it is already the `waters` facet,
   so it leaves the tree and all three paths collapse to one shape.

**Zones are derived from COORDINATES, not mention counts** — the decision that
matters most, since every spot below a zone re-parents if it is wrong.
`sources/spot-lists.md` (391 charted spots) is the authority: its `##` sections
are the zone skeleton, and complete-linkage clustering capped at 12 nm
subdivides the offshore-banks catch-all. Single-linkage was tested and
rejected — it chains the whole coast into one 309-spot, 192-nm blob. Corpus
depth decides how much a zone page can SAY, never whether it exists;
coordinate-less but corpus-rich zones (Cedros 38 notes, Guadalupe 30, Alijos
19, Mag Bay, Cabo, East Cape, BOLA, Loreto, La Paz) qualify on depth alone.

**Every spot in the library gets a page**, minimum coordinates + parent zone.
The 50 numbered artificial-reef waypoints collapse to 5 complex pages
carrying coordinate tables; every coordinate stays published.

### What the census caught before anything was generated

- **9 Mile Bank and 14 Mile Bank are 54.0 nm apart** and had been grouped as
  one zone (Cameron's catch, verified numerically); **the 178 is 4.9 nm from
  North 9 Mile** and belongs to it, not to a 181/182 group.
- `La Jolla` was slugging to `jolla` — Spanish articles are part of the name.
- Species-filtered sections (Catalina rockfish spots) double-claimed spots.
- 86 single-bank "zones" were a list, not a carve-up.
- MPA advisories in a label were excluding 12 real spots (Ship Rock,
  Windansea, Long Point).
- `105 / 150` scored 54 notes on line-test pounds and gear-ratio prose; the
  fixture check then caught this plan's own published table drifting, because
  that throwaway scan double-counted notes against their evidence files.

### The two gate artifacts

1. **Five exemplars** (shape): `species/bluefin-tuna-trolling.md`,
   `species/yellowtail-surface-iron.md`, `locations/mexican-waters.md`,
   `locations/coronado-islands.md`, `locations/pukey-point.md` (the minimum
   spot page — the tier that runs ~335 times).
2. **The census** (set): `scripts/review/build-geo-worklist.py --dry-run` —
   **427 pages** (2 jurisdiction + 5 region + 76 zone + 344 spot), each with
   its parent, depth count and bar clause, plus the parent-distance outliers,
   2 naval security zones excluded, and 19 spots carrying advisories.
   Coordinate conservation is asserted: 391 spots = 339 pages + 50 AR table
   rows + 2 excluded.

Cost note: keeping judgment work on Opus raises spend rather than lowering it,
and Sonnet 5's introductory rate ends 2026-08-31. The real levers are the
existence bar and the census, not the model dial.

## Amendment — pilot-feedback round (2026-08-24, cameron + nate)

Feedback source: `sources/pilot-feedback-2026-08-24.md`; `nate` registered
in the source registry (El Cajon local, relayed via Cameron).

- **Style guide v2.1** (templates/style-guide.md): no filler sentences;
  mechanism or explicit gap, never correlation-as-causation; scope every
  claim; presence ≠ catchability; **single observation ≠ doctrine** (lives
  in evidence); **no meta-attribution** (no user names in prose, no
  source-narration, no trip anecdotes inside doctrine, no side-by-side
  meta-commentary — contested doctrine leads with the decision rule);
  jargon links or dies; every situations row passes the reader-questions
  test (gear/size/color/when/why or a link).
- **Species skeleton v2.1** (templates/species.md): `## Where & when`
  becomes COMPACT (range/migration/temp/timing mechanics; no spot tour) and
  a new `## Zone guides` section links the species×zone targeting guides.
  Nate's acceptance test added beside Cameron's.
- **New gated type `zone-guide`** (templates/zone-guide.md;
  `species/<species>-<zone>.md`; region/zone level, never spot level):
  Lead → The program → Reading the day → Rigs & gear → Differs from nearby
  zones → Evidence. This round builds ONE exemplar
  (`species/yellowtail-coronado-islands.md`); the fleet builds the rest
  where the corpus supports, gap-flagged where thin.
- **Yellowtail rework** applying Cameron's point-by-point corrections
  (flyline class, yo-yo/dropper logic, demotions to evidence, sonar section
  restructure as feeding-state reads, jargon links, colors/sizing from
  nate, sea-lion row to Landing & handling, skip-jigging flagged, etc.),
  re-verified adversarially, committed via the wrapper.
- **Fleet prompts updated** (review-note.md step 3/3b, verify-review.md
  check 4) so every remaining row inherits the v2.1 rules.

---

## Context

The KB has grown through three ingestion batches to ~523k words across ~270
notes, and the growth exposed five problems this review fixes:

1. **Quote-heavy prose.** Notes lean on attributed reportage ("Erik says…",
   20–40-line attribution preambles) instead of stating knowledge plainly and
   citing sources. ~75–80% of `species/yellowtail.md` is attributed reportage;
   four inline citation conventions coexist.
2. **No true per-type structure** for the knowledge Cameron most wants: what
   causes presence, what causes feeding, spawn timing/location/mechanics, diet.
   Zero species notes have a spawn/diet/feeding section. Nailing the structure
   is also the gap-detection mechanism: an empty mandated section IS the gap
   report.
3. **Too much text for AI and human readers.** Hundreds of `**Observed**`
   blocks landed inline (76% of yellowtail.md's 1,556 lines), burying the
   decision tables the KB exists to serve.
4. **No fact check has ever run** (source fidelity, internal consistency,
   external verification of biology + regulatory claims).
5. **Spots aren't KB pages** — location knowledge stops at the zone lexicon;
   no per-spot pages.

**Structural model (Cameron): the RuneScape wiki.** Plain assertion; citations
on quotes, statistics, and disputables; one canonical section order per article
type enforced by machinery, not discipline; progressive disclosure (infobox →
lead → sections); subpages to drain detail; location pages with a containment
hierarchy plus "who's there" tables. Everything runs unattended via GitHub
Actions, reusing the battle-tested batch-3 pipeline, with one GATE B review at
the end.

## Decisions locked with Cameron (2026-08-23)

| # | Decision |
|---|---|
| 1 | Observations move to **per-note evidence subpages** (`species/evidence/yellowtail.md`), compressed to one-liners grouped by the section they support; the main note keeps a one-line `## Evidence` link. Nothing deleted. |
| 2 | **Corpus-only.** No external sources fill biology gaps. Missing content becomes `⚠ Flagged gap — no corpus source` entries feeding a generated gap report. |
| 3 | Fact check runs **all three modes** (source fidelity vs transcripts; internal cross-note consistency; external web verification of biology/physics + regulatory claims). **Flag, never delete** — single-source ≠ wrong; flags queue for Cameron's manual review. |
| 4 | Delivery via the **batch-3 pattern**: one review branch, worklist-driven self-re-dispatching Action, per-note commits, HTML review page, one GATE B review. |
| 5 | ~~Species stay **one note**; the `decision` spin-out valve remains.~~ **SUPERSEDED (v2.1, v2.2).** Species now have two sub-article rungs: `zone-guide` (`species/<species>-<zone>.md`) and `species-technique` (`species/<species>-<technique>.md`, optional zone variant). The `decision` type is retired — `species/bluefin-tuna-trolling.md` was its only instance and is now a `species-technique`. |
| 6 | Front matter grows into a **modest infobox**: ~5–8 per-type structured fields, validated like `regions`/`waters`. |
| 7 | Batch 3 merges first — DONE (verified 2026-08-23: `origin/main` contains the batch-3 GATE B merge; the review branch sits at main's tip `1e66a92`). |
| 8 | GATE A/B apply: this doc committed, Cameron sends `PLAN APPROVED`, supervised foundation, unattended fleet, GATE B review + merge. |
| 9 | **Spots become KB pages** — still true, but the hierarchy grew (v2.2). Five rungs, one type per rung, FLAT in `locations/` with the chain carried by a `parent` path field: **jurisdiction → region → area → zone → spot**. `area` is optional and built only where the corpus earns it; the census currently mints none. |
| 10 | **INVERTED (v2.2).** `sources/spot-lists.md` is the **authority**, not a third input: its `##` sections are the zone skeleton and its 391 coordinates decide zone membership. The KB harvest is demoted to a *depth* signal — it decides how much a page can SAY, never whether it exists. **Every spot in the library gets a page** (Cameron, 2026-08-24), minimum coordinates + parent zone. Charted/public coordinates only; personal waypoints stay profile-only. |

### The inventory (restated 2026-08-24 — spots changed the shape of this job)

Six tiers, not three. Costs are the budget points
`scripts/review/next-note.py` spends per unit.

| tier | cost | what | count |
|---|---|---|---|
| `full` | 5 | species routers | 24 |
| `standard` | 2 | techniques, lures, rigging, conditions, seasonal, bait, the 13 pre-existing `locations/` notes | 135 |
| `light` | 1 | tackle, fish-care, planning — structure/citation normalization only | 99 |
| `geo` | 2 | **NEW** — jurisdiction (2) + region (5) + zone (76) | 83 |
| `gazetteer` | 2 | spot pages the FLEET writes (corpus material exists) | ~13, grows with harvest |
| `cluster` | 3 | cross-note consistency sweeps | ~30 |
| `relocate` | 1 | queued cross-note moves | 8 open |

**Outside the fleet entirely:** ~327 minimum spot pages are generated
**mechanically** by `scripts/review/build-spot-pages.py`. Only a handful of
the 344 spot pages have any corpus material; the rest carry a coordinate and a
parent zone, and handing those to Opus meant writing ~330 pages from a
template at two subagent calls each — half the entire remaining job — while
retyping 391 coordinate pairs. A wrong waypoint is a real-world hazard, so
those positions are copied from the parsed source digit-for-digit and asserted
every chunk by `scripts/review/check-coordinates.py`.

`locations/` is therefore the largest folder in the review by a wide margin —
427 ladder pages against `tackle`'s 86 — not the 13 notes this plan originally
counted.

`profiles/` is guard-protected, so profile normalization happens in the
supervised endgame, not the fleet.

## Target structure

### Species note (FULL)

```
(front matter infobox)   existing fields + scientific_name, season_peak, sst_band_f,
                         depth_band, gear_classes, sonar_depth ('unknown' legal, auto-flags)
Lead                     2–4 sentences: what it is, why it matters, season in one breath
## Where & when          (exists)
## Presence & forage     WHY they're in a zone + what they eat            (NEW)
## Spawning              when/where/how + effect on the bite             (NEW)
## Feeding triggers      light, tide/slack, current, moon                (NEW)
## Finding them (sign & sonar)                                           (exists)
## Situations → techniques   ranked, footnoted conditions                (exists)
## Gear summary (class terms)                                            (exists)
## Regulations           jurisdiction + as-of + verify-current           (NEW, standardized)
## Doctrine & conflicts  side-by-side, attributed, decision frames       (exists)
## Landing & handling    short; links fish-care/                         (NEW)
## Evidence              one link → species/evidence/<name>.md           (NEW)
## Linked from           (auto)
```

### Technique note (STANDARD)

Lead → `## Reach for this when` → free mechanics sections → `## Gear class`
(mandated) → `## Common failures` (mandated) → `## Evidence` → `## Linked from`.
Source-named `##` sections merge into the skeleton.

### Spot page (NEW — locations gazetteer)

```
(front matter)   type: location, regions/waters (already gated) + parent (link,
                 validated), structure_type, depth_band, distance_nm, coordinates (charted only)
Lead → ## Getting there → ## Structure & bathymetry → ## What's there (species-by-season
table linking species routers) → ## How it fishes (current/wind/tide behavior) →
## Evidence → ## Linked from
```

### Prose & citation rules (repo-wide)

- Facts stated plainly, present tense. No hedging — uncertainty becomes a flag
  or a gap, never "some say".
- Compact cite — `` (`videoId`) `` or `(cameron)` — mandatory on quotes,
  statistics, and disputable claims. Attribution preambles and channel-status/
  confidence boilerplate compressed out (confidence lives in front matter;
  provenance in the evidence file).
- Doctrine conflicts keep names inline + a decision frame — there, attribution
  IS the content.
- Flag grammar: `⚠ Fact-check (<category>): …` / `⚠ Flagged gap — no corpus
  source` / `⚠ cite-unresolved`. Ledger categories: `single-source |
  contradicted-by-source | contradicted-internal | external-mismatch |
  cite-unresolved | flagged-gap`.

## Key mechanisms (verified against the repo)

- **`layout: v2` opt-in flag**: a new front-matter key written by the
  transform; all new validation (section order, infobox fields, evidence
  pairing) applies only to `layout: v2` notes — CI stays green while 250+
  notes are mid-migration.
- **Review guard replaces the line-count deletion rule with conservation
  rules**: (a) cite conservation — source tokens before ⊆ note-after ∪
  evidence-after; (b) observation conservation — `**Observed**` blocks removed
  ≤ evidence entries added; plus a **scope rule** — a commit
  `review: <note> — <phase>` may touch only the named note, its evidence file,
  READMEs, and exempt logs. Protected paths unchanged, plus `templates/`.
- **`export-site-index.py` evidence exemption is mandatory** — it currently
  hard-fails on any nested subdir of a published folder, and `validate.yml`
  dry-runs it on every PR.
- **Bare-date cite resolution is scriptable**: front-matter `sources` ∩
  manifest `upload_date` within [date, date+2d] (verified: `(8/3/22)` in
  `species/yellowfin-tuna.md` resolves uniquely to `CMQkHQMxbXM`).
- **Cross-note relocations** (the HookUp-Baits/C-1 case: content filed under
  the wrong lure/technique/species; the fix spans multiple notes plus new
  sections or new notes): the per-note transform NEVER moves content across
  notes in-line. It appends a row to a **relocation queue**
  (`sources/relocation-queue.md`: `| src | dst | what | rationale | cite |`,
  dst may be `NEW: <path>`) and drops a `⚠ misplaced-content` flag in place.
  After the transform phase, a dedicated pass (`prompts/relocate-content.md`)
  processes the queue: one commit per relocation with subject
  `review: relocate <src> → <dst>`, guarded by a **paired conservation rule** —
  cites/content leaving src must appear in dst ∪ evidence; the touch-set
  widens to src + dst (creation allowed — the repo's own rule "the router
  never absorbs execution — create the technique note" already mandates it) +
  both evidence files + READMEs + logs. Every relocation is adversarially
  verified, logged in the judgment-calls list, and surfaced on a dedicated
  review-watch panel; the agent's `escalate` verdict routes genuinely
  ambiguous reclassifications to Cameron instead of guessing. Relocations run
  BEFORE fact-check/consistency so those passes see final placement; stale
  references in third notes are caught by the cluster consistency sweep.

## Phases

### Phase 0 — Foundation (supervised session; touches guard-protected paths)

0. This document is committed; **Cameron replies `PLAN APPROVED` (GATE A)
   before any further foundation commits.**
1. **`templates/`** (new top-level dir): `style-guide.md` + one skeleton file
   per type (species, technique, lure, rig, conditions, seasonal, bait,
   location, tackle, fish-care, planning, evidence) — required sections in
   canonical order (extras allowed between), infobox fields, mini example.
   `link-maintenance.py` gets `VALIDATE_ONLY_DIRS = {templates/}` (links
   checked; not indexed/backlinked). The review guard adds `templates/` to
   PROTECTED.
2. **`scripts/note_schema.py`**: REQUIRED_SECTIONS + INFOBOX_FIELDS per type,
   cite regexes, flag grammar — the single source of truth for all validators.
3. **`scripts/link-maintenance.py` extensions** (+ fixtures in
   `tests/test_link_maintenance.py`, wired into `validate.yml`): `layout: v2`
   section/infobox validation (same all-or-nothing exit-1 pattern as region
   gating); evidence pairing in both directions; `type: evidence` NOT
   region-gated, skipped by the granularity watch, otherwise rides the
   existing backlinks/index machinery unchanged; location `parent` must
   resolve.
4. **`scripts/export-site-index.py`**: skip `evidence/` subdirs.
5. **`scripts/review/guard.py`** (clone of the batch-2 guard; conservation +
   scope rules above; trailer `Review-Guard: revert-of`). Exempt logs:
   `sources/review-worklist.md`, `fact-check-ledger.md`, `review-progress.md`,
   `gap-report.md`, `spot-harvest.md`, `relocation-queue.md`,
   `regulatory-claims.md`, `escalations.md`.
6. **`scripts/review/`**: `next-note.py` (worklist reader, `--count`/
   `--budget`, exit 2 on malformed; derives the active phase from row
   statuses), `commit-note.py` (sanctioned wrapper, exit-code contract
   0/2/3/4/5: row rewrite → check-note → link-maintenance → commit → guard
   check → push with rebase retry), `check-note.py` (machine acceptance:
   skeleton, evidence conservation, cite coverage — fail on uncited quotes,
   warn on uncited numbers — no legacy cite forms), `resolve-cites.py`
   (deterministic normalizer, run ONCE supervised; ambiguous →
   `⚠ cite-unresolved` + ledger), `build-worklist.py` (~257 rows from the tree
   + tier map), `build-spot-worklist.py` (dedupes the harvest into gazetteer
   rows), `gap-report.py`, `progress.py`, and `scripts/build-review-watch.py`
   (HTML: before/after vs merge-base, flag ledger, gap report, status board,
   relocations panel).
7. **Prompts** (siblings of the batch-3 set): `prompts/review-note.md`
   (single-pass transform: restructure + rewrite + evidence split +
   corpus-only new sections via targeted transcript grep + infobox +
   `layout: v2` + append spot mentions to `sources/spot-harvest.md`
   (`| spot | note | section | claim | cite |`); the front-matter `sources`
   list is append-only, never reflowed), `prompts/factcheck-note.md`
   (per-claim fidelity vs the cited transcript only, sharded ≤6 transcripts
   per subagent; FULL = all cited claims, STANDARD = quotes/statistics; tags
   biology/physics claims `ext-verify`), `prompts/relocate-content.md`
   (processes the relocation queue: paired-conservation moves, new-note/new-
   section creation, judgment-calls logging, escalate-on-ambiguity),
   `prompts/gazetteer-spot.md` (builds `locations/<spot>.md` from harvest +
   spot-lists + Cameron's profile, hierarchy-linked, corpus-only),
   `prompts/verify-review.md` (adversarial, "the patch is guilty": check-note
   + conservation hunt + corpus-cite spot-checks ≥3),
   `prompts/orchestrate-review-chunk.md` (thin loop: next-note → reset-tree →
   transform/factcheck/relocate/gazetteer subagent by row status → verify →
   commit-note → exit-code handling).
8. **`.github/workflows/review-chunk.yml`** (clone of `ingest-chunk.yml`):
   branch `claude/knowledge-base-review-g00k8s`, concurrency `kb-review`,
   preflight `next-note.py --count`, allowedTools UNCHANGED (no web tools),
   sweep = review guard, checkpoint runs progress + gap-report, budget 16
   points/chunk (FULL=5, STANDARD=2, LIGHT=1 ≈ 3 full or 16 light per chunk),
   chain ≈ 100 chunks, under the 200 cap.
9. **`sources/` files** (worklist, ledger, harvest, relocation queue,
   progress, gap-report) + **CLAUDE.md amendments** (observation rule →
   evidence subpages; citation standard; templates + `layout: v2`; evidence
   type; infobox fields; flag grammar; "no PERSONAL coordinates"; review-guard
   summary). Run `resolve-cites.py`; full local validation.
10. **Supervised pilot** (amended per Cameron, 2026-08-23: pilot on the notes
    he knows best, with an involved review): hand-run transform + verify on
    **`species/yellowtail.md`** (full — the most important article in the repo
    AND the hardest: 1,556 lines, 85 sources, 63 observed blocks; exercises
    the evidence split, cite conservation, biology-gap flagging, and likely
    the relocation queue at max scale), **`techniques/surface-iron.md`**
    (standard — yellowtail's signature technique, so the router↔technique
    interplay is reviewable in one sitting), and one tackle-express note
    (light). Cameron reviews yellowtail in depth — this pilot is a feedback
    loop, not a spot-check — and templates/prompts are adjusted before the
    chain dispatches. Reconcile the observed-block count (exact-marker grep
    ~397 vs audit 477) at worklist build.

### Phase 1 — Fleet: transform (unattended)

Worklist rows `| note | tier | status | flags | result |`; status machine
`pending → transformed → fact-checked → done` (+ `skipped | escalated |
reverted` terminals; LIGHT skips fact-check). Folder order: species first
(spec defects surface on the highest-value tier; Cameron can watch the
review-watch page and drop the STOP file cheaply), then techniques, lures,
rigging, conditions, seasonal, bait, locations, planning, fish-care, tackle
last.

### Phase 1.5 — Relocations (same workflow, rolls automatically)

When no `pending` rows remain, `next-note.py` emits relocation-queue rows
first: one paired-conservation commit per relocation, verified adversarially,
escalations to Cameron. Only then does fact-check begin, so it sees final
placement.

### Phase 2 — Fleet: fact-check + internal consistency (rolls automatically)

When the relocation queue is drained, `next-note.py` emits `transformed` rows.
Per-claim source fidelity (sharded); flags inline + ledger. Then ~30
mechanically-generated **cluster rows** (`cluster:bluefin` = router + its
linked technique/lure notes) for the cross-note contradiction sweep →
`contradicted-internal` flags in both notes.

### Phase 3 — The geographic ladder (same workflow, two tiers + one script)

Restated 2026-08-24; this section previously described only spot harvesting.

**`geo` tier (83 units, runs FIRST of all phases).**
`scripts/review/build-geo-worklist.py` derives the ladder from
`sources/spot-lists.md` coordinates and appends rows;
`prompts/geo-page.md` is the worker. Order matters twice over: a spot page
cannot resolve `parent` until its zone exists, and a species note being
rewritten should link a real zone page rather than fall back to a plain-text
name. `scripts/review/next-note.py` `buckets()` therefore puts `geo` ahead of
`transform`.

**Mechanical spot pages (~327, no fleet involvement).**
`scripts/review/build-spot-pages.py` runs at every chunk checkpoint and writes
the minimum pages under whatever zones have landed so far — self-sequencing,
idempotent, and it never touches a page that already exists. Coordinates are
copied from the parsed source digit-for-digit;
`scripts/review/check-coordinates.py` asserts every published position against
the library on every chunk and fails the sweep on a mismatch.

**`gazetteer` tier (~13 and growing).** Only spots that actually have corpus
material go to the fleet, via `prompts/gazetteer-spot.md`. As transforms feed
`sources/spot-harvest.md`, `build-spot-worklist.py` promotes newly-sourced
spots into this tier.

Nine isolated banks have a spot whose slug equals its own zone slug (Tanner
Bank, San Juan Seamount, The Bumps…). There the zone page IS the place and no
second file is minted.

### Phase 4 — External verification (separate workflow `verify-external.yml`)

Separate on purpose: web tools (`WebFetch,WebSearch`) are granted ONLY here,
never to the fleet that rewrites notes; the unit of work is a claim, not a
note. Processes `sources/regulatory-claims.md` rows + `ext-verify` ledger rows
in chunks; stamps `verified-current <date>` / `external-mismatch` verdicts in
the ledger; refreshes jurisdiction/as-of/verify-current stamps in notes.
Mismatches are flags, never edits.

### Phase 5 — Endgame (supervised) + GATE B

Profiles LIGHT normalization (guard-protected, human in loop); coverage
summary (worklist accounting: every row `done|skipped|escalated`;
observation-conservation totals; before/after word counts per folder);
judgment-calls list; final gap report; ledger triage counts; review-watch
refresh; retire the workflows (`review-chunk`, `verify-external` and the
`main` trampoline + registration copies, batch-3 retirement pattern).

**The geo layer adds its own GATE B preconditions (2026-08-24):**

- **Coordinate conservation**, the geo analogue of observation conservation:
  `391 spots = pages + AR-table rows + excluded` must still reconcile, and
  `check-coordinates.py` must exit clean — every published position tracing to
  `sources/spot-lists.md` digit-for-digit.
- **Census accounting**: every zone in `sources/geo-census.txt` has a page,
  and every page has a zone. No orphans in either direction.
- **Dispositions Cameron owes a call on**, all surfaced by the census and none
  of them auto-resolvable: the parent-distance outliers, the spots carrying
  MPA/advisory labels, the 2 excluded naval security zones, and the
  coordinate-less stubs (Cabo San Lucas, Loreto, La Paz).
- **The map** (`Review Watch → Map`) is a review surface in its own right:
  zone hulls, colour-by-zone and the needs-review layer are how a bad carve-up
  is seen rather than inferred from a column of numbers.

One GATE B review by Cameron on the review-watch page → merge to `main`.

## Verification

- Per-note: `check-note.py` + `link-maintenance.py` green (links, gates,
  `layout: v2` skeleton, infobox, evidence pairing) + the adversarial verify
  agent (conservation hunt, corpus-cite spot-checks) before every commit;
  guard check post-commit.
- CI: `validate.yml` (link-maintenance + idempotence diff + export dry run +
  pytest) on every PR.
- Pilot gate: 3 hand-run notes reviewed by Cameron before the chain starts.
- Endgame accounting: every worklist row terminal; every flag in the ledger;
  every gap in the report; the GATE B package mirrors the batch-3
  coverage-summary convention.

## Risks (top ones, with mitigations)

- **Chain-length against the 200-chunk cap.** The ladder roughly doubled the
  unit count, and geo pages commit as `transformed`, so they re-enter the
  fact-check bucket. Mechanical spot generation is what keeps this tractable:
  ~661 points ≈ 41 chunks, against ~1,333 ≈ 83 had the fleet written every
  spot. Still well inside the cap, but it is now a number to watch rather than
  an assumption — `next-note.py --count` and the review-watch ETA are the
  gauges, and the cap lives in `.github/workflows/review-chunk.yml`.

| Risk | Mitigation |
|---|---|
| Guard reverts legit compression | Conservation rules replace the line-count deletion rule; the pilot exercises them first |
| `export-site-index` fails CI on evidence dirs | Exemption lands in Phase 0, before any evidence file exists |
| Context overflow (yellowtail: 1,556 lines, 85 sources) | Transform never opens transcripts; fact-check shards per-claim to the cited transcript only, ≤6/subagent |
| CI red mid-migration | All new validation is `layout: v2` opt-in |
| Worklist merge conflicts | Single chain (concurrency group + in-flight guard) + rebase-retry push — ran 835 rows in batch 3 |
| Style drift across ~257 notes | Verify agent checks against `templates/`; Cameron samples early species output; the STOP file kills the chain cheaply |
| 85-source front-matter lines corrupted | `sources` append-only in prompts; guard cite-conservation catches drops |
| Dead run / half-done note | Per-note commits + row status + reset-tree at boundaries + STOP — inherited from batch 3 |


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
