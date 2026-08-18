# Scripts

Maintenance and build tooling for the knowledgebase.

- `link-maintenance.py` — the hard habit: run it before **every** commit. It
  validates that every relative link resolves (exiting nonzero on a dead link),
  regenerates each note's backlinks block, and regenerates each folder's
  `README.md` index and branch map.
- `build-skill-resources.py` — bundles a snapshot of the decision layer for the
  older `boat-day` skill. The distributed
  [socal-boat-day](../skills/socal-boat-day/README.md) skill does not use it; it
  fetches the knowledgebase live instead.
- `next-video.py`, `batch2/` — the ingestion pipeline's chunk runner and guards.

This folder has an index so the root branch map can point at a `README.md` like
every other branch. Raw file fetches (`raw.githubusercontent.com`) cannot list a
directory, so a link to a bare folder is a 404 for any tool reading the repo that
way.
