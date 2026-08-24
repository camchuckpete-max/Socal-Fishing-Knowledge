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
- **No filler sentences (v2.1 — pilot feedback, 2026-08-24).** Every sentence
  states something operational — a number, a condition, a decision — or
  explains a mechanism. Vacuous truisms are banned: "X are a
  structure-and-bait fish", "fish hold where bait, structure, and the right
  water stack" say nothing (every fish follows food and structure). A section
  with nothing concrete to say gets a gap flag, not prose.
- **Mechanism or gap.** A behavioral claim (a light window, a current gate, a
  wind response) carries its WHY when a source gives one; when none does, add
  `⚠ Flagged gap — no corpus source: mechanism` beside it. Correlation is
  never written as causation ("paddy yellows appear with the incoming
  bluefin" — coincident timing, not cause).
- **Scope every claim.** Say where/when/what-depths it applies: a hard-bottom
  rule is structure-fishing scope, meaningless over a paddy in 4,000 ft; a
  depth read is scoped to the depths its source fished; a zone-observed
  behavior stays scoped to that zone until corroborated elsewhere.
- **Presence ≠ catchability.** A zone entry that says fish are THERE must also
  say when they are catchable, or flag the gap (some yellows are in La Jolla
  year-round; half-day boats go months without one).
- **Jargon links or dies.** Terms of art (boil, breezing, exotics, slack,
  gray light) link to the note that owns them on first use — never explained
  inline, never left bare.
- **Reader-questions test.** A situations-table row answers what gear, what
  size/color/weight, when this beats the alternatives, and why — or links the
  note that does. A row that leaves an obvious "ok but which jig / what line /
  what hook" unanswered is unfinished.
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
- **No meta-attribution or self-narration (v2.1).** Never "(cameron)" or
  "(nate)" name-flags in prose, never "Modeling stance (X)", never "the
  corpus/the source/this KB says", never "kept side by side, not reconciled"
  commentary in the body. Registered-user doctrine is HOUSE doctrine — stated
  plainly, provenance in front matter and the evidence file. No trip
  narration inside doctrine ("a charter scratched rockfish until the current
  turned…"): write the rule with its cite; the trip goes to the evidence file.
- **Exception — genuinely contested doctrine keeps names.** When credible
  sources actually disagree, LEAD with the operational decision rule (what
  the choice turns on), then name the positions compactly. The
  reconciliation machinery ("section order is not a ranking" and the like)
  lives in the evidence file, not the body.
- **Single observation ≠ doctrine (v2.1).** An uncorroborated single-trip
  claim lives in the evidence file, full stop — the note keeps only
  corroborated doctrine or claims with stated reasoning. Moving a claim to
  evidence is not deletion; conservation rules apply to the pair.

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
