#!/usr/bin/env python3
"""resolve-cites.py — one-time deterministic citation normalizer (supervised).

Retires the legacy inline cite forms so the fleet never meets them:

  (D5DR7Kx42_A)          bare id in parens        -> (`D5DR7Kx42_A`)
  (8/3/22)               bare M/D/YY date         -> (`<resolved id>`)
  (8/17, 8/31/22)        date list sharing a year -> (`id1`, `id2`)

Date resolution: candidate ids = the note's front-matter `sources` list.
A dated report title ("... FISHING REPORT 10/12/2022") is matched EXACTLY
and wins outright — a bare cite names the report's own date, not the day
it was uploaded, and the two differ by up to 8 days in this corpus. Only
when no candidate carries a title date does it fall back to matching
manifest `upload_date` within [date, date+2 days] (report lag). A
unique hit rewrites; zero or ambiguous hits leave the original text and
append ` ⚠ cite-unresolved` beside it plus a row in
sources/fact-check-ledger.md. Code spans/fences are never touched.

Run ONCE in a supervised session (guard-protected scripts/ path). Idempotent:
a second run changes nothing.

Usage: resolve-cites.py [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST = ROOT / "sources" / "transcripts" / "_manifest.csv"
LEDGER = ROOT / "sources" / "fact-check-ledger.md"

FOLDERS = ["species", "techniques", "lures", "rigging", "conditions",
           "seasonal", "bait", "locations", "planning", "fish-care", "tackle"]

FM_SOURCES_RE = re.compile(r"^sources:\s*\[(.*?)\]", re.M | re.S)
BARE_ID_RE = re.compile(r"\((?!`)([A-Za-z0-9_-]{11})\)")
# (8/3/22) or (8/17, 8/31/22) — entries M/D or M/D/YY, at least one with a year
DATE_LIST_RE = re.compile(
    r"\((\d{1,2}/\d{1,2}(?:/\d{2})?(?:,\s*\d{1,2}/\d{1,2}(?:/\d{2})?)*)\)")
FLAG = "⚠ cite-unresolved"


def plausible_id(tok: str, manifest: dict | None = None) -> bool:
    """Is this 11-char token a video id rather than ordinary prose?

    Shape alone is not enough: `speed-troll` and `Baja-scoped` are both
    exactly 11 characters with a hyphen and would pass any character
    heuristic. A bare-id cite names a real video, so the manifest is the
    test; the old heuristic is kept only as a fallback when no manifest
    is passed.
    """
    if manifest is not None:
        return tok in manifest
    return bool(re.search(r"[0-9_-]", tok)
                or (tok != tok.lower() and tok != tok.upper()))


# A report titled with its own date — "Southern California Bight FISHING
# REPORT 10/12/2022". The upload trails the report by 0-8 days in this
# corpus, so the title is the authority for what a bare cite names.
TITLE_DATE_RE = re.compile(r"REPORT\s+(\d{1,2})/(\d{1,2})/(\d{2,4})", re.I)


def title_date(title: str) -> dt.date | None:
    m = TITLE_DATE_RE.search(title or "")
    if not m:
        return None
    mth, day, yr = (int(g) for g in m.groups())
    if yr < 100:
        yr += 2000
    try:
        return dt.date(yr, mth, day)
    except ValueError:
        return None


def load_manifest() -> dict[str, tuple[str, dt.date | None]]:
    """video_id -> (upload_date, date parsed out of a dated report title)."""
    dates: dict[str, tuple[str, dt.date | None]] = {}
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vid = (row.get("video_id") or "").strip()
            up = (row.get("upload_date") or "").strip()
            if vid and up:
                dates[vid] = (up, title_date(row.get("title") or ""))
    return dates


def note_sources(text: str) -> list[str]:
    m = FM_SOURCES_RE.search(text)
    if not m:
        return []
    out = []
    for tok in m.group(1).replace("\n", " ").split(","):
        tok = tok.split("#", 1)[0].strip().strip("'\"")
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", tok):
            out.append(tok)
    return out


def protected_spans(text: str) -> list[tuple[int, int]]:
    spans = []
    for m in re.finditer(r"^(```|~~~).*?^\1\s*$", text, re.M | re.S):
        spans.append(m.span())
    for m in re.finditer(r"`[^`\n]*`", text):
        spans.append(m.span())
    return spans


def in_spans(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(a <= pos < b for a, b in spans)


def resolve_date(date_str: str, sources: list[str],
                 manifest: dict[str, tuple[str, dt.date | None]],
                 year_hint: str | None) -> list[str]:
    """Candidate ids for a bare date, title date first.

    A candidate whose report TITLE carries this exact date wins outright:
    that is the report the cite names. Only if none does do we fall back
    to the upload-date window, which both misses long report->upload lags
    and goes ambiguous when two of a note's sources upload the same day.
    """
    parts = date_str.split("/")
    if len(parts) == 2:
        if not year_hint:
            return []
        mth, day, yr = parts[0], parts[1], year_hint
    else:
        mth, day, yr = parts
    try:
        d0 = dt.date(2000 + int(yr), int(mth), int(day))
    except ValueError:
        return []
    exact = [vid for vid in sources
             if manifest.get(vid, ("", None))[1] == d0]
    if exact:
        return exact
    hits = []
    for vid in sources:
        up = manifest.get(vid, ("", None))[0]
        try:
            du = dt.date(int(up[0:4]), int(up[5:7]), int(up[8:10]))
        except (ValueError, IndexError):
            continue
        if dt.timedelta(0) <= du - d0 <= dt.timedelta(days=2):
            hits.append(vid)
    return hits


def ledger_row(note: str, original: str, detail: str, dry: bool) -> None:
    if dry:
        return
    line = (f"| {note} | {original} | cite-unresolved | — | {detail} |\n")
    text = LEDGER.read_text(encoding="utf-8")
    marker = "<!-- review:ledger:end -->"
    LEDGER.write_text(text.replace(marker, line + marker), encoding="utf-8")


def process(path: Path, manifest: dict[str, tuple[str, dt.date | None]],
            dry: bool) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    sources = note_sources(text)
    rel = str(path.relative_to(ROOT))
    resolved = unresolved = 0
    out = []
    last = 0
    spans = protected_spans(text)

    events: list[tuple[int, int, str]] = []  # (start, end, replacement)

    for m in BARE_ID_RE.finditer(text):
        if in_spans(m.start(), spans) \
                or not plausible_id(m.group(1), manifest):
            continue
        events.append((m.start(), m.end(), f"(`{m.group(1)}`)"))

    for m in DATE_LIST_RE.finditer(text):
        if in_spans(m.start(), spans):
            continue
        entries = [e.strip() for e in m.group(1).split(",")]
        # Plausibility gate: spec numbers like (25/40/80), (1/0), (35/55) are
        # line-class ratings, not dates. Every entry must be a real M/D(/YY)
        # and at least one must carry a year, or this paren is NOT a cite.
        def _plausible_date(e: str) -> bool:
            parts = e.split("/")
            if len(parts) not in (2, 3):
                return False
            try:
                mth, day = int(parts[0]), int(parts[1])
            except ValueError:
                return False
            return 1 <= mth <= 12 and 1 <= day <= 31
        if not all(_plausible_date(e) for e in entries) \
                or not any(len(e.split("/")) == 3 for e in entries):
            continue
        year_hint = next((e.split("/")[2] for e in reversed(entries)
                          if len(e.split("/")) == 3), None)
        ids: list[str] = []
        ok = True
        for e in entries:
            hits = resolve_date(e, sources, manifest, year_hint)
            if len(hits) == 1:
                ids.append(hits[0])
            else:
                ok = False
                break
        if ok and ids:
            rep = "(" + ", ".join(f"`{i}`" for i in ids) + ")"
            # A date that resolves NOW may carry a stale flag from a run
            # under the old matcher — swallow it so the note is clean.
            end = m.end()
            tail = text[end:end + len(FLAG) + 1]
            if tail.startswith(" " + FLAG):
                end += len(FLAG) + 1
            elif tail.startswith(FLAG):
                end += len(FLAG)
            events.append((m.start(), end, rep))
        else:
            if FLAG in text[m.end():m.end() + 40]:
                continue  # already flagged on a prior run
            events.append((m.start(), m.end(),
                           f"{m.group(0)} {FLAG}"))
            ledger_row(rel, m.group(0),
                       "zero/ambiguous manifest matches among the note's "
                       "sources", dry)

    for start, end, rep in sorted(events):
        out.append(text[last:start])
        out.append(rep)
        if rep.endswith(FLAG):
            unresolved += 1
        else:
            resolved += 1
        last = end
    out.append(text[last:])
    new = "".join(out)
    if new != text and not dry:
        path.write_text(new, encoding="utf-8")
    return resolved, unresolved


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    manifest = load_manifest()
    total_r = total_u = files = 0
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).rglob("*.md")):
            if path.name == "README.md":
                continue
            r, u = process(path, manifest, args.dry_run)
            if r or u:
                files += 1
                print(f"{path.relative_to(ROOT)}: {r} resolved, {u} flagged")
            total_r += r
            total_u += u
    print(f"resolve-cites{' (dry run)' if args.dry_run else ''}: "
          f"{total_r} resolved, {total_u} flagged across {files} notes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
