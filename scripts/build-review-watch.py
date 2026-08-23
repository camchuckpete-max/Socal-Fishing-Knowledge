#!/usr/bin/env python3
"""build-review-watch.py — the editorial review's HTML review screen.

Cameron's GATE B surface: one self-contained page showing

  - the worklist status board (per folder, per status),
  - the fact-check ledger,
  - the gap report totals,
  - pending relocations,
  - per-note BEFORE/AFTER for every reviewed note, diffed against the review
    branch's merge-base with origin/main (or --base <ref>), with the evidence
    file shown beside the note.

Output: sources/review-watch.html (gitignored, like bight-watch.html).

    python scripts/build-review-watch.py [--base <ref>] [--out PATH]
"""
from __future__ import annotations

import argparse
import difflib
import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CSS = """
:root { color-scheme: light dark; --add:#1a7f37; --del:#cf222e;
        --bg:#fff; --fg:#1f2328; --muted:#656d76; --line:#d0d7de;
        --chip:#eef1f4; }
@media (prefers-color-scheme: dark) {
  :root { --add:#3fb950; --del:#f85149; --bg:#0d1117; --fg:#e6edf3;
          --muted:#8b949e; --line:#30363d; --chip:#21262d; } }
body { font: 14px/1.5 -apple-system, "Segoe UI", sans-serif;
       background: var(--bg); color: var(--fg); margin: 0 auto;
       max-width: 1100px; padding: 1rem 2rem 6rem; }
h1 { font-size: 1.4rem; } h2 { font-size: 1.15rem; margin-top: 2.2rem;
     border-bottom: 1px solid var(--line); padding-bottom: .3rem; }
table { border-collapse: collapse; width: 100%; font-size: 13px; }
th, td { border: 1px solid var(--line); padding: 4px 8px; text-align: left;
         vertical-align: top; }
.badge { display: inline-block; background: var(--chip); border-radius: 10px;
         padding: 0 8px; margin-right: 6px; font-size: 12px; }
details { margin: .6rem 0; border: 1px solid var(--line); border-radius: 6px; }
summary { cursor: pointer; padding: .5rem .8rem; font-weight: 600; }
.diff { font: 12px/1.45 ui-monospace, monospace; white-space: pre-wrap;
        overflow-x: auto; padding: .6rem .8rem; margin: 0; }
.diff .a { color: var(--add); } .diff .d { color: var(--del); }
.diff .h { color: var(--muted); }
.muted { color: var(--muted); }
.flag { color: var(--del); font-weight: 600; }
"""


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                       text=True)
    return r.stdout if r.returncode == 0 else ""


def show(ref: str, rel: str) -> str:
    r = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def table_rows(path: Path, start: str, end: str) -> list[list[str]]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    if start not in text:
        return []
    block = text.split(start, 1)[1].split(end, 1)[0]
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells and cells[0] and set(cells[0]) - {"-", " "} \
                    and cells[0] not in ("note", "src", "spot", "claim"):
                rows.append(cells)
    return rows


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def diff_html(before: str, after: str) -> str:
    out = []
    for line in difflib.unified_diff(before.splitlines(), after.splitlines(),
                                     lineterm="", n=2):
        if line.startswith(("---", "+++")):
            continue
        cls = ("a" if line.startswith("+")
               else "d" if line.startswith("-")
               else "h" if line.startswith("@@") else "")
        out.append(f'<span class="{cls}">{esc(line)}</span>' if cls
                   else esc(line))
    return "\n".join(out) or '<span class="h">(no textual change)</span>'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=None,
                    help="diff base ref (default: merge-base with origin/main)")
    ap.add_argument("--out", type=Path,
                    default=ROOT / "sources" / "review-watch.html")
    args = ap.parse_args()
    base = args.base or git("merge-base", "HEAD", "origin/main").strip() \
        or git("rev-parse", "HEAD").strip()
    head = git("rev-parse", "--short", "HEAD").strip()

    wl = table_rows(ROOT / "sources" / "review-worklist.md",
                    "<!-- review:worklist:start -->",
                    "<!-- review:worklist:end -->")
    ledger = table_rows(ROOT / "sources" / "fact-check-ledger.md",
                        "<!-- review:ledger:start -->",
                        "<!-- review:ledger:end -->")
    reloc = table_rows(ROOT / "sources" / "relocation-queue.md",
                       "<!-- review:relocations:start -->",
                       "<!-- review:relocations:end -->")

    parts = [f"<style>{CSS}</style>",
             "<h1>Review Watch — KB editorial review</h1>",
             f'<p class="muted">HEAD {esc(head)} vs base {esc(base[:9])} · '
             f'generated by scripts/build-review-watch.py</p>']

    # status board
    from collections import Counter
    counts = Counter(r[2] for r in wl if len(r) == 5)
    parts.append("<h2>Status</h2><p>")
    for status in ("pending", "transformed", "fact-checked", "done", "skipped",
                   "escalated", "reverted"):
        parts.append(f'<span class="badge">{status}: '
                     f'{counts.get(status, 0)}</span>')
    parts.append("</p>")

    # relocations panel (the highest-judgment changes — always visible)
    parts.append(f"<h2>Relocations ({len(reloc)})</h2>")
    if reloc:
        parts.append("<table><tr><th>src</th><th>dst</th><th>what</th>"
                     "<th>rationale</th><th>cite</th><th>status</th></tr>")
        for r in reloc:
            parts.append("<tr>" + "".join(f"<td>{esc(c)}</td>"
                                          for c in r[:6]) + "</tr>")
        parts.append("</table>")
    else:
        parts.append('<p class="muted">None queued.</p>')

    # fact-check ledger
    parts.append(f"<h2>Fact-check ledger ({len(ledger)})</h2>")
    if ledger:
        parts.append("<table><tr><th>note</th><th>claim</th><th>category</th>"
                     "<th>cite</th><th>detail</th></tr>")
        for r in ledger:
            cells = (r + [""] * 5)[:5]
            parts.append("<tr><td>" + esc(cells[0]) + "</td><td>"
                         + esc(cells[1]) + '</td><td class="flag">'
                         + esc(cells[2]) + "</td><td>" + esc(cells[3])
                         + "</td><td>" + esc(cells[4]) + "</td></tr>")
        parts.append("</table>")
    else:
        parts.append('<p class="muted">No flags yet.</p>')

    # gap report totals
    gap = ROOT / "sources" / "gap-report.md"
    if gap.exists():
        m = re.search(r"_Totals: (.+?)_", gap.read_text(encoding="utf-8"))
        parts.append("<h2>Gaps</h2><p>"
                     + esc(m.group(1) if m else "see sources/gap-report.md")
                     + ' <span class="muted">(full list: '
                     "sources/gap-report.md)</span></p>")

    # per-note before/after
    parts.append("<h2>Before / after</h2>")
    shown = 0
    for r in wl:
        if len(r) != 5:
            continue
        note, tier, status, flags, result = r
        if status in ("pending",) or note.startswith("cluster:"):
            continue
        rel = note
        before = show(base, rel)
        path = ROOT / rel
        after = path.read_text(encoding="utf-8") if path.exists() else ""
        if before == after:
            continue
        shown += 1
        blines = len(before.splitlines())
        alines = len(after.splitlines())
        parts.append(f"<details><summary>{esc(rel)} "
                     f'<span class="badge">{esc(tier)}</span>'
                     f'<span class="badge">{esc(status)}</span>'
                     f'<span class="muted">{blines} → {alines} lines'
                     + (f" · {esc(flags)}" if flags else "")
                     + f"</span></summary>"
                     f'<pre class="diff">{diff_html(before, after)}</pre>'
                     "</details>")
        ev_rel = str(Path(rel).parent / "evidence" / Path(rel).name)
        ev_path = ROOT / ev_rel
        if ev_path.exists():
            ev_after = ev_path.read_text(encoding="utf-8")
            ev_before = show(base, ev_rel)
            parts.append(f"<details><summary>{esc(ev_rel)} "
                         f'<span class="badge">evidence</span>'
                         f'<span class="muted">'
                         f"{len(ev_after.splitlines())} lines</span></summary>"
                         f'<pre class="diff">'
                         f"{diff_html(ev_before, ev_after)}</pre></details>")
    if not shown:
        parts.append('<p class="muted">No reviewed notes differ from base '
                     "yet.</p>")

    args.out.write_text("\n".join(parts), encoding="utf-8")
    print(f"review-watch: {shown} changed notes, {len(ledger)} ledger rows, "
          f"{len(reloc)} relocations -> {args.out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
