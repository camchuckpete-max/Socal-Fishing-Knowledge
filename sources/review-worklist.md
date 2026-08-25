# Review worklist

The editorial-review fleet's work queue (sources/plan-review.md). One row per
note; the sanctioned wrapper (scripts/review/commit-note.py) is the only
writer of status/flags/result cells. Status machine:
`pending -> transformed -> fact-checked -> done`, terminals
`skipped | escalated | reverted`; `light`-tier rows go straight
`pending -> done` at transform time. Gazetteer and cluster rows are appended
by their builders after the transform phase drains.

<!-- review:worklist:start -->
| note | tier | status | flags | result |
| --- | --- | --- | --- | --- |
| species/barracuda.md | full | transformed | gaps(8), misplaced(0), spots(14), reg-claims(1), fact-check(3), asr-uncertain(2) | transform verified, applied with 7 fixes: 1 invented tactic removed, 3 claim-inflations restated to source, 1 dropped before-claim restored under flag, 1 specific recovered |
| species/bluefin-tuna-trolling.md | full | transformed |  | retyped species-technique + reshaped to the v2.2 skeleton (supervised exemplar); cite conservation verified |
| species/bluefin-tuna.md | full | transformed | gaps(5), misplaced(1), spots(22), reg-claims(3), fact-check(4), zone-stubs(5), asr-uncertain(7) | escalate(apply): verified and applied with three fixes - conservation restoration (ouBrIdO7d4k), meaning-drift correction (HueC1KHrcVw temperature), cite-scoping (ftEvyfwjZFU red crab) |
| species/bonito.md | full | transformed | gaps(10), zone-stubs(7), fact-check(3), misplaced(1), spots(12), reg-claims(2), asr-uncertain(3) | transform verified and applied with date-attribution corrections; 162->272 lines + 207-line evidence file, 11 sources appended, 1 flagged stub resolved |
| species/cabrilla.md | full | pending |  |  |
| species/calico-bass.md | full | pending |  |  |
| species/california-halibut.md | full | pending |  |  |
| species/california-spiny-lobster.md | full | pending |  |  |
| species/dorado.md | full | pending |  |  |
| species/ocean-whitefish.md | full | pending |  |  |
| species/opah.md | full | pending |  |  |
| species/pacific-crevalle-jack.md | full | pending |  |  |
| species/rockfish-lingcod.md | full | pending |  |  |
| species/sand-bass.md | full | pending |  |  |
| species/sheephead.md | full | pending |  |  |
| species/skipjack-tuna.md | full | pending |  |  |
| species/snook.md | full | pending |  |  |
| species/spotted-bay-bass.md | full | pending |  |  |
| species/striped-marlin.md | full | pending |  |  |
| species/swordfish.md | full | pending |  |  |
| species/wahoo.md | full | pending |  |  |
| species/white-seabass.md | full | pending |  |  |
| species/yellowfin-tuna.md | full | pending |  |  |
| species/yellowtail.md | full | transformed | gaps(9) fc(1) ledger(4) misplaced(2) | feedback rework (2026-08-24): 563->423 lines, evidence 140->176; all 16 feedback items verified landed; 4 demotions to evidence; zone-guides section + Coronados link + 7 stubs; conservation clean after 3 verifier restorations; recommitted after guard protected-path churn fix |
| techniques/bait-and-switch.md | standard | pending |  |  |
| techniques/beach-lure-depth-control.md | standard | pending |  |  |
| techniques/cheater-troll.md | standard | pending |  |  |
| techniques/chunking.md | standard | pending |  |  |
| techniques/clearing-a-backlash.md | standard | pending |  |  |
| techniques/dart-jig-tuna.md | standard | pending |  |  |
| techniques/deep-drop-swordfishing.md | standard | pending |  |  |
| techniques/drop-shot.md | standard | pending |  |  |
| techniques/dropper-loop.md | standard | pending |  |  |
| techniques/fighting-big-bluefin.md | standard | pending |  |  |
| techniques/fighting-fish-from-the-rail.md | standard | pending |  |  |
| techniques/flat-fall-jigging.md | standard | pending |  |  |
| techniques/flyline.md | standard | pending |  |  |
| techniques/foamer-casting.md | standard | pending |  |  |
| techniques/glide-baits.md | standard | pending |  |  |
| techniques/hoop-netting.md | standard | pending |  |  |
| techniques/inshore-crankbaits.md | standard | pending |  |  |
| techniques/kayak-bass-fishing.md | standard | pending |  |  |
| techniques/kite-fishing.md | standard | pending |  |  |
| techniques/knife-jigging.md | standard | pending |  |  |
| techniques/leadhead-swimbait-retrieve.md | standard | pending |  |  |
| techniques/live-bait-pendulum-cast.md | standard | pending |  |  |
| techniques/mangrove-structure-livebait.md | standard | pending |  |  |
| techniques/ned-rig.md | standard | pending |  |  |
| techniques/night-bass-fishing.md | standard | pending |  |  |
| techniques/panga-team-trolling.md | standard | pending |  |  |
| techniques/rail-etiquette.md | standard | pending |  |  |
| techniques/rockfish-deep-dropping.md | standard | pending |  |  |
| techniques/rod-handling-live-bait.md | standard | pending |  |  |
| techniques/skip-jigging.md | standard | pending |  |  |
| techniques/sliding-sinker.md | standard | pending |  |  |
| techniques/slow-pitch-jigging.md | standard | pending |  |  |
| techniques/slow-trolling-bait.md | standard | pending |  |  |
| techniques/speed-trolling.md | standard | pending |  |  |
| techniques/spinnerbaits.md | standard | pending |  |  |
| techniques/spinning-reel-wind-knots.md | standard | pending |  |  |
| techniques/surface-iron-casting.md | standard | pending |  |  |
| techniques/surface-iron-color.md | standard | pending |  |  |
| techniques/surface-iron.md | standard | transformed | misplaced(1) spots(10) | faithful transform 654->512 lines + 77-line evidence: blockquotes to prose, source-scoped headings dissolved, 2 legacy cites transcript-verified; 2 verifier fixes (cite-scope split, harvest-row cite) |
| techniques/swimbaits.md | standard | pending |  |  |
| techniques/trolling.md | standard | pending |  |  |
| techniques/tube-bait-fishing.md | standard | pending |  |  |
| techniques/two-speed-low-gear-fight.md | standard | pending |  |  |
| techniques/underhand-casting.md | standard | pending |  |  |
| techniques/wacky-rig.md | standard | pending |  |  |
| techniques/wahoo-bomb-casting.md | standard | pending |  |  |
| techniques/wahoo-trolling.md | standard | pending |  |  |
| techniques/wind-in-your-face-positioning.md | standard | pending |  |  |
| techniques/yo-yo-iron.md | standard | pending |  |  |
| lures/bay-bass-plastics.md | standard | pending |  |  |
| lures/cedar-plug.md | standard | pending |  |  |
| lures/crocodile-spoons.md | standard | pending |  |  |
| lures/dtx-minnow.md | standard | pending |  |  |
| lures/halco-laser-pro.md | standard | pending |  |  |
| lures/iron-jigs.md | standard | pending |  |  |
| lures/jerkbaits.md | standard | pending |  |  |
| lures/knife-jigs.md | standard | pending |  |  |
| lures/lucky-craft-flash-minnow.md | standard | pending |  |  |
| lures/mad-mac.md | standard | pending |  |  |
| lures/rapala-husky-magnum.md | standard | pending |  |  |
| lures/soft-plastic-swimbaits.md | standard | pending |  |  |
| lures/spreader-bar.md | standard | pending |  |  |
| lures/tube-baits.md | standard | pending |  |  |
| lures/tuna-feathers-and-skirts.md | standard | pending |  |  |
| lures/tuna-poppers-and-stickbaits.md | standard | pending |  |  |
| rigging/assist-hooks.md | standard | pending |  |  |
| rigging/bimini-twist.md | standard | pending |  |  |
| rigging/bite-leaders.md | standard | pending |  |  |
| rigging/crimping.md | standard | pending |  |  |
| rigging/cut-loop-dropper.md | standard | pending |  |  |
| rigging/double-trouble-rig.md | standard | pending |  |  |
| rigging/dropper-loop-knot-and-spider-hitch.md | standard | pending |  |  |
| rigging/essential-knots.md | standard | pending |  |  |
| rigging/fg-and-albright.md | standard | pending |  |  |
| rigging/flying-fish-harness.md | standard | pending |  |  |
| rigging/haywire-twist.md | standard | pending |  |  |
| rigging/hollow-splice-and-serving.md | standard | pending |  |  |
| rigging/improved-clinch-knot.md | standard | pending |  |  |
| rigging/john-collins-knot.md | standard | pending |  |  |
| rigging/leadhead-mods.md | standard | pending |  |  |
| rigging/perfection-loop-knot.md | standard | pending |  |  |
| rigging/pr-knot.md | standard | pending |  |  |
| rigging/rp-knot.md | standard | pending |  |  |
| rigging/rubber-band-deep-rig.md | standard | pending |  |  |
| rigging/san-diego-jam-knot.md | standard | pending |  |  |
| rigging/san-diego-jam-single-vs-double.md | standard | pending |  |  |
| rigging/seaguar-knot.md | standard | pending |  |  |
| rigging/slim-beauty-knot.md | standard | pending |  |  |
| rigging/springer-knot.md | standard | pending |  |  |
| rigging/surgeons-knot-mono-to-fluoro.md | standard | pending |  |  |
| rigging/surgeons-loop.md | standard | pending |  |  |
| rigging/tony-pena-knot.md | standard | pending |  |  |
| rigging/trap-rig.md | standard | pending |  |  |
| rigging/tuna-feather-rig.md | standard | pending |  |  |
| rigging/wind-on-leader.md | standard | pending |  |  |
| rigging/wiring-a-surface-iron.md | standard | pending |  |  |
| conditions/bird-reading.md | standard | pending |  |  |
| conditions/current-diagnostics.md | standard | pending |  |  |
| conditions/current-structure.md | standard | pending |  |  |
| conditions/deep-scattering-layer.md | standard | pending |  |  |
| conditions/kelp-paddies.md | standard | pending |  |  |
| conditions/moon.md | standard | pending |  |  |
| conditions/sea-state.md | standard | pending |  |  |
| conditions/tide-and-slack.md | standard | pending |  |  |
| conditions/upwelling-and-turnover.md | standard | pending |  |  |
| conditions/water-color.md | standard | pending |  |  |
| conditions/water-regimes.md | standard | pending |  |  |
| conditions/water-temperature.md | standard | pending |  |  |
| seasonal/april.md | standard | pending |  |  |
| seasonal/august.md | standard | pending |  |  |
| seasonal/february-march.md | standard | pending |  |  |
| seasonal/june-july.md | standard | pending |  |  |
| seasonal/may.md | standard | pending |  |  |
| seasonal/november-december.md | standard | pending |  |  |
| seasonal/october.md | standard | pending |  |  |
| seasonal/september.md | standard | pending |  |  |
| seasonal/year-anniversary-prior.md | standard | pending |  |  |
| bait/bait-tanks.md | standard | pending |  |  |
| bait/fishing-live-bait.md | standard | pending |  |  |
| bait/making-bait.md | standard | pending |  |  |
| locations/bahia-de-los-angeles.md | standard | pending |  |  |
| locations/bahia-magdalena-lopez-mateos.md | standard | pending |  |  |
| locations/bass-structure.md | standard | pending |  |  |
| locations/bays-and-harbors.md | standard | pending |  |  |
| locations/bight-geography.md | standard | pending |  |  |
| locations/bightsst-eval-targets.md | standard | pending |  |  |
| locations/breakwalls-jetties-riprap.md | standard | pending |  |  |
| locations/cedros-island.md | standard | pending |  |  |
| locations/island-structure.md | standard | pending |  |  |
| locations/loreto.md | standard | pending |  |  |
| locations/regions.md | standard | pending |  |  |
| locations/sea-of-cortez.md | standard | pending |  |  |
| locations/zone-lexicon.md | standard | pending |  |  |
| planning/day-plan-protocol.md | light | pending |  |  |
| planning/electronics-and-sounder.md | light | pending |  |  |
| planning/fleet-intelligence.md | light | pending |  |  |
| planning/report-reading-and-forecasting.md | light | pending |  |  |
| planning/search-and-glassing.md | light | pending |  |  |
| planning/trip-length-selection.md | light | pending |  |  |
| fish-care/dehooking-and-release.md | light | pending |  |  |
| fish-care/dorado-and-general.md | light | pending |  |  |
| fish-care/gaffing.md | light | pending |  |  |
| fish-care/ikejime.md | light | pending |  |  |
| fish-care/sculpin-handling.md | light | pending |  |  |
| fish-care/tuna-care.md | light | pending |  |  |
| fish-care/wahoo-handling.md | light | pending |  |  |
| tackle/all-purpose-rod-line-rating.md | light | pending |  |  |
| tackle/bluefin-50-80lb-bait-outfit-ladder.md | light | pending |  |  |
| tackle/bluefin-retail-setup-high-end-vs-budget.md | light | pending |  |  |
| tackle/bluefin-rig-ladder-by-grade.md | light | pending |  |  |
| tackle/composite-rod-blank-construction.md | light | pending |  |  |
| tackle/drag-setting.md | light | pending |  |  |
| tackle/gear-classes.md | light | pending |  |  |
| tackle/hook-assortment-by-trip-length.md | light | pending |  |  |
| tackle/hooks.md | light | pending |  |  |
| tackle/jig-rod-rating-selection.md | light | pending |  |  |
| tackle/jigging-rod-guide-wrap.md | light | pending |  |  |
| tackle/lightweight-reel-pick-turners-outdoorsman.md | light | pending |  |  |
| tackle/line-and-leader.md | light | pending |  |  |
| tackle/offset-hooks.md | light | pending |  |  |
| tackle/reel-maintenance.md | light | pending |  |  |
| tackle/rod-action-testing-technique.md | light | pending |  |  |
| tackle/rod-and-reel-selection.md | light | pending |  |  |
| tackle/rod-blank-and-component-materials.md | light | pending |  |  |
| tackle/rod-length-for-angler-size.md | light | pending |  |  |
| tackle/searcher-30lb-large-tuna-outfit.md | light | pending |  |  |
| tackle/searcher-40lb-all-around-tuna-outfit.md | light | pending |  |  |
| tackle/searcher-50-60-80lb-flyline-outfit.md | light | pending |  |  |
| tackle/searcher-6-to-8-day-heavy-outfit.md | light | pending |  |  |
| tackle/searcher-alijos-rocks-ridge-7-day-quiver.md | light | pending |  |  |
| tackle/searcher-big-tuna-rig-ladder.md | light | pending |  |  |
| tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md | light | pending |  |  |
| tackle/searcher-daytime-dart-jig-outfit-ladder.md | light | pending |  |  |
| tackle/searcher-finesse-live-bait-outfit.md | light | pending |  |  |
| tackle/searcher-four-outfit-guadalupe-quiver.md | light | pending |  |  |
| tackle/searcher-lever-drag-reel-sizing.md | light | pending |  |  |
| tackle/searcher-rail-rod-ladder.md | light | pending |  |  |
| tackle/searcher-spring-bluefin-yellowtail-quiver.md | light | pending |  |  |
| tackle/searcher-three-outfit-minimum-quiver.md | light | pending |  |  |
| tackle/searcher-yellowtail-livebait-sliding-sinker-rig.md | light | pending |  |  |
| tackle/spectra-hollow-vs-solid.md | light | pending |  |  |
| tackle/spinning-reel-bait-feeder.md | light | pending |  |  |
| tackle/spooling-line-tension-and-twist.md | light | pending |  |  |
| tackle/star-drag-vs-lever-drag.md | light | pending |  |  |
| tackle/tackle-express-accurate-tern-2-reel.md | light | pending |  |  |
| tackle/tackle-express-accurate-valiant-2-spj-reel.md | light | pending |  |  |
| tackle/tackle-express-bait-tank-time-saver.md | light | pending |  |  |
| tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md | light | pending |  |  |
| tackle/tackle-express-baja-light-setup-yellowtail-insurance.md | light | pending |  |  |
| tackle/tackle-express-bates-edc-100-reel.md | light | pending |  |  |
| tackle/tackle-express-bkk-titan-diver-swimbait-hooks.md | light | pending |  |  |
| tackle/tackle-express-casting-reel-for-seabass-yellowtail.md | light | done |  | light transform verified: style/cites/structure only, full conservation, check-note OK |
| tackle/tackle-express-cedros-four-rod-quiver.md | light | pending |  |  |
| tackle/tackle-express-chad-fathom-lowprofile-surf-combo.md | light | pending |  |  |
| tackle/tackle-express-charter-bait-tank-hook-kit.md | light | pending |  |  |
| tackle/tackle-express-ci4-plus-reel-features.md | light | pending |  |  |
| tackle/tackle-express-daiwa-coastal-tw200-reel.md | light | pending |  |  |
| tackle/tackle-express-daiwa-luvias-st-spinning-reel.md | light | pending |  |  |
| tackle/tackle-express-daiwa-saltiga-reel.md | light | pending |  |  |
| tackle/tackle-express-daiwa-saltist-sd-reel.md | light | pending |  |  |
| tackle/tackle-express-fast-tip-for-finicky-bite-drag-drift.md | light | pending |  |  |
| tackle/tackle-express-fish-kicker-quick-clip-surf-bait.md | light | pending |  |  |
| tackle/tackle-express-how-co-split-ring-pliers.md | light | pending |  |  |
| tackle/tackle-express-icast2022-penn-fathom2-authority.md | light | pending |  |  |
| tackle/tackle-express-izorline-xxx-mono.md | light | pending |  |  |
| tackle/tackle-express-jig-stick-trolling-outfit.md | light | pending |  |  |
| tackle/tackle-express-maxcuatro-vs-depth-hunter-offshore.md | light | pending |  |  |
| tackle/tackle-express-maxima-shark-tooth-leader-tool.md | light | pending |  |  |
| tackle/tackle-express-minnow-rod.md | light | pending |  |  |
| tackle/tackle-express-mustad-heavy-duty-pliers.md | light | pending |  |  |
| tackle/tackle-express-night-bluefin-tg-jig-rig.md | light | pending |  |  |
| tackle/tackle-express-penn-handle-knob-replacement.md | light | pending |  |  |
| tackle/tackle-express-penn-pull-to-turn-preset-drag.md | light | pending |  |  |
| tackle/tackle-express-penn-vs-avet-lever-drag.md | light | pending |  |  |
| tackle/tackle-express-phenix-axis-rockfish-rod.md | light | pending |  |  |
| tackle/tackle-express-premade-rock-cod-rig.md | light | pending |  |  |
| tackle/tackle-express-rockfish-leader-line.md | light | pending |  |  |
| tackle/tackle-express-saltiga-300-round-jigging-reel.md | light | pending |  |  |
| tackle/tackle-express-saltiga-35-vs-talica-12-reel-sizing.md | light | pending |  |  |
| tackle/tackle-express-savage-gear-line-thru-swimbait-rigging.md | light | pending |  |  |
| tackle/tackle-express-shimano-nasci-fc-reel.md | light | pending |  |  |
| tackle/tackle-express-shimano-sedona-reel-features.md | light | pending |  |  |
| tackle/tackle-express-shimano-talica-reel-features.md | light | pending |  |  |
| tackle/tackle-express-shimano-tranx-300b-body-gearing-and-model-lineup.md | light | pending |  |  |
| tackle/tackle-express-shimano-tranx-300b-braking-system.md | light | pending |  |  |
| tackle/tackle-express-shimano-tranx-300b-x-protect-water-resistance.md | light | pending |  |  |
| tackle/tackle-express-shimano-vanford-fa-reel.md | light | pending |  |  |
| tackle/tackle-express-shogun-maxcuatro-braid.md | light | pending |  |  |
| tackle/tackle-express-speedmaster-fathom-reel-sizing.md | light | pending |  |  |
| tackle/tackle-express-surf-halibut-rod-lineup.md | light | pending |  |  |
| tackle/tackle-express-trophy-bluefin-jig-outfit.md | light | pending |  |  |
| tackle/tackle-express-white-seabass-rod-reel-line.md | light | pending |  |  |
| species/yellowtail-coronado-islands.md | standard | transformed | gaps(4) spots(2) | zone-guide exemplar: nate program + Coronados corpus, corpus-only verified with 11 timestamped spot-checks; name-cites stripped per v2.1 |
| species/yellowtail-surface-iron.md | standard | transformed |  | spun out of the yellowtail router + surface-iron (supervised exemplar); paired cite conservation verified |
| locations/mexican-waters.md | geo | transformed |  | jurisdiction exemplar (supervised); absorbed the relocated Mexico paperwork |
| locations/coronado-islands.md | geo | transformed |  | zone exemplar (supervised); 11 charted spots, gives the zone guide a real zone link |
| locations/pukey-point.md | gazetteer | transformed |  | minimum spot exemplar (supervised); coordinates + parent zone + flagged gaps |
| locations/ribbon-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lighthouse.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/5-minute-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/south-kelp-ridge.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/rockpile.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lower-9-mile-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/coronado-canyon.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/north-of-north-island-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-of-pukey-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/middle-grounds.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/farnsworth-bank.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/pyramid-head.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/mackerel-bank.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/desperation-reef.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/14-mile-bank.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/43.md | gazetteer | pending |  | corpus material harvested — fleet writes this one |
| locations/us-waters.md | geo | transformed |  | jurisdiction page written from 8 corpus sources; verified, 4 style/scope fixes applied; 4 gaps flagged |
| locations/socal-bight.md | geo | transformed | gaps:5 stubs:18 | region page, 41/41 census zones; verified with 5 fixes (cite rescope, compass fix, obs scoping, evidence pair) |
| locations/baja-pacific-north.md | geo | transformed |  | region page from 26 sources, 28/28 census zones; verified with 3 fixes (mis-cite re-sourced, unsupported descriptor, over-scoped caution) |
| locations/baja-pacific-south.md | geo | transformed |  | region page from 25 sources, 3/3 census zones (coordinate-less); verified with 4 fixes; La Bocana flagged as possible missing census zone |
| locations/cortez-north.md | geo | transformed |  | one-zone region page from BOLA/San Felipe/Gonzaga corpus, no charted coords; verified with 6 fixes; 3 zone stubs flagged |
| locations/cortez-south.md | geo | pending |  | region |
| locations/catalina-island-front-side.md | geo | pending |  | zone: 40 spots, 25 notes |
| locations/north-county-artificial-reefs.md | geo | pending |  | zone: 38 spots, 0 notes |
| locations/catalina-island-backside.md | geo | pending |  | zone: 21 spots, 25 notes |
| locations/san-diego-artificial-reefs.md | geo | pending |  | zone: 18 spots, 1 notes |
| locations/oceanside-north-county.md | geo | pending |  | zone: 18 spots, 8 notes |
| locations/la-jolla.md | geo | pending |  | zone: 14 spots, 11 notes |
| locations/point-loma.md | geo | pending |  | zone: 12 spots, 6 notes |
| locations/punta-banda-santo-tomas.md | geo | pending |  | zone: 12 spots, 2 notes |
| locations/san-clemente-island-back-side.md | geo | pending |  | zone: 12 spots, 30 notes |
| locations/san-nicolas-island.md | geo | pending |  | zone: 10 spots, 2 notes |
| locations/dana-point.md | geo | pending |  | zone: 9 spots, 15 notes |
| locations/san-quintin.md | geo | pending |  | zone: 8 spots, 2 notes |
| locations/santa-barbara-island.md | geo | pending |  | zone: 8 spots, 15 notes |
| locations/international-artificial-reef.md | geo | pending |  | zone: 7 spots, 1 notes |
| locations/san-clemente-island-front-side.md | geo | pending |  | zone: 7 spots, 30 notes |
| locations/rosarito-descanso.md | geo | pending |  | zone: 6 spots, 0 notes |
| locations/la-fonda-bajamar-salsipuedes.md | geo | pending |  | zone: 5 spots, 0 notes |
| locations/finger-bank-rockfish.md | geo | pending |  | zone: 5 spots, 1 notes |
| locations/1010-trench-378-213.md | geo | pending |  | zone: 5 spots, 0 notes |
| locations/imperial-beach.md | geo | pending |  | zone: 4 spots, 3 notes |
| locations/ensenada.md | geo | pending |  | zone: 4 spots, 21 notes |
| locations/colonet.md | geo | pending |  | zone: 4 spots, 5 notes |
| locations/davis-knoll-san-miguel-gap-rodriguez-seamount.md | geo | pending |  | zone: 4 spots, 0 notes |
| locations/corner-140-182.md | geo | pending |  | zone: 4 spots, 13 notes |
| locations/coronados-230-302-226.md | geo | pending |  | zone: 4 spots, 21 notes |
| locations/upper-cross-421-390.md | geo | pending |  | zone: 4 spots, 0 notes |
| locations/pistol-bell-bank-300.md | geo | pending |  | zone: 4 spots, 1 notes |
| locations/385-238-475.md | geo | pending |  | zone: 4 spots, 0 notes |
| locations/372-245-250.md | geo | pending |  | zone: 4 spots, 3 notes |
| locations/south-orange-county-crystal-cove.md | geo | pending |  | zone: 3 spots, 0 notes |
| locations/172-125.md | geo | pending |  | zone: 3 spots, 1 notes |
| locations/slide-152-277.md | geo | pending |  | zone: 3 spots, 4 notes |
| locations/51-181-138.md | geo | pending |  | zone: 3 spots, 3 notes |
| locations/81-381.md | geo | pending |  | zone: 3 spots, 1 notes |
| locations/43-91-300.md | geo | pending |  | zone: 3 spots, 14 notes |
| locations/w-butterfly-157.md | geo | pending |  | zone: 3 spots, 0 notes |
| locations/upper-500-hidden-bank.md | geo | pending |  | zone: 3 spots, 0 notes |
| locations/baja-270-double-220-295.md | geo | pending |  | zone: 3 spots, 94 notes |
| locations/483-500-437.md | geo | pending |  | zone: 3 spots, 2 notes |
| locations/1140-finger-450.md | geo | pending |  | zone: 3 spots, 0 notes |
| locations/baja-230-peanut-bank-60.md | geo | pending |  | zone: 3 spots, 94 notes |
| locations/sniffer-west-400-300.md | geo | pending |  | zone: 3 spots, 9 notes |
| locations/179-220.md | geo | pending |  | zone: 3 spots, 0 notes |
| locations/lower-cross.md | geo | pending |  | zone: 3 spots, 0 notes |
| locations/boot-504-307.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/hidden-reef-170.md | geo | pending |  | zone: 2 spots, 1 notes |
| locations/la-270-286.md | geo | pending |  | zone: 2 spots, 24 notes |
| locations/kidney-bank-63-175.md | geo | pending |  | zone: 2 spots, 1 notes |
| locations/279-267-14-mile-bank.md | geo | pending |  | zone: 2 spots, 7 notes |
| locations/474-711.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/209-312.md | geo | pending |  | zone: 2 spots, 7 notes |
| locations/289-284.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/north-9-mile-bank-178.md | geo | pending |  | zone: 2 spots, 2 notes |
| locations/south-9-mile-bank-439.md | geo | pending |  | zone: 2 spots, 1 notes |
| locations/e-butterfly-san-salvador-knoll.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/101-425.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/475-knuckle-upper-finger-bank.md | geo | pending |  | zone: 2 spots, 1 notes |
| locations/banda-bank-todos-santos-island.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/311.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/sverdrup-bank-126.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/tanner-bank.md | geo | pending |  | zone: 2 spots, 10 notes |
| locations/hancock-bank.md | geo | pending |  | zone: 2 spots, 0 notes |
| locations/12-mile-reef.md | geo | pending |  | zone: 1 spots, 0 notes |
| locations/san-juan-seamount.md | geo | pending |  | zone: 1 spots, 0 notes |
| locations/bumps.md | geo | pending |  | zone: 1 spots, 2 notes |
| locations/380.md | geo | pending |  | zone: 1 spots, 0 notes |
| locations/guadalupe.md | geo | pending |  | zone: 0 spots, 28 notes |
| locations/alijos-rocks.md | geo | pending |  | zone: 0 spots, 18 notes |
| locations/cabo-san-lucas.md | geo | pending |  | zone: 0 spots, 4 notes |
| locations/la-paz.md | geo | pending |  | zone: 0 spots, 5 notes |
| locations/east-cape.md | geo | pending |  | zone: 0 spots, 11 notes |
<!-- review:worklist:end -->
