---
type: planning
tags: [skill, entry-point, day-plan, multi-user, bootstrap]
sources: [cameron]
confidence: high
---

# ENTRY — SoCal Boat-Day Skill

The live entry point every distributed `socal-boat-day` skill copy fetches
first. It owns the read order, the profile contract, and what a plan must
state.

**This path is a contract. Never rename or move this file.** Copies of the
`socal-boat-day` skill are distributed as packaged files that cannot be edited
after they're sent; every one of them fetches this exact path. If the content
needs to move, leave a stub here that points to the new location.

    skills/socal-boat-day/ENTRY.md

This file is what an installed skill loads first. It owns the live planning
procedure so the procedure can change without reissuing the skill.

## Read order

1. [`config/endpoints.md`](../../config/endpoints.md) — the conditions APIs, the
   fallback ladder, and the source-validity rules. **Read this before any data
   pull.** Endpoints listed anywhere else, including in a model's memory, are
   stale by definition.
2. [`planning/day-plan-protocol.md`](../../planning/day-plan-protocol.md) — the
   four-step procedure. This is the spine of the plan.
3. Whatever the protocol routes you to — the folder
   [README](../../README.md) indexes are navigable and current.

Fetch notes on demand rather than pulling the whole repo. The protocol and the
folder indexes are written so a session can navigate from here.

**Which host to fetch from.** Prefer
`https://github.com/camchuckpete-max/Socal-Fishing-Knowledge/blob/main/<path>` —
that form is confirmed to work from a Claude chat, and GitHub lists directories,
so a folder path resolves as-is (use `/tree/main/<folder>` for a folder).

The raw mirror, `https://raw.githubusercontent.com/…/main/<path>`, returns plain
markdown and is a fine fallback, with one rule: **raw has no directory listing.**
`.../main/species` is a 404 there while `.../main/species/README.md` is the index
you wanted. Every link in this KB points at a file for that reason; if you hold a
folder path on the raw host, append `README.md`.

## Angler profile — the multi-user contract

The knowledgebase is universal. Everything angler-specific lives in
[`profiles/`](../../profiles/README.md), and
[`profiles/cameron/`](../../profiles/cameron/README.md) is **a worked example,
not the reader's gear**.

The installed skill resolves the user's own inventory before recommending
anything. If it hands you an inventory, resolve
[gear classes](../../tackle/gear-classes.md) against that inventory and name any
class the user has no match for. If it hands you nothing, recommend in class
terms — that is the designed degraded output, not a failure.

Same for the boat: [Cameron's boat](../../profiles/cameron/boat.md) bounds range
and sea state only for people fishing on it. On any other hull, use that hull's
envelope.

## What the plan must contain

Beyond what the protocol produces, every plan states:

- **The observation date of each data layer.** Satellite products lag.
- **Wind and swell resolved per spot and along the transit route**, observed and
  forecast. One coastal station standing in for a whole trip is not acceptable —
  it hides the part of the ride that's actually rough.
- **Chlorophyll alongside SST**, every run. If chlorophyll is unavailable, say
  so; don't silently drop it.
- **Named gaps** — spots not covered by data, gear classes the angler lacks,
  layers that came back empty.

## Regulations — consulted, never recited

Limits live in one place: [`planning/regulations.md`](../../planning/regulations.md).
They are **not** carried in the species notes and must not be volunteered into
ordinary answers.

**Open the regulations note when** the angler is deciding whether to **keep** a
fish — a question about limits or legality ("can I keep this," "what's the
limit," "is this legal"), or a plan step that involves a take decision.

**Do not surface limits** on "where do I go," "what do I throw," or "is it
fishable." That is most of what gets asked, and reciting limits into those
answers is noise.

**Resolve the jurisdiction from the destination first.** A California figure
never appears on a Mexico trip, and a Mexican figure never appears on a
California trip. Cedros does not get a CDFW size limit.

### Stating a limit — the output rule

**Never state a limit without its `checked:` date and a verify-current line in
the same response.** When summarizing, the date and the caveat survive the
summary — they are part of the answer, not context you may drop. The short form:

    (checked YYYY-MM-DD — confirm current rules before you keep anything;
    limits change)

**If the regulations note has no figure for something, say you don't know and
point at the authority — CDFW or CONAPESCA. Do not fill the gap from general
knowledge.** A number recalled from training arrives with no date and no
warning attached, which is worse than no answer.

## Reasoning discipline

- Reports describe where fish **were**. Reason about the mechanism that put them
  there and where that condition has moved by the fishing day. See
  [report reading & forecasting](../../planning/report-reading-and-forecasting.md).
- Sample **fields, not points** — rings and transects around a spot, so a break
  shows up as a gradient rather than a single pixel.
- Compare same-timestamp data only. Mixing observation times manufactures breaks
  that aren't there.
- Treat single-source SST extremes with suspicion and cross-check.

## Structure and current

When reasoning about bottom structure, reason about how water and current move
across the structure — which face is upcurrent, where the shear and the eddy
sit. Do not anchor on named points as though the name is the fish-holding
feature.

<!-- backlinks:start -->
## Linked from

- [Cameron's Boat — Panga Marine Marquesas 22](../../profiles/cameron/boat.md)
- [Conditions Endpoints & Fallback Ladder](../../config/endpoints.md)
- [Day-Plan Protocol](../../planning/day-plan-protocol.md)
- [Gear Classes — the class-term lexicon](../../tackle/gear-classes.md)
- [Report Reading and Forecasting](../../planning/report-reading-and-forecasting.md)
<!-- backlinks:end -->
