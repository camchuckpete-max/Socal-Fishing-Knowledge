#!/usr/bin/env python3
"""Regenerate sources/batch-2-progress.md from the worklist (mechanical)."""
from __future__ import annotations

import datetime
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

START = "<!-- batch2:worklist:start -->"
END = "<!-- batch2:worklist:end -->"


def main() -> int:
    text = (ROOT / "sources" / "extraction-log.md").read_text(encoding="utf-8")
    block = text.split(START, 1)[1].split(END, 1)[0]
    counts: Counter = Counter()
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) == 6 and cells[0] not in ("video_id", "") and set(cells[0]) - {"-", " "}:
            counts[cells[4]] += 1
    total = sum(counts.values())
    pending = counts.get("pending", 0)
    esc_file = ROOT / "sources" / "escalations.md"
    n_esc = len(re.findall(r"^## ", esc_file.read_text(encoding="utf-8"), re.M)) if esc_file.exists() else 0
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    run = os.environ.get("GITHUB_RUN_ID", "local")

    lines = [
        "# Batch 2 progress",
        "",
        f"Last update: {ts} (run {run})",
        "",
        f"| total rows | done | skipped | escalated | reverted | pending |",
        f"| --- | --- | --- | --- | --- | --- |",
        f"| {total} | {counts.get('done', 0)} | {counts.get('skipped', 0)} | "
        f"{counts.get('escalated', 0)} | {counts.get('reverted', 0)} | {pending} |",
        "",
        f"Escalation entries in sources/escalations.md: {n_esc}",
        "",
    ]
    if pending == 0:
        lines += ["**BATCH 2 WORKLIST COMPLETE** — no pending rows remain. The",
                  "chain stopped here. Phase 5 (coverage, acceptance tests, Gate B",
                  "package) was deferred to 'a separate reviewed session' and never",
                  "ran before batch 2 merged to `main` (540ea4a); it is being done",
                  "as Phase 1 of the batch-3 build — see the close-out section in",
                  "sources/extraction-log.md.", ""]
    (ROOT / "sources" / "batch-2-progress.md").write_text("\n".join(lines),
                                                          encoding="utf-8")
    print(f"progress: {total} total, {pending} pending, {n_esc} escalation entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
