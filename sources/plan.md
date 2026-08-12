# Plan: Build SoCal/Baja Fishing Knowledgebase

> **Provenance:** this is the governing plan document for the KB build,
> committed to the repo as `sources/plan.md` per Cameron's decision
> (2026-08-12, with the GATE A approval of the punch-list revision) so the
> governing spec lives beside the work it governs. The P5 governing-doc sync
> edits (Context correction, tree counts, regime framing) are applied in place
> and marked where they occur.

---
## ▶ GATE B Punch List (P1–P6) — APPROVED & EXECUTED, awaiting GATE B review

**Status:** Cameron's `PLAN APPROVED` for this revision was given 2026-08-12
(after the resuming session's state report). P1–P6 were executed in a single
commit ("GATE B punch list P1–P6") on branch
`claude/socal-fishing-kb-handoff-tp8lsx`. **GATE B — Cameron's post-build
review and merge decision — remains open.**

Cameron's expert pre-merge read. Execution-quality corrections + one
house-doctrine restructure (P5). This revision RE-OPENED GATE A (per the gate
rule — it amends the plan document and adds CLAUDE.md rules); execution of
P1–P6 began only after Cameron's fresh `PLAN APPROVED` for this revision. Once
approved: apply → run `scripts/link-maintenance.py` → **one commit** ("GATE B
punch list P1–P6") → push → **STOP at GATE B (do NOT merge; wait for Cameron's
separate GATE B decision).**

**P1 — `species/yellowtail.md` Where & when, rebuilt range-wide N→S** (present the
fishery evenly; SD/BOLA weighting is Cameron's *profile*, not the fishery):
Channel Islands incl. **SBI / Sutil squid→yellowtail zone** (4/21/22 `YZtX1MiT0y8`
squid-zone bite + squid-color/glow jig; 10/26/22 `5p6gu14ZC4w` "Nick/SBI …
catching yellowtail on squid") · **Catalina / SCI promoted to full entries** (out
of the buried bullet) · **coastal kelps** · **La Jolla / SD banks / Coronados** ·
**Baja coast** · **BOLA**. Add `5p6gu14ZC4w` to sources.

**P2 — `techniques/surface-iron.md`**: new **Size / weight selection** section —
wind-up → **heavier iron** to punch the cast (`D5DR7Kx42_A`); anchovy / "rice"
year → **downsize to lighter/smaller iron**, match the hatch (2/27/25
`pcwcRdmWmLc`). New **Color** section: honest **thin area** — no systematic color
doctrine in current sources (only a lone squid-color-with-glow observation,
4/21/22); awaiting the ~400-video batch. **Do not invent one.** Add `pcwcRdmWmLc`.

**P3 — `species/yellowfin-tuna.md`**: expand the trolling row into a **full
situation entry** — cedar plugs / feathers at **~6–6.5 kt** (already linked),
troll-to-locate vs cast; **flag spread-design depth (setback/position geometry)
as a thin area** (corpus gives speeds, not spread geometry).

**P4 — `species/yellowtail.md`** trolling **thin-area stub row** (trolled in the
real fishery, esp. Baja — no corpus source; flagged, pending new sources). **New
CLAUDE.md router rule:** a method popular in the real fishery but absent from
sources gets a **flagged stub, never silence** (silence reads as "not a method").
**Router-stub audit sanctioned** — audit the other routers and add flagged stubs
where clearly warranted; **log every stub added** to the judgment-calls list.

**P5 — Regime layer (Cameron house doctrine; attributed `cameron`, high):**
- New **`conditions/water-regimes.md`** — four **water-state** regimes
  (winter/upwelling · warming transition · warm stable · fall fragmentation),
  each with defining water state, typical-month mapping, and **anomaly guidance**
  ("warm years: warm-stable can arrive in March — use the regime note, not the
  month note").
- **`seasonal/README.md`** — curated prose above the auto-index routing
  **regime-first** (months are the typical-year mapping).
- Each **month note (8)** — header line naming its regime. *(Count corrected
  from "(9)" in the approved punch list: `seasonal/` holds 9 notes = 8 month
  notes + `year-anniversary-prior.md`.)*
- **Species Where & when** — key to **regime, month in parentheses** (e.g.
  "warm-stable regime (Aug–Sep)"), across species with seasonal content.
- **`seasonal/year-anniversary-prior.md`** — reframed as a **location prior
  WITHIN a regime**, attributed; the water-state-vs-anniversary conflict stays
  visible.
- **Governing-doc sync (same execution):** update **this plan document's**
  "Directory tree + note decomposition" **tree counts and section descriptions**
  so the governing doc matches the repo after execution — e.g. `conditions/`
  **12** (adds `water-regimes.md`), `techniques/` **18** (already incl.
  `deep-drop-swordfishing`, `hoop-netting`), and the regime-first seasonal
  framing. *(Applied throughout this file.)*

**P6 — Log P1–P5** in `sources/extraction-log.md` judgment-calls as **GATE B
review corrections**.

**Execution:** I write the core (water-regimes, seasonal README + month headers +
year-anniversary reframe, yellowtail, surface-iron, yellowfin, CLAUDE.md rule);
one focused subagent pass keys the remaining species Where & when to regimes.
`water-regimes.md` is created as a real note (no stub). **Verification:**
link-maintenance 0 dead links + idempotent; species acceptance test still 18/18;
`water-regimes.md` linked from seasonal + species; year-anniversary conflict
still visible; **grep confirms no invented color doctrine**; build script still
works with/without profile.

---


## Conformance table — Revision pass 3 (RESIDUAL FIXES + AMENDMENTS v3)

| Item | Change | Section(s) edited |
| --- | --- | --- |
| R1 | Canonical example → `species/bluefin-trolling.md` (was techniques/) | Governing conventions (altitude/spin-out) |
| R2 | §5–6 boat.md split corrected; identical wording here + log spec | Export→destination map (§6); Decomposition → profiles/cameron |
| R3 | Name **GATE A** (execution) and **GATE B** (merge); A's token ≠ B | GATES section; Merge gate; Execution |
| V3-1 | Registry-based confidence; manifest gains channel+upload_date; `sources/source-registry.md` seeded | Governing conventions (confidence); Decomposition → sources/; Execution step 0 |
| V3-2 | `**Observed** (channel, date, location):` convention; observations never change doctrine | Governing conventions (observation) |
| V3-3 | Batch-ingestion pipeline documented in CLAUDE.md (process only) | Future ingestion pipeline |
| V3-4 | CLAUDE.md notes a ~400-video multi-channel batch is the expected first use | Future ingestion pipeline |

## Conformance table — PLAN AMENDMENTS v2 (all ten, retained)

| # | Amendment | Section(s) |
| --- | --- | --- |
| 1 | `bluefin-trolling.md` → `species/`; spin-outs live in species/ | Conventions; Routing #3; species/ + techniques/ |
| 2 | Add `planning/report-reading-and-forecasting.md` | planning/; Execution |
| 3 | Add `species/ocean-whitefish.md`; mako/thresher = absent | species/; Thin areas |
| 4 | cameron doctrine=high, open-items=attributed not doctrine | Conventions (confidence) |
| 5 | Export sections → MULTIPLE destinations; "at least once, logged" | Export→destination map; Verification |
| 6 | Merge gate; main is canonical | GATES; Merge gate |
| 7 | `extraction-log.md` incremental per commit; finish verifies | Execution; sources/ |
| 8 | Kingfish = FL king mackerel → drop note | species/; Thin areas |
| 9 | Retain spot input renamed `sources/spot-lists.md` | Context; sources/ |
| 10 | Mermaid cap = 30, uniform | Conventions |

## GATES (named; override everything earlier)

- **GATE A — execution.** Nothing in this conversation constitutes approval to
  execute; "then approved to execute" and similar are void. GATE A unlocks ONLY
  by a future Cameron message containing exactly **`PLAN APPROVED`**. Applying
  amendments or returning the plan does not unlock it; **any later amendment
  re-opens GATE A.** Step 0 writes this rule verbatim into CLAUDE.md.
- **GATE B — merge to main.** Unlocked ONLY by Cameron's **post-build review**
  of the coverage summary + judgment-calls list, after which he merges to
  `main`. **GATE A's `PLAN APPROVED` token does NOT satisfy GATE B.** Nothing is
  canonical until merged; consumers (raw fetches, skill builds, future MCP)
  target `main`.

Status: species-first routing addendum + all ten v2 items + revision-pass-3
(R1–R3, V3-1–V3-4) are folded in. The main build (steps 0–7 + finish) received
`PLAN APPROVED` and was executed on branch `claude/socal-fishing-kb-build-tej9qg`
(head `139a883`); the GATE B punch list (P1–P6) received its own `PLAN APPROVED`
(2026-08-12) and was executed. **Awaiting GATE B.**

## Context

Cameron wants a personal-but-multi-user SoCal/Baja fishing knowledgebase in
`camchuckpete-max/Socal-Fishing-Knowledge`, plain GitHub markdown (no wikilinks).
It is the **system of record for fishing KNOWLEDGE**, paired with BightSST
(system of record for CONDITIONS); Claude chat is the day-planning surface.
Current state *(corrected 2026-08-12, P5 governing-doc sync — the original
"repo empty — fresh build" line was historical, true at plan time only)*: **the
full build is COMPLETE** — steps 0–7 + finish on branch
`claude/socal-fishing-kb-build-tej9qg`, followed by the GATE B punch list on
`claude/socal-fishing-kb-handoff-tp8lsx`. The repo, its `CLAUDE.md`, and
`sources/extraction-log.md` are the source of truth for current state.

**Mission (into CLAUDE.md purpose + root README, near-verbatim):** guide a
brand-new-to-SoCal fisherman through the full chain — where to go, when to go,
which techniques and when each applies, what tackle per technique, how to use a
fish finder to locate fish, and how to fish each technique.

**Scope principle:** the KB captures **all** valuable SoCal/Baja-specific
knowledge from the full **128**-transcript corpus that clears the curation bar,
**independent of whether Cameron targets/owns/has done it**. `memory-export.md`
merges in as attributed doctrine + populates his profile; it never bounds scope.

Inputs: `transcripts.zip` → 128 transcripts + `_manifest.csv` (kickoff said
~129; reconciles to 128); `bd-transcript-knowledge-proposal.md` (decompose,
don't re-derive); `memory-export.md` (preserve every number exactly);
`spot-lists-PRIVATE-ONLY.md` (GPS coords).

**Key decisions:**
- Repo is PUBLIC; Cameron waived the private-only rule ("none of these spots are
  secret"). Spot file + `profiles/cameron/spots.md` with coordinates committed.
- **[A9]** spot source retained renamed `sources/spot-lists.md`; choice logged.
- **[R3/A6]** `main` canonical; GATE B controls the merge.
- No `*.skill` zips → skills/ scaffolded with a build plan + generic build script.

## Governing conventions (every note)

- **Links:** relative markdown links, human text only. NO `[[wikilinks]]`.
- **Front matter:** `type`, `tags`, `sources`, `confidence`. **[V3-1] `sources`
  stay `video_id`s** (or `cameron`). No `owned` on general notes.
- **[V3-1] Confidence (registry-based):** **HIGH** = repeated doctrine from a
  source listed in **`sources/source-registry.md`** (seeded: Erik Landesfeind /
  SoCal Bight Fishing Academy, BD Outdoors named captains, `cameron`), OR
  anything `cameron`. **Unregistered channels cap at MEDIUM.** Sponsored/
  promotional = **LOW** regardless of channel. Cameron promotes sources by
  editing the registry. **[A4]** cameron-sourced *doctrine* is high; cameron
  *open items* ("open to", "considering", "wants to try") are captured as
  **attributed open items, never asserted as doctrine.**
- **[V3-2] Doctrine vs observation:** on-the-water/report footage yields
  **observations, not rules**. Inline under the relevant doctrine:
  `**Observed** (channel, date, location): <what happened, with conditions>`.
  **Observations never change a note's stated doctrine;** contradictions sit
  beside it, attributed. Added to CLAUDE.md.
- **Altitude:** decision logic at species/technique level; implementation at
  gear level; gear in **class terms**. **[R1] Canonical example (CLAUDE.md):**
  `species/bluefin-tuna.md` holds WHEN to pull Mad Mac vs spreader bar vs kite
  vs speed-troll, spinning the table out to **`species/bluefin-trolling.md`**
  when it grows (NOT techniques/); `lures/mad-mac.md` holds specs + links back.
- **[A1] Decision spin-out notes always live in `species/`** (techniques/ is
  execution-only). Rule in CLAUDE.md.
- **Doctrine MERGES** attributed; conflicts side by side, never reconciled.
- **Curation bar:** decision knowledge; knots/rigging = parameters + judgment +
  link the source video URL (never transcribe). Generic filler / out-of-region
  skipped and logged.
- **[A10] Mermaid cap = 30 nodes**, in CLAUDE.md, uniform.

## Species-first routing (routers own the situation→technique map)

1. **Species notes are routers.** Template: **Where & when** (link seasonal/ +
   locations/; **keyed to regime, month in parentheses** — P5) · **Finding them**
   (sign, birds, **species-specific sonar signatures with depths** — yellowtail
   5–10 fm near structure, bluefin 30–50 fm in wind, swordfish in/below DSL —
   link search-and-glassing + electronics-and-sounder) · **Situations →
   techniques** (table: conditions → ranked technique(s) → gear class →
   technique-note link) · **Gear summary** (class terms, link gear-classes) ·
   **Doctrine & conflicts** (attributed).
2. **Technique notes = execution only** + "Reach for this when"; the generated
   `## Linked from` + that list is the reverse map.
3. **[A1] `species/bluefin-trolling.md`** is the escape valve; router keeps a
   summary + link.
4. **Acceptance test** (finish; failures → judgment-calls): a species note read
   alone answers where/when/how-to-find (incl. meter)/technique-per-situation/
   gear-class, deeper detail one link away.
5. **(P4) Flagged stubs, never silence:** a method popular in the real fishery
   but absent from sources gets a flagged stub row in the router — logged in
   judgment-calls. Rule in CLAUDE.md.

## [A5] Export section → destination map (sections fan out to MULTIPLE notes)

Each export section logged with **at least one** destination; **every
destination logged**. Named splits:
- **§5** boat platform → `profiles/cameron/boat.md`.
- **[R2] §6** → **`boat.md` takes §5 plus the §6 PLATFORM facts (holder
  count/angles/geometry, no outriggers, 2–3 lures, shotgun = furthest-back,
  which setups troll); the §6 UNIVERSAL doctrine (rod-tip elevation rule ≈ 3 ft
  of tip costs 1 ft of depth; the 4-factor rod↔lure pairing framework) →
  `techniques/trolling.md`, attributed `cameron`.`** (Identical wording appears
  in the extraction-log spec.)
- **§7** rods → `profiles/cameron/rods.md`.
- **§8** hard baits → SPLIT: inventory → `profiles/cameron/tackle.md`; universal
  per-model knowledge (rigging, mechanics) enriches `lures/*.md`.
- **§9** trolling lures → SPLIT: inventory → `profiles/cameron/trolling-lures.md`;
  researched running-spec table → matching `lures/*.md` as spec backbone,
  attributed; profile links them.
- **§10** BightSST → `planning/day-plan-protocol.md` conditions-sources section
  (endpoints/role, cold-start caveat, goes_west quirk as doctrine: "distrust
  single-source SST extremes; cross-check models") + `conditions/
  upwelling-and-turnover.md`.
- **§1–4, §11** → conditions/, bait/, bird-reading, planning, CLAUDE.md sync
  rule per the log.

## [V3-3 / V3-4] Future ingestion pipeline (CLAUDE.md documents process ONLY — no execution now)

Additive; current build scope unchanged. CLAUDE.md will document:
(a) new batches land in `sources/transcripts/<channel>/` with manifest rows
appended; (b) **dedup pass** — byte-identical and same-video-different-ID logged
`duplicate-of`, near-dupe re-uploads flagged; (c) **triage pass** classifies
every video (tutorial | report | on-the-water | seminar | promo | out-of-region)
into the log BEFORE extraction — extraction depth follows type, skips logged with
reason; (d) extraction runs batch-by-batch, **amending** existing notes per the
merge/conflict conventions, incremental log per batch, link-maintenance before
each commit; (e) each batch ends with a coverage summary for Cameron — **same
GATE B review** as the main build. **[V3-4]** CLAUDE.md states a **~400-video
multi-channel batch** of mixed tutorials + on-the-water footage is the expected
first use of this pipeline.

## `scripts/link-maintenance.py` (before EVERY commit)

(a) validate links — exit nonzero on dead links; (b) regenerate backlinks
between markers; (c) regenerate dir README indexes between markers; (d) Mermaid
map between markers, **cap 30**, skipped past cap.

## Directory tree + decomposition (corpus-complete; counts synced 2026-08-12 per P5)

**conditions/** (12) — sea-state, moon, tide-and-slack, current-structure,
current-diagnostics, water-color, water-temperature, upwelling-and-turnover,
deep-scattering-layer, kelp-paddies, bird-reading (known merge, attributed),
**water-regimes (P5 — the four-regime planning layer, cameron house doctrine)**.

**seasonal/** (9, **regime-first** per P5) — february-march … november-december
(8 month notes, each headed by its regime; months are the typical-year mapping
of the four regimes in `conditions/water-regimes.md`) + year-anniversary-prior
(**a location prior WITHIN the fall-fragmentation regime**;
water-state-vs-calendar conflict kept).

**locations/** (7, universal, no coords) — zone-lexicon, island-structure,
bight-geography, bightsst-eval-targets, bays-and-harbors, bass-structure,
breakwalls-jetties-riprap.

**planning/** (4) — day-plan-protocol (4-step; step 2 references report-reading;
§10 conditions-sources section), search-and-glassing, electronics-and-sounder,
**[A2] report-reading-and-forecasting** (persistence-null; advection 10–15 nm
overnight for unassociated bluefin; water-miles report aging; post-moon &
late-season coverage bias; per-rod count normalization, no date = not current;
post-storm volatility).

**species/** (18 species + 1 decision note) — bluefin-tuna, yellowfin-tuna,
yellowtail (+ cameron water-state + BOLA), dorado, white-seabass,
california-halibut, calico-bass, sand-bass, spotted-bay-bass, rockfish-lingcod,
swordfish, barracuda, bonito, striped-marlin, skipjack-tuna,
pacific-crevalle-jack, **[A3] ocean-whitefish** (own note; logged),
california-spiny-lobster, **[A1] bluefin-trolling** (decision spin-out).
**[A8] white-croaker-kingfish DROPPED** (FL king mackerel; `skipped:
out-of-region`). All routers follow the template; re-mine the 17 dated reports.

**techniques/** (18, execution-only + "Reach for this when") — surface-iron,
yo-yo-iron, slow-pitch-jigging, knife-jigging, kite-fishing, speed-trolling,
foamer-casting, flyline, dropper-loop, sliding-sinker, chunking, **trolling**
(general + §6 universal doctrine [R2]), swimbaits, ned-rig, drop-shot,
rockfish-deep-dropping, **deep-drop-swordfishing** and **hoop-netting** (both
created during the build per the router-never-absorbs-execution rule; counts
synced per P5).

**lures/** (12, class-based; §9 specs are the backbone [A5]) — mad-mac,
spreader-bar, dtx-minnow, halco-laser-pro, rapala-husky-magnum, cedar-plug,
tuna-feathers-and-skirts, iron-jigs, knife-jigs, tuna-poppers-and-stickbaits,
soft-plastic-swimbaits, bay-bass-plastics.

**rigging/** (12) — wind-on-leader, fg-and-albright, essential-knots,
hollow-splice-and-serving, bite-leaders, flying-fish-harness, double-trouble-rig,
rubber-band-deep-rig, trap-rig, leadhead-mods, haywire-twist, tuna-feather-rig.

**tackle/** (5) — line-and-leader, rod-and-reel-selection, hooks, gear-classes
(class lexicon), reel-maintenance.

**bait/** (3) — making-bait, fishing-live-bait, bait-tanks.
**fish-care/** (3) — tuna-care, dorado-and-general, ikejime.

**profiles/cameron/** — **[R2] `boat.md`** takes §5 plus the §6 PLATFORM facts
(holder count/angles/geometry, no outriggers, 2–3 lures, shotgun = furthest-back,
which setups troll); the §6 UNIVERSAL doctrine (rod-tip elevation rule ≈ 3 ft of
tip costs 1 ft of depth; the 4-factor rod↔lure pairing framework) →
`techniques/trolling.md`, attributed `cameron`. Plus `rods.md` (§7), `tackle.md`
(§8 inventory), `trolling-lures.md` (§9 inventory), `spots.md` (coords),
`README.md`. **profiles/_template/** — same set blank + README.

**sources/** — `transcripts/` (128 raw + `_manifest.csv`), **[V3-1] manifest
gains `channel` + `upload_date` columns** (from each transcript header's
Channel / Upload date), **[V3-1] `source-registry.md`** (seeded: Erik
Landesfeind / SoCal Bight Fishing Academy, BD Outdoors named captains, cameron),
`memory-export.md`, `bd-transcript-knowledge-proposal.md`, **[A9]
`spot-lists.md`** (renamed), **[A7] `extraction-log.md` written INCREMENTALLY**
per commit (dead session resumes from CLAUDE.md + log), **`plan.md` (this
document — committed 2026-08-12)**. *Duplicate correction:* `vqsD0qpwcJA` and
`Jtf-bU4aM-c` are NOT identical — two distinct extractions, topic overlap
noted, not `duplicate-of`.

**skills/boat-day/README.md** — scaffold + build plan. **scripts/** —
`link-maintenance.py`, `build-skill-resources.py` (bundle from KB notes + named
profile default `profiles/cameron`; generic no-profile build works).

**Root** — `CLAUDE.md` (spec + GATE A/B + confidence-registry [V3-1] +
observation convention [V3-2] + ingestion pipeline [V3-3] + ~400-video note
[V3-4] + spin-out rule [A1/R1] + **router-stub rule (P4)** + Mermaid cap [A10] +
sync rule), `README.md`, `.gitignore`.

## Execution — one commit per step; link-maintenance + [A7] incremental log before each

*(Historical — all steps below are complete; see the punch-list section at top
for the follow-on work.)*

- **Step 0:** CLAUDE.md (GATE A verbatim), .gitignore, scaffold, unzip sources,
  rename spot file → `sources/spot-lists.md`, add manifest channel/upload_date
  columns + seed `source-registry.md` [V3-1], `link-maintenance.py`, seed
  `extraction-log.md`. Commit.
- **Step 1:** memory-export + proposal FIRST → profiles/cameron/*, conditions/*,
  seasonal/*, locations/*, planning/* (incl. report-reading-and-forecasting),
  species/swordfish.md, bird-reading.md. Update log. Commit.
- **Step 2:** species/ (routers + species/bluefin-trolling.md; re-mine 17
  reports). Update log. Commit.
- **Step 3:** techniques/. Update log. Commit.
- **Step 4:** lures/ + rigging/ (§8/§9 specs land [A5]). Update log. Commit.
- **Step 5:** tackle/. Update log. Commit.
- **Step 6:** bait/ + fish-care/. Update log. Commit.
- **Step 7:** skills/ + build-skill-resources.py + profiles/_template. Update
  log. Commit.
- **Finish:** VERIFY log completeness (not create it [A7]); coverage summary +
  judgment-calls list; species-note acceptance test. Push branch. **Stop at
  GATE B** — Cameron reviews, then merges to main.

## Thin areas & judgment calls (seeded; completed at finish)

- **[A3]** mako, thresher: **absent from both inputs** — thin area, not skipped.
- **[A8]** kingfish (FL king mackerel) + East Florida report → out-of-region;
  clothing/bags/what-to-bring → skipped filler.
- **[A3]** ocean whitefish → own note (rationale logged).
- Slow-pitch duplicate pair → two distinct extractions (logged).

## Verification

- `link-maintenance.py` exits 0, idempotent, cap 30 honored.
- `build-skill-resources.py` works with and without `--profile`.
- **[A5/A7]** Log: every §1–11 section and all 128 video_ids appear with **≥1
  destination, every destination logged**, nothing dropped; filler/out-of-region
  carry `skipped: <reason>`; log complete incrementally, verified at finish.
- **[V3-1]** manifest has channel+upload_date; `source-registry.md` seeded; a
  spot-check note's `confidence` matches the registry rule.
- **[V3-2]** an on-the-water datum appears as `**Observed** (…)` beside, not
  inside, doctrine.
- Specifics verbatim (Fathom 80 = 7'4" XXXX-H, ~1000 yd 100 lb braid; slurry
  ~2 cups salt/7–10 lb; SD Bay swell 160–186°).
- Root README renders; fresh session navigates from indexes alone.
- Species-note acceptance test per note; failures logged.
- **GATE A** respected (no execution pre-`PLAN APPROVED`); **GATE B** respected
  (no merge pre-review).


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
