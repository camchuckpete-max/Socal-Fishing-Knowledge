#!/usr/bin/env python3
"""Emit the next actionable editorial-review units as JSON lines.

Two sources of work, phase derived from state (no workflow edits between
phases — the chain rolls itself):

  1. sources/review-worklist.md   (<!-- review:worklist:start/end -->)
     columns: | note | tier | status | flags | result |
  2. sources/relocation-queue.md  (<!-- review:relocations:start/end -->)
     columns: | src | dst | what | rationale | cite | status |

Phase priority (first non-empty bucket wins):
  transform   worklist rows status=pending, tier full|standard|light
  relocate    relocation-queue rows status=pending
  gazetteer   worklist rows status=pending, tier gazetteer
  factcheck   worklist rows status=transformed (any tier)
  cluster     worklist rows status=pending, tier cluster

Usage: next-note.py [--count] [--budget P] [-n N]
  --count   total actionable units across ALL phases (preflight contract)
  --budget  emit rows until their cost exceeds P
            (full=5, standard=2, light=1, gazetteer=2, cluster=3, relocate=1)

Read-only. Exit 0 ok, 2 worklist malformed/missing (fails preflight loudly).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WORKLIST = ROOT / "sources" / "review-worklist.md"
RELOCATIONS = ROOT / "sources" / "relocation-queue.md"
WL_START, WL_END = "<!-- review:worklist:start -->", "<!-- review:worklist:end -->"
RQ_START, RQ_END = "<!-- review:relocations:start -->", "<!-- review:relocations:end -->"

STATUSES = {"pending", "transformed", "fact-checked", "done", "skipped",
            "escalated", "reverted"}
TIERS = {"full", "standard", "light", "gazetteer", "cluster"}
COST = {"full": 5, "standard": 2, "light": 1, "gazetteer": 2, "cluster": 3,
        "relocate": 1}


def parse_table(path: Path, start: str, end: str, ncells: int,
                header0: str) -> list[list[str]]:
    if not path.exists():
        print(f"next-note: {path.name} missing", file=sys.stderr)
        sys.exit(2)
    text = path.read_text(encoding="utf-8")
    try:
        block = text.split(start, 1)[1].split(end, 1)[0]
    except IndexError:
        print(f"next-note: markers not found in {path.name}", file=sys.stderr)
        sys.exit(2)
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or cells[0] in (header0, "") or set(cells[0]) <= {"-", " "}:
            continue
        if len(cells) != ncells:
            print(f"next-note: malformed row ({len(cells)} cells): {line}",
                  file=sys.stderr)
            sys.exit(2)
        rows.append(cells)
    return rows


def worklist_rows() -> list[dict]:
    rows = []
    for note, tier, status, flags, result in parse_table(
            WORKLIST, WL_START, WL_END, 5, "note"):
        if status not in STATUSES:
            print(f"next-note: unknown status {status!r} on {note}",
                  file=sys.stderr)
            sys.exit(2)
        if tier not in TIERS:
            print(f"next-note: unknown tier {tier!r} on {note}",
                  file=sys.stderr)
            sys.exit(2)
        rows.append({"note": note, "tier": tier, "status": status,
                     "flags": flags, "result": result})
    if not rows:
        print("next-note: worklist contains no rows", file=sys.stderr)
        sys.exit(2)
    return rows


def relocation_rows() -> list[dict]:
    if not RELOCATIONS.exists():
        return []
    text = RELOCATIONS.read_text(encoding="utf-8")
    if RQ_START not in text:
        return []
    rows = []
    for src, dst, what, rationale, cite, status in parse_table(
            RELOCATIONS, RQ_START, RQ_END, 6, "src"):
        rows.append({"src": src, "dst": dst, "what": what,
                     "rationale": rationale, "cite": cite, "status": status})
    return rows


def buckets() -> list[tuple[str, list[dict]]]:
    wl = worklist_rows()
    rq = [r for r in relocation_rows() if r["status"] == "pending"]
    return [
        ("transform", [r for r in wl if r["status"] == "pending"
                       and r["tier"] in ("full", "standard", "light")]),
        ("relocate", rq),
        ("gazetteer", [r for r in wl if r["status"] == "pending"
                       and r["tier"] == "gazetteer"]),
        ("factcheck", [r for r in wl if r["status"] == "transformed"]),
        ("cluster", [r for r in wl if r["status"] == "pending"
                     and r["tier"] == "cluster"]),
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", action="store_true",
                    help="total actionable units across all phases")
    ap.add_argument("--budget", type=int, default=None,
                    help="emit rows until cost exceeds this budget")
    ap.add_argument("-n", type=int, default=10)
    args = ap.parse_args()

    bks = buckets()
    if args.count:
        print(sum(len(rows) for _p, rows in bks))
        return 0

    phase, rows = next(((p, r) for p, r in bks if r), ("none", []))
    if not rows:
        return 0
    spent, emitted = 0, 0
    for r in rows:
        cost = COST["relocate"] if phase == "relocate" else COST[r["tier"]]
        if args.budget is not None and spent + cost > args.budget and emitted:
            break
        if args.budget is None and emitted >= args.n:
            break
        out = dict(r)
        out["phase"] = phase
        print(json.dumps(out, ensure_ascii=False))
        spent += cost
        emitted += 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
