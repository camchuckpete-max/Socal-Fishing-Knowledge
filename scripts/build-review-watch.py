#!/usr/bin/env python3
"""build-review-watch.py — Review Watch v3, the transform-job review surface.

Bight Watch's chassis (sonar map, rail, slide-over article reader, passage
notes with a markdown export), pointed at a TRANSFORM job instead of an
extraction job. Bight Watch answered "did this video's knowledge land?";
this page answers "did the rewrite keep the knowledge?" (Cameron,
2026-08-24: it should look and feel like Bight Watch, drill into articles
and changes, and take structured feedback the same way).

Per note the reviewer gets four tabs — the rewritten Article, the Before
version (as it stood at the merge base), the Changes diff, and the
Evidence file — plus the worklist verdict, cite-conservation check and
GitHub links. Every passage in the Article, Evidence and Changes views is
clickable: rate it 👍/👎, say what's wrong, and export all notes as one
markdown block to hand back (localStorage persists between visits; the
export is the deliverable, exactly like Bight Watch).

The rail carries the transform job's watch: progress by status + phase,
conservation, Cameron's adjudication queues (fact-check ledger,
relocations, escalations), knowledge gaps, recent units, on-deck rows,
activity, chain runs.

Output: sources/review-watch.html (gitignored). Published to GitHub Pages
by publish-review-watch.yml (on main), rebuilt after every chunk + hourly.

    python scripts/build-review-watch.py [--base <ref>] [--out PATH]
                                         [--runs runs.json]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "review"))
import guard  # noqa: E402  (cited_ids, evidence_path, EVIDENCE_ENTRY_RE)


def _load(name: str, fname: str):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).resolve().parent / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Proven pieces, reused rather than re-implemented: the deterministic graph
# layout, the diff parser and the chain-runs loader from Bight Watch; front
# matter / links / commits / escalations collectors from the vault.
_bw = _load("build_bight_watch", "build-bight-watch.py")
_bv = _load("build_vault", "build-vault.py")

# The geographic ladder comes from the census builder, never re-derived here —
# the map and the census must agree by construction, not by coincidence.
_geo_spec = importlib.util.spec_from_file_location(
    "build_geo_worklist",
    Path(__file__).resolve().parent / "review" / "build-geo-worklist.py")
_geo = importlib.util.module_from_spec(_geo_spec)
_geo_spec.loader.exec_module(_geo)

# The phase comes from the DISPATCHER, for the same reason. This page kept its
# own copy of the precedence list and drifted the moment the fleet reordered:
# geo was moved ahead of transform, and the dashboard went on reporting
# "transform" while every unit landing was a geo one. A watch surface that
# disagrees with the thing it watches is worse than no surface.
_nn_spec = importlib.util.spec_from_file_location(
    "next_note", Path(__file__).resolve().parent / "review" / "next-note.py")
_nn = importlib.util.module_from_spec(_nn_spec)
_nn_spec.loader.exec_module(_nn)

# What the dispatcher's bucket names are called on the page.
PHASE_LABEL = {"geo": "geo", "transform": "transform", "relocate": "relocations",
               "gazetteer": "gazetteer", "factcheck": "fact-check",
               "cluster": "cluster"}

GH = "https://github.com/camchuckpete-max/Socal-Fishing-Knowledge"
BRANCH = "claude/knowledge-base-review-g00k8s"
DIFF_LINE_CAP = 400          # per note; overflow is reported, not hidden
# Leaflet is INLINED, not CDN-loaded: the map is a gate review surface and a
# page that silently loses its basemap when a CDN is slow is worse than one
# that carries 160 KB. See scripts/vendor/README.md.
VENDOR = Path(__file__).resolve().parent / "vendor"
LEAFLET_JS = VENDOR / "leaflet-1.9.4.js"
LEAFLET_CSS = VENDOR / "leaflet-1.9.4.css"
SKIP = ("sources/", ".git/", "scripts/", "prompts/", ".github/", "tests/",
        "skills/")


def git(*args: str) -> str:
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def show(ref: str, rel: str) -> str | None:
    r = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


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


def collect_files(base: str) -> list[dict]:
    """Every KB page, with live content, plus the base version when changed."""
    changed, added = set(), set()
    for line in git("diff", "--name-status", f"{base}..HEAD",
                    "--", "*.md").splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        (added if parts[0][:1] == "A" else changed).add(parts[-1])

    files = []
    for p in sorted(ROOT.rglob("*.md")):
        rel = str(p.relative_to(ROOT))
        if rel.startswith(SKIP) or rel == "CLAUDE.md":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        title = next((l[2:].strip() for l in text.splitlines()
                      if l.startswith("# ")), rel)
        st = "added" if rel in added else (
            "modified" if rel in changed else "unchanged")
        row = {
            "path": rel, "title": title,
            "fm": _bv.parse_front_matter(text),
            "links": _bv.outbound_links(text, rel),
            "status": st, "lines": text.count("\n") + 1, "content": text,
        }
        if st == "modified":
            row["old"] = show(base, rel) or ""
        files.append(row)
    return files


def collect_diffs(base: str, files: list[dict]) -> dict:
    out = {}
    for f in files:
        if f["status"] != "modified":
            continue
        parsed, dropped = _bw._parse_diff(
            git("diff", "--unified=2", f"{base}...HEAD", "--", f["path"]),
            cap=DIFF_LINE_CAP)
        if not parsed:
            continue
        # true totals from numstat — the capped parse undercounts big rewrites
        add, rem = _bw._counts(parsed)
        ns = git("diff", "--numstat", f"{base}...HEAD", "--",
                 f["path"]).split()
        if len(ns) >= 2 and ns[0].isdigit() and ns[1].isdigit():
            add, rem = int(ns[0]), int(ns[1])
        out[f["path"]] = {"hunks": parsed[0]["hunks"], "add": add, "rem": rem,
                          "dropped": dropped}
    return out


def collect_gaps() -> dict:
    p = ROOT / "sources" / "gap-report.md"
    if not p.exists():
        return {"totals": "", "items": []}
    text = p.read_text(encoding="utf-8")
    m = re.search(r"_Totals: (.+?)_", text)
    items, cur = [], None
    if "<!-- review:gaps:start -->" in text:
        block = text.split("<!-- review:gaps:start -->", 1)[1] \
                    .split("<!-- review:gaps:end -->", 1)[0]
        for line in block.splitlines():
            bm = re.match(r"^- \*\*(\S+\.md)\*\*", line.strip())
            if bm:
                cur = {"note": bm.group(1), "lines": []}
                items.append(cur)
            elif cur and line.strip().startswith("- "):
                cur["lines"].append(line.strip()[2:])
    return {"totals": m.group(1) if m else "", "items": items}


def build(base: str, runs_path: str | None) -> dict:
    now = time.time()
    files = collect_files(base)
    wl_cells = table_rows(ROOT / "sources" / "review-worklist.md",
                          "<!-- review:worklist:start -->",
                          "<!-- review:worklist:end -->", ("note",))
    wl = [dict(zip(("n", "t", "s", "f", "r"), (c + [""] * 5)[:5]))
          for c in wl_cells]
    ledger = table_rows(ROOT / "sources" / "fact-check-ledger.md",
                        "<!-- review:ledger:start -->",
                        "<!-- review:ledger:end -->", ("note",))
    reloc = table_rows(ROOT / "sources" / "relocation-queue.md",
                       "<!-- review:relocations:start -->",
                       "<!-- review:relocations:end -->", ("src",))
    spots = table_rows(ROOT / "sources" / "spot-harvest.md",
                       "<!-- review:harvest:start -->",
                       "<!-- review:harvest:end -->", ("spot", "name"))

    statuses = Counter(r["s"] for r in wl)
    total = len(wl)
    processed = sum(v for k, v in statuses.items() if k != "pending")

    model = "?"
    wf = ROOT / ".github/workflows/review-chunk.yml"
    if wf.exists():
        m = re.search(r'MODEL_OVERRIDE:\s*"([^"]+)"',
                      wf.read_text(encoding="utf-8"))
        if m:
            model = m.group(1)

    # review commits: unit shas, throughput, recency
    log = git("log", "--format=%H|%ct|%s", "--grep", "^review: ", "-500")
    rcommits = []
    for line in log.splitlines():
        sha, ct, subj = line.split("|", 2)
        rcommits.append((sha, int(ct), subj))
    unit_commits = [c for c in rcommits
                    if not c[2].startswith("review: progress checkpoint")
                    and not c[2].startswith("review: guard sweep")]
    last_age_min = int((now - rcommits[0][1]) / 60) if rcommits else None
    recent6 = [c for c in unit_commits if now - c[1] < 6 * 3600]
    rate = len(recent6) / 6.0
    remaining = statuses.get("pending", 0) + statuses.get("transformed", 0)
    eta_h = round(remaining / rate) if rate > 0.2 else None

    note_commit: dict[str, str] = {}
    unit_order: list[str] = []          # most recent first
    for sha, _ct, subj in unit_commits:
        mm = re.match(r"^review: (\S+\.md) ", subj)
        if mm and mm.group(1) not in note_commit:
            note_commit[mm.group(1)] = sha[:9]
            unit_order.append(mm.group(1))

    # phase — MIRRORS scripts/review/next-note.py buckets(). Keep the two in
    # step: without a `geo` branch here, geo rows pending with no gazetteer
    # rows pending fell through to "drained — endgame" and reported the fleet
    # finished while the whole ladder was still unbuilt.
    reloc_pending = sum(1 for r in reloc if len(r) == 6 and r[5] == "pending")
    phase = "drained — endgame"
    for name, rows_ in _nn.buckets():
        if rows_:
            phase = PHASE_LABEL.get(name, name)
            break

    # per-note review record: verdict, conservation, evidence, links
    by_path = {f["path"]: f for f in files}
    rev: dict[str, dict] = {}
    cons_bad: list[str] = []
    for r in wl:
        note = r["n"]
        if note.startswith("cluster:") or not note.endswith(".md"):
            continue
        entry = {"tier": r["t"], "status": r["s"], "flags": r["f"],
                 "result": r["r"], "sha": note_commit.get(note, "")}
        if r["s"] != "pending":
            f = by_path.get(note)
            after = f["content"] if f else ""
            before = f.get("old") if f else None
            ev_rel = guard.evidence_path(note)
            ev = by_path.get(ev_rel)
            ev_text = ev["content"] if ev else ""
            entry["evPath"] = ev_rel if ev else ""
            entry["evN"] = len(guard.EVIDENCE_ENTRY_RE.findall(ev_text))
            entry["bL"] = len(before.splitlines()) if before else 0
            entry["aL"] = len(after.splitlines())
            lost = sorted(guard.cited_ids(before or "")
                          - (guard.cited_ids(after) | guard.cited_ids(ev_text)))
            entry["lost"] = lost
            if lost:
                cons_bad.append(note)
        rev[note] = entry

    # which marks ping: the notes the latest review commits touched
    recent: dict[str, int] = {}
    for i, path in enumerate(unit_order[:14]):
        recent.setdefault(path, i)
    for f in files:
        f["recent"] = recent.get(f["path"], -1)

    # graph layout — evidence pages and templates are reference material,
    # not marks on the sonar
    graph_files = [f for f in files
                   if "/evidence/" not in f["path"]
                   and not f["path"].startswith("templates/")]
    layout = _bw.layout_graph(graph_files)

    # ---- the geographic ladder, for the map view -------------------------
    geo = {"spots": [], "zones": [], "outliers": 0, "error": ""}
    try:
        raw_spots = _geo.parse_spot_lists()
        zones, spot_rows, ar_series, non_spot, unassigned = _geo.build_zones(
            raw_spots, docs=None)
        jur = {"socal-bight": "us-waters"}
        zmeta, zid = [], {}
        for i, z in enumerate(zones):
            zid[id(z)] = i
            c = _geo.centre(z["spots"]) if z["spots"] else None
            zmeta.append({
                "i": i, "name": z["display"], "slug": z["slug"],
                "region": z["region"],
                "jur": jur.get(z["region"], "mexican-waters"),
                "src": z["src"], "n": len(z["spots"]),
                "lat": round(c["lat"], 5) if c else None,
                "lon": round(c["lon"], 5) if c else None,
                "hull": [[round(s["lat"], 5), round(s["lon"], 5)]
                         for s in z["spots"]],
            })
        pins = []
        for r in spot_rows:
            src = next((s for s in r["zone"]["spots"]
                        if s["name"] == r["display"]), None)
            if not src:
                continue
            pins.append({
                "name": r["display"], "slug": r["slug"],
                "lat": round(src["lat"], 5), "lon": round(src["lon"], 5),
                "z": zid[id(r["zone"])], "d": round(r["dist"], 1),
                "far": r["dist"] > _geo.MAX_ZONE_DIAMETER_NM,
            })
        for key, a in ar_series.items():
            members = [s for s in a["zone"]["spots"]
                       if _geo.AR_SERIES.match(s["name"])
                       and _geo.slugify((_geo.AR_SERIES.match(s["name"]).group(1)
                                         or _geo.AR_SERIES.match(s["name"]).group(2)
                                         ).strip()) == key]
            for m in members:
                pins.append({
                    "name": m["name"], "slug": key, "ar": a["display"],
                    "lat": round(m["lat"], 5), "lon": round(m["lon"], 5),
                    "z": zid[id(a["zone"])],
                    "d": round(_geo.nm(m, _geo.centre(a["zone"]["spots"])), 1),
                    "far": False})
        for name, zone_name in non_spot:
            src = next((s for s in raw_spots if s["name"] == name), None)
            if src:
                pins.append({"name": name, "slug": "", "excluded": True,
                             "lat": round(src["lat"], 5),
                             "lon": round(src["lon"], 5), "z": -1, "d": 0,
                             "far": False})
        # what the corpus already says about each spot, keyed by slug — so a
        # page that has not been generated yet can still answer "does the KB
        # know anything about this place?"
        harvest: dict[str, list] = {}
        for row in spots:
            cells = (row + [""] * 5)[:5]
            harvest.setdefault(_geo.slugify(cells[0]), []).append(
                {"note": cells[1], "section": cells[2],
                 "claim": cells[3][:240], "cite": cells[4]})
        geo = {"spots": pins, "zones": zmeta, "harvest": harvest,
               "outliers": sum(1 for p_ in pins if p_.get("far")),
               "maxDiam": _geo.MAX_ZONE_DIAMETER_NM, "error": ""}
    except Exception as exc:                      # never break the dashboard
        geo["error"] = f"{type(exc).__name__}: {exc}"

    base_iso = git("show", "-s", "--format=%cI", base).strip()
    snap = {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD").strip(),
        "headSha": git("rev-parse", "--short", "HEAD").strip(),
        "baseSha": git("rev-parse", "--short", base).strip(),
        "phase": phase, "model": model,
        "stop": (ROOT / "STOP").exists(),
        "rateH": round(rate, 1), "etaH": eta_h, "lastAgeMin": last_age_min,
        "counts": dict(statuses), "totalUnits": total,
        "processedUnits": processed,
        "folderColor": _bw.FOLDER_COLOR,
        "files": files, "layout": layout,
        "worklist": wl, "rev": rev, "consBad": cons_bad,
        "unitOrder": unit_order,
        "diffs": collect_diffs(base, files),
        "ledger": ledger, "reloc": reloc, "relocPending": reloc_pending,
        "spots": len(spots),
        "gaps": collect_gaps(),
        # only escalations raised since the branch base — the file also holds
        # batch-2/3 history that is not this review's queue
        "escal": [e for e in _bv.collect_escalations(base_iso)
                  if e.get("thisBatch")],
        "commits": _bv.collect_commits(base, limit=40),
        "runs": _bw.load_runs(runs_path) if runs_path else [],
        "gh": GH,
        "geo": geo,
    }
    return snap


HTML = r"""<title>Review Watch</title>
<style>__LEAFLET_CSS__</style>
<script>__LEAFLET_JS__</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Bight Watch's sonar-screen design system, verbatim: light default, dark by
   preference or toggle; every colour a token so a theme never half-applies. */
:root{
  --bg:#f2f5f5; --panel:#ffffff; --panel2:#e8eeee; --ink:#132227; --ink2:#3f5359;
  --muted:#697f85; --hair:rgba(19,34,39,.14);
  --accent:#0f7d8a; --accent-ink:#0b626d;
  --good:#177a2f; --serious:#b2531f; --critical:#b03030; --pend:#c3cfd1;
  --ring:rgba(19,34,39,.28); --noteb:rgba(178,83,31,.16);
  --shadow:0 1px 2px rgba(0,0,0,.06),0 6px 20px rgba(0,0,0,.07);
  --vig:rgba(210,222,222,.5);
  --display:"Barlow Condensed",system-ui,sans-serif;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  color-scheme:light;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#0B1517; --panel:#122025; --panel2:#16262C; --ink:#D9E4E6; --ink2:#9FB2B7;
    --muted:#6E8288; --hair:rgba(217,228,230,.13);
    --accent:#3FB4C1; --accent-ink:#63C5D0;
    --good:#21b421; --serious:#ec835a; --critical:#e05252; --pend:#33454B;
    --ring:rgba(99,197,208,.34); --noteb:rgba(214,132,74,.20);
    --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 16px rgba(0,0,0,.35);
    --vig:rgba(4,10,12,.55);
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#0B1517; --panel:#122025; --panel2:#16262C; --ink:#D9E4E6; --ink2:#9FB2B7;
  --muted:#6E8288; --hair:rgba(217,228,230,.13);
  --accent:#3FB4C1; --accent-ink:#63C5D0;
  --good:#21b421; --serious:#ec835a; --critical:#e05252; --pend:#33454B;
  --ring:rgba(99,197,208,.34); --noteb:rgba(214,132,74,.20);
  --shadow:0 1px 2px rgba(0,0,0,.3),0 4px 16px rgba(0,0,0,.35);
  --vig:rgba(4,10,12,.55);
  color-scheme:dark;
}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 var(--sans);overflow:hidden}
.display{font-family:var(--display);letter-spacing:.01em;text-wrap:balance}
button{font-family:inherit;cursor:pointer}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

/* intro */
.intro{position:fixed;inset:0;z-index:1500;background:var(--vig);backdrop-filter:blur(7px);
  display:grid;place-items:center;padding:20px}
.intro[hidden]{display:none}
.intro-card{background:var(--panel);border:1px solid var(--hair);border-radius:16px;
  box-shadow:var(--shadow);max-width:640px;padding:26px 28px}
.intro-card h2{margin:0 0 6px;font-size:38px;font-weight:700}
.lead{color:var(--ink2);margin:0 0 14px}
.intro-card ul{margin:0 0 18px;padding-left:18px;color:var(--ink2)}
.intro-card li{margin:7px 0}
.k1{color:var(--accent-ink);font-weight:600}
.go{background:var(--accent);color:#fff;border:none;border-radius:9px;padding:9px 16px;
  font-size:14px;font-weight:600;margin-right:8px}
.go.alt{background:transparent;color:var(--accent-ink);border:1px solid var(--hair)}

.app{display:flex;flex-direction:column;height:100vh}
.bar{display:flex;align-items:center;gap:14px;padding:10px 16px;background:var(--panel);
  border-bottom:1px solid var(--hair);flex:none;flex-wrap:wrap}
.brand h1{margin:0;font-size:23px;font-weight:700;line-height:1.1}
.brand .sub{font-size:11.5px;color:var(--muted)}
.spacer{flex:1}
.pill{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--hair);border-radius:20px;
  padding:3px 11px;font-size:12px;color:var(--ink2);white-space:nowrap}
.pill[hidden]{display:none}
.dot{width:8px;height:8px;border-radius:50%;background:var(--muted);flex:none}
.dot.ok{background:var(--good)}.dot.wait{background:var(--serious)}
.dot.bad{background:var(--critical)}
.clockbox{text-align:right}
.clock{font-family:var(--mono);font-size:13px;color:var(--ink2);font-variant-numeric:tabular-nums}
.stamp{font-size:10.5px;color:var(--muted);position:relative}
.stale{position:absolute;right:0;top:20px;z-index:30;width:290px;text-align:left;
  background:var(--panel);border:1px solid var(--hair);border-radius:10px;
  box-shadow:var(--shadow);padding:10px 12px;font-size:11.5px;line-height:1.5;color:var(--ink2)}
.stale[hidden]{display:none}
.stale a{color:var(--accent-ink)}
.linkbtn{background:none;border:none;padding:0 0 0 2px;font:inherit;color:var(--accent-ink);
  font-weight:600;text-decoration:underline}
.mono{font-family:var(--mono)}
.help{background:var(--panel2);border:1px solid var(--hair);color:var(--ink2);border-radius:8px;
  width:32px;height:32px;font-size:15px}
main{flex:1;display:flex;min-height:0}
#graphwrap{flex:1;position:relative;min-width:0;overflow:hidden;background:
  radial-gradient(ellipse at 50% 45%, transparent 40%, var(--vig) 100%)}
#graph{display:block;width:100%;height:100%;cursor:grab}
#graph.drag{cursor:grabbing}
.legend{position:absolute;left:14px;bottom:14px;background:var(--panel);border:1px solid var(--hair);
  border-radius:10px;padding:9px 12px;font-size:11.5px;color:var(--ink2);box-shadow:var(--shadow);
  max-width:230px;display:flex;flex-wrap:wrap;gap:4px 12px}
.legend .lg{display:flex;align-items:center;gap:6px}
.legend .sw{width:9px;height:9px;border-radius:50%}
.legend .swr{width:9px;height:9px;border-radius:50%;border:2px solid var(--good);background:none}
.legend .swr.esc{border-color:var(--critical)}
.legend .swr.dim{border:none;background:var(--pend)}
.tip{position:absolute;pointer-events:none;background:var(--panel);border:1px solid var(--hair);
  border-radius:8px;padding:5px 9px;font-size:12px;box-shadow:var(--shadow);display:none;z-index:5}
.gstat{position:absolute;right:14px;top:12px;font-family:var(--mono);font-size:11px;color:var(--muted);
  text-align:right;font-variant-numeric:tabular-nums}

/* map view — the geographic ladder on real ground */
#mapwrap{position:absolute;inset:0;display:none}
#mapwrap.on{display:block}
#graphwrap.mapmode #graph,#graphwrap.mapmode .legend,#graphwrap.mapmode .gstat{display:none}
#map{position:absolute;inset:0;background:var(--panel2)}
.leaflet-container{background:var(--panel2);font:12px var(--sans)}
.leaflet-popup-content-wrapper,.leaflet-popup-tip{background:var(--panel);color:var(--ink);
  box-shadow:var(--shadow)}
.leaflet-popup-content{margin:10px 12px;font:12.5px var(--sans)}
.leaflet-bar a{background:var(--panel);color:var(--ink);border-color:var(--hair)}
.leaflet-bar a:hover{background:var(--panel2)}
.leaflet-control-attribution{background:color-mix(in srgb,var(--panel) 88%,transparent)!important;
  color:var(--muted)!important;font-size:10px}
.leaflet-control-attribution a{color:var(--accent-ink)!important}
.mapfail{position:absolute;inset:0;display:grid;place-items:center;text-align:center;
  padding:24px;color:var(--ink2);font-size:13px}
/* Stacking, and why the numbers are large: Leaflet's panes run to 400 and its
   controls to 800, all inside #mapwrap, which sets no z-index of its own — so
   its descendants compete directly with the page chrome. The slide-over read
   z-index:20 and was therefore painted UNDER the map: clicking a pin opened
   the article behind the tiles, and only a zoom (which clears the panes for a
   frame) let you glimpse it. Map chrome 1200 < slide-over 1300 < note popup
   1400 < intro 1500. */
.mpanel{position:absolute;z-index:1200;top:12px;left:12px;width:232px;max-height:calc(100% - 24px);
  overflow-y:auto;background:var(--panel);border:1px solid var(--hair);border-radius:11px;
  box-shadow:var(--shadow);padding:11px 12px;font-size:12px}
.mpanel h4{margin:0 0 7px;font-size:10.5px;font-weight:700;letter-spacing:.09em;
  text-transform:uppercase;color:var(--muted)}
.mpanel h4:not(:first-child){margin-top:12px}
.mrow{display:flex;align-items:center;gap:7px;padding:2px 0;cursor:pointer;color:var(--ink2)}
.mrow:hover{color:var(--ink)}
.mrow input{accent-color:var(--accent);margin:0}
.mrow .sw{width:10px;height:10px;border-radius:50%;flex:none}
.mrow .ct{margin-left:auto;font-family:var(--mono);font-size:10px;color:var(--muted)}
.mcrumb{position:absolute;z-index:1200;left:12px;bottom:12px;right:12px;max-width:640px;
  background:var(--panel);border:1px solid var(--hair);border-radius:11px;
  box-shadow:var(--shadow);padding:9px 12px;font-size:12.5px;color:var(--ink2)}
.mcrumb[hidden]{display:none}
.mcrumb b{color:var(--ink)}
.mcrumb .sep{color:var(--muted);margin:0 6px}
.mcrumb .far{color:var(--critical);font-weight:600}
.mcrumb .op{margin-left:auto}
.mcrumb .line{display:flex;align-items:center;flex-wrap:wrap;gap:2px}
.mcrumb .pick{display:block;width:100%;text-align:left;background:var(--panel2);
  border:1px solid var(--hair);border-radius:8px;padding:6px 9px;margin-top:5px;
  color:var(--ink);font:inherit;cursor:pointer}
.mcrumb .pick:hover{border-color:var(--accent)}
.mcrumb .pick .mut{float:right;color:var(--muted);font-size:11.5px}
.viewtoggle{display:inline-flex;border:1px solid var(--hair);border-radius:8px;overflow:hidden}
.viewtoggle button{background:var(--panel2);border:none;color:var(--ink2);padding:5px 12px;
  font-size:12px;font-weight:600}
.viewtoggle button[aria-selected="true"]{background:var(--accent);color:#fff}

/* detail slide-over */
.detail{position:absolute;top:0;right:0;bottom:0;width:min(620px,94%);background:var(--panel);
  border-left:1px solid var(--hair);box-shadow:var(--shadow);transform:translateX(101%);
  transition:transform .22s ease;display:flex;flex-direction:column;z-index:1300}
.detail.open{transform:none}
@media (prefers-reduced-motion:reduce){.detail{transition:none}}
.dhead{padding:14px 16px;border-bottom:1px solid var(--hair);flex:none}
.dtitle{font-family:var(--display);font-size:24px;font-weight:700;margin:0}
.dpath{font-family:var(--mono);font-size:11px;color:var(--muted)}
.dmeta{display:flex;flex-wrap:wrap;gap:5px;margin-top:9px}
.tag{font-family:var(--mono);font-size:10.5px;border:1px solid var(--hair);border-radius:20px;
  padding:1px 8px;color:var(--ink2)}
.tag.high{color:var(--good);border-color:color-mix(in srgb,var(--good) 45%,transparent)}
.tag.medium{color:var(--serious);border-color:color-mix(in srgb,var(--serious) 45%,transparent)}
.tag.low{color:var(--critical);border-color:color-mix(in srgb,var(--critical) 45%,transparent)}
.tag.st-done{color:var(--good);border-color:color-mix(in srgb,var(--good) 45%,transparent)}
.tag.st-transformed,.tag.st-fact-checked{color:var(--accent-ink);
  border-color:color-mix(in srgb,var(--accent) 45%,transparent)}
.tag.st-escalated,.tag.st-reverted{color:var(--critical);
  border-color:color-mix(in srgb,var(--critical) 45%,transparent)}
.tag a{color:inherit;text-decoration:none}
.tag a:hover{text-decoration:underline}
.dclose{position:absolute;top:11px;right:12px;background:var(--panel2);border:1px solid var(--hair);
  color:var(--ink2);border-radius:8px;width:30px;height:30px;font-size:15px}
.darticle{overflow-y:auto;padding:16px 18px 60px;flex:1}
.darticle h1{font-size:22px;margin:2px 0 12px}
.darticle h2{font-size:17px;margin:20px 0 7px;padding-bottom:4px;border-bottom:1px solid var(--hair)}
.darticle h3{font-size:14.5px;margin:15px 0 5px}
.darticle p,.darticle li{color:var(--ink)}
.darticle a{color:var(--accent-ink);text-decoration:none}.darticle a:hover{text-decoration:underline}
.darticle pre{background:var(--panel2);border:1px solid var(--hair);border-radius:8px;
  padding:10px 12px;overflow-x:auto;font-size:12px;line-height:1.45}
.darticle pre code{background:none;border:none;padding:0}
.darticle code{font-family:var(--mono);font-size:12px;background:var(--panel2);border-radius:4px;padding:1px 5px}
.darticle blockquote{margin:9px 0;padding:3px 13px;border-left:3px solid var(--accent);color:var(--ink2)}
.tw{overflow-x:auto;border:1px solid var(--hair);border-radius:8px;margin:10px 0}
.darticle table{border-collapse:collapse;font-size:12px;min-width:100%}
.darticle th{background:var(--panel2);text-align:left;color:var(--ink2);font-weight:600}
.darticle th,.darticle td{padding:5px 9px;border-bottom:1px solid var(--hair);vertical-align:top}

/* panel navigation — the slide-over is a stack: list -> note tabs */
.dback{background:none;border:none;color:var(--accent-ink);font-size:12px;padding:0 0 4px;
  font-weight:600}
.dtabs{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap}
.dtab{background:var(--panel2);border:1px solid var(--hair);color:var(--ink2);border-radius:8px;
  padding:4px 11px;font-size:12px;font-weight:600}
.dtab[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.seemore{display:block;width:100%;margin-top:9px;background:var(--panel2);border:1px solid var(--hair);
  border-radius:8px;padding:6px 9px;font-size:12px;font-weight:600;color:var(--accent-ink);
  text-align:left}
.seemore:hover{border-color:var(--accent)}

/* the review bar atop an article */
.hbar{position:sticky;top:0;z-index:5;display:flex;gap:9px;align-items:center;flex-wrap:wrap;
  background:var(--panel);border:1px solid var(--hair);border-radius:10px;
  padding:7px 11px;margin:0 0 14px;font-size:12px;color:var(--ink2)}
.hsw{width:11px;height:11px;border-radius:3px;flex:none;
  background:color-mix(in srgb,var(--accent) 28%,transparent);
  border:1px solid color-mix(in srgb,var(--accent) 60%,transparent)}

/* review notes — the reviewer's half of the surface. In review mode every
   block is a target: hover shows it, a saved note pins it. */
.darticle.rev .sel{cursor:pointer;border-radius:2px;scroll-margin-top:58px}
.darticle.rev .sel:hover{background:color-mix(in srgb,var(--accent) 12%,transparent);
  box-shadow:-10px 0 0 color-mix(in srgb,var(--accent) 12%,transparent),
             10px 0 0 color-mix(in srgb,var(--accent) 12%,transparent)}
.darticle .sel.noted{background:color-mix(in srgb,var(--serious) 10%,transparent);
  box-shadow:-10px 0 0 var(--noteb),10px 0 0 var(--noteb),inset 3px 0 0 var(--serious)}
.darticle .sel.noted.up{box-shadow:-10px 0 0 color-mix(in srgb,var(--good) 14%,transparent),
  10px 0 0 color-mix(in srgb,var(--good) 14%,transparent),inset 3px 0 0 var(--good)}
.sel .flag{float:right;margin-left:8px;font-size:11px;font-family:var(--mono);
  color:var(--serious);user-select:none}
.sel .flag.up{color:var(--good)}
.notebox{position:fixed;z-index:1400;width:min(400px,92vw);background:var(--panel);
  border:1px solid var(--hair);border-radius:12px;box-shadow:var(--shadow);padding:13px 14px}
.notebox[hidden]{display:none}
.notebox h3{margin:0 0 4px;font-size:13px;font-weight:700}
.notebox .quo{font-size:11.5px;color:var(--muted);margin:0 0 10px;max-height:64px;overflow:hidden}
.notebox textarea{width:100%;min-height:74px;resize:vertical;background:var(--panel2);
  border:1px solid var(--hair);border-radius:8px;padding:8px 9px;font:13px var(--sans);
  color:var(--ink)}
.rate{display:flex;gap:7px;margin:9px 0}
.rate button{flex:1;background:var(--panel2);border:1px solid var(--hair);color:var(--ink2);
  border-radius:8px;padding:6px;font-size:13px;font-weight:600}
.rate button[aria-pressed="true"]{color:#fff}
.rate button.up[aria-pressed="true"]{background:var(--good);border-color:var(--good)}
.rate button.down[aria-pressed="true"]{background:var(--critical);border-color:var(--critical)}
.nb-act{display:flex;gap:7px;justify-content:flex-end;margin-top:4px}
.nb-act button{background:var(--panel2);border:1px solid var(--hair);color:var(--ink2);
  border-radius:8px;padding:6px 12px;font-size:12.5px;font-weight:600}
.nb-act .save{background:var(--accent);border-color:var(--accent);color:#fff}
.nb-act .del{color:var(--critical)}
.expbox{width:100%;min-height:340px;resize:vertical;background:var(--panel2);
  border:1px solid var(--hair);border-radius:8px;padding:10px;font:12px var(--mono);
  color:var(--ink);white-space:pre;overflow-wrap:normal;overflow-x:auto}
.warn{background:color-mix(in srgb,var(--serious) 14%,transparent);
  border:1px solid color-mix(in srgb,var(--serious) 45%,transparent);
  border-radius:8px;padding:8px 10px;font-size:12px;margin:0 0 10px}

/* diffs */
.dfile{border:1px solid var(--hair);border-radius:10px;margin:0 0 12px;overflow:hidden}
.dfile > summary{padding:8px 11px;background:var(--panel2);cursor:pointer;font-size:12.5px;
  display:flex;gap:9px;align-items:center;list-style:none}
.dfile > summary::-webkit-details-marker{display:none}
.dfile > summary::before{content:"▸";color:var(--muted);font-size:11px}
.dfile[open] > summary::before{content:"▾"}
.dfile .fp{font-family:var(--mono);font-size:11.5px;color:var(--ink);overflow-wrap:anywhere}
.plus{color:var(--good);font-family:var(--mono);font-size:11px;font-weight:600}
.minus{color:var(--critical);font-family:var(--mono);font-size:11px;font-weight:600}
.hunk{border-top:1px solid var(--hair)}
.hunk .at{font-family:var(--mono);font-size:10.5px;color:var(--muted);padding:4px 11px;
  background:color-mix(in srgb,var(--panel2) 60%,transparent)}
.dl{font-family:var(--mono);font-size:11.5px;line-height:1.5;padding:1px 11px 1px 22px;
  white-space:pre-wrap;overflow-wrap:anywhere;position:relative;color:var(--ink2)}
.dl::before{position:absolute;left:8px;color:var(--muted)}
.dl.add{background:color-mix(in srgb,var(--good) 15%,transparent);color:var(--ink)}
.dl.add::before{content:"+";color:var(--good)}
.dl.del{background:color-mix(in srgb,var(--critical) 13%,transparent);color:var(--ink2)}
.dl.del::before{content:"−";color:var(--critical)}
.darticle.rev .dl:hover{outline:1px solid var(--accent);cursor:pointer}
.dl.noted{outline:2px solid var(--serious)}
.dl.noted.up{outline-color:var(--good)}
.dnote{font-size:11.5px;color:var(--muted);padding:7px 11px;border-top:1px solid var(--hair)}
.vrow{display:block;width:100%;text-align:left;background:none;border:none;border-bottom:1px solid var(--hair);
  padding:8px 2px;font-size:12.5px;color:var(--ink)}
.vrow:last-child{border-bottom:none}
.vrow:hover{background:var(--panel2)}
.vrow .vt{display:block;font-weight:600;overflow-wrap:anywhere}
.vrow .vm{display:block;color:var(--muted);font-size:11px;font-family:var(--mono);margin-top:2px}
.filt{width:100%;background:var(--panel2);border:1px solid var(--hair);border-radius:8px;
  padding:7px 10px;font:13px var(--sans);color:var(--ink);margin-bottom:10px}
.ghead{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
  margin:16px 0 5px}
.ghead:first-child{margin-top:0}

/* right rail */
.rail{width:340px;flex:none;border-left:1px solid var(--hair);background:var(--panel);
  overflow-y:auto;padding:12px}
@media (max-width:940px){
  body{overflow:auto}
  .app{height:auto;min-height:100vh}
  main{flex-direction:column}
  #graphwrap{flex:none;height:58vh;min-height:340px}
  .rail{width:auto;flex:none;border-left:none;border-top:1px solid var(--hair);overflow:visible}
  .detail{position:fixed;z-index:1300}
}
.card{border:1px solid var(--hair);border-radius:12px;padding:12px 13px;margin-bottom:11px;background:var(--panel)}
.card h2{margin:0 0 9px;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);display:flex;gap:8px;align-items:center}
.card h2 .sp{flex:1}
.card h2 .sub{font-weight:400;letter-spacing:0;text-transform:none;font-family:var(--mono);
  font-size:10.5px;color:var(--muted)}
.meter{height:9px;border-radius:5px;background:var(--pend);overflow:hidden;display:flex;gap:2px}
.meter span{display:block;height:100%}
.tally{display:flex;gap:10px;margin-top:8px;font-size:12px;color:var(--ink2);flex-wrap:wrap;
  font-variant-numeric:tabular-nums}
.tally b{font-family:var(--mono);color:var(--ink)}
.row{display:flex;gap:8px;align-items:baseline;padding:5px 0;border-bottom:1px solid var(--hair);font-size:12.5px}
.row:last-child{border-bottom:none}
.row .vid{font-family:var(--mono);font-size:10.5px;color:var(--muted);flex:none}
.row .txt{color:var(--ink2);overflow-wrap:anywhere}
.row .when{margin-left:auto;font-family:var(--mono);font-size:10px;color:var(--muted);flex:none}
.badge{display:inline-block;background:var(--panel2);border:1px solid var(--hair);border-radius:10px;
  padding:0 8px;margin:0 4px 4px 0;font-size:11.5px;color:var(--ink2)}
.mut{color:var(--muted);font-size:12px}
::-webkit-scrollbar{width:9px;height:9px}
::-webkit-scrollbar-thumb{background:var(--pend);border-radius:6px}
</style>

<div class="intro" id="intro">
  <div class="intro-card">
    <h2 class="display">Review Watch</h2>
    <p class="lead">Claude is rewriting Cameron's fishing knowledgebase —
    <strong id="introN">—</strong> pages — onto the wiki-style layout: plain statements with
    citations, evidence split out, fact-checks queued. This screen is the watch on that
    rewrite, and the place to judge it.</p>
    <ul>
      <li><span class="k1">The sonar screen</span> is the knowledgebase — every mark a page,
      coloured by topic. A ringed mark has been rewritten; pinging marks were just committed.
      Tap one to read it.</li>
      <li><span class="k1">Each page opens with tabs</span>: the rewritten article, the version
      it replaced, the exact diff, and its evidence file.</li>
      <li><span class="k1">Your job</span>: click any passage (or diff line), rate it
      👍/👎, say what's wrong. Export your notes when you're done — that markdown block is the
      feedback that steers the fleet. 🎣</li>
    </ul>
    <button class="go" id="introgo">Start reviewing</button>
    <button class="go alt" id="introrandom">🎲 Random rewritten page</button>
  </div>
</div>

<div class="app">
  <header class="bar">
    <div class="brand">
      <h1 class="display">Review Watch</h1>
      <div class="sub" id="subline"></div>
    </div>
    <span class="pill" id="phasepill"><span class="dot ok"></span><span id="phasetext"></span></span>
    <span class="pill" id="chainpill"><span class="dot" id="chaindot"></span><span id="chaintext">chain</span></span>
    <span class="pill" id="stoppill" hidden><span class="dot bad"></span><span>STOP — chain standing down</span></span>
    <div class="spacer"></div>
    <div class="clockbox">
      <div class="clock" id="clock">--:--:-- UTC</div>
      <div class="stamp">snapshot <span class="mono" id="gen"></span> · <span id="age"></span>
        <button class="linkbtn" id="refresh">refresh</button>
        <div class="stale" id="stale" hidden></div></div>
    </div>
    <span class="viewtoggle" id="viewtoggle">
      <button data-view="sonar" aria-selected="true">Sonar</button>
      <button data-view="map" aria-selected="false">Map</button>
    </span>
    <button class="help" id="themebtn" aria-label="Toggle day / night mode">☾</button>
    <button class="help" id="helpbtn" aria-label="What am I looking at?">?</button>
  </header>
  <main>
    <div id="graphwrap">
      <canvas id="graph" aria-label="Knowledgebase link graph"></canvas>
      <div class="gstat" id="gstat"></div>
      <div class="legend" id="legend"></div>
      <div class="tip" id="tip"></div>
      <div id="mapwrap">
        <div id="map"></div>
        <div class="mpanel" id="mpanel"></div>
        <div class="legend" id="mlegend"></div>
        <div class="mcrumb" id="mcrumb" hidden></div>
      </div>
      <div class="detail" id="detail" role="dialog" aria-label="Page detail">
        <button class="dclose" id="dclose" aria-label="Close">✕</button>
        <div class="dhead">
          <button class="dback" id="dback" hidden>← <span id="dbacktext"></span></button>
          <h2 class="dtitle" id="dtitle"></h2>
          <div class="dpath mono" id="dpath"></div>
          <div class="dmeta" id="dmeta"></div>
          <div class="dtabs" id="dtabs" hidden></div>
        </div>
        <div class="darticle" id="darticle"></div>
      </div>
    </div>
    <aside class="rail">
      <div class="card">
        <h2>Review progress<span class="sp"></span><span class="sub" id="pcttext"></span></h2>
        <div class="meter" id="meter"></div>
        <div class="tally" id="tally"></div>
        <button class="seemore" id="seeprocessed">See every processed page →</button>
        <button class="seemore" id="seeall">Browse the whole knowledgebase →</button>
      </div>
      <div class="card" id="chaincard" hidden><h2>Chain<span class="sp"></span><span class="sub" id="chainsub"></span></h2>
        <div id="runs"></div></div>
      <div class="card"><h2>Conservation<span class="sp"></span><span class="sub" id="conssub"></span></h2>
        <div id="conslist" class="mut"></div></div>
      <div class="card"><h2>Your adjudication queues<span class="sp"></span><span class="sub" id="adjsub"></span></h2>
        <div id="adjcats"></div>
        <button class="seemore" id="seeledger">Fact-check ledger →</button>
        <button class="seemore" id="seereloc">Relocation queue →</button>
        <button class="seemore" id="seeesc">Escalations →</button></div>
      <div class="card"><h2>Knowledge gaps<span class="sp"></span><span class="sub" id="gapsub"></span></h2>
        <div id="gapline" class="mut"></div>
        <button class="seemore" id="seegaps">See the gap report →</button></div>
      <div class="card"><h2>Recently rewritten<span class="sp"></span><span class="sub" id="recsub"></span></h2>
        <div id="reclist" class="mut"></div></div>
      <div class="card"><h2>On deck</h2><div id="upnext" class="mut"></div></div>
      <div class="card"><h2>Review notes<span class="sp"></span><span class="sub" id="notesub"></span></h2>
        <div id="noteslist" class="mut"></div>
        <button class="seemore" id="seenotes">Export my notes →</button></div>
      <div class="card"><h2>Activity<span class="sp"></span><span class="sub" id="feedsub"></span></h2>
        <div id="feed"></div></div>
    </aside>
  </main>
  <div class="notebox" id="notebox" hidden>
    <h3 id="nbtitle">Note on this passage</h3>
    <p class="quo" id="nbquote"></p>
    <div class="rate">
      <button class="up" id="nbup" aria-pressed="false">👍 Looks right</button>
      <button class="down" id="nbdown" aria-pressed="false">👎 Wrong / check</button>
    </div>
    <textarea id="nbtext" placeholder="What's wrong, or what should it say instead?"></textarea>
    <div class="nb-act">
      <button class="del" id="nbdel">Delete</button>
      <button id="nbcancel">Cancel</button>
      <button class="save" id="nbsave">Save</button>
    </div>
  </div>
</div>
<script id="snap" type="application/json">__SNAP__</script>
<script>
const D=JSON.parse(document.getElementById('snap').textContent);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byPath=new Map(D.files.map(f=>[f.path,f]));
const FC=D.folderColor, fol=p=>p.includes('/')?p.split('/')[0]:'.';
const col=p=>FC[fol(p)]||'#5E7076';
const REV=D.rev||{}, DIFFS=D.diffs||{};
const stClr={done:'var(--good)','fact-checked':'var(--accent)',transformed:'var(--accent)',
  escalated:'var(--critical)',reverted:'var(--critical)',skipped:'var(--muted)'};

/* theme */
const tb=document.getElementById('themebtn');
tb.onclick=()=>{const r=document.documentElement;
  const dark=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);
  r.setAttribute('data-theme',dark?'light':'dark'); tb.textContent=dark?'☾':'☀';
  if(typeof scheduleRender==='function')scheduleRender();};

/* header */
document.getElementById('introN').textContent=(D.totalUnits||0).toLocaleString();
document.getElementById('subline').textContent=
  `${D.processedUnits} of ${D.totalUnits} pages through the rewrite · model ${D.model}`;
document.getElementById('phasetext').textContent=`phase: ${D.phase}`;
document.getElementById('gen').textContent=D.generatedAt.replace('T',' ').replace('Z',' UTC');
if(D.stop)document.getElementById('stoppill').hidden=false;
const LIVE='https://camchuckpete-max.github.io/Socal-Fishing-Knowledge/';
const hosted=location.hostname.endsWith('github.io');
document.getElementById('refresh').onclick=()=>{
  if(hosted){location.reload();return;}
  const box=document.getElementById('stale');
  box.innerHTML=`This copy is a fixed snapshot, taken <strong>${esc(D.generatedAt.replace('T',' ').replace('Z',' UTC'))}</strong>. `+
    `The self-updating build rebuilds after every chunk and hourly: <a href="${LIVE}" target="_blank" rel="noopener">${LIVE}</a>`;
  box.hidden=!box.hidden;};
addEventListener('click',e=>{const b=document.getElementById('stale');
  if(b&&!b.hidden&&!e.target.closest('#stale')&&e.target.id!=='refresh')b.hidden=true;});
(function age(){
  const mins=Math.max(0,Math.round((Date.now()-Date.parse(D.generatedAt))/60000));
  const t=mins<2?'just now':mins<60?mins+' min old':
    mins<2880?Math.round(mins/60)+' h old':Math.round(mins/1440)+' days old';
  document.getElementById('age').textContent=t+' ·';
  setTimeout(age,60000);
})();
setInterval(()=>{document.getElementById('clock').textContent=
  new Date().toISOString().slice(11,19)+' UTC';},1000);
const cd=document.getElementById('chaindot'), ctx2=document.getElementById('chaintext');
const inflight=(D.runs||[]).some(r=>r.status!=='completed');
const pendN=D.counts.pending||0;
if(D.stop){cd.className='dot bad';ctx2.textContent='stopped';}
else if(inflight){cd.className='dot ok';ctx2.textContent='chunk in flight';}
else if(pendN>0){cd.className='dot wait';ctx2.textContent=`idle · ${pendN} queued`;}
else{cd.className='dot ok';ctx2.textContent='worklist clear';}
if(D.runs&&D.runs.length){
  const card=document.getElementById('chaincard');card.hidden=false;
  const cls=r=>r.status!=='completed'?'wait':(r.concl==='success'?'ok':
    (r.concl==='cancelled'?'':'bad'));
  const label=r=>r.status!=='completed'?r.status.replace('_',' ')
    :(r.concl==='cancelled'?'superseded in queue':r.concl);
  const bad=D.runs.filter(r=>r.concl&&r.concl!=='success'&&r.concl!=='cancelled').length;
  document.getElementById('chainsub').textContent=
    (bad?`${bad} failed · `:'')+
    (D.lastAgeMin!=null?`last commit ${D.lastAgeMin}m ago`:'no commits yet');
  document.getElementById('runs').innerHTML=D.runs.map(r=>
    `<div class="row"><span class="dot ${cls(r)}"></span><span class="txt">${esc(label(r))}</span>`+
    `<span class="when">${esc((r.when||'').slice(5,16).replace('T',' '))}</span></div>`).join('');
}

/* progress */
const C=D.counts;
const segs=[['done',C.done||0,'var(--good)'],['fact-checked',C['fact-checked']||0,'var(--accent)'],
  ['transformed',C.transformed||0,'color-mix(in srgb,var(--accent) 55%,transparent)'],
  ['escalated',(C.escalated||0)+(C.reverted||0),'var(--critical)'],
  ['skipped',C.skipped||0,'var(--muted)'],['pending',C.pending||0,'var(--pend)']];
document.getElementById('meter').innerHTML=segs.filter(s=>s[1])
  .map(([k,v,c])=>`<span style="flex:${v};background:${c}" title="${k}: ${v}"></span>`).join('');
document.getElementById('pcttext').textContent=
  (D.totalUnits?Math.round(D.processedUnits/D.totalUnits*100):0)+'%'+
  (D.etaH?` · ~${D.etaH}h left`:'')+` · ${D.rateH}/h`;
document.getElementById('tally').innerHTML=segs.filter(s=>s[1])
  .map(([k,v])=>`<span>${k} <b>${v.toLocaleString()}</b></span>`).join('');

/* conservation */
const consBad=D.consBad||[];
document.getElementById('conssub').textContent=consBad.length?`${consBad.length} LOST`:'all ✓';
document.getElementById('conslist').innerHTML=consBad.length
  ? consBad.map(p=>`<button class="vrow" data-p="${esc(p)}"><span class="vt"><span class="minus">✗</span> ${esc(p)}</span>`+
      `<span class="vm">cites missing from note + evidence — needs a human</span></button>`).join('')
  : 'Every processed page still carries all of its citations (checked against note + evidence file).';

/* adjudication */
const cats={};(D.ledger||[]).forEach(r=>{const c=r[2]||'?';cats[c]=(cats[c]||0)+1;});
document.getElementById('adjsub').textContent=
  `${(D.ledger||[]).length+D.relocPending+(D.escal||[]).length} open`;
document.getElementById('adjcats').innerHTML=
  Object.entries(cats).sort((a,b)=>b[1]-a[1]).map(([c,n])=>`<span class="badge">${esc(c)}: ${n}</span>`).join('')||'';
document.getElementById('gapsub').textContent=String((D.gaps.items||[]).length||'');
document.getElementById('gapline').textContent=D.gaps.totals||'No gaps flagged yet.';

/* recently rewritten + on deck */
const recents=(D.unitOrder||[]).slice(0,10);
document.getElementById('recsub').textContent=recents.length?`last ${recents.length}`:'';
document.getElementById('reclist').innerHTML=recents.length
  ? recents.map(p=>{const rv=REV[p]||{};const f=byPath.get(p);
      return `<button class="vrow" data-p="${esc(p)}"><span class="vt">${esc(f?f.title:p)}</span>`+
      `<span class="vm">${esc(p)} · ${esc(rv.status||'')}</span></button>`;}).join('')
  : 'Nothing rewritten yet — the fleet is warming up.';
const ondeck=(D.worklist||[]).filter(r=>r.s==='pending').slice(0,10);
document.getElementById('upnext').innerHTML=ondeck.length
  ? ondeck.map(r=>`<div class="row"><span class="vid">${esc(r.t)}</span><span class="txt">${esc(r.n)}</span></div>`).join('')
  : 'Worklist clear.';

/* activity */
document.getElementById('feedsub').textContent=`${(D.commits||[]).length} commits`;
document.getElementById('feed').innerHTML=(D.commits||[]).slice(0,16).map(c=>{
  const m=c.msg.match(/^review: (\S+\.md) /);
  const hit=m&&byPath.has(m[1]);
  return `<div class="row"${hit?` data-p="${esc(m[1])}" style="cursor:pointer"`:''}>`+
   `<span class="vid">${esc(c.sha)}</span><span class="txt">${esc(c.msg)}</span>
   <span class="when">${esc((c.when||'').slice(5,10))}</span></div>`;}).join('')
  ||'<span class="mut">No commits on this branch yet.</span>';

/* detail panel — markdown renderer (Bight Watch's, minus line attribution) */
function mdToHtml(src){
  const L=src.split('\n');let o=[],i=0;
  if(L[0]==='---'){i=1;while(i<L.length&&L[i]!=='---')i++;i++;}
  while(i<L.length&&!L[i].trim())i++;
  if(i<L.length&&/^#\s+/.test(L[i]))i++;
  // a cite token is a click away from its source video, like the pilot artifact
  const code=t=>/^[A-Za-z0-9_-]{11}$/.test(t)&&!/^[0-9]+$/.test(t)
    ?`<a href="https://www.youtube.com/watch?v=${t}" target="_blank" rel="noopener"><code>${t}</code></a>`
    :`<code>${t}</code>`;
  const inl=s=>esc(s).replace(/`([^`]+)`/g,(m,t)=>code(t))
    .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*\n]+)\*/g,'$1<em>$2</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,(m,t,h)=>h.includes('.md')
      ?`<a href="#" data-nav="${esc(h)}">${t}</a>`:`<a href="${esc(h)}" target="_blank" rel="noopener">${t}</a>`);
  while(i<L.length){const l=L[i];
    if(/^<!--/.test(l)){ // skip comment blocks (incl. the backlinks markers)
      while(i<L.length&&!/-->\s*$/.test(L[i]))i++;i++;continue;}
    if(/^\|/.test(l)){const b=[];while(i<L.length&&/^\|/.test(L[i]))b.push(L[i++]);
      const rs=b.filter(r=>!/^\|[\s:-]+\|/.test(r)).map(r=>r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim()));
      if(rs.length)o.push('<div class="tw"><table><thead><tr>'+rs[0].map(c=>`<th>${inl(c)}</th>`).join('')+
        '</tr></thead><tbody>'+rs.slice(1).map(r=>'<tr>'+r.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>').join('')+
        '</tbody></table></div>');continue;}
    let m;
    if((m=l.match(/^(#{1,6})\s+(.*)$/))){const d=Math.min(m[1].length,6);
      o.push(`<h${d}>${inl(m[2])}</h${d}>`);i++;continue;}
    if(/^>\s?/.test(l)){const b=[];while(i<L.length&&/^>\s?/.test(L[i]))b.push(L[i++].replace(/^>\s?/,''));
      o.push(`<blockquote>${inl(b.join(' '))}</blockquote>`);continue;}
    if(/^\s*[-*]\s+/.test(l)){const b=[];
      while(i<L.length){const mi=L[i].match(/^\s*[-*]\s+(.*)$/);
        if(mi){b.push(mi[1]);i++;continue;}
        if(b.length&&L[i].trim()&&/^\s{2,}\S/.test(L[i])&&!/^\s*[#>|]/.test(L[i])&&!/^\s*```/.test(L[i])){
          b[b.length-1]+=' '+L[i].trim();i++;continue;}
        break;}
      o.push('<ul>'+b.map(x=>`<li>${inl(x)}</li>`).join('')+'</ul>');
      continue;}
    if(/^```/.test(l)){i++;const b=[];while(i<L.length&&!/^```/.test(L[i]))b.push(L[i++]);
      if(i<L.length)i++;o.push(`<pre><code>${esc(b.join('\n'))}</code></pre>`);continue;}
    if(/^---+$/.test(l)){o.push('<hr>');i++;continue;}
    if(!l.trim()){i++;continue;}
    const b=[];while(i<L.length&&L[i].trim()&&!/^([#>|`]|\s*[-*]\s|<!--)/.test(L[i]))b.push(L[i++]);
    if(!b.length)b.push(L[i++]);
    o.push(`<p>${inl(b.join(' '))}</p>`);}
  return o.join('\n');
}

const det=document.getElementById('detail');
const body=document.getElementById('darticle'), dtabs=document.getElementById('dtabs'),
      dback=document.getElementById('dback'), dbacktext=document.getElementById('dbacktext');

function diffHunks(hunks,dropped){
  const h=hunks.map(k=>`<div class="hunk"><div class="at">${esc(k.at)}</div>`+
    k.lines.map(l=>{const c=l[0]==='+'?'add':l[0]==='-'?'del':'';
      return `<div class="dl ${c}">${esc(l.slice(1))}</div>`;}).join('')+`</div>`).join('');
  return h+(dropped?`<div class="dnote">${dropped.toLocaleString()} more changed lines not shown — the full diff is one click away on GitHub (commit link above).</div>`:'');
}

/* The panel is a stack. Back returns to wherever you came from. */
let back=null;
function show(o){
  if(typeof nb!=='undefined'&&nb)nb.hidden=true;
  document.getElementById('dtitle').textContent=o.title;
  document.getElementById('dpath').textContent=o.path||'';
  document.getElementById('dmeta').innerHTML=o.meta||'';
  dtabs.hidden=!o.tabs; dtabs.innerHTML=o.tabs||'';
  dback.hidden=!o.back; if(o.back)dbacktext.textContent=o.back.label;
  dback.onclick=o.back?o.back.go:null;
  body.innerHTML=o.html; body.scrollTop=0;
  det.classList.add('open');
}

/* one knowledgebase page: Article / Before / Changes / Evidence */
let curPath=null,curTab='article';
function open(path,tab,from){
  const f=byPath.get(path); if(!f)return;
  if(from!==undefined)back=from;
  curPath=path;
  const rv=REV[path], fm=f.fm||{}, d=DIFFS[path];
  const tags=[];
  if(rv){tags.push(`<span class="tag st-${esc(rv.status)}">${esc(rv.status)}</span>`);
    tags.push(`<span class="tag">${esc(rv.tier)} tier</span>`);}
  if(fm.type)tags.push(`<span class="tag">${esc(fm.type)}</span>`);
  if(fm.confidence)tags.push(`<span class="tag ${esc(fm.confidence)}">${esc(fm.confidence)}</span>`);
  (fm.regions||[]).forEach(r=>tags.push(`<span class="tag">${esc(r)}</span>`));
  if(fm.layout)tags.push(`<span class="tag">layout ${esc(fm.layout)}</span>`);
  if(rv&&rv.status!=='pending'){
    if(rv.bL)tags.push(`<span class="tag">${rv.bL} → ${rv.aL} lines</span>`);
    else if(f.status==='added')tags.push(`<span class="tag">new page · ${f.lines} lines</span>`);
    tags.push(rv.lost&&rv.lost.length
      ?`<span class="tag st-escalated">✗ ${rv.lost.length} cites lost</span>`
      :`<span class="tag st-done">✓ cites conserved</span>`);
  } else if(f.status!=='unchanged')
    tags.push(`<span class="tag">${esc(f.status)} on this branch</span>`);
  tags.push(`<span class="tag"><a href="${D.gh}/blob/${D.branch}/${esc(path)}" target="_blank" rel="noopener">GitHub ↗</a></span>`);
  if(rv&&rv.sha)tags.push(`<span class="tag"><a href="${D.gh}/commit/${esc(rv.sha)}" target="_blank" rel="noopener">commit ↗</a></span>`);

  const hasOld=!!f.old, ev=rv&&rv.evPath?byPath.get(rv.evPath):null;
  tab=tab||'article';
  if(tab==='before'&&!hasOld)tab='article';
  if(tab==='diff'&&!d&&f.status!=='added')tab='article';
  if(tab==='evidence'&&!ev)tab='article';
  curTab=tab;
  let tabs=`<button class="dtab" data-tab="article" aria-selected="${tab==='article'}">Article</button>`;
  if(hasOld)tabs+=`<button class="dtab" data-tab="before" aria-selected="${tab==='before'}">Before</button>`;
  if(d)tabs+=`<button class="dtab" data-tab="diff" aria-selected="${tab==='diff'}">Changes · +${d.add} −${d.rem}</button>`;
  else if(f.status==='added')tabs+=`<button class="dtab" data-tab="diff" aria-selected="${tab==='diff'}">Changes · new</button>`;
  if(ev)tabs+=`<button class="dtab" data-tab="evidence" aria-selected="${tab==='evidence'}">Evidence · ${rv.evN}</button>`;

  const revBar=`<div class="hbar"><span class="hsw"></span><span>Review mode — click any `+
    `${tab==='diff'?'line':'passage'} to rate it and leave a note.</span></div>`;
  let html;
  if(tab==='before'){
    html=`<div class="hbar"><span>As it stood before the review — base <code>${esc(D.baseSha)}</code>. Read-only; leave notes on the Article or Changes tab.</span></div>`+mdToHtml(f.old);
  } else if(tab==='diff'){
    html=revBar+(f.status==='added'
      ? `<div class="dnote" style="border:none">Written from scratch by the review — the whole article is the change. Rate passages on the Article tab.</div>`+mdToHtml(f.content)
      : `<details class="dfile" open><summary><span class="fp">${esc(path)}</span><span style="flex:1"></span>`+
        `<span class="plus">+${d.add}</span><span class="minus">−${d.rem}</span></summary>`+
        diffHunks(d.hunks,d.dropped)+`</details>`);
  } else if(tab==='evidence'){
    html=revBar+`<p class="mut" style="margin:0 0 10px">The observation layer behind the article — one line per sighting. Doctrine lives in the article; this is what it stands on.</p>`+mdToHtml(ev.content);
  } else {
    html=(rv&&rv.status!=='pending'?revBar:'')+
      (rv&&rv.result?`<p class="mut" style="margin:0 0 10px">Verifier: ${esc(rv.result)}${rv.flags?` · ${esc(rv.flags)}`:''}</p>`:'')+
      mdToHtml(f.content);
  }
  show({title:f.title,path:path,meta:tags.join(''),tabs:tabs,html:html,back:back});
  dtabs.querySelectorAll('.dtab').forEach(b=>b.onclick=()=>open(path,b.dataset.tab));
  body.querySelectorAll('a[data-nav]').forEach(a=>a.onclick=ev2=>{
    ev2.preventDefault();
    const raw=a.dataset.nav.split('#')[0], here=path.includes('/')?path.split('/').slice(0,-1):[];
    const st=[];here.concat(raw.split('/')).forEach(p=>p==='..'?st.pop():(p==='.'?0:st.push(p)));
    if(byPath.has(st.join('/')))open(st.join('/'),'article',{label:f.title,go:()=>open(path,tab)});});
  wireReview(path,tab,f,rv);
}

/* review wiring: which elements take notes on this tab */
function wireReview(path,tab,f,rv){
  body.classList.toggle('rev',tab!=='before');
  if(tab==='before')return;
  let els=[];
  if(tab==='diff'&&f.status!=='added'){
    els=[...body.querySelectorAll('.dl')];
  } else {
    els=[...body.querySelectorAll('.darticle > p,.darticle > h2,.darticle > h3,.darticle > h4,'+
      '.darticle > blockquote,.darticle > pre, .darticle li, .darticle .tw tbody tr')];
  }
  els.forEach(el=>{el.classList.add('sel');
    el.onclick=ev2=>{if(ev2.target.closest('a'))return;
      ev2.stopPropagation();openNote(el,path,tab);};});
  markNoted(path,tab);
}

/* ---- review notes — the reviewer's half of the surface -------------------
   Click a passage, rate it, say what is wrong. The deliverable is the
   markdown export handed back to Cameron/Claude; storage is only so a
   session is not lost to a reload. */
const NKEY='review-watch-notes-v1';
let NOTES={}, storageOK=true;
try{const raw=localStorage.getItem(NKEY); if(raw)NOTES=JSON.parse(raw);}
catch(e){storageOK=false;}
function saveNotes(){
  try{localStorage.setItem(NKEY,JSON.stringify(NOTES));}catch(e){storageOK=false;}
  paintNotes();
}
const noteKey=(path,tab,text)=>`${path}::${tab}::${(text||'').trim().slice(0,90)}`;
function paintNotes(){
  const all=Object.values(NOTES);
  document.getElementById('notesub').textContent=
    all.length?`${all.length} · ${all.filter(n=>n.rate==='down').length} flagged`:'none yet';
  document.getElementById('noteslist').innerHTML=all.length
    ? all.slice(-8).reverse().map(n=>
        `<button class="vrow" data-note="${esc(n.key)}"><span class="vt">`+
        `${n.rate==='down'?'<span class="minus">✗</span> ':n.rate==='up'?'<span class="plus">✓</span> ':''}`+
        `${esc((n.comment||'(no comment)').slice(0,64))}</span>`+
        `<span class="vm">${esc(n.path)} · ${esc(n.tab)}</span></button>`).join('')
    : 'Open a page, click a passage, and say what you think of it.';
  document.querySelectorAll('#noteslist [data-note]').forEach(b=>b.onclick=()=>{
    const n=NOTES[b.dataset.note]; if(n)open(n.path,n.tab==='diff'?'diff':n.tab==='evidence'?'evidence':'article',null);});
}
const nb=document.getElementById('notebox');
let nbKey=null;
function openNote(el,path,tab){
  const text=el.innerText.replace(/\s+/g,' ').trim();
  nbKey=noteKey(path,tab,text);
  const ex=NOTES[nbKey]||{};
  document.getElementById('nbquote').textContent='“'+text.slice(0,220)+(text.length>220?'…':'')+'”';
  document.getElementById('nbtext').value=ex.comment||'';
  document.getElementById('nbup').setAttribute('aria-pressed',String(ex.rate==='up'));
  document.getElementById('nbdown').setAttribute('aria-pressed',String(ex.rate==='down'));
  nb.dataset.nbpath=path; nb.dataset.nbtab=tab; nb.dataset.nbquote=text;
  const r=el.getBoundingClientRect();
  nb.hidden=false;
  const top=Math.min(Math.max(8,r.top),innerHeight-nb.offsetHeight-8);
  nb.style.top=top+'px';
  nb.style.left=Math.max(8,Math.min(r.left-420,innerWidth-nb.offsetWidth-8))+'px';
  document.getElementById('nbtext').focus();
}
document.getElementById('nbup').onclick=e=>{const b=e.currentTarget,on=b.getAttribute('aria-pressed')==='true';
  b.setAttribute('aria-pressed',String(!on));document.getElementById('nbdown').setAttribute('aria-pressed','false');};
document.getElementById('nbdown').onclick=e=>{const b=e.currentTarget,on=b.getAttribute('aria-pressed')==='true';
  b.setAttribute('aria-pressed',String(!on));document.getElementById('nbup').setAttribute('aria-pressed','false');};
document.getElementById('nbcancel').onclick=()=>{nb.hidden=true;};
document.getElementById('nbdel').onclick=()=>{delete NOTES[nbKey];saveNotes();nb.hidden=true;
  markNoted(nb.dataset.nbpath,nb.dataset.nbtab);};
document.getElementById('nbsave').onclick=()=>{
  const comment=document.getElementById('nbtext').value.trim();
  const rate=document.getElementById('nbup').getAttribute('aria-pressed')==='true'?'up'
    :document.getElementById('nbdown').getAttribute('aria-pressed')==='true'?'down':'';
  if(!comment&&!rate){delete NOTES[nbKey];}
  else NOTES[nbKey]={key:nbKey,path:nb.dataset.nbpath,tab:nb.dataset.nbtab,
    quote:nb.dataset.nbquote,comment:comment,rate:rate,at:new Date().toISOString()};
  saveNotes();nb.hidden=true;markNoted(nb.dataset.nbpath,nb.dataset.nbtab);};
addEventListener('keydown',e=>{if(e.key==='Escape'&&!nb.hidden){nb.hidden=true;e.stopPropagation();}});

function markNoted(path,tab){
  body.querySelectorAll('.sel').forEach(el=>{
    el.querySelectorAll('.flag').forEach(fl=>fl.remove());
    const text=el.innerText.replace(/\s+/g,' ').trim();
    const n=NOTES[noteKey(path,tab,text)];
    el.classList.toggle('noted',!!n);
    el.classList.toggle('up',!!n&&n.rate==='up');
    if(n&&n.rate&&!el.classList.contains('dl')){const fl=document.createElement('span');
      fl.className='flag'+(n.rate==='up'?' up':'');fl.textContent=n.rate==='up'?'✓ noted':'✗ flagged';
      el.prepend(fl);}});
}

/* the export — the thing that actually goes back to Cameron/Claude */
function exportNotes(){
  back=null;
  const all=Object.values(NOTES).sort((a,b)=>(a.path+a.tab).localeCompare(b.path+b.tab));
  let md=`# Review Watch feedback\n\nSnapshot ${D.generatedAt} · head ${D.headSha} · ${all.length} note`+
    `${all.length===1?'':'s'} · ${all.filter(n=>n.rate==='down').length} flagged wrong\n`;
  let cur='';
  all.forEach(n=>{
    if(n.path!==cur){cur=n.path;md+=`\n## ${n.path}\n`;}
    md+=`\n- **${n.rate==='down'?'WRONG':n.rate==='up'?'OK':'NOTE'}** · ${n.tab==='diff'?'in the diff':n.tab==='evidence'?'in the evidence file':'in the article'}\n`+
        `  - passage: "${n.quote.slice(0,300)}${n.quote.length>300?'…':''}"\n`+
        (n.comment?`  - cameron: ${n.comment}\n`:'');});
  if(!all.length)md+='\n(no notes yet)\n';
  show({title:'Review notes',path:`${all.length} to hand back`,
    html:(storageOK?'':`<div class="warn">This viewer blocked local storage, so notes live only until you close the tab. Copy them out before you go.</div>`)+
      `<p class="mut">Copy this block and paste it to Claude (or drop it in the repo) — it becomes the next feedback round, exactly like the pilot's.</p>`+
      `<div class="nb-act" style="justify-content:flex-start;margin:0 0 9px">`+
      `<button class="save" id="copyall">Copy all</button>`+
      `<button id="clearall" class="del">Clear notes</button>`+
      `<span class="mut" id="copied" style="align-self:center"></span></div>`+
      `<textarea class="expbox" id="expbox" spellcheck="false"></textarea>`});
  document.getElementById('expbox').value=md;
  document.getElementById('copyall').onclick=async()=>{
    const t=document.getElementById('expbox');t.select();
    let ok=false;
    try{await navigator.clipboard.writeText(t.value);ok=true;}
    catch(e){try{ok=document.execCommand('copy');}catch(e2){}}
    document.getElementById('copied').textContent=ok?'copied':'select the box and copy manually';};
  document.getElementById('clearall').onclick=()=>{
    if(!confirm('Delete all review notes? This cannot be undone.'))return;
    NOTES={};saveNotes();exportNotes();};
}
document.getElementById('seenotes').onclick=()=>exportNotes();
paintNotes();

/* list views */
function statusChip(s){return `<span class="${s==='escalated'||s==='reverted'?'minus':s==='pending'?'mut':'plus'}">${esc(s)}</span>`;}
function openProcessed(){
  back=null;
  const rows=(D.worklist||[]).filter(r=>r.s!=='pending'&&r.n.endsWith('.md'));
  const html=rows.map(r=>{const f=byPath.get(r.n),rv=REV[r.n]||{};
    return `<button class="vrow" data-open="${esc(r.n)}"><span class="vt">${esc(f?f.title:r.n)}</span>`+
      `<span class="vm">${esc(r.n)} · ${statusChip(r.s)}${rv.lost&&rv.lost.length?' · <span class="minus">✗ cites</span>':''}`+
      `${r.r?` · ${esc(r.r.slice(0,90))}`:''}</span></button>`;}).join('');
  show({title:'Processed pages',path:`${rows.length} through the rewrite`,
    html:`<input class="filt" id="pfilt" placeholder="Filter by title, path or status…"><div id="plist">${html||'<p class=mut>Nothing yet.</p>'}</div>`});
  wireList('pfilt','plist',{label:'Processed pages',go:openProcessed});
}
function openAll(){
  back=null;
  const groups=new Map();
  D.files.filter(f=>!f.path.endsWith('README.md')&&!f.path.includes('/evidence/')&&!f.path.startsWith('templates/'))
    .forEach(f=>{const k=fol(f.path);(groups.get(k)||groups.set(k,[]).get(k)).push(f);});
  const html=[...groups.entries()].sort((a,b)=>a[0].localeCompare(b[0])).map(([k,fs])=>
    `<div class="ghead">${esc(k)} · ${fs.length}</div>`+
    fs.sort((a,b)=>a.title.localeCompare(b.title)).map(f=>{const rv=REV[f.path];
      return `<button class="vrow" data-open="${esc(f.path)}"><span class="vt">${esc(f.title)}</span>`+
        `<span class="vm">${esc(f.path)}${rv?` · ${statusChip(rv.status)}`:''}</span></button>`;}).join('')).join('');
  show({title:'The knowledgebase',path:`${byPath.size} pages`,
    html:`<input class="filt" id="afilt" placeholder="Filter by title or path…"><div id="alist">${html}</div>`});
  wireList('afilt','alist',{label:'The knowledgebase',go:openAll});
}
function wireList(filtId,listId,home){
  const f=document.getElementById(filtId);
  if(f)f.oninput=()=>{const q=f.value.toLowerCase();
    document.querySelectorAll(`#${listId} .vrow`).forEach(b=>
      b.hidden=q&&!b.textContent.toLowerCase().includes(q));};
  document.querySelectorAll(`#${listId} [data-open]`).forEach(b=>
    b.onclick=()=>open(b.dataset.open,'article',home));
}
function openLedger(){
  back=null;
  const rows=(D.ledger||[]).map(r=>{const c=(r.concat(['','','','','']));
    return `<button class="vrow"${byPath.has(c[0])?` data-open="${esc(c[0])}"`:''}>`+
      `<span class="vt">${esc(c[1]||'(claim)')}</span>`+
      `<span class="vm">${esc(c[0])} · <span class="mut">${esc(c[2])}</span>${c[3]?` · ${esc(c[3])}`:''}${c[4]?` · ${esc(c[4].slice(0,110))}`:''}</span></button>`;}).join('');
  show({title:'Fact-check ledger',path:`${(D.ledger||[]).length} claims queued for your call`,
    html:`<p class="mut" style="margin:0 0 10px">Flags, never deletions: a single-source claim is not a wrong claim. Each row keeps its ⚠ flag in the article until you rule on it.</p>`+
      (rows||'<p class=mut>Ledger is empty.</p>')});
  document.querySelectorAll('#darticle [data-open]').forEach(b=>
    b.onclick=()=>open(b.dataset.open,'article',{label:'Fact-check ledger',go:openLedger}));
}
function openReloc(){
  back=null;
  const rows=(D.reloc||[]).map(r=>{const c=r.concat(['','','','','','']);
    return `<button class="vrow"${byPath.has(c[0])?` data-open="${esc(c[0])}"`:''}>`+
      `<span class="vt">${esc(c[2]||'(content)')}</span>`+
      `<span class="vm">${esc(c[0])} → ${esc(c[1])} · ${statusChip(c[5]||'pending')}${c[3]?` · ${esc(c[3].slice(0,90))}`:''}</span></button>`;}).join('');
  show({title:'Relocation queue',path:`${(D.reloc||[]).length} moves (${D.relocPending} pending)`,
    html:`<p class="mut" style="margin:0 0 10px">Misplaced content moves by a dedicated paired-conservation pass, never by an inline edit — this is that queue.</p>`+
      (rows||'<p class=mut>Queue is empty.</p>')});
  document.querySelectorAll('#darticle [data-open]').forEach(b=>
    b.onclick=()=>open(b.dataset.open,'article',{label:'Relocation queue',go:openReloc}));
}
function openEsc(){
  back=null;
  const rows=(D.escal||[]).map(e=>
    `<button class="vrow"${byPath.has(e.video)?` data-open="${esc(e.video)}"`:''}>`+
      `<span class="vt">${esc(e.kind||'escalation')}${e.thisBatch?' <span class="minus">· this run</span>':''}</span>`+
      `<span class="vm">${esc(e.video)} · ${esc((e.when||'').slice(0,16))}${e.why?` · ${esc(e.why.slice(0,110))}`:''}</span></button>`).join('');
  show({title:'Escalations',path:`${(D.escal||[]).length} needing a human call`,
    html:rows||'<p class="mut">None raised — nothing needs a human call yet.</p>'});
  document.querySelectorAll('#darticle [data-open]').forEach(b=>
    b.onclick=()=>open(b.dataset.open,'article',{label:'Escalations',go:openEsc}));
}
function openGaps(){
  back=null;
  const rows=(D.gaps.items||[]).map(g=>
    `<button class="vrow"${byPath.has(g.note)?` data-open="${esc(g.note)}"`:''}>`+
      `<span class="vt">${esc(g.note)}</span>`+
      `<span class="vm">${esc(g.lines.join(' · ').slice(0,160))}</span></button>`).join('');
  show({title:'Knowledge gaps',path:D.gaps.totals||'',
    html:`<p class="mut" style="margin:0 0 10px">Corpus-only rule: a gap is filled by finding a source, never by invention. These are the places the KB knows it is blind.</p>`+
      (rows||'<p class=mut>No gaps flagged yet.</p>')});
  document.querySelectorAll('#darticle [data-open]').forEach(b=>
    b.onclick=()=>open(b.dataset.open,'article',{label:'Knowledge gaps',go:openGaps}));
}
document.getElementById('seeprocessed').onclick=openProcessed;
document.getElementById('seeall').onclick=openAll;
document.getElementById('seeledger').onclick=openLedger;
document.getElementById('seereloc').onclick=openReloc;
document.getElementById('seeesc').onclick=openEsc;
document.getElementById('seegaps').onclick=openGaps;
document.getElementById('dclose').onclick=()=>{det.classList.remove('open');nb.hidden=true;};
addEventListener('keydown',e=>{if(e.key==='Escape')det.classList.remove('open');});
document.addEventListener('click',e=>{
  if(!e.target.closest('.rail'))return;
  const b=e.target.closest('[data-p]');
  if(b&&byPath.has(b.dataset.p))open(b.dataset.p,'article',null);});

/* intro */
const intro=document.getElementById('intro');
document.getElementById('introgo').onclick=()=>intro.hidden=true;
document.getElementById('helpbtn').onclick=()=>intro.hidden=false;
document.getElementById('introrandom').onclick=()=>{intro.hidden=true;
  const done=(D.unitOrder||[]).filter(p=>byPath.has(p));
  const pool=done.length?done:D.files.map(f=>f.path);
  open(pool[Math.floor(Math.random()*pool.length)],'article');};

/* ---- map view: the geographic ladder on real ground ----------------------
   The sonar shows how notes LINK; this shows where they ARE. It exists because
   a text census cannot show whether a carve-up is geographically sane — the
   Coronados sitting in `socal-bight`, or 9 Mile and 14 Mile Bank in one zone,
   are instantly obvious here and invisible in a list. */
const G=D.geo||{spots:[],zones:[]};
const ZONES=G.zones||[], PINS=G.spots||[];
const REGION_HUE={'socal-bight':205,'baja-pacific-north':28,
  'baja-pacific-south':340,'cortez-north':150,'cortez-south':270};
/* Hue by region so the coarse grouping reads at a glance; lightness varies per
   zone within a region so neighbouring zones stay distinguishable. */
function zoneColor(z){
  if(!z) return '#8b949e';
  const h=REGION_HUE[z.region]??0;
  const idx=ZONES.filter(o=>o.region===z.region).findIndex(o=>o.i===z.i);
  const l=38+((idx*37)%34);
  return `hsl(${h} 62% ${l}%)`;
}
const zoneOf=p=>p.z>=0?ZONES[p.z]:null;
let map=null,pinLayer=null,hullLayer=null,builtMap=false;
const BASE={};let baseName='ocean';
const shown={region:new Set(Object.keys(REGION_HUE)),hulls:true,farOnly:false};

function hull(pts){                    /* monotone chain, returns [[lat,lon]] */
  if(pts.length<3) return pts;
  const P=pts.map(p=>[p[1],p[0]]).sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
  const cross=(o,a,b)=>(a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]);
  const lo=[],up=[];
  for(const p of P){while(lo.length>=2&&cross(lo[lo.length-2],lo[lo.length-1],p)<=0)lo.pop();lo.push(p);}
  for(const p of P.slice().reverse()){while(up.length>=2&&cross(up[up.length-2],up[up.length-1],p)<=0)up.pop();up.push(p);}
  return lo.slice(0,-1).concat(up.slice(0,-1)).map(p=>[p[1],p[0]]);
}

function crumb(p){
  const box=document.getElementById('mcrumb');
  if(!p){box.hidden=true;return;}          // background click clears it
  const z=zoneOf(p);
  const jur=z?(z.jur==='us-waters'?'US waters':'Mexican waters'):'—';
  const path=`locations/${p.slug}.md`;
  const known=byPath.has(path);
  box.hidden=false;
  box.innerHTML=`<div class="line"><b>${esc(p.name)}</b>`+
    `<span class="sep">·</span>${p.lat.toFixed(3)}°N ${Math.abs(p.lon).toFixed(3)}°W`+
    (p.ar?`<span class="sep">·</span>in the <b>${esc(p.ar)}</b> coordinate table`:'')+
    (p.excluded?`<span class="sep">·</span><span class="far">excluded — not a fishing spot</span>`:'')+
    `<span class="op"><button class="linkbtn" id="mopen">`+
    `${known?'open page →':'what we know →'}</button></span></div>`+
    `<div class="line" style="margin-top:4px">${esc(jur)}<span class="sep">→</span>`+
    `${z?esc(z.region):'—'}<span class="sep">→</span>`+
    `<span class="mut">area: none yet</span><span class="sep">→</span>`+
    `${z?(byPath.has(`locations/${z.slug}.md`)
        ? `<button class="linkbtn" data-zonego="locations/${esc(z.slug)}.md">`+
          `<b>${esc(z.name)}</b></button>`
        : `<b>${esc(z.name)}</b>`)
       :'<span class="far">no zone</span>'}`+
    (z?`<span class="sep">·</span><span class="${p.far?'far':'mut'}">${p.d} nm from zone centre</span>`:'')+
    `</div>`;
  const b=document.getElementById('mopen');
  if(b)b.onclick=()=>openSpot(p);
  // the zone is one rung up and usually the more useful read; make the
  // breadcrumb take you there rather than just naming it
  const zb=box.querySelector('[data-zonego]');
  if(zb)zb.onclick=()=>open(zb.dataset.zonego,'article',null);
}

/* Pins overlap badly at low zoom: 281 of the 391 sit within 6px of another
   one at the default view, and the worst cluster stacks 23. Leaflet delivers
   the click to whichever marker it drew last, so clicking "Pukey Point"
   opened "North of North Island rockfish area" — the spot you asked for and
   the article you got were simply different places. Rather than guess, when a
   click lands on a pile, say so and let the reader pick. */
// A pin is drawn 4px across. Asking someone to hit that on a chart of the
// whole Bight is not a click target, it is a dexterity test — miss by 5px and
// the old code treated it as a background click and cleared the bar, which is
// what "nothing happens when I click a spot" actually was. Anything within
// HIT_PX of the click counts, nearest first.
const HIT_PX=14;
function pinsAt(pt){
  if(!map)return [];
  return PINS.map(q=>{
    const z=zoneOf(q); if(!q.excluded&&!vis(z))return null;
    const b=map.latLngToContainerPoint([q.lat,q.lon]);
    const d=Math.hypot(b.x-pt.x,b.y-pt.y);
    return d<=HIT_PX?{q,d}:null;
  }).filter(Boolean).sort((a,b)=>a.d-b.d).map(x=>x.q);
}

const CHOOSE_MAX=8;
function choose(all,zone){
  const box=document.getElementById('mcrumb');
  // Nearest first, capped: the Coronados put 15 spots inside one click radius
  // at region zoom, and a 15-row bar is a wall, not a choice.
  const list=all.slice(0,CHOOSE_MAX), more=all.length-list.length;
  box.hidden=false;
  const zpath=zone?`locations/${zone.slug}.md`:null;
  const zrow=zpath&&byPath.has(zpath)
    ?`<button class="pick" data-zone="1"><b>${esc(zone.name)}</b> — the whole zone`+
     `<span class="mut">zone article</span></button>`:'';
  box.innerHTML=`<div class="line"><b>${all.length} spots here</b>`+
    `<span class="sep">·</span><span class="mut">they overlap at this zoom —`+
    ` nearest first${more?`, showing ${CHOOSE_MAX}`:''}; zoom in to separate them`+
    `</span></div>`+
    zrow+
    list.map((q,i)=>{
      const has=byPath.has(`locations/${q.slug}.md`);
      return `<button class="pick" data-i="${i}">${esc(q.name)}`+
        `<span class="mut">${has?'article':'no page yet'}</span></button>`;
    }).join('')+
    (more?`<div class="line" style="margin-top:5px"><span class="mut">`+
          `+${more} more under the cursor — zoom in to reach them</span></div>`:'');
  box.querySelectorAll('.pick').forEach(btn=>{
    btn.onclick=()=>{
      if(btn.dataset.zone){open(zpath,'article',null);return;}
      const q=list[+btn.dataset.i];crumb(q);openSpot(q);};
  });
}

/* Clicking a pin answers two questions: what IS this, and what does the KB
   say about it. Spot pages land progressively — the minimum ones as each zone
   lands, the enrichable ones when the fleet reaches them — and "page not built
   yet" alone is a dead end, so an unbuilt spot still opens with its position,
   its place in the ladder, its queue status, and every corpus mention
   harvested for it. */
function openSpot(p){
  const path=`locations/${p.slug}.md`;
  if(p.slug&&byPath.has(path)){open(path,'article',null);return;}
  const z=zoneOf(p);
  const zpath=z?`locations/${z.slug}.md`:null;
  const zbuilt=zpath&&byPath.has(zpath);
  const jur=z?(z.jur==='us-waters'?'US waters':'Mexican waters'):'—';
  const jpath=z?`locations/${z.jur}.md`:null;
  const wl=(D.worklist||[]).find(r=>r.n===path);
  const hv=((D.geo&&D.geo.harvest)||{})[p.slug]||[];

  const tags=[`<span class="tag">${esc(p.lat.toFixed(4))}°N ${esc(Math.abs(p.lon).toFixed(4))}°W</span>`];
  if(z)tags.push(`<span class="tag">${esc(z.region)}</span>`);
  if(p.ar)tags.push(`<span class="tag">AR complex</span>`);
  if(p.excluded)tags.push(`<span class="tag st-escalated">not a fishing spot</span>`);
  else tags.push(`<span class="tag ${wl?'st-transformed':''}">${wl?esc(wl.s):'not queued yet'}</span>`);

  let html='';
  if(p.excluded){
    html+=`<p>Carried in the spot library but <strong>excluded from the
      gazetteer</strong>: this is a naval security zone, not a fishing spot. Its
      coordinates stay published in
      <a href="${D.gh}/blob/${D.branch}/sources/spot-lists.md" target="_blank" rel="noopener">the spot library</a>;
      no page is minted for it.</p>`;
  }else if(p.ar){
    html+=`<p>A numbered waypoint in the <strong>${esc(p.ar)}</strong> series.
      Numbered reef waypoints have no fishing identity apart from each other, so
      the series shares one page carrying a coordinate table of all of them —
      this position appears there. That page is
      <code>${esc(path)}</code>${byPath.has(path)?'':', not generated yet'}.</p>`;
  }else{
    html+=`<p><strong>This spot has no page yet.</strong> It is one of the
      ${(D.geo.spots||[]).length} charted spots that the geo phase will write,
      queued behind the gate. Everything the KB currently knows about it is
      below.</p>`;
  }

  html+=`<div class="ghead">Where it sits</div><ul>`+
    `<li>${esc(jur)}${jpath&&byPath.has(jpath)?` — <a href="#" data-go="${esc(jpath)}">page</a>`:' <span class="mut">(page pending)</span>'}</li>`+
    `<li>Region <code>${z?esc(z.region):'—'}</code> <span class="mut">(page pending)</span></li>`+
    `<li class="mut">Area — none yet; that rung is only built where the corpus earns it</li>`+
    `<li>Zone <strong>${z?esc(z.name):'none'}</strong>`+
      (zbuilt?` — <a href="#" data-go="${esc(zpath)}">page</a>`:' <span class="mut">(page pending)</span>')+
      (z?` · <span class="${p.far?'minus':'mut'}">${p.d} nm from zone centre${p.far?' — flagged for review':''}</span>`:'')+`</li>`+
    `</ul>`;

  if(hv.length){
    html+=`<div class="ghead">What the corpus says (${hv.length} mention${hv.length===1?'':'s'})</div>`+
      hv.map(h=>`<button class="vrow" data-go="${esc(h.note)}">`+
        `<span class="vt">${esc(h.claim||'(no claim recorded)')}</span>`+
        `<span class="vm">${esc(h.note)}${h.section?` · ${esc(h.section)}`:''}${h.cite?` · ${esc(h.cite)}`:''}</span>`+
        `</button>`).join('');
  }else if(!p.excluded){
    html+=`<div class="ghead">What the corpus says</div>`+
      `<p class="mut">Nothing harvested for this spot yet. Its page will be the
       minimum kind — coordinates, parent zone, and honest flagged gaps —
       until a source turns up. <a href="${D.gh}/blob/${D.branch}/locations/pukey-point.md" target="_blank" rel="noopener">Pukey Point</a>
       is the worked example.</p>`;
  }

  html+=`<div class="ghead">Position</div>`+
    `<p class="mut">${esc(p.lat.toFixed(4))}°N ${esc(Math.abs(p.lon).toFixed(4))}°W — charted, from
     <a href="${D.gh}/blob/${D.branch}/sources/spot-lists.md" target="_blank" rel="noopener">sources/spot-lists.md</a>.</p>`;

  // an excluded entry has no slug, so it has no path to show
  const label=p.excluded?'no page — excluded from the gazetteer'
    :path+(byPath.has(path)?'':' · not built yet');
  show({title:p.name,path:label,meta:tags.join(''),html:html});
  body.querySelectorAll('[data-go]').forEach(el=>el.onclick=ev=>{
    ev.preventDefault();
    if(byPath.has(el.dataset.go))open(el.dataset.go,'article',null);});
}

// Shared by paintMap and pinsAt: a pin the region filter has hidden must not
// turn up in the overlap chooser either.
function vis(z){return !!z&&shown.region.has(z.region);}

// Painted hulls, kept so a click in open water inside one can find its zone.
// The zone page is the level most people actually fish — "how does La Jolla
// fish" rather than "what is at South Kelp Ridge" — so it has to be reachable
// from the map, not only from a spot's breadcrumb (Cameron, 2026-08-26).
let HULLS=[];
function zoneAt(latlng){
  for(const h of HULLS){
    const b=h.poly.getBounds();
    if(b.contains(latlng)&&inPoly(latlng,h.ring))return h.z;
  }
  return null;
}
// ray casting over [lat,lng] pairs
function inPoly(ll,ring){
  let inside=false;
  for(let i=0,j=ring.length-1;i<ring.length;j=i++){
    const yi=ring[i][0],xi=ring[i][1],yj=ring[j][0],xj=ring[j][1];
    if(((yi>ll.lat)!==(yj>ll.lat))&&
       (ll.lng<(xj-xi)*(ll.lat-yi)/(yj-yi)+xi))inside=!inside;
  }
  return inside;
}

function paintMap(){
  if(!map)return;
  pinLayer.clearLayers(); hullLayer.clearLayers(); HULLS=[];
  if(shown.hulls){
    ZONES.forEach(z=>{
      if(!vis(z)||z.hull.length<2)return;
      const c=zoneColor(z);
      if(z.hull.length===2){
        L.polyline(z.hull,{color:c,weight:2,opacity:.5}).addTo(hullLayer);return;}
      const ring=hull(z.hull);
      const poly=L.polygon(ring,{color:c,weight:1.4,opacity:.65,fillColor:c,
        fillOpacity:.10}).addTo(hullLayer).bindTooltip(
          `${z.name} — ${z.n} spot${z.n===1?'':'s'} · click for the zone`,
          {sticky:true});
      HULLS.push({z,poly,ring});
    });
  }
  let n=0,built=0;
  PINS.forEach(p=>{
    const z=zoneOf(p);
    if(p.excluded){ if(!shown.region.has('socal-bight')&&!shown.region.has('baja-pacific-north'))return; }
    else if(!vis(z))return;
    if(shown.farOnly&&!p.far)return;
    n++;
    const c=p.excluded?'#8b949e':zoneColor(z);
    // A spot with a page reads SOLID, one without reads hollow. This is the
    // ladder filling in: at a glance you can see how much of the gazetteer
    // exists, without opening anything.
    const has=!p.excluded&&p.slug&&byPath.has(`locations/${p.slug}.md`);
    if(has)built++;
    const m=L.circleMarker([p.lat,p.lon],{
      radius:p.far?6:4,
      color:p.far?'#f85149':(has?'#e6edf3':c), weight:p.far?2.4:(has?1.6:1.2),
      fillColor:c, fillOpacity:p.excluded?.25:(has?.9:.28)});
    m.bindTooltip(`${p.name}${z?` — ${z.name}`:''}`+(has?'':' — no page yet'),
                  {direction:'top'});
    // No per-marker handler: the map-level one below owns every click, so
    // there is exactly one code path and nothing to race.
    m.addTo(pinLayer);
  });
  document.getElementById('mcount').textContent=
    `${n} of ${PINS.length} pinned · ${built} with pages`;
}

function buildPanel(){
  const counts={};
  PINS.forEach(p=>{const z=zoneOf(p);if(z)counts[z.region]=(counts[z.region]||0)+1;});
  const rows=Object.keys(REGION_HUE).map(r=>
    `<label class="mrow"><input type="checkbox" data-region="${r}" checked>`+
    `<span class="sw" style="background:hsl(${REGION_HUE[r]} 62% 48%)"></span>`+
    `${esc(r)}<span class="ct">${counts[r]||0}</span></label>`).join('');
  document.getElementById('mpanel').innerHTML=
    `<h4>Region</h4>${rows}`+
    `<h4>Basemap</h4>`+
    `<label class="mrow"><input type="radio" name="mbase" value="ocean" checked>`+
    `ocean <span class="mut">(bathymetry)</span></label>`+
    `<label class="mrow"><input type="radio" name="mbase" value="streets">`+
    `streets <span class="mut">(ports, coast)</span></label>`+
    `<h4>Layers</h4>`+
    `<label class="mrow"><input type="checkbox" id="mhulls" checked>zone hulls`+
    `<span class="ct">${ZONES.length}</span></label>`+
    `<label class="mrow"><input type="checkbox" id="mfar">needs review only`+
    `<span class="ct">${G.outliers||0}</span></label>`+
    `<h4>Pins</h4><div class="mut" id="mcount"></div>`+
    `<div class="mut" style="margin-top:8px;line-height:1.45">Colour = zone, `+
    `hue family = region. Red ring = further than ${G.maxDiam||12} nm from its `+
    `zone centre.</div>`;
  document.querySelectorAll('#mpanel [data-region]').forEach(cb=>cb.onchange=()=>{
    cb.checked?shown.region.add(cb.dataset.region):shown.region.delete(cb.dataset.region);
    paintMap();});
  document.querySelectorAll('#mpanel input[name="mbase"]').forEach(r=>r.onchange=()=>{
    if(!r.checked)return;
    if(BASE[baseName])map.removeLayer(BASE[baseName]);
    baseName=r.value; BASE[baseName].addTo(map);});
    // Pins and hulls need no re-stacking: Leaflet draws vectors in the overlay
    // pane, which always sits above the tile pane.
  document.getElementById('mhulls').onchange=e=>{shown.hulls=e.target.checked;paintMap();};
  document.getElementById('mfar').onchange=e=>{shown.farOnly=e.target.checked;paintMap();};
}

function initMap(){
  if(builtMap)return; builtMap=true;
  if(typeof L==='undefined'){
    document.getElementById('map').innerHTML=
      `<div class="mapfail"><div><strong>Map library missing.</strong><br>`+
      `Leaflet is vendored into the build (scripts/vendor/) and was not `+
      `inlined, so pins can't be drawn. Zone assignments are all in `+
      `<code>sources/geo-census.txt</code>.</div></div>`;
    return;
  }
  if(G.error){
    document.getElementById('map').innerHTML=
      `<div class="mapfail"><div><strong>Geo data unavailable.</strong><br>`+
      `${esc(G.error)}</div></div>`;
    return;
  }
  // Zoom control goes RIGHT: Leaflet's default top-left position sits on top
  // of the filter panel and swallows its clicks.
  // Zoom control goes RIGHT: Leaflet's default top-left position sits on top
  // of the filter panel and swallows its clicks.
  map=L.map('map',{zoomControl:false,attributionControl:true}).setView([32.6,-117.9],8);
  L.control.zoom({position:'topright'}).addTo(map);
  // Two basemaps, because most of these spots are offshore. Standard OSM is
  // near-empty out there — a tile over the banks is ~1.6 KB of blank water —
  // while the Esri ocean base carries BATHYMETRY, which is the thing that
  // explains why a high spot is a spot at all. Ocean is the default; streets
  // are there for ports, launches and the coastal zones.
  BASE.ocean=L.tileLayer(
    'https://services.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
    {maxZoom:13,attribution:'Esri, GEBCO, NOAA, National Geographic, and other contributors'});
  BASE.streets=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    {maxZoom:17,attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'});
  BASE.ocean.addTo(map);
  hullLayer=L.layerGroup().addTo(map);
  pinLayer=L.layerGroup().addTo(map);
  buildPanel(); paintMap();
  map.on('click',e=>{
    const here=pinsAt(e.containerPoint);
    const z=zoneAt(e.latlng);
    if(!here.length){
      // open water inside a hull is a click on the ZONE, not on nothing
      if(z&&byPath.has(`locations/${z.slug}.md`)){
        crumb(null);open(`locations/${z.slug}.md`,'article',null);return;}
      crumb(null);return;
    }
    // A lone pin opens its own spot whether or not a hull sits under it; the
    // zone stays one click away in the breadcrumb.
    if(here.length===1){crumb(here[0]);openSpot(here[0]);return;}
    choose(here,z);
  });
  if(PINS.length)map.fitBounds(L.latLngBounds(PINS.map(p=>[p.lat,p.lon])),{padding:[30,30]});
}

document.getElementById('viewtoggle').onclick=e=>{
  const b=e.target.closest('button[data-view]'); if(!b)return;
  const toMap=b.dataset.view==='map';
  document.querySelectorAll('#viewtoggle button').forEach(x=>
    x.setAttribute('aria-selected',String(x===b)));
  document.getElementById('graphwrap').classList.toggle('mapmode',toMap);
  document.getElementById('mapwrap').classList.toggle('on',toMap);
  if(toMap){initMap(); if(map)setTimeout(()=>map.invalidateSize(),0);}
};

/* sonar — layout arrives solved; the ring language changes meaning here:
   a halo = through the rewrite (good), critical halo = escalated, dim fill =
   still waiting its turn. Pings mark the latest commits, as ever. */
const cv=document.getElementById('graph'),cx=cv.getContext('2d');
const LAY=D.layout||{};
const nodes=D.files.filter(f=>!f.path.endsWith('README.md')&&LAY[f.path]).map(f=>{
  const [x,y,deg]=LAY[f.path];
  const rv=REV[f.path];
  return {p:f.path,t:f.title,c:col(f.path),recent:f.recent,deg:deg,x:x,y:y,
    rs:rv?rv.status:null};});
const ix=new Map(nodes.map((n,i)=>[n.p,i])),eds=[];
D.files.forEach(f=>(f.links||[]).forEach(l=>{
  if(ix.has(f.path)&&ix.has(l)&&f.path!==l)eds.push([ix.get(f.path),ix.get(l)]);}));
document.getElementById('gstat').textContent=`${nodes.length} pages · ${eds.length} links`;
const fols=[...new Set(nodes.map(n=>fol(n.p)))].sort();
document.getElementById('legend').innerHTML=
  fols.map(f=>`<span class="lg"><span class="sw" style="background:${FC[f]||'#5E7076'}"></span>${esc(f)}</span>`).join('')+
  `<span class="lg"><span class="swr"></span>rewritten</span>`+
  `<span class="lg"><span class="swr esc"></span>escalated</span>`+
  `<span class="lg"><span class="swr dim"></span>awaiting</span>`;
// The map has its own convention (solid = the spot has a page), stated where
// the map is rather than in the graph legend, which map mode hides.
document.getElementById('mlegend').innerHTML=
  `<span class="lg"><span class="sw" style="background:#58a6ff"></span>has a page</span>`+
  `<span class="lg"><span class="sw" style="background:#58a6ff;opacity:.28"></span>no page yet</span>`+
  `<span class="lg"><span class="swr esc"></span>far from zone centre</span>`;

let cam={x:0,y:0,z:1};
const bmp=document.createElement('canvas'),bcx=bmp.getContext('2d');
let baseKey='';
function cssVar(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim();}
function fit(){const r=cv.getBoundingClientRect(),d=devicePixelRatio||1;
  cv.width=Math.max(1,r.width*d);cv.height=Math.max(1,r.height*d);
  cx.setTransform(d,0,0,d,0,0);baseKey='';render();}
function drawBase(){
  const d=devicePixelRatio||1,w=cv.clientWidth,h=cv.clientHeight;
  bmp.width=cv.width;bmp.height=cv.height;
  bcx.setTransform(d,0,0,d,0,0);bcx.clearRect(0,0,w,h);
  bcx.save();bcx.translate(w/2+cam.x,h/2+cam.y);bcx.scale(cam.z,cam.z);
  bcx.strokeStyle=cssVar('--ring');bcx.globalAlpha=.20;bcx.lineWidth=1;bcx.beginPath();
  eds.forEach(([i,j])=>{bcx.moveTo(nodes[i].x,nodes[i].y);bcx.lineTo(nodes[j].x,nodes[j].y);});
  bcx.stroke();bcx.globalAlpha=1;
  const good=cssVar('--good'),crit=cssVar('--critical');
  nodes.forEach(n=>{const r=3+Math.min(n.deg,16)*.4;
    const processed=n.rs&&n.rs!=='pending';
    bcx.globalAlpha=(n.rs&&!processed)?.4:1;   // worklist rows not yet reached sit dim
    bcx.beginPath();bcx.arc(n.x,n.y,r,0,6.283);bcx.fillStyle=n.c;bcx.fill();
    bcx.globalAlpha=1;
    if(processed){
      bcx.strokeStyle=(n.rs==='escalated'||n.rs==='reverted')?crit:good;
      bcx.lineWidth=1.6;bcx.beginPath();bcx.arc(n.x,n.y,r+3.4,0,6.283);bcx.stroke();}});
  bcx.restore();
  baseKey=key();
}
const key=()=>`${cam.x}|${cam.y}|${cam.z}|${cv.width}|${cv.height}|${document.documentElement.dataset.theme||''}|${matchMedia('(prefers-color-scheme:dark)').matches}`;
const PING_FOR=7;
let started=0,anim=0;
const still=matchMedia('(prefers-reduced-motion:reduce)').matches;
function render(T){
  if(key()!==baseKey)drawBase();
  cx.setTransform(1,0,0,1,0,0);cx.clearRect(0,0,cv.width,cv.height);
  cx.drawImage(bmp,0,0);
  const d=devicePixelRatio||1,w=cv.clientWidth,h=cv.clientHeight;
  cx.setTransform(d,0,0,d,0,0);
  cx.save();cx.translate(w/2+cam.x,h/2+cam.y);cx.scale(cam.z,cam.z);
  nodes.forEach(n=>{if(n.recent<0)return;const r=3+Math.min(n.deg,16)*.4;
    if(T===undefined){
      cx.globalAlpha=.5;cx.strokeStyle=n.c;cx.lineWidth=1.2;
      cx.beginPath();cx.arc(n.x,n.y,r+6.5,0,6.283);cx.stroke();cx.globalAlpha=1;return;}
    const ph=(T*.7-n.recent*.12)%1.6;
    if(ph>0&&ph<1.4){cx.globalAlpha=(1-ph/1.4)*.55;cx.strokeStyle=n.c;cx.lineWidth=1.6;
      cx.beginPath();cx.arc(n.x,n.y,r+ph*26,0,6.283);cx.stroke();cx.globalAlpha=1;}});
  cx.restore();
}
function frame(now){
  if(!started)started=now;
  const T=(now-started)/1000;
  render(T);
  if(T<PING_FOR&&!document.hidden)anim=requestAnimationFrame(frame);
  else{anim=0;render();}
}
let queued=0;
function scheduleRender(){if(queued||anim)return;
  queued=requestAnimationFrame(()=>{queued=0;render();});}
function pingAgain(){if(still){render();return;}
  if(anim)cancelAnimationFrame(anim);started=0;anim=requestAnimationFrame(frame);}
addEventListener('resize',fit);
matchMedia('(prefers-color-scheme:dark)').addEventListener('change',()=>{baseKey='';render();});
fit();
pingAgain();
function pick(ev){const r=cv.getBoundingClientRect();
  const mx=(ev.clientX-r.left-r.width/2-cam.x)/cam.z,my=(ev.clientY-r.top-r.height/2-cam.y)/cam.z;
  let best=null,bd=1e9;nodes.forEach(n=>{const d=Math.hypot(n.x-mx,n.y-my);if(d<bd){bd=d;best=n;}});
  return bd<15?best:null;}
let drag=null;
cv.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,m:0};cv.classList.add('drag');});
addEventListener('pointerup',e=>{if(drag&&drag.m<4){const n=pick(e);if(n)open(n.p,'article',null);}
  drag=null;cv.classList.remove('drag');});
addEventListener('pointermove',e=>{
  if(drag){drag.m+=Math.abs(e.clientX-drag.x)+Math.abs(e.clientY-drag.y);
    cam.x+=e.clientX-drag.x;cam.y+=e.clientY-drag.y;drag.x=e.clientX;drag.y=e.clientY;
    scheduleRender();return;}
  const tip=document.getElementById('tip'),n=(e.target===cv)?pick(e):null;
  if(n){tip.style.display='block';tip.style.left=(e.clientX+12)+'px';tip.style.top=(e.clientY+12)+'px';
    tip.textContent=n.t+(n.rs&&n.rs!=='pending'?` · ${n.rs}`:'');}else tip.style.display='none';});
cv.addEventListener('wheel',e=>{e.preventDefault();
  cam.z=Math.max(.3,Math.min(3,cam.z*(e.deltaY<0?1.1:.9)));scheduleRender();},{passive:false});
</script>
"""


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
    snap = build(base, str(args.runs) if args.runs and args.runs.exists()
                 else None)
    payload = json.dumps(snap, ensure_ascii=False).replace(
        "</script>", "<\\/script>")
    out_html = HTML.replace("__SNAP__", payload)
    for token, path in (("__LEAFLET_CSS__", LEAFLET_CSS),
                        ("__LEAFLET_JS__", LEAFLET_JS)):
        try:
            asset = path.read_text(encoding="utf-8").replace(
                "</script>", "<\\/script>")
        except OSError:
            asset = ""          # map degrades to its own honest fallback
            print(f"WARNING: {path.name} missing — map will render its "
                  "'basemap unavailable' state", file=sys.stderr)
        out_html = out_html.replace(token, asset)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(out_html, encoding="utf-8")
    print(f"review-watch -> {args.out}  ({len(out_html)/1_000_000:.2f} MB)")
    print(f"  pages {len(snap['files'])} | processed {snap['processedUnits']}"
          f"/{snap['totalUnits']} | phase {snap['phase']}"
          f" | cite-loss {len(snap['consBad'])}")
    print(f"  ledger {len(snap['ledger'])} | reloc {len(snap['reloc'])}"
          f" | escalations {len(snap['escal'])} | runs {len(snap['runs'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
