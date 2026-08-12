---
name: boat-day
description: Plan a SoCal/Baja fishing day — pull conditions, apply seasonal priors and interpretation layers, route species to technique, and resolve gear against a profile.
---

# Boat-Day Planner

<!-- Hand-authored. scripts/build-skill-resources.py owns resources/ and
     resources/INDEX.md only; it will never overwrite this file. -->

Follow `resources/knowledge/planning/day-plan-protocol.md` step by step. It
consumes **BightSST** (live conditions, `bightai-api.onrender.com`) and **this
bundle** (the KB decision layer) at plan time.

1. Pull conditions from BightSST — per fishing zone and along the transit
   route, observed AND forecast.
2. Apply `resources/knowledge/seasonal/` priors and
   `resources/knowledge/conditions/` layers (regimes, moon, tide windows,
   water color/temp).
3. Enter the `resources/knowledge/species/` routers to map situation →
   technique → gear class.
4. Resolve gear. Check `resources/INDEX.md` for whether a profile is bundled:
   with a profile under `resources/profile/`, resolve gear classes to the
   owned rods/reels/lures and respect the boat envelope (range, sea-state,
   holder geometry); with no profile, give **class-term** recommendations
   (e.g. "surface-iron class, 40–60 lb") and note that adding a profile
   sharpens them.

Class terms resolve via `resources/knowledge/tackle/gear-classes.md`.

## Fetching execution detail

The bundle carries the KB's **decision layer** only. Links in bundled notes
that point outside `resources/knowledge/` — techniques, lures, rigging,
tackle beyond the gear-class lexicon, bait, fish-care, profiles — resolve
against the canonical repo on `main`:

    https://raw.githubusercontent.com/camchuckpete-max/Socal-Fishing-Knowledge/main/

Map the bundled note's relative link to its repo path first, then fetch
`<base>/<repo-path>`. Example: `../techniques/surface-iron.md` linked from
`resources/knowledge/species/yellowtail.md` is repo path
`techniques/surface-iron.md`, fetched as
`<base>/techniques/surface-iron.md`. Backlink (`## Linked from`) entries
resolve the same way.
