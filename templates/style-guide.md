# Style guide — how KB notes are written (layout v2)

Governing spec for the 2026-08 editorial review and for everything written
after it. The machine mirror of this directory is `scripts/note_schema.py`;
the two change together, in the same commit. A note that has been migrated
carries `layout: v2` in its front matter, which turns on structural
validation in `scripts/link-maintenance.py`.

The model (Cameron, 2026-08-23) is the RuneScape wiki: **state the knowledge
plainly, cite the source compactly, keep one structure per article type, and
drain detail to subpages instead of growing the page.**

## Voice and register

- **State facts plainly, in present tense.** "Yellowtail feed hardest in gray
  light" — not "Erik says that yellowtail feed hardest in gray light."
  The sourcing lives in the cite, not the sentence.
- **Instructional content addresses the reader**: "wind the jig through the
  zone", "stand off the paddy." Descriptive content uses the fish or the
  fishery as the subject.
- **No hedging.** "Some anglers think", "it may be the case" and hedges like
  them never appear. Uncertainty has exactly three homes: a **flag** (below),
  a **gap** line, or an attributed **doctrine conflict**. An estimate that
  must be published states its assumption instead ("assumes a half-day trip,
  two anglers").
- **Preserve specifics exactly** — weights, depths, degrees, line classes,
  dates, counts. Never smooth numbers into generalities. (Unchanged from
  CLAUDE.md.)
- **No relative time.** Absolute years and dates only. (Unchanged.)

## Cites

The canonical inline cite is a **backticked video id** or the token
**(cameron)**:

> Fresh line out-fishes old line on light-line days (`Xr4nURK-Z48`).
> Rig the surface-iron, yo-yo, and flyline outfits simultaneously and switch
> as the read changes (cameron).

- A cite is **mandatory** on: direct quotes, statistics and parameters
  (weights, depths, temperatures, speeds, dates, counts), and any claim a
  reasonable reader could dispute. Plain fishery common ground needs none.
- Multiple sources for one claim: ``(`id1`, `id2`)``.
- **What the cite replaces:** the attribution preamble. Channel names, upload
  dates, registration status, sponsor disclosures, ASR caveats, and inline
  confidence chatter ("unregistered channel — medium confidence") all move to
  the note's **evidence file** or stay in the machine layer (front-matter
  `confidence`, `sources/source-registry.md`). They no longer appear in
  doctrine prose.
- **Exception — doctrine conflicts keep names.** When two sources disagree,
  attribution IS the content: name the voices, keep the positions
  side-by-side, and state the decision frame (what the choice turns on).
  Section order is never a ranking, and the note says so.
- Speaker names may appear where the person is the point ("Cameron's tern
  model") — but the claim itself is still stated plainly and cited.

## Observations and evidence files

`**Observed**` blocks no longer sit in the main note. Each note that has
observations gets a sibling **evidence file** at `<folder>/evidence/<note>.md`
(template: `templates/evidence.md`):

- The main note keeps a one-line `## Evidence` section:
  `Trip reports and per-source provenance: [evidence file](evidence/<note>.md).`
- The evidence file compresses each observation to **one line** — channel,
  date, place, what happened — grouped under headings that mirror the main
  note's sections, and carries the full provenance detail the prose gave up.
- An observation that materially supports or contradicts stated doctrine may
  ALSO leave a one-line trace beside that doctrine in the main note, cited.
  Contradictions are never silently reconciled (unchanged).
- Nothing is deleted in the split: the review guard checks that every cite
  and every observation removed from a note lands in its evidence file.

## Flags

Machine-readable inline markers; grammar is fixed (`scripts/note_schema.py`):

| Marker | Meaning |
| --- | --- |
| `⚠ Flagged gap — no corpus source` | A mandated section/field the corpus cannot fill. Aggregated into `sources/gap-report.md`. |
| `⚠ Flagged stub — no corpus source yet` | Router-row form (pre-dates v2, unchanged). |
| `⚠ Fact-check (<category>): <one line>` | Fact-check finding; categories: `single-source`, `contradicted-by-source`, `contradicted-internal`, `external-mismatch`, `unverifiable`. Every flag also gets a row in `sources/fact-check-ledger.md`. **Flags never delete or reword the claim they sit beside** — single-source does not mean wrong; Cameron adjudicates the ledger. |
| `⚠ cite-unresolved: <original>` | A legacy cite that could not be mechanically resolved to a source id. |
| `⚠ misplaced-content: <one line>` | Content that belongs in another note; paired with a row in `sources/relocation-queue.md`. The transform never moves content across notes itself. |

## Structure

- Every type has a skeleton in this directory (`templates/<type>.md`):
  required `##` sections in canonical order. Extra sections are allowed
  between required ones; required ones must appear, in order. Heading match
  is by prefix, so `## Finding them (sign & sonar)` satisfies
  `## Finding them`.
- **Lead**: after the front matter and H1, 2–4 sentences that answer what it
  is, why it matters here, and when — a reader who stops there has the
  30-second version.
- **Front-matter infobox**: each type's quick-fact fields (listed in its
  template) — scalars and one-line flow lists only. The literal value
  `unknown` is legal and is counted by the gap report; omitting the key is a
  validation failure on v2 notes.
- **Tables before prose** inside a section: lead with the structured artifact
  (the situations table, the specs block), explain below it.
- **Ranked, not scored**: where options are ordered (techniques in a router
  row, gear alternatives), order best→worst, separate equal alternatives
  with `/`, and exile conditions to `[a]`-style footnotes below the table.
- **Requirements vs recommendations are never blended**: a hard gate (a
  permit, a minimum boat range) is stated separately from a soft threshold
  (a recommended line class).

## What is unchanged from CLAUDE.md

Species-first routing; the router never absorbs execution; decision spin-outs
live in `species/`; gear in class terms; region/waters gating; regulatory
claims carry jurisdiction + as-of + verify-current; doctrine merges as
attributed sources; the curation bar; kebab-case; one concept per note.
