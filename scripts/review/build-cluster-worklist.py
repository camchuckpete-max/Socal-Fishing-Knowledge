#!/usr/bin/env python3
"""build-cluster-worklist.py — append cross-note consistency cluster rows.

A cluster is one species router plus every techniques/ and lures/ note its
`## Situations → techniques` section links. The cluster pass (fact-check
phase 2b) compares the router's claims about each technique/lure against
that note's own doctrine and flags `contradicted-internal` mismatches in
both places.

Appends `| cluster:<species-stem> | cluster | pending |  | members: ... |`
rows to the worklist, append-if-absent (idempotent). Run at checkpoints; the
rows only become actionable once no `transformed` rows remain (next-note's
phase priority).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WORKLIST = ROOT / "sources" / "review-worklist.md"
WL_END = "<!-- review:worklist:end -->"
LINK_RE = re.compile(r"\]\(([^)#]+\.md)")


def members_of(router: Path) -> list[str]:
    text = router.read_text(encoding="utf-8")
    m = re.search(r"^## Situations → techniques.*?(?=^## |\Z)", text,
                  re.M | re.S)
    if not m:
        return []
    out = []
    for target in LINK_RE.findall(m.group(0)):
        resolved = (router.parent / target).resolve()
        try:
            rel = str(resolved.relative_to(ROOT))
        except ValueError:
            continue
        if rel.startswith(("techniques/", "lures/")) and resolved.exists():
            out.append(rel)
    return sorted(set(out))


def main() -> int:
    wl = WORKLIST.read_text(encoding="utf-8")
    added = 0
    rows = []
    for router in sorted((ROOT / "species").glob("*.md")):
        if router.name == "README.md":
            continue
        members = members_of(router)
        if not members:
            continue
        key = f"cluster:{router.stem}"
        if f"| {key} |" in wl:
            continue
        listing = "; ".join(members)
        if len(listing) > 400:
            listing = listing[:397] + "…"
        rows.append(f"| {key} | cluster | pending |  | members: {listing} |")
        added += 1
    if rows:
        wl = wl.replace(WL_END, "\n".join(rows) + "\n" + WL_END)
        WORKLIST.write_text(wl, encoding="utf-8")
    print(f"build-cluster-worklist: {added} cluster rows appended")
    return 0


if __name__ == "__main__":
    sys.exit(main())
