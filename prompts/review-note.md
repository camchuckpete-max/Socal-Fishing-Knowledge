# Review note — per-note transform (fresh context)

You are the TRANSFORMER for one note of the editorial-review fleet
(`sources/plan-review.md`). Fresh context. Your world is: `CLAUDE.md`, the
layout spec (`templates/style-guide.md` + `templates/<type>.md` for this
note's type — read all three FIRST), ONE note, its worklist row
(`note | tier | status | flags | result`), and — only for corpus-grounding
new sections — targeted greps of `sources/transcripts/`.

Your single deliverable: the note migrated to **layout v2**, with its
evidence file. Edit the working tree directly — your edits ARE the patch; an
adversarial verifier reviews the diff with fresh eyes and can reject it. Do
NOT commit, stage, or push. Do NOT run scripts other than read-only checks
(`wc -l`, `grep`, and `python scripts/review/check-note.py <note>` to
self-check before finishing).

## The transform, in order

1. **Read** CLAUDE.md, the style guide, this type's template, then the note
   in full.
2. **Restructure** to the type's skeleton: required sections in canonical
   order, extras merged in between. Source-named `##` sections are dissolved
   into the sections where their content belongs. Heading-label drift is
   normalized to the canonical labels.
3. **Rewrite to house style**: plain-statement present-tense prose; compact
   cites — `` (`videoId`) `` or `(cameron)` — on quotes, statistics, and
   disputables; attribution preambles, channel-status and inline-confidence
   boilerplate deleted (their information lives in the evidence file and the
   machine layer). Doctrine conflicts keep names + a decision frame. NEVER
   change what a claim says while rewriting how it says it. Preserve
   specifics exactly.
4. **Evidence split**: create `<folder>/evidence/<note>.md` per
   `templates/evidence.md`; move EVERY `**Observed**` block into it as a
   one-line entry (with a backticked source id) under a heading mirroring the
   section it supports; keep the provenance detail there. Add the one-line
   `## Evidence` section to the note. Duplicate observations are kept as
   separate lines marked `duplicate-of`, never merged away — the guard counts
   conservation. An observation that materially supports or contradicts
   doctrine may also leave a one-line cited trace beside that doctrine.
5. **New sections (FULL tier)**: fill `## Presence & forage`, `## Spawning`,
   `## Feeding triggers` — and `## Regulations`, `## Landing & handling` —
   **from the corpus only**: what the note already contains, plus targeted
   transcript searches (`grep -ril "<species> spawn" sources/transcripts/`
   and similar; read ONLY the matching portions of a hit, never whole
   transcript directories). Every claim you add carries a cite resolvable to
   a transcript or `cameron`. Where the corpus is silent, write a single
   `⚠ Flagged gap — no corpus source: <what is missing>` line under the
   heading — NEVER invent, never import outside knowledge. STANDARD tier
   fills only its type's required sections the same way; LIGHT tier adds no
   sections at all (structure + style + cites only).
6. **Infobox**: add the type's front-matter fields from `templates/<type>.md`,
   values from the note's own doctrine; `unknown` where the corpus is silent.
   Add `layout: v2`. The `sources:` list is APPEND-ONLY and must never be
   reflowed, reordered, or reformatted — do not touch it except to append.
7. **Misplaced content**: if content belongs in a different note (wrong lure
   class, execution sitting in a router, place narrative in a species note),
   do NOT move it. Leave it where it is, add
   `⚠ misplaced-content: <one line>` beside it, and append a row to
   `sources/relocation-queue.md` between its markers:
   `| <this note> | <dst path or NEW: <path>> | <what> | <why> | <cite> | pending |`.
   A dedicated relocation pass with a paired guard handles the move.
8. **Spot harvest**: append one row to `sources/spot-harvest.md` between its
   markers for every NAMED fishing spot/zone the note mentions:
   `| <spot name> | <this note> | <section> | <one-line claim> | <cite> |`.
   Named means the source named it — never infer a place.
9. **Regulatory claims**: normalize into `## Regulations` (jurisdiction +
   as-of + verify-current); ensure each has a row in
   `sources/regulatory-claims.md` (append if missing).
10. **Self-check**: run `python scripts/review/check-note.py <note>` and fix
    what it fails on. Then `wc -l <note>` — a FULL note should land well
    under 400 lines with observations gone; if a section still exceeds ~120
    lines, tighten prose (never drop claims).

## Hard rules (the guard reverts violations mechanically)

- Touch ONLY: this note, its evidence file, and the exempt logs named above.
  Never any other note, never `profiles/`, `templates/`, `scripts/`,
  `prompts/`, `sources/source-registry.md`, `sources/transcripts/`.
- Never delete a claim, a cite, or an observation — compress, relocate to
  evidence, or flag. The guard checks cite and observation conservation
  mechanically.
- Never resolve a doctrine conflict; never upgrade confidence; never add a
  place the source didn't name; ASR hazard rule and all extractor
  conventions in `prompts/extract-unit.md` apply unchanged.
- The tier is the depth contract: LIGHT never adds sections; STANDARD never
  adds species biology; FULL fills all mandated sections or flags gaps.

## Output (your final message = the log row, nothing else)

```
LOG: <note> | <evidence file or none> | <one-line outcome incl. before/after line counts> | flags: <none | comma-separated: gaps(<n>), misplaced(<n>), spots(<n>), reg-claims(<n>), asr-uncertain(<what>)>
```


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
