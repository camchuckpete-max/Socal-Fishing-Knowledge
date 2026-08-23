# Tackle & Rod Intake

Goal: get enough of the angler's gear on record that a plan can name **their**
rod and **their** jig instead of a class term. Partial is fine. A single rod and
four jigs already beats nothing.

## How to run it

Keep it short and conversational. Don't interrogate. Two ways in:

**Photos (preferred).** Ask them to shoot their jig box open, and one photo per
rod showing the reel and the blank print near the handle. Blank prints carry the
model, length, power, and line rating. Read what you can, research the model to
fill gaps, and **flag anything you inferred** rather than presenting it as
confirmed. If a print is unreadable, say so and ask.

**Typed.** Ask them to list what they've got in their own words. "Torium on a
10-foot Phenix, 50 braid" is plenty to work with.

Do it in passes. Rods first (fewer items, higher planning value), then irons and
jigs, then trolling lures, then boat if they aren't fishing the default one.

## What to capture

**Per rod setup:**
- Rod make/model, length, power, line rating
- Reel make/model
- Braid class spooled on it — this is the max line they'll put on that rod;
  top shots and leaders change constantly and aren't worth recording
- What they actually use it for — flyline, surface iron, yo-yo, trolling. Role
  matters more than specs when resolving a plan.

**Per lure:**
- Model and maker, color, size/weight
- Type: surface iron, yo-yo iron, knife/vertical jig, popper, stickbait,
  swimbait, trolling plug, spreader bar, cedar plug
- Action or retrieve if known — how it's fished decides when to recommend it

**Boat**, only if they aren't fishing the skill's default hull: range, top
speed, sea-state comfort, rod-holder count and angles, bait tank.

## Where it goes

Write it into the user's Claude memory, one subject per file, in their existing
format if they already have one:

- `/topics/rods.md` — one entry per setup
- `/topics/tackle.md` — casting and jigging hard baits
- `/topics/trolling-lures.md` — trolling spread
- `/topics/boat.md` — only if it's not the default boat

Treat these as living lists. Note the date. When the user later says they bought
or lost something, update the file rather than starting a new one.

If memory isn't available, write the same content as a markdown block they can
save and re-paste, or as a profile folder they can add to the repo.

## Don't

- Don't copy the repo author's inventory into their file to "get started."
- Don't record what they said they want to buy as gear they own. Keep wish-list
  items clearly separate.
- Don't guess a model number to fill a blank. An honest gap is better than a
  wrong ID that later drives a bad recommendation.
