#!/usr/bin/env python3
"""Emit the next N unprocessed batch-2 worklist rows as JSON lines.

The worklist is the marker-delimited table in sources/extraction-log.md
(`<!-- batch2:worklist:start -->` .. `<!-- batch2:worklist:end -->`), columns
`| video_id | channel | class | depth | status | result |`. A row is done
when its status cell says so; this script only reads. Exit codes: 0 ok,
2 worklist malformed/missing (fails the preflight loudly).

Usage: next-video.py [--count] [-n N]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "sources" / "extraction-log.md"
# Batch 3 uses its own marker pair; fall back to the batch-2 block so the
# script keeps working against the archived batch-2 worklist.
START = "<!-- batch3:worklist:start -->"
END = "<!-- batch3:worklist:end -->"
FALLBACK = ("<!-- batch2:worklist:start -->", "<!-- batch2:worklist:end -->")
STATUSES = {"pending", "done", "skipped", "escalated", "reverted"}


def parse_rows() -> list[dict]:
    text = LOG.read_text(encoding="utf-8")
    try:
        block = text.split(START, 1)[1].split(END, 1)[0]
    except IndexError:
      try:
        block = text.split(FALLBACK[0], 1)[1].split(FALLBACK[1], 1)[0]
      except IndexError:
        print("next-video: worklist markers not found in extraction-log.md",
              file=sys.stderr)
        sys.exit(2)
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or cells[0] in ("video_id", "") or set(cells[0]) <= {"-", " "}:
            continue
        if len(cells) != 6:
            print(f"next-video: malformed row ({len(cells)} cells): {line}",
                  file=sys.stderr)
            sys.exit(2)
        vid, channel, cls, depth, status, result = cells
        if status not in STATUSES:
            print(f"next-video: unknown status {status!r} on {vid}",
                  file=sys.stderr)
            sys.exit(2)
        rows.append({"video_id": vid, "channel": channel, "class": cls,
                     "depth": depth, "status": status, "result": result})
    if not rows:
        print("next-video: worklist block contains no rows", file=sys.stderr)
        sys.exit(2)
    return rows


def resolve_path(video_id: str) -> str | None:
    t = ROOT / "sources" / "transcripts"
    hits = [p for p in list(t.glob("*/*.md")) + list(t.glob("*.md"))
            if p.name.endswith(f"--{video_id}.md")]
    if len(hits) == 1:
        return str(hits[0].relative_to(ROOT))
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", action="store_true",
                    help="print the number of pending rows and exit")
    ap.add_argument("-n", type=int, default=15)
    args = ap.parse_args()

    rows = parse_rows()
    pending = [r for r in rows if r["status"] == "pending"]
    if args.count:
        print(len(pending))
        return 0
    for r in pending[: args.n]:
        path = resolve_path(r["video_id"])
        out = {k: r[k] for k in ("video_id", "channel", "class", "depth")}
        # pending rows carry the triage evidence in the result column; it is
        # part of the extractor's input and is overwritten by the outcome
        out["evidence"] = r["result"]
        if path is None:
            out["error"] = "path-resolution-failed"
        else:
            out["path"] = path
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
