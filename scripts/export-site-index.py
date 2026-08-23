#!/usr/bin/env python3
"""export-site-index.py — emit the machine-readable site manifest (index.json).

Consumed by the BightSST website's knowledge sync (and any future MCP). This
script is the SINGLE SOURCE OF TRUTH for which KB folders are published on the
site: downstream consumers vendor exactly the folders this manifest lists and
generate their routes from its records — adding or renaming a published folder
is a one-line edit to SITE_FOLDERS here, with zero changes on the site side.

    python scripts/export-site-index.py [--root PATH] [--out PATH]

Reuses link-maintenance.py's helpers (title_of, summary_of, strip_front_matter,
parse_links) so index semantics can never drift from KB link semantics. Run
link-maintenance.py FIRST — this script assumes a link-clean tree.

Hard-fails (nonzero exit, no output) when the tree violates the publishing
contract: a listed folder is missing, a note lacks the four required
front-matter keys, or a nested subdirectory appears inside a published folder
(routes are exactly folder/note deep — restructure deliberately, then extend
this script and the site's routes together). Exception: `evidence/` subdirs
(the per-note provenance layer, templates/evidence.md) are skipped — they are
deliberately unpublished.

Output is deterministic for a given tree + HEAD: notes sorted by path, stable
key order. Only `synced_at` varies between runs on the same commit.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# The publishing contract: KB folders that appear on the website, in display
# order. Personal data (profiles/), raw sources (sources/), and repo internals
# (skills/, scripts/, prompts/, config/, tests/) are NEVER listed here.
SITE_FOLDERS = [
    "species",
    "techniques",
    "lures",
    "rigging",
    "bait",
    "tackle",
    "conditions",
    "seasonal",
    "locations",
    "planning",
    "fish-care",
]

REQUIRED_KEYS = ("type", "tags", "sources", "confidence")
SCHEMA_VERSION = 1

INDEX_START = "<!-- index:start -->"
MERMAID_START = "<!-- mermaid:start -->"
MERMAID_END = "<!-- mermaid:end -->"

_KEY_RE = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$")


def load_link_maintenance(script_dir: Path):
    """Import the hyphenated sibling module so helpers are shared, not copied."""
    path = script_dir / "link-maintenance.py"
    spec = importlib.util.spec_from_file_location("link_maintenance", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parse_front_matter(text: str, rel: str) -> dict:
    """Parse the KB's YAML subset: scalar values and one-line-or-wrapped flow
    lists ([a, b, c]). Unknown keys are preserved; missing required keys are a
    contract violation reported by the caller."""
    if not text.startswith("---\n"):
        raise ValueError(f"{rel}: no front matter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{rel}: unterminated front matter")
    block = text[4:end]

    # Join wrapped flow-list continuations onto their key line.
    lines: list[str] = []
    for raw in block.splitlines():
        if lines and not _KEY_RE.match(raw):
            lines[-1] += " " + raw.strip()
        else:
            lines.append(raw.rstrip())

    out: dict = {}
    for line in lines:
        m = _KEY_RE.match(line)
        if not m:
            continue  # comment or stray line — tolerate
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(",")]
            out[key] = [v for v in items if v]
        else:
            out[key] = val.split("#", 1)[0].strip().strip("'\"") if val else ""
    return out


def load_video_manifest(root: Path) -> dict[str, dict]:
    """video_id -> {title, channel, upload_date} from the transcript manifest.
    The manifest lives under sources/ (never published); it is read here only
    to label source attributions with human-readable titles."""
    path = root / "sources" / "transcripts" / "_manifest.csv"
    videos: dict[str, dict] = {}
    if not path.exists():
        return videos
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vid = (row.get("video_id") or "").strip()
            if vid:
                videos[vid] = {
                    "title": (row.get("title") or "").strip(),
                    "channel": (row.get("channel") or "").strip(),
                    "date": (row.get("upload_date") or "").strip(),
                }
    return videos


def folder_intro(readme: Path) -> str:
    """Curated prose above the generated index block, minus the H1 and any
    mermaid block. Empty string when the README is index-only."""
    if not readme.exists():
        return ""
    text = readme.read_text(encoding="utf-8")
    if INDEX_START in text:
        text = text.split(INDEX_START, 1)[0]
    if MERMAID_START in text and MERMAID_END in text:
        pre, rest = text.split(MERMAID_START, 1)
        text = pre + rest.split(MERMAID_END, 1)[1]
    lines = [ln for ln in text.splitlines() if not ln.startswith("# ")]
    return "\n".join(lines).strip()


def git_head_sha(root: Path) -> str:
    try:
        return (
            subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=script_dir.parent)
    ap.add_argument("--out", type=Path, default=None, help="default: stdout")
    args = ap.parse_args()
    root = args.root.resolve()

    lm = load_link_maintenance(script_dir)
    videos = load_video_manifest(root)

    errors: list[str] = []
    notes: list[dict] = []
    folders: dict[str, dict] = {}
    note_paths: set[Path] = set()

    for folder in SITE_FOLDERS:
        fdir = root / folder
        if not fdir.is_dir():
            errors.append(
                f"{folder}/: listed in SITE_FOLDERS but missing — if the KB "
                "was restructured, update SITE_FOLDERS to match"
            )
            continue
        for sub in sorted(p for p in fdir.iterdir() if p.is_dir()):
            if sub.name == "evidence":
                # The provenance layer from the 2026-08 editorial review
                # (templates/evidence.md): per-note trip reports + source
                # detail. Deliberately NOT published — site routes stay
                # folder/note deep; an evidence route is a separate project.
                continue
            errors.append(
                f"{folder}/{sub.name}/: nested directories are not part of the "
                "site's folder/note route contract — extend export-site-index.py "
                "and the site routes together before nesting content"
            )
        readme = fdir / "README.md"
        folders[folder] = {
            "title": lm.title_of(readme) if readme.exists() else folder.replace("-", " ").title(),
            "intro_md": folder_intro(readme),
            "count": 0,
        }
        for md in sorted(fdir.glob("*.md")):
            if md.name == "README.md":
                continue
            note_paths.add(md.resolve())

    for path in sorted(note_paths):
        rel = path.relative_to(root).as_posix()
        folder = path.parent.name
        text = path.read_text(encoding="utf-8")
        try:
            fm = parse_front_matter(text, rel)
        except ValueError as e:
            errors.append(str(e))
            continue
        missing = [k for k in REQUIRED_KEYS if k not in fm]
        if missing:
            errors.append(f"{rel}: missing front-matter key(s): {', '.join(missing)}")
            continue

        sources = []
        raw_sources = fm["sources"] if isinstance(fm["sources"], list) else [fm["sources"]]
        for sid in raw_sources:
            entry = {"id": sid}
            if sid in videos:
                entry.update(videos[sid])
            sources.append(entry)

        tags = fm["tags"] if isinstance(fm["tags"], list) else [fm["tags"]]
        extra = {k: v for k, v in fm.items() if k not in REQUIRED_KEYS}

        record = {
            "path": rel,
            "folder": folder,
            "slug": path.stem,
            "title": lm.title_of(path),
            "summary": lm.summary_of(path),
            "type": fm["type"],
            "tags": tags,
            "confidence": fm["confidence"],
            "sources": sources,
            "linked_from": [],
        }
        if extra:
            record["extra"] = extra
        notes.append(record)
        folders[folder]["count"] += 1

    if errors:
        print("SITE EXPORT CONTRACT VIOLATIONS:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        print(f"\n{len(errors)} violation(s). Nothing was written.", file=sys.stderr)
        return 1

    # Inbound-link graph restricted to published notes (both endpoints).
    by_path = {n["path"]: n for n in notes}
    inbound: dict[str, set[str]] = {p: set() for p in by_path}
    for n in notes:
        src = root / n["path"]
        for _text, file_part, _raw in lm.parse_links(src):
            target = (src.parent / file_part).resolve()
            try:
                trel = target.relative_to(root).as_posix()
            except ValueError:
                continue
            if trel in inbound and trel != n["path"]:
                inbound[trel].add(n["path"])
    for p, srcs in inbound.items():
        by_path[p]["linked_from"] = sorted(srcs)

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "kb_repo": "camchuckpete-max/Socal-Fishing-Knowledge",
        "kb_sha": git_head_sha(root),
        "synced_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note_count": len(notes),
        "folders": folders,
        "notes": notes,
    }
    payload = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
        print(
            f"OK: {len(notes)} notes across {len(folders)} folders -> {args.out}",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
