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
- **Not a duplicate:** `vqsD0qpwcJA` ("Slow Pitch Jigging // Yellowtail LA Bay
  Baja", 2022-04-06) and `Jtf-bU4aM-c` ("Does SLOW PITCH JIGGING work for
  YELLOWTAIL?!", 2022-06-27) are **distinct** videos (different md5, titles,
  dates, bodies). Both extracted separately; topic overlaps — not `duplicate-of`.

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
episodes), plus one orphaned Stoked "part 3" whose parts 1–2 failed. If
captions can be sourced another way, they can land in a later batch.

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
| unARAuTgF_A | Dirty Hookers | tutorial | deep | escalated | escalated: guard: deleted 38 lines from curated note: rigging/assist-hooks.md |
| EmZO8QiOfik | Dirty Hookers | tutorial | deep | escalated | escalated: guard: protected path touched: sources/source-registry.md |
| M8hOYQ_6rSg | Dirty Hookers | tutorial | deep | done | bait/making-bait.md; lures/iron-jigs.md; lures/knife-jigs.md; lures/spreader-bar.md; rigging/trap-rig.md; tackle/hooks.md; tackle/rod-and-reel-selection.md; techniques/dropper-loop.md; techniques/knif |
| mWxyjDrcdXM | Roman Castro | tutorial | deep | done | techniques/foamer-casting.md / Added Roman Castro's bluefin-popper hookup/drag/fight doctrine (loosen drag on packed foamers, cast to edge to avoid scissoring, patience fighting 100lb+ fish, keep line |
| VpW91AKOFVQ | Roman Castro | tutorial | deep | done | lures/iron-jigs.md; rigging/essential-knots.md; tackle/rod-and-reel-selection.md; techniques/surface-iron.md; techniques/yo-yo-iron.md / Scotty/Brothers Sportfishing surface-iron doctrine merged: assi |
| _ZThckj2TIM | Roman Castro | tutorial | deep | escalated | escalated: guard: protected path touched: sources/source-registry.md |
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
| VUb7a3sP8zQ | Your Saltwater Guide | tutorial | parameter-skim | skipped | skipped: evaluator-reject: generic dehooking technique (gill-opening method) has no compliant destination at parameter-skim depth (router-absorption/no new-note-creation rules); the only calico-specif |
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
| frX09YMQxKE | Your Saltwater Guide | on-the-water | observations-only | pending | Baja (Lopez Mateo/Magdalena Bay mangroves); snook/pargo/grouper catch clip, drone scenery, no doctrine |
| 67qLBEtd3EU | Your Saltwater Guide | on-the-water | skip:duplicate-of-KTsXdQXAnkU | skipped | confirmed: identical dialogue/duration(7:07) to primary calico bass video, same recording |
| vyX5FGoDH0A | Your Saltwater Guide | on-the-water | observations-only | pending | Baja (Lopez Mateo mangroves); snook/grouper/spotted bay bass catch footage, no doctrine |
| dlxA22FVNGc | Your Saltwater Guide | tutorial | deep | pending | Baja (Lopez Mateo mangroves); anchoring, stealth leader/hook choice, tide-phase bite-timing doctrine |
| 5nTGoZ9_nzU | Your Saltwater Guide | non-fishing | skip:no-usable-content | skipped | Entire transcript is garbled nonsensical ASR (song lyrics), no recoverable fishing content |
| Dq1x__MI8Wk | Your Saltwater Guide | non-fishing | skip:not-fishing | skipped | Pure marlin filleting/cooking demo, no catch footage or location |
| BmENEt6gYm8 | Your Saltwater Guide | non-fishing | skip:not-fishing | skipped | Pure wahoo filleting/cooking demo, no catch footage or location |
| ZggReeO1nyU | Your Saltwater Guide | tutorial | deep | pending | Live-bait rigging: nose/butt/gill-hook methods for sardine+anchovy w/ species-specific rationale |
| 7WapaxdtjQg | Your Saltwater Guide | tutorial | parameter-skim | pending | Dana Point (SoCal) bait barge etiquette, VHF ch11 protocol, avoid-6am timing, tank-load capacity notes |
| Pv5JMTTY4nI | Your Saltwater Guide | tutorial | skip:duplicate-of-9qnQjPPT5yg | skipped | sweep sim 0.946, re-upload of 2021-05 PTO grip video (primary itself triaged skip:promo) |
| ur1F8gD1sF4 | Your Saltwater Guide | promo | skip:promo | skipped | Subscription-pitch-dominated; scattered tips (breeze-reading, avoid combat fishing) buried in rant |
| vJ70gNV72eY | Your Saltwater Guide | promo | skip:promo | skipped | Mostly generic date-day advice + subscription pitch; thin bait-tank-shape/fly-lining nugget |
| VsUUBICiBzQ | Your Saltwater Guide | tutorial | parameter-skim | pending | Improved-clinch knot tying procedure (7 wraps), retied after every fish due to teeth fraying line |
| qihSsdqBU2A | Your Saltwater Guide | non-fishing | skip:no-usable-content | skipped | Entire transcript garbled nonsensical ASR, no recoverable content (light-line theory unrecoverable) |
| 44pjBUn0nP8 | Your Saltwater Guide | on-the-water | skip:duplicate-of-wYeKJLoKo4g | skipped | confirmed: identical dialogue/duration(1:44) to primary yummy-flyer breezer clip |
| zVIfArUrpDI | Your Saltwater Guide | tutorial | deep | pending | SoCal rockfish quick-canyon rig: San Diego jam knot, dropper loop x2, circle-hook rationale, braid-vs-mono choice |
| CrLDC4O8qS8 | Your Saltwater Guide | on-the-water | observations-only | pending | SoCal kelp-paddy catch footage (dorado/yellowtail); minimal doctrine beyond patty-scouting heuristic |
| 8jC61LzQoxU | Your Saltwater Guide | tutorial | deep | pending | SoCal offshore bluefin fight doctrine: boat gear-tap, downswell drift, avoid death-circle, gaff timing (primary of bsbL7JeKxMo dup) |
| bsbL7JeKxMo | Your Saltwater Guide | tutorial | skip:duplicate-of-8jC61LzQoxU | skipped | confirmed: identical script/duration(5:53) to primary fight-giant-bluefin video |
| ftEvyfwjZFU | Your Saltwater Guide | tutorial | deep | pending | San Diego jam knot + lure selection by bluefin size, straight-tie-no-swivel rationale, match-the-hatch anchovy imitation |
| RbqOKkINSCM | Your Saltwater Guide | tutorial | deep | pending | Fly-line rig (San Diego jam, no weight/swivel, short fluoro), flat-fall/popper rig choice by mark depth, circle-hook rationale |
| 9qnQjPPT5yg | Your Saltwater Guide | promo | skip:promo | skipped | Product demo for patented PTO fighting-grip (22-degree angle mechanics); inventory/sales-pitch dominated |
| scmPq63lLWM | Your Saltwater Guide | tutorial | parameter-skim | pending | SoCal red-crab-pattern flat-fall color/rig selection logic (Fishlab product-focused), San Diego jam knot repeat |
| IMnoZVEYpm4 | Your Saltwater Guide | tutorial | single-pull | pending | longer YSG cut (442s) of BD hooks video m2q22sPPkEM (328s): extract ONLY tail content beyond the BD cut |
| f4qYtHACGyk | Your Saltwater Guide | tutorial | deep | pending | SoCal artificial-reef light-line finesse rig (straight-tied hook, small shot sized by current), chum-density feeding-frenzy technique |
| NC3-3pJDEgo | Your Saltwater Guide | tutorial | deep | pending | SoCal Santa Ana wind pattern + go/no-go thresholds (12kt wind, <10s swell interval), Catalina return-trip risk |
| FEXgl0eQCa8 | Your Saltwater Guide | tutorial | deep | pending | Sounder setup doctrine: manual range, bottom mid-screen, hard/soft-bottom ID, learn in harbor first (bottom-hardness reading) |
| 1hJoxwg9fy4 | Your Saltwater Guide | on-the-water | observations-only | pending | Catalina Island WSB catch/fight footage; generic fighting commentary (tip up, avoid kelp), no deep doctrine |
| fK2AT460xW4 | Your Saltwater Guide | tutorial | deep | pending | Tuna-under-dolphin live-bait rig: torpedo sinker, San Diego jam knot, circle hook, drop presentation; SoCal |
| HOYJ6TAMrg4 | Your Saltwater Guide | promo | skip:promo | skipped | PTO Fighting Grip product demo w/ marlin+sailfish action footage; sponsor-heavy; feeds dave-hansen registry |
| 6DzbsElGE7E | Your Saltwater Guide | tutorial | deep | pending | Reading the fish finder: hard vs mud bottom signature, bait marks, where to anchor for yellowtail; SoCal |
| w5_x6kkN-xE | Your Saltwater Guide | tutorial | deep | pending | Live mackerel fly-line rigging: butt-hook vs nose-hook vs kite back-hook and why each is used; SoCal |
| _aimmQmzqz0 | Your Saltwater Guide | promo | skip:promo | skipped | PTO Fighting Grip product intro/specs/sizing; sponsor-heavy, same product as HOYJ6TAMrg4 |
| OIqdmhKfuOc | Your Saltwater Guide | tutorial | deep | pending | Dropper-loop deploy procedure: drop straight down, index-on-spool/thumb-on-trigger bite detection |
| KLoEJInlmZo | Your Saltwater Guide | tutorial | deep | pending | Surface iron mechanics: sideways-reel cast for distance, tip-down retrieve, reading the kick, line guide |
| wzI0lpgKT1U | Your Saltwater Guide | tutorial | deep | pending | Yo-yo iron cadence: cast, sink to bottom, 10-crank increments, repeat; SoCal yellowtail |
| kr-DZP7OVmg | Your Saltwater Guide | tutorial | skip:duplicate-of-4xzK7YaXK5s | skipped | same recording as BD id already extracted in batch 1 (sweep sim 0.814) |
| e5qGRAzwEWQ | Your Saltwater Guide | promo | skip:promo | skipped | Subscription pitch for yoursaltwaterguide.com throughout; no standalone technique content |
| BdRX4b8Fo5w | Your Saltwater Guide | tutorial | parameter-skim | pending | Bait tank: round/oval shape, center of deck, change bait every minute, prey-density concept; SoCal |
| dgauGbNxP84 | Your Saltwater Guide | on-the-water | parameter-skim | pending | Trolling a current break back-and-forth holds fish; Cabo San Lucas region |
| ll7r4A6atno | Your Saltwater Guide | tutorial | parameter-skim | pending | Title says dorado, content is sierra: hoochie+wire rig, AM/sunset bite, dirty-water cue; Cabo |
| OSbAHdB4uPs | Your Saltwater Guide | tutorial | deep | pending | CA sheephead: #2/#4 bronze hook, quarter-half oz slider, suspend bait off bottom, pismo clam/mussel bait |
| EiItVWqFMYc | Your Saltwater Guide | tutorial | parameter-skim | pending | Hoop net soak/pull timing: soak 1hr before dark, pull 30min after sunset, reset nets on same spot |
| 2y0VznL2qk8 | Your Saltwater Guide | tutorial | deep | pending | Bluefin bait decision: >8kt wind = rubber flyer trolled 8.5kt; <8kt = dead flyer under kite/balloon |
| gKrYKvqHUjk | Your Saltwater Guide | tutorial | deep | pending | Fly-line rig: line weight matched to bait (40lb for mac vs 15-20lb for anchovy), casting for distance |
| Rf1HKJG-SDg | Your Saltwater Guide | tutorial | deep | pending | Bank-naming lexicon: fathom-depth naming convention, structure/bait/fish relationship; SoCal offshore |
| YPhc0zr7oBs | Your Saltwater Guide | seminar | skip:duplicate-of-aFb221LUoD0 | skipped | triage-confirmed: near-verbatim same swell/current/water-color seminar, shorter cut; longer cut is the primary |
| ShSxNKAcUB4 | Your Saltwater Guide | tutorial | deep | pending | WSB: sliding-sinker weight ladder by current/depth, thin-wire hook, suspend-and-retrieve technique |
| cEscIy278ew | Your Saltwater Guide | tutorial | deep | pending | Hoop net retrieval: always back stern into buoy, spotlight on line, bump-forward to clear prop |
| aFb221LUoD0 | Your Saltwater Guide | seminar | deep | pending | Swell/current/wind-based spot selection w/ named Catalina spots; overlaps YPhc0zr7oBs (longer cut) |
| 7HApvxvtxgo | Your Saltwater Guide | tutorial | skip:thin-generic | skipped | Generic sport-boat etiquette advice, no fishing-technique content |
| CjQD4vJmsog | Your Saltwater Guide | promo | skip:promo | skipped | Pure subscription pitch for yoursaltwaterguide.com, 1:23 runtime, no technique content |
| 89DmEDR-1sI | Your Saltwater Guide | on-the-water | skip:duplicate-of-6zYRI1ZQU3c | skipped | confirmed: same San Diego tuna chum footage as 6zYRI1ZQU3c, ASR/caption variance only |
| 6zYRI1ZQU3c | Your Saltwater Guide | on-the-water | observations-only | pending | Observed: San Diego yellowfin tuna chum-bite, free-swimmers charging boat |
| pX6mV3O0L_E | Your Saltwater Guide | on-the-water | observations-only | pending | Observed: Cabo San Lucas ballyhoo troll for dorado, catch footage, minimal rig narration |
| HeMNAw6MDVE | Your Saltwater Guide | non-fishing | skip:not-fishing | skipped | Cabo marina walkthrough: restaurants/hotels/beach tourism, only trivial fishing-license mention; not fishing content |
| qv0QbLgp72o | Your Saltwater Guide | on-the-water | single-pull | pending | Smaller bait raises prey-density reaction/bite rate on tuna+calico; overlaps zwNEhWtnBCE, subscribe-pitch framing |
| CLkO0QUwb_c | Your Saltwater Guide | tutorial | skip:thin-generic | skipped | Generic kids-fishing advice (calm day, small bait, dont go offshore); one Dana Point red-buoy mackerel mention |
| YQsbwfQ4wzY | Your Saltwater Guide | tutorial | parameter-skim | pending | Hoop-net lobster bait: fresh bait beats old, DIY PVC bait-tube (2in x18in) evades sea lions, Catalina 20-30ft, LB/SD post-rain timing |
| mdhoEQPqpng | Your Saltwater Guide | on-the-water | single-pull | pending | Yellowtail catch footage; real technique: free-spool slack to fool sea lion into releasing hooked fish, then wind fast |
| 8Asmd2H56Qk | Your Saltwater Guide | tutorial | skip:duplicate-of-sYrsPGXiYhI | skipped | same recording as BD rubber-band-rig video per analysis doc (sim 0.518, ASR variance) |
| TLEhULOWj7g | Your Saltwater Guide | on-the-water | skip:no-usable-content | skipped | Facebook-live hookup chaos/shouting, no location or conditions detail, no doctrine |
| xI9tPJFXbUM | Your Saltwater Guide | tutorial | deep | pending | Inshore 5-tips: chum bucket on bow not stern, anchor in front of rock, wind/current-to-spot matching logic; Catalina/SCI/San Onofre/La Jolla |
| 9hEa3sGTh40 | Your Saltwater Guide | tutorial | deep | pending | Offshore prep: round bait tank placement, fathom/manual-mode fishfinder 0-120ft rule, VHF ch72/65 use, radio-misinformation warning |
| zwNEhWtnBCE | Your Saltwater Guide | on-the-water | observations-only | pending | Calico-bass-on-bait catch footage; overlaps qv0QbLgp72o; heavy plug for paid website course (sponsor-heavy) |
| 5FzBwvMtRP8 | Your Saltwater Guide | tutorial | single-pull | pending | Microfiber rag lure catches mackerel for bait tank; dont hand-touch mackerel (strips slime), flick off with butter knife |
| AZ7N_nRmLnc | Your Saltwater Guide | on-the-water | skip:no-usable-content | skipped | Mislabeled tutorial; just wide-open dorado bite shouting, no fishfinder-reading content despite title |
| poqjnb1r1zk | Your Saltwater Guide | on-the-water | parameter-skim | pending | Dana Point bonito: small feathers trolled ~5.5kt, cast hard-bait lure while trolling; 5:45am start, slow morning |
| KCcEqHSZ84k | Your Saltwater Guide | on-the-water | parameter-skim | pending | Northwest Harbor SCI calico: hold rod tip high/no pump in ~6ft rock water; 65lb braid, 30lb fluoro top shot |
| KTsXdQXAnkU | Your Saltwater Guide | on-the-water | parameter-skim | pending | Never pump rod, grind calico out of kelp; 25lb fluoro, 1oz black/gold jig sunk to kelp base; grab lower lip, foam-rinse release |
| ZFqe49jRgA0 | Your Saltwater Guide | tutorial | deep | pending | Dont chase sport boats to find fish; drive straight up on kelp paddies, check meter 90-120ft, 1-2min dwell, paddies restock at night |
| eNcltRh-shc | Your Saltwater Guide | on-the-water | observations-only | pending | Repeats rod-tip-high technique; Northwest Harbor/SCI shallow rock, 30-40ft visibility, catch footage |
| _KldpqPPT1c | Your Saltwater Guide | on-the-water | observations-only | pending | Anchored outside Cat Harbor (Catalina), light bass catch footage, minimal conditions detail |
| HGyL7pXy3Ts | Your Saltwater Guide | tutorial | deep | pending | Anchoring on structure at Catalina: fathom-feet conversion, 120ft chain-to-rope drop then reset by boat lay, sonar bottom check |
| 6ueGWJek1gI | Your Saltwater Guide | tutorial | parameter-skim | pending | Bait-hooking technique: leave rod on rail, net not hands (keeps scales/slime), pick green-backed bait, dont cast hard |
| lF6jQklDCrY | Your Saltwater Guide | tutorial | single-pull | pending | SoCal rockfish season opens March 1; claims depth limit rising 350ft to 460ft (self-admitted uncertain reading of regs) |
| kzD0kSnnVPw | Your Saltwater Guide | tutorial | single-pull | pending | Current direction sets kelp/structure corner to fish (downhill=NW corner, uphill=SE); San Onofre/Pt Loma/La Jolla/SCI/Catalina |
| EE0P4SvcNFg | Your Saltwater Guide | tutorial | single-pull | pending | Cut squid into thin strips, not big chunks, for more bites |
| e16i7zKq1FY | Your Saltwater Guide | tutorial | single-pull | pending | Boats drift stern-first; always throw chum off the downhill (lee) corner matching wind/current side |
| wYeKJLoKo4g | Your Saltwater Guide | on-the-water | single-pull | pending | Approach breezing bluefin slowly; flying-fish-imitation Yummy lure w/ balloon triggers strike; San Clemente Island |
| jahddqzKhLY | StokedOnFishing | tutorial | parameter-skim | pending | Bimini twist quick-tie tip, generic knot skill, no region/species markers |
| eEcRPEoG4DQ | StokedOnFishing | tutorial | parameter-skim | pending | Rockfish dropper-loop bottom rig: surgeon's knot, leader length, hook spacing, line-wt-by-drift rule |
| YZT-_SdmQNs | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tube-bait flip/pitch rig near trees/weeds mimicking crawdad - reads as freshwater bass technique |
| IB3IqZKxEhk | StokedOnFishing | promo | skip:promo | skipped | Simrad rep (Tito Perez) demos chartplotter bridge-control feature; no fishing content, sponsor-heavy |
| ILoJ_fzV4fY | StokedOnFishing | promo | skip:promo | skipped | Simrad rep demos Go Free WiFi app/box incl. pricing; no fishing content, sponsor-heavy |
| 06lxuie5cZQ | StokedOnFishing | tutorial | parameter-skim | pending | Mono-to-fluorocarbon knot tie, generic, no region markers |
| Jvv6DMNIHbE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | CA lake threadfin-shad/striper bass fishing, freshwater; series: Bass Fishing Live Shad part 1 |
| 6-mi3Qxn37c | StokedOnFishing | on-the-water | observations-only | pending | SoCal Mission Bay spotted bay bass; tide pref 4-5ft, Alabama rig, 60-80lb braid/40lb fluoro topshot |
| 2gHRrR3D8rY | StokedOnFishing | tutorial | parameter-skim | pending | Halibut filleting walkthrough: spine-follow cut, skin removal, ice-saltwater soak trick; region unstated |
| rJ-Omw4Ob74 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Halibut rig setup explicitly filmed in Alaska |
| wALN3RpsSxU | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Anchor-retrieval buoy hack explicitly filmed in Alaska |
| H-vIGWPIPVc | StokedOnFishing | on-the-water | parameter-skim | pending | San Clemente Island SoCal yellowfin/bonita catch-clean-cook; gill-bleed tip; sponsor-heavy intro |
| KPzJuwh6kbo | StokedOnFishing | non-fishing | skip:not-fishing | skipped | Pure tuna-steak marinade/cook recipe, no catch footage, sponsor-heavy intro |
| z85Fy52itS8 | StokedOnFishing | non-fishing | skip:not-fishing | skipped | Pure rockfish ceviche recipe; fish caught in Alaska (mentioned only), no catch footage |
| tzeXXPAjqUY | StokedOnFishing | tutorial | parameter-skim | pending | Seaguar mono-to-fluoro knot tie, generic |
| 1BH7nQdIg5Q | StokedOnFishing | tutorial | parameter-skim | pending | San Diego knot tie basics, generic |
| NkjjDf6XPcE | StokedOnFishing | tutorial | parameter-skim | pending | Uni-to-uni knot tie, generic |
| AT6zmDYxjW4 | StokedOnFishing | tutorial | parameter-skim | pending | Royal Polaris (Roy Rose) braid-to-mono knot tie, generic |
| NLDKbLw2q-E | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Lake Cachuma freshwater bass camping trip; series: Lake Cachuma part 2 |
| _0xZV0PojhE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Lake Cachuma freshwater bass camping trip; series: Lake Cachuma part 1 |
| Y2bXn44lfqo | StokedOnFishing | on-the-water | parameter-skim | pending | Catalina SoCal white seabass MLPA/broodstock, anchoring, dropper-loop rig; series: WSB Conservation part 1 |
| 82gEHYel-4U | StokedOnFishing | on-the-water | parameter-skim | pending | Catalina/Carlsbad SoCal WSB wrap-up; milky-water uphill/downhill spot-ID method; series: WSB Conservation part 2 |
| ldVj0BoB-kE | StokedOnFishing | report | deep | pending | Confirmed pre-ID: Baja Cedros Island 100% catch-and-release reg change, calico/grouper/black seabass |
| ntQXxcH5sjI | StokedOnFishing | tutorial | deep | pending | Confirmed pre-ID: yo-yo iron doctrine, Tanner/Cortez Bank SoCal, jig/leader/knot specs |
| FE63WNlwkKw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Legg Lake/Whittier Narrows freshwater tournament; not saltwater despite LA/SoCal location |
| 3S3Tx-Me2HY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clear Lake NorCal freshwater LiveScope bass fishing; title-trap, not SoCal saltwater |
| c-LLt6fG2n0 | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Clear Lake bass w/ Garmin LiveScope; freshwater excluded despite CA location |
| af51LVG_5SE | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Clear Lake winter bass fishing w/ LiveScope guide; out of region |
| rI4P4PrOsPo | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Clear Lake bass/catfish/crappie trip; out of region |
| SHFrJzWZP-g | StokedOnFishing | on-the-water | skip:out-of-region | skipped | Freshwater Legg Lake (LA) bass/bluegill/crappie tourney; freshwater excluded despite SoCal loc |
| k4LCL9ALryA | StokedOnFishing | on-the-water | observations-only | pending | San Diego Bay spotted bay bass, SWBA pre-fish; dock-flip, ~18-20ft, shad-pattern color |
| wJl8SZhmaWg | StokedOnFishing | promo | skip:promo | skipped | SWBA tournament sizzle/testimonial reel, no instruction; promo |
| EU_Dod4wfYw | StokedOnFishing | on-the-water | observations-only | pending | Santa Barbara Island calico bite w/ Benny Florentino; catch montage, garbled ASR, notes kelp |
| AxLlx2Ug-rs | StokedOnFishing | on-the-water | parameter-skim | pending | Coastal Charters: fish hold tight to pilings, cast close; 7'2" med rod, Curado 200E7, 65lb braid |
| YijeuGOYoVQ | StokedOnFishing | on-the-water | observations-only | pending | East Cape Baja, wahoo/marlin/rooster at Lighthouse; sponsor-heavy; series: Hotel Buena Vista part 2 |
| mL4Ph7t0WcQ | StokedOnFishing | on-the-water | observations-only | pending | East Cape Baja, marlin/tuna/rooster fishing amid resort-booking talk; sponsor-heavy; series: Hotel Buena Vista part 1 |
| _Wb4z4ammoM | StokedOnFishing | on-the-water | parameter-skim | pending | Gonzaga Bay Sea of Cortez (Baja): wire leader/65lb spectra for toothy rock fish, 15lb+; series: Gonzaga Bay part 1 |
| A6s-A1NARuA | StokedOnFishing | on-the-water | parameter-skim | pending | Gonzaga Bay Sea of Cortez (Baja): grouper 80-90ft, big baits/wire/button drag; series: Gonzaga Bay part 2 |
| 9xNhdu2aBqE | StokedOnFishing | on-the-water | parameter-skim | pending | SCI calico w/ Todd Klein: smaller fish trigger bigger follow-up eats, MC9 swimbait, saved GPS marks |
| ROWgdFE9Ehc | StokedOnFishing | on-the-water | observations-only | pending | OC charity ep: kids fishing for yellowtail in the channel; sponsor-heavy |
| epWXURDU-oI | StokedOnFishing | on-the-water | skip:duplicate-of-9xNhdu2aBqE | skipped | Same trip/dialogue as 9xNhdu2aBqE (Todd Klein, SCI), short highlight cut - NEW dedup finding at triage |
| _C8w6zeVPak | StokedOnFishing | on-the-water | observations-only | pending | Cedros/Gono Islands Baja: yellowtail surface iron then calico shore; series: Shogun Skiff Trip part 3 |
| BvT560Nblqo | StokedOnFishing | on-the-water | observations-only | pending | Cedros Island Baja: yo-yo jig color note, trolled yellowtail; series: Shogun Skiff Trip part 2 |
| NGxyOlPx3ug | StokedOnFishing | on-the-water | observations-only | pending | Cedros/Gono Baja: MC Swimbaits giveaway intro, sponsor-heavy; series: Shogun Skiff Trip part 1 |
| Qa-j6LIwa1Q | StokedOnFishing | on-the-water | observations-only | pending | Cedros Island Baja: travel logistics + calico/yellowtail fishing; series: Cedros Island Adventure part 1 |
| XwwIvPFxRiQ | StokedOnFishing | on-the-water | observations-only | pending | Cedros Island Baja day 2: calico/white seabass/yellowtail catch montage; series: Cedros Island Adventure part 2 |
| 3SATCeA3KaU | StokedOnFishing | on-the-water | observations-only | pending | Baja (Geronimo/Cedros): calico surface iron, yellowtail brawl; sponsor-heavy; series: MC Swimbaits Skiff Trip part 3 |
| _r_qKX_7080 | StokedOnFishing | on-the-water | observations-only | pending | Baja, Chesters Rock: calico on weedless swimbaits; sponsor-heavy; series: MC Swimbaits Skiff Trip part 2 |
| L3tkGVu516A | StokedOnFishing | on-the-water | observations-only | pending | Baja (Sacramento Reef/Cedros): MC Swimbaits sponsor intro/gear giveaway; series: MC Swimbaits Skiff Trip part 1 |
| IATPg9110CE | StokedOnFishing | on-the-water | observations-only | pending | Catalina/Santa Barbara Is. tourney weigh-in drama, kelp/rock structure; series: CA Offshore Challenge part 3 |
| PKf7G3uL4io | StokedOnFishing | on-the-water | observations-only | pending | Catalina CA Offshore Challenge weigh-ins, minimal conditions detail; series: CA Offshore Challenge part 2 |
| iQLyBzhOSi8 | StokedOnFishing | on-the-water | observations-only | pending | Catalina, swell 3-7ft across days noted, thick kelp/sharp reef hazards; series: CA Offshore Challenge part 1 |
| 2ivn-N0as_A | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SWBA night tourney weigh-in/catch montage, no conditions detail; series: SWBA Midnight Standoff part 3 |
| 8KIsYpsIBwI | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Southwest Florida beach shark tournament; series: Giant Shark Florida part 2 |
| _Ejay_B77DA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Southwest Florida beach shark tournament; series: Giant Shark Florida part 1 |
| P6Slg6RQiXw | StokedOnFishing | on-the-water | deep | pending | Pre-ID deep confirmed: Aaron Martens/Benny Florentino SCI calico; braid/leader/reel-speed gear + kelp cadence/flip technique |
| vwH9ERf6zPI | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Long Beach Yacht Club SWBA/Olive Crest charity tourney catch footage, no conditions detail |
| M6U_FVdosr4 | StokedOnFishing | on-the-water | parameter-skim | pending | Dana Pt kelp bed kids trip: squid outfished sardine that AM, anchor vs drift in current decision |
| x1Vb7c4Ek-U | StokedOnFishing | promo | skip:promo | skipped | Stoked On Fishing show trailer announcing Fox Sports West premiere, sizzle reel only |
| NQsVlcpNfck | StokedOnFishing | promo | skip:promo | skipped | Shogun Sportfishing skiff-trip promo, Catalina kelp/skiff catch footage but ad for booking charter |
| pd1VOJbTEEM | StokedOnFishing | report | skip:thin-generic | skipped | Long Beach Yacht Club charity-venue talk for Olive Crest event, zero fishing footage |
| N1YBY1i600U | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SWBA California Offshore Challenge (Catalina/SCI) tourney hype+catch footage, no conditions detail |
| mXu8vJ8yr4Q | StokedOnFishing | on-the-water | single-pull | pending | Catalina backside calico: weedless swimbait hook survives many trips w/o losing paint or fish |
| xIUKmH9ccgQ | StokedOnFishing | on-the-water | observations-only | pending | Baja Cedros catch montage via small-plane charter, no doctrine, mostly reaction footage |
| IFhBVRoc4VQ | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SWBA/Sanderson Farms Shelf Bass Special weigh-in/catch footage, no conditions detail |
| fjMHM1V9iPc | StokedOnFishing | report | skip:thin-generic | skipped | Bass-stravaganza vendor/seminar-day recap interviews on standings/sponsors, no technique captured |
| FurifnQ27mM | StokedOnFishing | on-the-water | single-pull | pending | San Diego/Chula Vista spotted bay bass tourney (Border Town Brawl): shrimp-pattern lure worked |
| wdbqTio1SQU | StokedOnFishing | on-the-water | observations-only | pending | Baja Cedros: North Pt spot noted for 30+lb yellows, brief surface-iron/yo-yo mentions, sponsor-heavy |
| RPSRH0jwyw4 | StokedOnFishing | on-the-water | observations-only | pending | Baja Cedros West End backside spot catch footage; series: Cedros GOES OFF part 2 |
| yuXr3IJ8ybg | StokedOnFishing | on-the-water | observations-only | pending | SCI Pyramid Head Okuma gear-demo trip (PCH rods/Toro reels), sponsor-heavy, some catch footage |
| Turj5ZKNcuE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Kingdom of Tonga travel/lifestyle episode; series: Stoked On Tonga part 1 |
| sJCoSQpanU4 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tonga kiteboarding/kayak reef episode; series: Stoked On Tonga part 2 |
| xHT7oJGRQyk | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tonga vanilla factory/cave-swim wrap-up episode; series: Stoked On Tonga part 4 |
| U60jPPBu5CM | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Save The Brave veteran-charity trip, golf + brief rockfish catch reactions, region unclear/Baja island |
| qri15R3caYE | StokedOnFishing | on-the-water | observations-only | pending | Baja La Bocana co-op fishing village catch montage; series: Stoked On La Bocana part 1 |
| Cobp85UvHmM | StokedOnFishing | on-the-water | observations-only | pending | Baja La Bocana: 25mi offshore troll for marlin/tuna/wahoo + estuary fishing; series part 2 |
| tcso7Lpm_Xs | StokedOnFishing | on-the-water | observations-only | pending | Baja East Cape (Buena Vista resort): troll tuna/dorado/marlin, rooster fish beach teaser |
| 3yK3JYrKoZY | StokedOnFishing | on-the-water | parameter-skim | pending | Baja Cedros: yo-yo lazy-boy/clicker technique note + West End calico bite; series part 2 |
| d0yGBQDeY_4 | StokedOnFishing | on-the-water | parameter-skim | pending | Cedros, Baja; bait-ball yellowtail approach, sliding-sinker rig, circle hooks, fog/radar nav fact; series: Big Yellowtail pt1 |
| 84XPJAeH0Rw | StokedOnFishing | on-the-water | observations-only | pending | East Cape/Sea of Cortez Baja (Cabo mentioned); Fiesta catch montage, points race; series: Non-Stop Tuna Fiesta pt1 |
| GptrotE0x5M | StokedOnFishing | on-the-water | observations-only | pending | East Cape Baja Fiesta continuation; catch montage, points race; series: Non-Stop Tuna Fiesta pt2 |
| _c6UI3lGBVg | StokedOnFishing | on-the-water | parameter-skim | pending | East Cape Baja (Cabo mentioned), 52ft ~2mi off shore; squid presentation + big-tuna fight/hand-off tip; series pt2 |
| 6j7V34GYzzw | StokedOnFishing | on-the-water | observations-only | pending | East Cape Baja, Buena Vista Resort 2018; multi-species catch montage; series pt2 |
| ecJPMTCi-gw | StokedOnFishing | on-the-water | parameter-skim | pending | San Clemente Is. SoCal; yo-yo downsizing + surface-iron alternation + structure-corner tip |
| CuK0_9v1F_o | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus) halibut fishing |
| tJFSV3AcIdE | StokedOnFishing | on-the-water | parameter-skim | pending | Catalina/San Clemente Is. calico tournament pt2 (2016 throwback); gear specs, kelp-paddy edge position, culling |
| 7aF6uWVw76g | StokedOnFishing | on-the-water | single-pull | pending | Region unconfirmed (low confidence); single fact: 40lb leader landed striped marlin on baitcaster |
| 9D3Oiy0ASzg | StokedOnFishing | on-the-water | single-pull | pending | San Benito Is. Baja; sparse, one note: braid cuts through kelp then rock cutoff risk on yellowtail |
| wJgoRhZStz0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Amazon/Brazil peacock bass, freshwater |
| xudAbDj4GYw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama, Coiba Is. inshore/offshore |
| CdJ-ISFv8BI | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama offshore tuna/dorado/marlin |
| APsnsunT4gM | StokedOnFishing | on-the-water | observations-only | pending | East Cape Baja, Buena Vista Resort 5th annual Fiesta; catch montage, sponsor-heavy |
| SImABCBBxAo | StokedOnFishing | on-the-water | parameter-skim | pending | SoCal spotted bay bass; color-to-overcast, depth 18-30ft, bait-profile matching tips |
| LE49ush9zqA | StokedOnFishing | on-the-water | skip:thin-generic | skipped | No location/conditions given; pure catch montage of double yellowtail hookups |
| isXJONlpUP4 | StokedOnFishing | on-the-water | parameter-skim | pending | Magdalena Bay Baja inshore; wind/chop decision to switch offshore marlin plan to estuary mangroves |
| OVwqUKim9Pc | StokedOnFishing | on-the-water | parameter-skim | pending | Mag Bay Baja; sea-state based bank routing decision, names bank Modesto Main; series cont. |
| yjwIGFzWO8I | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja pt3; multi-stop itinerary macro banks to Benitos to mainland Chesters Rock; series pt3 |
| DGh-iUp63Hc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska Gustavus halibut/black bass/salmon |
| j-hRaVWkQw4 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska Gustavus halibut pt2 |
| 9pJA2BnCjpc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica private creek machaca, freshwater jungle stream |
| MhJeCS_c3h8 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica inshore wahoo/grouper + offshore tuna |
| Nz5kTJQvuEY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica catch-and-cook tuna, offshore fishing + cooking segment |
| V_ONnegk95M | StokedOnFishing | on-the-water | parameter-skim | pending | San Clemente Is. SoCal; captain briefing: bait selection, 30# test/3-0 hook, drag setting, timing |
| QSmE3mdEL28 | StokedOnFishing | on-the-water | parameter-skim | pending | Cedros Baja; 80-100# test in shallow 30ft, slow-troll mackerel, sabiki sizing, catch-release ethic tip |
| brx6Ie_L2FM | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja dorado bite on kelp paddy; personal-best yellowtail; sponsor-heavy intro |
| I-QBxuV2p7M | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja calico bass trip, day2 bait-making footage, mostly banter |
| e73wPONTOJU | StokedOnFishing | on-the-water | observations-only | pending | SoCal offshore ElDorado bluefin/dorado chase; Mad Max/spreader bar mention, foamers |
| VWClGAn2WEw | StokedOnFishing | on-the-water | deep | pending | Kelp-paddy pattern doctrine: drift setup, electronics+eyeballs, work-bird/discoloration cues |
| HMdrP4-i9MM | StokedOnFishing | on-the-water | observations-only | pending | Dana Point SoCal kids/Okuma trip; calico bass, kelp depth ~40ft, fly-line note |
| eUUtSmiskbA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Amazon peacock bass, freshwater, not SoCal/Baja |
| l0kB6y0klwY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Amazon Blackwater Explorer mothership promo, freshwater peacock bass |
| xzIaUEDklrE | StokedOnFishing | on-the-water | deep | pending | Pre-ID deep: captain-narrated SoCal bluefin trolling, Mad Max/spreader bar/kite selection logic |
| QCXlPULXf4A | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Puerto Rico wahoo/tuna/tarpon, Caribbean |
| RSMA1xrGngA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Puerto Rico Caribbean charter, wahoo/yellowfin |
| vdgf_C1-P08 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Puerto Rico Caribbean, Dorado/tarpon, sponsor-heavy |
| 55-Sx8V1Uk8 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama Coiba/Hannibal Bank charter |
| ZBRSB4iwtbU | StokedOnFishing | on-the-water | skip:duplicate-of-ldVj0BoB-kE | skipped | confirmed: identical Jose interview on Cedros C&R reg change, same 1:57 runtime |
| HEyt8fxoH5w | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama Coiba cubera snapper/roosterfish/yellowfin |
| 9tIp4n7q850 | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja halibut/yellowtail trip, SOS lodge, slow-troll mackerel bait |
| Zo92MG459gQ | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja halibut+giant yellowtail continuation, calico spot mention |
| zn4n7k3iaZo | StokedOnFishing | seminar | parameter-skim | pending | SD/Carlsbad hatchery history interview w/Bill Shedd; OREHP program, survival/tag data |
| xFS3MW4GpDU | StokedOnFishing | on-the-water | parameter-skim | pending | Carlsbad hatchery wrap + Catalina SoCal broodstock WSB catch program, <60ft, May-Jun timing |
| ORC1A68cEeM | StokedOnFishing | on-the-water | observations-only | pending | La Paz Baja first-time trip, yellowtail/cabrilla, bait-making routine noted |
| qM7iOO7fOBw | StokedOnFishing | on-the-water | observations-only | pending | La Paz Baja charter, dorado/yellowtail/pargo/grouper, fly-lined mackerel |
| 92y14x33etQ | StokedOnFishing | on-the-water | observations-only | pending | La Paz Baja, Espiritu Santo island snapper/grouper on live bait |
| haJ3BancQDI | StokedOnFishing | promo | skip:promo | skipped | Short Okuma Alijos lever-drag reel product highlight clip |
| YUdbrIm9vrE | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja Oct trip, multi-species yellowtail/tuna/dorado/halibut |
| A8SuzB5qiKE | StokedOnFishing | on-the-water | observations-only | pending | Cedros Baja Oct trip, yellowtail/tuna/dorado/calico/sheephead/halibut |
| PAZA-PzMcWQ | StokedOnFishing | promo | skip:promo | skipped | Sizzle reel montage, no content, channel promo |
| Xnq3FIUzvuw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska Gustavus king salmon charter |
| usHl-4SfqDA | StokedOnFishing | on-the-water | deep | pending | SoCal (Balboa Island/offshore CA); pre-ID deep Pacific Giants film; kite/flying-fish rig, tuna belt/railroading, bleed-gut process |
| RpfHO-kotc8 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus); king/sockeye salmon; sponsor-heavy intro |
| Sz88huROjtY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus) halibut/rockfish; sponsor-heavy intro |
| SS_ObRfLw2E | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska halibut dropper-loop/grub jig; sponsor-heavy intro |
| 6EDQtQHEwFE | StokedOnFishing | on-the-water | observations-only | pending | Baja (Cedros Island) yellowtail on surface iron; series: Cedros Oct trip part 1 |
| ILBl12Jm7-0 | StokedOnFishing | on-the-water | observations-only | pending | Baja (Cedros Island) yellowtail/calico, yo-yo+surface iron; series: Cedros Oct trip part 2 |
| u0scEBby7nA | StokedOnFishing | on-the-water | observations-only | pending | Baja (Cedros Island) wrap-up, yo-yo iron limits; series: Cedros Oct trip part 3 |
| qBZxnRuXtGo | StokedOnFishing | on-the-water | skip:duplicate-of-SdwwpQMJEOI | skipped | confirmed: identical Olive Crest tournament script/footage as SdwwpQMJEOI |
| PexiSOiN00o | StokedOnFishing | promo | skip:promo | skipped | Okuma Tesoro reel product demo; rock fishing/salmon/halibut clips, region unclear; sponsor-heavy |
| wj8IyrcsmF4 | StokedOnFishing | promo | skip:promo | skipped | 30s Okuma Tesoro reel teaser, same clips/lines as PexiSOiN00o; sponsor-heavy, no region |
| 0dIwWiOc1NY | StokedOnFishing | on-the-water | observations-only | pending | Baja (Ensenada) catch-for-donation trip; mackerel bait, yellowfin scouting 30-40mi out |
| DTrhKKBEQyY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska (Gustavus) salmon+halibut harpoon; sponsor-heavy intro |
| V7AfmB9pl_I | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama (Coiba/Chiriqui); Inshore-labeled but out-of-region travel trap; sponsor-heavy |
| UfuiWFVvz2E | StokedOnFishing | on-the-water | observations-only | pending | SoCal (San Diego, Constitution) Cortez Bank bluefin then Baja kelp-paddy yellows |
| 7U4N1f0viOU | StokedOnFishing | on-the-water | observations-only | pending | Baja (Cedros) best-of recap reusing earlier Cedros trip footage/dialogue |
| R1F66XIjf3E | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama (Coiba Island) yellowfin tuna; sponsor-heavy intro |
| sHnqSIOjTdM | StokedOnFishing | on-the-water | observations-only | pending | SoCal (San Clemente Is./offshore Eldorado) yellowtail then night bluefin jig |
| mDmbGdQAy-4 | StokedOnFishing | on-the-water | deep | pending | SoCal (Huntington Beach/Santa Barbara Is.) kite+flying-fish rig, railroading; overlaps usHl-4SfqDA footage |
| SdwwpQMJEOI | StokedOnFishing | on-the-water | observations-only | pending | SoCal (Long Beach) Olive Crest bass tournament; primary of qBZxnRuXtGo dup |
| Y1xeieQI3B4 | StokedOnFishing | on-the-water | observations-only | pending | SoCal (Cortez Bank/Eldorado) day2 wrap+switch to rockfishing; series: Cortez Bank trip part 3 |
| nQvJnfb5jQ4 | StokedOnFishing | on-the-water | observations-only | pending | SoCal (Cortez Bank/Eldorado) bluefin+yellowtail fly-line; series: Cortez Bank trip part 2 |
| eL1Qm33-Mj0 | StokedOnFishing | on-the-water | observations-only | pending | SoCal (Cortez Bank, Long Beach Eldorado) day1; series: Cortez Bank trip part 1 |
| zBd1mayUt_I | StokedOnFishing | on-the-water | observations-only | pending | SoCal (Cortez Bank/Ranger 85) yo-yo yellows+kite bluefin; series: Ranger 85 trip part 3 |
| QSvzVHW9UMk | StokedOnFishing | on-the-water | observations-only | pending | SoCal (Cortez Bank, 96mi SW San Pedro) bluefin; series: Ranger 85 trip part 2 |
| LsFMBCa9DOQ | StokedOnFishing | on-the-water | observations-only | pending | SoCal (San Diego H&M Landing, Cortez/Tanner Bank) 3-day charter; series: Ranger 85 trip part 1 |
| Ix0gG0-l3v0 | StokedOnFishing | on-the-water | deep | pending | Baja (Ensenada) bluefin tournament; detailed kite/flying-fish rig how-to, release clip, tagline specs |
| U1AgwmlY5bI | StokedOnFishing | on-the-water | observations-only | pending | Baja Bluefin Tournament, Ensenada Mexico, day 2; only tourney weigh/video rules, no fishing doctrine; series part 2/2 |
| prQpoN9qWBY | StokedOnFishing | on-the-water | observations-only | pending | Baja Bluefin Tournament, Ensenada Mexico, day 1; travel/check-in footage; series part 1/2 |
| r4J5nP5Bkl4 | StokedOnFishing | on-the-water | observations-only | pending | El Dorado, SoCal, backside San Clemente Is; kelp-paddy dorado/bluefin chum-and-bite footage |
| oB4BpIUTTl4 | StokedOnFishing | on-the-water | parameter-skim | pending | El Dorado SoCal night jigging: 100lb braid/mono min, 2-400lb leader, 350g+ jigs, flyline 25-40lb #2 hook |
| mj50D4rNfdI | StokedOnFishing | promo | skip:promo | skipped | 30s El Dorado boat ad, pure vessel-amenities pitch, no fishing content |
| c3NFkQbdDy0 | StokedOnFishing | on-the-water | observations-only | pending | El Dorado, 90mi off CA coast, bluefin/yellowtail catch footage, sponsor-heavy |
| 9qMLztwVx9g | StokedOnFishing | on-the-water | observations-only | pending | Red Rooster, San Diego SoCal, sponsor-heavy (GrundensUSA), night yo-yo bluefin footage |
| 947solNfiPw | StokedOnFishing | on-the-water | observations-only | pending | El Dorado, Tanner Bank SoCal, sardine-bite bluefin catch footage |
| Tz5y87zUp_Y | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama dorado catch footage, region confirmed in transcript |
| rhaie9Tbi8I | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama (Hannibal Bank, spinner dolphins), yellowfin/dorado catch footage |
| aPkRKI35XV0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama, Coiba National Park, rooster/snapper/amberjack footage |
| fDSd9kqwYW0 | StokedOnFishing | on-the-water | parameter-skim | pending | El Dorado, Cortez Bank SoCal; captain recs 25lb test #2 hook flyline for yellowtail/rockfish |
| elBPRrdkugU | StokedOnFishing | on-the-water | observations-only | pending | El Dorado SoCal, San Clemente/Catalina, spreader-bar bluefin fight footage |
| nsUdT-zXI8s | StokedOnFishing | on-the-water | observations-only | pending | El Dorado, San Clemente Is SoCal, veterans charity trip; seal depredation, yellowtail catch |
| vCskOx6N-XM | StokedOnFishing | on-the-water | deep | pending | Tanner Bank SoCal; kite/spreader-bar rigging + selection logic (cover-ground vs marked fish), fight technique |
| lxM-AbTn3Sc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Nosara, Costa Rica inshore wahoo/tuna/dorado footage, sponsor-heavy |
| b8IqxTQ6xr0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Nosara, Costa Rica yellowfin/wahoo footage, sponsor-heavy |
| c9xWDUyzDDI | StokedOnFishing | on-the-water | skip:thin-generic | skipped | 1min Fishlab Scrum Popper catch clip, no region/conditions stated, product-demo feel |
| Kiq4hdJ8Gsk | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska halibut jigging footage, series Alaska part 4 |
| 6N4zaJdHFck | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska salmon footage, series Alaska part 3 |
| M7BtON4GZgQ | StokedOnFishing | on-the-water | observations-only | pending | El Dorado, west end Catalina SoCal, 2020 limited-load bluefin footage |
| 4t_Z75shK_E | StokedOnFishing | on-the-water | observations-only | pending | Mag Bay, Baja Mexico (in-scope); marlin/wahoo/dorado inshore+offshore footage |
| BQ2U1PqxWi8 | StokedOnFishing | on-the-water | observations-only | pending | East Cape, Baja Mexico (in-scope), Hotel Buena Vista fiesta; tuna/dorado/marlin footage |
| UCADhIs5Ew0 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska rockfish/king salmon footage |
| 8GXiSWF_4wA | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Gustavus, Alaska halibut/rockfish/salmon footage |
| iczB-6A1Arc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama, Hannibal Bank/Coiba, tuna foamers footage |
| oXunQKSbc2g | StokedOnFishing | on-the-water | observations-only | pending | El Dorado 2-day, Long Beach, yellowtail/Cortes Bank, yo-yo & surface iron; SoCal |
| pu9zIm-Tsus | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Title misleads but content is Costa Rica trip w/ Craig Sutton |
| fxZGXrrpHz4 | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica marlin/sailfish/tuna/dorado trip, Nosara area |
| IxhdiX3oEEs | StokedOnFishing | on-the-water | observations-only | pending | SoCal bluefin catch-clean-cook, 184lb fish fight tips + sushi prep; fish-care angle |
| kS8eC_5y4oo | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Costa Rica double sailfish, release/handling footage |
| 9jDy4gUUyJk | StokedOnFishing | on-the-water | single-pull | pending | Drone spots fish holding under kelp paddies (technique); dorado catch; region unstated, treated in-scope |
| 1nK7vSPl2sg | StokedOnFishing | on-the-water | observations-only | pending | La Ventana Baja (East Cape/Sea of Cortez); amberjack, high spot 200->80ft, 30lb fluoro/circle hook |
| Klfb433I3Uk | StokedOnFishing | on-the-water | parameter-skim | pending | San Clemente Isl. yellowtail; chum-buddy/seal-avoidance tips; SoCal |
| SczdZIq3UmE | StokedOnFishing | on-the-water | parameter-skim | pending | SoCal tuna, 35ft Everglades; white-tern spotting tip; Simrad Halo radar demo, sponsor-heavy |
| Jz9KRNEHLkw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Alaska lingcod |
| 0bcDBGzQnGw | StokedOnFishing | on-the-water | observations-only | pending | Baja/Ensenada w/ Navico pt1; series: Fishing In Baja w/ Navico & Tito Ortiz part 1 |
| Q-gQuOegAx4 | StokedOnFishing | on-the-water | observations-only | pending | El Dorado 2-day, San Clemente Isl. bluefin 100-200lb then calico/bonita/yellowtail; SoCal |
| cLYqjT7ddl8 | StokedOnFishing | on-the-water | observations-only | pending | SoCal offshore bluefin, Okuma/PCH rod-reel product test; sponsor-heavy |
| CKq0Z6ExVs4 | StokedOnFishing | on-the-water | observations-only | pending | Ensenada Baja high spot (200->25ft): whitefish/yellowtail/rockfish/barracuda |
| YcLMhI5kzBo | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Tonga part 3, marlin/yellowfin, local cooking segment |
| SGbynqaiHdY | StokedOnFishing | on-the-water | observations-only | pending | Save The Brave veterans charity charter, San Clemente Isl. yellowtail target; light fishing content |
| rsCAh-QyK60 | StokedOnFishing | on-the-water | parameter-skim | pending | San Diego Bay/40mi off SD kite-fishing bluefin: kite distance/height/troll speed 6-8kn tips |
| tU4jhAkdzNw | StokedOnFishing | on-the-water | observations-only | pending | Top Gun 80 5-day pt3, SoCal islands; series: Top Gun 80 Epic 5 Day part 3; bluefin/yellowfin/yellowtail |
| 3T4c3Zez_DM | StokedOnFishing | on-the-water | observations-only | pending | Top Gun 80 5-day pt2, SoCal (SCI); series: Top Gun 80 Epic 5 Day part 2; bluefin then yellowfin/yellowtail |
| Rb5I2ljAqeE | StokedOnFishing | on-the-water | observations-only | pending | Top Gun 80 5-day pt1, SoCal (West End/SCI); series: Top Gun 80 Epic 5 Day part 1; squid bait, bluefin 40-90lb |
| mpcSgkQvIzg | StokedOnFishing | tutorial | parameter-skim | pending | Worm knot: mono topshot to Bimini twist, wrap count & fast field-retie method |
| 6kpWn2sXokI | StokedOnFishing | on-the-water | observations-only | pending | Intrepid pt3, Alijos Rocks Baja; series: yellowfin/wahoo/yellowtail/dorado on Intrepid part 3; yo-yo tip |
| ASitOLYzFEA | StokedOnFishing | on-the-water | observations-only | pending | Intrepid dock-day, Baja (lower banks/Alijos Rocks); testimonials, 300lb+ tuna, 4-day anchor |
| jznQMFoV0Ls | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Pure catch montage, almost no dialogue, no location/conditions detail |
| zUFbCIWZZMw | StokedOnFishing | on-the-water | observations-only | pending | Simrad radar/electronics demo (sponsor-heavy) then SCI/Catalina yellowtail & sea bass fishing |
| uyjTdgIw-1k | StokedOnFishing | on-the-water | parameter-skim | pending | SST temp-break method via Simrad electronics (3-4F diff) to locate fish; sponsor-heavy; SoCal Mission Bay |
| Ow3an9lSVh4 | StokedOnFishing | on-the-water | parameter-skim | pending | SoCal (San Clemente/Catalina lobster); sponsor-heavy; end-of-ep tips: sliding-sinker depth, butt-hook sardines, kelp-patty patience |
| 3qSY328fFYo | StokedOnFishing | on-the-water | deep | pending | SoCal marlin trolling (Catalina/tanker lanes/277 bank): spread setup, troll-downhill sun logic, tide timing, hookset technique |
| XH-Hrfet6To | StokedOnFishing | on-the-water | parameter-skim | pending | Cabo San Lucas (region); lure-selection logic: size by target/tournament, handling Cabo afternoon chop; Stoked On Cabo pt1 |
| Mwx5AAXNMvE | StokedOnFishing | on-the-water | observations-only | pending | Cabo San Lucas/East Cape (region); marlin catch-and-release footage + poke cook segment; Stoked On Cabo pt2 |
| 4bbKduPRlHE | StokedOnFishing | on-the-water | skip:no-usable-content | skipped | 1:48 near-wordless b-roll clip (mako hits hooked yellowtail); no location/date/technique content |
| skRo1z41Dnc | StokedOnFishing | on-the-water | observations-only | pending | San Diego offshore tuna footage; sponsor-heavy (Simrad); Top Gun 80 Offshore Grandslam pt1 |
| AfZoeSu_9hc | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Prince Edward Island, Canada bluefin trip; series pt1 |
| 27MMQGRIrpw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Prince Edward Island, Canada bluefin trip; series pt2 |
| SH7zOA9ZF3o | StokedOnFishing | on-the-water | parameter-skim | pending | San Diego/Bonita Isl yellowtail; yo-yo iron cadence explained step-by-step; fish-dive-to-structure note; series pt2 |
| pk2blktDQ9Y | StokedOnFishing | on-the-water | parameter-skim | pending | San Diego to Baja banks (long range); leader-test ladder by fish size, kite/squid double-hook rig, bait-care; series pt1 |
| Fq4aRI3YrKE | StokedOnFishing | on-the-water | observations-only | pending | Baja banks long-range tuna; fish-fight footage/personal-best chatter, no rigging detail; series pt2 |
| UuyqTE21-kc | StokedOnFishing | on-the-water | single-pull | pending | Baja the ridge; balloon-suspended flyer-bait downwind technique for tuna/marlin; series pt3 |
| D_Y2G0rBZCs | StokedOnFishing | on-the-water | parameter-skim | pending | San Clemente Isl yellowtail; sliding egg sinker/dropper loop, 20-25lb line, keep-bait-in-water tip |
| nkJNzdNlm_c | StokedOnFishing | on-the-water | observations-only | pending | San Diego offshore/Bonito Isl bluefin bite footage; sponsor-heavy; Top Gun 80 5-day Fun pt1 |
| JaKSGkZ6CAc | StokedOnFishing | on-the-water | parameter-skim | pending | Baja Bonito Isl; dropper-loop 100lb-min on bottom, yo-yo iron, squid-depth pattern (30-40fm); series pt2 |
| t-gIME7sV2A | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama trip; series pt1 |
| 2OANMH22qzE | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Panama/Hannibal Bank; series pt2 |
| IH4y6GM6BIY | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island (Revillagigedo Mexico), not Baja peninsula; series pt1 |
| aecs-mFrCdM | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island; series pt2 |
| HpPFogLwKOw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island; series pt3 |
| kWT_0Qp8wkw | StokedOnFishing | out-of-region | skip:out-of-region | skipped | Clarion Island; series pt4 |
| 8THSuqoPI_Q | StokedOnFishing | on-the-water | observations-only | pending | Catalina Isl + offshore bluefin footage; sponsor-heavy; Simrad Summer pt2 |
| -bw1KDfDjv4 | StokedOnFishing | on-the-water | parameter-skim | pending | SoCal offshore banks (14-mile bank); temp-break/kelp-paddy reading via electronics; sponsor-heavy; Simrad Summer pt1 |
| IwxqgocsQTY | StokedOnFishing | on-the-water | observations-only | pending | SoCal-to-Baja 8-day trip footage, mostly travel/banter; sponsor-heavy; Intrepid Style 8 Day pt1 |
| 97clKtVsEOs | StokedOnFishing | on-the-water | parameter-skim | pending | Benitos Isl/Alijos Rocks, Baja (region); anchor-vs-drift call via sounder, wahoo bomb-lure hookup logic; series pt2 |
| ilINTeknKB4 | StokedOnFishing | on-the-water | observations-only | pending | Benitos Isl, Baja (region); yellowtail/bluefin catch footage, noon-bite-timing note; series pt3 |
| _PGm-TlFU2A | StokedOnFishing | on-the-water | parameter-skim | pending | hook doctrine: thick-shank Mustad/VMC hold under heavy drag w/ light bait; #4-2 hooks, fly-line rig, 25-30lb fluoro |
| ZghZCFL6OZk | StokedOnFishing | on-the-water | skip:out-of-region | skipped | series: Stoked on Costa Rica part 3; Costa Rica out of region |
| HueC1KHrcVw | StokedOnFishing | on-the-water | parameter-skim | pending | series: Top Gun 80 Epic 5 Day part 1; bait-quality tell, 70-72F bluefin temp, yo-yo/dropper loop; generic landing logistics |
| i3qIAHW-SJc | StokedOnFishing | on-the-water | parameter-skim | pending | series: Top Gun 80 Epic 5 Day part 2; Cortez/Osborne banks; mono-to-fluoro knot + tag-end sinker rig demo |
| A6DJoXbID4c | StokedOnFishing | on-the-water | deep | pending | kelp-paddy pattern ep (pre-identified deep candidate): bird-reading, stay 100yd off patty, mackerel>sardine bait, jig selection |
| zQtExV8Z2eY | StokedOnFishing | on-the-water | parameter-skim | pending | trip-tips: 30lb mono/4ft 30lb fluoro topshot, 1/4oz slider+#2 hook+squid, fly-lined sardine |
| MUpvP-Yl2R0 | StokedOnFishing | on-the-water | observations-only | pending | sponsor-heavy Navico/Simrad electronics demo (buoy/radar/AIS); legal halibut 22in mentioned |
| AIHvJj-paoo | StokedOnFishing | on-the-water | parameter-skim | pending | sponsor-heavy Okuma Komodo 450 reel demo; trip-tips: downsize line, team chum, give space, watch surroundings |
| NEuoCgxjrhM | StokedOnFishing | promo | skip:promo | skipped | pure Komodo 450 reel product demo/highlight reel, no doctrine, 1:56 short |
| mG8ZZLFGlT8 | StokedOnFishing | on-the-water | observations-only | pending | series: Buena Vista Beach Resort part 3; East Cape Baja (Lighthouse Pt); marlin/dorado/wahoo/yellowfin catches |
| oadK6zIYyCo | StokedOnFishing | on-the-water | observations-only | pending | sponsor-heavy dealership ad x2; squid/sardine for calico; halibut catch-release |
| 3tQ1_xiqwVU | StokedOnFishing | on-the-water | parameter-skim | pending | series: Intrepid Long Range Sportfishing part 2; Baja Mag Bay/Alijos; yo-yo 180ft, kite/balloon 50lb rigs |
| XJaLubOVfvs | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Baja Mag Bay long-range trip intro; mostly boat/crew/food, thin fishing detail; cf. 3tQ1_xiqwVU |
| o1mJ5H8Np-s | StokedOnFishing | on-the-water | skip:thin-generic | skipped | pure catch montage (San Pablo yellowtail), no conditions/technique detail |
| 5LI0vPzlCUE | StokedOnFishing | on-the-water | skip:thin-generic | skipped | Alijos Rocks (far offshore Baja, edge-of-scope); pure catch montage, no doctrine |
| 0HILDC0ITLE | StokedOnFishing | on-the-water | skip:thin-generic | skipped | SoCal albacore catch footage; only generic line-in-front-of-you safety tip |
| 2TE46Hqoq5s | StokedOnFishing | promo | skip:promo | skipped | Intrepid boat/crew/food comfort testimonial ad; negligible actual fishing footage |
| ns992VlKpMc | StokedOnFishing | on-the-water | skip:thin-generic | skipped | near-silent Top Gun 80 yellowtail catch montage, almost no dialogue |
| RgtkbmBFUXI | StokedOnFishing | on-the-water | parameter-skim | pending | Guadalupe Island (Baja); 100lb leader on dropper loop near rocks, swings 120-250ft |
| 2K4urpo3q6Q | StokedOnFishing | on-the-water | observations-only | pending | dated observation: 15-18ft great white shark seen under boat |
| w37pHf0xjrw | StokedOnFishing | on-the-water | parameter-skim | pending | SoCal, 37mi off San Diego; torpedo sinker sizes, #2-3 hooks, light-line albacore rig |
| Bab_6o7JFh4 | Crust to Coast | seminar | parameter-skim | pending | Shelf/slope/abyssal provinces + euphotic/mesopelagic light zones, marine provinces -> conditions water-column and bathymetry |
| GIlM8fTmL5M | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: navigation history and bathymetric mapping techniques, no waves/tides/currents mechanism |
| d7IPkfjMZu8 | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: solar system/earth origin, mantle layers, isostasy, seismology; deep-time geology |
| SVLqaSa1bxU | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: continental drift, mantle convection, seamounts/hotspots; rock/plate-tectonics geology |
| 6pAmcsTtYGA | Crust to Coast | seminar | parameter-skim | pending | Salinity vs latitude/depth, dissolved gases, oxygen minimum layer and hypoxia -> conditions water-column |
| i4OB4G6_adI | Crust to Coast | seminar | parameter-skim | pending | Thermocline/pycnocline/mixed layer, density vs depth, sound channel, light penetration -> conditions water-column |
| OZejCm0ItEE | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: lithogenous/biogenous sediment classification, core sampling, paleoceanography |
| 32TQdFJKIlI | Crust to Coast | seminar | parameter-skim | pending | Gyres, Ekman transport, geostrophic flow, upwelling/downwelling, ENSO, kelp-productivity link -> conditions currents/upwelling |
| OEsW9K1IwpQ | Crust to Coast | seminar | parameter-skim | pending | Heat budget, Coriolis, wind belts, land/sea breezes, hurricane formation -> conditions wind-driven sea-state (cf dS0Y overlap) |
| dS0YUOyqN6g | Crust to Coast | seminar | parameter-skim | pending | Longer Oceans and Climate lecture, identical scripted intro to OEsW9K1IwpQ but diverges (albedo, Coriolis, winds) -> sea-state |
| RuNH5O9olfw | Crust to Coast | seminar | parameter-skim | pending | Surf zone/breaker/swash/berm zones, longshore sediment transport, beach types -> conditions nearshore processes |
| 9tTM99InluM | Crust to Coast | seminar | parameter-skim | pending | Lunar/solar tidal bulge mechanics, gravity, Bay of Fundy tidal range example -> conditions tides |
| rK1sWd84S04 | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: sea ice/glacial ice formation, cryosphere, brine rejection; no CA/Baja relevance |
| tKqZJZMLbq4 | Crust to Coast | seminar | parameter-skim | pending | Zooplankton/nekton types (copepods, krill, jellyfish), swimming modes, bioluminescence -> conditions food-web forage base |
| eg8IUjeWZx8 | Crust to Coast | seminar | parameter-skim | pending | Benthic habitat types, invertebrate dominance, coastal upwelling nutrients link -> conditions food-web and bottom structure |
| zvU45nkhhuE | Crust to Coast | seminar | parameter-skim | pending | Photosynthesis/phytoplankton base of food web; hydrothermal-vent chemosynthesis -> conditions food-web productivity |
| gT5g8Rhtpyg | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: life taxonomy/domains/kingdoms classification lecture, no conditions mechanism |
| 7jPK4aOctQo | Crust to Coast | non-fishing | skip:thin-generic | skipped | adjacent background: marine pollution types/sources, environmental-science survey |
| YGKgQp5HTLM | JoeWo | non-fishing | skip:not-fishing | skipped | JoeWo Warzone gaming aiming-guide video; unrelated to fishing (stray) |
| mwrFx2DdmO0 | Kevin Is Cooking | non-fishing | skip:no-usable-content | skipped | Kevin Is Cooking tacos al pastor; transcript is 3 useless lines, no content (stray) |
| 55IthpZZx9k | Okuma Fishing Tackle USA | promo | skip:promo | skipped | Okuma booth ad: Dave Hansen pitches Makaira 130 + PCH bent-butt rod for SoCal bluefin/swordfish; feeds dave-hansen registry |
<!-- batch2:worklist:end -->
