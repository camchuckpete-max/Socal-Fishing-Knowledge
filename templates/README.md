# Templates — the layout spec (v2)

The per-type article skeletons and the [style guide](style-guide.md) that
govern every KB note migrated by the 2026-08 editorial review
(`sources/plan-review.md`), and everything written after it. The machine
mirror is `scripts/note_schema.py` — the two change together, in the same
commit. A migrated note carries `layout: v2` in its front matter, which turns
on structural validation in `scripts/link-maintenance.py`; notes not yet
migrated are untouched by the new rules.

This directory is spec, not knowledge: links are validated but the files are
not indexed, get no backlinks, and are never published to the site. It is a
guard-protected path — the unattended review fleet cannot edit its own spec.

| File | Governs |
| --- | --- |
| [style-guide.md](style-guide.md) | Voice, cites, evidence files, flags, structure rules — read this first |
| [species.md](species.md) | Species routers (FULL tier) — the 10-section skeleton with the biology layer |
| [technique.md](technique.md) | Technique notes — execution only |
| [lure.md](lure.md) | Lure/class spec notes |
| [rig.md](rig.md) | Knots, leaders, terminal rigs |
| [location.md](location.md) | The gazetteer: zones and spot pages |
| [decision.md](decision.md) | Species-level decision spin-outs |
| [conditions.md](conditions.md) | Conditions interpretation layers |
| [seasonal.md](seasonal.md) | Month-by-month priors |
| [bait.md](bait.md) | Live-bait notes |
| [tackle.md](tackle.md) | Tackle selection + product notes (LIGHT tier) |
| [fish-care.md](fish-care.md) | Fish-care procedures (LIGHT tier) |
| [planning.md](planning.md) | Planning procedures (LIGHT tier) |
| [evidence.md](evidence.md) | Evidence files — the provenance layer from the observation split |
