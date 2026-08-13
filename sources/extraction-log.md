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
