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
| iAr6sbRC384 | Fisher Newb | seminar | deep | done | seminar/deep extraction - wind-retrieve skirted-bait presentation added to rockfish-deep-dropping.md, two regulatory rows (bag limit + RCA depth-boundary line) added to rockfish-lingcod.md and registered in regulatory-claims.md; fixed one invented competitor-weight comparison |
| lP6cg4eEU6s | Fisher Newb | seminar | deep | done | seminar/deep extraction of bay-bass tide/structure/crankbait/scent doctrine (Sav-On Tackle/IROD), confidence correctly downgraded on promo rod-endorsement content; three unflagged ASR/faithfulness issues found and fixed in place |
| m-M0iwX8DjA | Your Saltwater Guide | seminar | deep | done | Worked-example bait-tank data point (21ft Wellcraft, 60gal) and 0-300ft bluefin sounder-window reasoning + mark-and-troll workflow, dave-hansen medium confidence; one invented causal claim fixed during review |
| ouBrIdO7d4k | SD Fish and Sips | seminar | deep | done | Dana Point tungsten-headed King Buster-style finesse trolling lure for dolphin-associated yellowfin added to trolling.md/tuna-feathers-and-skirts.md/yellowfin-tuna.md; CI Made Lures Observed block in bluefin-tuna.md (SNI run, kite-bait ranking); fixed live-vs-artificial mischaracterization and overconfident identity claim before applying |
| sIoNELGlxmk | Your Saltwater Guide | seminar | deep | done | bait/bait-tanks.md; conditions/current-diagnostics.md; conditions/current-structure.md; species/california-spiny-lobster.md; species/white-seabass.md / mostly promo/comedic seminar filler; extractor pulled the ~6 substantive fishing claims (kelp/current mechanism, anchor-set current read, current≠tide framing, lobster rain-crawl mechanism + Observed charter anecdote, bait-tank turnover/air-bubble parameters, WSB West Cove example), attributed and confidence-scored correctly |
| ztpj1Xll0-U | Your Saltwater Guide | seminar | deep | done | bait/bait-tanks.md; sources/regulatory-claims.md; species/bluefin-tuna.md; techniques/fighting-big-bluefin.md / seminar/deep extraction — bait-barge timing, bluefin fight cadence corroboration, and 2014 bag-limit history added, minor faithfulness/format fixes applied |
| -62xDo4UQzo | SearcherSportfishing | tutorial | deep | done | species/wahoo.md; techniques/wahoo-bomb-casting.md; rigging/haywire-twist.md; species/yellowfin-tuna.md; techniques/trolling.md / new wahoo species router + cast-and-burn technique note created from this video, existing wahoo-bycatch mentions in yellowfin-tuna.md/trolling.md re-linked to it, haywire-twist.md gained a wahoo casting-leader spec with an unreconciled twist-vs-crimp data point |
| -BO1lMCTamg | SearcherSportfishing | tutorial | deep | done | rigging/fg-and-albright.md / Added Albright wrap-variant (spaced-then-overlap, 9 wraps) as an attributed bullet + tie-it link on the existing FG/Albright rig note; no new note needed |
| -OJ1FED7mxI | SearcherSportfishing | tutorial | deep | done | techniques/two-speed-low-gear-fight.md / deep-extracted the 6:1/3:1 two-speed gear-ratio mechanism into the existing low-gear-fight technique note (no prior note stated the raw ratio mechanic); fixed one unsupported "(or lever)" addition |
| -QnMvV4j_oM | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md / Added a medium-confidence "finicky daytime bluefin" chrome-jig entry (Salas 6X Jr. / Tady 4/0) to lures/iron-jigs.md, corroborating the existing ASR-uncertain "doua"->Tady 4/0 entry; link-maintenance.py clean (0 dead links). |
| -hY20bxz3oM | SearcherSportfishing | tutorial | deep | done | tackle/rod-and-reel-selection.md: added medium-confidence attributed spring-scale drag setter sub-entry under existing drag-scale doctrine |
| 0AtmEH6aQt0 | SearcherSportfishing | tutorial | deep | done | tackle/hooks.md: added Owner Hybrid Mutu booth-interview product note (sponsored, low confidence, ASR-uncertain hook name flagged) |
| 0Be1ARfvYaw | SearcherSportfishing | tutorial | deep | done | none: nothing extractable — entire transcript is a Fred Hall Show retail promo (Seaguar/P-Line fluorocarbon deals), no fishing knowledge |
| 0E9REoTjKrY | SearcherSportfishing | tutorial | deep | done | lures/knife-jigs.md; species/bluefin-tuna.md; tackle/bluefin-rig-ladder-by-grade.md: Steve Clarkson (Searcher) tip — 16VISX-class reel for angler endurance, 320g glow flat-fall jig w/ big hooks for night bite, 315 lb bluefin observed 59mi off Point Loma |
| 0hQJxESLTm4 | SearcherSportfishing | tutorial | deep | done | techniques/underhand-casting.md; bait/fishing-live-bait.md: new technique note for the underhand/lob cast, linked from fishing-live-bait.md |
| 0n4mJ3sfIqk | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md / Bob Bauer's pre-trip top-shot-refresh doctrine (cost + fresh line gets bit) merged into existing reel-maintenance note, distinguished from offseason respool section; medium confidence (unregistered channel) |
| 0xJqOtkmHqY | SearcherSportfishing | tutorial | deep | done | techniques/fighting-fish-from-the-rail.md; techniques/fighting-big-bluefin.md; techniques/two-speed-low-gear-fight.md / new technique note on rail-bracing/pump-stop-pump fight mechanics (Turner's Outdoorsman via SearcherSportfishing, Capt. Art of the Searcher), cross-linked into the two existing bluefin-fight technique notes |
| 0zgmoOH3Qag | SearcherSportfishing | tutorial | deep | done | rigging/haywire-twist.md; species/wahoo.md; techniques/wahoo-bomb-casting.md / second independent SearcherSportfishing demo merged into haywire-twist mechanics + wahoo bomb-casting lure choice, medium confidence; Catch tackle jig brand name flagged ASR-uncertain/provisional |
| 1uYIApdQQSM | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md; techniques/surface-iron-color.md / corroborating color/dating data point (Tady 45 mackerel, Salas 7X sardine-green-white) added as attributed observation; fixed a misattributed cross-link to techniques/surface-iron.md |
| 1wFoa11jPxQ | SearcherSportfishing | tutorial | deep | done | tackle/line-and-leader.md / Pete Gray/SearcherSportfishing sponsor-style tip (Talica 16, 80 lb Power Pro Maxcuatro, 42 lb Seaguar top shot) added as low-confidence attributed bullet; connecting knot name flagged asr-uncertain |
| 25sd2gZAIZ8 | SearcherSportfishing | tutorial | deep | done | sources/extraction-log.md: correct skip (generic lure-storage trick, no SoCal-specific fishing knowledge) |
| 2O4Z0S78KLg | SearcherSportfishing | tutorial | deep | done | rigging/surgeons-loop.md; species/yellowtail.md; rigging/essential-knots.md: new giant-yellowtail long-range surgeon's loop rig note, cross-linked |
| 2TmLaSCmfC8 | SearcherSportfishing | tutorial | deep | done | rigging/flying-fish-harness.md: added alternative braid wing-tie method for dead flyer kite rig |
| 2fwj24S9S-o | SearcherSportfishing | tutorial | deep | done | rigging/fg-and-albright.md: added third Albright variant (dissimilar-line, no dead-set wrap count, wet-before-cinch) |
| 3FghhsYAIFI | SearcherSportfishing | tutorial | deep | done | sources/extraction-log.md: skip, 48s ASR-garbled clip, only clean fact already documented in techniques/surface-iron.md |
| 3djuTW9GBr0 | SearcherSportfishing | tutorial | deep | done | done: lures/tuna-poppers-and-stickbaits.md — yellowfin popper/sniper/minnow gear params, medium confidence, asr-uncertain brand names |
| 3g82igEL8yk | SearcherSportfishing | tutorial | deep | done | done: lures/iron-jigs.md; tackle/line-and-leader.md; tackle/rod-and-reel-selection.md — surface-iron rod/reel/line/jig doctrine, fixed fabricated brand-name inference |
| 3gNTB4aMhCA | SearcherSportfishing | tutorial | deep | done | done: species/yellowtail.md; tackle/rod-and-reel-selection.md — Okuma PCH 7'6" long-range yellowtail setup, medium confidence, kept side-by-side with existing bracket |
| 3gykKyPdOvA | SearcherSportfishing | tutorial | deep | done | done: rigging/essential-knots.md; techniques/dropper-loop.md — surgeon's-knot dropper-loop corroboration + double-dropper build variant, trimmed cross-note duplication |
| 3zXcrGsIL-c | SearcherSportfishing | tutorial | deep | done | done: rigging/crimping.md (new note); rigging/bite-leaders.md; rigging/haywire-twist.md; rigging/README.md — crimping mechanic split from bite-leaders sizing table, fixed unstated-material claim and misread two-presses-per-sleeve step |
| 46wHgdTJWIM | SearcherSportfishing | tutorial | deep | done | tackle/spectra-hollow-vs-solid.md (new); rigging/hollow-splice-and-serving.md; tackle/line-and-leader.md — spun out hollow-vs-solid spectra note, cross-linked maintenance splice, trimmed post-review duplication |
| 4PY5H_YPJxY | SearcherSportfishing | tutorial | deep | done | none / skipped: 115s auto-caption promo for Accurate Reels, product names/prices/locations too ASR-garbled to reconstruct reliably, no extractable SoCal/Baja knowledge |
| 5472APCgym8 | SearcherSportfishing | tutorial | deep | done | rigging/fg-and-albright.md — merged Modified Albright as second attribution/wrap-count detail into existing spaced-then-overlap variant entry; fixed cinch-off mechanics wording inconsistency |
| 5CvFDpvlfSE | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md — amended with three new sourced sections (decision trigger, two rubber-band builds, drop-shot/brawler rig build) from Steve Carson/SearcherSportfishing |
| 5IN1wsOFR-k | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md — amended with winter lay-up section (corrosion spray + gear grease) from Tackle Tip Thursday Vol. 27; fixed one hardened-ASR claim before applying |
| 5J7a6UwTA90 | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md: added double jam knot naming + live-bait-vs-lure rule + wrap-count corroboration to San Diego jam entry |
| 5g7pK63hYnc | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md: added SearcherSportfishing surgeon's-knot mono-to-fluoro entry (36-40in/60lb/12in-tag/3-turn) with flyline-to-tuna application, corrected turn-count conflict framing vs Carson entry |
| 5pbA-wXoric | SearcherSportfishing | tutorial | deep | done | techniques/yo-yo-iron.md: added Steve Carson's Fred Hall Show hookset instruction (don't set hook, keep cranking) and line-class reasoning to mechanics |
| 5ppQob4N3Xw | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md: added on-the-water tackle-box field-repair section (reel-seat shim, tip-glue repair, DIY braid line-puller, dental picks, oil, UV flashlight, rail cable/S-hook) plus hook-file bullet, Norm Fujimoto/SearcherSportfishing, medium confidence |
| 6D_mf5gOfrM | SearcherSportfishing | tutorial | deep | done | none: nothing extractable, pure Fred Hall Show Accurate-reel booth promo/giveaway announcement, no fishing knowledge content |
| 6T3xZ9vufrM | SearcherSportfishing | tutorial | deep | done | rigging/san-diego-jam-single-vs-double.md; rigging/essential-knots.md / new rig note (San Diego jam single-vs-double selection rule) + companion-video link filled in on essential-knots.md |
| 6_E5JCRvazc | SearcherSportfishing | tutorial | deep | done | lures/knife-jigs.md; techniques/knife-jigging.md / tackle-shop hook/leader/reel/jig-model specifics and a bite-timing heuristic merged as attributed medium-confidence sub-bullets into existing notes |
| 6wVlDDno2TE | SearcherSportfishing | tutorial | deep | done | tackle/searcher-big-tuna-rig-ladder.md; tackle/bluefin-rig-ladder-by-grade.md; techniques/fighting-fish-from-the-rail.md; lures/knife-jigs.md; species/bluefin-tuna.md / split Searcher-channel tuna-rig content into a dedicated note (3-rig 80-130lb ladder + rail-fight variant), re-pointed existing links to it |
| 6wbO7qaU3sI | SearcherSportfishing | tutorial | deep | done | rigging/bite-leaders.md / corroborating flat-fall-jig bite-leader build (swivel + heavy-duty Owner split ring, crimp mechanic) added as an attributed sub-bullet under existing bluefin bite-leader doctrine |
| 7Ljt-DeFVcs | SearcherSportfishing | tutorial | deep | done | techniques/yo-yo-iron.md / added Penn Torque 40 / Phoenix Black Diamond Hybrid yo-yo reel-and-rod spec as concrete detail behind existing retrieve-speed doctrine in Gear-class detail |
| 7T6dIYqr3KI | SearcherSportfishing | tutorial | deep | done | species/sand-bass.md; species/calico-bass.md; techniques/slow-pitch-jigging.md / SPJ named effective for sand bass/sculpin (species-level, no conditions) plus a two-outfit gear example and a calico-bass personal-record catch |
| 7TPJsMc_clA | SearcherSportfishing | tutorial | deep | done | rigging/tony-pena-knot.md; rigging/essential-knots.md / new tackle-bench mono-to-spectra splice note spun out from the uni-to-uni entry, one step-order fix applied |
| 7iSGGb9ueAk | SearcherSportfishing | tutorial | deep | done | techniques/underhand-casting.md / folded short bait-cast tip (pull slack, lift rod tip, lob bait out) into existing underhand-casting.md as a second attributed source, no new note |
| 7ivBSL-mhW8 | SearcherSportfishing | tutorial | deep | done | rigging/slim-beauty-knot.md; rigging/essential-knots.md / new note for the modified slim beauty knot spectra-to-topshot splice, cross-linked from essential-knots.md as a distinct construction from the RP knot; fixed one misattributed quote during review |
| 83HROAgGW6Q | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md / dated update appended to existing Steve Carson drop-shot build with rod/reel/line detail and a corroborated/updated dropper-line figure, kept side by side per convention |
| 8A8y7LmRwVQ | SearcherSportfishing | tutorial | deep | done | no destinations; nothing extractable: 43s generic watch-the-hot-stick advice, no species/region/parameters, soak-vs-cycling already covered in techniques/flyline.md |
| 8MayoweWrAM | SearcherSportfishing | tutorial | deep | done | tackle/offset-hooks.md; tackle/hooks.md; tackle/README.md — new tackle note on offset vs. inline hooks (Owner SSW Inline Circle 6/0, Owner Super Mutu 6/0, Owner Gorilla 5/0, Owner Offshore 5/0; two stated reasons for offset) |
| 8UAtGqEjDtU | SearcherSportfishing | tutorial | deep | done | techniques/trolling.md; lures/cedar-plug.md; lures/halco-laser-pro.md — Capt R Taylor doctrine on why/when to troll (locate fish, less trolling on long drifts, 80-100lb outfit), cedar-plug Old Reliable and Halco swimmer confirmation |
| 9-3B-WRWqus | SearcherSportfishing | tutorial | deep | done | techniques/foamer-casting.md — Capt. Arch daytime visual-boil Colt Sniper program (120g, 50-60lb outfit, gear-and-burn) plus casting safety note |
| 91ZJbhAnzMg | SearcherSportfishing | tutorial | deep | done | planning/search-and-glassing.md; techniques/foamer-casting.md — boiler/foamer/breezer/flat-spot surface-sign vocabulary (medium confidence, unregistered channel), corroborates Hansen breezer entry, adds flat spot; fixed Hansen attribution error |
| 9IhmYstB8sA | SearcherSportfishing | tutorial | deep | done | lures/dtx-minnow.md; rigging/haywire-twist.md; species/wahoo.md; techniques/wahoo-bomb-casting.md / tutorial/deep extraction merged into 4 existing notes (DTX 200 trolling app, wahoo live-bait wire leader, router table rows, bomb/jig lure-choice + hookset mechanics) |
| 9_lwOzaLmXo | SearcherSportfishing | tutorial | deep | done | none / promotional tackle-sale ad with no decision-grade content; skip logged in sources/extraction-log.md |
| AGaVlYu61O4 | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / added corroborating entry (Pete Gray/SearcherSportfishing Vol.140) naming the single-pass tie San Diego jam knot and logging its 5-wrap count, medium confidence (unregistered channel) |
| AodUBhxPts8 | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md; techniques/foamer-casting.md / tough-foamer troubleshooting (keep trying / switch to what's biting / downsize jig / dead-stick stickbait / slow-wind iron) and a Halco-brand ASR corroboration added, both attributed to Billy (Fisherman's Landing) at medium confidence, with a retrieve-speed conflict logged rather than reconciled |
| Aorcd0Om7eI | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / third same-channel surgeon's-knot corroboration (Wendy/SearcherSportfishing, general break-off re-tie, 5-turn count, heavier pound test = fewer turns rule) appended to existing mono-to-fluoro entry, medium confidence, unregistered channel |
| AyN9MBWg-XY | SearcherSportfishing | tutorial | deep | done | lures/knife-jigs.md; techniques/knife-jigging.md / corroborating medium-confidence additions (fleet uptake/dart-vs-flutter framing, 240->300 ft depth-working example, swivel+split-ring rigging school) merged into existing lure and technique notes, one connection-point wording fixed |
| BLbUu_mfMJY | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md; techniques/surface-iron-casting.md / Two dated, medium-confidence attributions added (jig models 2018-10-18 predating existing 2020-06-11 corroboration; rod-length trade-off quote), correctly capped and split across lure vs technique notes |
| BacIrmOK-Bo | SearcherSportfishing | tutorial | deep | done | bait/fishing-live-bait.md / amended hand-picking/hold-time/shoulder-butt-hook doctrine into existing note, flagged as conflicting with logged net-and-carry doctrine |
| BcX-tp3I7LE | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / added as a supporting bare-line friction-test entry under the San Diego jam wetting-reasoning bullet, corroborating existing lubrication rationale with earliest-dated Wendy/SearcherSportfishing clip |
| Bn9fRKUmQ-U | SearcherSportfishing | tutorial | deep | done | rigging/fg-and-albright.md / added third Albright wrap-pattern variant (double-back wrap, Norm Fujimoto/Izorline) with its own bullet + demo link; confidence held at medium (unregistered channel) |
| Bo5Fj-XuWHo | SearcherSportfishing | tutorial | deep | done | rigging/springer-knot.md; rigging/essential-knots.md / new note for a single thin tackle-tip clip on a heavy-line hook knot, linked from Essential SoCal Knots router |
| Bz0WZNAofks | SearcherSportfishing | tutorial | deep | done | rigging/john-collins-knot.md; rigging/essential-knots.md / new note for a single thin tackle-tip clip on a named braid-to-mono/fluoro splice, linked from Essential SoCal Knots |
| CXrF7K4lKxE | SearcherSportfishing | tutorial | deep | done | tackle/rod-length-for-angler-size.md; tackle/rod-and-reel-selection.md / new tackle note on fitting rod length to angler build, linked from rod-and-reel-selection.md |
| CdjT_I_PBHQ | SearcherSportfishing | tutorial | deep | done | rigging/surgeons-loop.md; tackle/rod-and-reel-selection.md; techniques/dropper-loop.md / added Vol. 230 as corroborating segment on extra-heavy dropper-loop rig for long-range Baja giant yellowtail |
| E9YtH56Dngo | SearcherSportfishing | tutorial | deep | done | lures/knife-jigs.md; lures/tuna-poppers-and-stickbaits.md / tackle-stocking tip for bluefin (flat-fall, Colt Sniper, one unresolved personal-favorite jig) split across the two correct lure notes |
| ETw_3AFxEcM | SearcherSportfishing | tutorial | deep | done | species/wahoo.md; species/yellowfin-tuna.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/wahoo-bomb-casting.md; techniques/yo-yo-iron.md / amended 5 existing notes with Searcher yo-yo/fly-line rig spec, wahoo Ridge ground + bomb retrieve speed, Guadalupe six-day yellowfin fly-lining fishery, and color-by-forage reasoning; fixed one overgeneralized trip-length qualifier |
| EfaxxszOYFI | SearcherSportfishing | tutorial | deep | done | species/yellowfin-tuna.md / added hook-size/light-line data point for Guadalupe/ridge yellowfin tuna, sourced medium confidence (unregistered channel), fixed a misattributed cross-reference to the Vol. 189 source |
| F9XjGMEvvag | SearcherSportfishing | tutorial | deep | done | species/yellowtail.md; tackle/hooks.md / Coronados-bite hook-downsizing tip (Owner Ringed Flyliner, sizes 1/2/4) added to hooks.md with a routed summary in yellowtail.md; fixed missing sources entry |
| FN9-rgyC9ic | SearcherSportfishing | tutorial | deep | done | rigging/john-collins-knot.md / added Vol. 96 as earlier same-note demonstration with conflicting/scaled wrap counts (5/5 standard vs 3/3 for demo cord), direction-doesn't-matter judgment call, and visual cinch tell; kept side by side per 'prefer the latest' |
| G81HN0dIDg0 | SearcherSportfishing | tutorial | deep | done | lures/dtx-minnow.md; rigging/haywire-twist.md; species/wahoo.md; techniques/wahoo-bomb-casting.md / faithful deep extraction of a 79s tackle-tip into 4 existing notes (DTX-minnow troll leader, flylining wire conflict, bomb/stinger brands), two evaluator fixes for a misattributed benefit clause and an arithmetic approximation |
| GXXvT7pS2fM | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md: added medium-confidence JRI Stinger/Salas 7X/Tady 45 lightweight-combo data point with 9-10ft rod corroboration |
| GcgcnloKeZ4 | SearcherSportfishing | tutorial | deep | done | nothing extractable: auto-caption ASR too garbled to support any verifiable claim (retractable sonar dome transducer topic, no reliable parameters) |
| H5NHGLm1H5U | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md: added independent earlier-dated (2019-05-30) corroboration of improved-clinch/San Diego jam tie (Dave Hansen entry), hook-size flagged asr-uncertain |
| HH1YvOfMWx0 | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md: added pre-season rod inspection subsection (reel-seat threads, guide-insert fingertip check, weld points, tip check) |
| ILA6OMInWSM | SearcherSportfishing | tutorial | deep | done | planning/report-reading-and-forecasting.md: added plunker-style report-vocabulary section, cross-linked to techniques/flyline.md |
| IaVqJgUfcM8 | SearcherSportfishing | tutorial | deep | done | rigging/slim-beauty-knot.md / merged Vol.175 (rope demo) into existing slim-beauty-knot.md: 2nd source in front matter, wrap-count-scales-with-pound-test rule, rope-vs-Spectra thickness caveat on turn counts, and the stated reason (avoids back-to-back-uni tag-end catching in guides on a cast) to prefer this knot; second how-to link added |
| Ixyi1mY3Qeg | SearcherSportfishing | tutorial | deep | done | techniques/underhand-casting.md / folded a third short SearcherSportfishing clip's backlash-avoidance tip (lob not whip; re-thumb before splashdown) into the existing underhand-casting note as an additive section, medium confidence (unregistered channel), after removing two unstated invented rationale clauses |
| J0NJhN6-Thg | SearcherSportfishing | tutorial | deep | done | rigging/improved-clinch-knot.md; rigging/essential-knots.md / third SearcherSportfishing corroboration of the improved-clinch/San Diego-jam naming split, added to a new note split out of essential-knots.md; router pointer updated |
| J3FGJj5zYPE | SearcherSportfishing | tutorial | deep | done | techniques/wahoo-bomb-casting.md / Added color-matching doctrine (with stated on-camera reasoning) and a separate 'on the slide' cast-trigger mechanic to the existing wahoo-bomb-casting technique note; medium confidence (unregistered channel) |
| J7nreDb1dn8 | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md / added Colt Sniper stock hook/split-ring upgrade spec and three-retrieve rundown from Fisherman's Landing Tackle Shop segment, cross-linked to foamer-casting.md's existing let-it-sink retrieve |
| JHMCguO7sXE | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md; species/wahoo.md - spinning-vs-conventional popper rationale, Penn Slammer 3 spec (promotional flag), leader spec, wahoo wire-leader conflict cross-link |
| JOanxql39qg | SearcherSportfishing | tutorial | deep | done | none - skipped: promotional dockside fish-processing service ad, no fishing knowledge content |
| KGrussv1s3U | SearcherSportfishing | tutorial | deep | done | rigging/bite-leaders.md - corroborating flat-fall leader build (24in/200lb/size-1 crimp, decision-rationale on chafe-resistance) merged as medium-confidence sub-entry alongside existing Vol.28 entry |
| KHYoj9GEjCM | SearcherSportfishing | tutorial | deep | done | none - skipped: duplicate-of -62xDo4UQzo (identical 94s recording/ASR-artifact match; all content already captured in techniques/wahoo-bomb-casting.md + rigging/haywire-twist.md) |
| KLmNyflzsQ0 | SearcherSportfishing | tutorial | deep | done | techniques/dropper-loop.md - added heavy-tackle blood-knot dropper-loop build (Shimano TLD 30, 80lb, 16-20oz torpedo, 6/0-9/0 hook), medium confidence, as new subsection |
| KYE14piJAzI | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md / corroborating earlier (2019) instance of the same two rubber-band builds and tangle rationale added as a dated bullet to the existing Vol.225 section; leader figure flagged uncertain |
| LpReZmYQSCU | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / added SearcherSportfishing surgeon's-knot mono-to-fluoro corroborating entry (3-turn) as earliest-dated instance in the group, corrected sibling 5g7pK63hYnc's superseded earliest-data-point claim |
| M-W5mEjh1MY | SearcherSportfishing | tutorial | deep | done | rigging/seaguar-knot.md; rigging/essential-knots.md; techniques/flyline.md / new Seaguar-knot source folded into split-out note as 5th data point in loop/figure-eight family; evaluator fixed dropped front-matter source, orphaned how-to links, near-verbatim paraphrase, overclaimed first |
| MC3FTRRoOag | SearcherSportfishing | tutorial | deep | done | none / promotional tackle-shop pricing segment, no SoCal-specific fishing knowledge — correctly skipped by extractor; evaluator filled in pending extraction-log row |
| MjPY-nWZJ54 | SearcherSportfishing | tutorial | deep | done | bait/bait-tanks.md / added receiver-side bait-selection routine + Searcher deck-box/well scoop counts as new subsection, medium confidence; evaluator softened one hardened hedge and one unsourced tool definition |
| MuC0uGKDzxg | SearcherSportfishing | tutorial | deep | done | bait/fishing-live-bait.md / 3 attributed additions (nose-hook retrieve bite-getter, hold-the-leash carry tip, weak-sardine red-spot diagnostic) merged into existing bait note at medium confidence (unregistered channel), one faithfulness overstatement trimmed |
| NGtja-dCiC8 | SearcherSportfishing | tutorial | deep | done | tackle/spinning-reel-bait-feeder.md; tackle/rod-and-reel-selection.md / new tackle note on spinning-reel live-bait-feeder dual-drag mechanism, linked in from rod-and-reel-selection.md, medium confidence (unregistered channel, single mention) |
| NJ9ZLAU3sls | SearcherSportfishing | tutorial | deep | done | tackle/searcher-big-tuna-rig-ladder.md; techniques/chunking.md / Chunking rig + technique tip for Guadalupe Island big tuna split between tackle (reel/line/rod/hook/swivel) and technique (natural-fall secret) notes, region gate widened to include baja-pacific-north |
| NN5MWeRA28o | SearcherSportfishing | tutorial | deep | done | species/yellowfin-tuna.md / Faithful, correctly-scoped, promotional-low-confidence addition to existing Doctrine & conflicts entry cluster; no inversions, no rubric laundering, no dead links |
| OIiDJu4mx44 | SearcherSportfishing | tutorial | deep | done | fish-care/gaffing.md / Added three doctrine blocks (call-for-gaff timing, horizontal-profile positioning, free-spool-on-gaff) to existing gaffing note, correctly attributed and rated medium under searcher-sportfishing row |
| OL8D1l73RVg | SearcherSportfishing | tutorial | deep | done | techniques/skip-jigging.md; lures/iron-jigs.md; lures/tuna-poppers-and-stickbaits.md; species/dorado.md; species/yellowtail.md; techniques/surface-iron.md / New skip jigging technique note with 4 named lures, cross-linked into surface-iron, dorado, yellowtail routers; evaluator fixed confidence-laundering on 4 product endorsements |
| OmyRIw7Eye8 | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md / Added stick-jacket travel-protection block, single-mention medium confidence, corrected stale unregistered-channel label to reflect searcher-sportfishing registry promotion |
| P9H-bpzT7eU | SearcherSportfishing | tutorial | deep | done | species/dorado.md; lures/tuna-poppers-and-stickbaits.md / tutorial/deep dorado-101 short extracted cleanly (gear class, live-bait-vs-jig doctrine, grade/release practice, Colt Sniper dorado application) with two evaluator fixes for duplication and an unflagged ASR read |
| PS8CRYwTPiU | SearcherSportfishing | tutorial | deep | done | techniques/dropper-loop.md / corroborating knot-tying detail added to existing blood-knot-loop subsection, sources front-matter gap fixed |
| PYlqIODuIPQ | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md / bluefin hook-swap doctrine (Owner ST-66 treble, Owner Aki Twist, flat-fall hook transplant) added to iron-jigs.md sized/attributed correctly, one mis-routed link fixed |
| PjLa3oGm4Qg | SearcherSportfishing | tutorial | deep | done | techniques/wahoo-bomb-casting.md / Added Billy's (Fisherman's Landing/Searcher) lure-description, safety-pause, and named-gear data points to the existing wahoo-bomb-casting technique note; fixed one overconfident ASR-derived claim during review |
| QTWVs5BwQ0g | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md; techniques/foamer-casting.md / Added Shimano Orca/Yo-Zuri popper picks (low, sponsored-claim capped), a second non-conflicting reason for spinning-over-conventional tackle (medium), and a spinning-popper point-and-wind/walk-the-dog retrieve mechanic with stage-at-the-bow readiness note (medium) |
| Qa6Q8mOAV6I | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / added Shawn Trowbridge / SearcherSportfishing overlap-around-the-eye caution + cut-short breaking-strength demo as a sub-entry under the San Diego jam knot, corroborating the existing 6-wrap figure |
| R48YdVFfEOI | SearcherSportfishing | tutorial | deep | done | tackle/hooks.md / faithful single-mention addition under Circle vs. J, correctly attributed and medium-confidence, no dead links |
| RM7cBgCDWFA | SearcherSportfishing | tutorial | deep | done | rigging/flying-fish-harness.md; techniques/kite-fishing.md / Yummy Flyer/dead-flyer leader specs and a long-range kite/fighting-rod outfit added, corrected one overstated line-capacity claim |
| RNRFrfepiW0 | SearcherSportfishing | tutorial | deep | done | techniques/yo-yo-iron.md / three attributed entries added (base-case + upsize rig tiers, PA-depth-call rule) to existing yo-yo-iron technique note |
| Rudzy0DD08w | SearcherSportfishing | tutorial | deep | done | species/bluefin-tuna.md; tackle/rod-and-reel-selection.md / two-speed reels required for 1.5- and 3-day bluefin trips, TLD 20/Talica 12 example builds added; resolved prior italica ASR-garble as Talica via corroboration |
| S2cT2JqrWcY | SearcherSportfishing | tutorial | deep | done | none / nothing extractable: generic seasickness-prevention tip, no SoCal/Baja-specific fishing content, correctly skipped per curation bar |
| S80GRyuAbLY | SearcherSportfishing | tutorial | deep | done | rigging/crimping.md; rigging/haywire-twist.md; species/wahoo.md / added third wahoo live-bait wire-leader data point (60 lb wire / A2 sleeve, sleeve-crimped) with general sleeve-to-wire sizing parameter |
| SCQnyVEQfHY | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md; lures/tuna-feathers-and-skirts.md; tackle/hooks.md / Tackle Tip Thursday Vol.100 test-of-time segment merged three low-confidence product/model data points (Salas 6X/6X Jr. dating, Zuker Zucchini feather, Mustad 94150/94151) |
| Stw7SNyIgdg | SearcherSportfishing | tutorial | deep | done | none / skipped: promotional apparel content (sun gloves/buffs/hats), no SoCal/Baja fishing decision knowledge, generic what-to-bring content excluded by curation bar |
| TU5quAG4atM | SearcherSportfishing | tutorial | deep | done | techniques/dart-jig-tuna.md; lures/iron-jigs.md; rigging/essential-knots.md; species/bluefin-tuna.md; species/yellowfin-tuna.md; tackle/searcher-big-tuna-rig-ladder.md / new technique note (Dart/Colt-Sniper daytime finesse tuna jigging) plus corroborating additions to knots/hooks/rig-ladder/species routers; evaluator fixed fabricated term, unsupported reel spec, rubric-laundered confidence upgrade, missing sources id |
| TgOMUXxIQl4 | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md; tackle/rod-and-reel-selection.md / Steve Carson dockside tip merged as corroborating spinning-reel spec + leader-by-lure-type doctrine into existing popper/stickbait casting-gear section |
| Ud3hi9r1Nr4 | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md; techniques/foamer-casting.md; techniques/skip-jigging.md / 2018-07 Searcher fleet report on Colt Sniper/P-Line Laser Minnow bluefin retrieves, merged as corroborating data, skip-jigging bumped medium->high |
| UfuQr6gOIk8 | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / added fourth same-channel surgeon's-knot corroborating clip (3-turn count) plus trim-judgment caution cross-linked to Albright knot |
| UtYO1ubQFz0 | SearcherSportfishing | tutorial | deep | done | none / skipped - dockside 'red shirt' crew logistics/tipping etiquette, no fishing knowledge content; evaluator filled in dangling extraction-log row |
| UyfcYoNV2sg | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md / added post-trip breakdown routine (unmount, upright drainage, corrosion-inhibitor spray) attributed to Vince/Fisherman's Landing; evaluator softened an over-asserted unstated reason |
| VW2t_G8eorI | SearcherSportfishing | tutorial | deep | done | rigging/springer-knot.md merged Pete Gray Vol. 137 as second corroborating demo, confidence raised to high |
| VcJManCizRE | SearcherSportfishing | tutorial | deep | done | new techniques/rod-handling-live-bait.md capturing off-hand grip, thumb-on-lever, fingertip feed, backpedal; linked from bait/tackle notes |
| VxHYxXmPoWQ | SearcherSportfishing | tutorial | deep | done | tackle/searcher-big-tuna-rig-ladder.md added 2022 three-rig big-bluefin ladder, confidence raised to high; fixed one fabricated detail and one misattributed quote |
| VyFpIk-Na9Q | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md added 5-wrap/100lb San Diego jam entry for tuna; fixed one unflagged directional claim, flagged ASR ambiguities |
| W6RuHvaqkHs | SearcherSportfishing | tutorial | deep | done | techniques/wahoo-bomb-casting.md and rigging/haywire-twist.md merged three rod/reel/leader gear-class data points, medium confidence |
| WxlDxFjB8oQ | SearcherSportfishing | tutorial | deep | done | species/yellowfin-tuna.md; tackle/searcher-big-tuna-rig-ladder.md / Added Guadalupe-Island line-shy medium-grade tuna finesse rig (Gary Gillingham/Accurate, sponsored segment) as a third, separate data point cross-referenced with existing Vol.189/Vol.72 entries, correctly confidence-split (mechanism medium, product picks low) per registry's sponsored-claim caveat |
| X1zAA4DLOr0 | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md / Added 'Reel bags' entry (Wes/SearcherSportfishing) to existing rinse-discipline note; evaluator fixed an invented rationale (extractor had attributed the stick jacket's stated protection reasoning to the reel-bag claim, which transcript never gives) |
| XTsTpWnk1gU | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md / Diamond jig (SearcherSportfishing) added as a distinct heavy chrome yo-yo shape, darts on drop, ~10oz, fished 50-60fm for bluefin; evaluator corrected confidence medium to low per channel product-endorsement cap |
| Y2XZ34-Tpa0 | SearcherSportfishing | tutorial | deep | done | tackle/gear-classes.md; techniques/fighting-fish-from-the-rail.md / Rail-rod mechanism (hypalon foregrip, two-speed pairing) added to existing gear-class and fighting-technique notes with correct medium/low confidence split and cross-links |
| YJX-hYEIcNM | SearcherSportfishing | tutorial | deep | done | planning/search-and-glassing.md / Added 'Sunglass lens color for glassing' section (medium confidence, Rick/Fisherman's Landing guest voice) tying lens tint to existing kelp-paddy/breezer surface-sign vocabulary; evaluator ran link-maintenance backlink regen |
| Y_ElKixrhsc | SearcherSportfishing | tutorial | deep | done | tackle/rod-and-reel-selection.md: Steve Carson's traditional-vs-baitcast surface-iron outfit specs added as new section, kept side by side with Doug Kearn's tip; fixed fabricated cross-ref and overstated claim before applying |
| Yd3J4igs-QA | SearcherSportfishing | tutorial | deep | done | tackle/bluefin-50-80lb-bait-outfit-ladder.md (new); species/bluefin-tuna.md; tackle/bluefin-rig-ladder-by-grade.md; tackle/searcher-big-tuna-rig-ladder.md: new bait-outfit-ladder note (Gary/Accurate, sponsored segment) cross-linked to router, mechanism/strategy medium, product/reel picks low per registry |
| YeV--HarEYQ | SearcherSportfishing | tutorial | deep | done | rigging/san-diego-jam-knot.md (new, split from essential-knots.md) + 8 dependent notes: Armando's single-pass San Diego jam demo (7-wrap data point), tension-rationale clause added |
| YtlD1gQ_ULw | SearcherSportfishing | tutorial | deep | done | tackle/hooks.md: Gamakatsu Nautilus regular/HD/Light hook-size tip added as low-confidence sponsored endorsement, juxtaposed with existing Nautilus entry; fixed trailing ASR-garbled size specifics |
| ZECOKmD4fIs | SearcherSportfishing | tutorial | deep | done | rigging/slim-beauty-knot.md: amended with Vol.127's leader-naming, 4-turn uni, 9-forward/8-back wrap counts; confidence raised medium→high on repeated-doctrine grounds |
| ZKb13fNT6P0 | SearcherSportfishing | tutorial | deep | done | tackle/searcher-big-tuna-rig-ladder.md: Added flat-fall leader rig (SK 250g / Nomad 320g) entry to Searcher big-tuna rig ladder, appropriately confidence-split between mechanism (medium) and sponsored product names (low); fixed one wrong-target link to techniques/knife-jigging.md |
| Zhn-VDrlaLM | SearcherSportfishing | tutorial | deep | done | bait/fishing-live-bait.md; techniques/flyline.md; techniques/rod-handling-live-bait.md; techniques/underhand-casting.md; techniques/live-bait-pendulum-cast.md: new pendulum-cast technique note plus cross-links from flyline/underhand-casting/rod-handling/fishing-live-bait; third-occurrence repeated-doctrine bump to high for hold-the-line-not-the-bait |
| _VtL0DrNdAU | SearcherSportfishing | tutorial | deep | done | tackle/rod-and-reel-selection.md: Low-confidence product-endorsement addition (Seeker Athena flyline rod pick) merged into existing Flyline section; corrected an inaccurate same-doctrine attribution to Cesar's cast-quality bullet |
| _Z4yMtrYgeA | SearcherSportfishing | tutorial | deep | done | rigging/crimping.md; rigging/haywire-twist.md; species/wahoo.md: duplicate/re-cut of S80GRyuAbLY correctly logged as provenance-only addition (earliest-date push to 2020-10-29), confidence held at medium per re-cut/duplicate rule, no new notes |
| _jDXMtCrUZg | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md; tackle/searcher-big-tuna-rig-ladder.md: tutorial/deep extraction of Steve Carson's 40/50 lb flyline outfit (Penn Torque two-speed, 65 lb braid, 8 ft 30-60 lb rod, 1/0-2/0 circle hook) plus sinker-bait rubber-band variant (4-5 oz torpedo sinker, ~120 ft target depth), merged into two existing notes |
| _rf1TqLh1yE | SearcherSportfishing | tutorial | deep | done | rigging/perfection-loop-knot.md; rigging/essential-knots.md; techniques/hoop-netting.md / new sliding-loop hook-tie note (medium confidence, single corpus mention) linked from the knots router and cross-referenced with hoop-netting's existing rope-to-rope use of the same knot |
| aAqKHeyBwEo | SearcherSportfishing | tutorial | deep | done | tackle/gear-classes.md; techniques/wahoo-bomb-casting.md / Added Seeker SSR 7650 (wahoo bomb/rail rod) + corroborating Guadalupe-special OSP 1x3 mention; fixed missing sponsored-claim low-confidence flag on both product names and unflagged species-word ASR ambiguity |
| aD0Iim9C15o | SearcherSportfishing | tutorial | deep | done | bait/fishing-live-bait.md; techniques/flyline.md / Extracted Steve Carson's (Penn/SearcherSportfishing) three hooking methods - nose hook under any weight, sardine wishbone for fly-lined close-under-boat fish, shoulder hook + slow-wind retrieve for distant boiling bluefin - cross-linked into both notes at medium confidence |
| an_uw-5pjfw | SearcherSportfishing | tutorial | deep | done | techniques/flat-fall-jigging.md; species/bluefin-tuna.md; lures/knife-jigs.md; tackle/gear-classes.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/knife-jigging.md / new flat-fall-jigging technique note + router row + rig-ladder entry + gear-classes citation; fixed product/model confidence-laundering inconsistency across three files |
| b-oixz7pgAo | SearcherSportfishing | tutorial | deep | done | rigging/john-collins-knot.md; rigging/essential-knots.md / 3rd independent demo of John Collins/RP knot (Pete Gray, Vol. 150): 80 lb threshold + 15/20/60 lb use cases, 5-up/5-down wrap corroborating Vol. 96, decision-rationale, wood-dowel seating tip, and RP-knot/John-Collins naming conflict cross-logged; confidence raised medium to high |
| bEFhWtGBdBU | SearcherSportfishing | tutorial | deep | done | techniques/fighting-fish-from-the-rail.md / added SearcherSportfishing Vol. 138 stance-variant content (kids/legs stance, knee stance, stated reasoning) to the existing rail-fighting technique note; fixed a registry mislabel and two faithfulness/quote issues in the working tree |
| bbn-aJGRH5o | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md / Added Norm Fujimoto's post-trip top-shot-removal and annual spectra strip/clean/reseal/wax/respool routine as a new dated subsection; fixed two named-product mentions (Swifty line remover kit, Woody's carnauba wax) that the extractor left at medium instead of the registry-mandated low for product/model endorsements |
| cpUq7Z3UOwU | SearcherSportfishing | tutorial | deep | done | tackle/rod-and-reel-selection.md; techniques/two-speed-low-gear-fight.md / merged Nathan Winnicke's offshore-tuna rod-length/casting-distance rationale and two-speed bunching/corkscrewing fight rationale into the two existing gear/technique notes, cross-linked |
| cx7tKXHmiY4 | SearcherSportfishing | tutorial | deep | done | bait/making-bait.md / added long-range (3-10 day) trip bait-gear packing tip: two sabiki-style rig sizes + squid jig, medium confidence |
| ddataaVWoDc | SearcherSportfishing | tutorial | deep | done | tackle/searcher-lever-drag-reel-sizing.md; tackle/gear-classes.md; tackle/rod-and-reel-selection.md / new low-confidence sponsored-content note on Penn Fathom 30/60 two-speed sizing, cross-linked from gear-classes and rod-and-reel-selection; fixed a misquote and an unsupported ASR-based inference |
| dg1sbr6GuB8 | SearcherSportfishing | tutorial | deep | done | tackle/bluefin-rig-ladder-by-grade.md; rigging/essential-knots.md / third independent citation of Steve Carson's 4-turn/20-100 lb surgeon's-knot rule plus a corroborating second citation of Rig 1 (reel/rod/leader/hook match, backing-line and stretch-rationale detail, Observed note, hedged albacore-rig aside) |
| dkY7wJ4UM1c | SearcherSportfishing | tutorial | deep | done | tackle/bluefin-rig-ladder-by-grade.md; techniques/knife-jigging.md / Confirmed Izorline brand + six-color/100ft spec and worked depth-count example, resolving a prior asr-uncertain flag; cross-linked one line from knife-jigging.md |
| e1-tPTNejBo | SearcherSportfishing | tutorial | deep | done | none / nothing extractable: entire video is a generic long-range-trip packing list (chair, rod belt, jacket, layers, sun shirt, buff, deck boots, sunscreen) — no SoCal/Baja-specific tackle or technique content; matches curation-bar exclusion and precedent skips |
| eLFVhVyyOTw | SearcherSportfishing | tutorial | deep | done | bait/making-bait.md / added Logan Watson's stated reason (bait size growth on long-range trips) for carrying both a light and heavy sabiki, cross-linked, medium confidence |
| eLPTMO3-_1Q | SearcherSportfishing | tutorial | deep | done | rigging/surgeons-loop.md / added the 2018 earliest-dated SearcherSportfishing dropper-loop/San-Diego-jam segment (line class, sinker, Owner Gorilla hook size, loop-length figures) as a distinct dated entry alongside the 2024 segments; confidence high per registered channel + repeated doctrine |
| eZXPqiAtqi8 | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md; rigging/improved-clinch-knot.md; tackle/hooks.md / offshore kelp-paddy dorado/yellowfin rig (25-40 lb reel, 3 ft/25 lb fluoro leader via 3-turn surgeon's knot, Owner Live Bait hook 1/1-0 via improved clinch knot); fixed missing link-maintenance run |
| ew7Lru8wmQs | SearcherSportfishing | tutorial | deep | done | tackle/line-and-leader.md / added single-mention mono-to-fluoro size-match tip to Connections section, medium confidence |
| ewfWc7MTBPk | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md / third dated SearcherSportfishing instance of the wrapped/bridled rubber-band torpedo-sinker mechanic (Billy, Fisherman's Landing), placed chronologically between Vol. 55 and Vol. 225 entries |
| fg2v1kxoTMA | SearcherSportfishing | tutorial | deep | done | tackle/hook-assortment-by-trip-length.md; tackle/hooks.md; rigging/rubber-band-deep-rig.md / new trip-length hook-pack note (yellowtail J-hook range, bluefin circle-hook step-up/stealth rig, sinker-rig bigger-bait circle size) plus cross-ref links |
| fgTmUq78ofQ | SearcherSportfishing | tutorial | deep | done | planning/electronics-and-sounder.md; rigging/assist-hooks.md; rigging/crimping.md; rigging/double-trouble-rig.md; rigging/rubber-band-deep-rig.md; species/bluefin-tuna.md; species/yellowfin-tuna.md; techniques/fighting-big-bluefin.md; techniques/fighting-fish-from-the-rail.md; techniques/flat-fall-jigging.md; techniques/kite-fishing.md; techniques/knife-jigging.md; techniques/skip-jigging.md / tutorial/deep extraction across 13 existing notes from Turner's Outdoorsman seminar; fixed one inverted risk-grade claim and one invented single-vs-treble tradeoff |
| fyJA3o2hVh0 | SearcherSportfishing | tutorial | deep | done | tackle/searcher-40lb-all-around-tuna-outfit.md; lures/iron-jigs.md; rigging/essential-knots.md; tackle/bluefin-rig-ladder-by-grade.md; tackle/hooks.md; tackle/line-and-leader.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/two-speed-low-gear-fight.md / new all-around 40lb outfit note plus 7 corroborating cross-links; fixed missing sources video_id on all 7 touched files |
| gaHpCc_tc78 | SearcherSportfishing | tutorial | deep | done | lures/soft-plastic-swimbaits.md / corroborating single-mention swimbait size/weight/color data point for calico bass at 'the Ridge'/Baja coast; fixed missing 'bank' waters tag |
| gqEjWrPpa48 | SearcherSportfishing | tutorial | deep | done | tackle/searcher-lever-drag-reel-sizing.md / short promo clip merged as corroborating/earlier data point on the existing Penn Fathom 60 entry; giveaway plug excluded; fixed one unflagged ASR garble |
| h0NyGvIaDc8 | SearcherSportfishing | tutorial | deep | done | techniques/foamer-casting.md / added cast-into-a-busting-school mechanic (size-to-bait, bridge-called sounder-depth follow-down) and an ask-a-biting-angler troubleshooting tip; fixed a fabricated Current-Sniper/Colt-Sniper ASR resolution |
| hlmDnAct1cA | SearcherSportfishing | tutorial | deep | done | tackle/bluefin-retail-setup-high-end-vs-budget.md; species/bluefin-tuna.md; tackle/rod-and-reel-selection.md; tackle/searcher-lever-drag-reel-sizing.md / new low-confidence tackle note for a retail associate's high-end vs. budget bluefin reel/rod picks, linked from species router and two related tackle notes; fixed missing link-maintenance run |
| hteLeDIy9Qs | SearcherSportfishing | tutorial | deep | done | techniques/yo-yo-iron.md / added Fred/Secret Fishing Rods depth-tiered jig sizing, stretch-buffer leader reason, and don't-set-the-hook citation at medium confidence |
| i1Ul0XCG36o | SearcherSportfishing | tutorial | deep | done | none / 47s Turner's Outdoorsman house-brand rod-lineup promo — no decision logic, parameters, or SoCal-specific detail; correctly skipped |
| icpm7gADxvU | SearcherSportfishing | tutorial | deep | done | tackle/hooks.md; techniques/flyline.md / light-line bluefin bait scenario merged (J-hook baiting speed, bait-not-swimming rationale, Mutu Hybrid retail sighting); evaluator fixed a sponsored-claim confidence cap and cross-note duplication |
| iqTN2IBRP1A | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md / added Nomad Chug Norris hot-pink-mackerel data point and popper-vs-effectiveness framing; evaluator removed a fabricated Steve Carson cross-reference |
| it_YYh_8Z-w | SearcherSportfishing | tutorial | deep | done | lures/dtx-minnow.md; species/wahoo.md / third source merged into DTX Minnow wahoo-trolling section and wahoo.md situations table; mechanism claim medium, endorsement stat low per registry caveat |
| jDmHgRNnqhw | SearcherSportfishing | tutorial | deep | done | tackle/hooks.md / Fred Brent's J-hook-vs-circle rationale and Mustad 94151 corroboration added; evaluator corrected confidence to low (product/model endorsement per registry) |
| jJG6FWNXkok | SearcherSportfishing | tutorial | deep | done | none / skipped: promo for third-party fish-delivery courier service (Dock 2 Door), zero fishing knowledge content |
| jLFZIh15Fec | SearcherSportfishing | tutorial | deep | done | lures/knife-jigs.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/flat-fall-jigging.md / merged 200g flat-fall weight/color/leader/gear tip as 2018-07-12 dated entry; evaluator fixed a dead anchor link |
| jQzOdmP0zoQ | SearcherSportfishing | tutorial | deep | done | rigging/crimping.md; tackle/spectra-hollow-vs-solid.md / added crimp-vs-knot trip-length trigger and 135 lb hollow/solid breakpoint with competing solid-line lean; evaluator fixed an invented speaker gender pronoun |
| jqyu3wZdNF4 | SearcherSportfishing | tutorial | deep | done | rigging/haywire-twist.md; species/wahoo.md / two wahoo live-bait leader builds added to haywire-twist.md; free-spool bite-response doctrine added to wahoo.md beside existing conflicting doctrine; evaluator removed an invented causal mechanism |
| k4U3ETqmlEc | SearcherSportfishing | tutorial | deep | done | tackle/searcher-50-60-80lb-flyline-outfit.md; species/bluefin-tuna.md; tackle/searcher-big-tuna-rig-ladder.md / new note for Steve Carson's 50/60/80 lb flyline outfit, cross-linked as earlier citation of Rig 1, new gear-summary bullet on bluefin-tuna.md |
| kdEKEyVTIGU | SearcherSportfishing | tutorial | deep | done | none / promo for shoreside fish-processing vendor (Five Star Fish Processing), no SoCal/Baja fishing knowledge, correctly skipped |
| kuvfoJKpLYU | SearcherSportfishing | tutorial | deep | done | tackle/reel-maintenance.md / added pre-trip mono top-shot visual test and spectra fray-check, medium confidence |
| kzpeM56Gh7o | SearcherSportfishing | tutorial | deep | done | tackle/searcher-three-outfit-minimum-quiver.md; tackle/gear-classes.md; tackle/rod-and-reel-selection.md; tackle/searcher-big-tuna-rig-ladder.md; tackle/searcher-lever-drag-reel-sizing.md / new note: 3-outfit minimum quiver for a 1.5-4 day Searcher trip, cross-linked as third citation of OSP 1x3/Fathom 60 rail-rod pairing |
| m2g97MxmAGI | SearcherSportfishing | tutorial | deep | done | tackle/searcher-40lb-all-around-tuna-outfit.md; techniques/dart-jig-tuna.md / tuna dart-jig reel corroboration + size/color/depth data point merged; evaluator reverted an over-broad confidence bump to medium |
| m424-XxCFQw | SearcherSportfishing | tutorial | deep | done | none / nothing-extractable: 38s promo/PSA on eating yellowtail collars, no fishing knowledge to capture |
| nAGkYWuJrCI | SearcherSportfishing | tutorial | deep | done | none / nothing extractable: 25s personal color-aesthetic gear preference, no functional parameters or decision logic |
| nM7B5NQLy44 | SearcherSportfishing | tutorial | deep | done | rigging/bimini-twist.md; rigging/essential-knots.md; rigging/wind-on-leader.md; tackle/rod-and-reel-selection.md / spun Bimini Twist out of essential-knots.md into its own note, merged in traditional 30-50-turn tie alongside existing quick-tie, cross-linked from 3 parents |
| nWq2DVzBNeI | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md / amended note with a corroborating dated instance of the rubber-band sinker-rig mechanic (leader, surgeon's knot, sinker placement); evaluator fixed ordinal numbering and phrasing |
| nnrEjc-Gq2o | SearcherSportfishing | tutorial | deep | done | planning/search-and-glassing.md / merged Vol.81 sunglass-lens doctrine into existing sunglass section, upgraded shared pattern to high confidence as repeated channel doctrine, kept fit-beats-tint point at medium |
| o6Sawz5S7bk | SearcherSportfishing | tutorial | deep | done | rigging/crimping.md; rigging/haywire-twist.md / Wahoo leader tackle tip (275 lb steel wire, crimped, ~3 ft/39 in unreconciled) added as a wire-crimp-mechanic parameter to crimping.md and a full crimped-build entry to haywire-twist.md; fixed one dead cross-link anchor |
| otnnAon3F9Q | SearcherSportfishing | tutorial | deep | done | none / skipped: promotional/logistics content only (fish-cleaning reservation line), zero fishing knowledge despite Tackle Tip title |
| ouoyP7t2Nus | SearcherSportfishing | tutorial | deep | done | none / generic non-tackle packing-list video correctly skipped by extractor; evaluator filled in the missing extraction-log row |
| p9xeMl-r_CY | SearcherSportfishing | tutorial | deep | done | none / correctly skipped promotional shop-tour video (Fisherman's Processing new location); evaluator filled in the missing extraction-log row |
| pB10vaDaETM | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md / fifth dated Searcher instance of the wrapped/two-hole rubber-band sinker rig added with a new stated leader-abrasion reason and a placement conflict flagged asr-uncertain rather than reconciled |
| pCd6QykcZ0w | SearcherSportfishing | tutorial | deep | done | lures/iron-jigs.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/dart-jig-tuna.md; tackle/searcher-daytime-dart-jig-outfit-ladder.md / new daytime dart-jig outfit ladder note (light/heavy tiers, hook-strength and treble-vs-single-by-lure-style data points) cross-linked into existing iron-jig hook-style and dart-jig rig entries; one over-precise inferred number fixed |
| pQ9kGqgsX8I | SearcherSportfishing | tutorial | deep | done | techniques/wind-in-your-face-positioning.md; bait/fishing-live-bait.md; techniques/rod-handling-live-bait.md; techniques/underhand-casting.md / New technique note on windward-rail positioning during multi-angler drift stops, cross-linked from three related technique/bait notes, link-maintenance clean |
| pm8u6qUrVUI | SearcherSportfishing | tutorial | deep | done | lures/knife-jigs.md; lures/tuna-poppers-and-stickbaits.md / applied with one fix: removed an invented wind/casting rationale not supported by the ASR-garbled transcript, everything else faithful |
| ptoIvB2MspE | SearcherSportfishing | tutorial | deep | done | tackle/searcher-finesse-live-bait-outfit.md; species/bluefin-tuna.md; tackle/bluefin-rig-ladder-by-grade.md; tackle/hooks.md / new finesse-outfit note (20 lb + 15 lb step-down) plus corroboration/discrepancy notes added to the bluefin rig ladder, hooks, and species router |
| qBP3qRnK4H4 | SearcherSportfishing | tutorial | deep | done | rigging/rubber-band-deep-rig.md / sixth dated Searcher instance of the pull-through/simple rubber-band sinker rig added (6-8 oz torpedo sinker, nose-hooked sardine, crew-called depth for bluefin); evaluator hedged an overconfident build-identification claim and flagged it asr-uncertain |
| q_ciF1xiDiI | SearcherSportfishing | tutorial | deep | done | tackle/searcher-big-tuna-rig-ladder.md; techniques/knife-jigging.md / Thin 46s clip split into rig detail (tackle) and depth-tracking mechanic (technique); speaker name hedged asr-uncertain; one minor invented-intent phrase fixed |
| qtCZAB4EBs4 | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md / third wrap-count data point (5-wrap rule, 3 shown) added to existing uni-to-uni bullet, medium confidence, no new note needed |
| r9bF3VtzDUg | SearcherSportfishing | tutorial | deep | done | species/calico-bass.md; techniques/swimbaits.md; tackle/rod-and-reel-selection.md; techniques/surface-iron.md / faithful extraction of Doug Kearn's calico bird/flip sign and plastics tackle spec; evaluator restored a dropped surface-iron rod/reel claim into its correct existing home and added a bird-reading cross-link |
| rFmWrp-Vndo | SearcherSportfishing | tutorial | deep | done | rigging/cut-loop-dropper.md; techniques/dropper-loop.md; rigging/essential-knots.md / new cut-loop surgeon's-loop dropper variant extracted and linked from its router and knots note |
| rNiQKb3sCh4 | SearcherSportfishing | tutorial | deep | done | techniques/wind-in-your-face-positioning.md / corroborating citation added (Laurie/Turner's Outdoorsmen via SearcherSportfishing Vol. 56, 2019-07-10) confirming the core windward-side rule; confidence raised medium to high under repeated-doctrine rule |
| riEkdu8PEds | SearcherSportfishing | tutorial | deep | done | tackle/searcher-30lb-large-tuna-outfit.md; species/bluefin-tuna.md; tackle/bluefin-rig-ladder-by-grade.md; tackle/hooks.md; techniques/two-speed-low-gear-fight.md / new 30 lb large tuna outfit note plus cross-citations into the bluefin router, rig ladder, hooks, and two-speed fighting notes, all corroborating existing registered-channel doctrine |
| rziFyx7SRGI | SearcherSportfishing | tutorial | deep | done | species/yellowfin-tuna.md / added a fourth Guadalupe Island data point (jig-stick/casting-irons technique contrast) to the existing fly-line/hook-size/light-leader cluster under Where & when; fixed registered-channel mislabel |
| scScYJJF95Y | SearcherSportfishing | tutorial | deep | done | tackle/gear-classes.md; techniques/fighting-fish-from-the-rail.md / Seeker OSP 2x4 rail-rod specs + applications added to gear-classes.md rail-rod class; rail-fighting demo mechanics (watch-the-tip cue, low gear) added to fighting-fish-from-the-rail.md, contrasted with two-speed-low-gear-fight.md's continuous-grind cadence; fixed one silently-corrected ASR quote |
| sfZhPSTvZy8 | SearcherSportfishing | tutorial | deep | done | none / correctly skipped generic cooking/recipe video (no fishing tackle/species/technique content despite the Tackle Tip Thursday title); evaluator filled in the missing extraction-log row |
| sjOJiR6_HJ4 | SearcherSportfishing | tutorial | deep | done | tackle/searcher-rail-rod-ladder.md; tackle/gear-classes.md; tackle/rod-length-for-angler-size.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/fighting-fish-from-the-rail.md / new rail-rod ladder note (four tiers by line rating) plus cross-links into gear-classes, rod-length-for-angler-size, big-tuna-rig-ladder, and fighting-fish-from-the-rail |
| sjlL5GidM58 | SearcherSportfishing | tutorial | deep | done | techniques/surface-iron.md: added Billy/Fisherman's Landing fiberglass-vs-composite jig-stick doctrine (medium, single mention, registered channel) to Gear-class detail |
| t8GP_-DMlSU | SearcherSportfishing | tutorial | deep | done | tackle/lightweight-reel-pick-turners-outdoorsman.md; tackle/bluefin-retail-setup-high-end-vs-budget.md: new low-confidence tackle note (Lori Sack/Turner's Outdoorsman reel pick) cross-linked with sibling note; promo trip announcement skipped |
| tRlv1azFPlM | SearcherSportfishing | tutorial | deep | done | tackle/hooks.md: Owner Aki-hook-vs-J-hook stock-up tip merged into existing Owner-hooks cluster, low confidence (sponsored-claim caveat), garbled model/size hedged as asr-uncertain |
| tYebwLzTyf8 | SearcherSportfishing | tutorial | deep | done | tackle/star-drag-vs-lever-drag.md; tackle/rod-and-reel-selection.md: new lexicon note on star-drag vs lever-drag mechanism, linked from rod-and-reel-selection.md intro; fixed a fabricated/spliced quote during eval |
| tio1oeibVlM | SearcherSportfishing | tutorial | deep | done | species/opah.md: new opah species router from bycatch-while-tuna deep-jig doctrine + table fare, cross-linked from dart-jig notes; fixed invented 'pectoral' gloss, added pCd6QykcZ0w to sources during eval |
| tjBeR9tWd4s | SearcherSportfishing | tutorial | deep | done | species/wahoo.md; techniques/wahoo-bomb-casting.md: grounds/season corroboration + lure-weight, cast-mechanics, Seeker SSR 7650/line-choice detail, flagged 40lb-vs-50lb line-floor conflict |
| tnHltcDdVtU | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md: Fred Brandt/Seeker Rods Colt Sniper retrieve doctrine + Led Masters 150g conflict vs existing 100g cap (kept side by side); note now 682 lines, colt-sniper split warranted but deferred |
| ueDBCY1mIPk | SearcherSportfishing | tutorial | deep | done | tackle/searcher-40lb-all-around-tuna-outfit.md: merged third citation of Carson's 40lb outfit (Vol.222), gap-filled rod spec + effective grade range 15-80lb, corroborated reel/line/leader/knot/hook |
| vNIazq1aVwc | SearcherSportfishing | tutorial | deep | done | bait/fishing-live-bait.md; rigging/haywire-twist.md; species/wahoo.md: wahoo live-bait wire leader (6th leader build), hook positions, and bite-response doctrine added; asr-uncertain hook 'number 100' flagged; 40lb wire vs 200-300/44/60 conflict kept side by side |
| vVOkxHx58Eg | SearcherSportfishing | tutorial | deep | done | tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md (new); species/bluefin-tuna.md; lures/knife-jigs.md; tackle/searcher-daytime-dart-jig-outfit-ladder.md; tackle/searcher-big-tuna-rig-ladder.md; techniques/knife-jigging.md: new Carson bluefin jig ladder note 100-400g by daypart/depth, cross-linked; fixed sponsored-claim confidence gap on 3 named products during eval |
| vn4fmPxUqsU | SearcherSportfishing | tutorial | deep | done | techniques/two-speed-low-gear-fight.md: added Shane/SearcherSportfishing citation on shift-timing (stay high through run, drop to low when circling); corrected inflated high-confidence claim to medium during eval |
| wGWjnW7wCiI | SearcherSportfishing | tutorial | deep | done | tackle/drag-setting.md (new, split from rod-and-reel-selection.md); tackle/hooks.md; tackle/rod-and-reel-selection.md; tackle/line-and-leader.md: drag-setting doctrine (failure modes, hand-wrap test, mid-fight correction) added; verbatim section split verified, one stale cross-ref fixed during eval |
| wnlOU34RXs8 | SearcherSportfishing | tutorial | deep | done | techniques/rail-etiquette.md (new): rail-communication doctrine (names, simultaneous-hookup under/over, listen to crew), cross-linked from fighting-fish-from-the-rail.md and wind-in-your-face-positioning.md; trimmed one invented detail during eval |
| wqrIs5kg1qw | SearcherSportfishing | tutorial | deep | done | lures/tuna-poppers-and-stickbaits.md: appended corroborating 2018 Nomad Riptide sinking-stickbait entry (sweep-and-spin, sink bite, gear); fixed imprecise date-gap phrasing during eval |
| yGXSrUauo2w | SearcherSportfishing | tutorial | deep | done | tackle/searcher-yellowtail-livebait-sliding-sinker-rig.md (new); species/yellowtail.md; tackle/hooks.md; tackle/searcher-30lb-large-tuna-outfit.md; techniques/sliding-sinker.md: new Carson 30lb yellowtail sliding-sinker rig note, router row + cross-links; added asr-uncertain caveat on sinker weight ladder during eval |
| ypr-qZF4FTY | SearcherSportfishing | tutorial | deep | done | tackle/drag-setting.md: merged Part 1 (Captain Mark) — crew/priorities framing, free-spool-to-strike method (bumped to high, corroborates Vol.207), headroom-past-strike, crew-sets-drag recommendation; downgraded one unjustified high-confidence bullet to medium during eval |
| zkA1jqHXXD0 | SearcherSportfishing | tutorial | deep | done | rigging/essential-knots.md; techniques/sliding-sinker.md: added Captain Art surgeon's-loop connection + rail-rod rental rig build, sinker-placement/tangle-cause diagnosis, nose-hook fix, cross-linked |
| zuAuk-Kfa1Y | SearcherSportfishing | tutorial | deep | done | tackle/searcher-four-outfit-guadalupe-quiver.md (new); rigging/surgeons-loop.md; tackle/searcher-50-60-80lb-flyline-outfit.md; tackle/searcher-three-outfit-minimum-quiver.md: Captain Arch's 4-outfit rental quiver (25lb paddy, Fathom40 flyline, Talica20, Talica25 Guadalupe) + corroborating addenda; fixed hook-range mismatch and header inconsistency during eval |
| 49joKHD7Umc | SearcherSportfishing | seminar | deep | done | 9 files (lures/iron-jigs.md, techniques/surface-iron*.md, tackle/rod-and-reel-selection.md, rigging/*-knot.md, tackle/line-and-leader.md, tackle/hooks.md): surface-iron seminar merged — JRI-7/JRI-4 lineage, buying-counter selection tip, Tady C corroboration, casting/reel-placement mechanic, budget build, knots, sharpening distinction; fixed sponsored-claim confidence gap in budget-build section during eval |
| 4uNPLknRAQg | SearcherSportfishing | seminar | deep | done | techniques/wahoo-trolling.md (new); fish-care/wahoo-handling.md (new); species/wahoo.md; rigging/haywire-twist.md; tackle/hooks.md; techniques/trolling.md; techniques/wahoo-bomb-casting.md: dedicated wahoo-trolling technique note and deck-safety note from Searcher seminar, plus wire/leader/hook conflicts flagged and merged into existing wahoo notes |
| FETSTtbCMII | SearcherSportfishing | seminar | deep | done | sources/extraction-log.md: byte-identical duplicate of fgTmUq78ofQ (already fully extracted across 13 notes); log row filled in, no new note destinations |
| FXWOIB0TPfE | SearcherSportfishing | seminar | deep | done | lures/cedar-plug.md; lures/halco-laser-pro.md; lures/rapala-husky-magnum.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; techniques/fighting-big-bluefin.md; techniques/flat-fall-jigging.md: Tackle Talk Live seminar - bluefin hook-downsize lever, Guadalupe shark depredation tips, flat-fall mono-leader + stock-hook data point, trolling reel/rod/top-shot build, 3 trolling-lure data points |
| QHY5kmU7OTU | SearcherSportfishing | seminar | deep | done | bait/bait-tanks.md; bait/fishing-live-bait.md; rigging/flying-fish-harness.md; rigging/john-collins-knot.md; tackle/searcher-30lb-large-tuna-outfit.md; tackle/searcher-40lb-all-around-tuna-outfit.md; tackle/searcher-50-60-80lb-flyline-outfit.md; tackle/searcher-finesse-live-bait-outfit.md; techniques/two-speed-low-gear-fight.md; techniques/underhand-casting.md: 5-outfit ladder seminar (finesse/30/40/50-60-80lb), bait-curing, shoulder/wishbone hooking, John Collins knot, flying-fish float, two-speed fight mechanics; 4 fabricated/misattributed details corrected during eval |
| SAltQjih0ms | SearcherSportfishing | seminar | deep | done | species/yellowtail.md; techniques/dropper-loop.md; techniques/flyline.md; techniques/rod-handling-live-bait.md; techniques/underhand-casting.md; techniques/yo-yo-iron.md: live-bait flyline hookset+hooking, yo-yo iron cadence/build, dropper-loop build, paddy grade-by-depth pattern; fixed 1 invented depth claim + 2 sponsored-claim confidence overreaches |
| YntRJAN88fs | SearcherSportfishing | seminar | deep | done | tackle/hooks.md; tackle/line-and-leader.md; tackle/reel-maintenance.md; techniques/dropper-loop.md: bluefin tackle prep, 40lb circle-vs-J hook threshold, mono-vs-fluoro drag mechanism, spectra-reversal maintenance, dropper-loop citation; 2 minor factual fixes applied |
| eehDVb6_GoI | SearcherSportfishing | seminar | deep | done | bait/fishing-live-bait.md; rigging/john-collins-knot.md; rigging/rubber-band-deep-rig.md; species/bluefin-tuna.md; tackle/drag-setting.md; tackle/hooks.md; tackle/searcher-lever-drag-reel-sizing.md; techniques/flat-fall-jigging.md; techniques/knife-jigging.md: Turner's Outdoorsman bluefin seminar - sinker-rig/flat-fall tackle, RP/John Collins knot wrap counts, braid marking, drag-strike doctrine; fixed missing sources front matter + 1 overstated treble-hook claim |
| lf3S28nh-kk | SearcherSportfishing | seminar | deep | done | planning/electronics-and-sounder.md; planning/search-and-glassing.md; rigging/essential-knots.md; rigging/san-diego-jam-knot.md; tackle/reel-maintenance.md; tackle/searcher-four-outfit-guadalupe-quiver.md; tackle/searcher-three-outfit-minimum-quiver.md; tackle/searcher-spring-bluefin-yellowtail-quiver.md (new); techniques/flat-fall-jigging.md; techniques/foamer-casting.md; techniques/kite-fishing.md; techniques/surface-iron-color.md: spring bluefin/yellowtail tackle talk, new quiver note; fixed 2 fabricated details during eval |
| shZCjX2-fkI | SearcherSportfishing | seminar | deep | done | bait/fishing-live-bait.md; rigging/essential-knots.md; rigging/fg-and-albright.md; species/bluefin-tuna.md; tackle/hooks.md; techniques/fighting-big-bluefin.md; techniques/flat-fall-jigging.md; techniques/kite-fishing.md: bluefin tuna seminar - surgeon's knot leader length, flat-fall weight/leader, hook-downsize rule, rod-belt timing, kite rental outfit; fixed 1 temp-reading mislabel + 1 relative-time reference |
| tpmOYXYQwhU | SearcherSportfishing | seminar | deep | done | rigging/improved-clinch-knot.md; rigging/san-diego-jam-knot.md; rigging/slim-beauty-knot.md; species/opah.md; species/yellowtail.md; tackle/rod-length-for-angler-size.md; techniques/flat-fall-jigging.md; techniques/live-bait-pendulum-cast.md: knot line-class breakpoint, opah depth/incidental corroboration, marked-yellowtail depth-bite mechanism, rod-length counter-view, flat-fall 2019 recap, cast-distance drill; fixed channel-registry mislabel in 2 notes |
| -II7kzpklzE | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 8-second birthday-greeting clip with zero fishing content |
| 1axjidotnfE | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 1-second placeholder with no ASR content |
| 2pTRbsDwTO4 | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 7-min banter/footage clip with no fishing decision rationale, technique, or tackle content above curation bar |
| 38kxKgR4q2s | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, wordless music/highlight montage with no spoken fishing content |
| 3kGAA-T8IGw | SearcherSportfishing | on-the-water | decision-rationale | done | none: crew-introduction video, no fishing knowledge content |
| 5m1cHclspII | SearcherSportfishing | on-the-water | decision-rationale | done | none: on-the-water clip with no extractable content, garbled auto-captions, no species/technique/decision stated |
| 6BqmPN0xGZY | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 31s undifferentiated on-the-water audio/captions with no fishing knowledge content |
| 6I5Ma8n8PRE | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 34s clip with bluefin school on sonar not biting, no depth/location/reason stated; below curation bar |
| 76cj579gnTo | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, crew-banter/fish-fight on-the-water clip, garbled ASR, no decision rationale above curation bar |
| 7xnTtlaYs58 | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 14-second clip with no fishing content |
| 8gEvmdj0lec | SearcherSportfishing | on-the-water | decision-rationale | done | none: nothing extractable, 18-second on-the-water clip, garbled auto-captions, no species/technique/decision stated |
| 8vJEyJVBvSM | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable, 135-second on-the-water clip with sparse/garbled auto-captions, no species/technique/decision-rationale stated |
| 8wK37e921F8 | SearcherSportfishing | on-the-water | decision-rationale | done | on-the-water/decision-rationale — boat-maintenance/haul-out content only, no fishing knowledge, correctly extracted as nothing extractable |
| 9fVsfdOgUMI | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — fragmented auto-caption trip-outcome banter, no decision rationale or fishery knowledge present |
| A3PW3EMsu8c | SearcherSportfishing | on-the-water | decision-rationale | done | promotional prize-giveaway clip, no fishing knowledge to extract — correctly left as nothing-extractable |
| ACL2BD6gbkE | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — boat haul-out/maintenance video, no fishing knowledge content |
| AJzAbQ0i3QY | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 30s garbled auto-caption promo clip, no fishing content |
| B1r0T6f5kgM | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 95s promotional testimonial clip about ultra-limited-load charter trips (rail space, staterooms, no tangles), no fishing knowledge content |
| Bk0-P4oeFiU | SearcherSportfishing | on-the-water | decision-rationale | done | on-the-water/decision-rationale extraction — nothing extractable (raw celebratory footage, no stated rationale, no new decision/conditions content beyond existing dorado/Alijos coverage) |
| CSpBymCVWN4 | SearcherSportfishing | on-the-water | decision-rationale | done | tackle/drag-setting.md — merged as corroborating high-confidence doctrine (three-things-wrong list + rod-raise mid-fight tell) into existing Searcher drag-setting content, predating Vol. 205/207 by ~9 years |
| C_MmNnJrdrQ | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable: promotional/testimonial content only, no fishing knowledge or decisions present |
| Dr_npFZYLM4 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — pure fish-fight footage/crew banter, no stated decisions, techniques, or rationale in transcript |
| ELd90j4ZukI | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — garbled auto-caption dockside interview clip, no attributable location/technique/species-outcome combination survives scrutiny |
| EfAThf5gOFw | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 37s clip is entirely applause/crowd noise and photo-op stage directions, no fishing content |
| FIAvWu02xko | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 25s fragment of unattributed deck chatter, no species/technique/gear content |
| FPZBm0oFvKc | SearcherSportfishing | on-the-water | decision-rationale | done | on-the-water footage with only unintelligible ASR fragments (boat gaffing scene, no stated technique/rationale/species/location) — nothing extractable |
| Fdaq28LwK0I | SearcherSportfishing | on-the-water | decision-rationale | done | on-the-water/decision-rationale extraction — nothing extractable, transcript is banter with a bare catch count and no technique/decision content |
| HAxYMiqkBDs | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — crew-banter/fish-fight on-the-water clip with no species/technique/decision content |
| HCC1uhsPSas | SearcherSportfishing | on-the-water | decision-rationale | done | dockside unload footage with no fishing knowledge/decision content; correctly left unextracted |
| HJdwm0bn0H8 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — garbled auto-caption banter clip, no species/technique/decision content |
| HeRoKbDCDTw | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable: reaction chatter + bare catch tally (2 wahoo, ~8 yellowtail, dorado, tuna), no stated decisions or reasons |
| Ibt0vdrl48E | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — garbled crew-banter clip, no fishing knowledge content; extraction-log updated |
| Ij04nagr8g8 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — crew-banter/fish-fight clip, no fishing knowledge content; extraction-log updated |
| J52jzaMnKA0 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — rod-organizing banter and unlanded fish, no species/technique/rationale content |
| J61iyNrfqsg | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — promotional trip-schedule overview, generic beginner-progression advice; place/species mentions shallow duplicates of dedicated corpus coverage |
| JUSWISdzIq0 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — dockside fish-processing/service promo blurb, no SoCal-specific fishing knowledge |
| JWU3djUbfKY | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 48s clip, no substantive fishing content |
| K4GTUO57rio | SearcherSportfishing | on-the-water | decision-rationale | done | locations/cedros-island.md: added Observed block (2010 Cedros yellowtail session, grade + angler catch counts) |
| KrIednxCEKI | SearcherSportfishing | on-the-water | decision-rationale | done | techniques/wahoo-trolling.md: added Observed block (Dorado Marauder outcome, no stated reason) |
| L6BUIu5vFEc | SearcherSportfishing | on-the-water | decision-rationale | done | duplicate-of kzpeM56Gh7o, already captured in tackle/searcher-three-outfit-minimum-quiver.md; extraction-log updated |
| LYjdT3E3Rb4 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 43s auto-caption transcript unintelligible, no fishing content |
| LuSn3IeW9_c | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 36s promo/booking-ad video, zero fishing content |
| MPC_OQjvO-o | SearcherSportfishing | on-the-water | decision-rationale | done | tackle/searcher-6-to-8-day-heavy-outfit.md (new note): Guadalupe/ridge heavy outfit — Seeker OSP 1x3 rail rod, Penn Int'l 30/Accurate 50/TLD 30 options, 4 applications; cross-linked from gear-classes.md and 3 sibling quiver notes |
| NeSw-4df4H4 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 106s clip is personal banter about new gear purchase, no fishing content |
| NgdpWzPRlqQ | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — garbled auto-captions, no decision or stated reason |
| Nj_9ORYJhkg | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — unstructured on-the-water chatter/reactions, no stated reasons or doctrine |
| Ntwb6fU2zl4 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — garbled auto-captions, no doctrine/rationale content |
| OfJ_KI_D184 | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — garbled auto-captions, no decision-rationale content |
| PKwvkOOYzto | SearcherSportfishing | on-the-water | decision-rationale | done | rigging/surgeons-knot-mono-to-fluoro.md (new note, split from essential-knots.md): Captain Art's fluoro-to-mono surgeon's loop tie added as 13th citation; fixed cross-file links and citation-count typo |
| Psiiza6YQyE | SearcherSportfishing | on-the-water | decision-rationale | done | tackle/drag-setting.md: merged Capt. Aaron Remy's drag-setting reasoning (hands-free-hookset, drag-wear-like-brakes, star-drag test, crew-check corroboration); fixed date-ordering error |
| QMTCBY-kKeE | SearcherSportfishing | on-the-water | decision-rationale | done | nothing extractable — 11s clip contains only music and a single word, no fishing content |
| QOV9d0qTcEE | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: 49s clip with no extractable fishing content |
| QeU9J5XVhP4 | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, garbled clip with no stated rationale |
| Qk6Q1UJMTpQ | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, unintelligible ASR banter |
| RhULLaUsEDk | SearcherSportfishing | on-the-water | decision-rationale | done | locations/cedros-island.md: Observed block, flylined-sardines yellowtail session, medium confidence |
| S6Ic8aXDdIg | SearcherSportfishing | on-the-water | decision-rationale | done | techniques/fighting-fish-from-the-rail.md: Observed catchphrase-precedent, low gear + rail-bracing, 2010 |
| Sx40JvCXFuA | SearcherSportfishing | on-the-water | decision-rationale | done | species/yellowfin-tuna.md; species/yellowtail.md: Observed 2009 Guadalupe Island grade data (40-70lb YFT, to 25lb YT) |
| URJm6qDHgqg | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: promotional gift-guide video, no fishing content |
| UUiaoQVexy0 | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, generic fight-coaching banter; evaluator fixed extraction-log pending row |
| UYfvRQk_xT8 | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: dockside banter and website promo, no extractable content |
| VB_GYSk_vdY | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, banter-only footage with unresolvable location |
| Vphyeoxd7R4 | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, dockside catch-recap with no stated reasoning |
| XngQMsyvtNM | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, reaction-only footage; evaluator fixed extraction-log pending row |
| Y97blHr1F8k | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: 26s customer catch shout-out, no extractable content |
| Y9Ke1shXpwc | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: 17s camera banter clip, no fishing content |
| YeYO998pX0M | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: nothing extractable, weigh-in callouts and banter only |
| ZIJAvAEW_tU | SearcherSportfishing | on-the-water | decision-rationale | done | planning/electronics-and-sounder.md: 2010 Westar to Furuno CH250 gyro-stabilized transducer decision-rationale |
| ZY-cTuFtjh8 | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: silent aerial b-roll clip, no fishing content |
| ZcIiucZlBcM | SearcherSportfishing | on-the-water | decision-rationale | done | no destinations: 5s editing/outtake clip, no fishing content |
| _f5QmWSUUx8 | SearcherSportfishing | on-the-water | decision-rationale | done | techniques/wahoo-bomb-casting.md: Observed wire-leadered Raider-class jig, Alijos Rocks, Sept 2010, gear corroboration only |
| _r08B4bItAY | SearcherSportfishing | on-the-water | decision-rationale | done | species/wahoo.md; species/yellowfin-tuna.md; species/yellowtail.md; species/dorado.md; locations/cedros-island.md: fall 2009 trip-preview doctrine (Guadalupe/Alijos Rocks/Uncle Sam Bank grounds, season, run distances) |
| aXqFrQSNrDc | SearcherSportfishing | on-the-water | decision-rationale | done | none / 33s promotional ad for American Tuna canned-tuna brand, no extractable fishing knowledge; skip correct |
| atboDq5tZ0Q | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 35s clip is entirely applause/music, no fishing content |
| b9JThf2Jm0s | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 50s generic trip recap, no location/technique/gear/decision-reasoning |
| cjbAQ20Q9bQ | SearcherSportfishing | on-the-water | decision-rationale | done | none / no destinations: 97s dockside catch-celebration clip, no fishing content |
| ck6REMbJkww | SearcherSportfishing | on-the-water | decision-rationale | done | none / skipped: auto-generated captions too garbled/content-free to support extraction |
| drARx5Fpy-s | SearcherSportfishing | on-the-water | decision-rationale | done | none / correctly skipped: 29s auto-caption clip, no extractable fishing content |
| eIAKA8Jgopk | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: unintelligible auto-caption fragments, no fishing content |
| fHtTbZAWz1g | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: dock-interview chatter, no stated decisions/technique/gear/conditions |
| fcdWAo0VAKw | SearcherSportfishing | on-the-water | decision-rationale | done | techniques/flyline.md / added Observed tackle data point (40 lb test flyline, hook/brand ASR-hedged) |
| g1C-FK6o4nA | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: crew/staff bios and galley praise only, no fishing knowledge |
| gQb_3MW6L9M | SearcherSportfishing | on-the-water | decision-rationale | done | none / skipped: 14s music/silence clip, no fishing knowledge |
| jH0q4UPjwC0 | SearcherSportfishing | on-the-water | decision-rationale | done | techniques/kite-fishing.md / Added medium-confidence stated-reason block on 2-4oz sliding sinker on kite-flown bait (Alijos Rocks) |
| jU7qi40WTzQ | SearcherSportfishing | on-the-water | decision-rationale | done | planning/trip-length-selection.md; planning/day-plan-protocol.md / new planning note: 1-day vs 3-7-day trip rationale (late-afternoon tuna bite window) |
| kYZqFRBUDYg | SearcherSportfishing | on-the-water | decision-rationale | done | none / skipped: dockside weigh-in banter, no fishing knowledge |
| kqsg_t5MIzY | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: galley recipe content, not fishing knowledge |
| lYyi_Yh3S5g | SearcherSportfishing | on-the-water | decision-rationale | done | locations/cedros-island.md; lures/tuna-poppers-and-stickbaits.md; tackle/drag-setting.md; techniques/surface-iron.md / Capt. Art tackle-tips: crew/bait/drag priorities, Tady 45/Salas 7X, Cedros/San Benitos favorite spots, MegaBait mention |
| pNNrYXlgkO4 | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: crew banter/ribbing, no stated decisions or reasons |
| phRsYlu0mmc | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 29s clip, no discernible speech content |
| sAwPTPnHNzk | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: galley cooking recipe segment, no fishing knowledge |
| so1df8prECw | SearcherSportfishing | on-the-water | decision-rationale | done | none / skipped: fish-fight chatter, no species ID or stated technique/reason |
| srHnaMIrVIA | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: transcript has no usable ASR text |
| tj_mEL94ETg | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 10s promo clip, no fishing content |
| uPnM-qw696k | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 10s clip, no fishing content |
| uWGGeDOprsE | SearcherSportfishing | on-the-water | decision-rationale | done | tackle/searcher-alijos-rocks-ridge-7-day-quiver.md; tackle/hooks.md; tackle/line-and-leader.md; rigging/crimping.md; species/wahoo.md; species/yellowtail.md; species/yellowfin-tuna.md; tackle/searcher-6-to-8-day-heavy-outfit.md; tackle/searcher-four-outfit-guadalupe-quiver.md / five-outfit Alijos Rocks/Ridge tackle quiver note applied with one fix (removed invented tough-jaw rationale) |
| uXWliLLPzss | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 32s clip, fragmentary exclamations only, no fishing content |
| utTcrpscYHQ | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: music-video montage, lyrics/applause only |
| v8tPYYKM2JE | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: banter/action footage, no stated reasoning, gear already covered by existing tackle notes |
| vJGGfJfdDAk | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: fragmented rail banter during fish fight, no stated reasoning, unexplained jargon only |
| vMRLjvSQBNA | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: weigh-in/jackpot scene, no stated technique reasoning |
| wt-3dlbMGJc | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 18s clip, no depth/shape/location/decision stated for sonar mark |
| x0_v2COShBo | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 22s celebratory landing clip, no decisions/reasons/gear detail |
| xU6Rp1YJjm8 | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: home-video banter clip, no stated reasoning or doctrine |
| xo7njK7vXHQ | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: 66s music/gaff-shot highlight clip, no fishing content |
| y0LVT59inEA | SearcherSportfishing | on-the-water | decision-rationale | done | tackle/hooks.md / Captain Art sponsor segment: corroborating citation bumping 40 lb circle-vs-J threshold to high confidence, added line-class-to-J-hook-size table, merged ringed/non-ringed data point; fixed one misquote |
| y__TVzcePik | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: restates already-documented tough-foamer pattern, no new detail |
| yidQY2NeXtM | SearcherSportfishing | on-the-water | decision-rationale | done | none / nothing extractable: boat-maintenance/crew-intro clip, no fishing content |
| zKovnvOwlFc | SearcherSportfishing | on-the-water | decision-rationale | done | rigging/surgeons-knot-mono-to-fluoro.md; rigging/essential-knots.md / 14th surgeon's-knot citation (guide-clearance rule, 60-80lb ceiling, tie-speed) + 4th uni-to-uni wrap-count citation + speed-vs-cosmetics decision-rationale; fixed stale citation-count cross-reference |
| -BCEGxojaT4 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 10s pigeon joke clip, no fishing content |
| -FQ3cSdvnK0 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 23s ASR fragment, no gaff-specific content beyond existing doctrine |
| -KHdjYwefmM | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: promo clip, freshwater trout content, out of scope |
| -Ocrnb4rmMo | Tackle Express | tutorial | parameter-skim | escalated | escalated: subagent-failure |
| -zw76Sh7YCI | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md: appended 4-in vs 5-in sizing + O-ring/band keeper-hardware bullet, medium confidence |
| 05uB5V_jWTg | Tackle Express | tutorial | parameter-skim | done | techniques/slow-pitch-jigging.md: rockfish jig-weight/depth pairing relocated from rockfish-deep-dropping.md into matching Jig weight & selection section |
| 0OpWO3Yo4HE | Tackle Express | tutorial | parameter-skim | done | none: generic Palomar-knot mechanic already covered by rigging/essential-knots.md; only new content is a product plug, fails curation bar |
| 0PAPH1uqk4A | Tackle Express | tutorial | parameter-skim | done | rigging/leadhead-mods.md: added mid-column/current-drift squid presentation paragraph, medium confidence |
| 0_pEeh0n9Uo | Tackle Express | tutorial | parameter-skim | done | none: transcript is unusable auto-generated captions (music/noise only, no speech content) |
| 0pBFS6TLVUQ | Tackle Express | tutorial | parameter-skim | done | none: freshwater bass finesse-jig/craw-trailer content, out of scope (not SoCal/Baja saltwater) |
| 0z0bvF7o3ak | Tackle Express | tutorial | parameter-skim | done | none: 34s clip on lodge tipping etiquette, generic hospitality content, fails curation bar |
| 17sBBD0C4XY | Tackle Express | tutorial | parameter-skim | done | tackle/reel-maintenance.md: added grip-care section (hypalon/EVA hardening, heat-shrink fix), medium confidence |
| 1MxHXTv3a2A | Tackle Express | tutorial | parameter-skim | done | tackle/reel-maintenance.md: added line-change cadence subsection (co-poly 2 trips, fluoro 3-4 trips), braid-vs-fluoro preference, medium confidence |
| 1YKT275onlU | Tackle Express | tutorial | parameter-skim | done | none: 24s clip, no substantive fishing content |
| 1e6Oz5rAwRU | Tackle Express | tutorial | parameter-skim | done | techniques/inshore-crankbaits.md: added War Baits Neck Breaker point-reef/heavy-structure hardbait-avoidance rationale, medium confidence |
| 1l05hEXDaWw | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md: added light-drag/steady-tension fighting doctrine ('keep them asleep'), medium confidence |
| 1nBqYdvVrXY | Tackle Express | tutorial | parameter-skim | done | tackle/star-drag-vs-lever-drag.md + techniques/two-speed-low-gear-fight.md: narrow-spool two-speed casting counter-example + structure-context low-gear fight use, medium confidence |
| 28FQZvZ8v6k | Tackle Express | tutorial | parameter-skim | done | tackle/composite-rod-blank-construction.md (new) + tackle/rod-and-reel-selection.md: composite blank transition-line/taper mechanism, medium confidence |
| 2DfGpewNRYc | Tackle Express | tutorial | parameter-skim | done | none: generic packing/travel-logistics content, excluded by curation bar |
| 2Ee2DFZ9Wk4 | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md: Rapala Crush City Mooch Minnow parameters (fork-tail, material, suspended-fall use), medium confidence |
| 2QphkC2cK14 | Tackle Express | tutorial | parameter-skim | done | none: product plug for Shimano Sedona marketing features, no SoCal-specific parameters, fails curation bar |
| 2c8UomduE3c | Tackle Express | tutorial | parameter-skim | done | none: generic/out-of-region freshwater-bass tackle content |
| 2gmvTuXtu0Q | Tackle Express | tutorial | parameter-skim | done | none: freshwater bass-fishing crankbait content, no SoCal/Baja saltwater relevance |
| 2pkE9RwW1bU | Tackle Express | tutorial | parameter-skim | done | none / skipped: promotional product review (SKB backpack), no SoCal/Baja fishing knowledge content, generic gear-bag content excluded per curation bar |
| 3-0kaaHqA7A | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-night-bluefin-tg-jig-rig.md; tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md; techniques/knife-jigging.md / new tackle note (reel/metered-line/leader/depth ladder for night TG-jig bluefin) cross-linked from knife-jigging and the Searcher jig-ladder note |
| 3dyEQhMnPMU | Tackle Express | tutorial | parameter-skim | done | none / skipped: 36s clip, ASR-garbled/unidentifiable bait name, freshwater bass content, no SoCal/Baja saltwater relevance |
| 3n18taJWNEQ | Tackle Express | tutorial | parameter-skim | done | none / skipped: 60s fragmentary auto-captioned short, no SoCal-specific content, generic 'keep a bend in the rod' advice only |
| 3xx_vES0kdo | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-charter-bait-tank-hook-kit.md; tackle/hook-assortment-by-trip-length.md; tackle/hooks.md / new bait-tank-framed hook/leader checklist note, cross-linked, faithful to transcript |
| 3z1KZ_kIaec | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-rockfish-leader-line.md; species/rockfish-lingcod.md; tackle/line-and-leader.md; techniques/dropper-loop.md / new tackle note on rockfish dropper-loop leader material, cross-linked; evaluator trimmed duplicated restatement and fixed a smoothed line-size range |
| 41d5bquXkAc | Tackle Express | tutorial | parameter-skim | done | none / skipped: 35s pure-exclamation clip, no extractable technique/tackle/species content, fails curation bar |
| 46kVgZ6P62M | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-accurate-tern-2-reel.md; tackle/star-drag-vs-lever-drag.md / new Accurate Tern 2 product note (cast-control brake, twin drag, sizing/leader rule) plus a corroborating row in star-vs-lever-drag; evaluator fixed a fabricated Baja-framing claim bled over from an adjacent entry |
| 52jkCrA4I9w | Tackle Express | tutorial | parameter-skim | done | none / skipped: 26s clip, transcript captures only music/interjection, no extractable fishing-rod content despite title |
| 52le0jHiqyc | Tackle Express | tutorial | parameter-skim | done | none / skipped: 48s trade-show promo (booth/dates/venue/raffle), no fishing knowledge content, fails curation bar |
| 53FzsW4_U08 | Tackle Express | tutorial | parameter-skim | done | none / skipped: 40s team-intro/promo clip, captions are only music and stray letters, no speech content |
| 5EKrtI_f_xA | Tackle Express | tutorial | parameter-skim | done | none / skipped: 31s truncated clip, freshwater bass-tackle terminology, no SoCal/Baja saltwater content, no reason stated before cutoff |
| 5Fxwebsi9pU | Tackle Express | tutorial | parameter-skim | done | none / skipped: freshwater bass thermocline/blade-bait technique, illustrative placeholder depths, no SoCal/Baja saltwater relevance |
| 5OTBOIeQmis | Tackle Express | tutorial | parameter-skim | done | none / skipped: 34s fragmentary teaser clip, freshwater blade-bait/thermocline content, cuts off before delivering specifics |
| 5XWnm7ok09k | Tackle Express | tutorial | parameter-skim | done | lures/knife-jigs.md / corroborating finger-balance speed-vs-slow-pitch jig test, named speed-jig models (Nomad Streaker, Nature Boys, Shimano Flat Side), Rip Roller brand caution merged into existing entry |
| 5_z4pe7iH8k | Tackle Express | tutorial | parameter-skim | done | none / skipped: freshwater largemouth bass content (coves/points/spawn/shad), zero SoCal/Baja saltwater relevance |
| 5fxAN1Ofn8M | Tackle Express | tutorial | parameter-skim | done | species/sand-bass.md / appended attributed corroboration (unnamed ~20g bait, fall/winter, column-versatile, thumb-controlled fast sink) to existing suspended-bait-balls row |
| 5hnHrCUNk3Q | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md; tackle/gear-classes.md; tackle/rod-and-reel-selection.md / new reel size-ladder note (Speedmaster vs Fathom by line class for local offshore tuna/yellowtail/rockfish), linked from both parent notes |
| 5uEzREjLlLQ | Tackle Express | tutorial | parameter-skim | done | lures/tuna-poppers-and-stickbaits.md; species/calico-bass.md / Baja starter-kit tackle quantities merged into Colt Sniper stickbait entry, gear-summary cross-link added to calico-bass; evaluator ran link-maintenance |
| 6BzZotupVcs | Tackle Express | tutorial | parameter-skim | done | none / skipped: 16s generic motivational short, no SoCal/Baja-specific fishing knowledge |
| 6E39_PBt1P4 | Tackle Express | tutorial | parameter-skim | done | rigging/san-diego-jam-knot.md / merged two-tension-method + hook/swivel/clip/lure and mono/fluoro/braid applicability as corroborating parameter entry |
| 6SClBs16L2Y | Tackle Express | tutorial | parameter-skim | done | species/bluefin-tuna.md; techniques/knife-jigging.md; techniques/slow-pitch-jigging.md / added activity-axis slow-pitch-vs-speed-jig decision plus bluefin pick-bite jig-commotion tactic |
| 6Z6Dht20kTA | Tackle Express | tutorial | parameter-skim | done | techniques/yo-yo-iron.md / added common-failure entry: continuous in-school jigging spooks fish, bounce-vs-burn fix |
| 6dTz1640Y5c | Tackle Express | tutorial | parameter-skim | done | tackle/rod-action-testing-technique.md (new); tackle/rod-and-reel-selection.md / new note: hand-bend rod testing misreads action (artificial pivot, tip unreachable) |
| 6gwvP8_pjWc | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass wake-bait tutorial (Deps Buzzjet), correctly out of scope; no notes created; fixed stale extraction-log pending row |
| 6qz6aQ9PusA | Tackle Express | tutorial | parameter-skim | done | none / 35-second personal-banter clip about booking a trip, zero fishing knowledge content, correctly skipped |
| 6sfaYq9wMvQ | Tackle Express | tutorial | parameter-skim | done | none / 7-second clip, no fishing content in ASR caption, hashtags indicate freshwater bass/swimbait (out of scope) |
| 75lUj-uaArQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-icast2022-penn-fathom2-authority.md (new); tackle/gear-classes.md; tackle/star-drag-vs-lever-drag.md / ICAST 2022 promo: Penn Fathom II 40 Narrow SD gear-ratio retune + Penn Authority spec, confidence fixed to low (promotional) |
| 7AOtPUGwKDI | Tackle Express | tutorial | parameter-skim | done | none / generic finesse-vs-swimbait opinion, species/location unconfirmed, principle already captured with concrete figures in species/calico-bass.md |
| 7L7OVoXE7KU | Tackle Express | tutorial | parameter-skim | done | tackle/all-purpose-rod-line-rating.md (new); tackle/rod-and-reel-selection.md / new note: wide line-rating rod fished mid-range (15-40lb rod at 25-30lb) for summer offshore, plus island rod pairing; fixed cross-ref figure error |
| 7iJktLzCmLY | Tackle Express | tutorial | parameter-skim | done | none / 7-second transcript contains only [Music] and slow down, no substantive content |
| 7wdCk_LXezw | Tackle Express | tutorial | parameter-skim | done | none / 15s reaction clip, no spoken content beyond exclamations/music, nothing clears curation bar |
| 8FAgifEFSuU | Tackle Express | tutorial | parameter-skim | done | none / 36s hand-gesture retrieve demo, no bait/species/location/parameter named, cuts off mid-sentence |
| 8TO-tuYjwWk | Tackle Express | tutorial | parameter-skim | done | bait/fishing-live-bait.md; techniques/flyline.md; techniques/surface-iron.md / anchovy chum + fly-line mackerel-bycatch problem + collar-hook/iron-stickbait fix merged; two invented-reasoning passages trimmed by evaluator |
| 8U34yMGxvEw | Tackle Express | tutorial | parameter-skim | done | none / 32s clip is generic braid-material trivia plus truncated brand-naming sentence, no parameters stated |
| 8fSGyJL2GHM | Tackle Express | tutorial | parameter-skim | done | conditions/current-structure.md / added Observed note: multiple productive contour-line edges (inshore ridge vs steep outer footprint) on one structure |
| 8wbNDfihH1o | Tackle Express | tutorial | parameter-skim | done | none / 31s freshwater bass-lake trolling philosophy, no stated parameters, out of scope |
| 9-UtAaSacsc | Tackle Express | tutorial | parameter-skim | done | none / 71s holiday gift-guide promo naming Shimano/Mustad pliers with generic features, no SoCal/Baja decision content |
| 9MzNNwHiBXs | Tackle Express | tutorial | parameter-skim | done | species/white-seabass.md; tackle/tackle-express-charter-bait-tank-hook-kit.md / fin-bait-backup hook parameters (squid unavailable/weather) merged, ASR-uncertain hook sizes flagged not asserted |
| 9_iox_eRhpg | Tackle Express | tutorial | parameter-skim | done | none / 36s Damiki freshwater bass tackle promo, no SoCal/Baja saltwater content |
| 9a-Zy_D6c3w | Tackle Express | tutorial | parameter-skim | done | species/calico-bass.md; techniques/swimbaits.md / Beach bounce in ripping current stupid tube technique variant, unregistered channel medium confidence |
| 9ekSBpLG0GA | Tackle Express | tutorial | parameter-skim | done | none / 12-second clip, no extractable fishing content, correctly skipped |
| 9hXW9JCffsU | Tackle Express | tutorial | parameter-skim | done | tackle/rod-and-reel-selection.md; tackle/tackle-express-bates-edc-100-reel.md / new low-confidence product spec note for Bates EDC 100 DAB baitcaster, linked from inshore combo section |
| 9kGpcEHqIUc | Tackle Express | tutorial | parameter-skim | done | locations/cedros-island.md; tackle/hooks.md / Cedros yellowtail size data point (19-33lb) and Owner ST-66 hook upgrade citation merged into existing notes |
| 9qwsg-e9ECA | Tackle Express | tutorial | parameter-skim | done | techniques/drop-shot.md; species/california-halibut.md / surf drag-and-shake drop-shot cadence (drag=target length 22-30in, ~3-4ft strike radius) added to drop-shot technique + halibut router |
| A-D5MYB98yo | Tackle Express | tutorial | parameter-skim | done | none / 31-second fragment, no extractable parameters, duplicates existing vertical-jigging coverage |
| A6-KPjRwGSQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-accurate-valiant-2-spj-reel.md; techniques/slow-pitch-jigging.md; tackle/tackle-express-accurate-tern-2-reel.md / new low-confidence product note for Accurate Valiant 2 SPJ reel, linked from SPJ technique gear detail |
| A7rveRBkL-g | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-night-bluefin-tg-jig-rig.md / amended with day/surface rig variants, size-vs-lead/cast-distance comparison, durability claim, Captain Brian/Independence 189lb origin story |
| A8_ydUnS0CQ | Tackle Express | tutorial | parameter-skim | done | none / out-of-region freshwater Castaic Lake bass clip, cut off before any parameter stated |
| AJfDjN-7K4w | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass Carolina-rig tutorial, out of scope for SoCal/Baja saltwater KB |
| ALZtbMIOMBw | Tackle Express | tutorial | parameter-skim | done | none / 39s reaction-only clip, no extractable content |
| AhICQlAsreU | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-daiwa-saltiga-reel.md; tackle/rod-and-reel-selection.md / new low-confidence product note for Daiwa Saltiga reel (CRBB bearings, Digigear, Automatic Tournament Drag), linked from Saltiga 60 mention |
| B44kVCdUN0o | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-mustad-heavy-duty-pliers.md; tackle/reel-maintenance.md / new low-confidence product note for Mustad 7.5in pliers, other 6 products (freshwater bass tackle) skipped as out-of-scope |
| BGKH1ObX9Qs | Tackle Express | tutorial | parameter-skim | done | none / entirely freshwater trophy-bass swimbait tackle review, out of scope for saltwater SoCal/Baja KB |
| BNJlltYOpIk | Tackle Express | tutorial | parameter-skim | done | none / 32-second reaction clip, no spoken location/gear/reasoning parameters beyond title's unconfirmed X-Rap claim |
| BNp-gSOpWBw | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-jig-stick-trolling-outfit.md; tackle/gear-classes.md / new note on jig-stick-as-trolling-outfit dual use (gear pairing, clicker sequence), linked from jig-stick class row |
| BPxE3xn3gAc | Tackle Express | tutorial | parameter-skim | done | techniques/drop-shot.md; lures/bay-bass-plastics.md / light-finesse halibut drop-shot rig + Basstrix Flash Trick lure colors added; evaluator fixed an unsupported calico-bass gloss on presenter's green-bass comparison |
| Basv01kFjOs | Tackle Express | tutorial | parameter-skim | done | none / transcript is an unrelated Jet2 Holidays travel ad, zero fishing content |
| Bok0db0G4xE | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md; techniques/inshore-crankbaits.md / small-treble-to-Scrounger-head/cut-skirt-ChatterBait hook swap for big halibut; evaluator trimmed router duplication, kept implementation in technique note |
| BsWb5BQ1Tdc | Tackle Express | tutorial | parameter-skim | done | lures/knife-jigs.md; tackle/tackle-express-night-bluefin-tg-jig-rig.md / knife-jig downsizing trigger detail; Jarry rig name correction + anti-bind construction detail |
| BwDJ4VFvB3E | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater bass-fishing crankbait review, no SoCal/Baja saltwater relevance |
| CNMXkml1okI | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: no rig parameters, species, or location stated; speaker says reel model doesn't matter |
| CO8YU-TD8D4 | Tackle Express | tutorial | parameter-skim | done | none / 44s Shimano Current Sniper Scale Boost promo, no decision-grade or SoCal-specific content; extraction-log row filled in |
| CdgSBcN6PDo | Tackle Express | tutorial | parameter-skim | done | tackle/line-and-leader.md / added topwater floating-top-shot leader trick (1.5 ft/12 lb mono splice), medium confidence |
| CsKEtrcLgiQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-night-bluefin-tg-jig-rig.md / merged new TG-jig parameters (density, price, brands, surface outfit, rockfish open item), fixed relative-time |
| D0bQjAL0gGU | Tackle Express | tutorial | parameter-skim | done | species/rockfish-lingcod.md; techniques/rockfish-deep-dropping.md; sources/regulatory-claims.md / added hedged season-dependent depth-allowance data point (~800-850 ft) and torpedo-sinker rationale |
| D0oEQsTaL7A | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / Fathom 80 drag rating (50 lb) and build spec, medium confidence |
| DPrr0a3vQY0 | Tackle Express | tutorial | parameter-skim | escalated | escalated: guard: protected path touched: profiles/cameron/rods.md |
| DTvXJrtytwg | Tackle Express | tutorial | parameter-skim | done | tackle/jig-rod-rating-selection.md (new); tackle/all-purpose-rod-line-rating.md; tackle/rod-and-reel-selection.md / jig rods fish toward top of gram rating, not middle |
| DfLcSS-J3g4 | Tackle Express | tutorial | parameter-skim | done | tackle/all-purpose-rod-line-rating.md; tackle/composite-rod-blank-construction.md; tackle/drag-setting.md; tackle/rod-action-testing-technique.md; tackle/rod-length-for-angler-size.md; tackle/rod-blank-and-component-materials.md (new) / beginner 30lb bait-stick buying guide merged across 6 notes |
| DuNkl8F45NE | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-trophy-bluefin-jig-outfit.md (new); tackle/tackle-express-night-bluefin-tg-jig-rig.md; techniques/two-speed-low-gear-fight.md; species/bluefin-tuna.md / trophy-bluefin jig outfit, pinwheel fight-timing, fixed phantom Talica 25 to Avet HXW |
| DvhRMHw57c4 | Tackle Express | tutorial | parameter-skim | done | none / skipped: no extractable content (15s reaction-only clip) |
| E273T9jAmpg | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-saltiga-35-vs-talica-12-reel-sizing.md (new) / spec comparison, weight/capacity/drag/gear-ratio, cross-linked |
| E4CDqBFOaP8 | Tackle Express | tutorial | parameter-skim | done | lures/lucky-craft-flash-minnow.md (new); species/california-halibut.md; techniques/inshore-crankbaits.md / new lure note (trimmed duplication), halibut router update, stub fill |
| E4H9QB7UBbU | Tackle Express | tutorial | parameter-skim | done | none / out-of-scope freshwater-trout reel spec content, correctly skipped |
| EVqKoSZK5Dk | Tackle Express | tutorial | parameter-skim | done | none / skipped: freshwater bass swimbait casting content, out of scope; extraction-log row filled |
| EXqFODWABvM | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: resort/travel-time chatter, no named location, technique, or parameter |
| EcNijcqjLvE | Tackle Express | tutorial | parameter-skim | done | none / out-of-scope freshwater bass swimbait tuning content; extraction-log row filled |
| Ecqt-ZLnvaU | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-izorline-xxx-mono.md (new); tackle/line-and-leader.md / low-confidence Izorline XXX mono note, sponsored counterpoint linked |
| EdN3BowjYjg | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: promotional reel-bag product showcase, fails curation bar |
| Eo_bA8IWvyU | Tackle Express | tutorial | parameter-skim | done | rigging/leadhead-mods.md; species/white-seabass.md; tackle/tackle-express-charter-bait-tank-hook-kit.md; techniques/dropper-loop.md; techniques/sliding-sinker.md; tackle/tackle-express-white-seabass-rod-reel-line.md / parameter-skim extraction of dropper-loop/leadhead/slider/jig-soak/artificials rigs, hook-size ASR corroboration, and a new rod-reel-line tackle note |
| EuYOlsnxXko | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md / Merged Tackle Express/Shannon Gallagher grunion-cycle beach-timing parameters (staging birds, incoming-tide afternoon window, morning low-tide concentration, fall 9-11ft structure pattern) into the Where and when section, fixed two invented claims not supported by the transcript |
| F0849S6gBPY | Tackle Express | tutorial | parameter-skim | done | none / skipped: no extractable content (30s intro/teaser clip, cuts off before any technique or parameter is stated, near-verbatim re-cut of BPxE3xn3gAc already captured in techniques/drop-shot.md) |
| FR7Cg9Jqug4 | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: patch filed a lure-less, location-less 37s clip into techniques/inshore-crankbaits.md on strength of treble/assist-hook fight description whose only concrete example (big stripers down deep) reads as freshwater swimbait fishing, not this saltwater note's fishery; out-of-region content with no confirmed applicability, compliant move is exclusion |
| F_KDQo-k7CQ | Tackle Express | tutorial | parameter-skim | done | none / skipped: 28s auto-caption transcript contains only [music] tags and Heat Heat, no extractable content beyond the title |
| Fj1-SsbksRM | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: 35s fragment on Damiki Vault blade bait, generic/freshwater-bass content with no SoCal-specific parameter |
| G8HNjPiaOjU | Tackle Express | tutorial | parameter-skim | done | tackle/rod-action-testing-technique.md / parameter-skim merge of built-different rationale into existing tip-pull diagnostic, flagged as likely re-cut of DfLcSS-J3g4 (not independent confirmation) |
| Ga8Z1PyBqdE | Tackle Express | tutorial | parameter-skim | done | rigging/essential-knots.md / fifth corroborating data point on uni-to-uni: wrap count, tag length, cinch sequence |
| GchQpXW2jI0 | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: 29s teaser clip, product name-drop with no extractable content |
| GeydGK-62fw | Tackle Express | tutorial | parameter-skim | done | techniques/knife-jigging.md / corroborating medium-confidence addition to existing 60-degree rod-angle doctrine; fabricated reel/shock-absorber mechanism stripped by evaluator |
| H5Z-Mqt4qXs | Tackle Express | tutorial | parameter-skim | done | techniques/inshore-crankbaits.md / Tackle Express beach-channel sink-rate/current, color-by-clarity, and named Bassday Gyokusai 97 floater merged in |
| HQC-NwW4018 | Tackle Express | tutorial | parameter-skim | done | techniques/yo-yo-iron.md / Colt Sniper dual-mode cast-and-swim/cast-and-yo-yo doctrine plus smaller-profile Observed bullet merged in |
| HQH_1XxBx7w | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: auto-captions contain no fishing content, only stray word and music markers |
| HXsiiSWsfOY | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 30s on-the-water catch clip, only fragmented exclamations/names, no content clears curation bar |
| IHKuTb93XEU | Tackle Express | tutorial | parameter-skim | done | none / skipped: generic freshwater/trout ultralight rod product ranking, no SoCal/Baja content, fails curation bar |
| IUuP8gGaAAo | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-charter-bait-tank-hook-kit.md / corroborating occasion-to-hook-model map (Owner Flyliner ring/non-ring, Aki Twist, gorilla, Mutu circle) merged in |
| IXHHNOX_t5Y | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass-lake color-selection short, correctly skipped as out-of-scope for SoCal/Baja saltwater KB |
| IZHY3RXdyxg | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md / corroborating bullet quantifying 9-of-10 no-swing guidance on Owner Mutu circle hooks added to circle-vs-J section |
| IcS7QbJlSDA | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-bait-tank-time-saver.md; species/rockfish-lingcod.md; tackle/tackle-express-rockfish-leader-line.md / new note: artificial double-8 octopus bait-tank substitute on rock-cod dropper-loop rig, cross-checked against re-cut source qh3hL2Dt3HY |
| IqpeK5Xfhes | Tackle Express | tutorial | parameter-skim | done | techniques/fighting-fish-from-the-rail.md / added hip-braced rod posture as a companion default to rail-bracing, medium confidence |
| IxfTRWmMqQU | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md / merged Tackle Express thin-braid/jig-vs-bait-rig comparison into Weight & staying off the snag section |
| J40VxLNuZhk | Tackle Express | tutorial | parameter-skim | done | fish-care/sculpin-handling.md; species/rockfish-lingcod.md / merged rockfish mucus-vs-sculpin-venom safety point and deckhand practice; fixed missing front-matter source |
| JFauRUaz2AQ | Tackle Express | tutorial | parameter-skim | done | none / skipped: 34s fragment, freshwater Vault-Blade blade-bait vertical-presentation technique for suspended bass, no SoCal/Baja content |
| JJwyof_Nxqs | Tackle Express | tutorial | parameter-skim | done | none / freshwater largemouth-bass topwater/Kastmaster clip at Castaic Lake, out of scope for SoCal/Baja saltwater KB, skipped |
| JLaql6UUFVs | Tackle Express | tutorial | parameter-skim | done | none / out-of-domain freshwater bass jig-color content (Castaic/Pyramid lakes), no SoCal/Baja saltwater knowledge, correctly skipped |
| JNMwUUst1rw | Tackle Express | tutorial | parameter-skim | done | none / 12s fragment, captions reduce to disconnected words, no extractable content |
| JUcsUMJize0 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / added Speedmaster free-spool/SARB bearing spec and fly-lining/casting rationale |
| JekeeKZA1Kw | Tackle Express | tutorial | parameter-skim | done | none / freshwater reservoir bass jerkbait tackle picks, no SoCal/Baja saltwater relevance, correctly skipped |
| JgD1gOuQAaE | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-daiwa-saltiga-reel.md; tackle/tackle-express-saltiga-35-vs-talica-12-reel-sizing.md / added large-pair specs, lever-drag-stop and handle-style decision content, resolved pinion caption ambiguity; fixed fabricated handle-material attribution |
| JgXMpjxRxmo | Tackle Express | tutorial | parameter-skim | done | lures/iron-jigs.md; lures/tuna-poppers-and-stickbaits.md; techniques/surface-iron.md / merged small-anchovy iron-downsizing corroboration and Colt Sniper warm-water retrieve/Daiwa SP Minnow mention |
| JmGT0zAaVOY | Tackle Express | tutorial | parameter-skim | done | tackle/spooling-line-tension-and-twist.md; tackle/reel-maintenance.md / new note on spooling tension/line-twist mechanics, cross-linked from reel-maintenance.md |
| K50W5KaBN4E | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass finesse-rig tutorial, out of SoCal/Baja saltwater scope, correctly skipped |
| KFdvKXTHSeU | Tackle Express | tutorial | parameter-skim | done | lures/bay-bass-plastics.md / added Zoom Fluke nose-entry/shank-exposure rigging detail for underwater walk-the-dog action |
| KUsFT7tN-x0 | Tackle Express | tutorial | parameter-skim | done | rigging/leadhead-mods.md / added Warbaits Neck Breaker jig-head alternative to sliding-sinker section; fixed unsupported spinning-rod inference |
| K_0AeM4OvuE | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / merged full reel spec ladder, shift/drag/handle comparison; fixed two ASR-artifact inaccuracies |
| KamUiykeRlU | Tackle Express | tutorial | parameter-skim | done | tackle/rod-action-testing-technique.md / merged brand-lineup fit-variance and pain-test doctrine; trimmed redundant restatement |
| KjVLn4cWHbc | Tackle Express | tutorial | parameter-skim | done | planning/electronics-and-sounder.md / added bullet on running/stacking sounder marks depth-by-depth before committing to a stop |
| KqluHwsDicw | Tackle Express | tutorial | parameter-skim | done | none / generic freshwater bass wacky-rig/Texas-rig hook-set tip, out of SoCal/Baja saltwater scope, correctly skipped |
| LAQZOoEUZA0 | Tackle Express | tutorial | parameter-skim | done | none / promotional SKB backpack product spec/review, no SoCal/Baja fishing decision knowledge, curation bar excludes generic bags |
| LB9sUjDcRUw | Tackle Express | tutorial | parameter-skim | done | none / 11-second clip, ASR captured only 'uh', no fishing content or rationale stated |
| LKOL9g-qhSM | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: freshwater tournament-bass content, no SoCal/Baja saltwater knowledge present |
| LRRoGT2W4WY | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / merged O-ring/band placement parameter (bottom of egg-sack smooth section, closer to head; balance-driven; same across 4-in/5-in/Senko) |
| L_YH_xT7Pfs | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md; tackle/tackle-express-bkk-titan-diver-swimbait-hooks.md / new tackle note for BKK Titan Diver/Titan Diver Plus swimbait hooks, linked from soft-plastic-swimbaits.md |
| Lj2NCznK7Zg | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shogun-maxcuatro-braid.md; tackle/line-and-leader.md; tackle/tackle-express-night-bluefin-tg-jig-rig.md; techniques/knife-jigging.md / new note + cross-links for Power Pro Maxcuatro braid and reel/rod pairings from Shogun bluefin trip |
| LoJu3OYs20o | Tackle Express | tutorial | parameter-skim | done | lures/tuna-poppers-and-stickbaits.md / name-resolution (Tuna Propper) + mechanism-reason parameter added to existing Clear Choice TP entry, low confidence |
| M2qZiY2lR98 | Tackle Express | tutorial | parameter-skim | done | techniques/drop-shot.md / added VMC Spin Shot swivel-hook as distinct hook option, medium confidence |
| M4G8IKsZEFU | Tackle Express | tutorial | parameter-skim | done | lures/crocodile-spoons.md; lures/iron-jigs.md / new lure note for JP Standard/JP Micro crocodile-spoon swim-type distinction, linked from iron-jigs.md |
| M9_nvBPajDU | Tackle Express | tutorial | parameter-skim | done | tackle/drag-setting.md / amended note with drag-washer damage mechanism for off-free-spool lever adjustment, cross-linked to existing judgment-call doctrine |
| M9nIhEsKsqU | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: near-verbatim re-cut of E4CDqBFOaP8, already captured in lures/lucky-craft-flash-minnow.md |
| ME2jrqS_5bo | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: generic wacky-rig bite-detection tips, no SoCal/Baja-specific content, fails curation bar |
| MKe-Xu4XsGk | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 15s clip, transcript only a single garbled ASR token, no content to capture |
| MbYjzhHsiTU | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: 100% freshwater bass lure preview, no SoCal/Baja saltwater content |
| N24NBweNK4o | Tackle Express | tutorial | parameter-skim | done | rigging/wiring-a-surface-iron.md / added swivel-on-split-ring anti-twist entry for mini-iron jig; noted duplicate pairing with pending auiXY0R9ri8 |
| NBSJsN7uTKQ | Tackle Express | tutorial | parameter-skim | done | lures/bay-bass-plastics.md / added C3 Baits Shimmy rigging detail (hook-entry-matches-bend technique), medium confidence |
| NF8AJjqsDO8 | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: freshwater bass drop-shot color content at Castaic Lake, out of scope |
| NGkXPkE8kWI | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: generic Huddleston Weedless Shad product-spec plug, no SoCal-specific content |
| NGvwjJfAL2I | Tackle Express | tutorial | parameter-skim | done | none / skipped: generic filler/fragment, no extractable SoCal-specific parameter |
| NJh9EadWA7Y | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: family fight-coaching clip, no extractable technique/gear content |
| NUlHwrBT61U | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: generic/promotional spool-design blurb, no SoCal-specific parameter |
| NiEvdaHOHnM | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: personal lifestyle aside, no fishing knowledge content |
| Nsc23Chy3xk | Tackle Express | tutorial | parameter-skim | done | none: correctly skipped: freshwater bass/bluegill chartreuse-marker color theory, no SoCal/Baja saltwater content, fails curation bar |
| O49WsHP4Zh0 | Tackle Express | tutorial | parameter-skim | done | techniques/sliding-sinker.md: Amended sliding-sinker technique note with a Tackle Express long-leader/loose-drag/no-cast build variant (medium confidence, unregistered channel); fixed inaccurate above cross-reference during review. |
| O5t36yWGXCU | Tackle Express | tutorial | parameter-skim | done | none: correctly skipped: freshwater ultralight-reel product rundown, no SoCal/Baja-specific content, fails curation bar |
| OFEpEeFomp4 | Tackle Express | tutorial | parameter-skim | done | none: correctly skipped freshwater ultralight trout gear rundown (no SoCal/Baja saltwater content) |
| OKFUMvJbacE | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: no species/location evidence in 36s clip, ambiguous freshwater-vs-saltwater bass, extractor's sand-bass attribution unsupported |
| OURS05qEGcA | Tackle Express | tutorial | parameter-skim | done | techniques/leadhead-swimbait-retrieve.md; species/california-halibut.md; techniques/swimbaits.md; lures/soft-plastic-swimbaits.md / new technique note for leadhead-swimbait count-and-pause retrieve, wired into halibut router and cross-linked from swimbait notes |
| OdRZIDBO6Mg | Tackle Express | tutorial | parameter-skim | done | tackle/star-drag-vs-lever-drag.md; techniques/rockfish-deep-dropping.md / two-speed-vs-single-speed application rules merged into both notes, medium confidence |
| Oi5n-uVpY9g | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md; tackle/line-and-leader.md; techniques/leadhead-swimbait-retrieve.md / tackle-shop minimum-buy gear parameters merged as attributed medium-confidence bullets; two faithfulness fixes applied |
| OitNR_M4lxw | Tackle Express | tutorial | parameter-skim | done | none: correctly skipped freshwater blade-bait willow-leaf/kite-tail mod, no SoCal/Baja saltwater content |
| Ol3RPAsImg0 | Tackle Express | tutorial | parameter-skim | done | none: correctly skipped 25s promotional blurb for Duo Realis Spy baits, no extractable parameters, fails curation bar |
| OuO4Irjrat8 | Tackle Express | tutorial | parameter-skim | done | none: nothing extractable: freshwater bass/Alabama-rig content, entirely out of SoCal/Baja saltwater scope |
| Ow87j6AALAY | Tackle Express | tutorial | parameter-skim | done | none: nothing extractable: 45s of on-the-water outcome/banter narration with no parameters or stated reasoning |
| OxFyTk0CSZQ | Tackle Express | tutorial | parameter-skim | done | none: correctly skipped 55s charter raffle/hype clip, only technical aside already covered elsewhere, fails curation bar |
| PJEG_RIkzF0 | Tackle Express | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md; species/california-halibut.md / merged poly-rope-vs-fine/soft-mesh release-net finding, cross-linked from halibut fighting/release section |
| PNWsFa4iSSc | Tackle Express | tutorial | parameter-skim | done | none: nothing extractable: unresolved productivity-percentage anecdote, no parameters, cut off before example resolves |
| PPCzxTzXF0k | Tackle Express | tutorial | parameter-skim | done | none: nothing extractable: freshwater bass fishing content (blade bait / suspended bass), out of SoCal/Baja scope |
| PbiZMk4Ft6w | Tackle Express | tutorial | parameter-skim | done | tackle/jig-rod-rating-selection.md / merged rod-power-vs-jig-weight rule (150g jig/609 too stiff, drop to 7 or 6 power), medium confidence |
| PcJUo7h8WQA | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / PK3/PK5 tail-spin update, hook swap, winter/neck-breaker rig, colors merged into PK-series section, medium confidence |
| PciIsDkBgj4 | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md / merged fly-liner/J-hook hookset mechanics as attributed second Tackle Express clip, re-cut caveat noted, medium confidence |
| PfHjk3G0yek | Tackle Express | tutorial | parameter-skim | done | none: nothing extractable: 29s auto-captioned fragment, only numbers reference off-screen diagram, no anchorable SoCal parameter |
| Pn3BcC_IN9Y | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: freshwater largemouth-bass topwater-lure clip (Jackall Pompadour Jr), no SoCal/Baja saltwater content, fails curation bar |
| PnAnAS6QoG8 | Tackle Express | tutorial | parameter-skim | done | rigging/leadhead-mods.md; tackle/line-and-leader.md / banana-head + fluorocarbon parameter-skim merged; evaluator removed fabricated Ventura/Oxnard detail and resolved relative-time phrase |
| PoTRe9SRjm8 | Tackle Express | tutorial | parameter-skim | done | tackle/spooling-line-tension-and-twist.md / new section: spinning-reel reverse line-lay taper as distinct wind-knot cause, medium confidence |
| Pxky7drjPkU | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-minnow-rod.md; tackle/gear-classes.md; techniques/leadhead-swimbait-retrieve.md / new tackle note for minnow-style spinning rod power/tip pick, cross-linked; evaluator fixed one invented reasoning detail |
| PzjZxCRKXpc | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 27s ICAST 2022 teaser/promo, no fishing knowledge content |
| Q14rHkHGBsk | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 46s social/promo clip, boat chatter and fish hold-up only, no fishing-knowledge content |
| Q4WWkbc9nag | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-bait-tank-time-saver.md; tackle/tackle-express-charter-bait-tank-hook-kit.md / pre-scented packaged bait, double dropper loop, 1/0 Owner Aki Twist hooks merged; evaluator removed unsupported rock-cod inference |
| Q4sW6JRQzAY | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-trophy-bluefin-jig-outfit.md / 2025 recap folded into existing 2022 note as dated side-by-side citations (jig weight band, rig reasoning, reel/spectra class) |
| Q6ACpkS93sk | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-bait-tank-time-saver.md / corroborating citation: double dropper loop for SoCal rockfish, torpedo sinker, Owner Aki Twist 1/0 example |
| QEmxUIGmKbo | Tackle Express | tutorial | parameter-skim | done | species/white-seabass.md; species/yellowtail.md; tackle/tackle-express-white-seabass-rod-reel-line.md; tackle/tackle-express-casting-reel-for-seabass-yellowtail.md / casting-reel-over-heavy-tuna-gear recommendation added to both species routers and new tackle note |
| QEpa3WYbEa8 | Tackle Express | tutorial | parameter-skim | done | none / skipped: 23s reaction clip, no rig/technique parameters spoken despite title |
| QJd7A6oiV4U | Tackle Express | tutorial | parameter-skim | done | techniques/beach-lure-depth-control.md; species/california-halibut.md; techniques/inshore-crankbaits.md; techniques/leadhead-swimbait-retrieve.md / new technique note: rod-tip depth control across lure classes, cross-linked |
| QJeYLzFEbzs | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater Florida-strain largemouth bass wacky-rig content at Castaic Lake, out of scope |
| QP6c8vcslVs | Tackle Express | tutorial | parameter-skim | done | planning/electronics-and-sounder.md / merged as second source (re-cut of KjVLn4cWHbc) confirming 20/40/60ft search pattern bullet; evaluator removed unsupported suspended/structure claim |
| QQlQcPXARWk | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-penn-handle-knob-replacement.md; tackle/reel-maintenance.md; tackle/tackle-express-speedmaster-fathom-reel-sizing.md / new note for Penn Fathom/Torque/Squall handle-knob kit; evaluator corrected confidence low->medium |
| QTq-G2y237w | Tackle Express | tutorial | parameter-skim | done | none / skipped: freshwater bass tackle (Senko/Carolina rig/Ned rig/Nako rig), no SoCal/Baja saltwater content |
| Qj6brwOJk9E | Tackle Express | tutorial | parameter-skim | done | tackle/star-drag-vs-lever-drag.md; techniques/rockfish-deep-dropping.md / third citation on 2-speed reels for SoCal rockfishing (depth, sinker weight, two-hook retrieve, gear-ratio fatigue), medium confidence |
| Qqdt6f8Mjd4 | Tackle Express | tutorial | parameter-skim | done | lures/lucky-craft-flash-minnow.md; species/california-halibut.md / halibut lure color-selection doctrine (white default, white/pink-belly, pink for surf halibut) added, medium confidence |
| R0TQ7Afsh6Y | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 45s product ad for Deps Buzzjet trout-series wakebait, freshwater trout species, no SoCal/Baja saltwater content |
| R1spZEO1V-0 | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: near-verbatim re-cut of E4CDqBFOaP8, already captured in species/california-halibut.md and lures/lucky-craft-flash-minnow.md |
| R4yYK90-cZM | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / parameter-skim add: Megabass Sleeper Gills hollow-body/hidden-hook construction, jig-or-straight-swim, low confidence (promotional stock-alert) |
| R6ErrEIjlWw | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / added nested rigging sub-bullet (nose-hook/twist/exit-point-match + 3-in variant + field fix) under War Baits neck-breaker bullet, medium confidence; fixed pre-existing front-matter sources gap for XyKF34C5iB4 |
| RKfI8g_aRu8 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-daiwa-luvias-st-spinning-reel.md; tackle/gear-classes.md / new low-confidence tackle spec-sheet note for Daiwa Luvias ST, linked from gear-classes.md, ASR uncertainties flagged (Zaion/monocoque, 20000->2000) |
| RbOWJ0BAqSo | Tackle Express | tutorial | parameter-skim | done | tackle/rod-length-for-angler-size.md / added as corroborating re-cut source on existing 7.5-8ft rod-length doctrine (casting distance, leverage point, travel/shipping); medium confidence retained |
| RoBoQ6kulwA | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 38s clip is DIY spool-rack/wing-nut storage fixture demo, no fishing species/technique/parameter/region content, fails curation bar |
| Rtwz0oEfrKw | Tackle Express | tutorial | parameter-skim | done | tackle/line-and-leader.md / parameter-skim: added straight-pull 80lb-braid-doesn't-break claim + 65lb/200g-and-under jig-braid working choice with hull-abrasion caveat, medium confidence |
| S0-BCQWA0H4 | Tackle Express | tutorial | parameter-skim | done | techniques/yo-yo-iron.md / merged as earlier same-channel elaboration of existing 'don't jig in place inside a marked school' entry: sonar-marking + drop-to-bottom + rip-or-yo-yo mechanics |
| S9sQ8Vg8-5o | Tackle Express | tutorial | parameter-skim | done | lures/iron-jigs.md; lures/knife-jigs.md; species/rockfish-lingcod.md; tackle/tackle-express-rockfish-leader-line.md; techniques/dropper-loop.md; techniques/rockfish-deep-dropping.md; techniques/wind-in-your-face-positioning.md / parameter-skim of full rockfish gear-guide merged across 7 notes; de-duplicated 5 previously-separate short-clip citations as re-cuts of this video |
| SDNXNdGdmSQ | Tackle Express | tutorial | parameter-skim | done | none / skipped: out-of-scope freshwater bass content, no SoCal/Baja saltwater fishing knowledge present |
| SH5CZQi9ATw | Tackle Express | tutorial | parameter-skim | done | techniques/yo-yo-iron.md / merged 'rip it through' mechanism (heavy thermocline mark not necessarily a true school; ripping stirs and fires fish into chasing) into existing burn/rip-it-up entry, plus multi-angler and keep-lures-in-water add-ons |
| SK2M7L2vA1s | Tackle Express | tutorial | parameter-skim | done | rigging/dropper-loop-knot-and-spider-hitch.md; rigging/essential-knots.md; rigging/tony-pena-knot.md; rigging/seaguar-knot.md; techniques/dropper-loop.md / new dropper-loop-knot/spider-hitch note; second same-name Tony Pena tie added side by side; Seaguar-knot sixth variant added; Palomar quote attribution fixed |
| SL4zZbzdXNA | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-baja-light-setup-yellowtail-insurance.md; species/yellowtail.md; tackle/tackle-express-casting-reel-for-seabass-yellowtail.md / new tackle note: light Baja bass/halibut setup (15-30lb rod, Shimano Tranx 400, 50lb braid ~300yd, 15ft/40lb fluoro leader as yellowtail insurance), linked from yellowtail gear summary |
| SR-Fv3xxkVY | Tackle Express | tutorial | parameter-skim | done | none / no extractable content: auto-captioned transcript is incidental crew chatter, no rigging/kite/technique detail despite title |
| Sb20NtuNlkc | Tackle Express | tutorial | parameter-skim | done | none / correctly out-of-scope: freshwater largemouth-bass wakebait tackle video, no SoCal/Baja marine content |
| SbTEGKmWl7g | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: generic rod-transport/travel-packing tips (rod sleeves, rod straps), no SoCal/Baja-specific content, correctly skipped per curation bar |
| SclIN_ceduA | Tackle Express | tutorial | parameter-skim | escalated | escalated: guard: protected path touched: profiles/cameron/tackle.md |
| Se7bjtiiGv8 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater trout jerkbait clip, no SoCal/Baja species/location/parameters, out of KB scope |
| T33JsoZHO_c | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / added fluke lead-head weight-selection bullet (2oz bottom-bounce halibut vs 3/4oz suspended seabass/kelp), naming Nomad/Z-Man/Redemption flukes, cross-linked to california-halibut.md and white-seabass.md |
| T_XpItMhbjM | Tackle Express | tutorial | parameter-skim | done | lures/rapala-husky-magnum.md; lures/tuna-poppers-and-stickbaits.md / Husky Mag speed/color specs (5-6kt vs 12kt, Wahoo/Swordfish colors) and X-Rap Long Cast weight/hook data (1 7/8oz vs 1.5oz, stock singles); fixed silently-reconciled stock-hook contradiction, kept side by side |
| TdrFjnJb3Y0 | Tackle Express | tutorial | parameter-skim | done | none / skipped: freshwater trout promotional/sponsored product pitch, out of SoCal/Baja saltwater KB scope, no decision knowledge |
| TjQuU-x8sHM | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-ci4-plus-reel-features.md; tackle/reel-maintenance.md / new capped-low product-feature note for an unnamed Shimano reel (CI4+/Infinity Drive/Infinity Cross/Anti-Twist Fin), cross-linked from reel-maintenance.md's servicing section |
| To2Dvx3Ifnc | Tackle Express | tutorial | parameter-skim | done | rigging/pr-knot.md; rigging/essential-knots.md; rigging/fg-and-albright.md / new PR-knot note (bobbin-tied FG alternative), disambiguated from existing RP knot, linked from both parents |
| TwnvOIp38tI | Tackle Express | tutorial | parameter-skim | done | none / skipped: promotional bass-fishing (freshwater) product-announcement clip, no SoCal/Baja saltwater fishing knowledge present |
| TyxH9BBJ9U8 | Tackle Express | tutorial | parameter-skim | done | tackle/rod-blank-and-component-materials.md / provenance-only merge: confirmed re-cut/reposted clip of DfLcSS-J3g4's blank-material segment, added as source (not independent confirmation), no new note |
| TzK4iuVmUSE | Tackle Express | tutorial | parameter-skim | done | techniques/leadhead-swimbait-retrieve.md / added Hookset — don't swing section (grip-and-feel, wind-to-drag-slip mechanic) to existing leadhead/halibut retrieve note; fixed one invented direction detail |
| UASU-ikU1AQ | Tackle Express | tutorial | parameter-skim | done | none / skipped, no extractable knowledge content — 20s reaction/gaff clip |
| UXt-pR6bBjY | Tackle Express | tutorial | parameter-skim | done | none / correctly-scoped skip (generic extruded-line/mono-stretch 101 content, no SoCal/Baja parameters) |
| U_jXfgsGBzM | Tackle Express | tutorial | parameter-skim | done | tackle/rod-blank-and-component-materials.md / provenance-only merge: confirmed re-cut of DfLcSS-J3g4's grip-material segment, added as source, no new note |
| UbbkPKZ8_W4 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-maxcuatro-vs-depth-hunter-offshore.md; tackle/line-and-leader.md; tackle/tackle-express-night-bluefin-tg-jig-rig.md; tackle/tackle-express-shogun-maxcuatro-braid.md / new head-to-head product-comparison note (low confidence, sponsored), cross-linked |
| UtFX1K01bA4 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: generic lure-storage-wallet product description, excluded under curation bar (bags/accessories) |
| UtgMbyjlem8 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: generic reel-tier sales pitch, no concrete parameters, fails curation bar |
| V1tmGZh3MNg | Tackle Express | tutorial | parameter-skim | done | none / freshwater trout tackle-shop promo, no SoCal/Baja saltwater content — nothing extractable |
| V4opuMirbDU | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / provenance-only merge of duplicate same-channel fluke lead-head weight claim (3/4oz suspended vs 2oz bottom/halibut), already captured from T33JsoZHO_c |
| V54mcLzTubc | Tackle Express | tutorial | parameter-skim | done | none / freshwater trout clip, 20s auto-caption fragment only, no SoCal/Baja saltwater content — nothing extractable |
| VH5_kvuGGQY | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater bass Senko/Neko-worm tackle talk, no SoCal/Baja saltwater content, fragment ends before payoff |
| V_WjP52OJ7M | Tackle Express | tutorial | parameter-skim | done | none / transcript contains no substantive content (music-only, no speech); correctly skipped |
| Vbf40qvH9-Q | Tackle Express | tutorial | parameter-skim | done | conditions/current-diagnostics.md; techniques/flat-fall-jigging.md; techniques/yo-yo-iron.md / new Line scope cross-technique subsection added to current-diagnostics.md, backlinked from yo-yo-iron.md and flat-fall-jigging.md |
| Vjdv8o7otKY | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 43s Tackle Express product ad for the Shimano Current Sniper jig, no decision-grade parameters beyond what's already documented |
| Vl0BuetK2D0 | Tackle Express | tutorial | parameter-skim | done | techniques/clearing-a-backlash.md; tackle/reel-maintenance.md; techniques/underhand-casting.md / new technique note for hand-tensioning a backlash clear, cross-linked from underhand-casting.md and reel-maintenance.md |
| VotK9jwqRJ8 | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: freshwater bass/trout jerkbait-and-chatterbait line-preference chatter, no SoCal/Baja relevance, matches channel's own out-of-scope precedent |
| W0mj_LA-qcM | Tackle Express | tutorial | parameter-skim | done | tackle/rod-length-for-angler-size.md / re-cut of existing Tackle Express 9ft-rod doctrine, folded in as one new stated reason under point 4 (can't stand back far enough on a crowded rail); confidence held at medium, no new note created |
| WHLz0kR___I | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md / Added dangling-gangion bite-detection/hookset section (rod-tip tell, swing+turn vs turn-only preference), correctly cross-referenced against the existing wind-retrieve don't-swing doctrine as a different rig, not a conflict |
| WPYrq_jdK2o | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-bkk-titan-diver-swimbait-hooks.md; lures/soft-plastic-swimbaits.md / rigging steps for Kicker Pickle Kick on BKK Titan Diver center-pin spring merged into existing tackle note (confidence low->medium), cross-linked from soft-plastic-swimbaits.md, PK abbreviation confirmed as Pickle Kick |
| WeabGOvhgto | Tackle Express | tutorial | parameter-skim | done | techniques/spinning-reel-wind-knots.md; tackle/spooling-line-tension-and-twist.md; tackle/reel-maintenance.md; techniques/surface-iron-casting.md / new technique note for the casting-side (come-tight) wind-knot cause, cross-linked from the spooling note, surface-iron-casting, and reel-maintenance; fixed a README auto-summary truncation bug in the note's opening paragraph |
| Wk4wKFLbWEQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-saltiga-300-round-jigging-reel.md; tackle/tackle-express-daiwa-saltiga-reel.md; tackle/tackle-express-saltiga-35-vs-talica-12-reel-sizing.md / new low-confidence tackle note for the Saltiga 300 Round jigging reel (promotional product feature, correctly capped at low), cross-linked with the two existing Saltiga notes without merging their specs |
| X-itrm5QkcM | Tackle Express | tutorial | parameter-skim | done | species/white-seabass.md; techniques/swimbaits.md / Added a species-router row + a technique subsection on flanking fluke casters vs. the bait-rail dropper-loop crowd on a WSB drift, correctly capped at medium confidence, cross-linked both ways |
| XY4ZYDqD4Ag | Tackle Express | tutorial | parameter-skim | done | skipped: transcript is 11 seconds of auto-generated captions containing only interjections, no fishing knowledge despite the title, correctly extracted nothing |
| XfpUV_z5gFI | Tackle Express | tutorial | parameter-skim | done | lures/lucky-craft-flash-minnow.md / Added attributed white-belly theory (Tackle Express, medium confidence) as a companion rationale to existing color-selection doctrine, after removing an invented biological explanation not present in source |
| XtPUnC5jQnM | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-trophy-bluefin-jig-outfit.md / merged a second stated reason (jig-descent/retrieve effort) for thin braid into the existing reel/line ladder section, fixed two invented/unhedged claims in the extractor's patch |
| XxN7EzNDnf8 | Tackle Express | tutorial | parameter-skim | done | lures/knife-jigs.md / added as a source, correctly flagged as a re-cut/duplicate of S9sQ8Vg8-5o footage and explicitly excluded from independent corroboration |
| Y5crw_rQpeg | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-chad-fathom-lowprofile-surf-combo.md; tackle/tackle-express-casting-reel-for-seabass-yellowtail.md; tackle/tackle-express-mustad-heavy-duty-pliers.md; techniques/beach-lure-depth-control.md / new low-confidence tackle note (Penn Fathom Low Profile / Okuma Seros / Daiwa HMKL surf combo) created and cross-linked; one overclaiming link description fixed |
| YWTDpG6yYWo | Tackle Express | tutorial | parameter-skim | done | tackle/spooling-line-tension-and-twist.md / merged washer-position mechanism/fix into the existing line-lay-taper section, filling the gap the diagnostic-only PoTRe9SRjm8 clip left open |
| YyW4-8FRjn8 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-nasci-fc-reel.md; tackle/reel-maintenance.md / New capped-low product-feature note for the Nasci FC (X-Ship, Propulsion Line System, Core Protect vs. Sedona), linked from reel-maintenance and cross-linked among existing Tackle Express reel-feature notes |
| ZGs9kF4HHIM | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / cited as re-cut of K_0AeM4OvuE, no new parameters added, sources list updated |
| ZMrCAG7Cqmg | Tackle Express | tutorial | parameter-skim | done | skipped: 38s freshwater bass blade-bait rip/swing technique off a point in the thermocline zone, out of scope, not SoCal/Baja saltwater |
| ZolfRTcJBk4 | Tackle Express | tutorial | parameter-skim | done | skipped: freshwater lake bass/striper blade-bait technique off points in the thermocline zone, out of scope, not SoCal/Baja saltwater |
| ZrcwcugaEe4 | Tackle Express | tutorial | parameter-skim | done | lures/knife-jigs.md; rigging/pr-knot.md; tackle/jig-rod-rating-selection.md; techniques/knife-jigging.md; techniques/slow-pitch-jigging.md; species/bluefin-tuna.md / gear-breakdown merge (bite ratios, braid-by-jig-weight with dated fight times, reel choice, jig-rating rule, PR-knot surname) into 5 existing notes plus 3 missed re-cut-source annotations for 6SClBs16L2Y added |
| _3f8_JxtDRo | Tackle Express | tutorial | parameter-skim | done | skipped: freshwater suspended-bass Damiki rig / thermocline vertical-jigging technique, out of scope, not SoCal/Baja saltwater |
| _8Bno5mP4QE | Tackle Express | tutorial | parameter-skim | done | skipped: generic talk-to-the-shop-employees advice, no SoCal/Baja-specific or hard-won content to extract |
| _C7TJoGT0nw | Tackle Express | tutorial | parameter-skim | done | locations/cedros-island.md; lures/iron-jigs.md; lures/rapala-husky-magnum.md; lures/soft-plastic-swimbaits.md; tackle/hooks.md; tackle/tackle-express-baja-light-setup-yellowtail-insurance.md; tackle/tackle-express-jig-stick-trolling-outfit.md; tackle/tackle-express-cedros-four-rod-quiver.md; techniques/slow-trolling-bait.md; techniques/surface-iron-color.md / 32-min Cedros gear interview merged into 10 existing notes plus new four-rod-quiver note, cross-referencing shorter clips cut from same interview as non-independent |
| _L6mE8ip5l8 | Tackle Express | tutorial | parameter-skim | done | none / correctly skipped: 37s freshwater trout-jigging clip, near-duplicate re-cut of already-skipped OFEpEeFomp4, no SoCal/Baja saltwater content |
| _QgS6QUcvFs | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: generic 31s reel-fast bass clip, no SoCal/Ned-rig markers, matches freshwater Castaic Lake pattern already ruled out-of-scope for adjacent Tackle Express videos |
| _RfXwHSaG48 | Tackle Express | tutorial | parameter-skim | done | skipped: freshwater largemouth-bass crawfish-jig video (Castaic/Pyramid lakes), out of scope, not SoCal/Baja saltwater |
| _XfScSliRVk | Tackle Express | tutorial | parameter-skim | done | techniques/drop-shot.md: amended Hook option section with number-2 Spin Shot pick and mosquito-hook Palomar alternative, unregistered channel capped at medium confidence |
| _eON-xT2mOE | Tackle Express | tutorial | parameter-skim | done | nothing extractable: duplicate re-cut of already-processed 5fxAN1Ofn8M (merged into species/sand-bass.md); bait/species never named, generic column/weight/thumb-tension params already covered in techniques/knife-jigging.md and techniques/flat-fall-jigging.md |
| _rcxIWhNMSE | Tackle Express | tutorial | parameter-skim | done | techniques/drop-shot.md; lures/bay-bass-plastics.md: added lead-vs-tungsten weight/camouflage tip and re-cut-footage note to drop-shot.md; added C3 Baits sibling-product (ice pick/Joe Boo/teaser) mention to bay-bass-plastics.md |
| aF_16nVNch4 | Tackle Express | tutorial | parameter-skim | done | none: correctly out-of-scope freshwater lake bass/thermocline/Diki-rig content; extraction-log row completed with skip reason matching sibling skip pattern |
| aFsyWOLIM48 | Tackle Express | tutorial | parameter-skim | done | skipped: no extractable content - 15s clip, captions are only [Applause] and a cut-off fragment; also out-of-region (striped bass) |
| aKQqNbgISHY | Tackle Express | tutorial | parameter-skim | done | lures/bay-bass-plastics.md: freshwater reservoir Carolina-rig content out of scope, but added the one saltwater-relevant aside (C3 ice pick on darter head, surf, perch/corbina) |
| aauujAuF1hc | Tackle Express | tutorial | parameter-skim | done | nothing extractable: auto-captions contain no usable speech (only Heat. Heat. and music) despite title suggesting a knot-tying tutorial |
| af7a1tR2B84 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-talica-reel-features.md +4 linked notes: new low-confidence Talica feature-rundown note (S Compact body, Infinity Drive, Hagane body), fixed one ASR-order inversion |
| ajYmUmHdPEI | Tackle Express | tutorial | parameter-skim | done | skipped: pure store-promo/event announcement (toy drive), zero fishing knowledge content |
| akUrZ_OYy4c | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md: added boatside-panic-moment bullet (fight-technique addendum), medium confidence |
| akX66b5WGZA | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md; tackle/tackle-express-bkk-titan-diver-swimbait-hooks.md: three-way jig-head comparison (open hook/brush guard, Neck Breaker swivel, BKK Titan Diver underspin) merged, de-duplicated between the two notes |
| aqZxUmefwcw | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-premade-rock-cod-rig.md (new) + cross-links from rockfish-leader-line.md and dropper-loop.md: P-Line premade rock-cod rig (two-swivel construction) |
| au3EkXJswY8 | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: no transcript evidence this generic reel/line clip is SoCal saltwater inshore content vs freshwater bass tackle chat; channel mixes both |
| auiXY0R9ri8 | Tackle Express | tutorial | parameter-skim | done | none: duplicate of N24NBweNK4o (identical 33s clip), already captured in rigging/wiring-a-surface-iron.md; extraction-log row closed out |
| bB8zs0lXvvo | Tackle Express | tutorial | parameter-skim | done | techniques/knife-jigging.md: merged as third same-interview cut (rod/reel load-sharing mechanism, 2023 date resolution), treated as one source appearance not new repetition |
| bCQLyxKQAok | Tackle Express | tutorial | parameter-skim | done | skipped: content-free transcript, part of channel's freshwater bass blade-bait series, out of KB scope |
| bi2X9ANvDBs | Tackle Express | tutorial | parameter-skim | done | freshwater bass fishing content, entirely out of scope for SoCal/Baja saltwater KB - correctly skipped |
| blG8NnDhQ1c | Tackle Express | tutorial | parameter-skim | done | tackle/rod-blank-and-component-materials.md: added blG8NnDhQ1c as 4th provenance-only re-cut of reel-seat-material claims, no new content |
| bvYMtjbflq8 | Tackle Express | tutorial | parameter-skim | done | no KB destination (out of scope): freshwater largemouth-bass Neco/wacky-worm rig at Castaic Lake; evaluator applied change filling stale extraction-log row |
| cAZRaGB_RRM | Tackle Express | tutorial | parameter-skim | done | techniques/spinning-reel-wind-knots.md: merged loose-slack-under-spool failure mode + finger-tension/rod-tip-raise takeup methods, confidence held at medium |
| cBATKqWkQws | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-vanford-fa-reel.md (new, capped low): MGL rotor + CI4+ 2.5x rigidity claims; linked from gear-classes.md and cross-linked with CI4+ note; evaluator ran link-maintenance |
| cNfPlAZWLB8 | Tackle Express | tutorial | parameter-skim | done | no KB destination (out of scope): freshwater trout tackle, braid-to-leader knot avoidance via straight mono/fluoro; evaluator filled stale log row |
| cSTfQy8eb44 | Tackle Express | tutorial | parameter-skim | done | no KB destination (out of scope): freshwater bass blade-bait tight-line-on-fall tip, matches sibling blade-bait series already skipped; evaluator filled stale log row |
| cZ3KlPWiPWw | Tackle Express | tutorial | parameter-skim | done | no KB destination: generic feather-descent/vertical-fish tip, no species/region/depth named, duplicates existing doctrine in techniques/rockfish-deep-dropping.md |
| c_60Ms3QSMY | Tackle Express | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md: added hard-bait treble-hook angler-safety section (long hemostats); techniques/inshore-crankbaits.md: cross-linked; evaluator corrected two invented-causal-mechanism bullets |
| c_L2hqBXwYA | Tackle Express | tutorial | parameter-skim | done | no KB destination (out of scope): 72s generic Damiki Axe Blade tackle-shop product pitch, no species/technique/region stated; evaluator filled stale log row |
| c_YgwlJdsSk | Tackle Express | tutorial | parameter-skim | done | no KB destination: 34s freshwater ultra-light trout-rod (1-4lb) sizing tip, no SoCal/Baja content; evaluator filled stale log row |
| d0fxBYmAnIk | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-penn-vs-avet-lever-drag.md (new): Penn vs Avet Raptor Series comparison (knurl, strike-to-full button, drag curve/preset); linked from star-drag-vs-lever-drag.md |
| d31ID9JHgns | Tackle Express | tutorial | parameter-skim | done | no KB destination: 59s teaser clip, verbatim re-cut of already-extracted EuYOlsnxXko fall-beach-halibut segment (species/california-halibut.md); evaluator filled stale log row |
| d93vB_EBu30 | Tackle Express | tutorial | parameter-skim | done | bait/fishing-live-bait.md: added squid-tank grip (keep eyes covered); techniques/dropper-loop.md: corroborated 3-pass/flip Owner Octy-twist squid-tail rigging; evaluator fixed missing sources front-matter |
| dBAk9NScxSc | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-night-bluefin-tg-jig-rig.md: added as 6th provenance-only re-cut of Jerry-rig night/day/foamer TG-jig cycle, no new params; evaluator fixed invented causal claim + misquote |
| dDvNAZpmx-8 | Tackle Express | tutorial | parameter-skim | done | rigging/leadhead-mods.md: added split-ring nose-reinforcement hack for tube-style halibut soft plastics (#2 split ring, hot sauce/Smelly Jelly lube) |
| dFRpcvkLmb0 | Tackle Express | tutorial | parameter-skim | done | tackle/drag-setting.md: added dFRpcvkLmb0 as re-cut citation of DfLcSS-J3g4's weakest-link/80lb-braid-40lb-leader-15-40rod worked example, no new content |
| dKSnFf5IsmY | Tackle Express | tutorial | parameter-skim | done | no KB destination: freshwater bass topwater-lure comparison (Sammy/Gunfish/Zara-Spook-class), reservoir largemouth bass, out of scope |
| dNn8U9LbL8c | Tackle Express | tutorial | parameter-skim | done | techniques/inshore-crankbaits.md: added treble-hook absorption-during-fight rationale + rod-tip/mono-stretch bait-action bullet; evaluator reworded causal framing |
| dTJihVPudgQ | Tackle Express | tutorial | parameter-skim | done | no KB destination: 8-second clip, no substantive content |
| dWqD8l3jW6w | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md: merged surf halibut hook-set mechanic (reel down to tight before swinging, single-hook thump); evaluator trimmed invented causal rationale |
| degWvtQ4D_Y | Tackle Express | tutorial | parameter-skim | done | tackle/rod-length-for-angler-size.md: merged fatigue/shaking-as-length-signal doctrine, fixed one dropped-hedge misquote |
| dfv6S7RQ_bs | Tackle Express | tutorial | parameter-skim | done | tackle/all-purpose-rod-line-rating.md: provenance-only merge, re-cut of DfLcSS-J3g4, no new note |
| dnHev1PcLts | Tackle Express | tutorial | parameter-skim | done | none: nothing extractable, promotional product video (Stick Jacket Pro Series rod covers), no SoCal/Baja fishing knowledge |
| dpz4M1IEYQg | Tackle Express | tutorial | parameter-skim | done | none: 15s auto-caption clip with no extractable parameter/doctrine content, correctly skipped |
| dt3FXL-HjVo | Tackle Express | tutorial | parameter-skim | done | none: 33s pure promotional event-announcement, no fishing content, correctly skipped |
| dvmyKsk5BCo | Tackle Express | tutorial | parameter-skim | done | none: 40s promotional/personal-reflection clip, no fishing knowledge |
| eLwier3zVdo | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md: merged rod-length leverage/rail-hauling reasoning as third citation corroborating existing 7-7'6" range |
| eMAM6cjzANI | Tackle Express | tutorial | parameter-skim | done | none: 72s auto-generated reaction clip, no extractable doctrine, correctly skipped |
| eOLoHxoqk6E | Tackle Express | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md; lures/lucky-craft-flash-minnow.md; rigging/leadhead-mods.md; species/california-halibut.md; techniques/inshore-crankbaits.md: halibut surf-lure parameter-skim across 5 notes, fixed one non-standard gear-class label |
| ejkr3z7xkJA | Tackle Express | tutorial | parameter-skim | done | techniques/two-speed-low-gear-fight.md: merged Penn/Avet shift-mechanism + high/low timing citations, fixed missing paragraph break |
| enDs3G5bpDc | Tackle Express | tutorial | parameter-skim | done | none: freshwater bass craw rig, no SoCal/Baja content, correctly skipped |
| epuNd10icxQ | Tackle Express | tutorial | parameter-skim | done | none: airline travel/boarding-order tip for rod bundles, no fishing content, correctly skipped |
| eqRMpfcuM2s | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-bait-tank-time-saver.md; techniques/wind-in-your-face-positioning.md: re-cut of S9sQ8Vg8-5o merged as corroborating citations, fixed overconfident ASR product-name assertion |
| eqeESarhRrE | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md: re-cut citation confirming Speedmaster 20/25 round-knob issue and all-sizes Fathom T-bar claim |
| f0gBoLc7scw | Tackle Express | tutorial | parameter-skim | done | none: verbatim re-cut/subset of YyW4-8FRjn8, generic Shimano marketing content, no new claims |
| f1pZI-bfMz4 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md: added OEM Shimano T-bar handle subsection, low confidence (promotional) |
| f22V2HCv8tI | Tackle Express | tutorial | parameter-skim | done | rigging/flying-fish-harness.md: added California Delta Flyer 350 product-feature listing, low confidence (sponsored) |
| f9JOpLrYBiE | Tackle Express | tutorial | parameter-skim | done | lures/dtx-minnow.md: HD-version hardware diffs (harness, sizes, ring, hooks), low confidence (sponsored) |
| fATd3sje6R4 | Tackle Express | tutorial | parameter-skim | done | none: 15s clip, caption content is just 'oh', nothing extractable |
| fHMwcm1xRQk | Tackle Express | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md; species/california-halibut.md; techniques/drop-shot.md; techniques/inshore-crankbaits.md; tackle/tackle-express-surf-halibut-rod-lineup.md (new): shore grabber+float landing, surf-rod summary, beach leader-length rationale, hookset mechanic, new light/heavy surf-rod tackle note |
| fPxqoEforhA | Tackle Express | tutorial | parameter-skim | done | lures/tuna-poppers-and-stickbaits.md; locations/cedros-island.md / merged SP Minnow 115 floating/sinking parameter into stickbait note; corrected extractor's treatment of this clip as an independent source - it's a re-cut of the same Cedros trip already logged in cedros-island.md under _C7TJoGT0nw/9kGpcEHqIUc, now cross-linked both ways |
| fVtiwvqhzgI | Tackle Express | tutorial | parameter-skim | done | none / promotional Tackle Express product ad for Jackall Binksy topwater lure - no species, location, or SoCal/Baja-specific technique detail; correctly skipped |
| fnaGBGbrhqU | Tackle Express | tutorial | parameter-skim | done | locations/cedros-island.md / merged trigger (seabirds + wide-open bite) and bait shape (three-piece hard bait) into the existing triple-trout citation, hedged against the unconfirmed same-trip assumption |
| foLSQJ5oRWI | Tackle Express | tutorial | parameter-skim | done | rigging/pr-knot.md / Third re-cut of the Cesar Chang FG-vs-PR-knot interview appended as a dated correction block to the existing pr-knot note; confidence held at medium, sources array updated, no new note created |
| g5yDzjORhho | Tackle Express | tutorial | parameter-skim | done | rigging/leadhead-mods.md; lures/soft-plastic-swimbaits.md / Added War Baits Slayer/Pickle Kick open-hook rigging steps (exit-point marking, insertion, finish, straight-track/bite-rate reason) and cross-linked a named-example pointer |
| gFx8BXU2vkY | Tackle Express | tutorial | parameter-skim | done | lures/knife-jigs.md / merged single-clip stated-mechanism rationale (more fall action draws bigger, lazier fish) into knife-jigs.md's existing fall-behavior discussion, capped at medium confidence |
| gQ-SwPzmJWM | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater/Damiki-rig suspended-bass tail-spin-bait product talk, no SoCal/Baja species/location/technique named |
| gdACAKN8T7A | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater lake-bass weed-vs-bite identification tip, no SoCal/Baja saltwater species/technique/location named |
| gg1W2lLwm34 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: entire video is Northern California (Clear Lake) freshwater largemouth-bass fishing with freshwater techniques - no SoCal/Baja saltwater species, region, or technique overlap |
| ghHQe3fP9U4 | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md / amended california-halibut router with two-populations/depth-window, spawning-nest conservation practice, spot-fidelity/bait-indicator, and gillnet-corridor entries; fixed one invented-reason and one smoothed-number defect |
| gn2yquuU6eM | Tackle Express | tutorial | parameter-skim | done | tackle/line-and-leader.md; tackle/spooling-line-tension-and-twist.md / two small parameter-skim additions (Japan-made fluoro brand preference, leader-material-on-reel spooling caution), both merged into existing notes with correct cross-links |
| h311A3s-dkY | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md / merged bait-durability framing (mackerel=bigger/no damage risk, anchovy=smaller/lighter to avoid damage) into existing bait-sets-hook-size section, medium confidence |
| h3ZM-mnSNJ8 | Tackle Express | tutorial | parameter-skim | done | none / skipped: transcript is a 28-second teaser with no extractable parameter content (video cuts off before any comparison is made) |
| hAryw1v3I68 | Tackle Express | tutorial | parameter-skim | done | techniques/surface-iron-casting.md / added pros' reasons for low-profile baitcaster over conventional (level-wind removes line management; external brake/tensioner dials in on the water when switching lure weight), medium confidence |
| hBAxFcjts5A | Tackle Express | tutorial | parameter-skim | done | none / skipped: out-of-region/off-topic promo - freshwater bass tackle announcement, no SoCal/Baja saltwater content |
| hJjNZf-JYSs | Tackle Express | tutorial | parameter-skim | done | none / near-duplicate re-upload of Wk4wKFLbWEQ, content already captured in tackle/tackle-express-saltiga-300-round-jigging-reel.md; correctly no edit made |
| hMLwRt6Sxn8 | Tackle Express | tutorial | parameter-skim | done | tackle/line-and-leader.md / merged the braid break-in/wax-coating parameter-skim into the existing braid section, cross-referenced against existing leader/abrasion doctrine |
| hSJL9KhKngA | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: generic chatterbait line-class chatter, no SoCal/Baja/species markers on camera, matches prior same-channel out-of-scope rejection (VotK9jwqRJ8) |
| hXcgczEYcKE | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md / confirmed word-for-word re-cut of S9sQ8Vg8-5o's sinker-sizing-by-depth passage, added as duplicate-footage provenance note; fixed a mislabeled recut-count and false claim-pairing |
| hc8n16HQO_E | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 15s short is pure background dialogue (no species/technique/parameter content spoken); title's striper/topwater claim unconfirmed on camera |
| hjZ3hgq0Bzg | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md; species/california-halibut.md; species/white-seabass.md; techniques/leadhead-swimbait-retrieve.md; techniques/swimbaits.md — tackle/rig/retrieve-mechanics extraction merged into existing fluke-lure notes, with two faithfulness fixes applied |
| hkUH9vkt68Q | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: 94s celebratory first-catch clip, no technique/parameter/decision content |
| hmz8n_9MzZA | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable (evaluator apply-with-changes): 36s clip, no species qualifier beyond bare 'bass', no SoCal/Baja/saltwater marker, matches channel's freshwater-bass pattern |
| hokc5FLmSjA | Tackle Express | tutorial | parameter-skim | skipped | skipped: evaluator-reject: Deps Spiral Minnow is very likely a freshwater bass wake-bait (same-day companion to confirmed-freshwater Deps Buzzjet, same channel/presenter); no SoCal/Baja content in transcript |
| i4rJy9Uwb-U | Tackle Express | tutorial | parameter-skim | done | tackle/spooling-line-tension-and-twist.md — merged as second (likely re-cut) source into existing tension/braid/baitcaster bullets, confidence held at medium |
| i6G6vX0tKn4 | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: 14s clip is on-the-water chatter only, no gear/parameter content despite title |
| iBdz2SfeA1g | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-fast-tip-for-finicky-bite-drag-drift.md; tackle/rod-and-reel-selection.md; tackle/rod-action-testing-technique.md; tackle/README.md — new parameter-skim tackle note on why a fast tip matters for drag/drift bite detection, linked from rod-and-reel-selection.md |
| iHwvUl0dhxk | Tackle Express | tutorial | parameter-skim | done | locations/cedros-island.md — added take-home catch-handling excerpt (bins, cutting station, vacuum-seal) and revised ambiguous trip catch-weight figure with corrected sourcing rationale |
| iQjTILHaxqo | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: generic Baja resort catch-packing/vacuum-seal/freeze logistics, no technique/species/gear/care doctrine |
| ijNOphK4XRA | Tackle Express | tutorial | parameter-skim | done | species/california-halibut.md — re-cut Short of eOLoHxoqk6E logged as duplicate footage/provenance; evaluator corrected an over-claim about theory-sentence coverage |
| ijjtpoKZp8U | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: 20s clip, captions are only [Music]/you, no substantive content |
| j0btC9J0Wcc | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: freshwater bass content (Castaic Lake, C3 Baits), out of SoCal/Baja saltwater scope entirely |
| jFlAdWRj3HI | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-penn-pull-to-turn-preset-drag.md; tackle/drag-setting.md; tackle/tackle-express-penn-vs-avet-lever-drag.md — new note on Penn's pull-to-turn preset-drag philosophy, cross-linked from two parents |
| jWPv-OOM3uk | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md — added booty-spin blade's stated flash/vibration rationale + 3/5/7-in sizing; rigging-demo content correctly withheld as re-cut of four already-logged sibling clips |
| j_x1IskkSEE | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: 48s generic tackle/line product plug (Sunline Almighty braid for wacky rig), no SoCal-specific content, fails curation bar |
| jeJAsY_M0oc | Tackle Express | tutorial | parameter-skim | done | tackle/line-and-leader.md — appended diameter-equivalence example (8lb braid ≈ 1lb test) + stated leader-requirement reason to existing bullet list, medium confidence |
| jo8lMdFZ1bk | Tackle Express | tutorial | parameter-skim | done | techniques/panga-team-trolling.md; species/yellowtail.md — new technique note (3-angler panga follow-up-cast on troll hookup) + router row, cross-linked to Colt Sniper lure entry |
| k0rhryq2kYI | Tackle Express | tutorial | parameter-skim | done | none — nothing extractable: 38s clip, captions have no substantive speech (stray fragment, [music], single letter), no gear content despite title |
| k23JzE3Fr-I | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-fish-kicker-quick-clip-surf-bait.md; tackle/README.md; tackle/line-and-leader.md; tackle/tackle-express-surf-halibut-rod-lineup.md — new tackle note for Fish Kicker 25 lb quick clips, linked from two siblings |
| kHUQd9jqG-A | Tackle Express | tutorial | parameter-skim | done | rigging/hollow-splice-and-serving.md; tackle/reel-maintenance.md — parameter-skim addition (low-confidence promotional tip on braid cutters for trimming splice tag ends), cross-linked |
| kR-t-z1PPCE | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: auto-generated captions contain no substantive speech (only [music] tags and a repeated Heat fragment), despite the title implying fluorocarbon/tuna content |
| k_ocIsSD6vQ | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 31s freshwater largemouth-bass ice pick soft-plastic color tip, out of SoCal/Baja saltwater scope, fails curation bar |
| klb0VSg_I3w | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / War Baits A-Rig (bladed vs non-bladed) merged into jig-head-selection subsection |
| kt3G72gUldM | Tackle Express | tutorial | parameter-skim | done | lures/tuna-poppers-and-stickbaits.md / single-hook Current Sniper conversion (BKK Lone Sniper 3/0/2/0, barbless) added as conflicting rigging choice beside existing stock-treble guidance |
| kuIKWNZ3Koo | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass PB rats wake-bait plug, no SoCal/Baja saltwater content - nothing extractable |
| lNXZD79BvJY | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 45s generic hype clip on tungsten jigs for nighttime jumbo bluefin, no parameters given, topic already covered elsewhere |
| lYnD_MiALL8 | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md / added missing sources-array entry for already-cited re-cut of S9sQ8Vg8-5o; no new doctrine |
| l_L0PdOOWGs | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 46s personal career-change narrative, no fishing knowledge content |
| m6NxHaIifj8 | Tackle Express | tutorial | parameter-skim | done | rigging/tony-pena-knot.md / added as provenance/duplicate-footage note to existing entry, confidence unchanged at medium |
| mDRSoMYxDuY | Tackle Express | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md / logged as re-cut/duplicate of eOLoHxoqk6E footage, no new doctrine |
| mMa0oqI2tqA | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass free rig tying tutorial, out of SoCal/Baja saltwater scope entirely |
| mgUjxUoGkZU | Tackle Express | tutorial | parameter-skim | done | tackle/line-and-leader.md / companion-clip extending braid-by-jig-weight ladder to 350g+ to 80lb, same interview session as Rtwz0oEfrKw |
| mgsCmVxM8dM | Tackle Express | tutorial | parameter-skim | done | none / freshwater bass tackle showcase at Castaic Lake, out of SoCal/Baja saltwater scope entirely |
| nF6MosH63HY | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 27s clip, captions contain only [Music] and a stray fragment, no substantive speech |
| nJPQVouJQ0g | Tackle Express | tutorial | parameter-skim | done | techniques/dropper-loop.md / confirmed re-cut of S9sQ8Vg8-5o re-drop/contour passage, added as duplicate-footage provenance note |
| nORwiYXBQmQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / re-cut of K_0AeM4OvuE shift-mechanism demo, provenance note only, confidence unchanged |
| nRIAgz5G_Bc | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md; techniques/dropper-loop.md; techniques/sliding-sinker.md; rigging/leadhead-mods.md; lures/soft-plastic-swimbaits.md / Channel Islands WSB parameter-skim + provenance fix identifying nRIAgz5G_Bc as source of PnAnAS6QoG8/V4opuMirbDU re-cuts |
| nZfEB7466ys | Tackle Express | tutorial | parameter-skim | done | techniques/drop-shot.md / confirmed re-cut of _rcxIWhNMSE cylinder-weight/lead-vs-tungsten segment, provenance note only |
| nizu9cpPXUs | Tackle Express | tutorial | parameter-skim | done | none / skipped: generic packing/logistics content only, no SoCal/Baja fishing knowledge |
| nlrSBi_hrrg | Tackle Express | tutorial | parameter-skim | done | techniques/spinning-reel-wind-knots.md / third re-cut citation, payoff framing for 8-carrier braid, confidence held at medium |
| nnQFIho8sa0 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 36s reaction clip, no gaff/technique/parameter content despite title |
| ntS17IEKyJ0 | Tackle Express | tutorial | parameter-skim | done | techniques/spinning-reel-wind-knots.md / added Recovery section for freeing a loop that already formed while winding, medium confidence |
| nwjIEWJyjKU | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md / added shallow vs deep sinker-weight bracket (60-100ft/6-10oz, 600-700ft/16oz+), cross-linked dropper-loop.md |
| nwmIqR2VgfI | Tackle Express | tutorial | parameter-skim | done | tackle/rod-action-testing-technique.md / merged hip-pull rod-test safety rationale (no risk of breaking rod) into existing note |
| o5TR7y6-q6A | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 61s promo anecdote, no SoCal/Baja parameters, only location (Morro Bay) is out of region |
| o7Kd0aNAijQ | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: generic packing/clothing/luggage logistics, no fishing knowledge, out of scope per curation bar |
| oGCAX8dgR5o | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 17s clip is ambient dialogue fragments, no fishing knowledge despite title |
| okJCANlWWE4 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: out-of-scope freshwater bass-tackle Senko vs Neko worm comparison, no SoCal/Baja saltwater content |
| osAuU0W9zKA | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater Largemouth/striper/Muskie swimbait product review, no SoCal/Baja saltwater content |
| ov0T5MPdl_E | Tackle Express | tutorial | parameter-skim | done | tackle/spooling-line-tension-and-twist.md; tackle/searcher-lever-drag-reel-sizing.md / added overspooling/line-capacity rule of thumb (300-500yd offshore, 100-150yd bass) |
| p-gl7mLOeWw | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 34s clip restates halibut fighting doctrine already captured from 1l05hEXDaWw, no new parameter |
| p1KyyR0i7Kc | Tackle Express | tutorial | parameter-skim | done | rigging/rp-knot.md (new); rigging/essential-knots.md / split RP-knot detail into new dedicated note (wrap-by-line-ratio rule, lubrication/cinch/trim, track record), essential-knots.md keeps routing summary |
| p9YYIb4GKHM | Tackle Express | tutorial | parameter-skim | done | lures/iron-jigs.md; techniques/rockfish-deep-dropping.md / merged Lift & Drop technique name into rockfish jig-cadence doctrine; strengthened Ahi/AI's jig brand ASR note |
| pL7ZGuMVwo4 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-talica-reel-features.md / merged Core Protect water-resistant coating claim into Talica feature note, dropped unsupported corrosion-protection framing |
| pMsbeLOgUc4 | Tackle Express | tutorial | parameter-skim | done | techniques/leadhead-swimbait-retrieve.md / added as re-cut/duplicate of OURS05qEGcA to source attribution, no new content |
| pOFsjDTqaxY | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md (new); species/yellowtail.md; tackle/rod-and-reel-selection.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / new note: 7:1 baitcaster torque/versatility for big yellowtail, flagged conflict vs Dan Wade's 6.5-7.5:1-too-fast doctrine |
| pTenOTaHdUc | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 17s clip is only interjections, no fishing knowledge content |
| pa0MS0GK_2o | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: freshwater trout/bluegill/crappie ultralight reel sizing content, out of SoCal/Baja saltwater scope |
| ptwN9MUDxjk | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 18s on-the-water clip, fragmentary content only, no technique/gear/species detail |
| q0it3pyUW6Q | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-ci4-plus-reel-features.md; tackle/tackle-express-shimano-vanford-fa-reel.md; tackle/gear-classes.md / resolved reel identity (Shimano Vanford) across cBATKqWkQws/q0it3pyUW6Q/TjQuU-x8sHM via verified verbatim overlap, merged fuller Infinity Drive claim |
| qHS-ewTQs9Q | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md: re-cut/duplicate of _C7TJoGT0nw Cedros mackerel Owner-hook content; added as corroborating citation, ASR hook-size variance flagged not reconciled |
| qKOmJH_WtJo | Tackle Express | tutorial | parameter-skim | done | none: 33s reaction/landing clip, no rod/line/technique parameters or decision content - nothing extractable |
| qLDrhgE7-y0 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-tranx-300b-braking-system.md; tackle/rod-and-reel-selection.md: new product-mechanism note for Tranx 300B SVS Infinity braking system, capped low (promo, unregistered channel) |
| qLKLlZdiflA | Tackle Express | tutorial | parameter-skim | done | lures/tuna-poppers-and-stickbaits.md; rigging/rubber-band-deep-rig.md; techniques/flat-fall-jigging.md; techniques/knife-jigging.md; techniques/leadhead-swimbait-retrieve.md: five parameter-skim additions (popper size, sinker-rig failure mode, calm/windy jig-weight split, seasonal jig progression, seabass slow-retrieve conflict); fixed one fabricated location detail |
| qRrZakwbLoM | Tackle Express | tutorial | parameter-skim | done | none: clothing/apparel promotional content, out of scope per curation bar |
| q_NMbHJ7QoQ | Tackle Express | tutorial | parameter-skim | done | none: freshwater lake bass-fishing tackle video, no SoCal/Baja saltwater content, out of scope |
| qh3hL2Dt3HY | Tackle Express | tutorial | parameter-skim | done | tackle/all-purpose-rod-line-rating.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; tackle/tackle-express-premade-rock-cod-rig.md; techniques/flyline.md; techniques/rockfish-deep-dropping.md: original source for 5 already-cited re-cut shorts; merged reel/rod combo, weighted-flyline trigger, conventional-vs-spinning mechanism, sinker-by-depth figures |
| r7Bv49Ysgdw | Tackle Express | tutorial | parameter-skim | done | lures/iron-jigs.md; techniques/knife-jigging.md: treble-fouling tight-line-on-the-drop fact merged into iron-jigs.md, cross-linked to knife-jigging.md's opposite tightlining-drop failure to disambiguate rig types |
| rBt096uru3U | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-phenix-axis-rockfish-rod.md; tackle/rod-length-for-angler-size.md; techniques/rockfish-deep-dropping.md: new Phenix Axis rockfish rod note (7'8 heavy, 25-60lb), cross-linked as side-by-side product example |
| rd2Ia8HRbSg | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md; lures/soft-plastic-swimbaits.md: re-cut of already-logged 9kGpcEHqIUc/_C7TJoGT0nw Cedros interview, added as provenance-only citations, no new doctrine |
| reG4Xc91Mj4 | Tackle Express | tutorial | parameter-skim | done | none: transcript is song lyrics only, no fishing content, nothing extractable |
| reZBk4GsH_o | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md: added wide-gap-vs-long-shank hook + O-ring rigging bullet to existing O-ring cluster |
| rlZVbEO3WyQ | Tackle Express | tutorial | parameter-skim | done | none: freshwater trout ultralight rod tackle, out of scope for SoCal/Baja saltwater KB |
| rvmr9Jy9RjI | Tackle Express | tutorial | parameter-skim | done | rigging/san-diego-jam-knot.md: near-duplicate re-cut of already-logged 6E39_PBt1P4, added as provenance-only citation, no new doctrine |
| rxoaPT5Zaog | Tackle Express | tutorial | parameter-skim | done | techniques/two-speed-low-gear-fight.md: merged self-reported two-speed-vs-single-speed fight-time comparison (180lb/6min vs 140lb/15min) into existing section |
| s2yqtaHriqU | Tackle Express | tutorial | parameter-skim | done | none: freshwater trout/bass/striper lure pitch, no SoCal/Baja saltwater content |
| s3hJuucTqUI | Tackle Express | tutorial | parameter-skim | done | none: out-of-scope freshwater product plug for stocked-lake striper swimbait, nothing extractable |
| s7GMKI6c6RU | Tackle Express | tutorial | parameter-skim | done | none: 8-second promo clip, no extractable fishing knowledge |
| sGnY4QxqMmI | Tackle Express | tutorial | parameter-skim | done | lures/knife-jigs.md: merged Mustad Rip Roller vs Nomad Streaker shape comparison, re-cut of ZrcwcugaEe4/5XWnm7ok09k interview, medium confidence |
| sJGs-Jqt9Vo | Tackle Express | tutorial | parameter-skim | done | conditions/current-diagnostics.md: attributed alternate scoped-out-line fix (flick up-swell vs wind-it-in) added side by side in Line scope section |
| sPgP0aBUQm8 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-how-co-split-ring-pliers.md; tackle/tackle-express-maxima-shark-tooth-leader-tool.md; tackle/spooling-line-tension-and-twist.md; tackle/tackle-express-mustad-heavy-duty-pliers.md / two new low-confidence tackle notes (split-ring pliers, leader-spool band/cutter) cross-linked; four freshwater/bass-technique products correctly skipped as out-of-scope |
| sPs3Civek1w | Tackle Express | tutorial | parameter-skim | done | lures/bay-bass-plastics.md / word-for-word re-cut of already-extracted BPxE3xn3gAc closing segment (Basstrix Flash Trick halibut colors); added as provenance-only source, no new doctrine |
| sSH80AImFX4 | Tackle Express | tutorial | parameter-skim | done | none / nothing extractable: 24-second vlog clip with no stated fishing parameters, technique detail, or decision rationale |
| sj_9QYlGtGo | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / re-cut of existing Fathom build-features bullet list, added as third citation, no new parameter, confidence unchanged at medium |
| sl2MRqpiS60 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-talica-reel-features.md / added as third citation to existing Hagane-body/S-Compact bullet, treated as re-cut not independent confirmation, confidence low |
| smdXDSyuVnY | Tackle Express | tutorial | parameter-skim | done | none / 79s promotional product spotlight for the submission death blade jig, no SoCal/Baja-specific decision logic or region content, fails curation bar |
| t0kkwlrNwHk | Tackle Express | tutorial | parameter-skim | done | techniques/knife-jigging.md / added Ceasar Chang's reasoning for multi-color meter-mark braid over 100ft marks when jigging for tuna (no bottom reference, relocate bite zone by meter color); 100ft fine with depth reference and little current |
| t3kDnoGYfVs | Tackle Express | tutorial | parameter-skim | done | none / generic Palomar mechanic already covered by rigging/essential-knots.md; only new content is a shop line-cutter product plug, fails curation bar |
| t96ZBu0gvq4 | Tackle Express | tutorial | parameter-skim | done | none / 29s on-the-water reaction clip with no fishing knowledge content (no species/technique/gear/parameter in transcript) |
| tRvItFsxjmg | Tackle Express | tutorial | parameter-skim | done | tackle/rod-action-testing-technique.md / folded 32s recap clip into existing rod-testing note as another re-cut/non-independent confirmation, medium confidence retained; fixed an incorrect ordinal claim |
| tVgGBpzozMU | Tackle Express | tutorial | parameter-skim | done | none / 27-second promo teaser, no extractable parameters (no species/bait size/technique stated) |
| tugP0UsrzRI | Tackle Express | tutorial | parameter-skim | done | techniques/glide-baits.md / added asymmetric-weight (3-6oz bottom / 1-3oz top) three-way-swivel dancing hookup-bait rig variant for rockfish, contrasted against existing matched-weight guidance, medium confidence |
| u9sJyZhaDGQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-daiwa-coastal-tw200-reel.md; tackle/rod-and-reel-selection.md; tackle/tackle-express-saltiga-300-round-jigging-reel.md / new low-confidence promotional product note (Daiwa Coastal TW 200) cross-linked from inshore-baitcast rod/reel section and Saltiga 300 Hyper-naming-family note |
| ugML6PvRyc8 | Tackle Express | tutorial | parameter-skim | done | tackle/drag-setting.md / third Tackle Express re-cut of the weakest-link/15-40-rod worked example, confidence held at medium, adds in-range 12lb figure |
| ulWK3kaVQ5k | Tackle Express | tutorial | parameter-skim | done | lures/bay-bass-plastics.md / added Keitech Shad Impact pin-tail build/durability/scent notes and Owner-vs-Core-Tackle jig-head hover-strolling rigging; asr-uncertain caveat added to Owner head name |
| v5XtBi3wtVM | Tackle Express | tutorial | parameter-skim | done | none / out-of-region/off-topic (freshwater bass crankbait clip, no SoCal/Baja saltwater content) |
| v6X2s1lb1aE | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-sedona-reel-features.md; tackle/tackle-express-shimano-nasci-fc-reel.md / new low-confidence Sedona feature-rundown note (Hagane gear, G-Free Body, Silent Drive), cross-linked with sibling Nasci FC note |
| vALAeUaBmRM | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-speedmaster-fathom-reel-sizing.md / added Fathom 25/40 drag/capacity/weight figures as corroborating re-cut; corrected unsupported Speedmaster-10 identity inference for unnamed third reel |
| valIU8lsMX4 | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-savage-gear-line-thru-swimbait-rigging.md / evaluator created missing note for mono-loop pull-through rigging technique (threading mainline through hollow-body line-thru swimbait), linked from glide-baits.md, line-and-leader.md, gear-classes.md |
| vk3jbsINcPw | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-tranx-300b-x-protect-water-resistance.md; tackle/reel-maintenance.md; tackle/tackle-express-shimano-nasci-fc-reel.md; tackle/tackle-express-shimano-tranx-300b-braking-system.md / new low-confidence Tranx 300B X-Protect coating note, cross-linked to sibling Tranx/Nasci notes |
| w5iryVkSe-0 | Tackle Express | tutorial | parameter-skim | done | techniques/spinning-reel-wind-knots.md: added construction-side wind-knot cause (carrier count + breaking strength) at medium confidence |
| wk8bkqzdyM0 | Tackle Express | tutorial | parameter-skim | done | rigging/pr-knot.md: fourth re-cut of same interview, appended as duplicate-provenance paragraph |
| wl27BWAWpq0 | Tackle Express | tutorial | parameter-skim | done | tackle/hooks.md; techniques/dropper-loop.md: verbatim re-cut of nRIAgz5G_Bc, logged as re-cut provenance, no new claims |
| x2cQrPaZ_Z0 | Tackle Express | tutorial | parameter-skim | escalated | escalated: guard: protected path touched: profiles/cameron/rods.md |
| x5EkH9Vkdrk | Tackle Express | tutorial | parameter-skim | done | none: 28s music-only clip, no spoken fishing content despite title |
| x7LGWOehuw0 | Tackle Express | tutorial | parameter-skim | done | none: freshwater largemouth bass fishing, out of SoCal/Baja saltwater scope |
| xFW2002SaQk | Tackle Express | tutorial | parameter-skim | done | lures/bay-bass-plastics.md; techniques/wacky-rig.md: new wacky-rig technique note (bite detection), medium confidence |
| xL1sMpmWcnk | Tackle Express | tutorial | parameter-skim | done | tackle/drag-setting.md; tackle/tackle-express-penn-pull-to-turn-preset-drag.md: corroborated free-spool-only rule, added Penn Fathom roll-vs-pull-to-turn contrast, fixed invented stopper distinction |
| x_3ohQ_D-f8 | Tackle Express | tutorial | parameter-skim | done | none: freshwater largemouth bass content (crankbait rod vs worm rod, blade bait), out of SoCal/Baja saltwater scope |
| xfPcA1VRgsw | Tackle Express | tutorial | parameter-skim | done | none: generic freshwater-bass tackle-care/line-inspection content, no SoCal/Baja-specific material |
| xgPEt4Zj35Q | Tackle Express | tutorial | parameter-skim | done | fish-care/dehooking-and-release.md; lures/iron-jigs.md: added sport-boat single-hook swap for deck safety, medium confidence, fixed hook-attribution inversion |
| y3MaZYZvyUg | Tackle Express | tutorial | parameter-skim | done | none: freshwater minnow-style Diki rig content, out of SoCal/Baja saltwater scope |
| y9YlqMQh3BI | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-cedros-four-rod-quiver.md; tackle/tackle-express-jig-stick-trolling-outfit.md: re-cut duplicate footage, added as attributed re-cut confirmation, confidence held medium |
| yEsbyq3WjWE | Tackle Express | tutorial | parameter-skim | done | bait/fishing-live-bait.md: corroborating bullet added to red=cull bait-selection doctrine, medium confidence |
| yTPtYL9QAsw | Tackle Express | tutorial | parameter-skim | done | techniques/leadhead-swimbait-retrieve.md; techniques/inshore-crankbaits.md: added pier/boat-inshore wind-to-tight-line hookset rule, cross-referenced trimmed re-cut of fHMwcm1xRQk |
| yVYUY3PlvIw | Tackle Express | tutorial | parameter-skim | done | none: generic gear-storage product review (Avet reel bag), fails curation bar |
| yf7dEnzsNzQ | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-shimano-tranx-300b-body-gearing-and-model-lineup.md: new note, Hagane body/gearing/spec ladder, low confidence |
| yl-AkO5S64o | Tackle Express | tutorial | parameter-skim | done | techniques/inshore-crankbaits.md; techniques/leadhead-swimbait-retrieve.md: third re-cut citation, no new doctrine, confidence held medium |
| ywKI8gBK6vM | Tackle Express | tutorial | parameter-skim | done | none: freshwater bass crankbait/riprap-bank combo talk, out of SoCal/Baja scope |
| z1CS3To6ATA | Tackle Express | tutorial | parameter-skim | done | none: freshwater bass forward-facing-sonar/blade-bait/Diki-rig teaser, out of SoCal/Baja saltwater scope |
| z5UoW9pntvE | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-penn-vs-avet-lever-drag.md; tackle/star-drag-vs-lever-drag.md; techniques/two-speed-low-gear-fight.md / fuller original of two prior Tackle Express re-cuts (OdRZIDBO6Mg, ejkr3z7xkJA); added Penn Fathom/Avet Raptor bearing, free-spool/cast-control, handle, drag-washer, cost, and color/handedness spec detail plus the Avet's physical shift-to-low/shift-to-high steps |
| zItCqap4RdE | Tackle Express | tutorial | parameter-skim | done | none / lifestyle/personal-narrative video with no SoCal/Baja fishing decision knowledge, technique, tackle, or location content to extract; correctly skipped |
| zLN0v-gWpeI | Tackle Express | tutorial | parameter-skim | done | techniques/rockfish-deep-dropping.md / re-cut of qh3hL2Dt3HY logged as duplicate source, no new claim added |
| zLvKfwSmIIs | Tackle Express | tutorial | parameter-skim | done | none / reaction-shot short with no fishing knowledge content; correctly skipped, closed pending log row |
| zVMY4fZydRQ | Tackle Express | tutorial | parameter-skim | done | techniques/slow-pitch-jigging.md / merged as nested restatement sub-bullet under existing ZrcwcugaEe4 Cesar Chang spinning-vs-level-wind doctrine, medium confidence held, flagged as re-cut/non-independent |
| zVrsCf46_fI | Tackle Express | tutorial | parameter-skim | done | none / 46s freshwater lake striper-boil clip, no SoCal/Baja saltwater content extractable, out of region scope |
| zWpYFTIZP7w | Tackle Express | tutorial | parameter-skim | done | tackle/tackle-express-izorline-xxx-mono.md / merged as second low-confidence data point into existing Izorline XXX note (weight-by-application: 25 lb swimbait, 20 lb rats/crawlers, 2 lb trout/ultralight) |
| zYcXDoOE6jo | Tackle Express | tutorial | parameter-skim | done | lures/soft-plastic-swimbaits.md / near-verbatim earlier-uploaded short of already-logged jWPv-OOM3uk; added provenance-only citation, no independent content extracted |
| zYcsYhdyZrA | Tackle Express | tutorial | parameter-skim | done | tackle/all-purpose-rod-line-rating.md / parameter-skim add: Fathom 25 Narrow/Avet MXJ vs Seagate/Squall reel-capacity clip, cross-linked to existing Fathom-25 spec table |
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

## Batch 3 — tooling fixes during the autonomous run (2026-08-18)

Session-level, no video content. Recorded here so a dead session resumes
knowing why these changed mid-run.

- **guard.py — sweep scoped to the pipeline.** `cmd_sweep` reverted any
  commit touching a PROTECTED path, applied to every commit on the branch
  rather than to the unattended extractor the rule exists to constrain. It
  reverted two already-pushed, already-reviewed session commits (the Bight
  Watch generator; the chain's own correct fix to `commit-video.py`). Both
  reverts undone; the sweep now skips commits whose author is not in
  `PIPELINE_AUTHORS`. Protected-path rules still apply in full to extraction
  commits. The two escalations it raised are annotated as resolved in
  `sources/escalations.md` — no Gate B action.
- **commit-video.py — push target.** `BRANCH` was hardcoded to the finished
  batch-2 branch; it now reads the current branch. An unattended batch-3 run
  would otherwise have pushed extractions onto a merged branch.
- **link-maintenance.py — granularity watch.** Warns (never fails; the chain
  runs it pre-commit) when a note passes 400 lines or a section passes 120.
  Currently 23 notes and 33 sections, worst `species/yellowtail.md` at 1,439
  lines with an 1,183-line `## Where & when` carrying no subheadings. This is
  the Phase 4 split target, and the risk it watches for is a writer editing a
  note too large to hold in view — it cannot find the doctrine it should
  reconcile against. Measured this run: zero near-duplicate passages across
  the four largest notes, and every batch-3 write into yellowtail landed in
  the short router sections at 88-91% of the file, not in the wall.
- **Bight Watch** (`scripts/build-bight-watch.py`) — the review surface, built
  from the KB and the worklist; `sources/bight-watch.html` is generated and
  gitignored. `publish-bight-watch.yml` on `main` rebuilds it hourly for
  GitHub Pages; the build job passes and the deploy job is blocked on the
  repo's Pages setting (Settings -> Pages -> Source: GitHub Actions).

## Batch 3 — corrections queued for after the run (Cameron, 2026-08-18)

Deferred deliberately: Cameron's call is that these land **after** the
autonomous run finishes, not mid-run, so the chain is not editing under a
moving structure. Recorded here so they are not lost.

### C-1 — HookUp Baits are TUBE baits, not glide baits

**Cameron (2026-08-18), correcting the KB:** *"hookup baits are not glide
baits, they are tube baits. Tube baits are a type of soft plastic where the
lead head is inside of the soft plastic. Tube baits are a staple in socal and
definitely deserve their own section."*

This is a misclassification, not a nuance — the whole of
`techniques/glide-baits.md` (456 lines) is built on HookUp Baits seminars
(`5Oh3IPIC5g4` and a second HookUp Baits source), so the note's subject and
its name disagree with the SoCal lexicon.

Scope when it runs:

- **Create `lures/tube-baits.md`** (or `techniques/`, decided at the time) as
  its own note: the class definition Cameron gives — a soft plastic with the
  **lead head inside** the body — plus why it is a SoCal staple. It gets the
  HookUp Baits material that is genuinely about tube baits.
- **Re-home `techniques/glide-baits.md`.** Every HookUp Baits section moves to
  the tube-bait note. Whatever real glide-bait content remains (a glide bait
  is a different lure — jointed hard bait, side-to-side glide) either stays in
  a slimmed note or the note is retired.
- **15 notes link to `glide-baits.md`** and must be repointed:
  `tackle/gear-classes.md`, `techniques/` (surface-iron, swimbaits, yo-yo-iron,
  trolling, README), and the routers `skipjack-tuna`, `dorado`,
  `california-halibut`, `rockfish-lingcod`, `yellowfin-tuna`, `sand-bass`,
  `calico-bass`, `sheephead`, `yellowtail`. Several carry the phrase "glide
  bait" inside `Situations → techniques` rows, so the row text changes too,
  not just the link target.
- **Check the gear-class lexicon** — `tackle/gear-classes.md` needs a tube-bait
  entry, since the class term is what routers resolve against.
- The confidence treatment does not change: HookUp Baits material is
  co-owner-presented product content and stays `low` per the sponsored-claim
  rule.

**Note:** the KB currently has **zero** occurrences of "tube bait" outside
transcripts, so this is a genuine coverage gap as well as a naming error.

### C-2 — Searcher Sportfishing promoted; re-rate sweep owed

**Cameron, 2026-08-19:** *"Searcher should absolutely be promoted as a
source."* Row added to `sources/source-registry.md` the same day as
`searcher-sportfishing`, registered as a **channel/series** (like
`crust-to-coast`) rather than a person, because the channel carries several
named voices — Capt. Art, Steve Carson (Penn), Wendy (Izorline), Doug Kearn,
Logan Watson, other Team Searcher captains — and the instructional value is in
the numbered single-subject Tackle Tip Thursday format. Sponsored-claim caveat
attached, as with `cesar`: mechanism and parameters rate normally, product and
model endorsements stay `low`.

**Applied immediately, not deferred**, because the extractor reads the registry
at write time — every remaining video in the worklist now rates against the
correct standing. This was 74% of the run's chain output (91 of the first 123
completed videos), all previously capped at `medium` for want of this row.

**Owed at the post-run pass — a re-rate sweep of what is already written.**
Promotion removes the *cap*; it does not upgrade anything by itself. The rubric
still says repeated doctrine is `high` and a single mention is `medium`, so
this is a per-note judgment, never a find-and-replace.

Measured at the time of promotion — 54 notes cite a Searcher video, 36 of them
sit at `confidence: medium`:

- **14 cite exactly one Searcher video** — these stay `medium`. A single
  mention from a registered source is still a single mention.
- **22 cite two or more** — candidates for `high`, but only where the *same
  doctrine* repeats across those videos rather than several videos each
  contributing a different claim. Largest: `rigging/essential-knots.md` (10
  Searcher ids), `species/wahoo.md` (6), `techniques/wahoo-bomb-casting.md`
  (6), `tackle/rod-and-reel-selection.md` (5).

Each of the 22 needs reading before its rating moves. Notes that mix Searcher
with other sources also need the mixed-attribution check — a note is not `high`
because one of its several sources is registered.
