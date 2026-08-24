# Template: species note (`type: species`, FULL tier)

Species notes are the KB's entry points and routers (CLAUDE.md). The v2
skeleton keeps the five batch-era sections and adds the natural-history layer
a planner needs: why the fish is there, why it eats, and when it spawns.
Acceptance test (unchanged): a new-to-SoCal angler opening the note alone
learns where to go, when, how to find them (including on the meter), which
technique per situation, and what gear class — everything deeper one link away.

## Front matter

```yaml
---
type: species
tags: [yellowtail, ...]
sources: [<video_id>, ..., cameron]
confidence: high
regions: [socal-bight, ...]        # gated — locations/regions.md vocabulary
waters: [island, bank, ...]        # gated
layout: v2
scientific_name: Seriola dorsalis  # `unknown` if the corpus never names it
season_peak: [may, jun, jul, aug, sep, oct]
sst_band_f: 62-74                  # the band the bite lives in
depth_band: surface to 40 fathoms
gear_classes: [jig-stick, 30-40lb-live-bait, 50lb-yoyo]
sonar_depth: 5-10 fathoms near structure
---
```

All six infobox fields are required; the literal value `unknown` is legal and
feeds the gap report.

## Skeleton (canonical order — extras allowed between; v2.1 per pilot
feedback 2026-08-24: strategy before geography, spot tour extracted to zone
guides)

```
# <Species name>

<Lead: 2–4 sentences — what makes THIS species' program distinct, concrete
from the first sentence. No filler ("a structure-and-bait fish" bans itself:
every fish follows food and structure).>

## Where & when
COMPACT: range + migration/temperature/timing mechanics only — what moves
them, what water they bite in, presence vs catchability per sub-region.
NO spot-by-spot tour: zone detail lives in the zone guides and the
locations/ gazetteer; this section links them.

## Presence & forage
WHY they are in a zone: bait, structure, current, temperature — and what they
actually eat (natural forage, distinct from hook bait). Corpus-only; missing
pieces get a `⚠ Flagged gap — no corpus source` line.

## Spawning
When, where, how they spawn, and what it does to the bite. Corpus-only; gaps
flagged, never invented.

## Feeding triggers
What turns the bite ON: light, tide/slack, current, moon, temperature swing.
The mechanism when a source gives one.

## Finding them (sign & sonar)
Visual sign, bird behavior, species-specific sonar signatures WITH depths.
Links planning/search-and-glassing.md and planning/electronics-and-sounder.md.

## Situations → techniques
THE router table. One row per scenario: conditions that produce it →
technique(s) ranked best-first (`/` separates equals) → gear class → link.
Conditions/caveats go to `[a]` footnotes under the table. Flagged stubs stay.

## Gear summary (class terms)
Class terms only, linking tackle/gear-classes.md.

## Zone guides
One line per species×zone targeting guide (templates/zone-guide.md), linked:
what a trip to that zone looks like for this species. Region/zone level,
never spot level. Zones with corpus content but no guide yet get a flagged
stub row.

## Regulations
Jurisdiction + as-of date + verify-current, one line per jurisdiction.
Registered in sources/regulatory-claims.md. Cross-jurisdiction differences
are labels, not conflicts.

## Doctrine & conflicts
Attributed side-by-side positions WITH a decision frame (what the choice
turns on). Section order is not a ranking — say so.

## Landing & handling
Short, species-specific only; everything general links fish-care/.

## Evidence
One line: Trip reports and per-source provenance: [evidence file](evidence/<note>.md).

## Linked from   (machine-generated — never hand-edited)
```

Decision spin-outs (`type: decision`) still live in `species/` and follow
`templates/decision.md`; the router keeps a summary + link. Zone guides
(`type: zone-guide`, `templates/zone-guide.md`) also live in `species/` as
`<species>-<zone>.md`.

Acceptance tests: (Cameron) a new-to-SoCal angler learns where/when/how/what
gear from this note alone, one link deep — and no claim stands without scope,
mechanism, or a flag. (Nate) a lifelong local finds zone-trip reality (how an
LJ trip differs from a Coronados trip for the same fish), specific
colors/sizes/weights, and nothing that reads as filler.
