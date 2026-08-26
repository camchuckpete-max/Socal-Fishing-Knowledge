#!/usr/bin/env python3
"""check-note.py <note-path> — per-note machine acceptance for the review.

Run against the WORKING TREE before commit (the wrapper calls it; the verify
agent runs it too). Checks, in order:

  1. v2 layout contract (sections, infobox, evidence pairing) via
     link-maintenance.layout_problems — FAIL on any problem.
  2. Conservation vs HEAD: every source id cited in the HEAD version of the
     note survives in the working-tree note + evidence pair; `**Observed**`
     blocks removed are matched by evidence entries added — FAIL.
  3. Legacy cite forms on a v2 note (bare `(M/D/YY)` dates) — FAIL.
  4. Cite coverage: a direct quote (>=15 chars between double quotes) in a
     paragraph with no cite — FAIL; a number+unit token in a paragraph with
     no cite — WARN only (prose like "a couple pounds of drag" is legal).

Exit 0 = pass (warnings allowed), 1 = failures printed.
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import note_schema  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import guard  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "lm", ROOT / "scripts" / "link-maintenance.py")
lm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lm)

_cspec = importlib.util.spec_from_file_location(
    "check_coordinates", Path(__file__).resolve().parent / "check-coordinates.py")
check_coordinates = importlib.util.module_from_spec(_cspec)
_cspec.loader.exec_module(check_coordinates)

QUOTE_RE = re.compile(r'"[^"\n]{15,}"')
NUMBER_UNIT_RE = re.compile(
    r"\b\d[\d.,/–-]*\s?(?:lb|lbs|oz|g\b|kt|knots?|ft|feet|fathoms?|°F|°|"
    r"degrees|yd|yards|miles?|nm\b|rpm|inch(?:es)?|\")")
CITE_MARK_RE = re.compile(r"\(`[A-Za-z0-9_-]{11}`|\(cameron\)|`[A-Za-z0-9_-]{11}`")


def head_version(rel: str) -> str:
    r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def paragraphs(body: str) -> list[str]:
    out, cur = [], []
    fenced = False
    for line in body.splitlines():
        if line.startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        if line.strip():
            cur.append(line)
        elif cur:
            out.append("\n".join(cur))
            cur = []
    if cur:
        out.append("\n".join(cur))
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    rel = sys.argv[1]
    path = ROOT / rel
    if not path.exists():
        print(f"check-note: {rel} does not exist")
        return 1
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    warnings: list[str] = []

    # 1. layout contract
    for p in lm.layout_problems(path):
        failures.append(f"layout: {p}")

    # 1b. every published position traces to the spot library.
    # A wrong waypoint on a fishing page is a real-world hazard, so this
    # fails the UNIT rather than waiting for the whole-tree sweep. Five zone
    # pages published a computed zone CENTROID as a charted position — one
    # even called it "the computed centre" and printed it anyway, another
    # attributed it to cameron, who never gave it. A centroid is an average
    # of member spots: not a mark, not a place, and not somewhere anyone
    # should steer.
    if rel.startswith("locations/"):
        for coord in check_coordinates.unsourced_in(text):
            failures.append(
                f"unsourced coordinate {coord} — a published position must be "
                f"copied from sources/spot-lists.md, never computed. A zone "
                f"centre is not a position: state the distance without it.")

    # 2. conservation vs HEAD
    before = head_version(rel)
    if before:
        ev_rel = guard.evidence_path(rel)
        ev_path = ROOT / ev_rel
        ev_before = head_version(ev_rel)
        ev_after = ev_path.read_text(encoding="utf-8") if ev_path.exists() else ""
        before_ids = guard.cited_ids(before)
        after_ids = guard.cited_ids(text) | guard.cited_ids(ev_after)
        lost = before_ids - after_ids
        if lost:
            failures.append(
                f"conservation: {len(lost)} cited source id(s) lost: "
                + ", ".join(sorted(lost)[:5])
                + (" …" if len(lost) > 5 else ""))
        obs_removed = max(0, len(guard.OBSERVED_RE.findall(before))
                          - len(guard.OBSERVED_RE.findall(text)))
        ev_added = max(0, len(guard.EVIDENCE_ENTRY_RE.findall(ev_after))
                       - len(guard.EVIDENCE_ENTRY_RE.findall(ev_before or "")))
        if obs_removed > ev_added:
            failures.append(
                f"conservation: {obs_removed} **Observed** block(s) removed "
                f"but only {ev_added} evidence entrie(s) added")

    # 3 + 4 only apply to migrated notes
    if note_schema.layout_of(text) == note_schema.LAYOUT_CURRENT:
        body = lm.strip_backlinks_block(lm.strip_front_matter(text))
        for m in note_schema.LEGACY_BARE_DATE_RE.finditer(lm.strip_code(body)):
            failures.append(f"legacy cite form: ({m.group(1)}) — resolve to a "
                            f"source id or flag cite-unresolved")
        for para in paragraphs(body):
            has_cite = bool(CITE_MARK_RE.search(para))
            if QUOTE_RE.search(para) and not has_cite:
                failures.append("uncited direct quote: "
                                + para.strip().splitlines()[0][:90])
            elif NUMBER_UNIT_RE.search(para) and not has_cite \
                    and "⚠" not in para and not para.lstrip().startswith("|"):
                warnings.append("uncited number: "
                                + para.strip().splitlines()[0][:90])

    for w in warnings[:10]:
        print(f"WARN  {rel}: {w}")
    if len(warnings) > 10:
        print(f"WARN  … and {len(warnings) - 10} more uncited-number warnings")
    for f_ in failures:
        print(f"FAIL  {rel}: {f_}")
    if failures:
        print(f"check-note: {len(failures)} failure(s), "
              f"{len(warnings)} warning(s)")
        return 1
    print(f"check-note OK: {rel} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
