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
TIERS = {"full", "standard", "light", "geo", "gazetteer", "cluster"}
COST = {"full": 5, "standard": 2, "light": 1, "geo": 2, "gazetteer": 2,
        "cluster": 3, "relocate": 1}

# Which model each tier is worth (Cameron, 2026-08-26). Opus keeps the work
# where judgment is the product: the geographic ladder, the species routers
# and their situation→technique tables, the gazetteer pages written from
# harvested corpus, fact-check and cluster consistency. Sonnet takes the
# formulaic tail — 128 standard + 98 light units, over half the remaining
# points — where the note is a rewrite against a fixed skeleton.
MODEL_BY_TIER = {
    "geo": "claude-opus-5",
    "full": "claude-opus-5",
    "standard": "claude-sonnet-5",
    "light": "claude-sonnet-5",
    "gazetteer": "claude-opus-5",
    "cluster": "claude-opus-5",
    "relocate": "claude-opus-5",
}
DEFAULT_MODEL = "claude-opus-5"


def model_of(row: dict, phase: str) -> str:
    tier = "relocate" if phase == "relocate" else row.get("tier", "")
    return MODEL_BY_TIER.get(tier, DEFAULT_MODEL)


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
        # geo runs FIRST (Cameron, 2026-08-24). Two reasons: a spot page
        # cannot resolve `parent` until its zone exists, and a species note
        # being rewritten should link a real zone page rather than fall back
        # to a plain-text zone name. It is also the layer Cameron just
        # reviewed, so it appears early instead of ~30 chunks in.
        ("geo", [r for r in wl if r["status"] == "pending"
                 and r["tier"] == "geo"]),
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
    ap.add_argument("--model", action="store_true",
                    help="model the next chunk runs on, and nothing else")
    ap.add_argument("--phase", action="store_true",
                    help="name of the active bucket, and nothing else")
    args = ap.parse_args()

    bks = buckets()
    if args.count:
        print(sum(len(rows) for _p, rows in bks))
        return 0

    phase, rows = next(((p, r) for p, r in bks if r), ("none", []))
    if args.phase:
        print(phase)
        return 0
    if args.model:
        print(model_of(rows[0], phase) if rows else DEFAULT_MODEL)
        return 0
    if not rows:
        return 0
    spent, emitted = 0, 0
    chunk_model = model_of(rows[0], phase)
    for r in rows:
        # One model per chunk. The workflow sets --model once for the whole
        # run, so a chunk that mixed tiers would silently run some units on
        # the wrong one — Sonnet on a species router, or Opus on the light
        # tail Cameron moved off it. Stopping at the boundary costs at most a
        # short chunk and keeps the guarantee exact.
        if model_of(r, phase) != chunk_model and emitted:
            break
        cost = COST["relocate"] if phase == "relocate" else COST[r["tier"]]
        if args.budget is not None and spent + cost > args.budget and emitted:
            break
        if args.budget is None and emitted >= args.n:
            break
        out = dict(r)
        out["phase"] = phase
        out["model"] = chunk_model
        print(json.dumps(out, ensure_ascii=False))
        spent += cost
        emitted += 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
