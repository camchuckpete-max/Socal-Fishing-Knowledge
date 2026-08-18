# Extraction Log

Maps **every** `_manifest.csv` `video_id` and **every** `memory-export.md`
section to the note(s) it fed, or `skipped: <reason>`. Maintained
**incrementally** — updated at each build step's commit so a dead session
resumes from [CLAUDE.md](../CLAUDE.md) + this log alone. The finish step
**verifies** completeness (it does not build the log).

Accounting rule: every source and every export section appears with **at least
one** destination, and **every** destination is logged (sections fan out to
multiple notes). Not "exactly once."

## Corpus reconciliation

- Manifest rows + transcript files both reconcile to **128** (the kickoff said
  ~129). No missing transcripts.
- **CORRECTED 2026-08-17 (batch 3, Phase 0) — these ARE one recording.**
  `vqsD0qpwcJA` ("Slow Pitch Jigging // Yellowtail LA Bay Baja", 2022-04-06)
  and `Jtf-bU4aM-c` ("Does SLOW PITCH JIGGING work for YELLOWTAIL?!",
  2022-06-27) are the **same video re-uploaded under a new title**: identical
  duration (00:05:38), identical opening caption line ("first baja slow pitch
  yellowtail so much fun so much fun dude"), body trigram similarity **0.989**.
  The original batch-1 note ("distinct videos — different md5, titles, dates,
  bodies") was wrong: the md5s differ only because the *headers* differ
  (video_id, title, URL). Batch 2's dedup sweep found the collision
  independently (sim 1.000 on caption text, both 338 s) and flagged it for
  Gate B — see [Batch-1 internal duplicate](#batch-2-dedup--2026-08-13-precedes-triage-findings-only-files-kept)
  below. Per the re-cut rule they count as **ONE source**: `Jtf-bU4aM-c` is
  `duplicate-of vqsD0qpwcJA` (the earlier upload is primary). Any doctrine
  treated as independently confirmed by both is demoted to a single mention;
  the front-matter cleanup is logged in the Phase 1 close-out below.

## Known dispositions (seeded step 0; confirmed as steps run)

| video_id | title | disposition |
| --- | --- | --- |
| j2NhAD2An4s | How to Catch Kingfish | `skipped: out-of-region` (FL king mackerel, Port Canaveral) |
| gBAu56Uw8Fk | East Florida Fishing Report | `skipped: out-of-region` (East Florida) |

**Thin areas (absent from both inputs — recorded, not skipped):** mako shark,
thresher shark.

## Transcript video_id → notes

_Filled incrementally per step. Format: `video_id — note(s) | skipped: reason`._

<!-- log:transcripts:start -->
**Step 1 (conditions / seasonal / locations / planning / swordfish) — consumed:**

| video_id | note(s) fed |
| --- | --- |
| zKmZ4zql2ws | conditions/sea-state |
| DnSqw4r7A1s | conditions/sea-state, tide-and-slack, kelp-paddies; planning/search-and-glassing; seasonal/june-july |
| S2L3KLSQ6Is | conditions/sea-state; seasonal/may |
| OYOda6T3f-8 | conditions/sea-state, water-temperature, bird-reading; seasonal/october, november-december |
| Z3rZqy2Pi8E | conditions/sea-state; seasonal/november-december |
| HzE4FHHcvTk | conditions/sea-state, tide-and-slack, kelp-paddies, bird-reading; seasonal/august; locations/bight-geography; planning/report-reading-and-forecasting |
| XLVUhV8DW64 | conditions/moon, water-temperature; seasonal/october, year-anniversary-prior; planning/report-reading-and-forecasting |
| -JZpyWLdKlk | conditions/moon, kelp-paddies; seasonal/june-july; species/white-seabass |
| HnqiE05vdXs | conditions/moon, current-diagnostics, current-structure; seasonal/august; locations/island-structure; techniques/yo-yo-iron |
| 5D1vx29LVpI | conditions/moon; seasonal/november-december |
| LEiyB9QNzHY | conditions/moon |
| 6TBxHnkYXI0 | conditions/tide-and-slack, current-diagnostics, water-color; locations/island-structure; planning/search-and-glassing |
| 5to3Q5P7w90 | conditions/tide-and-slack, water-temperature; seasonal/september, october |
| h3PTupup17I | conditions/water-color, current-structure, upwelling-and-turnover |
| Blh2BA-7Ono | conditions/bird-reading; seasonal/june-july; locations/zone-lexicon; planning/report-reading-and-forecasting |
| yMiBtZ7k8-w | conditions/deep-scattering-layer; planning/electronics-and-sounder; species/swordfish |
| KuVwmfF6RAo | species/swordfish |
| nRFFM8DT-og | conditions/deep-scattering-layer |
| yLpDI8jnizU | conditions/deep-scattering-layer, bird-reading; planning/electronics-and-sounder |
| 0KQ--N5TjqE | conditions/current-structure; locations/island-structure, bass-structure |
| Kf5wk_TFgTc | seasonal/february-march |
| pcwcRdmWmLc | seasonal/february-march; techniques/surface-iron (P2 size/weight doctrine — added at GATE B punch list) |
| CMQkHQMxbXM | seasonal/august |
| 5p6gu14ZC4w | planning/report-reading-and-forecasting; species/yellowtail (P1 SBI/Catalina fall entries — added at GATE B punch list) |
| YZtX1MiT0y8 | seasonal/april; species/yellowtail; techniques/surface-iron (P1/P2 squid-zone + lone color datum — added at GATE B punch list) |
| YgqXf9iICyg | locations/bays-and-harbors |
| kwMIgkCtFUE | locations/bass-structure |
| bydQzE3F9yM | locations/breakwalls-jetties-riprap (incl. birds-at-structure; bird doctrine stays linked, not duplicated) |
| jTXIr9O6zYk | locations/breakwalls-jetties-riprap |
| E4vKwRaRueA | planning/search-and-glassing (glassing); (dorado species pending step 2) |
| 4xzK7YaXK5s | conditions/kelp-paddies (paddy freshness / night restock); bait/bait-tanks (round-vs-square doctrine) |
| 11npFUPOJKU | planning/electronics-and-sounder |

**Step 2 (species routers) — consumed (species videos; dated reports re-mined
for species behavior, adding species destinations to the step-1 report rows):**

| video_id | note(s) fed |
| --- | --- |
| HWx1jDTGsng | species/bluefin-tuna |
| HtuLTv1NlL0 | species/bluefin-tuna |
| EyB98RuKfeQ | species/bluefin-tuna |
| z1CmWHqe9uk | species/bluefin-trolling |
| YsiHziY_PWw | species/bluefin-trolling |
| VgpgJ8IAyJo | species/yellowfin-tuna, dorado, striped-marlin (Mad Scad mentions; promo-flagged; bluefin-trolling removed — no content traces to it) |
| 8M4QhL-Qb7E | species/yellowfin-tuna |
| lxFNVdDhMy4 | species/yellowfin-tuna, skipjack-tuna |
| sYrsPGXiYhI | species/bluefin-tuna (concept; full rig → rigging/rubber-band-deep-rig, step 4) |
| D5DR7Kx42_A | species/yellowtail |
| Jtf-bU4aM-c | species/yellowtail |
| vqsD0qpwcJA | species/yellowtail |
| E4vKwRaRueA | species/dorado (also planning/search-and-glassing, step 1) |
| YIABTTYXeqc | species/calico-bass |
| n6PTy8g3pb0 | species/calico-bass |
| Rwy4MqeXCIU | species/calico-bass |
| P2OzCf2CwXI | species/sand-bass |
| 9br4Z4sfcNI | species/sand-bass (double swimbait rig; also techniques/swimbaits, step 3) |
| GVP3IChsmRQ | species/spotted-bay-bass |
| um5MAeCjNDg | species/spotted-bay-bass (also techniques/ned-rig, step 3) |
| lm7D9Tlc7Po | species/barracuda (also rigging/haywire-twist, step 4) |
| O5aQkex0qGg | species/rockfish-lingcod, ocean-whitefish |
| 6-8KfjEg0x8 | species/rockfish-lingcod, ocean-whitefish |
| AqW_Z9pFcHU | species/rockfish-lingcod |
| OpcKQPA3vAI | species/california-halibut, white-seabass |
| a5u8BaYzw8c | species/california-halibut |
| Xr4nURK-Z48 | species/white-seabass (also rigging/leadhead-mods, step 4) |
| b19_AJjYCok | species/california-spiny-lobster; techniques/hoop-netting |

Dated reports (YZtX1MiT0y8, S2L3KLSQ6Is, DnSqw4r7A1s, Blh2BA-7Ono, CMQkHQMxbXM,
-JZpyWLdKlk, HzE4FHHcvTk, HnqiE05vdXs, 5to3Q5P7w90, XLVUhV8DW64, OYOda6T3f-8,
Z3rZqy2Pi8E, 5D1vx29LVpI) were re-mined for species behavior — destinations
added to bluefin-tuna, yellowfin-tuna, yellowtail, calico-bass, sand-bass,
white-seabass, barracuda, bonito, striped-marlin as applicable.

**New technique note this step:** `techniques/deep-drop-swordfishing.md` and
`techniques/hoop-netting.md` (created per rule C2 — router never absorbs
execution).

**Step 3 (techniques) — consumed:**

| video_id | technique note(s) |
| --- | --- |
| HTssdpnUGMo | surface-iron |
| PRNMGpLj7Pw, dLj0sW_l-_A, OHxbPovgvgc | slow-pitch-jigging |
| j37zxs33gws | knife-jigging (also nRFFM8DT-og, reused) |
| YsiHziY_PWw | kite-fishing |
| z1CmWHqe9uk | speed-trolling |
| HtuLTv1NlL0 | foamer-casting (+ HzE4FHHcvTk, HnqiE05vdXs reused, cameron) |
| T3p1mrqNjIo, mscHk0qiXnk, raUPkuaFXpw, SluBXkT3cuw, 8YvmROeVL-0 | flyline |
| mUrihh0V59M | dropper-loop |
| apyGy3XKlss | sliding-sinker |
| E4vKwRaRueA | chunking (dorado-on-paddy application; chunking mechanics from proposal §4.5/§6.7 — medium confidence, flagged) |
| — (cameron §6 + HzE4FHHcvTk) | trolling (rod-tip elevation rule + 4-factor framework, attributed cameron) |
| YIABTTYXeqc, n6PTy8g3pb0, 9br4Z4sfcNI | swimbaits |
| um5MAeCjNDg | ned-rig |
| k4mD2d6C81k, 1enjjFVcDG0 | drop-shot |
| O5aQkex0qGg, 11npFUPOJKU, 6-8KfjEg0x8, AqW_Z9pFcHU | rockfish-deep-dropping |

**Step 4 (lures + rigging) — consumed:**

| video_id | note(s) |
| --- | --- |
| VgpgJ8IAyJo | lures/tuna-poppers-and-stickbaits (Riptide 105 / Mad Scad, promo-flagged); species/dorado (promo-flagged) |
| AJMjWDKsdRg, j1YZ_9IMUVY | lures/tuna-poppers-and-stickbaits |
| _KE9InIHx8M, zkSKgP2bq10 | rigging/wind-on-leader |
| CIMTyepgonk, NXtvXkqpT9w | rigging/fg-and-albright |
| SwXh9Cwi4e0, hF4dFlSB12s | rigging/essential-knots (Palomar, San Diego jam, RP, uni-to-uni) |
| _w8KNSgGPVE, yr6z3DmWY4s | rigging/hollow-splice-and-serving |
| kO_BqzUYayc | rigging/bite-leaders |
| GqcVaTIlyg0 | rigging/flying-fish-harness |
| UrEymGvZx00 | rigging/double-trouble-rig |
| sYrsPGXiYhI | rigging/rubber-band-deep-rig (concept; captions garbled) |
| qIKGJSEE2aY | rigging/trap-rig |
| RXb0HvVwqO4, Xr4nURK-Z48, F-vOTerdulU | rigging/leadhead-mods |
| lm7D9Tlc7Po | rigging/haywire-twist |
| CWVPLM6NheY | rigging/tuna-feather-rig; lures/tuna-feathers-and-skirts |

Lure class notes (iron-jigs, knife-jigs, soft-plastic-swimbaits, bay-bass-plastics)
draw specs from cameron §8/§9 + technique-note sources already logged (XLVUhV8DW64,
HnqiE05vdXs, OHxbPovgvgc, YIABTTYXeqc, n6PTy8g3pb0, um5MAeCjNDg, k4mD2d6C81k).

**Step 5 (tackle) — consumed:**

| video_id | note(s) |
| --- | --- |
| aXF0bxAFtU0, GoVI7CtN6L8, evhJMzJ7Dz0, YrvQZojc1q0, 0EpILTF0yvE | tackle/line-and-leader (sponsored superiority claims kept low-confidence) |
| xPFm_ZV2PZU | tackle/rod-and-reel-selection, gear-classes, line-and-leader |
| ONH1K2MOp7Q, 8tTVMOV2arE, gOAOyMNG3Ug, qSgIwLX2FWw | tackle/rod-and-reel-selection |
| sWRSYCmt4Tw, HIXTFWlwnM0, m2q22sPPkEM | tackle/hooks |
| EyB98RuKfeQ | tackle/line-and-leader, hooks (also species/bluefin-tuna, step 2) |
| 5yfA5XAaLLY | tackle/reel-maintenance |
| dMJJbowNb40 | topic covered by rigging/essential-knots (uni-to-uni knot demo); Gold Label preference covered from stronger sources |

**Step 6 (bait + fish-care) — consumed:**

| video_id | note(s) |
| --- | --- |
| 1QWstxUibDA | bait/bait-tanks (East vs West tank design) |
| T3p1mrqNjIo, mscHk0qiXnk, raUPkuaFXpw, SluBXkT3cuw, 8YvmROeVL-0 | bait/fishing-live-bait (live-bait tip videos; also techniques/flyline, step 3) |
| lxFNVdDhMy4 | bait/fishing-live-bait (also species/yellowfin-tuna, skipjack-tuna, step 2) |
| JeexIvtUkZc, w6DDCSLu8vM | fish-care/tuna-care (gill-gut + gaffing) |
| WzT0RSHpaQc | fish-care/ikejime |
| E4vKwRaRueA | fish-care/dorado-and-general (also step 1 search-and-glassing, step 3 chunking) |

Content notes are complete after step 6. **Remaining unmapped video_ids** (weekly
sportboat roundups, gear roundups, and pure filler) are reconciled at the finish
step (mostly `skipped: thin sportboat roundup — superseded by the dated Bight
reports` or `skipped: generic filler / out-of-region`).
<!-- log:transcripts:end -->

## memory-export.md section → destinations

_Sections fan out; every destination logged._

<!-- log:memory:start -->
Sections fan out; every destination logged. `(→ step N)` marks a destination
that lands in a later step.

| § | destinations (step 1 landed unless marked) |
| --- | --- |
| §1 Angler profile & programs | profiles/cameron/README, boat, rods, spots (context); seeds species interests — species/swordfish (open item), yellowtail BOLA (→ step 2), species/pacific-crevalle-jack (toro open item), techniques/yo-yo-iron (BOLA yo-yo program) |
| §2 Personal doctrine & observations | conditions/tide-and-slack (slack/bait-rise), water-color (chlorophyll≥SST doctrine), sea-state (SD Bay swell 160–186°), upwelling-and-turnover (turnover model); profiles/cameron/boat (Garmin 840xs, data capture). **Deferred:** fleet-intelligence practices (AIS sportboat tracking, Everingham bait boats, VHF ch72) — see thin-areas below |
| §3 Bird-reading model | conditions/bird-reading (merged, attributed) |
| §4 Bait operation | profiles/cameron/boat (30-gal tank); bait/making-bait, bait-tanks (→ step 6); sabiki setup (→ step 6) |
| §5 Boat platform | profiles/cameron/boat |
| §6 Trolling platform | profiles/cameron/boat (platform facts); techniques/trolling (universal doctrine: rod-tip elevation rule, 4-factor framework — → step 3) |
| §7 Rods (8 setups) | profiles/cameron/rods |
| §8 Hard baits / casting / jigging | profiles/cameron/tackle; lures/iron-jigs, tuna-poppers-and-stickbaits, etc. (→ step 4) |
| §9 Trolling lures + specs | profiles/cameron/trolling-lures; lures/mad-mac, dtx-minnow, halco-laser-pro, rapala-husky-magnum, cedar-plug, tuna-feathers-and-skirts, spreader-bar (spec backbone — → step 4) |
| §10 BightSST platform | planning/day-plan-protocol (conditions-sources section); conditions/upwelling-and-turnover; locations/bightsst-eval-targets |
| §11 Sync & canonical | CLAUDE.md (sync rule, gates, provenance) |

**Deferred/thin (flag):** §2 fleet-intelligence practices are not yet in a
dedicated note — candidate destination planning/search-and-glassing or a future
`planning/fleet-intelligence.md`. Logged so it is not silently dropped.
<!-- log:memory:end -->

## Build decisions logged

- Spot input retained, renamed `sources/spot-lists-PRIVATE-ONLY.md` →
  `sources/spot-lists.md` (repo public; Cameron waived privacy 2026-08-12).
- Manifest augmented with `channel` + `upload_date` columns (from transcript
  headers) per amendment V3-1.
- `sources/source-registry.md` seeded per amendment V3-1.
- Ocean whitefish → its own note `species/ocean-whitefish.md` (tilefish
  relative, not a rockfish); rationale per amendment V3/A3.

### Review corrections (swordfish, C1–C4) — generalized to all species notes

- **C1 Region separation:** `species/swordfish.md` parameters labeled SoCal;
  East-coast/Gulf Stream detail moved to a labeled "East-coast contrast" block in
  the technique note. General rule added to CLAUDE.md.
- **C2 Router never absorbs execution:** created
  `techniques/deep-drop-swordfishing.md` and moved sword execution (deployment
  sequence/timing, drift-setup up-current, bite handling incl. don't-touch-the-rod
  with attribution, lead/leader rigging) there; `species/swordfish.md` keeps
  routing. General rule added to CLAUDE.md (create a technique note rather than let
  a router hold execution).
- **C3 Angler constraint → profile:** "manual reels only" reframed as Cameron's
  profile constraint (already in `profiles/cameron/rods.md`); the species note
  states the fishery uses both electric-assist and manual. General rule added.
- **C4 No relative time:** swordfish seminar pinned to Feb 2021 / seasons
  2019–2020; relative time banned KB-wide (CLAUDE.md). Enforced in the step-2
  review of all species notes.

### Step 7 (skills + template + build script)

- No `*.skill` package was provided → `skills/boat-day/` is a scaffold + build
  plan; `scripts/build-skill-resources.py` generates the deployable skill FROM
  the KB decision layer (planning + conditions + seasonal + locations + species
  routers + gear-classes) plus a named profile. Verified working with
  `profiles/cameron`, `--no-profile` (generic), and `profiles/_template`
  (56 notes bundled each).
- Generated skill artifacts (`skills/boat-day/resources/`, `SKILL.md`) are
  git-ignored and excluded from `link-maintenance.py` — regenerable, never
  committed.
- `profiles/_template/` completed (boat, rods, tackle, trolling-lures, spots +
  README): blank/generalized with fill-in prompts and a public-repo coordinate
  caution.
- Fixed a stale exclusion in `link-maintenance.py` (`spot-lists-PRIVATE-ONLY.md`
  → `spot-lists.md`) so the renamed raw spot file is treated as a raw input.

## Finish reconciliation — full 128 accounting

The 17 video_ids not consumed as a primary source in steps 1–6, accounted for
here (no silent drops):

| video_id | title | disposition |
| --- | --- | --- |
| aBnpfNKAN_g | Tackle & gear storage bags | `skipped: generic filler` (not SoCal-specific) |
| VK2By1vTKBc | Clothing options for sportboats | `skipped: generic filler` |
| Dixn41OzeSE | What to bring offshore | `skipped: generic filler` |
| gC7dxSmiip8 | SD sportboat roundup 1/27/22 | `skipped: thin weekly roundup` — current intel superseded by the 17 dated Bight reports; pattern layer lives in `seasonal/` |
| 9emFjXt89N4 | SD sportboat roundup 2/3/22 | `skipped: thin weekly roundup` |
| NeYxQT-w42o | SD sportboat roundup 2/10/22 | `skipped: thin weekly roundup` |
| UDkKa2PU_4c | SD sportboat roundup 3/3/22 | `skipped: thin weekly roundup` |
| _a1e7-7Mbjw | SD fishing tips roundup 5/19/22 | `skipped: thin weekly roundup` |
| F1omCfmMsCU | SD report & tackle tips 5/26/22 | `skipped: thin weekly roundup` |
| nTLweGNuHKw | SD report & tips 6/17/22 | `skipped: thin weekly roundup` |
| _9um-TZOUgE | Tackle tips roundup 11/10/22 | `covered`: uni-knot/tackle content captured in `rigging/essential-knots` + `tackle/` |
| tyG2wBr0m8Q | Bluefin gear roundup 12/02/22 | `covered`: captured in `species/bluefin-tuna`, `bluefin-trolling`, `tackle/line-and-leader` |
| KVdnRJYq4jU | SoCal bays fall tips | `covered`: captured in `species/spotted-bay-bass` + `locations/bays-and-harbors` |
| 3tur7-VCM2g | Academy Ep8 — structure setup | `covered`: structure-setup doctrine captured via Ep5/Ep14 in `locations/bass-structure`, `species/calico-bass`, `sand-bass` |
| -eaaWPN5Fxk | Academy Ep7 — calico/sand tackle | `covered`: bass tackle captured in `species/calico-bass`, `sand-bass`, `tackle/gear-classes`, `lures/soft-plastic-swimbaits` |
| gH8JWhlqYqw | Academy Ep4 — spotty tackle | `covered`: captured via Ep3 in `species/spotted-bay-bass` + `lures/bay-bass-plastics` |
| 3txdqaQdBd4 | How Do You Gulp — Lenny Rudow | `covered`: gulp/plastic doctrine captured via `AqW_Z9pFcHU` in `species/rockfish-lingcod` |

Plus the two out-of-region skips logged at the top (`j2NhAD2An4s` FL king
mackerel, `gBAu56Uw8Fk` East Florida). **All 128 `_manifest.csv` video_ids are
now accounted** — a destination, `covered`, or an explicit `skipped: <reason>`.

## Coverage summary

- **128** transcripts, **all** accounted (destinations, `covered`, or `skipped`).
- **~110 knowledge notes** across conditions (11 at the main build; **12 after
  the GATE B punch list** — adds `water-regimes`), seasonal (9), species (18
  routers + 1 decision spin-out), techniques (18 incl. deep-drop-swordfishing +
  hoop-netting), lures (12), rigging (12), tackle (5), bait (3), fish-care (3),
  locations (7), planning (4). Plus Cameron's profile (5 + README), the
  `_template` profile, and the boat-day skill scaffold + generator.
- **All 11 memory-export sections** mapped (multi-destination — see the memory
  table).
- `link-maintenance.py`: **0 dead links**, idempotent, Mermaid cap 30.
- `build-skill-resources.py`: works with `profiles/cameron`, `--no-profile`, and
  `profiles/_template` (56 notes bundled each).
- **Species acceptance test: 18/18 pass** (each router answers where / when /
  how-to-find incl. a sonar-depth signature / technique-per-situation / gear class).

## Judgment calls (for Cameron's review)

**Structure / scoping**
- `profiles/cameron/spots.md` curates home-water anchors + BightSST eval targets
  with coords and **links the full 391-waypoint library** in
  `sources/spot-lists.md` rather than duplicating 391 lines across two files.
- Ocean whitefish gets **its own note** (tilefish relative), not folded into
  rockfish-lingcod (per amendment A3).
- **Two technique notes created per rule C2** (router never absorbs execution):
  `deep-drop-swordfishing`, `hoop-netting`.
- Weekly SD sportboat roundups **skipped as thin** (7-day-cutoff current intel;
  the pattern layer is the 17 dated Bight reports in `seasonal/`).

**Correction to an amendment's premise**
- The "byte-identical duplicate" claim for `vqsD0qpwcJA` / `Jtf-bU4aM-c` **does
  not hold** — verified distinct (titles, upload dates 2022-04-06 vs 2022-06-27,
  md5s, bodies). Both extracted separately; topic overlap noted. (One step-3/step-4
  subagent repeated the "identical" claim in its report — not carried into any
  note.)

**Conflicts kept side by side, attributed (never reconciled)**
- Yellowtail **water-state-over-calendar** (cameron) vs the **year-anniversary
  prior** (corpus, bluefin) — in `species/yellowtail.md` + `seasonal/year-anniversary-prior.md`.
- **Parallel current** prior vs the **into-the-island late-fall/off-color**
  exception (both Landesfeind) — in `conditions/current-structure.md`, `seasonal/november-december.md`.
- Moon **leading-days-strongest** vs **7-days-before-and-after** — in `conditions/moon.md`.

**Thin / low-confidence areas**
- **Mako, thresher:** absent from both inputs — recorded as a thin area, not
  skipped (no source to skip).
- **Pacific crevalle jack (toro):** zero corpus mentions — built from general
  SoCal/Baja knowledge + Cameron's interest; `confidence: low`, sonar read marked
  inferred.
- **Barracuda, bonito:** report-bycatch mentions only — `confidence: medium`,
  technique tables inferred.
- **Chunking mechanics:** the mapped dorado video doesn't detail chunking; note
  kept lean at `confidence: medium`, mechanics from proposal §4.5/§6.7.
- **Fish-care §9 numbers** (slurry/chill) have no video_id in the corpus —
  attributed in prose to the seminar/report context, not in front matter.

**Deferred (flagged, not dropped)**
- Memory §2 **fleet-intelligence practices** (AIS sportboat tracking, Everingham
  bait boats, VHF ch72) have no dedicated note yet — candidate:
  `planning/fleet-intelligence.md` or a section in `planning/search-and-glassing.md`.
- **Lobster regs** stated from a 2019 source — flagged in-note to verify with
  current CDFW rules.

**Caption-garble corrections (flagged)**
- `leadhead-mods` (F-vOTerdulU): caption "8 oz → 1 oz" rendered as the plausible
  1/8–1 oz; `rubber-band-deep-rig` (sYrsPGXiYhI): concept only, no shaky numbers.

**GATE B review corrections (punch list P1–P6, approved & executed 2026-08-12)**

Cameron's expert pre-merge read, executed under a fresh `PLAN APPROVED` for the
punch-list revision (which also committed the governing plan as
`sources/plan.md`). Corrections and the judgment calls made executing them:

- **P1 — `species/yellowtail.md` Where & when rebuilt range-wide N→S** (Channel
  Islands/SBI–Sutil squid zone · Catalina · SCI · coastal kelps · La Jolla/SD
  banks · Coronados · paddies · Baja coast · BOLA); `5p6gu14ZC4w` added to
  sources. Judgment calls: (a) **caption-garble correction** — 10/26/22's
  "foreign First Bank" (Catalina, fall yo-yo, closure where only yellowtail and
  bonito may be kept) identified as **Farnsworth Bank** from the described
  closure rule; flagged in-note. (b) **Coastal kelps** and **Baja coast**
  entries carry thin corpus support — attributed `cameron` and marked thin
  in-note rather than padded.
- **P2 — `techniques/surface-iron.md`**: new **Size / weight selection**
  (wind → heavier iron, `D5DR7Kx42_A`; anchovy/"rice" → downsize ~⅓ weight,
  2–3:1 bite advantage, `pcwcRdmWmLc`) and **Color** sections. Color is an
  **honest thin area — no doctrine invented**; the lone color datum (squid
  color + glow, 4/21/22 `YZtX1MiT0y8`) is explicitly labeled as coming from the
  slow-pitch/knife-jig context, not surface iron. `D5DR7Kx42_A`, `pcwcRdmWmLc`,
  `YZtX1MiT0y8` added to the note's sources.
- **P3 — `species/yellowfin-tuna.md`**: trolling expanded to a full
  troll-to-locate situation entry (cedar/feathers ~6–6.5 kt, convert the stop);
  **spread-design geometry (setbacks/positions) flagged as a thin area** —
  corpus gives speeds, not spread design.
- **P4 — router-stub rule** added to CLAUDE.md (flagged stub, never silence).
  **Stubs added by the sanctioned audit** (each `⚠ Flagged stub — no corpus
  source yet`):
  - `species/yellowtail.md` — **trolling to locate** (esp. Baja) — the P4 stub.
  - `species/california-halibut.md` — **bounce-ball trolling** (standard SoCal
    coastal-flats halibut method; absent from corpus).
  - Audit found **no other clearly-warranted stubs** — the remaining routers'
    tables (bluefin, dorado, marlin, WSB, calico, sand bass, barracuda, bonito,
    rockfish-lingcod) already carry their standard real-fishery methods.
- **P5 — regime layer** (cameron house doctrine, high):
  `conditions/water-regimes.md` created (four regimes + anomaly guidance);
  `seasonal/README.md` routes regime-first; all **8 month notes** headed with
  their regime (punch-list "(9)" corrected — seasonal/ = 8 month notes +
  year-anniversary-prior); `year-anniversary-prior.md` reframed as a **location
  prior WITHIN the fall-fragmentation regime** with the
  water-state-vs-anniversary conflict kept visible; species Where & when keyed
  to regime with months in parentheses across all routers with seasonal
  content; governing plan committed as `sources/plan.md` with the Context
  correction and tree counts synced (conditions 12, techniques 18).
- **P6 — this entry.**

**2026-08-12 review fix pass (32 verified findings + A1–A5 + X1–X5; approved
manifest; one commit per tier).** Corrections and judgment calls:

- **Factual (F1–F5):** speed-troll trigger corrected to **too-LIGHT-to-kite**
  in both bluefin routers (the "too rough" direction was a build error — every
  source encodes no-wind; kite band 8–15 kt kept); "first sword flags
  mid-December" demoted to an **Observed** (5D1vx29LVpI, 12/15/22); the
  zero-width "900 ft – 150 fm" DSL band restored to the seminar's **≥600 ft,
  preferred ~950/150 fm and deeper**; Mad Mac speed doctrine reconciled as
  conditional (9–12-to-14 cameron normal-spread band vs 13–15 Winnicki
  speed-troll band, 15-vs-14 tension flagged); knife-jig leader conflict
  restored side-by-side (crimp school nRFFM8DT-og vs direct-tie school
  j37zxs33gws) in knife-jigging + bite-leaders.
- **Completeness (C1–C4):** sword seminar terminal rig / lights / drag pair /
  endgame extracted into deep-drop-swordfishing; kite flyer numbers
  (3–3.5 ft max leader, 45° wings, 5/0 5X Mustad) into flying-fish-harness
  (kite note's pointer now true); speed-troll leader cap + crimp-buffer rules
  into speed-trolling (+ mad-mac cross-ref); the **Eddie bomb** captured in
  knife-jigging.
- **Provenance (P1–P2, R1):** log rows corrected for 4xzK7YaXK5s (content was
  merged into kelp-paddies + bait-tanks all along — attribution added),
  -JZpyWLdKlk (june-july + white-seabass, not august), bydQzE3F9yM
  (breakwalls, not bird-reading), sYrsPGXiYhI (id added to the bluefin
  router); unlogged destinations added (yo-yo-iron, pacific-crevalle-jack,
  june-july); the false VgpgJ8IAyJo citation removed from mad-mac /
  dtx-minnow / tuna-feathers **and from bluefin-trolling** (log row 84
  corrected — no promo content traces to any of them).
- **Rubric (R2–R5):** Nomad/Yo-Zuri promo claims flagged low per the
  sponsored-claims rule (dorado, tuna-poppers); april/may priors downgraded
  to medium (single-report sources); nov–dec "He" threshold attributed to the
  Z3rZqy2Pi8E report speaker and the 11/23/22 temp edge recast as Observed.
- **Routing (G1–G7):** inshore/bay gear classes added to the lexicon (specs
  drawn only from the notes that use the terms; **Light troll class kept as a
  stub** — no corpus source defines it); `techniques/inshore-crankbaits.md`
  created (GVP3IChsmRQ, gH8JWhlqYqw, n6PTy8g3pb0) and the three bass routers
  trimmed to link it; `techniques/bait-and-switch.md` created as a **flagged
  stub whose skeleton is explicitly marked UNSOURCED** (judgment call: no
  transcript covers tailing/pitch and the export lists marlin only as an open
  item — the build-era router prose was retained but provenance-flagged, not
  asserted); bonito small-jig row stub-flagged; search-and-glassing links
  added (sword/halibut/spotted-bay; lobster gets a does-not-apply note);
  sword router gained seminar-sourced surface-sign (rips/highway rip) + a
  finning-fish stub; halibut squid-bed months resolve via April priors;
  day-plan protocol step 4 links the gear-class lexicon.
- **Duplication (D1–D4, per A2):** single-home established for the foamer
  program (foamer-casting; slack-tide timing merged there), post-moon
  discipline (moon.md; the two diverged copies merged — coverage-bias AND
  relocation-not-bite-death both kept), lure running params (lure notes;
  Half Fish spec → spreader-bar only), DSL sounder settings
  (electronics-and-sounder). Every trimmed router re-checked against the
  species acceptance test — where/when, finding, situation decisions, and
  gear classes all remain in-router with execution one link away.
- **Conventions + A4/A5:** relative time anchored ("2026 is his first
  season", "as of 2026-08"); "(memory, …)" Observed attribution corrected to
  cameron; two near-verbatim tuna-feather clauses paraphrased; **new
  regulatory-claims rule** added to CLAUDE.md and retro-applied
  (spiny-lobster, rockfish-lingcod, hoop-netting — California/CDFW, as of
  2026-08); `decision` added to the type enum and bluefin-trolling re-typed.
- **A6–A9 amendments (Cameron, 2026-08-12, approved separately after the fix
  pass merged):** speed-troll trigger widened to **wind OR coverage** (too
  light to kite, or fish too spread out to sit and kite over) across both
  bluefin routers + mad-mac, with Cameron's reading of Winnicki's "the
  conditions" made explicit; **presentation-size axis** added to the
  bluefin-trolling table (bar = small, Mad Mac = large; forage size can
  override the sea-state row); **yellowtail router reframed** — the three
  faces are outputs of water temp + bait depth on one population (states,
  not fish types; fish roam the column and feed looking up), rows marked
  starting-ranks-not-exclusive-routes, three-outfits switching doctrine
  added; **night-bite mechanism** recorded as two reads kept side by side —
  corpus food-following vs Cameron's reaction-bite read, the latter
  explicitly flagged *likely, not measured* (bluefin router + DSL layer).
  All cameron-attributed.
- **Tooling (X1–X5, T2):** link-maintenance now strips code before link
  parsing (fixture: `tests/link-fixture.md`), validates before writing
  (zero writes on dead links), and raises on reversed markers;
  `profiles/` + `skills/` get generated index READMEs; **SKILL.md is now
  hand-authored and committed** (un-gitignored) with the raw-GitHub fetch
  base for execution-layer links — judgment call on X4: rather than full
  note-treatment, link-maintenance validates SKILL.md's links without
  adding backlinks/indexing (VALIDATE_ONLY), since a skill definition is
  not a KB note; build script never overwrites SKILL.md and rejects
  `--profile` + `--no-profile` together.

**Cameron open items preserved (attributed, not doctrine)**
- SPJ/speed-jig setup shopping; 10 ft jig-stick yellowtail reps; kite (no helium/
  no tank room) + foamer (no-bait run-and-gun) constraints; dedicated sabiki-rod
  build; cast net for Mexico; striped-marlin deployment-trigger learning; toro
  target; drill-powered retrieve; Fathom 80 respool-to-bulk-spool; Yo-Zuri Hydro
  Minnow "LC 205" size to verify; dad's unidentified skirt bag; Tranx braid
  pending respool.

## Batch 2 landing (adopted) — 2026-08-13

Adopted onto `claude/batch2-ingestion-rb0v4i` (recut from `main` @ ef7f7c9)
from the two landing branches: `claude/raw-transcripts-private-e2zn7m`
(six playlist dirs, 400 transcripts, +429 manifest rows) and
`claude/add-zip-transcripts-1xjewx` (Crust to Coast batch, 18 transcripts).
Phase 0a adopted verbatim; Phase 0b reorganized per-channel and normalized
the master manifest. The batch-2 analysis doc is committed verbatim at
`batch-2-analysis.md` (source of the channel rules used in triage).

**Repo visibility:** Cameron CONFIRMED (2026-08-13) that full third-party
transcripts remain in this PUBLIC repo. (They were already public on the
landing branches; this records the explicit confirmation.)

### Landed state (verified; every figure recounted from disk/manifest)

| channel dir | .md files | manifest rows | failed rows |
| --- | --- | --- | --- |
| (flat) BDOutdoors batch 1 | 128 | 128 | 0 |
| stoked-on-fishing | 255 | 278 | 23 |
| your-saltwater-guide | 108 | 113 | 5 |
| dirty-hookers | 22 | 23 | 1 |
| roman-castro | 12 | 12 | 0 |
| crust-to-coast | 18 | 19 | 1 |
| joewo (stray) | 1 | 1 | 0 |
| kevin-is-cooking (stray) | 1 | 1 | 0 |
| okuma-fishing-tackle-usa (stray) | 1 | 1 | 0 |
| **total** | **546** | **576** | **30** |

546 ok rows map 1:1 onto the 546 transcript files (verified by id-suffix
match; note some video_ids begin with `-` or contain `--`). caption_type
normalized to the master vocabulary (223 `(en)`-suffixed rows). All 29
blank-channel failed rows backfilled by unambiguous block agreement.
Transcript files themselves are untouched raw sources — the dirty-hookers
`M:SS` duration format and Crust's YAML-front-matter headers (vs the
bullet-header format elsewhere) are normalized at parse time, never edited.

### Discrepancies (analysis doc / prior landing log vs what actually landed)

1. **Corpus size:** the analysis doc measured 5 zips / 294 files; 7 zip
   inputs were actually received and 400 files landed. The delta is exactly
   the stoked-on-fishing-offshore playlist the doc never saw (112 files +
   9 failed rows) plus a BDOutdoors zip byte-identical to batch 1 (logged
   duplicate, nothing copied). Arithmetic closes: 294 − 6 cross-zip dups
   dropped at land time + 112 = 400; failed rows 20 + 9 = 29.
2. **Prior landing-log table was wrong:** the "Batch 2 landing — 2026-08-12"
   section on the raw branch mis-attributed per-batch manifest rows (e.g.
   offshore 133 claimed vs 121 actual; roman 14 vs 13). The analysis doc's
   figures and the actual manifest agree; that branch's table does not.
   This section supersedes it.
3. **"Keep the more complete fetch" is unverifiable for 5 of the 6 known
   Stoked cross-zip duplicate ids** (6-mi3Qxn37c, H-vIGWPIPVc, Y2bXn44lfqo,
   82gEHYel-4U, ldVj0BoB-kE, FE63WNlwkKw): land-time dedup kept the
   stoked-on-fishing-zip copies and never committed the discarded Inshore
   fetches. For FE63WNlwkKw — the one pair the doc characterizes — the doc
   says the Inshore copy was the incomplete one, so the kept copy IS the
   more complete fetch. The other 5 kept copies stand as-is.
4. **Stoked "~90s post-2014 boilerplate":** caption-text evidence contradicts
   the doc — no ~90-second text block exists anywhere in the corpus (0 regex
   hits); the measurable artifact is a ~16-second giveaway/subscribe read on
   a 2019-era subset. Both claims recorded side by side, not reconciled
   (the ~90s open is presumably visual/music, invisible to captions).
   Operative triage/extraction rule: ignore intro sponsor/giveaway reads
   wherever present.
5. **"Backfill status for the 128 BD rows"** was already complete on `main`
   (all 128 rows `ok`) — no-op.
6. **Accounting denominator:** the doc's Phase 5 says "~314 new manifest
   rows"; the actual number is 448 (429 batch-2 + 19 crust).
7. **Crust to Coast was not in the analysis doc at all** (it arrived as a
   separate playlist fetch, not one of the zips): 19-part undergraduate
   "Geology 5" oceanography course, ~10.5 h, all auto captions, channel id
   UC4lyFLgi-ZqANz1m-zb2zrw, playlist PLOMMpqItRwQna8TRhb8KHjjD3zoZp-a1j,
   fetched 2026-08-12; 1 failed fetch (DRbl0fVgGIo, "Geology 5 - Climate
   Change", captions disabled by uploader — permanent). Characterized fresh
   at triage; proposed registry frame in the batch-2 report.

### Strays (header-vs-directory scan of all 546 files: exactly 3)

| video_id | actual channel | disposition |
| --- | --- | --- |
| YGKgQp5HTLM | JoeWo | Call of Duty gaming video — `skipped: not fishing` at triage |
| mwrFx2DdmO0 | Kevin Is Cooking | tacos recipe; transcript is 3 useless lines — `skipped: not fishing` |
| 55IthpZZx9k | Okuma Fishing Tackle USA | content is Capt. Dave Hansen (YSG) at the Okuma booth — triaged on merits, feeds the dave-hansen registry row |

### Failed fetches worth flagging to Cameron (in-scope losses)

`Qurgc-HtsuA` (yellowtail fillet local-style), `1CQGXwqmURA` (life of a
calico bass), `JgknlyfTtgE` / `9O0AnMQkEM4` / `gaa3_aBFL5A` (SD-bay + SWBA
episodes). If captions can be sourced another way, they can land in a later
batch.

**CORRECTED 2026-08-17 (batch 3, Phase 0) — the "orphaned part 3" sentence
here was inverted, and conflated two different series.** The original read
"one orphaned Stoked 'part 3' whose parts 1–2 failed." Verified from the
manifest and the worklist, the two cases are:

- **`CyOsniVmbN8`** ("Top Gun 80 Epic 5 Day, part 3", 2016 series) — a part 3
  whose **parts 1–2 SUCCEEDED and were extracted** (`HueC1KHrcVw`,
  `i3qIAHW-SJc`, both `done`/parameter-skim). The trip is 2/3 covered; only
  the finale is missing.
- **SWBA Midnight Standoff** — the inverse, and the worse loss: **parts 1–2
  both failed** (`9O0AnMQkEM4`, `gaa3_aBFL5A`) while part 3 (`2ivn-N0as_A`)
  landed but was `skip:thin-generic`. **That trip is entirely uncovered.**

Also checked while verifying: **"Top Gun 80 Epic 5 Day" is two different
3-part series sharing one title** — a 2016-08-08 run (`HueC1KHrcVw`,
`i3qIAHW-SJc`, `CyOsniVmbN8`) and a 2017-05 run (`Rb5I2ljAqeE`,
`3T4c3Zez_DM`, `tU4jhAkdzNw`). Body trigram similarity between the
corresponding parts is **0.035** — genuinely different trips, not duplicates.
This is the title-collision hazard `batch-2-analysis.md` flagged; no dedup
action needed, but the pairs must never be merged on title.

#### The remaining failed rows — full accounting (added 2026-08-17, batch 3 Phase 0)

The log's own accounting rule (top of this file) is that **every** manifest
row appears with at least one destination or a `skipped:` reason. 30 rows have
`status != ok`; before this pass only 7 were named anywhere in the log. The
other 23 existed solely as CSV rows. Logged here so the corpus reconciles:

| video_id | channel | title | why it failed |
| --- | --- | --- | --- |
| `uEBrJRF4XF0` | Dirty Hookers | (unknown - private) | private / unavailable |
| `2u8RltOpJvc` | StokedOnFishing | Feeding Bluefin Tuna Inside A Mexican Tuna Farm | no captions published |
| `MtDq59APQ5E` | StokedOnFishing | A Day in the Life: Fishing Aboard Stoked On Fishing Charters | no captions published |
| `TeyDZiFYucg` | StokedOnFishing | Spectacular underwater Dorado footage | no captions published |
| `1nzjUTKaqa0` | Your Saltwater Guide | Rubberband Technique (Live bait Rig) for Bluefin Tuna | no captions published |
| `HHosp_6UdsI` | Your Saltwater Guide | WIDE OPEN Offshore Fishing BITE \| Dorado | no captions published |
| `HTFXFQBtJWI` | Your Saltwater Guide | The Pro Tek Offshore Fighting Grip in Action! | no captions published |
| `WUml1d0tyjY` | Your Saltwater Guide | Lobster Tips from Captain Dave Hansen | no captions published (Polish auto only) |
| `2RXQrztyKXE` | StokedOnFishing | (no title captured) | private / unavailable |
| `54ot7AHYsDk` | StokedOnFishing | (no title captured) | private / unavailable |
| `R2Q5S69zudk` | StokedOnFishing | (no title captured) | private / unavailable |
| `YLwpDNSE7Pk` | StokedOnFishing | (unavailable) | private / unavailable |
| `ZTE6a8AJvM0` | StokedOnFishing | (no title captured) | private / unavailable |
| `_kINfxgG1eA` | StokedOnFishing | (no title captured) | private / unavailable |
| `hsAXP_KK18Y` | StokedOnFishing | (no title captured) | private / unavailable |
| `oZRaUkwN0KA` | StokedOnFishing | (unavailable) | private / unavailable |
| `pgu1bT8Rr5g` | StokedOnFishing | (no title captured) | private / unavailable |
| `sSjUSbr-hEo` | StokedOnFishing | (no title captured) | private / unavailable |
| `xBBLXq3BN2Q` | StokedOnFishing | (unavailable) | private / unavailable |
| `yfysrxXLtF4` | StokedOnFishing | (no title captured) | private / unavailable |
| `zA5DAGqKe-4` | StokedOnFishing | (unavailable) | private / unavailable |
| `zoZhRDdFU-8` | StokedOnFishing | (unavailable) | private / unavailable |
| `knkho_rBWDA` | Your Saltwater Guide | youtube video #knkho_rBWDA | private / unavailable |

**The split that matters for recovery:** "no captions published" means the
video is public and simply has no caption track — **transcribing the audio
recovers it**. "Private / unavailable" cannot be recovered at all. Across all
30 failed rows that is **14 recoverable / 16 permanently lost**. The
recoverable set is a batch-3 re-transcription target; `1nzjUTKaqa0`
(rubber-band rig) and `WUml1d0tyjY` (Hansen on lobster) are the two most
on-doctrine.

### Tooling note

`scripts/link-maintenance.py` `EXCLUDE_FULL` gained `batch-2-analysis.md`
(must stay byte-verbatim — no backlinks block), `escalations.md`, and
`batch-2-progress.md` (mechanical pipeline files). Made in this human-gated
setup session; the unattended pipeline's guard treats `scripts/` as
protected.

## Batch 2 dedup — 2026-08-13 (precedes triage; findings only, files kept)

Method: exact video_id collision check (none — 576 unique ids), body-md5
(no byte-identical files), then content word-trigram Jaccard similarity on
caption text over duration-matched pairs (±2s) across all 546 transcripts,
plus a YSG-internal pass with no duration gate. Duplicated/re-cut footage
never counts as independent confirmation of doctrine. Files and manifest
rows are all KEPT (provenance); duplicates enter the triage worklist as
`skipped: duplicate-of <primary>`.

### YSG intra-channel re-uploads (doc predicted 11 pairs; sweep found 11 candidates)

Keep earlier/longer as primary; the later re-upload is the duplicate.
Pairs at sim < 0.80 carry a `confirm-at-triage` flag (triage reads every
video anyway); the two mismatched-duration pairs are NOT re-uploads — both
sides stay in the worklist with a re-cut-footage cross-reference.

| duplicate (skipped) | primary (kept) | sim | durations | note |
| --- | --- | --- | --- | --- |
| 9xHgdtNek1U (2022) | gKrYKvqHUjk (2020) | 1.000 | 408s = 408s | text-identical; headers differ, so not byte-identical — closest match to the doc's "one byte-identical" claim (recorded as a doc-vs-sweep discrepancy, not reconciled) |
| Pv5JMTTY4nI (2021-12) | 9qnQjPPT5yg (2021-05) | 0.946 | 354s = 354s | |
| YVHdDbkQrKk (2022) | w5_x6kkN-xE (2021-04) | 0.922 | 502s = 502s | |
| bsbL7JeKxMo (2021) | 8jC61LzQoxU (2018) | 0.771 | 353s = 353s | confirm-at-triage |
| YvWHJ0Dgupc (2022-02) | ftEvyfwjZFU (2021-06) | 0.728 | 383s = 383s | confirm-at-triage |
| 44pjBUn0nP8 (2021) | wYeKJLoKo4g (2018) | 0.723 | 104s = 104s | confirm-at-triage |
| 67qLBEtd3EU (2022) | KTsXdQXAnkU (2019) | 0.694 | 427s = 427s | confirm-at-triage |
| q4NBPuH3gCA (2022) | 5FzBwvMtRP8 (2019) | 0.463 | 205s = 205s | confirm-at-triage (same duration + same rag-bait topic; heavy ASR divergence) |
| 89DmEDR-1sI (2020-01) | 6zYRI1ZQU3c (2019-12) | 0.430 | 197s = 197s | confirm-at-triage (same duration + same chumming topic) |
| — not a re-upload — | YPhc0zr7oBs ↔ aFb221LUoD0 | 0.514 | 515s ≠ 994s | overlapping Catalina footage; BOTH stay in worklist, cross-referenced |
| — not a re-upload — | qv0QbLgp72o ↔ zwNEhWtnBCE | 0.512 | 502s ≠ 284s | overlapping footage; BOTH stay, cross-referenced |

**Doc-vs-sweep discrepancy (reported, not reconciled):** the analysis doc
says 11 re-upload pairs, "one byte-identical, most ≥0.83 trigram overlap,
identical durations." The sweep finds 11 candidate pairs but only 3 at
≥0.83, none byte-identical at file level, and 2 with non-identical
durations. Similarities here are depressed by independent ASR fetches of
the same recording; the count matches exactly.

### YSG ↔ BD same-recording pairs (doc's known set of 3 — all located)

| YSG id | BD id (primary; already extracted in batch 1) | evidence | disposition |
| --- | --- | --- | --- |
| kr-DZP7OVmg | 4xzK7YaXK5s | sim 0.814, both 263s — found independently by the sweep | `skipped: duplicate-of 4xzK7YaXK5s` |
| 8Asmd2H56Qk | sYrsPGXiYhI | both 202s; sim only 0.518 (ASR variance; doc asserts same recording) | `skipped: duplicate-of sYrsPGXiYhI` |
| IMnoZVEYpm4 | m2q22sPPkEM | YSG cut 442s vs BD 328s (+114s), sim 0.560 — YSG is the longer cut, per the doc | worklist row, depth `single-pull`: extract ONLY tail content beyond the BD cut |

### Stoked working-title duplicates (new findings)

| duplicate (skipped) | primary (kept) | sim | durations | note |
| --- | --- | --- | --- | --- |
| ZBRSB4iwtbU ("cedros Jose calicoreleaseVid") | ldVj0BoB-kE (Cedros regulation-change episode) | 0.641 | 117s ≈ 117s | raw/working upload of the same footage; confirm-at-triage |
| qBZxnRuXtGo ("TMP -----------OliveCrest 25") | SdwwpQMJEOI (published Olive Crest episode) | 0.630 | 1367s ≈ 1368s | uncleaned working title the doc flagged; confirm-at-triage |

### Batch-1 internal duplicate (NEW finding — outside batch-2 scope, flagged for Gate B)

`Jtf-bU4aM-c` ("Does SLOW PITCH JIGGING work for YELLOWTAIL?!", 2022-06-27)
and `vqsD0qpwcJA` ("Slow Pitch Jigging // Yellowtail LA Bay Baja",
2022-04-06) are the same recording (sim 1.000, both 338s) — a re-upload
inside the original 128-video BD corpus that batch 1 treated as two
independent sources (both appear in `species/yellowtail.md` front-matter
sources). Per the re-cut rule they are ONE source; any doctrine counted as
independently confirmed by both should be demoted to a single mention.
Not fixed here (batch-1 accounting is canonical on main) — judgment call
for Cameron at Gate B.

### Sweep coverage note

The 6 known Stoked cross-zip ids exist as single copies on disk (land-time
dedup) — nothing to pair. No new-vs-BD duplicates surfaced beyond the known
YSG↔BD set and the batch-1 internal pair above. Near-dup flags below 0.60
were not recorded (noise floor); triage reads every video regardless.

## Batch 2 triage — 2026-08-13 (every video read; the table below IS the worklist)

Method: 17 parallel readers, ~25 transcripts each, every one of the 418
in-scope ok transcripts opened (title-only triage prohibited per the
analysis doc — and confirmed necessary: YSG titles mislead systematically,
several Stoked "Inshore"-playlist episodes are out-of-region travel).
Classes `tutorial|report|on-the-water|seminar|promo|out-of-region|
non-fishing`; depths `deep|parameter-skim|observations-only|single-pull|
skip:<reason>`. The 30 failed manifest rows have no transcripts and are
accounted in the landing section, not here.

**Totals: 418 rows = 271 pending + 147 skipped.**
Depth distribution: deep 62, parameter-skim 92, observations-only 101,
single-pull 16, skip 147.

| channel | pending | skipped |
| --- | --- | --- |
| Dirty Hookers | 20 | 2 |
| Roman Castro | 7 | 5 |
| Your Saltwater Guide | 75 | 33 |
| StokedOnFishing | 158 | 97 |
| Crust to Coast | 11 | 7 |
| strays (JoeWo / Kevin Is Cooking / Okuma) | 0 | 3 |

Doc-vs-triage yield comparison (doc measured only its 294-file view; its
estimates are non-binding for the stoked-offshore playlist it never saw):
DH 20 pending vs doc "~20 post-triage" — match. Roman 7 vs "~6" — match.
DH deep = 11, exactly the doc's "11 warrant deep extraction". YSG 75
pending is above the doc's "~32 clear the bar" because parameter-skim and
single-pull rows are included liberally (extraction depth bounds the
effort); YSG deep = 24. Stoked 158 pending of 255 runs obs-heavy
(observations-only 101 across the corpus), consistent with the doc's
"primarily an observation source". All six of the doc's pre-identified
Stoked doctrine carriers were confirmed from content (yo-yo ntQXxcH5sjI,
bluefin trolling xzIaUEDklrE, Cedros reg change ldVj0BoB-kE, Pacific
Giants usHl-4SfqDA, Aaron Martens calico P6Slg6RQiXw, kelp-paddy pattern
A6DJoXbID4c / VWClGAn2WEw) plus five content-escalated deep finds
(vCskOx6N-XM kite/spreader selection, 3qSY328fFYo marlin trolling,
Ix0gG0-l3v0 kite/flyer rigging, mDmbGdQAy-4 kite/railroading,
SH7zOA9ZF3o yo-yo cadence kept at skim).

### Judgment calls & flags (for Cameron's review at Gate B)

1. **Clarion Island (Revillagigedo) long-range series (4 eps) classified
   out-of-region** — reached from San Diego but far south of the Baja
   peninsula and not on the doc's in-scope list. Reversible by editing 4
   worklist rows.
2. **Alijos Rocks treated as in-scope Baja** (long-range bank on the Mag
   Bay routes); flagged as edge-of-scope.
3. **Two YSG transcripts are wholly garbled ASR** (5nTGoZ9_nzU,
   qihSsdqBU2A — song-lyric-like text unrelated to their titles; likely a
   captioning bug) — skipped no-usable-content; captions could be
   re-fetched in a later batch.
4. **lF6jQklDCrY carries a self-hedged regulatory claim** (rockfish depth
   limit 350→460ft, speaker admits uncertainty) — single-pull row; the
   extractor/evaluator escalation rule for regulatory claims applies.
5. **Freshwater SoCal content excluded** (Legg Lake tournament, Clear
   Lake, Lake Cachuma) per the freshwater rule even where the location is
   SoCal — including FE63WNlwkKw, one of the six known cross-zip ids.
6. **Cooking-only videos skipped as not-fishing**; catch-clean-cook with
   in-scope catch footage kept as observations-only with a fish-care note
   (e.g. IxhdiX3oEEs, H-vIGWPIPVc).
7. **Okuma stray 55IthpZZx9k judged promo** (ad-copy pitch) — still cited
   by the dave-hansen registry row as a cross-channel appearance.

### Dedup addenda discovered at triage (extends the Phase 1 tables)

| duplicate (skipped) | primary (kept) | evidence |
| --- | --- | --- |
| epWXURDU-oI | 9xNhdu2aBqE | same Todd Klein SCI trip/dialogue, short highlight cut (found by reader, not in the sweep's duration gate) |
| YPhc0zr7oBs | aFb221LUoD0 | RECLASSIFIED from Phase 1's "overlap, both stay": readers confirmed near-verbatim the same swell/current/water-color seminar in two cuts; shorter cut skipped |
| mDmbGdQAy-4 | usHl-4SfqDA | NOT skipped — both stay pending (both deep, different episodes sharing re-used kite/railroading footage); extraction must treat the shared segments as ONE source per the re-cut rule |
| 7U4N1f0viOU | (Cedros Oct trip series) | best-of recap reusing that trip's footage; stays observations-only but counts toward the SAME trip/observation event |
| All 6 Phase-1 confirm-at-triage YSG pairs | — | confirmed same-recording by opening both sides (bsbL7JeKxMo, YvWHJ0Dgupc, 44pjBUn0nP8, 67qLBEtd3EU, q4NBPuH3gCA, 89DmEDR-1sI) |

### Crust to Coast characterization (fresh, per plan)

18 lectures: 10 mechanism-relevant (seminar / parameter-skim → conditions/
destinations: water-column structure, currents/upwelling/ENSO, tides,
nearshore processes, wind-driven sea state, food web) and 8
adjacent-background skips (rock geology, plate tectonics, sediments,
taxonomy, sea ice, pollution, navigation history, deep time). The three
most fishing-relevant: 32TQdFJKIlI (Ocean Circulation — gyres, Ekman
transport, upwelling mechanics tied to kelp productivity, full ENSO
explanation; the clearest feed for upwelling/ENSO mechanism),
RuNH5O9olfw (Coastal Oceanography — surf-zone anatomy, longshore
transport), 9tTM99InluM (Tides — lunar/solar bulge mechanics, why the
moon dominates). Registry frame: mechanism source only, never fishing
doctrine, no Observed blocks (proposed registry row ships with the
infra commit).

### Worklist (the unattended pipeline's state machine)

Row order = extraction order (doctrine density first, per the analysis
doc): dirty-hookers → roman-castro → your-saltwater-guide →
stoked-on-fishing → crust-to-coast → strays. For pending rows the
`result` column carries the triage evidence (the extractor's input);
the pipeline overwrites it with the extraction outcome. Statuses:
`pending | done | skipped | escalated | reverted`.

<!-- batch2:worklist:start -->
| video_id | channel | class | depth | status | result |
| --- | --- | --- | --- | --- | --- |
| Ul5FLB2dFgQ | Dirty Hookers | seminar | deep | done | lures/knife-jigs.md; tackle/gear-classes.md; techniques/knife-jigging.md / Merged speed-jig stroke mechanics, depth-call/marking-interval variant, hookset doctrine, drag-conflict note, gear-class deta |
| gevNj2Y1Ep8 | Dirty Hookers | tutorial | parameter-skim | done | lures/knife-jigs.md; lures/tuna-poppers-and-stickbaits.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; techniques/knife-jigging.md / Amended 5 existing notes with parameter-skim content (line c |
| RfiC8sfIWTk | Dirty Hookers | tutorial | parameter-skim | done | lures/knife-jigs.md; rigging/rubber-band-deep-rig.md; tackle/hooks.md; techniques/knife-jigging.md / parameter-skim integrated as attributed medium-confidence additions (night-bite jig color, day/nigh |
| -MP2RqJC7B0 | Dirty Hookers | tutorial | parameter-skim | done | lures/knife-jigs.md; tackle/rod-and-reel-selection.md; techniques/knife-jigging.md / rod-stiffness caution at 40-50lb bluefin grade, mono-vs-fluoro bite-leader logic, 3-hook assist config kept as unre |
| 149px8WQ2Ng | Dirty Hookers | tutorial | parameter-skim | done | lures/knife-jigs.md; lures/tuna-poppers-and-stickbaits.md; rigging/rubber-band-deep-rig.md; species/bluefin-tuna.md; techniques/knife-jigging.md / deckhand-POV daytime/night bluefin gear parameters (j |
| dEPuDrhoClM | Dirty Hookers | tutorial | parameter-skim | done | bait/making-bait.md; tackle/hooks.md; techniques/dropper-loop.md / Baja/Sea-of-Cortez parameter-skim: sabiki line-weight logic, sabiki/grouper sinker sizing, cabrilla/grouper hook sizing by bait; medi |
| YGLFn8lPMu0 | Dirty Hookers | tutorial | parameter-skim | done | rigging/essential-knots.md / Merged RP-knot wrap-count variance, security loop, cinch tell, line-puller tool, uni-knot finish; reformatted bluefin anecdote as Observed block |
| WE643Fue1_A | Dirty Hookers | tutorial | parameter-skim | done | lures/iron-jigs.md; species/yellowtail.md; tackle/line-and-leader.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / 40lb Cedros line floor, jig picks (JRI Stinger/Starman 112/Kicker 25), mint |
| lJelQa1o6qk | Dirty Hookers | promo | skip:promo | skipped | Sponsor-announcement video (partnering w/ Opsin Fluorocarbon); product-property pitch, sponsor-heavy |
| A70kK2niu2Q | Dirty Hookers | tutorial | deep | done | lures/iron-jigs.md; lures/knife-jigs.md; lures/tuna-poppers-and-stickbaits.md; species/yellowtail.md; techniques/flyline.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / rod/reel/line/lure p |
| LPhnsEamRwI | Dirty Hookers | tutorial | deep | done | rigging/essential-knots.md; rigging/rubber-band-deep-rig.md / Bluefin sinker/rubber-band rig tie-on (leader wraps, San Diego-over-Palomar reasoning, band attachment sequence) merged; deduped repeated  |
| PrdPJy26H8c | Dirty Hookers | tutorial | parameter-skim | done | species/bluefin-tuna.md; species/skipjack-tuna.md; tackle/hooks.md / tuna-species downsizing logic (bluefin exempt vs skipjack/schoolie yellowfin), SoCal yellowtail/offshore baseline hook rotation (2/ |
| CW02kca8fh4 | Dirty Hookers | tutorial | skip:thin-generic | skipped | Apparel/gear unboxing + subscriber-count pitch; anecdotal rod tour, minimal decision logic |
| LTCFjqtSI8g | Dirty Hookers | tutorial | deep | done | techniques/flyline.md; techniques/knife-jigging.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / merged updated 2023 rod/reel/line/leader builds (flyline, yo-yo, new speed-jigging starter ki |
| 42A8Owhc8fw | Dirty Hookers | tutorial | parameter-skim | done | rigging/bite-leaders.md; rigging/rubber-band-deep-rig.md; tackle/rod-and-reel-selection.md; techniques/foamer-casting.md; techniques/surface-iron.md / pre-trip tackle update: foamer metal-bait picks,  |
| jQW2HLkMsmY | Dirty Hookers | tutorial | deep | done | lures/knife-jigs.md; lures/tuna-poppers-and-stickbaits.md; rigging/rubber-band-deep-rig.md; tackle/hooks.md; techniques/flyline.md; techniques/knife-jigging.md / top-5 bluefin techniques: two-rod flyl |
| F7jLrt2j2X8 | Dirty Hookers | seminar | deep | done | lures/iron-jigs.md; lures/tuna-poppers-and-stickbaits.md; tackle/rod-and-reel-selection.md; techniques/foamer-casting.md; techniques/surface-iron.md / Eric's Tackle seminar w/ Cesar: color-by-light fr |
| 48ZFXnCTTQE | Dirty Hookers | seminar | deep | done | bait/fishing-live-bait.md; rigging/essential-knots.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; techniques/flyline.md / Eric's Tackle seminar w/ Cesar: Seaguar knot, flyline sizing/bite-guar |
| U4zifdssSes | Dirty Hookers | tutorial | deep | done | rigging/assist-hooks.md; lures/knife-jigs.md / new rigging note on assist-hook sizing/cord-stiffness/tying (single top, double tail) from Cesar; cross-linked as 5th attributed hook-count/placement var |
| unARAuTgF_A | Dirty Hookers | tutorial | deep | done | rigging/assist-hooks.md; lures/knife-jigs.md / RECOVERED batch-3 Phase 1: commit 917703f was guard-reverted for "deleted 38 lines" but the diff was a net-positive restructure (167 insertions vs 40 deletions) that preserved the ASR-uncertain 215/300 lb cord weights and the Owner sponsorship caveat the escalation feared were lost. Cesar's hollow-core/swivel assist tying (pt 2); solid-ring-vs-swivel tradeoffs, PE-strength/abrasion logic, speed-vs-slow jig bite mechanism (stiff cord = hook stationary for the upswing bite; soft cord = flopping for the fall bite). Conflicts with later amendments resolved as unions; the colliding "sixth configuration" numbering renumbered (Cesar dual-top = sixth, Hansen Fish Lab = seventh) |
| EmZO8QiOfik | Dirty Hookers | tutorial | deep | done | species/cabrilla.md; lures/jerkbaits.md; lures/iron-jigs.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; techniques/yo-yo-iron.md; planning/electronics-and-sounder.md; planning/search-and-glassing.md; tackle/gear-classes.md / recovered at Gate B prep: original commit 0d33e3c was guard-reverted on the registry-backlink collision (mechanical false positive, fixed in 7f741ff); content cherry-picked intact |
| M8hOYQ_6rSg | Dirty Hookers | tutorial | deep | done | bait/making-bait.md; lures/iron-jigs.md; lures/knife-jigs.md; lures/spreader-bar.md; rigging/trap-rig.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; techniques/dropper-loop.md; techniques/knif |
| mWxyjDrcdXM | Roman Castro | tutorial | deep | done | techniques/foamer-casting.md / Added Roman Castro's bluefin-popper hookup/drag/fight doctrine (loosen drag on packed foamers, cast to edge to avoid scissoring, patience fighting 100lb+ fish, keep line |
| VpW91AKOFVQ | Roman Castro | tutorial | deep | done | lures/iron-jigs.md; rigging/essential-knots.md; tackle/rod-and-reel-selection.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / Scotty/Brothers Sportfishing surface-iron doctrine merged: assi |
| _ZThckj2TIM | Roman Castro | tutorial | deep | done | species/rockfish-lingcod.md; techniques/dropper-loop.md; techniques/rockfish-deep-dropping.md; rigging/essential-knots.md; planning/search-and-glassing.md / recovered at Gate B prep: original commit 0716a9d was guard-reverted on the registry-backlink collision (mechanical false positive, fixed in 7f741ff); Capt. Scotty weak-link dropper-loop doctrine cherry-picked intact |
| Qs9oEsh3b_w | Roman Castro | tutorial | deep | done | species/california-spiny-lobster.md; techniques/hoop-netting.md / Added Scotty's buoy/rope build (torpedo-sinker weighting, light mounting, rope-length splitting), bait-cage-by-sea-lion-pressure guida |
| sgH7MgaWD1E | Roman Castro | tutorial | skip:thin-generic | skipped | Generic hacks: fish-smell removal, zip-tie hook holder, tide-timing tip; not router-grade |
| fhv45utuKgQ | Roman Castro | on-the-water | skip:no-usable-content | skipped | Near-silent 300lb+ bluefin catch/fight footage, mostly music/yelling, no technique commentary |
| OQAZTZq-6-k | Roman Castro | on-the-water | skip:no-usable-content | skipped | Near-silent bluefin catch-fight footage, mostly music/applause, no usable commentary |
| EGKesj7V64M | Roman Castro | tutorial | deep | done | lures/bay-bass-plastics.md; species/spotted-bay-bass.md; techniques/drop-shot.md / 5 tips extracted (hookset-on-slack, swings-are-free, glue rigging tip, drag-and-pause retrieve, slack-window/current- |
| 6L8nIFeqvkw | Roman Castro | tutorial | deep | done | lures/bay-bass-plastics.md; planning/search-and-glassing.md; species/spotted-bay-bass.md; techniques/ned-rig.md / tackle combo, retrieve mechanics, bite/hookset, hook-rotation lure tip; kayak zone/spo |
| G6YRT4HNxr8 | Roman Castro | tutorial | parameter-skim | done | rigging/essential-knots.md; species/spotted-bay-bass.md; techniques/swimbaits.md / Umbrella/A-rig arm-bending, saltwater/freshwater hook-count caveat, and Palomar-over-rig knot merged as parameter-ski |
| xEqFwPJ2zFk | Roman Castro | on-the-water | skip:thin-generic | skipped | Channel recap/best-of-2018 montage; brief Baja B-roll clip, Coronado Is. mention |
| wysZwsjAkVs | Roman Castro | on-the-water | skip:thin-generic | skipped | Kayak-rental logistics/affiliate promo dominated; sponsor-heavy (Eco Boat Rentals affiliate deal) |
| HcEh5KOYTH4 | Your Saltwater Guide | on-the-water | observations-only | done | conditions/kelp-paddies.md; species/dorado.md; species/yellowtail.md / 4 Observed blocks added: pre-qualified-paddy approach behavior, October dorado persistence + technique corroboration, incidental  |
| yKaHcxX46l4 | Your Saltwater Guide | tutorial | parameter-skim | done | tackle/hooks.md; techniques/chunking.md / Squid cut-strip prep/hooking added to hooks.md; anchored chum-placement-vs-current added to chunking.md |
| q4NBPuH3gCA | Your Saltwater Guide | on-the-water | skip:duplicate-of-5FzBwvMtRP8 | skipped | confirmed: same mackerel-on-microfiber-rag recording as 5FzBwvMtRP8 (2019), ASR variance only |
| ohR9DeBOU9E | Your Saltwater Guide | tutorial | skip:thin-generic | skipped | Generic sand bass filleting demo, no conditions/decision content |
| r6j5w40fVHI | Your Saltwater Guide | tutorial | single-pull | done | species/calico-bass.md / added CA/CDFW 14in calico bass legal-size fact (dave-hansen) to Doctrine & conflicts |
| VUb7a3sP8zQ | Your Saltwater Guide | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md (new); species/calico-bass.md / RECOVERED batch-3 Phase 1. Rejected in batch 2 as "no compliant destination at parameter-skim depth (router-absorption/no new-note-creation rules)" — the content was fine, the depth contract had nowhere to put it. Under the batch-3 rule that any depth may create a note given process compliance, it gets one: Hansen's deep-hook removal through the gill opening (clear the bait first, enter through the gill rather than dragging the hook back up through the throat) plus mouth-closed/hold-don't-pull measuring. Linked from calico-bass Handling & release. The on-camera claim that a legal-size fish must be killed is logged as seen and deliberately NOT carried — a minimum size sets a floor for what may be kept, not an obligation to keep |
| ty8FtA3Y2bA | Your Saltwater Guide | tutorial | deep | done | fish-care/sculpin-handling.md: new fish-care note: thumb-in-lip unhooking technique, full spine map, bacteria/pain warning, 10in CDFW min-size regulatory claim, table quality |
| k80p1ShSvZs | Your Saltwater Guide | tutorial | parameter-skim | done | none: nothing extractable — generic twin-screw docking/seamanship, no fishing-specific content, no existing note to merge into |
| 3dVc-2rsYII | Your Saltwater Guide | tutorial | deep | done | techniques/surface-iron.md: amended with cast release point, calico slow-med retrieve, tip-down retrieve, wind-not-swing hookset (flagged conflict vs knife-jigging swing-to-set), Wounded Warrior color |
| I84uoay_jwQ | Your Saltwater Guide | tutorial | deep | done | fish-care/gaffing.md (new); linked from fish-care/tuna-care.md, fish-care/dorado-and-general.md, species/california-halibut.md — gaff sizing by species/weight, pec-shot+flip-upside-down, no-dig-hole o |
| 6X97e0AA3c8 | Your Saltwater Guide | out-of-region | skip:out-of-region | skipped | Peacock bass fishing in Florida |
| SgF5hRlEGqU | Your Saltwater Guide | tutorial | parameter-skim | done | planning/electronics-and-sounder.md; species/yellowfin-tuna.md: dolphin-pod bird-marker visual sign, manual sounder range 0-150ft parameter (vs auto-hunting bottom); trimmed duplicated explanation fro |
| pKWDxwBvTH8 | Your Saltwater Guide | tutorial | skip:thin-generic | skipped | Misleading title; mostly rant re: practice casting before trip, no cast mechanics |
| o8vLdz7OmaE | Your Saltwater Guide | seminar | deep | done | tackle/rod-and-reel-selection.md: added Dave Hansen's feel-based pull-test drag method, mid-fight re-check + thumb-as-drag warning, star-vs-lever drag mid-fight adjustability, left-hand-forward ration |
| -5kooyIyavs | Your Saltwater Guide | tutorial | deep | done | techniques/flyline.md: added Baja/Mag Bay mangrove structure-casting section (Lopez Mateos, no-weight fly-line rig, precision bait-placement doctrine, fast-current recast cycle, species landed) + Reac |
| FxgLol_IHa0 | Your Saltwater Guide | tutorial | deep | done | techniques/flyline.md: added anchor-lay-per-current-read bullet to existing Baja/Mag Bay mangrove structure-casting section (same Lopez Mateos trip as -5kooyIyavs), corroborating crew/location; soften |
| YVHdDbkQrKk | Your Saltwater Guide | tutorial | skip:duplicate-of-w5_x6kkN-xE | skipped | sweep sim 0.922, re-upload of 2021-04 live-bait video |
| JJClvPhKIdo | Your Saltwater Guide | promo | skip:promo | skipped | Promar sabiki stick-rod product demo, no technique content |
| F0g5r9Rkrd4 | Your Saltwater Guide | tutorial | parameter-skim | done | tackle/rod-and-reel-selection.md: added ready-position/index-on-spool/thumb-trigger/free-spool-to-bottom/wind-hookset section, attributed Dave Hansen, medium confidence |
| RXNebDr4j7s | Your Saltwater Guide | on-the-water | parameter-skim | done | techniques/chunking.md; species/calico-bass.md: added kelp-bed chum-then-anchor sequencing (medium confidence, Dave Hansen presenter-inferred), situations-table row + link in calico-bass; fixed gear-c |
| fri_BWI-VA0 | Your Saltwater Guide | tutorial | deep | done | conditions/moon.md; species/california-spiny-lobster.md: merged moon-phase doctrine (7-day pre/post-full-moon window, 20nm night-travel behavior, lobster no-moon timing), attributed dave-hansen, high  |
| U-dGRQ0X-Mc | Your Saltwater Guide | tutorial | parameter-skim | done | techniques/dropper-loop.md: added rockfish retrieve parameter (slow steady wind, no jerk/pump), attributed dave-hansen, high confidence per registry; trimmed an invented mechanism/gear detail not in t |
| OpA0OqRgj00 | Your Saltwater Guide | tutorial | deep | done | planning/search-and-glassing.md: added anchoring section (chain-and-rope ladder, anchor-size-by-boat, free-spool pinpoint drop), medium confidence; fixed a chain/rope doctrine inversion and doctored q |
| 9xHgdtNek1U | Your Saltwater Guide | tutorial | skip:duplicate-of-gKrYKvqHUjk | skipped | sweep sim 1.000, text-identical re-upload of 2020 fly-line rig video |
| pmfJlt2i_fo | Your Saltwater Guide | out-of-region | skip:out-of-region | skipped | Blue runner trolling explicitly Florida Keys/Bahamas |
| YvWHJ0Dgupc | Your Saltwater Guide | tutorial | skip:duplicate-of-ftEvyfwjZFU | skipped | confirmed: identical SD jam knot/bluefin tackle recording as ftEvyfwjZFU (2021) |
| L_FD-UzvEio | Your Saltwater Guide | tutorial | parameter-skim | done | bait/bait-tanks.md: amended with dave-hansen subsection on lid-off running, dead-bait toxin, tap-scoop culling, never-touch-bait; fixed a smoothed number (2.5 hours) |
| rwfjUa4zsyY | Your Saltwater Guide | on-the-water | observations-only | done | none: nothing extractable — auto-captions are near-total garbage (mostly music/applause tags), one fragment unresolvable without inventing context |
| frX09YMQxKE | Your Saltwater Guide | on-the-water | observations-only | done | techniques/flyline.md / Added third Mag Bay mangrove data point (Lopez Mateos, 2022-01-28) as an Observed block corroborating precision bait-placement doctrine; no new notes, no doctrine changed |
| 67qLBEtd3EU | Your Saltwater Guide | on-the-water | skip:duplicate-of-KTsXdQXAnkU | skipped | confirmed: identical dialogue/duration(7:07) to primary calico bass video, same recording |
| vyX5FGoDH0A | Your Saltwater Guide | on-the-water | observations-only | done | techniques/flyline.md / on-the-water observations (snook wide-open bite, grouper->spotted-bay-bass correction, hook-loss-to-brush, ravallo/rubble asr note) appended as Observed block; no doctrine crea |
| dlxA22FVNGc | Your Saltwater Guide | tutorial | deep | done | techniques/flyline.md / added tide-phase bite-timing, stealth hook/leader spec, reel-style flexibility, no-weight rationale, anchor-vs-drift doctrine, and an Observed multi-species block |
| 5nTGoZ9_nzU | Your Saltwater Guide | non-fishing | skip:no-usable-content | skipped | Entire transcript is garbled nonsensical ASR (song lyrics), no recoverable fishing content |
| Dq1x__MI8Wk | Your Saltwater Guide | non-fishing | skip:not-fishing | skipped | Pure marlin filleting/cooking demo, no catch footage or location |
| BmENEt6gYm8 | Your Saltwater Guide | non-fishing | skip:not-fishing | skipped | Pure wahoo filleting/cooking demo, no catch footage or location |
| ZggReeO1nyU | Your Saltwater Guide | tutorial | deep | done | bait/fishing-live-bait.md / Amended sardine nose/butt-hook mechanics and added anchovy nose-vs-gill-hook subsection, attributed to dave-hansen at high confidence |
| 7WapaxdtjQg | Your Saltwater Guide | tutorial | parameter-skim | done | bait/bait-tanks.md; bait/making-bait.md / Dana Point bait-barge etiquette/VHF-11/timing folded into making-bait.md; tank-load judgment factors folded into bait-tanks.md; one faithfulness fix applied |
| Pv5JMTTY4nI | Your Saltwater Guide | tutorial | skip:duplicate-of-9qnQjPPT5yg | skipped | sweep sim 0.946, re-upload of 2021-05 PTO grip video (primary itself triaged skip:promo) |
| ur1F8gD1sF4 | Your Saltwater Guide | promo | skip:promo | skipped | Subscription-pitch-dominated; scattered tips (breeze-reading, avoid combat fishing) buried in rant |
| vJ70gNV72eY | Your Saltwater Guide | promo | skip:promo | skipped | Mostly generic date-day advice + subscription pitch; thin bait-tank-shape/fly-lining nugget |
| VsUUBICiBzQ | Your Saltwater Guide | tutorial | parameter-skim | done | rigging/essential-knots.md / Improved-clinch (fisherman's knot) tying procedure merged: 7-wrap single-pass mechanic, retie-after-nearly-every-fish cadence (bluefin/calico/barracuda), attributed dave-h |
| qihSsdqBU2A | Your Saltwater Guide | non-fishing | skip:no-usable-content | skipped | Entire transcript garbled nonsensical ASR, no recoverable content (light-line theory unrecoverable) |
| 44pjBUn0nP8 | Your Saltwater Guide | on-the-water | skip:duplicate-of-wYeKJLoKo4g | skipped | confirmed: identical dialogue/duration(1:44) to primary yummy-flyer breezer clip |
| zVIfArUrpDI | Your Saltwater Guide | tutorial | deep | done | rigging/essential-knots.md; tackle/hooks.md; tackle/line-and-leader.md; techniques/dropper-loop.md; techniques/rockfish-deep-dropping.md / San Diego jam update, rockfish circle-hook rationale, braid-v |
| CrLDC4O8qS8 | Your Saltwater Guide | on-the-water | observations-only | done | conditions/kelp-paddies.md; species/dorado.md; species/yellowtail.md / on-the-water observations: loaded-paddy heuristic, dorado confirmation, incidental yellowtail; no doctrine changed, no new notes |
| 8jC61LzQoxU | Your Saltwater Guide | tutorial | deep | done | techniques/fighting-big-bluefin.md (new); fish-care/gaffing.md; fish-care/tuna-care.md; species/bluefin-tuna.md / new technique note: fight mechanics (gear-tap, down-swell walk, death-circle avoidance |
| bsbL7JeKxMo | Your Saltwater Guide | tutorial | skip:duplicate-of-8jC61LzQoxU | skipped | confirmed: identical script/duration(5:53) to primary fight-giant-bluefin video |
| ftEvyfwjZFU | Your Saltwater Guide | tutorial | deep | done | rigging/essential-knots.md; species/bluefin-tuna.md; techniques/flyline.md; lures/tuna-poppers-and-stickbaits.md; lures/soft-plastic-swimbaits.md / recovered at Gate B prep: original commit ed1860a was guard-reverted on the registry-backlink collision (mechanical false positive, fixed in 7f741ff); Hansen San Diego jam / bluefin tackle content cherry-picked intact |
| RbqOKkINSCM | Your Saltwater Guide | tutorial | deep | done | lures/knife-jigs.md; rigging/essential-knots.md; species/bluefin-tuna.md; tackle/hooks.md; techniques/flyline.md / Fly-line rig (San Diego jam), flat-fall/popper multi-rod pre-rig, circle-hook rationa |
| 9qnQjPPT5yg | Your Saltwater Guide | promo | skip:promo | skipped | Product demo for patented PTO fighting-grip (22-degree angle mechanics); inventory/sales-pitch dominated |
| scmPq63lLWM | Your Saltwater Guide | tutorial | parameter-skim | done | lures/knife-jigs.md; techniques/knife-jigging.md / Fishlab flat-fall red-crab color/hook-rig doctrine added, attributed dave-hansen; no San Diego jam knot content found despite triage note, correctly  |
| IMnoZVEYpm4 | Your Saltwater Guide | tutorial | single-pull | done | tackle/hooks.md / added Dave Hansen bronze/black-vs-nickel/chrome hook-finish doctrine (stealth + corrosion), scoped to bait fishing; duplicate content vs m2q22sPPkEM correctly excluded |
| f4qYtHACGyk | Your Saltwater Guide | tutorial | deep | done | techniques/chunking.md / added artificial-reef prey-density/feeding-frenzy mechanism (confidence bumped to high), light-line finesse rig (straight-tied hook, current-sized shot 1/16-1/4 oz, strip-bait |
| NC3-3pJDEgo | Your Saltwater Guide | tutorial | deep | done | conditions/sea-state.md / added dave-hansen go/no-go wind & swell thresholds (12kt cutoff, <10s interval, unfishable combo), Santa Ana mechanics + Catalina return-trip-risk subsection, both medium con |
| FEXgl0eQCa8 | Your Saltwater Guide | tutorial | deep | done | planning/electronics-and-sounder.md: Added Dave Hansen mid-screen manual-range sizing and harbor-first hard/soft-bottom practice doctrine; upgraded manual-vs-auto rule to high confidence |
| 1hJoxwg9fy4 | Your Saltwater Guide | on-the-water | observations-only | done | none: on-the-water WSB fight footage, no extractable doctrine beyond generic tip-up/avoid-kelp technique already covered elsewhere; correctly skipped |
| fK2AT460xW4 | Your Saltwater Guide | tutorial | deep | done | rigging/essential-knots.md; rigging/rubber-band-deep-rig.md; species/yellowfin-tuna.md: Added Dave Hansen's inline torpedo-sinker/San Diego jam/circle-hook drop rig for yellowfin under dolphin pods, c |
| HOYJ6TAMrg4 | Your Saltwater Guide | promo | skip:promo | skipped | PTO Fighting Grip product demo w/ marlin+sailfish action footage; sponsor-heavy; feeds dave-hansen registry |
| 6DzbsElGE7E | Your Saltwater Guide | tutorial | deep | done | planning/electronics-and-sounder.md; planning/search-and-glassing.md; species/yellowtail.md: added brand-agnostic bottom-hardness read, pass-and-grade/sand-anchor method, and yellowtail hard-bottom-on |
| w5_x6kkN-xE | Your Saltwater Guide | tutorial | deep | done | bait/fishing-live-bait.md; techniques/flyline.md; techniques/kite-fishing.md: Added mackerel hook-position doctrine (butt/nose/back by weight and kite use), bait-size/species-selectivity note, and fly |
| _aimmQmzqz0 | Your Saltwater Guide | promo | skip:promo | skipped | PTO Fighting Grip product intro/specs/sizing; sponsor-heavy, same product as HOYJ6TAMrg4 |
| OIqdmhKfuOc | Your Saltwater Guide | tutorial | deep | done | techniques/dropper-loop.md; tackle/rod-and-reel-selection.md: Added dropper-loop deploy procedure (drop-not-cast, nose-hook, index/thumb grip, bottom detection, bite read, two-crank lift-set, tail-cli |
| KLoEJInlmZo | Your Saltwater Guide | tutorial | deep | done | lures/iron-jigs.md; techniques/surface-iron.md: Added surface-iron cast/retrieve/hookset mechanics (reel-on-side cast, line guiding, dog-boning hookset) and Wounded Warrior (Tady 45) color/model detai |
| wzI0lpgKT1U | Your Saltwater Guide | tutorial | deep | done | techniques/yo-yo-iron.md: Added Dave Hansen's crank-and-drop yo-yo cadence (10-crank cast-and-retrieve; 5-6-crank straight up-and-down with depth bands; bite-on-the-drop) as attributed conflict beside |
| kr-DZP7OVmg | Your Saltwater Guide | tutorial | skip:duplicate-of-4xzK7YaXK5s | skipped | same recording as BD id already extracted in batch 1 (sweep sim 0.814) |
| e5qGRAzwEWQ | Your Saltwater Guide | promo | skip:promo | skipped | Subscription pitch for yoursaltwaterguide.com throughout; no standalone technique content |
| BdRX4b8Fo5w | Your Saltwater Guide | tutorial | parameter-skim | done | bait/bait-tanks.md; bait/fishing-live-bait.md; techniques/chunking.md: Added bait tank placement/shape, bait-changing cadence claim (medium confidence), and generalized prey-density mechanism beyond a |
| dgauGbNxP84 | Your Saltwater Guide | on-the-water | parameter-skim | done | conditions/current-diagnostics.md; species/skipjack-tuna.md; techniques/trolling.md: Added Observed current-break visual-ID and troll-it-back-and-forth execution (Cabo San Lucas, Baja), fixed Dave Han |
| ll7r4A6atno | Your Saltwater Guide | tutorial | parameter-skim | done | techniques/trolling.md; species/dorado.md; rigging/haywire-twist.md: Added Cabo surf-line sierra-trolling section (hoochie, wire leader, 6kt troll, AM/sunset bite, dirty-water cue), Observed cross-lin |
| OSbAHdB4uPs | Your Saltwater Guide | tutorial | deep | done | species/sheephead.md; tackle/hooks.md; techniques/sliding-sinker.md: New sheephead species router (hook/weight/bait table) plus corroborating entries in hooks.md and sliding-sinker.md; fixed over-attr |
| EiItVWqFMYc | Your Saltwater Guide | tutorial | parameter-skim | done | techniques/hoop-netting.md: Added soak/pull cadence (drop ~1hr before dark, first pull ~30min after sunset, reset-on-same-spot) and a sublegal-lobster handling judgment call, flagged for regulatory re |
| 2y0VznL2qk8 | Your Saltwater Guide | tutorial | deep | done | rigging/flying-fish-harness.md; species/bluefin-trolling.md; techniques/kite-fishing.md: Added wind-driven rubber-flyer-trolled-8.5kt vs dead-flyer-under-kite/balloon decision with deployment/hookset  |
| gKrYKvqHUjk | Your Saltwater Guide | tutorial | deep | done | techniques/flyline.md; tackle/rod-and-reel-selection.md: Merged fly-line rig doctrine (species-bait pairings, line-weight-to-bait matching, distance-over-weight, cast-control-brake mechanism) into exi |
| Rf1HKJG-SDg | Your Saltwater Guide | tutorial | deep | done | locations/zone-lexicon.md; planning/electronics-and-sounder.md; species/bluefin-tuna.md; species/rockfish-lingcod.md / added bank fathom-depth naming convention + fathometer terminology and cross-link |
| YPhc0zr7oBs | Your Saltwater Guide | seminar | skip:duplicate-of-aFb221LUoD0 | skipped | triage-confirmed: near-verbatim same swell/current/water-color seminar, shorter cut; longer cut is the primary |
| ShSxNKAcUB4 | Your Saltwater Guide | tutorial | deep | done | species/white-seabass.md; techniques/dropper-loop.md; techniques/sliding-sinker.md / WSB sliding-sinker weight ladder, thin-wire hook, and suspend-and-retrieve technique added with router row and drop |
| cEscIy278ew | Your Saltwater Guide | tutorial | deep | done | techniques/hoop-netting.md / added dave-hansen boat-approach/prop-safety subsection (stern-first, spotlight/rope-lay check, dual-spotlight habit, bump-forward clear) plus common-failures rows and date |
| aFb221LUoD0 | Your Saltwater Guide | seminar | deep | done | conditions/current-diagnostics.md; locations/island-structure.md / added Catalina swell/wind zone-selection doctrine (west-swell to east-end, south-swell tears up east end), named-spot wind fit (Fredd |
| 7HApvxvtxgo | Your Saltwater Guide | tutorial | skip:thin-generic | skipped | Generic sport-boat etiquette advice, no fishing-technique content |
| CjQD4vJmsog | Your Saltwater Guide | promo | skip:promo | skipped | Pure subscription pitch for yoursaltwaterguide.com, 1:23 runtime, no technique content |
| 89DmEDR-1sI | Your Saltwater Guide | on-the-water | skip:duplicate-of-6zYRI1ZQU3c | skipped | confirmed: same San Diego tuna chum footage as 6zYRI1ZQU3c, ASR/caption variance only |
| 6zYRI1ZQU3c | Your Saltwater Guide | on-the-water | observations-only | done | species/yellowfin-tuna.md / added dated Observed block (chum-triggered free-swimmer frenzy at boat, San Diego) under yellowfin sonar-signature/chum-rise doctrine |
| pX6mV3O0L_E | Your Saltwater Guide | on-the-water | observations-only | done | species/dorado.md / added Observed block (dead-ballyhoo troll, multiple dorado hookups, Cabo San Lucas Nov 2019) |
| HeMNAw6MDVE | Your Saltwater Guide | non-fishing | skip:not-fishing | skipped | Cabo marina walkthrough: restaurants/hotels/beach tourism, only trivial fishing-license mention; not fishing content |
| qv0QbLgp72o | Your Saltwater Guide | on-the-water | single-pull | done | techniques/chunking.md / added bait-size/prey-density reaction-bite nuance (tuna+calico, medium confidence) to prey-density mechanism section |
| CLkO0QUwb_c | Your Saltwater Guide | tutorial | skip:thin-generic | skipped | Generic kids-fishing advice (calm day, small bait, dont go offshore); one Dana Point red-buoy mackerel mention |
| YQsbwfQ4wzY | Your Saltwater Guide | tutorial | parameter-skim | done | species/california-spiny-lobster.md; techniques/hoop-netting.md / added bait freshness/quantity notes, DIY 2in x18in PVC bait-tube spec (sea-lion evasion), Catalina 20-30ft depth note, LB/SD post-rain |
| mdhoEQPqpng | Your Saltwater Guide | on-the-water | single-pull | done | techniques/fighting-big-bluefin.md; species/yellowtail.md / added observed sea-lion depredation free-spool counter-move as cross-species fight-stage section, linked from yellowtail router situations t |
| 8Asmd2H56Qk | Your Saltwater Guide | tutorial | skip:duplicate-of-sYrsPGXiYhI | skipped | same recording as BD rubber-band-rig video per analysis doc (sim 0.518, ASR variance) |
| TLEhULOWj7g | Your Saltwater Guide | on-the-water | skip:no-usable-content | skipped | Facebook-live hookup chaos/shouting, no location or conditions detail, no doctrine |
| xI9tPJFXbUM | Your Saltwater Guide | tutorial | deep | done | techniques/chunking.md; planning/search-and-glassing.md; conditions/current-structure.md / chum-bucket bow-not-stern rig (repeated doctrine, high), anchor-in-front-of-rock (repeated doctrine, high), w |
| 9hEa3sGTh40 | Your Saltwater Guide | tutorial | deep | done | bait/bait-tanks.md; planning/electronics-and-sounder.md; planning/fleet-intelligence.md (new); planning/day-plan-protocol.md; planning/search-and-glassing.md / new fleet-intelligence.md (VHF ch72/65 d |
| zwNEhWtnBCE | Your Saltwater Guide | on-the-water | observations-only | done | techniques/chunking.md / added earliest-dated (2019-07-31) kelp-stringer chumming Observed block, fixed front-matter source and de-conflated promo narration from the observed moment |
| 5FzBwvMtRP8 | Your Saltwater Guide | tutorial | single-pull | done | bait/making-bait.md / added microfiber-rag mackerel-jig method and no-hands/butter-knife bait-tank handling rule, medium confidence |
| AZ7N_nRmLnc | Your Saltwater Guide | on-the-water | skip:no-usable-content | skipped | Mislabeled tutorial; just wide-open dorado bite shouting, no fishfinder-reading content despite title |
| poqjnb1r1zk | Your Saltwater Guide | on-the-water | parameter-skim | done | species/bonito.md / added Observed block (5:45am Dana Point start, slow-then-improving morning, small-feather daisy-chain trolled ~5.5kt, Rapala-class hard-bait cast/twitch follow-up); reverted extrac |
| KCcEqHSZ84k | Your Saltwater Guide | on-the-water | parameter-skim | done | techniques/chunking.md / added Dave Hansen's shallow-rock calico fight technique (rod tip high, no pumping, 65lb braid/30lb fluoro top shot, Northwest Harbor SCI ~6ft), contrasted with calico-bass.md' |
| KTsXdQXAnkU | Your Saltwater Guide | on-the-water | parameter-skim | done | species/calico-bass.md; techniques/swimbaits.md / on-the-water parameter-skim of pitch-and-sink jig parameters, grind-don't-pump fighting technique, and lip-grab/foam-rinse release, folded into existi |
| ZFqe49jRgA0 | Your Saltwater Guide | tutorial | deep | done | conditions/kelp-paddies.md; planning/fleet-intelligence.md; species/dorado.md; species/yellowtail.md / tutorial/deep extraction — paddy-approach discipline (drive straight up, no sneaking), 90-120ft b |
| eNcltRh-shc | Your Saltwater Guide | on-the-water | observations-only | done | techniques/chunking.md / Observed block appended to existing Fighting-the-fish-out-of-shallow-rock section (Dave Hansen/Your Saltwater Guide) confirming rod-tip-high fight technique at a second Northw |
| _KldpqPPT1c | Your Saltwater Guide | on-the-water | observations-only | done | species/calico-bass.md / Added Observed block (anchored outside Cat Harbor, steady not-wide-open bass bite, fish running into kelp) to calico-bass doctrine section; fixed missing front-matter source |
| HGyL7pXy3Ts | Your Saltwater Guide | tutorial | deep | done | planning/electronics-and-sounder.md; planning/search-and-glassing.md / Added live fathom-conversion worked example + bottom-return-during-backing note to electronics-and-sounder.md; added chain/rope-s |
| 6ueGWJek1gI | Your Saltwater Guide | tutorial | parameter-skim | done | bait/bait-tanks.md; bait/fishing-live-bait.md / merged Capt. Dave Hansen's tank-to-hook workflow (rod on rail, net not hands, get bait back in water fast) and corroborated the existing green-over-silv |
| lF6jQklDCrY | Your Saltwater Guide | tutorial | single-pull | done | species/rockfish-lingcod.md / added caveated historical regs example (March 1 reopen; 300->350->460 ft depth progression, self-admitted uncertain reading) to Doctrine & conflicts |
| kzD0kSnnVPw | Your Saltwater Guide | tutorial | single-pull | done | conditions/current-structure.md / Kelp/rock corner-selection-by-current-direction doctrine (Dave Hansen, medium confidence) added as new subsection to existing current-structure note |
| EE0P4SvcNFg | Your Saltwater Guide | tutorial | single-pull | done | tackle/hooks.md / corroborated existing cut-squid-strips doctrine (thin strips not chunks) from a second Your Saltwater Guide video, bumping confidence medium to high per repeated-doctrine rubric |
| e16i7zKq1FY | Your Saltwater Guide | tutorial | single-pull | done | techniques/chunking.md / merged drift-chumming downhill/lee-corner rule (stern-first drift, chum off wind/lines-matching corner) into existing chunking note, single-pull depth respected, no new note c |
| wYeKJLoKo4g | Your Saltwater Guide | on-the-water | single-pull | done | techniques/kite-fishing.md / Added Observed block (slow approach on a gone-quiet breezer, Yummy rubber flyer under a balloon, misses then hookup); trimmed extractor's overreaching cross-video resolves |
| jahddqzKhLY | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md / added Bimini-twist quick-tie parameters + When-to-use entry to existing knots note (no new note, matching parameter-skim depth) / flags: asr-uncertain(final locking-wrap c |
| eEcRPEoG4DQ | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md; techniques/dropper-loop.md / Surgeon's-knot single-hook rockfish dropper loop amended into essential-knots.md and dropper-loop.md (leader length <=2.5 ft, 6 oz sinker on a  |
| YZT-_SdmQNs | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tube-bait flip/pitch rig near trees/weeds mimicking crawdad - reads as freshwater bass technique |
| IB3IqZKxEhk | StokedOnFishing | promo | skip:promo | skipped | Simrad rep (Tito Perez) demos chartplotter bridge-control feature; no fishing content, sponsor-heavy |
| ILoJ_fzV4fY | StokedOnFishing | promo | skip:promo | skipped | Simrad rep demos Go Free WiFi app/box incl. pricing; no fishing content, sponsor-heavy |
| 06lxuie5cZQ | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md / added a second, distinct mono-to-fluoro connection knot + tag-trim/tag-loop judgment to the Seaguar-knot entry, medium confidence, unregistered channel / flags: asr-uncert |
| Jvv6DMNIHbE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | CA lake threadfin-shad/striper bass fishing, freshwater; series: Bass Fishing Live Shad part 1 |
| 6-mi3Qxn37c | StokedOnFishing | on-the-water | observations-only | done | species/spotted-bay-bass.md; techniques/swimbaits.md / Added tide-preference Observed block to spotted-bay-bass.md and a detailed Alabama-rig gear/presentation Observed block to swimbaits.md (unregist |
| 2gHRrR3D8rY | StokedOnFishing | tutorial | parameter-skim | done | fish-care/dorado-and-general.md: halibut filleting storage/icing parameters merged as attributed source; spine-follow/skin-removal mechanics skipped as generic |
| rJ-Omw4Ob74 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Halibut rig setup explicitly filmed in Alaska |
| wALN3RpsSxU | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Anchor-retrieval buoy hack explicitly filmed in Alaska |
| H-vIGWPIPVc | StokedOnFishing | on-the-water | parameter-skim | done | fish-care/tuna-care.md; species/bonito.md; species/yellowfin-tuna.md: on-the-water observations added (gill-bleed mechanism, bonito table-quality vs yellowfin, SCI dolphin-pod troll-to-60lb-yellowfin) |
| KPzJuwh6kbo | StokedOnFishing | non-fishing | skip:not-fishing | skipped | Pure tuna-steak marinade/cook recipe, no catch footage, sponsor-heavy intro |
| z85Fy52itS8 | StokedOnFishing | non-fishing | skip:not-fishing | skipped | Pure rockfish ceviche recipe; fish caught in Alaska (mentioned only), no catch footage |
| tzeXXPAjqUY | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md: added third StokedOnFishing mono-to-fluoro tie explicitly named 'Seaguar knot', flagged as mechanically distinct from already-logged Cesar-sourced Seaguar knot (conflict ke |
| 1BH7nQdIg5Q | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md: added second independent San Diego jam corroboration (15in tag length, 6-wrap count); extraction-log row updated to done |
| NkjjDf6XPcE | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md: uni-to-uni wrap-count variant (3-4 turns) + mono-to-fluoro application added, medium confidence |
| AT6zmDYxjW4 | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md: RP knot corroboration added (naming variants, 12in tag length, 6-up/6-down wrap count, double-pass cinch) |
| NLDKbLw2q-E | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Lake Cachuma freshwater bass camping trip; series: Lake Cachuma part 2 |
| _0xZV0PojhE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Lake Cachuma freshwater bass camping trip; series: Lake Cachuma part 1 |
| Y2bXn44lfqo | StokedOnFishing | on-the-water | parameter-skim | done | bait/fishing-live-bait.md; conditions/tide-and-slack.md; rigging/leadhead-mods.md; species/white-seabass.md; techniques/dropper-loop.md: WSB broodstock-trip parameters merged (squid handling, 4am slac |
| 82gEHYel-4U | StokedOnFishing | on-the-water | parameter-skim | done | species/white-seabass.md: milky-water uphill/downhill spot-check method + reconciled HSWRI/Newport hatchery program history merged into existing broodstock context, medium confidence |
| ldVj0BoB-kE | StokedOnFishing | report | deep | done | species/calico-bass.md: added Baja regional note on Cedros Island operator-driven 100% catch-and-release for calico/grouper/black seabass (2023-10-16), medium confidence, region-labeled vs CDFW SoCal  |
| ntQXxcH5sjI | StokedOnFishing | tutorial | deep | done | species/bluefin-tuna.md; techniques/surface-iron.md; techniques/yo-yo-iron.md: bluefin router gained shallow-mark/yo-yo row + Tanner Bank Observed block, surface-iron sink-it-out tip, yo-yo-iron reach |
| FE63WNlwkKw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Legg Lake/Whittier Narrows freshwater tournament; not saltwater despite LA/SoCal location |
| 3S3Tx-Me2HY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clear Lake NorCal freshwater LiveScope bass fishing; title-trap, not SoCal saltwater |
| c-LLt6fG2n0 | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Clear Lake bass w/ Garmin LiveScope; freshwater excluded despite CA location |
| af51LVG_5SE | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Clear Lake winter bass fishing w/ LiveScope guide; out of region |
| rI4P4PrOsPo | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Clear Lake bass/catfish/crappie trip; out of region |
| SHFrJzWZP-g | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Legg Lake (LA) bass/bluegill/crappie tourney; freshwater excluded despite SoCal loc |
| k4LCL9ALryA | StokedOnFishing | on-the-water | observations-only | done | lures/bay-bass-plastics.md; species/spotted-bay-bass.md; techniques/inshore-crankbaits.md: added 3 Observed blocks (18-20ft/shad-pattern depth-bait observation, 25+ fish crankbait day) after correctin |
| wJl8SZhmaWg | StokedOnFishing | promo | skip:promo | skipped | SWBA tournament sizzle/testimonial reel, no instruction; promo |
| EU_Dod4wfYw | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md: added Observed block (wide-open kelp bite at Santa Barbara Island, 4.5-5lb fish, more-kelp-on-prior-visit remark), contrasted beside existing not-wide-open Cat Harbor observati |
| AxLlx2Ug-rs | StokedOnFishing | on-the-water | parameter-skim | done | locations/bays-and-harbors.md: added Observed block (fish hold tight to pilings, cast close to ambush), species-unspecified caveat; mis-scoped specific-model tackle paragraph dropped as out of locatio |
| YijeuGOYoVQ | StokedOnFishing | on-the-water | observations-only | done | none: nothing extractable, sponsor-heavy East Cape Baja footage with no existing anchor notes (no wahoo/roosterfish species notes, no matching lure notes); ambiguous ASR marlin ID left unattached rath |
| mL4Ph7t0WcQ | StokedOnFishing | on-the-water | observations-only | done | species/pacific-crevalle-jack.md; tackle/hooks.md; techniques/flyline.md: added three Observed blocks (Lighthouse Point mixed-species presence, circle-hook surf-cast roosterfish/tuna 10-count timing,  |
| _Wb4z4ammoM | StokedOnFishing | on-the-water | parameter-skim | done | tackle/line-and-leader.md: Gonzaga Bay wire-leader/65lb-spectra parameter for cabrilla/barred pargo, medium confidence |
| A6s-A1NARuA | StokedOnFishing | on-the-water | parameter-skim | done | tackle/line-and-leader.md; tackle/rod-and-reel-selection.md: Gonzaga Bay pt2 grouper deep-drop + casting gear rundown |
| 9xNhdu2aBqE | StokedOnFishing | on-the-water | parameter-skim | done | lures/soft-plastic-swimbaits.md; species/calico-bass.md; techniques/swimbaits.md: MC9 swimbait, follow-up-eat behavior, line class, water color |
| ROWgdFE9Ehc | StokedOnFishing | on-the-water | observations-only | done | techniques/flyline.md: Observed block, slow-trolled nose-hooked sardine 150-200ft, yellowtail, the channel |
| epWXURDU-oI | StokedOnFishing | on-the-water | skip:duplicate-of-9xNhdu2aBqE | skipped | Same trip/dialogue as 9xNhdu2aBqE (Todd Klein, SCI), short highlight cut - NEW dedup finding at triage |
| _C8w6zeVPak | StokedOnFishing | on-the-water | observations-only | done | lures/soft-plastic-swimbaits.md; species/calico-bass.md; species/yellowtail.md; techniques/flyline.md; techniques/surface-iron.md; techniques/trolling.md: 6 Observed blocks, Cedros/Gono skiff trip |
| BvT560Nblqo | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; techniques/trolling.md; techniques/yo-yo-iron.md: Observed blocks, Cedros ridge/chum/yo-yo iron, trolled yellowtail |
| NGxyOlPx3ug | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; techniques/surface-iron.md: Observed blocks, Cedros/Gonzo skiff calico grade, surface-iron fall-bite at anchor |
| Qa-j6LIwa1Q | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/california-halibut.md; techniques/yo-yo-iron.md: Observed blocks, Cedros high-volume calico bite, 41lb halibut on swimbait, calico on yo-yo iron |
| XwwIvPFxRiQ | StokedOnFishing | on-the-water | observations-only | done | lures/soft-plastic-swimbaits.md; species/calico-bass.md; species/yellowtail.md; techniques/fighting-big-bluefin.md; techniques/yo-yo-iron.md: Observed blocks, Cedros day2 catch montage |
| 3SATCeA3KaU | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/yellowtail.md: Observed blocks, Geronimo/Chester's Rock calico->yellowtail brawl, first-light birds push, plug bite |
| _r_qKX_7080 | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/yellowtail.md; techniques/swimbaits.md: Observed blocks, Chester's Rock weedless swimbait calico/yellowtail, TR car keel hook, Dono stop split out |
| L3tkGVu516A | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/yellowtail.md; techniques/swimbaits.md: Observed blocks, Dono/Sacramento Reef big-calico stop, spooled yellowtail, slow retrieve, kelp-fouled-hook release |
| IATPg9110CE | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; techniques/swimbaits.md: Observed blocks, SBI tournament win kelp/rock, slow-roll retrieve, rod length tradeoff |
| PKf7G3uL4io | StokedOnFishing | on-the-water | observations-only | done | locations/island-structure.md; lures/soft-plastic-swimbaits.md; species/calico-bass.md; tackle/line-and-leader.md; techniques/swimbaits.md: 5 Observed blocks, Catalina West End wind retreat, stealth a |
| iQLyBzhOSi8 | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; techniques/swimbaits.md: Observed blocks, SCI Northwest Harbor tournament conditions, swimbait cadence; fixed inherited 2014-dating vs on-camera 2012 slate |
| 2ivn-N0as_A | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SWBA night tourney weigh-in/catch montage, no conditions detail; series: SWBA Midnight Standoff part 3 |
| 8KIsYpsIBwI | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Southwest Florida beach shark tournament; series: Giant Shark Florida part 2 |
| _Ejay_B77DA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Southwest Florida beach shark tournament; series: Giant Shark Florida part 1 |
| P6Slg6RQiXw | StokedOnFishing | on-the-water | deep | done | species/calico-bass.md; techniques/swimbaits.md; tackle/rod-and-reel-selection.md / SCI on-the-water trip (Aaron Martens/Capt. Benny Florentino) — kelp-canopy flipping technique + situations-table row |
| vwH9ERf6zPI | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Long Beach Yacht Club SWBA/Olive Crest charity tourney catch footage, no conditions detail |
| M6U_FVdosr4 | StokedOnFishing | on-the-water | parameter-skim | done | species/calico-bass.md / added dated Observed block (unregistered channel, medium confidence): AM squid-vs-sardine tally (5 sand bass + 3 calico, all on squid) + anchor-on-light-current decision in Da |
| x1Vb7c4Ek-U | StokedOnFishing | promo | skip:promo | skipped | Stoked On Fishing show trailer announcing Fox Sports West premiere, sizzle reel only |
| NQsVlcpNfck | StokedOnFishing | promo | skip:promo | skipped | Shogun Sportfishing skiff-trip promo, Catalina kelp/skiff catch footage but ad for booking charter |
| pd1VOJbTEEM | StokedOnFishing | report | skip:thin-generic | skipped | Long Beach Yacht Club charity-venue talk for Olive Crest event, zero fishing footage |
| N1YBY1i600U | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SWBA California Offshore Challenge (Catalina/SCI) tourney hype+catch footage, no conditions detail |
| mXu8vJ8yr4Q | StokedOnFishing | on-the-water | single-pull | done | lures/soft-plastic-swimbaits.md / Observed block added to the weedless-rigged slug bullet: weedless swimbait held up through repeated kelp-boiler passes across a 4th/5th same-week trip on the same lea |
| xIUKmH9ccgQ | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/california-halibut.md; species/yellowtail.md / observations-only Cedros catch-montage footage added as three attributed Observed blocks (calico/mixed bite, incidental h |
| IFhBVRoc4VQ | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SWBA/Sanderson Farms Shelf Bass Special weigh-in/catch footage, no conditions detail |
| fjMHM1V9iPc | StokedOnFishing | report | skip:thin-generic | skipped | Bass-stravaganza vendor/seminar-day recap interviews on standings/sponsors, no technique captured |
| FurifnQ27mM | StokedOnFishing | on-the-water | single-pull | done | lures/bay-bass-plastics.md / added Observed block (shrimp-pattern lure worked, SWBA Border Town Brawl tournament day) + fixed missing front-matter source id |
| wdbqTio1SQU | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md / Cedros/North Point Observed block added (spot name + grade, surface-iron opening catch, yo-yo iron catch); one overclaimed species identity corrected during review |
| RPSRH0jwyw4 | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; species/calico-bass.md; fish-care/gaffing.md / on-the-water Observed blocks added for Cedros West End calico bite, front-side home-guard yellowtail bendo bite, and a missed-gaff |
| yuXr3IJ8ybg | StokedOnFishing | on-the-water | observations-only | done | bait/fishing-live-bait.md; species/bonito.md; species/yellowtail.md / on-the-water observations added: squid-grip corroboration, bonita-as-life-indicator + mid-fight species-tell caveat, SCI mixed-bit |
| Turj5ZKNcuE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Kingdom of Tonga travel/lifestyle episode; series: Stoked On Tonga part 1 |
| sJCoSQpanU4 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tonga kiteboarding/kayak reef episode; series: Stoked On Tonga part 2 |
| xHT7oJGRQyk | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tonga vanilla factory/cave-swim wrap-up episode; series: Stoked On Tonga part 4 |
| U60jPPBu5CM | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Save The Brave veteran-charity trip, golf + brief rockfish catch reactions, region unclear/Baja island |
| qri15R3caYE | StokedOnFishing | on-the-water | observations-only | done | species/barracuda.md; species/bonito.md; species/calico-bass.md; species/yellowtail.md / 4 Observed blocks added for the La Bocana, Baja co-op trip (mixed-bag species list, calico grading 5-9 lb, miss |
| Cobp85UvHmM | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/spotted-bay-bass.md; species/yellowtail.md; techniques/trolling.md / on-the-water observations added across 4 existing notes (La Bocana part 2: offshore troll/dorado fire-dr |
| tcso7Lpm_Xs | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/skipjack-tuna.md; techniques/trolling.md / Observed blocks added for Buena Vista Beach Resort/East Cape offshore troll (dorado/skipjack counts, wahoo count, unconfirmed marl |
| 3yK3JYrKoZY | StokedOnFishing | on-the-water | parameter-skim | done | species/calico-bass.md; techniques/yo-yo-iron.md / on-the-water/parameter-skim extraction of West End Cedros calico bite (corroborating RPSRH0jwyw4) and a lazy-boy/clicker yo-yo cadence variant; fixed |
| d0yGBQDeY_4 | StokedOnFishing | on-the-water | parameter-skim | done | planning/electronics-and-sounder.md; species/yellowtail.md; techniques/fighting-big-bluefin.md; techniques/sliding-sinker.md / on-the-water/parameter-skim: Cedros fog-radar-nav fact, bait-ball approac |
| 84XPJAeH0Rw | StokedOnFishing | on-the-water | observations-only | done | species/pacific-crevalle-jack.md; techniques/fighting-big-bluefin.md; techniques/flyline.md; techniques/foamer-casting.md / on-the-water observations added: jack crevalle catch-mix presence at East Ca |
| GptrotE0x5M | StokedOnFishing | on-the-water | observations-only | done | species/yellowfin-tuna.md; techniques/fighting-big-bluefin.md; techniques/flyline.md / Fiesta weigh-in grade data point + two hand-fought fight observations + squid-chum/circle-hook-mandatory observat |
| _c6UI3lGBVg | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowfin-tuna.md; techniques/fighting-big-bluefin.md / East Cape observations (distance/depth, grade, hand-off coaching, small-vs-circle-hook) appended to existing Observed blocks; front-matt |
| 6j7V34GYzzw | StokedOnFishing | on-the-water | observations-only | done | techniques/trolling.md / on-the-water observations (East Cape panga rooster session + unconfirmed offshore gamefish fight) merged into trolling.md; speculative striped-marlin identification rejected a |
| ecJPMTCi-gw | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowtail.md; techniques/yo-yo-iron.md / on-the-water/parameter-skim Observed additions (seal-worked drift, surface-iron/yo-yo alternation, unexplained yo-yo downsize bite, ASR-uncertain 'tat |
| CuK0_9v1F_o | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus) halibut fishing |
| tJFSV3AcIdE | StokedOnFishing | on-the-water | parameter-skim | done | species/calico-bass.md; tackle/rod-and-reel-selection.md; techniques/swimbaits.md / on-the-water/parameter-skim extraction: leading-edge kelp observation, calico grub/casting gear specs, and a followe |
| 7aF6uWVw76g | StokedOnFishing | on-the-water | single-pull | done | species/striped-marlin.md / on-the-water/single-pull: 40 lb leader landed a marlin (species/reel type per title only, not confirmed in audio) added as hedged Observed block, unsupported baitcaster cla |
| 9D3Oiy0ASzg | StokedOnFishing | on-the-water | single-pull | done | species/yellowtail.md / on-the-water observation added to San Benito Islands entry (braid-vs-kelp/rock cutoff during yellowtail fight); one internal cross-reference inaccuracy fixed |
| wJgoRhZStz0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Amazon/Brazil peacock bass, freshwater |
| xudAbDj4GYw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama, Coiba Is. inshore/offshore |
| CdJ-ISFv8BI | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama offshore tuna/dorado/marlin |
| APsnsunT4gM | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/pacific-crevalle-jack.md; techniques/trolling.md / added inshore beach-dorado, offshore troll (tuna/wahoo/marlin), and jack-crevalle-named-target Observed entries for East C |
| SImABCBBxAo | StokedOnFishing | on-the-water | parameter-skim | done | species/spotted-bay-bass.md; lures/bay-bass-plastics.md / 4 Observed blocks added (depth, color-to-overcast, bait-profile match, named bait) |
| LE49ush9zqA | StokedOnFishing | on-the-water | skip:thin-generic | skipped | No location/conditions given; pure catch montage of double yellowtail hookups |
| isXJONlpUP4 | StokedOnFishing | on-the-water | parameter-skim | done | techniques/trolling.md / Added Mag Bay estuary/mangrove troll-and-cast entry (wind/chop fallback from offshore marlin, 25-30ft channel depth, palometa/pompano-family ID, 3/4oz Cast Master casting swit |
| OVwqUKim9Pc | StokedOnFishing | on-the-water | parameter-skim | done | techniques/trolling.md / Added Mag Bay sea-state bank-routing Observed entry (Ridge vs Modesto Main, wahoo->dorado bite, final-day snook estuary) to existing Magdalena Bay section |
| yjwIGFzWO8I | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; species/calico-bass.md; species/dorado.md / additive Observed-block entries for Cedros macro-banks to Chester's Rock leg (yellowtail 30-40lb + kelp/spectra fight, mixed dorado,  |
| DGh-iUp63Hc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska Gustavus halibut/black bass/salmon |
| j-hRaVWkQw4 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska Gustavus halibut pt2 |
| 9pJA2BnCjpc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica private creek machaca, freshwater jungle stream |
| MhJeCS_c3h8 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica inshore wahoo/grouper + offshore tuna |
| Nz5kTJQvuEY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica catch-and-cook tuna, offshore fishing + cooking segment |
| V_ONnegk95M | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowtail.md; techniques/flyline.md; techniques/surface-iron.md / evening bite-window timing + 30lb/3-0 hook & drag-set + bait-selection params + green-and-yellow surface-iron color observed |
| QSmE3mdEL28 | StokedOnFishing | on-the-water | parameter-skim | done | bait/making-bait.md; species/yellowtail.md; tackle/line-and-leader.md; techniques/trolling.md / Cedros Baja trip: 80-100lb line class over 28-30ft resident structure, slow-trolled live mackerel on cir |
| brx6Ie_L2FM | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/yellowtail.md; techniques/trolling.md / Added three Observed blocks (Cedros dorado paddy account w/ 200-300 fish, personal-best yellowtail ~1 mi offshore, dock advice for sl |
| I-QBxuV2p7M | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/yellowtail.md; techniques/surface-iron.md; techniques/trolling.md / Cedros day-2 Observed blocks: yellowtail troll blanked at 30ft on 65/80lb gear, diverted to wide-ope |
| e73wPONTOJU | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-trolling.md; species/bluefin-tuna.md; species/dorado.md; species/striped-marlin.md; techniques/flyline.md; techniques/foamer-casting.md / on-the-water observations-only extraction appl |
| VWClGAn2WEw | StokedOnFishing | on-the-water | deep | done | conditions/kelp-paddies.md; species/dorado.md; species/yellowtail.md / on-the-water/deep Observed blocks: drift-setup/electronics+eyeballs/work-bird+discoloration search doctrine, plan-B bluefin-to-pa |
| HMdrP4-i9MM | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/sand-bass.md; techniques/dropper-loop.md; techniques/flyline.md / on-the-water kids/Okuma trip off Dana Point/N. San Diego Co.: calico+sand bass over hard bottom w/ sub |
| eUUtSmiskbA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Amazon peacock bass, freshwater, not SoCal/Baja |
| l0kB6y0klwY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Amazon Blackwater Explorer mothership promo, freshwater peacock bass |
| xzIaUEDklrE | StokedOnFishing | on-the-water | deep | done | lures/mad-mac.md; seasonal/november-december.md; species/bluefin-trolling.md; techniques/fighting-big-bluefin.md; techniques/trolling.md / on-the-water deep extraction: 6 Observed blocks (Mad Mac setb |
| QCXlPULXf4A | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Puerto Rico wahoo/tuna/tarpon, Caribbean |
| RSMA1xrGngA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Puerto Rico Caribbean charter, wahoo/yellowfin |
| vdgf_C1-P08 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Puerto Rico Caribbean, Dorado/tarpon, sponsor-heavy |
| 55-Sx8V1Uk8 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama Coiba/Hannibal Bank charter |
| ZBRSB4iwtbU | StokedOnFishing | on-the-water | skip:duplicate-of-ldVj0BoB-kE | skipped | confirmed: identical Jose interview on Cedros C&R reg change, same 1:57 runtime |
| HEyt8fxoH5w | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama Coiba cubera snapper/roosterfish/yellowfin |
| 9tIp4n7q850 | StokedOnFishing | on-the-water | observations-only | done | species/california-halibut.md; species/dorado.md; species/yellowtail.md; techniques/surface-iron.md; techniques/trolling.md / Cedros (Baja) halibut/dorado/yellowtail on-the-water observations: wide-op |
| Zo92MG459gQ | StokedOnFishing | on-the-water | observations-only | done | lures/tuna-poppers-and-stickbaits.md; species/calico-bass.md; species/california-halibut.md; species/yellowtail.md; techniques/trolling.md / on-the-water continuation of 9tIp4n7q850: Cedros home-guard |
| zn4n7k3iaZo | StokedOnFishing | seminar | parameter-skim | done | species/white-seabass.md / Added Bill Shedd (HSWRI/CCA Cal chairman) interview: OREHP program origin, 2M+ cumulative releases/eight-nine grow-out facilities, and the unresolved tag-return-vs-gillnet-s |
| xFS3MW4GpDU | StokedOnFishing | on-the-water | parameter-skim | done | bait/bait-tanks.md; rigging/leadhead-mods.md; species/white-seabass.md / on-the-water/parameter-skim: broodstock program depth ceiling (<60ft/40ft typical, air-bladder sensitivity), May/June migration |
| ORC1A68cEeM | StokedOnFishing | on-the-water | observations-only | done | bait/making-bait.md; species/yellowtail.md; techniques/trolling.md / La Paz, BCS observations: guide-led bait-making (mackerel jigging + purchased sardines) and shallow-water (12ft) live-bait slow-tro |
| qM7iOO7fOBw | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/yellowtail.md; techniques/flyline.md / StokedOnFishing La Paz (day 2) Observed entries: dorado school-holding corroboration (third region), yellowtail/cabrilla/dorado/pargo  |
| 92y14x33etQ | StokedOnFishing | on-the-water | observations-only | done | bait/making-bait.md; species/yellowtail.md; techniques/trolling.md / StokedOnFishing La Paz/Espiritu Santo: bait-wind note, El Bajo dropped-bait/slow-troll yellowtail Observed section (65lb braid/60lb |
| haJ3BancQDI | StokedOnFishing | promo | skip:promo | skipped | Short Okuma Alijos lever-drag reel product highlight clip |
| YUdbrIm9vrE | StokedOnFishing | on-the-water | observations-only | done | species/bonito.md; species/dorado.md; species/yellowfin-tuna.md; techniques/trolling.md / Cedros multi-species (yellowfin, dorado, bonito) Observed blocks: October tuna/dorado-before-yellowtail sequen |
| A8SuzB5qiKE | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/yellowtail.md; techniques/trolling.md; techniques/yo-yo-iron.md / Cedros Outdoor Adventures Oct-trip observations: yellowtail yo-yo iron rod/reel/leader builds (212ft drop,  |
| PAZA-PzMcWQ | StokedOnFishing | promo | skip:promo | skipped | Sizzle reel montage, no content, channel promo |
| Xnq3FIUzvuw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska Gustavus king salmon charter |
| usHl-4SfqDA | StokedOnFishing | on-the-water | deep | done | fish-care/tuna-care.md; locations/bays-and-harbors.md; rigging/flying-fish-harness.md; species/bluefin-tuna.md; species/calico-bass.md; species/spotted-bay-bass.md; techniques/fighting-big-bluefin.md; |
| RpfHO-kotc8 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus); king/sockeye salmon; sponsor-heavy intro |
| Sz88huROjtY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus) halibut/rockfish; sponsor-heavy intro |
| SS_ObRfLw2E | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska halibut dropper-loop/grub jig; sponsor-heavy intro |
| 6EDQtQHEwFE | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; techniques/surface-iron.md; techniques/sliding-sinker.md; techniques/fighting-big-bluefin.md / on-the-water Observed blocks: surface-iron sight-casting, sliding-sinker second Ce |
| ILBl12Jm7-0 | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; species/calico-bass.md; techniques/surface-iron.md; techniques/yo-yo-iron.md; tackle/line-and-leader.md / part-2 Cedros trip observations added (run-and-gun surface iron/yo-yo y |
| u0scEBby7nA | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / Part 3 of the Cedros Oct-2024 trip series (StokedOnFishing) - 44 lb personal-best yellowtail on a custom iron, San Augusti |
| qBZxnRuXtGo | StokedOnFishing | on-the-water | skip:duplicate-of-SdwwpQMJEOI | skipped | confirmed: identical Olive Crest tournament script/footage as SdwwpQMJEOI |
| PexiSOiN00o | StokedOnFishing | promo | skip:promo | skipped | Okuma Tesoro reel product demo; rock fishing/salmon/halibut clips, region unclear; sponsor-heavy |
| wj8IyrcsmF4 | StokedOnFishing | promo | skip:promo | skipped | 30s Okuma Tesoro reel teaser, same clips/lines as PexiSOiN00o; sponsor-heavy, no region |
| 0dIwWiOc1NY | StokedOnFishing | on-the-water | observations-only | done | bait/making-bait.md; species/bonito.md; species/calico-bass.md; species/rockfish-lingcod.md; species/sand-bass.md; species/yellowfin-tuna.md; species/yellowtail.md; techniques/slow-pitch-jigging.md; t |
| DTrhKKBEQyY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus) salmon+halibut harpoon; sponsor-heavy intro |
| V7AfmB9pl_I | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama (Coiba/Chiriqui); Inshore-labeled but out-of-region travel trap; sponsor-heavy |
| UfuiWFVvz2E | StokedOnFishing | on-the-water | observations-only | done | lures/knife-jigs.md; species/bluefin-tuna.md; species/yellowtail.md; tackle/hooks.md; techniques/knife-jigging.md / on-the-water observations-only extraction of a Constitution/Fisherman's Landing Cort |
| 7U4N1f0viOU | StokedOnFishing | on-the-water | observations-only | done | none / confirmed duplicate/re-cut recap footage of the already-logged Cedros Oct-trip series (Bonito Island/Chester's Rock/mackerel-bait-circle-hook content all previously captured); no new extractabl |
| R1F66XIjf3E | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama (Coiba Island) yellowfin tuna; sponsor-heavy intro |
| sHnqSIOjTdM | StokedOnFishing | on-the-water | observations-only | done | bait/bait-tanks.md; species/bluefin-trolling.md; species/bluefin-tuna.md; species/white-seabass.md; species/yellowtail.md; techniques/fighting-big-bluefin.md / on-the-water observations merged as Obse |
| mDmbGdQAy-4 | StokedOnFishing | on-the-water | deep | done | fish-care/tuna-care.md; species/bluefin-tuna.md; techniques/fighting-big-bluefin.md / on-the-water/deep extraction: weight-without-scale formula, foamer/troll-plug-failure observation, and 'railroadin |
| SdwwpQMJEOI | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/sand-bass.md; species/spotted-bay-bass.md / on-the-water observations-only extraction of Olive Crest ProAm bass tournament footage (release handling, pre-fishing plan,  |
| Y1xeieQI3B4 | StokedOnFishing | on-the-water | observations-only | done | fish-care/tuna-care.md; species/ocean-whitefish.md; species/rockfish-lingcod.md / added RSW fish-hold Observed to tuna-care, Cortez Bank ocean-whitefish Observed, and mid-trip pelagic-to-rockfish-swit |
| nQvJnfb5jQ4 | StokedOnFishing | on-the-water | observations-only | done | rigging/double-trouble-rig.md; species/bluefin-tuna.md; species/yellowtail.md; techniques/fighting-big-bluefin.md / on-the-water observations added as Observed blocks to 4 existing notes (kite/flyline |
| eL1Qm33-Mj0 | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/sheephead.md; techniques/surface-iron.md / Cortez Bank part-1 observations (build-up timeline, flyline/iron method split, incidental sheephead, casting-etiquette) merg |
| zBd1mayUt_I | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/yellowtail.md; techniques/kite-fishing.md / on-the-water observations added (slick/shutdown pattern, sundown 100lb+ kite+flyline bluefin bite, captain's tackle-heads-u |
| QSvzVHW9UMk | StokedOnFishing | on-the-water | observations-only | done | lures/tuna-poppers-and-stickbaits.md; species/bluefin-tuna.md; species/yellowtail.md; techniques/kite-fishing.md / on-the-water observations merged as attributed Observed blocks (Cortez Bank bluefin/y |
| LsFMBCa9DOQ | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; tackle/hooks.md; techniques/flyline.md; techniques/knife-jigging.md / on-the-water observations merged additively into bluefin-tuna, hooks, flyline, and knife-jigging notes; J |
| Ix0gG0-l3v0 | StokedOnFishing | on-the-water | deep | done | rigging/flying-fish-harness.md; species/bluefin-tuna.md; techniques/kite-fishing.md; planning/search-and-glassing.md / on-the-water/deep extraction - Baja tournament kite-rig how-to, tagline, gyro-bin |
| U1AgwmlY5bI | StokedOnFishing | on-the-water | observations-only | done | lures/mad-mac.md; lures/spreader-bar.md; species/bluefin-tuna.md; techniques/trolling.md — Observed-only additions: Mad Mac two-lure setback + reel model, 3-bar spreader setback, rapid-crank tip, comp |
| prQpoN9qWBY | StokedOnFishing | on-the-water | observations-only | done | none — skipped: travel/check-in/tournament-logistics footage, no fishing decision-knowledge or observed on-the-water outcome (pre-departure gear plan only, actual fishing deferred to part 2) |
| r4J5nP5Bkl4 | StokedOnFishing | on-the-water | observations-only | done | bait/fishing-live-bait.md; species/bluefin-tuna.md; species/dorado.md; techniques/fighting-big-bluefin.md — June 2023 El Dorado (Capt. TJ) trip: kelp-paddy dorado + backside-San-Clemente sundown bluef |
| oB4BpIUTTl4 | StokedOnFishing | on-the-water | parameter-skim | done | techniques/flyline.md; techniques/knife-jigging.md — night-jigging floor (100lb braid/mono min, 200-400lb leader, 350g+ jigs) and daytime flyline tackle (25-40lb, No.2 hook, ~90% corner hookup), same  |
| mj50D4rNfdI | StokedOnFishing | promo | skip:promo | skipped | 30s El Dorado boat ad, pure vessel-amenities pitch, no fishing content |
| c3NFkQbdDy0 | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/yellowtail.md — mixed bluefin/yellowtail anchor bite ~90mi off CA (El Dorado/Capt. TJ), Home Guard/Tanner Bank yellow naming, 40lb bluefin with pre-existing hook corro |
| 9qMLztwVx9g | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md — night yo-yo/jig bite 50-200lb vs daytime flyline bite 20-150lb, triples callout, Red Rooster SD trip; boat/landing naming hedged ASR-uncertain |
| 947solNfiPw | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md — sardine-bite Tanner Bank trip, day-one grade progression, 41lb prior-day report, mixed-grade 10-100lb tackle challenge, rod-handoff culture note, cross-matched to c3NFkQbdDy0 |
| Tz5y87zUp_Y | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama dorado catch footage, region confirmed in transcript |
| rhaie9Tbi8I | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama (Hannibal Bank, spinner dolphins), yellowfin/dorado catch footage |
| aPkRKI35XV0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama, Coiba National Park, rooster/snapper/amberjack footage |
| fDSd9kqwYW0 | StokedOnFishing | on-the-water | parameter-skim | done | species/rockfish-lingcod.md; species/yellowtail.md — Cortez Bank Observed blocks: rockfish stop (150ft ridge, drift-wind mechanics, 10-fish limit anecdote), yellowtail flyline leg (No.2 hook/25lb, 5-h |
| elBPRrdkugU | StokedOnFishing | on-the-water | observations-only | done | fish-care/gaffing.md; species/bluefin-trolling.md; species/bluefin-tuna.md; techniques/trolling.md; tackle/rod-and-reel-selection.md / RECOVERED WITH A CORRECTION, batch-3 Phase 1. The guard reported "protected path touched: profiles/cameron/rods.md", and the Gate B prep pass recorded it as a correct veto — but the extractor never wrote to the profile. It added a link FROM species/bluefin-trolling.md INTO profiles/cameron/rods.md (to identify a PCH rod model against Cameron's inventory), and link-maintenance.py then generated the reverse backlink inside the profile. Same mechanical class as the source-registry false positive. The underlying content problem was real though: a universal note must not reach into one user's gear list. Corrected on recovery — the rod is now described in class terms (150–200 lb heavy-troll class) with no profile link. Content: spreader-bar trip observations (mixed-speed spread + "dead zone" fuel framing in mph as spoken, 50-wide reels, all-hands gaff readiness on 100–115 lb fish, Huntington Harbor run profile, trip dated August 2022 from on-camera audio despite the 2022-12-22 upload) |
| nsUdT-zXI8s | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; techniques/fighting-big-bluefin.md; techniques/flyline.md — veterans-charity SCI trip: sea-lion depredation counter-move (conflicting technique), flyline sardine hook/line param |
| vCskOx6N-XM | StokedOnFishing | on-the-water | deep | done | fish-care/gaffing.md; rigging/flying-fish-harness.md; species/bluefin-trolling.md; species/bluefin-tuna.md; techniques/fighting-big-bluefin.md; techniques/kite-fishing.md — Tanner Bank bluefin trip: k |
| lxM-AbTn3Sc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Nosara, Costa Rica inshore wahoo/tuna/dorado footage, sponsor-heavy |
| b8IqxTQ6xr0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Nosara, Costa Rica yellowfin/wahoo footage, sponsor-heavy |
| c9xWDUyzDDI | StokedOnFishing | on-the-water | skip:thin-generic | skipped | 1min Fishlab Scrum Popper catch clip, no region/conditions stated, product-demo feel |
| Kiq4hdJ8Gsk | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska halibut jigging footage, series Alaska part 4 |
| 6N4zaJdHFck | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska salmon footage, series Alaska part 3 |
| M7BtON4GZgQ | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; techniques/flyline.md; techniques/foamer-casting.md — 2020 El Dorado Catalina west-end trip: fish-returning-from-islands pattern, shallow sonar marks (120/150ft), butt-hook fl |
| 4t_Z75shK_E | StokedOnFishing | on-the-water | observations-only | done | species/striped-marlin.md; techniques/trolling.md — Mag Bay trip: wind stand-down, bait/lure-size heuristic (dockside doctrine, not same-day data), wahoo transit-lure (confidence downgraded promotiona |
| BQ2U1PqxWi8 | StokedOnFishing | on-the-water | observations-only | done | species/striped-marlin.md; species/yellowfin-tuna.md; techniques/fighting-big-bluefin.md — East Cape Fiesta footage: yellowfin surface-boil/stickbait strike, scad-mac/flat-fall session, fight-slack re |
| UCADhIs5Ew0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska rockfish/king salmon footage |
| 8GXiSWF_4wA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska halibut/rockfish/salmon footage |
| iczB-6A1Arc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama, Hannibal Bank/Coiba, tuna foamers footage |
| oXunQKSbc2g | StokedOnFishing | on-the-water | observations-only | done | species/bonito.md; species/yellowtail.md — Cortez Bank El Dorado 2-day trip (Oct 2019): yellowtail-first/tuna-conditional/Cortez-fallback plan off peer intel, yo-yo+surface iron yellowtail, giant boni |
| pu9zIm-Tsus | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Title misleads but content is Costa Rica trip w/ Craig Sutton |
| fxZGXrrpHz4 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica marlin/sailfish/tuna/dorado trip, Nosara area |
| IxhdiX3oEEs | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; techniques/fighting-big-bluefin.md / added SoCal 184lb/65in bluefin catch as Observed entry in species router + teammate hand-off Observed entry beside East Cape hand-off doct |
| kS8eC_5y4oo | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica double sailfish, release/handling footage |
| 9jDy4gUUyJk | StokedOnFishing | on-the-water | single-pull | done | conditions/kelp-paddies.md / drone-as-paddy-precheck bullet added under Finding paddies; Observed dorado catch block added (one overreaching claim corrected to match hedged/garbled source) |
| 1nK7vSPl2sg | StokedOnFishing | on-the-water | observations-only | done | techniques/flyline.md / Observed block appended (La Ventana amberjack on high spot 200->80ft, 30lb fluoro topshot + 3/0 circle hook, Okuma reel); medium confidence per registry cap |
| Klfb433I3Uk | StokedOnFishing | on-the-water | parameter-skim | done | bait/fishing-live-bait.md; fish-care/tuna-care.md; techniques/fighting-big-bluefin.md / merged chum-buddy seal-avoidance chumming variant, yellowtail bleed-and-bucket observation, and two preventive s |
| SczdZIq3UmE | StokedOnFishing | on-the-water | parameter-skim | done | conditions/bird-reading.md; planning/electronics-and-sounder.md; species/yellowfin-tuna.md / tern-ID tip + 72F + yellowfin grades merged as Observed blocks, Simrad Halo radar zoom/dolphin-marking mech |
| Jz9KRNEHLkw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska lingcod |
| 0bcDBGzQnGw | StokedOnFishing | on-the-water | observations-only | done | species/striped-marlin.md; species/yellowfin-tuna.md; species/yellowtail.md; techniques/trolling.md / Ensenada/Navico dolphin-school-foamer-marlin stop and separate temp-break-search/Cal-Pal yellowtai |
| Q-gQuOegAx4 | StokedOnFishing | on-the-water | observations-only | done | bait/fishing-live-bait.md; species/bluefin-tuna.md; species/yellowtail.md / SCI bluefin (100-200lb) then inshore calico/bonita/yellowtail chum-line leg + pinniped bait-hooking data point added as Obse |
| cLYqjT7ddl8 | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md / two Observed blocks added (bird-on-school grade/weight data point; shallow-mark meter/jig depths); front-matter sources gap fixed |
| CKq0Z6ExVs4 | StokedOnFishing | on-the-water | observations-only | done | species/barracuda.md; species/ocean-whitefish.md; species/rockfish-lingcod.md; species/sheephead.md; species/yellowtail.md / Ensenada high-spot (200->25ft, 7-8mi off Hotel Coral) Observed blocks added |
| YcLMhI5kzBo | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tonga part 3, marlin/yellowfin, local cooking segment |
| SGbynqaiHdY | StokedOnFishing | on-the-water | observations-only | done | species/yellowtail.md; species/rockfish-lingcod.md / Save The Brave charity charter Observed blocks added (rig params/fallback rockfishing, depth/structure, mid-session reposition); triage-mismatch fl |
| rsCAh-QyK60 | StokedOnFishing | on-the-water | parameter-skim | done | species/bluefin-tuna.md; techniques/fighting-big-bluefin.md; techniques/kite-fishing.md / 3 Observed blocks added (272lb kite-caught bluefin; kite height/distance/troll-speed params; small-boat-vs-yac |
| tU4jhAkdzNw | StokedOnFishing | on-the-water | observations-only | done | rigging/rubber-band-deep-rig.md; species/bluefin-tuna.md; species/yellowfin-tuna.md; species/yellowtail.md / Top Gun 80 pt3 Observed entries: sliding-sinker trip-tip variant, AM bluefin/PM yellowtail  |
| 3T4c3Zez_DM | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/yellowfin-tuna.md / Top Gun 80 pt2 Observed blocks added: bluefin bite-window pattern (no on-camera grade), offshore bird/boil yellowfin bite ~30lb, cross-linked to pt |
| Rb5I2ljAqeE | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/yellowtail.md; techniques/flyline.md / Top Gun 80 pt1 day-1 Observed entries: desperation-reef squid-staging reasoning + 40-90lb bluefin, 18-25lb Home Guard yellowtail |
| mpcSgkQvIzg | StokedOnFishing | tutorial | parameter-skim | done | rigging/essential-knots.md / Worm-knot entry added (mono topshot to Bimini loop, ~10-wrap mechanic, fast field-retie judgment) |
| 6kpWn2sXokI | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/yellowfin-tuna.md; species/yellowtail.md; techniques/yo-yo-iron.md / Alijos Rocks Baja (Intrepid, long-range) mixed-bag Observed blocks added to dorado/yellowfin/yellowtail  |
| ASitOLYzFEA | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/yellowfin-tuna.md / Baja lower-banks Intrepid dock-day testimonials added as Observed blocks (4-day single-school anchor, dockside grade tallies, dorado bycatch); evaluator  |
| jznQMFoV0Ls | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Pure catch montage, almost no dialogue, no location/conditions detail |
| zUFbCIWZZMw | StokedOnFishing | on-the-water | observations-only | done | species/calico-bass.md; species/yellowtail.md / Added Bird Rock mixed-bag (yellowtail/calico bass/barracuda) and Catalina west-end bat ray/leopard shark misID Observed blocks; evaluator removed unsupp |
| uyjTdgIw-1k | StokedOnFishing | on-the-water | parameter-skim | done | planning/electronics-and-sounder.md; species/dorado.md; techniques/chunking.md / SST/wind-overlay break-finding method (Simrad demo, 69-72F/3-4F diff) + dorado light-tackle rig + chunk-vs-live-bait pr |
| Ow3an9lSVh4 | StokedOnFishing | on-the-water | parameter-skim | done | conditions/kelp-paddies.md; species/california-spiny-lobster.md; species/yellowfin-tuna.md; techniques/chunking.md; techniques/flyline.md; techniques/hoop-netting.md / Six trip-tip parameters merged ( |
| 3qSY328fFYo | StokedOnFishing | on-the-water | deep | done | species/striped-marlin.md; techniques/trolling.md; techniques/bait-and-switch.md / RECOVERED batch-3 Phase 1: commit bd4968b was guard-reverted for "deleted 21 lines" but the diff was a net-positive restructure (+139/-26) that sources a previously UNSOURCED flagged stub. Jimmy Decker via StokedOnFishing, Catalina tanker lanes/277 bank 2014-11-08: live green-back mackerel dropback execution (trigger on any marlin showing near the spread, boat stays in gear, outrigger-clip delivery worked back toward the jig, rod tip up to place the bait), plus tide timing / sun rule / sounder detail into the marlin router and trolling. The unsourced-skeleton provenance warning is correctly narrowed rather than removed — teaser handling and hookset stay flagged |
| XH-Hrfet6To | StokedOnFishing | on-the-water | parameter-skim | done | species/striped-marlin.md; techniques/trolling.md / Cabo San Lucas trip: species Observed block (dropback marlin catch, sailfish, water conditions) + Melton Tackle lure-size/tournament and afternoon-c |
| Mwx5AAXNMvE | StokedOnFishing | on-the-water | observations-only | done | species/striped-marlin.md; techniques/bait-and-switch.md; techniques/trolling.md / Cabo pt2 charter continuation: release-practice + fighting-chair Observed block, blue-marlin lost-strike lure data po |
| 4bbKduPRlHE | StokedOnFishing | on-the-water | skip:no-usable-content | skipped | 1:48 near-wordless b-roll clip (mako hits hooked yellowtail); no location/date/technique content |
| skRo1z41Dnc | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/dorado.md / Observed blocks added: whale-associated tuna sign, breezer holding bluefin-then-dorado ~2 days apart, four-species day; evaluator hedged an ASR-ambiguous c |
| AfZoeSu_9hc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Prince Edward Island, Canada bluefin trip; series pt1 |
| 27MMQGRIrpw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Prince Edward Island, Canada bluefin trip; series pt2 |
| SH7zOA9ZF3o | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowtail.md; techniques/yo-yo-iron.md / San Benito Island structure/kelp break-off corroboration and two-partial-crank-then-full-wind yo-yo cadence added; evaluator fixed a bare upload-date- |
| pk2blktDQ9Y | StokedOnFishing | on-the-water | parameter-skim | done | bait/bait-tanks.md; tackle/line-and-leader.md; techniques/fighting-big-bluefin.md; techniques/kite-fishing.md / Long-range multi-day bait load/care, line-class ladder by grade, fight-duration/topshot  |
| Fq4aRI3YrKE | StokedOnFishing | on-the-water | observations-only | done | species/yellowfin-tuna.md / Added Observed block (personal-best hookups, closing tally, bait-ball hold-position) as week-2 continuation of the pk2blktDQ9Y Intrepid trip; evaluator corrected an unsuppo |
| UuyqTE21-kc | StokedOnFishing | on-the-water | single-pull | done | techniques/kite-fishing.md / Added Observed block logging a kite-free helium-balloon flyer presentation fished downwind for giant Baja yellowfin; evaluator softened an unsupported visual claim (captio |
| D_Y2G0rBZCs | StokedOnFishing | on-the-water | parameter-skim | done | bait/fishing-live-bait.md; species/yellowtail.md / SCI squid bite grade split, 20-25lb line window, sliding-egg-sinker/dropper-loop rig, keep-bait-active tip merged as Observed entries; evaluator appl |
| nkJNzdNlm_c | StokedOnFishing | on-the-water | observations-only | done | planning/electronics-and-sounder.md; species/bluefin-tuna.md / Search-sonar range/audio-cue Observed entry and same-trip morning-bluefin/afternoon-yellowfin grade Observed entry added; evaluator appli |
| JaKSGkZ6CAc | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowtail.md; techniques/dropper-loop.md; techniques/yo-yo-iron.md / Baja/San Benito Island companion re-cut added squid-depth pattern (30-40fm), dropper-loop 100lb-min line-class parameter,  |
| t-gIME7sV2A | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama trip; series pt1 |
| 2OANMH22qzE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama/Hannibal Bank; series pt2 |
| IH4y6GM6BIY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island (Revillagigedo Mexico), not Baja peninsula; series pt1 |
| aecs-mFrCdM | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island; series pt2 |
| HpPFogLwKOw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island; series pt3 |
| kWT_0Qp8wkw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island; series pt4 |
| 8THSuqoPI_Q | StokedOnFishing | on-the-water | observations-only | done | conditions/kelp-paddies.md; species/bluefin-tuna.md; species/dorado.md; species/yellowtail.md / added 4 Observed blocks (small-paddy attitude, bluefin drift depth/hook-position, dorado hook-position c |
| -bw1KDfDjv4 | StokedOnFishing | on-the-water | parameter-skim | done | conditions/kelp-paddies.md; planning/electronics-and-sounder.md; planning/fleet-intelligence.md; techniques/flyline.md / 14 Mile Bank paddy re-work tactic, SST bank-vs-off-bank reading, radar fleet-sc |
| IwxqgocsQTY | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/yellowtail.md; techniques/sliding-sinker.md; techniques/surface-iron.md / on-the-water observations across 2 species routers + 2 technique notes (bluefin depth/rig/gra |
| 97clKtVsEOs | StokedOnFishing | on-the-water | parameter-skim | done | planning/electronics-and-sounder.md; species/yellowtail.md; techniques/trolling.md / anchor-vs-drift sounder-read doctrine, Alijos Rocks wahoo bomb-lure hookup-ratio and no-pump fighting-technique det |
| ilINTeknKB4 | StokedOnFishing | on-the-water | observations-only | done | species/bluefin-tuna.md; species/rockfish-lingcod.md; species/yellowfin-tuna.md; species/yellowtail.md; techniques/sliding-sinker.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / observation |
| _PGm-TlFU2A | StokedOnFishing | on-the-water | parameter-skim | done | tackle/hooks.md; techniques/flyline.md / thick-shank hook doctrine (30lb leader/65lb Spectra, no-shock-absorption failure mode) added to hooks.md; flyline Observed block (No.4-2 hooks, 25-30lb fluoro, |
| ZghZCFL6OZk | StokedOnFishing | on-the-water | skip:out-of-region | skipped | series: Stoked on Costa Rica part 3; Costa Rica out of region |
| HueC1KHrcVw | StokedOnFishing | on-the-water | parameter-skim | done | bait/bait-tanks.md; species/bluefin-tuna.md; species/yellowtail.md / bait-loading visual tell, 70-72F bluefin preference, 20lb straight yellowtail rig, wahoo incidental catches; fixed timing-polarity  |
| i3qIAHW-SJc | StokedOnFishing | on-the-water | parameter-skim | done | conditions/water-temperature.md; rigging/essential-knots.md; rigging/rubber-band-deep-rig.md / mono-to-fluoro knot tie, tag-end sinker attachment, bank-to-bank SST/bite Observed note; fixed sinker-mec |
| A6DJoXbID4c | StokedOnFishing | on-the-water | deep | done | bait/making-bait.md; conditions/bird-reading.md; conditions/kelp-paddies.md; lures/tuna-poppers-and-stickbaits.md; techniques/foamer-casting.md / deep extraction: bird-reading, 100yd-off-paddy positio |
| zQtExV8Z2eY | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowtail.md; techniques/sliding-sinker.md; techniques/flyline.md / SCI Thunderbird trip: 30lb mono/4ft 30lb fluoro topshot, 1/4oz slider+#2 hook+squid vs flylined sardine, 122-fish/9:30am an |
| MUpvP-Yl2R0 | StokedOnFishing | on-the-water | observations-only | done | planning/electronics-and-sounder.md; species/california-halibut.md; species/yellowtail.md; techniques/sliding-sinker.md / buoy/wind-wave overlay, AIS/structure-scan naming, bird-radar demo, Catalina y |
| AIHvJj-paoo | StokedOnFishing | on-the-water | parameter-skim | done | bait/fishing-live-bait.md; species/yellowfin-tuna.md / trip-tips (line downsize, private-boat chum-together/give-space etiquette); fixed invented leader/topshot pairing during review |
| NEuoCgxjrhM | StokedOnFishing | promo | skip:promo | skipped | pure Komodo 450 reel product demo/highlight reel, no doctrine, 1:56 short |
| mG8ZZLFGlT8 | StokedOnFishing | on-the-water | observations-only | done | species/dorado.md; species/striped-marlin.md; species/yellowfin-tuna.md; tackle/hooks.md; techniques/trolling.md / East Cape Fiesta trip observations (dorado/wahoo/yellowfin/marlin catches, rooster-fi |
| oadK6zIYyCo | StokedOnFishing | on-the-water | observations-only | done | species/barracuda.md; species/calico-bass.md; species/sheephead.md; species/yellowtail.md; techniques/surface-iron.md / calico squid-vs-sardine, sheephead nickname, yellowtail-on-squid, barracuda sink |
| 3tQ1_xiqwVU | StokedOnFishing | on-the-water | parameter-skim | done | techniques/yo-yo-iron.md; techniques/kite-fishing.md / added two hedged Observed blocks (180ft/10ft-off-bottom yo-yo yellowtail near Mag Bay ridge; stated kite/balloon/flyline 50lb plan for 60-90lb+ y |
| XJaLubOVfvs | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Baja Mag Bay long-range trip intro; mostly boat/crew/food, thin fishing detail; cf. 3tQ1_xiqwVU |
| o1mJ5H8Np-s | StokedOnFishing | on-the-water | skip:thin-generic | skipped | pure catch montage (San Pablo yellowtail), no conditions/technique detail |
| 5LI0vPzlCUE | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Alijos Rocks (far offshore Baja, edge-of-scope); pure catch montage, no doctrine |
| 0HILDC0ITLE | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SoCal albacore catch footage; only generic line-in-front-of-you safety tip |
| 2TE46Hqoq5s | StokedOnFishing | promo | skip:promo | skipped | Intrepid boat/crew/food comfort testimonial ad; negligible actual fishing footage |
| ns992VlKpMc | StokedOnFishing | on-the-water | skip:thin-generic | skipped | near-silent Top Gun 80 yellowtail catch montage, almost no dialogue |
| RgtkbmBFUXI | StokedOnFishing | on-the-water | parameter-skim | done | species/yellowtail.md; techniques/dropper-loop.md / Guadalupe Island 100 lb dropper-loop leader + 120-250ft drift + ~8-of-10 rock-cutoff loss rate added as Observed data points (medium confidence, unr |
| 2K4urpo3q6Q | StokedOnFishing | on-the-water | observations-only | done | none / no extractable fishing knowledge — incidental unlocated great white shark sighting, empty patch confirmed correct |
| w37pHf0xjrw | StokedOnFishing | on-the-water | parameter-skim | done | techniques/sliding-sinker.md / Merged albacore torpedo-sinker/slider Observed block (2oz torpedo+No.3 hook drop-back vs. smallest-slider+size-2-hook chum-drift, straight anchovy) into existing sliding |
| Bab_6o7JFh4 | Crust to Coast | seminar | parameter-skim | done | conditions/current-structure.md; conditions/deep-scattering-layer.md / mechanism vocabulary (continental margin bathymetry + light zones) merged into two existing conditions notes, parameter-skim dept |
| GIlM8fTmL5M | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: navigation history and bathymetric mapping techniques, no waves/tides/currents mechanism |
| d7IPkfjMZu8 | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: solar system/earth origin, mantle layers, isostasy, seismology; deep-time geology |
| SVLqaSa1bxU | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: continental drift, mantle convection, seamounts/hotspots; rock/plate-tectonics geology |
| 6pAmcsTtYGA | Crust to Coast | seminar | parameter-skim | done | conditions/deep-scattering-layer.md; conditions/water-temperature.md / merged salinity-vs-latitude/depth and oxygen-minimum-layer/hypoxia mechanism into two existing conditions notes as background-mec |
| i4OB4G6_adI | Crust to Coast | seminar | parameter-skim | done | conditions/water-color.md; conditions/water-temperature.md; planning/electronics-and-sounder.md / mechanism background (thermocline/pycnocline/mixed-layer depth structure, SOFAR/deep sound channel, li |
| OZejCm0ItEE | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: lithogenous/biogenous sediment classification, core sampling, paleoceanography |
| 32TQdFJKIlI | Crust to Coast | seminar | parameter-skim | done | conditions/upwelling-and-turnover.md / Ekman transport (SoCal alongshore-wind upwelling/downwelling mechanism) and ENSO/PDO basin-scale productivity modulation merged into existing conditions note as  |
| OEsW9K1IwpQ | Crust to Coast | seminar | parameter-skim | done | conditions/water-temperature.md / Heat budget (30/23/47% split), albedo table, equator-surplus/poles-deficit + thermohaline redistribution merged as mechanism-only section; triage-promised Coriolis/wi |
| dS0YUOyqN6g | Crust to Coast | seminar | parameter-skim | done | conditions/sea-state.md / Coriolis effect + Hadley/Ferrel/polar convection cells + doldrums/trade winds/polar easterlies background section added; unsupported westerlies claim dropped during evaluatio |
| RuNH5O9olfw | Crust to Coast | seminar | parameter-skim | done | conditions/current-structure.md / added surf-zone anatomy (bar/trough/surf zone/foreshore/backshore/swash/berm), seasonal beach-profile cycle, and longshore-current/rip-current mechanism as background |
| 9tTM99InluM | Crust to Coast | seminar | parameter-skim | done | conditions/tide-and-slack.md / mechanism-background section added (gravity/spring-neap/50-min lunar offset/mixed semi-diurnal), correctly labeled non-doctrine, no doctrine touched |
| rK1sWd84S04 | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: sea ice/glacial ice formation, cryosphere, brine rejection; no CA/Baja relevance |
| tKqZJZMLbq4 | Crust to Coast | seminar | parameter-skim | done | conditions/deep-scattering-layer.md / Zooplankton (copepods/krill/jellyfish) and nekton swimming-mode/bioluminescence mechanism added as generic background section; two faithfulness overreaches trimme |
| eg8IUjeWZx8 | Crust to Coast | seminar | parameter-skim | done | conditions/current-structure.md / added generic benthic-biomass (98%/2% species, coastal/polar concentration) sunlight+nutrients mechanism to existing upwelling section, no new claims beyond mechanism |
| zvU45nkhhuE | Crust to Coast | seminar | parameter-skim | done | conditions/upwelling-and-turnover.md / amended existing note with a labeled Crust to Coast mechanism section (primary productivity light/nutrients drivers + chemosynthesis), no new notes |
| gT5g8Rhtpyg | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: life taxonomy/domains/kingdoms classification lecture, no conditions mechanism |
| 7jPK4aOctQo | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: marine pollution types/sources, environmental-science survey |
| YGKgQp5HTLM | JoeWo | non-fishing | skip:not-fishing | skipped | JoeWo Warzone gaming aiming-guide video; unrelated to fishing (stray) |
| mwrFx2DdmO0 | Kevin Is Cooking | non-fishing | skip:no-usable-content | skipped | Kevin Is Cooking tacos al pastor; transcript is 3 useless lines, no content (stray) |
| 55IthpZZx9k | Okuma Fishing Tackle USA | promo | skip:promo | skipped | Okuma booth ad: Dave Hansen pitches Makaira 130 + PCH bent-butt rod for SoCal bluefin/swordfish; feeds dave-hansen registry |
<!-- batch2:worklist:end -->

## Batch 2 — Gate B prep pass (2026-08-15)

Run-complete state was 264 done / 6 escalated. A review pass before merge
fixed one pipeline defect and recovered the extractions it had bounced.

**Defect fixed (commit `7f741ff`).** `sources/source-registry.md` is a trust
table that notes legitimately link to ("<voice> is a registered voice").
`link-maintenance.py` regenerated a backlinks block inside it whenever such a
link appeared, which made the extraction commit touch a guard-protected path,
so the mechanical guard reverted the whole commit. Two of the pipeline's own
mechanisms were fighting; the extractor behaved correctly throughout. Fix: a
narrow `NO_BACKLINKS` set — the registry is still validated and indexed like
any note, it just never receives a generated backlinks block. The stale block
was removed from the registry, along with a phantom circular backlink it had
created into `fish-care/gaffing.md`.

**Recovered (3 videos, cherry-picked from the reverted commits):**

| video_id | original commit | recovered in | content |
| --- | --- | --- | --- |
| EmZO8QiOfik | 0d33e3c | 02ba68f | `species/cabrilla.md` + `lures/jerkbaits.md` (both new) + Sea-of-Cortez amendments across 7 notes |
| _ZThckj2TIM | 0716a9d | 3ff380b | Capt. Scotty weak-link dropper-loop doctrine across 5 notes |
| ftEvyfwjZFU | ed1860a | ab61aed | Hansen San Diego jam / bluefin tackle across 5 notes |

Conflicts against later videos' amendments were resolved as **unions, never as
a winner**: front-matter `tags`/`sources` merged, prose bullets kept from both
sides, generated backlink blocks left for `link-maintenance.py`. Each recovered
worklist row records its provenance inline.

**Still escalated — deliberately not auto-recovered (3 videos).** These are the
guard catches that need human judgment rather than a mechanical fix; each one's
full attempted diff is preserved in git history:

| video_id | commit | why it was reverted | the judgment call |
| --- | --- | --- | --- |
| unARAuTgF_A | 917703f | deleted 38 lines from `rigging/assist-hooks.md` | the extraction restructured a note built by this video's part 1 rather than appending; decide whether the consolidation is an improvement or drops attributed detail (the ASR-uncertain 215/300 lb cord weights and the sponsored-product caveat) |
| 3qSY328fFYo | bd4968b | deleted 21 lines from `techniques/bait-and-switch.md` | same shape: verify nothing attributed was smoothed away before restoring |
| elBPRrdkugU | 848d803 | wrote to `profiles/cameron/rods.md` | correct veto — general notes never write into a user profile; the gear content should be re-homed to `tackle/` in class terms, or dropped |

End state: **267 done / 148 skipped / 3 escalated** of 418 worklist rows.

## Batch 2 — close-out (Phase 5, run 2026-08-17 as batch-3 Phase 1)

Batch 2 merged to `main` (`540ea4a`) after only the Gate B *prep* pass — the
defect fix and three recoveries. The Phase 5 package it promised (coverage
reconciliation, acceptance tests, judgment-calls list) was deferred to "a
separate reviewed session" that never ran. This is that session.

### Coverage reconciliation — complete

| | count |
| --- | --- |
| manifest rows | **576** |
| — `ok` (transcript on disk) | 546 |
| — `failed` (no transcript) | 30 |
| ok rows accounted in the batch-1 section | 125 |
| ok rows accounted in the batch-2 worklist | 421 |
| **ok rows appearing nowhere in this log** | **0** |
| **failed rows appearing nowhere in this log** | **0** (was 23 before Phase 0) |

Batch-2 worklist end state: **418 rows = 271 done / 147 skipped / 0
escalated**. All four parked items were resolved this session (three guard
escalations + one evaluator reject), which moved 4 rows from
`escalated`/`skipped` to `done`.

**True yield is 264, not 271.** Seven `done` rows produced no content and are
silent nulls in the headline number: `k80p1ShSvZs`, `rwfjUa4zsyY`,
`1hJoxwg9fy4`, `YijeuGOYoVQ`, `7U4N1f0viOU`, `prQpoN9qWBY`, `2K4urpo3q6Q`.
Two of those are recoverable — `rwfjUa4zsyY` is a caption-quality failure, and
`YijeuGOYoVQ` was dropped for having "no existing anchor notes," which the
batch-3 note-creation rule fixes.

### Acceptance test — 21/21 routers pass

Every species router carries all five mandatory sections (Where & when /
Finding them / Situations → techniques / Gear summary / Doctrine & conflicts).

The sonar clause ("species-specific sonar signatures with depths") is
satisfied or **correctly and explicitly declared absent** in every case —
`sheephead.md` states "no species-specific sonar signature or visual sign is
documented in this corpus"; `striped-marlin.md` declares a sight fishery;
`sand-bass.md` and `ocean-whitefish.md` give real signatures without numeric
depths. That is the required behaviour, not a failure. One genuine omission
found and fixed: `cabrilla.md` gave no sonar read and did not say so — now a
flagged stub.

**The test passes structurally and fails practically for one note.**
`species/yellowtail.md` is 1,360 lines with `## Where & when` running ~1,180
of them; the routing payload starts past line 1,200. A new-to-SoCal angler
opening it cold does not reach the router table. Recorded here as the finding
that drives batch-3 Phases 3–4, not as a pass.

### Flagged-stub audit

Batch 2 added **zero** flagged stubs across 267 videos, so the stub rule
(CLAUDE.md §Species-first routing item 5) was not being applied during the
run. Current stubs: `california-halibut.md` (bounce-ball trolling),
`yellowtail.md` (locate-trolling), `calico-bass.md` (Wax Wing),
`swordfish.md` (finning/sunning fish), `inshore-crankbaits.md` (Wax Wing
model catalog), `gear-classes.md` (light troll class), and — added this
session — `cabrilla.md` (sonar signature). `bait-and-switch.md`'s stub is
**retired**: `3qSY328fFYo` sourced it.

### Escalations — 27 entries, triaged

Six were guard violations, **all now resolved** (three recovered at Gate B
prep, three this session; two of the three were false positives on
net-positive restructures and the third was a false positive on a generated
backlink). The 21 evaluator escalations split as:

- **13 compliant regulatory claims** → moved to
  [regulatory-claims.md](regulatory-claims.md), a standing register Cameron
  reviews before a trip rather than an interrupt. These were flagged only
  because the evaluator's trigger fired on category presence; the evaluators
  said so themselves in the escalation text.
- **4 framing questions** that do need a decision — see below.
- **3 router-table additions** (`fK2AT460xW4` dolphin-pod dropper row,
  `ntQXxcH5sjI` shallow bait-ball yo-yo row, `QSmE3mdEL28` Cedros live-bait
  slow-troll row). All three are additive rows for previously unhandled
  situations, which cannot change what an existing acceptance test returns.
  Recommend accepting all three; the Phase 5 evaluator change stops purely
  additive rows from escalating at all.
- **1 genuine cross-video factual problem** (`iQLyBzhOSi8`).

### Judgment calls for Cameron

1. **`xzIaUEDklrE` — a live conflict against your own doctrine.** A
   StokedOnFishing observation has the spreader bar selecting for *bigger*
   fish over the Mad Mac, which is the opposite of your registry-high
   presentation-size axis (small forage → bar, large forage → Mad Mac). Kept
   side by side and unreconciled per convention, but it is your doctrine on
   one side, so it needs your read.
2. **`iQLyBzhOSi8` — a dating error that may have propagated.** The on-camera
   slate reads **2012** for the fourth annual COOC, while the already-committed
   parts 2 (`PKf7G3uL4io`) and 3 (`IATPg9110CE`) assume ~2014 from the shared
   YouTube upload date alone. All three may document the 2012 tournament. The
   pipeline could not fix this — a one-video-at-a-time extractor cannot
   retroactively amend a sibling's committed entry.
3. **`EiItVWqFMYc` — sublegal lobster handling.** The added section frames
   redepositing a short lobster as legal via a not-possessing-it technicality,
   sitting beside the note's release-it-immediately doctrine. Regulatory-
   adjacent and worth your explicit sign-off before it stands.
4. **`Y1xeieQI3B4` / `fDSd9kqwYW0` — unstamped bag-limit figures.** Both are
   on-camera numbers ("20 fish per angler", "10 around") carried with
   verify-separately caveats rather than jurisdiction/as-of stamps, because
   the speakers gave none. Confirm the hedging is sufficient.
5. **Assist-hook confidence promotion.** `rigging/assist-hooks.md` went
   medium → high on the strength of two videos in one Cesar series
   (`U4zifdssSes` part 1, `unARAuTgF_A` part 2). Two parts of one teaching
   session may not be independent confirmation under the re-cut rule.
6. **The batch-1 double-count is fixed, and it cost a claim.** `vqsD0qpwcJA`
   and `Jtf-bU4aM-c` are one recording. The BOLA slow-pitch doctrine that
   rested on "both" is demoted to a single-trip data point at medium — and
   the narrator self-declares as new to the technique on camera. Phase 3's
   BOLA sources should not be merged into the old inflated prior.

### Known losses, recorded

- **SWBA Midnight Standoff** — parts 1–2 failed to fetch, part 3 skipped as
  thin-generic. Nothing of that trip is covered.
- **`CyOsniVmbN8`** — part 3 of the 2016 "Top Gun 80 Epic 5 Day" run; parts
  1–2 were extracted.
- **16 private/unavailable videos** — permanently unrecoverable.
- **Thin areas persist:** mako and thresher shark remain absent, as recorded
  at batch 1. Halibut is thinner than it looks — the Fred Hall "Halibut
  Secrets" seminar in the batch-3 corpus has no caption track in any
  language.

## Batch 3 — Phase 3 landing (BOLA + Strictly Irons), 2026-08-17

Supervised, not through the unattended chain (see the batch-3 plan, Decision
5): these corpora are multi-video synthesis units and the per-video machine
cannot hold two transcripts at once.

**Landed:** 50 transcripts + 7 failed accountability rows from two zips
(`cameron-peterson--bola`, `strictly-irons--channel`). Manifests normalized
from the 8-column export schema (`video_id,title,url,status,caption_type,
caption_lang,filename,failure_reason`) to the repo's 7-column schema;
`channel` and `upload_date` taken from each transcript's YAML header.

**Not landed — already in the corpus (4):** `dEPuDrhoClM`, `EmZO8QiOfik`,
`M8hOYQ_6rSg` (Dirty Hookers), `ntQXxcH5sjI` (StokedOnFishing). All four are
Cortez-relevant and are cited by the new location notes from their existing
copies. **Cross-zip duplicate (1):** `P36VGPPf120` appears in both the BOLA
and Strictly Irons zips — landed once under `strictly-irons/`.

### Notes created

| note | sources | what it closes |
| --- | --- | --- |
| `locations/bahia-de-los-angeles.md` | `P36VGPPf120`, `odiIWmut6gM`, + cameron | The whole BOLA trip: season table, the Mexican paperwork the KB had **zero** of (FMM, CONAPESCA licence, Baja Bound insurance), the 8-hour route leg by leg, costs ($800–1,000 pp / 4 days; panga $550/day), lodging, operators, comms blackout, and how a fishing day runs |
| `locations/sea-of-cortez.md` | the 9-episode Tony Reyes series + `M8hOYQ_6rSg`, `dEPuDrhoClM`, `_Wb4z4ammoM`, `A6s-A1NARuA` | The San Felipe mothership trip as a distinct fishery — overnight relocations, the 12–15 ft crossing, what happens when pangas can't launch, 6 ft water driving 80 lb line, the jerkbait pause-at-the-rock trigger |
| `locations/loreto.md` | 5 Loreto trip videos | The southern Cortez island fishery — Monserrat/Carmen/Six Mile Reef, roosterfish on the troll, fly-in access via CBX |

### Findings worth recording

1. **Independent corroboration of a cameron data point.** `P36VGPPf120`
   arrives at the same BOLA read Cameron did — as summer water heats the fish
   sound, you lose the surface bite and go to dropper loop / live bait / yo-yo
   / knife jigs. That was a single-angler observation in
   `seasonal/september.md`; it now has a second, independent source with the
   same stated mechanism.
2. **Baja corroboration of the surface-iron hookset.** `ZYAILGyrkRk` on
   cabrilla: *"don't swing, just wind — it's a surface iron."* Same
   wind-through-not-swing doctrine as the SoCal sources, in a different region
   on a different species. A trade-off comes with it: the same angler switched
   off iron because "surface iron recovery is so bad" on a fast shallow bite.
3. **The San Felipe / BOLA title problem is real but subtler than triage
   suggested.** `4Dn7yChmhk0` is titled "Bahía de Los Ángeles" and narrates
   "aboard the Tony Reyes out of San Felipe" — *and* the same narrator calls
   the grounds "Bay of LA." Since the mothership relocates 8–9 hours at a time,
   both labels can be partly true. Recorded as a naming caution with a rule
   (treat as San Felipe unless the grounds are named on camera) rather than as
   a flat mislabel.
4. **Wax Wing appears** (`ZYAILGyrkRk`, "gotten bit every cast") but on Baja
   cabrilla, not SoCal calico — so the `⚠ Wax Wing` flagged stubs in
   `calico-bass.md` and `inshore-crankbaits.md` **stand**.
5. **A date I could not establish** was removed rather than guessed:
   `odiIWmut6gM` gives day-of-month only on camera ("the 22nd", "Wednesday the
   24th") against a 2026-07-02 upload, so the trip month is recorded as
   unestablished.

### Phase 3, part 2 — Strictly Irons (18 transcripts), read in full 2026-08-17

Every transcript in `sources/transcripts/strictly-irons/` was read end to end,
not skimmed. Extraction was aimed at Cameron's correction C3 — **the decisions
and the stated reasons**, not more observation volume. Where a video's content
had no compliant destination, a note was created (C1) rather than the content
being dropped.

| video_id | type | destination(s) |
| --- | --- | --- |
| `Ec2GaNpiOHI` (Q&A with Dan Wade, 2019-03-19) | tutorial | `lures/iron-jigs.md` §Reading a jig (new); `techniques/surface-iron.md` §mechanism; `techniques/surface-iron-color.md` |
| `yn1suHH6b1Y` (jig masterclass, 2026-05-13, Fishing Syndicate) | seminar | same three notes — the corroborating half of the Dan Wade doctrine |
| `764kFzACKTc` (wiring a surface iron, 2021-01-28) | tutorial | **`rigging/wiring-a-surface-iron.md` (new)**; pointer + parameters cross-check into `rigging/haywire-twist.md` via that note |
| `IhBY5RHFvuk` (casting distance, 2026-01-24) | tutorial | **`techniques/surface-iron-casting.md` (new)** — wind→trajectory, follow-through aim, soft-cast, rod-action loading, spool tension, shore practice, the baitcaster path |
| `0DKmYId1NN4` (early-season bite, 2026-04-16) | on-the-water | `species/yellowtail.md` (40–60 ft → surface-iron/light-bait, not yo-yo); `techniques/surface-iron.md` §decisions; `techniques/surface-iron-casting.md` (drop-back-and-reel-tight) |
| `ejUTAnONf7o` (new Wise jig, 2026-04-21) | on-the-water | `species/yellowtail.md` (wind→yo-yo re-rank row); `techniques/surface-iron.md` §decisions + §common failures; casting note (reel-sideways corroboration) |
| `_MygUHw19q8` (Cedros days 3–4, 2024-06-08 on camera) | on-the-water | **`locations/cedros-island.md` (new)**; `techniques/surface-iron.md` §decisions |
| `IdMJnlg_rZk` (Cedros day 1, 2024) | on-the-water | `locations/cedros-island.md`; `species/calico-bass.md` (mid-day mini-iron row) |
| `2cxeg_AE418` (Cedros day 2, 2024) | on-the-water | `locations/cedros-island.md`; `species/calico-bass.md`; `techniques/surface-iron.md` §decisions |
| `4pT0efBD1j0` (Coronados vlog, 2020-08-18) | on-the-water | `techniques/surface-iron.md` §chum-then-cast; `locations/cedros-island.md` (grade/behaviour contrast) |
| `u80AI37soFI` (Coronados surface-iron bite) | on-the-water | `techniques/surface-iron.md` §decisions (keep winding on a miss) + §common failures (over-pulling) |
| `gdqI2dNd5_U` (Coronados yellowtail) | on-the-water | `techniques/surface-iron.md` §chum-then-cast (get bit back to hold the stop) |
| `dS9gd9k7A7Q` (Mission Belle, Coronados) | on-the-water | `techniques/surface-iron.md` §chum-then-cast (boat-shy read) — 166 words, two usable lines |
| `Ob45hK4HSWc` (yo-yo → hand-lining, 2019-02-07) | on-the-water | `species/yellowtail.md` (tuna-pen row + a Doctrine entry recording that the location is unestablished); `techniques/yo-yo-iron.md` §common failures (bycatch interception). **Corrected 2026-08-17 — see below** |
| `P36VGPPf120` (planning a BOLA trip) | tutorial | `locations/bahia-de-los-angeles.md` (landed in Phase 3 part 1) |
| `oRg9XKtnJW0` (2022 montage) | promo | `skipped: music-montage, 221 words, no extractable doctrine beyond "slow troll surface irons" already held in the trolling and surface-iron notes` |
| `vSBY4uS5624` (tuna foamers collab) | promo | `skipped: music-only, 67 words, zero speech` |
| `EuTVPVY9lAs` (brand/faith vlog) | promo | `skipped: brand-origin and personal-testimony vlog; no SoCal/Baja fishing decision content — fails the curation bar as generic non-fishery content` |
| `Ci5ZybXzj1Y` (Christmas charity event) | promo | `skipped: community-service event, not fishing content` |

**Notes created this pass (6):** `rigging/wiring-a-surface-iron.md`,
`techniques/surface-iron-casting.md`, `techniques/surface-iron-color.md`,
`locations/cedros-island.md`, `locations/ensenada.md`, plus the new
`## Reading a jig` section carved into `lures/iron-jigs.md`.

**Mega-note split executed (plan Phase 3 item 5).** `techniques/surface-iron.md`
was 515 lines at the start of this batch. Colour went to
`surface-iron-color.md`, jig selection went to `lures/iron-jigs.md`, and the
cast went to `surface-iron-casting.md`. The parent kept the retrieve, sizing,
gear-class detail, and failures — and still absorbed the new decision material,
so it did not shrink as far as the split alone implies. It remains the largest
technique note and is a Phase 4 re-check.

#### Findings worth recording

1. **Two independent sources for "lay the reel on its side."** Dave Hansen
   (registered, `KLoEJInlmZo`, 2021) and Strictly Irons (`ejUTAnONf7o`, 2026)
   coach the same casting detail six years apart on different channels. Logged
   as corroboration, not merged.
2. **A stated depth threshold that selects a technique.** 40–60 ft marks →
   surface iron + light bait, explicitly *not* yo-yo. The KB had bands for
   structure yellows (5–10 fm) and deep high-spot yellows (150–300 ft) but
   nothing for the shallow "they're about to come up" read.
3. **A real doctrine tension, kept unreconciled.** The same crew says lock the
   drag and pull as hard as you can (Cedros, over rock) and *"sometimes you
   pull too hard, it's not hooked that well and it'll just pop off"* (Coronados,
   open water). Recorded side by side in `surface-iron.md` §common failures
   with the water-type discriminator stated.
4. **The Cedros vs. Coronados grade-and-behaviour contrast.** 30–45 lb fish
   taking the jig *"like slow"* versus 10–12 lb schoolies that *"hit it like a
   freight train"* — same species, same crew, same technique, two fisheries.
   This is the kind of thing that reads as a contradiction if the two sessions
   are merged; it is recorded as a contrast with the practical consequence
   (a Coronados hookset habit costs fish at Cedros).
5. **Dan Wade remains unregistered, so all of it caps at `medium`.** Cameron
   called him *"the best surface iron fisherman I know"*; the plan lists him as
   a Phase 6 registry candidate. Nothing here was written at `high` on the
   strength of that description — promoting him is Cameron's edit to
   `sources/source-registry.md`, and it would lift several of these notes.
6. **Product-launch contamination is heavy on this channel** and was handled
   per the sponsored-claim rule: mechanism and parameters at `medium`, named
   rod/reel/jig models and the Cedros lodge amenities at `low`. No operator or
   product recommendation was written.
7. **A dating hazard, not resolved.** `IhBY5RHFvuk` carries a 2026-01-24 upload
   date but says on camera that the rods drop "the second week of December" and
   calls the combo a 2026 go-to. The upload date is what is cited; the filming
   date is not established and was not guessed.

#### Correction — `Ob45hK4HSWc` location claim retracted (Cameron, 2026-08-17)

**What went wrong.** The first pass created `locations/ensenada.md`, a note
titled and framed around Ensenada, on the strength of one caption line —
*"we're gonna be fishing a little local here two hours only from border."*
The transcript **never names Ensenada**. "Ensenada" was my inference from a
travel time, written into the KB as an established place. Cameron caught it and
pointed out that Ensenada and the Coronado Islands are not the same spot, and
that the tuna pens in question are, in his read, at the Coronados.

**What the transcript actually establishes** (the whole geographic content of a
4-minute video):

- a landing whose name the captions garble beyond recovery
  ("bloom Towanda modest sportfishing");
- *"we usually head down to Castro's which is in that [garbled] about four
  hours away"* — the usual destination, not this one, and itself ASR-uncertain;
- *"we're gonna be fishing a little local here two hours only from border"*;
- *"the yellowtail are really close to the tuna pens, dropping straight down to
  about 120 feet."*

No Ensenada, no Punta Banda, no Coronado Islands.

**What was done.** `locations/ensenada.md` deleted; every link to it removed;
the technique content re-homed where it does not depend on a place claim —
`techniques/yo-yo-iron.md` §common failures (a bycatch species intercepting the
jig, and the fix being to stop fishing metal rather than to change metal) and a
`species/yellowtail.md` Situations row for tuna-pen fish at ~120 ft, carrying a
⚠ pointer to a Doctrine & conflicts entry that states the ambiguity and both
readings.

**Region gating was never at risk.** Ensenada, Punta Banda, and the Coronado
Islands are all `baja-pacific-north`, so the front-matter gate would have
excluded this row from a SoCal-bight day plan either way. The failure was at
the place-attribution layer that sits *below* the gate — which is exactly the
layer the batch-3 plan says is not yet modelled (assignment is at region level,
not spot level, per Cameron 2026-08-17).

**Process lesson, for the Phase 5 extractor prompt.** The extractor has an ASR
hazard rule and it worked — garbled *names* were correctly marked uncertain.
There is no equivalent rule for **inferred places**, where nothing is garbled
and the model simply supplies a plausible location from a travel time, a
species range, or a channel's usual haunts. That is a distinct and more
dangerous failure than a mis-transcribed word, because it reads as confident.
Add to the Phase 5 prompt: **a location may only be named in a note if it is
named in the source.** Travel times, drive distances, and channel habits are
evidence for a question, never an answer to it — a note that needs a place the
source does not give records the ambiguity instead.

### `HTowqnwAMeA` — Yellowtail 101 (BDOutdoors), extracted 2026-08-17

**Flagged by Cameron.** The transcript was **already in the repo** — it landed
with the BOLA zip in Phase 3 part 1 (`sources/transcripts/bdoutdoors/`, manifest
row present) but **no note cited it**. It is a landed-not-extracted miss, and
the reason is instructive: the file carries `playlist: BOLA` in its header, so
it came in on the Baja pass, but the content is **SoCal local-coast yellowtail**
— a mid-August day "above the border" plus a studio breakdown. A pass reading
for Baja material had no reason to stop on it. **Process implication for Phase
5: playlist membership is not subject matter.** The landing stage should not let
a playlist label stand in for triage, and the coverage check should assert that
every landed transcript reaches a destination or a logged skip — this one had
neither.

**Source standing.** `nate-winnicki` is in
[`sources/source-registry.md`](source-registry.md) (BDOutdoors, named
contributor), so this is a **registered voice**, not an unregistered channel —
but it is the first commit of these specific claims, so it lands at `medium`
pending repetition, following the precedent set for Cesar on
`EmZO8QiOfik`. Named rod/reel/hook/lure/line brands stay `low` per the
sponsored-claim rule. A second angler appears on camera named only as
"Marshall" — attribution incomplete, so his sounder read is `medium` on its own
terms regardless of the channel.

**⚠ Dating caveat.** The manifest and header both record
`upload_date: 2026-08-17`, which is **identical to `retrieved:`** — a pattern
that usually indicates a landing-time metadata artifact rather than a real
upload date. The only date evidence inside the video is *"it is mid August"*
spoken on camera. Notes cite **mid-August** and the video id; no day-precision
date is asserted anywhere, and the upload date is not treated as established.
Worth a sweep of the BOLA-zip rows for the same collision.

#### Destinations

| what | where |
| --- | --- |
| **Trolling hard baits to prospect a zone** — the purpose, the colour-by-light rule, the gear split at the 40 ft diver, the short-top-shot reasoning | `techniques/trolling.md` §SoCal local coast (new section) |
| **Slow-trolling live bait** — speed 1.5–3 mph chosen by bait size, 100–150 ft setback, the lever-drag-at-"2" boat-sets-the-hook method, 25–40 lb with a lighter option, fluoro matched to mainline, hook sizing | **`techniques/slow-trolling-bait.md` (new)** |
| **Two sounder reads** — stratified column vs. ball on the bottom; high-and-spread vs. tucked-to-the-bottom | `species/yellowtail.md` §Finding them |
| **The anchor→move decision**, the bite-rate calibration, and the column-layer map | `species/yellowtail.md` §Doctrine & conflicts |
| **Dropper-loop bait hooking** — roof of the mouth, mouth open, and why; upsize from flyline size | `techniques/dropper-loop.md` (new section) |
| **Yo-yo jig sizing by current** (with the free-spool time-budget mechanism), the **~45° cast-out angle**, colour picks | `techniques/yo-yo-iron.md` |

#### The flagged stub is retired

`species/yellowtail.md`'s **"Covering water to locate fish"** row had carried
`⚠ Flagged stub — no corpus source yet` since batch 1 — the KB had no source for
**trolling to locate** yellowtail, only trolling as a presentation. This video
covers it directly and by name (prospecting an unworked zone, between bites, or
with no recent report), so the row is now sourced and the stub marker removed.
**First flagged stub in the KB to be filled by a later batch** — the mechanism
CLAUDE.md describes for stubs worked as intended.

#### Findings worth recording

1. **A behavioural sounder read the KB did not have.** Every existing yellowtail
   sonar signature is a *depth* band. This source adds *distribution* as the
   discriminator — fish spread through the column are biting, the same fish
   tucked tight on the bottom are not — which is what tells you whether to work
   a mark at all, and which technique layer to use when you do.
2. **A colour rule that inverts the common habit.** Overcast → high-visibility;
   bright blue day → dark colours. Stated as a **contrast** principle rather
   than a match-the-hatch one. Recorded as his stated rule; no corpus source
   contradicts it, and none corroborates it yet.
3. **Bite-rate calibration is decision-relevant, not trivia.** Three or four
   bites on a good local day means two fishless hours is not evidence a
   technique is wrong. Logged in the router because it changes when a planner
   should recommend switching.
4. **Independent support for a cameron-adjacent framing.** The "don't be glued
   to a technique" lesson, arrived at by pulling anchor and quadrupling the
   bite rate, sits directly beside yellowtail.md's existing
   **"the faces are states, not types"** (cameron) doctrine — the same claim
   from the angler's side rather than the fish's. Recorded beside it, not
   merged into it.

### Registry pass — three promotions (Cameron, 2026-08-17)

Cameron reviewed the registry and promoted three voices. Rows added to
[`sources/source-registry.md`](source-registry.md); Shay McKinty explicitly
left unregistered (*"no idea who Shay McKinty is"*).

| voice | scope | Cameron's words |
| --- | --- | --- |
| `dan-wade` | unscoped | *"a local legend for surface iron fishing"* |
| `roman-castro` | unscoped | *"very knowledgeable"* |
| `ray-sharifi` | **region-scoped** | *"knows his stuff in SoCal, but I'd consider him an expert for Baja"* |

**`ray-sharifi` is the registry's first region-scoped row.** Baja/Cortez claims
are eligible for `high` on repetition; `socal-bight` claims cap at `medium`
regardless. This is only enforceable because batch 3 added the `regions`
vocabulary — the scope is mechanically checkable against a note's front matter,
and where one note carries both, **the claim is rated, not the note.**

**Registering a person does not register their channel.** Two rows now sit on
channels whose other voices are unregistered: `dan-wade` (Strictly Irons' own
host is a different, unregistered voice) and `nate-winnicki` (BDOutdoors
guests). `techniques/surface-iron.md` now states this split explicitly, because
otherwise its Wade material at `high` and its host material at `medium` read as
an inconsistency rather than a rule.

#### What actually changed, and what didn't

**63 confidence clauses rewritten** across 21 notes. The honest headline:
**only two blocks actually lifted to `high`.**

| lifted to `high` | why |
| --- | --- |
| Dan Wade's colour doctrine (`techniques/surface-iron-color.md`, note-level) | repeated — same answer, two channels, seven years apart |
| Dan Wade's kick mechanism (`techniques/surface-iron.md`) | stated in both videos |

Everything else **kept its `medium` rating and had only its stated reason
corrected**, for one of two reasons:

- **Single mention.** Registered + one video = `medium` under the rubric. This
  covers the wiring note, all of Roman Castro's own doctrine, and most of Ray
  Sharifi's. The correction matters anyway: the old text said *"unregistered
  channel"*, which told a reader nothing could lift it; the new text says
  *registered, single mention*, which tells them **a second source would.**
- **SoCal cap.** 36 Sharifi clauses are SoCal-bight content and now read
  `ray-sharifi registered, SoCal-capped`. 12 are Baja/Cortez
  (`WE643Fue1_A`, `A70kK2niu2Q`, `dEPuDrhoClM`) and read
  `ray-sharifi registered (Baja-scoped)` — eligible to lift when a second Baja
  source repeats them.

A split rating was applied inside `lures/iron-jigs.md` §Reading a jig: the
governing principle (judge a jig by whether it swims; carry a few different
swims) is in both Wade videos → `high`; the specific parameters (hip offset,
hole placement, concave-vs-flat, nose shape) are single-video → `medium`.

**Method note.** The sweep was done in two passes because a blind
find-and-replace would have corrupted neighbouring citations: these notes
interleave Sharifi/Castro blocks with StokedOnFishing blocks, which are
*genuinely* unregistered. Pass one handled the 12 clauses where the name and
the confidence claim sat on the same line; pass two matched each clause inside
a 320-character window after a name mention, classifying Sharifi by video id.
Zero neighbouring citations were touched.

**Not done, and deliberately so:** no claim was promoted to `high` on the
strength of the registry alone. The repeated-doctrine requirement was applied
as written, so most of this batch's promotions will only pay off when Phase 6's
seminars and Tackle Express supply corroborating sources.

### `jared-saaib` promoted, attribution held open (2026-08-17)

Cameron identified **Jared Saaib** as Strictly Irons' main voice and promoted
him — *"another local legend for surface iron fishing."* The registry row is
added. **The attribution mapping is deliberately NOT applied yet**, and the
reason is evidence, not caution for its own sake.

**What the corpus shows.** "Jared" appears in six Strictly Irons transcripts.
In **every instance the speaker is addressing Jared or referring to him in the
third person** — never introducing himself:

| video | line |
| --- | --- |
| `gdqI2dNd5_U` | *"hey jared we've been up here on this one"* |
| `2cxeg_AE418` | *"sorry Jared they're biting"* / *"Jared come here take this one"* |
| `_MygUHw19q8` | *"gosh Jared I just finished my meeting"* |
| `P36VGPPf120` | *"We got Rafa. We got Jared. We got Jeff."* — crew roll-call the narrator excludes himself from |
| `P36VGPPf120` | *"I called Jared. I was like, 'Jared…'"* |
| `EuTVPVY9lAs` | *"it wasn't Jared's like idea to call it the Righteous"* |

The `EuTVPVY9lAs` narrator is unambiguously the **brand owner** — he narrates
naming his own jig — and that last line is the only genuinely two-way one: it
reads either as *he is not Jared*, or as *he is Jared, disclaiming credit in
the third person*, which is a normal move in a testimony-style vlog. The other
five are hard to read as self-reference. No transcript contains a
self-introduction.

**Most likely reconciliation:** the camera changes hands on a multi-angler
boat, so "the channel's main voice" and "the narrator of this clip" need not be
the same person. That would make Cameron's identification correct *and* the
transcript evidence correct, while leaving per-clip attribution unresolved.

**Held open rather than guessed.** Blanket-crediting Strictly Irons narration
to a named real person on a channel where the narrator repeatedly addresses
that person by name is a worse error than leaving ratings at `medium`. The
on-the-water blocks in `techniques/surface-iron.md`,
`techniques/surface-iron-casting.md`, `locations/cedros-island.md`,
`species/yellowtail.md`, and `species/calico-bass.md` therefore stay attributed
to the channel at `medium` pending Cameron's call.

**This is the same failure class as the Ensenada retraction earlier in this
batch** — supplying a plausible identity the source does not state. There it
was a place; here it would be a person. The Phase 5 rule already drafted for
places ("a location may only be named in a note if it is named in the source")
should be **generalised to named people**: attribute to a person only where the
source identifies the speaker, or where Cameron has resolved the mapping
explicitly and that resolution is recorded here.

#### Resolved (Cameron, 2026-08-17): Strictly Irons defaults to Jared Saaib

Cameron's ruling on the attribution question above: **"If it's on his channel,
assume it's him unless the speaker is clearly identified (like when he had Dan
Wade). Most of the tutorial content is Jared."** Applied.

The transcript evidence is kept in the registry rather than discarded, so a
future reader knows this is a **ruling** and not something the captions
establish — the camera changing hands on a multi-angler boat explains why a
crewmate filming will address Jared by name on camera.

**Consequence: Strictly Irons ratings now turn on repetition, not registry
status.** Two blocks lifted to `high`; the rest are single-session and stay
`medium` with corrected attribution.

| block | rating | why |
| --- | --- | --- |
| Chum-the-school-up-then-cast (`techniques/surface-iron.md`) | **`high`** | the sequence and its rationale appear in `4pT0efBD1j0` **and** `dS9gd9k7A7Q` |
| The two finicky signatures (same note) | **`high`** | stated in `0DKmYId1NN4` **and** `ejUTAnONf7o` |
| Wind→trajectory, follow-through aim, soft cast, spool tension (`surface-iron-casting.md`) | `medium` | all from `IhBY5RHFvuk` alone |
| Mid-retrieve decisions — visible-jig speed, keep winding on a miss, burn-and-return, speed-up strike, don't-twitch-a-follower | `medium` | one session each |
| Cedros trip envelope (`locations/cedros-island.md`) | `medium` | three videos, but **one trip** — repetition across episodes of a single trip is not repeated doctrine |
| Tuna-pen row + wind→yo-yo row (`species/yellowtail.md`), Cedros calico row, yo-yo bycatch block | `medium` | single session each |

The **reel-sideways** detail in `surface-iron-casting.md` is now corroborated by
**two registered voices** — Dave Hansen (2021) and Jared Saaib (2026) — rather
than by one registered voice and one unregistered channel. That block was
already `high` on Hansen; it is now independently supported.

**Rule generalised for Phase 5.** The Ensenada retraction produced *"a location
may only be named in a note if it is named in the source."* This episode
extends it to people, with the escape hatch Cameron just used: **attribute to a
named person only where the source identifies the speaker, or where a
channel-level attribution rule has been recorded in the source registry.** The
registry is the right home for such rulings because it is already the file
Cameron edits to make trust decisions.

### Duane Diego Mellor — spelling corrected, and a sweep gap found (2026-08-17)

**Confirmed by Cameron: Duane Diego Mellor.** Four occurrences across
`techniques/sliding-sinker.md` and `techniques/dropper-loop.md` carried
"Malloy" and were corrected. Two section headings changed with them; checked
first for inbound anchor links — there were none, so nothing broke.

**It was an ASR artifact, not a typo.** The corpus genuinely contains both:

| where the text came from | renders as |
| --- | --- |
| human-typed YouTube titles (`KuVwmfF6RAo`, `yLpDI8jnizU`) | **Duane Diego Mellor** |
| auto-caption self-intro (`yLpDI8jnizU`) | **Duane Diego Mellor** |
| auto-caption self-intro, 3 Dockside Tutorials | *"Dwayne Diego Malloy"* |

The three Dockside Tutorials are where he introduces himself and the captions
mishear both names. The two affected notes were sourced from those videos, so
they inherited the mis-transcription. The registry row now records the alias
explicitly so a future search on either spelling lands, plus his **Pinnacle
Sportfishing** affiliation and the three Dockside video ids that were not
previously listed on his row.

**General lesson: human-typed metadata beats ASR for proper nouns.** Titles,
descriptions, and playlist names are typed by the uploader. Where a name
appears in both, the title wins. This should be an explicit extractor rule in
Phase 5 — the existing ASR-hazard rule tells the extractor to *flag*
uncertainty, but not that a title is available as a **higher-quality source for
the same fact**.

#### Sweep gap: line-wrapped names defeated the registry-status pass

Correcting these notes surfaced three citations the earlier registry sweep
missed, all for the same reason: **the person's name was itself wrapped across
a line break** (`Ray\n  Sharifi`), so a pattern matching `Ray Sharifi` with a
literal space never saw them.

| note | citation | fix |
| --- | --- | --- |
| `techniques/yo-yo-iron.md` | Sharifi, `WE643Fue1_A` (Cedros) | Baja-scoped |
| `techniques/dropper-loop.md` | Sharifi, `dEPuDrhoClM` (Sea of Cortez) | Baja-scoped |
| `techniques/hoop-netting.md` | Castro, second clause further down the section | registered, single source |

The third is a different failure: the clause sat in running prose well past the
parenthetical after the name, so a fixed look-ahead window would have missed it
even with the name intact. Re-verified with a newline-tolerant pattern —
**0 registry-status errors remain**, and "Malloy" appears in no knowledge note.

**Phase 5 implication:** any sweep keyed on a person's name must be
newline-tolerant, because this repo hard-wraps prose at ~78 characters and
names land on the wrap boundary regularly. Worth a small helper in
`link-maintenance.py` rather than ad-hoc regexes per pass.

### BOLA date concern — checked and withdrawn (2026-08-17)

Earlier in this batch I flagged that `HTowqnwAMeA` had `upload_date` identical
to its `retrieved` date and suggested the BOLA-zip rows might carry the same
landing-time artifact, implying other notes could be citing dates that were
never real. **That was an overstatement from a single instance, and the check
does not support it.** Measured across all 634 manifest rows and 69
transcripts:

- **1** transcript has `upload_date == retrieved` — `HTowqnwAMeA`, already
  flagged and already carrying its caveat.
- **0** future-dated rows.
- `retrieved` dates cluster into three clean landing batches (2026-08-12 ×18,
  2026-08-13 ×17, 2026-08-17 ×34) exactly matching the known landing sessions.

No systemic lander bug; nothing to sweep. Recorded rather than quietly dropped
because the concern is in the log above and a future reader would otherwise go
looking for a problem that isn't there.

**One real finding did come out of the fuller check: 37 manifest rows carry an
empty `upload_date`.** All 37 are `status: failed` — never transcribed — and
**zero** are cited in any knowledge note, so this is an accounting gap, not a
knowledge-integrity one. It becomes live in Phase 6: the re-transcription pass
that recovers those videos must also recover their upload dates, or they will
enter the KB undated and unable to satisfy CLAUDE.md's absolute-dates rule.

### Batch 3 — Searcher Sportfishing landed (2026-08-17)

Fifth corpus of the batch. **SearcherSportfishing** (UCEii853qfORr2W1j40xI0EA) —
a San Diego long-range sportboat's channel, `/videos` tab fully enumerated.

| | |
| --- | --- |
| entries listed | 470 (0 duplicate ids within the zip) |
| `ok` / landed | **347** — all auto-generated captions, 0 manual |
| `failed` | 123 — 120 no English caption track, 2 caption listed but no json3, 1 empty caption file |
| collides with repo | **1** — `CdjT_I_PBHQ` (Tackle Tip Thursday Vol. 230, already landed in an earlier batch); logged `duplicate-of`, not re-copied |
| net new transcripts | **346** |

Manifest normalized from the 8-column export schema to the repo's 7-column
schema; `channel` and `upload_date` read from each transcript's YAML header.
Verified after landing: 347 `ok` rows and 347 files on disk, exact match, no
orphans in either direction. Repo manifest now **1,103 rows**.

**Title-shape preview of the 347 landed** (mechanical, pre-triage):

| shape | count | note |
| --- | ---: | --- |
| **Tackle Tip Thursday** (numbered tutorial series) | **219** | the core value — a long-running, single-topic-per-episode how-to series |
| other | 115 | trip reports, crew/angler features, season commentary |
| **Tackle Talk Live** | 11 | long-form live Q&A |
| boat/maintenance | 2 | dry dock, engine — expected skips |

The Tackle Tip Thursday series is the densest tutorial run landed in any batch
so far by episode count, and it is **numbered**, which makes gaps visible: the
123 failures include several TTT volumes (94 Surgeon's Knot, 87 Yo-yo Fishing,
77 Big Tuna, 60 Fly Line Outfit among them), so the series has known holes to
re-source in the uncaptioned-recovery pass.

Not yet triaged or extracted — this corpus is queued for the autonomous
pipeline along with the rest of the batch-3 backlog.


## Batch 3 — autonomous worklist (built 2026-08-17)

Priority order is deliberate and is the main lever on how the remaining
weekly budget is spent: **the backlog cannot finish before the quota reset**
(~847 pending at batch-2's ~6.8 min/video is ~96 h of processing against a
39 h window), so the rows are ordered by **value density** and the run simply
stops wherever it stops.

| # | bucket | rows | depth | why here |
| --- | --- | ---: | --- | --- |
| 1 | seminars | 32 | `deep` | densest material in the whole corpus (~9,200 words/video median); batch-2 lesson L8 — seminars carry doctrine, on-the-water carries anecdote |
| 2 | Searcher — Tackle Tip Thursday | 219 | `deep` | numbered, single-topic-per-episode how-to series |
| 3 | Searcher — Tackle Talk Live | 11 | `deep` | long-form Q&A |
| 4 | Searcher — other | 108 | `decision-rationale` | trip footage → the C3 depth: decisions and their stated reasons |
| 5 | Tackle Express | 477 | `parameter-skim` | 86% of the videos but 34% of the words (~437 words/video); lowest density, so last |

**107 rows were pre-filtered straight to `skipped`** so they never cost a run:
120→ tackle-express promo/product and sub-200-word shorts with no technique
keyword, plus Searcher boat-maintenance/merch/event videos. Each carries its
reason in the result cell, per the plan's "log what the filter dropped" rule.

<!-- batch3:worklist:start -->

| video_id | channel | class | depth | status | result |
| --- | --- | --- | --- | --- | --- |
| -nIhadZwxAA | CustomRodandReel | seminar | deep | done | lures/knife-jigs.md; rigging/assist-hooks.md; techniques/slow-pitch-jigging.md / Extracted general SPJ mechanics (hook geometry, weight/current formula, boat control, braid strand-count, drag/fight technique, spawn-cycle jig sizing) from East Coast/Gulf seminar as labeled out-of-region contrast, medium confidence |
| 0HwYl0HO2tc | Orange County SUP FISHING | seminar | deep | done | techniques/glide-baits.md; species/calico-bass.md; species/rockfish-lingcod.md; species/sand-bass.md; species/yellowtail.md / new glide-bait technique note (low confidence, promotional seminar) linked from 4 species routers, 2 faithfulness defects fixed in review |
| 0ZYCT-lUStM | Big Rocco | freshwater | skip:freshwater-non-target | done | none / skipped: freshwater largemouth-bass seminar, out of SoCal/Baja saltwater fishery scope, log entry fixed to record reason |
| 1iV1GnF4K-c | Bad Company Fishing Adventures | seminar | deep | done | none / skipped: global blue/black marlin World Tour seminar (Atlantic/Indian/Pacific islands) — fleet logistics, veteran charity, and Atlantic-marlin-specific trolling technique explicitly flagged by speakers as non-transferable even across marlin species; no SoCal/Baja-specific decision knowledge in source |
| 46ha7J1Fc6A | Roman Castro | seminar | deep | done | lures/bay-bass-plastics.md; species/california-halibut.md; species/spotted-bay-bass.md; techniques/inshore-crankbaits.md; techniques/sliding-sinker.md / Booth-interview seminar (Fred Hall Show 2020): landed 5 attributed, medium-confidence, decision-rationale entries across bay-bass gear/lures, halibut fast-retrieve, bluefin sinker-rig cadence, and kelp treble-swap; fixed faithfulness defects before applying |
| 5Oh3IPIC5g4 | Fisher Newb | seminar | deep | done | species/california-halibut.md; species/dorado.md; species/rockfish-lingcod.md; species/sand-bass.md; species/sheephead.md; species/skipjack-tuna.md; species/yellowfin-tuna.md; species/yellowtail.md; techniques/glide-baits.md / Second HookUp Baits seminar merged as attributed low-confidence source into glide-baits.md; 8 species routers gained a linked row/bullet each |
| 8XrMkWPRxgs | Utah Spahghettzi Björker | seminar | deep | done | conditions/kelp-paddies.md; planning/electronics-and-sounder.md; planning/fleet-intelligence.md / repeated-doctrine merge from Dave Hansen's earlier (2019-03-12) Fred Hall seminar into three existing notes, antedating and upgrading confidence on paddy-approach, restock-timing, sounder-manual-range, VHF-channel, and boat-chasing doctrine |
| 8txprrsY9Os | jdmarnell | freshwater | skip:freshwater-non-target | done | none / freshwater largemouth-bass seminar, out of SoCal/Baja saltwater scope, correctly skipped; only defect was an un-logged pending row, fixed |
| 9JnIS8HkZlA | Fishing From San Diego | seminar | deep | done | tackle/bluefin-rig-ladder-by-grade.md; techniques/two-speed-low-gear-fight.md; species/bluefin-tuna.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; rigging/essential-knots.md; lures/tuna-feathers-and-skirts.md; techniques/fighting-big-bluefin.md / deep extraction of Steve Carson's 4-rig bluefin line-class ladder, circle-vs-J hook picks by grade, two-speed low-gear fighting technique, drag-setting method; two new notes created |
| AH4Eiya1Hn0 | Your Saltwater Guide | seminar | deep | done | lures/bay-bass-plastics.md; lures/cedar-plug.md; sources/regulatory-claims.md; species/rockfish-lingcod.md; species/spotted-bay-bass.md; techniques/hoop-netting.md; techniques/rockfish-deep-dropping.md / faithful multi-destination seminar extraction (tide/wind bay-bass doctrine, cedar-plug daisy chain, CCCA reg claim + GPS-drop + lobster-bait doctrine, Ingram St Bridge); fixed a blended misquote, unsupported claim, and unflagged ASR guess |
| BskCsKaTiZw | Your Saltwater Guide | seminar | deep | done | conditions/current-diagnostics.md; planning/search-and-glassing.md / seminar/deep extraction: chart-plotter-arrows-are-wind-not-current diagnostic + same-spot re-anchor-on-current-reversal doctrine, unregistered host, medium confidence |
| EcQK5elTPJE | Your Saltwater Guide | seminar | deep | done | locations/bahia-magdalena-lopez-mateos.md; species/snook.md; techniques/mangrove-structure-livebait.md; techniques/sliding-sinker.md; tackle/gear-classes.md / Lopez Mateos/Magdalena Bay location note + snook species router + mangrove livebait technique + boca grouper/snook leader addition |
| Et2TUskzCSs | James Kikkawa | seminar | deep | done | tackle/bluefin-rig-ladder-by-grade.md; tackle/line-and-leader.md; techniques/knife-jigging.md; techniques/slow-pitch-jigging.md / Jigging 101 panel extraction: PE-rated rod/drag ladder, line-diameter-over-label doctrine, speed-jig ring-vs-swivel and fight-technique doctrine, slow-pitch pitch-counting mechanics |
| G1YIlakiRqg | SD Fish and Sips | seminar | deep | done | bait/fishing-live-bait.md; lures/knife-jigs.md; rigging/rubber-band-deep-rig.md; rigging/wind-on-leader.md; tackle/bluefin-rig-ladder-by-grade.md; tackle/hooks.md; techniques/knife-jigging.md; techniques/two-speed-low-gear-fight.md / Capt. Matt/Gavin bluefin day/night tactics seminar merged into 8 existing notes |
| JK2-cpaXkI8 | Your Saltwater Guide | seminar | deep | done | conditions/current-diagnostics.md; planning/search-and-glassing.md; species/sand-bass.md; techniques/chunking.md / attribution correction (BskCsKaTiZw host confirmed as dave-hansen) + heading-check/reset procedure + chum-tube device + sand-bass migration/bait-size rationale |
| JiJYamo0QHk | Utah Spahghettzi Björker | seminar | deep | done | seminar/deep extraction of Dave Hansen's live Fred Hall Show 2019 Part 2 talk merged into 10 existing notes (bird cast cue, chart color-age reading, fleet-avoidance restatement, kite/leader line-class + single-hook conflict, lobster 7/day bag limit regulatory claim, flat-fall program-philosophy tradeoff, one-fish-at-a-time fighting rule, breezer front-approach mechanism, kite skip-not-fly mechanism + 8.5kt corroboration); one spliced/altered quote fixed in review -> conditions/bird-reading.md; conditions/water-color.md; planning/fleet-intelligence.md; rigging/flying-fish-harness.md… |
| KD-RSfCE6kg | Fisher Newb | freshwater | skip:freshwater-non-target | done | freshwater Ned rig/Midwest finesse largemouth-bass seminar correctly out of scope for SoCal/Baja saltwater KB; extractor left the log row at pending with no diff -- fixed the log entry to record the skip and reason -> none |
| LqW32NSkObY | Fisher Newb | seminar | deep | done | seminar/deep extraction -- kayak-specific bass tactics (Tommy Ponce), new kayak-bass-fishing technique note plus doctrine additions to current/water-color conditions notes and both bass species routers, one regulatory row (bag limit, correctly formatted) -> conditions/current-diagnostics.md; conditions/water-color.md; species/calico-bass.md; species/sand-bass.md; sources/regulatory-claims.md; techniques/kayak-bass-fishing.md |
| NXvqLUZ6qp8 | Fisher Newb | seminar | deep | done | Deep seminar extraction (garbled ASR, unregistered single-mention speaker/product pitch) merged into three existing notes and one new technique note (cheater-troll), correctly capped at medium/low confidence per the sponsored-claim rule; fixed a missing router-table link and one weak inference -> lures/bay-bass-plastics.md; lures/soft-plastic-swimbaits.md; tackle/line-and-leader.md; techniques/slow-trolling-bait.md; techniques/cheater-troll.md; species/yellowtail.md |
| Q196GVwVqro | Your Saltwater Guide | seminar | deep | done | seminar/deep extraction: Ahi USA Live Deception flash jig (low-confidence, subscription-pitch cap), small-boat (20-30ft) bluefin circle-fighting variant (low), and an Observed near-record-lobster-lost-to-stopping anecdote (medium) merged additively into existing notes, correctly capped per source-registry precedent -> lures/tuna-poppers-and-stickbaits.md; techniques/fighting-big-bluefin.md; techniques/hoop-netting.md |
| RUuPNpK0x-s | n6yun | seminar | deep | done | locations/breakwalls-jetties-riprap.md; species/calico-bass.md; techniques/drop-shot.md; techniques/inshore-crankbaits.md; techniques/swimbaits.md / Fred Hall calico-bass panel: wall-casting/countdown method, night bite, light-angle & dawn/dusk timing, twilight pre-spawn depth, halibut weedless drop-shot rig, bay improvisation tactics, freshwater crossover baits, surf/bay-mouth anchored presentation, weightless weedless-slug walking retrieve |
| UP_3fBu7VPA | Fisher Newb | seminar | deep | done | bait/fishing-live-bait.md; rigging/rubber-band-deep-rig.md; tackle/bluefin-rig-ladder-by-grade.md; tackle/rod-and-reel-selection.md; techniques/knife-jigging.md; techniques/yo-yo-iron.md / seminar deep-extracted into 6 existing notes (belly/nose/butt hook rationale, brawler rig, two-speed threshold + line-class ladder, spinning-reel criteria, depth-marking, yo-yo jig-by-depth); one inversion fixed (nose vs butt hook in heavy current) |
| XyKF34C5iB4 | Time On The Water | seminar | deep | done | bait/fishing-live-bait.md; conditions/current-structure.md; locations/breakwalls-jetties-riprap.md; locations/island-structure.md; lures/soft-plastic-swimbaits.md; planning/search-and-glassing.md; rigging/wiring-a-surface-iron.md; species/calico-bass.md; species/sand-bass.md; species/spotted-bay-bass.md; techniques/glide-baits.md; techniques/inshore-crankbaits.md; techniques/surface-iron-color.md; techniques/night-bass-fishing.md; techniques/spinnerbaits.md / seminar/deep extraction, applied with 6 faithfulness/routing fixes; two new technique notes (night-bass-fishing, spinnerbaits) |
| ZoIzpyyS9xw | n6yun | seminar | deep | done | locations/breakwalls-jetties-riprap.md; lures/soft-plastic-swimbaits.md; species/calico-bass.md; tackle/line-and-leader.md; techniques/swimbaits.md / Fred Hall Show calico bass panel extracted for trophy-bait sizing, line-class-rating obsolescence, spool/braid-diameter mechanics, confidence-color doctrine, scent use, kelp-beach presentation, and live-bait-vs-plastic reasoning |
| bM2vUS1B-yQ | Your Saltwater Guide | seminar | deep | done | bait/bait-tanks.md; bait/making-bait.md; planning/electronics-and-sounder.md; species/bluefin-trolling.md; tackle/hooks.md; techniques/chunking.md / seminar/deep extraction, 6 doctrine additions across bait/electronics/trolling/hooks/chunking, all faithful and confidence-correct |
| gimFbgN5Jjk | James Kikkawa | seminar | deep | done | seminar/deep extraction across 8 destinations (7 amended + 1 new tackle note on spiral-wrap guides/narrow reels); one speaker misattribution fixed (Mag Bay bottom-fishing passage reassigned Brian Wen -> Benny Ortiz) |
| iAr6sbRC384 | Fisher Newb | seminar | deep | pending |  |
| lP6cg4eEU6s | Fisher Newb | seminar | deep | pending |  |
| m-M0iwX8DjA | Your Saltwater Guide | seminar | deep | pending |  |
| ouBrIdO7d4k | SD Fish and Sips | seminar | deep | pending |  |
| sIoNELGlxmk | Your Saltwater Guide | seminar | deep | pending |  |
| ztpj1Xll0-U | Your Saltwater Guide | seminar | deep | pending |  |
| -62xDo4UQzo | SearcherSportfishing | tutorial | deep | pending |  |
| -BO1lMCTamg | SearcherSportfishing | tutorial | deep | pending |  |
| -OJ1FED7mxI | SearcherSportfishing | tutorial | deep | pending |  |
| -QnMvV4j_oM | SearcherSportfishing | tutorial | deep | pending |  |
| -hY20bxz3oM | SearcherSportfishing | tutorial | deep | pending |  |
| 0AtmEH6aQt0 | SearcherSportfishing | tutorial | deep | pending |  |
| 0Be1ARfvYaw | SearcherSportfishing | tutorial | deep | pending |  |
| 0E9REoTjKrY | SearcherSportfishing | tutorial | deep | pending |  |
| 0hQJxESLTm4 | SearcherSportfishing | tutorial | deep | pending |  |
| 0n4mJ3sfIqk | SearcherSportfishing | tutorial | deep | pending |  |
| 0xJqOtkmHqY | SearcherSportfishing | tutorial | deep | pending |  |
| 0zgmoOH3Qag | SearcherSportfishing | tutorial | deep | pending |  |
| 1uYIApdQQSM | SearcherSportfishing | tutorial | deep | pending |  |
| 1wFoa11jPxQ | SearcherSportfishing | tutorial | deep | pending |  |
| 25sd2gZAIZ8 | SearcherSportfishing | tutorial | deep | pending |  |
| 2O4Z0S78KLg | SearcherSportfishing | tutorial | deep | pending |  |
| 2TmLaSCmfC8 | SearcherSportfishing | tutorial | deep | pending |  |
| 2fwj24S9S-o | SearcherSportfishing | tutorial | deep | pending |  |
| 3FghhsYAIFI | SearcherSportfishing | tutorial | deep | pending |  |
| 3djuTW9GBr0 | SearcherSportfishing | tutorial | deep | pending |  |
| 3g82igEL8yk | SearcherSportfishing | tutorial | deep | pending |  |
| 3gNTB4aMhCA | SearcherSportfishing | tutorial | deep | pending |  |
| 3gykKyPdOvA | SearcherSportfishing | tutorial | deep | pending |  |
| 3zXcrGsIL-c | SearcherSportfishing | tutorial | deep | pending |  |
| 46wHgdTJWIM | SearcherSportfishing | tutorial | deep | pending |  |
| 4PY5H_YPJxY | SearcherSportfishing | tutorial | deep | pending |  |
| 5472APCgym8 | SearcherSportfishing | tutorial | deep | pending |  |
| 5CvFDpvlfSE | SearcherSportfishing | tutorial | deep | pending |  |
| 5IN1wsOFR-k | SearcherSportfishing | tutorial | deep | pending |  |
| 5J7a6UwTA90 | SearcherSportfishing | tutorial | deep | pending |  |
| 5g7pK63hYnc | SearcherSportfishing | tutorial | deep | pending |  |
| 5pbA-wXoric | SearcherSportfishing | tutorial | deep | pending |  |
| 5ppQob4N3Xw | SearcherSportfishing | tutorial | deep | pending |  |
| 6D_mf5gOfrM | SearcherSportfishing | tutorial | deep | pending |  |
| 6T3xZ9vufrM | SearcherSportfishing | tutorial | deep | pending |  |
| 6_E5JCRvazc | SearcherSportfishing | tutorial | deep | pending |  |
| 6wVlDDno2TE | SearcherSportfishing | tutorial | deep | pending |  |
| 6wbO7qaU3sI | SearcherSportfishing | tutorial | deep | pending |  |
| 7Ljt-DeFVcs | SearcherSportfishing | tutorial | deep | pending |  |
| 7T6dIYqr3KI | SearcherSportfishing | tutorial | deep | pending |  |
| 7TPJsMc_clA | SearcherSportfishing | tutorial | deep | pending |  |
| 7iSGGb9ueAk | SearcherSportfishing | tutorial | deep | pending |  |
| 7ivBSL-mhW8 | SearcherSportfishing | tutorial | deep | pending |  |
| 83HROAgGW6Q | SearcherSportfishing | tutorial | deep | pending |  |
| 8A8y7LmRwVQ | SearcherSportfishing | tutorial | deep | pending |  |
| 8MayoweWrAM | SearcherSportfishing | tutorial | deep | pending |  |
| 8UAtGqEjDtU | SearcherSportfishing | tutorial | deep | pending |  |
| 9-3B-WRWqus | SearcherSportfishing | tutorial | deep | pending |  |
| 91ZJbhAnzMg | SearcherSportfishing | tutorial | deep | pending |  |
| 9IhmYstB8sA | SearcherSportfishing | tutorial | deep | pending |  |
| 9_lwOzaLmXo | SearcherSportfishing | tutorial | deep | pending |  |
| AGaVlYu61O4 | SearcherSportfishing | tutorial | deep | pending |  |
| AodUBhxPts8 | SearcherSportfishing | tutorial | deep | pending |  |
| Aorcd0Om7eI | SearcherSportfishing | tutorial | deep | pending |  |
| AyN9MBWg-XY | SearcherSportfishing | tutorial | deep | pending |  |
| BLbUu_mfMJY | SearcherSportfishing | tutorial | deep | pending |  |
| BacIrmOK-Bo | SearcherSportfishing | tutorial | deep | pending |  |
| BcX-tp3I7LE | SearcherSportfishing | tutorial | deep | pending |  |
| Bn9fRKUmQ-U | SearcherSportfishing | tutorial | deep | pending |  |
| Bo5Fj-XuWHo | SearcherSportfishing | tutorial | deep | pending |  |
| Bz0WZNAofks | SearcherSportfishing | tutorial | deep | pending |  |
| CXrF7K4lKxE | SearcherSportfishing | tutorial | deep | pending |  |
| CdjT_I_PBHQ | SearcherSportfishing | tutorial | deep | pending |  |
| E9YtH56Dngo | SearcherSportfishing | tutorial | deep | pending |  |
| ETw_3AFxEcM | SearcherSportfishing | tutorial | deep | pending |  |
| EfaxxszOYFI | SearcherSportfishing | tutorial | deep | pending |  |
| F9XjGMEvvag | SearcherSportfishing | tutorial | deep | pending |  |
| FN9-rgyC9ic | SearcherSportfishing | tutorial | deep | pending |  |
| G81HN0dIDg0 | SearcherSportfishing | tutorial | deep | pending |  |
| GXXvT7pS2fM | SearcherSportfishing | tutorial | deep | pending |  |
| GcgcnloKeZ4 | SearcherSportfishing | tutorial | deep | pending |  |
| H5NHGLm1H5U | SearcherSportfishing | tutorial | deep | pending |  |
| HH1YvOfMWx0 | SearcherSportfishing | tutorial | deep | pending |  |
| ILA6OMInWSM | SearcherSportfishing | tutorial | deep | pending |  |
| IaVqJgUfcM8 | SearcherSportfishing | tutorial | deep | pending |  |
| Ixyi1mY3Qeg | SearcherSportfishing | tutorial | deep | pending |  |
| J0NJhN6-Thg | SearcherSportfishing | tutorial | deep | pending |  |
| J3FGJj5zYPE | SearcherSportfishing | tutorial | deep | pending |  |
| J7nreDb1dn8 | SearcherSportfishing | tutorial | deep | pending |  |
| JHMCguO7sXE | SearcherSportfishing | tutorial | deep | pending |  |
| JOanxql39qg | SearcherSportfishing | tutorial | deep | pending |  |
| KGrussv1s3U | SearcherSportfishing | tutorial | deep | pending |  |
| KHYoj9GEjCM | SearcherSportfishing | tutorial | deep | pending |  |
| KLmNyflzsQ0 | SearcherSportfishing | tutorial | deep | pending |  |
| KYE14piJAzI | SearcherSportfishing | tutorial | deep | pending |  |
| LpReZmYQSCU | SearcherSportfishing | tutorial | deep | pending |  |
| M-W5mEjh1MY | SearcherSportfishing | tutorial | deep | pending |  |
| MC3FTRRoOag | SearcherSportfishing | tutorial | deep | pending |  |
| MjPY-nWZJ54 | SearcherSportfishing | tutorial | deep | pending |  |
| MuC0uGKDzxg | SearcherSportfishing | tutorial | deep | pending |  |
| NGtja-dCiC8 | SearcherSportfishing | tutorial | deep | pending |  |
| NJ9ZLAU3sls | SearcherSportfishing | tutorial | deep | pending |  |
| NN5MWeRA28o | SearcherSportfishing | tutorial | deep | pending |  |
| OIiDJu4mx44 | SearcherSportfishing | tutorial | deep | pending |  |
| OL8D1l73RVg | SearcherSportfishing | tutorial | deep | pending |  |
| OmyRIw7Eye8 | SearcherSportfishing | tutorial | deep | pending |  |
| P9H-bpzT7eU | SearcherSportfishing | tutorial | deep | pending |  |
| PS8CRYwTPiU | SearcherSportfishing | tutorial | deep | pending |  |
| PYlqIODuIPQ | SearcherSportfishing | tutorial | deep | pending |  |
| PjLa3oGm4Qg | SearcherSportfishing | tutorial | deep | pending |  |
| QTWVs5BwQ0g | SearcherSportfishing | tutorial | deep | pending |  |
| Qa6Q8mOAV6I | SearcherSportfishing | tutorial | deep | pending |  |
| R48YdVFfEOI | SearcherSportfishing | tutorial | deep | pending |  |
| RM7cBgCDWFA | SearcherSportfishing | tutorial | deep | pending |  |
| RNRFrfepiW0 | SearcherSportfishing | tutorial | deep | pending |  |
| Rudzy0DD08w | SearcherSportfishing | tutorial | deep | pending |  |
| S2cT2JqrWcY | SearcherSportfishing | tutorial | deep | pending |  |
| S80GRyuAbLY | SearcherSportfishing | tutorial | deep | pending |  |
| SCQnyVEQfHY | SearcherSportfishing | tutorial | deep | pending |  |
| Stw7SNyIgdg | SearcherSportfishing | tutorial | deep | pending |  |
| TU5quAG4atM | SearcherSportfishing | tutorial | deep | pending |  |
| TgOMUXxIQl4 | SearcherSportfishing | tutorial | deep | pending |  |
| Ud3hi9r1Nr4 | SearcherSportfishing | tutorial | deep | pending |  |
| UfuQr6gOIk8 | SearcherSportfishing | tutorial | deep | pending |  |
| UtYO1ubQFz0 | SearcherSportfishing | tutorial | deep | pending |  |
| UyfcYoNV2sg | SearcherSportfishing | tutorial | deep | pending |  |
| VW2t_G8eorI | SearcherSportfishing | tutorial | deep | pending |  |
| VcJManCizRE | SearcherSportfishing | tutorial | deep | pending |  |
| VxHYxXmPoWQ | SearcherSportfishing | tutorial | deep | pending |  |
| VyFpIk-Na9Q | SearcherSportfishing | tutorial | deep | pending |  |
| W6RuHvaqkHs | SearcherSportfishing | tutorial | deep | pending |  |
| WxlDxFjB8oQ | SearcherSportfishing | tutorial | deep | pending |  |
| X1zAA4DLOr0 | SearcherSportfishing | tutorial | deep | pending |  |
| XTsTpWnk1gU | SearcherSportfishing | tutorial | deep | pending |  |
| Y2XZ34-Tpa0 | SearcherSportfishing | tutorial | deep | pending |  |
| YJX-hYEIcNM | SearcherSportfishing | tutorial | deep | pending |  |
| Y_ElKixrhsc | SearcherSportfishing | tutorial | deep | pending |  |
| Yd3J4igs-QA | SearcherSportfishing | tutorial | deep | pending |  |
| YeV--HarEYQ | SearcherSportfishing | tutorial | deep | pending |  |
| YtlD1gQ_ULw | SearcherSportfishing | tutorial | deep | pending |  |
| ZECOKmD4fIs | SearcherSportfishing | tutorial | deep | pending |  |
| ZKb13fNT6P0 | SearcherSportfishing | tutorial | deep | pending |  |
| Zhn-VDrlaLM | SearcherSportfishing | tutorial | deep | pending |  |
| _VtL0DrNdAU | SearcherSportfishing | tutorial | deep | pending |  |
| _Z4yMtrYgeA | SearcherSportfishing | tutorial | deep | pending |  |
| _jDXMtCrUZg | SearcherSportfishing | tutorial | deep | pending |  |
| _rf1TqLh1yE | SearcherSportfishing | tutorial | deep | pending |  |
| aAqKHeyBwEo | SearcherSportfishing | tutorial | deep | pending |  |
| aD0Iim9C15o | SearcherSportfishing | tutorial | deep | pending |  |
| an_uw-5pjfw | SearcherSportfishing | tutorial | deep | pending |  |
| b-oixz7pgAo | SearcherSportfishing | tutorial | deep | pending |  |
| bEFhWtGBdBU | SearcherSportfishing | tutorial | deep | pending |  |
| bbn-aJGRH5o | SearcherSportfishing | tutorial | deep | pending |  |
| cpUq7Z3UOwU | SearcherSportfishing | tutorial | deep | pending |  |
| cx7tKXHmiY4 | SearcherSportfishing | tutorial | deep | pending |  |
| ddataaVWoDc | SearcherSportfishing | tutorial | deep | pending |  |
| dg1sbr6GuB8 | SearcherSportfishing | tutorial | deep | pending |  |
| dkY7wJ4UM1c | SearcherSportfishing | tutorial | deep | pending |  |
| e1-tPTNejBo | SearcherSportfishing | tutorial | deep | pending |  |
| eLFVhVyyOTw | SearcherSportfishing | tutorial | deep | pending |  |
| eLPTMO3-_1Q | SearcherSportfishing | tutorial | deep | pending |  |
| eZXPqiAtqi8 | SearcherSportfishing | tutorial | deep | pending |  |
| ew7Lru8wmQs | SearcherSportfishing | tutorial | deep | pending |  |
| ewfWc7MTBPk | SearcherSportfishing | tutorial | deep | pending |  |
| fg2v1kxoTMA | SearcherSportfishing | tutorial | deep | pending |  |
| fgTmUq78ofQ | SearcherSportfishing | tutorial | deep | pending |  |
| fyJA3o2hVh0 | SearcherSportfishing | tutorial | deep | pending |  |
| gaHpCc_tc78 | SearcherSportfishing | tutorial | deep | pending |  |
| gqEjWrPpa48 | SearcherSportfishing | tutorial | deep | pending |  |
| h0NyGvIaDc8 | SearcherSportfishing | tutorial | deep | pending |  |
| hlmDnAct1cA | SearcherSportfishing | tutorial | deep | pending |  |
| hteLeDIy9Qs | SearcherSportfishing | tutorial | deep | pending |  |
| i1Ul0XCG36o | SearcherSportfishing | tutorial | deep | pending |  |
| icpm7gADxvU | SearcherSportfishing | tutorial | deep | pending |  |
| iqTN2IBRP1A | SearcherSportfishing | tutorial | deep | pending |  |
| it_YYh_8Z-w | SearcherSportfishing | tutorial | deep | pending |  |
| jDmHgRNnqhw | SearcherSportfishing | tutorial | deep | pending |  |
| jJG6FWNXkok | SearcherSportfishing | tutorial | deep | pending |  |
| jLFZIh15Fec | SearcherSportfishing | tutorial | deep | pending |  |
| jQzOdmP0zoQ | SearcherSportfishing | tutorial | deep | pending |  |
| jqyu3wZdNF4 | SearcherSportfishing | tutorial | deep | pending |  |
| k4U3ETqmlEc | SearcherSportfishing | tutorial | deep | pending |  |
| kdEKEyVTIGU | SearcherSportfishing | tutorial | deep | pending |  |
| kuvfoJKpLYU | SearcherSportfishing | tutorial | deep | pending |  |
| kzpeM56Gh7o | SearcherSportfishing | tutorial | deep | pending |  |
| m2g97MxmAGI | SearcherSportfishing | tutorial | deep | pending |  |
| m424-XxCFQw | SearcherSportfishing | tutorial | deep | pending |  |
| nAGkYWuJrCI | SearcherSportfishing | tutorial | deep | pending |  |
| nM7B5NQLy44 | SearcherSportfishing | tutorial | deep | pending |  |
| nWq2DVzBNeI | SearcherSportfishing | tutorial | deep | pending |  |
| nnrEjc-Gq2o | SearcherSportfishing | tutorial | deep | pending |  |
| o6Sawz5S7bk | SearcherSportfishing | tutorial | deep | pending |  |
| otnnAon3F9Q | SearcherSportfishing | tutorial | deep | pending |  |
| ouoyP7t2Nus | SearcherSportfishing | tutorial | deep | pending |  |
| p9xeMl-r_CY | SearcherSportfishing | tutorial | deep | pending |  |
| pB10vaDaETM | SearcherSportfishing | tutorial | deep | pending |  |
| pCd6QykcZ0w | SearcherSportfishing | tutorial | deep | pending |  |
| pQ9kGqgsX8I | SearcherSportfishing | tutorial | deep | pending |  |
| pm8u6qUrVUI | SearcherSportfishing | tutorial | deep | pending |  |
| ptoIvB2MspE | SearcherSportfishing | tutorial | deep | pending |  |
| qBP3qRnK4H4 | SearcherSportfishing | tutorial | deep | pending |  |
| q_ciF1xiDiI | SearcherSportfishing | tutorial | deep | pending |  |
| qtCZAB4EBs4 | SearcherSportfishing | tutorial | deep | pending |  |
| r9bF3VtzDUg | SearcherSportfishing | tutorial | deep | pending |  |
| rFmWrp-Vndo | SearcherSportfishing | tutorial | deep | pending |  |
| rNiQKb3sCh4 | SearcherSportfishing | tutorial | deep | pending |  |
| riEkdu8PEds | SearcherSportfishing | tutorial | deep | pending |  |
| rziFyx7SRGI | SearcherSportfishing | tutorial | deep | pending |  |
| scScYJJF95Y | SearcherSportfishing | tutorial | deep | pending |  |
| sfZhPSTvZy8 | SearcherSportfishing | tutorial | deep | pending |  |
| sjOJiR6_HJ4 | SearcherSportfishing | tutorial | deep | pending |  |
| sjlL5GidM58 | SearcherSportfishing | tutorial | deep | pending |  |
| t8GP_-DMlSU | SearcherSportfishing | tutorial | deep | pending |  |
| tRlv1azFPlM | SearcherSportfishing | tutorial | deep | pending |  |
| tYebwLzTyf8 | SearcherSportfishing | tutorial | deep | pending |  |
| tio1oeibVlM | SearcherSportfishing | tutorial | deep | pending |  |
| tjBeR9tWd4s | SearcherSportfishing | tutorial | deep | pending |  |
| tnHltcDdVtU | SearcherSportfishing | tutorial | deep | pending |  |
| ueDBCY1mIPk | SearcherSportfishing | tutorial | deep | pending |  |
| vNIazq1aVwc | SearcherSportfishing | tutorial | deep | pending |  |
| vVOkxHx58Eg | SearcherSportfishing | tutorial | deep | pending |  |
| vn4fmPxUqsU | SearcherSportfishing | tutorial | deep | pending |  |
| wGWjnW7wCiI | SearcherSportfishing | tutorial | deep | pending |  |
| wnlOU34RXs8 | SearcherSportfishing | tutorial | deep | pending |  |
| wqrIs5kg1qw | SearcherSportfishing | tutorial | deep | pending |  |
| yGXSrUauo2w | SearcherSportfishing | tutorial | deep | pending |  |
| ypr-qZF4FTY | SearcherSportfishing | tutorial | deep | pending |  |
| zkA1jqHXXD0 | SearcherSportfishing | tutorial | deep | pending |  |
| zuAuk-Kfa1Y | SearcherSportfishing | tutorial | deep | pending |  |
| 49joKHD7Umc | SearcherSportfishing | seminar | deep | pending |  |
| 4uNPLknRAQg | SearcherSportfishing | seminar | deep | pending |  |
| FETSTtbCMII | SearcherSportfishing | seminar | deep | pending |  |
| FXWOIB0TPfE | SearcherSportfishing | seminar | deep | pending |  |
| QHY5kmU7OTU | SearcherSportfishing | seminar | deep | pending |  |
| SAltQjih0ms | SearcherSportfishing | seminar | deep | pending |  |
| YntRJAN88fs | SearcherSportfishing | seminar | deep | pending |  |
| eehDVb6_GoI | SearcherSportfishing | seminar | deep | pending |  |
| lf3S28nh-kk | SearcherSportfishing | seminar | deep | pending |  |
| shZCjX2-fkI | SearcherSportfishing | seminar | deep | pending |  |
| tpmOYXYQwhU | SearcherSportfishing | seminar | deep | pending |  |
| -II7kzpklzE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 1axjidotnfE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 2pTRbsDwTO4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 38kxKgR4q2s | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 3kGAA-T8IGw | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 5m1cHclspII | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 6BqmPN0xGZY | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 6I5Ma8n8PRE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 76cj579gnTo | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 7xnTtlaYs58 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 8gEvmdj0lec | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 8vJEyJVBvSM | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 8wK37e921F8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| 9fVsfdOgUMI | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| A3PW3EMsu8c | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| ACL2BD6gbkE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| AJzAbQ0i3QY | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| B1r0T6f5kgM | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Bk0-P4oeFiU | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| CSpBymCVWN4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| C_MmNnJrdrQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Dr_npFZYLM4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| ELd90j4ZukI | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| EfAThf5gOFw | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| FIAvWu02xko | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| FPZBm0oFvKc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Fdaq28LwK0I | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| HAxYMiqkBDs | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| HCC1uhsPSas | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| HJdwm0bn0H8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| HeRoKbDCDTw | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Ibt0vdrl48E | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Ij04nagr8g8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| J52jzaMnKA0 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| J61iyNrfqsg | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| JUSWISdzIq0 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| JWU3djUbfKY | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| K4GTUO57rio | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| KrIednxCEKI | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| L6BUIu5vFEc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| LYjdT3E3Rb4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| LuSn3IeW9_c | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| MPC_OQjvO-o | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| NeSw-4df4H4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| NgdpWzPRlqQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Nj_9ORYJhkg | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Ntwb6fU2zl4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| OfJ_KI_D184 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| PKwvkOOYzto | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Psiiza6YQyE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| QMTCBY-kKeE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| QOV9d0qTcEE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| QeU9J5XVhP4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Qk6Q1UJMTpQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| RhULLaUsEDk | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| S6Ic8aXDdIg | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Sx40JvCXFuA | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| URJm6qDHgqg | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| UUiaoQVexy0 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| UYfvRQk_xT8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| VB_GYSk_vdY | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Vphyeoxd7R4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| XngQMsyvtNM | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Y97blHr1F8k | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| Y9Ke1shXpwc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| YeYO998pX0M | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| ZIJAvAEW_tU | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| ZY-cTuFtjh8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| ZcIiucZlBcM | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| _f5QmWSUUx8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| _r08B4bItAY | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| aXqFrQSNrDc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| atboDq5tZ0Q | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| b9JThf2Jm0s | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| cjbAQ20Q9bQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| ck6REMbJkww | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| drARx5Fpy-s | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| eIAKA8Jgopk | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| fHtTbZAWz1g | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| fcdWAo0VAKw | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| g1C-FK6o4nA | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| gQb_3MW6L9M | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| jH0q4UPjwC0 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| jU7qi40WTzQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| kYZqFRBUDYg | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| kqsg_t5MIzY | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| lYyi_Yh3S5g | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| pNNrYXlgkO4 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| phRsYlu0mmc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| sAwPTPnHNzk | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| so1df8prECw | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| srHnaMIrVIA | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| tj_mEL94ETg | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| uPnM-qw696k | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| uWGGeDOprsE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| uXWliLLPzss | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| utTcrpscYHQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| v8tPYYKM2JE | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| vJGGfJfdDAk | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| vMRLjvSQBNA | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| wt-3dlbMGJc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| x0_v2COShBo | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| xU6Rp1YJjm8 | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| xo7njK7vXHQ | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| y0LVT59inEA | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| y__TVzcePik | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| yidQY2NeXtM | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| zKovnvOwlFc | SearcherSportfishing | on-the-water | decision-rationale | pending |  |
| -BCEGxojaT4 | Tackle Express | tutorial | parameter-skim | pending |  |
| -FQ3cSdvnK0 | Tackle Express | tutorial | parameter-skim | pending |  |
| -KHdjYwefmM | Tackle Express | tutorial | parameter-skim | pending |  |
| -Ocrnb4rmMo | Tackle Express | tutorial | parameter-skim | pending |  |
| -zw76Sh7YCI | Tackle Express | tutorial | parameter-skim | pending |  |
| 05uB5V_jWTg | Tackle Express | tutorial | parameter-skim | pending |  |
| 0OpWO3Yo4HE | Tackle Express | tutorial | parameter-skim | pending |  |
| 0PAPH1uqk4A | Tackle Express | tutorial | parameter-skim | pending |  |
| 0_pEeh0n9Uo | Tackle Express | tutorial | parameter-skim | pending |  |
| 0pBFS6TLVUQ | Tackle Express | tutorial | parameter-skim | pending |  |
| 0z0bvF7o3ak | Tackle Express | tutorial | parameter-skim | pending |  |
| 17sBBD0C4XY | Tackle Express | tutorial | parameter-skim | pending |  |
| 1MxHXTv3a2A | Tackle Express | tutorial | parameter-skim | pending |  |
| 1YKT275onlU | Tackle Express | tutorial | parameter-skim | pending |  |
| 1e6Oz5rAwRU | Tackle Express | tutorial | parameter-skim | pending |  |
| 1l05hEXDaWw | Tackle Express | tutorial | parameter-skim | pending |  |
| 1nBqYdvVrXY | Tackle Express | tutorial | parameter-skim | pending |  |
| 28FQZvZ8v6k | Tackle Express | tutorial | parameter-skim | pending |  |
| 2DfGpewNRYc | Tackle Express | tutorial | parameter-skim | pending |  |
| 2Ee2DFZ9Wk4 | Tackle Express | tutorial | parameter-skim | pending |  |
| 2QphkC2cK14 | Tackle Express | tutorial | parameter-skim | pending |  |
| 2c8UomduE3c | Tackle Express | tutorial | parameter-skim | pending |  |
| 2gmvTuXtu0Q | Tackle Express | tutorial | parameter-skim | pending |  |
| 2pkE9RwW1bU | Tackle Express | tutorial | parameter-skim | pending |  |
| 3-0kaaHqA7A | Tackle Express | tutorial | parameter-skim | pending |  |
| 3dyEQhMnPMU | Tackle Express | tutorial | parameter-skim | pending |  |
| 3n18taJWNEQ | Tackle Express | tutorial | parameter-skim | pending |  |
| 3xx_vES0kdo | Tackle Express | tutorial | parameter-skim | pending |  |
| 3z1KZ_kIaec | Tackle Express | tutorial | parameter-skim | pending |  |
| 41d5bquXkAc | Tackle Express | tutorial | parameter-skim | pending |  |
| 46kVgZ6P62M | Tackle Express | tutorial | parameter-skim | pending |  |
| 52jkCrA4I9w | Tackle Express | tutorial | parameter-skim | pending |  |
| 52le0jHiqyc | Tackle Express | tutorial | parameter-skim | pending |  |
| 53FzsW4_U08 | Tackle Express | tutorial | parameter-skim | pending |  |
| 5EKrtI_f_xA | Tackle Express | tutorial | parameter-skim | pending |  |
| 5Fxwebsi9pU | Tackle Express | tutorial | parameter-skim | pending |  |
| 5OTBOIeQmis | Tackle Express | tutorial | parameter-skim | pending |  |
| 5XWnm7ok09k | Tackle Express | tutorial | parameter-skim | pending |  |
| 5_z4pe7iH8k | Tackle Express | tutorial | parameter-skim | pending |  |
| 5fxAN1Ofn8M | Tackle Express | tutorial | parameter-skim | pending |  |
| 5hnHrCUNk3Q | Tackle Express | tutorial | parameter-skim | pending |  |
| 5uEzREjLlLQ | Tackle Express | tutorial | parameter-skim | pending |  |
| 6BzZotupVcs | Tackle Express | tutorial | parameter-skim | pending |  |
| 6E39_PBt1P4 | Tackle Express | tutorial | parameter-skim | pending |  |
| 6SClBs16L2Y | Tackle Express | tutorial | parameter-skim | pending |  |
| 6Z6Dht20kTA | Tackle Express | tutorial | parameter-skim | pending |  |
| 6dTz1640Y5c | Tackle Express | tutorial | parameter-skim | pending |  |
| 6gwvP8_pjWc | Tackle Express | tutorial | parameter-skim | pending |  |
| 6qz6aQ9PusA | Tackle Express | tutorial | parameter-skim | pending |  |
| 6sfaYq9wMvQ | Tackle Express | tutorial | parameter-skim | pending |  |
| 75lUj-uaArQ | Tackle Express | tutorial | parameter-skim | pending |  |
| 7AOtPUGwKDI | Tackle Express | tutorial | parameter-skim | pending |  |
| 7L7OVoXE7KU | Tackle Express | tutorial | parameter-skim | pending |  |
| 7iJktLzCmLY | Tackle Express | tutorial | parameter-skim | pending |  |
| 7wdCk_LXezw | Tackle Express | tutorial | parameter-skim | pending |  |
| 8FAgifEFSuU | Tackle Express | tutorial | parameter-skim | pending |  |
| 8TO-tuYjwWk | Tackle Express | tutorial | parameter-skim | pending |  |
| 8U34yMGxvEw | Tackle Express | tutorial | parameter-skim | pending |  |
| 8fSGyJL2GHM | Tackle Express | tutorial | parameter-skim | pending |  |
| 8wbNDfihH1o | Tackle Express | tutorial | parameter-skim | pending |  |
| 9-UtAaSacsc | Tackle Express | tutorial | parameter-skim | pending |  |
| 9MzNNwHiBXs | Tackle Express | tutorial | parameter-skim | pending |  |
| 9_iox_eRhpg | Tackle Express | tutorial | parameter-skim | pending |  |
| 9a-Zy_D6c3w | Tackle Express | tutorial | parameter-skim | pending |  |
| 9ekSBpLG0GA | Tackle Express | tutorial | parameter-skim | pending |  |
| 9hXW9JCffsU | Tackle Express | tutorial | parameter-skim | pending |  |
| 9kGpcEHqIUc | Tackle Express | tutorial | parameter-skim | pending |  |
| 9qwsg-e9ECA | Tackle Express | tutorial | parameter-skim | pending |  |
| A-D5MYB98yo | Tackle Express | tutorial | parameter-skim | pending |  |
| A6-KPjRwGSQ | Tackle Express | tutorial | parameter-skim | pending |  |
| A7rveRBkL-g | Tackle Express | tutorial | parameter-skim | pending |  |
| A8_ydUnS0CQ | Tackle Express | tutorial | parameter-skim | pending |  |
| AJfDjN-7K4w | Tackle Express | tutorial | parameter-skim | pending |  |
| ALZtbMIOMBw | Tackle Express | tutorial | parameter-skim | pending |  |
| AhICQlAsreU | Tackle Express | tutorial | parameter-skim | pending |  |
| B44kVCdUN0o | Tackle Express | tutorial | parameter-skim | pending |  |
| BGKH1ObX9Qs | Tackle Express | tutorial | parameter-skim | pending |  |
| BNJlltYOpIk | Tackle Express | tutorial | parameter-skim | pending |  |
| BNp-gSOpWBw | Tackle Express | tutorial | parameter-skim | pending |  |
| BPxE3xn3gAc | Tackle Express | tutorial | parameter-skim | pending |  |
| Basv01kFjOs | Tackle Express | tutorial | parameter-skim | pending |  |
| Bok0db0G4xE | Tackle Express | tutorial | parameter-skim | pending |  |
| BsWb5BQ1Tdc | Tackle Express | tutorial | parameter-skim | pending |  |
| BwDJ4VFvB3E | Tackle Express | tutorial | parameter-skim | pending |  |
| CNMXkml1okI | Tackle Express | tutorial | parameter-skim | pending |  |
| CO8YU-TD8D4 | Tackle Express | tutorial | parameter-skim | pending |  |
| CdgSBcN6PDo | Tackle Express | tutorial | parameter-skim | pending |  |
| CsKEtrcLgiQ | Tackle Express | tutorial | parameter-skim | pending |  |
| D0bQjAL0gGU | Tackle Express | tutorial | parameter-skim | pending |  |
| D0oEQsTaL7A | Tackle Express | tutorial | parameter-skim | pending |  |
| DPrr0a3vQY0 | Tackle Express | tutorial | parameter-skim | pending |  |
| DTvXJrtytwg | Tackle Express | tutorial | parameter-skim | pending |  |
| DfLcSS-J3g4 | Tackle Express | tutorial | parameter-skim | pending |  |
| DuNkl8F45NE | Tackle Express | tutorial | parameter-skim | pending |  |
| DvhRMHw57c4 | Tackle Express | tutorial | parameter-skim | pending |  |
| E273T9jAmpg | Tackle Express | tutorial | parameter-skim | pending |  |
| E4CDqBFOaP8 | Tackle Express | tutorial | parameter-skim | pending |  |
| E4H9QB7UBbU | Tackle Express | tutorial | parameter-skim | pending |  |
| EVqKoSZK5Dk | Tackle Express | tutorial | parameter-skim | pending |  |
| EXqFODWABvM | Tackle Express | tutorial | parameter-skim | pending |  |
| EcNijcqjLvE | Tackle Express | tutorial | parameter-skim | pending |  |
| Ecqt-ZLnvaU | Tackle Express | tutorial | parameter-skim | pending |  |
| EdN3BowjYjg | Tackle Express | tutorial | parameter-skim | pending |  |
| Eo_bA8IWvyU | Tackle Express | tutorial | parameter-skim | pending |  |
| EuYOlsnxXko | Tackle Express | tutorial | parameter-skim | pending |  |
| F0849S6gBPY | Tackle Express | tutorial | parameter-skim | pending |  |
| FR7Cg9Jqug4 | Tackle Express | tutorial | parameter-skim | pending |  |
| F_KDQo-k7CQ | Tackle Express | tutorial | parameter-skim | pending |  |
| Fj1-SsbksRM | Tackle Express | tutorial | parameter-skim | pending |  |
| G8HNjPiaOjU | Tackle Express | tutorial | parameter-skim | pending |  |
| Ga8Z1PyBqdE | Tackle Express | tutorial | parameter-skim | pending |  |
| GchQpXW2jI0 | Tackle Express | tutorial | parameter-skim | pending |  |
| GeydGK-62fw | Tackle Express | tutorial | parameter-skim | pending |  |
| H5Z-Mqt4qXs | Tackle Express | tutorial | parameter-skim | pending |  |
| HQC-NwW4018 | Tackle Express | tutorial | parameter-skim | pending |  |
| HQH_1XxBx7w | Tackle Express | tutorial | parameter-skim | pending |  |
| HXsiiSWsfOY | Tackle Express | tutorial | parameter-skim | pending |  |
| IHKuTb93XEU | Tackle Express | tutorial | parameter-skim | pending |  |
| IUuP8gGaAAo | Tackle Express | tutorial | parameter-skim | pending |  |
| IXHHNOX_t5Y | Tackle Express | tutorial | parameter-skim | pending |  |
| IZHY3RXdyxg | Tackle Express | tutorial | parameter-skim | pending |  |
| IcS7QbJlSDA | Tackle Express | tutorial | parameter-skim | pending |  |
| IqpeK5Xfhes | Tackle Express | tutorial | parameter-skim | pending |  |
| IxfTRWmMqQU | Tackle Express | tutorial | parameter-skim | pending |  |
| J40VxLNuZhk | Tackle Express | tutorial | parameter-skim | pending |  |
| JFauRUaz2AQ | Tackle Express | tutorial | parameter-skim | pending |  |
| JJwyof_Nxqs | Tackle Express | tutorial | parameter-skim | pending |  |
| JLaql6UUFVs | Tackle Express | tutorial | parameter-skim | pending |  |
| JNMwUUst1rw | Tackle Express | tutorial | parameter-skim | pending |  |
| JUcsUMJize0 | Tackle Express | tutorial | parameter-skim | pending |  |
| JekeeKZA1Kw | Tackle Express | tutorial | parameter-skim | pending |  |
| JgD1gOuQAaE | Tackle Express | tutorial | parameter-skim | pending |  |
| JgXMpjxRxmo | Tackle Express | tutorial | parameter-skim | pending |  |
| JmGT0zAaVOY | Tackle Express | tutorial | parameter-skim | pending |  |
| K50W5KaBN4E | Tackle Express | tutorial | parameter-skim | pending |  |
| KFdvKXTHSeU | Tackle Express | tutorial | parameter-skim | pending |  |
| KUsFT7tN-x0 | Tackle Express | tutorial | parameter-skim | pending |  |
| K_0AeM4OvuE | Tackle Express | tutorial | parameter-skim | pending |  |
| KamUiykeRlU | Tackle Express | tutorial | parameter-skim | pending |  |
| KjVLn4cWHbc | Tackle Express | tutorial | parameter-skim | pending |  |
| KqluHwsDicw | Tackle Express | tutorial | parameter-skim | pending |  |
| LAQZOoEUZA0 | Tackle Express | tutorial | parameter-skim | pending |  |
| LB9sUjDcRUw | Tackle Express | tutorial | parameter-skim | pending |  |
| LKOL9g-qhSM | Tackle Express | tutorial | parameter-skim | pending |  |
| LRRoGT2W4WY | Tackle Express | tutorial | parameter-skim | pending |  |
| L_YH_xT7Pfs | Tackle Express | tutorial | parameter-skim | pending |  |
| Lj2NCznK7Zg | Tackle Express | tutorial | parameter-skim | pending |  |
| LoJu3OYs20o | Tackle Express | tutorial | parameter-skim | pending |  |
| M2qZiY2lR98 | Tackle Express | tutorial | parameter-skim | pending |  |
| M4G8IKsZEFU | Tackle Express | tutorial | parameter-skim | pending |  |
| M9_nvBPajDU | Tackle Express | tutorial | parameter-skim | pending |  |
| M9nIhEsKsqU | Tackle Express | tutorial | parameter-skim | pending |  |
| ME2jrqS_5bo | Tackle Express | tutorial | parameter-skim | pending |  |
| MKe-Xu4XsGk | Tackle Express | tutorial | parameter-skim | pending |  |
| MbYjzhHsiTU | Tackle Express | tutorial | parameter-skim | pending |  |
| N24NBweNK4o | Tackle Express | tutorial | parameter-skim | pending |  |
| NBSJsN7uTKQ | Tackle Express | tutorial | parameter-skim | pending |  |
| NF8AJjqsDO8 | Tackle Express | tutorial | parameter-skim | pending |  |
| NGkXPkE8kWI | Tackle Express | tutorial | parameter-skim | pending |  |
| NGvwjJfAL2I | Tackle Express | tutorial | parameter-skim | pending |  |
| NJh9EadWA7Y | Tackle Express | tutorial | parameter-skim | pending |  |
| NUlHwrBT61U | Tackle Express | tutorial | parameter-skim | pending |  |
| NiEvdaHOHnM | Tackle Express | tutorial | parameter-skim | pending |  |
| Nsc23Chy3xk | Tackle Express | tutorial | parameter-skim | pending |  |
| O49WsHP4Zh0 | Tackle Express | tutorial | parameter-skim | pending |  |
| O5t36yWGXCU | Tackle Express | tutorial | parameter-skim | pending |  |
| OFEpEeFomp4 | Tackle Express | tutorial | parameter-skim | pending |  |
| OKFUMvJbacE | Tackle Express | tutorial | parameter-skim | pending |  |
| OURS05qEGcA | Tackle Express | tutorial | parameter-skim | pending |  |
| OdRZIDBO6Mg | Tackle Express | tutorial | parameter-skim | pending |  |
| Oi5n-uVpY9g | Tackle Express | tutorial | parameter-skim | pending |  |
| OitNR_M4lxw | Tackle Express | tutorial | parameter-skim | pending |  |
| Ol3RPAsImg0 | Tackle Express | tutorial | parameter-skim | pending |  |
| OuO4Irjrat8 | Tackle Express | tutorial | parameter-skim | pending |  |
| Ow87j6AALAY | Tackle Express | tutorial | parameter-skim | pending |  |
| OxFyTk0CSZQ | Tackle Express | tutorial | parameter-skim | pending |  |
| PJEG_RIkzF0 | Tackle Express | tutorial | parameter-skim | pending |  |
| PNWsFa4iSSc | Tackle Express | tutorial | parameter-skim | pending |  |
| PPCzxTzXF0k | Tackle Express | tutorial | parameter-skim | pending |  |
| PbiZMk4Ft6w | Tackle Express | tutorial | parameter-skim | pending |  |
| PcJUo7h8WQA | Tackle Express | tutorial | parameter-skim | pending |  |
| PciIsDkBgj4 | Tackle Express | tutorial | parameter-skim | pending |  |
| PfHjk3G0yek | Tackle Express | tutorial | parameter-skim | pending |  |
| Pn3BcC_IN9Y | Tackle Express | tutorial | parameter-skim | pending |  |
| PnAnAS6QoG8 | Tackle Express | tutorial | parameter-skim | pending |  |
| PoTRe9SRjm8 | Tackle Express | tutorial | parameter-skim | pending |  |
| Pxky7drjPkU | Tackle Express | tutorial | parameter-skim | pending |  |
| PzjZxCRKXpc | Tackle Express | tutorial | parameter-skim | pending |  |
| Q14rHkHGBsk | Tackle Express | tutorial | parameter-skim | pending |  |
| Q4WWkbc9nag | Tackle Express | tutorial | parameter-skim | pending |  |
| Q4sW6JRQzAY | Tackle Express | tutorial | parameter-skim | pending |  |
| Q6ACpkS93sk | Tackle Express | tutorial | parameter-skim | pending |  |
| QEmxUIGmKbo | Tackle Express | tutorial | parameter-skim | pending |  |
| QEpa3WYbEa8 | Tackle Express | tutorial | parameter-skim | pending |  |
| QJd7A6oiV4U | Tackle Express | tutorial | parameter-skim | pending |  |
| QJeYLzFEbzs | Tackle Express | tutorial | parameter-skim | pending |  |
| QP6c8vcslVs | Tackle Express | tutorial | parameter-skim | pending |  |
| QQlQcPXARWk | Tackle Express | tutorial | parameter-skim | pending |  |
| QTq-G2y237w | Tackle Express | tutorial | parameter-skim | pending |  |
| Qj6brwOJk9E | Tackle Express | tutorial | parameter-skim | pending |  |
| Qqdt6f8Mjd4 | Tackle Express | tutorial | parameter-skim | pending |  |
| R0TQ7Afsh6Y | Tackle Express | tutorial | parameter-skim | pending |  |
| R1spZEO1V-0 | Tackle Express | tutorial | parameter-skim | pending |  |
| R4yYK90-cZM | Tackle Express | tutorial | parameter-skim | pending |  |
| R6ErrEIjlWw | Tackle Express | tutorial | parameter-skim | pending |  |
| RKfI8g_aRu8 | Tackle Express | tutorial | parameter-skim | pending |  |
| RbOWJ0BAqSo | Tackle Express | tutorial | parameter-skim | pending |  |
| RoBoQ6kulwA | Tackle Express | tutorial | parameter-skim | pending |  |
| Rtwz0oEfrKw | Tackle Express | tutorial | parameter-skim | pending |  |
| S0-BCQWA0H4 | Tackle Express | tutorial | parameter-skim | pending |  |
| S9sQ8Vg8-5o | Tackle Express | tutorial | parameter-skim | pending |  |
| SDNXNdGdmSQ | Tackle Express | tutorial | parameter-skim | pending |  |
| SH5CZQi9ATw | Tackle Express | tutorial | parameter-skim | pending |  |
| SK2M7L2vA1s | Tackle Express | tutorial | parameter-skim | pending |  |
| SL4zZbzdXNA | Tackle Express | tutorial | parameter-skim | pending |  |
| SR-Fv3xxkVY | Tackle Express | tutorial | parameter-skim | pending |  |
| Sb20NtuNlkc | Tackle Express | tutorial | parameter-skim | pending |  |
| SbTEGKmWl7g | Tackle Express | tutorial | parameter-skim | pending |  |
| SclIN_ceduA | Tackle Express | tutorial | parameter-skim | pending |  |
| Se7bjtiiGv8 | Tackle Express | tutorial | parameter-skim | pending |  |
| T33JsoZHO_c | Tackle Express | tutorial | parameter-skim | pending |  |
| T_XpItMhbjM | Tackle Express | tutorial | parameter-skim | pending |  |
| TdrFjnJb3Y0 | Tackle Express | tutorial | parameter-skim | pending |  |
| TjQuU-x8sHM | Tackle Express | tutorial | parameter-skim | pending |  |
| To2Dvx3Ifnc | Tackle Express | tutorial | parameter-skim | pending |  |
| TwnvOIp38tI | Tackle Express | tutorial | parameter-skim | pending |  |
| TyxH9BBJ9U8 | Tackle Express | tutorial | parameter-skim | pending |  |
| TzK4iuVmUSE | Tackle Express | tutorial | parameter-skim | pending |  |
| UASU-ikU1AQ | Tackle Express | tutorial | parameter-skim | pending |  |
| UXt-pR6bBjY | Tackle Express | tutorial | parameter-skim | pending |  |
| U_jXfgsGBzM | Tackle Express | tutorial | parameter-skim | pending |  |
| UbbkPKZ8_W4 | Tackle Express | tutorial | parameter-skim | pending |  |
| UtFX1K01bA4 | Tackle Express | tutorial | parameter-skim | pending |  |
| UtgMbyjlem8 | Tackle Express | tutorial | parameter-skim | pending |  |
| V1tmGZh3MNg | Tackle Express | tutorial | parameter-skim | pending |  |
| V4opuMirbDU | Tackle Express | tutorial | parameter-skim | pending |  |
| V54mcLzTubc | Tackle Express | tutorial | parameter-skim | pending |  |
| VH5_kvuGGQY | Tackle Express | tutorial | parameter-skim | pending |  |
| V_WjP52OJ7M | Tackle Express | tutorial | parameter-skim | pending |  |
| Vbf40qvH9-Q | Tackle Express | tutorial | parameter-skim | pending |  |
| Vjdv8o7otKY | Tackle Express | tutorial | parameter-skim | pending |  |
| Vl0BuetK2D0 | Tackle Express | tutorial | parameter-skim | pending |  |
| VotK9jwqRJ8 | Tackle Express | tutorial | parameter-skim | pending |  |
| W0mj_LA-qcM | Tackle Express | tutorial | parameter-skim | pending |  |
| WHLz0kR___I | Tackle Express | tutorial | parameter-skim | pending |  |
| WPYrq_jdK2o | Tackle Express | tutorial | parameter-skim | pending |  |
| WeabGOvhgto | Tackle Express | tutorial | parameter-skim | pending |  |
| Wk4wKFLbWEQ | Tackle Express | tutorial | parameter-skim | pending |  |
| X-itrm5QkcM | Tackle Express | tutorial | parameter-skim | pending |  |
| XY4ZYDqD4Ag | Tackle Express | tutorial | parameter-skim | pending |  |
| XfpUV_z5gFI | Tackle Express | tutorial | parameter-skim | pending |  |
| XtPUnC5jQnM | Tackle Express | tutorial | parameter-skim | pending |  |
| XxN7EzNDnf8 | Tackle Express | tutorial | parameter-skim | pending |  |
| Y5crw_rQpeg | Tackle Express | tutorial | parameter-skim | pending |  |
| YWTDpG6yYWo | Tackle Express | tutorial | parameter-skim | pending |  |
| YyW4-8FRjn8 | Tackle Express | tutorial | parameter-skim | pending |  |
| ZGs9kF4HHIM | Tackle Express | tutorial | parameter-skim | pending |  |
| ZMrCAG7Cqmg | Tackle Express | tutorial | parameter-skim | pending |  |
| ZolfRTcJBk4 | Tackle Express | tutorial | parameter-skim | pending |  |
| ZrcwcugaEe4 | Tackle Express | tutorial | parameter-skim | pending |  |
| _3f8_JxtDRo | Tackle Express | tutorial | parameter-skim | pending |  |
| _8Bno5mP4QE | Tackle Express | tutorial | parameter-skim | pending |  |
| _C7TJoGT0nw | Tackle Express | tutorial | parameter-skim | pending |  |
| _L6mE8ip5l8 | Tackle Express | tutorial | parameter-skim | pending |  |
| _QgS6QUcvFs | Tackle Express | tutorial | parameter-skim | pending |  |
| _RfXwHSaG48 | Tackle Express | tutorial | parameter-skim | pending |  |
| _XfScSliRVk | Tackle Express | tutorial | parameter-skim | pending |  |
| _eON-xT2mOE | Tackle Express | tutorial | parameter-skim | pending |  |
| _rcxIWhNMSE | Tackle Express | tutorial | parameter-skim | pending |  |
| aF_16nVNch4 | Tackle Express | tutorial | parameter-skim | pending |  |
| aFsyWOLIM48 | Tackle Express | tutorial | parameter-skim | pending |  |
| aKQqNbgISHY | Tackle Express | tutorial | parameter-skim | pending |  |
| aauujAuF1hc | Tackle Express | tutorial | parameter-skim | pending |  |
| af7a1tR2B84 | Tackle Express | tutorial | parameter-skim | pending |  |
| ajYmUmHdPEI | Tackle Express | tutorial | parameter-skim | pending |  |
| akUrZ_OYy4c | Tackle Express | tutorial | parameter-skim | pending |  |
| akX66b5WGZA | Tackle Express | tutorial | parameter-skim | pending |  |
| aqZxUmefwcw | Tackle Express | tutorial | parameter-skim | pending |  |
| au3EkXJswY8 | Tackle Express | tutorial | parameter-skim | pending |  |
| auiXY0R9ri8 | Tackle Express | tutorial | parameter-skim | pending |  |
| bB8zs0lXvvo | Tackle Express | tutorial | parameter-skim | pending |  |
| bCQLyxKQAok | Tackle Express | tutorial | parameter-skim | pending |  |
| bi2X9ANvDBs | Tackle Express | tutorial | parameter-skim | pending |  |
| blG8NnDhQ1c | Tackle Express | tutorial | parameter-skim | pending |  |
| bvYMtjbflq8 | Tackle Express | tutorial | parameter-skim | pending |  |
| cAZRaGB_RRM | Tackle Express | tutorial | parameter-skim | pending |  |
| cBATKqWkQws | Tackle Express | tutorial | parameter-skim | pending |  |
| cNfPlAZWLB8 | Tackle Express | tutorial | parameter-skim | pending |  |
| cSTfQy8eb44 | Tackle Express | tutorial | parameter-skim | pending |  |
| cZ3KlPWiPWw | Tackle Express | tutorial | parameter-skim | pending |  |
| c_60Ms3QSMY | Tackle Express | tutorial | parameter-skim | pending |  |
| c_L2hqBXwYA | Tackle Express | tutorial | parameter-skim | pending |  |
| c_YgwlJdsSk | Tackle Express | tutorial | parameter-skim | pending |  |
| d0fxBYmAnIk | Tackle Express | tutorial | parameter-skim | pending |  |
| d31ID9JHgns | Tackle Express | tutorial | parameter-skim | pending |  |
| d93vB_EBu30 | Tackle Express | tutorial | parameter-skim | pending |  |
| dBAk9NScxSc | Tackle Express | tutorial | parameter-skim | pending |  |
| dDvNAZpmx-8 | Tackle Express | tutorial | parameter-skim | pending |  |
| dFRpcvkLmb0 | Tackle Express | tutorial | parameter-skim | pending |  |
| dKSnFf5IsmY | Tackle Express | tutorial | parameter-skim | pending |  |
| dNn8U9LbL8c | Tackle Express | tutorial | parameter-skim | pending |  |
| dTJihVPudgQ | Tackle Express | tutorial | parameter-skim | pending |  |
| dWqD8l3jW6w | Tackle Express | tutorial | parameter-skim | pending |  |
| degWvtQ4D_Y | Tackle Express | tutorial | parameter-skim | pending |  |
| dfv6S7RQ_bs | Tackle Express | tutorial | parameter-skim | pending |  |
| dnHev1PcLts | Tackle Express | tutorial | parameter-skim | pending |  |
| dpz4M1IEYQg | Tackle Express | tutorial | parameter-skim | pending |  |
| dt3FXL-HjVo | Tackle Express | tutorial | parameter-skim | pending |  |
| dvmyKsk5BCo | Tackle Express | tutorial | parameter-skim | pending |  |
| eLwier3zVdo | Tackle Express | tutorial | parameter-skim | pending |  |
| eMAM6cjzANI | Tackle Express | tutorial | parameter-skim | pending |  |
| eOLoHxoqk6E | Tackle Express | tutorial | parameter-skim | pending |  |
| ejkr3z7xkJA | Tackle Express | tutorial | parameter-skim | pending |  |
| enDs3G5bpDc | Tackle Express | tutorial | parameter-skim | pending |  |
| epuNd10icxQ | Tackle Express | tutorial | parameter-skim | pending |  |
| eqRMpfcuM2s | Tackle Express | tutorial | parameter-skim | pending |  |
| eqeESarhRrE | Tackle Express | tutorial | parameter-skim | pending |  |
| f0gBoLc7scw | Tackle Express | tutorial | parameter-skim | pending |  |
| f1pZI-bfMz4 | Tackle Express | tutorial | parameter-skim | pending |  |
| f22V2HCv8tI | Tackle Express | tutorial | parameter-skim | pending |  |
| f9JOpLrYBiE | Tackle Express | tutorial | parameter-skim | pending |  |
| fATd3sje6R4 | Tackle Express | tutorial | parameter-skim | pending |  |
| fHMwcm1xRQk | Tackle Express | tutorial | parameter-skim | pending |  |
| fPxqoEforhA | Tackle Express | tutorial | parameter-skim | pending |  |
| fVtiwvqhzgI | Tackle Express | tutorial | parameter-skim | pending |  |
| fnaGBGbrhqU | Tackle Express | tutorial | parameter-skim | pending |  |
| foLSQJ5oRWI | Tackle Express | tutorial | parameter-skim | pending |  |
| g5yDzjORhho | Tackle Express | tutorial | parameter-skim | pending |  |
| gFx8BXU2vkY | Tackle Express | tutorial | parameter-skim | pending |  |
| gQ-SwPzmJWM | Tackle Express | tutorial | parameter-skim | pending |  |
| gdACAKN8T7A | Tackle Express | tutorial | parameter-skim | pending |  |
| gg1W2lLwm34 | Tackle Express | tutorial | parameter-skim | pending |  |
| ghHQe3fP9U4 | Tackle Express | tutorial | parameter-skim | pending |  |
| gn2yquuU6eM | Tackle Express | tutorial | parameter-skim | pending |  |
| h311A3s-dkY | Tackle Express | tutorial | parameter-skim | pending |  |
| h3ZM-mnSNJ8 | Tackle Express | tutorial | parameter-skim | pending |  |
| hAryw1v3I68 | Tackle Express | tutorial | parameter-skim | pending |  |
| hBAxFcjts5A | Tackle Express | tutorial | parameter-skim | pending |  |
| hJjNZf-JYSs | Tackle Express | tutorial | parameter-skim | pending |  |
| hMLwRt6Sxn8 | Tackle Express | tutorial | parameter-skim | pending |  |
| hSJL9KhKngA | Tackle Express | tutorial | parameter-skim | pending |  |
| hXcgczEYcKE | Tackle Express | tutorial | parameter-skim | pending |  |
| hc8n16HQO_E | Tackle Express | tutorial | parameter-skim | pending |  |
| hjZ3hgq0Bzg | Tackle Express | tutorial | parameter-skim | pending |  |
| hkUH9vkt68Q | Tackle Express | tutorial | parameter-skim | pending |  |
| hmz8n_9MzZA | Tackle Express | tutorial | parameter-skim | pending |  |
| hokc5FLmSjA | Tackle Express | tutorial | parameter-skim | pending |  |
| i4rJy9Uwb-U | Tackle Express | tutorial | parameter-skim | pending |  |
| i6G6vX0tKn4 | Tackle Express | tutorial | parameter-skim | pending |  |
| iBdz2SfeA1g | Tackle Express | tutorial | parameter-skim | pending |  |
| iHwvUl0dhxk | Tackle Express | tutorial | parameter-skim | pending |  |
| iQjTILHaxqo | Tackle Express | tutorial | parameter-skim | pending |  |
| ijNOphK4XRA | Tackle Express | tutorial | parameter-skim | pending |  |
| ijjtpoKZp8U | Tackle Express | tutorial | parameter-skim | pending |  |
| j0btC9J0Wcc | Tackle Express | tutorial | parameter-skim | pending |  |
| jFlAdWRj3HI | Tackle Express | tutorial | parameter-skim | pending |  |
| jWPv-OOM3uk | Tackle Express | tutorial | parameter-skim | pending |  |
| j_x1IskkSEE | Tackle Express | tutorial | parameter-skim | pending |  |
| jeJAsY_M0oc | Tackle Express | tutorial | parameter-skim | pending |  |
| jo8lMdFZ1bk | Tackle Express | tutorial | parameter-skim | pending |  |
| k0rhryq2kYI | Tackle Express | tutorial | parameter-skim | pending |  |
| k23JzE3Fr-I | Tackle Express | tutorial | parameter-skim | pending |  |
| kHUQd9jqG-A | Tackle Express | tutorial | parameter-skim | pending |  |
| kR-t-z1PPCE | Tackle Express | tutorial | parameter-skim | pending |  |
| k_ocIsSD6vQ | Tackle Express | tutorial | parameter-skim | pending |  |
| klb0VSg_I3w | Tackle Express | tutorial | parameter-skim | pending |  |
| kt3G72gUldM | Tackle Express | tutorial | parameter-skim | pending |  |
| kuIKWNZ3Koo | Tackle Express | tutorial | parameter-skim | pending |  |
| lNXZD79BvJY | Tackle Express | tutorial | parameter-skim | pending |  |
| lYnD_MiALL8 | Tackle Express | tutorial | parameter-skim | pending |  |
| l_L0PdOOWGs | Tackle Express | tutorial | parameter-skim | pending |  |
| m6NxHaIifj8 | Tackle Express | tutorial | parameter-skim | pending |  |
| mDRSoMYxDuY | Tackle Express | tutorial | parameter-skim | pending |  |
| mMa0oqI2tqA | Tackle Express | tutorial | parameter-skim | pending |  |
| mgUjxUoGkZU | Tackle Express | tutorial | parameter-skim | pending |  |
| mgsCmVxM8dM | Tackle Express | tutorial | parameter-skim | pending |  |
| nF6MosH63HY | Tackle Express | tutorial | parameter-skim | pending |  |
| nJPQVouJQ0g | Tackle Express | tutorial | parameter-skim | pending |  |
| nORwiYXBQmQ | Tackle Express | tutorial | parameter-skim | pending |  |
| nRIAgz5G_Bc | Tackle Express | tutorial | parameter-skim | pending |  |
| nZfEB7466ys | Tackle Express | tutorial | parameter-skim | pending |  |
| nizu9cpPXUs | Tackle Express | tutorial | parameter-skim | pending |  |
| nlrSBi_hrrg | Tackle Express | tutorial | parameter-skim | pending |  |
| nnQFIho8sa0 | Tackle Express | tutorial | parameter-skim | pending |  |
| ntS17IEKyJ0 | Tackle Express | tutorial | parameter-skim | pending |  |
| nwjIEWJyjKU | Tackle Express | tutorial | parameter-skim | pending |  |
| nwmIqR2VgfI | Tackle Express | tutorial | parameter-skim | pending |  |
| o5TR7y6-q6A | Tackle Express | tutorial | parameter-skim | pending |  |
| o7Kd0aNAijQ | Tackle Express | tutorial | parameter-skim | pending |  |
| oGCAX8dgR5o | Tackle Express | tutorial | parameter-skim | pending |  |
| okJCANlWWE4 | Tackle Express | tutorial | parameter-skim | pending |  |
| osAuU0W9zKA | Tackle Express | tutorial | parameter-skim | pending |  |
| ov0T5MPdl_E | Tackle Express | tutorial | parameter-skim | pending |  |
| p-gl7mLOeWw | Tackle Express | tutorial | parameter-skim | pending |  |
| p1KyyR0i7Kc | Tackle Express | tutorial | parameter-skim | pending |  |
| p9YYIb4GKHM | Tackle Express | tutorial | parameter-skim | pending |  |
| pL7ZGuMVwo4 | Tackle Express | tutorial | parameter-skim | pending |  |
| pMsbeLOgUc4 | Tackle Express | tutorial | parameter-skim | pending |  |
| pOFsjDTqaxY | Tackle Express | tutorial | parameter-skim | pending |  |
| pTenOTaHdUc | Tackle Express | tutorial | parameter-skim | pending |  |
| pa0MS0GK_2o | Tackle Express | tutorial | parameter-skim | pending |  |
| ptwN9MUDxjk | Tackle Express | tutorial | parameter-skim | pending |  |
| q0it3pyUW6Q | Tackle Express | tutorial | parameter-skim | pending |  |
| qHS-ewTQs9Q | Tackle Express | tutorial | parameter-skim | pending |  |
| qKOmJH_WtJo | Tackle Express | tutorial | parameter-skim | pending |  |
| qLDrhgE7-y0 | Tackle Express | tutorial | parameter-skim | pending |  |
| qLKLlZdiflA | Tackle Express | tutorial | parameter-skim | pending |  |
| qRrZakwbLoM | Tackle Express | tutorial | parameter-skim | pending |  |
| q_NMbHJ7QoQ | Tackle Express | tutorial | parameter-skim | pending |  |
| qh3hL2Dt3HY | Tackle Express | tutorial | parameter-skim | pending |  |
| r7Bv49Ysgdw | Tackle Express | tutorial | parameter-skim | pending |  |
| rBt096uru3U | Tackle Express | tutorial | parameter-skim | pending |  |
| rd2Ia8HRbSg | Tackle Express | tutorial | parameter-skim | pending |  |
| reG4Xc91Mj4 | Tackle Express | tutorial | parameter-skim | pending |  |
| reZBk4GsH_o | Tackle Express | tutorial | parameter-skim | pending |  |
| rlZVbEO3WyQ | Tackle Express | tutorial | parameter-skim | pending |  |
| rvmr9Jy9RjI | Tackle Express | tutorial | parameter-skim | pending |  |
| rxoaPT5Zaog | Tackle Express | tutorial | parameter-skim | pending |  |
| s2yqtaHriqU | Tackle Express | tutorial | parameter-skim | pending |  |
| s3hJuucTqUI | Tackle Express | tutorial | parameter-skim | pending |  |
| s7GMKI6c6RU | Tackle Express | tutorial | parameter-skim | pending |  |
| sGnY4QxqMmI | Tackle Express | tutorial | parameter-skim | pending |  |
| sJGs-Jqt9Vo | Tackle Express | tutorial | parameter-skim | pending |  |
| sPgP0aBUQm8 | Tackle Express | tutorial | parameter-skim | pending |  |
| sPs3Civek1w | Tackle Express | tutorial | parameter-skim | pending |  |
| sSH80AImFX4 | Tackle Express | tutorial | parameter-skim | pending |  |
| sj_9QYlGtGo | Tackle Express | tutorial | parameter-skim | pending |  |
| sl2MRqpiS60 | Tackle Express | tutorial | parameter-skim | pending |  |
| smdXDSyuVnY | Tackle Express | tutorial | parameter-skim | pending |  |
| t0kkwlrNwHk | Tackle Express | tutorial | parameter-skim | pending |  |
| t3kDnoGYfVs | Tackle Express | tutorial | parameter-skim | pending |  |
| t96ZBu0gvq4 | Tackle Express | tutorial | parameter-skim | pending |  |
| tRvItFsxjmg | Tackle Express | tutorial | parameter-skim | pending |  |
| tVgGBpzozMU | Tackle Express | tutorial | parameter-skim | pending |  |
| tugP0UsrzRI | Tackle Express | tutorial | parameter-skim | pending |  |
| u9sJyZhaDGQ | Tackle Express | tutorial | parameter-skim | pending |  |
| ugML6PvRyc8 | Tackle Express | tutorial | parameter-skim | pending |  |
| ulWK3kaVQ5k | Tackle Express | tutorial | parameter-skim | pending |  |
| v5XtBi3wtVM | Tackle Express | tutorial | parameter-skim | pending |  |
| v6X2s1lb1aE | Tackle Express | tutorial | parameter-skim | pending |  |
| vALAeUaBmRM | Tackle Express | tutorial | parameter-skim | pending |  |
| valIU8lsMX4 | Tackle Express | tutorial | parameter-skim | pending |  |
| vk3jbsINcPw | Tackle Express | tutorial | parameter-skim | pending |  |
| w5iryVkSe-0 | Tackle Express | tutorial | parameter-skim | pending |  |
| wk8bkqzdyM0 | Tackle Express | tutorial | parameter-skim | pending |  |
| wl27BWAWpq0 | Tackle Express | tutorial | parameter-skim | pending |  |
| x2cQrPaZ_Z0 | Tackle Express | tutorial | parameter-skim | pending |  |
| x5EkH9Vkdrk | Tackle Express | tutorial | parameter-skim | pending |  |
| x7LGWOehuw0 | Tackle Express | tutorial | parameter-skim | pending |  |
| xFW2002SaQk | Tackle Express | tutorial | parameter-skim | pending |  |
| xL1sMpmWcnk | Tackle Express | tutorial | parameter-skim | pending |  |
| x_3ohQ_D-f8 | Tackle Express | tutorial | parameter-skim | pending |  |
| xfPcA1VRgsw | Tackle Express | tutorial | parameter-skim | pending |  |
| xgPEt4Zj35Q | Tackle Express | tutorial | parameter-skim | pending |  |
| y3MaZYZvyUg | Tackle Express | tutorial | parameter-skim | pending |  |
| y9YlqMQh3BI | Tackle Express | tutorial | parameter-skim | pending |  |
| yEsbyq3WjWE | Tackle Express | tutorial | parameter-skim | pending |  |
| yTPtYL9QAsw | Tackle Express | tutorial | parameter-skim | pending |  |
| yVYUY3PlvIw | Tackle Express | tutorial | parameter-skim | pending |  |
| yf7dEnzsNzQ | Tackle Express | tutorial | parameter-skim | pending |  |
| yl-AkO5S64o | Tackle Express | tutorial | parameter-skim | pending |  |
| ywKI8gBK6vM | Tackle Express | tutorial | parameter-skim | pending |  |
| z1CS3To6ATA | Tackle Express | tutorial | parameter-skim | pending |  |
| z5UoW9pntvE | Tackle Express | tutorial | parameter-skim | pending |  |
| zItCqap4RdE | Tackle Express | tutorial | parameter-skim | pending |  |
| zLN0v-gWpeI | Tackle Express | tutorial | parameter-skim | pending |  |
| zLvKfwSmIIs | Tackle Express | tutorial | parameter-skim | pending |  |
| zVMY4fZydRQ | Tackle Express | tutorial | parameter-skim | pending |  |
| zVrsCf46_fI | Tackle Express | tutorial | parameter-skim | pending |  |
| zWpYFTIZP7w | Tackle Express | tutorial | parameter-skim | pending |  |
| zYcXDoOE6jo | Tackle Express | tutorial | parameter-skim | pending |  |
| zYcsYhdyZrA | Tackle Express | tutorial | parameter-skim | pending |  |
| zi5J9UDJgBk | Tackle Express | tutorial | parameter-skim | pending |  |
| zkEMsCIhSic | Tackle Express | tutorial | parameter-skim | pending |  |
| zlelqp7Qo9Y | Tackle Express | tutorial | parameter-skim | pending |  |
| zqZQLgj5W4k | Tackle Express | tutorial | parameter-skim | pending |  |
| zwHzyv43H_Q | Tackle Express | tutorial | parameter-skim | pending |  |
| 0rY9CEV5vsA | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| 2mHypTjZPzs | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| KNrxEjI0b1M | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| OLzruy70f98 | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| SvALnRmu7-c | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| XByPbEiYNyI | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| YJBs3to0wcI | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| YkwYNakCrKw | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| oqgAn6HOrwM | SearcherSportfishing | promo | none | skipped | boat/merch/event — pre-filter |
| 0DbOXC55PGI | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 1hNZovypQYc | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 1iTWVP8tg5U | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 2R5HOIrxtiw | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 2mqel8IboSA | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 4cPjNdf_hT0 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 54xzYUBpFaI | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 5Q9VsvsmTb0 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 5qMbQfPUdts | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 6_6Tx3v8zAw | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 6bBWub9dQHE | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 6bqaGEteHhA | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 6tlII1ZfMoc | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 8IaSH0PNB4Y | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 9J-p1gJq44U | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| 9hNLBgym5ik | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| BdlkqYdE5_g | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| BuFPr_85M1Y | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| EB0aBjqFZ3A | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| EJjHjxaCAxc | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| ENI89WSGi4U | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| Ek0sm9uXiaw | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| EqbSidlhfh8 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| F6VcJvfN36k | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| GJQwmzKyG10 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| Gf1bzECcyN0 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| IAeFN4xsQCE | tackle-express | promo | none | skipped | promo/product — pre-filter |
| IC-dAEmtV2g | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| IbdtrXeUUzg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| KTXwgM0sjjg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| L5RZyeoQqMs | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| LGmPoQaNnug | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| LWpwjS-eFyg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| Mrke37jEt18 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| NInwJNN8oY4 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| OCNKjymbGiU | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| OG6xYqyMY2M | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| OUZzPFcDcUo | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| OZr1Ksz29wg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| PJxhU0Dfctc | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| PSWjfQ_f76c | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| QBphkojlfTY | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| ROXnvdfGLIw | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| USiJ8a9bv-8 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| UhKx1gAgUOk | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| UigBtqg2Z2M | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| UjMAHhdoCNo | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| UsQXBhmILdg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| VAaWX7q3aSk | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| VkcDVMax9bk | tackle-express | promo | none | skipped | promo/product — pre-filter |
| WUn4Gfkpl8A | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| WbiKEkD8vq8 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| XoyK3z79M0A | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| YcUYdjXBr1I | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| ZcUmuwj0iH0 | tackle-express | promo | none | skipped | promo/product — pre-filter |
| _4SGyxAUMHs | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| _WDS3oBla2Y | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| abwQ4pmb_cc | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| axcM1tA9nfk | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| bv-H3EuzFYA | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| cVRlM476QuQ | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| cln6errJlwg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| cn5el4g71tQ | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| eRkn0nmAVf0 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| f6ZEVL0Dkso | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| gG9gw3mGkQ8 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| gZqJTVbdN9o | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| gqGPckgNKZg | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| iQnRvf8AIpQ | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| iR8CDCyofDM | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| i_RtrHdze1c | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| icvyaBmvp6o | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| ih7o1JoDegM | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| jA79DpfCoG4 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| kJG4gWAxnkw | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| kuIMN4fXfng | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| m4AmQEFff5I | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| m__5nee8Qgk | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| nCcKoGBq3tY | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| nP7vf035314 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| o3yxa7aeJ5M | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| pUwVpvjJ23w | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| qpEbiAY_57Y | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| r1uE1kepQNE | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| redS77jO5SU | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| s-S2JIiPGtQ | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| sQP0pUpo0aU | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| tHLuXmZFxfw | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| tjajoMbhML8 | tackle-express | promo | none | skipped | promo/product — pre-filter |
| tuM3xcxWw_E | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| uLRGOxahfak | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| v5KKdDOaUCo | tackle-express | promo | none | skipped | promo/product — pre-filter |
| vAYzTyMKomo | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| vzSqxckqaS4 | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| wI5XgLIqvwY | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| xjck3mIgKiY | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| xpTR4wCsV5k | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |
| yoqjeAryddo | tackle-express | promo | none | skipped | short (<200w), no technique keyword — pre-filter |

<!-- batch3:worklist:end -->
