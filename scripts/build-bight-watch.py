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
import json
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
      <div class="stamp">snapshot <span class="mono" id="gen"></span> · static — ask Cameron to refresh</div>
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
          <h2 class="dtitle" id="dtitle"></h2>
          <div class="dpath mono" id="dpath"></div>
          <div class="dmeta" id="dmeta"></div>
        </div>
        <div class="darticle" id="darticle"></div>
      </div>
    </div>
    <aside class="rail">
      <div class="card">
        <h2>Extraction progress<span class="sp"></span><span class="sub" id="pcttext"></span></h2>
        <div class="meter" id="meter"></div>
        <div class="tally" id="tally"></div>
      </div>
      <div class="card" id="chaincard" hidden><h2>Chain<span class="sp"></span><span class="sub" id="chainsub"></span></h2>
        <div id="runs"></div></div>
      <div class="card"><h2>Pages written<span class="sp"></span><span class="sub" id="newsub"></span></h2>
        <div id="newlist" class="mut"></div></div>
      <div class="card"><h2>Logged videos<span class="sp"></span><span class="sub" id="donesub"></span></h2>
        <div id="donelist" class="mut"></div></div>
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
  ? D.done.slice(0,18).map(r=>`<div class="row"><span class="vid">${esc(r.video)}</span>
      <span class="txt">${esc(r.result||r.cls)}</span></div>`).join('')
  : 'Nothing logged yet.';
document.getElementById('upnext').innerHTML=D.ondeck.length
  ? D.ondeck.map(r=>`<div class="row"><span class="vid">${esc(r.video)}</span>
      <span class="txt">${esc(r.channel)} · ${esc(r.depth)}</span></div>`).join('')
  : 'Worklist clear.';
document.getElementById('feedsub').textContent=`${D.commits.length} commits`;
document.getElementById('feed').innerHTML=D.commits.slice(0,16).map(c=>
  `<div class="row"><span class="vid">${esc(c.sha)}</span><span class="txt">${esc(c.msg)}</span>
   <span class="when">${esc((c.when||'').slice(5,10))}</span></div>`).join('');
const escThis=D.escalations.filter(e=>e.thisBatch);
document.getElementById('escsub').textContent=`${escThis.length} this batch`;
document.getElementById('escs').innerHTML=escThis.length
  ? escThis.slice(0,12).map(e=>`<div class="row"><span class="vid">${esc(e.video)}</span>
     <span class="txt">${esc(e.kind)}</span></div>`).join('')
  : 'None raised — nothing needs a human call yet.';

/* detail panel */
function mdToHtml(src){
  src=src.replace(/^---\n[\s\S]*?\n---\n/,'').replace(/^\s*#\s+.*\n/,'');
  const L=src.split('\n');let o=[],i=0;
  const inl=s=>esc(s).replace(/`([^`]+)`/g,'<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*\n]+)\*/g,'$1<em>$2</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g,(m,t,h)=>h.includes('.md')
      ?`<a href="#" data-nav="${esc(h)}">${t}</a>`:`<a href="${esc(h)}" target="_blank" rel="noopener">${t}</a>`);
  while(i<L.length){const l=L[i];
    if(/^<!--/.test(l)){i++;continue;}
    if(/^\|/.test(l)){const b=[];while(i<L.length&&/^\|/.test(L[i]))b.push(L[i++]);
      const rs=b.filter(r=>!/^\|[\s:-]+\|/.test(r)).map(r=>r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim()));
      if(rs.length)o.push('<div class="tw"><table><thead><tr>'+rs[0].map(c=>`<th>${inl(c)}</th>`).join('')+
        '</tr></thead><tbody>'+rs.slice(1).map(r=>'<tr>'+r.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>').join('')+
        '</tbody></table></div>');continue;}
    let m;
    if((m=l.match(/^(#{1,6})\s+(.*)$/))){const d=Math.min(m[1].length,6);o.push(`<h${d}>${inl(m[2])}</h${d}>`);i++;continue;}
    if(/^>\s?/.test(l)){const b=[];while(i<L.length&&/^>\s?/.test(L[i]))b.push(L[i++].replace(/^>\s?/,''));
      o.push(`<blockquote>${inl(b.join(' '))}</blockquote>`);continue;}
    if(/^\s*[-*]\s+/.test(l)){const b=[];
      while(i<L.length){const mi=L[i].match(/^\s*[-*]\s+(.*)$/);
        if(mi){b.push(mi[1]);i++;continue;}
        // KB notes wrap bullets onto indented continuation lines — fold them
        // back into the item instead of spilling them out as paragraphs
        if(b.length&&L[i].trim()&&/^\s{2,}\S/.test(L[i])&&!/^\s*[#>|]/.test(L[i])&&!/^\s*```/.test(L[i])){
          b[b.length-1]+=' '+L[i].trim();i++;continue;}
        break;}
      o.push('<ul>'+b.map(x=>`<li>${inl(x)}</li>`).join('')+'</ul>');continue;}
    if(/^```/.test(l)){i++;const b=[];while(i<L.length&&!/^```/.test(L[i]))b.push(L[i++]);
      if(i<L.length)i++;o.push(`<pre><code>${esc(b.join('\n'))}</code></pre>`);continue;}
    if(/^---+$/.test(l)){o.push('<hr>');i++;continue;}
    if(!l.trim()){i++;continue;}
    const b=[];while(i<L.length&&L[i].trim()&&!/^([#>|`]|\s*[-*]\s)/.test(L[i]))b.push(L[i++]);
    if(!b.length)b.push(L[i++]);
    o.push(`<p>${inl(b.join(' '))}</p>`);}
  return o.join('\n');
}
const det=document.getElementById('detail');
function open(path){
  const f=byPath.get(path); if(!f) return;
  const fm=f.fm||{}, tags=[];
  if(fm.type)tags.push(`<span class="tag">${esc(fm.type)}</span>`);
  if(fm.confidence)tags.push(`<span class="tag ${esc(fm.confidence)}">${esc(fm.confidence)}</span>`);
  (fm.regions||[]).forEach(r=>tags.push(`<span class="tag">${esc(r)}</span>`));
  (fm.waters||[]).forEach(w=>tags.push(`<span class="tag">${esc(w)}</span>`));
  if(f.status!=='unchanged')tags.push(`<span class="tag">${f.status} this batch</span>`);
  document.getElementById('dtitle').textContent=f.title;
  document.getElementById('dpath').textContent=f.path;
  document.getElementById('dmeta').innerHTML=tags.join('');
  document.getElementById('darticle').innerHTML=mdToHtml(f.content||'');
  document.querySelectorAll('#darticle a[data-nav]').forEach(a=>a.onclick=ev=>{
    ev.preventDefault();
    const raw=a.dataset.nav.split('#')[0], here=path.includes('/')?path.split('/').slice(0,-1):[];
    const st=[];here.concat(raw.split('/')).forEach(p=>p==='..'?st.pop():(p==='.'?0:st.push(p)));
    open(st.join('/'));});
  det.classList.add('open');
  document.getElementById('darticle').scrollTop=0;
}
document.getElementById('dclose').onclick=()=>det.classList.remove('open');
addEventListener('keydown',e=>{if(e.key==='Escape')det.classList.remove('open');});
document.addEventListener('click',e=>{const b=e.target.closest('[data-p]');
  if(b&&byPath.has(b.dataset.p))open(b.dataset.p);});

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
