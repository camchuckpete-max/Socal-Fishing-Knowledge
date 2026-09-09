# Rigging, bait, care — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11 | 12 | 12 |
| found | 2 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.5 | 2 | 2 |
| honest | 2 | 2 | 2 |
| actionable | 1.5 | 2 | 2 |
| **wins** | 0 | 0 | 2 |
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
| Rigging, bait, care | 11 | 12 | 12 |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 18. [rigging] FG knot versus Albright: when do I use each, and at what line classes?

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B3', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three recovered the same decision rule (FG for lowest profile and guide-passing, Albright for speed or a step up to notably heavier leader) and all three were candid that the FG has exactly one documented pair, 50 lb braid to 80 lb leader, with no floor or ceiling. A wins on the axis the question actually asks about: it is the only answer that produced a second documented FG line class (80-100 lb braid, FG to a 15-20 ft top shot, from rigging/bite-leaders.md) and the only one that converts the corpus into a straight class-to-knot table from 8 lb bay finesse up to 100 lb jigging, with the FG's weaker heavier-leader geometry flagged in the one row where it bites; it also grounds its caveats in live fact-check-ledger rows rather than prose hedging. B is a very close second and has the best single insight - decide whether the knot lives inside the guides at all, since a rod-length leader plus a double uni at 9-and-5 skips the question - plus the sharpest provenance catch (the PR-vs-FG 98%/100% claim traces to four re-cuts of one interview), but its class picks hedge where A commits, and its 50-65 lb braid to 20 lb fluoro kelp pairing reads oddly against the other two. C is solid and honest, with the most vivid why-profile-matters material, but it carries only the base 10-wrap Albright, no second FG data point, and never states the note's region/waters gating.

- *B2 reasons:* found: core note plus good supporting material (why profile matters - jig lost at 40 lb, the Cedros thumb slice, Hansen's 3-4 ft 80 lb fluoro kept below the tip guide), but only the base 10-wrap Albright and no variant set, and no second FG line class; specific: real classes throughout (10/8 Ned rig, 15 lb halibut fluoro, 50-65 to 60, 65 to 40, 80 lb braid/50 lb 18 in iron, 25 lb mono to 50 lb bite guard, 80-150 lb bluefin leaders, 300 lb kite flyer); sourced: note paths, video ids, upload dates, confidence status per channel; scoped: never states the note's regions/waters gating, and gives no Baja/SoCal boundary - the only real shortfall, though nothing is stated in the wrong region and no regulation appears; honest: flags the qualifier-vs-demo contradiction, explicitly labels the RP/FG/Albright three-way framing as its own synthesis, nine-item gap list, absolute dates only; actionable: usable per-application classes and a clear three-way call, plus the ways to dodge the knot entirely (short leader, hollow splice).
- *B3 reasons:* found: same core note plus the best framing move - the guides-in/guides-out decision axis from tackle/line-and-leader.md that can make the whole FG-vs-Albright question moot; specific: dense numbers (double uni 9 braid/5 mono, min guide size 8, 40 lb braid to 20-25 lb fluoro so the bait isn't deadened, RP 65/25 = 7 wraps and 100/80 = 5, 130-200 lb bite leader), full dated variant table with channels; sourced: video ids with channels and upload dates throughout, and the sharpest provenance catch of the three - four PR-knot ids are re-cuts of one interview, not four confirmations; one soft spot, the 50-65 lb braid to 20 lb fluoro kelp/boiling-rock pairing sits oddly against the other readings of the same corpus; scoped: names the socal-bight gate and says no Baja guidance exists; honest: flags the unresolved 'leader thinner than braid' vs 50-to-80 contradiction, refuses to treat the 98%/100% figure as a test, nine-item gap list; actionable: bottom-line comparison table plus tie-it video links, though its class picks hedge ('most comfortable') where A commits.
- *NOW reasons:* found: hit the shared rigging/fg-and-albright.md core AND pulled a second documented FG line class (80-100 lb braid direct-tie to a 15-20 ft top shot, rigging/bite-leaders.md, j37zxs33gws) plus the live fact-check-ledger flags; specific: 50/80 FG pair, ~20 wraps, Albright 8-to-8 through 80-to-100, four variant wrap patterns (5-7, 7-10, 6-7/6-7, no dead-set number), 80 lb braid/50 lb 18 in surface-iron leader, RP 5-wrap floor at 100/80 up to 9-11 at 20/6; sourced: note paths plus video ids on nearly every claim, ledger rows cited for the flags, registry promotion date given; scoped: states the note's regions [socal-bight] and full waters list, no regulatory claims made; honest: labels the 'scales to other classes' line as carrying a contradicted-by-source flag, marks its wind-on ceiling reasoning explicitly as inference not doctrine, notes nothing from cameron, seven-item gap list, no relative time; actionable: the class-to-knot table (8-20 lb Albright only, 50-65 swimbait, 80/50 iron, 80-100 jig) lets an angler pick and tie at his actual line classes.

<details><summary>Full prompt</summary>

FG knot versus Albright: when do I use each, and at what line classes?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# FG vs Albright — when each one, and at what line classes

**Short version, straight from [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md):** pick the **FG for the lowest profile and the best guide-passing**; pick the **Albright when you want a faster tie, or when you're joining to notably heavier leader**. That's the KB's own one-line decision rule, and everything below is detail under it.

Both come from a single note sourced to two BDOutdoors how-to uploads — `CIMTyepgonk` ("How-to: FG Knot — Step by Step", 2022-11-16) and `NXtvXkqpT9w` ("The STRONGEST Braid to Mono Connection — How to Tie the Albright Knot", 2024-12-09). Neither presenter is a registered voice in [`sources/source-registry.md`](sources/source-registry.md), so per the rubric the whole note sits at **`confidence: medium`**. Treat the numbers below as one credible source each, not repeated doctrine.

---

## What each knot actually does

| | **FG** | **Albright** |
| --- | --- | --- |
| Mechanic | Braid wraps around a **straight** leader under tension and **cinches into the leader's surface** | Braid wraps around a **loop formed in the leader** and locks against it |
| Result | Extremely low-profile, high-strength join | Fast, flat-lying join, tags lie flat |
| Native use | Braid to thin/strong fluoro | Braid to **heavier** mono or fluoro |

(Both, [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), `CIMTyepgonk` / `NXtvXkqpT9w`.)

---

## When to reach for the FG

Reach for it **when the connection has to reel through the guides cleanly and not slap on the cast** — the note names these applications explicitly:

- [surface iron](techniques/surface-iron.md)
- [flylining](techniques/flyline.md)
- [swimbaits](techniques/swimbaits.md)
- any lure-casting where a bulky knot would bump the tip guide

The KB gives you a hard reason to care about profile on those, from two other notes:

- **Knot-through-the-guides is a documented failure mode, not a theoretical one.** A knot dragged through the guides on a cast hangs up and backlashes, and braid's zero stretch then **snaps your leader and loses the jig, even at 40 lb** ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), Academy Ep16, `aXF0bxAFtU0`).
- **It cuts people.** On a Cedros yellowtail trip an angler cast a surface iron past his mono-to-fluoro knot and took "a pretty good slice in the thumb" as the knot ran through his hand ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), StokedOnFishing, October 2024 trip / 2025-03-15 upload, `ILBl12Jm7-0`; unregistered channel, medium confidence).

**FG judgment — tie it in advance.** It's the fussier of the two: the note says tie it **during prep the night before or dockside, not in a frenzy with fish boiling** ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md)).

## When to reach for the Albright

The note frames it as the **all-round braid-to-solid-mono/fluoro knot**, and specifically calls out:

- the bays — [spotties](species/spotted-bay-bass.md) and [halibut](species/california-halibut.md)
- offshore for [bluefin](species/bluefin-tuna.md) and [yellowtail](species/yellowtail.md)
- even freshwater

Plus the two situational triggers: **you want the faster tie** (hot bite, re-rigging on the drift), or **you're stepping to a notably heavier leader**.

---

## Line classes — what the KB actually states

This is where the note is thinner than the question deserves, so here's exactly what it gives and what it doesn't.

**Albright — a stated span.** Tied from roughly **8 lb to 8 lb, up to 80 lb to 100 lb** ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), `NXtvXkqpT9w`). That is a very wide span and it covers essentially the whole inshore-to-mid-offshore SoCal range:

- **Bay finesse** — 10 lb braid / 8 lb leader on a Ned rig for spotties ([`species/spotted-bay-bass.md`](species/spotted-bay-bass.md)) sits right at the bottom of the documented span.
- **Bay/harbor halibut** — 15 lb fluoro on a downsized trap rig in 8–15 ft ([`species/california-halibut.md`](species/california-halibut.md)); island squid drops at 30 lb bait class.
- **Kelp calico/swimbait** — 50–65 lb braid to 60 lb fluoro (Landesfeind), 65 lb braid to 40 lb mono cinched button-down tight (Todd Klein, San Clemente Island, 2015-10-28, `9xNhdu2aBqE`), 65 lb braid to a 50 lb leader (Capt. Benny Florentino, `P6Slg6RQiXw`) — all inside the Albright's span ([`techniques/swimbaits.md`](techniques/swimbaits.md)).
- **Where the Albright runs out:** big-bluefin leaders in the KB are **80–150 lb**, with a short **≈130–200 lb** [bite leader](rigging/bite-leaders.md) as the last link and kite flyer rigs to **300 lb** ([`tackle/line-and-leader.md`](tackle/line-and-leader.md)). Above ~100 lb leader you're past the documented Albright range, and the KB's method there is **loop-to-loop off a [wind-on leader](rigging/wind-on-leader.md)**, not a tied braid-to-leader connection.

**FG — one demo pair, no stated range.** The note gives the worked example as **50 lb braid to 80 lb leader** and says only that "the knot scales" ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), `CIMTyepgonk`). There is **no min/max line class and no braid-to-leader diameter ratio** in the KB for the FG.

Be aware of a tension the KB does not resolve: the same note says the FG is "best when leader diameter is close to or thinner than what the wraps can bite into," yet its own demo is 50 lb braid to a **heavier** 80 lb leader, and it hands "notably heavier leader" to the Albright. I'm flagging that rather than papering over it — the note doesn't reconcile it.

**Practical line classes to hang the FG on**, from the applications it names:

- **Surface iron** — ~**80 lb braid** main to a short **50 lb, ~18 in** mono/fluoro leader, then a 100 lb clip to the iron; downsized stick runs ~**50 lb braid** to a short fluoro leader ([`techniques/surface-iron.md`](techniques/surface-iron.md)). Note the iron-specific wrinkle: a thick top shot dampens the iron's swim, so run the **lighter/thinner end** of your range on irons (Cesar via Dirty Hookers, `F7jLrt2j2X8`, 2023-10-09, medium confidence).
- **Flyline** — **25 lb mono** top shot to a **50 lb fluoro** bite guard **2–3 ft** long; the stepped-up trip numbers were 30 lb main → 40 lb leader and 25 lb main → 40 lb leader (Ray Sharifi, ~late-2023, unregistered, medium confidence) ([`techniques/flyline.md`](techniques/flyline.md)). A separate flyline build runs **60 lb braid to 35 lb fluoro**.
- **Swimbaits** — 50–65 lb braid to 60 lb fluoro, or 65 lb braid to 40–50 lb ([`techniques/swimbaits.md`](techniques/swimbaits.md)).
- **General braid class** — fish the lightest braid the job allows: **30 or 50 lb** mostly, up to **65** on a jig stick, **65–80** for casting at 100 lb-class bluefin; below 30 lb braid is too thin for a baitcaster (fine on spinning) ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), `aXF0bxAFtU0`).

---

## Tying parameters that decide whether it holds

**FG** ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), `CIMTyepgonk`):

- About **20** over-and-under wraps of braid up the leader, braid **under tension the whole time** — anchor it on the rod, your teeth, or a hitchpin.
- Lock with a **half hitch on the braid alone** so it can't slip while you finish, then **two half hitches around both lines** and cinch.
- **The tell:** the braid changes color as it constricts onto the leader. No color shift, it hasn't seated.
- Finish with a **four-wrap half hitch that you then unwrap** to cone-taper the knot, and trim the leader tag very close.

**Albright** ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), `NXtvXkqpT9w`):

- Form a loop ("shelf") in the leader, pass the braid up through and wrap it back **10 times** around the doubled leader, then feed the braid tag **back out the same end it entered** (top-down if you came bottom-up).
- Keep the leader loop **untwisted** or it won't lock.
- **Snug the leader first**, then work the braid tight so the final wrap seats into the knot.
- Trim tags **flat but not flush** — leave a little on each side so they can't pull back through.

**Failure modes** (same note): FG — too few wraps, or slack braid while wrapping (no color-change bite), or trimming the leader tag so tight the taper pulls. Albright — a twisted loop that won't cinch, or over-tight trims that let the flat tag slip.

**Video steps** are linked in the note: [FG](https://www.youtube.com/watch?v=CIMTyepgonk), [Albright](https://www.youtube.com/watch?v=NXtvXkqpT9w). Per the curation bar, the KB carries parameters and judgment, not step-by-step.

---

## One thing you should know before you commit to either

This KB does **not** actually name the FG or the Albright as its default SoCal braid-to-fluoro connection. [`rigging/essential-knots.md`](rigging/essential-knots.md) names the **RP knot (Royal Polaris / Roy Rose knot)** as "the preferred braid-to-fluoro leader join here" — small enough to pass the guides, **6 wraps up and 6 back down**, exit the loop the way you entered. It's "commonly tied to ~80 lb by the book, but it holds well beyond — tied clean to 100 lb and even ~130 lb," with a recounted **100 lb-plus bluefin landed on 65 lb braid to 80 lb fluoro, locked drag, no knot failure** (`YGLFn8lPMu0`; a second, independent naming and 6-and-6 corroboration at `AT6zmDYxjW4`, 2020-05-06).

So the real three-way call for a SoCal deck is: **RP** as the house braid-to-fluoro knot that passes guides and goes heavier than the Albright's documented span; **FG** when you want the absolute lowest profile on a casting stick and have prep time; **Albright** when you want speed or a big step up in leader diameter inside 8–100 lb. The KB never directly compares RP against FG or Albright, so that framing is me laying its notes side by side, not a doctrine statement from a source.

## Guides, and the option to dodge the question entirely

- **Knot inside the guides** → profile is the whole game: FG (or RP). If you're running a longer leader through the guides, use a **minimum guide size of 8** — many bass rods have size-6 guides that aren't leader-friendly ([`tackle/line-and-leader.md`](tackle/line-and-leader.md)).
- **Knot outside the guides** → the KB says a **double uni** is fast and reliable, with the trick being **9 turns on the braid side, 5 on the mono/fluoro side** (5-and-5 slips, 9-and-9 is bulky) ([`tackle/line-and-leader.md`](tackle/line-and-leader.md)).
- **Or keep the leader short enough that the knot never reaches the tip.** Capt. Dave Hansen (registered voice, high confidence) runs **3–4 ft of 80 lb fluoro** on a foamer flyline specifically so the connection stays below the tip guide and can't hang up on the cast (`RbqOKkINSCM`, 2021-05-25) ([`techniques/flyline.md`](techniques/flyline.md)).
- **On a mono top shot,** run it **long enough that the braid-to-mono knot never clears the spool on a full cast** — a 25 yd top shot on a 25 yd-plus cast is the classic way to lose a jig ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), `aXF0bxAFtU0`).
- **Hollow-core braid** sidesteps knots entirely: insert the fluoro leader and cinch it for a knotless connection ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), see [hollow splice](rigging/hollow-splice-and-serving.md)).

---

## What the KB does not answer

- **No stated FG line-class range** — one demo pair (50 lb braid → 80 lb leader) plus "it scales." No floor, no ceiling, no braid-to-leader diameter ratio.
- **No breaking-strength or percentage-of-line-strength comparison** between FG and Albright anywhere in the KB, despite the Albright video's "strongest" title.
- **No crossover threshold** — nothing says "FG below X lb, Albright above Y lb." The choice is given qualitatively (profile vs speed vs leader step-up) only.
- **No FG or Albright guidance above 100 lb** (bite leaders, kite flyers) — the KB routes that to loop-to-loop off a wind-on instead.
- **No direct comparison of FG or Albright against the RP knot**, which is the connection the KB actually calls preferred.
- **No word on tying FG or Albright to hollow-core braid.**


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `rigging/fg-and-albright.md`, `rigging/essential-knots.md`, `tackle/line-and-leader.md`, `techniques/surface-iron.md`, `techniques/flyline.md`, `techniques/swimbaits.md`, `species/spotted-bay-bass.md`, `species/california-halibut.md`, `sources/source-registry.md`, `sources/transcripts/_manifest.csv`, `sources/extraction-log.md`  
*videos:* `CIMTyepgonk`, `NXtvXkqpT9w`, `aXF0bxAFtU0`, `YGLFn8lPMu0`, `AT6zmDYxjW4`, `ILBl12Jm7-0`, `RbqOKkINSCM`, `P6Slg6RQiXw`, `9xNhdu2aBqE`, `F7jLrt2j2X8`  
*gaps admitted:* No stated FG line-class range — the KB gives only one worked example (50 lb braid to 80 lb leader) and the words 'the knot scales'; no floor, ceiling, or braid-to-leader diameter ratio. | No breaking-strength / percentage-of-line-strength comparison between the FG and the Albright anywhere in the KB. | No quantitative crossover threshold ('FG below X lb, Albright above Y lb') — the choice is stated only qualitatively as profile vs tying speed vs leader step-up. | The note's own guidance that FG is 'best when leader diameter is close to or thinner than what the wraps can bite into' sits unreconciled against its 50 lb braid to 80 lb leader demo and against handing 'notably heavier leader' to the Albright; the KB does not resolve it. | No FG or Albright guidance for the 100 lb-plus range (big-bluefin 80–150 lb leaders, 130–200 lb bite leaders, 300 lb kite flyers) — the KB routes those to loop-to-loop off a wind-on leader instead. | No direct comparison of FG or Albright against the RP knot, which essential-knots.md names as the preferred braid-to-fluoro join in SoCal. | No guidance on tying an FG or Albright to hollow-core braid (hollow is spliced knotlessly in the KB instead). | No Albright wrap-count variation by line class — 10 wraps is given flat, unlike the wrap-count ranges the KB records for the RP knot, San Diego jam, and uni-to-uni. | No per-application FG-vs-Albright assignment by line class beyond the note's qualitative application lists (surface iron / flyline / swimbaits for FG; bays, bluefin, yellowtail for Albright).

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# FG vs. Albright — the short version

The KB keeps both in one note, [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), and frames them as **two braid-to-leader knots that solve different problems**, not as better/worse:

- **FG** wraps the braid around a *straight* leader under tension and cinches it into the leader's surface — extremely low-profile, high-strength, braid to thin/strong fluoro.
- **Albright** wraps the braid around a *loop* formed in the leader and locks it — fast, flat-lying, and it shines going braid to heavier mono or fluoro.

The note's own one-line decision rule: **pick FG for the lowest profile and best guide-passing; pick the Albright when you want a faster tie or are joining to notably heavier leader.**

Note the confidence: `rigging/fg-and-albright.md` is `confidence: medium` and gated `regions: [socal-bight]`.

---

## The real decision axis: does the knot go through the guides?

[`tackle/line-and-leader.md`](tackle/line-and-leader.md) puts this cleanly in its Connections section:

- **Leader running through the guides → the FG knot is the smoothest braid-to-leader join.**
- **Leader kept outside the guides → you don't need either one** — a **double uni** is fast and reliable, with the trick being **9 turns on the braid side, 5 on the mono/fluoro side** (5-and-5 slips, 9-and-9 is bulky).
- If you want a longer leader living inside the guides, run a **minimum guide size of 8** — many bass rods have size-6 guides that aren't leader-friendly.

So before choosing between FG and Albright, decide leader length relative to your rod. Same note, from a San Diego kelp-calico seminar (`NXvqLUZ6qp8`): a common rule of thumb is a leader **roughly the length of the rod**, so the knot stays *outside* the tip guide and gets handled by hand at the boat. That build doesn't need the FG at all.

## When to reach for FG

Per [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md), reach for FG when the connection must reel through the guides cleanly and not slap on the cast:

- [surface iron](techniques/surface-iron.md)
- [flylining](techniques/flyline.md)
- [swimbaits](techniques/swimbaits.md)
- any lure-casting where a bulky knot would bump the tip guide

Stated qualifier: **best when leader diameter is close to or thinner than what the wraps can bite into.**

**Build spec** (from `CIMTyepgonk`, BD Outdoors, "How to FG Knot Step by Step"):

- About **20** over-and-under wraps of braid up the leader, braid under tension the whole time — anchor it to the rod, your teeth, or a hitchpin.
- Lock with a **half hitch on the braid alone** so it can't slip while you finish, then **two half hitches around both lines** and cinch.
- **The tell it seated:** the braid changes color as it constricts onto the leader.
- Finish with a **four-wrap half hitch that you then unwrap** to give the knot a cone taper; trim the leader tag **very close**.
- **Worked example: 50 lb braid to 80 lb leader.** The note says "the knot scales" but gives no other pound-test pair.

**FG judgment call, straight from the note:** it is the fussier of the two — **tie it during prep the night before or dockside, not in a frenzy with fish boiling.** Take that seriously; the failure mode is real (below).

## When to reach for Albright

Per the same note, the Albright is the all-round braid-to-solid-mono/fluoro knot:

- **Bays** — [spotted bay bass](species/spotted-bay-bass.md), [halibut](species/california-halibut.md)
- **Offshore** — [bluefin](species/bluefin-tuna.md) and [yellowtail](species/yellowtail.md)
- Even freshwater. It handles a wide pound-test span and lays its tags flat.

**Line classes — this is where the Albright has the KB's only explicit range:** tied from roughly **8 lb to 8 lb, up to 80 lb to 100 lb.** That's the widest span any braid-to-leader knot is given in this KB.

**Base build:** form a loop ("shelf") in the leader, pass the braid up through, wrap back **10 times** around the doubled leader, then feed the braid tag back out the same end it entered (top-down if you came bottom-up). **Keep the leader loop untwisted or it won't lock.** Snug the leader first, then work the braid tight so the final wrap seats. **Trim the tags flat but not flush** — leave a little on each side so they can't pull back through (`NXtvXkqpT9w`).

**Hollow spectra:** Captain Armando on SearcherSportfishing "Tackle Talk Live: Bluefin Tuna" (`shZCjX2-fkI`, 2021-01-14) confirms the identical Albright is tied on that boat's **kite outfits, which commonly run hollow spectra** — rather than needle-splicing the hollow line, the crew ties the Albright straight onto it "as if it was solid."

### The wrap counts do not agree — and the KB keeps them side by side

Five sourced Albright wrap patterns, deliberately unreconciled. Use whichever cinches cleaner for you:

| Variant | Wraps | Source |
| --- | --- | --- |
| Base, one direction around doubled leader | **10** | `NXtvXkqpT9w` |
| Double-back (wrap down, then back over the same wraps, same direction, same count) — tag through loop once or twice | **5–7** each pass | Norm Fujimoto, Izorline, `Bn9fRKUmQ-U`, 2019-05-16 — "for any test line," no pound-test range stated |
| Spaced-then-overlap, aka "Modified Albright" (space the wraps going down, reverse, overlap into the spaces coming back) | **9** in the 2019 demo; **7–10** stated range, **7** tied on camera in 2021 | `-BO1lMCTamg` (2019-10-10) and Ryan, `5472APCgym8` (2021-05-20). Stated reason: spacing then overlapping "cinches everything down" and finishes "a little bit smaller" |
| Dissimilar-line version (his example: 30 lb main line to a heavier leader), **wet it right before the final cinch**, then drop the tags and pull only the two main lines — it rolls into a tight barrel | **6–7**, with **"no dead-set number"** — wrap "until I got a good looking length of my knot" | Rick, Fisherman's Landing Tackle, `2fwj24S9S-o`, 2023-03-16 |
| 6–7 down / 6–7 back up, return wraps landing between the first pass's loops | **6–7** each way | Capt. Armando, `shZCjX2-fkI`, 2021-01-14 — called on camera "the easiest knot to tie" for spectra to mono/fluoro |

## Failure modes — the actual reason you'd pick one over the other

From `rigging/fg-and-albright.md`:

- **FG:** too few wraps, or slack braid while wrapping (no color-change bite); or trimming the leader tag so tight the taper pulls.
- **Albright:** a twisted loop that won't cinch, or over-tight trims that let the flat tag slip.

[`rigging/surgeons-knot-mono-to-fluoro.md`](rigging/surgeons-knot-mono-to-fluoro.md) logs a compatible caution from a separate source — cinch fully *before* trimming, or the knot can slip after the trim.

The FG's fussiness has its own corroboration. [`rigging/pr-knot.md`](rigging/pr-knot.md) carries a Tackle Express presenter (Cesar Chang) stating he's watched FG knots tied "rather quickly" and not exactly correctly **slip out and fail** — which is the argument for the **PR knot**, tied with a weighted **PR bobbin** so the tool holds constant tension instead of your hands. He cites (secondhand, from unnamed destruction-machine testing) the **PR at 100%** and the **FG at approximately 98%**. Treat that carefully: **no test source, sample size, or line class is given**, and the KB flags that four video IDs (`To2Dvx3Ifnc`, `ZrcwcugaEe4`, `foLSQJ5oRWI`, `wk8bkqzdyM0`) are **re-cuts of one interview, not four independent confirmations**. The PR is offered as an alternative to the **FG specifically — not to the Albright.**

## Practical line-class picks, using this KB's actual SoCal braid/leader brackets

The FG/Albright note gives one FG example (50→80) and the Albright's 8→8 to 80→100 span. To turn that into real picks, here are the braid and leader classes [`tackle/line-and-leader.md`](tackle/line-and-leader.md) actually specifies, mapped to the knot that fits:

**Bay / inshore bass, halibut — Albright is the note's named home, FG if you're casting hard at structure**
- Braid mostly **30 or 50 lb** — downsize, don't upsize; 65 lb braid is roughly the diameter of 20 lb mono, and **below 30 lb** braid is too thin for a baitcaster (fine on spinning) (`aXF0bxAFtU0`).
- Leader **heavier than braid** where you can tangle (kelp, eelgrass, anchor lines, riprap): **30 lb braid + hard bait → 40 lb leader; weedless swimbait on 50 lb braid → 60 lb leader**.
- Kelp / boiling rock: **50–65 lb braid to 20 lb fluoro** (`NXvqLUZ6qp8`). Action-preserving swimbait build: **40 lb braid to 20–25 lb fluoro**, because 30 lb starts to deaden the bait (`lP6cg4eEU6s`).
- All of these sit inside the Albright's stated span, and the lighter ones (40 lb braid to 20–25 lb fluoro) are where the FG's "leader close to or thinner than the braid" qualifier is most comfortable.

**Surface iron / jig stick — FG, because it lives in the guides**
- **Up to 65 lb** braid on a jig stick (`aXF0bxAFtU0`). One counter build: **65 lb spectra backing + ~100 yd of 40 lb mono top shot**, stepped to **50 lb** for bluefin (`3g82igEL8yk`). Another: **40 lb main line to a 20 lb fluoro leader** (`49joKHD7Umc`).

**Offshore top shots, paddy fish and small-to-mid tuna**
- **15–40 lb fluoro** (`xPFm_ZV2PZU`) — comfortably inside both knots' territory.

**Big bluefin — this is where you leave both knots behind**
- Casting at 100 lb-class bluefin runs **65–80 lb braid** (`aXF0bxAFtU0`). Kite / flat-fall / sinker rigs run **80–150 lb fluoro leader, loop-to-loop off a [wind-on leader](rigging/wind-on-leader.md)**, often crimped to a snap swivel, with a short **130–200 lb [bite leader](rigging/bite-leaders.md)** as the critical last link.
- The KB's only stated pound-test **ceiling** for a hand-tied braid-to-leader connection is on a *different* knot: Pete Gray, in [`rigging/john-collins-knot.md`](rigging/john-collins-knot.md) (`b-oixz7pgAo`, 2021-06-10), uses the John Collins/RP knot **up to about 80 lb test** and switches **above 80 lb** to a loop-to-loop with a **Sato crimp** on a wind-on leader. That ceiling is stated for John Collins/RP, **not** for the FG or Albright — but it lines up with the Albright's own stated top end of 80→100, and it's the direction the fishery goes at that grade.

## One thing worth knowing before you commit

FG and Albright are not the KB's default. [`rigging/essential-knots.md`](rigging/essential-knots.md) and [`rigging/rp-knot.md`](rigging/rp-knot.md) name the **RP knot (Royal Polaris)** as *the preferred braid-to-fluoro leader join in this corpus* — small enough to pass the guides, **6 wraps up and 6 back down**, and it has something neither the FG nor the Albright has here: **a wrap rule that scales with the line-diameter ratio** (lighter line, more wraps; heavier line, fewer) — **65 lb braid to 25 lb mono top shot → 7 wraps**, **100 lb braid to 80 lb top shot → 5 wraps**, stated as the floor (`p1KyyR0i7Kc`). Commonly tied to ~80 lb by the book, and it holds tied clean to 100 lb and even ~130 lb (`YGLFn8lPMu0`).

If your goal is one low-profile guide-passing knot to learn well, the KB's own corpus points at the RP first, with the FG as the higher-effort, lowest-profile option and the Albright as the fast, wide-range one.

## Bottom line

| | FG | Albright |
| --- | --- | --- |
| **Reach for it when** | The knot must reel through the guides and not slap on the cast — surface iron, flyline, swimbaits | You want a faster tie, or you're joining to notably heavier leader; bays through offshore |
| **Line classes in the KB** | One worked example: **50 lb braid → 80 lb leader**, "the knot scales." Best when leader is close to or thinner than the braid | **8 lb → 8 lb up through 80 lb → 100 lb** — an explicitly wide span |
| **Wraps** | ~**20**, under constant tension | **10** base; sourced variants at 5–7, 6–7, 7–10, or "no dead-set number" |
| **Tie it when** | Dockside or the night before — it's the fussier of the two | On the fly; it's the fast one |
| **Hollow spectra** | Not addressed | Confirmed — tied on hollow "as if it was solid" on kite outfits |

**Tie-it videos** (from the note): [FG step by step](https://www.youtube.com/watch?v=CIMTyepgonk), [the Albright](https://www.youtube.com/watch?v=NXtvXkqpT9w), [double-back variant](https://www.youtube.com/watch?v=Bn9fRKUmQ-U), [spaced-then-overlap variant](https://www.youtube.com/watch?v=-BO1lMCTamg), [the same retied as "Modified Albright"](https://www.youtube.com/watch?v=5472APCgym8), [dissimilar-line variant](https://www.youtube.com/watch?v=2fwj24S9S-o).

---

## What this KB does not answer

I want to be straight about the edges of what I could actually source:

- **No numeric line-class boundary for the FG.** One worked pair (50 lb braid → 80 lb leader) plus "the knot scales." There is no stated floor, ceiling, or "above X lb, don't."
- **No diameter-ratio wrap rule for the FG** the way the RP knot has one — the ~20-wrap count is given flat, not scaled to line pairing.
- **The FG's "leader close to or thinner than the braid" qualifier sits oddly next to its own 50→80 demo** (leader heavier than braid), and the KB never resolves that.
- **No head-to-head break test.** The only strength figure anywhere is the secondhand FG ≈98% / PR = 100% claim, with no line class, no sample size, no named test — and from four re-cuts of a single interview.
- **The five Albright wrap counts are not tied to line classes.** Nobody says "use 10 at 80 lb, 6 at 20 lb." You pick by feel.
- **FG on hollow spectra is unaddressed** — only the Albright is confirmed there.
- **Neither knot is given guidance above 100 lb.** The >80 lb → Sato-crimp loop-to-loop rule is stated for the John Collins/RP knot, not for these two.
- **No mono-vs-fluoro leader distinction** is drawn for either knot.
- **Region gating:** `rigging/fg-and-albright.md` is gated `regions: [socal-bight]` only, so nothing here is stated as Baja-specific.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `rigging/fg-and-albright.md`, `rigging/pr-knot.md`, `rigging/rp-knot.md`, `rigging/essential-knots.md`, `rigging/john-collins-knot.md`, `rigging/slim-beauty-knot.md`, `rigging/surgeons-knot-mono-to-fluoro.md`, `tackle/line-and-leader.md`, `techniques/surface-iron.md`, `techniques/flyline.md`, `techniques/swimbaits.md`  
*videos:* `CIMTyepgonk`, `NXtvXkqpT9w`, `-BO1lMCTamg`, `2fwj24S9S-o`, `5472APCgym8`, `Bn9fRKUmQ-U`, `shZCjX2-fkI`, `To2Dvx3Ifnc`, `ZrcwcugaEe4`, `foLSQJ5oRWI`, `wk8bkqzdyM0`, `aXF0bxAFtU0`, `xPFm_ZV2PZU`, `NXvqLUZ6qp8`, `lP6cg4eEU6s`, `3g82igEL8yk`, `49joKHD7Umc`, `b-oixz7pgAo`, `p1KyyR0i7Kc`, `YGLFn8lPMu0`  
*gaps admitted:* No stated line-class floor or ceiling for the FG knot — only one worked pair (50 lb braid to 80 lb leader) and the phrase 'the knot scales'. | No diameter-ratio wrap rule for the FG knot (the ~20-wrap count is flat), unlike the RP knot which has a sourced wrap-by-line-ratio rule. | The FG note's 'leader close to or thinner than the braid' qualifier is never reconciled with its own 50 lb braid to 80 lb leader demonstration. | No head-to-head break-strength test of FG vs Albright at any named line class; the only strength figure (FG ~98% vs PR 100%) is secondhand, gives no line class or sample size, and comes from four re-cuts of a single interview. | The five sourced Albright wrap counts (10; 5-7; 6-7; 7-10; 'no dead-set number') are kept side by side and none is tied to a specific line class. | FG knot on hollow spectra is not addressed anywhere; only the Albright is confirmed tied on hollow as if solid. | Neither FG nor Albright is given guidance above 100 lb — the >80 lb Sato-crimp loop-to-loop ceiling is stated for the John Collins/RP knot, not for these two. | No mono-vs-fluorocarbon leader distinction is drawn for either knot. | rigging/fg-and-albright.md is region-gated socal-bight only, so no Baja-specific guidance for either knot exists in the KB.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short version

The KB treats these as **two braid-to-leader knots that solve different problems**, not as a strength ranking ([`rigging/fg-and-albright.md`](rigging/fg-and-albright.md)):

- **FG** — the braid is wrapped around a *straight* leader under tension and cinched into the leader's surface. Lowest profile of the two. Reach for it when the connection has to **reel in and out through the guides cleanly and not slap on the cast**.
- **Albright** — the braid is wrapped around a *loop* formed in the leader and locked. Faster to tie, lays its tags flat, and is the one the note points at when you're **joining to notably heavier leader**.

The note's own one-liner: *pick FG for the lowest profile and best guide-passing; pick the Albright when you want a faster tie or are joining to notably heavier leader.*

Both notes are gated `regions: [socal-bight]`, `waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]` — i.e. nothing here is region-limited within the Bight.

---

## FG knot

**When (from [`rigging/fg-and-albright.md`](rigging/fg-and-albright.md)):** surface iron, flylining, swimbaits — any lure-casting where a bulky knot bumps the tip guide. Best when the leader diameter is close to or thinner than what the wraps can bite into.

**Line class the KB actually documents:** **50 lb braid to an 80 lb leader** — that is the only class the FG is demonstrated at in the corpus (`CIMTyepgonk`). The note's own front matter says "scales to other classes," but it carries a standing **⚠ fact-check (contradicted-by-source)** flag: the transcript hedges even its own weight ("I think this is 50 pound... 80 pound Gold Label") and never says the knot scales. That flag is live in [`sources/fact-check-ledger.md`](sources/fact-check-ledger.md) (rows for `rigging/fg-and-albright.md`). So treat 50/80 as the documented class and everything above/below as untested in this KB, not as a rule.

**One second, heavier documented FG use:** the direct-tie school for bluefin knife jigging runs **80–100 lb braid, FG knot to a 15–20 ft mono/fluoro top shot tied straight to the jig, no crimp** (West Coast Jiggerz, `j37zxs33gws`) — [`rigging/bite-leaders.md`](rigging/bite-leaders.md). That's the alternative to the crimped ≤2.5 ft, 130 lb bite-leader school; both are fished in the SoCal bluefin fleet and the note keeps them side by side.

**Parameters (`CIMTyepgonk`):**
- About **20 over-and-under wraps** of braid up the leader, braid held under tension the whole time (anchor it — rod, teeth, or hitchpin). ⚠ single-source flag on the wrap count.
- Lock with a half hitch on the braid alone, then two half hitches around both lines, then cinch.
- **The braid changes color as it constricts onto the leader — that color shift is the tell it seated.**
- Finish with a four-wrap half hitch that you then *unwrap* to give the knot a cone taper; trim the leader tag very close.

**Judgment:** it's the fussier of the two. Tie it **during prep the night before or dockside, not in a frenzy with fish boiling** (`CIMTyepgonk`).

**Failure modes:** too few wraps or slack braid while wrapping (no color-change bite); trimming the leader tag so tight the taper pulls.

---

## Albright knot

**When:** the note calls it the all-round braid-to-solid-mono/fluoro knot — bays (spotties, halibut), offshore for bluefin and yellowtail, even freshwater. Handles a wide pound-test span and lays its tags flat.

**Line class:** tied from roughly **8 lb-to-8 lb up to 80 lb-to-100 lb** (`NXtvXkqpT9w`) — a much wider documented span than the FG's single demoed class. ⚠ single-source flag on that span too. One variant is demoed at **30 lb main line to a heavier leader** and framed generally as a knot for joining two lines of *dissimilar diameter/strength* (`2fwj24S9S-o`).

**Base method (`NXtvXkqpT9w`):** form a loop ("shelf") in the leader, pass the braid up through and wrap it back **10 times** around the doubled leader, then feed the braid tag back out the same end it entered (top-down if you came bottom-up). Keep the leader loop untwisted or it won't lock. Snug the leader first, then work the braid tight so the final wrap seats. Trim the tags **flat but not flush** — leave a little on each side so they can't pull back through.

**Wrap count is a presenter preference, not a class rule.** The note logs four documented patterns; the shared requirement is a **fully cinched knot before trimming** — a loose wrap or an early trim is what lets the tag slip under load:

| Variant | Wraps | Source |
| --- | --- | --- |
| Double-back wrap (wrap up, then back down over the same wraps) | **5–7**, doubled in place; framed as usable for any line class, no pound-test range stated | `Bn9fRKUmQ-U` |
| Spaced-then-overlap ("Modified Albright") — wrap spaced, reverse, wrap back through the spaces | **9** tied on camera in one clip; **7–10** stated range with **7** tied in the other. Cinches down smaller than a one-way wrap | `-BO1lMCTamg`, `5472APCgym8` |
| Dissimilar-diameter version | **No fixed count** — "six or seven until it looks right"; wet the knot right before it stops moving, pull only the two main lines to seat it into a tight barrel | `2fwj24S9S-o` |
| 6-7 down / 6-7 back up, return loops between the first pass's | **6–7 each way**; also tied **unmodified straight onto hollow spectra** on kite outfits instead of needle-splicing, "as if it was solid" | `shZCjX2-fkI` |

That last one is worth knowing if you run hollow: a Searcher kite outfit gets the same Albright rather than a splice.

**Cinch sequence on the spaced-overlap version (`-BO1lMCTamg`, `5472APCgym8`):** pull both tags and the main line together; it cinches, then stops — release the braid tag and pull again, release the leader tag and pull tight. Trim **only** once fully cinched.

**Failure modes:** a twisted leader loop that won't cinch, or over-tight trims that let the flat tag slip.

---

## Picking by line class — what the KB supports

| Situation | Class | Knot the KB points to |
| --- | --- | --- |
| Light bay / finesse — e.g. Ned rig at 10 lb braid / 8 lb leader ([`species/spotted-bay-bass.md`](species/spotted-bay-bass.md), `GVP3IChsmRQ`, `um5MAeCjNDg`) | 8–20 lb | **Albright** — its 8-to-8 lb floor is the only one of the two documented that light. The KB gives no FG data down here. |
| Kelp/rock swimbaits — **50–65 lb braid to 60 lb fluoro**, or 65 lb braid to 40 lb mono ([`techniques/swimbaits.md`](techniques/swimbaits.md), `YIABTTYXeqc`, `n6PTy8g3pb0`, `9xNhdu2aBqE`) | 50–65 lb braid | **FG** is the named use case (swimbait casting, guide-passing). Note the leader here is *heavier* than the braid, which is the FG's weaker geometry per its own "when to use." Albright is the documented answer for heavier-leader joins. |
| Surface iron — **~80 lb braid, short 50 lb mono/fluoro leader ~18 in** to a 100 lb clip ([`techniques/surface-iron.md`](techniques/surface-iron.md)) | 80 lb braid / 50 lb leader | **FG** — leader thinner than braid, and the jig-stick cast is exactly the slap-on-the-cast problem it solves. |
| Bluefin knife jig, direct-tie school — **80–100 lb braid to a 15–20 ft top shot** (`j37zxs33gws`) | 80–100 lb | **FG**, documented at this class in [`rigging/bite-leaders.md`](rigging/bite-leaders.md). |
| Braid to notably heavier leader, any class in the 8–100 lb span | 8–100 lb | **Albright.** |

The underlying leader-vs-braid logic the knot has to serve is in [`tackle/line-and-leader.md`](tackle/line-and-leader.md) (`aXF0bxAFtU0`): **leader heavier than braid** when you fish stuff you can tangle in (30 lb braid + hard bait → 40 lb leader; weedless swimbait on 50 lb braid → 60 lb leader); **leader significantly lighter than braid** when you snag bottom and must break off. Offshore top shots run 15–40 lb fluoro for paddy fish and small-to-mid tuna, 80 lb and up for bigger bluefin (`xPFm_ZV2PZU`).

Also from that note, and it matters more than knot choice: **run the top shot long enough that the braid-to-leader knot never clears the spool on a full cast** — a knot dragged through the guides hangs up, backlashes, and braid's zero stretch then snaps the leader and loses the jig, even at 40 lb (`aXF0bxAFtU0`).

---

## The neighbors, so you know when neither is the answer

- **PR knot** — presented as a direct alternative to the **FG specifically** (not the Albright): a weighted PR bobbin holds constant tension instead of your hands, addressing the FG's fussiest failure mode, quick sloppy ties slipping out ([`rigging/pr-knot.md`](rigging/pr-knot.md), `To2Dvx3Ifnc`). The only strength figures anywhere in the KB for the FG come from here and are secondhand: PR at 100%, FG at ~98%, referencing unnamed destruction-test videos, no line class, sample size, or testing source given — flagged in the note.
- **RP knot** — the KB's preferred braid-to-fluoro join for sport-boat work, with an actual **wrap-by-diameter-ratio rule** (5-wrap floor at 100 lb braid/80 lb topshot up to 9–11 wraps at 20 lb braid/6 lb topshot), ~80 lb "by the book," clean to 100 and tested to ~130 ([`rigging/rp-knot.md`](rigging/rp-knot.md), [`rigging/essential-knots.md`](rigging/essential-knots.md), `b-oixz7pgAo`). If you want a class-scaled wrap rule, the RP note has one and the FG/Albright note does not.
- **Slim beauty** — same low-profile, guide-passing job by different construction ([`rigging/slim-beauty-knot.md`](rigging/slim-beauty-knot.md)).
- **Wind-on / hollow splice** — at the top of the range the KB stops tying knots: 100 lb braid to 100 lb fluoro matched, 130 lb braid to a 100 lb leader workable, 130-to-40 fails; heavy night-bluefin builds run 130–200 lb, ~25 ft ([`rigging/wind-on-leader.md`](rigging/wind-on-leader.md), `zkSKgP2bq10`). Requires hollow-core braid. The John Collins note states its own ceiling explicitly — above ~80 lb, switch to loop-to-loop with a Sato crimp on a wind-on ([`rigging/john-collins-knot.md`](rigging/john-collins-knot.md)) — but **no such ceiling is stated for the FG or the Albright**; that's my inference from the neighboring notes, not KB doctrine.

---

## Confidence, honestly

[`rigging/fg-and-albright.md`](rigging/fg-and-albright.md) is `confidence: medium`. The FG build rests on **one video** (`CIMTyepgonk`) and the base Albright on **one** (`NXtvXkqpT9w`), each with a standing single-source flag in [`sources/fact-check-ledger.md`](sources/fact-check-ledger.md); the five Albright variants are Searcher Tackle Tip Thursday clips. `searcher-sportfishing` is a registered channel in [`sources/source-registry.md`](sources/source-registry.md) (promoted 2026-08-19), though the note's evidence file still labels several of those clips "unregistered — medium confidence." Single-source is not wrong; it just means one more source could move any of these numbers.

Tying videos are linked in the note's "Tie it" section — the KB captures parameters and judgment, not step-by-step, so watch the clip for the hands.

## What the KB does not answer

- No stated **upper line-class limit** for the FG, and no per-class FG wrap-count table — the 20-wrap count is documented at one class only.
- No **wrap-count-by-pound-test rule for the Albright** — the counts vary by presenter (5–7, 7–10, 6–7/6–7, "no dead-set number"), not by class. The RP knot has that rule; these two don't.
- No **head-to-head strength test** of FG vs Albright at named line classes anywhere in the corpus.
- No **leader-to-braid diameter ratio rule** for the FG, which is exactly the axis its "when to use" turns on.
- No FG data at **light/bay classes** (8–20 lb) at all.
- Nothing from `cameron` on either knot — no personal preference in the KB, and nothing in [`profiles/cameron/`](profiles/cameron/) that names which he ties.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `rigging/README.md`, `rigging/fg-and-albright.md`, `rigging/evidence/fg-and-albright.md`, `rigging/essential-knots.md`, `rigging/pr-knot.md`, `rigging/bite-leaders.md`, `rigging/wind-on-leader.md`, `rigging/hollow-splice-and-serving.md`, `rigging/slim-beauty-knot.md`, `rigging/john-collins-knot.md`, `rigging/rp-knot.md`, `rigging/tony-pena-knot.md`, `rigging/surgeons-knot-mono-to-fluoro.md`, `tackle/line-and-leader.md`, `techniques/surface-iron.md`, `techniques/swimbaits.md`, `techniques/flyline.md`, `species/spotted-bay-bass.md`, `species/california-halibut.md`, `sources/fact-check-ledger.md`, `sources/extraction-log.md`, `sources/source-registry.md`  
*videos:* `CIMTyepgonk`, `NXtvXkqpT9w`, `Bn9fRKUmQ-U`, `-BO1lMCTamg`, `5472APCgym8`, `2fwj24S9S-o`, `shZCjX2-fkI`, `To2Dvx3Ifnc`, `j37zxs33gws`, `aXF0bxAFtU0`, `xPFm_ZV2PZU`, `zkSKgP2bq10`, `YIABTTYXeqc`, `n6PTy8g3pb0`, `9xNhdu2aBqE`, `GVP3IChsmRQ`, `um5MAeCjNDg`, `b-oixz7pgAo`  
*gaps admitted:* No upper line-class limit is stated anywhere in the KB for the FG knot, and no per-class FG wrap-count table exists — the 20-wrap spec is documented at 50 lb braid / 80 lb leader only, and the note's 'scales to other classes' line carries a standing contradicted-by-source flag. | No wrap-count-by-pound-test rule for the Albright — the four documented variants differ by presenter (5-7 doubled, 7-10 spaced-overlap, 6-7 down/6-7 up, 'no dead-set number'), not by line class. | No head-to-head strength test of FG vs Albright at named line classes; the only strength figures in the KB are a secondhand PR-vs-FG claim (100% vs ~98%) with no line class, sample size, or testing source named. | No leader-to-braid diameter ratio rule for the FG knot, even though its 'when to use' turns on leader diameter relative to the braid (the RP knot has such a rule; the FG does not). | No FG data at light or bay line classes (roughly 8-20 lb) — only the Albright is documented down to 8 lb-to-8 lb. | Nothing sourced to cameron on either knot — no stated personal preference in the KB and nothing in profiles/cameron/ naming which of the two he ties. | The KB never states when to stop using FG or Albright and move to a wind-on/hollow splice; the 100-200 lb heavy-class doctrine lives in the wind-on note without cross-referencing a FG/Albright ceiling.

</details>

### 19. [rigging] How do I bleed and chill a tuna properly on a small boat?

**Winner:** NOW · mapping {'A': 'B2', 'B': 'B3', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three deliver the same core chain with the same hard numbers (2 cups rock salt per 7-10 lb bag, 3/4 cup table salt to ~32F, 2h / 3-5h / overnight chill table, gaff sizing by grade) and all three are honest about the KB not writing out the actual bleed cut or the ikejime spike placement. C separates itself on three concrete things: it attaches a real video id (5to3Q5P7w90) to the slurry ratio, wet-towel step and chill table that A and B could only attribute vaguely to "BD Outdoors reporting"; it carries the operational corrections a small-boat angler most needs — a deck hose-down at high-70s F is not chilling, a car cooler if the drive exceeds ~10 minutes, and dorado on a mixed day are the opposite call (ice, do not bleed); and it is the only one to give a decision frame for the three competing kill/bleed/gut orderings rather than just listing them, plus the only correctly stamped regulation (CDFW, two per person per day, as of 2024-11, verify current). B is a close second and beats C on the pre-gaff boat-handling layer (big gentle circles, forward only, ~45 degrees on a 20-30 ft boat). A is the weakest only in small-boat translation: it names the gaps well but offers little beyond the ice-load figure to act on.

- *B2 reasons:* found: complete gaff→bleed/gill-and-gut→wet towel→slurry→chill-time→dockside chain from fish-care notes, and says up front there is no small-boat-specific note. specific: 2 cups rock salt per 7-10 lb bag, 3/4 cup table salt to ~32F, 2h/3-5h/overnight chill table, 3-in/6-ft vs 6-in/8-ft gaffs, length×girth²÷800 worked to 181 lb, 3-day/1-3-month storage windows. sourced: note paths plus video ids (w6DDCSLu8vM, I84uoay_jwQ, JeexIvtUkZc, usHl-4SfqDA, Klfb433I3Uk, 2gHRrR3D8rY) and it flags that the slurry ratio carries no video id in its version. scoped: RSW correctly labeled 85-ft charter and not small-boat; yellowtail data point labeled cross-species; states no regulation rather than guessing one. honest: names medium/low confidence on tuna-care and gaffing, labels its salt arithmetic as its own, long candid gap list. actionable: the chain itself is executable, but the small-boat translation is thinnest of the three — only Cameron's 100-125 lb ice figure, no capacity/kill-bag guidance, no decision frame for the competing kill/bleed/gut orderings it lists, no mixed-day species traps.
- *B3 reasons:* found: same care chain plus the pre-gaff boat-handling layer (fighting-big-bluefin) and the Baja panga capacity lesson, which is the only capacity material in the KB. specific: 20-30 ft boat, big gentle circles, forward only, ~45 degrees, 22-ft center-console counterpoint, gaff sizing by grade, all-hands/double-gaff at 100-115 lb, full slurry and chill numbers, 181 lb tape estimate. sourced: paths plus ids on nearly every parameter (Q196GVwVqro, rsCAh-QyK60, OIiDJu4mx44, elBPRrdkugU, usHl-4SfqDA, P36VGPPf120) and channel-registry caveats. scoped: kill-bag/ice advice explicitly region-labeled cortez-north and not SoCal doctrine; RSW ruled out as big-boat; yellowtail bleed flagged as not tuna; no regulation asserted, gap named. honest: names two unreconciled orderings and says the KB gives no decision frame, flags missing gaff/kill bag/rock salt/spike in the profile, no relative time. actionable: a two-person crew could run the fight, the gaff shot, the bleed and the cold chain from this.
- *NOW reasons:* found: full chain plus the items the others miss — the deck-hose-is-not-chilling correction (high 70s F), the >10-minute car-cooler rule, dorado's do-not-bleed opposite call, and the yellowfin/skipjack flagged gaps. specific: same slurry and chill numbers with the source video attached, 36F RSW, ~32F loin rinse, gaff sizing, 181 lb tape estimate, ice-load arithmetic shown and labeled as arithmetic. sourced: strongest cite density and cites verified against the notes (5to3Q5P7w90 carries the wet towel, slurry ratio, deck-hose figure and all three chill times; evidence file cited for mDmbGdQAy-4/H-vIGWPIPVc). scoped: Bahía de los Ángeles advice tagged cortez-north and not SoCal doctrine; the one legal claim — two Pacific bluefin per person per day — carries California/CDFW, as of 2024-11, single-source flag, and verify-with-CDFW, matching the note. honest: opens with the missing-small-boat-note caveat, gives a provenance paragraph admitting the core numbers rest on one video and several supports are an unregistered channel capped at medium, and the longest concrete gap list. actionable: three-ordering table with an explicit decision frame (ikejime only for sashimi), boat-specific constraints (no house battery so RSW is out, overnight-hold problem, bleed away from the rail with sea lions working), and named missing tools.

<details><summary>Full prompt</summary>

How do I bleed and chill a tuna properly on a small boat?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Bleeding and chilling a tuna on a small boat

Everything below comes from `fish-care/` in this KB. Two honesty notes up front: **`fish-care/tuna-care.md` is `confidence: medium` overall** (most of the on-the-water detail comes from StokedOnFishing, an unregistered channel), and **the KB deliberately does not write out the cuts** — it holds parameters and judgment and points you at the linked videos for the hands-on motions. There is also **no small-boat-specific care note** in this KB; the chain below is the general tuna chain, and I flag where the small-boat questions go unanswered.

---

## The chain, in order

**1. Boat it without wrecking it — the gaff is step one of care**
(`fish-care/tuna-care.md`, `fish-care/gaffing.md`)

- Doctrine A: aim the gaff at the **head/shoulder**, not mid-body or tail — a head-forward shot controls the fish and keeps the gaff out of the meat. Gaff on a committed pass with the fish's head coming toward you, not a wild swing (`w6DDCSLu8vM`).
- Doctrine B, kept side by side rather than merged: **aim for the pec and flip the fish upside down the instant it's gaffed** — a bluefin has never been upside down in its life, and it stuns it dead, "300 lb or 20 lb." Do **not** gaff the back, tail, or side of the head — the fish keeps driving and rips the gaff out of your hands (`I84uoay_jwQ`, repeated non-sponsored in `8jC61LzQoxU`). `fish-care/gaffing.md` sits at `low` confidence because the primary source is a sponsored gaff spot — treat the placement doctrine as directional, not gospel.
- **Hook orientation — "don't dig a hole":** never gaff with the point aimed away from the boat and pull outward. Turn the point back toward you and drag it **across the top of the water toward the boat** (or come up from underneath for the pec shot) so the stroke pulls the fish in, not away.
- **Landing:** hand over hand straight up onto the deck. Do not lift it like you're fighting it on a rod — that's how fish fall off the gaff.
- **Small-boat safety, which matters more the smaller the deck:** never stand the gaff butt-down with the hook up near head height while people are moving around. Rest it on the gunnel hook-up-and-out-of-the-way, or in a rod holder if the butt fits. Keep your hands off it until the shot.
- Gaff sizing: **6-in hook, ~8-ft gaff** for SoCal bluefin at the 200–300 lb grade; **3-in hook, ~6-ft gaff** for fish up to 40–50 lb (`I84uoay_jwQ`).

**2. Bleed and gill-and-gut immediately, on the water — before ice**
(`fish-care/tuna-care.md`)

- **Bleed it** so the meat doesn't hold blood, then **field-dress it: pull the guts and the gills.** The reason is thermal, not cosmetic — pulling gills and viscera removes the warm mass and the enzymes that spoil quality fastest, so the slurry cools the carcass instead of fighting a bellyful of heat. Walkthrough for the actual cuts on a bluefin: `JeexIvtUkZc`.
- One source describes the mechanism the same way: **cutting/pulling the gill opens the bloodline**, which bleeds the fish out and kills it faster — done boat-side immediately, fish on ice right after (`H-vIGWPIPVc`, StokedOnFishing, 2019-10-30, San Clemente Island — species not clearly diarized; the boat's catch that trip was yellowfin and bonito).
- A charter operation's stated order is **bleed, kill, then gut, immediately on landing** — followed by **packing the body cavity itself with ice and completely covering the fish** (`usHl-4SfqDA`, 2024-11-13). The cavity-packing detail is the useful addition for a small boat: an open, ice-packed cavity is how you get cold into the core when you can't submerge the whole fish.
- **Cross-species data point, flagged as such:** on a **yellowtail** (not a tuna), the practice was to **cut the artery as soon as the fish hits the deck** — "almost all the fish's blood goes through this artery within a matter of minutes" — then hold the fish **upside down in a bucket for ~5 minutes**, then ice it (`Klfb433I3Uk`, 2019-10-04, San Clemente Island). The KB logs this here because there's no yellowtail bleed note; the exact cut location was never specified beyond "down here" on camera. The upside-down-in-a-bucket trick scales to a small boat well.

**3. Ikejime if you're after sashimi — on top of bleeding, never instead of it**
(`fish-care/ikejime.md`, `WzT0RSHpaQc`)

- **Brain spike** to kill the fish instantly at a target point on the head; the related step is **pithing** — running a wire down the spinal cord to destroy the nerve line, so the whole nervous system shuts down and the fish doesn't thrash quality into the meat.
- The full quality chain stacks: **kill clean (ikejime) → bleed → field-dress → chill in the slurry.** Ikejime does not replace the slurry.
- Worth it for **sashimi-grade** flesh. For a fish headed to the smoker or grill, bleed-and-chill will carry it. The KB is explicit that **exact spike placement and depth are not in prose here** — that comes from the video and practice.

**4. Wet-towel cooldown before the ice**
(`fish-care/tuna-care.md`)

Knock the surface heat off the dressed carcass with a **wet towel** before it goes into the slurry. Dropping a hot fish straight into ice is less effective than letting it shed the worst of its heat first, then committing it to the cold.

**5. The below-freezing slurry — the actual numbers**
(`fish-care/tuna-care.md`, same numbers restated as universal in `fish-care/dorado-and-general.md`)

- **Rock salt, ~2 cups per 7–10 lb bag of ice**, plus a **splash of seawater** to wet it. The salt is the whole point: it drives the mix **below freezing**, which is why it out-chills bare ice or plain ice water and is what lets a big tuna chill to the core.
- Keep the fish **fully in the slurry** and **re-ice as the ice burns down** — a fish half in the cold chills unevenly.
- **Never fresh water on the fish** — no freshwater rinse, no letting it swim in freshwater melt (`fish-care/dorado-and-general.md`).
- The slurry numbers in this KB are attributed to "BD Outdoors care/seminar reporting" without a video ID in the note itself, so I can't hand you a specific source ID for the 2-cups figure.

**6. Chill times by fish size — plan the day around these**
(`fish-care/tuna-care.md`)

| Fish size | Time in the slurry |
|---|---|
| 30–40 lb | ≈ 2 h |
| ~100 lb | ≈ 3–5 h |
| >100 lb | **overnight, re-iced** |

A **>100 lb fish will not core-chill in an afternoon.** On a small boat that means the cold chain has to survive the run in, the ramp, and the trailer — plan to hold it overnight and re-ice.

**7. Dockside, after the fish is off the boat**
(`fish-care/tuna-care.md`, `usHl-4SfqDA`)

- **Rinse cut loins in a cold salt-water bath — never fresh water.** Moisture from fresh water speeds tuna decomposition. The crew mixes **regular table salt (Morton's), about 3/4 cup per batch of ice**, to bring the rinse water to **~32 °F, just under freezing**. Quick rinse right after cutting, then set aside.
- Loins go back into the bag / on ice **while still cold**, straight out of the salt rinse.
- Named failure mode: charters that just loin the fish, skin it, bag it in plastic and hand it over with no salt-water step and no attentive chilling — "a great way to waste a lot of the tuna" (100+ lb of loins cited).
- This step **follows** the slurry chain; it does not replace it.
- For the drive: `fish-care/dorado-and-general.md` says to **bring a separate car cooler** so the cold chain continues past the dock (stated there for dorado, but the note's "keep fish cold and out of the sun" principle is flagged as applying to all species).

**8. Fillet storage, once you're home**
(`fish-care/dorado-and-general.md`, `2gHRrR3D8rY`)

- Fresh fillets go straight into a **bucket of salt water with ice** and soak before bagging. Salt water only, never fresh.
- **Dry before freezing** — let them drip, pat dry; less residual water means a better fillet out of the freezer.
- **Water-displacement bagging** if you have no vacuum sealer: fill a zip-top bag most of the way, leave a small opening, slowly submerge it, and seal just before it goes fully under.
- Storage windows: **~3 days** refrigerated; **1–3 months** vacuum-sealed and frozen; **~1 week to 1 month** frozen in a plain ziplock.

---

## Two side notes the KB carries

- **Estimating weight with no scale on deck** (`mDmbGdQAy-4`, 2025-10-06, NE of Santa Barbara Island): tape measure and **length × girth² ÷ 800** (inches, result in lb). Worked on camera as 46 in girth × 68.5 in length ≈ **181 lb**. Useful on a small boat where you can't lift the fish to a scale — and it tells you which chill-time row you're in.
- **The RSW alternative is not a small-boat option:** the KB's other chilling mechanism is a refrigerated-seawater hold running at **~36 °F**, on an 85 ft charter at Cortez Bank (`Y1xeieQI3B4`). It's kept side by side with the slurry, not merged — different mechanism, and no chill-time detail was given.

## What this means for ice load

The only ice-quantity number in this KB is profile data, not doctrine: Cameron's **22 ft Panga Marine Marquesas** carries **100–125 lb of ice per trip**, ~100 lb of it in the cooler as running-out ballast (`profiles/cameron/boat.md`, source `cameron`). The blank profile template just points at the tuna-care note for ice capacity (`profiles/_template/boat.md`), so **the KB gives no rule for pounds of ice per pound of fish** — see the gaps below. If you pair 100 lb of ice with the stated ratio, that's roughly 10–14 bags and **~20–28 cups of rock salt**; that multiplication is mine, not a figure the KB states.

## Gaps — things you asked about that this KB does not cover

- **No small-boat-specific fish-care note at all** — nothing on kill bag vs. fish box vs. cooler, how to hold a fish longer than your cooler, or how to manage deck space and the cold chain on a trailer boat.
- **No ice-per-pound-of-fish rule**, and no slurry water-to-ice ratio beyond "a splash of seawater."
- **The bleed cuts themselves are not written down** — the KB deliberately defers to `JeexIvtUkZc` for the gill-and-gut, and the yellowtail artery cut was never specified on camera beyond "down here."
- **Ikejime spike placement and depth are explicitly not in the KB.**
- **No maximum time-to-bleed** after gaffing (only "immediately"), and nothing on how ambient or water temperature changes the urgency.
- **No coverage of fillet/carcass retention regulations** — whether California or Mexico requires fish to be kept whole or skin-on for identification when you gut or fillet at sea. Check CDFW and the relevant Mexican rules yourself before dressing fish on the water; this KB has nothing on it.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `fish-care/README.md`, `fish-care/tuna-care.md`, `fish-care/ikejime.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `species/bluefin-tuna.md`, `profiles/cameron/boat.md`, `profiles/_template/boat.md`, `sources/source-registry.md`  
*videos:* `w6DDCSLu8vM`, `JeexIvtUkZc`, `H-vIGWPIPVc`, `usHl-4SfqDA`, `Klfb433I3Uk`, `Y1xeieQI3B4`, `mDmbGdQAy-4`, `WzT0RSHpaQc`, `I84uoay_jwQ`, `8jC61LzQoxU`, `E4vKwRaRueA`, `2gHRrR3D8rY`  
*gaps admitted:* No small-boat-specific fish-care note exists — nothing on kill bag vs fish box vs cooler selection, deck space, or holding a fish larger than your cooler on a trailer boat. | No ice-per-pound-of-fish rule anywhere in the KB; the only ice quantity is Cameron's profile figure of 100–125 lb per trip on a 22 ft panga. | No slurry water-to-ice ratio beyond 'a splash of seawater' to wet the mix. | The bleed cuts themselves are not written down — the KB defers to video JeexIvtUkZc, and the yellowtail artery cut location was never specified on camera beyond 'down here'. | Ikejime spike placement and depth are explicitly excluded from the KB prose. | No maximum elapsed time to bleed after gaffing (only 'immediately'), and no guidance on how air/water temperature changes the urgency. | No coverage of fillet/carcass retention regulations (CDFW or Mexican rules on keeping fish whole or skin-on for identification when gutting or filleting at sea). | The slurry parameters (~2 cups rock salt per 7–10 lb bag of ice) are attributed only to 'BD Outdoors care/seminar reporting' with no video_id in the note, so no specific source ID can be carried for that figure. | fish-care/tuna-care.md sits at medium confidence overall and fish-care/gaffing.md at low (sponsored source), so the gaff-placement doctrine is directional rather than settled. | Nothing on whether to skip gill-and-gut if you want the fish whole for a scale weigh-in or photo, or on dockside vs onboard butchery choice.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Bleeding and chilling a tuna on a small boat

The whole chain lives in [`fish-care/tuna-care.md`](fish-care/tuna-care.md), with the gaff shot in [`fish-care/gaffing.md`](fish-care/gaffing.md) and the optional top tier in [`fish-care/ikejime.md`](fish-care/ikejime.md). One caveat up front: `fish-care/tuna-care.md` carries `confidence: medium`, and `fish-care/gaffing.md` carries `confidence: low` (its main source is a sponsored gaff spot, so the registry caps it). Treat the numbers below as what the corpus says, not as settled doctrine.

### 0. Before the fish is even aboard

How you fight it sets up how cleanly you can boat it, and a small boat has its own pattern. For a **20–30 ft private boat**, Capt. Dave Hansen coaches leaving the rod in the holder, turning the boat in **big, gentle circles** (explicitly not tight "spinning like a donut" turns), keeping the fish pinned on the **same side** of the boat from amidships back to the stern, and driving **forward only, never in reverse**, holding roughly a **45° angle** to the fish — [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md) (`Q196GVwVqro`). Same note logs a crew on a **22 ft center console** arguing a small, maneuverable boat works a circling fish better than a yacht (`rsCAh-QyK60`). Walk down-swell the whole fight and avoid the death circle.

### 1. Boat it cleanly — the gaff shot is the first care step

From [`fish-care/tuna-care.md`](fish-care/tuna-care.md) (`w6DDCSLu8vM`): aim the gaff at the **head/shoulder** region, not mid-body or tail, on a committed pass with the fish's head coming toward you.

Kept side by side with that in [`fish-care/gaffing.md`](fish-care/gaffing.md) (`I84uoay_jwQ`, corroborated non-sponsored in `8jC61LzQoxU`) is the more specific bluefin version: **aim for the pec and flip the fish upside down the instant it's gaffed** — a bluefin has never been upside down in its life, and it stuns it dead in the water, "I don't care if he weighs 300 lb or if he weighs 20 lb." Do **not** gaff the back, tail, or side of the head — it'll keep driving and rip the gaff out of your hands. The KB keeps both placements attributed rather than merging them; the pec/flip claim is the more specific one and sits at `low` confidence on the sponsored-source rule.

Small-boat-relevant mechanics from the same note:
- **Gaff sizing:** 3-in hook on a ~6-ft gaff for fish up to **40–50 lb**; 6-in hook on a ~8-ft gaff for SoCal bluefin at the **200–300 lb** grade.
- **Call for the gaff the moment the fish shows "in the colors"**, not when it's on the surface (`OIiDJu4mx44`).
- Keep the fish **lying horizontal just under the surface**; don't lift its head out before the shot — it makes the fish dive (`OIiDJu4mx44`).
- **Hook orientation:** never gaff with the point away from the boat and pull outward ("digging a hole"). Turn the point back toward the boat and drag across the top of the water toward you, so the stroke pulls the fish in.
- **Land hand over hand straight up**; don't lift it like you'd lift on a rod or it falls off the gaff. The angler puts the reel **in free spool with a thumb lightly on the spool** the instant the fish is gaffed so it doesn't backlash (`OIiDJu4mx44`).
- **Gaff safety on a crowded small deck:** never stand the gaff butt-down with the hook up at head height while people are moving around — rest it on the gunnel, hook up and out of the way. Keep hands off it until the shot.
- On **100–115 lb class** fish, one crew stressed **all hands on deck for the gaff shot**, and showed a double-gaff on one fish (`elBPRrdkugU`). On a small boat with two people that is a real constraint to plan around.

### 2. Bleed and gill-and-gut, immediately, on the water

This is the step that decides how the fish eats ([`fish-care/tuna-care.md`](fish-care/tuna-care.md), `JeexIvtUkZc`):

- **Bleed** the fish so the meat doesn't hold blood.
- **Field-dress** it — remove **guts and gills**. The mechanism the note gives: pulling the gills and viscera removes the warm mass and the enzymes that spoil quality fastest, so the slurry can cool the carcass instead of fighting a bellyful of heat.
- A second source describes the same mechanism — cutting/pulling the gill opens the bloodline, which bleeds the fish out and also kills it faster — done immediately boat-side, fish on ice right after (`H-vIGWPIPVc`, San Clemente Island, 2019-10-30, unregistered channel/medium).

**On ordering, the KB carries two versions side by side and does not reconcile them.** `fish-care/ikejime.md` states the chain as **kill clean (ikejime) → bleed → field-dress → chill**. A charter operation's stated order in `fish-care/tuna-care.md` is **bleed, kill, then gut, immediately on landing** (`usHl-4SfqDA`, 2024-11-13, unregistered channel/medium). What isn't in dispute: bleeding and gutting happen immediately, on the water, before ice.

That same source adds a detail that matters on a small boat where you can't submerge a big fish: **pack the body cavity itself with ice and cover the fish completely** (`usHl-4SfqDA`).

A cross-species data point the note logs for the bleed itself (this one is **yellowtail, not tuna** — `Klfb433I3Uk`, San Clemente Island, 2019-10-04): as soon as the fish is on deck, **cut the artery**, then hold the fish **upside down in a bucket** for about **5 minutes** — "almost all the fish's blood goes through this artery within a matter of minutes" — then on ice, called ready for sashimi at that point. The upside-down-in-a-bucket trick is genuinely useful on a small deck, but note the source species and that the exact cut location was not specified on camera.

### 3. Wet-towel cooldown before it hits the slurry

Give the dressed carcass a **wet-towel cooldown** to knock the surface heat off before committing it to the ice. Dropping a hot fish straight into the slurry is less effective than letting it shed the worst of its heat first ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)).

### 4. The below-freezing slurry — this is the part most small boats get wrong

Plain ice water won't core-chill a tuna. From [`fish-care/tuna-care.md`](fish-care/tuna-care.md) and repeated in [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md) (numbers attributed to BD Outdoors care/seminar reporting):

- **Rock salt, ~2 cups per 7–10 lb bag of ice**, mixed into the ice.
- Plus a **splash of seawater** to make it a wet slurry. The salt is what drives the mix **below freezing** — that's the entire reason it out-chills bare ice.
- Keep the fish **fully in the slurry** and **re-ice as the ice burns down**. A fish half in the cold chills unevenly.
- Keep it out of the sun; a fish baking on a hot deck is losing quality the whole time ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md)).
- **Never fresh water on the fish** — same note. Fresh water degrades color and flesh; don't let the catch swim in freshwater melt.

The RSW alternative in the corpus (a **36 °F refrigerated seawater hold**, fish stay in it until filleted — `Y1xeieQI3B4`, 85 ft *El Dorado*, Cortez Bank) is a big-boat option and is not applicable to a trailer boat; the KB keeps it beside the slurry chain rather than merged into it.

### 5. How long it needs in the cold

| Fish size | Chill time |
|---|---|
| 30–40 lb | ≈ 2 h |
| ~100 lb | ≈ 3–5 h |
| >100 lb | overnight, re-iced |

A **>100 lb** fish will not core-chill in an afternoon — plan to hold it overnight and re-ice as the slurry melts down ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)). On a small boat that means the cold chain has to survive the drive home, not just the ride in: [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md) says **bring a separate car cooler for the drive** rather than letting the fish warm up on the road.

If you need the weight and can't lift the fish onto a scale, the crew in `mDmbGdQAy-4` used **length × girth² ÷ 800** (inches in, pounds out) — worked on camera as 46 in girth, 68.5 in length → ≈181 lb.

### 6. Ikejime — worth it or not

[`fish-care/ikejime.md`](fish-care/ikejime.md) (`WzT0RSHpaQc`): a spike driven into the **brain** kills the fish instantly, optionally with **pithing** (a wire down the spinal cord to destroy the nerve line) so it doesn't thrash and burn quality into the meat. It **sits on top of, not in place of, bleeding and chilling** — the steps stack. Reach for it when you're after **sashimi-grade** flesh; for a fish going to the smoker or grill, bleed-and-chill carries it. The note is explicit that it does **not** teach the spike placement — that comes from the video and hands-on practice.

### 7. At the dock, after filleting

From [`fish-care/tuna-care.md`](fish-care/tuna-care.md) (`usHl-4SfqDA`) — this follows, and does not replace, the slurry chain:

- **Rinse cut loins in cold salt water, never fresh** — fresh water speeds decomposition of tuna meat. That crew mixes **regular table salt, about 3/4 cup per batch of ice**, to bring the rinse water to **about 32 °F, just under freezing**.
- Loins go back into the bag / onto ice **while still cold**, straight from the rinse.
- Named failure mode: charters that loin, skin, bag in plastic and hand it over with no salt-water step or attentive chilling are "a great way to waste a lot of the tuna" (100+ lb of loins cited).

Storage windows from [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md) (`2gHRrR3D8rY`): refrigerated fillets ≈ **3 days**; vacuum-sealed and frozen **1–3 months**; frozen in a plain ziplock **1 week to 1 month**. Same note gives a no-machine near-vacuum method — fill a zip-top bag, leave a small opening, slowly submerge it so water pressure pushes the air out, seal just before it goes under — and says to let fillets **drip and pat dry before bagging**.

### Small-boat capacity — the honest part

The only capacity guidance in the KB is region-labeled Baja panga trip planning, in [`locations/bahia-de-los-angeles.md`](locations/bahia-de-los-angeles.md) (`P36VGPPf120`, `cortez-north`): bring **a kill bag**, because coolers "only fit so many fish and ice," and bring **more ice than you think** — otherwise fish "burn up in the fish holds." The source's own lesson across trips was more ice, more coolers, more kill bags each time. That's panga advice rather than SoCal doctrine, but it's the closest the KB comes to sizing the cold for a small boat.

Against your own profile, [`profiles/cameron/boat.md`](profiles/cameron/boat.md): the Panga Marine Marquesas 22 runs **100–125 lb of ice per trip**, with ~100 lb in the cooler on the way out, and the trim routine puts that ice plus one person forward when running. On a >100 lb bluefin the chill table above wants the fish held overnight and re-iced — 100–125 lb of ice starting the day is the constraint to plan around, and the salt is what makes it work harder than it looks.

**Gear gaps I have to name** (the day-plan protocol says never assume gear you haven't said you own): your profile lists rods, reels, lures and ice, but **no gaff, no kill bag, no rock salt, and no ikejime spike**. The chain above wants a **6-in hook / ~8-ft gaff** if you're on a 200–300 lb-class fish, rock salt at ~2 cups per 7–10 lb bag, and a container the fish actually fits in. Those aren't in the profile, so I'm flagging them rather than assuming.

### What the KB does not tell you

- The **exact bleed cut on a tuna** is not written down anywhere here. `fish-care/tuna-care.md` deliberately doesn't give a play-by-play and points to the video (`JeexIvtUkZc`, gill & gut a bluefin) for where to cut and pull. The one explicit "cut the artery" instruction in the corpus is on a **yellowtail** and the location was left as "down here" on camera.
- No **bleed duration for tuna** — the ~5 minutes is the yellowtail data point.
- No **ice-to-fish ratio, slurry volume, or container sizing**, so I can't tell you how many pounds of ice a given tuna needs.
- No **ikejime spike placement or depth** — the note says so explicitly.
- No **chill time for a tuna under 30 lb** (the table starts at 30–40 lb).
- No note on whether **California/CDFW rules** allow gutting or filleting at sea, or require fish landed in a particular condition. The KB's fish-care regulatory notes cover only sculpin size and dehooking/measuring.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `fish-care/README.md`, `fish-care/tuna-care.md`, `fish-care/ikejime.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `techniques/fighting-big-bluefin.md`, `locations/bahia-de-los-angeles.md`, `profiles/cameron/boat.md`, `profiles/cameron/tackle.md`, `profiles/cameron/rods.md`, `species/bluefin-tuna.md`, `species/bonito.md`, `sources/source-registry.md`  
*videos:* `JeexIvtUkZc`, `w6DDCSLu8vM`, `H-vIGWPIPVc`, `usHl-4SfqDA`, `Klfb433I3Uk`, `Y1xeieQI3B4`, `mDmbGdQAy-4`, `WzT0RSHpaQc`, `I84uoay_jwQ`, `8jC61LzQoxU`, `OIiDJu4mx44`, `elBPRrdkugU`, `E4vKwRaRueA`, `2gHRrR3D8rY`, `P36VGPPf120`, `Q196GVwVqro`, `rsCAh-QyK60`  
*gaps admitted:* No note gives the exact anatomical bleed cut for a tuna — fish-care/tuna-care.md defers the cut/pull locations to the video JeexIvtUkZc rather than writing them down. | No stated bleed duration for a tuna; the only timed figure (~5 minutes, held upside down in a bucket) is a yellowtail observation (Klfb433I3Uk), not tuna doctrine. | No ice-to-fish ratio, slurry volume, or container/kill-bag sizing anywhere in the KB — I cannot say how many pounds of ice a given tuna needs. | No ikejime spike placement or depth; fish-care/ikejime.md states outright that the precise spot comes from the video and hands-on practice, not from the note. | No chill time given for a tuna under 30 lb — the table in fish-care/tuna-care.md starts at 30-40 lb. | No regulatory note on whether California/CDFW rules permit gutting or filleting at sea or require fish to be landed whole; fish-care regulatory content covers only sculpin size limits and dehooking/measuring. | No small-boat-specific deck-logistics note (where to hold a big tuna on a 22 ft boat, kill bag vs cooler); the only capacity guidance is Baja panga trip-planning in locations/bahia-de-los-angeles.md, region-labeled cortez-north. | The KB carries two unreconciled orderings of the kill/bleed/gut sequence (ikejime note: kill, bleed, dress, chill; usHl-4SfqDA: bleed, kill, then gut) and gives no decision frame for choosing between them. | Cameron's profile lists no gaff, kill bag, rock salt, or ikejime spike, so the gear this chain requires cannot be resolved against owned equipment.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Bleeding and chilling a tuna on a small boat

**Scope caveat first.** The KB has a complete tuna care chain, but **no small-boat-specific fish-care note** — nothing on cooler vs. kill-bag sizing, on ice budget split between bait and fish, or on what to do with a fish too big for your box. Everything below is the general chain from [`fish-care/tuna-care.md`](fish-care/tuna-care.md) (front-matter `confidence: medium`), plus the small-boat translation I can make from your own [`profiles/cameron/boat.md`](profiles/cameron/boat.md). Where the KB is silent I say so rather than filling it in.

---

## The chain, in order

The KB carries **three stated orderings** for the first steps and does not reconcile them. What is constant in all three: it all happens **immediately, on the water, before the fish goes in the cold**.

| Source | Stated order |
|---|---|
| [`fish-care/tuna-care.md`](fish-care/tuna-care.md) §2 (`JeexIvtUkZc`) | Bleed → pull gills and guts → chill |
| [`fish-care/ikejime.md`](fish-care/ikejime.md) (`WzT0RSHpaQc`) | Kill clean (ikejime) → bleed → field-dress → slurry |
| One charter's routine (`usHl-4SfqDA`) | Bleed → kill → gut immediately on landing → pack the cavity with ice and cover the fish completely |

Decision frame: ikejime is the extra step **only when the goal is sashimi-grade** — for a fish going to the grill or smoker, bleeding and chilling alone carry it (`WzT0RSHpaQc`). Ikejime **stacks on, never replaces**, bleeding and chilling.

### 1. Get it aboard without wrecking it — the gaff shot
From [`fish-care/gaffing.md`](fish-care/gaffing.md) (note `confidence: low` — the sizing figures come from a Promar sponsored gaff spot, `I84uoay_jwQ`; the pec/flip doctrine is corroborated in a separate non-sponsored tutorial from the same voice, `8jC61LzQoxU`):

- **Call for the gaff the moment the fish shows "in the colors,"** deep down — not when it's at the surface (`OIiDJu4mx44`, SearcherSportfishing 2022-10-13).
- **Gaff sizing:** 3-in hook / ~6-ft gaff for fish up to **40–50 lb**; 6-in hook / ~8-ft gaff for SoCal bluefin at the **200–300 lb** grade (`I84uoay_jwQ`).
- **Keep the fish horizontal just under the surface** — do not lift its head out, it makes the fish dive (`OIiDJu4mx44`).
- **Aim the pec** (a specific case of the head/shoulder region, `w6DDCSLu8vM`) and **flip the fish upside down the instant it's gaffed** — it stuns it and stops it dead, "300 lb or 20 lb" (`I84uoay_jwQ`). Never the back, tail, or side of the head — it keeps driving and rips the gaff out of your hands.
- **Hook points back toward the boat**, drag across the top of the water toward you. Hook pointed away is "digging a hole" and pushes the fish away from the boat (`I84uoay_jwQ`).
- **Angler goes to free spool the instant the fish is gaffed, thumb light on the spool** so it doesn't backlash on the slack (`OIiDJu4mx44`). Then **hand over hand straight up** onto the deck — don't lift it like you're fighting it on the rod, it falls off the gaff.
- **Tail rope the big ones** once gaffed (`RPSRH0jwyw4`).

### 2. Bleed and gill-and-gut — on the water, immediately
- **Bleed, then pull gills and guts** before the fish goes on ice. This removes the warm mass and the enzymes that spoil quality fastest, so the slurry cools the carcass instead of fighting a bellyful of heat (`JeexIvtUkZc`, BDOutdoors 2023-08-14 — the walkthrough video is the reference for the actual cuts; [`fish-care/tuna-care.md`](fish-care/tuna-care.md) deliberately doesn't transcribe them).
- Mechanism as described: **cutting/pulling the gill opens the bloodline**, which bleeds the fish out and also kills it faster — done boat-side with the fish going on ice right after (`H-vIGWPIPVc`, [`fish-care/evidence/tuna-care.md`](fish-care/evidence/tuna-care.md)).
- The charter variant adds **packing the body cavity itself with ice and covering the fish completely** (`usHl-4SfqDA`) — a genuinely useful addition on a small boat, where the cooler may not swallow the whole fish in slurry.

### 3. Wet-towel cooldown before it hits the ice
Field-dress, then give the carcass a **wet-towel cooldown** to knock the worst of the surface heat off. Dropping a hot fish straight into ice is less effective than letting it shed that heat first (`5to3Q5P7w90`).

### 4. The below-freezing slurry — the actual recipe
Rock salt in ice + seawater drives the mix **below the freezing point of fresh water**, which is what lets a big tuna chill through to the core (`5to3Q5P7w90`):

- **Rock salt, ~2 cups per 7–10 lb bag of ice**, plus a splash of **seawater** to wet it.
- **Fish fully in the slurry**, and **re-ice as the ice burns down** — a fish half in the cold chills unevenly.
- **Never fresh water** on the meat — salt water for every rinse, on every species ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md), `5to3Q5P7w90`, `2gHRrR3D8rY`).
- **A deck hose-down is not chilling.** Deck-hose water runs in the **high 70s °F** — it wets the bag without dropping the fish's temperature (`5to3Q5P7w90`).

### 5. Chill time by fish size — hold it in the cold at least this long (`5to3Q5P7w90`)

| Fish size | Chill time |
|---|---|
| 30–40 lb | ≈ 2 h |
| ~100 lb | ≈ 3–5 h |
| >100 lb | **overnight, re-iced** |

A >100 lb fish will not core-chill in an afternoon. The RSW alternative in the KB — a refrigerated seawater hold at about **36 °F** — is documented only on an 85-ft multi-day charter (`Y1xeieQI3B4`), not on anything small-boat scale.

### 6. After the fillet
- **Rinse cut loins in a cold salt-water bath, never fresh water** — fresh-water moisture speeds decomposition. **Table salt (Morton's), ~3/4 cup per batch of ice**, to bring the rinse water to **~32 °F**, quick rinse right after the cut, loins back on ice while still cold (`usHl-4SfqDA`).
- Fillet storage windows (`2gHRrR3D8rY`): refrigerated **~3 days**; vacuum-sealed frozen **1–3 months**; plain ziplock frozen **~1 week to 1 month**. Water-displacement bagging gets you a near-vacuum seal with no machine — fill the bag, leave a small opening, submerge slowly, seal just before it goes under.
- **Car cooler if the drive home is more than ~10 minutes** (`5to3Q5P7w90`).

### Ikejime, if you want sashimi grade
Spike the **brain** for an instant kill, then **pith** — run a wire down the spinal cord to destroy the nerve line, which stops the thrashing that burns the meat (`WzT0RSHpaQc`). [`fish-care/ikejime.md`](fish-care/ikejime.md) states plainly that **exact spike placement and depth are not in prose** — the video and hands-on practice are the reference.

---

## What actually changes on your boat

Reading this against [`profiles/cameron/boat.md`](profiles/cameron/boat.md) (22-ft Panga Marine Marquesas 22):

- **Ice load: 100–125 lb per trip**, carried in the cooler and doubling as forward trim ballast on the run out. At the note's ratio of ~2 cups rock salt per 7–10 lb bag, that's roughly **10–18 bags → ~20–36 cups (≈1.25–2.25 gal) of rock salt** to salt the whole load. *That conversion is my arithmetic from the ratio plus your stated ice load — it is not a figure any note states.*
- **RSW is structurally off the table** for you: **no AC/shore-power inlet and no house battery** — bait tank and accessories run off the single Group 24DC starting battery. The salted ice slurry is the only chilling mechanism the KB offers at your scale.
- **The >100 lb overnight problem is the hard constraint.** The chill table wants that fish held overnight and re-iced; your cold chain has to survive the run home, Dana Landing, and the night. The KB gives you no guidance on doing that off a 22-footer — see gaps.
- **Bleed away from the rail when sea lions are working.** Boatside is the depredation window — hooked *and boated* fish get grabbed at the rail (`d0yGBQDeY_4`); the counter-move on a hooked fish is wind continuously, never pump, and throw it into free spool when the sea lion grabs (`mdhoEQPqpng`) ([`species/yellowtail.md`](species/yellowtail.md)).
- **Gaff safety matters more, not less, on a small deck.** Never stand the gaff butt-down with the hook at head height while people are moving around — rest it on the gunnel, hook up and out of the way; keep hands off it until the shot (`I84uoay_jwQ`). At the **100–115 lb** class the KB says get **all hands on deck** for the shot, and a double-gaff works that grade (`elBPRrdkugU`) — worth planning for with a small crew.
- **Your profile lists no gaff, bleed knife, spike, or kill bag** ([`profiles/cameron/tackle.md`](profiles/cameron/tackle.md), [`profiles/cameron/rods.md`](profiles/cameron/rods.md)). Per the day-plan protocol's rule about naming gear gaps rather than assuming them: this whole chain assumes a gaff sized to the grade, a knife, a bucket, and salt aboard.
- **Baja analogue, region-labeled:** the nearest small-boat lesson in the KB is from **Bahía de los Ángeles** (`cortez-north`, not SoCal doctrine): bring a **kill bag**, because panga coolers "only fit so many fish and ice," and **more ice than you think** — the source's own lesson across trips was more ice, more coolers, more kill bags every time (`P36VGPPf120`, [`locations/bahia-de-los-angeles.md`](locations/bahia-de-los-angeles.md)).

## Cross-species traps on a mixed day
- **Dorado are the opposite call: do not bleed, ice immediately.** Their metabolism means the flesh breaks down fast — an hour or two warm in a dry gunny sack and the meat falls apart ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md), `5to3Q5P7w90`).
- **Yellowtail have their own procedure:** cut the artery as soon as the fish is on deck, hang it **upside down in a bucket ~5 minutes**, then ice (`Klfb433I3Uk`, [`species/yellowtail.md`](species/yellowtail.md)). The KB flags the physiological premise as single-source; the procedure itself is verbatim. **It does not say whether the 5-minute hang transfers to tuna.**
- [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md) and [`species/skipjack-tuna.md`](species/skipjack-tuna.md) both carry **flagged gaps** — no corpus source for yellowfin- or skipjack-specific bleeding/chilling; they route back to the general tuna chain above.

## Weight, and one regulatory line
- **No scale?** Estimate with a tape: **length × girth² ÷ 800** (inches, result in lb) — worked on camera as 46 in girth × 68.5 in length ≈ **181 lb** (`mDmbGdQAy-4`, [`fish-care/evidence/tuna-care.md`](fish-care/evidence/tuna-care.md)).
- **California / CDFW bag limit: two Pacific bluefin per person per day**, as of **2024-11**, flagged single-source in the KB (`usHl-4SfqDA`, [`species/bluefin-tuna.md`](species/bluefin-tuna.md)). **Verify current rules with CDFW before fishing.** The KB has **no source** on whether a fish may be filleted at sea in US waters, what must stay attached for identification, or how a limit is counted in transit ([`locations/us-waters.md`](locations/us-waters.md)).

## Provenance honesty
The **slurry ratio, the wet-towel step, the deck-hose figure, and all three chill times rest on a single video** — `5to3Q5P7w90` (BDOutdoors, "Southern California Bight FISHING REPORT 09/14/22", 2022-09-15). BDOutdoors as a channel is not blanket-high; only its registered named voices are ([`sources/source-registry.md`](sources/source-registry.md)). Several of the supporting cites (`usHl-4SfqDA`, `H-vIGWPIPVc`, `Klfb433I3Uk`, `2gHRrR3D8rY`, `elBPRrdkugU`) are StokedOnFishing, an unregistered channel capped at **medium**. Treat the numbers as good working parameters, not as verified doctrine.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `fish-care/README.md`, `fish-care/tuna-care.md`, `fish-care/evidence/tuna-care.md`, `fish-care/ikejime.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/skipjack-tuna.md`, `species/yellowtail.md`, `species/bonito.md`, `profiles/cameron/boat.md`, `profiles/cameron/tackle.md`, `profiles/cameron/rods.md`, `locations/bahia-de-los-angeles.md`, `locations/us-waters.md`, `sources/source-registry.md`, `sources/transcripts/_manifest.csv`  
*videos:* `5to3Q5P7w90`, `JeexIvtUkZc`, `usHl-4SfqDA`, `H-vIGWPIPVc`, `Klfb433I3Uk`, `Y1xeieQI3B4`, `mDmbGdQAy-4`, `WzT0RSHpaQc`, `w6DDCSLu8vM`, `I84uoay_jwQ`, `8jC61LzQoxU`, `OIiDJu4mx44`, `elBPRrdkugU`, `RPSRH0jwyw4`, `2gHRrR3D8rY`, `mdhoEQPqpng`, `d0yGBQDeY_4`, `P36VGPPf120`  
*gaps admitted:* No small-boat-specific fish-care note exists in the KB — nothing on cooler vs. kill-bag sizing, ice budget split between bait tank and fish, or handling a fish too big for the box on a 22-ft boat. | The actual bleed cut for a tuna is not described in prose — tuna-care.md points to the video (JeexIvtUkZc) for the cuts; only the yellowtail artery cut is written out anywhere in the KB. | No stated maximum time window from gaff to bleed beyond 'immediately'. | No core-temperature target and no way to verify a fish is chilled through — only the elapsed-time table by fish size. | The >100 lb 'overnight, re-iced' requirement has no small-boat implementation guidance (holding the cold chain through the run home, the dock, and the night). | The RSW alternative (~36 °F hold) is documented only on an 85-ft multi-day charter; no small-boat equivalent, and Cameron's boat has no house battery or shore power. | Exact ikejime spike placement and depth are deliberately not in the KB — the note defers to the video and hands-on practice. | Yellowfin- and skipjack-specific bleeding, chilling and ikejime parameters are flagged as absent by the KB itself. | Whether the yellowtail 5-minute upside-down bucket hang transfers to tuna is not stated. | No corpus source on US fillet-at-sea rules, what must stay attached for species/size identification, or how a limit is counted in transit. | The rock-salt quantity for a 100–125 lb ice load is my arithmetic from the note's ratio plus the boat profile — no note states a per-trip salt quantity. | Cameron's profile lists no gaff, bleed knife, spike, bucket or kill bag, so the whole chain assumes tools not recorded as owned. | Gaff sizing figures come from a sponsored gear video (I84uoay_jwQ), and gaffing.md carries confidence: low. | The slurry ratio, wet-towel step and all three chill times rest on a single video (5to3Q5P7w90); several supporting cites are from an unregistered channel capped at medium confidence.

</details>
