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
| locations/bahia-de-los-angeles.md | geo | transformed | gaps:12 stubs:3 fc:2 spots:5 | zone page under cortez-north from 9 corpus sources + cameron; retyped location->zone on the v2 skeleton, 0 charted spots so no child pages; K22a8Ui8tWg re-scoped out (San Felipe mothership, kept in evidence), roosterfish 'more reliable further south' escalation corrected to what P36VGPPf120 actually says, 20-miles-north cite corrected; 12 gaps, 3 stubs, 2 fact-check rows, 5 spot-harvest rows |
| locations/bahia-magdalena-lopez-mateos.md | geo | transformed | gaps:11 stubs:3 fc:3 spots:6 | zone page under baja-pacific-south from 12 corpus sources; retyped location->zone on the v2 skeleton, 0 charted spots so no child pages; pulled in the Mag Bay material that had only lived in flyline/trolling/yo-yo/kite/marlin/wahoo notes (mangrove tide windows, estuary channel depth, Ridge-vs-Modesto-Main bank choice, untapped jig fishery), retired the promotional-seminar attribution preambles into the evidence file, kept the two season claims side by side with a decision frame; 11 gaps, 3 stubs, 3 fact-check rows, 6 spot-harvest rows |
| locations/bass-structure.md | standard | pending |  |  |
| locations/bays-and-harbors.md | standard | pending |  |  |
| locations/bight-geography.md | standard | pending |  |  |
| locations/bightsst-eval-targets.md | standard | pending |  |  |
| locations/breakwalls-jetties-riprap.md | standard | pending |  |  |
| locations/cedros-island.md | geo | transformed | gaps:12 stubs:3 fc:1 | zone page (was type: location) from 44 sources, census zone 'Cedros / San Benitos'; no charted spots in the library; absorbed the queued Yellow Tail triangle geography; evidence file carries 44 observation lines and the Tackle Express gear cross-links |
| locations/island-structure.md | standard | pending |  |  |
| locations/loreto.md | geo | transformed | gaps:17 stubs:4 fc:2 spots:7 | zone page under cortez-south from 5 Loreto trip vlogs + P36VGPPf120 for the roosterfish contrast; retyped location->zone on the v2 skeleton, 0 charted spots so no child pages; added bank to waters for Six Mile Reef, dropped the uncited '250 miles south of BOLA' distance, split every trip observation into the new evidence file and retired the confidence/channel boilerplate into it; new material mined from the transcripts (Puerto Escondido launch, mothership/beach/panga access modes, bait-vendor sardine rig and dorado window, 20-mile/1-hour Carmen run, breakdown-and-tow, plumas troll, marlin… |
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
| locations/cortez-south.md | geo | transformed |  | region page from 19 sources, 3/3 census zones, no coords; verified with 5 fixes incl. one fabricated fight detail corrected |
| locations/catalina-island-front-side.md | geo | transformed |  | zone page from 16 sources + spot library, 40/40 census spots; verified with 6 fixes (census count, Avalon Bank added, wind/report drift, mis-cite) |
| locations/north-county-artificial-reefs.md | geo | transformed |  | thin-corpus zone page, 38 spots, doctrine routed to chunking; verified with 11 fixes; 1 fact-check row queued |
| locations/catalina-island-backside.md | geo | transformed | gaps:6 spots:21 | zone page written: 5 skeleton sections + closure table + evidence pair; 21 spots grouped W->E; 6 flagged gaps |
| locations/san-diego-artificial-reefs.md | geo | transformed | gaps:10 stubs:3 spots:18 | zone page written: 5 skeleton sections + MPA caution + evidence pair; 18 spots in 3 groups (Torrey Pines, Pacific Beach grid, Mission Bay Park); 10 gaps, 3 stubs |
| locations/oceanside-north-county.md | geo | transformed | gaps:8 stubs:2 spots:18 | zone page written: 5 skeleton sections + evidence pair; 18 spots in 5 coastal groups; 8 gaps, 2 zone-guide stubs, Flat Rock naming collision logged |
| locations/la-jolla.md | geo | transformed | gaps:5 stubs:1 spots:14 | zone page written: 5 skeleton sections + MPA edge table + evidence pair; 14 spots in 5 groups (canyon, shelf, north-end reef, beach, rockfish ground); the NW Corner yellowtail/sounder program and the 180-210 ft shelf rockfish drift are the two real fisheries; 5 gaps, 1 zone-guide stub |
| locations/point-loma.md | geo | transformed | gaps:5 stubs:2 spots:12 | zone page written: 5 skeleton sections + evidence pair; 12 spots in 4 groups (Sunset Cliffs face, the pipe, south of the point, bay entrance + Coronado); no MPA labels in the library; corpus is type-example only (named kelp bed, coastal pipe, Zuniga Jetty in a wall list), so 5 gaps and 2 zone-guide stubs; the two 'off Point Loma' bluefin catches labelled as offshore landmark references, not zone fishing |
| locations/punta-banda-santo-tomas.md | geo | transformed | gaps:7 stubs:1 spots:12 | zone page written from the spot library + regional doctrine: 5 skeleton sections + evidence pair; 12 spots in 2 groups (7 named coastal features, 5 fathom-named high spots); corpus carries no trip here, so 7 gaps + 1 zone-guide stub + 1 show-floor La Bufadora trace in evidence |
| locations/san-clemente-island-back-side.md | geo | transformed | gaps:7 stubs:3 spots:12 | zone page written: 5 skeleton sections + naval-security-zone access row + evidence pair; 12 spots in 3 groups (NW end, mid back side, SE/east end); the east-end squid yellowtail fishery and the late-fall into-island off-colour bass/bonito pattern are the two documented programs; Desperation Reef 'West End tuna zone' naming discrepancy flagged; China Point / West Cove name collisions with Catalina noted; 7 gaps, 3 zone-guide stubs |
| locations/san-nicolas-island.md | geo | transformed | gaps:7 stubs:3 spots:10 | zone page written: 5 skeleton sections + evidence pair; 10 spots in 4 groups (east end, Daytona stretch, named shore features, 2 census-assigned outer banks); the July white seabass window and the August/September bluefin ground are the two documented fisheries; weather-gating and thin fleet coverage carried as the zone's two defining constraints; 7 gaps, 3 zone-guide stubs; Potato Bank (17.5 nm) and Cherry Banks (20.3 nm) parent-distance outliers left as queued, no access/closure rule for the island anywhere in the corpus |
| locations/dana-point.md | geo | transformed | gaps:5 stubs:3 spots:9 | zone page written: 5 skeleton sections + evidence pair; 9 spots in 5 groups (the 100-fathom edge, Monarch/Salt Creek, harbour kelp, San Clemente city stretch, south end); the zone doubles as a port — the 6:00 a.m. fleet/barge clock and the northern paddy limit are its two Bight-level facts; documented fisheries are the July kelp bass/barracuda session and the bonito troll either side of the harbour mouth, plus the kayak-guide inshore program; 'San Clemente (mainland city)' vs San Clemente Island naming collision logged; 5 gaps, 3 zone-guide stubs |
| locations/san-quintin.md | geo | transformed | gaps:9 stubs:2 spots:8 | zone page written from the spot library + 4 corpus sources: 5 skeleton sections + evidence pair; 8 spots in 3 groups (San Martin Island anchorage/kelp, the coastal run south — Roca Ben, 6.5 and 15 fathom spots, Breakers Reef — and 2 census-assigned outliers, Tranquillo Kelp at 15.8 nm and the numbered bank 304); two documented fisheries — January 2021 bluefin schools just outside San Martin in 63-65 F that stuck with the boat but bit poorly, and the big-calico coast south of the island fished off the Shogun with skiffs; Dono and Sacramento Reef carried in prose as fished-but-uncharted stops… |
| locations/santa-barbara-island.md | geo | transformed | gaps:5 stubs:4 spots:8 | zone page written: 5 skeleton sections + MPA line + evidence pair; 8 spots in 4 groups (west-end boilers, east end incl. the Cave Canyon WSB zone and its MPA line, south end/Sutil, and census-assigned Osborn Bank at 6.1 nm); documented fisheries are the March 2012 wide-open calico bite, the November 2014 tournament-winning kelp/rock day, the July 2017 squid rockfish/yellowtail anchor session in ~102 ft, and two bluefin grounds (NE of the island on the kite, Osborn Bank graylight in 70-72 F); swell-gating and thin fleet coverage carried as the zone's two constraints; 5 gaps, 4 stubs (white… |
| locations/international-artificial-reef.md | geo | transformed | gaps:11 stubs:3 fc:0 spots:7 | new zone page under socal-bight: 7 charted waypoints (International Reef A-F + Missile Tower), no corpus source names the reef so the page carries the SoCal artificial-reef program (chunking doctrine, 8 sources) applied to it, the coordinate geometry from the library, and the border/jurisdiction caution; 11 gaps, 3 stubs, evidence file created; spot pages left to the gazetteer phase (series-vs-waypoint publish shape is the open escalation) |
| locations/san-clemente-island-front-side.md | geo | transformed | gaps:8 stubs:4 fc:1 spots:7 | zone page written: 5 skeleton sections + evidence pair; 7 spots in 4 groups (Northwest Harbor, mid-side rocks, the Pyramid end, attached Mackerel Bank); the documented program is the morning yellowtail window fading to a bass/barracuda/bonito pick day, plus the 6 ft shallow-rock calico game inside Northwest Harbor; Northwest Harbor's naval-security-zone label vs corpus footage of boats fishing it flagged to the ledger; White Rock name collision with Punta Banda noted; 8 gaps, 1 species stub, 3 zone-guide stubs |
| locations/rosarito-descanso.md | geo | transformed | gaps:8 stubs:3 spots:6 | new zone page under baja-pacific-north (split of the spot library Northern Baja section); corpus carries ZERO notes on this stretch, so it is a position-and-ladder page built from the 6 charted spots (cameron) plus the census: Bull Ring as the 14.0 nm parent-distance outlier at the border, Rosarito Flats logged as a big area, and the 4-spot Descanso cluster inside two minutes of latitude; only species signal is the two Descanso rockfish labels; 8 gaps, 3 stubs, 0 child pages until the gazetteer runs |
| locations/la-fonda-bajamar-salsipuedes.md | geo | transformed | gaps:11 stubs:4 spots:5 | new zone page under baja-pacific-north, southern half of the Northern Baja section split; 5 charted spots (Punta Mesquite, La Fonda, Bajamar, Punta Salsipuedes + the 97 bank attached from the offshore-banks catch-all) and ZERO corpus notes describing any of them, so it is a position-and-ladder page: coordinate geometry in minutes of lat/lon, the two-pair grouping with an 8-minute empty gap, the 97's fathom-name depth reading via zone-lexicon (Rf1HKJG-SDg), Ensenada named as nearest corpus port with the no-source-says-so flag, and the explicit note that the region's year-round yellowtail… |
| locations/finger-bank-rockfish.md | geo | transformed | gaps:9 stubs:1 spots:5 | new zone page under baja-pacific-north for the spot library's Finger Bank rockfish section (5 charted spots, cameron); position-and-ladder page — no corpus source describes fishing any mark. Built the depth ladder from the labels at six feet to a fathom (Rf1HKJG-SDg): 27 fa/162 ft, 180, 240, 300, 71 fa/426 ft, deepening north-to-south and west across the western four with the 27 Fathom Spot 3.2' of longitude east as the shoreward outlier. Flagged the name-vs-position mismatch (the charted Upper Finger Bank and 475 Knuckle sit 7-10' of latitude south and 3-7' east, in a different zone).… |
| locations/1010-trench-378-213.md | geo | transformed |  | geo zone page verified — coordinates, distances and clustering reproduce from census/spot library; 2 cite-hygiene fixes applied |
| locations/imperial-beach.md | geo | transformed | gaps:8 stubs:3 fc:0 spots:4 | new zone page under socal-bight: 4 charted spots (two kelp marks, the flats, the pipe) at the south end of the US mainland coast; corpus carries three on-camera ties — the Point Loma-to-Imperial Beach structure field and its sounder-search program (kwMIgkCtFUE), the 'Imperial pipe' named among the coast's larger sewer pipes with asr-uncertainty against the Buccaneer Pipe (Kf5wk_TFgTc), and the zone as the south anchor of the finicky Del Mar-to-Imperial Beach iron stretch (VpW91AKOFVQ); border/jurisdiction caution carried in Getting there; 8 gaps, 3 zone-guide stubs, evidence file created… |
| locations/ensenada.md | geo | transformed | gaps:6 stubs:5 spots:4 | new zone page under baja-pacific-north for the spot library's Ensenada section: 5 skeleton sections + evidence pair; 4 charted spots (Punta San Miguel, Punta Morro, San Miguel Reef, Punta Banda with its boiler caution) framing the region's working port. The corpus attaches its material to distances from the Hotel Coral marina rather than to the charted names, so the page is built as a distance ladder (bait outside the marina, the 7-8 mi high spot cresting to 25 ft from 200 ft, the 300 ft rock drop-off down-coast, the 20-30 mi temperature break, the 42-43 mi August 2024 tournament bank, a… |
| locations/colonet.md | geo | transformed | gaps:8 stubs:2 spots:4 | new zone page under baja-pacific-north on the v2 zone skeleton (page did not exist) from 4 corpus sources + cameron; census assigns 4 spots — the two charted Colonet fathom high spots (28/41 fa) plus banks 52 and 330 from the offshore-banks section, none of which have gazetteer pages yet so the children block is empty; new zone-level material mined from YAKOv9bXKO0 (winter/March-2026 yellowtail yo-yo destination, 120-180 ft with 220 ft outliers, fish ~30 ft off the bottom, anchored-with-current-both-rails presentation, red-crab blooms and red-crab jig colour, the heavier long-range yo-yo… |
| locations/davis-knoll-san-miguel-gap-rodriguez-seamount.md | geo | transformed | gaps:9 stubs:2 fc:0 spots:4 | new zone page under socal-bight on the v2 zone skeleton (page did not exist); the region's NW corner off Point Arguello and San Miguel Island. Census assigns 4 spots — Davis Knoll, Rodriguez Seamount and San Miguel Gap clustering inside 11.3 nm, with Arguello Canyon attached at 15.1 nm off centre and carried as queued, not re-parented; none has a gazetteer page yet so the children block is empty. Corpus carries ZERO fishing doctrine here (0 notes in the census), so this is a position-and-ladder page whose only scoped material is weather: the Conception night-wind trap and the 2+… |
| locations/corner-140-182.md | geo | transformed | gaps:9 stubs:2 fc:0 spots:4 | geo/zone verified, 6 fixes applied — census membership, coordinates and all distance arithmetic reproduce; 4 transcript spot-checks faithful; one documented mark (the 182) + 3 position-only, 181/182 census-vs-corpus split flagged |
| locations/coronados-230-302-226.md | geo | transformed | gaps:14 stubs:2 fc:0 spots:4 | zone page verified; census/coords/20+ derived distances reproduce, 5 transcript spot-checks faithful; 3 non-reproducing derived-geography claims corrected in place |
| locations/upper-cross-421-390.md | geo | transformed | gaps:10 stubs:0 fc:0 spots:4 | geo zone page minted (zero-corpus, position-and-ladder); applied after fixing two miscomputed port-distance ranges, one false nearest-position superlative and one wrong bearing; coordinates and all intra-zone distances reproduce |
| locations/pistol-bell-bank-300.md | geo | transformed | gaps:9 stubs:0 fc:0 spots:4 | geo zone page verified against the census and the spot library; four geographic-accuracy fixes applied, no information loss; corpus silent on all four marks so written as position-and-ladder, loose cluster (31.6 nm corner to corner) left as queued |
| locations/385-238-475.md | geo | transformed | gaps:9 stubs:0 fc:0 spots:4 | geo zone page applied with 6 verifier fixes (2 false distance comparisons, 1 unstated metric, 1 mis-attributed cite, 2 meaning-drift corrections); geometry and census fidelity verified exact; no corpus source names these four banks |
| locations/372-245-250.md | geo | transformed | gaps:9 stubs:0 fc:0 spots:4 | zone page verified and applied with three numeric/claim corrections; coordinates, 14 distance figures and 5 transcript cites all reproduce; census 3-notes count confirmed false positives so written as position-and-ladder |
| locations/south-orange-county-crystal-cove.md | geo | transformed | gaps:11 stubs:1 fc:0 spots:3 | new zone page verified — coordinates, deltas and all four cites trace to source; missing Evidence section added; zero-corpus stretch written as charted-position arithmetic plus labelled Bight-wide doctrine, Abalone Point MPA corner geometry surfaced |
| locations/172-125.md | geo | transformed | gaps:11 stubs:2 fc:0 spots:3 | apply-with-changes: new zone page under socal-bight; coords/23 derived distances/4 transcript cites verified; 4 numeric+meaning fixes applied, 1 attribution fix in evidence |
| locations/slide-152-277.md | geo | transformed | gaps:8 stubs:1 fc:0 spots:3 | escalate(apply): new zone page under socal-bight; census + 20+ derived distances/bearings + 5 transcript cites verified; 7 fixes applied (2 geometry, 2 meaning-drift, 2 false gap flags, 1 bearing wording) |
| locations/51-181-138.md | geo | transformed | gaps:11 stubs:2 spots:3 | apply-with-changes: new zone page under socal-bight; census membership, coordinates, all distances/bearings and 4 transcript cites verified; 5 fixes applied (distance range, front-matter figure, compass descriptor, quoted-term drift, ladder scope) |
| locations/81-381.md | geo | transformed | gaps:9 stubs:3 fc:0 spots:3 | apply: new zone page + evidence pair under socal-bight; all derived geometry recomputed correct, census untouched, 3 transcript spot-checks clean, no changes needed |
| locations/43-91-300.md | geo | transformed | gaps:12 stubs:2 spots:3 | apply-with-changes: new zone page under socal-bight; census, coordinates, all derived distances and 5 transcript cites verified; 3 fixes (two false superlatives, one unsupported count) |
| locations/w-butterfly-157.md | geo | transformed | gaps:13 spots:3 | apply-with-changes: new position-and-ladder zone page (zero corpus coverage); ~35 derived distances recomputed and census verified; 4 fixes (3 distance corrections, 1 miscited source, 1 missing neighbour link) |
| locations/upper-500-hidden-bank.md | geo | transformed | gaps:14 stubs:2 spots:3 | apply-with-changes: new zone page under baja-pacific-north; corpus hook the census missed (302-to-hidden-bank corridor) captured; 20+ derived distances recomputed correct; 1 mis-targeted cite link fixed |
| locations/baja-270-double-220-295.md | geo | transformed | gaps:10 stubs:1 spots:3 | apply-with-changes: new zone page under baja-pacific-north; corpus depth genuinely zero (row's 94 notes is a depth_term dash-split artifact scoring 'Baja'); 30+ derived distances verified; 3 fixes (false nearest-neighbour claim, rounded ratio, scope wording) |
| locations/483-500-437.md | geo | transformed | gaps:13 stubs:1 fc:0 spots:3 | new zone page under baja-pacific-north on the v2 zone skeleton (page did not exist); corpus depth is genuinely zero — the census's 3 note hits are all false positives on the bare number 500 (an Accurate Tern reel size, a jig weight in grams, Catalina's ~500-fathom curve). Position-and-ladder page: the 437/483-500 pair clusters at 7.9 nm and East 400 is an attached lone bank 17.5 nm off that pair's midpoint, giving a 20.7 nm zone on the 118 W meridian between Upper Cross and Lower Cross; East 400 sits 13.6 nm from Lower Cross, closer than to either zone-mate, logged as a queued question… |
| locations/1140-finger-450.md | geo | transformed | gaps:11 stubs:2 | zone page written — 3 charted spots, no corpus material; position-and-ladder page with 11 gaps |
| locations/baja-230-peanut-bank-60.md | geo | transformed | gaps:14 stubs:2 spots:3 | new zone page under baja-pacific-north on the v2 zone skeleton (page did not exist); corpus depth genuinely zero — the row's 94 notes is the depth_term dash-split artifact scoring 'Baja' (same as baja-270-double-220-295), and anchored greps on Peanut / the 230 / the 60 return only RW Peanut lures, a swimbait model and line/jig weights. Position-and-ladder page with two real findings: this is the TIGHTEST three-or-more-spot cluster in the region's bank grid (8.3 nm corner to corner, all three legs inside the 12 nm cap, src=cluster with nothing attached) and the CLOSEST-INSHORE one (the 60 is… |
| locations/sniffer-west-400-300.md | geo | transformed | gaps:14 stubs:3 fc:0 spots:3 | new zone page under baja-pacific-north on the v2 zone skeleton (page did not exist); corpus depth genuinely zero — the row's 9 notes are false positives on the bare number 300 (reel sizes, jig grams, line ratings in gear notes), and the bare word 'sniffer' returns only deck talk (pNNrYXlgkO4) and a jerkbait line (WE643Fue1_A). Position-and-ladder page with one real finding: this is the only Baja bank zone besides Baja-230/Peanut/60 whose every leg clusters inside the 12 nm cap (4.8 / 10.1 / 10.8 nm, src=cluster, nothing attached), so it is a genuine one-day circuit; the 245 sits 7.1 nm off… |
| locations/179-220.md | geo | transformed | gaps:13 stubs:2 spots:3 | new zone page under baja-pacific-north on the v2 zone skeleton (page did not exist); corpus depth genuinely zero — anchored greps on the 179 / the 220 / Tuna Hole return only the spot library and the collision-rule line in the zone lexicon. Position-and-ladder page with three findings: Tuna Hole (179) is the SOUTHERNMOST charted position in the entire spot library; it is the ONLY name in the 125-spot offshore-banks section that states a target species and the only 'hole' anywhere in the library; and 179 / Tuna Hole (179) is the only distinct-names-not-a-collision pair the census puts inside… |
| locations/lower-cross.md | geo | transformed | gaps:12 stubs:2 fc:0 spots:3 | new zone page, position-and-ladder only (corpus depth zero at all three marks); verifier applied 3 arithmetic/consistency fixes; all distances/bearings/superlatives reproduced from spot-lists via census nm(); census zone membership unaltered |
| locations/boot-504-307.md | geo | transformed | gaps:13 stubs:2 spots:2 | new zone page (The Boot (504) / 307) + evidence file, parented to socal-bight; corpus is one line — 5to3Q5P7w90 puts the Masters marlin tournament fleet 'in by the boot' in September 2022, and nothing names the 307 at all; ~30 derived distances computed from the spot library (9.3 nm pair separation on 067, LA - 270 at 6.8 nm inside the neighbouring zone, Catalina West End 16.3 nm, Pelican Point 36.2 nm); both fathom-name reads flagged; 13 gaps, 2 stubs, 2 spots, 0 child pages yet |
| locations/hidden-reef-170.md | geo | transformed | gaps:15 stubs:2 spots:2 | new zone page (Hidden Reef / 170) parented to socal-bight, no evidence file; zero corpus coverage — neither mark appears in any transcript, note or evidence file, so this is a position-and-ladder page; ~25 derived distances computed from the spot library (identical charted latitude 33 43.800 on both marks, 5.2 nm apart on 090/270, The Boot (504) within 0.03' of latitude making a 28.0 nm three-mark parallel across two zones, Kidney Bank (63) 11.9 nm, Webster Point SBI 15.7 nm, Pelican Point 65.9 nm, nearest eval target 14 Mile Bank 61.5 nm); 170 read as fathoms flagged, Hidden Reef makes no… |
| locations/la-270-286.md | geo | transformed | gaps:13 stubs:2 spots:2 | geo zone page verified — coordinates, distances and 12 nm clustering reproduce from the census/spot library; 2 mis-cites re-sourced, 1 bearing corrected, 1 mood hardening softened, 3 front-matter sources restored |
| locations/kidney-bank-63-175.md | geo | transformed | gaps:17 stubs:1 fc:2 spots:2 fixes:3 | geo zone page verified — coordinates, ~30 derived distances/bearings, the 25 nm fathom-name ranking and the census row all reproduce; 5 transcript spot-checks clean; 3 verifier fixes (false nearest-position superlative, mis-ordered neighbour list, compass label) |
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
| locations/pendleton-ar-center.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/oceanside-ar-2l.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/johnson-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/stony-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/parson-s-landing.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/arrow-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/indian-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/eagle-reef-buoy.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lions-head.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/ship-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/isthmus-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/bird-rock-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/yellowtail-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/empire-landing.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/red-bluff.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/little-gibraltar-main-big-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/long-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/hen-rock-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/toyon-bay.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/gallaghers.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/can-dump-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-quarry.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/jewfish-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/slide.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/west-end-humps-1.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/west-end-humps-2.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/west-end-humps-3.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-1-48-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-2-43-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-3-43-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-4-47-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-5-45-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-6-48-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-7-40-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-8-43-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde-cod-pinnacle.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/3rd-v-cod-1-36-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/3rd-v-cod-2-31-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-rockfish-1-46-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-rockfish-2-48-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-rockfish-3-47-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/avalon-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/pendleton-ar.md | gazetteer | done |  | mechanical: AR complex, 5 waypoints |
| locations/oceanside-ar.md | gazetteer | done |  | mechanical: AR complex, 19 waypoints |
| locations/carlsbad-ar.md | gazetteer | done |  | mechanical: AR complex, 12 waypoints |
| locations/181-182-289.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/anacapa-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/bird-rock-two-harbors.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/catalina-island.md | gazetteer | pending |  | harvest: 5 mention(s) |
| locations/catalina-west-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cedros-gono-islands-kelp-bed.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/channel-islands.md | gazetteer | pending |  | harvest: 2 mention(s) |
| locations/chester-s-rock.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/clemente-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cortez-bank.md | gazetteer | pending |  | harvest: 3 mention(s) |
| locations/dana-point-harbor.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/del-mar-to-imperial-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/dono.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/el-bajo.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/geronimo-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/guadalupe-island.md | gazetteer | pending |  | harvest: 2 mention(s) |
| locations/guadalupe-island-north-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/hotel-coral-high-spot.md | gazetteer | pending |  | harvest: 2 mention(s) |
| locations/isla-espiritu-santo.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-bocana.md | gazetteer | pending |  | harvest: 3 mention(s) |
| locations/macro-banks.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/newport.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/north-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/palos-verdes-outside-kelp-below-rocky-shark-fin-flat-rock.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/point-conception.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/punta-eugenia.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ridge-uncle-sam-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/rose-island-dondo-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-augustine.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-benito-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-benito-islands.md | gazetteer | pending |  | harvest: 2 mention(s) |
| locations/san-clemente-island.md | gazetteer | pending |  | harvest: 7 mention(s) |
| locations/san-clemente-island-catalina-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-martin-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-miguel-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/santa-barbara-island-sutil.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/santa-cruz-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/santa-monica-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-calico-spot.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ventura.md | gazetteer | pending |  | harvest: 2 mention(s) |
| locations/west-end-tuna-zone.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-jolla-canyon-shelf-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/la-jolla-shelf-hardbottom.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/cove.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/bump.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/half.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/northwest-corner.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/32-fathom-spot-rockfish.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/marine-street.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/windansea.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/crystal-pier.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/270-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/widow-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/airplane-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/la-jolla-canyon.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/mission-bay-park-artificial-kelp-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/mission-bay-park-nel-tower.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/mission-bay-park-ingraham-st-bridge-rubble.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/mission-bay-park-pier-pilings.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-onofre-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/box-canyon-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/barn-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/clam-beds.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/golf-ball.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/buccaneer-pipe.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/encina-powerplant-pipe.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/terramar-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/carlsbad-canyon.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/anderson-pipe.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/ponto.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/leucadia-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/beacons.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/encinitas-rockfish-devil-s-rock-north.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/solana-beach-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/powerhouse-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/del-mar-rockfish-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/flat-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/eagle-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/catalina-west-cove.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/iron-bound.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/ribbon-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/whale-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/cape-cortes.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lobster-bay.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/cat-harbor.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/pedestal-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/little-harbor.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/sentinel-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/ben-weston-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/catalina-china-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salta-verde.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/silver-canyon.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/palisades.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/3-v-s.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/church-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-light.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/seal-rocks.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/torrey-pines-artificial-reef.md | gazetteer | done |  | mechanical: AR complex, 2 waypoints |
| locations/pacific-beach-ar.md | gazetteer | done |  | mechanical: AR complex, 12 waypoints |
| locations/bank-23.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/bank-38.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/boca.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/bola-grounds-20-miles-north-of-the-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/bola-island-high-spot.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cardonosa-isla-cartito.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/honeymoon-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/isla-carmen-north-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/isla-monserrat-north-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/lower-banks.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/modesto-main.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/playa-la-gringa.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/puerto-escondido-marina.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/punta-perico.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/six-mile-reef.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-big-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-sante-desante.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/hill-street.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/college-area-sunset-cliffs.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/green-tank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lab.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/new-hope-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/5-tanks.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/point-loma-pipe.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/dropoff.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/buoy-3-hardbottom.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/whistler-buoy.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/zuniga-jetty.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/hotel-del-hardbottom.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-a.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-b.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-c.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-d.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-e.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-f.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/international-reef-missile-tower.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/la-bufadora.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/white-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/el-retiro.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/billy-s-bluff.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/47-fa-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/48-fa-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/bahia-soledad.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/15-fa-ridge.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-santo-tomas.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/isolete.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/38-fa-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/33-fa-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-martin-island-anchorage.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-martin-island-natural-jetty-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/roca-ben.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/6-5-fathom-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/15-fathom-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/breakers-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/tranquillo-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/304.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/hospital-100-fathom-curve.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/monarch-boilers.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/salt-creek.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/dana-point-kelp-red-buoy.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/barber-poles.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-clemente-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-clemente-artificial-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-mateo-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/trestles.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/cave-canyon-wsb-zone.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/landing-cove.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/webster-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/arch-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/caverns-area.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/three-sisters.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/sutil-island-squid-yellowtail-zone.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/osborn-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/blockhouse.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/airplane-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-squid-grounds.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/seabass-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-end-buoy.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/daytona-beach.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/daytona-wsb-zone.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/dutch-harbor.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/potato-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/cherry-banks.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/9-fathom-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/west-cove.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/dunes.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/eel-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/seal-cove.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/mail-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lost-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/china-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/caves.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/29-fathom-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/imperial-beach-kelp.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/imperial-beach-kelp-south-end.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/imperial-beach-flats.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/imperial-beach-pipe.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/bull-ring.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/rosarito-flats.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-descanso.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/descanso-rockfish-1.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/descanso-rockfish-2.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/sugarloaf-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-mesquite.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/la-fonda.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/bajamar.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-salsipuedes.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/97.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-finger-bank-rockfish-180ft.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-finger-bank-rockfish-240ft.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-finger-bank-rockfish-300ft.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-finger-bank-71-fathom-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-finger-bank-27-fathom-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-san-miguel.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-morro.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-miguel-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/punta-banda.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/colonet-high-spot-28-fathoms.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/colonet-41-fathoms.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/52.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/330.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/purse-seine-rock.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/pyramid-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/pyramid-cove.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/378.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/213.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/1010-trench.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/airplane.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/1067-knuckle.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/pelican-point-number-1-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/crystal-cove-number-2-spot.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/abalone-point.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/davis-knoll.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/rodriguez-seamount.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-miguel-gap.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/arguello-canyon.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/140.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/182.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/166.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/corner.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/226.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/302.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/coronados-230.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/371.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/421.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/390.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-cross.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/60-mile-bank-53-fa.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/pistol.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/bell-bank-300.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/worm.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/elephant.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/385.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/238.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/475.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/480.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/372.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/245.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/250.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/dumping-grounds.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/172.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/125.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/499.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/152.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/277.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/181.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/51.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/138.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/81.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/381.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/267.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/91.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/300.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/157.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/w-butterfly.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/mushroom.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/hidden-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-500.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-hidden-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/295.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/baja-270.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/double-220.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/307.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/boot-504.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/170.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/hidden-reef.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/437.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/483-500.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/east-400.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/450.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/1140-finger.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/lower-500.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/60.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/peanut-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/baja-230.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/west-400.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/sniffer.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/179.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/220.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/tuna-hole-179.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/catchers-mitt.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/950.md | gazetteer | done |  | mechanical: coordinates + parent zone |
<!-- review:worklist:end -->
