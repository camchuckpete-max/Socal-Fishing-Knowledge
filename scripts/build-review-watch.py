#!/usr/bin/env python3
"""build-review-watch.py — Review Watch, the transform-job dashboard.

Bight Watch answered an EXTRACTION job's question ("did this video's
knowledge land?"). This page answers the questions a TRANSFORM job raises
(Cameron, 2026-08-24):

  - conservation: is anything being LOST? (per-note cite-conservation check,
    lines before/after, evidence-entry counts)
  - adjudication: what queues need Cameron? (fact-check ledger by category,
    relocation queue, escalations)
  - gaps: what knowledge is the KB missing? (gap-report totals)
  - run health: phase, per-folder progress, throughput/ETA, model, STOP,
    chain runs
  - spot-review: recent notes with capped inline diffs; every processed note
    links to its GitHub commit

Output: sources/review-watch.html (gitignored). Published to GitHub Pages by
publish-review-watch.yml (on main), rebuilt after every chunk + hourly.

    python scripts/build-review-watch.py [--base <ref>] [--out PATH]
                                         [--runs runs.json]
"""
from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "review"))
import guard  # noqa: E402  (cited_ids, evidence_path)

GH = "https://github.com/camchuckpete-max/Socal-Fishing-Knowledge"
BRANCH = "claude/knowledge-base-review-g00k8s"
RECENT_DIFFS = 8
DIFF_LINE_CAP = 300

CSS = """
:root { color-scheme: light dark; --add:#1a7f37; --del:#cf222e; --warn:#9a6700;
        --bg:#ffffff; --fg:#1f2328; --muted:#656d76; --line:#d0d7de;
        --chip:#eef1f4; --ok:#1a7f37; }
@media (prefers-color-scheme: dark) {
  :root { --add:#3fb950; --del:#f85149; --warn:#d29922; --bg:#0d1117;
          --fg:#e6edf3; --muted:#8b949e; --line:#30363d; --chip:#21262d;
          --ok:#3fb950; } }
body { font: 14px/1.5 -apple-system, "Segoe UI", sans-serif;
       background: var(--bg); color: var(--fg); margin: 0 auto;
       max-width: 1150px; padding: 1rem 1.5rem 6rem; }
h1 { font-size: 1.35rem; margin-bottom:.2rem; }
h2 { font-size: 1.1rem; margin-top: 2rem; border-bottom: 1px solid var(--line);
     padding-bottom: .3rem; }
table { border-collapse: collapse; width: 100%; font-size: 13px; }
th, td { border: 1px solid var(--line); padding: 4px 8px; text-align: left;
         vertical-align: top; }
th { background: var(--chip); position: sticky; top: 0; }
.tbl { overflow-x: auto; max-height: 70vh; overflow-y: auto;
       border: 1px solid var(--line); }
.badge { display: inline-block; background: var(--chip); border-radius: 10px;
         padding: 0 8px; margin: 0 4px 4px 0; font-size: 12px; }
.num { font-variant-numeric: tabular-nums; }
.ok { color: var(--ok); font-weight: 600; }
.bad { color: var(--del); font-weight: 700; }
.warn { color: var(--warn); font-weight: 600; }
.muted { color: var(--muted); }
.bars { display: grid; grid-template-columns: 9rem 1fr 6rem; gap: 4px 10px;
        align-items: center; font-size: 13px; }
.bar { background: var(--chip); border-radius: 4px; height: 12px;
       overflow: hidden; }
.bar > div { background: var(--ok); height: 100%; }
.bar > div.part { background: var(--warn); }
details { margin: .6rem 0; border: 1px solid var(--line); border-radius: 6px; }
summary { cursor: pointer; padding: .45rem .8rem; font-weight: 600;
          font-size: 13px; }
.diff { font: 12px/1.45 ui-monospace, monospace; white-space: pre-wrap;
        overflow-x: auto; padding: .6rem .8rem; margin: 0; }
.diff .a { color: var(--add); } .diff .d { color: var(--del); }
.diff .h { color: var(--muted); }
.statgrid { display: flex; flex-wrap: wrap; gap: .6rem; margin: 1rem 0; }
.stat { border: 1px solid var(--line); border-radius: 8px; padding: .5rem .8rem;
        min-width: 7.5rem; }
.stat .n { font-size: 1.2rem; font-weight: 600; font-variant-numeric: tabular-nums; }
.stat .l { font-size: .7rem; text-transform: uppercase; letter-spacing: .05em;
           color: var(--muted); }
a { color: inherit; }
"""


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def show(ref: str, rel: str) -> str | None:
    r = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def table_rows(path: Path, start: str, end: str, skip0: tuple) -> list[list[str]]:
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
                    and cells[0] not in skip0:
                rows.append(cells)
    return rows


def diff_html(before: str, after: str, cap: int = DIFF_LINE_CAP) -> str:
    out, n = [], 0
    for line in difflib.unified_diff(before.splitlines(), after.splitlines(),
                                     lineterm="", n=2):
        if line.startswith(("---", "+++")):
            continue
        n += 1
        if n > cap:
            out.append(f'<span class="h">… diff truncated at {cap} lines — '
                       f"full diff on GitHub (link above)</span>")
            break
        cls = ("a" if line.startswith("+")
               else "d" if line.startswith("-")
               else "h" if line.startswith("@@") else "")
        out.append(f'<span class="{cls}">{esc(line)}</span>' if cls
                   else esc(line))
    return "\n".join(out) or '<span class="h">(no textual change)</span>'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=None)
    ap.add_argument("--out", type=Path,
                    default=ROOT / "sources" / "review-watch.html")
    ap.add_argument("--runs", type=Path, default=None,
                    help="JSON of recent review-chunk runs (chain card)")
    args = ap.parse_args()

    base = args.base or git("merge-base", "HEAD", "origin/main").strip() \
        or git("rev-parse", "HEAD").strip()
    head = git("rev-parse", "--short", "HEAD").strip()
    now = time.time()

    wl = table_rows(ROOT / "sources" / "review-worklist.md",
                    "<!-- review:worklist:start -->",
                    "<!-- review:worklist:end -->", ("note",))
    ledger = table_rows(ROOT / "sources" / "fact-check-ledger.md",
                        "<!-- review:ledger:start -->",
                        "<!-- review:ledger:end -->", ("note",))
    reloc = table_rows(ROOT / "sources" / "relocation-queue.md",
                       "<!-- review:relocations:start -->",
                       "<!-- review:relocations:end -->", ("src",))

    # ---- run health -----------------------------------------------------
    statuses = Counter(r[2] for r in wl if len(r) == 5)
    total = sum(statuses.values())
    processed_rows = [r for r in wl if len(r) == 5 and r[2] not in ("pending",)]
    stop = (ROOT / "STOP").exists()
    model = "?"
    m = re.search(r'MODEL_OVERRIDE:\s*"([^"]+)"',
                  (ROOT / ".github/workflows/review-chunk.yml")
                  .read_text(encoding="utf-8"))
    if m:
        model = m.group(1)

    log = git("log", "--format=%H|%ct|%s", "--grep", "^review: ", "-500")
    commits = []
    for line in log.splitlines():
        sha, ct, subj = line.split("|", 2)
        commits.append((sha, int(ct), subj))
    last_age_min = int((now - commits[0][1]) / 60) if commits else None
    # throughput over the last 6h of unit commits (exclude checkpoints)
    unit_commits = [c for c in commits
                    if not c[2].startswith("review: progress checkpoint")
                    and not c[2].startswith("review: guard sweep")]
    recent = [c for c in unit_commits if now - c[1] < 6 * 3600]
    rate = len(recent) / 6.0
    remaining = statuses.get("pending", 0) + statuses.get("transformed", 0)
    eta_h = (remaining / rate) if rate > 0.2 else None

    # phase (mirror next-note priority)
    reloc_pending = sum(1 for r in reloc if len(r) == 6 and r[5] == "pending")
    if any(r[2] == "pending" and r[1] in ("full", "standard", "light")
           for r in wl if len(r) == 5):
        phase = "transform"
    elif reloc_pending:
        phase = "relocations"
    elif any(r[2] == "pending" and r[1] == "gazetteer" for r in wl if len(r) == 5):
        phase = "gazetteer"
    elif statuses.get("transformed", 0):
        phase = "fact-check"
    elif any(r[2] == "pending" and r[1] == "cluster" for r in wl if len(r) == 5):
        phase = "cluster"
    else:
        phase = "drained — endgame"

    # note -> last unit commit sha
    note_commit: dict[str, str] = {}
    for sha, _ct, subj in unit_commits:
        mm = re.match(r"^review: (\S+\.md) ", subj)
        if mm and mm.group(1) not in note_commit:
            note_commit[mm.group(1)] = sha

    # ---- conservation & compression table -------------------------------
    cons_rows, cons_bad = [], 0
    folder_done: Counter = Counter()
    folder_total: Counter = Counter()
    for r in wl:
        if len(r) != 5 or r[0].startswith("cluster:"):
            continue
        folder = r[0].split("/", 1)[0]
        folder_total[folder] += 1
        if r[2] != "pending":
            folder_done[folder] += 1
    for note, tier, status, flags, result in processed_rows:
        if note.startswith("cluster:"):
            continue
        path = ROOT / note
        after = path.read_text(encoding="utf-8") if path.exists() else ""
        before = show(base, note)
        ev_rel = guard.evidence_path(note)
        ev_after = (ROOT / ev_rel).read_text(encoding="utf-8") \
            if (ROOT / ev_rel).exists() else ""
        b_lines = len(before.splitlines()) if before else 0
        a_lines = len(after.splitlines())
        ev_n = len(guard.EVIDENCE_ENTRY_RE.findall(ev_after))
        conserved = True
        if before:
            lost = guard.cited_ids(before) - (guard.cited_ids(after)
                                              | guard.cited_ids(ev_after))
            conserved = not lost
        if not conserved:
            cons_bad += 1
        sha = note_commit.get(note, "")
        links = f'<a href="{GH}/blob/{BRANCH}/{note}">note</a>'
        if ev_after:
            links += f' · <a href="{GH}/blob/{BRANCH}/{ev_rel}">evidence</a>'
        if sha:
            links += f' · <a href="{GH}/commit/{sha}">commit</a>'
        cons_rows.append(
            "<tr><td>" + esc(note) + "</td><td>" + esc(tier) + "</td><td>"
            + esc(status) + '</td><td class="num">'
            + (f"{b_lines} → {a_lines}" if before else f"new, {a_lines}")
            + '</td><td class="num">' + str(ev_n) + "</td><td>"
            + ('<span class="ok">✓</span>' if conserved
               else '<span class="bad">✗ LOST CITES</span>')
            + "</td><td>" + esc(flags) + "</td><td>" + links + "</td></tr>")

    # ---- assemble -------------------------------------------------------
    p: list[str] = [f"<style>{CSS}</style>",
                    "<h1>Review Watch</h1>",
                    f'<p class="muted">KB editorial review · branch {BRANCH} '
                    f"· HEAD {esc(head)} vs base {esc(base[:9])} · built "
                    f"{time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(now))}"
                    "</p>"]

    if stop:
        p.append('<p class="bad">⛔ STOP file present — the chain is standing '
                 "down.</p>")
    p.append('<div class="statgrid">')
    for label, val, cls in [
        ("phase", phase, ""),
        ("model", model, ""),
        ("pending", statuses.get("pending", 0), ""),
        ("transformed", statuses.get("transformed", 0), ""),
        ("fact-checked", statuses.get("fact-checked", 0), ""),
        ("done", statuses.get("done", 0), ""),
        ("escalated", statuses.get("escalated", 0),
         "warn" if statuses.get("escalated", 0) else ""),
        ("cite-loss notes", cons_bad, "bad" if cons_bad else "ok"),
        ("last commit", f"{last_age_min} min ago" if last_age_min is not None
         else "—", ""),
        ("rate (6h)", f"{rate:.1f}/h", ""),
        ("rough ETA", f"{eta_h:.0f} h" if eta_h else "—", ""),
    ]:
        p.append(f'<div class="stat"><div class="n {cls}">{esc(val)}</div>'
                 f'<div class="l">{esc(label)}</div></div>')
    p.append("</div>")

    # folder progress
    p.append("<h2>Progress by folder</h2><div class='bars'>")
    for folder in sorted(folder_total, key=lambda f: -folder_total[f]):
        t, d = folder_total[folder], folder_done[folder]
        pct = int(100 * d / t) if t else 0
        p.append(f"<div>{esc(folder)}/</div>"
                 f"<div class='bar'><div style='width:{pct}%'></div></div>"
                 f"<div class='num'>{d} / {t}</div>")
    p.append("</div>")

    # adjudication queues
    cats = Counter((r[2] if len(r) > 2 else "?") for r in ledger)
    p.append(f"<h2>Fact-check ledger — your adjudication queue "
             f"({len(ledger)})</h2><p>")
    for c, n in cats.most_common():
        p.append(f'<span class="badge">{esc(c)}: {n}</span>')
    p.append("</p>")
    if ledger:
        p.append('<div class="tbl"><table><tr><th>note</th><th>claim</th>'
                 "<th>category</th><th>cite</th><th>detail</th></tr>")
        for r in ledger:
            cells = (r + [""] * 5)[:5]
            p.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in cells)
                     + "</tr>")
        p.append("</table></div>")

    p.append(f"<h2>Relocations ({len(reloc)}, {reloc_pending} pending)</h2>")
    if reloc:
        p.append('<div class="tbl"><table><tr><th>src</th><th>dst</th>'
                 "<th>what</th><th>rationale</th><th>cite</th><th>status</th>"
                 "</tr>")
        for r in reloc:
            p.append("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r[:6])
                     + "</tr>")
        p.append("</table></div>")

    esc_file = ROOT / "sources" / "escalations.md"
    esc_heads = re.findall(r"^## (.+)$", esc_file.read_text(encoding="utf-8"),
                           re.M) if esc_file.exists() else []
    p.append(f"<h2>Escalations ({len(esc_heads)})</h2>")
    if esc_heads:
        p.append("<p>" + "".join(f'<span class="badge">{esc(h)}</span>'
                                 for h in esc_heads[-8:])
                 + f' <span class="muted">(last 8; full log: '
                 f'<a href="{GH}/blob/{BRANCH}/sources/escalations.md">'
                 "sources/escalations.md</a>)</span></p>")

    gap = ROOT / "sources" / "gap-report.md"
    if gap.exists():
        gm = re.search(r"_Totals: (.+?)_", gap.read_text(encoding="utf-8"))
        p.append("<h2>Knowledge gaps</h2><p>"
                 + esc(gm.group(1) if gm else "see gap-report")
                 + f' <span class="muted">(<a href="{GH}/blob/{BRANCH}/'
                 'sources/gap-report.md">full report</a>)</span></p>')

    # conservation table
    p.append(f"<h2>Conservation &amp; compression "
             f"({len(cons_rows)} processed notes)</h2>")
    if cons_rows:
        p.append('<div class="tbl"><table><tr><th>note</th><th>tier</th>'
                 "<th>status</th><th>lines</th><th>evidence entries</th>"
                 "<th>cites conserved</th><th>flags</th><th>links</th></tr>"
                 + "".join(cons_rows) + "</table></div>")
    else:
        p.append('<p class="muted">Nothing processed yet.</p>')

    # recent diffs
    p.append(f"<h2>Recent transforms (inline diff, last {RECENT_DIFFS})</h2>")
    shown = 0
    for sha, _ct, subj in unit_commits:
        mm = re.match(r"^review: (\S+\.md) ", subj)
        if not mm:
            continue
        note = mm.group(1)
        before, after = show(base, note), show("HEAD", note)
        if after is None or before == after:
            continue
        shown += 1
        if shown > RECENT_DIFFS:
            break
        p.append(f"<details><summary>{esc(subj)} — "
                 f'<a href="{GH}/commit/{sha}">commit</a></summary>'
                 f'<pre class="diff">{diff_html(before or "", after)}</pre>'
                 "</details>")
    if not shown:
        p.append('<p class="muted">No diffs vs base yet.</p>')

    # chain card
    if args.runs and args.runs.exists():
        try:
            runs = json.loads(args.runs.read_text())["workflow_runs"]
        except Exception:
            runs = []
        p.append(f"<h2>Chain (last {len(runs)} chunk runs)</h2><p>")
        for r in runs:
            concl = r.get("conclusion") or r.get("status") or "?"
            cls = ("ok" if concl == "success"
                   else "bad" if concl in ("failure", "cancelled") else "warn")
            p.append(f'<span class="badge {cls}">'
                     f'<a href="{GH}/actions/runs/{r.get("id")}">'
                     f'{esc(r.get("created_at", "")[:16])}</a> {esc(concl)}'
                     "</span>")
        p.append("</p>")

    args.out.write_text("\n".join(p), encoding="utf-8")
    print(f"review-watch: {len(cons_rows)} processed notes ({cons_bad} "
          f"cite-loss), {len(ledger)} ledger rows, {len(reloc)} relocations, "
          f"phase={phase} -> {args.out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
