---
type: planning
tags: [extraction-log, pending, regulations, provenance]
sources: [cameron]
confidence: high
---

# Pending log entry — regulations note (2026-08-18)

**Why this is a separate file.** `CLAUDE.md` requires provenance to be logged
incrementally at each step's commit, but the batch-3 extraction is writing to
`sources/extraction-log.md` continuously. Appending there mid-batch would
collide. This file holds the entry until the batch finishes, then folds into
the main log and is deleted.

## Sources → destinations

| Source | Destination | Notes |
| --- | --- | --- |
| *2026 California Ocean Sport Fishing Regulations*, CDFW, last updated 2026-07-17 (supplied by Cameron) | `planning/regulations.md` — California section | Figures read from the Regulations Summary Table for Ocean Finfish (pp. 45–49), the per-species sections, §632 MPA general rules, and Measurement Methods (p. 81). Stamped `checked: 2026-08-18`. First entry in the corpus from a published authority rather than a transcript. |
| NOM-017-PESC-1994 + the separate 2015 bluefin measure | `planning/regulations.md` — Mexico section | Base structure only. Official CONAPESCA PDF returned HTTP 403; FAO mirror would not parse. Corroborating detail from search plus long-range fleet practice. |
| `cameron` — Mexican bag-limit account, 2026-08-18 | `planning/regulations.md` — Mexico section | Per-species caps, the "two bluefin count as five" mechanic, and the mixed-bag open item, recorded as unresolved rather than guessed. Cameron's account was **more current than the 1995 norm alone** — bluefin is a 2015 addition. |
| Surfacing + output rules | `skills/socal-boat-day/ENTRY.md`, `planning/day-plan-protocol.md` | Regulations are consulted, not recited; jurisdiction resolves from the destination before any figure is read; a stated limit always carries its `checked:` date and a verify line. |

## Deferred until batch 3 finishes

- **Cross-links** from `planning/regulations.md` into the species routers, and
  the reverse. Species names in the note are currently plain text so that adding
  it touched no species file.
- **A `primary-source` tier row** in `sources/source-registry.md` for the CDFW
  booklet and NOM-017. The reasoning is written into the regulations note's
  provenance section in the meantime.
- **Folding this file into `sources/extraction-log.md`**, then deleting it.

## Known contradictions left in place, by instruction

Six regulatory claims in the species notes are wrong or stale and now contradict
`planning/regulations.md`. Cameron's instruction (2026-08-18) is to leave them
and clean them up after batch 3. Recorded so the contradiction is on the record
rather than discovered later:

| File | Says | Actually |
| --- | --- | --- |
| `species/spotted-bay-bass.md:164` | no minimum size limit | 14 in TL, 5-fish combined bass aggregate |
| `fish-care/sculpin-handling.md:47` | 10 in minimum to keep | no size limit (removed 2025) |
| `species/yellowtail.md:78` | Farnsworth — "only yellowtail and bonito may be kept" | a per-area, per-method rule; two adjacent SMCAs differ |
| `species/rockfish-lingcod.md:21` | season "closes year-end, roughly Jan–Feb" | wrong window; see the CDFW groundfish tables |
| `species/bluefin-tuna.md:870` | "two per person per day" | 2, *in addition to* the 20-fish general limit |
| `species/bluefin-tuna.md:858` | cowcod closure drives bluefin effort to the 43 | repealed for recreational groundfish, 2024 |

<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
