#!/usr/bin/env python3
"""Date- and id-matching tests for scripts/review/resolve-cites.py.

Both cases below are real defects that reached the branch and together
account for every `cite-unresolved` row Cameron ever had to look at.

  1. Bare dates were matched against the manifest's `upload_date` inside a
     2-day window, but the BDOutdoors bight reports are TITLED with the
     report date and upload 0-8 days later. That put `(2/6/25)` outside the
     window entirely, and made `(10/12/22)` AMBIGUOUS against an unrelated
     video that happened to upload the same day — so a cite whose video was
     already in the note's own `sources` list was flagged for Cameron.

  2. `plausible_id()` took any 11-character token containing a hyphen for a
     video id. `(speed-troll)` and `(Baja-scoped)` are both exactly 11
     characters with a hyphen, and were rewritten into cites — inventing
     provenance out of ordinary prose.
"""
from __future__ import annotations

import datetime as dt
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "rc", ROOT / "scripts" / "review" / "resolve-cites.py")
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)

failures: list[str] = []


def check(label: str, got, want) -> None:
    if got != want:
        failures.append(f"{label}: got {got!r}, want {want!r}")


# video_id -> (upload_date, title)
FIXTURE = {
    # report 02/06/2025, uploaded EIGHT days later — outside any lag window
    "Kf5wk_TFgTc": ("2025-02-14", "Southern California Bight  FISHING REPORT  02/06/2025"),
    # report 10/12/2022, uploaded the next day
    "XLVUhV8DW64": ("2022-10-13", "Southern California Bight FISHING REPORT 10/12/2022"),
    # an unrelated video uploading ON 10/12 — the source of the old ambiguity
    "OEsW9K1IwpQ": ("2022-10-12", "Oceans and Climate Part 1"),
    # a report whose upload happens to equal its report date
    "OYOda6T3f-8": ("2022-10-20", "Southern California Bight FISHING REPORT 10/20/2022"),
}
MAN = {v: (u, rc.title_date(t)) for v, (u, t) in FIXTURE.items()}


def test_title_date_parses_two_and_four_digit_years() -> None:
    check("4-digit year", rc.title_date("BIGHT FISHING REPORT 10/12/2022"),
          dt.date(2022, 10, 12))
    check("2-digit year", rc.title_date("BIGHT FISHING REPORT 09/14/22"),
          dt.date(2022, 9, 14))
    check("double-space", rc.title_date("REPORT  02/06/2025"), dt.date(2025, 2, 6))
    check("no date in title", rc.title_date("Oceans and Climate Part 1"), None)
    check("not a report", rc.title_date("5 Tips Before You Go Offshore"), None)


def test_long_report_to_upload_lag_still_resolves() -> None:
    """The 8-day lag case: the old upload window missed this entirely."""
    check("(2/6/25)", rc.resolve_date("2/6/25", ["Kf5wk_TFgTc"], MAN, None),
          ["Kf5wk_TFgTc"])


def test_title_date_disambiguates_a_same_day_upload() -> None:
    """Two of the note's sources sit in the window; only one IS the report."""
    srcs = ["XLVUhV8DW64", "OEsW9K1IwpQ"]
    check("(10/12/22) unique", rc.resolve_date("10/12/22", srcs, MAN, None),
          ["XLVUhV8DW64"])


def test_upload_window_still_works_without_a_title_date() -> None:
    """Fallback intact: no candidate carries a title date, so window matching."""
    man = {"OEsW9K1IwpQ": ("2022-10-12", None)}
    check("window fallback", rc.resolve_date("10/12/22", ["OEsW9K1IwpQ"], man, None),
          ["OEsW9K1IwpQ"])
    check("outside window", rc.resolve_date("10/01/22", ["OEsW9K1IwpQ"], man, None), [])


def test_a_date_outside_the_notes_sources_stays_unresolved() -> None:
    """Candidates are the note's OWN sources — a manifest-wide match is not one."""
    check("not in sources", rc.resolve_date("10/20/22", ["XLVUhV8DW64"], MAN, None), [])


def test_prose_that_looks_like_a_video_id_is_not_a_cite() -> None:
    """Both are exactly 11 chars with a hyphen; neither is in the manifest."""
    for tok in ("speed-troll", "Baja-scoped"):
        check(f"({tok}) rejected", rc.plausible_id(tok, MAN), False)
    check("real id accepted", rc.plausible_id("XLVUhV8DW64", MAN), True)


def main() -> int:
    for fn in (test_title_date_parses_two_and_four_digit_years,
               test_long_report_to_upload_lag_still_resolves,
               test_title_date_disambiguates_a_same_day_upload,
               test_upload_window_still_works_without_a_title_date,
               test_a_date_outside_the_notes_sources_stays_unresolved,
               test_prose_that_looks_like_a_video_id_is_not_a_cite):
        fn()
    if failures:
        print(f"FAILED ({len(failures)}):", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("resolve-cites tests: 6 check groups OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
