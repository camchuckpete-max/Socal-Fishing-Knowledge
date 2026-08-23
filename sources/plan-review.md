# Plan: Full KB Editorial Review — structure, rewrite, evidence split, fact check, gazetteer

> **Provenance:** governing plan document for the full editorial review of the
> knowledgebase, committed as `sources/plan-review.md` per the repo convention
> that the governing spec lives beside the work it governs (pattern:
> `sources/plan.md`, 2026-08-12). Scope and decisions were worked out with
> Cameron in conversation on 2026-08-23.

**Status: Cameron's `PLAN APPROVED` for this document (including the
yellowtail/surface-iron pilot amendment) was given 2026-08-23 — GATE A is
unlocked and the foundation build is executing.** Any later amendment to this
plan re-opens GATE A per `CLAUDE.md`. GATE B (merge to `main`) remains locked
until Cameron's post-build review of the coverage summary + judgment-calls
list.

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
| 5 | Species stay **one note** (no targeting split); the decision spin-out valve (`species/bluefin-trolling.md` pattern) remains. |
| 6 | Front matter grows into a **modest infobox**: ~5–8 per-type structured fields, validated like `regions`/`waters`. |
| 7 | Batch 3 merges first — DONE (verified 2026-08-23: `origin/main` contains the batch-3 GATE B merge; the review branch sits at main's tip `1e66a92`). |
| 8 | GATE A/B apply: this doc committed, Cameron sends `PLAN APPROVED`, supervised foundation, unattended fleet, GATE B review + merge. |
| 9 | **Spots become KB pages**: a `locations/` gazetteer modeled on RS-wiki location pages — containment hierarchy (region → zone/complex → named spot), infobox, species-by-season "what's there" table linking the species routers. |
| 10 | Gazetteer scope: **harvest the existing KB** (the per-note pass logs spot mentions) + `sources/spot-lists.md` + Cameron's profile; transcript re-mining is a future batch. **Charted/public coordinates OK** on universal spot pages; personal waypoints stay profile-only; the CLAUDE.md rule becomes "no PERSONAL coordinates". |

Effort tiers: **FULL** species (24); **STANDARD** techniques (49), lures (16),
rigging (31), conditions (12), seasonal (9), bait (3), locations (13);
**LIGHT** (structure/citation normalization only) tackle (86), fish-care (7),
planning (6). `profiles/` is guard-protected, so profile normalization happens
in the supervised endgame, not the fleet.

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
(front matter)   type: location, regions/waters (already gated) + parent_zone (link,
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
   existing backlinks/index machinery unchanged; location `parent_zone` must
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

### Phase 3 — Gazetteer (same workflow)

`build-spot-worklist.py` dedupes `sources/spot-harvest.md` into `spot:` rows;
`gazetteer-spot.md` builds/updates spot pages (hierarchy front matter, "what's
there" table, charted coords where public); new pages enter the worklist as
`transformed` so they flow through fact-check + verify like everything else.

### Phase 4 — External verification (separate workflow `verify-external.yml`)

Separate on purpose: web tools (`WebFetch,WebSearch`) are granted ONLY here,
never to the fleet that rewrites notes; the unit of work is a claim, not a
note. Processes `sources/regulatory-claims.md` rows + `ext-verify` ledger rows
in chunks; stamps `verified-current <date>` / `external-mismatch` verdicts in
the ledger; refreshes jurisdiction/as-of/verify-current stamps in notes.
Mismatches are flags, never edits.

### Phase 5 — Endgame (supervised) + GATE B

Profiles LIGHT normalization (guard-protected, human in loop); coverage
summary (worklist accounting: every note `done|skipped|escalated`;
observation-conservation totals; before/after word counts per folder);
judgment-calls list; final gap report; ledger triage counts; review-watch
refresh; retire the workflow (batch-3 trampoline-retirement pattern). One
GATE B review by Cameron on the review-watch page → merge to `main`.

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
