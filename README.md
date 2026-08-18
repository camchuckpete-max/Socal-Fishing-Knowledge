# SoCal / Baja Fishing Knowledgebase

The **system of record for fishing KNOWLEDGE** for the Southern California Bight
and Baja — the companion to [BightSST](https://bightai-api.onrender.com) (the
system of record for **conditions**). Claude chat is the day-planning surface
and consumes both at plan time. Knowledge here is **universal**; angler-specific
boats, rods, and spots live under [`profiles/`](profiles/README.md). Anyone can plan a day
with this KB, and the recommendations sharpen once they add their own gear.

**Mission:** guide a brand-new-to-SoCal fisherman through the full chain —
**where** to go, **when** to go, **which techniques** to use and **when each
applies**, **what tackle** goes with each technique, **how to use a fish finder**
to locate fish, and **how to actually fish** each technique.

## ▶ Start here: [the day-plan protocol](planning/day-plan-protocol.md)

The step-by-step procedure chat and the boat-day skill follow to turn conditions
+ priors into a gear'd-up plan. **Species notes are the entry points** — open
[`species/`](species/README.md) for the fish you want and route out to technique, gear,
and conditions from there.

## Branch map

| Branch | What lives here |
| --- | --- |
| [conditions/](conditions/README.md) | Interpretation layers — sea-state, moon, tide/slack, current-structure, water color/temp, upwelling/turnover, DSL, paddies, birds |
| [seasonal/](seasonal/README.md) | Month-by-month priors calendar (pattern layer, not current intel) |
| [species/](species/README.md) | Per-species behavior + the situation→technique router table |
| [techniques/](techniques/README.md) | How a method works + when to reach for it |
| [lures/](lures/README.md) | Per-lure / per-class specs, rigging, running params |
| [rigging/](rigging/README.md) | Knots, leaders, terminal rigs (parameters + judgment) |
| [tackle/](tackle/README.md) | Rod / reel / line / hook selection; the gear-class lexicon |
| [bait/](bait/README.md) | Making, keeping, and fishing live bait |
| [fish-care/](fish-care/README.md) | Bleeding, chilling, ikejime, handling |
| [locations/](locations/README.md) | Universal structure/zone knowledge — no personal coordinates |
| [planning/](planning/README.md) | Day-plan protocol, search & glassing, electronics |
| [profiles/](profiles/README.md) | Per-user boat, rods, tackle, lures, spots |
| [sources/](sources/README.md) | Raw transcripts, input docs, extraction log |
| [config/](config/README.md) | Runtime config the distributed skill reads at plan time — conditions endpoints, fallback ladder, source-validity rules |
| [skills/](skills/README.md) | Deployable skills — `socal-boat-day` (distributed, fetches the KB live) and `boat-day` (earlier bundled design) |
| [scripts/](scripts/README.md) | `link-maintenance.py`, `build-skill-resources.py` |

## Conventions

Native GitHub markdown — relative links only (no wikilinks), YAML front matter
on every note, sources named (`cameron` or a YouTube `video_id`). See
[CLAUDE.md](CLAUDE.md) for the full spec, the confidence rubric, and the
species-first routing contract. Run `python scripts/link-maintenance.py` before
every commit.
