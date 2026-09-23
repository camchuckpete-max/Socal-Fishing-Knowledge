# Judgment calls — the GATE B decision list

The calls the 2026-08 editorial review (sources/plan-review.md) could not make
for itself. CLAUDE.md names this document, alongside the coverage summary, as
the surface GATE B is decided against. Every entry below is an escalation
still marked `- status: open` in sources/escalations.md; the 54 closed ones
(38 guard-reverts, 11 check-note failures, 5 subagent failures) are noise and
are not listed.

**83 open calls of 137 escalations**, regenerable with `grep -c '^- status: open' sources/escalations.md`. Grouped by where the call lands so it can be triaged by area rather than read straight through.

| area | open calls |
|---|---:|
| locations | 38 |
| species | 12 |
| techniques | 6 |
| conditions | 2 |
| lures | 1 |
| rigging | 1 |
| cluster passes | 2 |
| unit-less / pipeline-wide | 21 |
| **total** | **83** |

Two standing decisions sit below the list, kept from the earlier version of this file.

## locations (38)

**`locations/289-284.md`**

- *2026-09-02 · verify-escalate* — The rollover-map flag engages the adjudicated (Cameron, 2026-08-26) ruling on locations/bight-geography.md ('the map stands, and it is not going to be re-sourced to another video'). The flag surfaces that YZtX1MiT0y8 does carry the map near-verbatim (01:33-02:06) and that ~12 zone pages already cite it — Cameron should decide the…

**`locations/385-238-475.md`**

- *2026-08-25 · verify-escalate* — Five pre-existing transcript-drift issues INHERITED from already-committed notes (locations/ensenada.md, species/bluefin-tuna.md), out of scope for this unit, belong in sources/fact-check-ledger.md: (1) 'breezing and kite-raised' bluefin — Ix0gG0-l3v0 says 'up on top' and the kite produced only a swirl, nothing landed; (2) '4 fish day…

**`locations/anacapa-island.md`**

- *2026-08-29 · verify-escalate* — harvest recorded 1 mention but transcript grep (incl. ASR garbles like 'nana capitol') finds 6 hits across 5 videos; Cameron should decide whether remaining gazetteer units need a transcript-level name grep before gap flags are trusted, and whether already-built low-mention spot pages need a re-sweep

**`locations/banda-bank-todos-santos-island.md -> split (locations/ensenada.md + locations/punta-banda-santo-tomas.md)`**

- *2026-08-29 · verify-escalate* — Whole-zone dissolution, not a content move, and un-executable by the relocation pass on four mechanical counts: (1) it requires deleting locations/banda-bank-todos-santos-island.md and locations/evidence/banda-bank-todos-santos-island.md, and guard.py CONSERVATION forbids deleting a note or evidence file (auto-revert); (2) the row names…

**`locations/bass-structure.md`**

- *2026-08-28 · verify-escalate* — Cameron should decide whether universal cross-zone notes in locations/ (bass-structure.md + 7 pending siblings: bays-and-harbors, bight-geography, bightsst-eval-targets, breakwalls-jetties-riprap, island-structure, regions, sea-of-cortez, zone-lexicon) get a distinct type (or a template amendment) instead of being forced into the…

**`locations/bightsst-eval-targets.md`**

- *2026-08-28 · verify-escalate* — Same open type-taxonomy question as the bass-structure.md escalation (sources/escalations.md, 2026-08-28T17:04:44Z), which names this note as one of 7 pending siblings — forces a universal cross-zone reference index into the spot-page type:location skeleton with parent:unknown and two structurally-inapplicable sections flagged as corpus…

**`locations/catalina-island-front-side.md`**

- *2026-09-01 · verify-escalate* — sources/spot-lists.md charts Arrow Point (118 32.274) and Lions Head (33 27.235) on the CLOSED side of the MPA boundary rules this page publishes for them — a boat navigating to either cameron-sourced waypoint would be inside the SMCA; neither arrow-point.md nor lions-head.md records the discrepancy; regulatory, needs correcting at source

**`locations/cedros-island.md`**

- *2026-09-01 · verify-escalate* — fog/radar passage is a Simrad sponsor spot (Gulf of Mexico/Venice marina) misattributed as Cedros captain doctrine, and the page is internally inconsistent on whether Dono is in-zone — both need a follow-up transform/relocation unit, not just flags

**`locations/coronados-230-302-226.md`**

- *2026-08-25 · verify-escalate* — Zone is gated socal-bight and badged [SoCal only], yet the 371 sits ~6.7 nm on the Mexican side of the census's approximated maritime boundary (census takes a cluster's region from its first member). Page flags it and says verify off a chart; Cameron should decide whether a jurisdiction-straddling zone is acceptable under the region…

**`locations/cortez-south.md`**

- *2026-08-25 · verify-escalate* — roosterfish 'more reliable further south' propagated to cortez-south/cortez-north/bahia-de-los-angeles, but P36VGPPf120 [00:12:03] states no reliability direction ('higher up in the Sea of Cortez as well') — Cameron to adjudicate across all three notes

**`locations/desperation-reef.md`**

- *2026-08-29 · verify-escalate* — Pre-existing false hedge 'source does not say which side' in san-clemente-island-back-side.md:152 + its evidence file (contradicted by DnSqw4r7A1s); and the 'West End tuna zone' name conflict may be a KB artifact unsupported by Rb5I2ljAqeE

**`locations/gonzaga-bay.md`**

- *2026-08-30 · ladder-rung + cross-note-misattribution* — (1) Ladder: Gonzaga Bay is bay-scale like Bahia de los Angeles (which is type: zone), but was queued as a spot row and the census derived no zone for it, so the page parents straight to the region locations/cortez-north.md — Cameron to decide whether it should be promoted to type: zone. Same open question already standing on…

**`locations/ingraham-st-bridge.md`**

- *2026-08-30 · verify-escalate* — Cameron should confirm whether the spoken 'Ingram/Ingraham Street Bridge' spotty spot inside Mission Bay is the same feature as the charted 'Mission Bay Park Ingraham St Bridge Rubble' (32°45.930'N 117°16.278'W); three already-committed places assume it is (species/spotted-bay-bass.md Zone guides link,…

**`locations/isla-espiritu-santo.md`**

- *2026-08-29 · verify-escalate* — locations/la-paz.md Spots section now contradicts itself — its prose says no place in the zone has a public name plus a charted position so no spot pages hang below it, and that all five are logged in the spot harvest rather than minted as pages, but the generated children block directly below now lists Isla Espiritu Santo; fix is one…

**`locations/la-bocana-estuary-baja-california-sur.md`**

- *2026-08-30 · ladder-rung* — the Estero is a sub-feature of the La Bocana camp (itself type: location), but only container rungs generate child lists, so the page parents to the region page baja-pacific-south.md and the camp/estuary relation is carried in prose only
- *2026-08-30 · worker-escalate + verify-escalate* — Ladder rung: the Estero is a sub-feature of the La Bocana camp, but the camp is itself type: location (a spot, not a container rung), so the child parents past it to the region page baja-pacific-south.md and the camp/estuary relation is carried in prose only. Cameron should decide whether La Bocana warrants a zone rung, or whether the…

**`locations/la-bocana.md`**

- *2026-08-29 · verify-escalate* — (1) locations/baja-pacific-south.md still lists La Bocana under 'Named grounds the census derives no zone for - flagged stub', now stale prose. (2) Rung question: this page is type: location parented directly to a region, skipping the zone rung; its three sibling children of baja-pacific-south are all type: zone and the region-page…

**`locations/lopez-mateos-magdalena-bay-boca.md`**

- *2026-08-30 · overturned-sibling-verdict* — PUBLISHED where a sibling row said SKIP. worklist:514 (locations/boca.md, committed 7a03c24d 2026-08-29 22:32) skipped the same feature and pre-adjudicated this row — "sibling row locations/lopez-mateos-magdalena-bay-boca.md is the same feature and should skip identically". Both legs of that verdict fail for this slug: (1) the…
- *2026-08-30 · verify-escalate* — Worker published a page where sibling row locations/boca.md (7a03c24d) skipped the same feature and pre-adjudicated this row as 'should skip identically'; CLAUDE.md's no-public-name/no-charted-identity rule points to skip, but locations/magdalena-bay-estuary-channel.md and locations/the-ridge.md were published in the same phase on the…

**`locations/magdalena-bay-estuary-channel.md`**

- *2026-08-30 · stale-parent-crossref* — locations/bahia-magdalena-lopez-mateos.md Spots section still states 'No ground in this zone has a charted position in the KB, so no spot pages hang below it' and lists no estuary-channel bullet, but two spot pages now hang below it (the-ridge.md and this page). Parent prose is out of scope for a gazetteer unit (only the generated…

**`locations/north-county-artificial-reefs.md`**

- *2026-08-25 · verify-escalate* — 38 library waypoints published as zero spot pages vs CLAUDE.md 'EVERY spot gets a page'; Cameron to rule: one page per series, 38 mechanical pages, or formal sub-pixel-cluster exemption — same question hits San Diego ARs, International Reef, Torrey Pines
- *2026-09-01 · verify-escalate* — Oceanside AR fails the sub-pixel-cluster test: spot-lists.md L16 and zone-lexicon.md list 1A-1H/2A-2L as one cluster but the coords span 2.18 nm (~4 MUR pixels) — Cameron must decide whether Oceanside splits into 1-series and 2-series cells (zone-census question, out of unit scope). Second call: the Pendleton 35-40 ft depth either…

**`locations/northwest-harbor.md`**

- *2026-08-30 · verify-escalate* — The drop-to-bottom / wind-10-or-15-turns / free-spool-back-down cadence is localized to Northwest Harbor at locations/san-clemente-island-front-side.md:152 and this page propagates it to the spot rung, but in iQLyBzhOSi8 the team leaves the harbor at 08:39 to run down the front, describes water too deep for the harbor's 6 ft shallow-rock…

**`locations/point-loma.md`**

- *2026-09-01 · verify-escalate* — 3 gap flags are known-false (kwMIgkCtFUE, KVdnRJYq4jU, wysZwsjAkVs, YAKOv9bXKO0, IH4y6GM6BIY cover ports/landings, structure relief, start-and-move) so the note needs a re-transform + sources front-matter update; also the worker committed 4da19a3c directly, bypassing the wrapper/guard

**`locations/regions.md`**

- *2026-09-01 · verify-escalate* — verifier found no working-tree diff for the factcheck worker pass and could not confirm whether the zero-flag outcome (all claims cameron-attributed, no contradictions found) is legitimate or a missed worker step

**`locations/ridge-uncle-sam-bank.md`**

- *2026-08-29 · zone-page-stale-prose* — locations/baja-pacific-south.md still carries "The Ridge / Uncle Sam Bank" as a flagged stub under "Named grounds the census derives no zone for" and omits it from the Zones table, and locations/alijos-rocks.md Spots says both it and Thetis Bank "are carried as flagged stubs on Baja Pacific — South" — both are now stale, the page exists.…
- *2026-08-29 · verify-escalate* — ridge name-collision: species/evidence/wahoo.md treats the Magdalena-area 'the ridge' as the same ground while the new page keeps them apart under unverifiable; plus stale flagged-stub prose on baja-pacific-south.md + alijos-rocks.md and the zone-vs-spot ladder rung

**`locations/san-benito-island.md`**

- *2026-08-29 · verify-escalate* — locations/cedros-island.md still stamps the Cedros catch-and-release operator agreement 'on or before 2023-05-24' where sources/regulatory-claims.md reframed it to on-or-before 2023-03-26 (ZBRSB4iwtbU); zone page out of scope for this unit

**`locations/san-diego-artificial-reefs.md`**

- *2026-09-01 · verify-escalate* — The four Mission Bay Park waypoints sit at 117 16.050-16.517 W (the Pacific Beach AR longitude band, west of Mission Bay water) with nearshore-coast child pages, so the page's Inside/Outside split, no-ocean-crossing access line and waters bay-harbor tag rest on an in-bay premise the coordinates contradict; plus Pacific Beach AR absent…

**`locations/san-felipe.md`**

- *2026-08-30 · verify-escalate* — sea-of-cortez.md and cortez-north.md#season-shape still say the trip is undated/no-season while dEPuDrhoClM dates it November 2022; and 'a week to ten days' is stated uncited in cortez-north.md (x2) + sea-of-cortez.md with no corpus source — Cameron to say whether it came from the operator schedule outside the corpus; a cross-note pass…

**`locations/san-miguel-island.md`**

- *2026-08-29 · verify-escalate* — Yellowtail row + CDFW no-retention claim rests on Z3rZqy2Pi8E auto-caption 'a really nice yellow ... cant keep them in Southern California waters'; yellowtail retention is legal in CA while yelloweye rockfish is not — caption likely dropped 'eye'. Claim left untouched because the same inherited doctrine already sits in…

**`locations/santa-cruz-island.md`**

- *2026-08-29 · verify-escalate* — inherited meaning inversion on `CMQkHQMxbXM` (2022-08-03, 00:02:06–00:02:18). The transcript says the barracuda zone was not "doable up there unless you're on a sport[boat] — but maybe not even then", i.e. the wind vetoed the PRIVATE boat first. Three already-committed notes state the opposite: locations/anacapa-island.md ("reachable…
- *2026-08-29 · verify-escalate* — CMQkHQMxbXM 00:02:06-00:02:18 says the zone was not doable except on a sportboat (a veto on the PRIVATE boat); the inverted reading 'reachable only aboard a private boat' is already committed in locations/anacapa-island.md, species/evidence/barracuda.md and locations/289-284.md, which this unit cannot touch. Cameron should adjudicate…

**`locations/santa-rosa-island.md`**

- *2026-08-30 · verify-escalate* — Inherited router error propagated: halibut squid-bed list says Coronados but OpcKQPA3vAI names Santa Cruz (fix belongs in species/california-halibut.md); 'with squid present' qualifier on the 22-fish day inherited from species/white-seabass.md is not in HnqiE05vdXs

**`locations/slide-152-277.md`**

- *2026-08-25 · verify-escalate* — species/striped-marlin.md (lines ~81-82, still pending) carries the same unsupported claim that the ~160 lb 3qSY328fFYo marlin was taken on a live mackerel dropback bait — the transcript says it was released on the flying-fish jig; out of scope for this unit, needs correcting in its own review.

**`locations/socal-bight.md`**

- *2026-08-25 · verify-escalate* — The region page's Offshore banks table still carries 'The Boot (504) / 307 | 2 | Flagged stub - no corpus source yet', but 5to3Q5P7w90 names the Boot for marlin (Masters tournament weekend, 2022-09-14 report) and that is now written up in locations/boot-504-307.md. The stub row is stale; out of scope for this unit (parent must not be…

**`locations/tanner-bank.md`**

- *2026-09-02 · verify-escalate* — Flag 4 supersedes a standing 'resolved — no action required' ledger row (Long Beach 90-vs-110 mi spread): nQvJnfb5jQ4's '90 Mi off the coast of Long Beach' is stated OF Cortez, not Tanner, inverting the near-end/far-end assignment and unsettling the page's Getting-there resolution — Cameron should rule

**`locations/zone-lexicon.md`**

- *2026-08-28 · verify-escalate* — One of the 7 named pending siblings in the open bass-structure.md type-taxonomy escalation (sources/escalations.md, 2026-08-28T17:04:44Z) — parent:unknown forced into the spot-page type:location skeleton, same pattern already escalate(apply)'d for bightsst-eval-targets.md; Cameron still needs to rule on it before the remaining siblings…

## species (12)

**`species/barracuda.md`**

- *2026-08-30 · verify-escalate* — barracuda note contradicts Cameron's adjudicated 2026-08-26 wire ruling in species/bonito.md ('no wire; being bitten off is rare') — barracuda Terminal line, 'Getting bit off' router row and half of Doctrine & conflicts assume the opposite; flagged in place, not reconciled; Cameron must rule whether the adjudication extends to barracuda

**`species/bluefin-tuna-trolling.md`**

- *2026-08-30 · cross-note-mistarget* — the note routes flat-fall execution to the wrong page — "flat-fall depth and mechanism live in [knife jigging](../techniques/knife-jigging.md#reach-for-this-when)" — but techniques/knife-jigging.md carries no flat-fall depth or mechanism content, and techniques/flat-fall-jigging.md exists and is the correct target. Not a claim error, so…

**`species/bluefin-tuna.md`**

- *2026-08-24 · verify-escalate* — calendar-vs-water-state decision frame now effectively ranks Cameron's water-first stance above the corpus year-anniversary prior, adjudicating a conflict Cameron is a party to; Cameron's kite-since-July-2026 / helium-balloon-ruled-out / 80-140 lb foamer-preference items flagged misplaced-content and queued to profiles/cameron/tackle.md…
- *2026-08-30 · verify-escalate* — (1) new unverifiable DSL flag sits under the (cameron) food-following-vs-reaction-bite sentence and questions the risen-layer premise that cameron claim rests on (ext-verify ledger row 72); (2) ledger row 69: the California/CDFW jurisdiction on the two-fish bag limit is the note's own framing, not sourced; (3) two inline flags overstate…

**`species/bluefin-tuna.md -> profiles/cameron/tackle.md`**

- *2026-08-29 · verify-escalate* — executed with the removal-plus-evidence-pointer workaround before Cameron ruled on the guard-protected profiles/ question; Cameron must confirm that workaround IS the ruling. Note the helium-balloon-assist item now lives only in species/evidence/bluefin-tuna.md and in no profile — if profiles/ is later unprotected it still needs landing…

**`species/sand-bass.md -> species/sand-bass-alabama-rig.md`**

- *2026-08-29 · verify-escalate* — commit-note.py set_relocation_status keys on src alone and takes the first match, so any src with 2+ queue rows mis-stamps; ~13 rows across 6 multi-row srcs still queued; key on src+dst

**`species/skipjack-tuna.md -> profiles/cameron/README.md`**

- *2026-08-29 · verify-escalate* — destination profiles/cameron/README.md carries NO line for this interest and the guard blocks writing profiles/, so the interest lives only in species/evidence/skipjack-tuna.md — Cameron must land 'interested in rare/unusual species and oddball bycatch, not just target fish' in his profile himself; also a cameron-cited Doctrine &…

**`species/striped-marlin.md -> profiles/cameron/README.md`**

- *2026-08-29 · verify-escalate* — same trigger as the skipjack row — profiles/ is guard-protected and the README carries no marlin line, so Cameron's stated intention to troll marlin from the panga lives ONLY in species/evidence/striped-marlin.md; Cameron must land it in his profile or rule on unprotecting profiles/ for the relocation pass

**`species/wahoo.md -> species/wahoo-live-bait.md`**

- *2026-08-29 · verify-escalate* — the 4uNPLknRAQg free-spool trigger was mis-characterized upstream as 'bait gone dead'; transcript gives the same failed-hookset trigger as vNIazq1aVwc, turning a three-way split into proactive vs twice-corroborated reactive — Cameron should confirm the reframing; nothing reconciled, decision frame intact

**`species/white-seabass.md -> species/white-seabass-hatchery-program.md`**

- *2026-08-29 · verify-escalate* — The OREHP/HSWRI program history is correctly identified as misplaced (no where/when/how-to-fish content), but the destination has no legal shape: templates/README.md lists no type for a fishery-management or conservation page. type: species forces the 11-section router skeleton and six infobox fields onto a page that can fill none of…

**`species/yellowtail-dropper-loop.md`**

- *2026-09-02 · verify-escalate* — verifier found no working-tree diff for the factcheck worker pass and could not confirm whether the zero-flag outcome (17/17 claims verified against SAltQjih0ms/YntRJAN88fs/HTowqnwAMeA, no contradictions) is legitimate or a missed worker step

**`species/yellowtail.md -> locations/cortez-bank.md`**

- *2026-08-29 · verify-escalate* — dst redirected at execution to locations/tanner-bank.md; two gazetteer worklist rows still schedule the page the review decided not to build — sources/review-worklist.md:422 locations/cortez-bank.md and :821 locations/cortez-bank-tanner-bank.md, both pending, would produce duplicate pages under the variant spelling

## techniques (6)

**`techniques/drop-shot.md`**

- *2026-08-30 · worker-escalate* — worker self-committed and pushed 62ea26fb directly instead of leaving the patch in the working tree, bypassing the orchestrator's independent verifier step entirely; post-hoc verification confirms the content (new contradicted-by-source flag, miscited video ID _XfScSliRVk vs actual source _rcxIWhNMSE/M2qZiY2lR98) is accurate and…

**`techniques/foamer-casting.md`**

- *2026-08-27 · verify-escalate* — The before-text explicitly flagged the surface-iron retrieve speed as a not-reconciled conflict (burn-it-back vs. wind-it-real-slow). The transform rewrote it into a decision rule (default to burn, drop to real-slow as tough-foamer fallback) — well-grounded in AodUBhxPts8 but resolves a conflict the source note deliberately left open.…

**`techniques/sliding-sinker.md -> species/cabrilla-sliding-sinker.md`**

- *2026-08-29 · worker-escalate* — content is misplaced but the queued destination may be wrong: the Cortez build is a 100 lb-class grouper program (12/0 on 300-400 lb, broomtail on dEPuDrhoClM) while species/cabrilla.md is the 5-17 lb leopard grouper, and species/evidence/cabrilla.md:97-105 already recorded the opposite decision. Cameron to pick: (a) cabrilla.md is the…

**`techniques/sliding-sinker.md -> species/snook-sliding-sinker.md`**

- *2026-08-29 · verify-escalate* — the sibling cabrilla row escalated the same classification question and this one was resolved rather than escalated: a mixed grouper-and-snook build now lives on a single-species page with the unnamed ~100 lb grouper as bycatch context - Cameron should confirm one answer covers both rows

**`techniques/surface-iron.md -> profiles/cameron/rods.md`**

- *2026-08-29 · verify-escalate* — profiles/ is guard-protected (scripts/review/guard.py:58) so no relocate unit can land content at a profiles/ destination — harmless here (dst already held both facts) but two pending rows would be real information loss as removal-only: species/bluefin-tuna.md -> profiles/cameron/tackle.md (kite/helium/July-2026 absent from tackle.md)…

**`techniques/yo-yo-iron.md -> profiles/cameron/rods.md`**

- *2026-08-29 · verify-escalate* — The restored 10 ft Phoenix Axis sentence traces solely to memory-export-2026-08-11.md:15 where it is a cameron OPEN ITEM (rarely used, wants reps, considering yo-yoing with it), so stating it as doctrine violates the CLAUDE.md Cameron nuance; Step-3-era defect, out of a relocation pass's scope — Cameron to decide…

## conditions (2)

**`conditions/deep-scattering-layer.md`**

- *2026-09-01 · worker-escalate* — worker agent returned garbage: 'I'll wait for the background agents completion notifications rather than polling' with no LOG line and no commit; treated as subagent-failure per protocol

**`conditions/tide-and-slack.md`**

- *2026-09-01 · worker-escalate* — worker agent returned garbage: 'Waiting for the first verification batch to complete before finalizing the fact-check flags.' with no LOG line and no commit; treated as subagent-failure per protocol

## lures (1)

**`lures/cedar-plug.md`**

- *2026-08-31 · verify-escalate* — worker self-committed and pushed (1e6236ed) instead of leaving a working-tree diff for verification; content verified sound post-hoc but bypassed the normal wrapper flow

## rigging (1)

**`rigging/flying-fish-harness.md`**

- *2026-08-31 · worker-escalate* — worker subagent produced non-conforming garbage output instead of a LOG line, working tree left clean/untouched

## cluster passes (2)

**`cluster:cabrilla`**

- *2026-09-02 · out-of-scope-finding* — Two findings land outside this cluster row's guard scope (the row lists only the 5 technique/lure members, not the species-technique sub-articles). (1) STALENESS SWEEP: species/cabrilla-yo-yo-iron.md's 'Differs from the general method' bullet 1 says the general method 'positions up-current of a metered school or the bottom and…

**`cluster:calico-bass`**

- *2026-09-02 · stale-anchors* — link-maintenance reports 203 stale anchors repo-wide (0 dead links) and does not fail on them; 9 sit in this cluster alone, all from the plain-statement rewrite dropping attribution tails from headings. Flagged the 3 router-side ones and ledgered the rest rather than seeding ~200 per-note flags — needs one mechanical anchor-repair pass

## unit-less / pipeline-wide (21)

**`EiItVWqFMYc`**

- *2026-08-14 · evaluator-escalate* — The added Sublegal ('short') lobster handling section frames redepositing a short lobster as legal via a not-possessing-it technicality, positioned beside the species note's release-it-immediately doctrine; regulatory-adjacent content about lobster possession/release law that Cameron should review before it stands published.

**`G6YRT4HNxr8`**

- *2026-08-14 · evaluator-escalate* — freshwater three-hook-cap claim is a gear-limit-flavored claim under CDFW's purview; hedged as Castro's personal operating rule (no jurisdiction/as-of stamp by design since unverified) — confirm framing is acceptable

**`GptrotE0x5M`**

- *2026-08-14 · evaluator-escalate* — the flyline.md addition states a circle-hook-mandatory claim as a Mexican sportfishing regulation (jurisdiction/as-of-date/verify-current flag are present and compliant with CLAUDE.md's regulatory-claim rule) — per evaluate-unit.md's mandatory escalation trigger, any regulatory claim must be flagged for Cameron's review regardless of how…

**`HMdrP4-i9MM`**

- *2026-08-14 · evaluator-escalate* — sand-bass.md's new Observed block states a numeric legal-size figure (14 in) leaning on calico-bass.md's already-flagged CDFW entry rather than restating its own regulatory citation — confirm cross-referencing is acceptable vs a standalone flagged citation

**`MUpvP-Yl2R0`**

- *2026-08-15 · evaluator-escalate* — species/california-halibut.md adds a CDFW 22in legal-minimum-size claim for California halibut (jurisdiction/as-of-date/verify-current flag present and compliant) - per evaluate-unit.md's mandatory trigger, every regulatory claim goes to Cameron regardless of correct labeling

**`QSmE3mdEL28`**

- *2026-08-14 · evaluator-escalate* — (1) router-table fix in species/yellowtail.md changes acceptance-test output (live-bait slow-troll now sourced for Cedros resident structure instead of no-source stub) - confirm row split reads correctly; (2) new catch-and-release content is framed as on-camera crew ethic but touches the Cedros 2023 regulatory catch-and-release change -…

**`Qs9oEsh3b_w`**

- *2026-08-14 · evaluator-escalate* — species/california-spiny-lobster.md's new Gear limits (two-person minimum to fish full 10-net boat limit) and Buoy marking (marker vs tape by shared-license gear) bullets are new regulatory/compliance guidance — flag for Cameron's Gate B review

**`Rf1HKJG-SDg`**

- *2026-08-14 · evaluator-escalate* — mandatory trigger — patch adds regulatory claim (43-bank rockfish closure→bluefin effort shift) correctly formatted with jurisdiction/as-of-date/verify-current flag, needs Cameron's review of current CDFW rockfish-closure status before Gate B

**`Y1xeieQI3B4`**

- *2026-08-14 · evaluator-escalate* — rockfish-lingcod.md Observed block restates an on-camera '20 fish per day' boat allowance figure (bag-limit-shaped claim) without jurisdiction/as-of stamping; verify-current caveat added but should go to Cameron for review since it's adjacent to CDFW/CPFV bag-limit territory

**`Y2bXn44lfqo`**

- *2026-08-14 · evaluator-escalate* — species/white-seabass.md's new Broodstock/hatchery collection context bullet states fishing inside a Catalina MLPA is otherwise closed to the public (California/CDFW) — regulatory closure claim; Cameron should confirm the framing/date-stamp before treating as canonical.

**`Zo92MG459gQ`**

- *2026-08-14 · evaluator-escalate* — calico-bass.md addition reframes the recording date of the Cedros 100%-catch-and-release policy claim as on-or-before 2023-05-24 (not October 2023) - confirm this redating doesn't need to update the claim's as-reported date/verify-current framing per the regulatory-claim escalation trigger

**`fDSd9kqwYW0`**

- *2026-08-14 · evaluator-escalate* — species/rockfish-lingcod.md's new Observed block reports a 'fulfilled our 10 around on the rockfish' bag-limit figure — a regulatory claim, correctly hedged as an on-camera anecdote not current guidance; Cameron should confirm hedging is sufficient

**`fK2AT460xW4`**

- *2026-08-14 · evaluator-escalate* — species/yellowfin-tuna.md's Situations to techniques router table gained a new row (dolphin/porpoise-pod dropper rig) - a router-table change, mandatory escalation per checklist item 5 even though the addition is accurate and additive; Cameron should confirm the new row belongs in the router at GATE B review.

**`iQLyBzhOSi8`**

- *2026-08-14 · evaluator-escalate* — On-camera slate reads 2012 for the fourth annual COOC, while already-committed parts 2 (PKf7G3uL4io) and 3 (IATPg9110CE) entries assume ~2014 from the shared YouTube upload date only; Cameron should decide whether those two entries need the same on-camera-year caveat since all three parts may document the 2012 tournament, not 2014.

**`lF6jQklDCrY`**

- *2026-08-14 · evaluator-escalate* — Regulatory claim (SoCal rockfish season reopen date + historical depth-limit progression 300->350->460 ft) added to species/rockfish-lingcod.md — mandatory escalation trigger per evaluate-unit.md even though the content is well-caveated as a dated, self-admittedly-uncertain historical data point, not current guidance.

**`ldVj0BoB-kE`**

- *2026-08-14 · evaluator-escalate* — Cedros Island 2023 voluntary 100% catch-and-release for calico/grouper/black seabass is a regulatory/policy-adjacent claim; Cameron should confirm operator-agreement framing (distinct from CDFW/Mexican-government rule) and current status before treating as actionable guidance.

**`ntQXxcH5sjI`**

- *2026-08-14 · evaluator-escalate* — species/bluefin-tuna.md's Situations to techniques router table gained a new row (shallow bait-ball marks / yo-yo iron) — router-table change, mandatory escalation per acceptance-test trigger even though accurate/faithful/additive; Cameron should confirm the new row belongs in the router at GATE B review.

**`r6j5w40fVHI`**

- *2026-08-14 · evaluator-escalate* — patch introduces a regulatory claim (CA/CDFW calico bass 14in minimum legal size); confirm the size is still current before treating as verified

**`ty8FtA3Y2bA`**

- *2026-08-14 · evaluator-escalate* — Cameron should review the 10-inch minimum-size claim in fish-care/sculpin-handling.md — it's a regulatory claim (CDFW size limit) sourced from a 2022-04-16 video and needs a current-regs check before the KB relies on it

**`usHl-4SfqDA`**

- *2026-08-14 · evaluator-escalate* — two CDFW regulatory claims added (bluefin bag limit 2/person/day in species/bluefin-tuna.md; spotted-bay-bass no-minimum-size in species/spotted-bay-bass.md), both jurisdiction/as-of/verify-flagged per convention but need Cameron's verify-current confirmation before Gate B

**`xzIaUEDklrE`**

- *2026-08-14 · evaluator-escalate* — species/bluefin-tuna-trolling.md adds a StokedOnFishing observation where spreader bar selects for bigger fish over Mad Mac, opposite to Cameron's registry-high presentation-size axis (small forage->bar, large forage->Mad Mac); flagged side-by-side as a non-reconciled conflict per convention, but needs Cameron's read before treated as…

## Standing decisions

Kept from the earlier version of this file: not open calls, but context the
open ones are read against.

### Zone groupings — provenance (2026-08-24)

The zone carve-up was shaped by a FishDope daily report Cameron supplied on
2026-08-24, used as a STRUCTURAL reference only: how the fishery groups spots
into run-sized zones. Per his instruction, FishDope is **not** registered in
`sources/source-registry.md`, none of its report content was mined, and no
conditions or bite information from it entered the KB (BightSST is the system
of record for conditions; a day's bite is not knowledge).

The groupings are therefore attributed `(cameron)` — an editorial carve-up,
not a sourced claim. Zones were then derived primarily from the coordinates in
`sources/spot-lists.md`; see `scripts/review/build-geo-worklist.py`.

### Coverage summary and the merge recommendation (2026-09-09)

The run's coverage summary is
[`review-coverage-summary.md`](review-coverage-summary.md). Its calls:

- **Do not merge as-is.** The ladder, evidence layer and v2 skeletons are sound
  and conserved pre-existing content (500/500 router cites, all four
  adjudications, all 23 routers). The new zone/region prose is not: 813 of the
  1,000 location fact-check flags sit on 77 pages, ~10 per zone page, and a
  40-row sample found 39 of 40 over-claims were introduced by the review.
- **The rewrite pass dropped numeric specifics**, at an aggregate rate near
  4–6%. The guard does not conserve parameters, so the rule is worth adding
  whatever the restoration decision. _(Corrected 2026-09-23: the per-note
  attribution was wrong and the headline example inverted — `knife-jigs.md`
  carries 19 gram parameters before and 31 after. Most apparent loss is the
  relocation pass moving parameters to other notes. The genuinely-lost residue
  is small and must be re-derived case by case before anything is restored.)_
- **`verify-external.yml` has never run**; 299 ledger rows are tagged and
  waiting.
- The Tanner/Cortez "90 vs 110 mi" resolution was overturned by the verifier.
  The ledger row is re-opened (2026-09-23) and sits in the live table for a
  ruling.

Cameron's answer on 2026-09-23 was **correction pass first, and run the
external verification before it**. The plan for both is
[`plan-correction-pass.md`](plan-correction-pass.md).

_(Corrected 2026-09-23: this section previously said "74 escalations are
genuine judgment calls (of 135)". The file holds 137 entries and 83 are
genuine; the 74 figure reconciled with no cut of it.)_

<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
