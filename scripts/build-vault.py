#!/usr/bin/env python3
"""Build the batch-3 vault: a self-contained HTML progress/accuracy dashboard.

Successor to the batch-2 vault. Same three-pane IDE shape (explorer / graph +
worklist + reader / telemetry) so it reads the same way, plus region and waters
chips — batch 3 added region gating, and that gating is what "accuracy" now
turns on.

The page is a STATIC SNAPSHOT. Re-run this script to refresh it while the
ingestion chain runs; nothing here polls, so what you see is the moment it was
generated (stamped in the header).

Usage: python scripts/build-vault.py [-o out.html] [--base origin/main]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = ("sources/", ".git/", "scripts/", "prompts/", ".github/")
WL_START, WL_END = "<!-- batch3:worklist:start -->", "<!-- batch3:worklist:end -->"


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(ROOT), *args],
                              capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return ""


def parse_front_matter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line.strip())
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        val = re.sub(r"\s*#.*$", "", val).strip()
        if val.startswith("[") and val.endswith("]"):
            fm[key] = [v.strip() for v in val[1:-1].split(",") if v.strip()]
        else:
            fm[key] = val
    return fm


def outbound_links(text: str, path: str) -> list[str]:
    """Relative .md links, excluding the generated backlinks block."""
    si, ei = text.find("<!-- backlinks:start -->"), text.find("<!-- backlinks:end -->")
    if si != -1 and ei != -1 and ei > si:
        text = text[:si] + text[ei:]
    here = Path(path).parent
    out = []
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+\.md)(?:#[^)]*)?\)", text):
        target = m.group(1)
        if target.startswith(("http://", "https://")):
            continue
        try:
            resolved = (here / target).resolve().relative_to(ROOT.resolve())
        except (ValueError, OSError):
            continue
        s = str(resolved)
        if s not in out:
            out.append(s)
    return out


def collect_files(base: str) -> list[dict]:
    changed = set()
    added = set()
    for line in git("diff", "--name-status", f"{base}..HEAD", "--", "*.md").splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0][:1], parts[-1]
        (added if status == "A" else changed).add(path)

    files = []
    for p in sorted(ROOT.rglob("*.md")):
        rel = str(p.relative_to(ROOT))
        if rel.startswith(SKIP_DIRS) or rel == "CLAUDE.md":
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), rel)
        files.append({
            "path": rel,
            "title": title,
            "fm": parse_front_matter(text),
            "links": outbound_links(text, rel),
            "status": "added" if rel in added else ("modified" if rel in changed else "unchanged"),
            "lines": text.count("\n") + 1,
            "content": text,
        })
    return files


def collect_worklist() -> list[dict]:
    log = (ROOT / "sources" / "extraction-log.md").read_text(encoding="utf-8")
    try:
        block = log.split(WL_START, 1)[1].split(WL_END, 1)[0]
    except IndexError:
        return []
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 6 or cells[0] in ("video_id", "") or set(cells[0]) <= {"-", " "}:
            continue
        rows.append(dict(zip(("video", "channel", "cls", "depth", "status", "result"), cells)))
    return rows


def collect_commits(base: str, limit: int = 60) -> list[dict]:
    # The record separator must LEAD the format. With it trailing, every chunk
    # after the first begins with the previous commit's --name-status lines and
    # the header parse silently drops the commit (73 commits parsed as 1).
    out = git("log", f"{base}..HEAD", f"-{limit}", "--date=iso-strict",
              "--pretty=format:%x1e%h%x1f%ad%x1f%s", "--name-status")
    commits = []
    for chunk in out.split("\x1e"):
        chunk = chunk.strip("\n")
        if not chunk:
            continue
        head, _, rest = chunk.partition("\n")
        parts = head.split("\x1f")
        if len(parts) < 3:
            continue
        sha, when, subject = parts[0].strip(), parts[1], parts[2]
        touched = []
        for line in rest.splitlines():
            bits = line.split("\t")
            if len(bits) >= 2 and bits[-1].endswith(".md"):
                touched.append({"st": bits[0][:1], "path": bits[-1]})
        commits.append({"sha": sha, "when": when, "msg": subject, "files": touched[:12]})
    return commits


def collect_escalations(base_iso: str = "") -> list[dict]:
    """Parse '## <iso-timestamp> - <video_id> - <kind>' headings.

    The file is append-only prose sections, not a table; an earlier table
    parser here silently returned zero.
    """
    p = ROOT / "sources" / "escalations.md"
    if not p.exists():
        return []
    rows = []
    lines = p.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if not line.startswith("## "):
            continue
        parts = [s.strip() for s in re.split(r"\s+[—-]\s+", line[3:].strip())]
        when = parts[0] if parts else ""
        body = []
        for nxt in lines[i + 1:]:
            if nxt.startswith("## "):
                break
            if nxt.strip():
                body.append(nxt.strip())
            if len(" ".join(body)) > 300:
                break
        rows.append({
            "when": when,
            "video": parts[1] if len(parts) > 1 else "?",
            "kind": parts[2] if len(parts) > 2 else "",
            "why": " ".join(body)[:300],
            "thisBatch": bool(base_iso and when > base_iso),
        })
    rows.reverse()
    return rows


def build_snapshot(base: str) -> dict:
    wl = collect_worklist()
    counts: dict[str, int] = {}
    for r in wl:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    files = collect_files(base)
    base_iso = git("show", "-s", "--format=%cI", base).strip()
    return {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD").strip(),
        "headSha": git("rev-parse", "--short", "HEAD").strip(),
        "base": base,
        "baseSha": git("rev-parse", "--short", base).strip(),
        "files": files,
        "worklist": wl,
        "counts": counts,
        "commits": collect_commits(base),
        "escalations": collect_escalations(base_iso),
    }


HTML = r"""<title>Batch 3 Vault</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Deliberate single-theme design: this is an IDE surface, dark by intent.
   Every colour is painted explicitly so the page holds on either host ground. */
:root{
  --ground:#16181d; --panel:#1b1e25; --panel2:#21252e; --border:#2a2e38;
  --ink:#dcdfe6; --muted:#8b91a0; --dim:#5c6270;
  --accent:#a08cff; --accent-dim:#6f5fd0;
  --ok:#3fb950; --warn:#d29922; --bad:#f85149; --skip:#565d6b; --pend:#7d8496;
  --sans:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  color-scheme:dark;
}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;background:var(--ground);color:var(--ink);font:14px/1.45 var(--sans);overflow:hidden}
#app{display:flex;flex-direction:column;height:100vh}
#topbar{display:flex;align-items:center;gap:14px;padding:9px 14px;background:var(--panel);
  border-bottom:1px solid var(--border);flex:none;flex-wrap:wrap}
.vname{font-weight:600;letter-spacing:.01em;white-space:nowrap}
.chipm{font-family:var(--mono);font-size:11.5px;color:var(--muted);background:var(--panel2);
  border:1px solid var(--border);padding:2px 9px;border-radius:20px;white-space:nowrap}
#minibar{flex:1 1 140px;min-width:80px;max-width:420px}
.stack{display:flex;gap:2px;height:8px;border-radius:4px;overflow:hidden;background:var(--panel2)}
.stack span{display:block;height:100%;min-width:0}
#minilabel{font-family:var(--mono);font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
#main{display:flex;flex:1;min-height:0}
aside{background:var(--panel);flex:none;display:flex;flex-direction:column;min-height:0}
#explorer{width:252px;border-right:1px solid var(--border)}
#telemetry{width:326px;border-left:1px solid var(--border);overflow-y:auto;padding:10px}
.searchwrap{padding:8px;border-bottom:1px solid var(--border)}
input[type=search],select{width:100%;background:var(--panel2);border:1px solid var(--border);
  color:var(--ink);border-radius:6px;padding:5px 8px;font:12.5px var(--sans);outline:none}
input[type=search]:focus,select:focus{border-color:var(--accent-dim)}
#tree{overflow-y:auto;flex:1;padding:4px 0 24px}
.fhead{display:flex;align-items:center;gap:6px;padding:3px 8px;cursor:pointer;color:var(--muted);
  font-size:12.5px;font-weight:600;user-select:none;border:none;background:none;width:100%;text-align:left;font-family:inherit}
.fhead:hover{color:var(--ink)}
.fhead .tw{width:10px;font-size:9px;transition:transform .12s;display:inline-block}
.fhead.open .tw{transform:rotate(90deg)}
.fhead .cnt{margin-left:auto;font-family:var(--mono);font-size:10.5px;color:var(--dim);font-variant-numeric:tabular-nums}
.ffiles{display:none}.fhead.open+.ffiles{display:block}
.frow{display:flex;align-items:center;gap:6px;padding:2.5px 8px 2.5px 26px;cursor:pointer;
  font-size:13px;color:var(--muted);white-space:nowrap;overflow:hidden;border:none;background:none;width:100%;text-align:left;font-family:inherit}
.frow:hover{background:var(--panel2);color:var(--ink)}
.frow.active{background:var(--panel2);color:var(--accent)}
.frow .fn{overflow:hidden;text-overflow:ellipsis}
.badge{flex:none;font-size:9px;font-weight:700;border-radius:4px;padding:0 4px;line-height:14px;letter-spacing:.04em}
.badge.added{color:#7ee2a0;background:rgba(63,185,80,.14)}
.badge.modified{color:#f0c674;background:rgba(210,153,34,.14)}
#center{flex:1;display:flex;flex-direction:column;min-width:0;background:var(--ground)}
#tabs{display:flex;align-items:center;gap:2px;padding:6px 10px 0;border-bottom:1px solid var(--border);background:var(--panel);flex:none}
.tab{padding:5px 14px 7px;font-size:13px;color:var(--muted);cursor:pointer;border:1px solid transparent;
  border-bottom:none;border-radius:7px 7px 0 0;user-select:none;max-width:320px;overflow:hidden;
  text-overflow:ellipsis;white-space:nowrap;background:none;font-family:inherit}
.tab:hover{color:var(--ink)}
.tab.active{background:var(--ground);border-color:var(--border);color:var(--ink)}
.tab:focus-visible,.frow:focus-visible,.fhead:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
#views{flex:1;min-height:0;position:relative}
.view{position:absolute;inset:0;display:none}.view.active{display:block}
#graphwrap{overflow:hidden}
#gcanvas{display:block;width:100%;height:100%;cursor:grab}
#gcanvas.drag{cursor:grabbing}
#ghud{position:absolute;left:12px;bottom:12px;background:rgba(27,30,37,.93);border:1px solid var(--border);
  border-radius:9px;padding:9px 12px;font-size:11.5px;color:var(--muted);max-width:230px}
#ghud .lg{display:flex;align-items:center;gap:7px;padding:1.5px 0}
#ghud .dot{width:9px;height:9px;border-radius:50%;flex:none}
#gstats{position:absolute;right:12px;top:10px;font-family:var(--mono);font-size:11px;color:var(--dim);
  text-align:right;font-variant-numeric:tabular-nums}
#noteview{overflow-y:auto}
#noteinner{max-width:74ch;margin:0 auto;padding:28px 34px 90px}
.fmchips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:18px}
.chip{font-size:11px;font-family:var(--mono);border:1px solid var(--border);background:var(--panel);
  color:var(--muted);border-radius:20px;padding:2px 9px}
.chip.high{color:#7ee2a0;border-color:rgba(63,185,80,.42)}
.chip.medium{color:#f0c674;border-color:rgba(210,153,34,.42)}
.chip.low{color:#ff9b94;border-color:rgba(248,81,73,.42)}
.chip.type{color:var(--accent);border-color:var(--accent-dim)}
.chip.reg{color:#8fd0ff;border-color:rgba(88,166,255,.38)}
.chip.wat{color:#9adcc6;border-color:rgba(63,185,80,.28)}
.md h1,.md h2,.md h3{line-height:1.25;text-wrap:balance;font-weight:600}
.md h1{font-size:26px;margin:4px 0 14px}
.md h2{font-size:19px;margin:26px 0 8px;padding-bottom:5px;border-bottom:1px solid var(--border)}
.md h3{font-size:15.5px;margin:20px 0 6px}
.md p,.md li{color:var(--ink)}.md li{margin:2px 0}
.md a{color:var(--accent);text-decoration:none}.md a:hover{text-decoration:underline}
.md code{font-family:var(--mono);font-size:12.5px;background:var(--panel2);border-radius:4px;padding:1px 5px}
.md pre{background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:12px 14px;overflow-x:auto}
.md pre code{background:none;padding:0}
.md blockquote{margin:10px 0;padding:4px 14px;border-left:3px solid var(--accent-dim);color:var(--muted)}
.tblwrap{overflow-x:auto;margin:12px 0;border:1px solid var(--border);border-radius:8px}
.md table{border-collapse:collapse;font-size:12.5px;min-width:100%}
.md th{text-align:left;color:var(--muted);font-weight:600;background:var(--panel)}
.md th,.md td{padding:5px 10px;border-bottom:1px solid var(--border);vertical-align:top}
#queueview{display:none;flex-direction:column}#queueview.active{display:flex}
#qbar{display:flex;gap:8px;align-items:center;padding:10px 12px;border-bottom:1px solid var(--border);flex:none;flex-wrap:wrap}
#qsearch{width:210px}#qchannel{width:190px}
.fchip{font-size:12px;padding:3px 10px;border-radius:20px;border:1px solid var(--border);color:var(--muted);
  cursor:pointer;user-select:none;font-variant-numeric:tabular-nums;background:none;font-family:inherit}
.fchip.on{color:var(--ink);border-color:var(--accent-dim);background:rgba(160,140,255,.09)}
#qscroll{flex:1;overflow:auto}
#qtable{border-collapse:collapse;width:100%;font-size:12.5px}
#qtable th{position:sticky;top:0;background:var(--panel);color:var(--muted);text-align:left;font-weight:600;
  padding:6px 10px;border-bottom:1px solid var(--border);z-index:1}
#qtable td{padding:4.5px 10px;border-bottom:1px solid var(--border);vertical-align:top}
#qtable td.vid{font-family:var(--mono);font-size:11.5px;color:var(--muted);white-space:nowrap}
#qtable td.res{color:var(--muted);max-width:520px}
.st{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.03em;border-radius:4px;padding:1px 7px}
.st.pending{color:var(--pend);background:rgba(125,132,150,.15)}
.st.done{color:#7ee2a0;background:rgba(63,185,80,.15)}
.st.skipped{color:var(--skip);background:rgba(86,93,107,.2)}
.st.escalated{color:#f0c674;background:rgba(210,153,34,.15)}
.st.reverted{color:#ff9b94;background:rgba(248,81,73,.15)}
.card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:12px 13px;margin-bottom:10px}
.card h3{margin:0 0 9px;font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);display:flex;align-items:center;gap:7px}
.card h3 .sp{flex:1}
.card h3 .sub{font-weight:400;letter-spacing:0;text-transform:none;font-family:var(--mono);font-size:10.5px;color:var(--dim)}
.prow{display:flex;align-items:center;gap:8px;font-size:12.5px;padding:2px 0;font-variant-numeric:tabular-nums}
.prow .pd{width:8px;height:8px;border-radius:3px;flex:none}
.prow .pl{color:var(--muted)}
.prow .pv{margin-left:auto;font-family:var(--mono);font-size:12px}
.feed{padding:7px 0;border-bottom:1px solid var(--border);font-size:12.5px}
.feed:last-child{border-bottom:none}
.fh{display:flex;gap:8px;align-items:baseline}
.fsha{font-family:var(--mono);font-size:11px;color:var(--accent);flex:none}
.ftime{margin-left:auto;font-family:var(--mono);font-size:10.5px;color:var(--dim);flex:none}
.fmsg{color:var(--ink);overflow-wrap:anywhere}
.ffile{display:flex;gap:6px;font-family:var(--mono);font-size:10.5px;color:var(--muted);cursor:pointer;padding:1px 0;
  border:none;background:none;width:100%;text-align:left}
.ffile:hover{color:var(--accent)}
.ffile .s{flex:none;width:10px;font-weight:700}
.ffile .s.A{color:var(--ok)}.ffile .s.M{color:var(--warn)}.ffile .s.D{color:var(--bad)}
.ffile .p{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nlink{display:block;padding:3px 0;font-size:12.5px;color:var(--ink);cursor:pointer;overflow:hidden;
  text-overflow:ellipsis;white-space:nowrap;border:none;background:none;width:100%;text-align:left;font-family:inherit}
.nlink:hover{color:var(--accent)}
.nlink .nf{color:var(--dim);font-size:11px;font-family:var(--mono)}
.mut{color:var(--dim);font-size:12px}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-thumb{background:#30353f;border-radius:6px;border:2px solid var(--ground)}
::-webkit-scrollbar-track{background:transparent}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
@media (max-width:900px){#explorer,#telemetry{display:none}}
</style>

<div id="app">
  <div id="topbar">
    <span class="vname">Batch 3 Vault</span>
    <span class="chipm" id="branchchip"></span>
    <div id="minibar"><div class="stack" id="mbar"></div></div>
    <span id="minilabel"></span>
    <span class="chipm" id="stamp"></span>
  </div>
  <div id="main">
    <aside id="explorer">
      <div class="searchwrap"><input id="fsearch" type="search" placeholder="Search notes…" aria-label="Search notes"></div>
      <div id="tree"></div>
    </aside>
    <div id="center">
      <div id="tabs">
        <button class="tab active" id="tab-graph">Graph</button>
        <button class="tab" id="tab-queue">Worklist</button>
        <button class="tab" id="tab-note" style="display:none"></button>
      </div>
      <div id="views">
        <div class="view active" id="graphwrap">
          <canvas id="gcanvas"></canvas>
          <div id="gstats"></div>
          <div id="ghud"><div id="legend"></div></div>
        </div>
        <div class="view" id="noteview"><div id="noteinner"></div></div>
        <div class="view" id="queueview">
          <div id="qbar">
            <input id="qsearch" type="search" placeholder="Filter rows…" aria-label="Filter worklist">
            <select id="qchannel" aria-label="Channel filter"><option value="">All channels</option></select>
            <span id="qchips"></span>
          </div>
          <div id="qscroll">
            <table id="qtable">
              <thead><tr><th>status</th><th>video</th><th>channel</th><th>class</th><th>depth</th><th>result</th></tr></thead>
              <tbody id="qbody"></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <aside id="telemetry">
      <div class="card"><h3>Extraction progress<span class="sp"></span><span class="sub" id="pupd"></span></h3>
        <div class="stack" id="bigbar" style="height:10px;margin-bottom:9px"></div>
        <div id="prows"></div></div>
      <div class="card"><h3>New notes<span class="sp"></span><span class="sub" id="newcount"></span></h3>
        <div id="newnotes" class="mut"></div></div>
      <div class="card"><h3>Region coverage<span class="sp"></span><span class="sub">gated types</span></h3>
        <div id="regcov"></div></div>
      <div class="card"><h3>Commits<span class="sp"></span><span class="sub" id="csub"></span></h3><div id="feed"></div></div>
      <div class="card"><h3>Escalations<span class="sp"></span><span class="sub" id="esub"></span></h3>
        <div id="ebody" class="mut"></div></div>
    </aside>
  </div>
</div>
<script id="snap" type="application/json">__SNAP__</script>
<script>
const D = JSON.parse(document.getElementById('snap').textContent);
const esc = s => String(s??'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const byPath = new Map(D.files.map(f => [f.path, f]));
const SC = {done:'#3fb950', pending:'#7d8496', skipped:'#565d6b', escalated:'#d29922', reverted:'#f85149'};
const ORDER = ['done','pending','escalated','skipped','reverted'];

/* ---------- topbar + progress ---------- */
document.getElementById('branchchip').textContent = D.branch + ' @ ' + D.headSha;
document.getElementById('stamp').textContent = 'snapshot ' + D.generatedAt.replace('T',' ').replace('Z',' UTC');
document.getElementById('pupd').textContent = D.headSha;
const total = D.worklist.length;
function renderBars(){
  const seg = ORDER.filter(k => D.counts[k]).map(k =>
    `<span style="flex:${D.counts[k]};background:${SC[k]}" title="${k}: ${D.counts[k]}"></span>`).join('');
  document.getElementById('mbar').innerHTML = seg;
  document.getElementById('bigbar').innerHTML = seg;
  const done = D.counts.done||0;
  document.getElementById('minilabel').textContent = `${done}/${total} done · ${D.counts.pending||0} pending`;
  document.getElementById('prows').innerHTML = ORDER.filter(k=>D.counts[k]).map(k =>
    `<div class="prow"><span class="pd" style="background:${SC[k]}"></span><span class="pl">${k}</span>
     <span class="pv">${D.counts[k]}</span></div>`).join('') +
    `<div class="prow" style="border-top:1px solid var(--border);margin-top:6px;padding-top:6px">
       <span class="pl">total</span><span class="pv">${total}</span></div>`;
}
renderBars();

/* ---------- explorer ---------- */
const folders = {};
D.files.forEach(f => { const d = f.path.includes('/') ? f.path.split('/')[0] : '.'; (folders[d] ||= []).push(f); });
function renderTree(filter=''){
  const q = filter.toLowerCase();
  const t = document.getElementById('tree'); t.innerHTML='';
  Object.keys(folders).sort().forEach(dir => {
    const hits = folders[dir].filter(f => !q || f.path.toLowerCase().includes(q) || (f.title||'').toLowerCase().includes(q));
    if(!hits.length) return;
    const open = !!q || hits.some(f => f.status !== 'unchanged');
    const head = document.createElement('button');
    head.className = 'fhead' + (open ? ' open' : '');
    head.innerHTML = `<span class="tw">▶</span><span>${esc(dir)}</span><span class="cnt">${hits.length}</span>`;
    head.onclick = () => head.classList.toggle('open');
    const wrap = document.createElement('div'); wrap.className='ffiles';
    hits.forEach(f => {
      const b = document.createElement('button'); b.className='frow'; b.dataset.path=f.path;
      const badge = f.status==='unchanged' ? '' : `<span class="badge ${f.status}">${f.status==='added'?'NEW':'MOD'}</span>`;
      b.innerHTML = `<span class="fn">${esc(f.path.split('/').pop())}</span>${badge}`;
      b.onclick = () => openNote(f.path);
      wrap.appendChild(b);
    });
    t.appendChild(head); t.appendChild(wrap);
  });
}
document.getElementById('fsearch').oninput = e => renderTree(e.target.value);
renderTree();

/* ---------- markdown reader (small, deliberate subset) ---------- */
function md(src){
  src = src.replace(/^---\n[\s\S]*?\n---\n/, '');
  const lines = src.split('\n'); let out=[], i=0;
  const inline = s => esc(s)
    .replace(/`([^`]+)`/g,'<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*\n]+)\*/g,'$1<em>$2</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m,txt,href) =>
      href.endsWith('.md')||href.includes('.md#')
        ? `<a href="#" data-nav="${esc(href)}">${txt}</a>`
        : `<a href="${esc(href)}" target="_blank" rel="noopener">${txt}</a>`);
  while(i < lines.length){
    const l = lines[i];
    if(/^<!--/.test(l)){ i++; continue; }
    if(/^```/.test(l)){ const buf=[]; i++; while(i<lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]); i++;
      out.push(`<pre><code>${esc(buf.join('\n'))}</code></pre>`); continue; }
    if(/^\|/.test(l)){ const buf=[]; while(i<lines.length && /^\|/.test(lines[i])) buf.push(lines[i++]);
      const rows = buf.filter(r => !/^\|[\s:-]+\|/.test(r))
        .map(r => r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim()));
      if(rows.length){ out.push('<div class="tblwrap"><table><thead><tr>' +
        rows[0].map(c=>`<th>${inline(c)}</th>`).join('') + '</tr></thead><tbody>' +
        rows.slice(1).map(r=>'<tr>'+r.map(c=>`<td>${inline(c)}</td>`).join('')+'</tr>').join('') +
        '</tbody></table></div>'); }
      continue; }
    let m;
    if((m = l.match(/^(#{1,4})\s+(.*)$/))){ const n=m[1].length; out.push(`<h${n}>${inline(m[2])}</h${n}>`); i++; continue; }
    if(/^>\s?/.test(l)){ const buf=[]; while(i<lines.length && /^>\s?/.test(lines[i])) buf.push(lines[i++].replace(/^>\s?/,''));
      out.push(`<blockquote>${inline(buf.join(' '))}</blockquote>`); continue; }
    if(/^[-*]\s+/.test(l)){ const buf=[]; while(i<lines.length && /^\s*[-*]\s+/.test(lines[i])) buf.push(lines[i++].replace(/^\s*[-*]\s+/,''));
      out.push('<ul>'+buf.map(b=>`<li>${inline(b)}</li>`).join('')+'</ul>'); continue; }
    if(/^---+$/.test(l)){ out.push('<hr>'); i++; continue; }
    if(!l.trim()){ i++; continue; }
    const buf=[]; while(i<lines.length && lines[i].trim() && !/^([#>|`-]|\s*[-*]\s)/.test(lines[i])) buf.push(lines[i++]);
    out.push(`<p>${inline(buf.join(' '))}</p>`);
  }
  return out.join('\n');
}
function openNote(path){
  const f = byPath.get(path); if(!f) return;
  const fm = f.fm||{};
  const chips = [];
  if(fm.type) chips.push(`<span class="chip type">${esc(fm.type)}</span>`);
  if(fm.confidence) chips.push(`<span class="chip ${esc(fm.confidence)}">${esc(fm.confidence)}</span>`);
  (fm.regions||[]).forEach(r => chips.push(`<span class="chip reg">${esc(r)}</span>`));
  (fm.waters||[]).forEach(w => chips.push(`<span class="chip wat">${esc(w)}</span>`));
  chips.push(`<span class="chip">${f.lines} lines</span>`);
  if(f.status!=='unchanged') chips.push(`<span class="chip">${f.status} this batch</span>`);
  document.getElementById('noteinner').innerHTML =
    `<div class="fmchips">${chips.join('')}</div><div class="md">${md(f.content)}</div>`;
  document.querySelectorAll('#noteinner a[data-nav]').forEach(a => a.onclick = ev => {
    ev.preventDefault();
    const raw = a.dataset.nav.split('#')[0];
    const here = path.includes('/') ? path.split('/').slice(0,-1) : [];
    const parts = here.concat(raw.split('/')); const stack=[];
    parts.forEach(p => p==='..' ? stack.pop() : (p==='.'?null:stack.push(p)));
    openNote(stack.join('/'));
  });
  const tb = document.getElementById('tab-note');
  tb.style.display=''; tb.textContent = path.split('/').pop();
  showTab('note');
  document.querySelectorAll('.frow').forEach(r => r.classList.toggle('active', r.dataset.path===path));
  document.getElementById('noteview').scrollTop = 0;
}
function showTab(which){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  ({graph:['graphwrap','tab-graph'],queue:['queueview','tab-queue'],note:['noteview','tab-note']})[which]
    .forEach((id,ix)=>document.getElementById(id).classList.add(ix?'active':'active'));
}
document.getElementById('tab-graph').onclick = ()=>showTab('graph');
document.getElementById('tab-queue').onclick = ()=>showTab('queue');
document.getElementById('tab-note').onclick  = ()=>showTab('note');

/* ---------- worklist ---------- */
const chans = [...new Set(D.worklist.map(r=>r.channel))].sort();
document.getElementById('qchannel').innerHTML =
  '<option value="">All channels</option>' + chans.map(c=>`<option>${esc(c)}</option>`).join('');
let stFilter = new Set();
document.getElementById('qchips').innerHTML = ORDER.filter(k=>D.counts[k])
  .map(k=>`<button class="fchip" data-st="${k}">${k} ${D.counts[k]}</button>`).join('');
document.querySelectorAll('.fchip').forEach(c => c.onclick = () => {
  const k=c.dataset.st; stFilter.has(k)?stFilter.delete(k):stFilter.add(k);
  c.classList.toggle('on'); renderQueue();
});
function renderQueue(){
  const q = document.getElementById('qsearch').value.toLowerCase();
  const ch = document.getElementById('qchannel').value;
  const rows = D.worklist.filter(r =>
    (!stFilter.size || stFilter.has(r.status)) && (!ch || r.channel===ch) &&
    (!q || (r.video+r.channel+r.cls+r.depth+r.result).toLowerCase().includes(q)));
  document.getElementById('qbody').innerHTML = rows.slice(0,1200).map(r =>
    `<tr><td><span class="st ${esc(r.status)}">${esc(r.status)}</span></td>
      <td class="vid">${esc(r.video)}</td><td>${esc(r.channel)}</td>
      <td>${esc(r.cls)}</td><td>${esc(r.depth)}</td><td class="res">${esc(r.result)}</td></tr>`).join('')
    || `<tr><td colspan="6" class="mut" style="padding:14px">No rows match.</td></tr>`;
}
document.getElementById('qsearch').oninput = renderQueue;
document.getElementById('qchannel').onchange = renderQueue;
renderQueue();

/* ---------- telemetry cards ---------- */
const newNotes = D.files.filter(f=>f.status==='added');
document.getElementById('newcount').textContent = newNotes.length + ' created';
document.getElementById('newnotes').innerHTML = newNotes.length
  ? newNotes.map(f=>`<button class="nlink" data-p="${esc(f.path)}"><span class="nf">${esc(f.path.split('/')[0])}/</span> ${esc(f.title)}</button>`).join('')
  : 'No new notes yet.';

const gated = new Set(['species','technique','lure','rig','location','seasonal','bait','decision']);
const regCount = {};
D.files.forEach(f => { if(gated.has(f.fm?.type)) (f.fm.regions||['— missing —']).forEach(r => regCount[r]=(regCount[r]||0)+1); });
document.getElementById('regcov').innerHTML = Object.entries(regCount).sort((a,b)=>b[1]-a[1])
  .map(([r,n])=>`<div class="prow"><span class="pl">${esc(r)}</span><span class="pv">${n}</span></div>`).join('');

document.getElementById('csub').textContent = D.commits.length + ' since ' + D.baseSha;
document.getElementById('feed').innerHTML = D.commits.slice(0,25).map(c =>
  `<div class="feed"><div class="fh"><span class="fsha">${esc(c.sha)}</span>
    <span class="ftime">${esc((c.when||'').slice(5,16).replace('T',' '))}</span></div>
   <div class="fmsg">${esc(c.msg)}</div>
   <div>${c.files.map(f=>`<button class="ffile" data-p="${esc(f.path)}"><span class="s ${esc(f.st)}">${esc(f.st)}</span><span class="p">${esc(f.path)}</span></button>`).join('')}</div></div>`).join('');

const escThis = D.escalations.filter(e=>e.thisBatch);
document.getElementById('esub').textContent = `${escThis.length} this batch · ${D.escalations.length} all`;
document.getElementById('ebody').innerHTML = D.escalations.length
  ? (escThis.length ? '' : `<div class="mut" style="padding-bottom:6px">None raised this batch — the rows below are batch-2 legacy.</div>`)
    + D.escalations.slice(0,25).map(e=>`<div class="feed"><div class="fh">
        <span class="fsha">${esc(e.video)}</span>
        <span class="ftime">${esc((e.when||'').slice(5,16).replace('T',' '))}</span></div>
       <div class="fmsg">${esc(e.kind)}${e.why?' — '+esc(e.why):''}</div></div>`).join('')
  : 'None recorded.';

document.addEventListener('click', ev => {
  const b = ev.target.closest('[data-p]'); if(b && byPath.has(b.dataset.p)) openNote(b.dataset.p);
});

/* ---------- force graph ---------- */
const cv = document.getElementById('gcanvas'), ctx = cv.getContext('2d');
const TYPE_COLOR = {species:'#a08cff',technique:'#58a6ff',lure:'#3fb950',rig:'#d29922',
  tackle:'#f0883e',location:'#ff7b9d',conditions:'#5ee0d0',seasonal:'#c9a0ff',
  planning:'#8b91a0',bait:'#7ee2a0','fish-care':'#ff9b94',decision:'#ffd280',profile:'#5c6270'};
const nodes = D.files.filter(f => !f.path.endsWith('README.md'))
  .map(f => ({p:f.path, t:f.fm?.type||'other', st:f.status, deg:0,
              x:Math.random()*800-400, y:Math.random()*600-300, vx:0, vy:0}));
const idx = new Map(nodes.map((n,i)=>[n.p,i]));
const edges = [];
D.files.forEach(f => (f.links||[]).forEach(l => {
  if(idx.has(f.path) && idx.has(l) && f.path!==l){
    edges.push([idx.get(f.path), idx.get(l)]);
    nodes[idx.get(f.path)].deg++; nodes[idx.get(l)].deg++;
  }
}));
document.getElementById('gstats').textContent = `${nodes.length} notes · ${edges.length} links`;
document.getElementById('legend').innerHTML = Object.entries(TYPE_COLOR)
  .filter(([t]) => nodes.some(n=>n.t===t))
  .map(([t,c]) => `<div class="lg"><span class="dot" style="background:${c}"></span>${t}</div>`).join('')
  + `<div class="lg" style="margin-top:6px;color:var(--dim)">ring = new this batch</div>`;
let cam={x:0,y:0,z:1};
function resize(){ const r=cv.getBoundingClientRect(), d=devicePixelRatio||1;
  cv.width=r.width*d; cv.height=r.height*d; ctx.setTransform(d,0,0,d,0,0); }
addEventListener('resize', resize); resize();
let ticks=0;
function step(){
  if(ticks++ < 320){
    for(let i=0;i<nodes.length;i++){ const a=nodes[i];
      for(let j=i+1;j<nodes.length;j++){ const b=nodes[j];
        let dx=b.x-a.x, dy=b.y-a.y, d2=dx*dx+dy*dy||1;
        if(d2<40000){ const f=900/d2, d=Math.sqrt(d2); const ux=dx/d,uy=dy/d;
          a.vx-=ux*f; a.vy-=uy*f; b.vx+=ux*f; b.vy+=uy*f; } } }
    edges.forEach(([i,j])=>{ const a=nodes[i],b=nodes[j];
      const dx=b.x-a.x, dy=b.y-a.y, d=Math.hypot(dx,dy)||1, f=(d-90)*0.012;
      const ux=dx/d,uy=dy/d; a.vx+=ux*f; a.vy+=uy*f; b.vx-=ux*f; b.vy-=uy*f; });
    nodes.forEach(n=>{ n.vx-=n.x*0.0022; n.vy-=n.y*0.0022;
      n.x+=n.vx*=0.86; n.y+=n.vy*=0.86; });
  }
  const w=cv.clientWidth, h=cv.clientHeight;
  ctx.clearRect(0,0,w,h); ctx.save(); ctx.translate(w/2+cam.x,h/2+cam.y); ctx.scale(cam.z,cam.z);
  ctx.strokeStyle='rgba(140,148,166,.16)'; ctx.lineWidth=1; ctx.beginPath();
  edges.forEach(([i,j])=>{ ctx.moveTo(nodes[i].x,nodes[i].y); ctx.lineTo(nodes[j].x,nodes[j].y); });
  ctx.stroke();
  nodes.forEach(n=>{ const r=3.2+Math.min(n.deg,14)*0.42;
    ctx.beginPath(); ctx.arc(n.x,n.y,r,0,6.284);
    ctx.fillStyle=TYPE_COLOR[n.t]||'#5c6270'; ctx.fill();
    if(n.st==='added'){ ctx.strokeStyle='#fff'; ctx.lineWidth=1.4; ctx.stroke(); } });
  ctx.restore();
  requestAnimationFrame(step);
}
step();
let drag=null;
cv.addEventListener('pointerdown', e=>{ drag={x:e.clientX,y:e.clientY}; cv.classList.add('drag'); });
addEventListener('pointerup', ()=>{ drag=null; cv.classList.remove('drag'); });
addEventListener('pointermove', e=>{ if(!drag) return;
  cam.x+=e.clientX-drag.x; cam.y+=e.clientY-drag.y; drag={x:e.clientX,y:e.clientY}; });
cv.addEventListener('wheel', e=>{ e.preventDefault();
  cam.z=Math.max(.25,Math.min(3,cam.z*(e.deltaY<0?1.1:0.9))); }, {passive:false});
cv.addEventListener('click', e=>{
  const r=cv.getBoundingClientRect();
  const mx=(e.clientX-r.left-r.width/2-cam.x)/cam.z, my=(e.clientY-r.top-r.height/2-cam.y)/cam.z;
  let best=null,bd=1e9;
  nodes.forEach(n=>{ const d=Math.hypot(n.x-mx,n.y-my); if(d<bd){bd=d;best=n;} });
  if(best && bd<14) openNote(best.p);
});
</script>
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default=str(ROOT / "sources" / "batch-3-vault.html"))
    ap.add_argument("--base", default="origin/main")
    a = ap.parse_args()

    snap = build_snapshot(a.base)
    payload = json.dumps(snap, ensure_ascii=False).replace("</script>", "<\\/script>")
    html = HTML.replace("__SNAP__", payload)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    c = snap["counts"]
    print(f"vault -> {out}  ({len(html)/1_000_000:.2f} MB)")
    print(f"  notes {len(snap['files'])} | new {sum(1 for f in snap['files'] if f['status']=='added')}"
          f" | modified {sum(1 for f in snap['files'] if f['status']=='modified')}")
    print(f"  worklist {len(snap['worklist'])} rows: " +
          ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
    print(f"  commits {len(snap['commits'])} | escalations {len(snap['escalations'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
