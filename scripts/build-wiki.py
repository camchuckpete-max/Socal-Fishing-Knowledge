#!/usr/bin/env python3
"""Build the single-file wiki UI for the knowledgebase.

Reads every knowledge note in the repo, renders it to HTML with a small
dependency-free Markdown engine, and writes one self-contained page —
``wiki/index.html`` — that carries the whole KB, its fonts, its styles and its
search. No network, no CDN, no build tooling: ``python3 scripts/build-wiki.py``.

Run it after content changes (and after ``link-maintenance.py``), then publish
``wiki/index.html``.
"""

from __future__ import annotations

import base64
import html
import json
import posixpath
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "scripts" / "wiki"
OUT = ROOT / "wiki" / "index.html"
REPO = "https://github.com/camchuckpete-max/Socal-Fishing-Knowledge"
BLOB = REPO + "/blob/main/"

# ---------------------------------------------------------------------------
# What goes in the wiki, in navigation order.
# code:  two-letter chart label used in the sidebar
# group: sidebar grouping
# ---------------------------------------------------------------------------

BRANCHES = [
    ("species", "Species", "SP", "fish", "Behaviour, where &amp; when, and the situation&rarr;technique router for every fish in the Bight."),
    ("techniques", "Techniques", "TQ", "fish", "How each method is actually executed, and when to reach for it."),
    ("lures", "Lures", "LU", "fish", "Per-lure specs, rigging and running parameters."),
    ("rigging", "Rigging", "RG", "fish", "Knots, leaders and terminal rigs &mdash; parameters and judgment."),
    ("tackle", "Tackle", "TK", "fish", "Rod, reel, line and hook selection by application."),
    ("bait", "Bait", "BA", "fish", "Making bait, keeping it alive, and fishing it."),
    ("conditions", "Conditions", "CN", "water", "The interpretation layers: temperature, colour, current, moon, tide, birds."),
    ("seasonal", "Seasonal", "SE", "water", "Month-by-month priors &mdash; the pattern layer, not current intel."),
    ("locations", "Locations", "LO", "water", "Universal structure and zone knowledge across the Bight."),
    ("planning", "Planning", "PL", "water", "The day-plan protocol, searching, glassing and electronics."),
    ("fish-care", "Fish care", "FC", "boat", "Bleeding, chilling, ikejime and handling."),
    ("profiles", "Profiles", "PR", "boat", "Per-angler boat, rods, tackle and spots."),
    ("sources", "Sources", "SO", "meta", "Provenance &mdash; source registry, extraction log and input documents."),
    ("skills", "Skills", "SK", "meta", "The boat-day skill built from these notes."),
    ("prompts", "Prompts", "PT", "meta", "The extraction and evaluation prompts behind the corpus."),
]

GROUPS = [
    ("fish", "Fish &amp; gear"),
    ("water", "Read the water"),
    ("boat", "On the boat"),
    ("meta", "Behind the KB"),
]

# Files pulled in outside the branch folders.
EXTRA_FILES = [("README.md", "meta"), ("CLAUDE.md", "meta")]

# Short labels for the sidebar where the note's own H1 is too long for a rail.
NAV_TITLES = {"readme": "Knowledgebase README", "spec": "Repo conventions"}

# Never walk these (raw transcripts are 8 MB of source material, not notes).
SKIP_DIRS = {"sources/transcripts", "tests", ".git", "wiki", "scripts"}


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
FENCE_RE = re.compile(r"^\s*```+\s*([\w-]*)\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
BARE_URL_RE = re.compile(r"(?<![\"(=>])\bhttps?://[^\s<>\"'`)\]]+")
CODE_RE = re.compile(r"(`+)(.+?)\1", re.S)
STRONG_RE = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", re.S)
EM_STAR_RE = re.compile(r"(?<![\w*])\*(?=[^\s*])([^*]+?)(?<=\S)\*(?![\w*])", re.S)
EM_US_RE = re.compile(r"(?<![\w_])_(?=[^\s_])([^_]+?)(?<=\S)_(?![\w_])", re.S)
STRIKE_RE = re.compile(r"~~(?=\S)(.+?)(?<=\S)~~", re.S)


def slugify(text: str) -> str:
    """GitHub's heading-anchor slug, so in-note ``#anchors`` keep working."""
    s = re.sub(r"<[^>]+>", "", text)
    s = html.unescape(s).strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


class Renderer:
    """Markdown subset covering exactly what the KB writes: headings, lists,
    tables, fences, quotes, links and emphasis."""

    def __init__(self, note_dir: str, resolver):
        self.dir = note_dir
        self.resolve = resolver
        self.toc: list[dict] = []
        self.slugs: dict[str, int] = {}

    # -- inline ----------------------------------------------------------
    def inline(self, text: str) -> str:
        codes: list[str] = []

        def stash(m: re.Match) -> str:
            codes.append(m.group(2).strip())
            return f"\x00c{len(codes) - 1}\x00"

        text = CODE_RE.sub(stash, text)
        text = html.escape(text, quote=False)
        text = LINK_RE.sub(self._link, text)
        text = BARE_URL_RE.sub(
            lambda m: '<a class="x-ext" href="%s" target="_blank" rel="noopener">%s</a>'
            % (m.group(0), m.group(0)),
            text,
        )
        text = STRONG_RE.sub(r"<strong>\1</strong>", text)
        text = EM_STAR_RE.sub(r"<em>\1</em>", text)
        text = EM_US_RE.sub(r"<em>\1</em>", text)
        text = STRIKE_RE.sub(r"<del>\1</del>", text)
        text = re.sub(
            r"\x00c(\d+)\x00",
            lambda m: "<code>%s</code>" % html.escape(codes[int(m.group(1))], quote=False),
            text,
        )
        return text

    def _link(self, m: re.Match) -> str:
        label = m.group(1)
        href = html.unescape(m.group(2))
        # label may itself contain a code stash / emphasis — handled by the
        # caller's later passes, since we only emit the anchor wrapper here.
        target = self.resolve(href, self.dir)
        if target["kind"] == "note":
            anchor = target["anchor"]
            return '<a class="x-note" data-note="%s" data-anchor="%s" href="#/%s%s">%s</a>' % (
                target["note"],
                anchor,
                target["note"],
                ("~" + anchor) if anchor else "",
                label,
            )
        if target["kind"] == "anchor":
            return '<a class="x-anchor" data-anchor="%s" href="#%s">%s</a>' % (
                target["anchor"],
                target["anchor"],
                label,
            )
        return '<a class="x-ext" href="%s" target="_blank" rel="noopener">%s</a>' % (
            html.escape(target["href"], quote=True),
            label,
        )

    # -- blocks ----------------------------------------------------------
    def render(self, md: str, collect_toc: bool = True) -> str:
        lines = md.replace("\r\n", "\n").replace("\t", "    ").split("\n")
        return self._blocks(lines, collect_toc)

    def _blocks(self, lines: list[str], collect_toc: bool = False) -> str:
        out: list[str] = []
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]
            if not line.strip():
                i += 1
                continue

            fence = FENCE_RE.match(line)
            if fence:
                lang = fence.group(1)
                body: list[str] = []
                i += 1
                while i < n and not FENCE_RE.match(lines[i]):
                    body.append(lines[i])
                    i += 1
                i += 1
                code = html.escape("\n".join(body), quote=False)
                cls = f' data-lang="{lang}"' if lang else ""
                out.append(f'<div class="x-pre"><pre{cls}><code>{code}</code></pre></div>')
                continue

            head = HEADING_RE.match(line)
            if head:
                level = len(head.group(1))
                raw = head.group(2)
                text = self.inline(raw)
                slug = slugify(raw)
                seen = self.slugs.get(slug, 0)
                self.slugs[slug] = seen + 1
                if seen:
                    slug = f"{slug}-{seen}"
                if collect_toc and level in (2, 3) and slug:
                    self.toc.append({"id": slug, "text": html.unescape(re.sub(r"<[^>]+>", "", text)), "level": level})
                out.append(
                    f'<h{level} id="{slug}" class="x-h">{text}'
                    f'<a class="x-anchorlink" href="#{slug}" aria-label="Link to this section">#</a></h{level}>'
                )
                i += 1
                continue

            if re.match(r"^\s{0,3}(\*\s*\*\s*\*|-\s*-\s*-|_\s*_\s*_)[\s*\-_]*$", line):
                out.append('<hr class="x-hr">')
                i += 1
                continue

            if line.lstrip().startswith(">"):
                quote: list[str] = []
                while i < n and (lines[i].lstrip().startswith(">") or (quote and lines[i].strip())):
                    stripped = re.sub(r"^\s*>\s?", "", lines[i])
                    quote.append(stripped)
                    i += 1
                out.append('<blockquote class="x-quote">%s</blockquote>' % self._blocks(quote))
                continue

            if "|" in line and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]) and "|" in lines[i + 1]:
                html_table, i = self._table(lines, i)
                out.append(html_table)
                continue

            if ITEM_RE.match(line):
                html_list, i = self._list(lines, i)
                out.append(html_list)
                continue

            para: list[str] = []
            while i < n and lines[i].strip():
                if (
                    HEADING_RE.match(lines[i])
                    or FENCE_RE.match(lines[i])
                    or lines[i].lstrip().startswith(">")
                    or (ITEM_RE.match(lines[i]) and para)
                    or (ITEM_RE.match(lines[i]) and not para)
                ):
                    if para:
                        break
                para.append(lines[i].strip())
                i += 1
                if i < n and ITEM_RE.match(lines[i]):
                    break
            if para:
                out.append("<p>%s</p>" % self.inline("\n".join(para)))
        return "\n".join(out)

    def _table(self, lines: list[str], start: int) -> tuple[str, int]:
        def cells(row: str) -> list[str]:
            row = row.strip()
            if row.startswith("|"):
                row = row[1:]
            if row.endswith("|"):
                row = row[:-1]
            return [c.strip() for c in re.split(r"(?<!\\)\|", row)]

        header = cells(lines[start])
        aligns = []
        for spec in cells(lines[start + 1]):
            left, right = spec.startswith(":"), spec.endswith(":")
            aligns.append("center" if left and right else "right" if right else "left")
        i = start + 2
        rows = []
        while i < len(lines) and lines[i].strip() and "|" in lines[i]:
            rows.append(cells(lines[i]))
            i += 1

        def cell(tag: str, value: str, idx: int) -> str:
            align = aligns[idx] if idx < len(aligns) else "left"
            style = f' style="text-align:{align}"' if align != "left" else ""
            return f"<{tag}{style}>{self.inline(value.replace('<br>', ' '))}</{tag}>"

        head = "".join(cell("th", c, k) for k, c in enumerate(header))
        body = "".join(
            "<tr>%s</tr>" % "".join(cell("td", c, k) for k, c in enumerate(r)) for r in rows
        )
        return (
            '<div class="x-tablewrap"><table class="x-table">'
            f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>",
            i,
        )

    def _list(self, lines: list[str], start: int) -> tuple[str, int]:
        base = indent_of(lines[start])
        first = ITEM_RE.match(lines[start])
        ordered = bool(re.match(r"^\d", first.group(2)))
        items: list[list[str]] = []
        i = start
        n = len(lines)
        while i < n:
            line = lines[i]
            if not line.strip():
                j = i + 1
                while j < n and not lines[j].strip():
                    j += 1
                nxt = lines[j] if j < n else ""
                cont = bool(nxt.strip()) and (
                    indent_of(nxt) > base or (ITEM_RE.match(nxt) and indent_of(nxt) == base)
                )
                if cont and items:
                    items[-1].append("")
                    i = j
                    continue
                break
            m = ITEM_RE.match(line)
            ind = indent_of(line)
            if m and ind == base:
                same_kind = bool(re.match(r"^\d", m.group(2))) == ordered
                if not same_kind and items:
                    break
                items.append([m.group(3)])
                i += 1
                continue
            if ind > base or (items and not m):
                items[-1].append(line)
                i += 1
                continue
            break

        html_items = []
        for raw in items:
            body = [raw[0]]
            rest = raw[1:]
            pad = min(
                (indent_of(l) for l in rest if l.strip()),
                default=0,
            )
            body += [l[pad:] if l.strip() else "" for l in rest]
            inner = self._blocks(body)
            single = inner.count("<p>") == 1 and inner.startswith("<p>") and inner.endswith("</p>")
            if single:
                inner = inner[3:-4]
            html_items.append(f"<li>{inner}</li>")
        tag = "ol" if ordered else "ul"
        cls = "x-ol" if ordered else "x-ul"
        return f'<{tag} class="{cls}">%s</{tag}>' % "".join(html_items), i


# ---------------------------------------------------------------------------
# Notes
# ---------------------------------------------------------------------------


@dataclass
class Note:
    id: str
    path: str
    branch: str
    title: str = ""
    meta: dict = field(default_factory=dict)
    summary: str = ""
    html: str = ""
    text: str = ""
    toc: list = field(default_factory=list)
    backlinks: list = field(default_factory=list)
    children: list = field(default_factory=list)
    updated: str = ""
    words: int = 0
    is_index: bool = False
    subdir: str = ""


def parse_front_matter(raw: str) -> tuple[dict, str]:
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end == -1:
        return {}, raw
    block = raw[3:end]
    body = raw[end + 4 :].lstrip("\n")
    meta: dict = {}
    for line in block.split("\n"):
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key] = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        else:
            meta[key] = value.strip("\"'")
    return meta, body


def note_id_for(path: str) -> str:
    stem = path[:-3] if path.endswith(".md") else path
    if stem.endswith("/README"):
        return stem[: -len("/README")]
    if stem == "README":
        return "readme"
    if stem == "CLAUDE":
        return "spec"
    return stem


def strip_tags(markup: str) -> str:
    """Plain text for search snippets — heading anchor marks removed, and no
    stray space left where an inline tag used to sit before punctuation."""
    text = re.sub(r'<a class="x-anchorlink".*?</a>', "", markup, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", html.unescape(text))
    return re.sub(r"\s+([,.;:!?%)\]])", r"\1", text).strip()


def git_dates() -> dict[str, str]:
    """path -> ISO date of the commit that last touched it."""
    try:
        raw = subprocess.run(
            ["git", "-C", str(ROOT), "log", "--name-only", "--format=\x01%cs", "--no-merges"],
            capture_output=True,
            text=True,
            check=True,
            timeout=90,
        ).stdout
    except Exception:
        return {}
    dates: dict[str, str] = {}
    current = ""
    for line in raw.split("\n"):
        if line.startswith("\x01"):
            current = line[1:].strip()
        elif line.strip() and current:
            dates.setdefault(line.strip(), current)
    return dates


def collect_paths() -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for slug, *_ in BRANCHES:
        base = ROOT / slug
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            rel = path.relative_to(ROOT).as_posix()
            if any(rel.startswith(skip + "/") for skip in SKIP_DIRS):
                continue
            found.append((rel, slug))
    for name, branch in EXTRA_FILES:
        if (ROOT / name).exists():
            found.append((name, branch))
    return found


def build_notes() -> list[Note]:
    paths = collect_paths()
    ids = {}
    for rel, _ in paths:
        ids[note_id_for(rel)] = rel
    known = set(ids)
    dates = git_dates()

    def resolver(href: str, note_dir: str) -> dict:
        href = href.strip()
        if href.startswith(("http://", "https://", "mailto:")):
            return {"kind": "ext", "href": href}
        anchor = ""
        if "#" in href:
            href, _, anchor = href.partition("#")
        if not href:
            return {"kind": "anchor", "anchor": anchor}
        target = posixpath.normpath(posixpath.join(note_dir, href)) if note_dir else posixpath.normpath(href)
        target = target.lstrip("./")
        candidates = [target]
        if target.endswith("/"):
            candidates.append(target.rstrip("/"))
        if not target.endswith(".md"):
            candidates += [target + "/README.md", target.rstrip("/")]
        for cand in candidates:
            nid = note_id_for(cand)
            if nid in known:
                return {"kind": "note", "note": nid, "anchor": anchor}
        return {"kind": "ext", "href": BLOB + target + (("#" + anchor) if anchor else "")}

    notes: list[Note] = []
    for rel, branch in paths:
        raw = (ROOT / rel).read_text(encoding="utf-8")
        meta, body = parse_front_matter(raw)

        # Pull the generated blocks out before rendering: the wiki draws its own
        # index cards and backlink chips from the structured data instead.
        backlinks: list[dict] = []
        children: list[dict] = []
        note_dir = posixpath.dirname(rel)

        def harvest(marker: str, sink: list) -> None:
            nonlocal body
            pattern = re.compile(
                r"<!--\s*%s:start\s*-->(.*?)<!--\s*%s:end\s*-->" % (marker, marker), re.S
            )
            match = pattern.search(body)
            if not match:
                return
            for line in match.group(1).split("\n"):
                item = re.match(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)\s*(?:—|--|-)?\s*(.*)$", line)
                if not item:
                    continue
                target = resolver(item.group(2), note_dir)
                if target["kind"] != "note":
                    continue
                sink.append(
                    {
                        "title": item.group(1).strip("`"),
                        "note": target["note"],
                        "blurb": item.group(3).strip(),
                    }
                )
            body = pattern.sub("", body)

        harvest("backlinks", backlinks)
        harvest("index", children)
        body = re.sub(
            r"<!--\s*mermaid:start\s*-->.*?<!--\s*mermaid:end\s*-->", "", body, flags=re.S
        )
        body = COMMENT_RE.sub("", body)

        title = ""
        first_h1 = re.search(r"^#\s+(.+)$", body, re.M)
        if first_h1:
            title = strip_tags(Renderer(note_dir, resolver).inline(first_h1.group(1)))
            body = body[: first_h1.start()] + body[first_h1.end() :]
        stem = Path(rel).stem
        if not title:
            title = stem.replace("-", " ").title()

        renderer = Renderer(note_dir, resolver)
        rendered = renderer.render(body)
        text = strip_tags(rendered)

        summary = ""
        para = re.search(r"<p>(.*?)</p>", rendered, re.S)
        if para:
            summary = strip_tags(para.group(1))
        if len(summary) > 220:
            cut = summary[:220].rsplit(" ", 1)[0]
            summary = cut + "…"

        nid = note_id_for(rel)
        depth_dir = posixpath.dirname(rel)
        subdir = ""
        if depth_dir and depth_dir != branch and depth_dir.startswith(branch + "/"):
            subdir = depth_dir[len(branch) + 1 :]

        notes.append(
            Note(
                id=nid,
                path=rel,
                branch=branch,
                title=title,
                meta=meta,
                summary=summary,
                html=rendered,
                text=text,
                toc=renderer.toc,
                backlinks=backlinks,
                children=children,
                updated=dates.get(rel, ""),
                words=len(text.split()),
                is_index=Path(rel).name == "README.md" or rel in ("README.md", "CLAUDE.md"),
                subdir=subdir,
            )
        )
    return notes


# ---------------------------------------------------------------------------
# Page assembly
# ---------------------------------------------------------------------------


def font_face_css() -> str:
    faces = [
        ("Source Serif 4", "sourceserif4-400-700-normal.woff2", "normal", "400 700"),
        ("Source Serif 4", "sourceserif4-400-600-italic.woff2", "italic", "400 600"),
        ("Barlow Condensed", "barlowcondensed-500-normal.woff2", "normal", "500"),
        ("Barlow Condensed", "barlowcondensed-600-normal.woff2", "normal", "600"),
        ("Barlow Condensed", "barlowcondensed-700-normal.woff2", "normal", "700"),
        ("IBM Plex Mono", "plexmono-400-normal.woff2", "normal", "400"),
        ("IBM Plex Mono", "plexmono-500-normal.woff2", "normal", "500"),
    ]
    blocks = []
    for family, filename, style, weight in faces:
        data = (ASSETS / "fonts" / filename).read_bytes()
        b64 = base64.b64encode(data).decode("ascii")
        blocks.append(
            "@font-face{font-family:'%s';font-style:%s;font-weight:%s;font-display:swap;"
            "src:url(data:font/woff2;base64,%s) format('woff2');}" % (family, style, weight, b64)
        )
    return "\n".join(blocks)


def payload(notes: list[Note]) -> dict:
    by_branch: dict[str, list[Note]] = {}
    for note in notes:
        by_branch.setdefault(note.branch, []).append(note)

    branches = []
    for slug, label, code, group, blurb in BRANCHES:
        items = by_branch.get(slug, [])
        if not items:
            continue
        branches.append(
            {
                "id": slug,
                "label": label,
                "code": code,
                "group": group,
                "blurb": blurb,
                "count": sum(1 for n in items if not n.is_index),
                "index": slug if any(n.id == slug for n in items) else "",
            }
        )

    def as_dict(note: Note) -> dict:
        meta = note.meta
        return {
            "id": note.id,
            "path": note.path,
            "branch": note.branch,
            "title": note.title,
            "type": meta.get("type", ""),
            "confidence": meta.get("confidence", ""),
            "tags": meta.get("tags", []),
            "sources": meta.get("sources", []),
            "summary": note.summary,
            "html": note.html,
            "text": note.text,
            "toc": note.toc,
            "backlinks": note.backlinks,
            "children": note.children,
            "updated": note.updated,
            "words": note.words,
            "isIndex": note.is_index,
            "subdir": note.subdir,
            "nav": NAV_TITLES.get(note.id, ""),
        }

    knowledge = [n for n in notes if n.branch not in ("sources", "prompts", "skills") and not n.is_index]
    all_sources: set[str] = set()
    for note in notes:
        for src in note.meta.get("sources", []):
            all_sources.add(src)
    transcripts = len(list((ROOT / "sources" / "transcripts").glob("*.md"))) if (ROOT / "sources" / "transcripts").is_dir() else 0

    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "repo": REPO,
        "groups": [{"id": g, "label": l} for g, l in GROUPS],
        "branches": branches,
        "notes": [as_dict(n) for n in notes],
        "stats": {
            "notes": len(knowledge),
            "species": sum(1 for n in notes if n.branch == "species" and not n.is_index),
            "techniques": sum(1 for n in notes if n.branch == "techniques" and not n.is_index),
            "sources": len(all_sources),
            "transcripts": transcripts,
            "words": sum(n.words for n in knowledge),
        },
    }


def main() -> int:
    notes = build_notes()
    if not notes:
        print("no notes found", file=sys.stderr)
        return 1

    data = payload(notes)
    shell = (ASSETS / "shell.html").read_text(encoding="utf-8")
    css = (ASSETS / "app.css").read_text(encoding="utf-8")
    js = (ASSETS / "app.js").read_text(encoding="utf-8")
    blob = json.dumps(data, ensure_ascii=True, separators=(",", ":")).replace("</", "<\\/")

    page = (
        shell.replace("/*__FONTS__*/", font_face_css())
        .replace("/*__STYLE__*/", css)
        .replace("/*__SCRIPT__*/", js)
        .replace("__DATA__", blob)
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")

    size = OUT.stat().st_size
    print(
        f"wrote {OUT.relative_to(ROOT)} — {len(notes)} notes, "
        f"{data['stats']['words']:,} words, {size / 1_048_576:.2f} MB"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
