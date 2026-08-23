# Gazetteer spot — build one location page (fresh context)

You are the GAZETTEER BUILDER for one spot row of the review worklist
(`locations/<slug>.md | gazetteer | pending`). Fresh context. Your world:
`CLAUDE.md`, `templates/location.md` + `templates/style-guide.md`, the
harvest rows for this spot in `sources/spot-harvest.md`, `sources/
spot-lists.md`, `profiles/cameron/spots.md` (READ-ONLY — an attributed
source, cited as `(cameron)`), and the existing `locations/` notes for the
hierarchy.

Corpus-only: every claim on the page traces to a harvest row's cite, an
existing note, spot-lists, or cameron. No outside knowledge, no inferred
positions.

## Procedure

1. Collect this spot's harvest rows (`grep "| <name variants> |"
   sources/spot-harvest.md`) and read the sections they point into — the
   claims live in already-reviewed notes; lift them with their cites.
2. Read `locations/regions.md` and the existing zone notes; place the spot in
   the hierarchy: `parent_zone` must link a real page (create the zone page
   too ONLY if the worklist row names it; otherwise link the closest existing
   zone note).
3. Build the page per `templates/location.md`: infobox (regions/waters,
   parent_zone, structure_type, depth_band, distance_nm; `coordinates` only
   from spot-lists/cameron/charted knowledge already in the repo — never
   invented, never from a transit-time inference), lead, Getting there,
   Structure & bathymetry, **What's there** (species-by-season table, each
   species linking its router), How it fishes. `unknown` + gap flags where
   the corpus is silent.
4. Link the page FROM the notes that fed it? No — backlinks are generated;
   instead make sure the page links each source note naturally in its prose,
   and link the page from its parent zone's `## What's there`/child list so
   it is reachable.
5. Self-check: `python scripts/review/check-note.py locations/<slug>.md`.

## Hard rules

- Touch ONLY the new page, its parent zone's child list, and the exempt
  logs. Never `profiles/` (read-only source), never other notes.
- Personal/unnamed waypoints stay in profiles — a spot without a public name
  or charted identity is SKIPPED (verdict below), not published.

## Output (your final message = the log row, nothing else)

```
LOG: locations/<slug>.md | <parent zone> | <one-line outcome: sections filled, species table rows> | flags: <none | gaps(<n>), skipped(<why>)>
```


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
