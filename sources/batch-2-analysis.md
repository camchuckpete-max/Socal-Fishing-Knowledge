# Five-Channel Transcript Batch — Analysis & Ingestion Process

## Context

Cameron uploaded five zips of new YouTube transcripts (the "~400-video
multi-channel batch" anticipated by CLAUDE.md's *Future ingestion pipeline*
section). **This session is analysis-only — no writes to GitHub under any
circumstances.** The deliverable is (a) an evaluation of the new corpus and
(b) a concrete, session-by-session process for a *future* session to integrate
it. Execution of that process remains behind GATE A (`PLAN APPROVED`) and
GATE B (Cameron's post-build coverage review) as usual.

## 1. Batch inventory (measured, not estimated)

294 transcript `.md` files, ~559k words / ~64 hours of video (~2× the existing
128-video BD Outdoors corpus by word count), same generator/format as the
existing corpus (metadata header + timestamped transcript). **Zero overlap with
the 128 existing video_ids.**

| Zip / folder | Channel (per headers) | Files | Manifest rows | Failed rows | Words | Hours | Years |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Stoked-On-Fishing-Inshore | StokedOnFishing | 120 | 133 | 13 | 270k | 38.1 (median 22 min) | 2012–2026 |
| Yoursaltwaterguide-tutorials | Your Saltwater Guide | 109 | 114 | 5 | 115k | 10.3 (median 5 min) | 2018–2022 |
| Stoked-On-Fishing | StokedOnFishing | 30 | 31 | 1 | 51k | 5.5 (median 6 min) | 2012–2026 |
| Dirty-Hookers (DHTackleTalks zip) | Dirty Hookers | 22 | 23 | 1 | 70k | 5.3 (median 14 min) | 2018–2025 |
| Roman-Castro-Saltwater-Tips | Roman Castro | 13 | 13 | 0 | 53k | 5.1 (median 22 min) | 2017–2021 |

Failure reasons across the 20 failed rows: private videos (sign-in required)
and no-English-captions. These have **no transcript file** — they are logged
rows only.

## 2. Data-quality findings (must be handled at landing)

1. **Manifest schema drift.** The five new `_manifest.csv` files have only
   `video_id,title,status,caption_type,failure_reason` — missing the repo
   manifest's `channel,upload_date` columns. Yoursaltwaterguide's manifest
   deviates further: `video_id,title,status,caption_type,reason,file`.
   Channel + upload date ARE present in each transcript's header, so the
   landing step can normalize mechanically.
2. **True duplicates across the two Stoked zips.** Both zips are the same
   YouTube channel ("StokedOnFishing") split by playlist. 6 video_ids appear
   in both: `6-mi3Qxn37c, H-vIGWPIPVc, Y2bXn44lfqo, 82gEHYel-4U, ldVj0BoB-kE,
   FE63WNlwkKw`. The copies are **separate caption fetches, not identical**
   (`FE63WNlwkKw`'s Inshore copy is missing opening narration lines) → compare
   each pair, keep the more complete fetch, log `duplicate-of`.
3. **Foreign-channel strays inside zips**: one "JoeWo" file in Roman-Castro,
   one "Kevin Is Cooking" in Stoked-Inshore, one "Okuma Fishing Tackle USA" in
   Yoursaltwaterguide. Attribution must follow the *actual* channel, and the
   promo/cooking ones triage accordingly.
4. **None of the five channels are in `sources/source-registry.md`** → per the
   confidence rubric, content from this batch caps at **medium** (and
   sponsored claims at low) except where a promoted voice speaks. **Resolved:
   Cameron decided (2026-08-12) to promote Hansen, Florentino, Capt. Scotty,
   and Cesar-with-caveat — see Phase 4.**

## 3. Content characterization

### Dirty Hookers (22 files, 70k words) — highest doctrine density in the batch
- Mix: seminars at Eric's Tackle Shop, tackle breakdowns, tutorials; ~77% clear
  the curation bar, 11 warrant deep extraction. Mean 8.1 spec-numbers/1k words.
- Voices: **Ray Sharifi** (host; deckhand aboard the *Highliner* from 2023;
  self-declared non-expert; heavy sponsor integration — Opsin discount code) and
  **Cesar** (rod-company rep, 25+ yrs Sea of Cortez cabrilla; the strongest
  registry-promotion candidate, but model picks skew low as a rep). Also Capt.
  Jason (*Pride* → *Highliner*), Capt. Scotty appears via Roman's channel.
- **Major NEW topics with zero KB coverage:** cabrilla (full router-grade
  content), Sea of Cortez / Bay of LA panga-trip fishery (grouper/pargo leader
  systems, trip envelope), speed-jigging as distinct from slow-pitch (balance-
  point test, "blanking" retrieve), assist-hook building, jerkbaits,
  Seaguar knot (mono→fluoro).
- Amends many existing notes: flyline (long-mono depth math), knife-jigging,
  yo-yo, surface iron, bite-leaders, hooks, line-and-leader, knife-jigs, etc.
- **Doctrine conflicts found** (keep side by side): assist-hook count/placement
  (existing "single bottom pair, no top hook" vs Cesar's top+bottom and 3-hook
  jig), jigging strike drag 19–20 lb vs "35 lb online advice", swing-on-the-bite
  (vertical jig) vs wind-through (surface iron), flyline braid+short-fluoro vs
  long mono top shot.
- Skips: 1 promo (sponsor announcement), 1 apparel haul (marginal), 1 private
  (manifest-only).

### Roman Castro (13 files, 53k words) — procedural value, low parameter density
- ~6/13 clear the bar. Deep: 50-min spotted-bay-bass walkthrough (zone→spot→
  cast-fan search method; re-cast-the-same-line rule), rockfishing with Capt.
  Scotty (Brothers Sportfishing — registry candidate; weak-link dropper-loop
  doctrine), hoop-net full setup, surface iron with Scotty, 25-tips spotty video.
- **Explicitly unsponsored** ("I pay regular price") — raises gear-claim trust.
- Skips: the **JoeWo Call of Duty video** (ingestion contamination), channel
  recap, two near-silent catch videos, generic hacks, kayak-rental logistics.

### Cross-channel extraction hazards (from sampling)
- **ASR corruption is severe and systematic**: names and lure brands mangled
  (cabrilla→"Cambria", Tady→"teddy", Yo-Zuri→"yui", Ray Sharifi→"Rach Rapier").
  No diarization — multi-speaker files risk misattribution (the highest-value
  seminar never names its presenter on mic; attribution is inferential).
- **Relative-time landmines** throughout ("three years ago…"); must resolve to
  absolute years at extraction per CLAUDE.md.
- **Re-cut footage across distinct videos** (two 2025 DH videos share blocks
  near-verbatim) — repetition must NOT count as independent confirmation.
- **Version drift within a channel** (2018 vs 2023 "Yellowtail Arsenal") —
  prefer latest, date every parameter.
- **Region labeling**: Sea of Cortez / Guadalupe / Cedros content is in scope
  (Baja) but must carry region labels; SoC 3-hook jig rigs collide with the
  KB's "two hooks max in US waters" claim — flag, don't reconcile.

### StokedOnFishing (150 files → 144 unique, 321k words, ~44 h) — adventure TV
- **The inverse of the BD corpus**: ~62% full 22–25 min TV episodes
  (travel/adventure footage), ~14% promo/sizzle, only 16 tutorials, ~9 report
  shorts, 4 cooking, 1 seminar/interview cluster. Host: **Shay McKinty**;
  recurring voices: Capt. Andrew, Jose (Cedros Outdoor Adventures), and
  **Capt. Benny Florentino** (one episode — he's already a named voice in the
  BD corpus, making him the cleanest registry candidate).
- **Region census:** ~40 Baja (Cedros/San Benito/La Bocana/Mag Bay/Gonzaga/
  La Paz/East Cape — in scope), ~38 SoCal, ~15 region-neutral procedure,
  **~27 out-of-region saltwater (Alaska/Panama/Costa Rica/PR/Tonga/Florida/
  Amazon) + 7 freshwater + 1 non-fishing = ~35 hard skips (24%) on region
  alone.**
- **Extraction-value verdict:** ~12–15 full extracts (~10%) — the yo-yo
  deep-dive (`ntQXxcH5sjI`), the captain-narrated bluefin trolling episode
  with Mad-Mac-vs-spreader-bar-vs-kite selection logic (`xzIaUEDklrE`), the
  103-min "Pacific Giants" film, calicos with Aaron Martens, the **2023
  Cedros catch-and-release regulation change** (`ldVj0BoB-kE` — hard
  regulatory + spawning-timing fact), kelp-paddy pattern episode, knot set at
  parameters-only depth. **~55–60 episodes are observations-only** (dated
  `**Observed**` lines under existing doctrine). ~70 skip.
  **This channel is primarily an *observation* source** — triage it that way
  up front rather than mining episode by episode.
- Sponsorship saturation measured: 79/150 files carry sponsor blocks, 39
  self-promos, 2014+ episodes embed a ~90 s verbatim brand film; the first
  ~90 s of every post-2014 episode is boilerplate (skip programmatically).
- **Playlist/dir names are meaningless for triage** ("Inshore" holds the
  offshore bluefin + all the Alaska/Panama/Tonga travel + the cooking file).
- Multi-part series are pervasive (≥17 series) — treat each series as ONE
  trip for observation purposes, not N independent sightings; some titles
  collide across different years/trips; some working titles were never
  cleaned ("TMP ---------OliveCrest 25", "Basstravaganza.mov").
- The 6 cross-zip duplicate IDs are **separate caption fetches, not identical
  copies** — `FE63WNlwkKw`'s Inshore copy is missing opening narration.
  Canonical-copy selection must prefer the more complete fetch.
- 14 failed fetches; two in-scope losses worth flagging to Cameron
  (`Qurgc-HtsuA` yellowtail fillet local-style; `1CQGXwqmURA` life of a
  calico bass); one orphaned "part 3" whose parts 1–2 failed.
- 4 manual-caption files are far cleaner than the rest — read them first.
  ASR normalization mandatory (Cedros→"SED Ros", Salas→"Solace",
  Okuma→"Akuma", Tady→"Tatty"…) or keyword-driven extraction misses most
  gear references.

### Your Saltwater Guide (109 files, 115k words) — one voice: Capt. Dave Hansen
- Single host throughout: **Capt. Dave Hansen**, working SoCal sportboat/charter
  captain (also runs Cabo charters ~4 mo/yr; sells a $4.99/mo subscription site
  plugged in 14 files). ~62 tutorials, ~20 on-the-water, 9 promo, 3 Florida,
  ~9 generic/non-fishing, **0 dated reports**.
- **CRITICAL: Hansen is already in the KB.** Three of this batch's videos are
  the same recordings BD Outdoors published under different IDs, already
  extracted (`IMnoZVEYpm4`≈`m2q22sPPkEM` hooks 101 → `tackle/hooks.md`;
  `kr-DZP7OVmg`≈`4xzK7YaXK5s` offshore tips → `conditions/kelp-paddies.md`;
  `8Asmd2H56Qk`≈`sYrsPGXiYhI` rubber-band rig). Existing "high"-confidence hooks
  doctrine is *his*. The dissenting "7-days-before-AND-after" moon captain
  already quoted in `conditions/moon.md` is almost certainly Hansen
  (`fri_BWI-VA0` states exactly that doctrine). → registry/attribution question
  for Cameron.
- **11 intra-batch duplicate pairs (~20% of files)** — the 2022 upload wave is
  largely re-uploads of 2018–2021 videos under new titles (one byte-identical,
  most ≥0.83 trigram overlap, identical durations). Dedup MUST precede triage
  or doctrine gets double-attributed.
- **Title-vs-content mismatch is systematic** ("5 Secrets to Bluefin" = mostly
  subscription pitch; "Proper Way to Fish a Kelp Patty" = 95% catch footage).
  Title-only triage does not work for this channel — needs content skim.
- Parameter density: mean 2.12/1k words, median 0.88 — about **¼ the density of
  the BD corpus** (mean 4.90/median 3.68). Hansen teaches rules-of-thumb and
  mechanics, not numbers.
- Attrition estimate: **~32 videos (~30%) clear the bar**; yield ≈ 3–6 new notes
  (california-sheephead, anchoring-on-structure — strongest new-note candidate,
  sculpin/venomous handling; optionally filleting, drag-setting procedure),
  ~25–30 amended notes, ~8–12 Observed blocks, ~75 skip rows.
- High-value merges: yo-yo iron cadence, dropper-loop procedure, San Diego jam
  (7 wraps, no-swivel doctrine), WSB sliding-sinker weight ladder + forward-
  facing-mouth rule, bank-naming lexicon (`Rf1HKJG-SDg` — fills a real
  `locations/zone-lexicon` gap), sounder bottom-hardness reading, cross-cutting
  "hand in front of the reel / finger on spool while sinking" doctrine.
- Region traps: "SoCal style" surface-iron video actually filmed in Cabo;
  hooks video mixes SoCal + Cabo sizing in consecutive sentences → needs the
  region-separation treatment. 3 Florida videos = out-of-region skips.
- Manifest quirk: one failed row is Polish-captions-only. One implausible claim
  flagged (Tady 45 "under an ounce" — do not carry).

### Expected yield across the batch (synthesis)
- **New notes: ~10–14.** Confident: `species/cabrilla.md`,
  `species/grouper-and-pargo.md`, `locations/sea-of-cortez.md`,
  `locations/cedros-island.md` (incl. the 2023 catch-and-release change),
  `techniques/speed-jigging.md`, `rigging/assist-hooks.md`,
  `lures/jerkbaits.md`, anchoring-on-structure, `species/california-sheephead.md`.
  Borderline: sculpin/venomous handling, filleting, drag-setting procedure,
  Roman's inshore search method (vs a section in `search-and-glassing.md`).
- **Amended notes: ~40–60** across every branch — the bulk of the value.
- **Observed blocks: ~70–90** dated observations (Stoked mined at full
  depth per Cameron's decision; one-per-trip for multi-part series).
- **Skip rows: ~150** with logged reasons (region, promo, non-fishing,
  duplicates, failed fetches).
- **Deep-read set after dedup/triage: ~70–75 videos** (DH 17, Roman 6,
  YSG ~32, Stoked ~15) **plus all ~55–60 in-scope Stoked episodes mined for
  observations** (decided 2026-08-12).
- Thin areas (mako, thresher) are NOT closed by this batch.

## 4. Proposed ingestion process (for the future incorporation session(s))

Instantiates CLAUDE.md's Land → Dedup → Triage → Extract → Coverage pipeline.
All work on a feature branch; nothing merges to `main` until GATE B. Every
phase ends with an `extraction-log.md` update + `link-maintenance.py` pass +
commit, so a dead session resumes from CLAUDE.md + the log alone.

**Logistics prerequisite:** this container is ephemeral and nothing was pushed.
The execution session needs the same five zips re-uploaded (or fetched) before
Phase 0.

### Phase 0 — Land (1 commit)
- Extract zips into `sources/transcripts/<channel>/`: `dirty-hookers/`,
  `roman-castro/`, `your-saltwater-guide/`, `stoked-on-fishing/` (both Stoked
  zips merge into one folder — same channel). The 6 cross-zip duplicate IDs
  are **different caption fetches** with identical filenames: before merging,
  compare each pair and keep the more complete copy (verified: `FE63WNlwkKw`'s
  Inshore copy is missing the opening narration lines).
- Leave the existing 128 BD transcripts flat where they are (no churn; the
  manifest's `channel` column already distinguishes them).
- Normalize manifests into the master `sources/transcripts/_manifest.csv`
  (7-column schema): append rows, populating `channel` + `upload_date` from
  each transcript's header (per-file, not per-zip — catches the JoeWo /
  Kevin Is Cooking / Okuma strays); map Yoursaltwaterguide's `reason`→
  `failure_reason`, drop its `file` column. Keep all 20 failed rows —
  they're accountability rows (`skipped: no transcript (<reason>)` later).
- Log "batch 2 landed" in `extraction-log.md` with per-channel counts.

### Phase 1 — Dedup (1 commit; MUST precede triage)
- **Within-batch:** log the 6 Stoked cross-zip IDs as `duplicate-of` (single
  copy landed). Mark the 11 YSG re-upload pairs: keep the earlier/longer
  original as primary, log the re-upload `duplicate-of: <primary>`; extract
  from primaries only.
- **Cross-corpus:** log the 3 YSG↔BD same-recording pairs
  (`IMnoZVEYpm4`↔`m2q22sPPkEM`, `kr-DZP7OVmg`↔`4xzK7YaXK5s`,
  `8Asmd2H56Qk`↔`sYrsPGXiYhI`) as `duplicate-of: <bd-id>`; the YSG hooks cut
  is longer — extract only tail content beyond the BD version.
- Sweep the remaining ~280 IDs vs the repo's 128 for near-dup re-uploads
  (title+duration+trigram), since exact-ID overlap is already verified zero.
- **Rule (feeds confidence rubric):** re-cut/duplicated footage never counts
  as independent confirmation of doctrine.

### Phase 2 — Triage (1 commit; every video classified BEFORE extraction)
- Classify all non-duplicate videos:
  `tutorial | report | on-the-water | seminar | promo | out-of-region |
  non-fishing`, each with a planned depth:
  `deep | parameter-skim | observations-only | single-pull | skip:<reason>`.
- **Title-only triage is prohibited for this batch** — YSG titles mislead
  systematically and Stoked episode titles say nothing about doctrine content.
  Triage = header metadata + opening-skim + keyword scan (subagent per
  channel).
- Commit the triage table to `extraction-log.md`. It becomes the extraction
  worklist.

### Phase 3 — Extract (channel-by-channel, 1+ commit per channel)
Order by doctrine density — sharpen merge conventions on the dense corpora
before the big low-density one:
1. **Dirty Hookers** (~20 post-triage) — new notes: `species/cabrilla.md`,
   `species/grouper-and-pargo.md`, `locations/sea-of-cortez.md`,
   `techniques/speed-jigging.md`, `rigging/assist-hooks.md`,
   `lures/jerkbaits.md`; heavy amends to flyline, knife-jigging, yo-yo,
   surface-iron, bite-leaders, hooks, line-and-leader.

   **Baja conventions (DECIDED 2026-08-12: additive, no partition):** Baja
   species notes live in `species/` with region front-matter tags
   (`[baja, sea-of-cortez]` etc.) and a region line up top; `locations/`
   destination notes (`sea-of-cortez.md`, `cedros-island.md` — the latter
   holds the 2023 catch-and-release change + trip envelope, fed mostly by
   Stoked) are the Baja entry points and hold seasonal windows + local regs;
   the `species/` README index groups a Baja subsection in its curated
   prose; `seasonal/` stays a SoCal-bight calendar. Acceptance test for Baja
   routers uses the trip-planning variant: a first-time SoC panga angler
   opening `species/cabrilla.md` learns where/when/how-to-find/technique-
   per-situation/gear class, one link deep. Thin Baja species (roosterfish,
   sierra, snapper) get rows in the destination note's species table, not
   their own notes. Cabo/East Cape/La Paz/Mag Bay content is captured as
   labeled observations under existing notes — no destination notes until a
   corpus supports them.
2. **Roman Castro** (~6 deep) — spotted-bay-bass search method (zone→spot→
   cast-fan; re-cast-the-same-line rule), weak-link dropper-loop doctrine,
   hoop-net setup; amends to surface-iron and rockfish notes.
3. **Your Saltwater Guide** (~32 clearing, ~95 post-dedup to account) — new:
   anchoring-on-structure (strongest candidate), california-sheephead,
   sculpin handling; wide shallow amends (2–5 bullets each) + bank-naming
   lexicon into `locations/zone-lexicon.md`.
4. **StokedOnFishing** (~144 unique) — DECIDED (Cameron 2026-08-12): **mine
   every in-scope episode.** Full-extract the ~12–15 doctrine carriers
   (yo-yo deep-dive, captain-narrated bluefin trolling, Pacific Giants film,
   Aaron Martens calicos, Cedros 2023 regulation change, kelp-paddy pattern
   episode, knot set at parameters-only); read ALL ~55–60 SoCal/Baja
   episodes for dated `**Observed**` lines (these feed seasonal priors and
   species routers); one multi-part series = one trip = one observation
   event; strip the post-2014 90-second boilerplate and sponsor reads before
   reading; hard-skip only the ~35 out-of-region/freshwater and ~20
   promo/sizzle files, with logged reasons.

Batch-specific extraction rules (generalized from sampling — add to the log's
conventions header so subagents inherit them):
- **ASR hazard rule:** never carry a garbled brand/name; verify against
  context or flag. Attribution in multi-speaker files only when contextually
  clear (no diarization); presenter-inferred attributions are recorded as
  inferred (e.g. the DH jigging seminar).
- **Region labels mandatory** for Baja/Cabo/Sea-of-Cortez/Guadalupe content
  (in scope, but labeled; Cabo footage hides inside "SoCal"-titled videos).
  Florida/freshwater/gaming = `skipped: out-of-region` / `not fishing`.
- **Relative time resolved to absolute years** at extraction (per CLAUDE.md),
  using upload date as the anchor.
- **Sponsored product claims = low**; mechanism/parameters surrounding a
  sponsored product = medium. DH's Opsin code videos and YSG's PTO/Promar/
  Okuma spots are the flagged cases.
- **Prefer the latest version** where a channel updated its own doctrine
  (2018 vs 2023 "Yellowtail Arsenal"), date every parameter, keep genuine
  conflicts side by side (assist-hook count, strike-drag numbers,
  swing-vs-wind-through, flyline mono-vs-braid — all found in sampling).

### Phase 4 — Registry pass (DECIDED by Cameron 2026-08-12: promote all strong candidates)
Registry rows drafted in Phase 0 (so extraction assigns confidence
correctly from the start), covered by PLAN APPROVED, re-reviewed at GATE B:
- **Capt. Dave Hansen** (`dave-hansen`) — Your Saltwater Guide channel + his
  BD Outdoors guest videos (`m2q22sPPkEM`, `4xzK7YaXK5s`, `sYrsPGXiYhI` are
  the same voice; row notes the cross-channel identity). Fixes the existing
  inconsistency (his hooks/moon doctrine is already `high` under BD IDs).
- **Capt. Benny Florentino** (`benny-florentino`) — already a named BD-corpus
  voice (`Rwy4MqeXCIU`), appears in Stoked (`AxLlx2Ug-rs`).
- **Capt. Scotty** (`capt-scotty-brothers`) — Brothers Sportfishing, La
  Jolla; via Roman Castro's channel.
- **Cesar** (`cesar-<surname-if-verifiable>`) — Sea of Cortez / cabrilla /
  jigging mechanism doctrine. **Row carries an explicit caveat: rod-company
  rep — mechanism/parameter doctrine qualifies for high when repeated;
  product/model endorsements remain low per the sponsored-claim rule.**
  Verify his full name from video descriptions before writing the row.
- NOT promoted now: Roman Castro, Shay McKinty, Ray Sharifi (their content
  stays at the medium cap; revisit at GATE B).
- If promoted, registry rows note cross-channel identity (Hansen = BD guest
  spots + YSG channel).

### Phase 5 — Coverage summary → GATE B
- Full accounting: all ~314 new manifest rows → destination(s) | `covered` |
  `skipped: <reason>` | `duplicate-of` — same standard as the 128-video finish
  reconciliation.
- Re-run the species-note acceptance test on every new/heavily-amended router.
- Check whether the batch closes the KB's recorded thin areas (mako,
  thresher — neither YSG nor Stoked does; the only shark content is Florida
  beach fishing, out of region — thin areas persist).
- Flag notable in-scope losses among failed fetches (`Qurgc-HtsuA` yellowtail
  fillet local-style, `1CQGXwqmURA` life of a calico bass,
  `JgknlyfTtgE`/`9O0AnMQkEM4`/`gaa3_aBFL5A` SD-bay + SWBA episodes) in case
  Cameron can source captions another way.
- Coverage summary + judgment-calls list for Cameron's GATE B review; he
  merges.

### Effort shape
- Session 1: Phases 0–2 (mechanical + triage; subagent per channel).
- Sessions 2–3: Phase 3 (DH+Roman together, then YSG, then Stoked; each
  channel is a resumable commit boundary), Phases 4–5 close.
- Post-dedup/triage the deep-read set is ~70–75 videos plus ~55
  observation-mining episodes — comparable in reading effort to the original
  128-video build, but with far lower average density and a much larger
  skip ledger.

## 5. Decisions (Cameron, 2026-08-12) & remaining open items

1. **Registry — DECIDED: promote all strong candidates** (Hansen, Florentino,
   Capt. Scotty, Cesar-with-caveat). See Phase 4.
2. **Stoked depth — DECIDED: mine every in-scope episode** (~55–60 episodes
   read for Observed blocks; only region/promo skips remain).
3. **Baja scope — DECIDED: additive, current structure.** Build only what the
   corpus supports at router grade (~4–6 Baja notes); no folder partition.
   Conventions in Phase 3. **Written-in trigger:** when a future Baja-heavy
   batch lands, graduate the README grouping to a real `baja/` partition —
   the region tags added now make that migration mechanical.
4. **Filleting/butchery notes** (YSG has 5, Stoked has 2 + a failed fetch):
   generic butchery is a stated curation-bar skip; species-specific SoCal
   handling arguably isn't. Default unless overridden: skip generic, capture
   species-specific handling inside existing `fish-care/` notes.
