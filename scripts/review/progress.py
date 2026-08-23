#!/usr/bin/env python3
"""Regenerate sources/review-progress.md from the review worklist (mechanical).

Pass --check to print the summary WITHOUT writing (same reason as
scripts/batch2/progress.py: a bare run during an active chunk leaves a dirty
tree that a later `git add -A` sweeps into an unrelated commit).
"""
from __future__ import annotations

import datetime
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WORKLIST = ROOT / "sources" / "review-worklist.md"
START, END = "<!-- review:worklist:start -->", "<!-- review:worklist:end -->"


def main() -> int:
    check_only = "--check" in sys.argv
    text = WORKLIST.read_text(encoding="utf-8")
    block = text.split(START, 1)[1].split(END, 1)[0]
    counts: Counter = Counter()
    by_tier: Counter = Counter()
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) == 5 and cells[0] not in ("note", "") \
                and set(cells[0]) - {"-", " "}:
            counts[cells[2]] += 1
            by_tier[cells[1]] += 1
    total = sum(counts.values())
    reloc_path = ROOT / "sources" / "relocation-queue.md"
    reloc_pending = 0
    if reloc_path.exists():
        reloc_pending = len(re.findall(r"\| pending \|$",
                                       reloc_path.read_text(encoding="utf-8"),
                                       re.M))
    esc_file = ROOT / "sources" / "escalations.md"
    n_esc = len(re.findall(r"^## ", esc_file.read_text(encoding="utf-8"),
                           re.M)) if esc_file.exists() else 0
    ts = datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%d %H:%M UTC")
    run = os.environ.get("GITHUB_RUN_ID", "local")

    statuses = ["pending", "transformed", "fact-checked", "done", "skipped",
                "escalated", "reverted"]
    lines = [
        "# Review progress",
        "",
        f"Last update: {ts} (run {run})",
        "",
        "| total | " + " | ".join(statuses) + " |",
        "| --- |" + " --- |" * len(statuses),
        f"| {total} | " + " | ".join(str(counts.get(s, 0)) for s in statuses)
        + " |",
        "",
        f"Rows by tier: " + ", ".join(f"{t} {n}" for t, n in
                                      sorted(by_tier.items())),
        f"Pending relocations: {reloc_pending}",
        f"Escalation entries in sources/escalations.md: {n_esc}",
        "",
    ]
    if counts.get("pending", 0) == 0 and counts.get("transformed", 0) == 0 \
            and reloc_pending == 0:
        lines += ["**REVIEW WORKLIST COMPLETE** — no actionable rows remain. "
                  "Endgame (coverage summary, judgment calls, GATE B package) "
                  "runs in a supervised session per sources/plan-review.md.",
                  ""]
    if not check_only:
        (ROOT / "sources" / "review-progress.md").write_text(
            "\n".join(lines), encoding="utf-8")
    print(f"progress: {total} rows, {counts.get('pending', 0)} pending, "
          f"{counts.get('transformed', 0)} transformed, "
          f"{reloc_pending} relocations pending, {n_esc} escalations")
    return 0


if __name__ == "__main__":
    sys.exit(main())
