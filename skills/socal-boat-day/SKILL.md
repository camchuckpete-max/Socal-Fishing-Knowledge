---
name: socal-boat-day
description: Plan a Southern California / Baja fishing day — pull live ocean conditions, apply the SoCal Fishing Knowledgebase, and recommend gear from the angler's OWN tackle inventory. Use this skill whenever the user asks about planning a fishing trip, where to fish, what conditions look like, what to throw, what to bring, whether a day looks fishable, or mentions a spot, bank, island, or target species in SoCal or Baja — even if they don't say "plan a trip." Also use it when the user wants to record, update, or review their tackle and rod inventory.
---

# SoCal Boat-Day Planner

This skill is a **thin bootstrap**. It holds almost no fishing logic on purpose.
All the planning doctrine lives in a GitHub repo that is updated constantly, so
the skill fetches it fresh every run instead of carrying a snapshot that would
go stale the day it was packaged.

Your two jobs here: **load the live logic**, and **make sure the plan is built
on this angler's own gear**, not someone else's.

## Constants (the only baked-in values)

```
REPO_BASE = https://github.com/camchuckpete-max/Socal-Fishing-Knowledge/blob/main
ENTRY     = <REPO_BASE>/skills/socal-boat-day/ENTRY.md
ENDPOINTS = <REPO_BASE>/config/endpoints.md
```

**Use the `github.com` form above.** It is the one confirmed to work from a
Claude chat, and GitHub lists directories, so a folder path resolves too.

If a fetch of `github.com` fails, the same files are mirrored on the raw host at
`https://raw.githubusercontent.com/camchuckpete-max/Socal-Fishing-Knowledge/main/<path>`
— identical paths, plain markdown instead of a rendered page. That host has **no
directory listing**, so a folder there must be requested as `<folder>/README.md`.
Try the raw mirror before concluding the repo is unreachable.

Never hardcode an API endpoint from memory. Endpoints move, break, and get
fixed in the repo — that is the whole reason they live there.

## Step 0 — Bootstrap

1. Fetch `ENTRY.md`. Use the `web_fetch` tool (works without code execution).
2. Fetch `endpoints.md`.
3. Follow `ENTRY.md`. It owns the planning procedure and tells you what else to
   read from the repo.

If `ENTRY.md` fetches successfully, it supersedes anything below about *how to
plan*. This file still governs profile handling and the honesty rules.

### When a fetch fails, the status code decides what you do

These are opposite situations and they get opposite responses. Do not collapse
them into "the repo is down."

- **404 on `ENTRY.md`** — the repo is fine; this skill is pointing at a path
  that no longer exists. Retrying will never help. Check the repository's main
  page to see whether the file moved, and **tell the user this copy of the skill
  is out of date and needs replacing.** Then fall back for today's plan.
- **A network error, timeout, or 5xx** — the repo or the network is having a
  moment. Retry once with a longer timeout before concluding anything.

**Either way, if you end up without `ENTRY.md`**, say so plainly — do not
quietly plan without it. Read `references/offline-fallback.md` and give a
clearly-labeled reduced plan. A reduced plan the user knows is reduced is
useful; a confident plan built on nothing is not.

**Folders are not URLs on the raw host.** `raw.githubusercontent.com` serves
files and has no directory listing, so `.../main/species` is a 404 while
`.../main/species/README.md` is the index. Every link in the repo points at a
file; if you ever hold a folder path, append `README.md`.

## Step 1 — Resolve the angler profile

Do this before recommending any gear. Resolve in this order and stop at the
first hit:

1. **The user's Claude memory.** Look for their tackle, rods, trolling lures,
   and boat notes (commonly `/topics/tackle.md`, `/topics/rods.md`,
   `/topics/trolling-lures.md`). If memory is unavailable, move on — don't
   announce a missing feature.
2. **A file they've uploaded or pasted** this conversation.
3. **A profile folder in the repo**, if the user says they have one
   (`<REPO_RAW_BASE>/profiles/<their-handle>/`).
4. **Nothing found** → read `references/tackle-onboarding.md` and run the
   inventory intake. Offer it; don't force it. A user in a hurry can get a
   class-term plan today and do intake later.

### The rule that matters most

**Never recommend gear the user hasn't told you they own.** The repo contains a
worked example profile belonging to its author (Cameron). That profile exists so
the notes have something concrete to point at. It is **not** the user's box.

Concretely:

- The knowledgebase speaks in **gear classes** — "surface-iron class, 40–60 lb",
  "200 g knife-jig class". Resolve those classes against the user's inventory.
- When a class the plan calls for has **no match** in their inventory, say so
  outright: *"The plan wants a heavy yo-yo iron and I don't see one in your
  box — that's the gap for the 40-fathom stop."* Naming the gap is more useful
  than substituting something that doesn't fish the same way.
- With **no profile at all**, give class terms only and note that adding an
  inventory sharpens them. That is a legitimate, working output — not a failure.

### The boat

The repo's example boat is a 22 ft panga with a specific range and sea-state
limit, and the plan is bounded by it. If this user is fishing on that boat, that
default is correct. **If they're on a different boat, ask once** for range, top
speed, sea-state comfort, and rod-holder count, and use theirs instead.

Getting this wrong is the failure mode with real consequences: a range or
sea-state ceiling inherited from someone else's hull can send a plan somewhere a
boat shouldn't go. When you don't know whose boat it is, ask.

## Step 2 — Keep the inventory current

Inventories drift. Jigs get bought, lost, given away.

- When the user mentions acquiring or losing gear, offer to update their
  inventory in memory. Write it in the same format the rest of their inventory
  uses.
- If a run surfaces a gap, mention it once at the end — one line, not a gate,
  and never a lecture about what they should buy.
- Never move a user's inventory into the shared repo unless they explicitly ask.
  Their box is theirs.

## Step 3 — Setup, first run

If ocean-data pulls fail with network errors, the user likely hasn't enabled
outbound network access for code execution. Read `references/setup.md` and walk
them through it. Note that many pulls work through `web_fetch` without it — try
that path before telling anyone to change settings.

## Honesty rules

These override any instinct to produce a tidy plan:

- **Report data age.** Say which date the SST and chlorophyll are from. Ocean
  data lags, sometimes by days.
- **A missing layer is a miss, not a zero.** If an endpoint returns an empty
  result for a layer, that is missing data. Never present it as a reading.
- **Don't launder reports into forecasts.** A plan that just repeats where fish
  were caught two days ago is a weak plan. Reason about why they were there and
  where that condition has moved.
- **Distrust single-source extremes.** Cross-check an outlier SST value against
  another source before building a plan on it.
- **Never invent depths, coordinates, or regulations.** If the repo doesn't say
  it and the data doesn't show it, say you don't know.

## Reference files

- `references/tackle-onboarding.md` — inventory intake and the memory format
- `references/setup.md` — network egress, first run, troubleshooting
- `references/offline-fallback.md` — reduced procedure when the repo is down
