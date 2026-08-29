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
| species/cabrilla.md | full | transformed | gaps(9), misplaced(1), spots(2), reg-claims(1), spinout(2), factcheck(2), asr-uncertain(2) | transform verified, applied with 5 fixes: 2 drift corrections, 1 restored conflict position, 2 pairing/format fixes |
| species/calico-bass.md | full | transformed | gaps(5), fc(4), misplaced(1), spinout(1), spots(21), reg-claims(3), asr-uncertain(7) | transform verified, applied with 6 fixes: 1 lead drift correction, 1 uncited inference removed, 1 template mislabel, 1 relative-time fix, 1 meta-commentary trim, 1 restored cross-link |
| species/california-halibut.md | full | transformed | gaps(3), misplaced(1), spots(9), reg-claims(2), spinout(2), factcheck(2), asr-uncertain(5) | transform verified, 5 fixes applied (1 table break, 1 scope narrowing, 1 style, 2 conservation restores); 511->402 lines + 307-line evidence file |
| species/california-spiny-lobster.md | full | transformed | gaps(6), spots(5), reg-claims(1), fact-check(4), asr-uncertain(1) | apply-with-changes — conservation clean across all 7 prior source ids, 3 new sources verified against transcript, 3 minor fixes applied |
| species/dorado.md | full | transformed | gaps(4), stubs(8), spots(13), spinout(1), fact-check(2), asr-uncertain(4) | apply-with-changes: full conservation confirmed, one before-state leader-floor inversion corrected, four verifier fixes applied |
| species/ocean-whitefish.md | full | transformed | gaps(6), stubs(6), fact-check(2), misplaced(1), spots(5), reg-claims(3), asr-uncertain(3) | apply-with-changes: v2 skeleton complete, evidence split conserves all four before-state observations, 14 new cited sources added; 4 verifier fixes |
| species/opah.md | full | transformed | gaps(9), spots(1), reg-claims(0), asr-uncertain(1), fact-check(3) | apply-with-changes: faithful transform, 5 outside-knowledge/causal-inference fixes applied by verifier |
| species/pacific-crevalle-jack.md | full | transformed | gaps(9), stubs(2), spots(3), reg-claims(3), fact-check(5), asr-uncertain(3) | apply-with-changes: faithful v2 migration + evidence split; verifier added sourced terminal-tackle spec and rescoped 3 flags |
| species/rockfish-lingcod.md | full | transformed | gaps(5), stubs(5), misplaced(1), spots(11), reg-claims(2), fact-check(3), spinout(1), asr-uncertain(3) | apply-with-changes: faithful v2 migration + evidence split; verifier fixed one hedge-hardened-into-doctrine row |
| species/sand-bass.md | full | transformed | gaps(4), spots(9), spinout(2), reg-claims(1), asr-uncertain(3) | apply-with-changes — conservation clean, 12 router rows, evidence split faithful; verifier fixed one unsupported detail, one hardened hedge, one mis-cite, added a mandated tide trigger, converted an unsituated SPJ row into the cited deep-spot jig situation |
| species/sheephead.md | full | transformed | gaps(7), stubs(6), fact-check(1), spots(9), reg-claims(3), spinout(2), asr-uncertain(1) | apply-with-changes — conservation clean (5 prior source ids + 3 Observed blocks traced), check-note OK, 0 dead links; 4 verifier fixes: invented jig type, two title-only claims stated as doctrine, one mis-scoped cite, two missing zone stubs |
| species/skipjack-tuna.md | full | transformed | gaps(7), stubs(6), misplaced(1), spots(8), reg-claims(1), fact-check(1), asr-uncertain(2) | apply-with-changes — conservation clean (6 pre-existing cites + both Observed blocks land in the note/evidence pair, legacy grade claim retained under flag), 4 cite-accuracy fixes applied |
| species/snook.md | full | transformed | gaps(6), misplaced(1), spots(3), reg-claims(1), spinout(0), asr-uncertain(25 vs 35 lb mangrove fluorocarbon; snook mouth-abrasion mechanism; 40 lb snook species pairing) | apply-with-changes: conservation clean, 8-source expansion corpus-verified, two overreaching synthesis claims tightened to their sources |
| species/spotted-bay-bass.md | full | transformed | gaps(3), spinout(2), spots(9), reg-claims(1), fact-check(1 - eyelids/shade single-source), asr-uncertain(bait brand 'war bait'; suspension-vs-bottom depth split; 'the sunset wall') | apply-with-changes: layout v2 skeleton, ~120 new cited lines from YgqXf9iICyg, evidence split created, 1 conservation gap repaired |
| species/striped-marlin.md | full | transformed | gaps(6), misplaced(1), spots(12), reg-claims(2), spinout(1), fact-check(1), asr-uncertain(11:15 vs 11:30-12:00 low tide in 3qSY328fFYo; circle-hook size for marlin mackerel in m2q22sPPkEM) | apply-with-changes: v2 skeleton complete, 23 evidence entries from 8 Observed blocks, no parameter or conflict lost; three verifier fixes (mis-attributed cite restored, unsupported clause cut, retired claim traced) |
| species/swordfish.md | full | transformed | gaps(6), stubs(5), fact-check(2), misplaced(1), spots(9), reg-claims(2), asr-uncertain(1) | apply-with-changes: one cited claim corrected against transcript, one spot link retargeted, missing Zone-material section added; conservation and cite coverage clean |
| species/wahoo.md | full | transformed | gaps(6), stubs(5), spots(6), reg-claims(2), fc(2), spinout(1), asr-uncertain(3) | apply-with-changes: 3 fixes applied (1 meaning drift, 1 mis-cite x3, 1 unsupported number); conservation and cite coverage clean |
| species/white-seabass.md | full | transformed | gaps(8), misplaced(1), spots(4), reg-claims(2), spinout(2), stubs(3), asr-uncertain(1) | apply-with-changes: full v2 skeleton, evidence split conserves all 19 cites and every parameter; one unsourced inference trimmed |
| species/yellowfin-tuna.md | full | transformed | gaps(7), stubs(10), misplaced(1), spots(18), reg-claims(4), spinout(2), fact-check(2), asr-uncertain(7) | transform verified — full conservation (all numbers and cites survive), 6 transcript spot-checks clean, 2 wording fixes applied |
| species/yellowtail.md | full | transformed | gaps(9) fc(1) ledger(4) misplaced(2) | feedback rework (2026-08-24): 563->423 lines, evidence 140->176; all 16 feedback items verified landed; 4 demotions to evidence; zone-guides section + Coronados link + 7 stubs; conservation clean after 3 verifier restorations; recommitted after guard protected-path churn fix |
| techniques/bait-and-switch.md | standard | transformed | spots(2) | migrated to layout v2, evidence split, Gear class/Common failures filled, verified conservation clean |
| techniques/beach-lure-depth-control.md | standard | transformed | gaps(3) | transform verified, one cite-support fix applied in Gear class section, no information loss found |
| techniques/cheater-troll.md | standard | transformed | gaps(1) | transform verified faithful, ASR caveats conserved to evidence, gap flags correct, check-note.py clean |
| techniques/chunking.md | standard | transformed | spots(4) | transform verified faithful, observations split to evidence, execution consolidated into Gear class, no information loss found |
| techniques/clearing-a-backlash.md | standard | transformed | gaps(1) | transform verified faithful, template-compliant, mechanics conserved, backlinks regenerated |
| techniques/dart-jig-tuna.md | standard | transformed | none | transform verified, one meaning-drift defect (cross-source gear conflation) fixed in place |
| techniques/deep-drop-swordfishing.md | standard | transformed | fact-check(2) | transform verified with fixes: restored 2 deleted doctrine claims beside fact-check flags, restored dropped attribution on contested doctrine |
| techniques/drop-shot.md | standard | transformed | misplaced-content(3), spinout(1) | transform verified with in-tree fixes: 2 conservation restores, 1 unsupported-claim removal, 1 missing relocation flag added |
| techniques/dropper-loop.md | standard | transformed | gaps(0), misplaced(0), spots(4), reg-claims(0), spinout(1), gap(gear-class-lexicon, new) | v2 migration: dissolved 6 source-named headings, compacted to compact cites, split observations to evidence file with traces kept beside doctrine, completed infobox; verified with 2 fixes (resolved cite-unresolved to mUrihh0V59M; corrected fabricated gear_classes) |
| techniques/fighting-big-bluefin.md | standard | transformed | gaps(1) | migrated to layout v2: technique skeleton, plain-statement prose with compact cites, dissolved source-named headings, split ~26 observed blocks to evidence with traces beside doctrine, decision frame for sea-lion conflict; verified with 1 fix (restored dropped kite-fishing.md link) |
| techniques/fighting-fish-from-the-rail.md | standard | escalated |  | escalated: guard: out of scope for 'review: techniques/fighting-fish-from-the-rail.md': tackle/gear-classes.md |
| techniques/flat-fall-jigging.md | standard | transformed | gaps(2) | restructured to technique skeleton, house-style rewrite with compact cites, decision-rule-first leader conflict; verified with fixes (restored conflict-speaker attribution, restored a product-confidence caveat) |
| techniques/flyline.md | standard | escalated |  | escalated: guard: out of scope for 'review: techniques/flyline.md': locations/la-paz.md |
| techniques/foamer-casting.md | standard | transformed | spots(3) | transform applied with one evidence-grouping fix; escalated a resolved retrieve-speed conflict for Cameron |
| techniques/glide-baits.md | standard | transformed | gaps(2) | restructured to v2 technique skeleton, dissolved source-named heading, moved attribution preamble to cites, added infobox; verified with fix (restored dropped tube-bait-fishing.md link) |
| techniques/hoop-netting.md | standard | transformed | spots(4), reg-claims(1) | migrated to layout v2: restructured to technique skeleton, dissolved source-named headings, moved Observed block to evidence, added regulations/infobox; verified with 4 fixes (restored dropped statistic, restored altered direct quote, restored dropped contrast claim, removed leftover reconciliation-machinery phrase) |
| techniques/inshore-crankbaits.md | standard | transformed | spinout(1) | transform applied with 3 fixes (hedge-hardening x2, invented flag) |
| techniques/kayak-bass-fishing.md | standard | transformed | spots(2) | transform verified, one style fix applied (meta-attribution phrase) |
| techniques/kite-fishing.md | standard | transformed | spots(8), asr-uncertain(cat's-paw knot name, ~75ft payout knot function, tagline attachment mechanism, mph-to-knots conversion) | transform verified, 5 defects fixed in-tree (1 fabricated figure, 1 internal contradiction, 2 style-guide v2.1 violations, 1 dropped link) |
| techniques/knife-jigging.md | standard | transformed | spots(2), spinout(1) | transform verified with fixes (2 conservation gaps + 2 dropped cross-links repaired) |
| techniques/leadhead-swimbait-retrieve.md | standard | transformed | gaps(1), spinout(1) | transform applied with changes — fixed one misattributed citation and four instances of quote/caveat smoothing |
| techniques/live-bait-pendulum-cast.md | standard | transformed | gaps(1) | transform verified, 2 defects fixed in-tree (uncited borrowed claim, smoothed specific) |
| techniques/mangrove-structure-livebait.md | standard | transformed | none | transform verified: attribution preamble to plain-statement+cites, evidence file split, facts conserved and transcript-verified |
| techniques/ned-rig.md | standard | transformed | none | transform verified, one smuggled-specificity fix applied (baitcast to heavier tackle/drag near max) |
| techniques/night-bass-fishing.md | standard | transformed | spots(1) | restructured to v2 skeleton, dissolved source-named heading, stripped meta-attribution to evidence, added Common failures + infobox fields; verifier fixed fabricated retrieve_speed claim |
| techniques/panga-team-trolling.md | standard | transformed | gap(common-failures) | attribution preamble moved to machine layer, added Gear class + Common failures + species-applications, infobox fields added |
| techniques/rail-etiquette.md | standard | transformed | gaps(1) | attribution preamble split to evidence file, plain-statement rewrite, v2 skeleton sections added, all claims traced to source |
| techniques/rockfish-deep-dropping.md | standard | transformed | asr-uncertain(SoCal depth range, sinker oz rendering, bait product name) | restructured to v2 skeleton, consolidated sinker-weight table; verifier fixed systemic mis-citation of ~16 claims to correct source transcripts, one fabricated depth-weight pairing, restored 2 dropped cross-links |
| techniques/rod-handling-live-bait.md | standard | transformed | asr-uncertain(backpedal hand/arm motion gestured on camera) | migrated to v2 skeleton, attribution moved to evidence file, cites added; verifier confirmed 3/3 transcript spot-checks, regenerated backlinks |
| techniques/skip-jigging.md | standard | transformed | gap(skip-jigging reel/rod-action/line-class), gap(common failures) | migrated to v2 skeleton, added Gear class + Common failures, dissolved source-named heading, plain-statement rewrite; verifier confirmed 3 transcript spot-checks, regenerated backlinks |
| techniques/sliding-sinker.md | standard | transformed | spinout(3), asr-uncertain(TLC jig name, Jobu hook oz-vs-aught mishearing), spots(5) | restructured to v2 skeleton, evidence split, 3 spinouts + 5 spots queued; verifier fixed one meaning-drift (personal snelling limitation hardened into general fact) |
| techniques/slow-pitch-jigging.md | standard | transformed | misplaced(1), spots(2), reg-claims(1) | migrated to v2 skeleton, evidence split, regulatory claim stamped, misplaced-content flagged; verifier reverted an unauthorized doctrine reconciliation on jig-weight formulas, regenerated backlinks |
| techniques/slow-trolling-bait.md | standard | transformed | spots(1) | migrated to layout v2: added infobox fields, added missing Gear class section, per-claim cites replacing attribution preamble, moved secondhand Cedros observation to evidence (147→156 lines; evidence 29 lines) |
| techniques/speed-trolling.md | standard | transformed | none | transform verified, apply-with-changes: fixed a fabricated gear_classes slug and a misattributed internal cite; all doctrine, numbers, and the Cameron no-swivel conflict traced faithfully to source |
| techniques/spinnerbaits.md | standard | transformed | gaps(1), spots(2), asr-uncertain(War Baits HD vs 1 oz HP Warhead) | transform verified faithful — v2 skeleton, cites, and evidence split all conform; Lane attribution correctly relocated to evidence per style-guide v2.1 |
| techniques/spinning-reel-wind-knots.md | standard | transformed | gaps(1) | transform verified faithful — v2 skeleton, cites conserved, 5/5 transcript spot-checks match |
| techniques/surface-iron-casting.md | standard | transformed | spots(3) | transform verified, one jargon-link fix applied in place |
| techniques/surface-iron-color.md | standard | transformed | spots(8) | 258->130 lines, 14 single-trip colour reports split to evidence, tuna colour-by-light kept as doctrine, one corroboration cross-reference restored by verifier |
| techniques/surface-iron.md | standard | transformed | misplaced(1) spots(10) | faithful transform 654->512 lines + 77-line evidence: blockquotes to prose, source-scoped headings dissolved, 2 legacy cites transcript-verified; 2 verifier fixes (cite-scope split, harvest-row cite) |
| techniques/swimbaits.md | standard | transformed | contradicted-by-source(1), single-source(1), misplaced-content(2) | transform verified with 5 fixes (2 restored facts, 1 conflict-attribution restore, 1 invented-number correction, 2 ledger rows added) |
| techniques/trolling.md | standard | escalated |  | escalated: guard: out of scope for 'review: techniques/trolling.md': bait/making-bait.md |
| techniques/tube-bait-fishing.md | standard | transformed | spots(2), spinout(1), asr-uncertain(unnamed ~5 mph troll lure identity in the yellowtail troll-to-locate section) | transform verified with 5 fixes (2 dropped quotes/details restored, 1 miscited source corrected, 1 missing misplaced-content flag added, 1 fabricated depth figure removed) |
| techniques/two-speed-low-gear-fight.md | standard | transformed | none | 300->235 lines in note (observation/provenance split to a new 131-line evidence file), one self-narration phrase fixed in verify |
| techniques/underhand-casting.md | standard | transformed | none | layout v2 migration, plain-statement rewrite, evidence split - no information loss, all 5 sources spot-checked and faithful |
| techniques/wacky-rig.md | standard | transformed | gaps(1) | v2 migration faithful: evidence split, gap flag, and infobox fields all conserve prior content; no drift found |
| techniques/wahoo-bomb-casting.md | standard | skipped |  | skipped: verifier-reject: conservation failure - dropped bomb-weight/hook-size parameter, color detail, jaw/hookset mechanism, and species-router cross-reference |
| techniques/wahoo-trolling.md | standard | transformed | spots(2) | transform verified faithful - observation split to evidence file, v2 front matter/gear_classes added, gear-class-detail anchor preserved |
| techniques/wind-in-your-face-positioning.md | standard | transformed | none | transform verified - plain-statement rewrite conserves all before-facts via evidence-file split; no meaning drift |
| techniques/yo-yo-iron.md | standard | transformed | misplaced(2), spinout(1) | transform verified with 3 conservation gaps found and fixed in-tree (two dropped top-technique attributed claims, one dropped colour pick) |
| lures/bay-bass-plastics.md | standard | transformed | none | transform verified with 4 fixes (2 fabricated infobox numbers corrected, 2 dropped cross-refs restored) |
| lures/cedar-plug.md | standard | transformed | gaps(1), asr-uncertain(amp chobby pattern name) | transform applied, three named subsections compressed to plain-statement Color-and-finish section per v2.1 style, Specs table added, When-to-choose-it section added |
| lures/crocodile-spoons.md | standard | transformed | gaps(1) | transform verified; one conservation gap (dropped SoCal-anglers-generally claim/quote) found and fixed in-tree, all other facts/cites/links traced clean |
| lures/dtx-minnow.md | standard | transformed | spots(2) | transform verified faithful, v2 skeleton compliant, all quotes/parameters conserved and cite-traced |
| lures/halco-laser-pro.md | standard | transformed | none | transform verified with fix: recovered lost per-source attribution/confidence-caveat detail into a newly created evidence file; all specs/parameters/cites otherwise conserved |
| lures/iron-jigs.md | standard | escalated |  | escalated: guard: out of scope for 'review: lures/iron-jigs.md': fish-care/dehooking-and-release.md |
| lures/jerkbaits.md | standard | transformed | gaps(1) | transform verified with 2 in-tree fixes (hedge restored on spawn exception, invented clause removed; Current Sniper switch-timing specificity restored) |
| lures/knife-jigs.md | standard | transformed | misplaced(1), spots(3) | transform verified with fixes: restored 6 dropped facts/quotes + 3 dropped cross-links, removed 1 fabricated detail, added 1 missing front-matter source id |
| lures/lucky-craft-flash-minnow.md | standard | transformed | asr-uncertain(color-pattern count) | transform verified, one conserved-fact fix applied (Japan/California tackle contrast restored) |
| lures/mad-mac.md | standard | transformed | spots(1), asr-uncertain(reel model caption) | transform verified faithful — specs/observations conserved via new evidence split, contested speed-band conflict kept attributed, all cites spot-checked against source transcripts |
| lures/rapala-husky-magnum.md | standard | transformed | none outstanding | transform applied, one flag-grammar fix made by verifier |
| lures/soft-plastic-swimbaits.md | standard | skipped |  | skipped: verifier-reject: 4 before-facts dropped (sizes, rod/reel models, jighead+cross-link, color/location tactic) plus one cite reattached to unsupported claim |
| lures/spreader-bar.md | standard | transformed | spots(1) | transform verified — specs/observations conserved via evidence split, transcript spot-checks confirm no meaning drift |
| lures/tube-baits.md | standard | transformed | spots(5) | v2 migration + plain-statement transform, construction/scent/color doctrine and Oreo-cookie-effect conserved, stale anchors fixed, cite added for the stupid tube line via 9a-Zy_D6c3w |
| lures/tuna-feathers-and-skirts.md | standard | transformed | gaps(1), spots(1) | transform verified, applied clean — no fixes needed, all facts conserved via evidence split |
| lures/tuna-poppers-and-stickbaits.md | standard | skipped |  | skipped: verifier-reject: house-style rewrite incomplete (56 retired boilerplate instances remain across an 840-line note) |
| rigging/assist-hooks.md | standard | transformed | none | transform verified with 3 in-tree fixes (2 dropped claims restored, 1 opinion-hardened-to-fact reverted) |
| rigging/bimini-twist.md | standard | transformed | asr-uncertain(quick-tie wrap counts) | transform verified, apply-with-changes: added missing evidence/bimini-twist.md to conserve dropped presenter/channel/date provenance |
| rigging/bite-leaders.md | standard | transformed | none | transform: attribution preambles migrated to new evidence/bite-leaders.md, doctrine-conflict decision frame added per style-guide v2.1, v2 infobox fields added; conservation and 3 transcript spot-checks confirmed faithful |
| rigging/crimping.md | standard | transformed | asr-uncertain(A2 crimp designation on 3zXcrGsIL-c) | transform: attribution moved to new evidence/crimping.md, sections merged into one When to use per v2 skeleton, layout v2 + line_class/hook_sizes added; 6/6 transcript spot-checks faithful |
| rigging/cut-loop-dropper.md | standard | transformed | gaps(2), spots(1), asr-uncertain(place name) | verified transform - attribution preamble correctly retired to machine layer, all doctrine/parameters conserved and paraphrased, template gap-flags added, 3 transcript spot-checks confirmed, 0 dead links |
| rigging/double-trouble-rig.md | standard | transformed | spots(2) | transform verified clean: full conservation, 4 transcript spot-checks passed, only fix was a missed link-maintenance regen |
| rigging/dropper-loop-knot-and-spider-hitch.md | standard | transformed | none | transform verified clean: presenter-framing removed, cites added, all parameters and the halibut-rig ambiguity note conserved |
| rigging/essential-knots.md | standard | transformed | asr-uncertain(worm knot ~10-wrap count, uneven on-camera tally, mpcSgkQvIzg) | transform verified, one conservation gap fixed (restored dropped Palomar line-loss detail to evidence) |
| rigging/fg-and-albright.md | standard | transformed | none | transform verified, conservation intact (all params + variant provenance traced to note or new evidence file), one v2.1 self-narration phrase fixed in place |
| rigging/flying-fish-harness.md | standard | transformed | spots(3), asr-uncertain(commercial pre-rig leader-material brand withheld; dead-flyer leader hook model name withheld; presenter surname uncertain) | transform applied clean - v2 layout, evidence split, hook-count conflict given decision frame, spot-harvest updated |
| rigging/haywire-twist.md | standard | transformed | none | transform verified, one dropped named attribution (Mike Lackey) restored in evidence file, all other content conserved |
| rigging/hollow-splice-and-serving.md | standard | transformed | spots(1) | transform verified: conservation intact, attribution correctly split to evidence file, cites confirmed against 3 transcripts |
| rigging/improved-clinch-knot.md | standard | transformed | asr-uncertain(hook size on H5NHGLm1H5U; tag re-entry description on H5NHGLm1H5U; wrap-before-eye narration order on J0NJhN6-Thg) | transform verified: v2 skeleton, plain-statement rewrite, citation compression; conservation traced, 3-source spot-check clean |
| rigging/john-collins-knot.md | standard | transformed | none | transform verified, two defects fixed in-tree (restored Tony Pena mechanism comparison; corrected false clip-duration claim) |
| rigging/leadhead-mods.md | standard | transformed | gaps(1), spots(4), asr-uncertain(leader connection name on the actively-cast squid rig) | transform verified, apply-with-changes: restored two dropped source-provenance entries + a quote/ASR-caveat to evidence file, cleaned two meta-attribution phrasings |
| rigging/perfection-loop-knot.md | standard | transformed | gaps(1) | transform verified, one hedge-hardened-to-fact drift fixed in tree |
| rigging/pr-knot.md | standard | transformed | gaps(1) | transform applied with link-maintenance backlink regen; evidence split conserved all four-video duplicate analysis, no content loss or drift |
| rigging/rp-knot.md | standard | transformed | none | transform verified, apply-with-changes: ran link-maintenance.py to regenerate rigging/README.md + rigging/evidence/README.md index entries the worker's patch omitted |
| rigging/rubber-band-deep-rig.md | standard | transformed | spots(3), asr-uncertain(leader 60-80lb Vol.55, hook knot Vol.104, placement-side Vol.84, build-ID Vol.71, hook model Vol.233) | transform verified: evidence split, v2 front matter, and Bralla-naming adjudication faithful; verifier restored 5 secondary numeric parameters (leader/top-shot lengths, sinker weights, one depth example) dropped during compression |
| rigging/san-diego-jam-knot.md | standard | transformed | asr-uncertain(doubled-tie slide direction on VyFpIk-Na9Q; wetting-rationale caption inversion on VyFpIk-Na9Q) | transform verified: v2 skeleton, plain-statement rewrite, per-source citation compression, wrap-count/mechanic/naming/caution facts all traced from HEAD into AFTER; one dropped cross-reference link restored |
| rigging/san-diego-jam-single-vs-double.md | standard | transformed | none | transform verified clean, minor README index regen applied |
| rigging/seaguar-knot.md | standard | transformed | conservation-loss(2, fixed), meaning-drift(1, fixed) | transform applied with fixes: restored two conservation losses (Cesar tenure figures, Improved Clinch Knot cross-link) and corrected a factually-wrong on-camera-naming claim introduced by the transform |
| rigging/slim-beauty-knot.md | standard | transformed | none | transform verified with fixes — restored dropped presenter/ASR-caption attribution, corrected malformed flag grammar |
| rigging/springer-knot.md | standard | transformed | none | transform verified, 1 fix applied (removed uncited 'flylined' detail smuggled into low-profile bullet) |
| rigging/surgeons-knot-mono-to-fluoro.md | standard | transformed | asr-uncertain(zKovnvOwlFc presenter unresolved; PKwvkOOYzto presenter name Captain Mark vs title-credited Capt Art) | transform verified, 6 conservation gaps fixed in-tree (5 dropped parameters/quotes + 1 dropped species cross-link pair) |
| rigging/surgeons-loop.md | standard | transformed | spots(1), asr-uncertain(reel name juice beet reel, hook size 60 J hook to 6/0-9/0, presenter name pattern noer to paternoster) | transform verified with 2 restored parameters (sinker-attachment knot + rig topology, plus 2 minor color/reasoning details) that the worker dropped without an evidence file; all other content, cites, and asr-uncertain flags traced cleanly |
| rigging/tony-pena-knot.md | standard | transformed | none | transform verified faithful - de-attribution moved out of prose per style-guide v2.1, v2 front matter added accurately, mechanics/numbers/quotes fully conserved, check-note.py clean |
| rigging/trap-rig.md | standard | transformed | spots(1) | transform verified faithful - both applications parameters, judgment, and citations conserved; anchor link to sliding-sinker.md renamed heading confirmed valid; spot-harvest row and README index in sync |
| rigging/tuna-feather-rig.md | standard | transformed | none | transform applied with one conservation fix (restored dropped lure-variety fact) |
| rigging/wind-on-leader.md | standard | transformed | none | transform verified faithful - plain-statement rewrite, v2 infobox added, all cites and parameters conserved, quotes verified against source transcripts |
| rigging/wiring-a-surface-iron.md | standard | transformed | gaps(1) | transform verified, one meaning-drift fix applied (candy-bar exclusivity degree restored) |
| conditions/bird-reading.md | standard | transformed | gaps(1), spots(4) | transform applied with 2 conservation fixes (restored dropped Cameron facts: cormorant prior-view, shearwater model-gap); mis-citation on bird radar correctly repaired to HWx1jDTGsng |
| conditions/current-diagnostics.md | standard | transformed | none | transform verified faithful - attribution preambles moved to new evidence.md pair, single-trip Cabo observation demoted intact, 4-source spot-check clean, check-note.py 0 warnings |
| conditions/current-structure.md | standard | transformed | gaps(2), spots(8), cite-correction | transform verified; conservation intact, style-v2 compliant, one fabricated/misattributed cite found and corrected in-tree (wrong video id for the SCI 2022-11-23 exception, now Z3rZqy2Pi8E) |
| conditions/deep-scattering-layer.md | standard | transformed | spots(1) | transform applied - v2 skeleton, cites, evidence split, How to use it in planning section all faithful; link-maintenance regen applied as fix |
| conditions/kelp-paddies.md | standard | transformed | none | transform verified: v2 split faithful, no info loss, 4/4 transcript spot-checks matched, check-note.py passed (1 non-blocking uncited-number WARN) |
| conditions/moon.md | standard | transformed | gaps(1), spots(1), fact-check(1), conservation-fix, cite-fix | transform applied with fixes: restored dropped conflict-attribution (Capt. Dave Hansen) in 3 spots, removed one over-reaching citation, synced evidence-file source list |
| conditions/sea-state.md | standard | transformed | spots(9), asr-uncertain(1) | transform verified - plain-statement rewrite, evidence split, and How-to-use section all conserve before-state facts; one meaning-drift wording fix applied |
| conditions/tide-and-slack.md | standard | transformed | spots(2), cite-fix(1) | transform applied - evidence split (2 observations), cite Ep.15 -> OpcKQPA3vAI resolved, How to use it in planning section added, layout v2 added |
| conditions/upwelling-and-turnover.md | standard | transformed | spots(8) | transform verified - attribution moved to cites/manifest, all before-content conserved, template skeleton + How to use it in planning section added compliantly, 0 dead links |
| conditions/water-color.md | standard | transformed | gaps(1), spots(3) | transform applied: attribution preambles moved to new evidence/water-color.md, Duane Diego cite resolved to HWx1jDTGsng, How to use it in planning + Evidence sections added, layout: v2 |
| conditions/water-regimes.md | standard | transformed | spots(2) | transform verified: plain-statement rewrite adds layout:v2, per-claim (cameron) cites, How to use it in planning section; linked bare Cortez Bank mention to locations/tanner-bank.md; no fact/cite/source dropped |
| conditions/water-temperature.md | standard | transformed | spots(3) | transform applied: attribution preambles retired, single-trip Cortez/Osborn observation split to evidence file with a one-line doctrine trace retained, per-bullet cites added to mechanism sections, dorado boundary enriched with E4vKwRaRueA, layout: v2 |
| seasonal/april.md | standard | transformed | gaps(1), spots(3) | transform verified: additive-only diff (cites, layout v2 + regime infobox fields, one mechanism-gap flag, 3 spot-harvest rows); zero claims reworded or dropped |
| seasonal/august.md | standard | transformed | spots(7) | layout:v2 + regime field added, 3 missing cites added to previously-uncited disputable claims, spot-harvest seeded (6 rows) |
| seasonal/february-march.md | standard | transformed | spots(1) | transform: added inline cites to 5 existing claims, stripped attribution preamble on open-item line, added layout:v2 + regime:cold, harvested one spot mention - no content lost |
| seasonal/june-july.md | standard | transformed | spots(9) | transform verified: additive-only diff (1 new cite on existing claim, layout:v2 + regime:warm-stable, 9 spot-harvest rows) - zero claims reworded or dropped |
| seasonal/may.md | standard | transformed |  | transform: added missing cites (S2L3KLSQ6Is) to 4 uncited claims, migrated to layout v2 with regime:warming, corrected one claim's wording to match transcript more precisely |
| seasonal/november-december.md | standard | transformed | spots(6), reg-claims(1), gaps(0), misplaced(0) | seasonal/evidence/november-december.md / transform: layout v2 + regime:transition added, 3 Observed blocks split to evidence with cited traces kept beside doctrine, meta-attribution/name-flag conflict framing rewritten to decision-rule-first (SCI current), mis-cited Academy Ep. 14 label corrected to plain cite after transcript check, unsupported 300 lb figure corrected to sourced 60-80/100+ lb split (Z3rZqy2Pi8E), regulatory closure claim scoped with jurisdiction/as-of/verify-current; ledger row added for corrected figure |
| seasonal/october.md | standard | transformed | spots(8) | none / additive-only diff: layout:v2 + regime:cooling added, 3 cites added to previously-uncited disputable claims (2 warm-band-track bullets, 1 everything-season claim), transcript-verified against OYOda6T3f-8 and XLVUhV8DW64; check-note.py clean; 100->106 lines |
| seasonal/september.md | standard | transformed | spots(2) | seasonal/evidence/september.md / migrated to layout v2 (regime:warm-stable field, regions gate widened socal-bight to +cortez-north for the BOLA content, 4 previously-uncited claims given cites, one Observed block + one single-observation claim moved to evidence with cited traces kept beside doctrine; before/after 85->98 lines + 34-line evidence file) |
| seasonal/year-anniversary-prior.md | standard | transformed | cite-unresolved(1) | seasonal/evidence/year-anniversary-prior.md / migrated to layout v2, split Cameron's water-state observation to evidence, added decision-rule framing consistent with species/yellowtail.md; 84->91 lines |
| bait/bait-tanks.md | standard | transformed | misplaced(1: barge-queue-timing duplicates making-bait.md, queued to relocation-queue.md), spots(2) | bait/evidence/bait-tanks.md / migrated to layout v2: source-named headings dissolved into content-based sections, attribution preambles replaced with compact cites, 3 Observed blocks split to evidence file with corroborating traces left in main note, decision frame added for 3-vs-5-scoop offshore floor conflict, mechanism gap flagged on 8-minute turnover figure; 378->251 lines note, +72 evidence; link-maintenance run for new evidence file |
| bait/fishing-live-bait.md | standard | transformed | spots(12) | bait/evidence/fishing-live-bait.md / migrated to layout v2: source-named headings dissolved into content sections, 4 Observed blocks + 3 single-trip claims split to evidence with corroborating traces, net-vs-hand-pick conflict given decision frame; verifier restored 4 facts the worker had dropped (depth parameter, missing cite, handling detail, two selection tells); 784->492 lines note, +86 evidence |
| bait/making-bait.md | standard | escalated |  | escalated: guard: out of scope for 'review: bait/making-bait.md': bait/bait-tanks.md |
| locations/bahia-de-los-angeles.md | geo | transformed | gaps:12 stubs:3 fc:2 spots:5 | zone page under cortez-north from 9 corpus sources + cameron; retyped location->zone on the v2 skeleton, 0 charted spots so no child pages; K22a8Ui8tWg re-scoped out (San Felipe mothership, kept in evidence), roosterfish 'more reliable further south' escalation corrected to what P36VGPPf120 actually says, 20-miles-north cite corrected; 12 gaps, 3 stubs, 2 fact-check rows, 5 spot-harvest rows |
| locations/bahia-magdalena-lopez-mateos.md | geo | transformed | gaps:11 stubs:3 fc:3 spots:6 | zone page under baja-pacific-south from 12 corpus sources; retyped location->zone on the v2 skeleton, 0 charted spots so no child pages; pulled in the Mag Bay material that had only lived in flyline/trolling/yo-yo/kite/marlin/wahoo notes (mangrove tide windows, estuary channel depth, Ridge-vs-Modesto-Main bank choice, untapped jig fishery), retired the promotional-seminar attribution preambles into the evidence file, kept the two season claims side by side with a decision frame; 11 gaps, 3 stubs, 3 fact-check rows, 6 spot-harvest rows |
| locations/bass-structure.md | standard | transformed | gaps(2), spots(7), asr-uncertain(4) | locations/evidence/bass-structure.md / transform applied, faithful to source, zero information loss; escalated for a type-taxonomy decision affecting 7 pending sibling notes (universal locations/ knowledge forced into spot-page type:location skeleton with parent:unknown) |
| locations/bays-and-harbors.md | standard | transformed | gaps(1), misplaced(0), spots(3), reg-claims(0), asr-uncertain(none) | transform verified, 2 fixes applied (cite corroboration + restored dropped depth figure) |
| locations/bight-geography.md | standard | transformed | gaps(3), misplaced(0), spots(16), reg-claims(0) | transform verified: conservation clean, new OYOda6T3f-8 claims spot-checked against transcript, v2 infobox/sections match template and prior precedent |
| locations/bightsst-eval-targets.md | standard | transformed | gaps(2), spots(10) | transform verified faithful, zero information loss, mechanically clean; escalated (repeat of open bass-structure.md taxonomy question) |
| locations/breakwalls-jetties-riprap.md | standard | transformed | gaps(1), misplaced(1), spots(7), reg-claims(0), asr-uncertain(2) | transform verified with 1 in-tree fix (evidence-heading mismatch corrected to mirror source section) |
| locations/cedros-island.md | geo | transformed | gaps:12 stubs:3 fc:1 | zone page (was type: location) from 44 sources, census zone 'Cedros / San Benitos'; no charted spots in the library; absorbed the queued Yellow Tail triangle geography; evidence file carries 44 observation lines and the Tackle Express gear cross-links |
| locations/island-structure.md | standard | transformed | gaps(1), misplaced(1, pre-existing queue row), spots(5), reg-claims(1) | transform verified, apply-with-changes: closed 2 uncited-claim gaps in the new What's there table; conservation and cite resolution otherwise clean |
| locations/loreto.md | geo | transformed | gaps:17 stubs:4 fc:2 spots:7 | zone page under cortez-south from 5 Loreto trip vlogs + P36VGPPf120 for the roosterfish contrast; retyped location->zone on the v2 skeleton, 0 charted spots so no child pages; added bank to waters for Six Mile Reef, dropped the uncited '250 miles south of BOLA' distance, split every trip observation into the new evidence file and retired the confidence/channel boilerplate into it; new material mined from the transcripts (Puerto Escondido launch, mothership/beach/panga access modes, bait-vendor sardine rig and dorado window, 20-mile/1-hour Carmen run, breakdown-and-tow, plumas troll, marlin… |
| locations/regions.md | standard | transformed | gaps(2), asr-uncertain(repeat of open type-taxonomy escalation) | transform verified, one conservation gap fixed in-tree (restored dropped finer-tier-can-be-added-later clause) |
| locations/sea-of-cortez.md | standard | transformed | gaps(4), misplaced(0), spots(3), reg-claims(0), asr-uncertain(1: captain name Joel/Joelle/hoell) | transform verified: conservation intact, 3 transcript spot-checks pass, mechanical check clean |
| locations/zone-lexicon.md | standard | transformed | gaps(3), spots(7), asr-uncertain(1) | transform verified faithful, zero information loss, mechanically clean; escalated (repeat of open bass-structure.md taxonomy question) |
| planning/day-plan-protocol.md | light | done | none | added layout:v2 + missing (cameron) cite on the SST-outlier doctrine sentence, no content changed |
| planning/electronics-and-sounder.md | light | done | spots(4) | layout v2 migration: attribution/date/confidence chatter moved to evidence file, plain-statement rewrite, conservation gap fixed by verifier (restored dropped ice-bag quote), 4 spot-harvest rows added |
| planning/fleet-intelligence.md | light | done | spots(3) | layout v2 migration, evidence split, plain-statement rewrite; verifier restored 3 conserved details (binoculars anecdote, 'number one mistake' framing, Everingham name) |
| planning/report-reading-and-forecasting.md | light | done | none | layout v2 migration, evidence split, plain-statement rewrite, 3 cites resolved (Blh2BA-7Ono, ILA6OMInWSM, OpcKQPA3vAI) |
| planning/search-and-glassing.md | light | done | gaps(1) | layout v2 migration, evidence split, plain-statement rewrite; verifier restored dropped rockfish link and stripped residual named attribution |
| planning/trip-length-selection.md | light | done | none | layout v2 migration, evidence split, plain-statement rewrite; verifier restored 2 dropped quote phrases |
| fish-care/dehooking-and-release.md | light | done | none | layout v2 migration, evidence split, plain-statement rewrite; verifier ran link-maintenance.py to regenerate backlinks, no content lost |
| fish-care/dorado-and-general.md | light | done | fc(1) | layout v2 migration, evidence split; corrected misattributed cite E4vKwRaRueA->5to3Q5P7w90 (verified), added missing fact-check-ledger row |
| fish-care/gaffing.md | light | done | spots(2) | layout v2 migration, evidence split, plain-statement rewrite, 3 Observed blocks moved to evidence, 2 spot-harvest rows added |
| fish-care/ikejime.md | light | done | none | layout v2 migration, plain-statement rewrite; verifier ran link-maintenance.py to regenerate README index |
| fish-care/sculpin-handling.md | light | done | none | layout v2 migration, plain-statement rewrite, Regulations section split out; check-note.py clean, no conservation loss |
| fish-care/tuna-care.md | light | done | misplaced(1) | layout v2 migration, evidence split, misplaced-content flagged + queued; verifier trimmed 4 out-of-scope net-new facts to stay within LIGHT-tier license |
| fish-care/wahoo-handling.md | light | done | none | layout v2 migration, plain-statement rewrite; verifier fixed one meaning-drift (misattributed questioner's 5-10 count figure hardened into session doctrine) |
| tackle/all-purpose-rod-line-rating.md | light | done | none | layout v2 migration, evidence split, plain-statement rewrite; verifier restored one dropped dorado link |
| tackle/bluefin-50-80lb-bait-outfit-ladder.md | light | done | none | layout v2 migration, evidence split, plain-statement rewrite; verifier restored dropped '(lightest)' designation and a dropped reel-sizing cross-note comparison, removed self-narration |
| tackle/bluefin-retail-setup-high-end-vs-budget.md | light | done | none | layout v2 migration, evidence split, plain-statement rewrite; verifier restored dropped 'expensive' framing quote and fixed sources list completeness |
| tackle/bluefin-rig-ladder-by-grade.md | light | done | none | migrated to layout v2 — stripped named-individual attribution/inline confidence to cites, split 1 Observed block to evidence, fixed 1 quoted heading + 1 relative-time phrase; check-note.py passes; verified faithful |
| tackle/composite-rod-blank-construction.md | light | done | none | LIGHT-tier v2 migration: stripped channel-status/attribution boilerplate, plain-statement rewrite, added layout: v2 + corroborating cite 48ZFXnCTTQE; verified faithful, link-maintenance re-run for README index |
| tackle/drag-setting.md | light | done | none | migrated to layout v2, per-source chronicle to 10 topical sections, house-style rewrite, evidence file split; verifier restored 2 dropped items (Carson's lever-drag method, Hansen's star-drag preference) |
| tackle/gear-classes.md | light | done | none | rail-rod citation apparatus compressed to spec table, style-guide v2.1 fixes, layout v2 added, evidence file split; verified faithful, no information loss |
| tackle/hook-assortment-by-trip-length.md | light | done | spots(2), asr-uncertain(Alijos Rocks/Mustad 94150) | LIGHT-tier v2 migration: meta-attribution/channel-status boilerplate removed, compact cites, layout: v2 added; verifier added evidence file for dropped presenter/confidence detail, spots logged |
| tackle/hooks.md | light | done | spots(9) | LIGHT transform 1051→614 lines, layout v2, evidence file split; verifier found and fixed conservation gap (18 source ids' attribution reconstructed into evidence file), 1 typo fixed |
| tackle/jig-rod-rating-selection.md | light | done | none | restructured to LIGHT-tier skeleton, provenance split to evidence file, plain-statement rewrite, 2 dead anchors fixed; verifier removed 1 banned self-narration phrase, all facts conserved |
| tackle/jigging-rod-guide-wrap.md | light | done | none | migrated to layout v2, stripped attribution-preamble/confidence chatter to compact cites, kept contested-doctrine names per exception; verified faithful, no information loss |
| tackle/lightweight-reel-pick-turners-outdoorsman.md | light | done | none | migrated to layout v2, presenter/channel provenance split to evidence file, plain-statement rewrite; verified faithful, link-maintenance re-run for backlinks |
| tackle/line-and-leader.md | light | done | spots(7), asr-uncertain(panelist-surname, illegible-knot-name) | LIGHT-tier v2 migration, attribution/confidence to evidence file, 2 observation blocks split; verifier restored 5 sources' dropped provenance in evidence file |
| tackle/offset-hooks.md | light | done | gaps(1) | LIGHT-tier v2 migration: attribution preamble to compact cites, stale hooks.md anchor repaired, hedge reworded to gap flag; verified faithful |
| tackle/reel-maintenance.md | light | done | none | LIGHT-tier v2 migration, 9 source-named sections dissolved into 13 topic sections, evidence file created; verifier fixed a dropped count and an ambiguous merged sentence |
| tackle/rod-action-testing-technique.md | light | done | none | restructured, attribution to compact cites + evidence file, layout v2; verifier fixed 1 meaning-drift inversion (taper-variation claim) |
| tackle/rod-and-reel-selection.md | light | done | spots(3) | LIGHT-tier v2 migration, house-style rewrite, evidence file created, decision frames added to 2 doctrine conflicts; verified faithful, all 27 cites conserved |
| tackle/rod-blank-and-component-materials.md | light | done | none | LIGHT-tier v2 migration, provenance moved to evidence file, stale anchor fixed; verifier fixed 1 unscoped-generalization drift on a presenter's personal practice |
| tackle/rod-length-for-angler-size.md | light | done | none | restructured to house style, provenance split to evidence file, layout v2; verifier fixed 1 quote-hardening drift and removed 1 banned reconciliation phrase |
| tackle/searcher-30lb-large-tuna-outfit.md | light | done | none | transform verified with in-tree conservation fixes (named-attribution drops + a direction-inversion bug) |
| tackle/searcher-40lb-all-around-tuna-outfit.md | light | done | gaps(1) | transform verified, two conservation gaps fixed (fly-lining hook scope, two-speed-reel causal detail in evidence) |
| tackle/searcher-50-60-80lb-flyline-outfit.md | light | done | none | transform verified — full conservation of parameters/observations across main note + new evidence file, corpus claims spot-checked against all 3 source transcripts, one v2.1 self-narration phrase fixed in tree |
| tackle/searcher-6-to-8-day-heavy-outfit.md | light | done | spots(2), asr-uncertain(season-window, reel-model-suffix, third-reel-identity) | transform verified clean — v2 layout, evidence split, cites conserved, no loss |
| tackle/searcher-alijos-rocks-ridge-7-day-quiver.md | light | done | spots(2), asr-uncertain(Avitz-Avet reel brand; seven strand monofilament wire caption) | v2 transform: plain-statement rewrite, evidence file split, layout v2 added; all doctrine, quotes, figures, cross-links conserved |
| tackle/searcher-big-tuna-rig-ladder.md | light | done | none | faithful v2 transform, cites added, provenance/confidence/sponsor detail + 2 observed catches split to new evidence file, no claims lost, doctrine conflict preserved with added decision frame |
| tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md | light | done | none | transform verified: plain-statement conversion clean, all product names/asr-uncertain flags/hook numbers/depths conserved into evidence split, link-maintenance 0 dead links |
| tackle/searcher-daytime-dart-jig-outfit-ladder.md | light | done | gaps(1) | transform verified faithful, evidence split compliant, no conservation or drift defects |
| tackle/searcher-finesse-live-bait-outfit.md | light | done | none | evidence file created; two video citations merged per-parameter into 20lb/15lb structure, 44lb-bluefin observation split to evidence with doctrine trace kept, stale anchors fixed |
| tackle/searcher-four-outfit-guadalupe-quiver.md | light | done | asr-uncertain(Captain Arch identity, Talica 20/25 reads) | transform verified, one minor conservation gap (dropped old faithful nickname) fixed in evidence file |
| tackle/searcher-lever-drag-reel-sizing.md | light | done | none | light transform verified: attribution split to evidence file, ASR flags and worked-capacity figures conserved |
| tackle/searcher-rail-rod-ladder.md | light | done | asr-uncertain(Tier 3 reel 16BX vs 16VISX) | transform verified, one on-camera hedge restored to evidence during verification |
| tackle/searcher-spring-bluefin-yellowtail-quiver.md | light | done | none | transform (light tier): plain-statement rewrite, cite insertion, evidence-file split for presenter/provenance detail |
| tackle/searcher-three-outfit-minimum-quiver.md | light | done | asr-uncertain(rod model 72 mismatch, Colt Sniper caption, 6X junior caption) | transform verified: attribution preamble split cleanly into evidence file, all before-facts traced into after-state with cites |
| tackle/searcher-yellowtail-livebait-sliding-sinker-rig.md | light | done | gaps(1) | transform verified, faithful split to evidence file, cites checked against transcript |
| tackle/spectra-hollow-vs-solid.md | light | done | none | transform applied with one restored claim (deleted TactX/Threadlock sponsored-caveat sentence, no relocation logged) |
| tackle/spinning-reel-bait-feeder.md | light | done | none | transform applied, attribution preamble retired to cite per v2 style guide, no facts lost, check-note.py clean |
| tackle/spooling-line-tension-and-twist.md | light | done | none | transform applied, light tier, 0 check-note warnings, no information loss found |
| tackle/star-drag-vs-lever-drag.md | light | transformed | none | transform verified faithful, LIGHT-tier prose/cite normalization, no information loss |
| tackle/tackle-express-accurate-tern-2-reel.md | light | transformed | asr-uncertain(guest name, Torx driver sizing, twin-drag stack mechanism, closing 165 lb anecdote) | transform applied with 2 verifier fixes (evidence-file wording contradiction, restored species-ambiguity caveat) |
| tackle/tackle-express-accurate-valiant-2-spj-reel.md | light | transformed | none | transform verified: evidence split conserved, quotes match transcript, link-maintenance run |
| tackle/tackle-express-bait-tank-time-saver.md | light | transformed | asr-uncertain(product names: double-8 octopus trailer; Gulp swimming mullets/grub series) | v2 transform verified, one dropped cross-reference restored to evidence file |
| tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md | light | transformed | none | transform verified: plain-statement rewrite, evidence split, contested-doctrine decision frame added, check-note.py clean |
| tackle/tackle-express-baja-light-setup-yellowtail-insurance.md | light | transformed | none | clean v2 transform, all specs/provenance conserved to evidence file, transcript-verified |
| tackle/tackle-express-bates-edc-100-reel.md | light | transformed | none | transform verified, one hedge-smoothing fix applied |
| tackle/tackle-express-bkk-titan-diver-swimbait-hooks.md | light | transformed | asr-uncertain(hook top-size 40 or 5, grommet final-lock action cut off mid-sentence) | transform applied, check-note.py clean, evidence split conserved all facts |
| tackle/tackle-express-casting-reel-for-seabass-yellowtail.md | light | done |  | light transform verified: style/cites/structure only, full conservation, check-note OK |
| tackle/tackle-express-cedros-four-rod-quiver.md | light | transformed | asr-uncertain(Daiwa Lexa 500 model number, resolved via cross-check with QEmxUIGmKbo) | transform applied: attribution preamble split to new evidence file, plain-statement cites added, table wording normalized, check-note.py and link-maintenance.py both clean |
| tackle/tackle-express-chad-fathom-lowprofile-surf-combo.md | light | transformed | none | transform verified, 2 conservation gaps found and fixed in-tree (dropped reel/rod claims restored) |
| tackle/tackle-express-charter-bait-tank-hook-kit.md | light | transformed | asr-uncertain(Aki Twist/Oy Twist/OSHAY hook names still unresolved) | transform: plain-statement rewrite + evidence split (layout v2, light tier) |
| tackle/tackle-express-ci4-plus-reel-features.md | light | transformed | none | transform verified, apply-with-changes: restored dropped provenance (titles/upload dates) into a new evidence file per established sibling pattern |
| tackle/tackle-express-daiwa-coastal-tw200-reel.md | light | transformed | none | transform verified, one dropped quote restored |
| tackle/tackle-express-daiwa-luvias-st-spinning-reel.md | light | transformed | none | transform applied cleanly: prose compressed to plain-statement style, cites added throughout, provenance/presenter detail split to new evidence/ file, layout: v2 added |
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
| locations/279-267-14-mile-bank.md | geo | transformed | gaps:13 spots:2 | new zone page verified against the coordinate census and 4 transcripts; 3 fixes applied (cite scope, superlative drift, relative time) |
| locations/474-711.md | geo | transformed | gaps:14 stubs:1 spots:2 | geo verify: new zone page, all coordinates/distances/bearings/areas reproduce from the census + spot library; 1 dropped corpus specific restored and 1 endpoint-choice inference qualified |
| locations/209-312.md | geo | transformed | gaps:9 stubs:2 spots:2 | new zone page verified — coordinates, distances, bearings and 12 nm clustering reproduce from the census/spot library; 1 mis-cite re-sourced, 1 source added to front matter, 2 evidence dates stamped, 1 tally corrected |
| locations/289-284.md | geo | transformed | gaps:13 stubs:1 spots:2 | applied with 5 verifier fixes: 1 cite misattribution, 1 direction error (seaward to inshore), 3 precision/scope wordings; all coordinates, distances and bearings independently recomputed and correct; census row unaltered |
| locations/north-9-mile-bank-178.md | geo | transformed | gaps:16 stubs:4 fc:2 spots:2 | geo zone page verified against census + spot library and 4 transcripts; two derived-distance errors fixed; 2 fact-check rows ledgered (South/Lower 9 Mile region anomaly, unmapped 'upper nine' reading) |
| locations/south-9-mile-bank-439.md | geo | transformed | gaps:12 fc:3 | zone page verified against the spot library and transcripts; 3 inverted bearings fixed, 3 cite-scope defects flagged |
| locations/e-butterfly-san-salvador-knoll.md | geo | transformed | gaps:11 spots:2 | apply-with-changes: new position-and-ladder zone page (zero corpus coverage); coordinates + census verified, ~30 distances recomputed; 5 fixes (distance mis-anchor, 2 false superlatives, over-broad universal, miscited source) |
| locations/101-425.md | geo | transformed |  | zone page written: 2 charted spots, 0 corpus notes; position-and-ladder page with 9 flagged gaps |
| locations/475-knuckle-upper-finger-bank.md | geo | transformed | gaps:15 stubs:1 spots:2 | new zone page under baja-pacific-north for the two-mark coordinate cluster the census carved out of the offshore-banks catch-all: Upper Finger Bank and 475 Knuckle, 3.6 nm apart on 218 degrees and the tightest bank zone in the region. Position-and-ladder page — no corpus source describes fishing either mark. Documented the two name collisions the zone sits at the centre of: the five depth-labelled Upper Finger Bank rockfish marks (162-426 ft) lie 7.6-12.7 nm NNW of the position charted under that name and stay in their own spot-library section, and the 475 Knuckle is 28.1 nm from the 475 in… |
| locations/banda-bank-todos-santos-island.md | geo | transformed | gaps:13 stubs:1 fc:2 spots:2 | apply-with-changes: position-and-ladder zone page verified against coordinate library + 3 transcripts; fixed 1 distance, 1 inverted bearing frame, 1 merged observation; 2 ledger rows raised (census grouping, ambiguous Todos Santos mention) |
| locations/311.md | geo | transformed | gaps:13 stubs:2 spots:2 | apply-with-changes: new 311 (Trask Knoll) zone page verified — census membership, 12/25 nm attach logic and ~20 derived distances reproduce; 6 transcript spot-checks clean; 1 fix (false neighbour claim in isolation ranking) |
| locations/sverdrup-bank-126.md | geo | transformed | gaps:15 spots:2 | zone page written: Sverdrup Bank (126) + Albatross Knoll, corpus-silent, positions and ladder only |
| locations/tanner-bank.md | geo | transformed | gaps:9 fc:1 spots:2 | apply-with-changes: corpus-rich outer-banks zone page (Tanner + Cortes) from 16 sources; coordinates, 8 derived distances, census and 10 cited parameters verified; 3 fixes (2 quote-fidelity, 1 conflicting Long Beach run distance now ledgered) |
| locations/hancock-bank.md | geo | transformed | gaps:13 stubs:1 spots:2 | zone page written: Hancock Bank + Northeast Bank, corpus-silent two-bank zone at the SW corner of the charted library; positions, ladder arithmetic and neighbour distances only |
| locations/12-mile-reef.md | geo | transformed | gaps:14 stubs:2 fc:0 spots:1 | zone page written: the 12 Mile Reef, a single-mark zone at the north end of the region in the Santa Barbara Channel (page did not exist). Corpus names the mark nowhere, so this is a position-and-ladder page: charted position (the mark itself, not a computed centre), the census arithmetic that made a lone spot into a zone (nearest charted position 35.8 nm, past both the 12 nm cluster cap and the 25 nm attach radius), the distance-name reading that the chart cannot check here, and the region's second-most-isolated-zone ranking. Scoped-adjacent material only, all labelled as stated for the… |
| locations/san-juan-seamount.md | geo | transformed | gaps:15 stubs:2 fc:0 spots:1 | zone page written: the San Juan Seamount, a single-mark zone on the western edge of the region (page did not exist). No corpus source names the mark, so this is a position-and-ladder page: charted position (the mark itself, not a computed centre), the census arithmetic that made a lone spot into a zone (nearest charted position Sverdrup Bank at 30.9 nm, past both the 12 nm cluster cap and the 25 nm attach radius; only three positions inside 50 nm), the fourth-westernmost position in the 391-spot library and the westernmost south of the Point Arguello corner, and an empty 125-350 deg arc out… |
| locations/bumps.md | geo | transformed | gaps:13 stubs:2 fc:0 spots:1 | zone page written: The Bumps, a single-mark zone on the southern edge of the charted Baja offshore grid (page did not exist). No corpus source names the mark, so this is a position-and-ladder page: charted position (the mark itself, not a computed centre), the census arithmetic that made a lone spot into a zone (nearest charted position Catchers Mitt at 31.3 nm, past both the 12 nm cluster cap and the 25 nm attach radius; nothing inside 30 nm in any direction), the four-single-mark-zone isolation ranking and the 380 pairing, the shape-name-family reading of the plural name against the fathom… |
| locations/380.md | geo | transformed | gaps:12 stubs:1 fc:0 spots:1 | zone page written: the 380, a single-mark zone at the southwest corner of the charted Baja offshore grid (page did not exist). No corpus source names the mark — not one transcript hit — so this is a position-and-ladder page: charted position (the mark itself, no computed centre), the census arithmetic that made a lone spot a zone (nearest charted position The Bumps at 31.4 nm, past both the 12 nm cluster cap and the 25 nm attach radius; nothing charted inside 30 nm, one position inside 45 nm), the isolation ranking (second-most isolated of 391; the four single-mark zones are the four most… |
| locations/guadalupe.md | geo | transformed | gaps:9 spots:0 fc:2 reg:2 | new zone page verified against 15 transcripts; 3 meaning-drift fixes + 1 miscite + 1 missing link applied |
| locations/alijos-rocks.md | geo | transformed | gaps:9 stubs:2 fc:1 spots:0 | new zone page under baja-pacific-south from 14 corpus sources; census zone with 0 charted spots (the spot library stops at San Quintin) so no child pages; pulled the Alijos material that had only lived in wahoo/yellowfin/yellowtail/dorado routers and the trolling/yo-yo/kite/wahoo-bomb technique notes into one zone page (surface-to-bottom rock, the deepest yo-yo tier, the wahoo bomb program, the 100 lb flyline, the kite/balloon plan); flagged the 488 mi vs ~400 mi run-distance conflict as contradicted-internal with a ledger row; 9 gaps, 2 zone-guide stubs, 1 fact-check row, 2 spot-harvest rows |
| locations/cabo-san-lucas.md | geo | transformed | gaps:10 stubs:5 fc:2 spots:2 | new zone page under baja-pacific-south from the 5 Cabo sources (no page existed); 0 charted spots in the library so no child pages. Two documented programs kept separate — the surf-line sierra troll (6 kt hoochies on wire, AM/sunset window, dirty-water eyesight cue) and the offshore troll (current-break work, dropback on 80 lb/#9 circle, medium-to-large marlin heads); pulled the zone-level access facts that had never left the transcripts (2 hr flight from John Wayne, clearing the harbor past El Arco, bait-boats-early), flagged the winter-only record (Nov/Dec/Jan) and the total absence of… |
| locations/la-paz.md | geo | transformed | gaps:10 stubs:4 fc:2 spots:5 | new zone page under cortez-south from the 3 StokedOnFishing La Paz episodes (no page existed); 0 charted spots in the library so no child pages. Wrote the zone as the region's structure end — three grounds at three depths (12 ft shallow rock, Isla Espiritu Santo island rock, the El Bajo high spot at 50 ft low / <=80 ft high) plus an unnamed crowded high spot — and separated the three documented programs (shallow-rock live-bait slow-troll on 40 lb with a counted 3-second hookset; flylined mackerel fished outside the pack; dropped-bait-then-slow-troll at El Bajo on 65 lb braid / 60 lb fluoro).… |
| locations/east-cape.md | geo | transformed | gaps:11 fc:5 spots:6 | created zone page + evidence pair from 11 sources; recovered YijeuGOYoVQ (logged as unextractable for want of an anchor note) — yields the beach ATV sight fishery, wahoo at 1-1.5 mi, radio blue-marlin bite; 5 fact-check flags (summer-vs-Dec-Apr framing, Kabul Eidos/Kabul movie as Cabo Pulmo, the point vs lighthouse point, ciraolo island + rink on area, unresolved billfish IDs); no coordinates published - zone has none |
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
| locations/la-270.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/286.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/175.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/kidney-bank-63.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/279-267.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/474.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/711.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/209.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/312.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/289.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/284.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/178.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/north-9-mile-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/south-9-mile-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/439.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/san-salvador-knoll.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/e-butterfly.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/101.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/425-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/upper-finger-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/475-knuckle.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/todos-santos-island.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/banda-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/patton-ridge.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/albatross-knoll.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/cortes-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/northeast-bank.md | gazetteer | done |  | mechanical: coordinates + parent zone |
| locations/el-arco.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-petroglyph.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/thetis-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/beach-in-front-of-buena-vista-beach-resort.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ciraolo-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/kabul-eidos-kabul-movie.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-paz-bait-containers.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-paz-roosterfish-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-paz-shared-high-spot.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/lighthouse-lighthouse-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/rink-on-area.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/benitos-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/bird-rock.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/camp-pendleton-coast.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/catalina-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cedros-island-west-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/coronado-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/dana-point-kelp-bed.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ensenada-point-reef.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/huntington.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/isla-san-martin.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-beach-breakwater.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/loreto-puerto-escondido.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/northwest-harbor.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/redondo.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/sacramento-reef.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-clemente-island-west-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-diego-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-nicholas-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/santa-rosa-flats.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/two-harbors.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/catalina-island-backside-below.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ensenada-high-spot-78-mi-from-the-hotel-coral-marina.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-beach-harbor-la-harbor-complex.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/mission-bay.md | gazetteer | pending |  | harvest: 2 mention(s) |
| locations/rainbow-harbor.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-diego-offshore.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/uncle-sam-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/43-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/catalina-offshore.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cow-cod-conservation-area.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/lighthouse-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/santa-rosa-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/alamitos-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/camp-pendleton-stretch.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/huntington-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-jolla-artificial-reefs.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-rasa-high-spot.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-beach-break-wall.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-beach-harbor.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/newport-pipe.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/palos-verdes.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/socal-artificial-reefs.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/152-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/277-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/boot.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/coast-guard-helicopter-port-launch-ramps.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/coronado-bridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ingraham-st-bridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-bocana-estuary-baja-california-sur.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-beach-alamitos-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/lopez-mateos-magdalena-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/magdalena-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/magdalena-bay-estuary-channel.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/newport-bay-newport-harbor.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/santa-barbara-island-nick-san-clemente-catalina-the-square.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/tanker-lanes.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/the-sunset-wall.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/9-mile-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/baja-lower-banks.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/huntington-beach-oil-platforms.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/181-182-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cedros-san-benitos.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/desperation-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/pendleton-artificial-reef.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/tanker-lanes-277-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/bolsa-chica.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cortez-bank-tanner-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/mag-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/shelter-island-san-diego-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/port-of-long-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/dono-baja.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/newport-harbor.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/cedros-island-baja.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/ensenada-baja.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/209-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/43-san-clemente-island.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/14-mile-bank-la.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/302-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/9-mile-bank-sd.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/avalon.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/catalina.md | gazetteer | pending |  | harvest: 3 mention(s) |
| locations/east-end-of-catalina.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-jolla-nw-corner.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/mexican-rockpile.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-diego-bay-entrance.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-onofre.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/oceanside.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/west-of-catalina.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/isaac-s-reef.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-rock-santa-ana-river-pipe.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/rat-s-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/rocky-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-clemente-island-desperation-point.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/shark-fin-flat-rock.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/torrance-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/14.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/302-371-west-end-of-catalina.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/below-clemente-complex-43-181-182-289-clemente-ridge-mackerel-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/catalina-island-west-end.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/coronados.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/east-400-west-400.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/gonzaga-bay.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/la-ventura-coastal-shelf.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/long-beach-federal-breakwater.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/marina-del-rey.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/newport-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/nine-mile-bank.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/northern-channel-islands.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/san-felipe.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/seal-beach-wall.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/surfside-wall.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/volume-square.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/14-mile-bank-209-267-complex.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/dump.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/alijos-rocks-the-ridge.md | gazetteer | pending |  | harvest: 1 mention(s) |
| locations/lighthouse-point-beach.md | gazetteer | pending |  | harvest: 1 mention(s) |
<!-- review:worklist:end -->
