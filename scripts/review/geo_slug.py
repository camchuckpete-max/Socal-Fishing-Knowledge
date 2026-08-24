#!/usr/bin/env python3
"""geo_slug.py — one slug implementation for the whole geographic ladder.

Split out of build-spot-worklist.py (amendment v2.2) because two independent
slug implementations is exactly how `locations/bah-a-de-los-ngeles.md` and
`locations/bah-a-de-los-ngeles-bola.md` both ended up queued alongside the
existing `locations/bahia-de-los-angeles.md`.

Two defects fixed here:

  * non-ASCII was DESTROYED rather than folded — "Bahía" became "bah-a".
    NFKD normalization maps accented Latin letters to their ASCII base first.
  * zone names carry slashes ("Tanner / Cortez Bank", "371 / 425 / Upper
    Hidden"), which slugify into path separators or run-on hyphens. Zones
    therefore declare an EXPLICIT canonical slug; the display name keeps its
    slashes.
"""
from __future__ import annotations

import re
import unicodedata

# Names whose slug is not the mechanical one.
ALIASES = {
    "the-rockpile": "rockpile",
    "the-425": "425-bank",
    "425": "425-bank",
    "bahia-de-los-angeles-bola": "bahia-de-los-angeles",
    "bola": "bahia-de-los-angeles",
}

_PARENTHETICAL = re.compile(r"\s*\((?!\d)[^)]*\)")   # "(caution — boilers)"
# ONLY the English article. Spanish articles are part of the place name —
# stripping them turned "La Jolla" into "jolla" and would have done the same
# to La Paz, Los Coronados and El Bajo.
_LEADING_ART = re.compile(r"^the\s+")


def ascii_fold(text: str) -> str:
    """Bahía -> Bahia, Ángeles -> Angeles. Folds, never deletes."""
    return (unicodedata.normalize("NFKD", text)
            .encode("ascii", "ignore").decode("ascii"))


def slugify(name: str) -> str:
    s = ascii_fold(name).strip().lower()
    s = _PARENTHETICAL.sub("", s)          # drop advisory asides, keep "(63)"
    s = _LEADING_ART.sub("", s)
    s = s.replace("/", " ")                # zone names: slash is a separator
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return ALIASES.get(s, s)


def dedupe_key(name: str) -> str:
    """Normalized identity for existing-page collision checks.

    `slugify` alone missed the accented duplicates because it compared a
    mangled slug against a clean filename. This compares folded forms.
    """
    return re.sub(r"[^a-z0-9]", "", slugify(name))
