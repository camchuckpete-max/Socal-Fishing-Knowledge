#!/usr/bin/env python3
"""Build Bight Watch for batch 3 — the shareable accuracy-review screen.

Successor to the batch-2 Bight Watch. Same idea: the knowledgebase drawn as a
sonar screen, every mark a page, recently-touched marks pinging, so someone who
knows the fishery can wander in and catch a wrong depth or season. Data
collection is reused from build_vault.py; only the presentation differs.

    python scripts/build-bight-watch.py        # -> sources/bight-watch.html

Static snapshot — re-run to refresh while the ingestion chain works.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
# build-vault.py isn't a valid module name; load it by path instead.
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "build_vault", Path(__file__).resolve().parent / "build-vault.py")
_bv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bv)

ROOT = _bv.ROOT

# Folder → hue. Colours carry meaning here: a reviewer scanning the sonar
# should be able to tell a species page from a rig page without reading.
FOLDER_COLOR = {
    "species": "#3987e5", "techniques": "#d95926", "lures": "#199e70",
    "rigging": "#16a34a", "tackle": "#0d9488", "conditions": "#c98500",
    "seasonal": "#b45309", "locations": "#d55181", "planning": "#9085e9",
    "bait": "#65a30d", "fish-care": "#e05252", "profiles": "#5E7076",
    "sources": "#5E7076", "skills": "#5E7076",
}


# ---------------------------------------------------------------------------
# Diffs. Two views of the same history:
#   * per-note  — cumulative change vs the base, answering "what did this run
#                 do to this page?"
#   * per-video — one extraction commit, answering "what did this video teach
#                 the knowledgebase?"
# Added files carry no diff: the whole page is the change, and the rendered
# article already shows it.

DIFF_LINE_CAP = 600  # per note and per video; overflow is reported, not hidden

_SKIP_HEADERS = ("index ", "--- ", "+++ ", "new file", "deleted file",
                 "similarity ", "rename ", "old mode", "new mode")


def _parse_diff(raw: str, cap: int = DIFF_LINE_CAP):
    """git diff text -> ([{path, hunks:[{at, lines}]}], lines omitted)."""
    files, cur, hunk, used, dropped = [], None, None, 0, 0
    for line in raw.splitlines():
        if line.startswith("diff --git "):
            cur = {"path": line.split(" b/")[-1], "hunks": []}
            files.append(cur)
            hunk = None
            continue
        if cur is None or line.startswith(_SKIP_HEADERS):
            continue
        if line.startswith("@@"):
            hunk = {"at": line.split("@@")[1].strip(), "lines": []}
            cur["hunks"].append(hunk)
            continue
        if hunk is None:
            continue
        if used >= cap:
            dropped += 1
            continue
        hunk["lines"].append(line or " ")
        used += 1
    for f in files:
        f["hunks"] = [h for h in f["hunks"] if h["lines"]]
    return [f for f in files if f["hunks"]], dropped


def _counts(files: list) -> tuple[int, int]:
    lines = [l for f in files for h in f["hunks"] for l in h["lines"]]
    return (sum(1 for l in lines if l[:1] == "+"),
            sum(1 for l in lines if l[:1] == "-"))


def collect_note_diffs(base: str, files: list[dict]) -> dict:
    """Cumulative diff vs the base for every note this run modified."""
    out = {}
    for f in files:
        if f["status"] != "modified":
            continue
        parsed, dropped = _parse_diff(
            _bv.git("diff", "--unified=2", f"{base}...HEAD", "--", f["path"]))
        if not parsed:
            continue
        add, rem = _counts(parsed)
        out[f["path"]] = {"hunks": parsed[0]["hunks"], "add": add, "rem": rem,
                          "dropped": dropped}
    return out


VIDEO_COMMIT = re.compile(r"^batch\d+: (\S+) ")


def collect_video_diffs(base: str, worklist: list[dict], titles: dict,
                        keep: int = 200):
    """One entry per video whose extraction commit lives on this branch."""
    log = _bv.git("log", f"{base}..HEAD", "--date=iso-strict",
                  "--pretty=format:%h\x1f%ad\x1f%s")
    by_video = {}
    for line in log.splitlines():
        parts = line.split("\x1f")
        if len(parts) >= 3:
            m = VIDEO_COMMIT.match(parts[2])
            if m:
                by_video.setdefault(m.group(1), (parts[0], parts[1], parts[2]))

    meta = {r["video"]: r for r in worklist}
    order = [r["video"] for r in worklist if r["video"] in by_video][::-1]
    skipped = max(0, len(order) - keep)

    vids = []
    for vid in order[:keep]:
        sha, when, subject = by_video[vid]
        parsed, dropped = _parse_diff(
            _bv.git("show", sha, "--format=", "--unified=2", "--", "*.md",
                    ":(exclude)sources/transcripts"))
        add, rem = _counts(parsed)
        row = meta.get(vid, {})
        vids.append({"v": vid, "sha": sha, "when": when, "msg": subject,
                     "ch": row.get("channel", ""), "cls": row.get("cls", ""),
                     "depth": row.get("depth", ""), "result": row.get("result", ""),
                     "title": titles.get(vid, ""), "files": parsed,
                     "add": add, "rem": rem, "dropped": dropped})
    return vids, skipped


def collect_attribution(base: str, files: list[dict]) -> dict:
    """Which video wrote each line of each note, as it stands right now.

    A diff hunk shows fragments; this shows the live article with one video's
    sentences lit up inside it, which is the thing worth reviewing — a claim
    is only judgeable in the context it sits in.

    git blame does the work, so a line a later video rewrote belongs to that
    later video, not to whoever typed it first. Lines predating the batch
    blame to old commits and simply go unattributed.
    """
    sha_to_video = {}
    log = _bv.git("log", f"{base}..HEAD", "--pretty=format:%H\x1f%h\x1f%s")
    for line in log.splitlines():
        parts = line.split("\x1f")
        if len(parts) >= 3:
            m = VIDEO_COMMIT.match(parts[2])
            if m:
                sha_to_video[parts[0]] = m.group(1)
    if not sha_to_video:
        return {}

    hdr = re.compile(r"^([0-9a-f]{40}) \d+ (\d+)")
    out: dict[str, list] = {}
    for f in files:
        if f["status"] == "unchanged":
            continue
        blame = _bv.git("blame", "--porcelain", "--", f["path"])
        if not blame:
            continue
        # line number (0-based, matching the content we ship) -> video
        marks: dict[int, str] = {}
        for line in blame.splitlines():
            m = hdr.match(line)
            if not m:
                continue
            vid = sha_to_video.get(m.group(1))
            if vid:
                marks[int(m.group(2)) - 1] = vid
        if not marks:
            continue
        # collapse to runs so the payload stays small
        runs: list[list] = []
        for ln in sorted(marks):
            vid = marks[ln]
            if runs and runs[-1][2] == vid and runs[-1][0] + runs[-1][1] == ln:
                runs[-1][1] += 1
            else:
                runs.append([ln, 1, vid])
        out[f["path"]] = runs
    return out


def load_titles() -> dict:
    """Video titles, from every landed manifest."""
    titles: dict[str, str] = {}
    for man in ROOT.glob("sources/transcripts/**/_manifest.csv"):
        try:
            with man.open(encoding="utf-8", newline="") as fh:
                for row in csv.DictReader(fh):
                    vid = (row.get("video_id") or "").strip()
                    if vid and row.get("title"):
                        titles.setdefault(vid, row["title"].strip())
        except OSError:
            continue
    return titles


def build(base: str) -> dict:
    snap = _bv.build_snapshot(base)
    # Which notes did the most recent commits touch? Those ping on the sonar.
    recent: dict[str, int] = {}
    for i, c in enumerate(snap["commits"][:14]):
        for f in c["files"]:
            recent.setdefault(f["path"], i)
    for f in snap["files"]:
        f["recent"] = recent.get(f["path"], -1)
    wl = snap["worklist"]
    snap["done"] = [r for r in wl if r["status"] == "done"][-40:][::-1]
    snap["ondeck"] = [r for r in wl if r["status"] == "pending"][:14]
    snap["folderColor"] = FOLDER_COLOR
    snap["runs"] = []
    snap["diffs"] = collect_note_diffs(base, snap["files"])
    snap["videos"], snap["videosOmitted"] = collect_video_diffs(
        base, wl, load_titles())
    snap["attrib"] = collect_attribution(base, snap["files"])
    # Each video learns which live notes still carry its writing, so the
    # video view can open the article rather than only a hunk.
    wrote: dict[str, dict] = {}
    for path, runs in snap["attrib"].items():
        for start, count, vid in runs:
            e = wrote.setdefault(vid, {}).setdefault(path, 0)
            wrote[vid][path] = e + count
    for v in snap["videos"]:
        v["wrote"] = sorted(wrote.get(v["v"], {}).items(),
                            key=lambda kv: -kv[1])
    return snap


def load_runs(path: str) -> list[dict]:
    """Recent ingest-chunk runs, from a saved GitHub list_workflow_runs payload.

    Read from a file rather than fetched, so the generator stays offline and
    the page stays a snapshot of a known moment."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    runs = raw.get("workflow_runs", raw if isinstance(raw, list) else [])
    return [{"id": str(r["id"]), "status": r.get("status", ""),
             "concl": r.get("conclusion") or "", "when": r.get("created_at", "")}
            for r in runs[:10]]


HTML = r"""<title>Bight Watch</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Sonar screen. Light is the default state; dark is where it belongs and is
   what the toggle and a dark OS both resolve to. Every colour is a token so a
   theme never half-applies. */
:root{
  --bg:#f2f5f5; --panel:#ffffff; --panel2:#e8eeee; --ink:#132227; --ink2:#3f5359;
  --muted:#697f85; --hair:rgba(19,34,39,.14);
  --accent:#0f7d8a; --accent-ink:#0b626d;
  --good:#177a2f; --serious:#b2531f; --critical:#b03030; --pend:#c3cfd1;
  --ring:rgba(19,34,39,.28);
  --shadow:0 1px 2px rgba(0,0,0,.06),0 6px 20px rgba(0,0,0,.07);
  --vig:rgba(210,222,222,.5);
  --display:"Barlow Condensed",system-ui,sans-serif;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  color-scheme:light;
}
:root:not([data-theme="light"]){ }
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#0B1517; --panel:#122025; --panel2:#16262C; --ink:#D9E4E6; --ink2:#9FB2B7;
    --muted:#6E8288; --hair:rgba(217,228,230,.13);
    --accent:#3FB4C1; --accent-ink:#63C5D0;
    --good:#21b421; --serious:#ec835a; --critical:#e05252; --pend:#33454B;
    --ring:rgba(99,197,208,.34);
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
  --ring:rgba(99,197,208,.34);
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
.intro{position:fixed;inset:0;z-index:50;background:var(--vig);backdrop-filter:blur(7px);
  display:grid;place-items:center;padding:20px}
.intro[hidden]{display:none}
.intro-card{background:var(--panel);border:1px solid var(--hair);border-radius:16px;
  box-shadow:var(--shadow);max-width:620px;padding:26px 28px}
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
.dot{width:8px;height:8px;border-radius:50%;background:var(--muted);flex:none}
.dot.ok{background:var(--good)}.dot.wait{background:var(--serious)}
.clockbox{text-align:right}
.clock{font-family:var(--mono);font-size:13px;color:var(--ink2);font-variant-numeric:tabular-nums}
.stamp{font-size:10.5px;color:var(--muted)}
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
  max-width:210px;display:flex;flex-wrap:wrap;gap:4px 12px}
.legend .lg{display:flex;align-items:center;gap:6px}
.legend .sw{width:9px;height:9px;border-radius:50%}
.tip{position:absolute;pointer-events:none;background:var(--panel);border:1px solid var(--hair);
  border-radius:8px;padding:5px 9px;font-size:12px;box-shadow:var(--shadow);display:none;z-index:5}
.gstat{position:absolute;right:14px;top:12px;font-family:var(--mono);font-size:11px;color:var(--muted);
  text-align:right;font-variant-numeric:tabular-nums}

/* detail slide-over */
.detail{position:absolute;top:0;right:0;bottom:0;width:min(560px,92%);background:var(--panel);
  border-left:1px solid var(--hair);box-shadow:var(--shadow);transform:translateX(101%);
  transition:transform .22s ease;display:flex;flex-direction:column;z-index:20}
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

/* panel navigation — the slide-over is a stack: list -> video -> page */
.dback{background:none;border:none;color:var(--accent-ink);font-size:12px;padding:0 0 4px;
  font-weight:600}
.dtabs{display:flex;gap:6px;margin-top:10px}
.dtab{background:var(--panel2);border:1px solid var(--hair);color:var(--ink2);border-radius:8px;
  padding:4px 11px;font-size:12px;font-weight:600}
.dtab[aria-selected="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
.seemore{display:block;width:100%;margin-top:9px;background:var(--panel2);border:1px solid var(--hair);
  border-radius:8px;padding:6px 9px;font-size:12px;font-weight:600;color:var(--accent-ink);
  text-align:left}
.seemore:hover{border-color:var(--accent)}

/* in-place attribution — reading the live article with one video's writing
   lit up. The unhighlighted text dims rather than disappearing, so a claim
   is still judged in the context it sits in. */
.hbar{position:sticky;top:0;z-index:5;display:flex;gap:9px;align-items:center;flex-wrap:wrap;
  background:var(--panel);border:1px solid var(--hair);border-radius:10px;
  padding:7px 11px;margin:0 0 14px;font-size:12px;color:var(--ink2)}
.hsw{width:11px;height:11px;border-radius:3px;flex:none;
  background:color-mix(in srgb,var(--accent) 28%,transparent);
  border:1px solid color-mix(in srgb,var(--accent) 60%,transparent)}
.hnav{display:inline-flex;align-items:center;gap:5px}
.hnav button{background:var(--panel2);border:1px solid var(--hair);color:var(--ink2);
  border-radius:6px;width:23px;height:23px;font-size:12px;line-height:1}
.hnav button:hover{border-color:var(--accent);color:var(--accent-ink)}
#hcount{font-size:10.5px;color:var(--muted);min-width:34px;text-align:center}
.darticle.focus > :not(.hbar):not(.mine){opacity:.42}
.darticle.focus .mine,.darticle.focus li.mine{opacity:1}
/* the jump target must clear the sticky attribution bar */
.darticle .mine{scroll-margin-top:58px;background:color-mix(in srgb,var(--accent) 13%,transparent);
  box-shadow:-10px 0 0 color-mix(in srgb,var(--accent) 13%,transparent),
             10px 0 0 color-mix(in srgb,var(--accent) 13%,transparent);
  border-radius:2px}
.darticle .mine.at{background:color-mix(in srgb,var(--accent) 26%,transparent);
  box-shadow:-10px 0 0 color-mix(in srgb,var(--accent) 26%,transparent),
             10px 0 0 color-mix(in srgb,var(--accent) 26%,transparent)}
.darticle.focus ul:has(.mine){opacity:1}
.darticle.focus ul:has(.mine) li:not(.mine){opacity:.42}

/* diffs — the point of the whole screen: what actually changed */
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
  .detail{position:fixed;z-index:60}
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
.nlink{display:block;width:100%;text-align:left;background:none;border:none;padding:3px 0;
  font-size:12.5px;color:var(--ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nlink:hover{color:var(--accent-ink)}
.nlink .nf{font-family:var(--mono);font-size:10.5px;color:var(--muted)}
.mut{color:var(--muted);font-size:12px}
::-webkit-scrollbar{width:9px;height:9px}
::-webkit-scrollbar-thumb{background:var(--pend);border-radius:6px}
</style>

<div class="intro" id="intro">
  <div class="intro-card">
    <h2 class="display">Bight Watch</h2>
    <p class="lead">Claude is reading <strong id="introN">—</strong> SoCal &amp; Baja fishing videos —
    seminars, tackle breakdowns, on-the-water lessons — and merging what they teach into Cameron's
    fishing knowledgebase. This screen is the watch on that process.</p>
    <ul>
      <li><span class="k1">The sonar screen</span> is the knowledgebase — every mark is a page,
      coloured by topic. Marks with pinging rings were just written. Tap one to read the page.</li>
      <li><span class="k1">The rail</span> tracks the run: how far along, what landed, what's on deck.</li>
      <li><span class="k1">Your job</span>: you know this fishery. If a depth, a season, a rig or a
      claim reads wrong — screenshot it and tell Cameron. That's the whole gig. 🎣</li>
    </ul>
    <button class="go" id="introgo">Start watching</button>
    <button class="go alt" id="introrandom">🎲 Take me to a random new page</button>
  </div>
</div>

<div class="app">
  <header class="bar">
    <div class="brand">
      <h1 class="display">Bight Watch</h1>
      <div class="sub" id="subline"></div>
    </div>
    <span class="pill" id="chainpill"><span class="dot" id="chaindot"></span><span id="chaintext">chain</span></span>
    <div class="spacer"></div>
    <div class="clockbox">
      <div class="clock" id="clock">--:--:-- UTC</div>
      <div class="stamp">snapshot <span class="mono" id="gen"></span> · <span id="age"></span>
        <button class="linkbtn" id="refresh" title="Reload — on the live build this pulls the newest snapshot">refresh</button></div>
    </div>
    <button class="help" id="themebtn" aria-label="Toggle day / night mode">☾</button>
    <button class="help" id="helpbtn" aria-label="What am I looking at?">?</button>
  </header>
  <main>
    <div id="graphwrap">
      <canvas id="graph" aria-label="Knowledgebase link graph"></canvas>
      <div class="gstat" id="gstat"></div>
      <div class="legend" id="legend"></div>
      <div class="tip" id="tip"></div>
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
        <h2>Extraction progress<span class="sp"></span><span class="sub" id="pcttext"></span></h2>
        <div class="meter" id="meter"></div>
        <div class="tally" id="tally"></div>
        <button class="seemore" id="seevideos">See the videos we've read →</button>
      </div>
      <div class="card" id="chaincard" hidden><h2>Chain<span class="sp"></span><span class="sub" id="chainsub"></span></h2>
        <div id="runs"></div></div>
      <div class="card"><h2>Pages written<span class="sp"></span><span class="sub" id="newsub"></span></h2>
        <div id="newlist" class="mut"></div>
        <button class="seemore" id="seepages">See every page this run touched →</button></div>
      <div class="card"><h2>Logged videos<span class="sp"></span><span class="sub" id="donesub"></span></h2>
        <div id="donelist" class="mut"></div>
        <button class="seemore" id="seevideos2">See all read videos →</button></div>
      <div class="card"><h2>On deck</h2><div id="upnext" class="mut"></div></div>
      <div class="card"><h2>Activity<span class="sp"></span><span class="sub" id="feedsub"></span></h2>
        <div id="feed"></div></div>
      <div class="card"><h2>Escalations<span class="sp"></span><span class="sub" id="escsub"></span></h2>
        <div id="escs" class="mut"></div></div>
    </aside>
  </main>
</div>
<script id="snap" type="application/json">__SNAP__</script>
<script>
const D=JSON.parse(document.getElementById('snap').textContent);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byPath=new Map(D.files.map(f=>[f.path,f]));
const FC=D.folderColor, fol=p=>p.includes('/')?p.split('/')[0]:'.';
const col=p=>FC[fol(p)]||'#5E7076';

/* theme */
const tb=document.getElementById('themebtn');
tb.onclick=()=>{const r=document.documentElement;
  const dark=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);
  r.setAttribute('data-theme',dark?'light':'dark'); tb.textContent=dark?'☾':'☀';};

/* header */
const done=D.counts.done||0, pend=D.counts.pending||0, skip=D.counts.skipped||0;
const totalVid=D.worklist.length;
document.getElementById('introN').textContent=totalVid.toLocaleString();
document.getElementById('subline').textContent=
  `${done.toLocaleString()} of ${totalVid.toLocaleString()} videos read into the knowledgebase`;
document.getElementById('gen').textContent=D.generatedAt.replace('T',' ').replace('Z',' UTC');
/* Say how stale this snapshot is rather than claiming it is live. The hosted
   build refreshes itself hourly, so a reload really does pull newer data
   there; in a static copy the reload is honest about changing nothing. */
document.getElementById('refresh').onclick=()=>location.reload();
(function age(){
  const mins=Math.max(0,Math.round((Date.now()-Date.parse(D.generatedAt))/60000));
  const t=mins<2?'just now':mins<60?mins+' min old':
    mins<2880?Math.round(mins/60)+' h old':Math.round(mins/1440)+' days old';
  document.getElementById('age').textContent=t+' ·';
  setTimeout(age,60000);
})();
const cd=document.getElementById('chaindot'), ct=document.getElementById('chaintext');
if(pend>0){cd.className='dot wait';ct.textContent=`${pend.toLocaleString()} queued`;}
else{cd.className='dot ok';ct.textContent='worklist clear';}
/* chain — the ingestion runs behind the numbers above */
if(D.runs&&D.runs.length){
  const card=document.getElementById('chaincard');card.hidden=false;
  const cls=r=>r.status!=='completed'?'wait':(r.concl==='success'?'ok':'');
  const label=r=>r.status!=='completed'?r.status.replace('_',' '):r.concl;
  document.getElementById('chainsub').textContent=
    D.runs.filter(r=>r.concl==='success').length+' of '+D.runs.length+' clean';
  document.getElementById('runs').innerHTML=D.runs.map(r=>
    `<div class="row"><span class="dot ${cls(r)}"></span><span class="txt">${esc(label(r))}</span>`+
    `<span class="when">${esc((r.when||'').slice(5,16).replace('T',' '))}</span></div>`).join('');
}
setInterval(()=>{document.getElementById('clock').textContent=
  new Date().toISOString().slice(11,19)+' UTC';},1000);

/* progress */
const segs=[['done',done,'var(--good)'],['skipped',skip,'var(--muted)'],['pending',pend,'var(--pend)']];
document.getElementById('meter').innerHTML=segs.filter(s=>s[1])
  .map(([k,v,c])=>`<span style="flex:${v};background:${c}" title="${k}: ${v}"></span>`).join('');
document.getElementById('pcttext').textContent=Math.round(done/totalVid*100)+'%';
document.getElementById('tally').innerHTML=segs.filter(s=>s[1])
  .map(([k,v])=>`<span>${k} <b>${v.toLocaleString()}</b></span>`).join('');

/* rail lists */
const newNotes=D.files.filter(f=>f.status==='added');
document.getElementById('newsub').textContent=`${newNotes.length} new · ${D.files.filter(f=>f.status==='modified').length} updated`;
document.getElementById('newlist').innerHTML=newNotes.length
  ? newNotes.map(f=>`<button class="nlink" data-p="${esc(f.path)}"><span class="nf">${esc(fol(f.path))}/</span> ${esc(f.title)}</button>`).join('')
  : 'None yet.';
document.getElementById('donesub').textContent=`${done} read`;
document.getElementById('donelist').innerHTML=D.done.length
  ? D.done.slice(0,18).map(r=>`<div class="row" data-vid="${esc(r.video)}"
      ${(D.videos||[]).some(v=>v.v===r.video)?'style="cursor:pointer"':''}><span class="vid">${esc(r.video)}</span>
      <span class="txt">${esc(r.result||r.cls)}</span></div>`).join('')
  : 'Nothing logged yet.';
document.getElementById('upnext').innerHTML=D.ondeck.length
  ? D.ondeck.map(r=>`<div class="row"><span class="vid">${esc(r.video)}</span>
      <span class="txt">${esc(r.channel)} · ${esc(r.depth)}</span></div>`).join('')
  : 'Worklist clear.';
document.getElementById('feedsub').textContent=`${D.commits.length} commits`;
document.getElementById('feed').innerHTML=D.commits.slice(0,16).map(c=>{
  const m=c.msg.match(/^batch\d+: (\S+) /);
  const hit=m&&(D.videos||[]).some(v=>v.v===m[1]);
  return `<div class="row"${hit?` data-vid="${esc(m[1])}" style="cursor:pointer"`:''}>`+
   `<span class="vid">${esc(c.sha)}</span><span class="txt">${esc(c.msg)}</span>
   <span class="when">${esc((c.when||'').slice(5,10))}</span></div>`;}).join('');
const escThis=D.escalations.filter(e=>e.thisBatch);
document.getElementById('escsub').textContent=`${escThis.length} this batch`;
document.getElementById('escs').innerHTML=escThis.length
  ? escThis.slice(0,12).map(e=>`<div class="row"><span class="vid">${esc(e.video)}</span>
     <span class="txt">${esc(e.kind)}</span></div>`).join('')
  : 'None raised — nothing needs a human call yet.';

/* detail panel */
/* Markdown -> HTML, carrying line attribution through.

   Line numbers are the ones git blame saw, so front matter and the H1 are
   SKIPPED rather than sliced off — slicing would shift every index and the
   highlighting would land a few paragraphs adrift. Each emitted block records
   the videos whose lines it contains, which is what lights it up. */
function mdToHtml(src,marks){
  const L=src.split('\n');let o=[],i=0;
  // skip front matter and the leading H1 without renumbering
  if(L[0]==='---'){i=1;while(i<L.length&&L[i]!=='---')i++;i++;}
  while(i<L.length&&!L[i].trim())i++;
  if(i<L.length&&/^#\s+/.test(L[i]))i++;
  const inl=s=>esc(s).replace(/`([^`]+)`/g,'<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*\n]+)\*/g,'$1<em>$2</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,(m,t,h)=>h.includes('.md')
      ?`<a href="#" data-nav="${esc(h)}">${t}</a>`:`<a href="${esc(h)}" target="_blank" rel="noopener">${t}</a>`);
  // who wrote lines [a,b)? blank-only blocks stay unattributed
  const who=(a,b)=>{if(!marks)return '';const set=[];
    for(let k=a;k<b;k++){const v=marks[k];if(v&&!set.includes(v)&&L[k]&&L[k].trim())set.push(v);}
    return set.length?` data-v="${esc(set.join(' '))}"`:'';};
  const put=(open,rest,a,b)=>o.push(open.slice(0,-1)+who(a,b)+'>'+rest);
  while(i<L.length){const l=L[i],st=i;
    if(/^<!--/.test(l)){i++;continue;}
    if(/^\|/.test(l)){const b=[];while(i<L.length&&/^\|/.test(L[i]))b.push(L[i++]);
      const rs=b.filter(r=>!/^\|[\s:-]+\|/.test(r)).map(r=>r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim()));
      if(rs.length)put('<div class="tw">','<table><thead><tr>'+rs[0].map(c=>`<th>${inl(c)}</th>`).join('')+
        '</tr></thead><tbody>'+rs.slice(1).map(r=>'<tr>'+r.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>').join('')+
        '</tbody></table></div>',st,i);continue;}
    let m;
    if((m=l.match(/^(#{1,6})\s+(.*)$/))){const d=Math.min(m[1].length,6);
      put(`<h${d}>`,`${inl(m[2])}</h${d}>`,st,st+1);i++;continue;}
    if(/^>\s?/.test(l)){const b=[];while(i<L.length&&/^>\s?/.test(L[i]))b.push(L[i++].replace(/^>\s?/,''));
      put('<blockquote>',`${inl(b.join(' '))}</blockquote>`,st,i);continue;}
    if(/^\s*[-*]\s+/.test(l)){const b=[],spans=[];
      while(i<L.length){const mi=L[i].match(/^\s*[-*]\s+(.*)$/);
        if(mi){b.push(mi[1]);spans.push([i,i+1]);i++;continue;}
        // KB notes wrap bullets onto indented continuation lines — fold them
        // back into the item instead of spilling them out as paragraphs
        if(b.length&&L[i].trim()&&/^\s{2,}\S/.test(L[i])&&!/^\s*[#>|]/.test(L[i])&&!/^\s*```/.test(L[i])){
          b[b.length-1]+=' '+L[i].trim();spans[spans.length-1][1]=i+1;i++;continue;}
        break;}
      // attribute per LIST ITEM — a note usually gains a bullet, not a list
      o.push('<ul>'+b.map((x,k)=>`<li${who(spans[k][0],spans[k][1])}>${inl(x)}</li>`).join('')+'</ul>');
      continue;}
    if(/^```/.test(l)){i++;const b=[];while(i<L.length&&!/^```/.test(L[i]))b.push(L[i++]);
      if(i<L.length)i++;put('<pre>',`<code>${esc(b.join('\n'))}</code></pre>`,st,i);continue;}
    if(/^---+$/.test(l)){o.push('<hr>');i++;continue;}
    if(!l.trim()){i++;continue;}
    const b=[];while(i<L.length&&L[i].trim()&&!/^([#>|`]|\s*[-*]\s)/.test(L[i]))b.push(L[i++]);
    if(!b.length)b.push(L[i++]);
    put('<p>',`${inl(b.join(' '))}</p>`,st,i);}
  return o.join('\n');
}
/* runs -> a flat line->video lookup, built once per note on demand */
const marksCache=new Map();
function marksFor(path){
  if(marksCache.has(path))return marksCache.get(path);
  const runs=(D.attrib||{})[path];
  let m=null;
  if(runs){m=[];runs.forEach(([a,n,v])=>{for(let k=0;k<n;k++)m[a+k]=v;});}
  marksCache.set(path,m);return m;
}
const det=document.getElementById('detail');
const body=document.getElementById('darticle'), dtabs=document.getElementById('dtabs'),
      dback=document.getElementById('dback'), dbacktext=document.getElementById('dbacktext');
const videos=D.videos||[], byVideo=new Map(videos.map(v=>[v.v,v]));
const diffs=D.diffs||{};

/* Rendering a diff. Added lines green, removed red, context plain — the
   highlighting IS the review surface, so it stays legible in both themes. */
function diffHunks(hunks,dropped){
  const h=hunks.map(k=>`<div class="hunk"><div class="at">${esc(k.at)}</div>`+
    k.lines.map(l=>{const c=l[0]==='+'?'add':l[0]==='-'?'del':'';
      return `<div class="dl ${c}">${esc(l.slice(1))}</div>`;}).join('')+`</div>`).join('');
  return h+(dropped?`<div class="dnote">${dropped.toLocaleString()} more changed lines not shown — the page itself has them all.</div>`:'');
}
function diffFile(path,d,openFirst){
  return `<details class="dfile"${openFirst?' open':''}>`+
    `<summary><span class="fp">${esc(path)}</span><span class="sp" style="flex:1"></span>`+
    `<span class="plus">+${d.add}</span><span class="minus">−${d.rem}</span></summary>`+
    diffHunks(d.hunks,d.dropped)+`</details>`;
}

/* The panel is a stack. Back returns to wherever you came from. */
let back=null;
function show(o){
  document.getElementById('dtitle').textContent=o.title;
  document.getElementById('dpath').textContent=o.path||'';
  document.getElementById('dmeta').innerHTML=o.meta||'';
  dtabs.hidden=!o.tabs; dtabs.innerHTML=o.tabs||'';
  dback.hidden=!o.back; if(o.back)dbacktext.textContent=o.back.label;
  dback.onclick=o.back?o.back.go:null;
  body.innerHTML=o.html; body.scrollTop=0;
  det.classList.add('open');
}

/* a knowledgebase page — the article, and what this run changed in it */
/* a knowledgebase page. `vid` lights up what that one video wrote, in place;
   without it, everything this batch wrote is lit in a neutral tint. */
let activeVid=null;
function open(path,tab,from,vid){
  const f=byPath.get(path); if(!f) return;
  if(from!==undefined)back=from;
  if(vid!==undefined)activeVid=vid;
  const fm=f.fm||{}, tags=[];
  if(fm.type)tags.push(`<span class="tag">${esc(fm.type)}</span>`);
  if(fm.confidence)tags.push(`<span class="tag ${esc(fm.confidence)}">${esc(fm.confidence)}</span>`);
  (fm.regions||[]).forEach(r=>tags.push(`<span class="tag">${esc(r)}</span>`));
  (fm.waters||[]).forEach(w=>tags.push(`<span class="tag">${esc(w)}</span>`));
  if(f.status!=='unchanged')tags.push(`<span class="tag">${f.status} this batch</span>`);
  const d=diffs[path], isNew=f.status==='added';
  tab=tab||'page';
  let tabs='';
  if(d||isNew){
    const cl=isNew?'new page':`+${d.add} −${d.rem}`;
    tabs=`<button class="dtab" data-tab="page" aria-selected="${tab==='page'}">Article</button>`+
         `<button class="dtab" data-tab="diff" aria-selected="${tab==='diff'}">Raw diff · ${esc(cl)}</button>`;
  }
  const art=()=>mdToHtml(f.content||'',marksFor(path));
  let html, banner='';
  if(activeVid){
    const x=byVideo.get(activeVid);
    banner=`<div class="hbar"><span class="hsw"></span><span>Highlighted: what `+
      `<button class="linkbtn" id="hvid">${esc(x?(x.title||activeVid):activeVid)}</button> wrote in this page</span>`+
      `<span class="sp" style="flex:1"></span><span class="hnav"><button id="hprev" title="Previous change">↑</button>`+
      `<span id="hcount" class="mono"></span><button id="hnext" title="Next change">↓</button></span>`+
      `<button class="linkbtn" id="hclear">show all</button></div>`;
  }
  if(tab==='diff'){
    html=isNew
      ? `<div class="dnote" style="border:none">Written from scratch this run — the whole article is new.</div>`+art()
      : diffFile(path,d,true);
  } else html=banner+art();
  show({title:f.title,path:path,meta:tags.join(''),tabs:tabs,html:html,back:back});
  if(activeVid)body.classList.add('focus'); else body.classList.remove('focus');
  dtabs.querySelectorAll('.dtab').forEach(b=>b.onclick=()=>open(path,b.dataset.tab));
  body.querySelectorAll('a[data-nav]').forEach(a=>a.onclick=ev=>{
    ev.preventDefault();
    const raw=a.dataset.nav.split('#')[0], here=path.includes('/')?path.split('/').slice(0,-1):[];
    const st=[];here.concat(raw.split('/')).forEach(p=>p==='..'?st.pop():(p==='.'?0:st.push(p)));
    open(st.join('/'),null,undefined,null);});
  if(activeVid&&tab!=='diff')wireHighlight(path);
}

/* mark this video's blocks, and let the reviewer step through them */
function wireHighlight(path){
  const hits=[...body.querySelectorAll('[data-v]')]
    .filter(el=>el.dataset.v.split(' ').includes(activeVid));
  hits.forEach(el=>el.classList.add('mine'));
  let at=-1;
  const cnt=document.getElementById('hcount');
  const paint=()=>{cnt.textContent=hits.length?`${Math.max(at,0)+1}/${hits.length}`:'0';};
  const jump=n=>{if(!hits.length)return;at=(at+n+hits.length)%hits.length;
    hits.forEach(el=>el.classList.remove('at'));hits[at].classList.add('at');
    hits[at].scrollIntoView({block:'center',behavior:'smooth'});paint();};
  paint();
  document.getElementById('hnext').onclick=()=>jump(1);
  document.getElementById('hprev').onclick=()=>jump(-1);
  document.getElementById('hclear').onclick=()=>open(path,'page',undefined,null);
  const hv=document.getElementById('hvid');
  if(hv)hv.onclick=()=>openVideo(activeVid,{label:byPath.get(path).title,go:()=>open(path)});
  if(hits.length)jump(1);
}

/* one video — every page its extraction touched, changes highlighted */
function openVideo(v,from){
  const x=byVideo.get(v); if(!x) return;
  if(from!==undefined)back=from;
  activeVid=null;
  const tags=[x.ch,x.cls,x.depth].filter(Boolean)
    .map(t=>`<span class="tag">${esc(t)}</span>`).join('')+
    `<span class="tag">${x.files.length} page${x.files.length===1?'':'s'}</span>`+
    `<span class="tag"><span class="plus">+${x.add}</span> <span class="minus">−${x.rem}</span></span>`;
  const res=(x.result||'').split(' / ').slice(1).join(' / ')||x.result||'';
  const head=`<p class="mut" style="margin:0 0 6px">${esc(x.when.slice(0,10))} · commit <code>${esc(x.sha)}</code> · `+
    `<a href="https://www.youtube.com/watch?v=${encodeURIComponent(v)}" target="_blank" rel="noopener">watch on YouTube</a></p>`+
    (res?`<p style="margin:0 0 14px">${esc(res)}</p>`:'');

  /* The point of this screen: open the ARTICLE with this video's writing lit
     up in place. `wrote` counts lines still standing in the live note, so a
     page a later video overwrote shows the smaller number honestly. */
  const wrote=x.wrote||[];
  const live=wrote.length
    ? `<div class="ghead">Read what it wrote, in the article</div>`+
      wrote.map(([path,n])=>{const f=byPath.get(path);
        return `<button class="vrow" data-open="${esc(path)}">`+
          `<span class="vt">${esc(f?f.title:path)}</span>`+
          `<span class="vm">${esc(path)} · <span class="plus">${n} line${n===1?'':'s'} still standing</span></span></button>`;
      }).join('')
    : `<p class="mut">Nothing this video wrote is still in the knowledgebase — a later extraction rewrote it, or the commit only touched logs.</p>`;

  const others=x.files.filter(f=>!wrote.some(([p])=>p===f.path));
  const raw=x.files.length
    ? `<div class="ghead">Raw diff, exactly as committed</div>`+
      x.files.map((f,i)=>{const [ad,rm]=[f.hunks.reduce((n,h)=>n+h.lines.filter(l=>l[0]==='+').length,0),
                                        f.hunks.reduce((n,h)=>n+h.lines.filter(l=>l[0]==='-').length,0)];
        return diffFile(f.path,{hunks:f.hunks,add:ad,rem:rm,dropped:0},false);}).join('')
      +(x.dropped?`<div class="dnote">${x.dropped.toLocaleString()} more changed lines not shown.</div>`:'')
    : `<p class="mut">No page changes recorded for this video — it was logged as skipped or yielded nothing.</p>`;

  show({title:x.title||v,path:v,meta:tags,html:head+live+raw,
        back:back||{label:'All videos',go:()=>openVideoList()}});
  const home={label:x.title||v,go:()=>openVideo(v)};
  body.querySelectorAll('[data-open]').forEach(el=>el.onclick=()=>
    open(el.dataset.open,'page',home,v));
  body.querySelectorAll('.fp').forEach(el=>{el.style.cursor='pointer';
    el.onclick=ev=>{ev.stopPropagation();ev.preventDefault();
      if(byPath.has(el.textContent))open(el.textContent,'diff',home,v);};});
}

/* the list of videos already read */
function openVideoList(){
  back=null;
  const rows=videos.map(x=>`<button class="vrow" data-v="${esc(x.v)}">`+
    `<span class="vt">${esc(x.title||x.v)}</span>`+
    `<span class="vm">${esc(x.ch||'')} · ${esc(x.when.slice(0,10))} · ${x.files.length} page${x.files.length===1?'':'s'} `+
    `<span class="plus">+${x.add}</span> <span class="minus">−${x.rem}</span></span></button>`).join('');
  const omitted=D.videosOmitted?`<div class="dnote">${D.videosOmitted} earlier videos are not listed here — the page keeps diffs for the ${videos.length} most recent.</div>`:'';
  show({title:'Videos read',path:`${videos.length} with a recorded extraction`,
        html:`<input class="filt" id="vfilt" placeholder="Filter by title, channel or id…">`+
             `<div id="vlist">${rows}</div>`+omitted});
  const f=document.getElementById('vfilt');
  f.oninput=()=>{const q=f.value.toLowerCase();
    document.querySelectorAll('#vlist .vrow').forEach(b=>{
      b.hidden=q&&!b.textContent.toLowerCase().includes(q)&&!b.dataset.v.toLowerCase().includes(q);});};
  document.querySelectorAll('#vlist .vrow').forEach(b=>
    b.onclick=()=>openVideo(b.dataset.v,{label:'All videos',go:()=>openVideoList()}));
}

/* every page the run touched, new and edited, grouped by folder */
function openPageList(){
  back=null;
  const touched=D.files.filter(f=>f.status!=='unchanged');
  const byFolder=new Map();
  touched.forEach(f=>{const k=f.path.includes('/')?f.path.split('/')[0]:'root';
    (byFolder.get(k)||byFolder.set(k,[]).get(k)).push(f);});
  const html=[...byFolder.entries()].sort((a,b)=>a[0].localeCompare(b[0])).map(([k,fs])=>
    `<div class="ghead">${esc(k)} · ${fs.length}</div>`+
    fs.sort((a,b)=>a.title.localeCompare(b.title)).map(f=>{const d=diffs[f.path];
      const badge=f.status==='added'?'<span class="plus">new</span>'
        :d?`<span class="plus">+${d.add}</span> <span class="minus">−${d.rem}</span>`:'';
      return `<button class="vrow" data-page="${esc(f.path)}"><span class="vt">${esc(f.title)}</span>`+
        `<span class="vm">${esc(f.path)} ${badge}</span></button>`;}).join('')).join('');
  const nNew=touched.filter(f=>f.status==='added').length;
  show({title:'Pages this run touched',
        path:`${nNew} written from scratch · ${touched.length-nNew} edited`,
        html:`<input class="filt" id="pfilt" placeholder="Filter by title or path…"><div id="plist">${html}</div>`});
  const f=document.getElementById('pfilt');
  f.oninput=()=>{const q=f.value.toLowerCase();
    document.querySelectorAll('#plist .vrow').forEach(b=>
      b.hidden=q&&!b.textContent.toLowerCase().includes(q));};
  document.querySelectorAll('#plist .vrow').forEach(b=>b.onclick=()=>
    open(b.dataset.page,diffs[b.dataset.page]?'diff':'page',{label:'All pages',go:()=>openPageList()}));
}

document.getElementById('seevideos').onclick=()=>openVideoList();
document.getElementById('seevideos2').onclick=()=>openVideoList();
document.getElementById('seepages').onclick=()=>openPageList();
document.getElementById('dclose').onclick=()=>det.classList.remove('open');
addEventListener('keydown',e=>{if(e.key==='Escape')det.classList.remove('open');});
document.addEventListener('click',e=>{
  const v=e.target.closest('[data-vid]');
  if(v&&byVideo.has(v.dataset.vid)){openVideo(v.dataset.vid,null);return;}
  const b=e.target.closest('[data-p]');
  if(b&&byPath.has(b.dataset.p))open(b.dataset.p,null,null);});

/* intro */
const intro=document.getElementById('intro');
document.getElementById('introgo').onclick=()=>intro.hidden=true;
document.getElementById('helpbtn').onclick=()=>intro.hidden=false;
document.getElementById('introrandom').onclick=()=>{intro.hidden=true;
  const pool=newNotes.length?newNotes:D.files;
  open(pool[Math.floor(Math.random()*pool.length)].path);};

/* sonar */
const cv=document.getElementById('graph'),cx=cv.getContext('2d');
const nodes=D.files.filter(f=>!f.path.endsWith('README.md')).map(f=>({
  p:f.path,t:f.title,c:col(f.path),recent:f.recent,st:f.status,deg:0,
  x:(Math.random()-.5)*760,y:(Math.random()-.5)*560,vx:0,vy:0}));
const ix=new Map(nodes.map((n,i)=>[n.p,i])),eds=[];
D.files.forEach(f=>(f.links||[]).forEach(l=>{
  if(ix.has(f.path)&&ix.has(l)&&f.path!==l){eds.push([ix.get(f.path),ix.get(l)]);
    nodes[ix.get(f.path)].deg++;nodes[ix.get(l)].deg++;}}));
document.getElementById('gstat').textContent=`${nodes.length} pages · ${eds.length} links`;
const fols=[...new Set(nodes.map(n=>fol(n.p)))].sort();
document.getElementById('legend').innerHTML=fols.map(f=>
  `<span class="lg"><span class="sw" style="background:${FC[f]||'#5E7076'}"></span>${esc(f)}</span>`).join('');
let cam={x:0,y:0,z:1},t0=performance.now(),ticks=0;
function fit(){const r=cv.getBoundingClientRect(),d=devicePixelRatio||1;
  cv.width=r.width*d;cv.height=r.height*d;cx.setTransform(d,0,0,d,0,0);}
addEventListener('resize',fit);fit();
function frame(now){
  if(ticks++<340){
    for(let i=0;i<nodes.length;i++){const a=nodes[i];
      for(let j=i+1;j<nodes.length;j++){const b=nodes[j];
        const dx=b.x-a.x,dy=b.y-a.y,d2=dx*dx+dy*dy||1;
        if(d2<36000){const d=Math.sqrt(d2),f=820/d2,ux=dx/d,uy=dy/d;
          a.vx-=ux*f;a.vy-=uy*f;b.vx+=ux*f;b.vy+=uy*f;}}}
    eds.forEach(([i,j])=>{const a=nodes[i],b=nodes[j],dx=b.x-a.x,dy=b.y-a.y,
      d=Math.hypot(dx,dy)||1,f=(d-86)*.012,ux=dx/d,uy=dy/d;
      a.vx+=ux*f;a.vy+=uy*f;b.vx-=ux*f;b.vy-=uy*f;});
    nodes.forEach(n=>{n.vx-=n.x*.0024;n.vy-=n.y*.0024;n.x+=n.vx*=.86;n.y+=n.vy*=.86;});
  }
  const w=cv.clientWidth,h=cv.clientHeight,T=(now-t0)/1000;
  cx.clearRect(0,0,w,h);cx.save();cx.translate(w/2+cam.x,h/2+cam.y);cx.scale(cam.z,cam.z);
  cx.strokeStyle=getComputedStyle(document.documentElement).getPropertyValue('--ring');
  cx.globalAlpha=.20;cx.lineWidth=1;cx.beginPath();
  eds.forEach(([i,j])=>{cx.moveTo(nodes[i].x,nodes[i].y);cx.lineTo(nodes[j].x,nodes[j].y);});
  cx.stroke();cx.globalAlpha=1;
  nodes.forEach(n=>{const r=3+Math.min(n.deg,16)*.4;
    if(n.recent>=0){const ph=(T*.7-n.recent*.12)%1.6;
      if(ph>0&&ph<1.4){cx.globalAlpha=(1-ph/1.4)*.55;cx.strokeStyle=n.c;cx.lineWidth=1.6;
        cx.beginPath();cx.arc(n.x,n.y,r+ph*26,0,6.283);cx.stroke();cx.globalAlpha=1;}}
    cx.beginPath();cx.arc(n.x,n.y,r,0,6.283);cx.fillStyle=n.c;cx.fill();
    if(n.st==='added'){cx.strokeStyle='#fff';cx.lineWidth=1.3;cx.stroke();}});
  cx.restore();requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
function pick(ev){const r=cv.getBoundingClientRect();
  const mx=(ev.clientX-r.left-r.width/2-cam.x)/cam.z,my=(ev.clientY-r.top-r.height/2-cam.y)/cam.z;
  let best=null,bd=1e9;nodes.forEach(n=>{const d=Math.hypot(n.x-mx,n.y-my);if(d<bd){bd=d;best=n;}});
  return bd<15?best:null;}
let drag=null;
cv.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,m:0};cv.classList.add('drag');});
addEventListener('pointerup',e=>{if(drag&&drag.m<4){const n=pick(e);if(n)open(n.p);}
  drag=null;cv.classList.remove('drag');});
addEventListener('pointermove',e=>{
  if(drag){drag.m+=Math.abs(e.clientX-drag.x)+Math.abs(e.clientY-drag.y);
    cam.x+=e.clientX-drag.x;cam.y+=e.clientY-drag.y;drag.x=e.clientX;drag.y=e.clientY;return;}
  const tip=document.getElementById('tip'),n=(e.target===cv)?pick(e):null;
  if(n){tip.style.display='block';tip.style.left=(e.clientX+12)+'px';tip.style.top=(e.clientY+12)+'px';
    tip.textContent=n.t;}else tip.style.display='none';});
cv.addEventListener('wheel',e=>{e.preventDefault();
  cam.z=Math.max(.3,Math.min(3,cam.z*(e.deltaY<0?1.1:.9)));},{passive:false});
</script>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default=str(ROOT / "sources" / "bight-watch.html"))
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--runs", help="saved GitHub list_workflow_runs JSON for the Chain card")
    a = ap.parse_args()
    snap = build(a.base)
    if a.runs:
        snap["runs"] = load_runs(a.runs)
    payload = json.dumps(snap, ensure_ascii=False).replace("</script>", "<\\/script>")
    html = HTML.replace("__SNAP__", payload)
    out = Path(a.out)
    out.write_text(html, encoding="utf-8")
    c = snap["counts"]
    print(f"bight-watch -> {out}  ({len(html)/1_000_000:.2f} MB)")
    print(f"  pages {len(snap['files'])} | new {sum(1 for f in snap['files'] if f['status']=='added')}")
    print(f"  videos: " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
    print(f"  commits {len(snap['commits'])} | escalations {len(snap['escalations'])}"
          f" | chain runs {len(snap['runs'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
