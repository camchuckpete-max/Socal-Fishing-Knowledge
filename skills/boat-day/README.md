# Boat-Day Skill

The boat-day skill runs [`planning/day-plan-protocol.md`](../../planning/day-plan-protocol.md):
pull conditions from BightSST, apply seasonal priors + interpretation layers,
route species → technique via the species routers, and resolve gear against a
profile. It degrades gracefully — no profile yields class-term recommendations.

## No skill sources were provided

No `*.skill` package accompanied this build, so this folder is a **scaffold + the
build plan**. The deployable skill is **generated from the KB** by
[`scripts/build-skill-resources.py`](../../scripts/build-skill-resources.py), so
it never drifts from the notes.

## Build it

```
python scripts/build-skill-resources.py                 # default profile: profiles/cameron
python scripts/build-skill-resources.py --profile profiles/_template
python scripts/build-skill-resources.py --no-profile    # generic, class-term only
```

This writes (git-ignored — a regenerable artifact, never committed):

- `resources/knowledge/` — the bundled **decision layer**: `planning/`,
  `conditions/`, `seasonal/`, `locations/`, `species/` (the situation→technique
  routers), and `tackle/gear-classes.md`. Execution detail (techniques, lures,
  rigging) is fetched from the repo on demand at the raw-GitHub fetch base
  stated in `SKILL.md`.
- `resources/profile/` — the chosen profile (omitted for `--no-profile`).

`SKILL.md` itself is **hand-authored and committed** — the skill entry point
(the 4-step protocol, the profile rule, and the fetch base for execution-layer
links). The script never overwrites it; it creates a starter version only if
the file is absent.

A generic build with no profile still produces a working skill.

## Canonical source

Consumers target `main` (see the merge gate in
[CLAUDE.md](../../CLAUDE.md)); rebuild the bundle after the branch merges so the
skill reflects canonical knowledge.
