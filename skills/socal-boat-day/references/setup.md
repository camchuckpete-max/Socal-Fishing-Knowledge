# Setup

One-time, and only if data pulls are failing.

## Try `web_fetch` first

Most of what this skill needs — the repo files, and single JSON reads from the
ocean-data APIs — comes through the `web_fetch` tool, which does **not** require
code execution or any settings change. Exhaust that path before asking the user
to change anything.

Code execution is only needed for the heavier work: sampling many points around
a spot, computing temperature gradients, comparing sources across a grid.

## Enabling network access for code execution

If code runs but every outbound request fails, outbound network access is off.
In Claude's settings, find the code execution / analysis tool setting and set
network access to allow all domains, then **start a new conversation** — the
setting applies to new conversations, not the one already running.

Wording and location of that setting change over time. If the user can't find
it, have them search Claude's help site rather than guessing at menu names.

## What "working" looks like

A healthy run pulls, at minimum:

- Sea surface temperature at each spot under consideration
- Chlorophyll at those same spots
- Wind and swell — observed and forecast — **for each fishing spot and along the
  route out and back**, not one coastal station standing in for the whole day
- Current, observed and forecast

If any of those come back empty, that's a gap to report, not a value to skip
past quietly.

## Common failures

**Everything times out on the first call, then works.** The conditions API runs
on a free tier that sleeps. Cold starts take 30–60 seconds. Retry once with a
longer timeout before declaring it down.

**A layer returns an empty result instead of an error.** This happens. Treat an
empty layer as missing data and fall back to the alternate source listed in the
repo's endpoint config.

**The repo fetch 404s.** The entry path may have moved. Try the repo's main page
to see whether the file was renamed, and tell the user the skill needs an update
if it was.
