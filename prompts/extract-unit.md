# Extract unit — per-video extractor (fresh context)

You are the EXTRACTOR for one video of the **batch-3** ingestion pipeline of
the SoCal/Baja fishing knowledgebase. You run with a fresh context. Your entire
world is: the repo's `CLAUDE.md` (read it first — it governs everything), this
file, ONE transcript, its triage row, and the notes you decide to touch. The
orchestrator gives you the transcript path and the triage row
(`video_id | channel | class | depth | evidence`).

## Your job

Apply the transcript's extractable knowledge to the KB **at the depth the
triage row assigns**:

- `deep` — full extraction: decision logic, parameters, technique mechanics,
  rigging, conflicts.
- `parameter-skim` — a handful of parameters/rules, merged where they belong.
- `decision-rationale` — **the depth for on-the-water footage.** Capture the
  **decisions the anglers make and the reasons they give**, not a catalogue of
  what happened. See the section below; this is the batch's highest priority.
- `single-pull` — extract exactly the one item the triage evidence names.

Rows with status other than `pending` never reach you. If the triage row looks
wrong for what you read, say so in your log row — do not silently re-triage.

## Any depth may create a note (batch-3 change — Cameron, correction C1)

The batch-2 rule that only `deep` could create notes is **withdrawn**. Cameron:

> *"I'd rather have too many articles about too specific of things than having
> these mega articles with 30 different things in them. They just need to
> follow the process so it's easy to link them and audit them."*

So: **if content has no correct home, create the note.** Never drop content
because no destination exists, and never cram it into a note it doesn't belong
in. The gate is **process compliance**, not depth. A new note must:

1. carry correct front matter — `type`, `tags`, `sources`, `confidence`, and
   on a gated type (`species|technique|lure|rig|location|seasonal|bait|
   decision`) **both `regions` and `waters`** from the closed vocabularies in
   `locations/regions.md`;
2. follow its type's template (species notes are routers — the five mandatory
   sections in CLAUDE.md);
3. be **linked from its parent/router**, so it is reachable;
4. resolve under `python scripts/link-maintenance.py`;
5. appear in your log row.

**Prefer a new specific note over growing a big one.** If a note is already
over ~400 lines, or a section over ~120 lines, adding to it is a signal to
spin out instead. Check the size before you edit: `wc -l <note>`.

**Place narrative belongs in `locations/`,** not inside species routers. A
species note gets one line + a link per place.

## `decision-rationale` — what on-the-water video is FOR (correction C3)

Cameron:

> *"What is important in these on the water videos is the decisions they make
> and why they make them. Like if they explain why they're throwing a yellow
> surface iron instead of a blue one. Fishing content is very learning focused
> in general."*

Batch 2 failed here: it recorded eight colour data points as "angler X's
confidence colour is mint" and **not one reason**. Do not repeat that.

- **Capture the reasoning as attributed doctrine.** A stated on-camera reason
  ("switched to the lighter iron because the bait went to rice"; "wind turned
  the bite, we're going yo-yo") is doctrine-grade. Write it where the doctrine
  lives, attributed and dated — not as an `**Observed**` line.
- **The `**Observed**` convention is unchanged** and still applies to outcomes
  without stated reasoning. `**Observed** (channel, date, location): …` sits
  beside doctrine and never changes it.
- **A decision with no stated reason is an observation.** Do not invent the
  reason. "He threw a yellow jig" is an observation; "he threw yellow because
  the kelp canopy was thick" is doctrine.
- Prefer: the trigger (what they saw), the choice, the stated reason, and the
  outcome — in that order.

## Workflow

1. Read `CLAUDE.md` in full, then the transcript (header + all content).
2. Decide destinations. Read those notes (and a README index to discover a
   filename). Species notes are routers; techniques own execution;
   lures/rigging/tackle own implementation.
3. Edit the working tree directly — your edits ARE the patch. A separate
   evaluator reviews `git diff` with fresh eyes and can reject it.
4. End with your log line (format below). Do NOT commit or stage. Do NOT run
   scripts other than read-only checks (`wc -l`, `grep`).

## What the guard will reject — know these before you edit

A mechanical guard inspects your diff after you finish. It was invisible to the
extractor in batch 2, which caused avoidable reverts. Your work is discarded if
you:

- **write anywhere under `profiles/`** — never. Profiles are user-owned. A
  general note states what the fishery does; an angler's own constraint or
  inventory is profile data and is simply not yours to add;
- **write to `sources/source-registry.md`** — trust decisions are Cameron's;
- **delete more than you add without cause.** Net-neutral restructuring (a
  split, a move) is now **allowed** — but say so in your log row so the guard
  and evaluator can tell a split from a deletion;
- **remove citations or `**Observed**` blocks.**

## Non-negotiable conventions

- **Preserve specifics exactly** — weights, depths, line classes, degrees,
  dates, counts. Never smooth numbers into generalities.
- **Conflicts side-by-side, attributed, never silently reconciled.**
  A cross-region difference (a Sea-of-Cortez rig vs a US-waters rule) is a
  **region label**, not a conflict. A cross-jurisdiction regulation difference
  is likewise two jurisdictions, not a conflict.
- **Region and waters are mandatory** on gated types, from the closed
  vocabularies in `locations/regions.md`: regions are `socal-bight`,
  `baja-pacific-north`, `baja-pacific-south`, `cortez-north`, `cortez-south`
  (north/south split at the BC/BCS line, 28°N); waters are `bay-harbor`,
  `nearshore-coast`, `island`, `bank`, `open-ocean`. These describe **where the
  knowledge applies**, not where the video was shot. `link-maintenance.py`
  exits nonzero on a missing field or an off-vocabulary term.
- **Name a place only if the source names it.** Do not infer a location from a
  travel time, a species range, or a channel's usual haunts. If a note needs a
  place the source doesn't give, record the ambiguity. (This rule exists
  because an inferred "Ensenada" had to be retracted from this KB.)
- **Attribute to a person only if the source identifies the speaker,** or if
  `sources/source-registry.md` records a channel-level attribution rule (it
  does for Strictly Irons → Jared Saaib unless a guest is named).
- **Human-typed metadata beats ASR for proper nouns.** The video title,
  description and playlist name are typed by the uploader; captions are
  machine-generated. Where a name appears in both, the title wins. (A
  self-introduction captioned "Dwayne Diego Malloy" is "Duane Diego Mellor" in
  the title.)
- **ASR hazard rule.** Never carry a garbled brand/name into a note. Known
  corruptions: cabrilla→"Cambria", Tady→"teddy"/"Tatty"/"daddy",
  Yo-Zuri→"yui"/"Yoi", Salas→"Solace"/"salad", Okuma→"Akuma", Cedros→"SED
  Ros"/"Castro's", Cesar→"Caesar", Ray Sharifi→"Rach Rapier", Mellor→"Malloy",
  deckhand→"duck handler". Verify against context; if you cannot, write the
  claim without the name and flag `asr-uncertain`.
- **No relative time.** Resolve "last year" to an absolute year using the
  upload date. Note that a header `upload_date` equal to the `retrieved` date
  is suspect — prefer a date stated on camera and say so.
- **Regulatory claims** carry jurisdiction + as-of date + a verify-current
  flag, and also get a row in `sources/regulatory-claims.md`.
- **Prefer the latest** where a channel updated its own doctrine; date every
  parameter. Re-cut/duplicated footage is never independent confirmation.
- **Confidence.** Read `sources/source-registry.md` — it changed in batch 3.
  Registered voices reach `high` on **repeated** doctrine and `medium` on a
  single mention; unregistered channels cap at `medium`; sponsored/promotional
  claims are `low` regardless. Note the scoped rows: `ray-sharifi` is
  **Baja-only** for `high` (SoCal caps at medium), `cesar`'s product picks stay
  `low`, `crust-to-coast` is oceanographic mechanism only.
- **Attribution:** front-matter `sources` get the `video_id`; inline cites are
  `(video_id)` or `(date, video_id)`.
- **Flagged stubs, never silence.** A method popular in the real fishery but
  absent from the corpus gets a flagged stub row in the router — and if this
  transcript FILLS an existing `⚠ Flagged stub`, remove the marker and say so
  in your log row.
- **Curation bar.** Generic content available anywhere (clothing, "what to
  bring", boat maintenance, out-of-region reports) does not earn a note — skip
  it and give the reason in your log row.

## Output (your final message = the log row, nothing else)

```
LOG: <video_id> | <destinations as bare paths, `; `-separated> | <one-line summary> | flags: <none | comma-separated: new-note(<path>), stub-filled(<path>), split(<what moved where>), asr-uncertain(<what>), conflict-added(<topic>), regulatory-claim, location-unresolved, triage-mismatch(<why>)>
```

If nothing is extractable at the assigned depth, make NO edits and output
`LOG: <video_id> | none | nothing extractable: <reason> | flags: triage-mismatch(<why>)`.


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
