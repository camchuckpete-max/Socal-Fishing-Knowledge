# Technique — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11 | 11.75 | 12 |
| found | 2 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 2 | 2 | 2 |
| honest | 1.75 | 1.75 | 2 |
| actionable | 1.25 | 2 | 2 |
| **wins** | 0 | 1 | 3 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 0 | 0 | 0 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | None | None | None |
| Gear | None | None | None |
| Technique | 11 | 11.75 | 12 |
| Finding fish | None | None | None |
| Conditions & season | None | None | None |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 10. [technique] How do I fish a yo-yo iron at Farnsworth Bank? Retrieve, depth, current, and the tackle to use.

**Winner:** NOW · mapping {'A': 'B3', 'B': 'NOW', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 1 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 1 | 2 | **11** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three correctly refuse to invent Farnsworth-specific depth or preferred current directions and all three deliver a rig-able yo-yo answer, so the separation is accuracy and context, not coverage. B wins because it is the only answer that stamps the closure with jurisdiction plus as-of 2022-10 plus verify-current, the only one that warns the ~5-10 fathom sonar band is contradicted by its own source, the only one that surfaces the unresolved jig-weight conflict (depth-keyed 5-6 oz vs current-keyed 8/4 oz) and then gives a practical reconciliation, and the only one that reaches the zone page for the closure table and the bonito-bycatch trap that matters at a bank where bonito is one of two keepable species. C is the strongest day-runner — tide windows, manual-range sounder setup, dropper-loop and flat-fall fallbacks — but passes on the 5-10 fm band and 'fall spot' unqualified and has the weakest line/leader detail. A is a close third: excellent tackle table and cadence-selection judgment, but no timing layer, no zone context, and the same unqualified 5-10 fm claim.

- *B2 reasons:* found: all four axes plus the widest adjacent pull — tide/slack windows, sounder setup, dropper-loop and flat-fall fallbacks, electronics note. specific: 120-200 ft with fish ~20 ft off bottom, 100-120 ft band, 10-crank increments over 150 yd, Tanner 80 ft drop on 60 ft marks, Cedros 212 ft and San Augustine 130 ft, 5-6 oz vs 2-3 oz, 6-10 oz dropper sinkers, 100-180 g flat-fall. sourced: cites carry note paths, video ids and channel-registration/confidence, and out-of-region items are labeled. scoped: Baja material fenced in explicit contrast blocks with a do-not-mix warning; closure carries CDFW, the 10/26/22 report date, verify-current, and the caption-garble caveat. honest: eight-item gap list and flags the reconstructed name, but states the ~5-10 fathom band as the classic read and 'Farnsworth is a fall yo-yo spot' flatly, without the source's own negative on prime time. actionable: most complete day-run — tide window, manual-range sounder setup, three cadences, bite feel, and a plan-B technique — but its line/leader table is the thinnest of the three (two rows with no main-line spec, fluoro vs no-fluoro left unexplained, no mono-buffer mechanism).
- *B3 reasons:* found: covers all four asked axes (retrieve, depth, current, tackle) plus the standalone-bank structure type and the charted position; no zone/tide layer but nothing wandered. specific: dense real numbers — 120-240 ft yo-yo band, 6X at 5-6 oz vs 6X Jr, 120-180 ft base case, 40-60 ft surface-iron threshold, Fathom 30 / 65 lb braid / 50-yd 40-50 lb top shot, 43 in per turn, 6.6:1. sourced: every parameter carries a video id and a note path, and the profile match cites profiles/cameron/rods.md and tackle.md. scoped: SoCal doctrine kept separate, closure named as regulation with CDFW, the 2022-10-26 report date and an explicit verify-current instruction. honest: strong ten-item gap list and refuses to invent a Farnsworth depth, but passes on the ~5-10 fathom sonar band as the 'classic read' with no note that the cited source carries no depth figure. actionable: rig-able and executable — cadence menu with a stated selection rule (mark shape picks A/B/C), positioning, scope fixes, and two named profile gaps (no top shot, no scrambled-egg/red iron).
- *NOW reasons:* found: hits all four axes and is the only answer that reaches the zone-level page (Catalina backside: weather side, closure table, escalated Farnsworth row) rather than only the spot-list row. specific: front-matter working band (60-250 ft; 120-180 nearshore, 150-250+ on banks), depth/jig table, 5-6 oz vs 2-3 oz, 10-crank and 5-6 crank cadences, 100-120 ft band on 120 ft marks, full Fathom 30 build with 65 lb braid and 50-yd top shot. sourced: note paths plus video ids throughout, and it names which claims rest on a single cite. scoped: the only answer that stamps the closure as-of 2022-10 with CDFW named and verify-current, and it labels the Fathom 40 / 80 lb tier as the Baja upsize rather than the Catalina call. honest: best in class — flags that the 5-10 fm band is contradicted by its source, surfaces the unresolved 6X-vs-6X Jr depth-keyed (5-6 oz) vs current-keyed (8/4 oz) conflict, and quotes the same report saying late October is 'not really a prime time' rather than selling 'fall spot'. actionable: numbered drop-to-hookset sequence, when yo-yo is the wrong tool (40-60 ft staging fish), two named failure modes including bonito bycatch inside a closure where bonito is keepable, and four concrete inventory gaps.

<details><summary>Full prompt</summary>

How do I fish a yo-yo iron at Farnsworth Bank? Retrieve, depth, current, and the tackle to use.

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Yo-yo iron at Farnsworth Bank

**Up front, so you can calibrate:** the KB has a lot on *how to fish a yo-yo iron* and on *what kind of spot Farnsworth is*, but almost nothing that is specifically about Farnsworth. Two sentences is the whole of it. Everything else below is the general SoCal yo-yo doctrine applied to a standalone-bank spot — I've flagged where I'm extrapolating.

---

## 1. What the KB actually says about Farnsworth

- **It's a fall yo-yo spot for yellowtail.** "Farnsworth Bank … gives good **fall yo-yo fishing**" (`species/yellowtail.md`, from the 10/26/22 report, video `5p6gu14ZC4w`). The note flags that the name was caption-garbled as "foreign First Bank" and was identified by the described closure rule — so treat the name attribution as reconstructed, not verbatim.
- **Closure — read this before you go.** The same note says it "sits in a marine closure where **only yellowtail and bonito may be kept**" (`species/yellowtail.md`, `5p6gu14ZC4w`), and the spot library lists it as **"Farnsworth Bank (partial-take SMCA — see DFW)"** (`sources/spot-lists.md`). **The KB carries no jurisdiction stamp or as-of date on that claim** — verify the current CDFW rules for the Farnsworth Bank SMCA yourself before fishing. Convenient for you: yellowtail is exactly what the yo-yo is for there.
- **Position:** `33 20.560 N / 118 31.010 W`, Catalina backside, between Ben Weston Point and China Point in the W→E backside run (`sources/spot-lists.md`).
- **Structure type — this is the load-bearing one.** Farnsworth is the KB's *named archetype* for a **standalone bank**: "structure rising off the plain, not attached to land," and standalone banks **fish in any current direction, but each individual bank still has its own preferred directions. You learn a standalone bank's good directions spot by spot; there is no single rule"** (`locations/island-structure.md`, `conditions/current-structure.md`). So the parallel-current rule that governs land-attached island ridges **does not gate Farnsworth** — you don't get to write the day off because the current is running into or off the beach. But the KB does **not** tell you Farnsworth's preferred directions. That's yours to log.

---

## 2. Current — how to read it and what it tells you to do

**The go/no-go is not direction, it's whether the water is running at all.** The KB's failure mode for a standalone bank is dead water, not wrong-direction water.

- **Bias to the up-current face.** Upwelling forms where current impinges on structure, so "bias toward the **up-current face** under whatever current vector is running that day" — that's where the food chain stacks (`conditions/current-structure.md`).
- **Read strength off the kelp — this is your yo-yo-vs-surface-iron switch** (`conditions/current-diagnostics.md`):
  | Kelp | Current | Call |
  |---|---|---|
  | Pulled **~20 ft under** | Raging | Surface presentations are **dead** — go deep/weighted. **This is the yo-yo's day.** |
  | **Laid flat** on the surface | Strong | Fishable but hard; work the down-current side |
  | **Resurfacing / standing back up** | Slacking | **Switch back** to surface iron |
  The `techniques/yo-yo-iron.md` "reach for this when" list says the same thing directly: when kelp is pulled under or laid flat, go vertical; when it resurfaces, go back to [surface iron](techniques/surface-iron.md).
- **"The treadmill is off."** No current at anchor reads as **bait pointing in all directions** (not lined up) plus **fish metering but not biting**. Marks will not convert. Move or wait for the tide change (`conditions/current-diagnostics.md`). A second tell from Dave Hansen: baits getting hit nearly every drop, then several drops in a row with nothing, is often the first sign the current just stopped.
- **Separate true current from wind push** by the **chum-drift angle relative to how the boat is lying** — drift straight off the stern = wind-dominated; drift swinging off at an angle = real current cutting across, and that angle is your direction sensor (`conditions/current-diagnostics.md`).
- **Timing:** be on the highest-percentage zone **an hour before the tide change**, not at it; the **late-morning slack** (tide falling after ~09:30) is the prime pop-up window, with a second afternoon cluster — re-run water you marked earlier at those tide times (`conditions/tide-and-slack.md`, `5p6gu14ZC4w`). On marginal/post-moon days, action **compresses into the tide windows**; on strong days it isn't tide-gated.
- **Spatial coherence saves you a lap:** current direction is coherent across the region on a given day — read it once (at any Catalina backside stop), apply it to every spot on the list, then confirm with the kelp/chum tells at each (`conditions/current-structure.md`).
- **Boat handling on the drop:** position **up-current of the mark so the drop sweeps down onto the structure** (`techniques/yo-yo-iron.md`).
- *Baja data point, labeled as such:* at San Benito Island a surface-iron yellowtail bite died at anchor while the fish still marked; the crew's fix was to **position above the marks and drift through** instead of staying pinned, and the bite came back (`planning/electronics-and-sounder.md`, `97clKtVsEOs`, unregistered channel, medium confidence). Not a Farnsworth observation — offered as an anchor-to-drift pivot to keep in your pocket.

---

## 3. Depth — what to look for, and where to drop

**The KB gives no depth or bathymetry for Farnsworth Bank at all** — no crest depth, no fathom range, nothing beyond the coordinates. So the depth answer is "whatever your meter says," driven by these SoCal reads:

**The yellowtail sonar signature** (`species/yellowtail.md`, `D5DR7Kx42_A`):
- **Tight balls hugging the structure** on hard bottom, pinnacles and high spots; the classic yellowtail read is **arcs / boil-ups at ~5–10 fathoms (30–60 ft) near structure**. "We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite."
- **Hard bottom only, never mud** — structure yellows sit exclusively on hard/rocky bottom (Dave Hansen, `6DzbsElGE7E`). Read bottom hardness off **return thickness**: thin/faint = sand/mud, thicker/darker = rock. Grade the bottom *before* you look for fish sign on it.
- **A thin, lighter mark riding higher than the bait ball can be the yellowtail itself**, pushing bait up off the rocks — that's the commit signal, not the bait pile alone (same source).
- **Stop only on marks you can grade — it's a bait budget** (`planning/electronics-and-sounder.md`).

**Sounder setup:** run **manual range, not auto**, sized so the bottom sits roughly **mid-screen** rather than pinned at the edge — that leaves vertical room to separate hard from soft bottom and to pick fish out of the column above it (Dave Hansen, `FEXgl0eQCa8`; the core "manual not auto" rule repeats across three of his videos and sits at high confidence in `planning/electronics-and-sounder.md`).

**Depth bands the corpus actually gives, SoCal:**
- **Tanner Bank, 2024-08-29** (`ntQXxcH5sjI`, StokedOnFishing, unregistered channel — medium confidence): dropping to about **80 ft** with bait marks sitting around **60 ft**.
- **Hansen's near-bottom band, SoCal coast, spring squid/red-crab bottom** (`wzI0lpgKT1U`, registered voice — high confidence): **120–200 ft of water with fish suspended ~20 ft off the bottom** — work the **100–120 ft band when marks sit at 120 ft**, cycling the same ~20-ft band rather than winding up out of it.
- The router's shorthand for structure yellows: **hit bottom, a couple cranks off the bottom = reaction bite** (`species/yellowtail.md`).

*Baja contrast block (do not mix into your Farnsworth numbers):* at Cedros Island crews called drops at **212 ft** with fish showing anywhere **50–150 ft**, and a **130 ft** drop at San Augustine that got bit on the second drop (`techniques/yo-yo-iron.md`, `A8SuzB5qiKE`, `u0scEBby7nA` — unregistered channel, medium confidence).

---

## 4. The retrieve — and the honest conflict in it

The KB keeps **three cadences side by side, unreconciled** (`techniques/yo-yo-iron.md`). Section order there is not a ranking; pick by what the fish are doing.

**The drop, common to all three:** **free-spool the iron straight down**, thumbing the spool so it falls under light tension and **tracks straight down rather than scoping away from the boat**. Keep the **ready-position grip the whole way down** — index finger resting on the spool, thumb on the reel's trigger, left hand forward — so you snap straight into gear on the bite instead of fumbling for the lever (`tackle/rod-and-reel-selection.md`, `F0g5r9Rkrd4`; repeated in the dropper-loop walkthrough, high confidence on the grip).

**Cadence A — continuous wind to the top (this note's baseline doctrine).** Drop to the mark, then **wind as fast as you can, all the way up**. There is no finesse cadence — **the speed is the trigger**; the strike is a reaction to the fleeing iron. Nothing hits, drop back to the mark and rip it again.

**Cadence B — crank-then-freespool, staying in the zone (Capt. Dave Hansen, `wzI0lpgKT1U`, 2021-03-16; registered voice — high confidence).** Hansen explicitly defines "yo-yoing" as a repeated cycle that **stays down in the strike zone**, not one wind to the surface:
- *Working water (cast-and-retrieve):* cast, free-spool **all the way to the bottom**, engage, crank as fast as possible for **10 cranks**, straight back to freespool, sink to bottom again — repeat in **10-crank increments**, walking the iron back toward the boat over as much as **150 yards**. His stated reason: winding continuously the whole way pulls the iron up out of the band where suspended fish are holding and off the angle that makes it look like a fleeing baitfish.
- *Straight up-and-down under the boat:* in gear for **five or six quick cranks (~20 ft of retrieve)**, straight back to freespool, let it fall, repeat — cycling the band where fish are marked. **Never let the jig sit dead on the bottom, and never wind it up out of the zone.**
- **Strikes often come on the drop**, not the crank — the falling iron on freespool looks like a dying baitfish.

**Cadence C — two partial cranks, then a full wind (San Benito Island, Baja — `SH7zOA9ZF3o`, unregistered channel, medium confidence).** Free-spool to the bottom, "reel like the devil" **about halfway up**, out of gear and fall straight back to bottom, crank halfway up again, fall back to bottom again, then **reel it all the way up** to finish. Region-labeled Baja; carried here because it's a third distinct answer to your exact question.

**What the bite feels like:**
- On the crank: the rod suddenly **goes heavy — "almost like it got stuck on the bottom"** — rather than an obvious rap (`ntQXxcH5sjI`, Tanner Bank, medium confidence).
- On the sink: often a **brief stop** before the fish takes off with it (`wzI0lpgKT1U`).
- Set by **winding to the bite**, not a big swing.
- *Baja data point:* at Cedros, anglers called hookups both **right on the drop and on the wind-up**, not only on the fall (`ILBl12Jm7-0`, medium confidence).

**Common failures** (`techniques/yo-yo-iron.md`):
1. **Iron too light for the current** — never reaches the mark, or planes off sideways and never fishes vertical.
2. **Winding too slow** — a lazy grind gets refused; the bite comes off speed.
3. **Fishing yo-yo when the surface is alive** — if fish are boiling or the kelp is standing, surface iron reaches more fish.
4. **The physical toll** — the lift-reel-drop cycle punishes arms and shoulders over a long session, and the rapid aggressive action **can spook more cautious fish** (`ntQXxcH5sjI`).

**A trick worth having at Farnsworth:** at San Clemente Island an angler **downsized to a smaller yo-yo iron and drew a bite** while others worked surface iron up top over fish the Simrad showed holding below — two crews working the same column at different depths at once (`ecJPMTCi-gw`, SoCal, unregistered channel, medium confidence; no bait-size reason stated). The Baja version of the same move ties the downsize to small forage — red crabs, small sardines.

---

## 5. Tackle

**Class terms** (`tackle/gear-classes.md`, `species/yellowtail.md`):
- **Rod — yo-yo / heavy-iron class:** **~8 ft, XH, 40–80 lb, fast crank.** The yellowtail router states it as a **stout 40–60 lb class rod with a high-speed reel** to burn a heavy iron off the bottom. A 10 ft jig stick (Phenix Axis class) also works if you want to cast-then-yo-yo the same iron.
- **Reel:** high-torque conventional wound tight. The appeal is a hard, fast retrieve — **a strong power grind matters more than top gear ratio** (`techniques/yo-yo-iron.md`). Counterpoint from the same note: for an angler who isn't a strong cranker, a **~6.6:1 ratio** makes it easier to take line fast enough on the wind-up (Scotty, Brothers Sportfishing, `VpW91AKOFVQ`, registered — high confidence).

**The iron:**
- **Heavy yo-yo class — Salas 6X or Salas CP 105 type.** Weight is the whole point: **roughly 5–6 oz against a surface iron's 2–3 oz**, heavy enough to sink fast and **hold vertical** in current (`VpW91AKOFVQ`, high confidence). Tady 4/0 and heavier CNC irons fill the same role; 6X/7X-class solid irons are the documented rotation (`lures/iron-jigs.md`).
- **Colors — traditional yo-yo colors for yellowtail: scrambled egg, and blue and white** (Ray Sharifi, `A70kK2niu2Q`, unregistered channel — medium confidence). Dorado-pattern irons also show up repeatedly in the corpus.
- **Hooks — assist vs treble is a live judgment call, not a rule.** On bigger fish, two points of a treble share one shank and can "auger" each other back out; assist hooks ride on **separated cords** so two stuck hooks aren't fighting each other — the stated reason bigger-fish gear favors assists (`lures/iron-jigs.md`, `VpW91AKOFVQ`).

**Line — three documented builds, kept side by side because they disagree about fluorocarbon:**
| Build | Main | Leader | Source |
|---|---|---|---|
| Tanner Bank, SoCal | 65 lb braid | **40 lb fluoro**, uni-to-uni; Salas 6X Jr blue/white; Okuma PCH XH rod | `ntQXxcH5sjI` (medium) |
| Dirty Hookers, 2023 | — | **50–80 yards of mono top shot straight to the jig, no fluoro**; 7 ft Black Diamond XH 30–80 lb + Torium 16HG | `LTCFjqtSI8g` (medium) |
| Dirty Hookers, 2022 | — | 7 ft heavy 30–80 lb rod (general guidance **40–60 lb rated**), enough tip left to wind through the bite; Trinidad 20A | `A70kK2niu2Q` (medium) |

**If you're Cameron, the profile resolves the classes to:** the **Trinidad 40 setup** — M&M custom on a Rainshadow RCJB96XH blank, **8'0", XH, 40–80 lb, 4–10 oz**, Shimano Trinidad 40, **80 lb braid** — which `profiles/cameron/rods.md` names as the heavy yo-yo/sinker-rig setup, and which `techniques/yo-yo-iron.md` names outright as "Cameron's yo-yo rod." Owned irons that fit: **Salas 6X (blue)** and **Salas CP 105 (silver/chrome)** (`profiles/cameron/tackle.md`). Your 10 ft Phenix Axis jig stick is logged as an open item — you've wanted reps yo-yoing it.

**Rig all three, don't commit to one.** Cameron's own stated doctrine in `species/yellowtail.md`: rig the **surface-iron outfit, the heavy yo-yo/dropper outfit, and the flyline outfit simultaneously** and switch as the read changes — "the faces are states, not types."

**If the yo-yo gets refused on marks you trust:** the router's #2 for the same tight-balls-on-structure situation is the **dropper loop** on the same heavy rod — **6–10 oz sinker, hook on a long loop above it; up the weight if the current is heavy** (`techniques/dropper-loop.md`, `species/yellowtail.md`). The corpus change-up on the same marks is a **vertical/flat-fall jig, 100–180 g depending on current** (`D5DR7Kx42_A`).

---

## 6. What the KB does not cover for this spot

I'd rather say it than paper over it:

1. **No depth or bathymetry for Farnsworth** — no crest depth, no fathom range, nothing. Your meter is the only depth source.
2. **No preferred current directions for Farnsworth.** The KB explicitly says standalone banks each have their own and that you learn them spot by spot — and then gives you none for this bank. Log yours.
3. **No tide/slack timing specific to Farnsworth**; the arrival-before-the-change rule is general SoCal doctrine.
4. **The closure claim is unstamped** — no jurisdiction, no as-of date, and the underlying source caption was garbled. Check current CDFW rules for the Farnsworth Bank SMCA before you fish, and don't rely on the KB's "yellowtail and bonito only" phrasing as legally current.
5. **No iron weight, size or color specific to Farnsworth** — only class-level guidance.
6. **No season window beyond "fall."** No month-by-month prior for this bank; `seasonal/october.md` doesn't mention it.
7. **No anchor-vs-drift or boat-positioning guidance for this bank specifically** — the only anchor-to-drift pivot in the KB is a Baja observation.
8. **No cadence recommendation for this spot** — you're choosing between three unreconciled cadences on your own read.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/yo-yo-iron.md`, `lures/iron-jigs.md`, `species/yellowtail.md`, `locations/island-structure.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/tide-and-slack.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `planning/electronics-and-sounder.md`, `techniques/dropper-loop.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`, `seasonal/october.md`  
*videos:* `5p6gu14ZC4w`, `D5DR7Kx42_A`, `6DzbsElGE7E`, `wzI0lpgKT1U`, `ntQXxcH5sjI`, `VpW91AKOFVQ`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `ecJPMTCi-gw`, `SH7zOA9ZF3o`, `ILBl12Jm7-0`, `A8SuzB5qiKE`, `u0scEBby7nA`, `97clKtVsEOs`, `F0g5r9Rkrd4`, `FEXgl0eQCa8`  
*gaps admitted:* No depth, crest height, or bathymetry for Farnsworth Bank anywhere in the KB — only the coordinates 33 20.560 / 118 31.010 in sources/spot-lists.md. | No preferred current directions for Farnsworth specifically; the KB states standalone banks each have their own and that you must learn them spot by spot, then supplies none for this bank. | No Farnsworth-specific tide or slack timing — only the general SoCal arrive-an-hour-before-the-change and late-morning-slack doctrine. | The 'only yellowtail and bonito may be kept' closure claim carries no jurisdiction and no as-of date, and its source caption was garbled ('foreign First Bank') — it is not verifiable as current regulation from the KB. | No Farnsworth-specific iron weight, size, or color — guidance is class-level only (heavy 5-6 oz Salas 6X / CP 105 class). | No season window for Farnsworth beyond the single word 'fall'; seasonal/october.md and seasonal/november-december.md do not mention the bank. | No anchor-vs-drift or boat-positioning guidance for Farnsworth; the only anchor-to-drift pivot in the KB is a Baja (San Benito Island) observation. | The KB gives three unreconciled yo-yo retrieve cadences and no guidance on which applies at this bank. | No information on whether the Farnsworth yo-yo bite is a bottom-hugging or mid-column bite, or what depth band the fish typically hold in there.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

# Yo-yo iron at Farnsworth Bank

**First, what the KB actually knows about this spot.** Farnsworth is thin in this knowledgebase. There is no location note for it. What exists is three things:

- It's charted in the spot library under **Catalina Island — Backside (W→E)** at **33 20.560 / 118 31.010**, sitting between Ben Weston Point and China Point, and it's flagged **partial-take SMCA — see DFW** (`sources/spot-lists.md`).
- The yellowtail router says Farnsworth gives **good fall yo-yo fishing**, and that it sits in a marine closure where **only yellowtail and bonito may be kept** (`species/yellowtail.md`, `5p6gu14ZC4w`, 10/26/22). Same source: ~40 yellows in a day at Catalina in late October, and "no reason you couldn't catch a yellowtail" while temps stay good even outside prime time. **Treat the take rule as a regulation, not fishery knowledge** — the note carries no as-of stamp or jurisdiction, so verify the current partial-take SMCA rules with CDFW before you keep anything.
- Structurally it's the KB's named example of a **standalone bank** — "structure rising off the plain, not attached to land" (`locations/island-structure.md`, `conditions/current-structure.md`, Academy Ep. 14 / 2-20-25 report).

Everything below is the general yo-yo doctrine applied to that structure type. Where the KB has no Farnsworth-specific number, I say so rather than inventing one.

---

## 1. Current — this is the part that decides the day

**Farnsworth's structure class fishes any current direction — but with a caveat you have to solve on the water.** Land-attached perpendicular ridges are two-directional spots that only work on parallel current; coastal deep spots default-prefer downhill (N→S); **standalone banks (Farnsworth type) fish in any direction, but each individual bank has its own preferred directions, and there is no single rule — you learn them spot by spot** (`locations/island-structure.md`, `conditions/current-structure.md`). **The KB does not record Farnsworth's preferred directions.** That's a real gap, not a shortcut you can take.

What you *can* apply:

- **Fish the up-current face.** Upwelling forms where current impinges on the structure; with the summer uphill (counter) current that's the **lower / south face** of a bank — "that uphill current hits the lower end of those banks." Within-bank spot selection: bias toward the up-current face under whatever vector is running that day, because that's where nutrients are forced up and the food chain stacks (`conditions/current-structure.md`, Academy Ep. 1).
- **Read current strength off the kelp, if there is any.** Kelp pulled ~20 ft under = **raging** — surface presentations are dead, go deep/weighted. Kelp laid flat = **strong** — fishable but hard, work the down-current side. Kelp resurfacing = **slacking** — switch back to the surface (`conditions/current-diagnostics.md`, 8-31-22 `HnqiE05vdXs` / Academy Ep. 14). That transition is the trigger to swap between yo-yo and [surface iron](techniques/surface-iron.md) — the yo-yo note names "kelp pulled under or laid flat" as its own reach-for-this-when condition (`techniques/yo-yo-iron.md`).
- **On a bare rock bank with no kelp and no buoys, you have no visual tell — the anchor line *is* the current sensor.** Drop the anchor and watch which way the line points once it sets; that first read can be wrong, and resetting is normal, not a bad read. One presenter pulls and resets **10–12 times in a day** to stay precisely on the spot he wants (Dave Hansen, `sIoNELGlxmk`, 2023-03-04, in `conditions/current-diagnostics.md`).
- **Separate true current from wind push** with the chum line: chum drifting straight back in line with the boat = wind-dominated lay; chum swinging off at an angle to the boat's lay = real current cutting across, and that angle is your direction sensor. **Do not trust the chart plotter's current-arrow layer — it's reading wind** (`conditions/current-diagnostics.md`, 2-20-25; `BskCsKaTiZw`).
- **No current at anchor = "the treadmill is off"**: bait pointing every direction, fish metering but not biting (`conditions/current-diagnostics.md`).
- **Wind/swell picks the side of Catalina.** A big west swell is the trigger to send anglers **down to the east end**; a south swell tears up the east end and reverses the pattern the fish are conditioned to (Dave Hansen, `aFb221LUoD0`, 2020-10-20, in `locations/island-structure.md`). Farnsworth is on the **backside** — one observed data point has a team finding the West End "just blowing," worse the further back along the backside they went, and retreating to the front side (`PKf7G3uL4io`, ~Nov 2014). The KB does not state Farnsworth's own preferred wind, and it warns that each spot has one.

**Positioning for the drop:** set up **up-current of the mark so the drop sweeps down onto the structure**, and **free-spool the iron straight down, thumbing the spool** so it falls under light tension and tracks vertical instead of scoping away from the boat (`techniques/yo-yo-iron.md`). If it does scope out toward the horizon, two attributed fixes are kept side by side: **wind it in and drop it back down to reset vertical**, cycling drop-wind-drop rather than leaving it scoped (`Vbf40qvH9-Q`), or **flick it a little further up-swell** so the boat drifts down onto it as it sinks (`sJGs-Jqt9Vo`) — both in `conditions/current-diagnostics.md`. Scope costs you bite feel and builds slack between rod tip and jig that you have to catch up on when the bite comes.

---

## 2. Depth — what to look for and how deep to drop

**The KB gives no depth figure for Farnsworth Bank itself.** You'll be reading it off your own sounder. What the notes do give:

**Marks that mean yellowtail** (`species/yellowtail.md`):
- **Tight balls hugging the structure** on hard bottom, pinnacles and high spots — the classic read being **arcs / boil-ups at ~5–10 fathoms near structure** (`D5DR7Kx42_A`). "Tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite."
- **Hard bottom only, never mud** — thin return = sand/mud, thick return = rock. Read bottom hardness to decide whether the spot is worth working before you hunt for fish sign (`6DzbsElGE7E`).
- **A thin, lighter mark riding above the bait ball is often the yellowtail itself**, pushing bait up off the rocks — that's the commit signal, not the bait pile alone (`6DzbsElGE7E`).
- **Behaviour beats depth:** fish **up in the column and spread out** eat; fish **tucked tight on the bottom** don't (`HTowqnwAMeA`). A **stratified column** (marks running bottom-up through mid-column) = actively hunting; a **ball stuck to the bottom** = present but not hunting, which is dropper-loop water more than flyline water.
- **The 40–60 ft band rules the yo-yo out.** Fish metered at 40–60 ft and not yet showing were called on camera as "surface iron fish and light bait zone — so we're not going to be yo-yoing today" (`0DKmYId1NN4`, 2026-03-21). That's a stated threshold that picks the technique *before* the fish show.
- **A marked school that never surfaces is still worth fishing vertically:** "just about every lure that makes it down to the depth that fish is, is a bite," and the same source says yo-yo has "absolutely" out-fished live bait multiple times in that scenario (`tpmOYXYQwhU`, 2020-04-21).

**Drop depth and jig size, the ladder** (`techniques/yo-yo-iron.md`):
- Typical yo-yo depth on overnight/multi-day trips runs **120–240 ft**; check with the crew what depth and jig size is producing before you drop (`UP_3fBu7VPA`, 2024-03-20).
- **150–250 ft → full-size 6X-class iron**; shallower, or when getting down fast matters less → **smaller iron (6X Jr, or a Tady 40-class jig)** (`UP_3fBu7VPA`).
- Three-tier version: **60 / 80 / 100 ft → a small jig (6X Jr class)**; **120–150 ft → a Salas 6X, roughly 5–6 oz**; **real deep → a 7X heavy**, on the reasoning that more time in the strike zone on the straight up-and-down improves your odds (`hteLeDIy9Qs`, 2020-10-15).
- Base case for average **12–30 lb yellowtail near an island or bank** is stated as **120–180 ft** (`RNRFrfepiW0`, 2023-04-27).
- **When a depth is called with no bottom to reference, get the jig a little deeper than the called depth, then wind up through the school** at full speed the whole way (`RNRFrfepiW0`).
- **Upsize the iron for wind or strong current** — light current and nice weather → small jig; wind or hard current → upsize. The reason given is a **time budget**, not action: "you don't want to spend the majority of your time in free spool waiting for your lure to hit bottom when you could be actively working up and down in a zone" (`HTowqnwAMeA`). Too light and it also planes off sideways and never fishes vertical.

---

## 3. The retrieve — and the honest conflict in it

The KB carries **several cadences side by side, attributed and deliberately not reconciled**. Section order is not a ranking. What the choice turns on, from the reasons the sources themselves give, is **where the fish are sitting in the column and how long a session you're fishing**.

**A. Continuous full-speed wind to the top** — the note's headline doctrine. Free-spool to the mark or the bottom, engage, and **wind as fast as you can, all the way up**. The strike is a reaction to the fleeing iron; there is no finesse cadence, **the speed is the trigger**. If nothing hits, drop back and rip it again. Grip: once the jig hits bottom and the reel's in gear, **tuck the rod under your left armpit** and crank — "you cannot crank the jig too fast, but it's easy to crank it too slow" (Steve Carson, `RNRFrfepiW0`, 2023-04-27).

**B. Crank-then-freespool cycles that stay down in the zone** — Capt. Dave Hansen defines yo-yoing as this, explicitly *not* one continuous wind (`wzI0lpgKT1U`, 2021-03-16):
- *Straight up-and-down under the boat:* **five or six quick cranks (~20 ft of retrieve)**, then straight back to free spool and let it fall; repeat, cycling the band where fish are marked — e.g. **120–200 ft of water with fish suspended ~20 ft off the bottom** (work the 100–120 ft band when marks sit at 120 ft). Never let it sit dead on the bottom, never wind it up out of the zone.
- *Working water, cast out:* free-spool to the bottom, crank hard for **10 cranks**, back to free spool to the bottom, repeat in 10-crank increments while walking the iron back toward the boat over as much as **150 yards**. His stated reason: winding continuously pulls the iron up out of the band where suspended fish hold and off the fleeing-baitfish angle.
- **Strikes often come on the drop** — the falling iron on free spool looks like a dying baitfish.

**C. Half-depth wind, then re-drop** — free-spool to the bottom, crank as fast as possible **only about halfway back up** (his worked example: in **120–150 ft**, wind **60–70 ft** off the bottom), then free spool back to the bottom and repeat. Two stated reasons: it **saves your arm** over a long session, and it keeps the iron in the band **close to the bottom where the fish are actually holding** (SearcherSportfishing, `SAltQjih0ms`, 2020-05-20).

**D. Two partial cranks, then a full wind** — bottom, crank hard about halfway up, out of gear back to the bottom, halfway up again, back to the bottom, then reel it all the way up to finish the cycle (`SH7zOA9ZF3o`, San Benito, 2015).

**Rules all of them agree on:**
- **Do not set the hook. Keep cranking through the bite.** "Just keep grinding — that fish is stronger than you and if you just keep winding, he's going to set the hook himself" (`5pbA-wXoric`, `ETw_3AFxEcM`). Get the rod on the rail and keep turning the handle.
- **Do not work the iron with short hops right at the bottom.** That's called out by name as the wrong motion — **bouncing it in place near the bottom draws rockfish instead of yellowtail** (`SAltQjih0ms`). A separate source adds that continuous in-place jigging inside a marked school can spook and disperse the whole school (`6Z6Dht20kTA`, `S0-BCQWA0H4`).
- **Winding too slow gets refused** — a lazy grind is the classic failure (`techniques/yo-yo-iron.md`).
- **Bites come on the drop and on the wind-up**, both (`ILBl12Jm7-0`).

**One preference kept beside the vertical doctrine, not replacing it:** Nate Winnicki casts the jig out (or flips it away from the boat) so the line sits at roughly **45°** on the wind-back rather than working it straight up and down — his stated reason is that the diagonal path makes the jig behave more naturally, and he's explicit that he's seen fish caught both ways (`HTowqnwAMeA`, in `techniques/yo-yo-iron.md`).

**My read for a standalone bank like Farnsworth:** cadence follows the mark. Fish stacked in a tight band off the bottom → **C or B**, cycle that band and save your arm. Fish stratified up through the column, or a school the captain calls at a depth → **A**, get below them and wind through.

---

## 4. Tackle

**Class terms** (`tackle/gear-classes.md`, `species/yellowtail.md`):
- **Yo-yo / heavy-iron class rod: ~8 ft, XH, 40–80 lb, fast crank.** The yellowtail router's short version is "a stout **40–60 lb class** rod with a **high-speed reel** to burn a heavy iron (Salas 6X class) off the bottom."
- **Reel:** high-torque conventional wound tight — a strong power grind matters more than top gear ratio, because the appeal of yo-yo is a hard fast retrieve (`techniques/yo-yo-iron.md`).

**Concrete builds the KB carries**, all in `techniques/yo-yo-iron.md`:

| Build | Spec | Source |
|---|---|---|
| Base case, 12–30 lb fish, 120–180 ft | Two-speed **Penn Fathom 30**, **65 lb braid**, **50-yard 40–50 lb mono top shot** (stretch, plus it helps when a hooked fish tangles a neighbor), **8 ft rod rated 30–60 lb**, treble hook, **Tady 4/0** | `RNRFrfepiW0` |
| Recreational, direct-tied | Two-speed conventional, **80 lb braid → 40–60 lb mono top shot, no fluorocarbon**, iron tied straight to the top shot on a **[San Diego jam knot](rigging/san-diego-jam-knot.md)**, **7 ft** rod stiffer-tipped than a flyline stick. **High gear while searching/retrieving; shift to low gear only after the fish is hooked** | `SAltQjih0ms` |
| Bigger/meaner fish, rocky ground, windy, or trouble getting down | Two-speed **Penn Fathom 40 Narrow**, **80 lb braid**, **60 lb mono top shot**, shorter more powerful **30–80 lb rod** | `RNRFrfepiW0` |
| Retrieve-rate pick | **Penn Torque 40** on a 40–100 lb rod, chosen for **43 in of line per handle turn** — the technique "needs a fast action reel that retrieves a lot of line at a time" | `7Ljt-DeFVcs` |
| For anglers who aren't strong crankers | A **~6.6:1** ratio reel, so they can take line fast enough on the wind-up | `VpW91AKOFVQ` |
| Leader detail worth stealing | If you want fluorocarbon, run a **short piece of mono between the braid and the short fluoro leader** — going straight from spectra to a short fluoro with no stretch buffer **bends and pulls hooks** | `hteLeDIy9Qs` |

**Line class:** **40 lb minimum, 50–60 lb preferred** (`UP_3fBu7VPA`). The stated reasoning for going heavy: "40 lb works, 50 lb is better, 60 lb better still, **because the fish don't care**" — no bite-rate cost to fishing as heavy as you can still crank fast and control the fish (`5pbA-wXoric`).

**The iron:** heavy yo-yo class — **Salas 6X** and **Salas CP 105** are the classic benchmarks, Tady 4/0 and heavier CNC irons fill the same role. Weight **roughly 5–6 oz** against a surface iron's 2–3 oz, heavy enough to sink fast and hold vertical (`lures/iron-jigs.md`, `VpW91AKOFVQ`).

**Colors:** the classics are **scrambled egg, blue and white, mint**. The mechanism: **blue and white when they're on thin baits — anchovies, sardines; scrambled egg when they're on invertebrates — squid or crabs**; mint is a stated go-to with no forage reason given. **Red-toned jigs produce specifically during red-crab years** — match forage color to what's present rather than carrying a fixed favorite (`ETw_3AFxEcM`, `UP_3fBu7VPA`).

**Hooks:** treble or one/two single assist hooks on braided cord — a live judgment call, not a fixed rule. Assist hooks are favored for bigger fish because a treble's three points share one shank and can auger each other back out, while assists ride on separated cords (`VpW91AKOFVQ`, `lures/iron-jigs.md`). If you fish a treble, **keep the line tight through the drop** rather than free-falling on slack — the extra flutter lets trebles foul on your own line (`r7Bv49Ysgdw`).

**Against the one profile in this KB (Cameron's):** the yo-yo outfit is **Setup 1, the Trinidad 40** — M&M custom on a Rainshadow RCJB96XH blank, **8'0", XH, 40–80 lb, 4–10 oz**, Shimano Trinidad 40, **80 lb braid**, explicitly logged as the heavy yo-yo/sinker-rig rod with a relatively soft tip (`profiles/cameron/rods.md`). Owned yo-yo irons: **Salas 6X (blue)** and **Salas CP 105 (silver/chrome)** (`profiles/cameron/tackle.md`). That's a clean match to the class. Two gaps worth naming rather than papering over: **no scrambled-egg or red-toned yo-yo iron is listed in the inventory** — if squid or red crab are the forage, the color doctrine above says you're short the right jig — and the profile records braid only, not a top shot, so build the 40–60 lb mono top shot (or the mono-buffer-then-fluoro version) before the trip.

---

## What this KB can't tell you about Farnsworth

I want to be blunt about the edges, because a couple of them matter a lot for this specific spot:

1. **No location note, no depth, no contour, no description of the pinnacle** — only a coordinate row and the "standalone bank" type classification.
2. **No record of Farnsworth's preferred current or wind directions**, which is exactly the thing the standalone-bank rule says you have to know and learn spot by spot.
3. **No Farnsworth-specific drop depth** — every depth number above is general yo-yo doctrine.
4. **No tide/slack or bite-window guidance tied to this bank.**
5. **The take restriction is unstamped** — verify the partial-take SMCA rules with CDFW yourself before keeping a fish.
6. **You gave me no conditions**, so I've pulled none and assumed none. Before you go, run the day-plan protocol properly (`planning/day-plan-protocol.md`): conditions per zone and along the transit, then priors and layers, then the species router. The coordinate **33 20.560 / 118 31.010** is what you'd feed BightSST for the per-spot pull.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/yo-yo-iron.md`, `lures/iron-jigs.md`, `species/yellowtail.md`, `locations/island-structure.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `tackle/gear-classes.md`, `sources/spot-lists.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `rigging/san-diego-jam-knot.md`, `locations/zone-lexicon.md`, `locations/bight-geography.md`  
*videos:* `5p6gu14ZC4w`, `D5DR7Kx42_A`, `6DzbsElGE7E`, `HTowqnwAMeA`, `0DKmYId1NN4`, `tpmOYXYQwhU`, `RNRFrfepiW0`, `UP_3fBu7VPA`, `hteLeDIy9Qs`, `SAltQjih0ms`, `wzI0lpgKT1U`, `SH7zOA9ZF3o`, `5pbA-wXoric`, `ETw_3AFxEcM`, `7Ljt-DeFVcs`, `VpW91AKOFVQ`, `ILBl12Jm7-0`, `6Z6Dht20kTA`, `S0-BCQWA0H4`, `r7Bv49Ysgdw`, `Vbf40qvH9-Q`, `sJGs-Jqt9Vo`, `sIoNELGlxmk`, `BskCsKaTiZw`, `HnqiE05vdXs`, `aFb221LUoD0`, `PKf7G3uL4io`  
*gaps admitted:* No location note exists for Farnsworth Bank — no depth, bathymetry, pinnacle description, or size; only a coordinate row in sources/spot-lists.md and a structure-type classification. | The KB does not record Farnsworth Bank's preferred current directions, even though its own standalone-bank rule says each bank has preferred directions you must learn spot by spot. | No Farnsworth-specific drop depth or depth band — all depth numbers given are general yo-yo/yellowtail doctrine from elsewhere in the corpus. | No Farnsworth-specific preferred wind direction, despite the KB stating that individual Catalina spots each have one. | No tide, slack-water, or bite-window timing guidance tied to Farnsworth Bank. | The 'only yellowtail and bonito may be kept' closure claim carries no jurisdiction stamp, as-of date, or verify-current flag in the note — it must be checked against current CDFW rules. | No anchoring-vs-drifting doctrine specific to Farnsworth Bank (only the general hard-bottom anchor-line current read). | No conditions were supplied in the question and none were pulled — no SST, chlorophyll, wind, swell, or current data informs this answer. | The KB gives no Farnsworth-specific forage record (squid vs. red crab vs. anchovy), which is what the color-selection doctrine actually keys on. | Cameron's profile records braid weight only for the Trinidad 40 yo-yo setup; no top-shot or leader spec is recorded, and no scrambled-egg or red-toned yo-yo iron is in his logged inventory.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Yo-yo iron at Farnsworth Bank

**First, the honest framing:** the KB has **no spot page for Farnsworth Bank**. `locations/catalina-island-backside.md` says so outright — "`locations/farnsworth-bank.md` was never written (the worklist row is `escalated`)" — so there is **no charted depth, bottom composition, or working depth band** for this bank anywhere in the KB. What follows is the bank's *structure type* and *regulatory status* from the zone page, plus the general yo-yo doctrine, which you then key to what your own meter shows on the day.

Charted position, from the spot library (`sources/spot-lists.md`): **33 20.560 / 118 31.010**, listed as "Farnsworth Bank (partial-take SMCA — see DFW)".

---

## Before you drop: the closure

Inside the closure area **only yellowtail and bonito may be kept** — everything else goes back (`5p6gu14ZC4w`). Stamped **as of 2022-10**; **verify current MPA rules with CDFW before fishing** (`species/yellowtail.md`, `species/bonito.md`, `locations/catalina-island-backside.md`).

That claim carries a live fact-check flag in the KB: the source says only "Marine closure," names no agency, no boundary and no as-of date, and the auto-caption garbles the bank's name to "foreign First Bank." Five KB notes restate that one cite. Treat it as a reason to pull the actual CDFW boundary before you fish, not as a settled rule.

Convenient coincidence for this trip: **yellowtail is exactly the fish yo-yo iron targets**, and it is one of the two keepable species inside the closure.

---

## Current — read it first, because it gates the whole call

**Farnsworth is a standalone bank, not shoreline, and that changes the read.** Land-attached perpendicular ridges are two-directional spots that only produce on current running parallel to the shoreline. **Standalone banks — Farnsworth is the KB's named example — sit off the island with open water on every side and fish in *any* current direction**, but each one still has its own preferred directions, learned spot by spot (`6TBxHnkYXI0`; `locations/island-structure.md`, `conditions/current-structure.md`). So unlike China Point or Salta Verde, you do not pre-judge Farnsworth off the day's current vector — it is the one spot in that zone whose read does not start from the island's shoreline orientation (`locations/catalina-island-backside.md`).

**The KB does not record which directions Farnsworth itself prefers.** That is a gap you fill with your own logbook.

Within the bank, bias toward the **up-current face** — that is where nutrients are forced up and the food chain stacks (`h3PTupup17I`, `conditions/current-structure.md`).

**Current is the on/off switch for the bite.** Slack current keeps it off; the current *starting* is what starts it (`fDSd9kqwYW0`), and even a puff can fire a lee-side bite to 40 lb (`_r_qKX_7080`) (`species/yellowtail.md`).

**How to actually measure it on a bare rock bank** (`conditions/current-diagnostics.md`):

- **No kelp to read?** On hard-bottom/rock spots with no buoys and no kelp — called out specifically for yellowtail/seabass rock structure — the only way to find current direction is to **drop the anchor and watch which way the line settles**; it points the way the current runs (`sIoNELGlxmk`). That first read is often wrong; captains who know a spot reset repeatedly (one presenter resets 10–12 times a day on his skiff).
- **Chum-drift angle vs boat lay** separates true current from wind push: chum straight back off the stern = boat and water moving together; chum swinging off at an angle to the boat's lay = real current cutting across, and that angle is your direction sensor (`6TBxHnkYXI0`).
- **Do not trust the plotter's current-arrow layer** — it reads wind, not current (`BskCsKaTiZw`).
- **If there is kelp**: pulled ~20 ft under = raging, surface presentations dead, go deep/weighted — this is your yo-yo window. Laid flat = strong, fishable but hard, work the down-current side. Resurfacing = slacking, switch back to surface iron (`HnqiE05vdXs`). The ~20 ft figure is flagged single-source.

**Current also decides whether yo-yo is even the right tool.** Yo-yo is what you reach for when hard current has shut the surface down, or after **hard wind (20–25 kt+) following a run of surface days** — the fleet bite goes mostly yo-yo, the fish are still there, just no longer showing on top; surface iron still picks a fish, so it is a re-rank, not an abandonment (`ejUTAnONf7o`) (`species/yellowtail.md`, `techniques/yo-yo-iron.md`).

---

## Depth — what the meter has to tell you

**Read the bottom before you hunt fish**: thin return = sand/mud, thick return = rock, and the fish hold on rock (`6DzbsElGE7E`).

Yellowtail-specific sonar reads (`species/yellowtail.md`):

- **Structure fish mark as tight balls hugging hard bottom** — arcs and boil-ups at **~5–10 fathoms (30–60 ft) near pinnacles and high spots** (`D5DR7Kx42_A`). *Flagged*: that source carries no depth figure at all, only "tight balls of yellowtails sometimes hugging the structure" — the 5–10 fm band is the note's addition.
- **Fish balled tight to the bottom are present but not feeding** — dropper-loop water, and worth a **yo-yo burned past them for the reaction strike** (`HTowqnwAMeA`, `tpmOYXYQwhU`). Fish spread up through the column, stratified bottom-to-mid, are *hunting* — slow-troll and flyline instead.
- **Fish metered at 40–60 ft and not yet showing are staging up** — surface-iron and light-bait fish, **not yo-yo fish**; when they boil, go all-in on the surface iron (`0DKmYId1NN4`).
- **A school metered deep and not showing can still be caught at its depth** — the yo-yo is worth deploying on marked fish (`tpmOYXYQwhU`).

**Working depth band for the technique** (`techniques/yo-yo-iron.md` front matter): **60–250 ft; commonly 120–180 ft nearshore, 150–250+ ft on offshore banks and islands.** On overnight/multi-day trips yo-yo depth commonly runs **120–240 ft**.

**Jig weight by depth** (`UP_3fBu7VPA`, `VpW91AKOFVQ`, `hteLeDIy9Qs`):

| Depth | Iron |
| --- | --- |
| 60 / 80 / 100 ft | smaller jig — Salas 6X Jr class |
| 120–150 ft | Salas 6X, roughly **5–6 oz** |
| 150–250 ft | full-size 6X-class iron |
| real deep (Colonet, the ridge, Alijos, Guadalupe) | 7X-heavy iron |

For scale: a yo-yo iron runs **5–6 oz against a surface iron's 2–3 oz** (`VpW91AKOFVQ`).

**Known conflict, kept side by side — the KB does not resolve it.** `techniques/yo-yo-iron.md` sizes 6X vs 6X Jr **by depth** (table above). `species/yellowtail.md` states the same ladder twice keyed to **current** instead — "full-size (Salas 6X class, **8 oz**) in stronger current, 6X Jr (**4 oz**) when it's light" — and neither the 8 oz nor the 4 oz figure appears in the technique note. Both notes carry reciprocal fact-check flags on this. Practical read: the two rules mostly point the same way (deeper water and harder current both call for more lead), and there is a third statement that reconciles them operationally — **under-sizing costs working time, not just action**: light current and nice weather → small jig; wind or strong current → upsize, because a jig too light for the conditions spends most of its retrieve in free-spool waiting to hit bottom instead of working the zone (`HTowqnwAMeA`).

**Colour follows forage, not favouritism** (`ETw_3AFxEcM`, `UP_3fBu7VPA`, `RNRFrfepiW0`): blue-and-white on thin baitfish (anchovy, sardine); scrambled egg on invertebrates (squid, crab); mint as a third go-to with no stated mechanism; red-toned irons specifically in red-crab years.

---

## The retrieve

**Base retrieve** (`techniques/yo-yo-iron.md`):

1. **Position up-current of the mark** so the drop sweeps down onto the structure.
2. **Free-spool straight down, thumbing the spool** so it falls under light tension and tracks vertical rather than scoping away from the boat.
3. **The instant it touches, start winding — never let it sit.** The most common yo-yo error is settling into position first; a jig left on the bottom gets picked up by ocean whitefish, small cod and other bottom critters before a yellowtail finds it (`8XIy7hPsFkQ`).
4. **Tuck the rod under your arm, reel in gear, and crank back as fast as possible.** The jig cannot be cranked too fast, only too slow (`RNRFrfepiW0`). The fleeing iron's speed is the strike trigger, not a cadence.
5. **On the bite, keep cranking — do not swing to set.** The continuous full-speed wind drives the hookset itself (`5pbA-wXoric`, `ETw_3AFxEcM`, `hteLeDIy9Qs`, `SAltQjih0ms`).
6. Nothing? Drop back to the mark and rip it again.

**Cadence variants — kept side by side, not reconciled to one count:**

- **Working water (cast-and-retrieve):** free-spool to bottom, engage, **10 fast cranks**, freespool back to bottom, repeat while walking the iron toward the boat over as much as **150 yd**. Winding continuously the whole way pulls the iron out of the zone where suspended fish hold (`wzI0lpgKT1U`).
- **Straight up-and-down under the boat:** **5–6 quick cranks (~20 ft)**, then freespool back down, cycling through the marked band — e.g. working the **100–120 ft band on marks sitting at 120 ft in 120–200 ft of water**, fish suspended ~20 ft off the bottom (`wzI0lpgKT1U`).
- **Half-depth wind, then re-drop:** free-spool to bottom, crank flat-out only about halfway — in **120–150 ft, wind up 60–70 ft off the bottom** — then freespool down and repeat. Saves your arm and keeps the iron in the near-bottom band where the fish actually hold (`SAltQjih0ms`).
- **Do NOT work the iron in short hops right at the bottom** — that motion draws rockfish instead of yellowtail (`SAltQjih0ms`). At Farnsworth that matters twice over: rockfish are not on the keep list.

**The 45° option:** casting the iron out (or flipping it away from the boat) so the line sits at roughly 45° on the wind-back reads as more natural because of the diagonal retrieve path. Fish are taken both ways — a stated preference with a mechanism, not a correction to the vertical retrieve (`HTowqnwAMeA`).

**Strikes often come on the drop**, not the crank — the falling iron on freespool looks like a dying baitfish — but bites also come on the wind-up, so work the whole cycle (`wzI0lpgKT1U`, `ILBl12Jm7-0`). Keep the ready grip through the drop: **index finger on the spool, thumb on the trigger, left hand forward**, so the gear-and-crank on a bite is instant. On the drop a bite often reads as a brief stop before the fish takes off with it (`wzI0lpgKT1U`).

**Line scope** (`conditions/current-diagnostics.md`): bite feel drops off the more the line scopes off vertical, and a scoped line leaves slack to catch up on when a bite comes, costing hookups (`Vbf40qvH9-Q`). Two fixes, neither reconciled — which applies turns on whether the drift lets you reset in time: (a) cycle the presentation (drop, wind, drop) and, if it gets away toward the horizon, wind in and re-drop to reset vertical (`Vbf40qvH9-Q`); (b) when the drift is strong enough that winding in can't stop it, **flick the jig further up-swell** so it sinks as the boat drifts down onto the spot and arrives roughly vertical at the bottom (`sJGs-Jqt9Vo`).

**Two failure modes worth naming for a bank stop:**

- **Continuous jigging inside a marked school can spook and disperse it.** Some fish won't bite while it's worked that way, the motion scares fish off, and the school moves with them. Fix: let it hit bottom and bounce it there, or burn it up on a fast continuous retrieve (`6Z6Dht20kTA`, `S0-BCQWA0H4`, `SH5CZQi9ATw`).
- **A bycatch species can own the water column and mask the problem as a jig problem.** One yellowtail day planned around yo-yo and surface iron was abandoned to bonito bycatch; switching to dead sardines — not a different jig — restarted the yellowtail bite (`Ob45hK4HSWc`). At Farnsworth, where bonito is the other keepable species and the KB names it as a fall presence there, that is a live scenario.

---

## Tackle

### Class terms (`tackle/gear-classes.md`, `species/yellowtail.md`)

- **Yo-yo / heavy-iron class:** **~8 ft, XH, 40–80 lb, fast crank.**
- The yellowtail router states it as a **stout 40–60 lb class rod with a high-speed reel** to burn a heavy iron off the bottom.
- **Rod:** heavy jig-stick class with real backbone. A 10 ft stick (Phoenix Axis class) also works for casting-then-yo-yoing the same iron (cameron).
- **Reel:** high-torque conventional wound tight — a strong power grind matters more than top gear ratio, but on a boat with anglers who aren't strong crankers a **~6.6:1** reel makes it easier to take line fast enough on the wind-up (`VpW91AKOFVQ`). One concrete number behind that: a Penn Torque 40 on a 40–100 lb rod, picked for **43 in of line per handle rotation** (`7Ljt-DeFVcs`) — flagged single-source.
- **Line:** fish as heavy as you can still crank fast and control the fish — **40 lb works, 50 lb is better, 60 lb better still** (`5pbA-wXoric`, `UP_3fBu7VPA`). The "bite rate is unaffected by line diameter" mechanism is flagged as resting on `5pbA-wXoric` only.
- **Leader:** run a **short piece of mono between braid and a short fluoro leader** for stretch. Going straight from spectra to short fluoro with no buffer bends hooks and pulls fish — the mono cushion stops that specific failure (`hteLeDIy9Qs`).
- **Iron:** heavy yo-yo class — **Salas 6X / Salas CP 105 type**; Tady 4/0 and heavier CNC irons fill the same role (`lures/iron-jigs.md`).

### The attributed build that matches this stop most closely

**12–30 lb yellowtail near an island or bank in 120–180 ft** (`RNRFrfepiW0`): two-speed **Penn Fathom 30**, **65 lb braid**, a **50-yard 40–50 lb mono top shot**, an **8 ft 30–60 lb rod**, a **treble hook**, and a **Tady 4/0**.

Alternates the KB keeps side by side (`techniques/yo-yo-iron.md`):

- **Recreational base build:** two-speed conventional, **80 lb braid to a 40–60 lb mono top shot**, no fluoro, tied **straight to the iron on a San Diego jam knot** (`rigging/san-diego-jam-knot.md`), on a **7 ft rod stiffer than a flyline stick**. Run **high gear while searching** for the fastest wind-up, **low gear only once a fish is hooked** and settled (`SAltQjih0ms`).
- **A 50 lb short, stout rod** rated 40, 50 or 60 lb, paired with the mono-buffer leader above (`hteLeDIy9Qs`).
- Heavier tiers (Fathom 40 Narrow, 80 lb braid, 60 lb mono) are the **Baja upsize**, triggered by big fish, wind, or difficulty getting the jig down (`RNRFrfepiW0`) — not what a Catalina bank stop calls for unless the current is beating you.

### Against your profile (`profiles/cameron/rods.md`, `profiles/cameron/tackle.md`)

- **Trinidad 40 setup is your yo-yo rod**: M&M custom on a Rainshadow RCJB96XH — **8'0", XH, 40–80 lb, 4–10 oz** — Shimano Trinidad 40, **80 lb braid**. Its stated role is yo-yo iron and sinker rigs; note the relatively soft tip. That sits squarely inside the yo-yo/heavy-iron class and inside the 4–10 oz window the depth ladder above asks for.
- **Irons you own:** **Salas 6X** (blue) and **Salas CP 105** (silver/chrome) — both classic heavy yo-yo benchmarks. The 6X is the 120–150 ft / 150–250 ft answer.
- **Gap — name it rather than substitute:** you have **no 6X Jr or lighter yo-yo iron** in the box. If the marks come in at **60–100 ft**, or the fish are keyed on small forage (red crab, small sardines) where the doctrine is to **downsize, including to a brass-finish iron** (`WE643Fue1_A`), nothing in your inventory fishes that call the same way.
- **Gap — colour:** blue and silver/chrome only. The KB's forage-matching picks — **scrambled egg** for squid/crab, and **red-toned** for red-crab years — have no match in your yo-yo irons.
- **Gap — leader:** the mono-buffer-between-braid-and-fluoro rule wants a mono top shot; your profile records 80 lb braid on the Trinidad and no top shot. Worth confirming before the trip.
- **Open item, not doctrine:** you own a **10 ft Phoenix Axis jig stick**, always bring it to BOLA, rarely use it, and are considering yo-yoing with it — logged as an open item, not a recommendation.

---

## What the KB does not tell you about this bank

- **No spot page, so no depth.** The zone page's `depth_band` for the whole Catalina backside is `unknown` — the backside spot library carries no charted depths. Everything above is a general depth ladder you key to your own sounder.
- **No preferred current direction for Farnsworth specifically** — the KB says every standalone bank has its own, learned spot by spot, and does not record this one's.
- **Season:** the one corpus source calls Farnsworth the **fall yo-yo call** (`5p6gu14ZC4w`, 2022-10-26), but the KB flags that same source as saying the opposite half out loud — "the water temperatures still look pretty good at cats so there's no reason you couldn't catch Yellow Tail **but I don't it's not really a prime time a year to go there and catch one**." Take the yo-yo routing; don't take "fall = prime."
- **No zone guide** for yellowtail at Catalina — that row is a flagged stub, with material parked in `species/evidence/yellowtail.md`.
- **No run distance or time** from any mainland port to the backside, and no sea-state envelope for the crossing — a flagged gap on the zone page. Note also that the backside is the island's weather side.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/yo-yo-iron.md`, `techniques/evidence/yo-yo-iron.md`, `species/yellowtail.md`, `species/evidence/yellowtail.md`, `species/bonito.md`, `locations/catalina-island-backside.md`, `locations/evidence/catalina-island-backside.md`, `locations/island-structure.md`, `locations/socal-bight.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `lures/iron-jigs.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `sources/spot-lists.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `5p6gu14ZC4w`, `6TBxHnkYXI0`, `h3PTupup17I`, `HnqiE05vdXs`, `sIoNELGlxmk`, `BskCsKaTiZw`, `Vbf40qvH9-Q`, `sJGs-Jqt9Vo`, `fDSd9kqwYW0`, `_r_qKX_7080`, `ejUTAnONf7o`, `D5DR7Kx42_A`, `6DzbsElGE7E`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `0DKmYId1NN4`, `UP_3fBu7VPA`, `VpW91AKOFVQ`, `hteLeDIy9Qs`, `5pbA-wXoric`, `ETw_3AFxEcM`, `SAltQjih0ms`, `RNRFrfepiW0`, `8XIy7hPsFkQ`, `wzI0lpgKT1U`, `ILBl12Jm7-0`, `6Z6Dht20kTA`, `S0-BCQWA0H4`, `SH5CZQi9ATw`, `Ob45hK4HSWc`, `7Ljt-DeFVcs`, `WE643Fue1_A`  
*gaps admitted:* No locations/farnsworth-bank.md spot page exists — the zone page records it as never written (worklist row 'escalated'), so the KB carries no Farnsworth-specific content beyond its position, structure type and closure. | No charted depth, bottom composition, structure shape or working depth band for Farnsworth Bank — the whole Catalina backside zone page carries depth_band: unknown. | Farnsworth's own preferred current directions are not recorded; the KB only says standalone banks fish any direction but each has its own preferences learned spot by spot. | Whether Farnsworth is fished on anchor or on the drift is not stated anywhere; the anchor-line current read is general yellowtail/seabass rock-structure doctrine, not scoped to this bank. | The yo-yo jig-weight rule is unresolved in the KB: techniques/yo-yo-iron.md keys 6X vs 6X Jr to depth (5-6 oz for a 6X), species/yellowtail.md keys the same ladder to current (8 oz vs 4 oz); both notes carry reciprocal fact-check flags and neither figure appears in the other note. | The 5-10 fathom structure-fish sonar band is flagged contradicted-by-source — the cited transcript carries no depth figure at all, only 'tight balls of yellowtails hugging the structure'. | No tide, slack-water or moon-phase window is documented for Farnsworth or for Catalina-backside yellowtail; the KB's yellowtail moon-phase entry is itself a flagged gap. | The Farnsworth keep-list (yellowtail and bonito only) rests on a single 2022-10-26 report that names no agency, no boundary and no as-of date, and garbles the bank's name; the closure's actual boundary must be pulled from CDFW. | No California/CDFW bag limit or size gauge for yellowtail exists in the KB — flagged gap in the species router. | No zone guide for yellowtail at Catalina (flagged stub); material is parked unstructured in species/evidence/yellowtail.md. | No run distance, run time or sea-state envelope from any mainland port to the Catalina backside — flagged gap on the zone page. | Season shape for Farnsworth is one report, and the KB flags that the same source says late October is 'not really a prime time a year to go there'. | Cameron's profile has no 6X Jr or lighter yo-yo iron, no scrambled-egg or red-toned yo-yo iron, and no recorded mono top shot on the Trinidad 40 — the downsize, forage-colour and mono-buffer calls have no match in the inventory.

</details>

### 11. [technique] How do I slow-troll a live mackerel for yellowtail? Speed, how to rig it, and when it is the right call versus…

**Winner:** B3 · mapping {'A': 'NOW', 'B': 'B2', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** A and C both had a real slow-trolling technique note behind them and delivered the full chain — bait-graded 1.5-3 mph, nose hook, 3/0 default, ~6 ft matched fluoro, 100-150 ft setback, light drag at the lever '2' because the fish takes 50-100 yd immediately — while B's version of the KB had only scattered Baja observations, so B could give one speed number and no hook size, hook position or drag at all; B handled that absence with exemplary honesty but leaves the angler unable to finish rigging. C edges A on the decision half of the question: a six-row meter-driven table (including the bonito-interception sliding-sinker escape and the paddy/chum flyline rows), the column framing that ties all five yellowtail presentations together, hookset counts, and a drag cross-check against the quarter-to-third-of-line-class rule, plus an explicit waters/regions gate up front. A's compensating strengths are real — it resolves the technique against Cameron's profile and names the missing 8 ft glass rod, and it flags its own hook-position inference and an internal ASR disagreement C quietly resolves — so the gap is narrow. None of the three fabricated specifics, bluffed coverage, or stated a bare regulation.

- *B2 reasons:* found: said plainly its KB has no standalone slow-troll note and mined what exists (trolling.md observations, one router row) — correct handling of absence, but the core material simply is not there. specific: dense on what it has — 12 ft/28-30 ft/40 ft/50-80 ft depths, 80-100 lb, 65/80, 40 lb, 50-75 ft and 150-200 ft setbacks, ~2 lb macks — but only one speed number and no hook size, leader length or drag. sourced: every entry carries note path plus video id, with confidence and channel-registration status called out. scoped: strongest region discipline of the three — Baja-vs-SoCal labeled repeatedly, the lone SoCal datapoint correctly noted as sardine, 2015; no regulatory claims. honest: exemplary — labels its own decision frame as an assembled reading not KB doctrine, marks the idle-speed arithmetic as its own, long accurate gap list. actionable: partial — no hook size, no hook position from any slow-troll entry, no drag setting, no speed range, so the angler cannot fully rig from it.
- *B3 reasons:* found: same right chain as A plus drag-setting and rod-and-reel-selection notes, and opens by stating the technique note's waters/regions gate. specific: 1.5-3 mph bait-graded, four mackerel hook positions with the weight rule, 3/0 default and 1/0-2 downsize, ~6 ft matched fluoro halved at most, 25-40 lb, 100-150 ft, lever '2' cross-checked against quarter-to-third of line class (~10-13 lb on 40), 3-count vs wind-tight hooksets, Baja 12/28/30/40 ft and 40/60/80/100 lb brackets. sourced: note path plus video id throughout, including an independent corroboration (aD0Iim9C15o) of the any-sinker nose-hook rule. scoped: waters and five-region gate stated up front, SoCal doctrine and Baja programs in separate sections kept unreconciled; no regulations asserted. honest: flags the anthropomorphising failure mode, the low-confidence promo seminar, an incomplete attribution, keeps the secondhand downrigger datapoint out of doctrine, and admits no conditions were pulled; no relative time. actionable: the fullest execution path — rig, speed, setback, drag, hookset, fight, and a six-row meter-driven troll-vs-flyline table including the bonito sliding-sinker escape.
- *NOW reasons:* found: pulled the dedicated technique note plus the yellowtail router, flyline, trolling, bait and hook notes — exactly the right chain. specific: 1.5-3 mph bait-graded band, 3/0 default with 1/0-2 downsize, ~6 ft matched fluoro, 25-40 lb main, 100-150 ft setback, lever-drag '2', 50-100 yd first run, Baja 40/65-80/80-100 lb brackets, 15 in and ~2 lb macks. sourced: note paths plus video ids on essentially every parameter (HTowqnwAMeA, 9tIp4n7q850, w5_x6kkN-xE, QSmE3mdEL28). scoped: SoCal local-coast numbers explicitly separated from Baja shallow-rock line classes with a stated decision frame; no regulatory claims made. honest: flags its own hook-position inference, an internal 10/30/50 vs 1/0-5/0 ASR disagreement, an unsupported cite in the router, the unreconciled 1 mph seminar figure, and that no conditions were pulled; no relative time. actionable: an angler can rig, set drag, set the bait back and pick troll vs flyline off the meter; profile check names the missing 8 ft glass rod rather than papering over it.

<details><summary>Full prompt</summary>

How do I slow-troll a live mackerel for yellowtail? Speed, how to rig it, and when it is the right call versus flylining.

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Slow-trolling a live mackerel for yellowtail

**Read this first — what the KB actually has.** There is no standalone "slow-trolling live bait" technique note in this knowledgebase (`techniques/README.md` lists 21 techniques; a live-bait slow-troll is not one of them). The material lives as **observed, location-specific entries inside `techniques/trolling.md`**, plus one router row in `species/yellowtail.md`. Almost all of it is **Baja** — Cedros Island, La Paz, Ensenada — logged from an unregistered channel at **medium confidence**. SoCal has exactly **one** data point. So: the parameters below are real and specific, but they are one or two crews' choices, not repeated doctrine.

---

## 1. Speed

- **~3 mph** — the only trolling speed the corpus gives for this technique. Called out on camera as "putt putt putt" on a Cedros morning slow-troll on live mackerel (`techniques/trolling.md`, `9tIp4n7q850`). That's roughly 2.6 kt.
- Everything else is described only as "slow-trolling," with no number (`techniques/trolling.md`, `QSmE3mdEL28`, `ORC1A68cEeM`, `92y14x33etQ`, `0dIwWiOc1NY`).
- Practical note for your panga: it **idles ~1.5 kt** (`profiles/cameron/boat.md`), so ~3 mph is above idle — you'd be bumping in and out of gear or trimmed just off idle. The KB does not cover throttle/gear technique, turning, or how to hold that speed; that's my arithmetic on your idle speed, not a KB claim.

## 2. Rigging it

**The bait.**
- Mackerel is the right bait class and the KB is emphatic about size. Yellowtail have been seen eating mackerel **up to 1.5 lb**, sometimes **five or six fish attacking one mackerel** at once, and fishing live mackerel rather than sardine/anchovy at **San Clemente, Catalina or the Coronados skews the catch toward yellowtail specifically**, screening out calico, barracuda and bonito bycatch (`bait/fishing-live-bait.md`, `w5_x6kkN-xE` — Dave Hansen, registered voice, high confidence).
- The Cedros crew that landed a **45 lb personal best** on a slow-trolled mackerel spent **parts of two days** catching bait specifically: **big, fat, roughly 2 lb mackerel**. Hooked bait macks kept getting eaten by seals at the surface, worked around by **fishing the bait deeper rather than at the top** (`techniques/trolling.md`, `Zo92MG459gQ`).
- Side by side, unreconciled: one registered voice states his species-bait pairing as **sardine for yellowtail**, mackerel for striped marlin (`techniques/flyline.md`, `gKrYKvqHUjk`). And the single SoCal slow-troll observation ran **sardine**, not mackerel (below).
- Bait quality rules carry over: **~90% of live-bait success is bait selection** — fish the lime-green, scales-intact bait that's hardest to catch in the tank; **60-second rule**, if it isn't pulling line off the reel shortly after it hits the water, wind it in and grab a fresh one (`bait/fishing-live-bait.md`, `SluBXkT3cuw`, `8YvmROeVL-0`).
- Making your own: your program is **Coronado Islands sabiki, ~100 ft, 8 oz sinker**, and you've loaded **5 twelve-inch mackerel on one drop** — twelve-inch macks are exactly the hearty, big-bait end this technique wants (`bait/making-bait.md`, cameron).

**The hook.**
- **Circle hook** in every observed slow-troll: Cedros (`QSmE3mdEL28`), Cedros day two — visually confirmed circle (`I-QBxuV2p7M`), La Paz (`ORC1A68cEeM`), and the 45 lb Cedros fish, on a circle called "a number 3" (brand ASR-garbled, not carried) (`Zo92MG459gQ`) — all in `techniques/trolling.md`.
- **Conflict, kept side by side:** `tackle/hooks.md` (`sWRSYCmt4Tw`, `m2q22sPPkEM`) names **J hooks as the pick for islands yellowtail** and circles as the offshore live-bait default. Every observed slow-troll used circles. The KB never reconciles these for this specific application — your call turns on whether you want to set or let the fish load the hook.
- **Hook position is never stated in any of the slow-troll entries.** What the KB gives you is the general rule: the **nose hook** — the clear spot in front of the eyes, one nostril to the other — is the position that "can be slow-trolled," swims naturally and stays up (`bait/fishing-live-bait.md`, `T3p1mrqNjIo`, `mscHk0qiXnk`; same in `techniques/flyline.md`).
- Mackerel-specific hard rule worth knowing: **butt hook is for zero-weight flylining only**; the moment any weight goes on, switch to the nose hook, because a butt-hooked mack under a sinker gets **dragged backward** and doesn't read as a feeding fish (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`). One caution that bears on a towed bait: any tension on a **nose-hooked** bait drags its head back toward the boat (`techniques/flyline.md`, `48ZFXnCTTQE`, Cesar, medium confidence) — the KB does not resolve how that interacts with a deliberate troll.
- Circle-hook baiting mechanic: **hold the hook high on the arch and press straight down** into the bait; holding from the bottom leaves no gap and mangles it (`techniques/flyline.md`).

**Line and leader — three brackets, kept side by side, not reconciled** (`techniques/trolling.md`, `tackle/line-and-leader.md`):

| Program | Line | Source |
| --- | --- | --- |
| Cedros home-guard, 28–30 ft rock | **80–100 lb line class** as standing gear | `QSmE3mdEL28` |
| Cedros day two, same spot, ~30 ft | **65 lb braid → 80 lb fluorocarbon leader** ("big fish could care less what size line you're using") | `I-QBxuV2p7M` |
| Cedros, different trip/year | **40 lb fluorocarbon top shot** | `9tIp4n7q850` |
| Cedros, 45 lb fish | **straight 80 lb** ("straight 80 on 80"); some in the group recommend stepping to **100 lb** | `Zo92MG459gQ` |
| La Paz shallow rock, 12 ft | **40 lb** | `ORC1A68cEeM` |
| La Paz "El Bajo" bank, dropped-bait variant | **65 lb braid → 60 lb fluorocarbon** top shot | `92y14x33etQ` |

For context, `tackle/line-and-leader.md` logs a Cedros **line-class floor of 40 lb, with 50 lb covering most everything** (`WE643Fue1_A`) — the 80–100 lb bracket above is a different operator's independent choice for the same risk (a 30 lb-plus fish putting you in shallow rock), not a correction of it.

**Setback — pick by what you're fishing over:**
- **"Not too far" back** over the structure, over 40 ft of water (`QSmE3mdEL28`).
- **50 to 75 ft** back off the stern, flylined, at ~3 mph (`9tIp4n7q850`).
- **150 to 200 ft** back — the one SoCal data point: a **nose-hooked live sardine** slow-trolled that far behind the boat produced yellowtail in "the channel," on a mix of circle and wide-gap hooks (`techniques/flyline.md`, `ROWgdFE9Ehc`, 2015-10-28).
- **Bank/high-spot variant (dropped bait):** let out roughly **10 yards** of line, then drop the weight **straight to the bottom** — don't stop halfway. Once it touches down, the ongoing troll speed lifts the bait back off the bottom on its own, presenting it "out the back in the high column zone" rather than dragging bottom. Produced multiple yellowtail on El Bajo, a bank whose shallowest point is **~50 ft on low tide, no more than 80 ft on high** (`techniques/trolling.md`, `92y14x33etQ`).

## 3. Where you put it

This is a **standing program over known structure, not a locate method** (`species/yellowtail.md` router row). Observed depths:

- **12 ft** of water, working close to visible rock — hooked fish repeatedly ran back toward the rocks, one went "in the grass" (La Paz, `ORC1A68cEeM`).
- **28 ft** crest called the day's "perfect" biting depth, fish also worked to **30 ft**; a third stop that trip was over **40 ft** (Cedros, `QSmE3mdEL28`).
- **50–80 ft** bank high spot, dropped-bait variant (La Paz, `92y14x33etQ`).

Structure rule that gates all of it: yellowtail sit **exclusively on hard/rocky bottom, never mud** — read bottom hardness (thin return = sand/mud, thick = rock) before you bother working a spot (`species/yellowtail.md`, `6DzbsElGE7E`). The classic yellowtail sonar read is **tight balls hugging structure, arcs/boil-ups at ~5–10 fathoms** (`species/yellowtail.md`, `D5DR7Kx42_A`).

**Combine it with cast jigs.** At an Ensenada reef/point, the crew slow-trolled a couple of live mackerel from the stern **while simultaneously casting jigs from the bow** at the same structure — stated logic being that the surface splashes draw fish into the area alongside the trolled bait rather than competing with it. Target was described as constantly moving around the structure rather than holding (`techniques/trolling.md`, `0dIwWiOc1NY`).

## 4. The bite, the hookset, the fight

- **Test drags before you start.** Called out as the standard first step of this style of fishing: "this style of fishing always ask the captain to test your drags, numero uno" (`techniques/trolling.md`, `ORC1A68cEeM`).
- **Hookset — two variants, kept side by side:**
  - **No strike.** Let the rod load and **wind tight** rather than swinging — the standing circle-hook doctrine (`techniques/trolling.md`, `QSmE3mdEL28`; `tackle/hooks.md`: engage the reel, point the rod where the fish is going, wind tight, and it pins the corner of the mouth).
  - **A counted 3-second pause** ("1, 2, 3") before putting the reel in gear (`techniques/trolling.md`, `ORC1A68cEeM`). Note `tackle/hooks.md` logs a **10 count for circle hooks** and a **3 count for small J hooks** (`48ZFXnCTTQE`, `mL4Ph7t0WcQ`) — the La Paz crew ran a 3-count on circles. Unreconciled; pick one and be consistent.
- **Back the boat down** once a big one takes off — called out on camera as an important, deliberate move, compared to backing down on big bluefin (`techniques/trolling.md`, `QSmE3mdEL28`).
- **"Railing" it.** When a big fish couldn't be lifted conventionally out of shallow structure, the crew worked it up and over the gunnel with the rod rather than continuing a standard fight (same source).
- **Don't add drag mid-fight** — "a couple more clicks" mid-fight is called "always the wrong thing to do" (`species/yellowtail.md`, `Zo92MG459gQ`).
- **Expect losses in the shallows.** The La Paz crew's own closing assessment: "you win some and you lose more when you're fishing shallow water yellowtail" — tied specifically to shallow, rock-adjacent structure (`techniques/trolling.md`, `ORC1A68cEeM`).
- **Species calls are unreliable by feel** — the Cedros bite ran mixed with bonita and the crew repeatedly couldn't call the fish until it was boatside (`species/yellowtail.md`, `9tIp4n7q850`).

## 5. When it's the right call — versus flylining

The KB contains **no explicit head-to-head comparison** of these two for yellowtail. The frame below is assembled from what each entry says about itself; treat it as a reading, not KB doctrine.

**Slow-troll when:**
- **You're on known resident/home-guard structure and the fish are moving around it, not holding.** This is the router's own framing: "resident/home-guard fish over known shallow structure … not a locate method — a standing program over a known rock" (`species/yellowtail.md`). Ensenada made the same read: yellowtail "constantly moving around the structure rather than holding" (`techniques/trolling.md`, `0dIwWiOc1NY`).
- **It's windy or choppy.** The strongest single argument in the corpus: the Cedros program kept running through building wind and whitecaps — "the good news is we're just slow-trolling… I don't think the fish care" — **because it doesn't depend on a clean cast the way iron does** (`techniques/trolling.md`, `QSmE3mdEL28`). Your boat has **no trim tabs** and a hull that springs on hard impacts (`profiles/cameron/boat.md`), so wind days are exactly where this earns its place.
- **You want to keep baits working while covering a piece of structure repeatedly**, with no chum line and no anchored presentation set up.
- **You want to screen out bycatch** — a big live mackerel skews the catch toward yellowtail over calico/barracuda/bonito (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`).

**Flyline instead when:**
- **Bait is in the water and fish are on the chum or the bait line**, or working a paddy — that's the flyline note's own "reach for this when" (`techniques/flyline.md`).
- **Fish are boiling or breezing on the surface, or on a kelp paddy** — the router ranks **surface iron first, flylined bait second** there, not trolling (`species/yellowtail.md`).
- **Fish are visible but not biting** (picky/finicky) — the router's answer is flylined bait, **downsize leader and hook, and wait for the bite window** (`species/yellowtail.md`). Nothing in the KB suggests trolling a picky bite.
- **You're anchored or holding on one mark** — a flyline lets the bait swim naturally with zero weight, the most natural presentation in the box (`techniques/flyline.md`).
- Worked example of the two on the same trip: day one at La Paz was windy with strong current and slow fishing on the shallow slow-troll (`ORC1A68cEeM`); day two moved to a calmer shared high spot and **flylined live mackerel**, producing multiple yellowtail plus cabrilla, dorado and pargo (`techniques/flyline.md`, `qM7iOO7fOBw`).

**Timing beats technique choice.** The Ensenada crew ran the slow-troll for a couple of hours and got no yellowtail, and blamed the clock, not the method: **yellowtail feed hardest during gray light early in the morning**, and this stop was fished after that window, with the tide "off" (`species/yellowtail.md`, `0dIwWiOc1NY`). And day two at Cedros ran the same slow-troll, at the same spot, on heavier gear, and got **zero yellowtail bites** all day (`techniques/trolling.md`, `I-QBxuV2p7M`) — day-to-day variability the crew itself calls out.

**Don't treat it as either/or.** `species/yellowtail.md` is explicit: the three faces of yellowtail are **states, not fish types**, no situation locks you to a single presentation, and Cameron's own three-outfits doctrine is to rig the surface-iron, heavy yo-yo/dropper and flyline outfits **simultaneously** and switch as temp and bait depth change. Ensenada ran troll and cast jigs at the same time on purpose.

## 6. Your gear (from your profile)

- **Rods:** the **Talica 25** setup (Phenix Axis 8'0" 3X-H, 60–130 lb rail class, Talica 25II 2-speed, **100 lb braid**) is your commonly-trolled heavy setup and matches the **80–100 lb Cedros bracket**. The **Trinidad 40** (8'0" XH 40–80, **80 lb braid**, "some trolling") sits right on the straight-80 program. If you want the 40–65 lb brackets, the **Avet** setup (Teramar 90MHB2, MXJ, 50 lb braid) is your flyline rod — but note it's classed as a flyline rod, not a troller. **Never the Lexa 400** (`profiles/cameron/rods.md`, `profiles/cameron/boat.md`).
- **Boat:** 10 holders / 6 vertical; trolling set is two gunnel holders per side at 15° plus an elevated shotgun at 5°; you normally run **2–3 lures**. The Ensenada crew ran "a couple of live mackerel from the stern" — the KB gives no spread geometry for live baits, so the gunnel pair is the obvious start (`profiles/cameron/boat.md`, `techniques/trolling.md`).
- **Bait:** 30 gal tank, Rule 401 500 GPH — dialed, bait normally survives well (`profiles/cameron/boat.md`).

## 7. What this KB does not cover — don't fill these from anywhere else

- No standalone slow-troll technique note; no speed **range** (one number, ~3 mph); no throttle/gear/turning guidance.
- No stated **hook position** for a slow-trolled mackerel in any of the source entries.
- No hook size/model, leader length, or terminal connection (swivel vs. straight tie) for this rig.
- No SoCal doctrine at all — one SoCal observation, on sardine, from 2015.
- No guidance on how many baits to pull, setback stagger, or tangle management for live baits.
- No coverage of bait survivability at troll speed or how often to swap a trolled bait.
- No trolling drag settings.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `species/yellowtail.md`, `techniques/trolling.md`, `techniques/flyline.md`, `techniques/README.md`, `bait/fishing-live-bait.md`, `bait/making-bait.md`, `tackle/hooks.md`, `tackle/line-and-leader.md`, `tackle/gear-classes.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`  
*videos:* `QSmE3mdEL28`, `I-QBxuV2p7M`, `9tIp4n7q850`, `Zo92MG459gQ`, `ORC1A68cEeM`, `92y14x33etQ`, `0dIwWiOc1NY`, `qM7iOO7fOBw`, `ROWgdFE9Ehc`, `T3p1mrqNjIo`, `mscHk0qiXnk`, `w5_x6kkN-xE`, `48ZFXnCTTQE`, `gKrYKvqHUjk`, `SluBXkT3cuw`, `8YvmROeVL-0`, `sWRSYCmt4Tw`, `m2q22sPPkEM`, `mL4Ph7t0WcQ`, `D5DR7Kx42_A`, `6DzbsElGE7E`, `WE643Fue1_A`  
*gaps admitted:* No standalone slow-trolling-live-bait technique note exists — the knowledge lives only as observed, location-specific entries inside techniques/trolling.md plus one router row in species/yellowtail.md. | Only one trolling speed for this technique appears anywhere in the corpus (~3 mph, 9tIp4n7q850); no speed range, RPM, throttle/gear technique, or turning guidance. | Hook position for a slow-trolled mackerel is never stated in any of the slow-troll source entries — only the general nose-hook table row says a nose-hooked bait 'can be slow-trolled'. | No hook size or model, leader length, or terminal connection (swivel vs straight tie) is specified for the slow-troll rig; the one hook reference ('a number 3' circle) is ASR-garbled. | Essentially all sourced slow-troll-for-yellowtail material is Baja (Cedros, La Paz, Ensenada) at medium confidence from an unregistered channel; SoCal has exactly one observation (ROWgdFE9Ehc, 2015, on sardine) and no SoCal doctrine — Coronados/Catalina/San Clemente slow-troll programs are not covered. | No explicit head-to-head comparison of slow-trolling versus flylining for yellowtail exists in the KB; the decision frame given is assembled from what each individual entry states about itself. | Number of baits to pull, setback stagger, holder geometry and tangle management for a live-bait troll spread are not covered. | Bait survivability at troll speed and how often to change a trolled live bait are not covered. | Trolling drag settings / strike drag numbers for this technique are not covered. | Circle vs J for this specific application is unreconciled: tackle/hooks.md names J hooks for island yellowtail while every observed slow-troll ran circle hooks.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Slow-trolling a live mackerel for yellowtail

You didn't give me conditions or a launch point, so this is the technique answer, not a day plan — I haven't pulled or assumed any SST, wind, or tide. Note the gate before you use it: `techniques/slow-trolling-bait.md` is scoped `waters: [nearshore-coast, island, bank]` — it is not a bay/harbor or open-ocean method in this KB, and it applies across all five regions (SoCal Bight through both Cortez regions).

One framing thing up front, because it changes how you read everything below: **slow-trolling and flylining are the same bait on the same outfit — the only thing that changes is what the boat is doing** (`techniques/slow-trolling-bait.md`). You are not re-rigging to switch.

---

## 1. Rigging the bait

**Hook position — nose hook is the one that slow-trolls.**

- **Nose**, through the clear cartilage spot right in front of the eyes (one nostril to the other). The bait swims naturally and stays up, and this is the position explicitly listed as slow-trollable as well as flylineable (`bait/fishing-live-bait.md`, `SluBXkT3cuw`, `mscHk0qiXnk`, `T3p1mrqNjIo`; `techniques/flyline.md` calls it "the all-purpose flyline hook: the bait swims naturally, stays up, and can also be slow-trolled").
- **Do not butt-hook a slow-troll bait if there's any weight involved.** On mackerel specifically, the doctrine is a hard rule — only two positions get used day to day: **butt hook for flylining with zero weight only**, and **nose hook the moment any weight goes on** (dropper loop, sliding sinker, rubber core). A butt-hooked mackerel under a sinker gets dragged backwards, and a mackerel swimming backwards doesn't read as a feeding-fish silhouette (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`, Dave Hansen — high confidence). The same "any sinker at all → nose hook, across the bridge of the nose" rule is stated independently by Steve Carson, from half an ounce up through 16 oz (`bait/fishing-live-bait.md`, `aD0Iim9C15o`).
- **Shoulder / dorsal** is the other mackerel-relevant position — called out as "mackerel especially" — and it holds the bait **high, skating across the top**, with your **line up out of the water** (`techniques/flyline.md`, `bait/fishing-live-bait.md`, `mscHk0qiXnk`). Worth knowing, but the notes attach it to flylined/offshore stealth presentations, not to the boat-speed slow-troll.
- **Back / dorsal hook is kite-only** in the mackerel doctrine — right in front of the dorsal, a hard spot that holds well, reserved for a live mackerel off a kite (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`).

**Hook style and size.**

- SoCal local-coast doctrine: **a J hook in the 3/0 range is the working default**, with **1/0, 1, and 2** carried for two specific cases — small bait, and finicky fish. Downsizing is a **paired** move: drop line class *and* hook size together, not one or the other (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`, Nate Winnicki / BDOutdoors). A full-grown mackerel sits at the big end of that: the note's own speed rule brackets mackerel as "any bait big enough for a **3/0–5/0** hook."
- J vs circle is region- and source-split, and the KB keeps it that way. For islands yellowtail the corpus pick is a **J hook** (`tackle/hooks.md`), and a Cortez Bank captain's stated split was **J hooks for yellowtail, circle hooks for bluefin** (`species/yellowtail.md`, `nsUdT-zXI8s`-family Cortez entry). Every documented **Cedros and La Paz** slow-troll ran **circle hooks** (`techniques/trolling.md`, `QSmE3mdEL28`, `I-QBxuV2p7M`, `Zo92MG459gQ`, `ORC1A68cEeM`). That's two working traditions, not a resolved question.
- Cedros bait-size-matched hook lineup: **Owner ringed offshore hooks in sizes 10, 30, and 50** carried so the angler could match hook to whatever the bait dock had that day, up to **15-inch mackerel** (`techniques/slow-trolling-bait.md`, `tackle/hooks.md`, `_C7TJoGT0nw`). A re-cut of the same clip renders those as "1.0, 3.0, 5.0" and the KB reads both as the **1/0, 3/0, 5/0** progression (`qHS-ewTQs9Q`).

**Line and leader — SoCal local coast (`HTowqnwAMeA`, `techniques/slow-trolling-bait.md`):**

- **25–40 lb** mainline for local yellowtail, and **always carry a lighter option, 20–25 lb**, even on a day that starts on 40. A full day of bites on 40 lb is described as luck, not the norm. *"You'd be really surprised how hard you can pull on 25 lb"* — provided the drag is set for it.
- **Short fluoro at the hook, ~6 ft, sized to the mainline** — 30 lb main gets 30 lb fluoro. **At most halve it** for finicky fish (30 → 25 lb). Explicit warning: do not go much lighter. The payoff is abrasion resistance right at the hook, where you otherwise get bitten off or rubbed off on rock.
- Full setup as described: **8 ft fiberglass or composite rod, size-25 reel, 50 lb braid to a 30–40 lb mono top shot**, then the short fluoro (`tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`).

---

## 2. Speed — 1.5 to 3 mph, and the bait picks the number

The range is wide on purpose (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`):

- **Small-grade sardine** (size 1 or 2 hook bait) — go **as slow as you possibly can**; a small bait can't swim against much.
- **Mackerel, or any bait big enough for a 3/0–5/0 hook** — you can pull it **faster** within that range. That's your case.

**The governing test is not the speedometer — the bait must look natural, and the failure mode is a bait that reads as being dragged by a machine.** Set speed by watching the bait; use 1.5–3 mph as the sanity check.

Corroborating numbers from other trips, kept separate rather than merged: a Cedros live-mackerel slow-troll called **roughly 3 mph** on camera ("putt putt putt") (`techniques/trolling.md`, `9tIp4n7q850`), and at the other end, **~1 mph** given for slow-trolling live *sardines* in a promotional seminar the KB flags at low confidence (`species/yellowtail.md`, `5Oh3IPIC5g4`). Mackerel at ~3 mph and sardine at ~1 mph is exactly the bait-picks-the-speed rule playing out.

---

## 3. Setback

- **SoCal doctrine: 100–150 ft.** Explicitly *not* far — a long setback is not the goal. Past ~150 ft you lose the hook-setting benefit of boat motion and gain nothing (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`).
- Cedros mackerel program: **50–75 ft back off the stern** on a 40 lb fluorocarbon top shot (`techniques/trolling.md`, `9tIp4n7q850`); the `QSmE3mdEL28` crew put the mackerel "**not too far**" back over 40 ft of water.
- The one longer number in the corpus is a *sardine* observation, not mackerel: nose-hooked sardine slow-trolled **150 to 200 ft** back produced yellowtail (`techniques/flyline.md`, `ROWgdFE9Ehc`).

---

## 4. Drag, and letting the boat set the hook

This is the part people get wrong (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`):

- **Fish a light drag and let the boat drive the hook.** On a lever drag, around the **"2"** mark — enough that forward boat motion seats the hook the instant the fish eats, not so much that it snaps you off or overruns the reel. Whether you fish in gear at all is presented as angler preference; the light-drag setting is the specific recommendation.
- **Why it can't be pinned:** a yellowtail eating a slow-trolled bait takes **50–100 yards immediately**, more if it's any size. A locked drag at that moment either breaks the line or backlashes the reel.
- Cross-check that "2" against the general rule: set strike drag to **a quarter to a third of your lowest line-class rating**, starting on the light end — on 40 lb that's **~10–13 lb** (`tackle/drag-setting.md`, `VpW91AKOFVQ`, high confidence). On 25–30 lb main it's proportionally lighter.
- **Don't swing.** On a circle hook, no strike — let the rod load and wind tight (`techniques/trolling.md`, `QSmE3mdEL28`; `tackle/hooks.md`). A La Paz crew counted it out explicitly: **give the fish a 3-second count ("1, 2, 3") before putting the reel in gear** (`techniques/trolling.md`, `ORC1A68cEeM`), kept side by side with the Cedros phrasing rather than merged. For newer anglers on a J hook, the guidance is a **solid three count, then raise the rod to about 45° and wind tight** — still no bass-style swing (`tackle/hooks.md`, `R48YdVFfEOI`).
- Mid-fight: **backing the boat down** on a hooked fish is called out as a deliberate, important move once a big yellowtail takes off — compared on camera to backing down on big bluefin (`techniques/trolling.md`, `QSmE3mdEL28`). Same source: **adding drag mid-fight** ("a couple more clicks") is called "always the wrong thing to do" (`species/yellowtail.md`, `Zo92MG459gQ`).

---

## 5. When it's the right call vs. flylining

The clean discriminator in this KB is **what the meter shows**, not the calendar (`species/yellowtail.md`, "Finding them"; `HTowqnwAMeA`):

| What you're looking at | Call |
| --- | --- |
| **Stratified column** — marks running as lines from the bottom up through mid-column, sometimes to the surface | **Fish are actively hunting bait → put slow-trolled baits out.** This is the stated trigger. |
| **Ball stuck to the bottom** | Fish present but *not* hunting → **dropper loop** water, not flyline and not slow-troll |
| Fish **up in the column and spread out** over a small rock (~20–30 ft across) | They'll eat; tucked tight to the bottom, they won't (`HTowqnwAMeA`, second angler, attribution incomplete — medium) |
| Fish **visible on the surface but not biting** (picky/finicky) | **Flyline**, downsize leader and hook, wait for the tide/current window (`species/yellowtail.md` situations table) |
| Bait in the water, fish **on the chum or the bait line**, or working a paddy | **Flyline** (`techniques/flyline.md`, "Reach for this when") |
| **Bonito intercepting** your flylined baits before they reach the yellowtail | Neither — go to a **sliding sinker**, 2–4 oz egg to a 2/0–4/0 J, to get under the bonito layer (`species/yellowtail.md`, `yGXSrUauo2w`) |

Four more decision inputs the notes give:

1. **Cover water instead of committing to an anchor.** The strongest attributed decision in the corpus: a crew was told the spot was anchor fishing, anchored, fished it **an hour to an hour and a half for a couple of bites**, pulled the anchor, started moving around the zone slow-trolling — and their **bite rate roughly quadrupled**. Stated lesson: *"You can't really be glued to a certain technique or style of fishing"* (`species/yellowtail.md` → Doctrine & conflicts, `HTowqnwAMeA`).
2. **Calibrate before you decide it isn't working.** On the SoCal local coast a **good day is three or four bites**; a 12–15 bite day was called an anomaly on camera. At that rate, two fishless hours is *not* evidence the technique is wrong (`species/yellowtail.md`, `HTowqnwAMeA`). That's a local-coast expectation, not a Baja or island one.
3. **Wind.** Slow-trolling keeps running through building wind and whitecaps — *"the good news is we're just slow-trolling... I don't think the fish care"* — because it doesn't depend on a clean cast the way iron does (`techniques/trolling.md`, `QSmE3mdEL28`). Separately, on the SoCal side, hard wind (20–25 kt+) after good surface days re-ranks the day toward **yo-yo iron** (`species/yellowtail.md`, `ejUTAnONf7o`).
4. **Fatigue / bycatch.** At Cedros the stated reason to switch to slow-trolled mackerel was simply that arms hurt after several yellowtail on iron (`techniques/slow-trolling-bait.md`, `_C7TJoGT0nw`). And **fishing live mackerel rather than sardine or anchovy skews the catch toward yellowtail specifically**, screening out calico, barracuda, and bonito bycatch a smaller bait draws — reach for mackerel when straight yellowtail is the goal (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`). Yellowtail have been seen eating mackerel **up to 1.5 lb**, sometimes five or six fish on one mackerel at once.

The column framing that ties it together (`species/yellowtail.md`, `HTowqnwAMeA`): **flyline and slow-trolled bait up top** because that's how the fish feed when they're feeding; **trolled hard baits mid-column as a search tool**; **surface iron** on top; **yo-yo iron** for the mid-to-lower band; **dropper loop** on the bottom for inactive fish. Explicitly stated as not interchangeable.

---

## 6. If you're doing this in Baja, the numbers change

The Cedros/La Paz programs are a different bracket and the KB keeps them unreconciled with the SoCal doctrine above:

- **Cedros home-guard, shallow structure:** rock cresting at **28 ft** called the day's "perfect" biting depth, fish worked to **30 ft**, a stop over **40 ft** of water; crew stepped up to an **80–100 lb line class**, live mackerel on a **circle hook**, and **railed** big fish over the gunnel when they couldn't be lifted conventionally in the shallow structure (`species/yellowtail.md`, `techniques/trolling.md`, `QSmE3mdEL28`). Day two at the same spot on **65 lb braid to 80 lb fluoro** over 30 ft produced **zero yellowtail bites** — kept side by side as day-to-day variability, not a gear verdict (`I-QBxuV2p7M`).
- **A separate Cedros trip** ran the far lighter **40 lb fluorocarbon top shot** at ~3 mph, 50–75 ft back (`9tIp4n7q850`); another angler credited a **45 lb personal best** to **straight 80 lb**, with some of the group recommending stepping to 100 lb (`Zo92MG459gQ`). Same source note also has the practical bait problem: seals picking off hooked bait mackerel at the surface, worked around by **fishing the bait deeper**.
- **La Paz, Sea of Cortez side:** trolled in water called out as just **12 ft** deep tight to visible rock, **40 lb** line, circle hooks, every angler drag-tested before starting; doubles close to **30 lb** (`techniques/trolling.md`, `ORC1A68cEeM`). At the "El Bajo" high spot (50 ft on low tide, no more than 80 on high) the variant was: let out roughly **10 yards**, drop the weight straight to the bottom, and let the troll speed lift the bait back into the high column on its own — **65 lb braid to 60 lb fluoro** (`92y14x33etQ`).
- **Ensenada reef/point:** slow-trolled a couple of live mackerel from the stern **while simultaneously casting jigs from the bow** — stated logic being that surface splashes from the cast jigs pull fish into the area alongside the trolled bait (`techniques/trolling.md`, `0dIwWiOc1NY`). That stop ran a couple of hours with no yellowtail.

---

## 7. The named failure modes

From `techniques/slow-trolling-bait.md` (`HTowqnwAMeA`):

- **Pinning the drag** — costs the fish on the first 50–100 yard run.
- **Setting the bait too far back** — past ~150 ft you lose the boat's hook-set and gain nothing.
- **Over-dropping the fluoro** — halving the mainline class is the floor, not a starting point.
- **Running one speed all day** — speed is a function of what bait is in the tank and changes when the bait does.
- **Treating educated fish as naive** — the source's view (flagged in the note as possibly anthropomorphising, recorded as his stated view rather than established fish behaviour) is that local-coast fish north of the border have seen a great many slow-trolled baits.

---

## What the KB doesn't cover here

I'd rather flag these than fill them in:

- **No stated in-gear vs. free-spool rule.** Whether you fish in gear at all is left as angler preference; only the light-drag number is given.
- **No SoCal-side circle-vs-J verdict for a slow-trolled mackerel** — the circle-hook slow-troll doctrine is entirely Baja (Cedros/La Paz), the J-hook pick is the islands/Cortez Bank recommendation, and no note tests them against each other.
- **No spread layout or bait count.** The only number anywhere is "a couple of live mackerel from the stern" at Ensenada. Nothing on how many rods, short vs. long, or holder geometry for this technique.
- **No bridling doctrine for this application.** `bait/fishing-live-bait.md` covers bridling big mackerel but flags it as general big-bait practice for tuna/marlin, explicitly not from the SoCal clips.
- **No temperature or seasonal threshold** for choosing slow-troll over flyline — the KB's discriminator is the sounder picture and boat behaviour, not a calendar or SST number.
- **Downriggers are effectively uncovered** — one secondhand, unconfirmed Cedros data point (2 lb max weights, 30 ft of water, two big fish hooked and neither landed), explicitly kept out of doctrine.
- **No documented head-to-head** of slow-troll vs. flyline on the same fish; the anchored-to-moving bite-rate quadrupling is the closest thing and it's a single session.
- **No mackerel-size-to-speed table** beyond "big enough for a 3/0–5/0 hook → you can pull it faster."
- I pulled **no conditions** — no SST, chlorophyll, wind, swell, tide or moon — because none were given. If you tell me the date, launch point and boat range, I can run the actual day-plan protocol against this.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/slow-trolling-bait.md`, `techniques/flyline.md`, `techniques/trolling.md`, `species/yellowtail.md`, `bait/fishing-live-bait.md`, `tackle/hooks.md`, `tackle/drag-setting.md`, `tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`  
*videos:* `HTowqnwAMeA`, `_C7TJoGT0nw`, `qHS-ewTQs9Q`, `QSmE3mdEL28`, `I-QBxuV2p7M`, `9tIp4n7q850`, `Zo92MG459gQ`, `ORC1A68cEeM`, `92y14x33etQ`, `0dIwWiOc1NY`, `w5_x6kkN-xE`, `SluBXkT3cuw`, `mscHk0qiXnk`, `T3p1mrqNjIo`, `aD0Iim9C15o`, `ROWgdFE9Ehc`, `VpW91AKOFVQ`, `R48YdVFfEOI`, `yGXSrUauo2w`, `ejUTAnONf7o`, `5Oh3IPIC5g4`, `nsUdT-zXI8s`, `8YvmROeVL-0`, `NXvqLUZ6qp8`  
*gaps admitted:* No stated rule for fishing in gear vs. free-spool on a slow-troll — the KB leaves it as angler preference and only specifies the light drag setting. | No SoCal-side circle-hook vs. J-hook verdict for slow-trolled mackerel; the circle-hook slow-troll doctrine in the KB is entirely Baja (Cedros/La Paz) and the J-hook recommendation comes from islands/Cortez Bank sources, with no head-to-head. | No spread layout or bait count for slow-trolling — the only figure anywhere is 'a couple of live mackerel from the stern' at Ensenada; nothing on rod count, short/long positioning, or holder geometry. | No bridling doctrine for a slow-trolled mackerel — the bridle entry is flagged as general big-bait (tuna/marlin) practice, explicitly not from the SoCal source clips. | No water-temperature or seasonal threshold for choosing slow-troll over flyline; the KB's discriminator is the sounder picture and boat behaviour, not SST or calendar. | Downriggers for slow-trolled bait are covered only by one secondhand, unconfirmed Cedros data point (2 lb weights, 30 ft of water, two fish hooked, none landed), deliberately not folded into doctrine. | No documented head-to-head comparison of slow-troll vs. flyline on the same fish; the anchored-to-moving bite-rate quadrupling is a single session. | No mackerel-size-to-speed table beyond 'bait big enough for a 3/0-5/0 hook can be pulled faster' within the 1.5-3 mph range. | No conditions data used or available — no SST, chlorophyll, wind, swell, tide or moon were given in the question and none were pulled.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Slow-trolling live mackerel for yellowtail

The KB treats this as one technique note — [`techniques/slow-trolling-bait.md`](techniques/slow-trolling-bait.md) — with the decision logic sitting in the router, [`species/yellowtail.md`](species/yellowtail.md). The core idea: **it is your flyline outfit, with the boat moving.** The bait is the presentation; the boat's job is to cover ground and set the hook (`HTowqnwAMeA`). Nothing about the tackle changes when you switch — only the boat's behavior does.

---

## 1. Speed

**1.5–3 mph, graded to the bait in the tank — not to the species** (`HTowqnwAMeA`, [`techniques/slow-trolling-bait.md`](techniques/slow-trolling-bait.md)):

- **Small sardine** (size 1 or 2 hook bait) — as slow as you possibly can. A small bait can't swim against much speed.
- **Mackerel, or any bait big enough for a 3/0–5/0 hook** — pull it **faster within the range**. (The note carries its own fact-check flag here: the source states the faster-pull trigger as bait big enough for a "40 or 50" — 4/0–5/0 — hook; 3/0 is the note's stated default working hook size elsewhere, not the source's lower bound for this rule.)
- **The test is the bait, not the speedometer.** Watch it swim, and slow down the moment it reads as *dragged* rather than *swimming*.

Since mackerel is the big-bait end, you're at the **top** of that band. One on-camera Cedros data point puts a live-mackerel slow-troll at **roughly 3 mph** ("putt putt putt"), with the mackerel set **50–75 ft** back off the stern on a 40 lb fluorocarbon top shot (`9tIp4n7q850`, [`techniques/trolling.md`](techniques/trolling.md)) — an observation, not doctrine, but it lands exactly where the technique note says mackerel should.

**A conflicting number worth knowing:** a seminar source brackets trolled search speeds as ~1 mph for slow-trolled live **sardines** (thorough, covers little ground), 3–4 mph for a trolled bullet tube bait, ~5 mph for a faster lure (`5Oh3IPIC5g4`, [`species/yellowtail-tube-bait-fishing.md`](species/yellowtail-tube-bait-fishing.md) — the KB flags all three figures as single-source). That ~1 mph is below the technique note's stated 1.5–3 mph floor. It's a sardine number, and the sardine end is where "as slow as you possibly can" lives, so the two are reconcilable — but the KB does not reconcile them, so treat 1.5–3 mph as the mackerel working band and don't be surprised if the bait wants slower.

## 2. Rigging it

**Hook position — nose hook.** The nose spot is the position the KB names as slow-trollable: the clear spot on the end of the nose right before the eyes, side to side (one nostril to the other), which works on mackerel, sardine and anchovy alike (`SluBXkT3cuw`, `T3p1mrqNjIo`, `mscHk0qiXnk`; [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md)). The hook-position table lists nose as "swims naturally, stays up; can be **slow-trolled** or fly-lined."

On mackerel specifically, only two positions get used day to day — **butt hook and nose hook** — and the butt hook is scoped explicitly to **fly-lining with zero weight only**; the nose hook becomes mandatory the moment any weight is added, because a butt-hooked bait under load gets dragged backward, and a mackerel swimming backward doesn't read as a natural silhouette (`w5_x6kkN-xE`). The back/dorsal hook is reserved for kite fishing. So: **nose-hook the mackerel.** (Caveat below in the gaps — no note in this KB states a hook position *for the slow-troll under tow* in so many words; this is the position the KB names as slow-trollable and the one whose mechanics survive being pulled.)

**Hook style and size:**
- Technique-note default: **J hook, 3/0 as the working default**, carrying **1/0, 1 and 2** for two situations — small bait and finicky fish. Downsize line class and hook size *together*; downsizing only one rarely works (`HTowqnwAMeA`).
- Match the hook to the **bait, not the fish** — an oversized hook stops the bait swimming right and it won't get bit ([`bait/fishing-live-bait.md`](bait/fishing-live-bait.md)).
- A Cedros kit carried **Owner ringed offshore hooks in 1/0, 3/0 and 5/0** to cover whatever the dock had that day, from small sardines up to **15 in** mackerel (`_C7TJoGT0nw`, `qHS-ewTQs9Q`; [`tackle/hooks.md`](tackle/hooks.md)). The KB flags an internal disagreement on whether the source said 1/0/3/0/5/0 or literal 10/30/50 — the ASR is ambiguous.
- **Circle hooks are what the Baja slow-troll crews actually run:** live mackerel on a circle hook at Cedros (`QSmE3mdEL28`, `Zo92MG459gQ`, `I-QBxuV2p7M`) and at La Paz (`ORC1A68cEeM`), all in [`techniques/trolling.md`](techniques/trolling.md). If you use one, press the hook **straight down into the bait holding it high on the arch** — holding it from the bottom like a J hook squeezes the bait into a "potato chip" (`8YvmROeVL-0`).

**Line, leader, top shot** (SoCal local coast, `HTowqnwAMeA`):
- **Mainline class 25–40 lb**, and carry a **20–25 lb** option even on a day that starts on 40 — a full day of bites on 40 lb is described as luck rather than the norm locally: *"you'd be really surprised how hard you can pull on 25 lb"* once the drag is set for it.
- **~6 ft of fluorocarbon matched to the mainline** — 30 lb main gets 30 lb fluoro — and at most **halve it** when fish are finicky (30 lb main → 25 lb floor). Going lighter than that costs fish to abrasion right at the hook.
- **Full outfit as described:** 8 ft fiberglass or composite rod, **size-25 reel**, **50 lb braid** to a **30–40 lb mono top shot**, then the short fluoro to the hook. The braid capacity matters because the first run has to come off the spool before you can advance the light drag.

**Setback: 100–150 ft.** Not far — a long setback isn't the goal, and past ~150 ft you lose the hook-setting benefit of boat motion and gain nothing (`HTowqnwAMeA`).

**Drag — this is the part people get wrong.** Fish a **light drag and let the boat's forward motion drive the hook**; on a lever drag, around the **"2"** mark ([`tackle/star-drag-vs-lever-drag.md`](tackle/star-drag-vs-lever-drag.md)). Why it can't be pinned tighter: a yellowtail eating a slow-trolled bait takes **50–100 yd immediately**, more on a bigger fish — a locked drag at that moment either parts the line or backlashes the reel (`HTowqnwAMeA`). Whether you fish in gear at all is angler preference; the light setting is the specific call. On a circle hook, **don't strike** — let the rod load and wind tight (`QSmE3mdEL28`); one La Paz crew instead counted a deliberate **"1, 2, 3"** before putting the reel in gear (`ORC1A68cEeM`). The KB keeps those two side by side rather than reconciling them.

**Baja / heavy-structure line classes run much heavier, and that is a real fork.** Over shallow resident rock the same technique is fished at **80–100 lb line class** with mackerel on a circle hook (`QSmE3mdEL28`), **65 lb braid to 80 lb fluoro** (`I-QBxuV2p7M`), **straight 80 lb** with some of the group recommending 100 (`Zo92MG459gQ`), **40 lb** at La Paz over 12 ft of water with drags tested before the troll starts (`ORC1A68cEeM`), and **65 lb braid to 60 lb fluoro** at the El Bajo high spot (`92y14x33etQ`). **The decision frame the KB supports:** 25–40 lb is the SoCal local-coast number; you step up where grade and structure punish light line — Cortez fish "swim straight down" into the rocks (`UfuiWFVvz2E`), and 40–50 lb landed Cedros-triangle shallow-rock fish that lighter line lost (`_r_qKX_7080`) ([`species/yellowtail.md`](species/yellowtail.md), footnote [b]). Hooked fish in that shallow rock repeatedly run back at the structure, and **backing the boat down** on a big one was called out as a deliberate, important move (`QSmE3mdEL28`, `ORC1A68cEeM`).

## 3. When it's the right call vs. flylining

They are the same tackle and the same bait — so this is a boat-behavior decision, not a tackle decision. Three things drive it:

**a) The meter read — this is the primary trigger.** From [`species/yellowtail.md`](species/yellowtail.md#finding-them-sign--sonar):

| What you see | What it means | What to fish |
| --- | --- | --- |
| **Stratified column** — marks from the bottom up through mid-column, sometimes to the surface; or fish sitting high and spread over a small rock (~20–30 ft across) | Fish are actively **hunting bait** | **Slow-trolled bait and flylined bait both work** (`HTowqnwAMeA`) |
| **Balled tight to the bottom** | Present but **not feeding** | Dropper loop, or a yo-yo burned past them — **neither slow-troll nor flyline** (`HTowqnwAMeA`; the note flags that `tpmOYXYQwhU` does not actually support the burned-yo-yo half) |
| Fish metered **40–60 ft**, not yet showing | Staging up | Surface iron and light bait — go all-in on the iron when they boil (`0DKmYId1NN4`) |

So the meter tells you whether it's a **bait day at all**; it does not by itself pick troll over flyline.

**b) Slow-troll when you want to keep covering water; flyline when you're committed to a spot with bait in the water.** Slow-trolling is the choice when live bait is rigged and you don't want to commit to an anchor or a drift (`HTowqnwAMeA`). The KB's strongest statement on this is in the router's Doctrine section: **"Don't marry the technique"** — pulling the anchor and slow-trolling around the same zone **roughly quadrupled a bite rate** over anchor-fishing the spot that had been chosen for anchoring (`HTowqnwAMeA`, [`species/yellowtail.md`](species/yellowtail.md#doctrine--conflicts)). Flylining, conversely, is the call when **bait is in the water and fish are on the chum or the bait line**, or on a paddy or boil ([`techniques/flyline.md`](techniques/flyline.md)) — and it's the specific pick for **fish visible or metered but not eating**, where you downsize and fish the tide/current window ([`species/yellowtail.md`](species/yellowtail.md#situations--techniques)).

The Coronados zone guide sequences both explicitly: with live bait aboard, **switch to slow-trolled bait over the same zones**, put a **flylined bait out when current and tide turn the fish onto bait**, and drop a dropper loop to bottom marks (`D5DR7Kx42_A`, [`species/yellowtail-coronado-islands.md`](species/yellowtail-coronado-islands.md)).

**c) Conditions — slow-troll survives wind that kills casting.** A Cedros crew kept the live-mackerel slow-troll running through building wind and whitecaps precisely because it doesn't depend on a clean cast the way iron does — *"the good news is we're just slow-trolling... I don't think the fish care"* (`QSmE3mdEL28`). Note the counterweight in the router: hard wind (~25) after a run of surface days generally sends the whole bite down to the **yo-yo** (`ejUTAnONf7o`). So wind favors slow-troll *over casting bait or iron*, but it does not make a bait presentation beat a deep iron.

**Why mackerel rather than sardine here:** live mackerel at San Clemente, Catalina or the Coronados **screens the catch toward yellowtail**, cutting out the calico, barracuda and bonito bycatch a smaller bait draws — reach for it when you want straight yellowtail. Yellowtail have been seen eating mackerel up to **1.5 lb**, sometimes five or six fish attacking one bait at once (`w5_x6kkN-xE`, [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md)). Cedros crews specifically hunted **big, fat ~2 lb mackerel** for this program (`Zo92MG459gQ`), and one Cedros kit was built around mackerel up to **15 in** (`_C7TJoGT0nw`).

**Calibrate before you blame the technique:** a good SoCal local-coast yellowtail day is **three or four bites**; 12–15 bites is an anomaly. Two fishless hours is not evidence the technique is wrong (`HTowqnwAMeA`). That's local-coast scope, not an island or Baja expectation.

## 4. Common failures (all `HTowqnwAMeA`)

- **Pinning the drag** — costs the fish on the first 50–100 yd run.
- **Setting the bait past ~150 ft** — the boat can no longer set the hook.
- **Over-dropping the fluoro** — halving the mainline class is the floor, not a starting point.
- **Running one speed all day** — speed is a function of what's in the tank and changes when the bait does.
- **Treating educated local fish as naive** — fish on the heavily-worked coast north of the border have seen a lot of slow-trolled baits (single source's stated view, not measured behavior).

## 5. Against your profile

Your listed flyline outfit — **setup #2, the Teramar TMC90MHB2 (9'0", MH, fast, 30–65 lb braid class) + Avet MXJ 5.8 MC, 50 lb braid** ([`profiles/cameron/rods.md`](profiles/cameron/rods.md)) — is the flyline / soft-rod class the technique calls for ([`tackle/gear-classes.md`](tackle/gear-classes.md)), and its 50 lb braid matches the note's build exactly; add a 30–40 lb mono top shot and ~6 ft of matched fluoro. **Two gaps worth naming rather than papering over:** the note's build specifies an **8 ft glass or composite** bait rod, and the only E-glass rod in your inventory is the 6'0" Seeker 660H on diver-troll duty — not the same tool. And if you take this program to shallow Baja rock at the 80–100 lb line classes above, nothing in your profile is routed to slow-trolling at that class; the Talica 25 and Trinidad 40 exist but the KB does not map them to this technique.

---

**Not covered by this KB** — I'm not filling these from outside knowledge:

- No note states a mackerel hook position **specifically for the slow-troll under tow**. The nose hook is the position the KB names as slow-trollable, and the mackerel-specific guidance scopes the butt hook to zero-weight flylining only — that's the inference I made, but it isn't stated as slow-troll doctrine.
- No **course pattern** for the live-bait slow-troll (sweeps, arcs, passes over the structure). The KB's "sweeps, not straight lines" doctrine is scoped to hard-bait tuna trolling (`HzE4FHHcvTk`).
- No stated **number of baits** to slow-troll. The only data point is an Ensenada observation of "a couple of live mackerel from the stern" while casting jigs from the bow (`0dIwWiOc1NY`).
- No **bait-refresh interval** on the troll (the "swap after two or three minutes" guidance is flyline-scoped, `MuC0uGKDzxg`).
- No **circle vs. J decision rule** for this technique — J is the technique note's default (`HTowqnwAMeA`), circle is what the Baja crews run, and the KB never reconciles them.
- No **bridling** guidance for a slow-trolled yellowtail mackerel; the KB's bridle entry is scoped to big baits for tuna/marlin and is explicitly flagged as general practice not covered by its SoCal sources.
- No conditions data for today — you gave none and I made no BightSST call, so nothing above is timed to actual water.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/slow-trolling-bait.md`, `techniques/evidence/slow-trolling-bait.md`, `techniques/flyline.md`, `techniques/trolling.md`, `species/yellowtail.md`, `species/yellowtail-coronado-islands.md`, `species/yellowtail-tube-bait-fishing.md`, `bait/fishing-live-bait.md`, `tackle/hooks.md`, `tackle/gear-classes.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `HTowqnwAMeA`, `_C7TJoGT0nw`, `qHS-ewTQs9Q`, `9tIp4n7q850`, `Zo92MG459gQ`, `QSmE3mdEL28`, `I-QBxuV2p7M`, `ORC1A68cEeM`, `92y14x33etQ`, `0dIwWiOc1NY`, `w5_x6kkN-xE`, `SluBXkT3cuw`, `T3p1mrqNjIo`, `mscHk0qiXnk`, `8YvmROeVL-0`, `D5DR7Kx42_A`, `0DKmYId1NN4`, `tpmOYXYQwhU`, `ejUTAnONf7o`, `_r_qKX_7080`, `UfuiWFVvz2E`, `5Oh3IPIC5g4`, `MuC0uGKDzxg`, `HzE4FHHcvTk`, `cameron`  
*gaps admitted:* No note states a mackerel hook position specifically for slow-trolling under tow — nose is the position the KB names as slow-trollable, and the mackerel guidance scopes butt-hooking to zero-weight flylining, but the slow-troll case itself is never stated. | No course/steering pattern for the live-bait slow-troll; the KB's 'sweeps, not straight lines' doctrine is scoped to hard-bait tuna trolling only. | No stated number of baits to run on a live-bait slow-troll — only a single Ensenada observation of 'a couple of live mackerel from the stern'. | No bait-refresh interval for a slow-trolled bait; the two-to-three-minute swap guidance is flyline-scoped. | No circle-hook vs J-hook decision rule for this technique — J is the technique note's default, circle is what the Baja crews run, and the KB keeps them side by side without a frame. | No bridling guidance for a slow-trolled yellowtail mackerel; the KB's bridle entry is scoped to big tuna/marlin baits and flagged as general practice its SoCal sources do not cover. | The technique note's 1.5-3 mph band and the seminar's ~1 mph slow-trolled-sardine figure are not reconciled anywhere in the KB. | No conditions were supplied and no BightSST pull was made, so none of this is timed to actual water, tide, or wind. | Cameron's profile has no 8 ft glass/composite bait rod matching the note's stated build, and no rod routed to the 80-100 lb Baja shallow-rock version of this program.

</details>

### 12. [technique] When does kite fishing for bluefin beat a flyline, and what is the setup?

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B3', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three get the decision rule right (100–300 lb grade plus wind plus located fish for the kite; picky/smaller/chummed-up bait bite or no wind for the flyline) and all three admit the corpus never compares the two head-to-head. A wins because it is the only one that does all three jobs completely: it names the seam it had to bridge, it delivers the full kite outfit — rail rod rating, named reels, 130–200 lb main with top-shot spec, 500 lb swivel, hook sizes, harness, kite line and release — and it resolves against the boat, catching that Cameron's 100 lb braid sits under every documented kite program, that the 8–15 kt band overlaps the 12 kt sea-state cutoff, that boat.md's range and sea-state fields are null, and adding small-boat fight mechanics no other answer has. B is a close second with equally good hardware and the unique pool-noodle flyer, but a thinner profile pass that never tests the wind band against the panga. C has the best conflict-spotting (the unreconciled bite-leader material) and the most scrupulous labeling of its own inference, but it answers the "what is the setup" half at class level only — no rod/reel models, no top-shot or swivel spec, no J-hook size — so an angler could not build the outfit from it.

- *B2 reasons:* found: correct notes, and the sharpest read on internal disagreement — it catches the kite bite-leader material conflict (200–400 lb mono vs 200 lb+ fluoro vs 300–400 lb fluoro) that neither other answer surfaces. specific: dates and places attached to most cites, full harness detail, 120–150 yd, ~45° wings, 3–3.5 ft leader, the two boat-speed programs, and an unusually deep flyline contrast (4/0 thin-wire circle for sardine, 15–20 lb on anchovy, 60-second bait discipline). sourced: paths and video ids with upload dates and named captains, all plausible. scoped: region-correct, labels the Baja long-range squid item as not a SoCal bank program, no bare regulation, tagline flagged as unconfirmed — but never states the regions/waters gate explicitly. honest: best-labeled inference in the set — the ~8–12 kt panga window is explicitly called its own read across two notes, not KB doctrine; no relative time. actionable: weakest on the setup half the question asks for — the kite outfit is class terms only (150–200 lb, ~100 lb braid, one observed Makaira 50W), with no rod/reel models, no main-line/top-shot build, no swivel spec and no J-hook size, so the fighting outfit cannot be assembled from this alone.
- *B3 reasons:* found: right notes, clean decision table, and adds the micro-bait foamer case and the charter ranking of frozen dead flyers. specific: strong hardware — ATD 50 on Seeker 2x4, 200 lb spectra to 400 lb mono, Tiagra 50W with 15 ft 135 lb top shot, ~1,000 yd of 130–200 lb, 3–3.5 ft leader, 9/0–12/0 J + 5X treble, plus the unique pool-noodle 'life jacket' flyer as a kite-free option. sourced: paths and video ids throughout; attributions to Searcher/Hansen match the cited ids. scoped: states the kite regions/waters gate and points at day-plan steps 1–1b, labels the Baja squid item, no bare regulation and the tagline is flagged as unconfirmed. honest: keeps a losing kite day as a counter-data point, leaves the ~8 kt frameworks deliberately unreconciled, and admits no controlled kite-vs-flyline comparison exists; no relative time. actionable: buildable and fishable, but the profile pass is thinner — it flags the 100 lb braid yet never tests the 8–15 kt band against the panga's sea-state limit.
- *NOW reasons:* found: pulls the bluefin router, trolling spin-out, kite/flyline/fighting technique notes, harness rig, live-bait note, gear classes, sea-state and both profile files, and opens by naming the seam (no head-to-head kite-vs-flyline source in corpus). specific: fullest build — 7'6" 80–200 lb rail rod, Seeker 2x4/ATD 50/Tiagra 50W/Talica 25, 130–200 lb braid with 15 ft 135 lb top shot, 500 lb ball-bearing swivel, 200–400 lb bite leader at 3–3.5 ft, 9/0–12/0 J + 5/0 5X treble, 45° wings, 120–150 yd kite run, 8.5 kt rubber-flyer troll, 4–5 kt hookset drive. sourced: note paths plus video ids on essentially every parameter, and it separates what a cite supports from what it doesn't (six-fish claim marked as a stated goal, not an achieved rate). scoped: states the regions/waters gate for kite fishing up front, keeps the Baja squid and tournament items region-labeled, no bare regulation — the 30 ft tagline is explicitly flagged as unconfirmed as a regulation and Mexican limits are logged as a gap. honest: flags the internal 8–15 kt contradiction, the flyline line-class conflict across three notes, the ASR-garbled fight duration, the untested sinker report, and 20+ real gaps; no relative time. actionable: an angler can build the harness, the outfit and the kite line, work the bait, set the hook and fight it from a small boat, and knows exactly which pieces Cameron does not own.

<details><summary>Full prompt</summary>

When does kite fishing for bluefin beat a flyline, and what is the setup?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short answer

The kite wins when **the grade is big (100–300 lb), there is wind to fly it (~8–15 kt), and the fish are concentrated enough to sit over**. The flyline wins when **you have live bait in the water and a chum-line/foamer bite going, especially on picky or smaller-grade fish, and on days with no wind**. They are not mutually exclusive — the corpus repeatedly shows both fished in the same window off the same boat.

Note: you gave me no conditions, so nothing below is a go/no-go for a specific day. Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), step 1 is still pulling live BightSST wind/swell for your zone and transit before this decision is real.

---

## When the kite beats the flyline

**1. Grade 100–300 lb with 8–15 kt of wind — this is the kite's row, outright.**
The bluefin router puts it plainly: for **big fish 100–300 lb, wind ~8–15 kt**, fly a flying fish under a kite — "*the* most effective method for 100–300 lb" ([`species/bluefin-tuna.md`](species/bluefin-tuna.md), Situations → techniques). The trolling spin-out repeats it as doctrine: "anyone who fishes big SoCal bluefin will tell you the most effective way to catch **100–300 lb** fish is a flying fish under a kite" ([`species/bluefin-trolling.md`](species/bluefin-trolling.md)). The flyline row in that same table is a different job — "chummed up / picky on bait," **40–60 lb class**, sardine on a circle hook.

**2. Fish locked on tiny natural bait and refusing everything else.**
NE of Santa Barbara Island, foamers all around the boat would not convert — a trolled spreader-bar pass and cast plugs both went scoreless, the crew's read being the fish were locked onto **saury, anchovies, microbait**. Going back to a dead flying fish under the kite is what converted (`mDmbGdQAy-4`, 2025-10-06; [`species/bluefin-tuna.md`](species/bluefin-tuna.md)).

**3. Once you've located fish and want to hold on them.**
The Tanner Bank program from a charter captain: **troll spreader bars to cover ground and search until the sounder is marking good numbers, then stop and fish a dead flying fish under the kite in the drift** over those marks — the stated preference is kite over spreader bar once fish are located (`vCskOx6N-XM`, late October 2021; [`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`species/bluefin-trolling.md`](species/bluefin-trolling.md)). That day a group entirely new to bluefin landed multiple 100 lb+ fish.

**4. The wind sub-decision *inside* the kite program (Capt. Dave Hansen, `2y0VznL2qk8`, 2020-12-29; [`techniques/kite-fishing.md`](techniques/kite-fishing.md)):**
- **~8 kt of wind or more → troll a rubber flyer at ~8.5 kt under the kite.** Covers water while searching and converts bite-to-hookup at a better ratio than sitting dead-boat. Mark the school on the GPS and keep working it.
- **Under ~8 kt, fish already located** (surface sign or heavy sounder marks) **→ go dead-boat**, deploy (typically **two**) dead flying fish under the kite or a balloon and drift them like float fishing. Never deploy a dead flyer speculatively over blind water.

**Where the kite loses to trolling, not to the flyline:** when it's **too light to fly a kite, or the fish are too spread out to sit and kite over** — a coverage need, not a sea-state call (cameron) — speed-troll a full-size Mad Mac at **13–15 kt** (Nate Winnicki, `z1CmWHqe9uk`; [`species/bluefin-trolling.md`](species/bluefin-trolling.md)).

**Honest counter-data point:** a kited flying fish drew a swirl that would not commit during a Baja tournament day, and that boat landed nothing across the event despite kite and spreader-bar effort in a zone with confirmed sign (`IxhdiX3oEEs`, 2019-11-13; [`species/bluefin-tuna.md`](species/bluefin-tuna.md)). The kite is the highest-percentage tool for the grade, not a guarantee.

---

## When the flyline beats the kite

- **Live bait is in the water and fish are on the chum or bait line** — that is the flyline's trigger ([`techniques/flyline.md`](techniques/flyline.md), "Reach for this when"). The kite needs wind and a rigged flyer; the flyline needs neither.
- **The daytime bite is often just a bait bite.** On one Highliner trip, **~90% of daytime bites came on flyline**, fished on a dedicated **25–30 lb fluorocarbon** flyline stick, majority on **size 2 circle hooks** (sizes 1 and 1/0 also used); the remaining daytime bites were 2 on a sinker rig and 1 on a Colt Sniper (Ray Sharifi, `149px8WQ2Ng`, 2023-04-24; [`species/bluefin-tuna.md`](species/bluefin-tuna.md)).
- **Some days they eat *only* the flyline.** A June 2023 El Dorado day ~45 mi offshore: the bluefin bit strictly on flyline and refused a sinker rig; **25–40 lb test to a straight No. 2 hook**, sardine bait (`oB4BpIUTTl4`/`r4J5nP5Bkl4`; [`techniques/flyline.md`](techniques/flyline.md)).
- **Picky / finicky fish** — the fix is thinner, not heavier: skipper guidance caps fly line at **20–25 lb test, no more than 30** for tough bites (Cesar, Eric's Tackle, `48ZFXnCTTQE`; [`techniques/flyline.md`](techniques/flyline.md)).
- **Marginal, gusty or dying wind** makes the flyer inconsistent on the surface — that's the cue to leave the kite down ([`techniques/kite-fishing.md`](techniques/kite-fishing.md), "Wind window").

**They run side by side more often than they compete.** A sundown Cortez-Bank-to-port bite produced multiple bluefin **over 100 lb on both the kite and flyline fished alongside it in the same window**; one kite fish took **~40–45 minutes** to land (`zBd1mayUt_I`; [`techniques/kite-fishing.md`](techniques/kite-fishing.md), [`species/bluefin-tuna.md`](species/bluefin-tuna.md)). Earlier in that same 3-day charter the kite was flown during a hot morning bite alongside bait rods while the boat was still adrift (`QSvzVHW9UMk`, 2025-02-12, Cortez Bank).

---

## The kite setup

### Rod, reel, line
- **Kite/fighting outfit: 150–200 lb class**, ~**100 lb braid** for capacity and less wind-blow. **It never casts** ([`species/bluefin-tuna.md`](species/bluefin-tuna.md) gear summary, [`species/bluefin-trolling.md`](species/bluefin-trolling.md), [`tackle/gear-classes.md`](tackle/gear-classes.md) — the trolling / spreader-bar class row).
- Heavy fighting-rod class — these are 100–300 lb fish and the rod is pure leverage ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)). Observed reel example: **Okuma Makaira 50 Wide** (`usHl-4SfqDA`, 2024-11-13).
- **Kite line** runs on its own dedicated reel: **straight braid, no separate leader section**, a **heavy-duty snap swivel** (don't over-crank it down on the line), spooled out roughly **a couple hundred yards** once set (`Ix0gG0-l3v0`, 2024-08-21, Ensenada).

### The connections
- The fishing line runs to a **release clip on the kite line**; on the eat the line **pops out of the clip** and you come tight directly to the fish — no clip in the fighting system ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)).
- **Breakaway:** thread a small ring onto the fishing line *before* tying on the snap swivel, then tie a **rubber band from that ring to the release clip** — no knot ties the fishing line to the clip; the rubber band is the weak link (`Ix0gG0-l3v0`).
- **Quick release on the kite line:** make a loop in the line and flip/hook it onto the release-clip mechanism rather than tying a knot (`Ix0gG0-l3v0`).
- **Balloon-to-kite (when you run one):** balloon twists into a dedicated balloon clip with no knot; the clip is rubber-banded to the kite; back that up with about **three taped fishing-line safety tethers** per kite (plain tape — it doesn't develop a sharp edge and pop the balloon) so a broken rubber band doesn't cost you the kite and balloon (`vCskOx6N-XM`).
- **Launch:** hand the kite up and let it go with the wind — it flies straight up off the stern, and once the boat turns onto an angle it carries away instead of sitting overhead (`vCskOx6N-XM`).

### Flying it
- **Height:** as high as you can while still **seeing the flyer skipping** — bait visibility sets the ceiling, not a fixed number (`rsCAh-QyK60`, 2017-06-06, ~40 mi off San Diego).
- **Distance:** **120–150 yd** off the boat in that session, shifting with wind, drift and boat heading (`rsCAh-QyK60`).
- **Set the clip so the flying fish just touches the surface** — skipping and splashing, never dragging under. That splashing commotion is the whole trigger ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)).
- **Boat speed, two different observed programs, not reconciled in the KB:** **8 mph (~7 kn)** trolling the flyer under the kite (`rsCAh-QyK60`) vs. roughly **2 kt on a single center engine** to work the spread slowly while searching (`Ix0gG0-l3v0`). Dead-boat drift is the third mode (`2y0VznL2qk8`).
- **Pay the kite line out by loosening the star drag** on the kite reel rather than thumbing the spool (`Ix0gG0-l3v0`).
- **Gyro-stabilized binoculars** were called mandatory — both for spotting fish and for watching the flyer stay upright and skipping correctly (`Ix0gG0-l3v0`).

### The bait and its rig — [`rigging/flying-fish-harness.md`](rigging/flying-fish-harness.md)
- **Dead natural flying fish**, harnessed: skewer in behind the shoulder just above the spine; a second skewer opens the wing hole; wings held open with zip ties, both sides, everything cinched so nothing slips.
- **Wing angle ~45°** — set further out and a swell knocks the bait off its presentation (`YsiHziY_PWw`).
- **Body skewer** down the middle entered through the mouth, pushed ~three quarters in, lifting the tail as you finish so the bait sits slightly tail-down. **Mouth skewer** pins the mouth closed so it doesn't scoop water.
- **Hooks:** standard San Diego flyer rig — **large J hook up front with a large treble trailing as a stinger**, the treble set into the back just behind the body stick, under the spine and out the other side. Tail treble spec: **5/0 5X-strong Mustad** (`YsiHziY_PWw`).
- **Leader — the KB carries three unreconciled numbers here:** **200–400 lb mono, typically 400** (`GqcVaTIlyg0`, [`rigging/flying-fish-harness.md`](rigging/flying-fish-harness.md)); "heavy fluorocarbon bite leader, 200 lb-plus, 300 lb common" ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)); **300–400 lb fluoro** in the trolling table ([`species/bluefin-trolling.md`](species/bluefin-trolling.md)). Pick heavy; the KB does not settle mono vs fluoro.
- **Bite-leader length: 3 ft, 3.5 ft maximum** (`YsiHziY_PWw`) — any longer and the swivel hits the rod tip before the fish is in gaff range.
- **Volume:** rig **10–12 flyers for a four-angler day**, stored neatly in the cooler ready to deploy. Most anglers buy flyers at the tackle shop — you can sabiki them, but it's tough.

### Bait alternatives under the kite
- **Live mackerel, back/dorsal-hooked right in front of the dorsal fin** (a hard spot that holds a hook) — the simpler live-bait alternative for the same 100–300 lb grade; the bait sits flat and flutters/daps each touchdown without the leader dragging where a leader-shy tuna sees it. This is **kite-only** — mackerel otherwise get butt-hooked (zero weight) or nose-hooked (any weight) (Dave Hansen, `w5_x6kkN-xE`, 2021-04-06; [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md), [`techniques/kite-fishing.md`](techniques/kite-fishing.md)). Also draws yellowtail and calico bass.
- **Rubber flyer ("Yummy Flyer")** — the trolled version, ~8.5 kt, for searching in ≥8 kt wind (`2y0VznL2qk8`).
- **Popsicle-stick wing lock** stapled to the bait as a fast field substitute for the skewer/zip-tie harness, with the same big-single-plus-trailing-treble tandem (`usHl-4SfqDA`).
- **[Baja, long range] whole squid on a double-hook rig** under the kite for giant grade, drifted with current and wind (`pk2blktDQ9Y`, Intrepid, lower banks ~608 nm south of San Diego) — a Baja long-range data point, not a SoCal bank program.

### The bite, hookset and gaff
- **Dead-boat bite:** it shows as a surface explosion on the flyer. Put the boat in gear and drive **forward gently, ~4–5 kt, not a hard throttle** — keeps the rod bent and constant pressure on as the fish takes off without shock-loading (`2y0VznL2qk8`).
- Keep the flyer **dapping** — constantly touching the water, bouncing with the swell, never submerged and never airborne — and watch it continuously through binoculars (`2y0VznL2qk8`).
- **At the boat:** lay the short leader flat on the surface to bring the fish into gaff range at the swivel ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)). Full fight mechanics are in [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md) via the router.
- **Common failures:** wings set too far out (a swell kills the presentation); leader too long (you hit the swivel before gaff range); letting the flyer sink or drag instead of skipping.

---

## The flyline setup, for contrast

- **Class: 40–60 lb**, circle hooks **size 1–2/0**. A first-time big-fish build wants **400+ yd of line, 80 lb backing, 50–60 lb mono top shot, and ~3 ft of fluoro** ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)).
- **Two-rod light/heavy system covering 25–80 lb** (Ray Sharifi, `jQW2HLkMsmY`, 2022-05-02): **light stick** 8 ft rated 20–50 lb, Torium 16, **30 lb mono top shot, 50+ yd**, short matched fluoro leader, for 20–50 lb grade; **heavy stick** 7 ft rated 30–80 lb, Trinidad 20A, **40 lb (sometimes 50 lb)** fly line direct, for bigger fish. Mono over straight braid-to-fluoro specifically for flylining — it comes off the reel more easily and doesn't stick to itself, so the bait swims naturally ([`techniques/flyline.md`](techniques/flyline.md)).
- **Sportboat sardine for bluefin: 4/0 thin-wire circle hook, straight-tied — no swivel, no bead —** with a San Diego jam, fluoro throughout. Thin wire because a sardine, unlike a heartier mackerel, has a hard time swimming a heavier-gauge hook around convincingly (Dave Hansen, `ftEvyfwjZFU`, 2021-06-08).
- **Mackerel into a foamer:** thick-wire Mustad circle tied straight to **3–4 ft of 80 lb fluoro**, San Diego jam, **no weight, no swivel, no beads**, mackerel nose-hooked, thrown right into the foam (Dave Hansen, `RbqOKkINSCM`, 2021-05-25). Kept side by side in the KB with the downsizing philosophy below — different bait, different situation, not a contradiction.
- **Finicky-bite build: 25 lb mono top shot → 50 lb fluoro bite guard, 2–3 ft**, Seaguar knot. The 25 lb mono is what pulls through the water so the bait swims like it's on 25 lb; the short heavy fluoro rides inside the mouth against teeth and gill plates. Applied steps: 30 lb main → 40 lb leader, 25 lb main → 40 lb leader (Cesar / Ray Sharifi, `48ZFXnCTTQE`).
- **Circle hooks specifically for big bluefin** — their teeth saw through leader, so the corner-of-the-mouth hookset keeps the leader out of the teeth (Dave Hansen, `RbqOKkINSCM`).
- **Match line to the bait, not just the fish:** 40 lb to flyline a mackerel, drop to **15–20 lb** if the tank turns to anchovy (`gKrYKvqHUjk`). **Distance beats weight** — get your bait beyond everyone else's; a split shot to help the cast is a crutch, not an upgrade.
- **Bait discipline:** cull bloody/scaly/lethargic baits; if a bait isn't pulling line within about **60 seconds**, change it. Butt-hooked sardine was the "hot ticket" on one Catalina-west-end morning, **2/0–3/0** hook, **25–30 lb** test (`M7BtON4GZgQ`).

---

## Resolved against your profile (Cameron)

- **Kite rod:** the **Fathom 80** setup is already designated the future kite rod — Okuma PCH-C-741XXXXH, **7'4", XXXX-H, 150–200 lb**, Penn Fathom II 80LD2 2-speed (50 lb max drag), **~1000 yd of 100 lb braid**, spreader-bar trolling only, never casts. Keep the 100 lb braid for capacity and less wind-blow; 200 lb leader; small boat can chase ([`profiles/cameron/rods.md`](profiles/cameron/rods.md)). That is the only rod in the 8 that matches the 150–200 lb kite class.
- **Flyline rod:** the **Avet setup** (Teramar TMC90MHB2 9'0" MH 30–65 lb, Avet MXJ, 50 lb braid) is the flyline/soft-rod class; the **Trinidad 40** covers heavy flyline ([`profiles/cameron/rods.md`](profiles/cameron/rods.md), [`tackle/gear-classes.md`](tackle/gear-classes.md)).
- **Light-wind kite window is closed on the panga:** helium-balloon assist is ruled out — too expensive and no room for a tank on the boat. That's a platform constraint, not a rule of the fishery; on a bigger boat the light-wind window reopens ([`techniques/kite-fishing.md`](techniques/kite-fishing.md), [`species/bluefin-tuna.md`](species/bluefin-tuna.md)). You started kite fishing July 2026.
- **Wind-window tension worth planning around:** the kite row wants **8–15 kt**, but the go/no-go doctrine in [`conditions/sea-state.md`](conditions/sea-state.md) has **wind above ~12 kt raising whitecaps** with a working-captain cutoff at 12 kt, and calls **12–15 kt with 4–8 ft swell at 9 seconds** flatly unfishable (Dave Hansen, `NC3-3pJDEgo`, 2020-11-18, medium confidence, single mention). On a 22 ft panga the realistic kite window is the **~8–12 kt** overlap, and the upper half of the router's band is a bigger-boat number. The KB does not state this reconciliation — it's my read of two notes side by side, so treat it as a planning caution, not KB doctrine.
- **Boat handling:** the Panga tops ~35 kt and idles ~1.5 kt, so the ~2 kt slow-search-under-kite mode and the 4–5 kt hookset drive are both inside the envelope; the ~8 mph trolled-kite mode is too ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)).

---

## What the KB does not cover

- **No explicit head-to-head kite-vs-flyline rule.** The two live in separate rows of the router table and the corpus shows them fished simultaneously; nothing in the KB ranks them for the case where you have both wind *and* a hot chum-line bite.
- **No lower grade cutoff for the kite** — it's specified for 100–300 lb, with nothing saying at what grade the kite stops being worth flying.
- **No kite hardware specs** — no kite size, model, or wind-rating-per-kite guidance; height is given only as "as high as you can still see the flyer."
- **Mono vs fluoro for the kite bite leader is unresolved** (200–400 lb mono vs 200–300 lb-plus fluoro vs 300–400 lb fluoro across three notes).
- **No drag settings or strike-drag numbers** for the kite outfit.
- **How many kite rods/flyers to fly at once** is only implied ("typically two" dead flyers under the kite/balloon in one source).
- **The ~30 ft "mandatory" tagline** from the Baja tournament is logged with its attachment point and mechanism unresolved on the audio, and is not confirmed as any jurisdiction's regulation.
- **No live conditions were provided**, and the KB deliberately holds no conditions data — the actual wind/swell call requires a BightSST pull per the day-plan protocol.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `CLAUDE.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `techniques/kite-fishing.md`, `techniques/flyline.md`, `rigging/flying-fish-harness.md`, `bait/fishing-live-bait.md`, `tackle/gear-classes.md`, `conditions/sea-state.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`  
*videos:* `YsiHziY_PWw`, `GqcVaTIlyg0`, `2y0VznL2qk8`, `w5_x6kkN-xE`, `gKrYKvqHUjk`, `RbqOKkINSCM`, `ftEvyfwjZFU`, `48ZFXnCTTQE`, `149px8WQ2Ng`, `jQW2HLkMsmY`, `rsCAh-QyK60`, `Ix0gG0-l3v0`, `vCskOx6N-XM`, `usHl-4SfqDA`, `zBd1mayUt_I`, `QSvzVHW9UMk`, `mDmbGdQAy-4`, `IxhdiX3oEEs`, `z1CmWHqe9uk`, `NC3-3pJDEgo`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `pk2blktDQ9Y`, `M7BtON4GZgQ`, `cameron`  
*gaps admitted:* No note states an explicit kite-vs-flyline decision rule; the two are separate rows in the bluefin router and are shown fished side by side, never ranked against each other for a day with both wind and a hot bait bite. | No lower grade threshold for the kite — it is specified only for the 100-300 lb class, with no guidance on when fish are too small to bother flying one. | No kite hardware specs: no kite size, model, or wind rating per kite; flying height is given only as 'as high as you can still see the flyer.' | Kite bite-leader material is unreconciled across three notes: 200-400 lb mono (typically 400), 200 lb-plus fluoro (300 common), and 300-400 lb fluoro. | No drag settings or strike-drag numbers given for the kite/fighting outfit. | Number of kite rods or flyers to fly simultaneously is only implied ('typically two' dead flyers under the kite or a balloon in one source). | The ~30 ft 'mandatory' tagline from the Baja tournament has its attachment point and mechanism unresolved on the audio and is not confirmed as any jurisdiction's regulation. | The 8-15 kt kite window vs. the sea-state note's ~12 kt whitecap/no-go cutoff is not reconciled anywhere in the KB; my ~8-12 kt panga-realistic window is inference across two notes, not KB doctrine. | No conditions were supplied and the KB holds no conditions data, so no go/no-go call for a specific day is possible without a BightSST pull.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short answer

Kite beats a flyline when **the grade is 100–300 lb and there is wind to fly it** — that combination is where the KB puts the kite first, ahead of everything else in the bluefin box. The flyline wins when the fish are **chummed up / picky on bait**, when the grade is **smaller (roughly 20–80 lb)**, or when the bite has gone finicky and the answer is thinner line, not a bigger presentation. On a lot of real days both are in the water at once.

No conditions were given in your question, so what follows is the doctrine layer. On an actual day, run steps 1–1b of `planning/day-plan-protocol.md` first (conditions, then the `{regions, waters}` envelope) — kite fishing is gated to `regions: socal-bight, baja-pacific-north, baja-pacific-south` and `waters: open-ocean, bank` (`techniques/kite-fishing.md`), so it is never an island-lee or nearshore play.

---

## When the kite beats a flyline

| Condition | Call | Source |
| --- | --- | --- |
| **Fish 100–300 lb, wind ~8–15 kt, fishable swell** | Kite a flying fish. "A flying fish under a kite is *the* most effective method for 100–300 lb" — stated as consensus doctrine, not one captain's preference | `species/bluefin-tuna.md`, `species/bluefin-trolling.md` |
| **Fish located and concentrated enough to sit over** | Troll to find, then **stop and kite the drift over the marks**. Captain Andrew's stated program at Tanner Bank: run spreader bars to cover ground, then once the sounder marks good numbers, stop and set a dead flyer under the kite — with a stated personal preference for the kite once fish are found | `species/bluefin-trolling.md` (`vCskOx6N-XM`) |
| **Foamers all around but locked onto micro-bait** (saury, anchovy, tiny stuff) and refusing everything | Kite. A trolled spreader-bar pass and cast plugs both went scoreless into visibly feeding fish; going back to a dead flying fish under the kite is what converted | `species/bluefin-tuna.md` (`mDmbGdQAy-4`) |
| **You want the highest-percentage single presentation on a big-fish boat** | One charter captain ranked **kite-fished frozen dead flying fish as producing the majority of his boat's bites**, ahead of an artificial "California flyer" under the same kite | `species/bluefin-tuna.md` (`ouBrIdO7d4k`) |

The kite's floor is grade, not just wind: the *Searcher* carries three dedicated kite outfits but **only fishes them once 100 lb+ bluefin are confirmed around** — as of that 2021 seminar the crew hadn't needed to fly them yet that season (`techniques/kite-fishing.md`, `fgTmUq78ofQ`).

**Honest counter-data point:** at the 2024 Baja Blue Fin Tournament out of Ensenada, a kited flyer drew a swirl that wouldn't commit and the boat landed nothing across two days despite kite and spreader-bar effort in a zone with confirmed sign (`species/bluefin-tuna.md`, `Ix0gG0-l3v0`). The kite is the best tool for that grade; it is not a guarantee.

## When the flyline wins instead

- **Chummed up / picky on bait** — flyline a sardine on a circle hook and scale the leader down; **40–60 lb class**, circle hooks size 1–2/0 (`species/bluefin-tuna.md` situations table).
- **Volume daytime bite** — one deckhand's trip log put **~90% of daytime bites on the flyline**, fished on a dedicated **25–30 lb fluorocarbon flyline stick**, majority on **size 2 circle hooks** (size 1 to 1/0 also used); the other daytime bites were 2 on a sinker rig and 1 on a Colt Sniper (`species/bluefin-tuna.md`, `149px8WQ2Ng`).
- **Fish that refuse anything but bait** — a June 2023 El Dorado day bit **strictly on flyline**; the sinker rig got nothing. 25–40 lb test to a straight No. 2 hook, sardine (`techniques/flyline.md`, `oB4BpIUTTl4` / `r4J5nP5Bkl4`).
- **Finicky 40–60 lb grade** — the fix is thinner, not heavier: **20–25 lb test**, because a bait on heavy line doesn't swim right (`techniques/flyline.md`, `icpm7gADxvU`; mechanism from `48ZFXnCTTQE`).
- **They are not mutually exclusive.** At a Cortez Bank sundown 100 lb+ bite, two kite hookups were filmed alongside fish converted on flyline gear in the same window (`techniques/kite-fishing.md`, `zBd1mayUt_I`), and the kite was also flown during a hot morning bite earlier in that trip alongside bait rods (`QSvzVHW9UMk`). Capt. Dave Hansen runs the two together as a deliberate **kite/flyline volume program**, chosen specifically *against* flat-fall fishing — his stated math is six fish landed in the time a flat-fall boat lands one (`species/bluefin-trolling.md`, `JiJYamo0QHk`).

## The wind rule — flagged, because the KB keeps two versions side by side

The KB does **not** reconcile these, and says so explicitly:

- **Router version:** kite at **8–15 kt**; when it's **too light to kite (under ~8 kt), or the fish are too spread out to sit and kite over**, speed-troll a Mad Mac at **13–15 kt** to locate (`species/bluefin-trolling.md`; the "too spread out" half is cameron's reading — a coverage need, not sea state).
- **Hansen's flyer-specific version:** at **~8 kt of wind or more, troll a rubber flyer at ~8.5 kt** under the kite to search (better bite-to-hookup ratio than sitting); **under ~8 kt with fish already spotted or marked heavy, go dead-boat** with (typically two) dead flyers under the kite or a balloon (`techniques/kite-fishing.md`, `2y0VznL2qk8`).

Same ~8 kt number, opposite directions — one says light wind ends the kite, the other says light wind changes how you fish the kite. Different lure, different speed (8.5 vs 13–15 kt). Treat it as two frameworks and pick by whether you already have fish located.

---

## The kite setup

**The fighting outfit** — a dedicated **150–200 lb class** rod, ~100 lb braid for capacity and less wind-blow; it never casts (`species/bluefin-trolling.md`, `tackle/gear-classes.md`). Real outfits in the corpus:

- **Searcher's kite program:** three setups — **Accurate ATD 50** on **Seeker 2x4** rods, **200 lb spectra tied straight to 400 lb mono** (`fgTmUq78ofQ`).
- **Long-range kite/fighting rod:** **Shimano Tiagra 50 Wide**, 200 lb line, a **15 ft top shot of 135 lb mono over 200 lb braid**, on a **7'6", 80–200 lb unlimited-class rail rod** built so a big fish can be fought off the rail; **500 lb ball-bearing swivel** joins the top shot to the harness leader. General statement in the same talk: kite main line wants roughly **1,000 yd of 130–200 lb mono** (`RM7cBgCDWFA`).
- **Hansen's program:** **200 lb braid → 400 lb fluorocarbon**, fished with **40 lb of drag** (`JiJYamo0QHk`).
- **Budget floor:** an **80 lb-class two-speed** at minimum if bringing your own; or **100 lb top shot on a big heavy rail rod** (`shZCjX2-fkI`, `lf3S28nh-kk`). A 2021 Fisherman's Landing rental kite outfit was a **7 ft Calstar 770XH + Shimano Talica 25 two-speed, 80 lb** (`shZCjX2-fkI`).

**The bait — flying fish harness** (`rigging/flying-fish-harness.md`):
- Skewer behind the shoulder just above the spine; wings pinned open with zip ties at **about 45°** — set further out and a swell knocks the bait off its presentation (`YsiHziY_PWw`).
- Body skewer in through the mouth, pushed ~3/4 in, lift the tail as you finish so it sits **slightly tail-down**; a final skewer pins the mouth shut so it doesn't scoop water.
- **Leader: 200–400 lb mono, typically 400** (`GqcVaTIlyg0`). **Bite leader 3 ft, 3.5 ft absolute max** (`YsiHziY_PWw`) — any longer and the swivel hits the rod tip before the fish is in gaff range. Corroborated at 3 ft of 400 lb (`RM7cBgCDWFA`).
- **Hooks:** big J with a trailing treble stinger set behind the body stick under the spine. Sizes cited: **9/0–12/0 J** (Owner) with a **5X-strong treble**; **12/0 stainless Mustad + treble** in the Searcher program; **5/0 5X-strong Mustad** treble from `YsiHziY_PWw`. **Conflict kept open:** Hansen runs a **single hook, no treble** — his own departure from the standard San Diego rig, not a correction of it (`JiJYamo0QHk`).
- **Rig 10–12 flyers for a four-angler day** and store them neatly in the cooler. Field simplifications on the wing lock: popsicle stick stapled on (`usHl-4SfqDA`), rubber band instead of a zip tie (`Ix0gG0-l3v0`), or **30–50 lb braid tied through the wing** with a locking third knot (`2TmLaSCmfC8`).

**The kite line and release** (`techniques/kite-fishing.md`):
- Kite flies on its own dedicated line — **straight braid, no separate leader**, spooled out to **a couple hundred yards**; run **120–150 yd** out was the working number on one 22 ft center console, and that distance shifts with wind, drift, and boat heading (`rsCAh-QyK60`).
- **Kite height:** as high as you can go and **still see the flyer skipping** — bait visibility sets the ceiling, not a fixed number (`rsCAh-QyK60`).
- **The breakaway:** thread a small ring onto the fishing line *before* tying the snap swivel, then rubber-band that ring to the kite line's release clip. No knot ties fishing line to clip; the rubber band is the weak link (`Ix0gG0-l3v0`).
- **Quick release** on the kite line: loop the line and flip it onto the clip mechanism rather than knotting it. **Pay out by loosening the star drag** on the kite reel instead of thumbing the spool (`Ix0gG0-l3v0`).
- **Balloon-to-kite:** balloon twists into its own clip (no knot), clip rubber-bands to the kite, backed up by ~three tape-wrapped line tethers so a popped rubber band doesn't cost you the kite and balloon (`vCskOx6N-XM`).
- **Gyro-stabilized binoculars called mandatory** — for spotting fish *and* for watching the flyer stay upright and skipping (`Ix0gG0-l3v0`; general doctrine in `planning/search-and-glassing.md`).

**The presentation — this is where the technique is won or lost:**
- Set the clip so the **flyer just touches down** — skipping and splashing, never dragging under, never flying clear through the air. Flying it like a kite instead of skipping it wave-to-wave is flagged on camera as the common angler mistake: the fish are in the water, not the sky (`JiJYamo0QHk`).
- **Dapping** is the whole trigger — constant surface contact, bouncing with the swell, watched continuously through binoculars.
- **Speeds:** trolled rubber flyer at **~8.5 kt** (`2y0VznL2qk8`, restated in `JiJYamo0QHk`); one crew called **8 mph (~7 kn)** on the GPS working a kited spread (`rsCAh-QyK60`); another worked the spread slowly at roughly **2 kt on a single center engine** while searching (`Ix0gG0-l3v0`).

**The bite, the set, the fight:**
- On the eat the line **pops out of the release clip** and you come tight directly to the fish — no clip in the fighting system.
- **Dead-boat hookset:** the take is a surface explosion; put the boat in gear and drive **forward gently, ~4–5 kt, not a hard throttle**, to load the rod without shock-loading it (`2y0VznL2qk8`).
- **Fight:** boat-driven gear-tap at **~8 kt** — out of gear when line peels, back in the instant it stops; rod stays in the holder. **130 lb+ braid** minimum on this program, and Hansen deliberately fishes **one hooked fish at a time** so two cows can't death-circle at once (`techniques/fighting-big-bluefin.md`, `JiJYamo0QHk`, `xzIaUEDklrE`). One kite-hooked fish in the corpus took **40–45 minutes** (`zBd1mayUt_I`).
- **Gaff:** lay the short leader flat on the surface to bring the fish into range at the swivel — this is why the 3–3.5 ft leader limit exists.

**Alternative kite baits** if you don't have flyers: **live mackerel, back/dorsal-hooked** right in front of the dorsal — that placement is *kite-only*, and it makes the bait sit flat and flutter on each touchdown without the leader dragging where a leader-shy tuna sees it (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`). On Baja long-range for giant grade, whole **squid on a double-hook rig** under the kite, left to drift (`pk2blktDQ9Y`). Hard-bodied artificials — the "California Flyer" slides up the leader on a hookup so it survives to be reused (`rigging/flying-fish-harness.md`, `vCskOx6N-XM`).

## The flyline setup, for the comparison

- **Class:** 40–60 lb, circle hooks 1–2/0; a first-time big-fish build wants **400+ yd of line, 80 lb backing, 50–60 lb mono top shot, ~3 ft of fluoro** (`species/bluefin-tuna.md`).
- **Hansen's mackerel rig, stripped to the minimum:** thick-wire Mustad **circle hook tied straight to 3–4 ft of 80 lb fluorocarbon** with a San Diego jam knot — no weight, no swivel, no beads. Mackerel nose-hooked, thrown right into the foamer. Short on purpose so the knot doesn't sit past the tip guide on the cast (`techniques/flyline.md`, `RbqOKkINSCM`). He switches to circles **specifically for big bluefin** because their teeth saw through leader and a corner-of-mouth hookset keeps the leader out of them.
- **Finicky-bite rig:** **25 lb mono top shot → 2–3 ft of 50 lb fluoro bite guard**, joined with a Seaguar knot. The 25 lb is what pulls through the water so the bait swims like it's on 25; the heavy short section takes the abrasion inside the mouth. Stated personal best on that setup: **~100 lb** (`techniques/flyline.md`, `48ZFXnCTTQE`).
- **Two-rod system:** light stick 8 ft rated 20–50 lb with a 30 lb mono top shot for **20–50 lb grade**; heavy stick 7 ft rated 30–80 lb running **40 lb (sometimes 50)** direct, for bigger fish (`techniques/flyline.md`, `jQW2HLkMsmY`).
- **Rod material matters:** graphite tips whip-crack the bait off or stun it; a slow-taper **glass or composite** loads gently and the bait lands lively (`techniques/flyline.md`, `48ZFXnCTTQE`).

## If the wind won't fly the kite

1. **Speed-troll a full-size Mad Mac at 13–15 kt** to cover water and locate (`species/bluefin-trolling.md`; Nate Winnicki / BD). Note the practical ceiling: a SoCal *sportboat* tops out around 9 kt, so this is a private-boat technique (`bM2vUS1B-yQ`).
2. **Helium-balloon assist** is the general light-wind fix for holding a kite up (`techniques/kite-fishing.md`).
3. **The "life jacket" flyer** — a kite-free, balloon-free option: toothpicks pinning the wings open, a **pool noodle cut in half lengthwise** fitted over the fish's back so it floats on its own. Fish it on the slide or dropped off the bow. Named as especially suited to private boats; the stated trade-off is it must be built ahead of time, not deployed on the fly (`rigging/flying-fish-harness.md`, `QHY5kmU7OTU`).

## Against your profile

Your designated kite rod is the **Fathom 80 setup** — 7–7.5 ft XXXX-H, 150–200 lb, Penn Fathom II 80LD2 two-speed (50 lb max drag), **~1000 yd of 100 lb braid**, currently spreader-bar-only and never casts, listed as the future kite rod with 100 lb braid kept for capacity and less wind-blow, 200 lb leader (`profiles/cameron/rods.md`). That braid is lighter than the 130–200 lb the corpus kite programs run — worth knowing before a 200 lb fish tests it. You started kite fishing **July 2026** and **ruled out a helium-balloon assist** — too expensive, no room for a tank on the panga (`species/bluefin-tuna.md`). That's a platform constraint, not a rule of the fishery: it means your light-wind kite window stays closed and the sub-8 kt answer for you is the speed-troll or the noodle-float flyer, not the balloon.

## What the KB does not cover

Listed below in `gaps_admitted` — the main ones are that no note names a kite model or a wind-rating by kite size, no note gives a kite-line pound test, the ~8 kt wind mark is left deliberately unreconciled between two frameworks, and there is no controlled kite-vs-flyline hookup-rate comparison anywhere in the corpus.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/kite-fishing.md`, `techniques/flyline.md`, `techniques/fighting-big-bluefin.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `rigging/flying-fish-harness.md`, `bait/fishing-live-bait.md`, `tackle/gear-classes.md`, `profiles/cameron/rods.md`  
*videos:* `YsiHziY_PWw`, `GqcVaTIlyg0`, `JiJYamo0QHk`, `2y0VznL2qk8`, `w5_x6kkN-xE`, `fgTmUq78ofQ`, `RM7cBgCDWFA`, `lf3S28nh-kk`, `shZCjX2-fkI`, `rsCAh-QyK60`, `Ix0gG0-l3v0`, `vCskOx6N-XM`, `usHl-4SfqDA`, `zBd1mayUt_I`, `QSvzVHW9UMk`, `mDmbGdQAy-4`, `ouBrIdO7d4k`, `pk2blktDQ9Y`, `2TmLaSCmfC8`, `QHY5kmU7OTU`, `RbqOKkINSCM`, `48ZFXnCTTQE`, `icpm7gADxvU`, `149px8WQ2Ng`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `jQW2HLkMsmY`, `xzIaUEDklrE`, `bM2vUS1B-yQ`, `cameron`  
*gaps admitted:* No note names a kite model, size, or a wind-rating by kite size — the KB only gives wind bands (~8-15 kt), never which kite to fly in which wind. | No pound test is given for the kite line itself — only 'straight braid' and 'a couple hundred yards' spooled out. | The ~8 kt wind mark is used in two opposite directions (trigger to troll under the kite vs. trigger to abandon the kite and speed-troll) and the KB explicitly leaves the two frameworks unreconciled. | No controlled or quantified kite-vs-flyline comparison exists in the corpus — only attributed rankings ('majority of the boat's bites') and single-session observations. | Whether a hand-inflated or helium balloon flown with a kite adds lift or just serves as a visual marker is flagged as unresolved in the KB. | No sea-state / swell ceiling is given for kiting beyond 'fishable swell' — the KB gives no wave-height number at which the kite stops working. | No source covers kiting for school-grade bluefin (roughly 30-80 lb); the kite is documented only for the 100-300 lb grade, so the KB cannot say whether it underperforms a flyline on smaller fish. | The 2-4 oz sliding sinker added to a kite-flown bait (Alijos Rocks, jH0q4UPjwC0) is a single, self-described untested mention with no leader position, hook, or bait species given. | The 'mandatory' ~30 ft tagline seen during Baja tournament kite prep is unresolved on the audio and is not confirmed as any jurisdiction's regulation. | No drag-setting number is given for the flyline outfit specifically (the kite side has Hansen's 40 lb); flyline drag guidance in the notes I read is qualitative only. | The KB gives no guidance on how many kites/flyers to fly at once beyond 'typically two' dead flyers on a dead-boat drift and Hansen's one-hooked-fish-at-a-time rule.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Kite vs. flyline for bluefin

**First, a caveat about how solid this is.** No source in the corpus compares the two head-to-head on the same fish. The KB adjudicates *kite vs. troll* explicitly (`species/bluefin-tuna-trolling.md`), but the kite/flyline boundary has to be assembled from two separate statements that live in different notes. I've flagged where the seam is.

Also: you gave me no date, launch point, wind or SST, so I have not pulled conditions and I'm not calling a zone or a day. This is the decision rule and the build.

---

## When the kite beats a flyline

The kite is a **grade + wind + located-fish** call, and all three have to be true.

**1. Grade is 100–300 lb.** `species/bluefin-tuna.md` routes "Big fish 100–300 lb" to the kite and calls a flying fish under a kite *the* most effective method at that grade; `species/bluefin-tuna-trolling.md` states it the same way — "the most effective way to catch 100–300 lb SoCal bluefin is a flying fish under a kite" (`YsiHziY_PWw`). Every kite citation in the KB is scoped to that class. The Searcher reserves its kite gear for **confirmed 100 lb+ fish** and hadn't needed to fish it at all through the 2021 season as of that May seminar (`fgTmUq78ofQ`).

**2. There's enough wind to fly it.** `techniques/kite-fishing.md` — marginal, gusty or dying wind makes the flyer inconsistent on the surface, and that is the cue to switch to `techniques/speed-trolling.md`, which needs no wind.

**3. The fish are located and concentrated enough to sit over.** Foamers or high sounder marks. **Never deploy a dead flyer speculatively over blind water** — it's fished over confirmed sign (`2y0VznL2qk8`). The hand-off is explicit: once the sounder marks good numbers, stop trolling and set a dead flyer under the kite to fish the drift over the marks (`vCskOx6N-XM`).

Two secondary reasons the kite wins:

- **Leader-shy fish.** A back/dorsal-hooked live mackerel off the kite sits flat on the surface and flutters, **without the leader dragging through the water where a leader-shy tuna can see it** (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`). No bait presentation in the water can do that.
- **Volume.** One SoCal kite program says it lands **six fish in the time a flat-fall boat lands one** (`JiJYamo0QHk`). Read that carefully — it's against flat-fall, not flyline, and the KB flags that the source states it as a goal ("we want to catch six in the time you catch your one"), not an achieved rate.

## When the flyline beats the kite

- **No wind.** The kite is simply unavailable; `species/bluefin-tuna-trolling.md` gives the towed presentation as the answer for a big-fish day with no wind, not the flyline.
- **Grade is 40–60 lb and the fish are picky.** This is the flyline's own row in the router ("chummed up / picky on bait"), and `techniques/flyline.md` is blunt about the mechanism: bluefin grading **40–60 lb stop biting because the bait can't swim heavier line** — drop to **20–25 lb test** so the bait looks livelier (`icpm7gADxvU`, `48ZFXnCTTQE`).
- **Fish are down, not up.** Bait fished **80–100 ft** down to fish holding off the chum line is a butt-hooked flyline job (`oB4BpIUTTl4`/`r4J5nP5Bkl4`); fish off the top on an offshore drift at **50–100 ft** the same (`8THSuqoPI_Q`).
- **Raw daytime bite count.** About **90% of one boat's daytime bites** on an overnight trip came off flyline, on a dedicated **25–30 lb fluorocarbon** stick with a **size 2 circle hook** (`149px8WQ2Ng`). That's a boat total on a trip, not a kite comparison.

**They are not mutually exclusive.** One Cortez Bank sundown 100 lb+ bite converted fish on **both** — two kite hookups filmed plus additional fish on flyline gear fished alongside the kite in the same window (`zBd1mayUt_I`). The realistic call on a big-grade day is kite up *and* bait in the water, not one or the other.

### The wind numbers are contradicted inside the KB — know this before you plan around them

The router's kite row says **wind ~8–15 kt**. The KB itself flags that figure:

- `techniques/kite-fishing.md` states **no wind numbers at all** in its wind-window section.
- `species/bluefin-tuna-trolling.md` flags that `z1CmWHqe9uk` (the speed-troll cite) states no wind figure at all, and that `2y0VznL2qk8` **flies a kite under 8 kt** — so ~8 kt is a presentation split inside a kite program, not a floor below which the kite won't fly.
- Separately, `species/yellowfin-tuna.md` names **calm water** as its kite trigger — the exact condition the bluefin notes treat as the failure mode. `techniques/kite-fishing.md` carries that as an open contradiction.

Treat 8–15 kt as a rough working band with a disputed floor, not a threshold.

---

## The setup

Region/waters gate first: kite fishing is `regions: socal-bight, baja-pacific-north, baja-pacific-south`, `waters: open-ocean, bank`. This is a bank/offshore call — it never surfaces for an island-only or nearshore day.

### Rod, reel, line

| Piece | Spec | Cite |
| --- | --- | --- |
| **Rod** | **7 ft 6 in, rated 80–200 lb-plus (unlimited class)**, built as a rail rod, so a big fish is fought off the rail without breaking the rod down | `RM7cBgCDWFA` |
| | Searcher's three dedicated kite setups: **Seeker 2x4** rods | `fgTmUq78ofQ` |
| | Rental/lighter tier: **7 ft graphite Calstar 770XH** rail rod | `shZCjX2-fkI` |
| **Reel** | **Two-speed conventional, 50-class** — Accurate ATD 50, Accurate twin-drag, **Shimano Tiagra 50 Wide**; an Okuma Makaira 50 Wide observed on a kite/fighting outfit | `fgTmUq78ofQ`, `lf3S28nh-kk`, `RM7cBgCDWFA`, `usHl-4SfqDA` |
| | Rental-grade alternative: **Shimano Talica 25** on **80 lb**. Personal-outfit floor: an **80-lb-class two-speed** at minimum | `shZCjX2-fkI` |
| **Main line** | **130–200 lb braid/spectra.** Either **200 lb spectra tied straight to 400 lb mono**, or a **~15 ft top shot of 130–200 lb mono** (one Tiagra 50W: 15 ft of 135 lb mono over 200 lb braid). Another program: 130 lb braid, personal minimum **100 lb top shot** | `fgTmUq78ofQ`, `RM7cBgCDWFA`, `lf3S28nh-kk` |
| | Hansen's own kite program: **200 lb braid → 400 lb fluorocarbon, 40 lb of drag** | `JiJYamo0QHk` |
| **Connection** | **500 lb ball-bearing swivel** joins top shot to the harness leader | `RM7cBgCDWFA` |
| **Bite leader** | **200–400 lb mono, typically 400.** Length **3 ft, 3.5 ft max** — any longer and the swivel hits the rod tip before the fish is in gaff range | `GqcVaTIlyg0`, `YsiHziY_PWw` |
| **Hooks** | **9/0–12/0 J hook (Owner) + trailing 5X-strong treble stinger**; a **12/0 stainless Mustad** J + treble is one documented spec; tail treble also given as **5/0 5X-strong Mustad** | `RM7cBgCDWFA`, `fgTmUq78ofQ`, `YsiHziY_PWw` |

**Hook-count is unresolved doctrine, and the KB calls it a program choice, not a conditions call.** Most SoCal boats run J-plus-trailing-treble; Hansen's boat runs **single hook, no trebles** (`JiJYamo0QHk`, `rigging/flying-fish-harness.md`).

Reel picks split on **budget, not capability** — a higher tier (Accurate, Talica) against a workhorse tier (Penn International, Tiagra); all named reels are called adequate for the job (`shZCjX2-fkI`).

### The flying fish harness (`rigging/flying-fish-harness.md`)

- **Wing skewers:** one behind the shoulder just above the spine; a second through a hole between the ribs and the wing at the position you want the wing to sit. Hold the wings open with **zip ties** through additional holes both sides and cinch everything tight — slippage along the skewers during deployment kills the action (`GqcVaTIlyg0`).
- **Wing angle: about 45°.** Set further out, a swell knocks the bait off its presentation (`YsiHziY_PWw`).
- **Body skewer:** in through the mouth, down the middle of the fish, pushed about **three-quarters of the way in**; lift the tail as you finish so the bait sits slightly down-and-tail-in-the-water (`GqcVaTIlyg0`).
- **Mouth skewer:** pin the mouth closed — stops water being scooped through the lower lip and out the roof of the mouth, and the bait presents longer (`GqcVaTIlyg0`).
- **Stinger placement:** treble into the back, just behind the body skewer, under the spine and out the other side (`GqcVaTIlyg0`).
- **Quantity: rig 10–12 flyers for a four-angler day**, stored in the cooler ready to deploy (`GqcVaTIlyg0`).
- **Field alternatives to zip ties:** staple a popsicle stick to the bait (`usHl-4SfqDA`); a rubber band (`Ix0gG0-l3v0`); or **30–50 lb braid** through the wing hole and around the skewer — overhand knot twice plus a **third locking knot** or the wing knot slips, wing holes punched at the **second or third bone in** from the edge, flyer rigged **partially thawed, not fully thawed** (`2TmLaSCmfC8`).

### The kite line itself (`techniques/kite-fishing.md` + its evidence file)

- The kite flies on its **own dedicated line, separate from the fishing line**. A **ring** on the fishing line ahead of the terminal tackle carries a **rubber band** to the kite line's release clip — no knot joins the fishing line to the clip, so the rubber band is the weak link that lets the fishing line pop free on the bite (`Ix0gG0-l3v0`).
- Kite-line build detail from that same program: a **loop-flip quick release** on the kite line, **star-drag payout control** rather than thumbing the spool, a knot marking **~75 ft** out during payout (function unresolved on the audio), a heavy-duty snap swivel (don't over-crank it), **straight braid with no leader section**, roughly **a couple hundred yards** spooled out once set, boat run on a **single center engine at ~2 kt** while working the spread, and **gyro-stabilized binoculars called mandatory** — both for spotting fish and for watching the flyer stay upright (`Ix0gG0-l3v0`). That tournament also called a **~30 ft tagline** mandatory (attachment point unresolved; read as its own boatside-handling rule, not confirmed as a regulation).
- **Kite run: 120–150 yd out**, shifting with wind, drift and the boat's heading relative to kite height (`rsCAh-QyK60`).
- **Height: as high as the crew can still see the flying fish skipping** — visibility, not a fixed height, sets the ceiling (`rsCAh-QyK60`).

### Working the bait

- Adjust the clip and kite so the flyer **just touches the surface** — it skips and splashes on top, never drags under, never flies clear of the water.
- The common mistake is **flying the bait through the air** rather than skipping wave-to-wave: the fish are in the water, not the sky, so the bait has to stay in **constant contact with the surface** to draw a strike (`JiJYamo0QHk`).
- **Deploying a dead flyer:** drive forward a little to open distance between boat and bait, then lower the flyer slowly onto the surface and keep it **dapping** — bouncing with the swell, never submerged, never airborne (`2y0VznL2qk8`).

### The wind-driven sub-decision inside the kite program (`2y0VznL2qk8`)

- **~8 kt of wind or more → troll a rubber flyer** (the "Yummy Flyer") under the kite at **~8.5 kt**. Trolling covers more water while searching and converts a bite to a hookup at a better ratio than dead-boat fishing. Once a school is raised, mark it on the GPS and keep working it.
- **Under ~8 kt with fish already located → go dead-boat with a dead flyer**, typically **two** of them, under the kite or a balloon, drifted like float fishing.

### The bite, the hookset, the gaff

- On the eat, the line **pops out of the release clip** and you come tight directly to the fish — no clip in the fighting system.
- **Dead-boat hookset:** the take is a surface explosion on the flyer. Put the boat in gear and drive **forward gently — about 4–5 kt, not a hard throttle** — to keep the rod bent and constant pressure on as the fish takes off, driving the hook home without shock-loading it (`2y0VznL2qk8`).
- **Lay the short leader out flat on the surface** to bring the fish into gaff range at the swivel. A leader run too long stops the fish short of the gaff.
- Budget the time: a kite-hooked 100 lb+ bluefin has been fought **40–45 minutes** before landing (`zBd1mayUt_I`) — the KB flags that figure as ASR-garbled in the source, so treat it as approximate.
- **The fight is boat-driven** (`techniques/fighting-big-bluefin.md`): rod stays in the holder, **tap in and out of gear** — out the moment line peels, back in the instant it stops — which draws the fish toward the boat rather than letting it take drag. **No reason to fish bluefin under 130 lb spectra/braid minimum**, whichever fighting style. Hand-fighting in a harness at **30–40 lb of drag** is an endurance choice, not a functional advantage (`8jC61LzQoxU`). On a **20–30 ft** boat specifically: leave the rod in the holder, turn in **big gentle circles** (not tight spins), keep the fish pinned on **one side**, **drive forward only, never reverse**, holding roughly **45°** to the fish (`Q196GVwVqro`).

### Bait alternatives under the kite

- **Default:** pre-rigged **dead flying fish** on the harness. Frozen dead flyers produced the majority of one charter's bites, ahead of a "California flyer" artificial under the same kite (`ouBrIdO7d4k`).
- **Live mackerel, back/dorsal-hooked** — right in front of the dorsal, a hard spot that holds the hook. Simpler live-bait alternative for the same 100–300 lb grade; also drew yellowtail and calico bass off the kite (`w5_x6kkN-xE`).
- **Whole squid on a double-hook rig** for giant-grade tuna, left to drift with current and wind (`pk2blktDQ9Y`). No hook size, spacing or leader weight given.
- **Artificials:** the trolled rubber "Yummy Flyer"; the **"California Flyer,"** which slides up the leader on a hookup so it isn't damaged and can be reused, with replaceable wings (`vCskOx6N-XM`).
- **One unreconciled report** adds a **2–4 oz sliding sinker** ahead of a kite-flown bait, on secondhand reasoning that it keeps the bait in the water better — offered as untested by the speaker himself, and it stands against the bare-flyer dapping doctrine (`jH0q4UPjwC0`). I'd not build around it.

### Light wind: helium

The general fix for holding a kite up in light wind is a **helium-balloon assist** — the balloon twists into a dedicated clip with no knot, the clip rubber-bands to the kite, and a taped fishing-line tether backs up that rubber band so a failure leaves balloon and kite cradled together instead of lost (`vCskOx6N-XM`). **Whether a balloon adds lift or is only a strike marker is explicitly unsettled in the KB** — one report flies a rubber flyer under a balloon without saying whether a kite was up (`wYeKJLoKo4g`), another flies a balloon *together with* the kite in fishable wind (`usHl-4SfqDA`).

### Common failures (`techniques/kite-fishing.md`)

- **Wings set too far out** — a swell knocks the bait off and ruins the presentation.
- **Leader too long** — the fish hits the swivel before it's in gaff range.
- **Letting the flyer sink or drag** instead of skipping — the splashing surface contact is the whole trigger.

---

## The flyline build, for when that's the call instead

So you have the other half in hand:

- **Picky bite, 40–60 lb grade:** **20–25 lb test, no more than 30**. The fix for light leaders breaking is a **25 lb mono top shot to a 2–3 ft section of 50 lb fluorocarbon**, joined with a Seaguar knot — the 25 lb mono is what pulls through the water so the bait swims like it's on 25 lb, while the short heavy fluoro rides inside the mouth and along the teeth (`48ZFXnCTTQE`, `techniques/flyline.md`).
- **Boat-side foamer on mackerel:** a **thick-wire Mustad circle hook tied straight to 3–4 ft of 80 lb fluorocarbon** with a San Diego jam knot — no weight, no swivel, no beads — mackerel nose-hooked, thrown into the foamer (`RbqOKkINSCM`). Kept side by side with the light-line philosophy above, not reconciled: different bait, different situation.
- **Two-rod system:** light stick 8 ft rated 20–50 lb / Torium 16 / **30 lb mono top shot, 50+ yd** for 20–50 lb grade; heavy stick 7 ft rated 30–80 lb / Trinidad 20A / **40 lb (sometimes 50)** run directly for bigger fish (`jQW2HLkMsmY`).
- **Depth mechanism worth knowing:** at 200 ft back, braid + a 10 ft fluoro top shot holds the bait only **10–12 ft** down; straight mono at the same distance puts it **50–60 ft** down. That matters for bluefin that won't come to the surface — rig at least one rod with **50+ yards of mono** (`48ZFXnCTTQE`).

**Line-class conflict, flagged and unresolved in the KB:** `species/bluefin-tuna.md` routes its picky-fish row to the **40–60 lb class** with 1–2/0 circles; `techniques/flyline.md` caps it at **20–25 lb, no more than 30**; `tackle/gear-classes.md` calls 12–30 lb the finesse fly-line class. The decision frame that actually works from the notes: line weight follows **the bait and the bite**, not the fish.

---

## Against your own boat and rods

From `profiles/cameron/rods.md` and `profiles/cameron/boat.md` — kite fishing for bluefin is listed as a program in progress (started July 2026), so this is the gear read:

- **Your designated kite rod is the Fathom 80 setup** — Okuma PCH-C-741XXXXH (**7'4", XXXX-H, 150–200 lb**) with a Penn Fathom II 80LD2 two-speed (**50 lb max drag**), ~**1000 yd of 100 lb braid**. The rod rating sits squarely in the documented kite class. The 50 lb max drag comfortably covers the **40 lb** Hansen runs (`JiJYamo0QHk`). It's the one rod of your eight that has never caught a bluefin.
- **Gap — main line.** Your 100 lb braid is below the **130–200 lb** every dedicated kite program in the corpus reports, and below the **130 lb spectra minimum** stated for fighting big bluefin at all (`8jC61LzQoxU`). Your own profile note already flags the 100 lb as possibly light. The one nearby data point in your favour: a personal-outfit floor of **100 lb top shot** (`lf3S28nh-kk`) — but that's a top shot over 130 lb braid, not the main line.
- **Gap — everything else in the kite system.** The profile records **no kite**, no flying fish or harness materials (skewers, zip ties), no 500 lb ball-bearing swivel, and no 12/0 J or 5/0 treble hooks. That's the shopping list, not a substitution.
- **Helium is out on your platform.** Too expensive and no room to carry a tank on the panga (cameron, `techniques/kite-fishing.md`) — a constraint of your setup, not of the fishery. On a bigger boat with room for a tank the light-wind window reopens. Practically: your kite window is wind-gated with no light-wind fix.
- **Sea-state tension nothing in the KB resolves.** `conditions/sea-state.md` gives a **12 kt personal cutoff for not running** (`NC3-3pJDEgo`) — which sits inside the top half of the router's 8–15 kt kite band. For a 22 ft panga that's a real conflict and no note reconciles it. Your `boat.md` has **`range_nm` and `sea_state_max_ft` null**, so the day-plan protocol's step-1b envelope can't be derived — I'd need those from you before calling whether a Tanner/Cortez or below-Clemente kite day is even inside your operating limits.
- **Your flyline side is already built:** the Avet MXJ on the Teramar 9'0" (30–65 lb, 50 lb braid) is your dedicated flyline rod, with the Trinidad 40 for heavy flyline and the Tranx as utility.

**Bottom line for your boat:** on a big-grade day with wind, the kite is the higher-percentage presentation and you have the rod for it — but the program is unowned gear and the braid wants a rethink. Until then, the router's honest answer for a located 100 lb+ school with no kite in the boat is speed-trolling a Mad Mac (`species/bluefin-tuna-trolling.md`), with bait in the water alongside.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `species/bluefin-tuna-trolling.md`, `techniques/kite-fishing.md`, `techniques/evidence/kite-fishing.md`, `techniques/flyline.md`, `techniques/fighting-big-bluefin.md`, `rigging/flying-fish-harness.md`, `bait/fishing-live-bait.md`, `tackle/gear-classes.md`, `conditions/sea-state.md`, `profiles/cameron/README.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`  
*videos:* `YsiHziY_PWw`, `2y0VznL2qk8`, `Ix0gG0-l3v0`, `rsCAh-QyK60`, `JiJYamo0QHk`, `zBd1mayUt_I`, `RM7cBgCDWFA`, `fgTmUq78ofQ`, `lf3S28nh-kk`, `shZCjX2-fkI`, `GqcVaTIlyg0`, `2TmLaSCmfC8`, `usHl-4SfqDA`, `vCskOx6N-XM`, `pk2blktDQ9Y`, `jH0q4UPjwC0`, `wYeKJLoKo4g`, `ouBrIdO7d4k`, `w5_x6kkN-xE`, `8jC61LzQoxU`, `Q196GVwVqro`, `48ZFXnCTTQE`, `icpm7gADxvU`, `149px8WQ2Ng`, `RbqOKkINSCM`, `jQW2HLkMsmY`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `8THSuqoPI_Q`, `gimFbgN5Jjk`, `z1CmWHqe9uk`, `NC3-3pJDEgo`  
*gaps admitted:* No corpus source compares kite and flyline head-to-head on the same fish; the KB only adjudicates kite vs. troll, so the kite/flyline boundary had to be assembled from the 100-300 lb kite grade statement plus the separate 40-60 lb picky-fish flyline statement. | The ~8-15 kt kite wind band is internally contradicted: the kite technique note carries no wind numbers at all, and the trolling note flags ~8 kt as unsupported by z1CmWHqe9uk and contradicted by 2y0VznL2qk8, which flies a kite under 8 kt. | No upper wind limit for kite fishing anywhere in the KB - nothing says what happens above 15 kt. | The KB gives no kite specification at all: no brand, size, square footage, or wind-rating-per-kite-size, and no guidance on which kite to buy. | No kite-line test rating or spool capacity spec beyond 'straight braid, no leader section, roughly a couple hundred yards'. | No numeric kite flying height - the only guidance is 'as high as the crew can still see the flyer'. | Nothing covers whether a kite is worth flying for sub-100 lb / schoolie-grade bluefin; every kite citation is scoped to 100-300 lb. | No guidance on running a kite and flyline rods simultaneously - spread management, rod count, keeping bait lines clear of the kite line - only the observation that both were fished in the same window (zBd1mayUt_I). | Kite hook count is unresolved doctrine (J-plus-trailing-treble vs Hansen's single hook, no trebles) and the KB calls it a program choice with no conditions test to pick between them. | Whether a balloon adds lift or is only a strike marker is explicitly unsettled across three sources (helium assist for light wind, balloon flown with the kite in fishable wind, stand-alone balloon with no kite). | The 2-4 oz sliding sinker on a kite-flown bait is single-source, self-described as untested, with no leader position, hook or bait species given. | No hook size, hook spacing or leader weight for the whole-squid double-hook kite rig. | No stated trigger for abandoning the kite - nothing on how long to soak a dead flyer over marks before switching. | The flyline line class for picky bluefin is contradicted between notes (router: 40-60 lb class with 1-2/0 circles; flyline note: 20-25 lb capped at 30; gear-classes: finesse fly-line class 12-30 lb) and the KB flags it without resolving it. | The Baja tournament's 'mandatory ~30 ft tagline' attachment point and mechanism are unresolved on the audio and unconfirmed as a regulation. | The 40-45 minute kite fight duration is flagged in the KB as ASR-garbled in the source clip. | Cameron's profile records no kite, no flying fish, no harness materials, no 500 lb ball-bearing swivel and no 12/0 J or 5/0 treble hooks - the kite program is unowned gear. | Cameron's boat.md has range_nm and sea_state_max_ft null, so the day-plan protocol's step-1b envelope cannot be derived; the 8-15 kt kite band overlaps the sea-state note's 12 kt run cutoff with no note reconciling them for a 22 ft panga. | Nothing in the KB covers kite-line handling or spread geometry in a small panga cockpit. | No flyer-consumption or deployment-count guidance beyond 'rig 10-12 flyers for a four-angler day'. | The question supplied no date, launch point, wind or SST, so no zone, timing or conditions call was made and no BightSST pull was performed. | No Mexican (CONAPESCA) bluefin bag/size limits or permit requirements for the Ensenada kite fishery - flagged as a gap in the species note.

</details>

### 13. [technique] How do I fish a drop-shot for calico bass along a kelp line?

**Winner:** NOW · mapping {'A': 'B2', 'B': 'B3', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three got the central fact right - the KB has no drop-shot doctrine for calico bass and not even a flagged stub row for one - so the separation is in what they recovered around the gap. C wins narrowly: it is the only answer that both reproduces the rig well enough to tie (Palomar tag length, point-up rule, three named hooks, weight/line pairings, retrieve cadences) and surfaces the one drop-shot-family rig the corpus documents around structure (weedless slug on an Owner twist-lock, ~2 ft leader, 1 oz torpedo, cast down sand channels between heads), then closes with an explicitly labeled substitution set; it also flags the KB's own internal contradictions and unverifiable figures rather than passing them on. B is a very close second and beats C on two things C lacks - the 14 in CDFW size limit with as-of and verify-current, and the warning that 'drop shot rig' means a different offshore deep-bait rig - plus the best line-class decision frame (leader abraded in the last 6-8 in, re-tie rule, Florentino's 30 lb floor and 'structure position matters more than line class'). A is honest and rich on kelp-line reads but never surfaces the nearest documented drop-shot variant, never applies the island/nearshore waters gate, and leans on unidentified 'Ep. 14' style cites.

- *B2 reasons:* found: correctly identifies techniques/drop-shot.md as halibut/spotty-scoped and the calico router as carrying no drop-shot row or stub. specific: full rig numbers (12-14 in Palomar tag, 6-10 in dropper, 1/4-2 oz, 8-12 lb with 1 oz), kelp line specs 50-65 lb braid / 60 lb fluoro vs 65/40, 50 ft to 25 ft edge band, 20-25 vs 10-12 casts. sourced: note paths plus ids (k4mD2d6C81k, EGKesj7V64M, KTsXdQXAnkU, 9xNhdu2aBqE), though several claims cite only 'Ep. 14 / Ep. 5 / Ep. 13' with no id. scoped: 14 in kelp bass with California/CDFW + as-of 2026-08 + verify-current; nothing mis-regioned, but it never applies the waters envelope (drop-shot note is not island-gated) so an island kelp line is treated the same as coastal. honest: states the gap up front, labels the light-leader carry-over as the part that gets you cut off, no relative time. actionable: strong kelp-line reads and alternatives, but never surfaces the one drop-shot-family rig documented near structure and offers no assembled build for the thing actually asked.
- *B3 reasons:* found: states the gap plainly, cites the front-matter waters gate, and surfaces the weedless-slug-on-a-dropper near-miss from the calico panel source. specific: line-class comparison table (10-12 lb vs 60/40/25 lb), 2 ft leader + 1 oz keel weight, Spin Shot #2, 3/8-3/4 oz keel hooks, 1.5 oz tube, 65-68 F, 0-8 ft and 20-100 ft bands. sourced: paths plus ids throughout (RUuPNpK0x-s, ZoIzpyyS9xw, 9xNhdu2aBqE, P6Slg6RQiXw, BPxE3xn3gAc, LqW32NSkObY). scoped: applies the bay-harbor/nearshore-coast vs island envelope as binding; 14 in with California/CDFW, as-of 2026-08, verify-current, and the older bag figure explicitly dated and flagged. honest: labels every assembled part as assembled, flags the 'green bass' passage as not a calico data point, and warns the offshore 'drop shot rig' is a different rig entirely. actionable: gives a defensible hybrid (rig geometry from the drop-shot note, 25-30 lb line floor from the calico side), the abrasion re-tie rule, and five real substitute presentations.
- *NOW reasons:* found: same correct gap call, plus the most complete recovery of adjacent material - the alternate weedless-slug drop-shot leader, the dead-bite improvisation doctrine, and the spotted-bay-bass row the KB itself flags as contradicting the technique note. specific: full tie sequence, hook options (O'Shaughnessy long shank, VMC Spin Shot #2, #2 mosquito), 1/4-2 oz with matched line, cylinder/tungsten, 45-degree grub retrieve, 2 ft leader + 1 oz torpedo, 7/0 3/8 oz vs 3/4 oz preferred keel heads, 6.2:1 reel, kelp-posture current table. sourced: dense ids and paths, and it names which cites the KB flags as miscited or unresolved. scoped: quotes locations/regions.md to draw the nearshore-coast vs island line and states the protocol consequence; no regulation asserted, so no unstamped legal claim - though it omits the 14 in minimum an angler needs. honest: strongest - surfaces the KB's own fact-check flags (miscited Spin Shot content, unverifiable 70-80 ft depth, uncited 50/25 ft band) and labels its closing build explicitly as inference the KB does not sanction. actionable: an angler can tie the rig, choose the substitution set, place it in the sand lanes between heads, and run the sourced swimbait program instead.

<details><summary>Full prompt</summary>

How do I fish a drop-shot for calico bass along a kelp line?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Straight answer first: the KB does not cover this

There is **no drop-shot doctrine for calico bass anywhere in this knowledgebase.** I checked all three places it would live:

- `techniques/drop-shot.md` is written entirely for **sand/bay bottom** — its own tags are `[drop-shot, halibut, spotted-bay-bass, bays, finesse, vertical]`, and its "Reach for this when" list names only [California halibut](species/california-halibut.md) buried in the sand and [spotted bay bass](species/spotted-bay-bass.md). Kelp and calico appear nowhere in it. Confidence on that note is `medium`, and all three of its sources (`k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`) are back-bay / halibut videos.
- The `species/calico-bass.md` **Situations → techniques** router has nine rows and **not one of them is a drop shot** — and it doesn't even carry a `⚠ Flagged stub` row for it, which under this KB's own rules means no source in the corpus has raised it as a calico method.
- The reverse map agrees: the only notes linking to the drop shot are `species/california-halibut.md`, `species/spotted-bay-bass.md`, `lures/bay-bass-plastics.md` and `tackle/gear-classes.md`.

So I can't hand you a sourced kelp-line drop-shot procedure. What I can do is give you (1) exactly what the KB's drop-shot mechanics are and where they'll fight you on a kelp line, and (2) what the KB actually prescribes for the presentation you're reaching for — a bait worked low and near-vertical on the kelp edge.

---

## 1. The drop-shot rig as the KB has it — and the kelp problem

From `techniques/drop-shot.md` (Nathan Winch / Rod Marquez per the note; `k4mD2d6C81k`, `1enjjFVcDG0`):

- Hook tied **up the line**, weight hanging **below on a tag end**, bait suspended a fixed height above bottom while the lead stays pinned to the deck.
- **Palomar knot**, leaving **12–14 in** of leader; then pass the tag back down through the top of the hook eye so the **hook points upward**. The note calls a hook not riding point-up "the single most common rigging error."
- Hook: **strong long-shanked forged J** (O'Shaughnessy style) so the plastic can't slide around.
- **Hook-to-weight distance 6–10 in** (Marquez) — sized to the halibut strike zone, on the logic that a predator won't burn energy chasing a bait 15 ft off but will commit to one 6–10 in up.
- **Weight 1/4 oz to 1 oz**, light when it's glassy; Marquez runs **1–2 oz** and matches line to it — **8–12 lb test with 1 oz**, **15–20 lb with 2 oz**.
- Bait: **4-in scented finesse fluke** (ZMan), hook exposed **toward the tail** on a Gamakatsu size 1 straight worm hook because halibut bite from behind; swap for a grub or small swimbait (`lures/bay-bass-plastics.md`).
- Retrieve: weight on bottom, bait just above, **shake it in place**. **Grub** = rod tip down at **45°**, constant retrieve. **Fluke** = twitch, reel the slack, twitch again.
- Hookset (Roman Castro, `EGKesj7V64M`, 2019-06-18; medium confidence): **never set into slack** — wind down and drop the rod to come tight first, *then* swing. A missed swing costs nothing, so swing on anything that doesn't feel like bottom.
- Mobility: **~20 minutes with no bite, move** — the fish may be only 20 yards off.

**Where that collides with a kelp line, on the KB's own numbers.** The whole rig above is specced at **10–12 lb leader with a light drag** on a **2000-size spinning reel** — the "light spinning class" in `tackle/gear-classes.md` (10–20 lb). The KB's kelp-bass line specs are three to six times that: `techniques/swimbaits.md` has Landesfeind at **50–65 lb braid on a 300-size reel with 60 lb fluorocarbon leader**, explicitly because "the leader gets braided up and chafed just from throwing it in the kelp"; Todd Klein runs **65 lb braid to 40 lb mono** for kelp-bed calico, cinched down tight (`9xNhdu2aBqE`, San Clemente Island, 2015-10-28; unregistered channel, medium confidence), and that note contrasts it against a 10 lb braid / 5 lb fluoro freshwater setup to make the point that the SoCal kelp game needs markedly heavier line. The same note carries Dave Hansen's fight rule: once bit, **set the hook and then wind — never pump**, because every drop of a pump gives a hooked calico the slack it uses to dive back into the kelp (`KTsXdQXAnkU`, 2019-06-05; repeated doctrine, high confidence).

The KB never reconciles those two — because it never puts a drop shot on kelp. **It gives you no heavy-leader drop-shot variant, no weedless drop-shot rigging, and no dropper length for rock or kelp.** Anything I told you about running 6–10 in of 10 lb leader through stringers would be me inventing it.

## 2. What the KB does prescribe for a low, near-vertical presentation on a kelp line

Two presentations in the corpus are the closest mechanical relatives of what you're after, and both are sourced:

**Pitch-and-sink at the kelp base** — `techniques/swimbaits.md`, "Depth and where you throw it" (Dave Hansen, Your Saltwater Guide, `KTsXdQXAnkU`, 2019-06-05; registered voice, single mention — medium confidence). Pitch a **1 oz black/gold leadhead** right at the **base of the kelp line** and let it **sink straight to the bottom**; the bite typically comes on that sink. He runs **25 lb fluoro** for this pitch — notably lighter than the 60 lb above, and the note keeps both side by side rather than reconciling them.

**Flipping / punching the canopy** — `techniques/swimbaits.md` and the matching router row in `species/calico-bass.md` (Aaron Martens with Capt. Benny Florentino, San Clemente Island, December 2013, `P6Slg6RQiXw`). A **heavy head flip**: a heavy leadhead pitched on a short, accurate cast — not a long cast — into **gaps in the kelp canopy itself**, where fish were sitting **up underneath the floating canopy**, working the dropped bait before eating it. The KB flags this explicitly as a **single-session observed data point, not established doctrine**, and no leader, hook or weight spec was given on camera.

Also in range: **lead-head swimbait sunk 70–80 ft** over structure for calico — fish holding up and feeding will rise to meet it (`techniques/swimbaits.md`). And when the current rages and the kelp is pulled under, the router's answer is to **switch to subsurface — sunk iron or leadhead** — not to keep working on top (`species/calico-bass.md`).

If you specifically want to sit still and work a vertical rig rather than cover water, the KB's stationary play on a kelp edge is **chum-and-anchor**: chum-bucket the spot, then reposition **up-current** and back the boat down onto it as the anchor sets — fish come out of the kelp and start biting as the anchor goes down (`species/calico-bass.md` router row, `RXNebDr4j7s`; execution in `techniques/chunking.md`).

## 3. Where on the kelp line to put it, and when

This part the KB is emphatic about, and it applies regardless of what you're throwing.

- **The edge is the spot.** Biting fish sit on the **up-current / leading edge** of a kelp head — "hit three or four sides of it and you know in two or three casts" (Ep. 14). Calico face **into** the current and ambush from the front, so a lure swept past the leading edge draws them out (Benny Florentino, `Rwy4MqeXCIU`). Fish the **edges and pinch-points** — leading edge, outside edge, isolated stringers off the main bed — **not the dense middle** (`locations/bass-structure.md`, `species/calico-bass.md`). A 2016 SWBA tournament day at San Clemente corroborates it: most fish sat right on the front, up-current edge, with bites falling off past it (`tJFSV3AcIdE`).
- **Current, not tide.** Calico are **current-driven and largely tide-indifferent** — the opposite of harbor spotties. Current running **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage and gets skipped (`species/calico-bass.md`, `conditions/current-structure.md`). Late-fall exception kept side by side: at San Clemente the bass wanted **off-color water with current running into the island**, using the dirt to ambush against structure (11/23/22).
- **Read the current off the kelp itself:** kelp **pulled 20 ft under** = raging current, surface presentations dead; **laid down** = strong; **resurfacing** = slacking, switch your presentation back (`locations/bass-structure.md`, `conditions/current-diagnostics.md`).
- **Depths.** Typical working depths run the **outside kelp edge ~50 ft in to ~25 ft**, and calico will rise **10–15 ft off 80–100 ft of reef** to eat a crankbait or sunk iron. They mark **tight to the kelp and structure edges and on hard bottom** — on the reef-to-sand transition and the outside kelp line, not roaming open water (`species/calico-bass.md`).
- **Bait picture:** a **solid, unbroken wall of bait usually has no predators on it**; **broken or harried bait** does (Ep. 5, `locations/bass-structure.md`).
- **Birds:** **cormorants diving *in* the kelp** = actively feeding = a calico tell, better than gulls inshore (`conditions/bird-reading.md`, via the calico router).
- **Water color:** a green-stained, near-opaque color with roughly **5–10 ft visibility** was called the preferred kelp-edge read — the stain gives fish "a place to hide" and makes them more comfortable feeding up in the open (`9xNhdu2aBqE`, San Clemente West End, 2015-10-28; medium confidence).
- **Moon:** on clear full-moon nights calico gorge after dark and **shut down by mid-morning** — bite early, then dead until late day. Plan coastal bass segments for first light or late afternoon on the full (`conditions/moon.md`, via the calico router).
- **Cover water.** Fish a bed **20–25 casts if you're getting bites, only 10–12 if you're not**, then move **100 ft or 100 yards** to the next patch of stringers. Beds re-bite, so come back later (Ep. 13, `techniques/swimbaits.md`). Note this is a much tighter leash than the drop-shot note's 20-minute rule, which was written for bay water.

## 4. Housekeeping

- **Legal size:** calico (kelp bass) minimum is **14 in** — California / CDFW, as of 2026-08 per the note; **verify current rules before you fish** (`species/calico-bass.md`, dave-hansen, `r6j5w40fVHI`, 2022-04-25).
- **Release handling:** grab them by the **lower lip** to control the fish for hook removal; before release, **rub your hands together to build a light lather and rinse the fish off** — a slime-coat step (Dave Hansen, `KTsXdQXAnkU`; medium confidence). SoCal practice in the corpus is photo-and-release — "our bass are slow to grow, so let them go" (`usHl-4SfqDA`, Long Beach breakwater, 2024-11-13).

## What I'd suggest

Fish the KB's sourced kelp-line presentations — weedless slug on the stringers, surface iron along the line, and the 1 oz pitch-and-sink at the kelp base when you want a bait falling vertically right at the edge — rather than porting a bay drop shot onto structure the notes never tested it on. If you run a drop shot out there anyway, treat the 6–10 in dropper and the hook-point-up Palomar as the transferable parts and the 10–12 lb leader / light drag as the part that will get you cut off, and log what you learn: this is exactly the kind of gap the KB wants filled with a real source rather than a guess.

You didn't give me conditions and I haven't pulled any, so nothing above is timed to a day. Per `planning/day-plan-protocol.md`, the actual go/no-go on a specific kelp bed comes from a BightSST pull (per-spot SST, chlorophyll, wind/swell/current, observed and forecast) run against the parallel-current rule and the seasonal priors — tell me the date and where you're launching from and I'll take it from there.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/drop-shot.md`, `species/calico-bass.md`, `techniques/swimbaits.md`, `locations/bass-structure.md`, `lures/bay-bass-plastics.md`, `tackle/gear-classes.md`, `species/spotted-bay-bass.md`, `species/california-halibut.md`, `techniques/dropper-loop.md`, `rigging/leadhead-mods.md`, `techniques/README.md`  
*videos:* `k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`, `KTsXdQXAnkU`, `P6Slg6RQiXw`, `9xNhdu2aBqE`, `Rwy4MqeXCIU`, `RXNebDr4j7s`, `tJFSV3AcIdE`, `r6j5w40fVHI`, `usHl-4SfqDA`, `kwMIgkCtFUE`, `0KQ--N5TjqE`  
*gaps admitted:* The KB has no drop-shot doctrine for calico bass at all — techniques/drop-shot.md is scoped to halibut and spotted bay bass on bay/sand bottom, and the species/calico-bass.md Situations-to-techniques router carries no drop-shot row and not even a flagged stub for it. | No heavy-leader or kelp-abrasion variant of the drop shot exists in the KB — the only leader specs given are 10-12 lb (Winch) and 8-20 lb matched to weight (Marquez), against the 40-65 lb leader specced everywhere else for kelp bass. | No guidance anywhere on rigging a drop shot weedless, or on whether/how a drop-shot dropper and weight foul in kelp stringers or on rock. | No hook-to-weight (dropper) length is given for kelp or reef — the 6-10 inch figure is explicitly derived from the halibut strike zone on sand. | No drop-shot weight sizing for the 25-50 ft outside-kelp-edge depth band; the 1/4 oz to 2 oz range in the note is bay-calibrated. | No calico-specific bite detection or hookset guidance for a bottom-suspended finesse rig; the take-up-slack-then-swing rule comes from a light-line bay context (EGKesj7V64M), and the KB's calico hookset doctrine is swimbait-specific (set on the pause, then grind, never pump). | No boat-positioning or drift guidance for holding a vertical presentation on a kelp edge, beyond the chum-and-anchor router row and the general up-current standoff geometry. | The prompt gave no conditions and I made no BightSST call, so no date, tide/current window, zone, or specific kelp bed is recommended. | No angler profile was applied, so all gear is given in KB class terms rather than owned rods and reels.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short answer first: the KB does not have a drop-shot-for-calico program

I followed the protocol in `planning/day-plan-protocol.md` (species router first, then technique note), and the honest result is that **this knowledgebase has no drop-shot doctrine for calico bass, and none for a kelp line.** Two specific places where it's absent:

- **`techniques/drop-shot.md`** is scoped to **California halibut and spotted bay bass** — every build, weight, leader and cadence in it comes from bay, sand-channel or surf fishing. Its front matter gates it to `waters: [bay-harbor, nearshore-coast]`. **It does not carry `island`**, so under the protocol's binding step-1b envelope filter, this technique would never be offered at all for a Catalina / San Clemente / Channel Islands kelp line. A mainland coastal kelp line (`nearshore-coast`) is the only place it even passes the gate.
- **`species/calico-bass.md`** — the router, and the thing that decides what technique a calico situation maps to — has a 16-row Situations → techniques table and **there is no drop-shot row in it.** Under the KB's own "flagged stubs, never silence" rule (`CLAUDE.md`), a popular-but-unsourced method is supposed to appear as a `⚠ Flagged stub`. It doesn't appear even as that.

One terminology trap worth clearing before anything else: in SoCal *offshore* usage, **"drop shot rig" means something completely different** — Capt. Matt's ring-and-tag-line bluefin deep-bait rig for fish 500–600 ft down (`rigging/rubber-band-deep-rig.md`, `G1YIlakiRqg`). That note explicitly says the name is coincidental and it is "not the bay/halibut finesse drop shot technique of the same name." If someone on a boat tells you to tie a drop-shot rig, confirm which one they mean.

So what follows is **assembled from KB parts, and I'm labelling where each part came from.** It is not KB doctrine, and I've flagged the joints where the two halves genuinely fight each other.

---

## The rig mechanics that transfer (from `techniques/drop-shot.md`, medium confidence)

These are geometry facts about the rig and carry over regardless of species:

- **Hook tied up the line, weight on a tag end below it** — bait suspended a fixed height above bottom while the lead stays pinned down, so you can **shake it in place** without dragging it off the spot.
- **Tie the hook on a Palomar**, leaving **12–14 in** of leader, then **pass the tag back down through the top of the hook eye** so the knot lies flat and the **hook point rides up**. The note calls a point that isn't riding up "the single most common rigging error" — the rig doesn't work well without it.
- **Hook-to-weight distance: 6–10 in** (Rod Marquez). Note the reason given is halibut-specific — that's the halibut strike zone off a sandy bottom, and a predator "won't burn energy to chase a bait 15 feet off." **The KB gives no kelp-line equivalent of that number.**
- **Weight: 1/4 oz to 1 oz**, light when it's glassy (Nathan Winch); Marquez runs **1–2 oz** and matches line to weight — **8–12 lb test with 1 oz, 15–20 lb with 2 oz**. Preferred shape is a **cylinder** weight; lead works, tungsten is "a little bit pricier" with "a lot more sensitivity" (`_rcxIWhNMSE`).
- **Hooks:** a strong long-shanked forged J-hook (O'Shaughnessy) is the primary pick; alternatives are a **VMC Spin Shot #2** (swivel-built, lets the bait swing 360°, costs one extra knot) or a **#2 mosquito hook** (`M2qZiY2lR98`, `_XfScSliRVk`).
- **Hookset — never set into slack** (Roman Castro, `EGKesj7V64M`). On light line it's the slack, not the hookset force, that pops the leader: wind down and lower the rod to come tight, *then* set. Swing on anything that isn't clearly bottom — a missed swing costs nothing.

The Winch and Marquez sections are attributed by name in the note without an inline video ID; the note's front-matter sources include `k4mD2d6C81k` and `1enjjFVcDG0`.

**One near-miss worth knowing about.** The one drop-shot-family rig in the KB that actually came off a *calico bass* panel (Fred Hall, `RUuPNpK0x-s`) is the **weedless slug on a drop-shot-style rig**: a slug-style plastic with a tail fin rigged **weedless on an Owner twist-lock**, on roughly a **2 ft leader** from weight to bait, with a **1 oz torpedo/keel weight** below — cast down a visible sand channel between structure and twitched back. But the note is explicit that it was described producing on **halibut in bay sand channels**, not on a kelp line. It's the closest thing the KB has to a weedless, long-leader drop shot, and it's the direction you'd have to move in for kelp — but the KB doesn't take it there. That same panel also names a "**reverse drop shot**" as a slow-day improvisation, with **rig detail not given on camera**.

---

## The joint that actually breaks: line, and the weedless problem

This is where you should be careful, because the two halves of the KB disagree by a factor of five.

| | Drop-shot note (bay / surf) | Calico kelp-line notes |
|---|---|---|
| Leader | **10–12 lb, light drag**; light-finesse halibut build runs **10 lb, 12 lb at the most** (`BPxE3xn3gAc`) | **60 lb fluoro** to 50–65 lb braid (Landesfeind); **65 lb braid → 40 lb mono** (Todd Klein, `9xNhdu2aBqE`); **65 → 50 lb** (Florentino, `P6Slg6RQiXw`); **25 lb fluoro** on the pitch-and-sink (Dave Hansen, `KTsXdQXAnkU`) — the lightest kelp figure in the KB |
| Class | **Light spinning class, 10–20 lb**, 2000-size reel (`tackle/gear-classes.md`) | **Bass class: 7–9 ft graphite-composite, 200–300 reel, 30–65 lb braid** |

`tackle/line-and-leader.md` gives the mechanism: Jack (Fred Hall panel, `ZoIzpyyS9xw`) reports calico teeth abrading **even 40 lb leader down to almost nothing in the last 6–8 in above the hook** — "like it had been cut with a knife." His rule is to run fingers over the leader and re-tie after any decent fish (3–5 lb+). He starts on a **4 ft leader and trims/re-ties it down over about two hours.** A 10–12 lb drop-shot leader has no margin for that.

The same panel keeps the counterweight side by side, so you get both: Capt. Benny Florentino says **30 lb is a fine floor**, his own biggest local calico came on **20 lb Spider Wire Ultracast to a short 20 lb leader**, and that line class is **not** the dominant variable — **where the fish gets hooked relative to structure is.** A fish hooked in open water over soft bottom gives you a real fight; a fish hooked in 3 ft over surging rock only has to load the rod before it reaches structure and cuts you, regardless of line strength. He also flags that break-off odds on 30 lb climb on an **outside kelp edge** (his example: Palos Verdes) versus fishing *inside* the kelp.

Two more things a light drop-shot outfit conflicts with directly:

- **A bare, upward-riding J-hook is not weedless.** Every kelp presentation the KB documents is either weedless (7 in slug on a **3/8–3/4 oz keel-weighted hook**, Gamakatsu 7/0 or Trokar, `techniques/swimbaits.md`) or an exposed leadhead pitched to *bare* spots. The drop-shot hooks the KB names — long-shank J, Spin Shot, mosquito, red octopus — are all open-point bay hooks. There's a documented fix for fouling in a *different* rig: an Owner weighted **"sled" head** slid into a slit in the bait's belly so the hook rides flush with the topline (`techniques/tube-bait-fishing.md`, low confidence, single promotional seminar). The KB has never combined it with a drop shot.
- **Fighting doctrine is grind, never pump** (Dave Hansen, `KTsXdQXAnkU`, high confidence — repeated in `techniques/chunking.md`). Set, then wind continuously; pumping gives slack on every drop that a hooked calico uses to dive back into the kelp. That is hard to execute on the light drag the drop-shot note calls for.

**Practical read:** if you're going to try it, the KB's own numbers argue for taking the *rig geometry* from the drop-shot note and the *line* from the calico side — Hansen's **25 lb fluoro** pitch leader is the lightest thing the KB actually endorses in kelp, and Florentino's 30 lb floor is the other anchor. Fishing 10–12 lb on a kelp edge is not something any note here supports.

---

## What the KB tells you to fish instead, if what you want is a bottom-contact presentation on the kelp line

These are the real rows in the calico router and the nearest neighbours to a drop shot:

1. **Pitch-and-sink at the kelp base** — pitch a **1 oz black/gold jig** (a leadhead the source calls a "hook up bait") right at the base of the kelp line and **let it sink straight to the bottom; the bite typically comes on that sink.** Runs **25 lb fluoro** (Dave Hansen, `KTsXdQXAnkU`, 2019-06-05). This is the closest thing in the KB to a vertical, in-place presentation on kelp.
2. **Leadhead swimbait deep** — sink the same bait class **70–80 ft down for calicos** over structure; fish holding up and feeding will rise to meet it (`techniques/swimbaits.md`). For a long-range beach stop, **3/4 oz to 1½ oz leadhead** with a 4–8 in plastic on a 7'6"–8'6" rod (Doug Kearn, `r9bF3VtzDUg`).
3. **Free-spool bottom bounce in ripping current** — the "stupid tube," **1.5 oz**, worked in free spool; each bounce the current swept it **5–10 ft further** down-current instead of winding back. "Calicos every cast" (`9a-Zy_D6c3w`, medium confidence — note the source names no kelp, just "tight to the beach").
4. **Tube bait on the Owner sled** when grass or heavy kelp fouls a standard weedless rig — but it needs an **8 ft full-length parabolic-bend rod, 40 lb+ for 3–4 oz baits**, or the hook pulls (⚠ low confidence, single promotional seminar).
5. **Flip / punch a heavy leadhead into gaps in the canopy** — Aaron Martens' "heavy head flip" on a short accurate pitch, fish sitting up *underneath* the floating canopy (`P6Slg6RQiXw`). ⚠ Single-session observed data point, explicitly **not** established doctrine, and no leader/hook/weight spec was given on camera.

---

## The kelp-line reads that govern whatever you tie on

These apply to any presentation, and they're the highest-confidence content here (`species/calico-bass.md` is `confidence: high`, primary voice Erik Landesfeind):

- **The edge is the spot.** Biting fish sit on the **up-current / leading edge**. Hit three or four sides of a kelp head and **you know in two or three casts.** Calico face **into** the current and ambush from the front of the kelp (Benny Florentino, `Rwy4MqeXCIU`).
- **Parallel current is the switch.** Current running **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage — skip it. (Late-fall exception kept side by side: at San Clemente the bass wanted off-color water with current running *into* the island, 11/23/22.)
- **Read the kelp itself as a current gauge** (`conditions/current-diagnostics.md`, `HnqiE05vdXs` / Ep. 14): kelp **pulled ~20 ft under = raging**, surface presentations dead, go deep/weighted; **laid down = strong**, fishable but hard; **resurfacing = slacking**, switch back to the surface. That raging/pulled-under state is the one condition where the router actually sends you subsurface — the closest real trigger you have for wanting a bottom-contact rig.
- **Working depths:** the outside kelp edge runs **~50 ft in to ~25 ft**, and calico will rise **10–15 ft off 80–100 ft of reef** to eat. Tommy Ponce's Dana Point water is worked at **0–8 ft and 20–100 ft** (`LqW32NSkObY`), with a stated temperature preference of **65–68°F** — past ~70°F they get lethargic and drop to cooler water.
- **Light angle:** bright, stable-light days push calico up into the **outer canopy edge**; overcast **spreads them out** through the column (`RUuPNpK0x-s`). Fish the hour before sunrise into early morning and the hour before sunset.
- **Cover water — that's the method.** **20–25 casts** to a bed if you're getting bites, **10–12** if you aren't, then move 100 ft or 100 yards. Beds re-bite, so come back. Note this directly overrides the drop-shot note's own "**move after ~20 minutes**" rule, which is a bay/surf cadence.
- **Legal size: 14 in for kelp bass** (California / CDFW, as of 2026-08 — verify current rules before fishing; `r6j5w40fVHI`). The KB also logs a 5-fish bag figure from 2019-03-13, flagged as its oldest regulatory number.

---

## One thing to not misread

`techniques/drop-shot.md` contains a light-finesse halibut build where the presenter says he fishes it "the same way he fishes what he calls **'green bass**,' just very slightly heavier" (`BPxE3xn3gAc`). The KB explicitly declines to read "green bass" as calico — elsewhere in that channel's catalog it means freshwater largemouth. So that passage is **not** a calico drop-shot data point, even though it looks like one.

No conditions, date, launch point or profile were given with your question, so I haven't picked a zone, a tide window or specific gear from anyone's inventory — under the protocol I'd need the day's `{regions, waters}` envelope and your rod/line inventory first, and I won't invent conditions.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/drop-shot.md`, `species/calico-bass.md`, `techniques/swimbaits.md`, `techniques/tube-bait-fishing.md`, `techniques/ned-rig.md`, `locations/bass-structure.md`, `conditions/current-diagnostics.md`, `tackle/gear-classes.md`, `tackle/line-and-leader.md`, `tackle/tackle-express-baja-light-setup-yellowtail-insurance.md`, `lures/bay-bass-plastics.md`, `rigging/rubber-band-deep-rig.md`  
*videos:* `k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`, `RUuPNpK0x-s`, `9qwsg-e9ECA`, `BPxE3xn3gAc`, `M2qZiY2lR98`, `_XfScSliRVk`, `_rcxIWhNMSE`, `fHMwcm1xRQk`, `KTsXdQXAnkU`, `9xNhdu2aBqE`, `P6Slg6RQiXw`, `ZoIzpyyS9xw`, `Rwy4MqeXCIU`, `9a-Zy_D6c3w`, `r9bF3VtzDUg`, `HnqiE05vdXs`, `LqW32NSkObY`, `r6j5w40fVHI`, `G1YIlakiRqg`, `kwMIgkCtFUE`, `0KQ--N5TjqE`  
*gaps admitted:* No calico-bass drop-shot doctrine exists anywhere in the KB: techniques/drop-shot.md names only California halibut and spotted bay bass, and species/calico-bass.md's Situations to techniques table has no drop-shot row — not even a flagged stub, which the CLAUDE.md 'flagged stubs, never silence' rule would call for. | techniques/drop-shot.md is gated waters: [bay-harbor, nearshore-coast] and does not carry 'island', so the KB would never offer it for an island kelp line (Catalina, San Clemente, Channel Islands) under the day-plan protocol's binding envelope filter. | No hook-to-weight (tag length) figure exists for a kelp-line drop shot. The 6-10 in number is Rod Marquez's halibut strike-zone figure off sandy bottom; nothing in the KB gives a kelp equivalent, and the only long-leader drop-shot variant it records (~2 ft, RUuPNpK0x-s) is bay sand channels. | No weedless drop-shot hook or bait combination for kelp is documented. Every drop-shot hook the KB names (long-shank J, VMC Spin Shot #2, mosquito #2, red octopus) is an open-point bay/surf hook; the Owner 'sled' weedless fix is documented only for tube baits, at low confidence, and never combined with a drop shot. | The KB never reconciles drop-shot line class (10-12 lb leader, 15-20 lb with a 2 oz weight, light drag, 2000-size spinning) with calico kelp-line line class (25 lb fluoro at the very lightest, more commonly 40-65 lb leader on 50-80 lb braid). There is no note that says what line to fish a drop shot on in kelp. | Nothing on snag rate, break-off management, or lead recovery when dropping a weight into kelp — the whole point of failure for a bottom-pinned rig in structure is uncovered. | No boat-handling guidance for working a drop shot vertically along a kelp stringer. The KB's calico boat-position doctrine (jog the bow out to feed the caster the outside stringers, 10-25 casts then move) is written for casting programs, not for holding on a vertical presentation. | The drop-shot note's 'move after ~20 minutes' rule and the calico router's cast-count rule (20-25 casts with bites, 10-12 without) are two different search cadences and the KB does not say which governs a hybrid. | No conditions, date, launch point, boat envelope or angler profile were supplied with the question, so no zone, tide/timing window, or owned-gear resolution could be made; the protocol requires the day's {regions, waters} envelope and a rod/line inventory first.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short version first

**The knowledgebase does not cover the drop shot for calico bass.** Not on a kelp line, not anywhere. I want to be blunt about that before giving you anything, because the gap is structural rather than an oversight I can paper over:

- `techniques/drop-shot.md` is scoped to **California halibut and spotted bay bass**. Its "Reach for this when" list names exactly those two fisheries, its front matter is `waters: [bay-harbor, nearshore-coast]`, and the word "calico" does not appear in it.
- `species/calico-bass.md` is the router, and its **Situations → techniques** table runs about fifteen rows — weedless swimbait to stringers, open slug, surface iron, crankbaits, flyline, beach bounce, canopy punching, chum-and-anchor, night, trophy sizing, winter reaction bait — and **not one of them is a drop shot.** There is not even a flagged stub row for it, which by this repo's own "flagged stubs, never silence" rule means the silence here is a defect, not a verdict.

So anything below that touches calico specifically is me joining two notes that the knowledgebase never joined itself. I have marked where that happens.

One gating point before the mechanics, because the day-plan protocol (`planning/day-plan-protocol.md`, step 1b) makes it binding rather than advisory: **which kelp line matters.** Per `locations/regions.md`, `nearshore-coast` is "the coastal strip — kelp lines, breakwalls, jetties, riprap, coastal reef" and `island` is "island shorelines, boiler rocks, island ridges and their kelp." `techniques/drop-shot.md` carries `bay-harbor` and `nearshore-coast` only. **If your kelp line is at Catalina, San Clemente, the Channel Islands or Cedros, the drop-shot note is outside the day's envelope and the protocol says it is never offered — not ranked lower, not offered with a caveat.** On a coastal bed (Dana Point, North County San Diego) the water class does intersect; the species coverage still does not.

---

## The rig, as the KB actually documents it

All of this is halibut/spotty doctrine. It transfers as far as you decide it transfers.

**The concept** (`techniques/drop-shot.md`): hook tied up the line, weight hanging below on a tag end, so the bait is suspended a **fixed height just above the bottom** while the lead stays pinned to the deck. That is what lets you shake it in place without dragging it out of the spot.

**The tie** (`k4mD2d6C81k`): Palomar — leave **12 to 14 inches** of leader, double the line, through the eye, overhand knot, loop over the shank, cinch. Then **pass the leader tag back down through the top of the hook eye** so the knot lies flat and the **hook points upward**. The note is emphatic: if the point isn't riding up, the rig doesn't work, and hook-not-facing-up is listed as the single most common rigging error under Common failures.

**Hooks:**
- A **strong forged long-shanked J-hook** — an O'Shaughnessy — which holds the bait in position and stops it sliding (`k4mD2d6C81k`).
- **VMC Spin Shot, size 2** — a drop-shot hook built on a swivel, so the bait swings freely through 360° and any line movement or current spins it; costs one extra knot to tie (`_rcxIWhNMSE`, re-cut as `M2qZiY2lR98`). The note carries a fact-check flag here: that content is miscited to `_XfScSliRVk`, a 39-second clip that never mentions swinging or the extra knot.
- **Size 2 mosquito hook** as the simpler alternative if you don't want the swivel build (`_XfScSliRVk`), same Palomar, same point-up rule.

**Weights:**
- **1/4 oz up to 1 oz**, light when it's glassy (`k4mD2d6C81k`).
- A second build runs **1 to 2 oz** matched to line: **8–12 lb test with 1 oz**, **15–20 lb test with 2 oz** (`1enjjFVcDG0`).
- **Cylinder style** preferred. Lead does the job; tungsten works, "a little bit pricier," "a lot more sensitivity," but the stated practice stays with lead (`_rcxIWhNMSE`). Painting the lead black or green to kill flash is offered explicitly hedged — "maybe it makes a difference, maybe it doesn't."

**Gear class:** light spinning class, **10–20 lb**, 2000-size reel (`tackle/gear-classes.md`; `techniques/drop-shot.md`, `k4mD2d6C81k`). Braid specifically, so you can **see** the bite and feel it on a slack line. Leader **10 to 12 lb**, light drag.

**Working it:**
- Weight on the bottom, bait suspended just above, **shake it in place** (`1enjjFVcDG0`).
- **Grub:** rod tip down at **45 degrees**, constant retrieve. **Fluke:** twitch the rod, reel the slack, twitch again (`1enjjFVcDG0`).
- **Move after about 20 minutes** with no bite — the fish may be 20 yards off (`1enjjFVcDG0`). "Camping dead water" is a listed failure.
- **Hookset: never set into slack** (`EGKesj7V64M`). On light line, driving the hookset with slack between tip and bait is what pops the leader. Wind down, lower the rod, take up the slack, *then* set. Swings are free — swing on anything that isn't obviously bottom.
- The drag-shake-drag cadence in that note (22–30 in of drag, 3–4 ft stated strike radius) is explicitly a **surf halibut** program off the beach (`9qwsg-e9ECA`, itself flagged as a verbatim re-cut of `fHMwcm1xRQk`). Do not carry it to a kelp edge.

**Hook-to-weight distance:** this is the parameter you would most want for a kelp line, and the KB does not have it for calico. `techniques/drop-shot.md` states only the principle — too long and the bait rides out of the strike zone, too short and it isn't above the bottom — and routes the actual spacing number to `species/california-halibut-surf-lures.md`, where it is a halibut strike-zone figure.

---

## Why the KB's own content argues against this on a kelp line

I am joining notes here; neither states this conclusion.

**1. The rig is bottom-anchored; calico on a kelp line are not.** `species/calico-bass.md` puts the biting fish on the **up-current / leading edge** of the kelp head — they face into the current and ambush from the front, so a lure swept past the leading edge draws them out (`0KQ--N5TjqE`, `Rwy4MqeXCIU`). On bright, stable-light days they **levitate up into the canopy**, concentrating on the outer canopy edge (`RUuPNpK0x-s`). The commonly worked bands off Dana Point are **0–8 ft and 20–100 ft** (`LqW32NSkObY`). The drop shot's whole proposition is a short fixed rise off a pinned weight, with too much rise named as a failure mode — that is a poor fit for fish holding at canopy level in 25–50 ft.

There is a live internal contradiction in the KB on exactly this point, and it is worth knowing about: `species/spotted-bay-bass.md` ranks the drop shot for "fish suspended off structure / need a slow horizontal fall," and `techniques/drop-shot.md` carries a fact-check flag saying that row describes a presentation the technique note does not have, and that the row carries no cite. So the one place the KB gestures at drop-shotting suspended structure fish is the place it flags as wrong.

**2. The line class is not kelp line class.** The drop shot runs 10–20 lb with a 10–12 lb leader. What `techniques/swimbaits.md` says a kelp-line calico rig takes: **50 to 65 lb braid on a 300-size reel with 60 lb fluorocarbon leader**, because "the leader gets braided up and chafed just from throwing it in the kelp, so keep it stout" (`YIABTTYXeqc`, `n6PTy8g3pb0`). A second workable combination is **65 lb braid to 40 lb mono** (`9xNhdu2aBqE`), and the note explicitly frames a freshwater setup (10 lb braid to 5 lb fluoro) as the contrast for how much heavier the SoCal kelp game runs. The night program steps to **50 lb+ fluoro** for abrasion (`species/calico-bass.md`).

**3. The fight rule is incompatible with light-line finesse.** `techniques/swimbaits.md`: once bit, **set and then wind — never pump the rod**, because every drop of a pump gives slack a hooked calico uses to dive back into the kelp (`KTsXdQXAnkU`). That is a grind-them-out-on-heavy-line doctrine. It is the opposite of the drop shot's own instruction to let a big one run and play it out on light tackle.

---

## The one drop-shot-family rig the KB does document around structure

This is the closest thing in the corpus, and notably its source **is** the Fred Hall Calico Bass Panel (`RUuPNpK0x-s`), even though the KB scopes the effectiveness claim to bay species rather than calico.

**Weedless slug on a drop-shot-style leader** (`techniques/drop-shot.md`, "Alternate rig"):
- A **slug-style soft plastic with a tail fin**, rigged **weedless on an Owner twist-lock** hook — the same weedless-slug family in `techniques/swimbaits.md`, adapted onto a dropper-style leader.
- Roughly a **2 ft leader** from weight to bait, with a **1 oz torpedo/keel weight** below it.
- **Cast down a visible sand channel between structure and twitch it back.** Called effective enough on halibut, spotted bay bass and other bay species that "they cannot handle it."
- The bait was brought to the Fred Hall show as a dedicated drop-shot bait roughly seven or eight years before the 2013-03-09 source date — so introduced around **2005–2006**.

That 2 ft leader and the weedless twist-lock are the two changes that matter for structure: the leader gets the bait up out of the bottom, and weedless is what survives the junk. If you are determined to run a drop-shot presentation near a kelp bed, this is the version the KB actually documents, and the sand channels **between** heads are where it says to put it — not through the bed.

The same panel also supplies the KB's "improvising when the bite goes dead" doctrine (`RUuPNpK0x-s`): the trigger is a confirmed slow, scratching bite; the decision is to deliberately reach for unconventional rigs rather than keep soaking the standard program; the stated reason is that an odd rig costs nothing worse than a recast. Named examples include a **reverse drop shot** (rig detail not given on camera) and **a worm on a drop shot with a shrimp bait rigged above it.** That is explicitly a dead-bite escape valve, not a primary program.

---

## What the KB routes you to instead on a kelp line

If the goal is calico on a kelp edge rather than the drop shot specifically, here is what the notes actually prescribe.

**Set the gate first** (`species/calico-bass.md`, `conditions/current-diagnostics.md`):
- Current **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal but a viable off-colour state; **off** the beach is garbage — skip the spot (`0KQ--N5TjqE`).
- Read the kelp's posture: **pulled ~20 ft under** = raging, surface presentations dead, go deep or weighted; **laid down** = strong, work the down-current side; **resurfacing** = slacking, switch back toward the surface (`HnqiE05vdXs`). That table is the KB's actual trigger for reaching for a weighted bottom presentation on a kelp line. The ~20 ft figure carries a single-source flag.
- Fish the **edges and pinch-points** — leading edge, outside edge, isolated stringers — not the dense middle (`locations/bass-structure.md`).

**The default presentation** (`techniques/swimbaits.md`):
- **7-inch weedless/MC slug on a keel-weighted hook** — Gamakatsu **7/0, 3/8 oz** or a Trokar keel-weighted hook. Weights come half oz, 3/4 oz or nano; **3/4 oz is preferred** because it keeps the bait in the water while you wind fast (`YIABTTYXeqc`, `n6PTy8g3pb0`).
- Replace the stock spring with an **Owner large** or **Trokar/Eagle Claw XL** spring, buried all the way so the plastic butts against the hook — tracks better and gets roughly **10 times as many fish per bait**.
- **Short, pinpoint casts to individual stringers**, starting at the leading edge. Bomb the open slug to call fish off the structure; the weedless is the precision cast.
- **Fast steady wind** by default. **Set on the pause, never on the grab** — the fish eats from behind; watch it eat, pause to let it turn away, then set. Swing on the feel and "nine times out of ten you pull the bait out of the fish's mouth."
- Reel **at least 6.2:1**, because calico eat and come right back at the boat and a slow reel can't take up the slack (`P6Slg6RQiXw`). The KB flags this as an unreconciled doctrine conflict against Landesfeind's general inshore-baitcast advice in `tackle/rod-and-reel-selection.md`.

**If your instinct is specifically "I want something vertical at the kelp"** — the KB has a presentation for that, and it is not a drop shot. **Pitch-and-sink at the kelp base** (`techniques/swimbaits.md`, `KTsXdQXAnkU`): pitch a **1 oz black/gold jig** (a leadhead the source calls a "hook up bait," brand not confirmed) right at the base of the kelp line and **let it sink straight to the bottom — the bite typically comes on that sink.** Run **25 lb fluoro** for this one, lighter than the 60 lb above; the note records it as a second workable combination, not a contradiction.

Two more vertical options in the same note:
- **Punching gaps in the canopy** with a heavy jighead when fish hold up underneath a dense floating canopy rather than at the edge — a freshwater flipping transfer, fish work the dropped bait from below before eating (`P6Slg6RQiXw`, flagged single-source, one San Clemente session December 2013).
- **Leadhead swimbait sunk 70 to 80 feet** over structure for calico, with feeding fish rising to meet it. Flag it: the KB marks that depth figure "unverifiable" — the only cite on the bullet (`OURS05qEGcA`) is entirely a halibut video and the calico depth's source is unresolved.

**Covering water is the method** — grade a bed with a handful of casts to the prime edge, then move (`YIABTTYXeqc`, `0KQ--N5TjqE`).

---

## If you want to try it anyway

Nothing here forbids it, and the KB's own dead-bite doctrine says an odd rig costs nothing worse than a recast. If I were assembling it from what these notes support, I would take the **weedless-slug-on-a-dropper** build (Owner twist-lock, ~2 ft leader, 1 oz torpedo weight) rather than the bay fluke build, put it **in the sand lanes between heads and off the outside edge** rather than into the bed, and carry the leader at kelp class (**40 lb mono or 60 lb fluoro**) rather than the drop shot's 10–12 lb. Every one of those substitutions is my inference from adjacent notes — the KB does not sanction the combination, and none of it is corpus-sourced as a calico program. Log what happens; that is exactly the kind of observation the repo's evidence layer is built to take.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `techniques/drop-shot.md`, `techniques/evidence/drop-shot.md`, `species/calico-bass.md`, `techniques/swimbaits.md`, `techniques/ned-rig.md`, `species/spotted-bay-bass.md`, `lures/bay-bass-plastics.md`, `tackle/gear-classes.md`, `conditions/current-diagnostics.md`, `locations/bass-structure.md`, `locations/regions.md`  
*videos:* `k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`, `RUuPNpK0x-s`, `_XfScSliRVk`, `_rcxIWhNMSE`, `M2qZiY2lR98`, `nZfEB7466ys`, `BPxE3xn3gAc`, `fHMwcm1xRQk`, `9qwsg-e9ECA`, `0KQ--N5TjqE`, `Rwy4MqeXCIU`, `LqW32NSkObY`, `HnqiE05vdXs`, `YIABTTYXeqc`, `n6PTy8g3pb0`, `9xNhdu2aBqE`, `P6Slg6RQiXw`, `KTsXdQXAnkU`, `OURS05qEGcA`  
*gaps admitted:* No note anywhere in the KB documents the drop shot for calico bass — techniques/drop-shot.md is scoped to California halibut and spotted bay bass only, and 'calico' does not appear in it. | species/calico-bass.md's Situations → techniques table (roughly fifteen rows) contains no drop-shot row and no flagged stub for one, so the KB's own 'flagged stubs, never silence' rule is unmet for this method. | No hook-to-weight (leader rise) distance is given for calico bass anywhere; techniques/drop-shot.md states only the principle and routes the actual figure to species/california-halibut-surf-lures.md as a halibut strike-zone parameter. | techniques/drop-shot.md carries waters: [bay-harbor, nearshore-coast] and no 'island' class, so under the day-plan-protocol step-1b filter it is out of envelope for any island kelp line (Catalina, San Clemente, Channel Islands, Cedros) — the KB gives no island-gated drop-shot content at all. | No leader or line spec exists for a drop shot fished in kelp; the note's 10–12 lb leader is bay/surf spec, and the KB's kelp abrasion specs (50–65 lb braid / 60 lb fluoro, or 65 lb braid / 40 lb mono) live only in techniques/swimbaits.md for a different rig. | No weedless drop-shot hook option is documented — every hook named in techniques/drop-shot.md (forged O'Shaughnessy long shank, VMC Spin Shot #2, #2 mosquito) is an open-hook bay build. | No guidance on presenting a drop shot from a drifting or anchored boat on a kelp edge — boat positioning for kelp work exists only in techniques/swimbaits.md for cast-and-wind presentations. | The KB gives no figure for how far off the bottom calico hold on a kelp line, so there is no basis in the notes for setting a drop-shot leader length for them. | species/spotted-bay-bass.md's drop-shot row ('fish suspended off structure / need a slow horizontal fall') is the only KB text suggesting a suspended-structure drop shot, and techniques/drop-shot.md carries a fact-check flag stating that row describes a presentation the technique note does not have and carries no cite. | The 'weedless slug on a drop-shot-style leader' rig in techniques/drop-shot.md comes from a Calico Bass Panel source (RUuPNpK0x-s) but the KB scopes its stated effectiveness to halibut, spotted bay bass and other bay species — it makes no calico claim for the rig. | The 'reverse drop shot' named in the KB's dead-bite improvisation list has no rig detail — the note states the detail was not given on camera. | The 70–80 ft leadhead-swimbait calico depth in techniques/swimbaits.md is flagged 'unverifiable' by the KB itself — its only cite is a halibut-only transcript and the figure's source is unresolved. | The '~50 ft in to ~25 ft' outside-kelp-edge sonar band in species/calico-bass.md is flagged by the KB as carrying no cite, appearing in no other note, and being absent from its own evidence file.

</details>
