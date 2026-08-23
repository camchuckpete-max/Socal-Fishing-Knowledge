#!/usr/bin/env python3
"""link-maintenance.py — the hard-habit maintenance pass for the KB.

Run before EVERY commit:

    python scripts/link-maintenance.py

It does four things:
  (a) validates every relative markdown link resolves — EXITS NONZERO on any
      dead link, WITHOUT writing anything (no partial regeneration). Links
      inside fenced code blocks and inline code spans are ignored everywhere
      (validation, backlinks, mermaid); `tests/link-fixture.md` exercises this
      and must always pass. Region gating (a2) and the v2 layout contract
      (a3 — section skeletons, infobox fields, evidence pairing, per
      scripts/note_schema.py; opt-in via front-matter `layout: v2`) validate
      under the same all-or-nothing rule;
  (b) regenerates each note's `## Linked from` backlinks section idempotently
      between <!-- backlinks:start --> / <!-- backlinks:end --> markers;
  (c) regenerates each directory's README.md index between
      <!-- index:start --> / <!-- index:end --> markers (curated prose outside
      the markers is preserved);
  (d) writes a capped Mermaid map of a branch's intra-folder note connections
      between <!-- mermaid:start --> / <!-- mermaid:end --> markers on each
      branch README (skipped, with a note, if the branch exceeds the node cap).

The script is deterministic: a second run with no editorial changes produces no
diff.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MERMAID_NODE_CAP = 30

sys.path.insert(0, str(Path(__file__).resolve().parent))
import note_schema  # noqa: E402  (same directory; the v2 layout schema)

# Files never processed at all (raw inputs + top-level spec doc).
EXCLUDE_FULL = {
    ROOT / "CLAUDE.md",
    ROOT / "sources" / "memory-export.md",
    ROOT / "sources" / "bd-transcript-knowledge-proposal.md",
    ROOT / "sources" / "spot-lists.md",
    # Batch-2 ingestion: raw input doc (committed verbatim — must never gain
    # a backlinks block) and the pipeline's mechanical append-only files.
    ROOT / "sources" / "batch-2-analysis.md",
    ROOT / "sources" / "escalations.md",
    ROOT / "sources" / "batch-2-progress.md",
}
# Files whose links ARE validated but which are not notes: no backlinks block,
# not indexed, not a backlink source (e.g. the hand-authored skill definition).
VALIDATE_ONLY = {
    ROOT / "skills" / "boat-day" / "SKILL.md",
    # The distributed skill's source of record. These are the files that get
    # packaged and handed to another angler, so they are committed here to be
    # diffable against whatever someone actually has installed. They are not
    # KB notes: no backlinks block, not indexed, never a backlink source.
    ROOT / "skills" / "socal-boat-day" / "SKILL.md",
    ROOT / "skills" / "socal-boat-day" / "references" / "offline-fallback.md",
    ROOT / "skills" / "socal-boat-day" / "references" / "setup.md",
    ROOT / "skills" / "socal-boat-day" / "references" / "tackle-onboarding.md",
}
# Directories whose markdown is validated for links but which are spec, not
# notes: no backlinks block, not indexed, never a backlink source, README
# hand-authored. The layout spec lives here — see templates/README.md.
VALIDATE_ONLY_DIRS = {
    ROOT / "templates",
}
# Notes that are indexed and validated normally but never receive a generated
# backlinks block. The registry is a trust table every note may legitimately
# link to ("<voice> is a registered voice"); regenerating a block inside it made
# each such extraction touch a guard-protected path, which reverted three
# otherwise-clean batch-2 extractions. Keep it indexed — just never write to it.
NO_BACKLINKS = {
    ROOT / "sources" / "source-registry.md",
}
# Directories whose markdown is raw or generated and never linked into the graph.
EXCLUDE_DIRS = {
    ROOT / ".git",
    ROOT / "sources" / "transcripts",
    ROOT / "skills" / "boat-day" / "resources",  # generated skill bundle
}

# --- region gating (see locations/regions.md) --------------------------------
# Closed vocabularies. A day plan filters species/technique notes by the trip's
# {regions, waters} envelope before routing, so a missing or mistyped value is a
# correctness bug, not a style nit — it is what let a Mission Bay plan reach a
# Sea-of-Cortez-only species. Adding a term means editing locations/regions.md.
REGIONS = {
    "socal-bight",          # Point Conception to the US border
    "baja-pacific-north",   # US border to the BC/BCS line at 28N
    "baja-pacific-south",   # 28N round to Cabo San Lucas
    "cortez-north",         # Sea of Cortez above 28N (San Felipe, BOLA, Midriff)
    "cortez-south",         # Sea of Cortez below 28N (Loreto, La Paz, East Cape)
}
WATERS = {"bay-harbor", "nearshore-coast", "island", "bank", "open-ocean"}
GATED_TYPES = {"species", "technique", "lure", "rig", "location", "seasonal",
               "bait", "decision"}
FM_LIST_RE = re.compile(r"^(regions|subregions|waters): \[(.*?)\]\s*(?:#.*)?$",
                        re.M)
FM_TYPE_RE = re.compile(r"^type:\s*(\S+)", re.M)

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
H1_RE = re.compile(r"^#\s+(.*?)\s*$", re.MULTILINE)

BACKLINK_START = "<!-- backlinks:start -->"
BACKLINK_END = "<!-- backlinks:end -->"
INDEX_START = "<!-- index:start -->"
INDEX_END = "<!-- index:end -->"
MERMAID_START = "<!-- mermaid:start -->"
MERMAID_END = "<!-- mermaid:end -->"


def is_excluded(path: Path) -> bool:
    if path in EXCLUDE_FULL:
        return True
    for d in EXCLUDE_DIRS:
        if d in path.parents:
            return True
    return False


def is_validate_only(path: Path) -> bool:
    if path in VALIDATE_ONLY:
        return True
    return any(d in path.parents for d in VALIDATE_ONLY_DIRS)


def all_markdown() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        if is_excluded(p):
            continue
        out.append(p)
    return sorted(out)


def title_of(path: Path) -> str:
    """First H1, else a title-cased filename."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return path.stem
    m = H1_RE.search(strip_front_matter(text))
    if m:
        return m.group(1).strip()
    return path.stem.replace("-", " ").title()


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            nl = text.find("\n", end + 1)
            return text[nl + 1 :] if nl != -1 else ""
    return text


def summary_of(path: Path) -> str:
    """First real paragraph (lines joined), trimmed to one sentence-ish."""
    text = strip_front_matter(path.read_text(encoding="utf-8"))
    para: list[str] = []
    for line in text.splitlines():
        s = line.strip()
        # NB: bullet markers are "- " / "* " WITH the trailing space. Testing a
        # bare "*" also swallowed a "**Bold lead:** ..." opening line, which is
        # how several notes state the thing that most needs to reach the index —
        # the region on species/cabrilla.md, the regime on every seasonal note,
        # the flagged-stub warning on techniques/bait-and-switch.md. A lone "-"
        # or "*" on its own line is a thematic break, still skipped.
        skip = (
            not s
            or s.startswith("#")
            or s.startswith("<!--")
            or s.startswith(">")
            or s.startswith("|")
            or s.startswith("- ")
            or s.startswith("* ")
            or s in ("-", "*", "---", "***")
            or s.startswith("```")
        )
        if para and (not s or skip):
            break  # end of the first paragraph
        if skip:
            continue
        para.append(s)
    if not para:
        return ""
    joined = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", " ".join(para))  # strip links
    joined = re.sub(r"\*\*|`", "", joined)  # drop bold/code marks
    m = re.match(r"(.{0,160}?[.!?])(\s|$)", joined)
    return (m.group(1) if m else joined[:160]).strip()


FENCE_RE = re.compile(r"^(```|~~~).*?^\1\s*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans so link-looking text
    inside code is never parsed as a link (validation, backlinks, mermaid)."""
    text = FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def region_problems(path: Path) -> list[str]:
    """Validate the region-gating front matter on a gated note.

    Returns a list of human-readable problems (empty = fine). A note whose
    `type` is not gated is skipped entirely.
    """
    text = path.read_text(encoding="utf-8")
    m = FM_TYPE_RE.search(text)
    if not m or m.group(1) not in GATED_TYPES:
        return []
    found = {k: [x.strip() for x in v.split(",") if x.strip()]
             for k, v in FM_LIST_RE.findall(text)}
    problems = []
    if "subregions" in found:
        problems.append(
            "`subregions:` is retired — assignment is at region level only; "
            "fold the value into `regions`")
    for key, vocab in (("regions", REGIONS), ("waters", WATERS)):
        vals = found.get(key)
        if vals is None:
            problems.append(f"missing `{key}:` (type {m.group(1)})")
            continue
        if not vals:
            problems.append(f"`{key}:` is empty")
        for v in vals:
            if v not in vocab:
                problems.append(
                    f"`{key}:` has off-vocabulary term {v!r} "
                    f"(allowed: {', '.join(sorted(vocab))})")
    return problems


def region_badge(path: Path) -> str:
    """A short region marker for the generated index line, or "".

    Generated from front matter, so it cannot drift from the gate and cannot
    be silently dropped the way the prose region line was. Only marks the
    cases a planner can get wrong — a note covering both regions needs no
    badge, a Baja-only one very much does.
    """
    text = path.read_text(encoding="utf-8")
    m = FM_TYPE_RE.search(text)
    if not m or m.group(1) not in GATED_TYPES:
        return ""
    found = dict(FM_LIST_RE.findall(text))
    regions = {x.strip() for x in found.get("regions", "").split(",") if x.strip()}
    if not regions:
        return ""
    if regions == {"socal-bight"}:
        return " **[SoCal only]**"
    if "socal-bight" not in regions:
        return " **[Baja only]**"
    return ""


def layout_problems(path: Path) -> list[str]:
    """Validate the v2 layout contract (see templates/ + scripts/note_schema.py).

    Applies ONLY to notes carrying `layout: v2` in front matter, plus every
    `type: evidence` file — notes not yet migrated by the editorial review are
    untouched, so the tree stays green mid-migration. Checks: required-section
    presence and relative order, per-type infobox fields, path-valued front
    matter resolving (`parent`, `parent_zone`), and evidence pairing in both
    directions.
    """
    text = path.read_text(encoding="utf-8")
    m = FM_TYPE_RE.search(text)
    ntype = m.group(1) if m else ""
    is_v2 = note_schema.layout_of(text) == note_schema.LAYOUT_CURRENT
    if ntype != "evidence" and not is_v2:
        return []
    problems = note_schema.infobox_problems(ntype, text)
    for key in note_schema.PATH_FIELDS:
        val = note_schema.fm_value(text, key)
        if val and val != "unknown":
            if not (path.parent / val).resolve().exists():
                problems.append(f"front-matter `{key}: {val}` does not resolve")
    if ntype == "evidence":
        if path.parent.name != "evidence":
            problems.append("`type: evidence` outside an evidence/ directory")
        parent_val = note_schema.fm_value(text, "parent")
        if parent_val:
            parent_path = (path.parent / parent_val).resolve()
            if (parent_path.exists()
                    and f"evidence/{path.name}"
                    not in parent_path.read_text(encoding="utf-8")):
                problems.append(
                    f"parent note {parent_val} does not link this evidence file")
    else:
        problems += note_schema.section_problems(
            ntype, strip_code(strip_front_matter(text)))
        ev = path.parent / "evidence" / path.name
        if ev.exists():
            if not re.search(r"^## Evidence\b", text, re.M):
                problems.append(
                    "has an evidence file but no `## Evidence` section")
            elif f"evidence/{path.name}" not in text:
                problems.append(
                    f"`## Evidence` section does not link evidence/{path.name}")
    return problems


def strip_backlinks_block(text: str) -> str:
    """Remove the generated '## Linked from' block.

    Its entries are links to the notes that link *here* — the reverse of an
    outbound reference. Parsing them as outbound made every backlink breed a
    reciprocal one: 557 of 1729 backlink entries (32%) existed only for that
    reason, and the resulting writes into guard-protected paths reverted four
    otherwise-clean batch-2 extractions. Validation still covers these links,
    because the block is regenerated from real links and never hand-edited.
    """
    si, ei = text.find(BACKLINK_START), text.find(BACKLINK_END)
    if si != -1 and ei != -1 and ei > si:
        return text[:si] + text[ei + len(BACKLINK_END):]
    return text


def parse_links(path: Path):
    """Yield (link_text, file_part, raw_target) for each relative link.
    Code blocks, inline code spans, and the generated backlinks block are
    stripped first."""
    text = strip_backlinks_block(strip_code(path.read_text(encoding="utf-8")))
    for m in LINK_RE.finditer(text):
        text_part, target = m.group(1), m.group(2).strip()
        # strip optional title:  path "Title"
        target = target.split(" ", 1)[0].strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        file_part = target.split("#", 1)[0]
        if not file_part:
            continue
        yield text_part, file_part, target


def replace_block(text: str, start: str, end: str, body: str, where: str = "") -> str:
    """Replace content between start/end markers (inclusive) with markers+body.
    Appends a fresh block at EOF if the markers are absent. Raises if the end
    marker precedes the start marker (a malformed file must not be rewritten)."""
    block = f"{start}\n{body}\n{end}"
    if start in text and end in text:
        si, ei = text.index(start), text.index(end)
        if ei < si:
            raise ValueError(
                f"{where or '<text>'}: end marker {end!r} precedes start "
                f"marker {start!r} — fix the markers by hand"
            )
        pre = text[:si]
        post = text[ei + len(end) :]
        return pre + block + post
    sep = "" if text.endswith("\n\n") else ("\n" if text.endswith("\n") else "\n\n")
    return text + sep + "\n" + block + "\n"


def main() -> int:
    md_files = all_markdown()
    extraction_log = ROOT / "sources" / "extraction-log.md"
    note_files = [
        p
        for p in md_files
        if p.name != "README.md" and p != extraction_log and not is_validate_only(p)
    ]

    # ---- (a) validate links FIRST + build note->note graph ----
    # On any dead link: report and exit 1 with ZERO writes — a failing run must
    # not leave partially regenerated backlinks or indexes behind.
    dead: list[str] = []
    inbound: dict[Path, set[Path]] = {p: set() for p in note_files}
    for src in md_files:
        for _text, file_part, raw in parse_links(src):
            target = (src.parent / file_part).resolve()
            if not target.exists():
                dead.append(f"{src.relative_to(ROOT)} -> {raw}")
                continue
            # record editorial note->note backlinks (README/log excluded as source)
            if (
                src in note_files
                and target in inbound
                and target != src
            ):
                inbound[target].add(src)

    # ---- (a2) validate region gating on every note, same all-or-nothing rule ----
    region_bad: list[str] = []
    for n in note_files:
        for prob in region_problems(n):
            region_bad.append(f"{n.relative_to(ROOT)}: {prob}")
    if region_bad:
        print("REGION GATING:", file=sys.stderr)
        for r_ in sorted(set(region_bad)):
            print(f"  {r_}", file=sys.stderr)
        print(
            f"\n{len(set(region_bad))} region-gating problem(s). Nothing was "
            f"written. See locations/regions.md for the vocabulary.",
            file=sys.stderr)
        return 1

    # ---- (a3) validate the v2 layout contract, same all-or-nothing rule ----
    layout_bad: list[str] = []
    for n in note_files:
        for prob in layout_problems(n):
            layout_bad.append(f"{n.relative_to(ROOT)}: {prob}")
    if layout_bad:
        print("LAYOUT (v2):", file=sys.stderr)
        for l_ in sorted(set(layout_bad)):
            print(f"  {l_}", file=sys.stderr)
        print(
            f"\n{len(set(layout_bad))} layout problem(s). Nothing was written. "
            f"See templates/ for the per-type skeletons.",
            file=sys.stderr)
        return 1

    if dead:
        print("DEAD LINKS:", file=sys.stderr)
        for d_ in sorted(set(dead)):
            print(f"  {d_}", file=sys.stderr)
        print(
            f"\n{len(set(dead))} dead link(s). Nothing was written.",
            file=sys.stderr,
        )
        return 1

    # ---- (b) regenerate backlinks on every note ----
    for note in note_files:
        if note in NO_BACKLINKS:
            continue
        srcs = sorted(inbound[note], key=lambda p: title_of(p).lower())
        if srcs:
            lines = ["## Linked from", ""]
            for s in srcs:
                rel = os.path.relpath(s, note.parent)
                lines.append(f"- [{title_of(s)}]({rel})")
            body = "\n".join(lines)
        else:
            body = "## Linked from\n\n_Nothing links here yet._"
        text = note.read_text(encoding="utf-8")
        new = replace_block(
            text, BACKLINK_START, BACKLINK_END, body, where=str(note.relative_to(ROOT))
        )
        if new != text:
            note.write_text(new, encoding="utf-8")

    # ---- (c)+(d) directory READMEs: index + mermaid ----
    # group notes by directory
    dirs = sorted({p.parent for p in note_files})
    # Notes-free parent branch folders (e.g. profiles/, skills/) still get an
    # index README listing their indexed children — walk up from note dirs and
    # from hand-maintained README dirs to just below ROOT.
    parent_dirs: set[Path] = set()
    seed_dirs = set(dirs) | {
        p.parent for p in md_files if p.name == "README.md" and p.parent != ROOT
    }
    for d in seed_dirs:
        cur = d.parent
        while cur != ROOT and cur not in dirs:
            parent_dirs.add(cur)
            cur = cur.parent
    for d in dirs:
        readme = d / "README.md"
        dir_notes = sorted(
            [p for p in note_files if p.parent == d], key=lambda p: p.name
        )
        subdirs = sorted(
            {p.parent for p in note_files if d in p.parents and p.parent != d}
        )
        # direct child subdirs only
        child_dirs = sorted({sd for sd in subdirs if sd.parent == d})

        # index body
        idx = ["## Index", ""]
        for n in dir_notes:
            summ = summary_of(n)
            tail = f" — {summ}" if summ else ""
            idx.append(f"- [{title_of(n)}]({n.name}){region_badge(n)}{tail}")
        if child_dirs:
            idx.append("")
            idx.append("### Subfolders")
            for cd in child_dirs:
                idx.append(f"- [{cd.name}/]({cd.name}/README.md)")
        index_body = "\n".join(idx)

        # mermaid body (intra-folder edges only)
        node_ids = {n: f"n{i}" for i, n in enumerate(dir_notes)}
        edges = []
        for n in dir_notes:
            for _t, file_part, _raw in parse_links(n):
                tgt = (n.parent / file_part).resolve()
                if tgt in node_ids and tgt != n:
                    edges.append((node_ids[n], node_ids[tgt]))
        edges = sorted(set(edges))
        if len(dir_notes) > MERMAID_NODE_CAP:
            mer_body = (
                f"## Map\n\n_Map skipped: {len(dir_notes)} notes exceed the "
                f"{MERMAID_NODE_CAP}-node cap._"
            )
        elif not edges:
            mer_body = "## Map\n\n_No intra-folder links yet._"
        else:
            lines = ["## Map", "", "```mermaid", "graph LR"]
            for n in dir_notes:
                label = title_of(n).replace('"', "'")
                lines.append(f'  {node_ids[n]}["{label}"]')
            for a, b in edges:
                lines.append(f"  {a} --> {b}")
            lines.append("```")
            mer_body = "\n".join(lines)

        if readme.exists():
            text = readme.read_text(encoding="utf-8")
        else:
            title = d.name.replace("-", " ").title() if d != ROOT else "Index"
            text = f"# {title}\n\n"
        rel = str(readme.relative_to(ROOT))
        text = replace_block(text, INDEX_START, INDEX_END, index_body, where=rel)
        text = replace_block(text, MERMAID_START, MERMAID_END, mer_body, where=rel)
        readme.write_text(text, encoding="utf-8")

    # notes-free parent branch folders: index of indexed children, no mermaid
    indexed = set(dirs) | parent_dirs
    for d in sorted(parent_dirs):
        readme = d / "README.md"
        children = sorted(
            c
            for c in d.iterdir()
            if c.is_dir()
            and (c in indexed or (c / "README.md").exists())
            and not is_excluded(c / "README.md")
        )
        idx = ["## Index", ""]
        for c in children:
            idx.append(f"- [{c.name}/]({c.name}/README.md)")
        if readme.exists():
            text = readme.read_text(encoding="utf-8")
        else:
            text = f"# {d.name.replace('-', ' ').title()}\n\n"
        text = replace_block(
            text,
            INDEX_START,
            INDEX_END,
            "\n".join(idx),
            where=str(readme.relative_to(ROOT)),
        )
        readme.write_text(text, encoding="utf-8")

    # ---- granularity watch ----
    # WARNS, never fails: an over-long note is a spin-out candidate, not a
    # broken one, and this runs before every commit including the unattended
    # chain's. The risk it watches for is an autonomous writer editing a note
    # too big to hold in view — it cannot find existing doctrine to reconcile
    # against, so a contradiction ends up sitting quietly beside it.
    NOTE_LINES, SECTION_LINES = 400, 120
    long_notes, long_sections = [], []
    for f in note_files:
        text = f.read_text(encoding="utf-8")
        tm = FM_TYPE_RE.search(text)
        if tm and tm.group(1) == "evidence":
            continue  # the provenance layer may legitimately run long
        lines = text.splitlines()
        if len(lines) > NOTE_LINES:
            long_notes.append((len(lines), str(f.relative_to(ROOT))))
        head, start = None, 0
        for i, line in enumerate(lines + ["## "]):
            if line.startswith("## "):
                if head and i - start > SECTION_LINES:
                    long_sections.append(
                        (i - start, str(f.relative_to(ROOT)), head.strip()))
                head, start = line, i
    if long_notes or long_sections:
        print(f"\nGRANULARITY WATCH (warning only — see CLAUDE.md)")
        for n, p in sorted(long_notes, reverse=True)[:6]:
            print(f"  note   {n:5d} lines  {p}")
        if len(long_notes) > 6:
            print(f"         … and {len(long_notes) - 6} more over {NOTE_LINES} lines")
        for n, p, h in sorted(long_sections, reverse=True)[:6]:
            print(f"  section{n:5d} lines  {p}  {h}")
        if len(long_sections) > 6:
            print(f"         … and {len(long_sections) - 6} more over "
                  f"{SECTION_LINES} lines")

    # ---- report ----
    print(
        f"OK: {len(note_files)} notes, {len(dirs) + len(parent_dirs)} indexes, "
        "0 dead links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
