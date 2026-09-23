#!/usr/bin/env python3
"""build-worklist.py — one-shot generator of sources/review-worklist.md.

One row per fleet-reviewable note (folder order = fleet order; species first
so spec defects surface on the highest-value tier). Tier map per
sources/plan-review.md. profiles/ is guard-protected and handled in the
supervised endgame; sources/, skills/, templates/ are not notes. evidence/
subdirs are review OUTPUT, never rows.

Also prints the observed-block reconciliation count (exact-marker grep) so
the coverage summary can account for every observation.

Refuses to overwrite an existing worklist unless --force (rows carry state).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "sources" / "review-worklist.md"

# Fleet order (plan): species first, tackle last.
TIERS = [
    ("species", "full"),
    ("techniques", "standard"),
    ("lures", "standard"),
    ("rigging", "standard"),
    ("conditions", "standard"),
    ("seasonal", "standard"),
    ("bait", "standard"),
    ("locations", "standard"),
    ("planning", "light"),
    ("fish-care", "light"),
    ("tackle", "light"),
]

HEADER = """# Review worklist

The editorial-review fleet's work queue (sources/plan-review.md). One row per
note; the sanctioned wrapper (scripts/review/commit-note.py) is the only
writer of status/flags/result cells. Status machine:
`pending -> transformed -> fact-checked -> done`, terminals
`skipped | escalated | reverted`; `light`-tier rows go straight
`pending -> done` at transform time. Gazetteer and cluster rows are appended
by their builders after the transform phase drains.

**`fact-checked` is the last phase any unit actually runs** (2026-09-23). The
`-> done` transition above was never implemented for the full and geo tiers, and
the orchestrator's "or done when the tier is standard/gazetteer" branch was not
taken either, so 246 completed rows sat one step short of terminal while
`next-note.py` — which only ever selects `pending` — could never advance them.
The chain reported itself drained with those rows open. They were relabelled
`done` in bulk at GATE B prep after sampling across every affected tier
confirmed the work was complete (`layout: v2` present, evidence files written,
ledger rows produced). Nothing was re-run. Treat `fact-checked` as a
transitional value that should no longer appear.

"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    if OUT.exists() and not args.force:
        print("build-worklist: sources/review-worklist.md already exists "
              "(rows carry state) — pass --force to regenerate", file=sys.stderr)
        return 1

    rows = []
    observed = 0
    for folder, tier in TIERS:
        for path in sorted((ROOT / folder).glob("*.md")):
            if path.name == "README.md":
                continue
            rows.append(f"| {folder}/{path.name} | {tier} | pending |  |  |")
            observed += len(re.findall(r"^[ \t>-]*\*\*Observed\*\*",
                                       path.read_text(encoding="utf-8"), re.M))

    body = (HEADER
            + "<!-- review:worklist:start -->\n"
            + "| note | tier | status | flags | result |\n"
            + "| --- | --- | --- | --- | --- |\n"
            + "\n".join(rows) + "\n"
            + "<!-- review:worklist:end -->\n")
    OUT.write_text(body, encoding="utf-8")
    print(f"build-worklist: {len(rows)} rows "
          f"({sum(1 for _f, t in TIERS if t == 'full')} folders full-tier); "
          f"observed-block reconciliation count: {observed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
