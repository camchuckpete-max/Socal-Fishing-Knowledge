# Rigging, bait, care — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 10.5 | 12 | 12 |
| found | 2 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.5 | 2 | 2 |
| honest | 1.5 | 2 | 2 |
| actionable | 1.5 | 2 | 2 |
| **wins** | 0 | 1 | 1 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 0 | 0 | 0 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | None | None | None |
| Gear | None | None | None |
| Technique | None | None | None |
| Finding fish | None | None | None |
| Conditions & season | None | None | None |
| Rigging, bait, care | 10.5 | 12 | 12 |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 18. [rigging] FG knot versus Albright: when do I use each, and at what line classes?

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B3', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 1 | 2 | **10** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** A and B are close in quality and both far cleaner on scoping than C; A edges it because it answers the actual line-class question most accurately - it is the only answer that reports the FG's 'the knot scales' claim as fact-check-flagged against its own hedging transcript (ledger row 520) instead of repeating it, and it supplies a second genuinely sourced FG class (80-100 lb braid to a 15-20 ft top shot) rather than a single 50/80 example. B compensates with the clearest guides-pass-or-not fork, the four unreconciled Albright wrap patterns kept side by side, an explicit socal-bight gating caveat, and a per-rod mapping A does not attempt. C is the most specific on numbers but builds an FG class ladder out of technique-note line classes the KB never attaches to the FG, and never mentions region or waters at all, so its extra reach comes at the cost of honesty and scope.

- *B2 reasons:* found: right note plus the widest reach into technique notes and wind-on/double-uni alternatives; specific: richest class table - 80-100 lb braid to 15-20 ft top shot, 65-to-80, 100-to-130 mono, wind-on ~2 ft bury and ~25 ft top shots; sourced: note paths and ids throughout plus the two how-to video links; scoped: no region or waters statement at all, and cites a Baja-range surface-iron line class inside the FG table without noting the note's gating; honest: admits eight gaps but presents technique-level line classes as 'where the KB puts an FG' and derives an unstated 'FG territory ~20 to 100 lb braid' range while repeating the note's 'the knot scales' line; actionable: full tying parameters, use-neither cases, an explicit decision frame, and per-rod calls.
- *B3 reasons:* found: same core note plus crimping, hollow-splice, essential-knots, slim-beauty and the rod profile; specific: 50-to-80 FG example, Albright 8-8 to 80-100, ~20 and 10 wraps, four variant counts, 30/50/65/80 lb braid ladder, min guide size 8, 400 lb crimp demo; sourced: note paths as live links with video ids and absolute dates; scoped: strongest region handling - flags both notes as socal-bight-gated and says the guidance does not formally extend to Baja/Cortez; honest: nine gaps admitted, flags the 98%/100% figure as secondhand, though it passes along the note's unqualified 'the knot scales' line; actionable: guides-or-not fork plus per-rod mapping of Cameron's rack.
- *NOW reasons:* found: nails the dedicated fg-and-albright note plus pr-knot, rp-knot, bite-leaders, line-and-leader, and the evidence file; specific: 50/80 FG demo, 80-100 lb braid FG bluefin build, Albright 8-8 to 80-100, ~20 wraps, 10 wraps, 5-7/7-10/6-7 variants, 50-65 lb braid to 20 lb rod-length leader, min guide size 8; sourced: every parameter carries a note path and a video id plus ledger row numbers; scoped: states both knots are socal-bight with all five waters, no regulatory claims made; honest: uniquely catches that the 'knot scales' generalization is contradicted by its own transcript (ledger 520), marks single-source items as flagged-not-wrong, and lists eight real gaps including no head-to-head break test; actionable: build parameters, failure modes, and a two-question on-boat filter let an angler rig immediately.

<details><summary>Full prompt</summary>

FG knot versus Albright: when do I use each, and at what line classes?

</details>

<details><summary><b>B2 — batch 2</b> · 10/12</summary>

# FG vs Albright — the split, and the line classes

The KB has one note dedicated to exactly this question: [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md) (sources `CIMTyepgonk` for the FG, `NXtvXkqpT9w` for the Albright; the note is stamped `confidence: medium` — BD Outdoors is not blanket-high as a channel per [`sources/source-registry.md`](sources/source-registry.md), only its registered named voices are).

## The one-line decision

Both are braid-to-leader joins on the same system — braid main line, fluoro or mono leader ([`tackle/line-and-leader.md`](tackle/line-and-leader.md)). They solve different problems:

- **FG** — braid wrapped around a **straight** leader under tension, cinched *into* the leader's surface. Extremely low profile, high strength, braid to thin/strong fluoro.
- **Albright** — braid wrapped around a **loop** formed in the leader and locked. Fast to tie, lies flat, and shines going braid to **notably heavier** mono or fluoro.

> **Pick FG for the lowest profile and best guide-passing; pick the Albright when you want a faster tie or are joining to notably heavier leader.** (`rigging/fg-and-albright.md`)

## When each one

**Reach for the FG when the connection has to reel through the guides cleanly and not slap on the cast** (`rigging/fg-and-albright.md`):

- [surface iron](techniques/surface-iron.md)
- [flylining](techniques/flyline.md)
- [swimbaits](techniques/swimbaits.md)
- any lure-casting where a bulky knot would bump the tip guide

It works best when the leader diameter is close to, or thinner than, what the braid wraps can bite into. **It is the fussier of the two — tie it during prep the night before or dockside, not in a frenzy with fish boiling.** Related: [`tackle/line-and-leader.md`](tackle/line-and-leader.md) calls the FG "the smoothest braid-to-leader join" for any leader that runs through the guides, and adds that if you want a long leader inside the guides you need a **minimum guide size of 8** — many bass rods have size-6 guides that aren't leader-friendly.

**Reach for the Albright as the all-round braid-to-solid-mono/fluoro knot** (`rigging/fg-and-albright.md`): the bays — [spotties](species/spotted-bay-bass.md), [halibut](species/california-halibut.md) — and offshore for [bluefin](species/bluefin-tuna.md) and [yellowtail](species/yellowtail.md). It handles a wide pound-test span and lays its tags flat.

## Line classes — what the notes actually give

**Albright — the range is stated explicitly:** tied from roughly **8 lb to 8 lb** up to **80 lb to 100 lb** (`rigging/fg-and-albright.md`, `NXtvXkqpT9w`). That is the widest documented span of any braid-to-leader knot in this KB, and it is why it is the default when the leader is a big step up from the braid.

**FG — no ceiling is stated.** The worked example is **50 lb braid to 80 lb leader**, and the note says only that "the knot scales" (`CIMTyepgonk`). Where the KB puts an FG at a specific class:

| Application | Braid → leader the notes specify | Note |
| --- | --- | --- |
| Knife jigging, direct-tie school | **80–100 lb braid → FG → 15–20 ft of 80–100 lb mono/fluoro top shot**, tied direct to the jig, no crimp (`j37zxs33gws`) | [`techniques/knife-jigging.md`](techniques/knife-jigging.md), [`rigging/bite-leaders.md`](rigging/bite-leaders.md) |
| Knife jigging, light/day outfit | **65 lb braid → 25 ft of 80 lb top shot** (`Ul5FLB2dFgQ`) | [`techniques/knife-jigging.md`](techniques/knife-jigging.md) |
| Knife jigging, heavy/night outfit | **100 lb braid → 130 lb top shot**, mono not fluoro, for the stretch (`Ul5FLB2dFgQ`) | [`techniques/knife-jigging.md`](techniques/knife-jigging.md) |
| Slow-pitch jigging | a thin knot of the **PR/FG class** at the braid-to-leader join specifically so it clears the small guides; the rockfish rig runs **20 lb braid → 25 ft of 50 lb braid → 4-turn surgeon's → ~3 ft of 80 lb** mono/fluoro; pelagics step to ~**40 lb braid** | [`techniques/slow-pitch-jigging.md`](techniques/slow-pitch-jigging.md) |
| Surface iron | ~**80 lb braid** main, short **50 lb, ~18 in** mono/fluoro leader to a 100 lb clip; downsized light-iron setup ~**50 lb braid** to a short fluoro leader (`pcwcRdmWmLc`); long-top-shot alternate builds run **50–60 (up to 80) lb braid → 80–100 yd of 40–50 lb mono** (`A70kK2niu2Q`), location-sized at **40 lb** for local islands and **50 lb** for overnight range and Baja (`LTCFjqtSI8g`) | [`techniques/surface-iron.md`](techniques/surface-iron.md) |
| Swimbaits / kelp | **50–65 lb braid → 60 lb fluoro leader**; **65 lb braid → 50 lb leader**; **65 lb braid → 40 lb mono** (`9xNhdu2aBqE`); on 80 lb braid the leader steps to mono for stretch | [`techniques/swimbaits.md`](techniques/swimbaits.md) |
| Flylining | roughly the **25–30 lb** class, with skipper guidance capping fly line at **20–25 lb test** in one source; a mono-main/short-heavy-fluoro-bite-guard build runs **25 lb mono → 50 lb fluoro** | [`techniques/flyline.md`](techniques/flyline.md) |
| Bay work (Albright's home turf) | spotties finesse **10–20 lb**, Ned rig **10 lb braid / 8 lb leader**; halibut **30 lb** class islands/offshore and **15 lb** in the bay, with a **2.5–3 ft, 25–30 lb fluoro leader** | [`species/spotted-bay-bass.md`](species/spotted-bay-bass.md), [`species/california-halibut.md`](species/california-halibut.md) |

Practical read of that: **FG territory in this KB runs about 20 lb braid up through 100 lb braid**, and the Albright is documented up to **80 lb braid → 100 lb leader**. Above that pairing the KB stops recommending a knot at all (see below).

## Tying parameters — the numbers, not the video

**FG** (`rigging/fg-and-albright.md`, `CIMTyepgonk`):
- About **20** over-and-under wraps of braid up the leader, braid **under tension the whole time** — anchor it to the rod, your teeth, or a hitchpin.
- Lock with a **half hitch on the braid alone** so it can't slip while you finish, then **two half hitches around both lines**, and cinch.
- The **braid changes color** as it constricts onto the leader — that color shift is the tell that it seated.
- Finish with a **four-wrap half hitch that you then unwrap** to cone-taper the knot, and trim the leader tag very close.
- Failure modes: too few wraps, or slack braid while wrapping (no color-change bite); trimming the leader tag so tight the taper pulls.

**Albright** (`rigging/fg-and-albright.md`, `NXtvXkqpT9w`):
- Form a loop ("shelf") in the leader, pass the braid up through, wrap it back **10 times** around the doubled leader, then feed the braid tag back out **the same end it entered** (top-down if you came bottom-up).
- Keep the leader loop **untwisted** or it won't lock.
- **Snug the leader first**, then work the braid tight so the final wrap seats into the knot.
- Trim the tags **flat but not flush** — leave a little on each side so they can't pull back through.
- Failure modes: a twisted loop that won't cinch; over-tight trims that let the flat tag slip.

Step-by-step video is deliberately not transcribed in the KB: [FG](https://www.youtube.com/watch?v=CIMTyepgonk), [Albright](https://www.youtube.com/watch?v=NXtvXkqpT9w).

## Two cases where the KB says use neither

- **Leader stays outside the guides:** use a **double uni — 9 turns on the braid side, 5 on the mono/fluoro side** (5-and-5 slips, 9-and-9 is bulky) ([`tackle/line-and-leader.md`](tackle/line-and-leader.md)).
- **Heavy tuna gear on hollow-core braid:** skip the knot and splice a **wind-on** — near-100% strength, almost no diameter bump, matched within about one pound-test step (100 lb braid to 100 lb fluoro; 130 lb braid to 100 lb leader is acceptable; 130 lb braid to 40 lb leader will not hold), **~2 ft minimum bury**, ~25 ft finished top shots ([`rigging/wind-on-leader.md`](rigging/wind-on-leader.md), `_KE9InIHx8M`, `zkSKgP2bq10`). Requires hollow-core braid — it won't work on solid.

## One unreconciled point you should know about

The KB carries a third answer that is not adjudicated against the FG. [`rigging/essential-knots.md`](rigging/essential-knots.md) calls the **RP knot (Royal Polaris / Roy Rose)** "the preferred braid-to-fluoro leader join here" — **6 wraps up and 6 back down**, exit the loop the way you entered, lubricate, draw slow, snap to seat; commonly tied to ~80 lb "by the book" but holding clean at **100 lb and even ~130 lb**, small enough to pass the guides, with a recounted triple-digit bluefin landed on **65 lb braid to 80 lb fluoro** tied with it (`YGLFn8lPMu0`, name corroborated in `AT6zmDYxjW4`). Meanwhile [`tackle/line-and-leader.md`](tackle/line-and-leader.md) calls the FG the smoothest. **No note in this KB compares FG against RP directly**, so I'm leaving both standing rather than picking for you. The decision frame the notes do support: all three (FG, RP, Albright) pass the guides; they differ in tie time and fussiness, and the FG is explicitly the fussiest. Choose by what you can tie correctly at 4am on a rolling deck, and pre-tie the FG at the dock.

## If this is Cameron's boat

Mapping to [`profiles/cameron/rods.md`](profiles/cameron/rods.md) (braid listed is the max he'll run on that rod):

- **Torium 20HG surface-iron setup — 50 lb braid.** FG to the short 50 lb leader/clip. Squarely inside the documented FG example range (50 lb braid → 80 lb leader).
- **Avet MXJ flyline setup — 50 lb braid**, and the **Lexa 400 workhorse — 50 lb braid.** FG for anything cast; Albright if you're stepping to a much heavier bite guard.
- **Trinidad 40 — 80 lb braid** (yo-yo iron, sinker rigs, heavy flyline). Both knots are in range; Albright's top documented pairing is 80 lb → 100 lb.
- **Talica 25II — 100 lb braid** (trolling, jumbo foamer casting). At the top of the FG's documented use (100 lb braid → 130 lb top shot appears in `techniques/knife-jigging.md`) and past the Albright's stated 80→100 span — this is wind-on territory if that spool is hollow.
- **Fathom 80 — 100 lb braid, spreader-bar trolling only, never casts.** The FG's whole advantage (guide-passing, no slap on the cast) doesn't buy you anything here.
- **Tranx 400 — braid TBD, respool pending**, so no class call.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `rigging/fg-and-albright.md`, `rigging/README.md`, `rigging/essential-knots.md`, `rigging/bite-leaders.md`, `rigging/wind-on-leader.md`, `tackle/line-and-leader.md`, `techniques/knife-jigging.md`, `techniques/slow-pitch-jigging.md`, `techniques/surface-iron.md`, `techniques/swimbaits.md`, `techniques/flyline.md`, `species/spotted-bay-bass.md`, `species/california-halibut.md`, `profiles/cameron/rods.md`, `sources/source-registry.md`, `sources/extraction-log.md`  
*videos:* `CIMTyepgonk`, `NXtvXkqpT9w`, `j37zxs33gws`, `Ul5FLB2dFgQ`, `YGLFn8lPMu0`, `AT6zmDYxjW4`, `pcwcRdmWmLc`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `9xNhdu2aBqE`, `_KE9InIHx8M`, `zkSKgP2bq10`, `aXF0bxAFtU0`  
*gaps admitted:* No head-to-head knot-strength or break-test numbers (percent of line strength) for FG vs Albright anywhere in the KB — the choice is described qualitatively (profile, tie speed, leader step-up) only. | No stated upper line-class ceiling for the FG knot: the note gives one worked example (50 lb braid to 80 lb leader) and says only that 'the knot scales'. | The FG/Albright note gives no leader-length guidance for either knot — top-shot lengths had to be pulled from the technique notes instead. | No guidance on how braid construction (strand count, hollow vs solid, coating) affects an FG's bite into the leader; the KB only covers hollow-core in the wind-on context. | No spinning-vs-conventional distinction for either knot. | FG vs the RP knot is never adjudicated: tackle/line-and-leader.md calls the FG the smoothest braid-to-leader join while rigging/essential-knots.md calls the RP the preferred one, and no note compares them. | No Albright variants (Alberto, slim beauty, or similar) are covered anywhere in the KB. | No coverage of either knot for braid-to-wire connections (the KB routes wire to the haywire twist instead).

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# FG vs. Albright — the decision, and the line classes

Short version from [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md) (the KB keeps both in one note because they solve different problems, `confidence: medium`, region-gated `socal-bight`):

> **Pick FG for the lowest profile and best guide-passing; pick the Albright when you want a faster tie or are joining to notably heavier leader.**

## The real decision test: does the connection have to reel through the guides?

That is the fork, and it's stated the same way from both sides of the KB.

- **Knot passes through the guides on every cast and every crank →  FG.** [`tackle/line-and-leader.md`](tackle/line-and-leader.md) puts it flatly under Connections: "**Leader running through the guides: the FG knot is the smoothest braid-to-leader join.**" The FG note names the applications — [surface iron](techniques/surface-iron.md), [flylining](techniques/flyline.md), [swimbaits](techniques/swimbaits.md), "any lure-casting where a bulky knot would bump the tip guide" (`CIMTyepgonk`).
- **Knot stays outside the tip guide →  Albright is fine, and faster.** [`tackle/line-and-leader.md`](tackle/line-and-leader.md) documents the leader-length rule that makes this work — Robert Schneider's kelp/boiling-rock setup runs **50–65 lb braid to a 20 lb fluoro leader roughly the length of the rod**, specifically "so the leader knot stays outside the tip guide and can be handled by hand at the boat rather than having to crank the knot through the guides" (`NXvqLUZ6qp8`).
- Related guide detail from the same note: if you want a **longer leader through the guides**, use a **minimum guide size of 8** — many bass rods have size-6 guides that aren't leader-friendly.

## Line classes — what the KB actually states

| | FG knot | Albright |
| --- | --- | --- |
| **Stated span** | **No range given.** One worked example: **50 lb braid → 80 lb leader**, and the note says "the knot scales" (`CIMTyepgonk`) | **Roughly 8 lb-to-8 lb up to 80 lb-to-100 lb** — "a very wide span" (`NXtvXkqpT9w`) |
| **Diameter fit** | "Best when **leader diameter is close to or thinner** than what the wraps can bite into" — braid to thin/strong fluoro | Explicitly the knot for **dissimilar diameters**; Rick at Fisherman's Landing frames it generally as joining two lines of dissimilar diameter/strength, his example **30 lb main to a heavier leader** (`2fwj24S9S-o`, 2023-03-16) |
| **Applications named** | Surface iron, flyline, swimbaits — lure-casting | Bays ([spotties](species/spotted-bay-bass.md), [halibut](species/california-halibut.md)), offshore for [bluefin](species/bluefin-tuna.md) and [yellowtail](species/yellowtail.md), even freshwater |
| **When to tie it** | The fussier of the two — "**tie it during prep the night before or dockside, not in a frenzy with fish boiling**" | Fast enough to tie on the water |

Cross-referenced against the braid-class doctrine in [`tackle/line-and-leader.md`](tackle/line-and-leader.md) (Academy Ep16, `aXF0bxAFtU0`) — **30 or 50 lb braid for most SoCal work, up to 65 on a jig stick, 65–80 for casting at 100 lb-class bluefin, below 30 lb too thin for a baitcaster** — the Albright's stated 8→8 through 80→100 span covers essentially every SoCal class in that ladder. The FG has no equivalent published span in this KB; its one documented build (50 → 80) sits right in the middle of it.

## Building each one

**FG (`CIMTyepgonk`):**
- **~20 over-and-under wraps** of braid up a straight leader, braid held under tension the whole time — anchor it to the rod, your teeth, or a hitchpin.
- Lock with **a half hitch on the braid alone** so it can't slip while you finish, then **two half hitches around both lines**, and cinch.
- **The tell it seated: the braid changes color as it constricts onto the leader.** No color shift means it hasn't bitten.
- Finish with a **four-wrap half hitch that you then unwrap** to leave a cone taper, and **trim the leader tag very close**.
- **Failure modes:** too few wraps or slack braid while wrapping (no color-change bite); trimming the leader tag so tight the taper pulls.

**Albright — base method (`NXtvXkqpT9w`):**
- Form a loop ("shelf") in the leader, pass the braid up through it and wrap back **10 times** around the doubled leader, then feed the braid tag out **the same end it entered** (top-down if you came bottom-up).
- **Keep the leader loop untwisted or it won't lock.** Snug the leader first, then work the braid tight so the final wrap seats into the knot.
- **Trim the tags flat but not flush** — leave a little on each side so they can't pull back through.
- **Failure modes:** a twisted loop that won't cinch, or over-tight trims that let the flat tag slip.

## The Albright wrap counts are not reconciled — pick one and be consistent

The KB deliberately keeps four distinct Albright wrap patterns side by side rather than declaring a winner ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md)):

1. **10 wraps, one way** — the base method above (`NXtvXkqpT9w`).
2. **Double-back wrap** — Norm Fujimoto, Izorline, 2019-05-16 (`Bn9fRKUmQ-U`): wrap **5 to 7 times**, pinch, then wrap back down **over the same wraps in the same direction** the same number of times, doubling each wrap in place. Tag back through the loop once or twice, pull everything tight, then drop the tags and pull only the main lines. Framed as good "for any test line" — **no pound-test range stated**.
3. **Spaced-then-overlap, aka "Modified Albright"** — 2019-10-10 (`-BO1lMCTamg`) and Ryan, 2021-05-20 (`5472APCgym8`): wrap down the loop **spacing the wraps out**, then reverse and wrap back up **through the same spaces**, overlapping on the return. **9 wraps** in the 2019 demo; **7 to 10** stated as the working range in 2021 (7 tied on camera). The stated reason: spacing then overlapping "cinches everything down" and ends up "a little bit smaller." **Cinch fully before you trim or it can slip and pull through.**
4. **6–7 down / 6–7 back up** — Captain Armando, Tackle Talk Live: Bluefin Tuna, 2021-01-14 (`shZCjX2-fkI`), keeping each return-pass loop between the loops of the first pass. He calls it "the easiest knot to tie" for spectra to a mono/fluoro leader.

Rick's version (`2fwj24S9S-o`) adds two things the others don't: **six or seven wraps but "no dead-set number"** — wrap "until I got a good looking length of my knot" — and an explicit **wet-it right before the knot stops moving**, then drop the tags and pull only the two main lines so it rolls into a tight barrel.

**Hollow-core braid, from the same Armando citation:** on that boat's kite outfits, which commonly run hollow spectra, the crew ties **this same Albright straight onto the hollow line "as if it was solid"** rather than needle-splicing it (`shZCjX2-fkI`). That's a real convenience if you're rigging hollow and don't want to run a splice — the knotless alternatives are in [`rigging/hollow-splice-and-serving.md`](rigging/hollow-splice-and-serving.md) (18 in of each line buried into the other; hollow-core only, doesn't work with solid braid).

## The FG's known weakness, and the two ways around it

The FG's fussiness is documented as a real failure mode, not a stylistic gripe. In [`rigging/pr-knot.md`](rigging/pr-knot.md), Cesar Chang on Tackle Express states the FG "requires no tool but must be tied very tight with consistent tension held by the angler throughout," and that he has watched FG knots tied "rather quickly" and not exactly correctly **slip out and fail**. His fix is the **PR knot** — the same braid-to-leader job, but tied with a weighted **PR bobbin** whose own weight lays wraps evenly and holds constant tension automatically. He reports ~10 years fishing it with **spectra breaking above the knot and mono below it, but never the knot itself**.

Two cautions on that: the strength figures he cites — **PR at 100%, FG at approximately 98%** on "a destruction-testing machine" — are a **secondhand citation with no testing source, sample size, or line class given**, and the KB flags four Tackle Express video IDs (`To2Dvx3Ifnc`, `ZrcwcugaEe4`, `foLSQJ5oRWI`, `wk8bkqzdyM0`) as **re-cuts of one interview, to be treated as a single source appearance**, capped at medium confidence.

If you want a low-profile guide-passing connection without the FG's tension discipline, the KB's other two candidates for that exact territory are the **RP knot** (6 wraps up, 6 back down, preference range 5–11 by diameter ratio; "commonly tied to ~80 lb by the book, but it holds well beyond — tied clean to 100 lb and even ~130 lb") in [`rigging/essential-knots.md`](rigging/essential-knots.md), and the **slim beauty** ([`rigging/slim-beauty-knot.md`](rigging/slim-beauty-knot.md)) — which is the one knot in this family carrying **`confidence: high`**, on four episodes from the registered `searcher-sportfishing` channel.

## Where both knots stop

[`rigging/crimping.md`](rigging/crimping.md) defines the ceiling in kind rather than in numbers: crimp sleeves are "the standard connection for **leader classes heavy enough that a tied knot is impractical or unreliable**" — demonstrated on **400 lb** (`3zXcrGsIL-c`). And for the bluefin knife-jig terminal specifically, [`rigging/bite-leaders.md`](rigging/bite-leaders.md) has the heavy fluoro **crimped**, not knotted, in a **≤2–2.5 ft** section.

## Against your own rack ([`profiles/cameron/rods.md`](profiles/cameron/rods.md))

- **Torium 20HG / Phenix Abyss 10'0", 50 lb braid — your full surface-iron setup.** This is the textbook FG case: the FG note names surface iron first, and this connection cranks through the guides on every retrieve. Tie it dockside.
- **Avet MXJ / Teramar 9'0", 50 lb braid — mainly flyline.** Same argument, flyline is also named. FG.
- **Lexa 400 / Okuma PCH 9'0", 50 lb braid — your biggest workhorse.** Whichever you tie, both are in range; the FG's own worked example is 50 lb braid to 80 lb leader.
- **Trinidad 40, 80 lb braid; TLD 20, 80 lb braid.** 80 lb sits at the top of the Albright's stated 8→8-through-80→100 span, so an Albright to a heavier leader is inside documented territory here.
- **Talica 25 (100 lb braid) and Fathom 80 (~1000 yd of 100 lb braid, 200 lb leader planned for kite duty).** These sit **at or past the top edge of the Albright's stated span**, and the KB gives no FG range at all — so it doesn't cover them by knot. For that tier it points elsewhere: crimped bite leaders, or the hollow splice/serving route. Note Armando's kite-outfit Albright-on-hollow data point is the one thing in the KB that speaks to the kite build directly.

## One protocol caveat

Both [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md) and [`rigging/pr-knot.md`](rigging/pr-knot.md) are region-gated **`socal-bight` only**. Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) step 1b, that filter is binding — so if you're asking for a Baja or Cortez trip, the KB does not formally extend this guidance there. Both do carry all five `waters` values, so the guidance spans bay-harbor through open-ocean within the Bight.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `rigging/README.md`, `rigging/fg-and-albright.md`, `rigging/essential-knots.md`, `rigging/pr-knot.md`, `rigging/slim-beauty-knot.md`, `rigging/surgeons-knot-mono-to-fluoro.md`, `rigging/crimping.md`, `rigging/bite-leaders.md`, `rigging/hollow-splice-and-serving.md`, `tackle/line-and-leader.md`, `profiles/cameron/rods.md`  
*videos:* `CIMTyepgonk`, `NXtvXkqpT9w`, `Bn9fRKUmQ-U`, `-BO1lMCTamg`, `5472APCgym8`, `2fwj24S9S-o`, `shZCjX2-fkI`, `To2Dvx3Ifnc`, `ZrcwcugaEe4`, `foLSQJ5oRWI`, `wk8bkqzdyM0`, `aXF0bxAFtU0`, `NXvqLUZ6qp8`, `3zXcrGsIL-c`  
*gaps admitted:* No pound-test range is stated anywhere in the KB for the FG knot — only one worked example (50 lb braid to 80 lb leader) plus the assertion that 'the knot scales'; there is no documented floor or ceiling. | No head-to-head strength comparison between the FG and the Albright exists in the KB. The only percentage figure is FG at ~98% vs PR at 100%, a secondhand destruction-test claim with no testing source, sample size, or line class, from four video IDs the KB flags as re-cuts of a single interview. No Albright strength figure is given at all. | The KB gives no rule for choosing among the four documented Albright wrap patterns (10-one-way, 5-7 double-back, 7-10 spaced-then-overlap, 6-7 down/6-7 up) — they are deliberately kept side by side, unreconciled, and none is keyed to a line class. | No FG-with-hollow-core-braid guidance. The 'tie it onto hollow as if it were solid' confirmation covers the Albright only (Captain Armando, shZCjX2-fkI); nothing states whether the FG behaves the same on hollow spectra. | No leader-to-braid diameter-ratio rule for the FG (the RP knot has a wrap-by-line-ratio rule; the FG note only says 'best when leader diameter is close to or thinner than what the wraps can bite into'). | No line class is stated at which a tied braid-to-leader connection should give way to a crimp or a hollow splice — rigging/crimping.md says only 'heavy enough that a tied knot is impractical or unreliable,' demonstrated at 400 lb. | Nothing cameron-sourced on this choice: profiles/cameron/ records braid classes per setup but not which braid-to-leader knot he ties, so the profile pass here is inference from stated line classes rather than recorded preference. | Both the FG/Albright note and the PR-knot note are region-gated socal-bight only — the KB does not state whether this guidance applies to Baja Pacific or Sea of Cortez trips. | No guidance on either knot for spinning vs. conventional reels, or on how braid brand/coating affects the FG's grip.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## The split, in one line each

Both are braid-to-leader connection knots and the KB keeps them in one note, `rigging/fg-and-albright.md` (both tagged `regions: [socal-bight]`, all five `waters`, so neither is region-gated out of a SoCal day):

- **FG** — braid wrapped around a **straight** leader under tension and cinched **into the leader's surface**. Extremely low-profile, high-strength; the smoothest braid-to-leader join in this corpus (`rigging/fg-and-albright.md`; `tackle/line-and-leader.md` names it the smoothest join for a leader that runs through the guides).
- **Albright** — braid wrapped around a **loop formed in the leader** and locked. Fast, lays its tags flat, and spans a much wider pound-test range (`rigging/fg-and-albright.md`, `NXtvXkqpT9w`).

The note's own decision rule: **pick FG for the lowest profile and best guide-passing; pick the Albright when you want a faster tie or are joining to notably heavier leader** (`rigging/fg-and-albright.md`).

## When to reach for FG

- The connection has to reel through the guides cleanly and not slap on the cast — **surface iron, flylining, swimbaits**, any lure-casting where a bulky knot bumps the tip guide (`rigging/fg-and-albright.md`).
- Best when **leader diameter is close to or thinner than what the wraps can bite into** (same note).
- **Timing judgment:** it is the fussier of the two to tie under tension — **tie it during prep the night before or dockside, not in a frenzy with fish boiling** (`CIMTyepgonk`). The PR-knot note adds the mechanism: FG knots tied quickly and not exactly correctly **slip out and fail**, because hand tension is inconsistent (`rigging/pr-knot.md`, `To2Dvx3Ifnc`).

## When to reach for Albright

- All-round braid-to-solid-mono/fluoro: the **bays** (spotties, halibut), **offshore for bluefin and yellowtail**, even freshwater (`rigging/fg-and-albright.md`).
- Whenever you're joining to **notably heavier leader** — its loop-and-wrap structure is explicitly framed by one source as the tie for **two lines of dissimilar diameter/strength** (`2fwj24S9S-o`).
- When you need speed, or the knot won't be cranked through the guides anyway.
- **Hollow spectra:** the same Albright is tied unmodified straight onto hollow-spectra kite outfits, "as if it was solid," rather than needle-splicing (`shZCjX2-fkI`, via `rigging/evidence/fg-and-albright.md`).

## Line classes — only what the corpus actually documents

| Knot | Documented class | Cite |
| --- | --- | --- |
| FG | **50 lb braid to 80 lb leader** — the only class it is demonstrated on | `CIMTyepgonk` |
| FG | **80–100 lb braid**, FG to a **15–20 ft mono/fluoro top shot tied straight to the jig, no crimp** — the direct-tie alternative to a crimped bluefin bite leader, fished in the SoCal knife-jig fleet | `j37zxs33gws` (`rigging/bite-leaders.md`) |
| Albright | **8 lb-to-8 lb up to 80 lb-to-100 lb** — a very wide span | `NXtvXkqpT9w` |
| Albright | **30 lb main line to a heavier leader** (the dissimilar-diameter variant) | `2fwj24S9S-o` |
| Albright | one variant framed as usable for **any line class**, no pound-test stated | `Bn9fRKUmQ-U` |

**Read the FG row with the flag on it.** The note carries an explicit fact-check: the transcript hedges its own weight class ("I think this is 50 pound... 80 pound Gold Label") and **never states or implies the knot scales to other line classes** — that generalization is not in the source (`rigging/fg-and-albright.md`, `sources/fact-check-ledger.md` row 520). So the honest answer is: FG is documented here at **50/80**, and separately fished at **80–100 lb braid** in the bluefin build — there is no sourced FG class ladder. The Albright's 8-8-to-80-100 range is likewise flagged **single-source** (ledger row 522) — flagged, not doubted; single-source is not wrong in this KB.

## Build parameters (the numbers, not the steps)

**FG** (`CIMTyepgonk`, wrap count flagged single-source, ledger row 519):
- About **20 over-and-under wraps** of braid up the leader, braid **under tension the whole time** — anchor it to the rod, your teeth, or a hitchpin.
- The **braid changes color as it constricts** onto the leader — that colour shift is the tell it seated.
- Lock with a **half hitch on the braid alone**, then **two half hitches around both lines**, cinch.
- Finish with a **four-wrap half hitch that you then unwrap** to give the knot a cone taper; trim the leader tag **very close**.

**Albright — base method** (`NXtvXkqpT9w`, wrap count flagged single-source, ledger row 521):
- Form a loop ("shelf") in the leader, pass the braid up through, wrap back **10 times** around the doubled leader, feed the braid tag **back out the same end it entered** (top-down if you came bottom-up).
- Keep the **leader loop untwisted** or it won't lock. **Snug the leader first**, then work the braid tight.
- **Trim the tags flat but not flush** — leave a little on each side so they can't pull back through.

**Albright wrap pattern varies by presenter** — the note says to treat wrap count and pass direction as preference within these ranges; the shared requirement is a **fully cinched knot before trimming** (`rigging/fg-and-albright.md`):
- **Double-back:** braid up through the loop, pinch off **5–7** wraps, then wrap back down over the same wraps in the same direction the same number of times; tag back through the loop once or twice (`Bn9fRKUmQ-U`).
- **Modified Albright (spaced-then-overlap):** wrap down the loop with wraps **spaced apart**, reverse and wrap back up through the same spaces, overlapping on the return — cinches down **smaller** than a one-way wrap. **9** wraps in one clip, **7-to-10** stated as the range with **7** tied in another. It cinches, then stops: release the braid tag and pull, release the leader tag and pull tight (`-BO1lMCTamg`, `5472APCgym8`).
- **Dissimilar-diameter version:** no fixed count — six or seven until it looks right; **wet the knot right before it stops moving** and pull **only the two main lines** to seat it into a tight barrel (`2fwj24S9S-o`).
- **6-7 down / 6-7 back up**, return loops sitting between the first pass's loops; tag back through the original loop (`shZCjX2-fkI`).

**Failure modes** (`rigging/fg-and-albright.md`):
- **FG** — too few wraps or slack braid while wrapping (no colour-change bite); trimming the leader tag so tight the taper pulls.
- **Albright** — a twisted loop that won't cinch; over-tight trims that let the flat tag slip; **trimming before it's fully cinched lets it slip and pull through**.

## The practical filter I'd apply on the boat

**Does the knot have to pass the tip guide on every cast?** If yes, that is the FG's entire argument and it's worth the dockside prep time. If the leader is sized to stay **outside** the guides — e.g. the kelp / boiling-rock build of **50–65 lb braid to a 20 lb fluoro leader roughly the length of the rod**, kept that length precisely so the knot stays outside the tip guide and can be handled by hand at the boat (`tackle/line-and-leader.md`, `NXvqLUZ6qp8`) — the FG's advantage evaporates and the Albright's speed wins. If you do want a long leader through the guides, `tackle/line-and-leader.md` calls for a **minimum guide size of 8**.

**Is the leader much heavier than the braid?** That's the structure/abrasion case — 30 lb braid + hard bait to a **40 lb** leader, weedless swimbait on 50 lb braid to a **60 lb** leader (`aXF0bxAFtU0`, `tackle/line-and-leader.md`) — and by the note's own criterion that's Albright territory, since the FG wants leader close to or thinner than what the wraps can bite into.

## Where the ceiling is, and the alternatives at each end

- **Tool-tied instead of hand-tensioned:** the **PR knot** is offered in this corpus as a direct alternative **to the FG specifically, not the Albright** — a weighted bobbin holds tension for you, addressing the FG's fussiest failure mode. A secondhand strength claim puts PR at 100% and FG at ~98%, referencing unnamed third-party destruction tests — **no testing source, sample size, or line class given**, and flagged as such (`rigging/pr-knot.md`, `To2Dvx3Ifnc`).
- **The corpus's preferred braid-to-fluoro guide-passing join is actually the RP / John Collins knot**, not the FG (`rigging/essential-knots.md`, `rigging/rp-knot.md`) — worth knowing if you're choosing a knot to learn rather than choosing between these two.
- **Above ~80 lb test**, one source stops tying connection knots at all: switch to a **loop-to-loop with a Sato crimp on a wind-on leader** (`b-oixz7pgAo`, `rigging/john-collins-knot.md`). And on big bluefin the last link is a **crimped 130–200 lb bite leader**, not a knot (`kO_BqzUYayc`, `rigging/bite-leaders.md`). The Albright's stated 80-100 ceiling sits right at that boundary.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `rigging/fg-and-albright.md`, `rigging/evidence/fg-and-albright.md`, `rigging/pr-knot.md`, `rigging/essential-knots.md`, `rigging/rp-knot.md`, `rigging/john-collins-knot.md`, `rigging/bite-leaders.md`, `rigging/slim-beauty-knot.md`, `tackle/line-and-leader.md`, `sources/fact-check-ledger.md`, `rigging/README.md`  
*videos:* `CIMTyepgonk`, `NXtvXkqpT9w`, `Bn9fRKUmQ-U`, `-BO1lMCTamg`, `5472APCgym8`, `2fwj24S9S-o`, `shZCjX2-fkI`, `j37zxs33gws`, `To2Dvx3Ifnc`, `b-oixz7pgAo`, `kO_BqzUYayc`, `aXF0bxAFtU0`, `NXvqLUZ6qp8`  
*gaps admitted:* No head-to-head strength or break test of FG vs Albright anywhere in the KB - the only strength figures are a secondhand, unsourced PR-vs-FG claim (100% vs ~98%) with no line class or sample size, itself fact-check flagged. | No FG wrap-count-by-line-class ladder: the corpus gives ~20 wraps at one demoed class (50 lb braid / 80 lb leader) and the note's 'scales to other classes' line is flagged contradicted-by-source. | No sourced leader-diameter ratio or threshold for when a leader is too heavy for an FG - the guidance is qualitative ('close to or thinner than what the wraps can bite into'). | No FG data point on hollow-core spectra; only the Albright is documented tied straight onto hollow spectra (kite outfits). | The Albright's 8-8-to-80-100 lb range and both base wrap counts (FG 20, Albright 10) are single-source and flagged in sources/fact-check-ledger.md - flagged, not disproven. | No cameron-sourced doctrine or preference on either knot; both notes carry confidence: medium and neither cites cameron. | No guidance in either note on braid-to-leader knot choice above about 100 lb - the corpus routes that grade to crimps, wind-on leaders and a Sato crimp loop-to-loop instead. | No sourced retie-speed figures (seconds per knot) or on-the-water fatigue comparison to put a number on 'the Albright is the faster tie'.

</details>

### 19. [rigging] How do I bleed and chill a tuna properly on a small boat?

**Winner:** B3 · mapping {'A': 'B2', 'B': 'B3', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three deliver the same core doctrine - clean gaff, bleed and gill-and-gut immediately, wet-towel cooldown, salted below-freezing slurry (~2 cups rock salt per 7-10 lb bag), and the 2h / 3-5h / overnight chill table - and all three admit plainly that no small-boat fish-care note exists. B wins on scoping and provenance: it is the only answer that region-labels its borrowed small-boat advice (the Bahia de los Angeles panga kill-bag/ice lesson, marked cortez-north rather than promoted to SoCal doctrine), the only one that tells the reader the slurry ratio and all three chill times carry no video_id and are single-source seminar reporting, and it stamps the CDFW bluefin limit with an as-of date and verify-current while flagging the missing fillet-at-sea rule. C is a close second and the most readable, with genuinely useful additions no one else has (deck hose water in the high 70s F, the dorado do-not-bleed contrast, no house battery so RSW is structurally off the table) but it skips the gaffing-note confidence caveat and any regulatory framing. A is accurate and well-cited but the weakest on the actual question: its small-boat section is mostly a list of what the KB lacks, so the angler gets the general chain without B's and C's translation to a 22-footer.

- *B2 reasons:* found: pulled the right chain (tuna-care, ikejime, gaffing, dorado-and-general) and stated up front there is no small-boat care note. specific: rock salt ~2 cups per 7-10 lb bag, chill table 2h/3-5h/overnight, gaff sizes 3in/6ft vs 6in/8ft, length x girth^2 / 800 worked to 181 lb, 32F loin rinse, 36F RSW. sourced: note paths plus video ids (w6DDCSLu8vM, I84uoay_jwQ, JeexIvtUkZc, H-vIGWPIPVc, Klfb433I3Uk, usHl-4SfqDA, mDmbGdQAy-4) and flags gaffing.md as low confidence/sponsored. scoped: bluefin bag limit carries California/CDFW + as-of 2024-11 + verify-current + medium-confidence caveat; yellowtail data labeled cross-species; no relative time. honest: long, concrete gap list including the deliberately-unwritten bleed cut and spike placement. actionable: the general chain is executable, but the small-boat translation is almost entirely deferred to gaps - only the profile ice load and 'RSW is a big-boat answer' land.
- *B3 reasons:* found: same core chain plus gaff-call timing, freespool-with-thumb, all-hands at the 100-115 lb class, and the Bahia de los Angeles panga kill-bag/ice lesson as the nearest small-boat analogue. specific: every parameter the others carry, plus 100-125 lb ice per trip converted to ~10-14 bags / ~20-28 cups salt, explicitly labeled arithmetic not doctrine. sourced: paths + ids throughout, with channel/date on OIiDJu4mx44 and elBPRrdkugU, and confidence tiers separated within gaffing.md. scoped: best of the three - region-labels the Baja panga advice as cortez-north rather than promoting it to SoCal doctrine; CDFW bluefin limit with as-of 2024-11, 2014 zero-retention history, and verify-current; flags the fillet-at-sea reg as absent. honest: strongest provenance honesty - states the slurry ratio and all three chill times have no video_id and are single-source seminar reporting, and flags the profile's missing gaff/knife/spike rather than assuming them. actionable: converts the chain into decisions for a 22-ft boat (cavity packing, bleed into a bucket not over the rail after the sea-lion case, cold chain past the dock).
- *NOW reasons:* found: right chain, tightest structure, and adds small-boat-relevant material the others miss (fighting doctrine for 20-30 ft private boats, no house battery/shore power so RSW is structurally unavailable). specific: same slurry ratio and chill table, plus deck-hose water in the high 70s F, the 10-minute drive-home ice-chest rule, 32F loin rinse, 181 lb worked estimate. sourced: most granular per-claim ids (5to3Q5P7w90 carries the slurry/chill/wet-towel parameters, plus Q196GVwVqro, elBPRrdkugU, 2gHRrR3D8rY) and cites the evidence file; does not note gaffing confidence the way A and B do. scoped: correctly quarantines the 5-minute upside-down figure as yellowtail-only and single-source, and warns dorado are the opposite call (no bleed, ice immediately); no regulation asserted, so no bare limit. honest: clean gap list including flagged yellowfin/skipjack care gaps, no core-temp verification, no max gaff-to-bleed window. actionable: shortest path to running the sequence, with the rock-salt quantity worked for the actual ice load and cross-species mistakes pre-empted.

<details><summary>Full prompt</summary>

How do I bleed and chill a tuna properly on a small boat?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Bleeding and chilling a tuna on a small boat

The KB's chain for this lives in [`fish-care/tuna-care.md`](fish-care/tuna-care.md) (confidence: medium), with the kill step in [`fish-care/ikejime.md`](fish-care/ikejime.md) and the gaff shot in [`fish-care/gaffing.md`](fish-care/gaffing.md). Up front, one honest caveat: **the KB has no small-boat-specific fish-care note.** The chain below is the general tuna chain; where a small boat changes the math (ice volume, cooler vs. kill bag, a fish too big to fit anything you own) the KB is silent and I've flagged it rather than filled it in.

## The order of operations

Per [`fish-care/ikejime.md`](fish-care/ikejime.md), the full quality chain is **kill clean (ikejime) → bleed → field-dress → chill in the below-freezing slurry**. Each step protects the meat differently, so they stack — ikejime does *not* replace bleeding and chilling. One charter's stated on-camera order is **bleed, kill, then gut, immediately on landing the fish** (`usHl-4SfqDA`, 2024-11-13) — same chain, different sequencing of the first two, and the KB keeps both side by side rather than reconciling them.

### 1. Boat it cleanly — the gaff is a care step

A torn-up fish is a quality problem before you ever pick up a knife ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)).

- Aim the gaff at the **head/shoulder region**, not mid-body or tail — a head-forward shot controls the fish and keeps the gaff out of the meat (`w6DDCSLu8vM`).
- The more specific doctrine in [`fish-care/gaffing.md`](fish-care/gaffing.md) — kept beside the above, not merged — is **aim for the pec and flip the fish upside down the instant it's gaffed**; a bluefin has never been upside down in its life, and it stuns it dead in the water, "I don't care if he weighs 300 lb or if he weighs 20 lb" (`I84uoay_jwQ`, corroborated in a separate non-sponsored tutorial, `8jC61LzQoxU`). **Do not gaff the back, tail, or side of the head** — the fish keeps driving and rips the gaff out of your hands.
- **Hook orientation:** never gaff with the hook pointed away from the boat and pull outward ("digging a hole"). Turn the point back toward the boat and drag it across the top of the water toward you, so the stroke pulls the fish *in*.
- **Landing:** hand over hand straight up onto the deck. Do not lift it like you'd lift on a rod — that's how it falls off.
- **Gaff sizing:** 3-in hook / ~6-ft gaff for fish to **40–50 lb**; 6-in hook / ~8-ft gaff for SoCal bluefin at the **200–300 lb** grade.
- Note that [`fish-care/gaffing.md`](fish-care/gaffing.md) carries `confidence: low` — its source is a sponsored gaff spot, and the KB caps that voice's sponsored content at low regardless of content.

Small-boat safety, which matters more the less deck you have: **never stand the gaff butt-down with the hook up at head height** while people are moving around excited — rest it on the gunnel, hook up and out of the way, or in a rod holder if the butt fits. Keep your hands off it until the shot itself.

### 2. Bleed and gill-and-gut, immediately, on the water

Do it while the fish is fresh, **before** it goes on ice ([`fish-care/tuna-care.md`](fish-care/tuna-care.md), walkthrough video `JeexIvtUkZc`).

- **Bleed** it so the meat doesn't hold blood.
- **Field-dress it: pull the guts and the gills.** That removes the warm mass and the enzymes that spoil quality fastest, so the slurry cools the carcass instead of fighting a bellyful of heat.
- The mechanism, as described independently (`H-vIGWPIPVc`, San Clemente Island, 2019-10-30): **cutting/pulling the gill opens the bloodline**, which bleeds the fish out *and* kills it faster — done immediately boat-side, fish onto ice right after.
- The KB deliberately does **not** give you a play-by-play of where to cut — it says the parameters and judgment are here and the hands-on motions come from the video. Watch `JeexIvtUkZc` for exactly where to cut and pull.
- Cross-species data point the KB logs here for lack of a yellowtail bleed note (`Klfb433I3Uk`, San Clemente Island, 2019-10-04, **yellowtail not tuna**): cut the artery as soon as the fish is on deck — "almost all the fish's blood goes through this artery within a matter of minutes" — then hold the fish **upside down in a bucket** for **~5 minutes**, which was called out as enough to pump the blood out, then onto ice.

### 3. Ikejime, if you're after sashimi

Reach for it when you want **top-quality / sashimi-grade** flesh; an instant clean kill leaves better meat than a fish that fights out in the hold ([`fish-care/ikejime.md`](fish-care/ikejime.md), `WzT0RSHpaQc`). It's a **spike driven into the brain** at a target point on the head, optionally followed by **pithing** — running a wire down the spinal cord to destroy the nerve line so the whole nervous system shuts down cleanly and the fish doesn't thrash quality into the meat. For a fish headed to the smoker or grill, skip the ritual — bleed and chill will carry it. The KB is explicit that **spike placement and depth are learned from the video and hands-on, not from prose** — it does not give you the spot.

### 4. Wet-towel cooldown before the ice

Before the dressed carcass goes into the slurry, give it a **wet-towel cooldown** to knock the surface heat off. Dropping a hot fish straight into ice is less effective than letting it shed the worst of its heat first, then committing it to the cold ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)).

### 5. The below-freezing slurry — the actual recipe

This is the step most small-boat guys get wrong by using bare ice. From [`fish-care/tuna-care.md`](fish-care/tuna-care.md) and repeated as the all-species principle in [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md) (numbers sourced to BD Outdoors care/seminar reporting):

- **Rock salt, ~2 cups per 7–10 lb bag of ice**, mixed into the ice, plus a **splash of seawater** to make it wet. The salt drives the mix **below freezing** — that is the entire reason it out-chills plain ice water, and the only way a thick tuna chills through to the core.
- **Keep the fish fully in the slurry** and **re-ice as the ice burns down**. A fish half in the cold chills unevenly.
- The charter variant (`usHl-4SfqDA`) adds: **pack the body cavity itself with ice** and **cover the fish completely**.
- **Never rinse the fish in fresh water**, and don't let it sit swimming in freshwater melt — it degrades color and flesh ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md), `E4vKwRaRueA`). Keep it in cold salt slurry or on ice.
- Keep it **out of the sun**; a fish baking on a hot deck is losing quality the whole time.

### 6. Chill times — how long before it's actually done

| Fish size | Chill time in the slurry |
|---|---|
| 30–40 lb | ≈ 2 h |
| ~100 lb | ≈ 3–5 h |
| >100 lb | **overnight, re-iced** |

A **>100 lb** fish will not core-chill in an afternoon — plan to hold it overnight and re-ice as the slurry melts down ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)). This is the single hardest constraint for a small boat: it means the cold chain has to survive the run home, the dock, and the night.

No scale on board? The KB records the crew formula used on deck (`mDmbGdQAy-4`, 2025-10-06, NE of Santa Barbara Island): **length × girth² ÷ 800**, inches in, pounds out — worked on camera as 46 in girth × 68.5 in length ≈ **181 lb**. Good enough to pick your row in that table.

### 7. Past the dock

- **Bring a car cooler for the drive home** — plan the cold chain past the dock rather than letting the fish warm up on the road ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)).
- **Loins get rinsed in cold salt water, never fresh** (`usHl-4SfqDA`): moisture from fresh water speeds tuna decomposition. That crew mixes **regular table salt, about 3/4 cup per batch of ice**, to bring the rinse water to **about 32 °F, just under freezing**; loins get a quick rinse straight after cutting and go back into the bag / onto ice **while still cold**. Their named failure mode: charters that loin, skin, bag in plastic and hand it over with no salt-water step and no attentive chilling are "a great way to waste a lot of the tuna."
- Storage windows from [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md) (`2gHRrR3D8rY`): refrigerated fillets ~**3 days**; vacuum-sealed frozen **1–3 months**; plain ziplock frozen roughly **1 week to 1 month**. Dry the fillets before bagging, and if you have no vacuum sealer, use **water-displacement bagging** — fill the bag, leave a small opening, submerge slowly so water pressure pushes the air out, seal just before it goes under.

## What this means on a small boat specifically

The KB doesn't have a note on this, so treat the following as the only anchored numbers rather than a doctrine:

- **Ice load.** The one small-boat figure in the KB is from [`profiles/cameron/boat.md`](profiles/cameron/boat.md) — a 22-ft Panga Marine Marquesas carries **100–125 lb of ice per trip**, with ~100 lb of it riding in the cooler on the run out (it's also part of the boat's trim routine). There is no general rule in the KB for pounds of ice per pound of fish.
- **The RSW alternative is not available to you.** The multi-day charter option the KB records is an onboard **refrigerated-seawater hold running at about 36 °F**, fish in it until they're filleted (`Y1xeieQI3B4`, Cortez Bank, 2025-05-10, aboard the 85 ft *El Dorado*). It's kept side by side with the slurry chain as a different mechanism, not a replacement — and it's a big-boat answer. On a small boat, the salted slurry *is* the mechanism.
- **Cooler space is a limit worth planning against.** Bag limit stated on camera is **two Pacific bluefin per person per day** (California / CDFW, as of 2024-11, unregistered channel — medium confidence; **verify current regs before you fish**), per [`species/bluefin-tuna.md`](species/bluefin-tuna.md).

One process note, since it front-loads everything above: the fight determines how clean the gaff shot is. [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md) is the boat-handling note (gear-tap the boat in and out of gear, walk down-swell, avoid the death circle) and [`fish-care/tuna-care.md`](fish-care/tuna-care.md) explicitly treats that as the setup for a controlled gaff rather than a rushed one.

## What I could not answer from this KB

- No small-boat fish-care note at all — nothing on kill bags vs. coolers, cooler sizing, or ice-to-fish ratios.
- Nothing on what to do with a fish too big to fit your cooler on a small boat (the >100 lb overnight-re-iced requirement is stated, but not how to meet it on a trailer boat).
- The exact bleed cut is deliberately not written down — the KB points you at video `JeexIvtUkZc` and says to learn it there.
- Ikejime spike placement and depth likewise are not in the KB — video `WzT0RSHpaQc` and hands-on only.
- No target temperature for the whole-fish slurry itself (only "below freezing"; the 32 °F figure is for the dockside loin rinse and 36 °F for a charter RSW hold).
- No guidance on running a slurry cooler's drain, or on managing freshwater melt beyond "don't let the fish soak in it."
- No regulation content on whether a tuna must stay whole or intact for measurement in California waters, which bears directly on gutting at sea.
- Doing this solo — no note covers whether a one-man crew should gaff, kill, bleed, and dress in the same order on a rolling deck.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `fish-care/README.md`, `fish-care/tuna-care.md`, `fish-care/ikejime.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `species/bluefin-tuna.md`, `techniques/fighting-big-bluefin.md`, `profiles/cameron/boat.md`  
*videos:* `JeexIvtUkZc`, `w6DDCSLu8vM`, `H-vIGWPIPVc`, `usHl-4SfqDA`, `Klfb433I3Uk`, `mDmbGdQAy-4`, `Y1xeieQI3B4`, `WzT0RSHpaQc`, `I84uoay_jwQ`, `8jC61LzQoxU`, `E4vKwRaRueA`, `2gHRrR3D8rY`  
*gaps admitted:* No small-boat-specific fish-care note exists in the KB — nothing on kill bags vs. coolers, cooler sizing, or ice-to-fish ratios. | No guidance on handling a tuna too large to fit a cooler or fish bag on a trailer boat, despite the >100 lb overnight-re-iced requirement. | The exact bleed cut location for a tuna is not written down — the KB explicitly defers to video JeexIvtUkZc. | Ikejime spike placement and depth are not in the KB — deferred to video WzT0RSHpaQc and hands-on practice. | No target temperature for the whole-fish slurry itself (only 'below freezing'); the 32 °F figure applies to the dockside loin rinse and 36 °F to a charter RSW hold. | No guidance on cooler drain management or handling freshwater melt beyond 'don't let the fish soak in it'. | No regulatory content on whether a tuna must be landed whole/intact for measurement in California, which bears on gutting at sea. | Nothing on performing the gaff/kill/bleed/dress sequence solo on a rolling small-boat deck. | No general rule for how much ice to carry per pound of fish — the only figure is Cameron's profile (100–125 lb per trip on a 22-ft panga).

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Bleeding and chilling a tuna on a small boat

Short version of what the KB actually says: **gaff it clean → bleed and gill-and-gut it immediately on deck → knock the surface heat off with a wet towel → commit it to a salted, below-freezing slurry and hold it there long enough for the mass you're holding.** The chain lives in [`fish-care/tuna-care.md`](fish-care/tuna-care.md) (confidence `medium`), with the brain-spike tier in [`fish-care/ikejime.md`](fish-care/ikejime.md) and the gaff mechanics in [`fish-care/gaffing.md`](fish-care/gaffing.md).

One thing up front so you can calibrate: **the KB has no small-boat-specific fish-care note.** Every parameter below is the general tuna chain. Where the small-boat problem is real (cooler capacity, ice load, where a 100 lb fish rides on a 22-footer) I've said so rather than invented an answer — see the gaps at the bottom.

---

## 1. Get it aboard without wrecking it — the care starts at the gaff

Boating the fish cleanly is step one of care, not a separate job ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)).

- **Call for the gaff the moment the fish first shows deep down — "in the colors"** — so whoever's gaffing is standing at the rail ready instead of scrambling once it's up (`OIiDJu4mx44`, Capt. Art Taylor & Capt. Mike, Searcher Sportfishing, *Tackle Tip Thursday* Vol. 200, 2022-10-13 — [`fish-care/gaffing.md`](fish-care/gaffing.md)).
- **Keep the fish lying horizontal just under the surface. Do not lift its head out of the water** before the shot — that's unnatural for the fish and makes it dive (`OIiDJu4mx44`).
- **Two placements are kept side by side in the KB, both attributed, not reconciled:** aim at the **head/shoulder** region — not mid-body or tail — so the gaff controls the fish and stays out of the meat (`w6DDCSLu8vM`, [`fish-care/tuna-care.md`](fish-care/tuna-care.md)); and aim for the **pec and flip the fish upside down the instant it's gaffed** — a bluefin has never been upside down in its life, and it stops it dead, "I don't care if he weighs 300 lb or if he weighs 20 lb" (`I84uoay_jwQ`, corroborated in a separate non-sponsored tutorial `8jC61LzQoxU`, [`fish-care/gaffing.md`](fish-care/gaffing.md)). Both agree on the negative: **never gaff the back, tail, or side of the head** — the fish keeps driving and rips the gaff out of your hands.
- **Hook orientation:** point the hook back *toward* the boat and drag it across the top of the water toward you, so the stroke pulls the fish in. Gaffing with the hook pointed away — "digging a hole" — knocks the fish around and pushes it away from you.
- **Land it hand-over-hand straight up.** Don't lift it like you'd lift a rod; the fish falls off. Meanwhile the angler **puts the reel in free spool with a thumb on the spool** the instant it's gaffed, so it doesn't backlash on the slack (`OIiDJu4mx44`).
- **Gaff sizing:** 6-in hook / ~8-ft gaff for SoCal bluefin at the **200–300 lb** grade; 3-in hook / ~6-ft gaff for fish up to **40–50 lb** ([`fish-care/gaffing.md`](fish-care/gaffing.md)).

Note the confidence here: `gaffing.md` as a whole sits at **`low`** because the primary source is a sponsored gaff spot; the `OIiDJu4mx44` items above are the medium-confidence ones.

**Small-boat safety, which matters more with two of you than with a full crew:** on **100–115 lb class** fish the doctrine is **all hands on deck for the gaff shot** — a gaffed fish that size can still take off — and a double-gaff was used on one fish (`elBPRrdkugU`, [`fish-care/gaffing.md`](fish-care/gaffing.md)). And **never stand the gaff butt-down with the hook up near head height** on a deck full of excited people; rest it on the gunnel or in a rod holder, hook up and out of the way.

## 2. Bleed and gill-and-gut immediately, on the water

Do this **before it goes on ice**, while the fish is fresh ([`fish-care/tuna-care.md`](fish-care/tuna-care.md), walkthrough `JeexIvtUkZc`).

- **Bleed** it so the meat doesn't hold blood.
- **Field-dress it: pull the guts and the gills.** The mechanism the KB states is the one that should drive your urgency — the viscera and gills are the **warm mass and the spoilage enzymes**. Strip them out and your slurry cools the carcass instead of fighting a bellyful of heat. That is the single biggest lever you have on a small boat with limited ice.
- **The gill cut is the bleed cut.** Cutting/pulling the gill opens the bloodline, which bleeds the fish out *and* kills it faster — done immediately boat-side, fish on ice right after (`H-vIGWPIPVc`, StokedOnFishing, 2019-10-30, San Clemente Island — unregistered channel, medium confidence; the species being bled isn't clearly identified in that transcript, the boat's catch that trip was yellowfin and bonito).
- **Stated order from a charter operation: bleed → kill → gut, immediately on landing**, then **pack the body cavity itself with ice and completely cover the fish** (`usHl-4SfqDA`, 2024-11-13, unregistered channel, medium). The cavity-packing is the addition worth stealing — an empty gut cavity is a place to put cold right at the core.
- **A cross-species data point on how long the bleed takes** (this one is **yellowtail, not tuna**, logged in `tuna-care.md` because no yellowtail bleed note exists): cut the artery as soon as it's on deck — framed on camera as "almost all the fish's blood goes through this artery within a matter of minutes" — then hold the fish **upside down in a bucket**, **~5 minutes** called out as enough to pump the blood out, then on ice (`Klfb433I3Uk`, 2019-10-04, San Clemente Island, unregistered channel, medium). Take the ~5 minutes and the upside-down-in-a-bucket trick as the useful shape; the exact cut location wasn't specified on camera beyond "down here."

**Small-boat caution the KB does support:** don't leave a bled fish hanging over the rail unattended. A boated yellowtail being bled out over the rail at Cedros was grabbed by a sea lion and pulled back into the water — "you took it right out of his hand" (`d0yGBQDeY_4`, 2019-03-05, Cedros Island, [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md)). Bleed it into a bucket or in the cockpit, not dangling outboard.

## 3. Wet-towel cooldown before it goes in the slurry

Before the dressed carcass hits the ice, **give it a wet-towel cooldown** to knock the surface heat off. Dropping a hot fish straight into ice is less effective than letting it shed the worst of its heat first, then committing it to the cold ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)). On a small boat this is also free time — you're doing it while someone else is mixing the slurry.

## 4. The below-freezing slurry — the actual recipe

A saltwater slurry gets **colder than plain ice water**, which is the only reason a big tuna chills through to the core ([`fish-care/tuna-care.md`](fish-care/tuna-care.md); the same recipe is restated as the all-species principle in [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)):

- **Rock salt, ~2 cups per 7–10 lb bag of ice**, plus **a splash of seawater** to make it wet. The salt is what drives the mix below freezing.
- **Keep the fish fully in the slurry**, and **re-ice as the ice burns down** — a fish half in the cold chills unevenly.
- **Keep it out of the sun**, and **do not drown it in fresh water** — no freshwater rinse, and don't let it sit swimming in freshwater melt ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)).

**Provenance flag, because you should know how solid this is:** the slurry ratio and the chill times below come from BD Outdoors care/seminar reporting and **have no video_id in the corpus** — [`sources/extraction-log.md`](sources/extraction-log.md) records them as attributed in prose to the seminar/report context, not in front matter. They're the KB's numbers, but they're single-source.

## 5. Chill times — how long it has to stay in there

| Fish size | Chill time |
|---|---|
| 30–40 lb | ≈ 2 h |
| ~100 lb | ≈ 3–5 h |
| >100 lb | overnight, re-iced |

A **>100 lb fish will not core-chill in an afternoon** — plan to hold it overnight and re-ice it as the slurry melts down ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)). This is the parameter that actually governs your small-boat plan: a 3-hour run home on a 40-pounder is roughly the chill window; on a 100+ lb fish the boat ride is only the first fraction of it, and the cold chain has to continue in the truck.

**To know which row you're in without a scale**, the KB gives the field formula: **length × girth² ÷ 800** (inches in, pounds out) — worked on camera on a bluefin at **46 in girth, 68.5 in length ≈ 181 lb** (`mDmbGdQAy-4`, StokedOnFishing, 2025-10-06 upload, NE of Santa Barbara Island; unregistered channel, medium confidence).

**Kept side by side, not as an option for you:** the big-boat alternative is an onboard **RSW (refrigerated seawater) hold running about 36 °F**, fish in it until they're filleted (`Y1xeieQI3B4`, 2025-05-10, Cortez Bank aboard the 85-ft *El Dorado*). That's a mechanically refrigerated hold, not a salted slurry — different mechanism, and not something a trailer boat carries.

## 6. Ikejime — the tier above, if you're eating it raw

**Ikejime sits on top of bleeding and chilling, it never replaces them** ([`fish-care/ikejime.md`](fish-care/ikejime.md), `WzT0RSHpaQc`). The full quality chain the KB states is: **kill clean (spike) → bleed → field-dress → chill in the below-freezing slurry.** Each step protects the meat differently, so they stack.

- **What it is:** a spike driven into the fish's **brain** to kill it instantly, at a target point on the head; the related step is **pithing** — running a wire down the spinal cord to destroy the nerve line, so the fish doesn't thrash and burn quality into the meat.
- **When it's worth it:** reach for it when you're after **sashimi-grade** flesh. For a fish going to the smoker or the grill, bleed-and-chill will carry it.
- **The KB is explicit that it can't teach you the spike:** exact placement and depth come from the video and hands-on practice, not from prose. That's a real limit, not modesty.

## 7. Past the boat — the cold chain doesn't end at the dock

- **Bring a separate cooler for the vehicle** so the fish stays cold on the drive home instead of warming up on the road ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)). Stated for dorado, but it's the plan-the-cold-chain-past-the-dock principle.
- **When you cut loins, rinse in cold salt water — never fresh.** Moisture from fresh water speeds decomposition. The crew mixes **regular table salt (Morton's), ~3/4 cup per batch of ice**, to chill the rinse water to **about 32 °F, just under freezing**; loins get a quick rinse and go back on ice **while still cold** (`usHl-4SfqDA`, [`fish-care/tuna-care.md`](fish-care/tuna-care.md)).
- **Named failure mode:** loining the fish, skinning it, bagging it in plastic with no salt-water step and no attentive chilling is "a great way to waste a lot of the tuna" — cited against a 100+ lb yield of loins.
- **Storage windows** ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md), `2gHRrR3D8rY`): refrigerated fillets ~**3 days**; vacuum-sealed and frozen **1–3 months**; frozen in a plain ziplock, roughly **1 week to 1 month**. That note also has the water-displacement bagging trick if you don't own a vacuum sealer.

---

## What this means for your boat specifically

Your profile ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)) is a **2004 Panga Marine Marquesas 22**, and it records **100–125 lb of ice per trip**, with **~100 lb in the cooler running out**. Two things follow that the KB lets me say:

- 100 lb of ice at the stated ratio is roughly **10–14 bags**, so budget **~20–28 cups of rock salt** if you intend to salt the whole load. That's arithmetic on the `tuna-care.md` ratio, not a number the KB states — treat it as a sanity check, not doctrine.
- Your trim routine already accounts for ~100 lb of ice forward and a 30-gal bait tank you drain coming in. **It does not account for a 100+ lb fish aboard**, and the KB has nothing on where that fish should ride on a 22-ft panga. That's your call, not the KB's.

**Gear gap, flagged rather than substituted:** your profile lists rods, reels, trolling lures and tackle, but **no gaff, no bleed knife, and no ikejime spike**. The chain above wants a gaff sized to the grade you're targeting (6-in hook / ~8-ft for 200–300 lb bluefin; 3-in / ~6-ft up to 40–50 lb), a knife you can pull gills with, and a spike if you want the sashimi tier. I'm naming those rather than assuming you have them.

**Closest thing the KB has to small-boat capacity advice** is region-labeled Baja panga trip planning, not SoCal doctrine — from [`locations/bahia-de-los-angeles.md`](locations/bahia-de-los-angeles.md) (`regions: cortez-north`): bring **a kill bag**, because the boat's coolers "only fit so many fish and ice," and bring **more ice than you think** or fish "burn up in the fish holds." The source's own lesson across repeat trips was more ice, more coolers, more kill bags each time. That's a panga-fishery observation, and I'm labeling it as such rather than promoting it into general small-boat doctrine — but the logic transfers.

**Regulation, since a tuna is the fish in question:** [`sources/regulatory-claims.md`](sources/regulatory-claims.md) records the **California / CDFW Pacific bluefin bag limit as 2 per person per day, as of 2024-11** (`usHl-4SfqDA`), raised from zero-retention in 2014 (`ztpj1Xll0-U`). **Verify current rules with CDFW before you fish** — nothing in that register is current by virtue of being written down. The KB has **no** entry on whether you may dress or fillet tuna at sea or must land it in a condition where size can be measured; check that with CDFW yourself.

---

## What the KB does not cover (don't take silence as an answer)

1. **No small-boat fish-care note exists.** Kill-bag sizing, what to do with a tuna too big for your cooler, and how to chill a fish you can't fully submerge are all uncovered.
2. **How much ice per pound of fish**, and how long a salted slurry holds in a cooler on a hot deck, are not stated anywhere.
3. **The exact bleed cut on a tuna** is not written down — the artery-cut detail is from a yellowtail video and was "not specified beyond 'down here'" on camera. The gill-cut mechanism is stated; the anatomy is not.
4. **Ikejime spike placement and depth** are explicitly video-only.
5. **The slurry ratio and all three chill times have no video_id** — single-source seminar reporting.
6. **Where a big fish should ride on a small boat** (trim, ballast, deck security) is not covered; your boat note handles ice and people, not fish.
7. **Fillet-at-sea / whole-condition regulations** are absent from the regulatory register.
8. **Yellowfin vs. bluefin** — the chain is written for bluefin and stated to apply to "other tuna," with no yellowfin-specific parameters.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `fish-care/README.md`, `fish-care/tuna-care.md`, `fish-care/ikejime.md`, `fish-care/dorado-and-general.md`, `fish-care/gaffing.md`, `techniques/fighting-big-bluefin.md`, `locations/bahia-de-los-angeles.md`, `profiles/cameron/boat.md`, `sources/regulatory-claims.md`, `sources/extraction-log.md`, `species/bonito.md`, `species/bluefin-tuna.md`  
*videos:* `JeexIvtUkZc`, `w6DDCSLu8vM`, `H-vIGWPIPVc`, `usHl-4SfqDA`, `mDmbGdQAy-4`, `Y1xeieQI3B4`, `Klfb433I3Uk`, `WzT0RSHpaQc`, `E4vKwRaRueA`, `2gHRrR3D8rY`, `I84uoay_jwQ`, `8jC61LzQoxU`, `OIiDJu4mx44`, `elBPRrdkugU`, `d0yGBQDeY_4`, `ztpj1Xll0-U`  
*gaps admitted:* No small-boat-specific fish-care note exists anywhere in the KB — kill-bag sizing, handling a tuna too large for the onboard cooler, and chilling a fish you cannot fully submerge are all uncovered. | No guidance on how much ice is needed per pound of fish, or how long a salted slurry holds its temperature in a cooler on a hot deck. | The exact bleed-cut location on a tuna is not written down; the artery-cut detail in the KB is from a yellowtail video and was explicitly 'not specified beyond down here' on camera. | Ikejime spike placement and depth are explicitly video-only — the note states the prose cannot teach it. | The slurry ratio (~2 cups rock salt per 7-10 lb bag of ice) and all three chill times have no video_id in the corpus; sources/extraction-log.md records them as single-source BD Outdoors seminar/report attribution only. | Where a large fish should ride on a small boat (trim, ballast, securing it on deck) is not covered; profiles/cameron/boat.md covers trim for ice and passengers only. | Whether tuna may be dressed or filleted at sea, or must be landed in a condition where size can be measured, is absent from sources/regulatory-claims.md. | No yellowfin-specific care parameters — the chain is written for bluefin and stated to apply to 'other tuna' without species-specific numbers. | No guidance on how long a bled fish may sit before going into the slurry; 'immediately' is the only timing given. | Sea-lion/shark depredation of a bled fish at the rail is covered by a single yellowtail observation, not by any dedicated note or counter-move doctrine.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Bleeding and chilling a tuna on a small boat

Everything below comes from the KB's fish-care chain — mainly [`fish-care/tuna-care.md`](fish-care/tuna-care.md), which is `confidence: medium` because most of its sources are StokedOnFishing, an unregistered channel that caps at medium under [`sources/source-registry.md`](sources/source-registry.md). Treat it as good working practice, not gospel.

## The chain, in order

**1. Land it clean — the care starts at the gaff**

- Aim the gaff at the **head/shoulder** region, never mid-body or tail: a head-forward shot controls the fish and keeps the gaff out of the meat (`w6DDCSLu8vM`, [`fish-care/tuna-care.md`](fish-care/tuna-care.md)).
- On a big bluefin the more specific version is **aim for the pec and flip the fish upside down the instant it's gaffed** — it stuns it and stops it dead "whether he weighs 300 lb or 20 lb." Do **not** gaff the back, tail, or side of the head; the fish keeps driving and rips the gaff out of your hands (`I84uoay_jwQ`, [`fish-care/gaffing.md`](fish-care/gaffing.md)).
- Gaff sizing: **3-in hook / ~6-ft gaff** for fish to 40–50 lb; **6-in hook / ~8-ft gaff** for SoCal bluefin at the 200–300 lb grade (`I84uoay_jwQ`).
- Small-boat relevance: at the **100–115 lb class** the note says get *all hands* on deck for the shot, and a double-gaff works that grade (`elBPRrdkugU`). With a two-person crew on a 22-footer that's your whole roster — plan who drives, who gaffs, who clears rods before the fish is at color.
- The fight that sets up a clean gaff on a 20–30 ft private boat has its own doctrine: leave the rod in the holder, walk big gentle circles, keep the fish on one side, drive forward only at ~45° to the fish, never reverse (`Q196GVwVqro`, [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md)).

**2. Bleed and gill-and-gut immediately, on the water**

- **Bleed the fish, then pull the gills and guts** — right away, before it goes on ice. That strips the warm mass and the enzymes that spoil quality fastest, so the slurry cools the carcass instead of fighting a bellyful of heat (`JeexIvtUkZc`). Same bleed-then-gut sequence on a yellowfin/bonito trip, fish iced immediately after (`H-vIGWPIPVc`).
- The mechanism the KB records for the bleed cut is at the gill: **cut or pull the gill to open the bloodline** — it bleeds the fish out and kills it faster (`H-vIGWPIPVc`, stated in [`species/bonito.md`](species/bonito.md) and echoed in [`fish-care/evidence/tuna-care.md`](fish-care/evidence/tuna-care.md)).
- One charter's stated order is **bleed → kill → gut immediately on landing**, then **pack the body cavity itself with ice and cover the fish completely** (`usHl-4SfqDA`). The cavity-packing is the useful addition for a boat without a real fish hold.
- **Rinse the cavity in salt water, never the fresh-water hose** — "you don't want to do this with a fresh water hose ever" (`5to3Q5P7w90`, [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)).
- The hands-on knife work is deliberately not transcribed in the KB — it points you at the walkthroughs: gill & gut a bluefin (`JeexIvtUkZc`), gaffing (`w6DDCSLu8vM`).

**3. Wet-towel cooldown before the fish goes in the slurry**

Field-dress, then give the carcass a **wet-towel cooldown** to shed surface heat before it hits the slurry — dropping a hot fish straight into ice is less effective (`5to3Q5P7w90`, [`fish-care/tuna-care.md`](fish-care/tuna-care.md)).

**4. Build a below-freezing slurry, not an ice box**

- **Rock salt, roughly 2 cups per 7–10 lb bag of ice**, plus a splash of seawater to wet it. The salt is what drives the mix below the freezing point of fresh water, and that's what lets a big tuna chill *through to the core* (`5to3Q5P7w90`).
- Keep the fish **fully submerged** in the slurry and **re-ice as it burns down** — a fish half in the cold chills unevenly.
- Do **not** count on the deck hose: that water runs in the **high 70s °F**, so hosing a bagged fish wets it without dropping its temperature (`5to3Q5P7w90`).

**5. Chill times by size — hold it in the cold at least this long** (`5to3Q5P7w90`)

| Fish size | Chill time |
|---|---|
| 30–40 lb | ≈ 2 h |
| ~100 lb | ≈ 3–5 h |
| >100 lb | overnight, re-iced |

A >100 lb fish will not core-chill in an afternoon. The big-boat alternative — an onboard **RSW hold at about 36 °F** that fish go into and stay in until filleting (`Y1xeieQI3B4`) — is not available to you on a trailer boat, so ice volume is your only lever.

**6. Optional top tier: ikejime, stacked on top — not instead of**

Drive a spike into the brain for an instant kill, then run a wire down the spinal cord to pith it; shutting the nervous system down stops the thrashing that burns the meat (`WzT0RSHpaQc`, [`fish-care/ikejime.md`](fish-care/ikejime.md)). Worth it when you want sashimi-grade; for a fish headed to the grill or smoker, bleeding and chilling alone carry it. **Exact spike placement and depth are not written down in the KB** — the note deliberately defers to the video.

**7. After the fillet knife**

- Rinse cut loins in a **cold salt-water bath, never fresh water** — moisture from fresh water speeds tuna decomposition. Mix **regular table salt, about 3/4 cup per batch of ice**, to bring the rinse water to **about 32 °F**, and rinse right after cutting; loins go back on ice still cold (`usHl-4SfqDA`).
- If the drive home from the ramp is more than about **10 minutes**, put an ice chest in the truck so fillets have somewhere cold to go the moment they leave the boat (`5to3Q5P7w90`).
- Storage windows: refrigerated ≈ **3 days**; vacuum-sealed frozen **1–3 months**; plain ziplock frozen roughly **1 week to 1 month**. Dry the fillets before bagging, and if you have no vacuum sealer, use water-displacement bagging — submerge a nearly-sealed zip bag slowly and seal it just before it goes under (`2gHRrR3D8rY`, [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)).

## Sizing it for a small boat

If this is your Panga Marine Marquesas 22 ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)): the profile has you carrying **100–125 lb of ice per trip**, running out with **~100 lb in the cooler**, and there's **no house battery and no shore power** — so RSW is off the table and the salted slurry in that cooler is the whole cold chain. Arithmetic on the stated recipe (not a KB claim): 100 lb of ice is roughly 10–14 of the 7–10 lb bags the recipe is keyed to, so about **20–28 cups of rock salt** to salt it all down. Buy the rock salt with the ice.

Also worth knowing before the fish is on the deck: the profile's trim routine assumes ~100 lb of ice in the cooler with a person forward on the bow bean bag running out, and draining the 30-gal bait tank coming in. The KB does **not** say how a 100+ lb tuna in that cooler changes the trim plan — that's your call, not something a note covers.

## Two things not to carry over from other species

- **Dorado are the opposite call**: no bleed, ice immediately, because they break down unusually fast (`5to3Q5P7w90`, [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)). Don't apply the tuna chain to a mahi in the same cooler.
- The **"5 minutes upside down in a bucket after the artery cut"** figure is **yellowtail doctrine** (`Klfb433I3Uk`, [`species/yellowtail.md`](species/yellowtail.md)), and the KB itself flags its physiological premise as single-source. There is no equivalent stated bleed-out duration for tuna.

## Handy extra

No scale on deck? Estimate with a tape: **length × girth² ÷ 800** (inches → lb). The worked corpus example: 46 in girth, 68.5 in length ≈ 181 lb (`mDmbGdQAy-4`).

## What the KB does not cover

I'm not going to fill these from outside knowledge:

- There is **no small-boat-specific fish-care note** — nothing on kill bag vs. cooler, cooler sizing, deck layout, or how to physically secure and work a 100+ lb tuna on a small deck.
- **No ice-per-pound-of-fish guidance**, and no seawater-to-ice ratio beyond "a splash."
- **No exact bleed-cut anatomy for tuna in prose** — the gill/bloodline cut is recorded from a yellowfin/bonito trip and from the bonito note; the tuna note sends you to the video for the actual cuts.
- **No ikejime spike placement or depth** in text.
- **Yellowfin-specific** bleeding, chilling, ikejime and gaffing are an explicit flagged gap in [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md); **skipjack** care is a flagged gap too ([`species/skipjack-tuna.md`](species/skipjack-tuna.md)). The chain above is written for tuna generally, anchored on bluefin.
- **No stated maximum window** between gaff and bleed (only "immediately"), and **no target core temperature** or way to verify a fish is chilled through beyond the time-by-size table.
- **No guidance for a day-trip trailer boat on the ">100 lb, hold overnight re-iced" requirement** — where that fish lives overnight once it's off the boat isn't addressed.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `fish-care/README.md`, `fish-care/tuna-care.md`, `fish-care/evidence/tuna-care.md`, `fish-care/ikejime.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `fish-care/evidence/dorado-and-general.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/skipjack-tuna.md`, `species/yellowtail.md`, `species/bonito.md`, `techniques/fighting-big-bluefin.md`, `profiles/cameron/boat.md`, `sources/source-registry.md`  
*videos:* `JeexIvtUkZc`, `w6DDCSLu8vM`, `H-vIGWPIPVc`, `usHl-4SfqDA`, `5to3Q5P7w90`, `Y1xeieQI3B4`, `mDmbGdQAy-4`, `Klfb433I3Uk`, `WzT0RSHpaQc`, `2gHRrR3D8rY`, `I84uoay_jwQ`, `elBPRrdkugU`, `Q196GVwVqro`  
*gaps admitted:* No small-boat-specific fish-care note exists: nothing on kill bag vs. cooler, cooler sizing, deck layout, or securing/working a 100+ lb tuna on a small deck. | No ice-quantity-per-pound-of-fish guidance, and no seawater-to-ice ratio for the slurry beyond 'a splash of seawater'. | Exact bleed-cut anatomy for a tuna is not written in prose - the KB records the gill/bloodline cut from a yellowfin/bonito source and defers the hands-on cuts to the linked video. | Ikejime spike placement and depth are not stated in text; the note explicitly defers to the video. | Yellowfin-specific bleeding, chilling, ikejime and gaffing are a flagged gap in species/yellowfin-tuna.md; skipjack care is a flagged gap in species/skipjack-tuna.md. | No stated maximum time window between gaff and bleed (only 'immediately'), and no bleed-out duration for tuna (the 5-minute upside-down figure is yellowtail-only). | No target core temperature and no way to verify a fish is chilled through, beyond the time-by-size table. | No guidance for a day-trip trailer boat on the '>100 lb, hold overnight re-iced' requirement - where the fish is held overnight once off the boat is not addressed. | The KB does not say how a large tuna in the cooler affects the small boat's trim/ballast routine.

</details>
