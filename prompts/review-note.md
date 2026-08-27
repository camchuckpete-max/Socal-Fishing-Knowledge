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
3. **Rewrite to house style** (style-guide v2.1 — read its Voice and Cites
   sections as a checklist, every rule is enforced by the verifier):
   plain-statement present-tense prose; compact video-id cites on quotes,
   statistics, and disputables; attribution preambles, channel-status and
   inline-confidence boilerplate deleted. **No filler sentences** — every
   sentence carries a number, condition, decision, or mechanism.
   **Mechanism or gap** — behavioral claims carry their WHY or a mechanism
   gap flag; never write correlation as causation. **Scope every claim**
   (where/when/depths). **Presence ≠ catchability.** **No meta-attribution**
   — no user names in prose, no "the source says", no trip narration inside
   doctrine, no "kept side by side" commentary. **Jargon links or dies.**
   Genuinely contested doctrine leads with the decision rule, then names the
   positions compactly. NEVER change what a claim says while rewriting how
   it says it. Preserve specifics exactly.
3a. **Adjudicated passages are settled — do not touch them.** A passage
   marked `⚠ adjudicated (Cameron, <date>)` has already been ruled on by
   Cameron and is final. Preserve its substance and its `(cameron)`
   attribution verbatim: never reword it toward the corpus wording it
   replaced, never re-flag it as a fact-check, never demote it to evidence
   as a single-source claim, and never "reconcile" it with a source that
   disagrees — the ruling IS the reconciliation. You may reflow whitespace
   and fix a broken link. If an adjudicated passage looks wrong to you, say
   so in your `LOG:` line and change nothing. The guard conserves the
   `cameron` cite token, but not the wording — this rule is what protects
   the wording.
3b. **Single observation ≠ doctrine**: an uncorroborated single-trip claim
   moves to the evidence file (that is conservation, not deletion); the note
   keeps only corroborated doctrine or claims with stated reasoning. Where
   demotions leave a section thin, flag the gap.
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

7b. **Deep per-species execution → queue a spin-out, never bloat the page**
   (amendment v2.2, Cameron: *"the species pages aren't carrying the full
   weight of different techniques, the techniques pages aren't trying to
   explain every variation of each technique for every species"*).
   While transforming a **species router**, if one situation row's program
   carries real execution depth, or while transforming a **technique note**,
   if one species' variation does, queue a species-technique sub-article
   instead of expanding either note:
   `| <this note> | NEW: species/<species>-<technique>.md | <what> | deep per-species execution | <cite> | pending |`
   **The bar is countable: >= 2 distinct CITED execution parameters** specific
   to that species x technique pairing — retrieve, depth, speed, bite
   handling, rig geometry. A gear-weight change alone is never enough
   ("if it's just using heavier gear it shouldn't have its own article").
   Below the bar, the detail stays as a router row or a technique bullet.
   A zone variant (`species/<species>-<technique>-<zone>.md`) needs the
   technique itself to differ in that zone, not just heavier tackle.
   Log every spin-out you queue in your `LOG:` flags as `spinout(<n>)`.
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
