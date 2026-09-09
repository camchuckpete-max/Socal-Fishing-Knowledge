# Technique — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11 | 11.75 | 12 |
| found | 2 | 2 | 2 |
| specific | 1.75 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.75 | 2 | 2 |
| honest | 2 | 1.75 | 2 |
| actionable | 1.5 | 2 | 2 |
| **wins** | 1 | 1 | 2 |  (ties: 0)
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

**Winner:** B2 · mapping {'A': 'B3', 'B': 'NOW', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 1 | 2 | **11** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three correctly reported that the KB has no Farnsworth depth, bottom composition or preferred current directions, and all three handled the partial-take closure with CDFW named and verify-current. C wins on execution: it is the only answer that turns the continuous-wind vs crank-and-freespool conflict into a decision frame (band-cycling for bottom-hugging structure yellows, long burn when marks ride up), the only one carrying drag numbers with a worked example on Cameron's own 80 lb setup, sounder range setup, and the paired dropper-loop alternative, and it region-labels its Baja depth numbers instead of parking them beside SoCal doctrine. B is a close second and is the most epistemically careful — it alone surfaces that the source hedges the fall claim ('not really a prime time'), that the 5-10 fathom sonar figure is absent from the cited transcript, and that the KB contradicts itself on 6X weight — but it offers no drag guidance, no worked drop depths and no alternative presentation. A is the most fluent and has the richest cadence menu and failure modes, but it hands over six equal cadences with no rule for choosing and repeats the fathom figure and the unhedged fall claim as settled, which is exactly where the other two show the KB is flagged.

- *B2 reasons:* found: same three Farnsworth facts, plus the caption-garble provenance from the extraction log, and explicitly says there is no bank page, depth or contour. specific: kelp-lean table, real drop depths region-labeled (Tanner 80 ft/bait 60 ft SoCal; Cedros 212 ft, San Augustine 130 ft, Mag Bay 180 ft flagged Baja), 100-180 g flat-falls, four-row line/leader table, drag at 1/4-1/3 of lowest class with a worked 10-13 lb example and 20-27 lb on the owner's 80 lb braid. sourced: note paths, video ids, dates; conflicts attributed by name where attribution is the content. scoped: California/CDFW with as-of 2022-10 and verify-current; declines to extend island-scale Catalina swell doctrine to a bank the KB never places, and labels Baja parameters as out-of-region contrast. honest: longest and sharpest gaps list, admits no BightSST call, no yellowtail tide rating, unresolved fluoro/mono split, and that it did not open boat.md. actionable: gives the base retrieve, a real decision frame for the cadence conflict keyed to where fish sit, the dropper-loop pairing, sounder range setup and drag math — a new angler could rig and execute.
- *B3 reasons:* found: pulled the three real Farnsworth facts (fall yo-yo 5p6gu14ZC4w, partial-take closure, standalone-bank typology) plus full yo-yo doctrine, and said plainly the bank has no depth data. specific: dense numbers — 120-180 ft and 120-240 ft bands, 5-6 oz 6X, 65 lb braid + 50 yd 40-50 lb top shot, 43 in/turn, 6.6:1, coords 33 20.560/118 31.010. sourced: every claim carries a note path and video id. scoped: socal-bight/island-bank gate stated up front; closure given with CDFW named, source date 10/26/22, note's missing as-of called out and verify-current instructed. honest: strong gaps list, but presents the ~5-10 fathom sonar figure and the unhedged 'good fall yo-yo' line as settled where the other answers show the KB flags them, and never surfaces the jig-weight conflict; the six-cadence table is handed over with 'pick one' and no decision frame. actionable: an angler can rig and run it — position up-current, thumb the drop, burn it, plus failure modes, bycatch trap and bite-rate calibration.
- *NOW reasons:* found: opens by naming that no Farnsworth page exists (escalated worklist row) and still assembles bank-level context from catalina-island-backside plus the technique note. specific: jig-size-by-depth ladder (60/80/100 -> 6X Jr; 120-150 -> 6X 5-6 oz; 150-250 -> full 6X; 120-240 overnight), 5-6 cranks/~20 ft, 60-70 ft half-wind, 150 yd walk, 40/50/60 lb line ladder, Penn Fathom 30 build. sourced: note paths plus video ids throughout, including evidence-file citations. scoped: CDFW named with 'as of 2022-10', boundary and agency admitted absent, verify-current stated; weather-side/backside framing correct. honest: best in class — surfaces the source's own hedge ('not really a prime time'), flags the 5-10 fathom figure as absent from the transcript, names the 8 oz/4 oz vs 5-6 oz internal conflict, and refuses to assume a null boat envelope. actionable: closes with a concrete run-the-day paragraph, though it gives no drag setting, no real drop-depth examples and no paired alternative presentation.

<details><summary>Full prompt</summary>

How do I fish a yo-yo iron at Farnsworth Bank? Retrieve, depth, current, and the tackle to use.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

# Yo-yo iron at Farnsworth Bank

First, an honesty note on scope. This KB has **no dedicated Farnsworth Bank page** — there is no depth, crest depth, bank footprint, or charted contour for Farnsworth anywhere in it. What it does have is (a) three Farnsworth-specific facts, (b) a complete yo-yo-iron execution note, and (c) the structure/current doctrine that tells you how a bank of that *type* fishes. I've built the answer from those and flagged every place I'm handing you a general rule instead of a Farnsworth-specific one. You also gave me no conditions, and I have not called BightSST — step 1 of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) (per-spot SST/chlorophyll + wind/swell/current, observed and forecast) is still yours to run. Everything below is the pattern layer.

---

## 1. Read the closure before you plan the day

Farnsworth sits in a **partial-take SMCA**. The corpus records the rule as: **only yellowtail and bonito may be kept there** ([`species/yellowtail.md`](species/yellowtail.md), from the 10/26/22 BD Bight report, `5p6gu14ZC4w`; the spot library flags it the same way — "Farnsworth Bank (partial-take SMCA — see DFW)", [`sources/spot-lists.md`](sources/spot-lists.md)).

- **Jurisdiction:** California / CDFW.
- **As of:** the source claim dates to 2022-10 and the spot-list annotation says "see DFW" rather than quoting the reg. **Verify current rules with CDFW before you fish it** — the KB does not carry the SMCA boundary or the current take list.
- **Why it matters to a yo-yo trip specifically:** a heavy iron worked on hard bottom will also pick off calico bass — the KB has a documented instance of a calico eating a yo-yo iron bounced on bottom (`Qa-j6LIwa1Q`, [`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)) — plus whatever else lives on the structure. Under the rule as recorded, those go back. Plan it as a yellowtail (and bonito) trip, not a mixed-bag trip.

**Position (charted/public):** 33° 20.560' N / 118° 31.010' W, listed in the Catalina **backside** sequence between Ben Weston Point and Catalina's China Point ([`sources/spot-lists.md`](sources/spot-lists.md)).

The Farnsworth name reached the KB through a caption-garble correction — the 10/26/22 report says "foreign First Bank," identified as Farnsworth from the described closure rule ([`sources/extraction-log.md`](sources/extraction-log.md)). So the fall-yo-yo claim rests on one video, and I'm labeling it as such.

## 2. Season: fall is the stated window

The single Farnsworth-specific fishing claim in the KB: **Farnsworth gives good fall yo-yo fishing** (10/26/22, `5p6gu14ZC4w`, in [`species/yellowtail.md`](species/yellowtail.md)). Same report gives you the surrounding Catalina context — ~40 yellows in a day at Catalina in late October, and "no reason you couldn't catch a yellowtail" while temps hold, even outside prime time.

Hold that loosely against Cameron's own doctrine, which the KB keeps side by side with the corpus: **calendar date doesn't matter for yellowtail — water state (temp + bait) does** ([`species/yellowtail.md`](species/yellowtail.md), `cameron`). Read the water; don't fish the date.

## 3. Where on the bank — Farnsworth is the textbook standalone bank

Farnsworth is literally the KB's named example of the type. Two notes use it that way:

- **Standalone banks (Farnsworth type — structure rising off the plain, not attached to land) fish in ANY current direction**, unlike land-attached perpendicular ridges, which are two-directional and die on off-the-beach current. But **each individual bank still has its own preferred directions, learned spot by spot — there is no single rule** ([`locations/island-structure.md`](locations/island-structure.md), [`conditions/current-structure.md`](conditions/current-structure.md); 2/20/25 = `6TBxHnkYXI0`, Academy Ep. 14 = `0KQ--N5TjqE`).
- **The KB holds no record of Farnsworth's own preferred directions.** That's a gap, and the doctrine tells you what to do about it: keep a per-spot log of which wind direction and which current direction the spot produces on, and match the day's read against that list ([`conditions/current-structure.md`](conditions/current-structure.md), Hansen, `xI9tPJFXbUM`). Start yours.

**Within the bank, bias to the up-current face.** Upwelling forms where the current impinges on the structure, so the up-current face is where the food chain stacks. Under the summer uphill (counter)current that means the **lower / south face** of a bank — "that uphill current hits the lower end of those banks" (Academy Ep. 1, `h3PTupup17I`, [`conditions/current-structure.md`](conditions/current-structure.md)). Under a different vector that day, move to whichever face the water is being forced onto.

**Read the current once, apply it region-wide.** Current direction is spatially coherent across the Bight on a given day — one HF-radar cell or one on-water report propagates across your whole spot list; confirm with the observables at each spot ([`conditions/current-structure.md`](conditions/current-structure.md), Ep. 14).

Adjacent and worth knowing: at Catalina, **the ~500-fathom curve is itself structure** — the uphill current compresses climbing the slope, spins eddies, and aggregates bait and paddies along it ([`locations/island-structure.md`](locations/island-structure.md), 8/31/22 `HnqiE05vdXs`). That's an island-scale feature, not Farnsworth, but it's the same run.

## 4. Current — this is the trigger that decides whether you yo-yo at all

Yo-yo is not the default presentation; it's what you go to when the surface is dead. The KB gives you a physical gauge — **kelp lean** ([`conditions/current-diagnostics.md`](conditions/current-diagnostics.md), 8/31/22 `HnqiE05vdXs` / Ep. 14):

| Kelp behavior | Current | Call |
|---|---|---|
| Kelp pulled **~20 ft under** the surface | **Raging** | Surface presentations are **dead** — go deep / weighted. **This is your yo-yo signal.** |
| Kelp **laid flat** along the surface | **Strong** | Fishable but hard; work the down-current side |
| Kelp **resurfacing / standing back up** | **Slacking** | Switch back to [surface iron](techniques/surface-iron.md) |

The explicit reach-for-this rule in [`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md): *"A hard current has shut the surface down: when the kelp is pulled under or laid flat, surface presentations are dead — go vertical. When the kelp resurfaces, switch back to surface iron."* Watch the kelp, not the clock — the laid-down→resurfacing transition is your cue to change gear *before* the window.

Two more current reads for the bank:

- **Chum-drift angle vs. boat lay** separates true current from wind push. Chum straight back off the stern = boat and water moving together (wind-dominated). Chum swinging off at an angle to the boat's lay = **real current cutting across** — that angle is your direction sensor (2/20/25, `6TBxHnkYXI0`).
- **"The treadmill is off."** No current at anchor reads as **bait pointing in all directions** (not lined up) plus **fish metering but not biting**. Marks will not convert. That's a move-or-wait signal: reposition to where current runs, or wait for the tide change ([`conditions/current-diagnostics.md`](conditions/current-diagnostics.md), 2/20/25). A bite-pattern version of the same tell: baits hit on nearly every drop, then several drops in a row with nothing, is often the first sign the current just stopped (Hansen, `aFb221LUoD0`).

**Timing.** Be at the highest-percentage zone **an hour before the tide change** — arrive before it, be fishing when it hits (2/20/25, [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md)). On off-peak days (post-moon, pressured, marginal), action **compresses into the tide windows**, so anchor the plan to tide times; on strong days the bite isn't tide-gated and you can route freely. The KB records **no yellowtail-specific tide dependence** — the species table there lists calico as current-driven/tide-indifferent, white seabass, marlin and bluefin foamers as slack biters, and does not rate yellowtail. Don't let me invent one.

## 5. Depth — fish the meter, and here are the bands the KB gives

The KB gives **no depth for Farnsworth**. What it gives is the yellowtail sonar signature and a set of real drop depths from other spots:

**The signature to look for** ([`species/yellowtail.md`](species/yellowtail.md)):
- Structure/bottom yellows show as **tight balls hugging the structure** on hard bottom, pinnacles and high spots, with the classic read being **arcs / boil-ups at ~5–10 fathoms (30–60 ft) near structure**. *"We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite"* (`D5DR7Kx42_A`).
- **Hard bottom only, never mud** — structure yellows sit exclusively on hard/rocky bottom. Read bottom hardness off return thickness (thin, faint line = sand/mud; thickening, darkening = rock) and decide whether the spot is even worth working before hunting fish sign on it (Hansen, `6DzbsElGE7E`; brand-agnostic method, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)).
- **A thin, lighter mark riding above the bait ball can be the yellowtail itself**, pushing bait up off the rocks. That's the sign to commit the anchor over a hard-bottom mark — not the bait pile alone (same source).
- Set your sounder's **manual range so the bottom sits mid-screen**, not pinned at the edge, so you have vertical room to separate hard from soft bottom and pick fish out of the column above it (Hansen, `FEXgl0eQCa8`, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)).

**Real drop depths in the corpus** (none of them Farnsworth — use them as range, not as a target):
- **SoCal, Tanner Bank:** dropped to about **80 ft** with bait marks sitting around **60 ft** (`ntQXxcH5sjI`, 2024-08-29).
- **Hansen's near-boat band:** **120–200 ft** of water with fish suspended **~20 ft off the bottom** — when marks sit at 120 ft, work the **100–120 ft** band (`wzI0lpgKT1U`).
- **Baja/Cedros (region-labeled, not SoCal):** one drop called at **212 ft** with fish showing anywhere **50–150 ft** (`A8SuzB5qiKE`); **130 ft** at San Augustine (`u0scEBby7nA`); **180 ft, 10 ft off the bottom** on a ridge near Mag Bay (`3tQ1_xiqwVU`).

The operative instruction is unchanged across all of them: **drop to the mark or to the bottom, and let the meter set the number.**

## 6. The retrieve — and the conflict the KB deliberately does not resolve

**Headline doctrine** ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)):

1. **Position up-current of the mark** so the drop sweeps down onto the structure.
2. **Free-spool the iron straight to the mark** (or to the bottom), **thumbing the spool** so it falls under light tension and tracks straight down rather than scoping away from the boat.
3. **Wind as fast as you can, all the way up.** The strike is a reaction to the fleeing iron — there is no finesse cadence, **the speed is the trigger**. Nothing hits, drop back to the mark and rip it again.
4. **Hand position through the drop:** index finger on the spool, thumb on the trigger, left hand forward — never thumb-on-spool from behind — so you snap straight into gear-and-crank on the bite instead of repositioning first ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md), `wzI0lpgKT1U`).

**The documented conflict.** Capt. Dave Hansen (registered voice, high confidence, `wzI0lpgKT1U`, 2021-03-16) defines yo-yoing as the *opposite* of a continuous wind — a **crank-then-freespool cycle that stays down in the strike zone**:

- **Straight up-and-down under the boat:** in gear for **five or six quick cranks** (roughly 20 ft of retrieve), then straight back to freespool and let it fall; repeat, cycling the same 20-ft band where fish are marked. Never let the jig sit dead on the bottom, and never wind it up out of the zone.
- **Cast-and-retrieve version:** iron all the way to the bottom, engage, crank hard for **10 cranks**, back to freespool to the bottom; repeat in 10-crank increments, walking the iron back toward the boat over as much as **150 yards**. His stated reason: winding continuously pulls the iron up out of the band where suspended fish hold, and off the angle that makes it look like a fleeing baitfish.
- **Strikes often come on the drop**, not the crank — the falling iron on freespool looks like a dying baitfish. A bite on the sink often reads as a **brief stop** before the fish takes off with it.

A third recorded variant (San Benito Island, Baja, `SH7zOA9ZF3o`): bottom → crank hard about **halfway up** → out of gear, fall to bottom → halfway up again → fall to bottom → **then** reel it all the way to the top.

**The KB keeps these side by side and does not reconcile them.** Here is the frame I'd apply, using only what the notes say each one is for:

- **What the choice turns on is where the fish are sitting**, not which source you like. Broad reaction bite, fish willing to come up the column → continuous full-speed wind, speed is the trigger. Fish pinned in a narrow band tight to structure → cycle the band, because a full wind takes the iron out of it after the first few seconds.
- **For your case — structure yellows on a hard-bottom bank — the species router leans toward working near the bottom.** Its structure row reads: *"hit bottom, **a couple cranks off the bottom = reaction bite**"* ([`species/yellowtail.md`](species/yellowtail.md), `D5DR7Kx42_A`). That's the same shape as Hansen's cycle, not the full wind. Start there at Farnsworth; if the marks are riding well up off the bottom, switch to the long burn.
- One further data point from a Baja/Cedros session: hookups were called out **both on the drop and on the wind-up**, so don't stop paying attention on either half of the cycle (`ILBl12Jm7-0`).

**Stack the column.** Two independent SoCal/Baja sessions in the KB record crews working **surface iron up top and yo-yo iron down simultaneously**, with the sounder showing fish holding below even while some anglers got bit on top (`ecJPMTCi-gw`, San Clemente Island, 2019-06-19; `ILBl12Jm7-0`, Cedros). Cameron's own doctrine is the same shape: **rig the surface-iron outfit, the heavy yo-yo/dropper outfit, and the flyline outfit simultaneously** and switch as the read changes ([`species/yellowtail.md`](species/yellowtail.md), `cameron`).

**The paired alternative.** The species router ranks the structure situation **1) yo-yo iron, 2) [dropper loop](techniques/dropper-loop.md)** — live bait to the same marks on the same heavy-class rod, sinker **6–10 oz**, weight up if the current is heavy ([`techniques/dropper-loop.md`](techniques/dropper-loop.md)). Cameron's stated BOLA-September program is exactly that pair: bottom yellows → dropper loops + yo-yo iron.

## 7. Tackle

**Class terms** — [`tackle/gear-classes.md`](tackle/gear-classes.md) defines the **yo-yo / heavy-iron class** as **~8 ft, XH, 40–80 lb, fast crank**. The yellowtail router's gear summary calls for a **stout 40–60 lb class rod with a high-speed reel** to burn a heavy iron off the bottom.

**Rod.** Heavy jig-stick class with real backbone ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)). Concrete builds in the corpus:
- **7 ft, heavy-action, rated 30–80 lb** (Black Diamond example), with general guidance of **40–60 lb rated** and enough tip left to wind through the bite (Ray Sharifi, `A70kK2niu2Q`, 2022-02-17; unregistered channel — medium confidence). Same rod a year later, an **XH 30–80 lb** (`LTCFjqtSI8g`, 2023-03-29).
- **PCH extra-heavy** rods appear twice — a 7'6" XH at Cedros (`A8SuzB5qiKE`) and an Okuma PCH XH at Tanner Bank (`ntQXxcH5sjI`).
- A **10 ft stick (Phoenix Axis class)** also works if you want to cast the iron and then yo-yo it ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)).
- The 8-ft-over-9-ft preference in [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) is **region-labeled Baja/Sea of Cortez panga reasoning** (short gaffs, small platform) — I'm not carrying it to a Catalina trip as doctrine.

**Reel.** High-torque conventional wound tight — the appeal of yo-yo is a hard, fast retrieve, so **power grind matters more than top gear ratio** ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)). The exception is stated explicitly: for a less-experienced angler who isn't a strong cranker, a **~6.6:1** ratio makes it easier to take line fast enough on the wind-up — retrieve speed beats cranking power for someone still learning (Scotty, Brothers Sportfishing, via Roman Castro, `VpW91AKOFVQ`, 2020-01-28; registered — high confidence). Named reels in the corpus: Shimano Trinidad 20A, Torium 16HG, two-speed lever drags.

**Iron.** **Heavy yo-yo iron — roughly 5–6 oz**, against a surface iron's 2–3 oz (`VpW91AKOFVQ`, registered — high confidence). Heavier is mandatory so it **reaches the zone and stays vertical** in current.
- Benchmarks: **Salas 6X**, **Salas CP 105**, **Salas 6X Jr**, **Tady 4/0**, **Salas 7X Heavy**, heavier CNC irons ([`lures/iron-jigs.md`](lures/iron-jigs.md), [`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)). The species router's structure row names **Salas 6X class** as the heavy full-size default.
- **Change-up:** vertical / flat-fall jigs **100–180 g depending on current** (`D5DR7Kx42_A`).
- **Colors:** the traditional yo-yo yellowtail colors are **scrambled egg** and **blue and white** (`A70kK2niu2Q`), corroborated repeatedly across Cedros/San Benito sessions (`XwwIvPFxRiQ`, `u0scEBby7nA`, `A8SuzB5qiKE`); **dorado** pattern also produces (`XwwIvPFxRiQ`, `ilINTeknKB4`).
- **Downsize when the bait is small** — red crabs, small sardines — instead of the standard heavy class (Ray Sharifi, Cedros, `WE643Fue1_A`). A SoCal instance at San Clemente Island records a downsize drawing a bite with **no stated bait-size reason** (`ecJPMTCi-gw`) — the KB keeps those two side by side rather than merging them.
- **Hooks:** assist vs. treble is a live judgment, not a rule. The argument for **assist hooks on bigger fish**: two points of a treble share one shank and can auger each other back out through a fight, where assists ride on **separated cords** and don't fight each other the same way (`VpW91AKOFVQ`, [`lures/iron-jigs.md`](lures/iron-jigs.md)).

**Line and leader — three documented builds, kept side by side, not reconciled:**

| Build | Main | Top shot / leader | Connection | Source |
|---|---|---|---|---|
| Tanner Bank, SoCal | 65 lb braid | **40 lb fluorocarbon** leader | uni-to-uni | `ntQXxcH5sjI` |
| Cedros, Baja | 65 lb braid | **60 lb straight mono, no fluoro** | — | `A8SuzB5qiKE` |
| Cedros, Baja (same session, different rod) | 60 lb braid | **60 lb fluorocarbon** | — | `A8SuzB5qiKE` |
| Dirty Hookers 2023 build | — | **50–80 yards of mono top shot straight to the jig, no fluoro** | — | `LTCFjqtSI8g` |

The fluoro / no-fluoro split is a genuine unresolved conflict in the corpus — including *within a single session* — so pick one and don't expect the KB to settle it for you.

**A Catalina-flavored line-class caution.** On a boiler-rock yellowtail session the crew fished **30 lb** and, after multiple hookups, a crew member's parting advice was to **go higher than 30 lb for these fish**; the same session had a dropper-loop angler lose a big yellow that "took me to the rocks" (`IwxqgocsQTY`, in [`species/yellowtail.md`](species/yellowtail.md)). Caveat the note itself carries: the location is called "the West End" on camera and is **not confidently placed at Catalina**. Rock-cutoff risk on a hard-bottom bank is real either way — Farnsworth is structure, and a big yellow's first move is down into it.

**Drag.** Set to roughly **a quarter to a third of your lowest line-class rating**. Worked example from the source: 65 lb braid backing to a 40 lb mono top shot → 40 lb is the limiting class → **~10–13 lb strike drag**. **Start at the light end**, not the heavy end — an over-tight drag popping the line the instant a fish comes tight is the common avoidable mistake. If you're in a stalemate and not gaining, bump **one click at a time**; if the fish makes a hard run, let the drag do its job ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md), `VpW91AKOFVQ`, registered — high confidence). One fight-mechanics note from Cedros: **point the rod down** during the fight so slack line comes tight faster (`A8SuzB5qiKE`).

## 8. Your own gear, resolved

Your profile resolves the class cleanly ([`profiles/cameron/rods.md`](profiles/cameron/rods.md), [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md)):

- **Setup 1 — Trinidad 40.** M&M Custom on a Rainshadow RCJB96XH blank: **8'0", XH, 40–80 lb, 4–10 oz**, Shimano Trinidad 40, **80 lb braid**. Its listed role is yo-yo iron / sinker rigs. This is a textbook match to the 8 ft / XH / 40–80 lb yo-yo class, and the 4–10 oz rating covers the 5–6 oz iron with room. Note the profile also records a **relatively soft tip** — consistent with the "enough tip left to wind through the bite" guidance, less so with a pure broomstick.
- **Irons you own:** **Salas 6X** (blue) and **Salas CP 105** (silver/chrome) — both classic heavy yo-yo benchmarks. Against the color doctrine, blue/white is covered; **you have no scrambled egg in the yo-yo box**, and that's the other traditional yellowtail color. Worth adding before a fall Farnsworth trip.
- **Drag math on that rod:** if you're running straight 80 lb braid, the quarter-to-third rule puts strike drag around **20–27 lb**; if you add a lighter mono or fluoro top shot per the builds above, the top shot becomes the limiting class and the number drops accordingly (e.g. a 40 lb top shot → ~10–13 lb).
- **Open item, not doctrine:** you own a **10 ft Phoenix Axis jig stick** you always bring to BOLA and rarely use, and you've said you want reps hooking and landing yellowtail on it — including considering yo-yoing with it. The technique note does allow a 10 ft stick for cast-then-yo-yo of the same iron. Farnsworth in the fall would be a reasonable place to take those reps, but the KB records this as your open item, not as a recommendation.
- **Access:** your profile records you trailer for Catalina (shorter tow vs. a longer crossing) out of Dana Landing, Mission Bay ([`profiles/cameron/spots.md`](profiles/cameron/spots.md)). Boat envelope is in your `boat.md`, which I did not open for this question.

## 9. The failure modes the KB names

From [`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md):

- **Iron too light for the current** — never reaches the mark, or planes off sideways and never fishes vertical. Match iron weight to how hard the water is running. On a bank in real current this is the #1 way the day fails.
- **Winding too slow** — a lazy grind gets refused; the bite comes off speed.
- **Fishing yo-yo when the surface is alive** — if fish are boiling or the kelp is standing (slack current), surface iron reaches more fish.
- **Physical toll, and it can spook cautious fish** — the constant lift-reel-drop cycle punishes arms and shoulders over a long session, and the rapid aggressive action can put off more cautious fish (`ntQXxcH5sjI`, medium confidence).
- **The treadmill tell** — marks on the meter that won't convert, with bait pointing every direction, means no current. Reposition or wait for the change; don't grind drops into dead water.

---

## What the KB does not cover (don't let me paper over these)

- No Farnsworth Bank page at all — **no depth, crest depth, bank size, relief, or bathymetry**.
- **No Farnsworth-specific preferred current directions** — only that standalone banks each have their own, learned spot by spot.
- **No Farnsworth-specific wind or swell fit** — no record of which side is fishable in what wind. The general Catalina doctrine (south swell tears up the east end; big west swell sends you to the east end — `aFb221LUoD0`) is island-scale and I'm not extending it to a bank the KB never places against it.
- **No Farnsworth depth band for where the yellows hold** — every depth number above comes from Tanner Bank, Cedros, San Benito or Mag Bay.
- **No Farnsworth-specific forage note** — no squid, red crab or bait record for the bank.
- **The cadence conflict is unresolved in the KB.** I gave you a decision frame built from what each source says its cadence is *for*; the notes themselves keep continuous-wind and crank-and-drop side by side with no rule for choosing.
- **The fluoro vs. straight-mono top shot question is unresolved**, including within a single recorded session.
- **No yellowtail tide-dependence rating** in the tide table — I applied only the general arrival and window-compression discipline.
- **No SMCA boundary or current take list** — the KB says "see DFW," and the take claim is a single 2022 source.
- The **fall-yo-yo-at-Farnsworth claim rests on one video** (`5p6gu14ZC4w`, 10/26/22), reached through a caption-garble correction.
- **No live conditions were pulled** — you gave none and I made no BightSST call. Step 1 of the day-plan protocol is still outstanding.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/yellowtail.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/surface-iron.md`, `lures/iron-jigs.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/tide-and-slack.md`, `locations/island-structure.md`, `planning/electronics-and-sounder.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`, `sources/extraction-log.md`, `sources/transcripts/_manifest.csv`  
*videos:* `5p6gu14ZC4w`, `D5DR7Kx42_A`, `wzI0lpgKT1U`, `VpW91AKOFVQ`, `ntQXxcH5sjI`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `A8SuzB5qiKE`, `u0scEBby7nA`, `3tQ1_xiqwVU`, `ILBl12Jm7-0`, `ecJPMTCi-gw`, `WE643Fue1_A`, `XwwIvPFxRiQ`, `ilINTeknKB4`, `SH7zOA9ZF3o`, `Qa-j6LIwa1Q`, `IwxqgocsQTY`, `6DzbsElGE7E`, `FEXgl0eQCa8`, `HnqiE05vdXs`, `6TBxHnkYXI0`, `0KQ--N5TjqE`, `h3PTupup17I`, `aFb221LUoD0`, `xI9tPJFXbUM`, `cameron`  
*gaps admitted:* No Farnsworth Bank location page exists in the KB — no depth, crest depth, bank size, relief or bathymetry anywhere. | No record of Farnsworth's own preferred current directions; the KB only says standalone banks each have their own, learned spot by spot. | No Farnsworth-specific wind or swell fit — nothing on which side of the bank fishes in which wind or swell direction. | No depth band for where yellowtail hold at Farnsworth specifically; every depth figure cited comes from Tanner Bank, Cedros, San Benito or Mag Bay. | No forage record for Farnsworth — nothing on squid, red crab or bait presence on the bank. | The retrieve-cadence conflict (continuous full-speed wind vs. Hansen's crank-then-freespool cycling) is explicitly kept side by side and unreconciled in the KB; no rule for choosing is given. | The leader question is unresolved in the corpus — fluorocarbon vs. straight mono top shot conflict appears even within a single recorded session. | The tide-dependence table rates calico, spotted bay bass, white seabass, marlin and bluefin foamers but gives no yellowtail tide relationship. | The Farnsworth SMCA boundary and current take list are not in the KB — the spot list says 'see DFW' and the only take claim (yellowtail and bonito only) is a single 2022-10 source needing CDFW verification. | The 'good fall yo-yo fishing at Farnsworth' claim rests on one video (5p6gu14ZC4w, 10/26/22), reached via a caption-garble correction logged in the extraction log. | No live conditions were used — the user supplied none and no BightSST call was made, so step 1 of the day-plan protocol is unfulfilled. | The Catalina line-class caution (go heavier than 30 lb) comes from a session the note itself says is not confidently placed at Catalina.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

## Fishing a yo-yo iron at Farnsworth Bank

**Envelope first (day-plan protocol step 1b, `planning/day-plan-protocol.md`):** Farnsworth is a Catalina backside bank — `regions: socal-bight`, `waters: island/bank`. Both `techniques/yo-yo-iron.md` and `species/yellowtail.md` pass that gate, so the whole program below is in-region.

**What the KB actually says about Farnsworth specifically — it's thin, so read it first:**
- **Fall yo-yo is the named pattern.** "Farnsworth Bank gives good **fall yo-yo fishing**" (`species/yellowtail.md`, 10/26/22, `5p6gu14ZC4w`). The same source logs ~40 yellows in a day at Catalina in late October, and "no reason you couldn't catch a yellowtail" while temps stay good even outside prime time.
- **It's a partial-take closure — only yellowtail and bonito may be kept** there (`species/yellowtail.md`, `5p6gu14ZC4w`; `sources/spot-lists.md` lists it as "partial-take SMCA — see DFW", 33 20.560 / 118 31.010). The note carries **no jurisdiction stamp or as-of date**, so treat that as unverified: check current CDFW regs for the Farnsworth SMCA before you fish it.
- **Structure type: standalone bank ("Farnsworth type").** `locations/island-structure.md` and `conditions/current-structure.md` use Farnsworth as *the* example of a bank rising off the plain, not attached to land: **it fishes in any current direction**, unlike a land-attached perpendicular ridge that only works on parallel current — but "each individual bank still has its own preferred directions. You learn a standalone bank's good directions spot by spot; there is no single rule." The KB does **not** record what Farnsworth's preferred directions are.

---

### 1. Depth — where to put the jig

The KB gives no charted depth for Farnsworth itself, so work off the marks, not a number:

- **Hard bottom only.** Structure yellows sit exclusively on hard/rocky bottom — "they're not going to be out in the mud" — so read bottom hardness (thin return = sand/mud, thick = rock) before you even look for fish (`species/yellowtail.md`, `6DzbsElGE7E`).
- **The classic structure read: tight balls hugging the structure, arcs/boil-ups at ~5–10 fathoms near structure** (`species/yellowtail.md`, `D5DR7Kx42_A`). That's the row that routes to yo-yo iron: *tight balls on hard bottom or pinnacles → 1) yo-yo iron 2) dropper loop*.
- **Typical yo-yo working bands in the corpus:** 120–180 ft for average 12–30 lb yellows near an island or bank (`techniques/yo-yo-iron.md`, `RNRFrfepiW0`); 120–240 ft as the common depth on overnight/multi-day trips (`UP_3fBu7VPA`).
- **When the school is suspended with no bottom to reference:** get the jig **a little deeper than the depth called**, then wind up through the school at full speed (`techniques/yo-yo-iron.md`, `RNRFrfepiW0`).
- **A depth read that cancels the yo-yo:** fish metering at **40–60 ft** and not yet showing is the "they're coming up" read — that's surface-iron and light-bait water, not yo-yo water (`species/yellowtail.md`, `0DKmYId1NN4`).
- **Fish marked but not boiling still eat.** "Just about every lure that makes it down to the depth that fish is, is a bite," named specifically for yo-yo iron, which that source says has out-fished live bait "multiple times" in exactly that marked-but-not-showing situation (`species/yellowtail.md`, `tpmOYXYQwhU`).
- **Shape beats depth.** A ball stuck to the bottom = present but not hunting (dropper-loop water); fish **up in the column and spread out** are the ones that eat, fish tucked tight to the bottom are not (`species/yellowtail.md`, `HTowqnwAMeA`).

### 2. The retrieve

The core doctrine is one thing: **free-spool to the mark or the bottom, then wind as fast as you can.** The strike is a reaction to the fleeing iron — speed is the trigger, there's no finesse cadence (`techniques/yo-yo-iron.md`).

- Thumb the spool on the drop so the iron falls under light tension and **tracks straight down instead of scoping away** from the boat.
- **Tuck the rod under your left armpit** once the jig hits bottom and the reel is in gear, then crank: "you cannot crank the jig too fast, but it's easy to crank it too slow" (`RNRFrfepiW0`).
- **Do not set the hook — keep cranking through the bite.** "Just keep grinding… that fish is stronger than you and if you just keep winding, he's going to set the hook himself" (`5pbA-wXoric`, `ETw_3AFxEcM`).
- **Bites come on the drop and on the wind-up.** The falling iron on free-spool looks like a dying baitfish; on the sink a bite often reads as a brief stop before the fish takes off with it (`wzI0lpgKT1U`), and one Cedros session called hookups both right on the drop and on the wind-up (`ILBl12Jm7-0`). One bluefin bite read as the rod simply "going heavy… almost like it got stuck on the bottom" (`ntQXxcH5sjI`).

**Cadence is an open conflict in the KB — these are kept side by side, not reconciled** (`techniques/yo-yo-iron.md`). Pick one and fish it honestly; what they share is speed and staying in the band the fish are in:

| Cadence | How it runs | Source |
|---|---|---|
| Continuous wind to the top | Bottom → full-speed all the way up → re-drop | base doctrine, `RNRFrfepiW0` |
| Halfway up, re-drop | In 120–150 ft, wind up only **60–70 ft** off the bottom, then free-spool back down. Saves your arm and keeps the iron in the band the fish hold in | `SAltQjih0ms` |
| Tight-band cycling under the boat | **5–6 quick cranks (~20 ft)**, straight back to free spool, repeat — e.g. in 120–200 ft with fish ~20 ft off the bottom, work the 100–120 ft band | `wzI0lpgKT1U` |
| Cast-and-walk | Cast, sink to bottom, **10 cranks**, free-spool to bottom, repeat in 10-crank increments, walking it back as much as 150 yards | `wzI0lpgKT1U` |
| Two half-depth cranks, then a full wind | Bottom → hard crank halfway → drop → halfway → drop → then all the way up | `SH7zOA9ZF3o` |
| Cast for a ~45° angle | Flip it away from the boat so the line sits ~45° on the wind-back; stated reason is the diagonal path looks more natural. Explicitly a preference — he's seen fish caught both ways | `HTowqnwAMeA` |

**Do not** work it with short hops right at the bottom — that's named as the wrong motion, and it's what draws rockfish instead of yellowtail (`SAltQjih0ms`). And don't stop it inside a marked school to jig it in place: that spooks fish and the rest of the school follows the ones that leave; bounce it on the bottom or burn it up instead (`6Z6Dht20kTA`).

**Readiness matters as much as jig choice** — a school may only hold under the boat for **5–10 seconds** in an otherwise long search, so be rigged and ready to drop the instant marks show (`UP_3fBu7VPA`).

### 3. Current — the part that decides whether Farnsworth fishes at all

- **Standalone bank = fishes any direction, but with its own preferred directions** (`locations/island-structure.md`). Since the KB doesn't record Farnsworth's, you'll have to build that record yourself — the KB's own advice is to keep a per-spot log of which wind and which current direction each spot produces on (`conditions/current-structure.md`, `xI9tPJFXbUM`).
- **Bias the up-current face.** Upwelling forms where current impinges on structure, so nutrients — and the food chain — stack on the up-current face under whatever vector is running that day (`conditions/current-structure.md`).
- **Position the boat up-current of the mark** so the drop sweeps down onto the structure (`techniques/yo-yo-iron.md`).
- **Reading strength:** kelp lean is the gauge — kelp pulled ~20 ft under = raging (surface presentations dead, go deep/weighted); laid flat = strong; resurfacing = slacking, switch back to surface iron (`conditions/current-diagnostics.md`, `HnqiE05vdXs`). On a hard, kelp-free rock with no buoys there's **no visual tell** — the stated method is to drop the anchor and watch which way the line points once it sets, and expect to pull and reset (that source resets **10–12 times in a day** on his own skiff) (`conditions/current-diagnostics.md`, `sIoNELGlxmk`). On the drift, read the **chum-line angle against how the boat lies**: straight back = wind-dominated, swinging off at an angle = real current.
- **A chart plotter's current-arrow layer is reading wind, not current** — confirm with kelp lean or chum drift (`conditions/current-diagnostics.md`, `BskCsKaTiZw`).
- **No current = "the treadmill is off":** bait pointing in all directions and fish metering but not biting. Marks will not convert — move or wait for the change (`conditions/current-diagnostics.md`). Timing: be on the highest-percentage zone **an hour before** the tide change, not at it (`conditions/tide-and-slack.md`).
- **Fix line scope.** Once the line pulls off vertical, bite feel drops and slack builds between rod tip and jig. Either wind it in and drop it back down, or (kept side by side) flick it a little further up-swell so the boat drifts onto it as it sinks (`conditions/current-diagnostics.md`, `Vbf40qvH9-Q`, `sJGs-Jqt9Vo`).
- **Current sets jig weight — and it's a time budget, not just an action argument:** light current and nice weather → smaller jig; wind or strong current → upsize, because "you don't want to spend the majority of your time in free spool waiting for your lure to hit bottom" (`techniques/yo-yo-iron.md`, `HTowqnwAMeA`).
- **Hard wind is a re-rank toward yo-yo, not away from it.** At the Coronados in 25 kt gusts, fish that had been surface fish went deep and the whole fleet went "mostly yo-yo" — the surface iron still picked two, so keep one going (`species/yellowtail.md`, `ejUTAnONf7o`).
- **Catalina-side planning input:** a big west swell is the trigger to fish the **east end**; a south swell tears up the east end and makes it hard to fish (`locations/island-structure.md`, `aFb221LUoD0`). Also worth knowing for the run out: at Catalina's **~500-fathom curve** the uphill current compresses, spins eddies, and aggregates bait and paddies — the curve is a line you can hunt on the way (`locations/island-structure.md`, `HnqiE05vdXs`).

### 4. Tackle

**Class terms** (`tackle/gear-classes.md`, `species/yellowtail.md`): yo-yo / heavy-iron class — **~8 ft, XH, 40–80 lb, fast crank**, i.e. a stout 40–60 lb rod with a high-speed reel to burn a heavy iron off the bottom.

Specific builds the corpus gives, for the 12–30 lb grade you'd expect at Catalina in 120–180 ft (`techniques/yo-yo-iron.md`):

- **Rod:** 8 ft, **30–60 lb** rated all-around — no specialty rod needed (`RNRFrfepiW0`). Other data points: a 7 ft heavy-action **30–80 lb** (`A70kK2niu2Q`); a short stout **40/50/60 lb** rod (`hteLeDIy9Qs`); 7–7.5/8 ft rated 30–60, 30–80, or as heavy as 40–100 (`ETw_3AFxEcM`); a 7 ft stiffer-tipped-than-a-flyline-stick on a live-bait reel (`SAltQjih0ms`).
- **Reel:** two-speed conventional, **Penn Fathom 30/40-class** — high gear to wind the jig back fast, low gear to work a hooked fish out of structure (`RNRFrfepiW0`, `UP_3fBu7VPA`). Run **high gear while searching, shift to low only after the fish is hooked and settled** (`SAltQjih0ms`). What matters is line recovered per turn, not raw power: a Penn Torque 40 is named for **43 in per handle rotation** (`7Ljt-DeFVcs`); a **~6.6:1** ratio is the pick for anglers who aren't strong crankers (`VpW91AKOFVQ`).
- **Line:** **65 lb braid + a 50-yard, 40–50 lb mono top shot** — the mono gives stretch and helps when a hooked fish tangles a neighbor's line (`RNRFrfepiW0`). Floor and preference: **40 lb minimum, 50–60 lb preferred** (`UP_3fBu7VPA`); "40 works, 50 is better, 60 better still, because the fish don't care" (`5pbA-wXoric`). Also logged: 80 lb braid to a 40–60 lb mono top shot, **no fluorocarbon**, iron tied straight to the top shot on a [San Diego jam knot](`rigging/san-diego-jam-knot.md`) (`SAltQjih0ms`). If you *do* run fluoro, put a **short piece of mono between the braid and the short fluoro leader** — going straight from spectra to fluoro with no buffer bends and pulls hooks (`hteLeDIy9Qs`).
- **Iron:** heavy yo-yo class — **Salas 6X / Salas CP 105** benchmarks, roughly **5–6 oz** against a surface iron's 2–3 oz, heavy enough to sink fast and hold vertical (`lures/iron-jigs.md`, `VpW91AKOFVQ`). Sizing by depth: **150–250 ft → full-size 6X-class**; shallower, or when getting down fast matters less → **6X Jr or a Tady 40-class** (`UP_3fBu7VPA`). A three-tier version: 60/80/100 ft → smaller jig; **120–150 ft → Salas 6X (~5–6 oz)**; real deep → a **7X heavy** (`hteLeDIy9Qs`). The Tady 4/0 is named as a year-in-year-out top yo-yo producer (`RNRFrfepiW0`, `ETw_3AFxEcM`).
- **Colors:** the classics — **scrambled egg, blue and white, mint**, with the stated mechanism: **blue and white when they're eating thin baits (anchovy, sardine), scrambled egg when they're on invertebrates (squid or crab)**; mint has no stated forage reason, it just gets bit (`ETw_3AFxEcM`). **Red-toned jigs during red-crab years** — match forage color to the bait present (`UP_3fBu7VPA`, `RNRFrfepiW0`).
- **Hook:** a **treble typically works best for yellowtail** (`lures/iron-jigs.md`, `3g82igEL8yk`); assist hooks on separated cords are the bigger-fish/bluefin answer, because two points of a treble sharing one shank can auger each other out (`VpW91AKOFVQ`).

**Against your profile (`profiles/cameron/rods.md`, `profiles/cameron/tackle.md`):**
- **Setup 1, the Trinidad 40** is already your yo-yo rod — M&M custom on a Rainshadow RCJB96XH, **8'0", XH, 40–80 lb, 4–10 oz**, 80 lb braid. That sits right on the class spec; the corpus builds run a **40–60 lb mono top shot** over that braid, which is the piece to set up before the run.
- **Irons you own:** **Salas 6X (blue)** and **Salas CP 105 (silver/chrome)** — both squarely in the heavy yo-yo class for a 120–180 ft band.
- **Gaps to name rather than paper over:** you have **no scrambled-egg, mint, or red-toned yo-yo iron** — your scrambled-egg irons (Squidco Candy Bar SR Lite, JRI-5) are surface irons, and scrambled egg is the color the corpus wants when yellows are on **squid or crab**, which is exactly the fall Catalina forage case. No **Tady 4/0** and no **7X heavy** in the box either, so if the current is running hard enough that the 6X won't hold vertical you have no heavier step to go to.
- Open item from your own profile: you own a **10 ft Phenix Axis jig stick** and have wanted reps yo-yoing with it — the KB does note a 10 ft stick works for casting-then-yo-yoing the same iron (`techniques/yo-yo-iron.md`), which fits the ~45° cast-it-out cadence above.

### 5. Failure modes to watch for

- **Iron too light for the current** — never reaches the mark or planes off sideways (`techniques/yo-yo-iron.md`).
- **Winding too slow** — a lazy grind gets refused.
- **Fishing yo-yo while the surface is alive** — if fish are boiling or the kelp is standing (slack current), surface iron reaches more fish.
- **Bycatch owning the column.** A yellowtail day planned around yo-yo and surface iron was lost to **bonito intercepting the jig**; the fix wasn't a different iron or a different speed, it was to stop fishing metal — dead sardines turned the bite (`Ob45hK4HSWc`). Worth naming because the reflex is to change jig weight, and that doesn't address an interception problem.
- **Bite-rate calibration** so you don't misread the day: on the SoCal local coast, a **good day is three or four bites** — two fishless hours is not evidence the technique is wrong (`species/yellowtail.md`, `HTowqnwAMeA`).

### 6. What the KB does not cover

- **No charted depth, no bottom profile, and no pinnacle-top depth for Farnsworth Bank** — the only Farnsworth data in the KB is the coordinate (33 20.560 / 118 31.010, `sources/spot-lists.md`), the "standalone bank" typology, the fall yo-yo line, and the closure. Nothing on where on the bank to set up.
- **No preferred current or wind directions for Farnsworth specifically.** The KB says every standalone bank has them and that you learn them spot by spot — it doesn't tell you Farnsworth's.
- **No stamped regulation.** The keep-yellowtail-and-bonito-only rule has no jurisdiction or as-of date in-note. Verify with CDFW before you fish it.
- I have no live conditions here — you gave none and I don't pull BightSST — so nothing above is weighted to today's water, temp, chlorophyll, wind, swell or tide. Step 1 of `planning/day-plan-protocol.md` still needs doing before this becomes a plan.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/yo-yo-iron.md`, `species/yellowtail.md`, `lures/iron-jigs.md`, `tackle/gear-classes.md`, `locations/island-structure.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/tide-and-slack.md`, `seasonal/october.md`, `sources/spot-lists.md`, `sources/extraction-log.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`  
*videos:* `5p6gu14ZC4w`, `RNRFrfepiW0`, `5pbA-wXoric`, `UP_3fBu7VPA`, `ETw_3AFxEcM`, `hteLeDIy9Qs`, `SAltQjih0ms`, `wzI0lpgKT1U`, `HTowqnwAMeA`, `VpW91AKOFVQ`, `7Ljt-DeFVcs`, `A70kK2niu2Q`, `ntQXxcH5sjI`, `tpmOYXYQwhU`, `0DKmYId1NN4`, `D5DR7Kx42_A`, `6DzbsElGE7E`, `ejUTAnONf7o`, `Ob45hK4HSWc`, `3g82igEL8yk`, `SH7zOA9ZF3o`, `ILBl12Jm7-0`, `6Z6Dht20kTA`, `Vbf40qvH9-Q`, `sJGs-Jqt9Vo`, `sIoNELGlxmk`, `BskCsKaTiZw`, `xI9tPJFXbUM`, `HnqiE05vdXs`, `aFb221LUoD0`, `cameron`  
*gaps admitted:* No charted depth, bottom profile, or pinnacle-top depth for Farnsworth Bank anywhere in the KB — only the coordinate (33 20.560 / 118 31.010) from sources/spot-lists.md. | No Farnsworth-specific preferred current directions; the KB only says standalone banks have their own and must be learned spot by spot. | No Farnsworth-specific preferred wind or swell fit; the Catalina swell/wind guidance in locations/island-structure.md is east-end vs front/back/middle only. | The Farnsworth closure claim (yellowtail and bonito only may be kept) carries no jurisdiction or as-of date in-note — unverified, must be checked against current CDFW rules. | No Farnsworth-specific jig weight, color, or depth data point — all yo-yo depth bands and jig sizes cited are general or from other locations (Catalina generally, Coronados, Cedros, San Benito, Alijos). | No live conditions were supplied and none were pulled (no BightSST), so nothing in the answer is weighted to today's SST, chlorophyll, wind, swell, current or tide. | No seasonal note in the KB gives a Catalina-backside or Farnsworth-specific fall yellowtail timing window beyond the single 'good fall yo-yo fishing' line. | The KB does not record whether Farnsworth holds kelp, so the kelp-lean current gauge may not be usable there; only the anchor-line and chum-drift reads are offered as alternatives.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short version

The KB will get you a good yo-yo program at Farnsworth, but you should know up front where the knowledge is thin: **Farnsworth Bank has no spot page in this KB** (`locations/farnsworth-bank.md` was never written — `locations/catalina-island-backside.md` says so explicitly, and the worklist row in `sources/review-worklist.md` is `escalated`). So there are **no charted depths, no bottom composition, and no preferred current directions for this specific bank** anywhere in here. What follows is the bank-level context the KB does carry, plus the general yo-yo doctrine from `techniques/yo-yo-iron.md`, and I've flagged every place where I'm handing you a general rule instead of a Farnsworth-specific one.

---

## 1. What the KB says about Farnsworth itself

- **Position: 33 20.560 / 118 31.010** — from the spot library, `sources/spot-lists.md` (Catalina backside section), quoted again in `locations/catalina-island-backside.md`. That's the charted position you'd feed to BightSST for a per-spot SST/chlorophyll pull.
- **It is a standalone bank, not shoreline** (`locations/catalina-island-backside.md`, `locations/island-structure.md`). It's the named example of that structure class in this KB.
- **It is the fall yo-yo call.** `locations/catalina-island-backside.md` lists yellowtail for this zone as "fall, while water temperatures hold," with Farnsworth as the fall **yo-yo** call (`5p6gu14ZC4w`). `species/evidence/yellowtail.md` carries the same line: Farnsworth "gives good fall yo-yo fishing." **Caveat carried in the note:** that row has a standing fact-check flag — the source states the temperature half with an explicit negative the row drops: "the water temperatures still look pretty good at cats so there's no reason you couldn't catch Yellow Tail **but I don't it's not really a prime time a year to go there and catch one**." So treat "fall yo-yo call" as a real but hedged single-source claim from one 2022-10-26 report.
- **Regulations — read this before you go.** Inside the closure area **only yellowtail and bonito may be kept; everything else goes back** (`5p6gu14ZC4w`, as of 2022-10, logged in `sources/regulatory-claims.md`). That's convenient for a yo-yo trip since yellowtail is exactly what you're throwing at — but rockfish, bass and whitefish are all release-only. The note flags that the source says only "Marine closure," names no agency and no boundary (the auto-caption even garbles the bank name to "foreign First Bank"), and that the spot library's "partial-take SMCA" label is Cameron's, not the source's. **California / CDFW — verify the current MPA boundary and take rules with CDFW before fishing.**

---

## 2. Depth

**The KB does not give a depth for Farnsworth Bank.** `locations/catalina-island-backside.md` carries `depth_band: unknown` and an explicit flagged gap: "no corpus source: charted depths, bottom composition, kelp extent and working depth bands for the individual backside spots." The only worked depth on that whole side of the island is an unrelated 32 ft anchor set at West Cove (`sIoNELGlxmk`).

So you fish it off the meter, using the general yo-yo depth ladder from `techniques/yo-yo-iron.md`:

**Jig size by depth** (the technique note's ladder):
- **60 / 80 / 100 ft** — smaller jig, Salas 6X Jr class.
- **120–150 ft** — Salas 6X, roughly **5–6 oz** (against a surface iron's 2–3 oz) (`VpW91AKOFVQ`).
- **150–250 ft** — full-size 6X-class iron (`UP_3fBu7VPA`).
- **Real deep** (Colonet, "the ridge," Alijos, Guadalupe) — 7X-heavy (`hteLeDIy9Qs`).
- Overnight/multi-day yo-yo depth commonly runs **120–240 ft** (`UP_3fBu7VPA`).

⚠ **Known internal conflict, kept side by side, not reconciled:** `species/yellowtail.md` states the same ladder as a **current**-keyed rule at different weights — "full-size (Salas 6X class, **8 oz**) in stronger current, 6X Jr (**4 oz**) when it's light" — and `techniques/yo-yo-iron.md` keys 6X vs 6X Jr to **depth** and puts the 6X at 5–6 oz. Neither the 8 oz nor the 4 oz figure appears in the technique note. Both notes carry the flag. My read for you: size by whichever is binding on the day — if you can't get down and stay vertical, upsize regardless of what the depth ladder says.

**Depth on the meter — what you're looking for** (`species/yellowtail.md`, Finding them):
- Structure yellowtail mark as **tight balls hugging hard bottom**, given as arcs and boil-ups at **~5–10 fathoms (30–60 ft) near pinnacles and high spots** (`D5DR7Kx42_A`). ⚠ That note flags this: the source supports only "tight balls of yellowtails sometimes hugging the structure" — **the 5–10 fathom figure is not in the transcript**. Don't plan the day around that number.
- **Grade the bottom before hunting fish:** thin return = sand/mud, thick return = rock, and the fish hold on rock (`6DzbsElGE7E`).
- **Marks at 40–60 ft that aren't showing are staging fish — surface-iron and light-bait fish, not yo-yo fish** (`0DKmYId1NN4`). Don't burn a heavy iron through them; when they boil, go all-in on surface iron.
- **Fish balled tight to the bottom** = present but not feeding — that's dropper-loop water, and worth a yo-yo burned past them for the reaction strike (`HTowqnwAMeA`). Fish spread up through the column are hunting — flyline/slow-troll them instead.
- When a school is called with no bottom to mark against, **get the jig a little deeper than the depth called, then wind it up through the school at full speed** (`RNRFrfepiW0`).
- A school may hold under the boat for only **5–10 seconds** — being rigged and ready to drop matters as much as jig choice (`UP_3fBu7VPA`).

---

## 3. Current

This is where Farnsworth's structure class actually earns you something.

**Standalone banks fish in any current direction** — they sit off the island with open water on every side, unlike the land-attached perpendicular ridges along the Catalina shore, which only produce on current running **parallel** to the shoreline (`locations/island-structure.md`, `conditions/current-structure.md`, `6TBxHnkYXI0`). `locations/catalina-island-backside.md` makes the point directly: Farnsworth "is the one spot in this zone whose read does not start from the island's shoreline orientation." So when the day's set kills Salta Verde, China Point and the ridges, Farnsworth is still on the table.

**But:** the same notes say **each standalone bank has its own preferred directions, learned spot by spot — there is no single rule**, and **the KB does not record Farnsworth's preferred directions.** That's a real gap; you'd be learning it yourself.

**Where on the bank:** bias toward the **up-current face** — that's where nutrients get forced up and the food chain stacks (`conditions/current-structure.md`, `h3PTupup17I`). Under a summer uphill (counter)current that's the lower end of the banks.

**Reading current with no kelp to read.** Farnsworth is a bank, not a kelp bed, so the kelp-lean gauge may not be available. `conditions/current-diagnostics.md` gives the substitutes:
- **Anchor-line read** — called out specifically for kelp-free yellowtail/seabass rock structure: drop the anchor and watch which way the line settles; it points the way the current runs. Expect to reset — one presenter resets 10–12 times a day on his own skiff to stay on the spot, framed as a normal cost, not a bad read (`sIoNELGlxmk`).
- **Chum-drift angle vs. the boat's lay** separates true current from wind push; chum swinging off at an angle to the boat's lay is real current cutting across (`6TBxHnkYXI0`). **A chart plotter's current-arrow layer reads wind, not current** (`BskCsKaTiZw`) — don't trust it.
- **If you do have kelp on the bank:** pulled ~20 ft under = raging, surface is dead, go deep/weighted; laid flat = strong, work the down-current side; resurfacing = slacking, switch back to surface iron (`HnqiE05vdXs`). Watch the kelp, not the clock.
- **"Treadmill off"** — bait pointing every direction and marks that won't convert means no current; reposition or wait for the tide change (`6TBxHnkYXI0`). Note `conditions/current-structure.md` also states current and tide are **independent** — don't assume a tide swing gives you current.

**Current → presentation call:**
- Hard current that has pulled the kelp under or laid it flat = **the trigger to go vertical** (`techniques/yo-yo-iron.md`). When the kelp resurfaces, switch back to `techniques/surface-iron.md`.
- **Hard wind (20–25 kt+) after a run of surface days, fish metered but not showing:** the fleet bite goes mostly yo-yo, with surface iron still picking a fish — a re-rank, not an abandonment (`species/yellowtail.md`, `ejUTAnONf7o`).
- **Under-sizing the iron for the current costs working time, not just action** — a jig too light spends most of its retrieve in free spool waiting to hit bottom instead of working the zone (`HTowqnwAMeA`). Stated rule: light current + nice weather → small jig; wind or strong current → upsize.
- **Line scope:** free-spool with your thumb on the spool so the iron tracks straight down instead of scoping away from the boat. If it scopes out, wind it in and redrop to reset vertical; if the drift is too strong to wind in, **flick it further up-swell** so it lands back near vertical by the time it reaches bottom (`conditions/current-diagnostics.md`, `Vbf40qvH9-Q`, `sJGs-Jqt9Vo`). Position up-current of the mark so the drop sweeps down onto the structure.

**Side selection, upstream of all this:** Catalina's backside is the **weather side** — prevailing wind, current and swell out of the west (`aFb221LUoD0`), and when the West End is blowing it gets worse the further back you run (`PKf7G3uL4io`). Read swell direction before you pick the spot. Rounding the east end onto that side crosses a slop hotspot off the ridge that lays down 3–4 mi past it. ⚠ Flagged gap: the KB has **no run distance or run time from any mainland port** to this side, and no sea-state envelope for the crossing.

---

## 4. The retrieve

From `techniques/yo-yo-iron.md`:

**Base retrieve — one motion.** Free-spool the iron straight to the mark or the bottom, thumbing the spool so it falls under light tension and tracks vertical. Then **wind as fast as you can, all the way up**. The fleeing iron's speed is the strike trigger, not a cadence. Nothing hits — drop back and rip it again.

- **Tuck the rod under your arm** once the jig hits and the reel is in gear, then crank. **The jig cannot be cranked too fast, only too slow** (`RNRFrfepiW0`).
- **Start winding the instant it touches, and never let it sit.** The most common yo-yo error is settling into position first; a jig left on the bottom gets picked up by ocean whitefish, small cod and other bottom critters before a yellowtail finds it (`8XIy7hPsFkQ`). At Farnsworth that error costs you double — whitefish and cod are release-only inside the closure.
- **Don't swing to set the hook.** Keep cranking; the continuous full-speed wind drives the hookset (`5pbA-wXoric`, `ETw_3AFxEcM`, `hteLeDIy9Qs`, `SAltQjih0ms`).
- **Do not work the iron in short hops right at the bottom** — that motion draws rockfish instead of yellowtail (`SAltQjih0ms`). Again, rockfish are release-only here.
- **Ready-position grip through the drop** — index finger on the spool, thumb on the trigger, left hand forward — so the gear-and-crank on a bite is instant. On the drop a bite often reads as a **brief stop** before the fish takes off with it (`wzI0lpgKT1U`).
- **Strikes come on the drop as well as the wind** — the falling iron on freespool looks like a dying baitfish (`wzI0lpgKT1U`, `ILBl12Jm7-0`). Work the whole cycle.

**Cadence variants** — the KB keeps these side by side rather than picking one:
- **Working water:** free-spool to bottom, 10 fast cranks, freespool back down, repeat while walking the iron toward the boat over as much as **150 yd** (`wzI0lpgKT1U`).
- **Straight up-and-down under the boat:** **5–6 quick cranks (~20 ft)**, freespool back down, cycling the band where fish are marked — e.g. working the 100–120 ft band on marks at 120 ft in 120–200 ft of water, fish suspended ~20 ft off the bottom (`wzI0lpgKT1U`).
- **Half-depth wind:** free-spool to bottom, crank hard only about halfway — in 120–150 ft, wind up 60–70 ft off the bottom — then drop back. Saves your arm and keeps the iron in the band near the bottom where the fish hold (`SAltQjih0ms`).
- **45° cast instead of straight down:** for yellowtail, casting or flipping the iron away from the boat so the line sits at roughly 45° on the wind-back reads as more natural because of the diagonal path. Fish are taken both ways — a stated preference with a mechanism, not a correction (`HTowqnwAMeA`).

**Colour** — follows forage, not a fixed favourite (`ETw_3AFxEcM`):
- **Blue and white** when they're on thin baitfish (anchovy, sardine).
- **Scrambled egg** when they're on invertebrates — squid or crabs.
- **Mint** is a third go-to with no stated forage reason. **Red-toned** jigs produce specifically in red-crab years (`UP_3fBu7VPA`, `RNRFrfepiW0`). All red is named alongside blue/white and scrambled egg as one of the three most reached for (`HTowqnwAMeA`).
- **Downsize to match small forage** — on red crabs or small sardines, drop to a smaller/lighter yo-yo jig, including a brass-finish iron (`WE643Fue1_A`).

**Failure modes to avoid** (same note):
- Iron too light for the current — never reaches the mark or planes off sideways.
- Winding too slow — a lazy grind gets refused.
- Fishing yo-yo when the surface is alive — if fish are boiling or the kelp is standing, surface iron reaches more fish.
- **Continuous active jigging inside a marked school spooks and disperses it.** Fix: let it reach bottom and bounce it there, or burn it up on a fast continuous retrieve (`6Z6Dht20kTA`, `S0-BCQWA0H4`). A heavy mark at the thermocline may not be a cohesive school at all — casting through and ripping the jig stirs them into chasing (`SH5CZQi9ATw`).
- **A bycatch species owning the column masks itself as a jig problem.** One yellowtail day planned around yo-yo and surface iron was abandoned to bonito bycatch; switching to dead sardines — not a different jig — restarted the yellowtail bite (`Ob45hK4HSWc`). Worth knowing at Farnsworth specifically, since bonito is the *other* keepable species there and the backside is called "mostly against Bonita, bass and Rockfish" by late October (`5p6gu14ZC4w`).
- The lift-reel-drop cycle is physically demanding over a long session, and the aggressive action can spook more cautious fish (`ntQXxcH5sjI`).

---

## 5. Tackle

**Class terms** (`tackle/gear-classes.md`, `techniques/yo-yo-iron.md`, `species/yellowtail.md`):
- **Rod:** yo-yo / heavy-iron class — **~8 ft, XH, 40–80 lb, fast crank**. Real backbone.
- **Reel:** high-torque conventional wound tight. Power grind matters more than top gear ratio, but for anglers who aren't strong crankers a **~6.6:1** reel makes it easier to take line fast enough (`VpW91AKOFVQ`). One concrete build: Penn Torque 40 on a 40–100 lb rod, picked for **43 in of line per handle turn** (`7Ljt-DeFVcs`) — ⚠ flagged single-source.
- **Line:** fish as heavy as you can still crank fast and control the fish — **40 lb works, 50 lb is better, 60 lb better still** (`5pbA-wXoric`, `UP_3fBu7VPA`). ⚠ Flagged: the "bite rate is unaffected by line diameter" mechanism is `5pbA-wXoric` only; `UP_3fBu7VPA` states only a personal floor ("I wouldn't do any less than 40 lb").
- **Leader:** run a **short piece of mono between the braid and a short fluoro leader** for stretch. Braid straight to a short fluoro leader with no buffer bends hooks and pulls fish (`hteLeDIy9Qs`).
- **Iron:** heavy yo-yo class — **Salas 6X / Salas CP 105 / Tady 4/0** type (`lures/iron-jigs.md`).
- **Hooks:** treble or single assists on separated cords. Assists are favoured on bigger fish because two points of a treble share one shank and can auger each other out through a fight (`VpW91AKOFVQ`).

**Named builds the KB carries, kept side by side (order is not a ranking):**
- **Base case — 12–30 lb yellowtail near an island or bank in 120–180 ft** (this is the closest match to a Farnsworth trip): two-speed Penn Fathom 30, 65 lb braid, a **50-yard 40–50 lb mono top shot**, an 8 ft 30–60 lb rod, a treble hook, a **Tady 4/0** (`RNRFrfepiW0`).
- **Recreational base build:** two-speed conventional, 80 lb braid to a 40–60 lb mono top shot, no fluoro, tied straight to the iron on a San Diego jam knot, on a 7 ft rod stiffer than a flyline stick. High gear while searching for the fastest wind-up, low gear only once a fish is settled into the fight (`SAltQjih0ms`).
- **50 lb short, stout rod** rated 40/50/60 lb, with the mono-buffer leader above (`hteLeDIy9Qs`).

**Against your own box** (`profiles/cameron/rods.md`, `profiles/cameron/tackle.md`):
- **Setup 1, the Trinidad 40** is your yo-yo rig and it's a clean class match: M&M custom on a Rainshadow RCJB96XH blank — **8'0", XH, 40–80 lb, 4–10 oz** — Shimano Trinidad 40, **80 lb braid**. Its role is listed as yo-yo iron first. That 4–10 oz rating covers the whole 5–6 oz 6X band and the heavier tier if the current is up.
- **Irons owned:** **Salas 6X (blue)** and **Salas CP 105 (silver/chrome)** — both the classic heavy yo-yo benchmarks.
- **Gaps I'd name rather than substitute around:**
  - **No 6X Jr or other light yo-yo iron in your inventory.** If Farnsworth fishes shallow (60–100 ft) or the current is light, the ladder wants a 6X Jr and you don't have one. Same for the **downsize-to-small-forage** call on red crabs or small sardines — no smaller/brass-finish yo-yo iron is listed.
  - **No scrambled-egg or red yo-yo iron.** You have blue and chrome. Blue/white covers the thin-baitfish case; if they're on squid or crabs the KB's colour doctrine wants scrambled egg, and in a red-crab year, red.
  - **Top shot / leader isn't recorded.** Your rods note says the braid weight listed is the max you'll put on that rod and that top shots change per application — so the mono-buffer-plus-short-fluoro rule from `hteLeDIy9Qs`, or a 40–60 lb mono top shot, is a build decision you'd still make on the day.
  - **The 10 ft jig stick is an open item, not doctrine.** Your tackle note records that you own a 10 ft Phenix/Phoenix Axis jig stick, rarely use it, and are *considering* yo-yoing with it; `techniques/yo-yo-iron.md` carries the matching cameron line that a 10 ft stick works for casting-then-yo-yoing the same iron. Captured as an attributed open item — not something the KB asserts as the better tool.
- **Boat envelope: I can't check it.** `profiles/cameron/boat.md` has `range_nm: null` and `sea_state_max_ft: null` — the protocol says to **ask** rather than assume. The Panga Marine Marquesas 22 tops out ~35 kt with a 115 hp Yamaha, but I have no stated range or sea-state ceiling, and the KB has no run distance from any mainland port to Catalina's backside. On the weather side of the island in the fall, that's the piece I'd want nailed down before committing.

---

## What I'd actually do

Go on a day the swell isn't out of the west, pull SST/chlorophyll for 33 20.560 / 118 31.010, and treat the bank as a "fishes on any current direction" mark — meaning it stays on the list when the shoreline ridges are dead. Get on top of it, grade the bottom (thick return = rock), find the balls hugging structure, and position up-current so the drop sweeps onto the mark. Trinidad 40, Salas 6X in blue, mono buffer to a short fluoro leader. Free-spool with your thumb on it, start winding the instant it touches, full speed to the top, drop back. If your arm gives out before the fish do, go to the half-depth wind — bottom, hard crank 60–70 ft up, drop back. Upsize to the CP 105 the moment the iron isn't getting down or is planing off sideways. And everything except a yellowtail or a bonito goes back — verify the current closure boundary with CDFW first.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/yo-yo-iron.md`, `locations/catalina-island-backside.md`, `locations/evidence/catalina-island-backside.md`, `locations/island-structure.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `species/yellowtail.md`, `species/evidence/yellowtail.md`, `species/bonito.md`, `lures/iron-jigs.md`, `tackle/gear-classes.md`, `sources/spot-lists.md`, `sources/regulatory-claims.md`, `sources/review-worklist.md`, `sources/escalations.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/boat.md`, `seasonal/october.md`, `locations/socal-bight.md`  
*videos:* `5p6gu14ZC4w`, `6TBxHnkYXI0`, `ETw_3AFxEcM`, `5pbA-wXoric`, `hteLeDIy9Qs`, `SAltQjih0ms`, `RNRFrfepiW0`, `8XIy7hPsFkQ`, `HTowqnwAMeA`, `wzI0lpgKT1U`, `VpW91AKOFVQ`, `UP_3fBu7VPA`, `WE643Fue1_A`, `7Ljt-DeFVcs`, `6Z6Dht20kTA`, `S0-BCQWA0H4`, `SH5CZQi9ATw`, `ntQXxcH5sjI`, `Ob45hK4HSWc`, `HnqiE05vdXs`, `Vbf40qvH9-Q`, `sJGs-Jqt9Vo`, `sIoNELGlxmk`, `D5DR7Kx42_A`, `6DzbsElGE7E`, `0DKmYId1NN4`, `ejUTAnONf7o`, `aFb221LUoD0`, `PKf7G3uL4io`, `BskCsKaTiZw`, `h3PTupup17I`, `ILBl12Jm7-0`  
*gaps admitted:* Farnsworth Bank has no spot page in this KB — locations/farnsworth-bank.md was never written (worklist row is `escalated` in sources/review-worklist.md; escalation logged 2026-08-29 in sources/escalations.md), so there is no dedicated note carrying its structure, depths or program. | No charted depth or depth band for Farnsworth Bank anywhere in the KB — locations/catalina-island-backside.md carries `depth_band: unknown` and an explicit flagged gap for charted depths, bottom composition, kelp extent and working depth bands on all backside spots. Every depth number I gave is general yo-yo doctrine, not Farnsworth-specific. | No bottom composition for Farnsworth Bank (rock vs. sand, pinnacle vs. flat crest) — you have to grade it on the sounder yourself. | Farnsworth's own preferred current directions are not recorded. The KB says standalone banks fish on any current direction but each has its own preferred directions 'learned spot by spot — there is no single rule', and never states which directions Farnsworth prefers. | No run distance or run time from any mainland port (Long Beach, Newport, Dana Point, San Pedro) to Catalina's backside, and no sea-state envelope for the crossing — explicitly flagged as a gap in locations/catalina-island-backside.md. | No yellowtail zone guide for Catalina exists — species/yellowtail.md lists Catalina as a flagged stub with material only parked in the evidence file, so there is no trip-level 'what a day at Farnsworth looks like' note. | No Farnsworth-specific jig size, colour, retrieve cadence or line class — every tackle and retrieve parameter I gave comes from general yo-yo iron doctrine or other zones (Coronados, Cortez Bank, Baja, long-range), not from a Farnsworth source. | No season window for Farnsworth beyond a single hedged 2022-10-26 report calling it the fall yo-yo call — and that same source explicitly says fall is 'not really a prime time of year' for Catalina yellowtail. | The Farnsworth closure claim rests on one 2022-10-26 fishing report that names no agency, no MPA designation and no boundary, and garbles the bank's name in the captions; the 'partial-take SMCA' label comes from Cameron's spot library, not a regulator. Jurisdiction, boundary coordinates and current take rules are unverified — check CDFW. | Unresolved internal conflict on yo-yo jig sizing: techniques/yo-yo-iron.md sizes Salas 6X vs 6X Jr by depth (6X at roughly 5-6 oz); species/yellowtail.md sizes the same jigs by current at 8 oz / 4 oz. Both notes carry the flag; the KB does not reconcile them. | The ~5-10 fathom yellowtail sonar signature is flagged contradicted-by-source in species/yellowtail.md — the cited transcript carries no depth figure at all, so there is no reliable KB depth for where structure yellowtail mark. | Cameron's boat envelope is unusable for gating this trip: profiles/cameron/boat.md has range_nm and sea_state_max_ft both null, and the protocol says to ask rather than assume. | Cameron's inventory has no 6X Jr or other light/small yo-yo iron and no scrambled-egg or red yo-yo iron, so the KB's light-current, shallow-water and small-forage downsize calls have no owned match. | No top shot or leader spec is recorded for Cameron's Trinidad 40 setup — only the 80 lb braid maximum.

</details>

### 11. [technique] How do I slow-troll a live mackerel for yellowtail? Speed, how to rig it, and when it is the right call versus…

**Winner:** B3 · mapping {'A': 'NOW', 'B': 'B2', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 1 | 2 | 2 | 2 | 1 | **10** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** A and C both worked from a KB that holds a real slow-trolling technique note, and both deliver the full answer the question asks for — the 1.5-3 mph bait-graded band, nose-hook doctrine, 100-150 ft setback, the light lever-drag-at-2 rationale, and the stratified-column-vs-bottom-ball meter read that picks troll over flyline; B's KB has none of that, and B says so honestly but can only offer one Baja speed number (~3 mph), no hook size, no setback doctrine and no drag guidance for SoCal water. C edges A by turning the same material into usable decisions rather than open questions: it gives the J-vs-circle conflict a working frame (hook style decides your hookset, chosen before the bait goes in), explains what the SoCal 25-40 lb versus Baja 80-100 lb split actually turns on (educated coast fish you must fool vs home-guard fish you must muscle off a 28-40 ft rock), and resolves speed and rod against a real boat — where A explicitly reports that no such frame exists. A's compensating strength is the sharpest honesty of the three: it alone flags that the mackerel-plus-slow-troll hook pairing is an inference across two notes and catches a cite whose video does not support the claim, which makes it a very close second rather than a clear loser.

- *B2 reasons:* found: drew on everything its KB actually held (router row + trolling observations) and stated plainly at the top that no standalone slow-troll technique note exists — the honest version of a thin shelf. specific: real numbers exist (3 mph, 50-75 ft, 40/65/80/100 lb brackets, 28-40 ft depths, 12 ft La Paz, 2 lb mackerel, El Bajo 10 yd drop) but the core asks are unanswered — no speed range, no hook size, no setback doctrine, no drag setting, and the one SoCal data point is a sardine. sourced: clean note paths and video ids on every bracket, including a table attributing each line class to its trip. scoped: strongest region discipline of the three — every mackerel program labelled Baja (Cedros/Ensenada/La Paz), the SoCal transfer explicitly called the reader's own call, and the router's SoCal locate-troll row named as a flagged stub. honest: no bluffing, names ASR uncertainty ('number 3' circle, brand garbled), keeps the zero-bite day beside the hot day, 11-item gap list. actionable: rig-able and runnable at ~3 mph over a known rock, but a new-to-SoCal angler is left with no SoCal-calibrated speed, setback, leader or drag guidance for the water they will actually fish.
- *B3 reasons:* found: same core material as A (slow-trolling-bait, yellowtail router, flyline, bait, hooks) and adds the column map that places slow-troll against iron/yo-yo/dropper, plus the bonito-interception branch. specific: full parameter set — 1.5-3 mph bait-graded, 100-150 ft setback with 50-75/150-200 ft variants, lever '2', 25-40 lb main plus 20-25 lb backup, ~6 ft matched fluoro halved as floor, 3/0 J vs 1/0-3/0-5/0 circles up to 15 in mackerel, 8 ft glass rod / size-25 reel / 50 lb braid / 30-40 lb topshot, 50-100 yd first run. sourced: note paths as live links plus video ids on essentially every claim, with confidence tiers and the sponsored-model cap called out. scoped: waters gate quoted explicitly (nearshore-coast/island/bank, not paddy/open-ocean), SoCal doctrine and Baja home-guard bracket tabled side by side with the reason they differ; no bare regulation anywhere. honest: 9-item gap list, flags the low-confidence promotional 1 mph sardine figure, notes the downrigger point is secondhand and unconfirmed, names the profile gap (no size-25 lever drag owned), absolute dates. actionable: highest — hook style tied to hookset as a pre-drop decision, the heavy-vs-light line choice framed on grade and structure, five concrete 'reach for it when' triggers, four concrete 'stay on the flyline when' triggers, and speed/rod resolved against the actual boat.
- *NOW reasons:* found: hit the dedicated slow-trolling-bait note plus the yellowtail router, flyline note, bait note and hooks note — all three parts of the question answered from the right material. specific: 1.5-3 mph bait-graded band, 100-150 ft setback, lever drag at '2', 25-40 lb main with ~6 ft matched fluoro halved at most, 3/0 J default with 1/0-2 downsize, 50-100 yd first run, Cedros ~3 mph / 50-75 ft, 80-100 lb Baja bracket, 28-30 ft rock. sourced: every parameter carries a note path plus video id (HTowqnwAMeA, QSmE3mdEL28, w5_x6kkN-xE, ORC1A68cEeM...), and it names where two notes disagree internally. scoped: SoCal local-coast doctrine kept strictly apart from the Cedros/La Paz heavy variant in its own section; the only regulatory item (Mexican circle-hook 'mandatory') is quarantined in gaps as unverified with a verify-before-fishing instruction. honest: best-in-class — flags that no note states 'nose-hook a slow-trolled mackerel' in one sentence and calls it an inference across two notes, flags the 3/0 vs 4/0-5/0 discrepancy, flags a missing corroborating claim in a cited video, 11-item gap list, absolute dates throughout. actionable: an angler can rig, set speed, set setback and drag, and knows the meter read that triggers the call; slightly weakened by no decision frame for J vs circle (which it admits) and no profile resolution.

<details><summary>Full prompt</summary>

How do I slow-troll a live mackerel for yellowtail? Speed, how to rig it, and when it is the right call versus flylining.

</details>

<details><summary><b>B2 — batch 2</b> · 10/12</summary>

# Slow-trolling a live mackerel for yellowtail

**Read this first — what the KB actually holds.** There is no standalone technique note for slow-trolling live bait in this KB. The doctrine lives as one row in the yellowtail router (`species/yellowtail.md`, "Situations → techniques") plus a stack of on-the-water observations inside `techniques/trolling.md`. Almost all of it is **Baja**: Cedros Island and a point/reef off Ensenada (Pacific side), and La Paz (Sea of Cortez side). Nearly every source is StokedOnFishing — an unregistered channel, so those parameters carry **medium confidence and are observations, not rules**. The one SoCal-side data point is a sardine, not a mackerel (below). Numbers below are given exactly as the notes state them, including where two trips disagree — the KB deliberately keeps those side by side rather than reconciling them.

---

## 1. Speed and setback

- **~3 mph — "putt putt putt."** The only explicit speed number in the KB, from a Cedros slow-troll session: live mackerel **flylined 50 to 75 ft back off the stern**, on a **40 lb fluorocarbon top shot** (`techniques/trolling.md`, `9tIp4n7q850`). That is the number to start on.
- A different Cedros trip set the bait **"not too far" back** behind the boat, over **40 ft** of water at that stop — no distance given (`techniques/trolling.md`, `QSmE3mdEL28`).
- The one **SoCal** slow-troll data point in the KB is a **nose-hooked live sardine slow-trolled 150 to 200 ft behind the boat**, in "the channel" (exact location not stated on camera), producing yellowtail; hooks were a mix of circle and wide-gap (`techniques/flyline.md`, `ROWgdFE9Ehc`). That is a much longer setback than the Cedros mackerel numbers — different bait, different place, and the KB does not reconcile the two.
- For contrast so you don't confuse the two methods: **speed-trolling** is a different technique entirely — a Mad Mac-class hard bait at **13 to 15 knots** to locate bluefin (`techniques/speed-trolling.md`, `z1CmWHqe9uk`). A live-bait slow-troll is an order of magnitude slower.

**Depth of water fished:** Cedros ran it over a rock **cresting at 28 ft** — called the day's "perfect" biting depth — with fish also worked down to **30 ft**, and a second stop over **40 ft** (`species/yellowtail.md`, `techniques/trolling.md`; `QSmE3mdEL28`, `I-QBxuV2p7M`). La Paz started the troll in water called out as just **12 ft** deep, tight to visible rock (`techniques/trolling.md`, `ORC1A68cEeM`). This is genuinely shallow-water work.

## 2. Rigging it

**Bait.** Big live mackerel, deliberately. The Cedros crews spent parts of two days catching **giant mackerel** specifically for this — landed bait described as **big, fat, roughly 2 lb** (`techniques/trolling.md`, `Zo92MG459gQ`), and day two of the earlier trip made a point of targeting "the big green mackerel… big bait today" (`species/yellowtail.md`, `I-QBxuV2p7M`). That is not oversized: yellowtail have been seen eating mackerel up to **1.5 lb**, sometimes with **five or six fish attacking one mackerel at once** (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`). Bait selection still governs — roughly **90% of live-bait success is bait selection**; fish the hardest bait to catch in the tank, the lively lime-green one with scales intact and no bloody nose (`bait/fishing-live-bait.md`, `SluBXkT3cuw`, `raUPkuaFXpw`).

**Hook position — nose hook.** The nose hook (the clear spot in front of the eyes, one nostril to the other) is the position the KB says **can be slow-trolled**: the bait swims naturally and stays up (`bait/fishing-live-bait.md`, `mscHk0qiXnk`, `T3p1mrqNjIo`, `SluBXkT3cuw`). On mackerel specifically the doctrine is hard: **butt hook is for flylining with zero weight only; nose hook the moment any tension or weight is in play**, because a butt-hooked bait dragged from behind swims backward and doesn't read as a feeding fish (`bait/fishing-live-bait.md`, `w5_x6kkN-xE` — Dave Hansen, registered voice, high confidence). One angler at Cedros chose the nose hook specifically because that bait "seemed to be swimming okay" (`species/yellowtail.md`).

**Hook style — circle, on every sourced slow-troll session.** Cedros ran circle hooks throughout (`techniques/trolling.md`, `QSmE3mdEL28`; a circle visually confirmed on a bait-caught fish the following day, `I-QBxuV2p7M`); the 2 lb mackerel was fished on a circle called a **"number 3"** on camera, brand garbled (`Zo92MG459gQ`); La Paz likewise fished circles (`ORC1A68cEeM`).

⚠ **Conflict, kept side by side, not reconciled:** `tackle/hooks.md` states the general rule that **J hooks are the pick for islands yellowtail** — circles being the offshore live-bait default — while every observed yellowtail slow-troll in this KB ran circles. The KB does not resolve which wins for a trolled bait. Hook *size* for mackerel is also unresolved: the sizing table only says **"mackerel — step up again, bigger hook"** with no number (`tackle/hooks.md`, `HIXTFWlwnM0`, `m2q22sPPkEM`).

**Line and leader — four brackets, all kept side by side:**

| Bracket | Where / when | Source |
| --- | --- | --- |
| **80–100 lb line class**, fielded as the standing gear (one angler: "straight 80 on 80"; some in the group recommend stepping to **100 lb**) | Cedros, shallow rock, 2021-10 trip | `QSmE3mdEL28`, `Zo92MG459gQ` |
| **65 lb braid → 80 lb fluorocarbon leader** | Cedros, day two of that same trip, same spot, heavier leader on lighter braid — reasoning stated as "big fish could care less what size line you're using, they just want to eat that giant mackerel and go back to their hole" | `I-QBxuV2p7M` |
| **40 lb fluorocarbon top shot** | Cedros, a different trip/year (the ~3 mph / 50–75 ft session) | `9tIp4n7q850` |
| **40 lb line** | La Paz, shallow-rock jurel/yellowtail troll | `ORC1A68cEeM` |

`tackle/line-and-leader.md` adds the other Cedros view — a **40 lb line-class floor**, **50 lb** covering most everything on the trip, **80 lb** carried just-in-case (`WE643Fue1_A`) — explicitly logged as a lighter bracket than the 80–100 lb standing gear above, "read as two operators' independent line-class choices for the same resident-fish risk (getting spooled into shallow rock), not a correction of each other." **The decision frame the notes give you:** the risk you are buying insurance against is a 30–45 lb resident fish reaching the rocks from 28–40 ft of water. Heavier line is bought for that, not for the bite; lighter line is what one operator judged sufficient. Neither is ranked above the other in the KB.

## 3. Running it

1. **Make bait first.** Every sourced session starts with a bait-making run (`bait/making-bait.md`). La Paz's guide targeted **20–40 mackerel per boat** (`ORC1A68cEeM`). At Cedros, hooked bait mackerel were repeatedly lost to seals working them at the surface — the fix was **fishing the bait deeper** rather than at the top (`techniques/trolling.md`, `Zo92MG459gQ`).
2. **Test drags before you start.** La Paz's crew had every angler test their drag at the captain's prompt as a standard first step — "this style of fishing always ask the captain to test your drags, numero uno" (`techniques/trolling.md`, `ORC1A68cEeM`). Mid-fight, adding "a couple more clicks" of drag was called on camera "always the wrong thing to do" (`species/yellowtail.md`, `Zo92MG459gQ`).
3. **Do not strike.** Circle-hook doctrine: don't swing — engage the reel, point the rod where the fish is going, wind tight, and it pins the corner of the mouth on its own (`tackle/hooks.md`). Cedros ran exactly that — let the rod load and wind tight (`techniques/trolling.md`, `QSmE3mdEL28`). **Variant, kept side by side:** the La Paz crew gave a biting fish an explicit **3-second count ("1, 2, 3")** before putting the reel in gear (`ORC1A68cEeM`). At the smallest hook sizes the KB elsewhere cites a **10 count** on a circle (`tackle/hooks.md`, `48ZFXnCTTQE`). Same philosophy — let the fish load the hook — three different descriptions of the pause.
4. **Back the boat down** once a big one takes off. Called out on camera as an important, deliberate move, compared to backing down on big bluefin (`techniques/trolling.md`, `QSmE3mdEL28`).
5. **Expect the fish to run for the rocks**, and expect to lose some. When one couldn't be lifted conventionally in the shallow structure, the crew **"railed" it** — worked it up and over the gunnel with the rod rather than continuing a standard fight (`QSmE3mdEL28`). La Paz's crew closed the day with "you win some and you lose more when you're fishing shallow water yellowtail" (`ORC1A68cEeM`).
6. **Variant worth knowing — the dropped-bait troll over a bank.** At La Paz's "El Bajo" high spot (shallowest ~**50 ft on low tide, no more than 80 ft on high**), the crew let out roughly **10 yards** of line, dropped the weight straight to the bottom, and let the ongoing troll speed lift the bait back up off bottom on its own rather than cranking — presenting it "out the back in the high column zone." **65 lb braid to a 60 lb fluorocarbon** top shot. Produced multiple yellowtail (`techniques/trolling.md`, `92y14x33etQ`).

## 4. When it's the right call — versus flylining

The router row is specific about scope: slow-trolled live mackerel is for **resident/home-guard fish over known shallow structure**, and it is explicitly **"not a locate method — a standing program over a known rock"** (`species/yellowtail.md`). Reach for it when:

- **You have a known piece of shallow structure holding resident fish**, and you're working it as the day's standing program rather than searching. Cedros ran it all day for repeated hookups — "slow trolls are popping… bendo here, doubles over there" (`techniques/trolling.md`, `QSmE3mdEL28`).
- **The fish are moving around the structure rather than holding on it.** At the Ensenada reef/point, yellowtail were described as constantly on the move around the structure — the crew's answer was to slow-troll a couple of live mackerel from the stern **while simultaneously casting jigs from the bow** at the same structure, the stated logic being that the surface splashes from the cast jigs pull fish into the area alongside the trolled bait rather than competing with it (`techniques/trolling.md`, `0dIwWiOc1NY`).
- **It's blowing and you can't cast clean.** The Cedros program kept running through building wind and whitecaps — "the good news is we're just slow-trolling… I don't think the fish care" — precisely because the technique doesn't depend on a clean cast the way iron does (`techniques/trolling.md`, `QSmE3mdEL28`). This is the sharpest decision lever in the KB between this and any casting presentation.
- **You want yellowtail specifically, not bycatch.** Fishing live mackerel rather than smaller sardine or anchovy **skews the catch toward yellowtail**, screening out calico bass, barracuda and bonito (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`, high confidence). It also skews grade: the mackerel troll produced a **45 lb personal best** at Cedros while surface iron the same morning produced a smaller class of fish (`species/yellowtail.md`, `Zo92MG459gQ`, `QSmE3mdEL28`); La Paz produced doubles close to **30 lb** (`ORC1A68cEeM`).

**Flyline instead when:**

- **Live bait is in the water and the fish are on the chum or the bait line** — you're anchored or drifting, and the fish are coming to the boat (`techniques/flyline.md`, "Reach for this when"). The whole slow-troll premise is the opposite: the boat, not the bait's own swim, is doing the moving.
- **Fish are visible but not biting — picky, seeing-not-biting.** The router sends this straight to flylined bait: downsize leader and hook, and wait for the tide/current window (`species/yellowtail.md`).
- **Boiling/breezing surface fish, or fish on a kelp paddy.** Ranked: **1) surface iron, 2) flylined bait, 3) stickbait/jerkbait** — the troll isn't in that row at all (`species/yellowtail.md`).
- Flyline builds for yellowtail, if you go that way: an **8–8'6" rod rated 20–40 to 20–50 lb**, reel that free-spools well, **50 lb braid backing → 30 lb mono top shot → 20–30 lb fluoro leader** (25 lb gets bit better, 30 lb gives leverage to turn a fish off the rocks), **2/0** hook for jumbo bait and smaller mackerel, **1/0** for smaller sardines and anchovies (`techniques/flyline.md`, `A70kK2niu2Q`, `LTCFjqtSI8g`).

**Three caveats the KB insists on:**

- **The rows are starting ranks, not exclusive routes.** "The faces are states, not types" (cameron): yellowtail roam the column and feed looking up, so no situation locks you to one presentation — re-read water temp and bait depth before committing the day (`species/yellowtail.md`). Cameron's own doctrine is to rig the surface-iron, heavy yo-yo/dropper, and flyline outfits **simultaneously** and switch as the read changes.
- **Timing beats presentation.** At the Ensenada reef the crew blanked on yellowtail over a couple of hours and attributed it to timing, not method: **yellowtail feed hardest during gray light early in the morning**, and that stop was fished after the window with the tide also "off" (`species/yellowtail.md`, `0dIwWiOc1NY`).
- **Day-to-day variance is brutal on this program.** Same crew, same Cedros spot, one day later, with heavier gear and bigger bait: **zero yellowtail bites all day** — "every single day is different here" (`species/yellowtail.md`, `I-QBxuV2p7M`). The KB keeps that beside the repeated-hookup day rather than averaging them.

## 5. Resolving this to your boat (Cameron's profile)

- **Closest outfit to the Cedros bracket:** the **Trinidad 40** setup — 8'0" XH, 40–80 lb, **80 lb braid**, relatively soft tip, role explicitly includes "some trolling" (`profiles/cameron/rods.md`). That lands on the low edge of the 80–100 lb Cedros standing gear and squarely on the 80 lb-fluoro-leader variant. The **Avet** setup (Teramar 90MHB2, 30–65 lb class, 50 lb braid) is your flyline stick, and the **Talica 25** (100 lb braid, rail-rod class) is heavier than anything the slow-troll sources fielded.
- **Speed:** ~3 mph is about 2.6 kt. Your boat idles **~1.5 kt** (`profiles/cameron/boat.md`), so this is just above idle — bumps in and out of gear, not a fixed troll setting.
- **Bait:** your own sabiki program already produces the right bait class — **~100 ft, 8 oz sinker at the Coronado Islands**, with **five twelve-inch mackerel on one drop** recorded (`bait/making-bait.md`, cameron). Twelve-inch mackerel is the size class this technique is built around. **30-gallon tank** on a Rule 401 500 GPH pump (`profiles/cameron/boat.md`).
- One caution the notes support: the Cedros/La Paz programs pull **one or two baits over a specific rock** from the stern, not a staggered spread — your 15° gunnel holders and the 5° elevated shotgun are set up for a lure spread (`profiles/cameron/boat.md`, `techniques/trolling.md`). The KB gives no holder geometry or rod-count guidance for a live-bait slow-troll.

---

**Where the KB runs out.** Everything above with a mackerel in it is **Baja-sourced** — Cedros and Ensenada on the Pacific side, La Paz in the Sea of Cortez. The KB has no sourced live-mackerel slow-troll program for Catalina, San Clemente, the Coronados or any US-side zone; the router's own locate-troll row for yellowtail is still a **⚠ flagged stub with no corpus source**. Treat the transfer to a SoCal island as your own call, not something this KB backs.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `species/yellowtail.md`, `techniques/trolling.md`, `techniques/flyline.md`, `techniques/speed-trolling.md`, `bait/fishing-live-bait.md`, `bait/making-bait.md`, `tackle/hooks.md`, `tackle/line-and-leader.md`, `tackle/gear-classes.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`  
*videos:* `QSmE3mdEL28`, `I-QBxuV2p7M`, `9tIp4n7q850`, `Zo92MG459gQ`, `0dIwWiOc1NY`, `ORC1A68cEeM`, `92y14x33etQ`, `ROWgdFE9Ehc`, `w5_x6kkN-xE`, `mscHk0qiXnk`, `T3p1mrqNjIo`, `SluBXkT3cuw`, `raUPkuaFXpw`, `sWRSYCmt4Tw`, `m2q22sPPkEM`, `HIXTFWlwnM0`, `48ZFXnCTTQE`, `WE643Fue1_A`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `z1CmWHqe9uk`  
*gaps admitted:* No standalone technique note for slow-trolling live bait — the method exists only as one router row in species/yellowtail.md plus observation entries inside techniques/trolling.md, so there is no doctrine-level 'reach for this when' list for it the way flyline and surface iron have. | Only ONE explicit troll speed exists in the whole KB (~3 mph, one Cedros trip, 9tIp4n7q850). No speed range, no RPM or gear-engagement guidance, and no speed stated for the Ensenada or La Paz sessions. | No SoCal/US-side sourced live-mackerel slow-troll for yellowtail. Every mackerel program is Baja (Cedros, Ensenada, La Paz); the only SoCal data point is a nose-hooked sardine in 'the channel' with the location not stated on camera. The router's yellowtail locate-troll row is still a flagged stub with no corpus source. | No hook size number for a slow-trolled mackerel. tackle/hooks.md says only 'mackerel — step up again, bigger hook'; the single Cedros number ('number 3' circle) is ASR-uncertain with the brand garbled. | Circle vs J is unresolved for this application — every observed slow-troll ran circles, while tackle/hooks.md states J hooks are the pick for islands yellowtail. The KB keeps both and does not say which governs a trolled bait. | No spread geometry for a live-bait slow-troll: how many baits to pull, rod-holder vs hand-held, holder angle, or how to stagger two baits. The Ensenada entry says only 'a couple of live mackerel from the stern'. | No turn/sweep pattern doctrine for a bait troll. The sweeps-not-straight-lines doctrine in techniques/trolling.md is written for offshore lure trolling, and the notes never say how to work a pass over a known rock. | No drag setting numbers — only the ritual of testing drags before starting and the warning against increasing drag mid-fight. | No water-temperature, seasonal, tide or current trigger for choosing the slow-troll. The only timing cue attached to it is the crew's gray-light/early-morning remark at Ensenada. | No sourced guidance on adding weight to keep a trolled bait down in open water — the only weighted variant is the La Paz dropped-bait troll over a bank high spot, and the rig format ('D-rigger') is unspecified on camera. | No head-to-head comparison of slow-troll versus flyline anywhere in the KB. The versus framing above is assembled from the two techniques' separate scope statements and router rows, not from a source that compares them.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Slow-trolling a live mackerel for yellowtail

Short version: it's the same bait and the same outfit you'd flyline, with the boat moving. [`techniques/slow-trolling-bait.md`](techniques/slow-trolling-bait.md) frames it exactly that way — "the bridge between flylining (same bait, same tackle, boat stopped) and trolling (boat moving, but hard baits and a search purpose). The bait is the presentation; the boat's job is to cover ground **and to set the hook**."

Two things to know up front about the sourcing:
- The core SoCal doctrine below is one source — **Nate Winnicki, BDOutdoors (`HTowqnwAMeA`)**, filmed mid-August. The note is `confidence: medium` (registered voice, first commit of these specific claims), and named rod/reel/hook/line **models** in it sit at `low` per the sponsored-claim rule. The parameters and reasoning qualify normally.
- The note is region-gated to all five regions but **`waters: [nearshore-coast, island, bank]`** — it is a coast/island/bank tool, not something the KB offers for open-ocean/paddy work.

---

### 1. Speed — 1.5–3 mph, and the bait picks the number

- The stated band is **1.5 to 3 mph**, deliberately wide, because **the bait chooses where in it you sit** ([`techniques/slow-trolling-bait.md`](techniques/slow-trolling-bait.md), `HTowqnwAMeA`):
  - **Small-grade sardine** (the kind that wants a size 1 or 2 hook) — "as slow as you possibly can." A small bait can't swim against much.
  - **Mackerel, or any bait big enough for a 3/0–5/0 hook** — you can **pull it faster** inside that range. That's your case.
- **The governing test is not the speedometer.** The bait must *look natural*; the failure mode is a bait that reads as being dragged by a machine. Set speed by watching the bait and use the range as a sanity check.
- **A real-water number for mackerel specifically:** a Cedros Island slow-troll session called its speed **~3 mph** on camera ("putt putt putt"), pulling live mackerel (StokedOnFishing, `9tIp4n7q850`, 2023-05-17 — unregistered channel, medium; logged in [`techniques/trolling.md`](techniques/trolling.md)). That sits at the **top** of the band, which is consistent with the bait-picks-the-speed rule for a big bait.
- For contrast, a promotional seminar source names **~1 mph** for slow-trolling live *sardines* as the slow end of trolled-search methods ([`techniques/tube-bait-fishing.md`](techniques/tube-bait-fishing.md), `5Oh3IPIC5g4`) — ⚠ that note is flagged low confidence (promotional), and it's a sardine number, not a mackerel one.
- **Common failure named:** running one speed all day. The speed is a function of what's in the tank and changes when the bait does.

### 2. Rigging the mackerel

**Hook position — nose hook.** The clear cartilage spot right in front of the eyes, one nostril to the other; it's the same spot on mackerel, sardine and anchovy ([`bait/fishing-live-bait.md`](bait/fishing-live-bait.md), `SluBXkT3cuw`). That table names the nose hook as the one that "swims naturally, stays up; **can be slow-trolled** or fly-lined" (`T3p1mrqNjIo`, `mscHk0qiXnk`).

Mackerel-specific doctrine is stricter, and it's `high` confidence (Capt. Dave Hansen, Your Saltwater Guide, `w5_x6kkN-xE`, 2021-04-06 — [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md)): only **two** positions get used on mackerel day to day — **butt hook for flylining with zero weight only**, and **nose hook the moment any weight is added** (dropper loop, sliding sinker, rubber core), because a butt-hooked bait under a pull gets dragged backward and a mackerel swimming backward doesn't read as a feeding-fish silhouette. Back/dorsal is reserved for kite baits. Since a slow troll is a sustained pull on the bait, the nose hook is the position the KB supports here.

**Hook style and size — two documented programs, kept side by side:**

| | SoCal local coast (`HTowqnwAMeA`) | Cedros / Baja home-guard (`QSmE3mdEL28`, `Zo92MG459gQ`, `_C7TJoGT0nw`) |
| --- | --- | --- |
| Hook style | **J hook**, ~**3/0** working default; carry **1/0, 1, 2** for small bait and finicky fish | **Circle hook** throughout |
| Sizing logic | Downsize line class *and* hook size **together** to get a bite — a paired move, not one or the other | Size to the bait: Owner ringed offshore hooks **10, 30, 50** carried to match the day's bait dock (read as **1/0, 3/0, 5/0**; ASR-rendering noted in [`tackle/hooks.md`](tackle/hooks.md)) for baits up to **15-inch** mackerel; a **"number 3"** circle on ~**2 lb** mackerel |
| Hookset | Boat sets it on light drag (below) | **No strike** — let the rod load and wind tight ([`tackle/hooks.md`](tackle/hooks.md) circle doctrine). La Paz variant: give a **3-second count ("1, 2, 3")** before putting the reel in gear (`ORC1A68cEeM`) |

Decision frame: **hook style decides your hookset**, so pick before you drop the bait, not during the bite. A J hook you set; a circle you never swing on — engage, point the rod where the fish is going, wind tight ([`tackle/hooks.md`](tackle/hooks.md)).

**Line and leader (SoCal local coast, `HTowqnwAMeA`):**
- **Mainline class 25–40 lb**, and **always carry a lighter option, 20–25 lb**, even on a day that starts on 40. A full day of bites on 40 lb is described as luck rather than the norm on the local coast. *"You'd be really surprised how hard you can pull on 25 lb"* — provided the drag is set for it.
- **~6 ft of fluorocarbon at the hook, matched to the mainline** — 30 lb main gets 30 lb fluoro — and **at most halved** when fish are finicky (30 → 25). Explicit warning: do not go much lighter. The payoff is abrasion resistance right at the hook, where you otherwise get bitten or rubbed off on rock. Over-dropping the fluoro is listed as a common failure: halving is the floor, not a starting point.
- **Full stated build:** an **8 ft fiberglass or composite rod**, a **size-25 reel**, **50 lb braid** with a **30–40 lb mono top shot**, then the short fluoro to the hook.

**The Baja home-guard bracket is much heavier and is deliberately not reconciled with the above.** At Cedros over shallow rock the crew stepped up to an **80–100 lb line class** (`QSmE3mdEL28`); day two of the same trip ran **65 lb braid to 80 lb fluoro** (`I-QBxuV2p7M`); a later trip credited a fish to **straight 80 lb** with some of the group recommending **100 lb** (`Zo92MG459gQ`); a different Cedros trip ran only a **40 lb fluoro top shot** (`9tIp4n7q850`). A La Paz shallow-water program ran **40 lb** (`ORC1A68cEeM`), and the El Bajo bank program **65 lb braid to 60 lb fluoro** (`92y14x33etQ`). What it turns on: grade and structure — 40 lb-class home-guard fish that dive straight back into a shallow rock and have to be muscled, versus educated local-coast fish that have to be fooled first.

### 3. Setback, drag, and letting the boat do the work

- **Setback: 100–150 ft.** Explicitly *not* far — a long setback isn't the goal. Past ~150 ft you lose the hook-setting benefit of boat motion and gain nothing (`HTowqnwAMeA`).
- Real-water variants, side by side: Cedros ran mackerel **50–75 ft** back off the stern at ~3 mph (`9tIp4n7q850`); another Cedros stop set it "not too far" back over **40 ft** of water (`QSmE3mdEL28`); an observed *sardine* slow-troll ran **150–200 ft** back and produced yellowtail (StokedOnFishing, `ROWgdFE9Ehc`, in [`techniques/flyline.md`](techniques/flyline.md)).
- **Fish a light drag and let the boat drive the hook.** On a lever drag, set around the **"2"** mark: enough that forward boat motion seats the hook when the fish eats, not so much that it snaps you off or overruns the reel. Whether you fish in gear at all is presented as angler preference; the light-drag setting is the specific recommendation.
- **Why the drag can't be pinned:** a yellowtail eating a slow-trolled bait takes **50–100 yards immediately**, more if it's any size. A locked drag at that moment either breaks the line or backlashes the reel. Pinning the drag is the first-listed common failure.
- Before you start, the La Paz crew's ritual is worth copying: **every angler tests their drag** at the captain's prompt — "this style of fishing always ask the captain to test your drags, numero uno" (`ORC1A68cEeM`).

### 4. Once you're bit (shallow-structure Baja specifics)

- **Back the boat down** on a hooked fish — called out explicitly as a deliberate, important move once a big yellowtail takes off, compared on camera to backing down on big bluefin (`QSmE3mdEL28`).
- When a big fish can't be lifted conventionally in shallow structure, the crew **"railed" it** — worked it up and over the gunnel with the rod rather than continuing a standard fight (`QSmE3mdEL28`).
- **Don't add drag mid-fight** — a couple of extra clicks during a fight is called "always the wrong thing to do" (`Zo92MG459gQ`).
- Expect the fish to run **back at the rocks**; La Paz's crew summed up their shallow rock-adjacent program as "you win some and you lose more when you're fishing shallow water yellowtail" (`ORC1A68cEeM`).

### 5. When slow-trolling is the right call vs. flylining

**The meter shape is the primary discriminator** ([`species/yellowtail.md`](species/yellowtail.md) → Finding them, `HTowqnwAMeA`):

- **Stratified column** — marks running as lines from the bottom up through mid-column, sometimes to the surface — reads as **fish actively hunting bait**, and is the stated cue to **put slow-trolled baits out**.
- **A ball glued to the bottom** is the opposite read: fish present but not hunting. That is **dropper-loop water, not flyline water** — don't slow-troll it either.
- Layered on top: **high and spread = biting; tucked tight to the bottom = not** (same trip, second angler named only as Marshall, so medium regardless of channel).
- A separate depth read: fish metering at **40–60 ft** and not yet showing is called "surface iron fish and light bait zone" and specifically **rules out the yo-yo** (Strictly Irons, `0DKmYId1NN4`).

**Reach for the slow troll when** ([`techniques/slow-trolling-bait.md`](techniques/slow-trolling-bait.md)):
1. You're seeing that stratified/hunting column.
2. You have live bait and **want to keep covering water instead of committing to an anchor**.
3. The outfit and bait you'd flyline is already rigged — this is a change of *boat behaviour*, not of tackle.
4. **It's windy.** The Cedros program kept running through building wind and whitecaps — "the good news is we're just slow-trolling… I don't think the fish care" — because it doesn't depend on a clean cast the way iron does (`QSmE3mdEL28`).
5. **Your arms are done.** A documented Cedros use case is a rest break from casting iron after four or five yellowtail, with the operator's own bait dock supplying mackerel (Tackle Express, `_C7TJoGT0nw` / `qHS-ewTQs9Q`).

**Stay on the flyline when** ([`species/yellowtail.md`](species/yellowtail.md) Situations → techniques, [`techniques/flyline.md`](techniques/flyline.md)):
- **Bait is in the water and fish are on the chum/bait line** or working a paddy — that's the flyline's stated trigger.
- **Boiling/breezing surface fish or paddy fish:** the router ranks **surface iron 1st, flylined bait 2nd**, stickbait 3rd — not the slow troll.
- **Fish visible but not biting (picky/finicky):** flylined bait, **downsize leader and hook**, and anchor the plan to the daily bite window. That's a fooling problem, and the flyline is the most natural presentation in the box.
- If **bonito are intercepting your flylined baits** before they reach the yellowtail, the documented answer isn't the slow troll — it's a **sliding sinker** (2–4 oz egg sinker to a 2/0–4/0 J hook) to get under the bonito layer (Steve Carson, `yGXSrUauo2w`).

**The column map that ties it together** ([`species/yellowtail.md`](species/yellowtail.md) → Doctrine & conflicts, `HTowqnwAMeA`): flyline and slow-trolled bait **up top** because that's how the fish feed when they're feeding; trolled hard baits **mid-column as a search tool**; surface iron on top; yo-yo iron for the **mid-to-lower** band the surface iron can't reach; dropper loop **on the bottom for inactive fish**.

**Two calibration points before you switch off anything:**
- **Don't marry the technique.** That crew was told the spot was anchor fishing, anchored, fished it **an hour to an hour and a half** for a couple of bites, then pulled the anchor, started moving around the zone and slow-trolling — and their **bite rate roughly quadrupled**. Stated lesson: "You can't really be glued to a certain technique or style of fishing" (`HTowqnwAMeA`).
- **But a slow day isn't proof the technique is wrong.** A **12–15 bite** day was called an anomaly on camera; a **good** day of local yellowtail fishing is **three or four bites**. At that rate, two fishless hours is not evidence (`HTowqnwAMeA`, SoCal local-coast expectation only).

### 6. Two extras worth knowing

- **Mackerel is a species filter, not just a bigger bait.** At San Clemente, Catalina and the Coronados, fishing live mackerel instead of sardine/anchovy **skews the catch toward yellowtail specifically**, screening out calico, barracuda and bonito bycatch. Yellowtail have been seen eating mackerel up to **1.5 lb**, sometimes five or six fish attacking one mackerel at once (`w5_x6kkN-xE`, `high` confidence).
- **Run it alongside casting, not instead of it.** An Ensenada crew slow-trolled **a couple of live mackerel from the stern** while **casting jigs from the bow** at the same reef/point — the stated logic being that the surface splashes from the cast jigs pull fish into the area alongside the trolled bait (`0dIwWiOc1NY`; that particular two-hour stop produced no yellowtail).
- **Weighted variant, if the fish are down:** at the La Paz "El Bajo" bank (crest ~50 ft on low tide, no more than 80 ft on high), the crew let out roughly **10 yards**, dropped the weight straight to the bottom, and let the troll speed lift the bait back up "out the back in the high column zone" rather than cranking it (`92y14x33etQ`). Note the mackerel doctrine above: **any weight means nose-hook**, which you're already doing.

### If this is Cameron's boat ([`profiles/cameron/`](profiles/cameron/README.md))

- **Speed is inside your envelope but at the bottom of it.** [`profiles/cameron/boat.md`](profiles/cameron/boat.md) records the Panga Marquesas 22 idling at **~1.5 kt** (≈1.7 mph by unit conversion — the KB states knots, not mph). That's the *slow* end of the 1.5–3 mph band, i.e. sardine speed. Pulling a mackerel at the fast end means running **above idle**, which on a single 115 Yamaha with no trim tabs is a throttle-and-watch-the-bait job, not a set-and-forget.
- **Closest owned outfit:** the **Avet setup** — Teramar TMC90MHB2, 9'0" MH, 30–65 lb braid class, Avet MXJ, 50 lb braid, role "mainly flyline" ([`profiles/cameron/rods.md`](profiles/cameron/rods.md)) — is the nearest match to the 25–40 lb slow-troll build, and the flyline role is the point: this is the same outfit with the boat moving. The **Trinidad 40** (8'0" XH 40–80, 80 lb braid) is your match for the heavy Baja/Cedros bracket.
- **Named gap:** the stated build wants an **8 ft glass or composite rod with a size-25 lever-drag reel**; your inventory lists graphite/composite inshore and jig blanks and no size-25 lever drag in that class — the Avet MXJ is a lever drag but not that size, and the Talica 25 sits on a 60–130 lb rail rod. Not a blocker, but the "set the lever at 2" instruction is written for a lever-drag reel, so translate it to a measured drag setting on whatever you fish.
- Your **30-gallon tank** ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)) is what makes this technique available at all — mackerel-catching is in [`bait/making-bait.md`](bait/making-bait.md).

---

### What the KB does not cover (don't take these from me, they aren't in the notes)

- No **mackerel-specific speed number for the SoCal local coast** — only "faster within 1.5–3 mph." The ~3 mph figure is Cedros, Baja.
- The KB names **only the nose hook** as slow-trollable. It has no coverage of butt-, shoulder- or bridle-rigging a bait *for a slow troll* (the bridle section in [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md) is explicitly flagged as general big-bait practice, "not covered in the SoCal deckhand clips").
- No **boat-handling pattern** for a live-bait slow troll — the sweeping-arcs/zigzag doctrine in [`techniques/trolling.md`](techniques/trolling.md) is written for lure spreads, and the KB never extends it to live bait.
- No doctrine on **how many baits to pull, or how to stagger them** on a live-bait slow troll (Ensenada names "a couple" from the stern; that's all).
- No **temperature or water-color threshold** that picks slow-troll over flyline — the KB's discriminators are meter shape and boat behaviour, not water state.
- No SoCal rule for **when to add weight or a downrigger** to a slow-trolled bait. The only downrigger data point is secondhand and unconfirmed (2 lb max weights, 30 ft of water, two big fish hooked and both lost — `_C7TJoGT0nw`).
- Nothing on **how long a mackerel survives on the troll or when to change it** — the 60-second "if it isn't pulling line, swap it" rule in [`techniques/flyline.md`](techniques/flyline.md) is a flyline bait-selection rule, not a troll rule.
- Nothing on running this **without a bait tank, or from a kayak**.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/slow-trolling-bait.md`, `techniques/flyline.md`, `techniques/trolling.md`, `techniques/tube-bait-fishing.md`, `species/yellowtail.md`, `bait/fishing-live-bait.md`, `tackle/hooks.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`  
*videos:* `HTowqnwAMeA`, `_C7TJoGT0nw`, `qHS-ewTQs9Q`, `QSmE3mdEL28`, `I-QBxuV2p7M`, `9tIp4n7q850`, `Zo92MG459gQ`, `ORC1A68cEeM`, `92y14x33etQ`, `0dIwWiOc1NY`, `w5_x6kkN-xE`, `SluBXkT3cuw`, `T3p1mrqNjIo`, `mscHk0qiXnk`, `ROWgdFE9Ehc`, `5Oh3IPIC5g4`, `0DKmYId1NN4`, `yGXSrUauo2w`, `NXvqLUZ6qp8`  
*gaps admitted:* No mackerel-specific slow-troll speed number for the SoCal local coast — the KB only says 'faster' within the 1.5-3 mph band; the ~3 mph figure is a Cedros, Baja trip. | The KB names only the nose hook as slow-trollable; it has no coverage of butt-, shoulder- or bridle-rigging a bait specifically for a slow troll (the bridle section is self-flagged as general big-bait practice, not SoCal-sourced). | No boat-handling pattern doctrine (sweeps, arcs, turns) for a live-bait slow troll — the sweeping-arcs doctrine in techniques/trolling.md is written for lure spreads only. | No doctrine on how many live baits to pull at once, or how to stagger their setbacks, on a slow troll (only 'a couple of live mackerel from the stern' at Ensenada). | No water-temperature or water-color threshold that selects slow-trolling over flylining — the KB's discriminators are meter shape and boat behaviour. | No SoCal rule for when to add weight or run a downrigger on a slow-trolled bait; the only downrigger data point is secondhand and unconfirmed (2 lb weights, 30 ft of water, two fish lost). | Nothing on how long a mackerel lasts on the troll or when to swap it — the 60-second bait-freshness rule is a flyline bait-selection rule, not a troll rule. | No coverage of slow-trolling live bait without a bait tank, or from a kayak. | The core SoCal slow-troll doctrine rests on a single source (HTowqnwAMeA) at medium confidence, with its named rod/reel/hook/line models capped at low — no second independent SoCal source in the corpus yet.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Slow-trolling a live mackerel for yellowtail

Short version: it's the **same bait and the same tackle you'd flyline** — what changes is the boat. `techniques/slow-trolling-bait.md` states it plainly: "slow-trolling is a change of boat behavior, not a change of tackle" (`HTowqnwAMeA`). So the real question is speed, hook placement, setback and drag — and the meter read that tells you which of the two to run.

One honesty note up front: the **SoCal-coast parameter set below comes from a single video** (`HTowqnwAMeA`), and `techniques/slow-trolling-bait.md` carries `confidence: medium`. The heavier Baja numbers come from a separate cluster of Cedros/La Paz trip footage on an unregistered channel (also medium). I've kept them apart rather than blending them, because the KB does.

---

### 1. When it's the right call vs. flylining

**The meter read is the primary trigger** (`species/yellowtail.md`, "Finding them"):

- **Fish spread up through the column** — stratified marks running from the bottom through mid-column, sometimes to the surface, or fish sitting high and spread over a small rock (~20–30 ft across) — read as **hunting**. That is the trigger to put slow-trolled *and* flylined baits out (`HTowqnwAMeA`).
- **Fish balled tight to the bottom** are present but not feeding — that's [dropper loop](rigging) water, plus a yo-yo burned past them for a reaction strike. Not slow-troll water. (`species/yellowtail.md` flags that the second source for that read, `tpmOYXYQwhU`, doesn't actually contain the bottom-balled/burned-yo-yo claim — so treat the bottom-ball half as thinner than it looks.)

**What tips it toward the slow-troll specifically:**

- **You want to keep covering water instead of committing to an anchor.** The KB's sharpest data point on this: told a spot was anchor fishing, a crew anchored, fished an hour to an hour and a half for a couple of bites, then pulled the anchor and worked the same zone slow-trolling — **bites roughly quadrupled** (`species/yellowtail.md`, "Don't marry the technique," `HTowqnwAMeA`).
- **It's windy and casting has gone to hell.** A Cedros crew kept the program running through building wind and whitecaps — "the good news is we're just slow-trolling… I don't think the fish care" — precisely because it doesn't depend on a clean cast the way iron does (`techniques/trolling.md`, `QSmE3mdEL28`).
- **You specifically want yellowtail, not bycatch.** Live mackerel (rather than sardine or anchovy) at San Clemente Island, Catalina or the Coronados **skews the catch toward yellowtail**, screening out calico, barracuda and bonito (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`). Yellowtail have been seen eating mackerel **up to 1.5 lb**, sometimes five or six fish attacking one mackerel at once. Bigger bait also selects bigger fish — Cedros crews spend days making giant mackerel for the resident grade (`species/yellowtail.md`, `Zo92MG459gQ`, `I-QBxuV2p7M`).

**What tips it toward flylining:**

- **Bait is in the water and the fish are on the chum or on the bait line**, or they're boiling/visible in casting range — boat stopped, cast well away from the hull (`techniques/flyline.md`).
- **Fish visible or metered but not eating** — the router's answer there is a flylined bait, downsized, fished into the tide/current window, not a troll (`species/yellowtail.md`, Situations → techniques).
- The Coronados guide gives the cleanest sequencing of the two: with live bait aboard, **slow-troll the zones**, and **put a flylined bait out when current and tide turn the fish onto bait** (`species/yellowtail-coronado-islands.md`, `D5DR7Kx42_A`).

They also run **at the same time**: an Ensenada crew slow-trolled a couple of live mackerel off the stern while casting jigs from the bow at the same reef/point, the logic being that the surface splashes pull fish into the area alongside the trolled bait (`techniques/trolling.md`, `0dIwWiOc1NY` — that stop produced no yellowtail, for what it's worth).

Before you blame the technique: **a good SoCal local-coast yellowtail day is three or four bites**; a 12–15-bite day is an anomaly. Two fishless hours is not evidence you're doing it wrong (`species/yellowtail.md`, `HTowqnwAMeA`, local-coast scope only).

---

### 2. Speed — 1.5–3 mph, graded to the bait

`techniques/slow-trolling-bait.md` (`HTowqnwAMeA`):

- **Band: 1.5–3 mph**, chosen by what's in the tank, not by the target species.
- **Small-grade sardine** (size 1 or 2 hook) — as slow as you possibly can; a small bait can't swim against much speed.
- **Mackerel, or any bait big enough for a 3/0–5/0 hook** — pull it **faster within the range**. ⚠ The note itself flags this: the source actually states the faster-pull trigger as bait big enough for a "40 or 50" (4/0–5/0) hook; 3/0 is the note's default working hook size from elsewhere, not the source's stated lower bound here.
- **The test is the bait, not the speedometer** — watch it swim and slow down the moment it starts reading as dragged rather than swimming.

Cross-checks from other footage, kept separate because they're different regions/trips:

- **Cedros, live mackerel: roughly 3 mph** ("putt putt putt"), 50–75 ft back off the stern, 40 lb fluorocarbon top shot (`techniques/trolling.md`, `9tIp4n7q850`).
- **~1 mph for slow-trolled live sardines** appears as a bracketing figure in one promotional seminar (thorough, covers little ground) against 3–4 mph for a trolled bullet bait as a *locating* speed and ~5 mph for a faster lure (`species/yellowtail-tube-bait-fishing.md`, `5Oh3IPIC5g4` — flagged single-source, and the sardine end of it is a different bait than yours).

So on mackerel: **the upper half of 1.5–3 mph**, and the Cedros ~3 mph is consistent with that.

---

### 3. Rigging the mackerel

**Hook placement — nose hook.** The nose hook is the all-purpose position: through the clear cartilage spot right in front of the eyes (side to side, one nostril to the other), the bait swims naturally, stays up, **and can be slow-trolled** (`bait/fishing-live-bait.md`, `techniques/flyline.md`; `T3p1mrqNjIo`, `mscHk0qiXnk`). The nose spot works on mackerel, sardine and anchovy alike (`SluBXkT3cuw`).

Mackerel-specific (`bait/fishing-live-bait.md`, `w5_x6kkN-xE`): only two placements get used day to day —
- **Butt hook** (through the meat back near, not through, the vent) — **fly-lining with zero weight only**. It reads as something biting the bait's tail, so the mackerel bolts away from the pull. That's the flyline placement, not the troll placement.
- **Nose hook** — becomes mandatory the moment any weight is added, because a butt-hooked bait under a sinker gets dragged backward and a mackerel swimming backward doesn't read as a natural feeding-fish silhouette.
- **Back/dorsal hook** is reserved for a kite bait only.

Be aware of what the KB does *not* say: it never writes "for slow-trolling a mackerel, nose-hook it" in one sentence. The nose hook is the position the corpus attaches slow-trolling to, and butt/back are explicitly scoped elsewhere — that's an inference across two notes, not a stated rule.

One corroborating observation on sardine: a nose-hooked live sardine slow-trolled **150–200 ft** behind the boat produced yellowtail, on a mix of circle and wide-gap hooks (`techniques/flyline.md`, `ROWgdFE9Ehc`, SoCal, 2015).

**Hook style and size.** Two doctrines sit side by side and the KB doesn't reconcile them:

- **SoCal slow-troll default: J hook, 3/0**, with **1/0, 1 and 2** carried for small bait and finicky fish. Downsize line class and hook size *together* — downsizing only one rarely works (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`). J hooks are also the general pick for island yellowtail (`tackle/hooks.md`, `m2q22sPPkEM`).
- **Baja slow-troll programs run circle hooks** — Cedros and La Paz both (`QSmE3mdEL28`, `Zo92MG459gQ`, `ORC1A68cEeM`). Circle sizing is matched to the bait: Cedros ran Owner ringed offshore hooks in **1/0, 3/0 and 5/0** to cover whatever the dock had, up to **15 in** mackerel (`tackle/hooks.md`, `_C7TJoGT0nw`, `qHS-ewTQs9Q` — ⚠ the notes disagree internally on whether the source said 1/0/3/0/5/0 or literal "10/30/50"). For a genuinely big mackerel on thick-wire Mustad circles, **8/0, 6/0, 4/0** is the logged range, though that's from a bluefin-foamer flyline context (`tackle/hooks.md`, `RbqOKkINSCM`).
- If you run a circle: **don't swing.** Engage the reel, point the rod where the fish is going, wind tight — it pins the corner of the mouth on its own (`tackle/hooks.md`). Cedros: "no strike — let the rod load and wind tight." La Paz ran a counted variant: give the fish a **3-second count ("1, 2, 3")** before putting the reel in gear (`techniques/trolling.md`, `ORC1A68cEeM`).

**Line and leader — SoCal local coast** (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`):

- **Mainline 25–40 lb**, and carry a lighter option (20–25 lb) even on a day that starts on 40 — a full day of bites on 40 lb is described as luck rather than the norm locally: *"you'd be really surprised how hard you can pull on 25 lb"* once the drag is set for it.
- **~6 ft of fluorocarbon matched to the mainline** — 30 lb main gets 30 lb fluoro — and **at most halve it** when they're finicky (30 lb main → 25 lb fluoro floor). Going lighter than that costs fish to abrasion right at the hook.
- **Full outfit as described:** an **8 ft fiberglass or composite rod**, a **size-25 reel**, **50 lb braid** to a **30–40 lb mono top shot**, then the short fluoro to the hook. The braid capacity is load-bearing — see the drag section.

**Setback: 100–150 ft.** Not far; a long setback isn't the goal. Past ~150 ft you lose the hook-setting benefit of boat motion and gain nothing (`techniques/slow-trolling-bait.md`). Cedros ran shorter — 50–75 ft, or "not too far" (`9tIp4n7q850`, `QSmE3mdEL28`).

**Drag — light, and let the boat set the hook.** On a lever drag, around the **"2"** mark: enough to seat the hook the instant a fish eats, not enough to snap the leader or overrun the reel on the strike. Whether to fish in gear at all is angler preference; the light setting is the specific call. **Why you can't pin it:** a yellowtail eating a slow-trolled bait takes **50–100 yd immediately**, more on a bigger fish — a locked drag at that moment either parts the line or backlashes the reel (`techniques/slow-trolling-bait.md`, `HTowqnwAMeA`). The La Paz crew made every angler **test their drag before starting the troll** — "this style of fishing always ask the captain to test your drags, numero uno" (`ORC1A68cEeM`).

---

### 4. The heavy variant — resident fish over shallow structure (Baja)

If you're running this at Cedros-class shallow structure rather than the SoCal coast, the KB's router row is a different build entirely: **slow-trolled live giant mackerel on a circle hook, worked over the structure**, 40 lb line-class floor with 50 lb for most of it (`species/yellowtail.md`). The trip footage behind it went heavier still, and the KB keeps those side by side rather than reconciling them (`techniques/trolling.md`):

- Rocks cresting at **28–30 ft** (one stop over 40 ft), **80–100 lb line class**, circle hook, no strike/wind tight, **back the boat down** once a big fish takes off, and "rail" the fish over the gunnel if it can't be lifted in the structure (`QSmE3mdEL28`).
- Day two at the same rock: **65 lb braid to 80 lb fluorocarbon leader**, roughly 30 ft of water — and **zero yellowtail bites all day** (`I-QBxuV2p7M`). "Every single day is different here."
- Big, fat **~2 lb mackerel** on a circle hook, angler credited the fish to **straight 80 lb**, landed a **45 lb personal best** in water shallow enough to see the bottom (`Zo92MG459gQ`).
- La Paz shallow rock: **12 ft** of water, **40 lb**, circle hooks, doubles close to 30 lb — and the guide crew's own closing line, "you win some and you lose more when you're fishing shallow water yellowtail" (`ORC1A68cEeM`).
- A bank high-spot variant at "El Bajo" (≈50 ft low tide, ≤80 ft high): let out ~**10 yd**, drop the weight straight to the bottom, and let the ongoing troll speed lift the bait back up into the high column rather than cranking it — **65 lb braid to 60 lb fluorocarbon** (`92y14x33etQ`).

---

### 5. Making the bait

If you're catching your own: sabiki at ~**100 ft** with an **8 oz** sinker at the Coronados (or La Jolla during shortages) — Cameron has loaded five twelve-inch mackerel on one drop, and twelve-inch mackerel are big, hearty baits, heartier than sardine (`bait/making-bait.md`, cameron).

---

### What the KB doesn't cover

Listed below in `gaps_admitted` — the main ones are that no note states a slow-troll hook placement for mackerel in so many words, there's no rule reconciling the SoCal J-hook default against the Baja circle-hook programs, and there's no boat-handling detail at all (trolling pattern over structure, turns, how many rods, holder geometry).


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/slow-trolling-bait.md`, `techniques/evidence/slow-trolling-bait.md`, `techniques/flyline.md`, `techniques/trolling.md`, `species/yellowtail.md`, `species/evidence/yellowtail.md`, `species/yellowtail-coronado-islands.md`, `species/yellowtail-tube-bait-fishing.md`, `bait/fishing-live-bait.md`, `bait/making-bait.md`, `tackle/hooks.md`, `tackle/star-drag-vs-lever-drag.md`  
*videos:* `HTowqnwAMeA`, `_C7TJoGT0nw`, `qHS-ewTQs9Q`, `w5_x6kkN-xE`, `T3p1mrqNjIo`, `mscHk0qiXnk`, `SluBXkT3cuw`, `ROWgdFE9Ehc`, `QSmE3mdEL28`, `I-QBxuV2p7M`, `9tIp4n7q850`, `Zo92MG459gQ`, `ORC1A68cEeM`, `92y14x33etQ`, `0dIwWiOc1NY`, `D5DR7Kx42_A`, `tpmOYXYQwhU`, `RbqOKkINSCM`, `m2q22sPPkEM`, `5Oh3IPIC5g4`  
*gaps admitted:* No note states a hook placement for a slow-trolled MACKEREL directly — the nose hook is the placement the corpus ties to slow-trolling generally (bait/fishing-live-bait.md, techniques/flyline.md), while the mackerel-specific section only splits butt (zero-weight flyline) vs nose (any weight) vs back (kite only); the mackerel + slow-troll pairing is an inference across two notes. | No rule reconciling the SoCal slow-troll J-hook default (3/0, HTowqnwAMeA) against the Baja slow-troll circle-hook programs (Cedros/La Paz) — the KB keeps them side by side with no decision frame for which to run where. | No boat-handling detail anywhere: trolling pattern over structure, how to turn, how many rods to run, rod-holder geometry, or where baits sit relative to each other in a slow-troll spread. | No mackerel-specific slow-troll speed in mph for SoCal — the 1.5-3 mph band is bait-graded and general, and the only numeric mackerel figure (~3 mph) is a Cedros, Baja observation from an unregistered channel. | No guidance on bait husbandry during the troll: how long a mackerel lasts on the troll, how often to change it, or how to tell a spent bait from a swimming one beyond 'watch it swim'. | No stated leader LENGTH for the Baja circle-hook mackerel program (only line classes and top-shot ratings: 40 lb fluoro at Cedros, 80 lb fluoro day two, 60 lb fluoro at El Bajo). | No targeted-depth control for slow-trolling — the note calls it near-surface and explicitly not a targeted-depth method; the one downrigger variant (2 lb max weights, 30 ft) is logged as secondhand and unconfirmed in techniques/evidence/slow-trolling-bait.md. | No head-to-head comparison in the corpus of slow-troll vs flyline productivity on the same day/fish — the choice rests on the meter read (stratified column vs bottom-balled) and the tide/current-turns-them-onto-bait cue only. | No numeric SST bands for yellowtail anywhere in the KB (species/yellowtail.md flags this gap itself), so no water-temperature trigger for choosing this technique. | No circle-hook regulatory status for Mexican waters is confirmed in the corpus — one 2019 video calls a circle hook 'mandatory' in Baja California Sur, logged unverified against CONAPESCA/DOF text; verify current rules before fishing Mexico. | The prompt gave no conditions, so nothing here is tuned to a specific date, zone, wind, tide or water state — no BightSST pull was made.

</details>

### 12. [technique] When does kite fishing for bluefin beat a flyline, and what is the setup?

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B3', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three get the decision boundary right — kite is a grade-and-wind call (100-300 lb, ~8-15 kt, fish located), flyline is the chummed/picky-bait call — and all three honestly state that no head-to-head rule exists in the KB. A wins on two concrete margins: it is the only answer that flags the 8-15 kt band as internally contradicted inside its own notes (kite note carries no wind numbers; the ~8 kt figure is flagged unsupported and contradicted by a source that kites under 8 kt) and replaces it with a behavioral test, and it is the only one that closes the loop for a 22 ft panga — the small-boat fight procedure (rod stays in the holder, big gentle circles, forward only, ~45 degrees) plus a blunt shopping list of the kite, flyers, skewers, 500 lb swivel and 12/0 J that the profile does not own. B is a very close second with the best side-by-side outfit table and equally complete rigging, but leaves the wind ceiling open ("nothing says what to do at 18 kt") where A and C tie it to the 12 kt whitecap cutoff, and stops at "the rod is designated" for the profile. C reads cleanest and is the only one to stamp a regulation correctly (CDFW, as of 2024-11, verify current), but its fighting-outfit spec is materially thinner — no front hook size, no top shot, no swivel, no drag — so the "what is the setup" half is incomplete.

- *B2 reasons:* found: right rows found and the kite-vs-troll adjudication correctly distinguished from the unstated kite-vs-flyline rule; decision table is the cleanest to read. specific: 100-300 lb, 8-15 kt, 3-3.5 ft leader, 200-400 lb (typ. 400) / 300-400 lb fluoro, 5/0 5X treble, 45 degrees, 10-12 flyers, 120-150 yd, 8 mph / ~2 kt / 8.5 kt speeds, 272 lb fish; richest flyline-side detail (4/0 thin-wire circle, 8 ft 20-50 lb + Torium 16 two-rod system). sourced: note links plus video ids on most claims; promotional 'California Flyer' claims correctly demoted. scoped: region context held, and the only answer to carry a regulation properly — CDFW two Pacific bluefin/person/day, as of 2024-11, verify current. honest: leads with the no-head-to-head caveat, flags the opposing 8 kt frameworks, the 15 kt band vs 12 kt run cutoff, the unresolved balloon lift and tagline audio. actionable: the setup half is thinner — no front J-hook size, no top-shot or main-line spec beyond '~100 lb braid', no 500 lb swivel, no drag figure, one reel example, and no owned-vs-missing gear reckoning, so an angler still has holes to fill before rigging.
- *B3 reasons:* found: correct material — grade/wind/concentration triad, the Santa Barbara Island microbait conversion, the mixed kite+flyline sessions, the whole rigging chain. specific: same parameter set as A plus a five-row boat-by-boat outfit table (ATD 50 / Tiagra 50W / Talica 25, 200 lb spectra to 400 lb mono, 40 lb drag, 100 lb top-shot floor), 8.5 kt vs 13-15 kt, ~$30 pre-rigged flyer. sourced: per-row video ids and note paths throughout; confidence and channel status carried inline. scoped: SoCal vs Baja labeled (squid rig marked Baja long-range), panga helium constraint framed as platform not fishery; no regulation asserted. honest: explicit that no head-to-head rule exists, flags the two opposing ~8 kt frameworks, lists nine real gaps; says flatly there is no upper wind limit rather than inventing one. actionable: complete enough to buy, rig and deploy; weaker only on small-boat execution and on connecting the kite band to a go/no-go sea-state ceiling.
- *NOW reasons:* found: hit both halves — the kite/flyline boundary (grade, wind, located fish, microbait selectivity, May priors) and the full kite program, plus the flyline counter-cases. specific: 100-300 lb grade, 8-15 kt, 3-3.5 ft of 200-400 lb (typ. 400), 9/0-12/0 J + 5/0 5X treble, 500 lb BB swivel, 130-200 lb braid / 15 ft 135 lb top shot, 45-degree wings, 10-12 flyers, 120-150 yd kite run, 4-5 kt hookset, 40-45 min fight. sourced: note paths plus video ids on essentially every parameter (YsiHziY_PWw, GqcVaTIlyg0, 2y0VznL2qk8, RM7cBgCDWFA, fgTmUq78ofQ, JiJYamo0QHk). scoped: SoCal/Baja separation held, panga platform constraints (helium out, 8-12 kt working window vs the 12 kt whitecap cutoff) called out; no bare regulation stated. honest: uniquely flags that the 8-15 kt band is internally contradicted in its own KB, flags garbled captions on the 40-45 min figure, flags the untested sliding-sinker outlier, no relative time. actionable: only answer that gives the 20-30 ft private-boat fight procedure (rod in holder, big gentle circles, forward only, ~45 degrees) and an explicit owned-vs-missing gear list — rig-and-run usable.

<details><summary>Full prompt</summary>

When does kite fishing for bluefin beat a flyline, and what is the setup?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Kite vs flyline for bluefin — when, and the setup

**Short version from the KB:** the kite is a **grade + wind** call, not a general "better bait" call. Fly the kite when the fish present as **100–300 lb** and there is **~8–15 kt of wind** to hold a kite up; flyline when you're on **chummed / picky fish on a bait line**, or when the wind won't fly a kite. Nothing in the KB says the flyline is the weaker method in the abstract — on plenty of days it's the only thing that gets bit.

Note up front: **no note in this KB states a head-to-head kite-vs-flyline rule or hookup-rate comparison.** The ranking below is assembled from the router rows in [`species/bluefin-tuna.md`](species/bluefin-tuna.md) and the wind logic in [`techniques/kite-fishing.md`](techniques/kite-fishing.md) / [`species/bluefin-trolling.md`](species/bluefin-trolling.md). The kite-vs-**troll** decision is the one the KB actually adjudicates.

## When the kite wins

| Condition | Call | Source |
| --- | --- | --- |
| Fish **100–300 lb**, wind **~8–15 kt**, fishable swell | **Kite** — a flying fish under a kite is *the* most effective method for that grade | [`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`species/bluefin-trolling.md`](species/bluefin-trolling.md) |
| Fish located and concentrated enough to sit over, wind will fly the kite | Kite over trolling — "kite is king for cows" doctrine (high) | [`species/bluefin-trolling.md`](species/bluefin-trolling.md) |
| Fish **locked onto tiny natural bait** (saury, anchovies, microbait) and refusing everything | Kite converted where a trolled spreader-bar pass and cast plugs both went scoreless — SoCal, NE of Santa Barbara Island (`mDmbGdQAy-4`) | [`species/bluefin-tuna.md`](species/bluefin-tuna.md) |
| Wind **too light to kite (under ~8 kt)**, OR fish too spread out to sit and kite over | **Not** kite — speed-troll a full-size Mad Mac 200 at **13–15 kt** (Winnicki) to locate; coverage need, not sea state (cameron) | [`species/bluefin-trolling.md`](species/bluefin-trolling.md) |
| Chummed up / picky on bait, 40–60 lb-class fish on the chum line | **Flyline** a sardine on a circle hook, scale the leader down | [`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`techniques/flyline.md`](techniques/flyline.md) |

**Where the flyline still owns the day** (so you don't over-rotate to the kite):
- One El Dorado trip, ~45 mi offshore SoCal, June 2023: the day's bluefin bit **strictly on flyline** — the boat tried a sinker rig and the fish would not take it (`oB4BpIUTTl4` / `r4J5nP5Bkl4`), [`techniques/flyline.md`](techniques/flyline.md).
- Highliner deckhand POV, 2023-04-24: **~90% of daytime bites came on flyline**, on a dedicated **25–30 lb fluorocarbon** flyline stick, majority on **size 2 circle hooks** (`149px8WQ2Ng`), [`species/bluefin-tuna.md`](species/bluefin-tuna.md).
- They are not exclusive. An intense sundown bite at Cortez Bank produced multiple **100 lb+** fish on **both the kite and flyline fished alongside it in the same window** (`zBd1mayUt_I`); the kite was also up during a hot morning bite alongside bait rods earlier in that same trip (`QSvzVHW9UMk`) — [`techniques/kite-fishing.md`](techniques/kite-fishing.md). Practically: fly the kite for the big-grade shot and keep bait rods working under it.

**Sub-decision once you've committed to the kite** (Capt. Dave Hansen, `2y0VznL2qk8`, [`techniques/kite-fishing.md`](techniques/kite-fishing.md)):
- **~8 kt of wind or more** → **troll a rubber flyer** ("Yummy Flyer") at about **8.5 kt** under the kite to cover water; a trolled bait converts a bite to a hookup at a better ratio than sitting dead-boat. Mark the school on the GPS when it produces and keep working it.
- **Under ~8 kt, with fish already spotted or marked heavy** → **dead-boat with a dead flyer** (typically **two**) under the kite or a balloon, drifted like float fishing. Never deploy a dead flyer speculatively — it's fished over confirmed sign, not blind water.
- Note the KB flags this ~8 kt mark as running **opposite** to the Mad Mac row's ~8 kt (there it triggers speed-trolling once the kite won't fly). The two frameworks are kept side by side, unreconciled — [`species/bluefin-trolling.md`](species/bluefin-trolling.md).

**Wind ceiling caveat:** the kite band tops out at 15 kt in the router, but [`conditions/sea-state.md`](conditions/sea-state.md) carries Hansen's personal **12 kt run cutoff** (above ~12 kt raises whitecaps) and names **12–15 kt wind with 4–8 ft swell at 9 s** as an unfishable combo (`NC3-3pJDEgo`). The KB does not reconcile these — read the upper half of the kite band against your own boat.

## The setup

**Fighting outfit** ([`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`species/bluefin-trolling.md`](species/bluefin-trolling.md), [`tackle/gear-classes.md`](tackle/gear-classes.md)):
- **150–200 lb class rod** — dedicated, pure leverage, **never casts**. In the class lexicon that's the trolling/spreader-bar class: 7–7.5 ft, XXXX-H, 150–200 lb, 2-speed, ~1000 yd capacity.
- **~100 lb braid** — for capacity and less wind-blow.
- Observed reel example: **Okuma Makaira 50 Wide** (`usHl-4SfqDA`).

**Bite leader / flyer rig** ([`rigging/flying-fish-harness.md`](rigging/flying-fish-harness.md)):
- **200–400 lb mono, typically 400** (`GqcVaTIlyg0`); the router's kite row calls **300–400 lb fluoro**. A commercially pre-rigged flyer seen in Baja was built on **300 lb** (`Ix0gG0-l3v0`).
- **Bite-leader length 3 ft, 3.5 ft max** (`YsiHziY_PWw`) — any longer and the swivel hits the rod tip before the fish is in gaff range.
- **Hooks:** large **J hook up front with a large treble trailing as a stinger**, the treble set into the back of the fish just behind the body stick, under the spine and out the other side. Tail treble spec: **5/0 5X-strong Mustad** (`YsiHziY_PWw`).
- **Harness:** skewer behind the shoulder just above the spine, a second opening the wing hole between ribs and wing, wings zip-tied open on both sides, **pinned at about 45°** — set further out and a swell knocks the bait off its presentation. A body skewer runs in through the mouth about three-quarters of the way, lifting the tail as you finish for a slight tail-down profile; a final skewer pins the mouth shut so water isn't scooped through the lower lip.
- **Rig 10–12 flyers for a four-angler day**, stored neatly in the cooler.
- Field simplifications, kept side by side: **staple a popsicle stick** to lock the wings (`usHl-4SfqDA`); **rubber band instead of zip tie** (`Ix0gG0-l3v0`).

**The kite line side** ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)):
- The kite flies on its own dedicated line — **straight braid**, spooled out roughly **a couple hundred yards** once set (`Ix0gG0-l3v0`).
- **Breakaway to the fishing line:** thread a small ring onto the fishing line *before* tying on the snap swivel, then **tie a rubber band from that ring to the kite line's release clip** — no knot ties the fishing line to the clip. The rubber band is the weak link that pops on the bite (`Ix0gG0-l3v0`).
- **Quick release on the kite line:** make a loop in the line and flip/hook that loop onto the release-clip mechanism rather than tying to it.
- **Paying out:** loosen the **star drag** on the kite reel to control payout instead of thumbing the spool.
- **Balloon-to-kite (if you run one):** the balloon twists into a dedicated balloon clip with no knot, the clip is rubber-banded to the kite, and about **three taped line tethers** back that rubber band up so a failure doesn't separate balloon and kite (`vCskOx6N-XM`). **Launch:** hand the kite up and let it go with the wind — it flies straight up off the stern, then carries away once the boat turns onto an angle.
- **Set height:** as high as you can and still see the flyer skipping — bait visibility sets the ceiling, not a fixed number. **Kite distance 120–150 yd** off the boat on one San Diego session, shifting with wind, drift and boat heading (`rsCAh-QyK60`).
- **Boat speed working a kited spread:** **8 mph (~7 kn)** trolling the flyer on that San Diego trip (`rsCAh-QyK60`); **~2 kt on a single center engine** to work a spread slowly while searching in the Baja tournament (`Ix0gG0-l3v0`); **~8.5 kt** for the trolled rubber flyer (`2y0VznL2qk8`).
- **Gyro-stabilized binoculars called mandatory** — both for spotting fish and for watching the flyer stay upright and skipping (`Ix0gG0-l3v0`); same doctrine as [`planning/search-and-glassing.md`](planning/search-and-glassing.md).

**Presentation:** adjust the clip and kite so the **flying fish just touches the surface** — skipping and splashing, never dragging under, never airborne. On a dead-boat set, keep it **dapping** — in constant contact with the water, bouncing with the swell — and watch it continuously through binoculars.

**The bite:** the line **pops out of the release clip** and you come tight directly to the fish — no clip in the fighting system. On a dead-boat bite (surface explosion on the flyer), put the boat in gear and drive **forward gently, ~4–5 kt, not a hard throttle**, to load the rod without shock-loading it (`2y0VznL2qk8`). Then lay the short leader flat on the surface to bring the fish into gaff range at the swivel. Fight mechanics — gear-tapping in and out at ~8 kt, walking down-swell for the whole fight, avoiding the death circle — are in [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md). One kite fish in the corpus was fought **40–45 minutes** (`zBd1mayUt_I`); another weighed **272 lb** (`rsCAh-QyK60`).

**Bait alternatives to the rigged dead flyer:**
- **Live mackerel, back/dorsal-hooked right in front of the dorsal fin** — the kite is the *only* application where the back hook is used on mackerel. It sits flat on the surface and daps each time it touches down, without the leader dragging where a leader-shy tuna sees it. Same 100–300 lb grade; also draws yellowtail and calico (`w5_x6kkN-xE`) — [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md).
- **Whole squid on a double-hook rig**, drifted with current and wind so it offers the fish no resistance — Baja long-range, giant grade (`pk2blktDQ9Y`). No hook size, spacing or leader weight given on camera.
- **Artificial flyers:** the rubber "Yummy Flyer" for trolling (`2y0VznL2qk8`); a hard-bodied "California Flyer" fished dead-boat that slides up the leader on a hookup so it survives to be reused, with replaceable wings (`vCskOx6N-XM` — brand claims logged as promotional/low).

**Light-wind fix and its limit:** a **helium-balloon assist** is the general way to hold a kite up in light wind, but **Cameron's panga program rules helium out** — too expensive, no room for a tank — a platform constraint, not a rule of the fishery. On a bigger boat the light-wind window reopens ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)). The KB does not resolve whether a balloon flown *with* the kite in fishable wind (`usHl-4SfqDA`) is extra lift or a visual marker.

**Flyline side, for contrast** ([`techniques/flyline.md`](techniques/flyline.md), [`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md)):
- **40–60 lb class**, circle hooks **1–2/0**; a first big-fish build wants **400+ yd of line, 80 lb backing, 50–60 lb mono top shot, ~3 ft of fluoro**.
- Hansen's big-bluefin rig: **circle hook** specifically because their teeth saw through leader — a corner-of-the-mouth hookset keeps the leader out of the teeth — on a **San Diego jam**, **no weight or swivel**, **~3–4 ft of 80 lb straight fluorocarbon** (`RbqOKkINSCM`). Sportboat sardine: **4/0 thin-wire circle**, straight-tied, thin wire because a sardine can't swim a heavy-gauge hook convincingly (`ftEvyfwjZFU`).
- Two-rod system: **8 ft, 20–50 lb rod / Torium 16 / 30 lb mono top shot (50+ yd)** for 20–50 lb grade; **7 ft, 30–80 lb / Trinidad 20A / 40–50 lb** straight for bigger (`jQW2HLkMsmY`).

## Resolving against your profile ([`profiles/cameron/rods.md`](profiles/cameron/rods.md))

- **Kite rod:** the **Fathom 80 setup** — Okuma PCH-C-741XXXXH (7'4", XXXX-H, 150–200 lb) + Penn Fathom II 80LD2 2-speed, **~1000 yd of 100 lb braid**. The profile already designates it the future kite rod: keep the 100 lb braid for capacity and less wind-blow, run **200 lb leader**, and the small boat can chase. It is the one setup in the inventory that has not yet caught a bluefin.
- **Flyline rod:** the **Avet setup** — Teramar TMC90MHB2 (9'0", MH, fast, 30–65 lb) + Avet MXJ, 50 lb braid.
- You started kite fishing **July 2026** and ruled out the helium assist for the panga ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)).
- **Bag limit (California/CDFW, as of 2024-11, verify current regs before fishing):** two Pacific bluefin per person per day (`usHl-4SfqDA`).

## Common failures ([`techniques/kite-fishing.md`](techniques/kite-fishing.md))

- **Wings set too far out** on the flyer — a swell knocks the bait off and ruins the presentation. Rig them tighter, ~45°.
- **Leader too long** — you hit the swivel before the fish is in gaff range.
- **Letting the flyer sink or drag** instead of skipping — the splashing surface commotion is the whole trigger.
- Loose skewers or zip ties let the harness slip and kill the action; too light a leader risks a bite-off on this grade.

## What the KB does not cover

- No head-to-head kite-vs-flyline rule or hookup-rate comparison — the ranking above is assembled from grade + wind rows, not a stated doctrine.
- No kite size, model, or wind-range-per-kite-size guidance, and no kite-reel or kite-line test spec beyond "straight braid, a couple hundred yards."
- No numeric kite flying height (bait visibility sets it), and no guidance on managing a kite and flyline rods in the same spread.
- The Baja tournament's "mandatory ~30 ft tagline" attachment and mechanism are unresolved on the audio and not confirmed as any jurisdiction's regulation.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `techniques/kite-fishing.md`, `techniques/flyline.md`, `techniques/fighting-big-bluefin.md`, `rigging/flying-fish-harness.md`, `bait/fishing-live-bait.md`, `tackle/gear-classes.md`, `conditions/sea-state.md`, `profiles/cameron/rods.md`  
*videos:* `YsiHziY_PWw`, `GqcVaTIlyg0`, `2y0VznL2qk8`, `w5_x6kkN-xE`, `rsCAh-QyK60`, `Ix0gG0-l3v0`, `vCskOx6N-XM`, `usHl-4SfqDA`, `zBd1mayUt_I`, `QSvzVHW9UMk`, `mDmbGdQAy-4`, `149px8WQ2Ng`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `ftEvyfwjZFU`, `RbqOKkINSCM`, `jQW2HLkMsmY`, `pk2blktDQ9Y`, `NC3-3pJDEgo`  
*gaps admitted:* No note states a head-to-head kite-vs-flyline rule or hookup-rate comparison; the KB only adjudicates kite vs troll, so the kite/flyline ranking had to be assembled from the router's grade + wind rows. | No kite size, model, brand, or wind-range-per-kite-size guidance anywhere in the KB. | No kite-line test or capacity spec and no kite-reel spec beyond 'straight braid' and 'a couple hundred yards'. | No numeric kite flying height — the only guidance is 'as high as you can still see the flyer'. | No guidance on running a kite and flyline rods simultaneously (spread management, rod count, keeping bait lines clear of the kite line) — only the observation that both were fished in the same window. | The ~8-15 kt kite band is never reconciled against the sea-state go/no-go thresholds (12 kt run cutoff; 12-15 kt with 4-8 ft at 9 s called unfishable). | The balloon-vs-kite lift-assist relationship is explicitly unresolved across three sources (helium assist for light wind, balloon flown with the kite in fishable wind, stand-alone balloon with no kite). | The Baja tournament's 'mandatory ~30 ft tagline' attachment point and mechanism are unresolved on the audio and unconfirmed as a regulation. | No hook size, hook spacing, or leader weight is given for the squid double-hook kite rig. | No flyer-consumption or deployment-count guidance beyond 'rig 10-12 flyers for a four-angler day'.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short version

The kite is a **grade-and-wind** call; the flyline is a **bait-and-behavior** call. The KB's rule, straight out of the bluefin decision table (`species/bluefin-trolling.md`):

> **8–15 kt wind, fishable swell, 100–300 lb fish present → kite a flying fish.** *The* most effective big-fish method when the wind will fly a kite.

The flyline row in the same family of tables (`species/bluefin-tuna.md`) is a different situation entirely — **"chummed up / picky on bait" → flyline a sardine on a circle hook, 40–60 lb class.**

So the kite beats the flyline when **all three** of these are true, and it's the flyline's day when any of them isn't.

---

## When the kite wins

1. **Grade is 100–300 lb.** `techniques/kite-fishing.md` scopes the whole method to that class. The Searcher's own kite program is stated as reserved for the biggest fish — the boat typically doesn't even fish it until **100 lb+ bluefin are confirmed around** (`fgTmUq78ofQ`, Art Taylor/Mike, 2021-05-14). A flyline outfit at 40–60 lb class is not the tool for that grade, and one captain's briefing on the Ranger 85 warned explicitly against fighting a big bluefin on tackle "not meant" for it (`zBd1mayUt_I`).
2. **You have wind — 8–15 kt.** No wind, no kite. Marginal, gusty, or dying wind makes the flyer inconsistent on the surface, and `techniques/kite-fishing.md` calls that the cue to switch to speed-trolling (`techniques/speed-trolling.md`) instead — not to a flyline. Helium-balloon assist is the general light-wind fix; **Cameron has ruled it out** on the panga (too expensive, no room for a tank) — a platform constraint, not a rule of the fishery.
3. **The fish are concentrated enough to sit over.** `species/bluefin-trolling.md` is explicit: if fish are too spread out to sit and kite over, that's a **coverage** problem, not a sea-state problem (cameron), and you speed-troll a Mad Mac at **13–15 kt** to locate first. The stated program from Tanner Bank, late October 2021: troll spreader bars to cover ground, then **once the sounder is marking good numbers, stop and set a dead flying fish under the kite in the drift** over the marks (`vCskOx6N-XM`) — multiple 100 lb+ fish that day for a crew entirely new to bluefin.

**The strongest case for the kite over bait** in the corpus: NE of Santa Barbara Island, foamers all around the boat, and a trolled spreader-bar pass plus cast plugs both went scoreless — the crew's read was the fish were locked onto **tiny saury, anchovies and microbait**. Going back to the dead flying fish under the kite is what converted (`mDmbGdQAy-4`). And a captain running charters off a 39 ft Contender ranked **kite-fished frozen dead flying fish as producing the majority of his boat's bites** (`ouBrIdO7d4k`, medium confidence, unregistered channel).

## When the flyline wins instead

- **Fish are on the chum line and picky.** That's the flyline row. The mechanism doctrine (Cesar, Eric's Tackle, `48ZFXnCTTQE`): in warm water bait doesn't "cure" and toughen, so a bait on line that's too thick won't swim convincingly. Cap the fly line at **20–25 lb test, no more than 30**. Vince at Fisherman's Landing states the same range against bluefin grading **40–60 lb** (`icpm7gADxvU`).
- **Fish flat refuse anything else.** A June 2023 El Dorado day ~45 mi off: bluefin bit **strictly on flyline**, and the boat's sinker rig was refused outright — **25–40 lb test to a straight No. 2 hook** on sardine (`oB4BpIUTTl4` / `r4J5nP5Bkl4`).
- **No wind, or no flyers.** The kite has a hard input requirement the flyline doesn't.

## The honest caveat: they are not really rivals

`species/bluefin-tuna.md` logs a **sundown Cortez Bank bite that produced multiple bluefin over 100 lb on the kite *and* on flyline fished alongside it in the same window** (`zBd1mayUt_I`), and a daytime kite flown alongside bait rods earlier in the same 3-day trip (`QSvzVHW9UMk`). Capt. Dave Hansen describes his boat's program as a **kite/flyline volume program** — one program, both tools — built to land six fish in the time a flat-fall boat lands one (`JiJYamo0QHk`). Fly the kite as the big-fish line and keep bait in the water underneath it; the KB never asks you to pick one exclusively.

---

## The setup

### Kite-line side (this is a separate system from your fishing rod)

- Kite flies on its **own dedicated line — straight braid, no leader section**, spooled out **a couple hundred yards** once set (`Ix0gG0-l3v0`, Baja tournament, medium confidence).
- **Breakaway connection:** thread a small ring onto the *fishing* line **before** tying on the snap swivel, then **rubber-band that ring to the kite line's release clip**. No knot ties the fishing line to the clip — the rubber band is the weak link that pops on the bite (`Ix0gG0-l3v0`).
- **Quick release on the kite line:** make a loop and flip/hook it onto the release-clip mechanism rather than tying to it.
- **Paying out:** loosen the **star drag** on the kite reel to control payout speed instead of thumbing the spool.
- **Distance out:** **120–150 yd** ran on one San Diego session, shifting with wind, drift and the boat's direction of travel (`rsCAh-QyK60`, 2017-06-06, 22 ft center console ~40 mi off San Diego, medium confidence).
- **Height:** as high as you can go **while still seeing the flyer skip** — bait visibility sets the ceiling, not a fixed height (`rsCAh-QyK60`).
- **Balloon-to-kite variant** (`vCskOx6N-XM`): balloon twists into a dedicated clip with no knot, clip is rubber-banded to the kite, plus ~three lengths of **tape-wrapped fishing line as a safety tether** so a broken rubber band doesn't send the balloon and kite separate ways. Launch by handing the kite up into the wind; it flies straight off the stern, then carries away once the boat turns onto an angle.
- **Gyro-stabilized binoculars are called mandatory** — both for spotting fish and for watching the flyer stay upright and skipping (`Ix0gG0-l3v0`); same doctrine as `planning/search-and-glassing.md`.

### The fighting outfit

`tackle/gear-classes.md` puts this in the **trolling / spreader-bar class**: 7–7.5 ft, XXXX-H, 150–200 lb, 2-speed, ~1000 yd capacity. `species/bluefin-trolling.md`'s gear summary: **dedicated 150–200 lb class, ~100 lb braid** (capacity plus less wind-blow), **never casts**.

Real boat-supplied examples, kept side by side rather than reconciled into one rig:

| Source | Rod | Reel | Line |
| --- | --- | --- | --- |
| Hansen's own program (`JiJYamo0QHk`) | — | **40 lb of drag** set | **200 lb braid → 400 lb fluoro** |
| Searcher's three kite setups (`fgTmUq78ofQ`) | Seeker 2x4 | Accurate ATD 50 | **200 lb spectra tied straight to 400 lb mono** |
| Logan Watson, Searcher (`RM7cBgCDWFA`) | 7'6" **rail rod, 80–200 lb unlimited class** (built so a big fish can be fought off the rail without breaking the rod down) | Shimano Tiagra 50 Wide | **15 ft top shot of 135 lb mono over 200 lb braid**; general statement that kite main line wants roughly **1,000 yd of 130–200 lb mono** |
| Team Searcher (`lf3S28nh-kk`) | big Seeker rail rod | Accurate twin-drag | **130 lb braid**; if bringing your own outfit, the stated minimum is **100 lb top shot on a big, heavy rail rod** |
| Fisherman's Landing rental, 2021 (`shZCjX2-fkI`) | 7 ft graphite Calstar 770XH rail rod | Shimano Talica 25 two-speed | **80 lb** — with an **80-lb-class two-speed as the stated floor** for a personal kite outfit |

A **500 lb ball-bearing swivel** joins the top shot to the flying-fish-harness leader (`RM7cBgCDWFA`).

### The bait and harness (`rigging/flying-fish-harness.md`)

- **Bite leader: 200–400 lb mono, typically 400** (`GqcVaTIlyg0`), and **3 ft, 3.5 ft at the max** (`YsiHziY_PWw`) — any longer and the swivel hits the rod tip before the fish is in gaff range. Corroborated independently as **3 ft of 400 lb mono** (`RM7cBgCDWFA`).
- **Hooks:** standard San Diego flyer rig is a **big J up front with a large treble trailing as a stinger** — **9/0–12/0 J (Owner)** with a **5X-strong Owner treble** (`RM7cBgCDWFA`), or a **12/0 stainless Mustad plus treble stinger** (`fgTmUq78ofQ`). Tail treble also specced as **5/0 5X-strong Mustad** (`YsiHziY_PWw`). **Conflict, kept side by side:** Hansen runs a **single hook, no treble** — "we is single hook, no trebles" (`JiJYamo0QHk`). The choice turns on your own confidence in hook-holding vs. the fouling/damage cost of a treble; section order here is not a ranking.
- **Wing angle: about 45°.** Set further out and a swell knocks the bait off its presentation (`YsiHziY_PWw`). Skewer behind the shoulder above the spine, second skewer opening the wing hole, zip ties through additional holes, everything cinched so nothing slips. Field simplifications: **staple a popsicle stick** across the bait (`usHl-4SfqDA`), a **rubber band** instead of a zip tie (`Ix0gG0-l3v0`), or **30–50 lb braid tied through the wing hole** at the second or third bone in from the edge, finished with a third locking knot so it can't slip (`2TmLaSCmfC8`).
- **Body skewer** in through the mouth, pushed about three-quarters in, lifting the tail as you finish so the bait sits slightly down-and-tail-in; a **final skewer pins the mouth shut** so it doesn't scoop water.
- **Quantity: rig 10–12 flyers for a four-angler day**, stored neatly in the cooler. Most anglers buy them at the tackle shop (a pre-rigged dead "G Fly Yummy" ran ~$30 each in 2021, `2TmLaSCmfC8`); you can sabiki your own but it's hard. Rig them **thawed a little but not fully** (`2TmLaSCmfC8`).

**Bait alternatives:** a **live mackerel, back/dorsal-hooked** — and that back hook is used **only** on the kite, never on a normal flyline (`w5_x6kkN-xE`, Hansen, high confidence; details in `bait/fishing-live-bait.md`). For giant-grade Baja tuna, **whole squid on a double-hook rig** put out and left to drift (`pk2blktDQ9Y`, medium confidence).

### Running it — the wind sub-rule inside the kite program

Hansen's second, flyer-specific wind rule (`2y0VznL2qk8`, `techniques/kite-fishing.md`):

- **~8 kt wind or more → troll a rubber flyer ("Yummy Flyer") at about 8.5 kt** under the kite. Covers water while searching and converts bites to hookups at a better ratio than sitting dead-boat. Once trolling produces a school, mark it and keep working it.
- **Under ~8 kt, with fish already located** (surface sign or heavy marks) **→ go dead-boat with a dead flyer**, typically **two**, under the kite or a balloon, drifted like float fishing. **Never deploy a dead flyer speculatively over blind water.**

⚠ **Flagged conflict, not reconciled in the KB:** this ~8 kt mark runs the *opposite* direction from the Mad Mac row — here ~8 kt triggers trolling *under the kite*; there ~8 kt triggers speed-trolling *because the kite won't fly*. Different lure, different speed (8.5 kt vs 13–15 kt). Both frameworks are kept side by side in `species/bluefin-trolling.md`.

Observed working speeds vary widely: **8 mph (~7 kn) on the GPS** while trolling a flyer under the kite (`rsCAh-QyK60`) versus **~2 kt on a single center engine** to work the spread slowly while searching (`Ix0gG0-l3v0`).

### The presentation — the whole trigger

- Adjust the clip and kite so **only the flying fish touches the surface**. It must be **skipping and splashing**, never dragging under and never airborne.
- **The single most-flagged mistake:** flying the bait clear through the air like a kite itself instead of skipping wave-to-wave. Hansen's stated reason — *the fish are in the water, not the sky* — the bait has to stay in constant contact with the surface (`JiJYamo0QHk`).
- **Dapping:** drive forward a little to open distance, then lower the flyer slowly onto the surface and keep it bouncing with the swell. Watch it continuously through binoculars.
- **Hookset on a dead-boat bite:** the take is a surface explosion. Put the boat in gear and drive **forward gently — about 4–5 kt, not a hard throttle** — to keep the rod bent and drive the hook home without shock-loading it (`2y0VznL2qk8`).
- **On the bite** the line **pops out of the release clip** and you come tight directly to the fish — no clip anywhere in the fighting system.
- **At the boat:** lay the short leader out **flat on the surface** to bring the fish into gaff range at the swivel. Then `techniques/fighting-big-bluefin.md` — boat-driven tension, walking down-swell the whole way — and `fish-care/gaffing.md`.

Expect a real fight: one kite-hooked fish on that Cortez sundown bite went **roughly 40–45 minutes** (`zBd1mayUt_I`); a kite-caught flying-fish-lure fish off San Diego weighed **272 lb** (`rsCAh-QyK60`).

### Common failures (`techniques/kite-fishing.md`)

- **Wings set too far out** — a swell knocks the bait off. Rig them tighter, ~45°.
- **Leader too long** — you hit the swivel before the fish is in gaff range.
- **Letting the flyer sink or drag** instead of skipping — the splashing surface action *is* the trigger.

---

## For your boat specifically

`profiles/cameron/rods.md` designates setup #7 — **Seeker-class rod, Penn Fathom II 80LD2 two-speed (4.2:1 / 1.6:1, 50 lb max drag), ~1000 yd of 100 lb braid** — as the **future kite rod**, keeping the 100 lb braid for capacity and less wind-blow, 200 lb leader, on the reasoning that a small boat can chase. That's the only outfit in your inventory that matches the 150–200 lb kite class, and it's currently spreader-bar-trolling-only. Note the corpus kite leaders run **300–400 lb**, heavier than the 200 lb noted in your profile.

Two profile constraints the KB already records: **helium is ruled out** (no room for a tank on the panga), so your kite window really is wind-dependent; and `profiles/cameron/boat.md` has **`range_nm` and `sea_state_max_ft` still null** — so I can't verify from the KB whether a given 100–300 lb zone (Tanner/Cortez, the below-Clemente complex) is inside your envelope on a given day. Per `planning/day-plan-protocol.md` step 1b, that has to be answered before a kite day gets planned, not after.

If the kite is out on a small boat, `rigging/flying-fish-harness.md` logs a **kite-free and balloon-free** alternative (Steve Carson, `QHY5kmU7OTU`, medium confidence): toothpicks pinning the wings open, a **pool noodle cut in half lengthwise fitted over the fish's back like a life jacket** so it floats and rides the surface on its own — fished on the slide or dropped off the bow. Named as especially suited to private boats. Stated trade-off: it has to be built and thawed ahead of time rather than deployed on the fly.

---

## What the KB does **not** answer

- **There is no direct head-to-head "kite vs flyline" decision rule anywhere in the corpus.** I derived the boundary above from the kite's grade/wind row and the flyline's "chummed up / picky" row, plus the observed sessions where both were fished together. Nothing states a hookup-rate or fish-per-hour comparison between the two.
- **No upper wind limit for the kite.** The table gives 8–15 kt; nothing says what to do at 18, 20, or 25 kt, or whether the kite becomes unfishable.
- **No kite specs at all** — no size, square footage, model, or wind-rating ladder for which kite to fly in which wind band.
- **No stated abandon-the-kite trigger** — nothing tells you how long to soak a dead flyer over marks before giving up on it.
- **Balloon vs kite lift is unresolved.** Three separate sources use balloons with, instead of, or alongside a kite, and the KB explicitly keeps that ambiguity open rather than settling it.
- **The 2–4 oz sliding sinker on a kite-flown bait** (`jH0q4UPjwC0`, Alijos Rocks, medium confidence) is logged as untested by the angler who described it, with no leader position, hook, or bait species given — it sits beside, not inside, the bare-flyer doctrine.
- **No bait-quantity guidance for the flyline side** of a mixed kite/flyline day.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `techniques/kite-fishing.md`, `techniques/flyline.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `rigging/flying-fish-harness.md`, `tackle/gear-classes.md`, `bait/fishing-live-bait.md`, `techniques/fighting-big-bluefin.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`, `profiles/cameron/README.md`  
*videos:* `YsiHziY_PWw`, `GqcVaTIlyg0`, `JiJYamo0QHk`, `2y0VznL2qk8`, `rsCAh-QyK60`, `Ix0gG0-l3v0`, `vCskOx6N-XM`, `fgTmUq78ofQ`, `RM7cBgCDWFA`, `lf3S28nh-kk`, `shZCjX2-fkI`, `usHl-4SfqDA`, `mDmbGdQAy-4`, `zBd1mayUt_I`, `QSvzVHW9UMk`, `2TmLaSCmfC8`, `w5_x6kkN-xE`, `pk2blktDQ9Y`, `jH0q4UPjwC0`, `QHY5kmU7OTU`, `ouBrIdO7d4k`, `48ZFXnCTTQE`, `icpm7gADxvU`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `ftEvyfwjZFU`, `jQW2HLkMsmY`  
*gaps admitted:* No direct head-to-head kite-vs-flyline decision rule exists in the KB; the boundary had to be inferred from the kite's grade/wind row and the flyline's 'chummed up / picky on bait' row. | No hookup-rate, fish-per-hour, or any quantitative comparison between kite and flyline is recorded. | No upper wind limit for kite fishing — the table gives 8-15 kt but nothing says what happens above 15 kt. | No kite specs of any kind: no size, square footage, model, or which-kite-for-which-wind ladder. | No stated trigger for abandoning the kite — nothing on how long to soak a dead flyer over marks before switching. | Balloon vs. kite lift is explicitly unresolved in the KB: three sources use balloons with, instead of, or alongside a kite and the notes keep the ambiguity open. | The 2-4 oz sliding sinker on a kite-flown bait is single-source, medium confidence, and self-described as untested, with no leader position, hook, or bait species given. | No bait-quantity guidance for the flyline side of a mixed kite/flyline day (only the 10-12 flyers per four-angler day figure for the kite side). | Cameron's boat profile has range_nm and sea_state_max_ft null, so the KB cannot confirm whether the 100-300 lb zones (Tanner/Cortez, below-Clemente complex) are inside his operating envelope. | The ~8 kt wind mark appears in two frameworks pointing in opposite directions (trigger to troll under the kite vs. trigger to speed-troll because the kite won't fly); the KB flags this as unreconciled.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Kite vs. flyline for bluefin — the split, and the full kite setup

## The short version

The KB doesn't treat these as competing answers to the same question. **The kite is a grade tool; the flyline is a bite tool.** Kite beats flyline when you have (1) the **100–300 lb** class of fish, (2) **wind to fly it**, and (3) **fish already located**. Flyline wins when the fish are **chummed up and picky**, when the grade is the 40–60 lb class, or when there's no wind at all. On the days both apply, the corpus fishes them **at the same time** — one Tanner-area sundown session converted on kite gear and flyline gear in the same window (`zBd1mayUt_I`, [techniques/kite-fishing.md](techniques/kite-fishing.md), [locations/tanner-bank.md](locations/tanner-bank.md); the location note flags that the "over 100 lb" figure comes from the episode's promo intro, while the on-deck recap says only "a couple kite bites, couple fly line on that better grade").

---

## When the kite beats the flyline

**1. The grade is 100–300 lb.** A flying fish under a kite is stated flatly as *the* most effective method for that class of SoCal bluefin (`YsiHziY_PWw`, [species/bluefin-tuna-trolling.md](species/bluefin-tuna-trolling.md)). The router's row reads "**Big fish 100–300 lb**, wind ~8–15 kt → kite fishing, **150–200 lb class** + flying-fish harness" ([species/bluefin-tuna.md](species/bluefin-tuna.md)). The Searcher reserves its dedicated kite outfits for **confirmed 100 lb+ fish** and hadn't needed to deploy them at all through the point in the 2021 season the seminar was filmed (`fgTmUq78ofQ`, [techniques/evidence/kite-fishing.md](techniques/evidence/kite-fishing.md)).

**2. Selective fish that refuse everything else.** This is the sharpest case in the corpus and it's the opposite of the flyline answer. Bluefin gorging microbait are "not looking for anything else except what they are eating," and the bait is often too small to hook (`qLKLlZdiflA`). On one trip, foamers breaking all around the boat produced **nothing** on a trolled spreader bar or cast plugs — **only a dead flying fish under the kite converted** (`mDmbGdQAy-4`, [species/bluefin-tuna.md](species/bluefin-tuna.md)). Flyline answers selectivity by going *smaller and lighter*; the kite answers it by presenting a big fleeing flyer the fish reacts to instead of inspects.

**3. May specifically.** The seasonal note pairs the night bite with **daytime flying-fish imitations for grade** — the bigger fish come to surface presentations that mimic flying fish during the day (`S2L3KLSQ6Is`, [seasonal/may.md](seasonal/may.md)).

**4. Bait choice inside the kite program.** Frozen **dead natural flying fish** produced the majority of one charter boat's bites, ahead of a "California Flyer" artificial fished under the same kite (`ouBrIdO7d4k`, [species/bluefin-tuna.md](species/bluefin-tuna.md)).

## When the flyline wins instead

- **Chummed up / picky on bait** — the router sends this straight to flyline: a sardine on a circle hook, corner-of-mouth bite ([species/bluefin-tuna.md](species/bluefin-tuna.md)).
- **Volume on a normal day.** About **90% of one boat's daytime bites** on an overnight trip (27 bluefin for 26 passengers) came off flyline, worked on a dedicated **25–30 lb fluorocarbon** stick with a **size 2 circle hook** (sizes 1 to 1/0 also used); the rest split between a sinker rig and a Colt Sniper (`149px8WQ2Ng`).
- **Fish that will eat nothing else.** A June 2023 El Dorado day bit **strictly on flyline** — the boat tried a sinker rig and the fish refused it; **25–40 lb test** to a straight **No. 2** hook on sardine (`oB4BpIUTTl4`, `r4J5nP5Bkl4`, [techniques/flyline.md](techniques/flyline.md)).
- **Mid-grade fish that quit on heavy line.** Bluefin grading **40–60 lb** stop biting because the bait isn't swimming right on heavier line — drop to **20–25 lb test** and the fish want it (`icpm7gADxvU`); one skipper's cap for a tough bite is **20–25 lb, no more than 30** (`48ZFXnCTTQE`).

**No wind is not a flyline cue — it's a trolling cue.** When the kite won't fly, the KB's answer is to **speed-troll** (a Mad Mac or X-Rap Magnum Extreme, 13–15 kt) to cover water and pull bites, not to switch to bait ([techniques/kite-fishing.md](techniques/kite-fishing.md), [species/bluefin-tuna-trolling.md](species/bluefin-tuna-trolling.md), `z1CmWHqe9uk`). Same for fish too scattered to sit and kite over — that's a coverage need, not a sea state (cameron).

## Honest warning on the wind numbers

The "8–15 kt" band you'll see in the router is **internally contested in this KB and I'd treat it as soft**: the kite technique note states **no wind numbers at all** in its wind-window section, and the trolling note carries a flag that the ~8 kt figure is unsupported by `z1CmWHqe9uk` and contradicted by `2y0VznL2qk8`, which flies a kite under 8 kt ([species/bluefin-tuna.md](species/bluefin-tuna.md), [species/bluefin-tuna-trolling.md](species/bluefin-tuna-trolling.md)). The reliable test is behavioral, not numeric: **marginal, gusty or dying wind makes the flyer inconsistent on the surface — that's the cue to switch to speed trolling** ([techniques/kite-fishing.md](techniques/kite-fishing.md)).

**The ~8 kt mark that *is* well-cited is a split inside the kite program, not an on/off switch** (`2y0VznL2qk8`):

| Wind | Presentation | Why |
| --- | --- | --- |
| **~8 kt or more** | Troll a rubber flyer ("Yummy Flyer") under the kite at **~8.5 kt** | Covers water while searching and converts bite→hookup at a better ratio than dead-boat; mark raised schools on the GPS and keep working that spot |
| **Under ~8 kt, fish already located** (surface sign or heavy sounder marks) | Dead-boat: deploy **typically two** dead flyers under the kite (or a balloon) and drift them | Never deploy a dead flyer speculatively — it's fished over confirmed sign, not blind water |

Dead-boat deployment: drive forward a little to open distance from the bait, then lower the flyer slowly onto the surface and keep it **dapping** — bouncing with the swell, never submerged, never airborne. On the take (a surface explosion), put the boat in gear and drive **forward gently at 4–5 kt, not a hard throttle**, to keep the rod bent and drive the hook without shock-loading it (`2y0VznL2qk8`).

Light-wind fix: a **helium balloon assist** — the balloon twists into a dedicated clip with no knot, the clip rubber-bands to the kite, and a taped fishing-line tether backs that up so a failure leaves balloon and kite cradled together instead of lost (`vCskOx6N-XM`). **Your panga rules helium out** — cost, and no room for a tank (cameron, [techniques/kite-fishing.md](techniques/kite-fishing.md)) — so your light-wind window stays closed unless you're on a bigger boat.

---

## The kite setup

### Outfit
- **Rod:** heavy fighting rod, pure leverage — not a casting tool. Documented rail rods for this program: **7 ft 6 in, rated 80–200 lb unlimited class** (`RM7cBgCDWFA`). Class term: **150–200 lb class** ([tackle/gear-classes.md](tackle/gear-classes.md) puts this in the trolling/spreader-bar row — 7–7.5 ft, XXXX-H, 150–200 lb, 2-speed, ~1000 yd capacity — and notes kite outfits run heavier than the 60–130 lb rail-rod row).
- **Reel:** two-speed conventional. Dedicated boat programs field **50-class**: Accurate ATD 50s, Accurate twin-drags, Shimano Tiagra 50 Wide. A rental-grade **Talica 25 with 80 lb** is also offered as a kite/fighting outfit. **Personal-outfit floor: an 80-lb-class two-speed on a big rail rod** (`fgTmUq78ofQ`, `lf3S28nh-kk`, `RM7cBgCDWFA`, `shZCjX2-fkI`). Reel picks are reported to split on **budget, not capability** — all named reels are called adequate.
- **Main line + top shot:** **130–200 lb braid/spectra**, either tied straight to heavy mono or joined to a **~15 ft top shot of 130–200 lb mono** (one documented reel: 200 lb braid + 15 ft of 135 lb mono). The Searcher's kite setups run **200 lb spectra tied straight to 400 lb mono**. Personal-outfit floor is **100 lb** top shot (`RM7cBgCDWFA`, `fgTmUq78ofQ`, `lf3S28nh-kk`).
- **Connection:** a **500 lb ball-bearing swivel** joins the top shot to the harness leader (`RM7cBgCDWFA`).
- **Drag reference:** Dave Hansen's kite program runs **200 lb braid → 400 lb fluorocarbon with 40 lb of drag** (`JiJYamo0QHk`, [rigging/flying-fish-harness.md](rigging/flying-fish-harness.md)).

### Bite leader and hooks
- **Length: 3 ft, 3.5 ft at the absolute max.** Any longer and the swivel reaches the rod tip before the fish is in gaff range (`YsiHziY_PWw`). This is the single most commonly listed failure mode besides wing set.
- **Material: 200–400 lb mono, typically 400** (`GqcVaTIlyg0`); heavy fluoro **200 lb-plus, 400 lb common**. Named build: **400 lb Izorline XXX**.
- **Hooks: a large J up front with a big treble stinger trailing.** Documented specs: **9/0–12/0 J (Owner) with a 5X-strong Owner treble**; a **12/0 stainless Mustad** J plus treble; tail treble **5/0 5X-strong Mustad** (`GqcVaTIlyg0`, `YsiHziY_PWw`, `fgTmUq78ofQ`, `RM7cBgCDWFA`).
- **Hook-count conflict, kept side by side:** most SoCal boats run J-plus-trailing-treble, but Hansen's boat runs **single hook, no trebles** — "I know a lot of people have to use a treble… that's what you feel you need" (`JiJYamo0QHk`). The KB calls this a **program choice, not a conditions call** ([rigging/flying-fish-harness.md](rigging/flying-fish-harness.md)).

### Rigging the flying fish ([rigging/flying-fish-harness.md](rigging/flying-fish-harness.md), `GqcVaTIlyg0`)
- Skewer in behind the shoulder just above the spine; a second skewer through a hole between the ribs and the wing at the position you want the wing to sit.
- **Zip-tie the wings open through extra holes on both sides and cinch everything tight** — any slippage along the skewers during deployment kills the action.
- **Wing angle ~45°.** Set further out, a swell knocks the bait off its presentation (`YsiHziY_PWw`).
- Body skewer down the middle, entered through the mouth, pushed about **three-quarters** of the way in; **lift the tail as you finish the push** so the bait sits slightly tail-down at the surface.
- **Pin the mouth closed** with a final skewer — keeps it presenting longer and stops water scooping through the lower lip.
- **Rig 10 to 12 flyers for a four-angler day** and store them in the cooler ready to deploy.
- Field shortcuts for the wing lock: a **stapled popsicle stick** (`usHl-4SfqDA`), a **rubber band** in place of the zip tie (`Ix0gG0-l3v0`), or **30–50 lb braid** threaded through the wing hole and around the skewer — two overhand knots plus a **third locking knot** or the wing tie slips; rig the flyer **partially thawed**, not fully (`2TmLaSCmfC8`).

### Bait alternatives if you can't get flyers
- **Live mackerel, back/dorsal-hooked** right in front of the dorsal (hard spot, holds the hook): the bait sits flat and daps each time it touches down, with the leader out of the water where a leader-shy tuna can't see it. Same 100–300 lb grade; yellowtail and calicos have also eaten it off the kite (`w5_x6kkN-xE`, [bait/fishing-live-bait.md](bait/fishing-live-bait.md)).
- **Whole squid on a double-hook rig** for giant grade, drifted with current and wind and presented almost unresisted on the take (`pk2blktDQ9Y`).
- **"California Flyer"** — a hard artificial fished dead-boat under the kite that slides up the leader on a hookup so it isn't chewed up (`vCskOx6N-XM`).
- **Pool-noodle "life jacket"** — half a noodle over the flyer's back for buoyancy, wings pinned with toothpicks, fished on the slide or off the bow with **no kite or balloon at all**; a Penn International 20-class is a suitable pairing, sized for a 300 lb-class fish. Called especially suited to private boats; the trade-off is it has to be rigged ahead of time (`QHY5kmU7OTU`).
- Untested outlier, flagged as such: one report adds a **2–4 oz sliding sinker** ahead of a kite-flown bait on secondhand advice that it keeps the bait in the water — offered untested by the speaker, and it stands unreconciled against the bare-flyer dapping doctrine (`jH0q4UPjwC0`).

### The kite line itself
- The kite flies on **its own dedicated line**, separate from the fishing line. A ring tied on the fishing line ahead of the terminal tackle carries a **rubber band** running to the kite line's release clip — **no knot joins the fishing line to the clip**, so the rubber band is the weak link that pops on the bite (`Ix0gG0-l3v0`).
- Documented kite-line build: straight braid with no separate leader, **roughly a couple hundred yards** spooled out once set, **star-drag payout control** instead of thumbing the spool, a heavy-duty snap swivel (don't over-crank it), and a knot marking ~75 ft out during payout (function unresolved in the source). **Gyro-stabilized binoculars called mandatory** — for spotting fish *and* for watching the flyer stay upright (`Ix0gG0-l3v0`).
- **Height:** fly it as high as the crew can still **see the flying fish skipping** — visibility, not a fixed height, sets the ceiling (`rsCAh-QyK60`). Kite run reported at **120–150 yd out**, shifting with wind, drift and the boat's heading.

### The presentation — this is where it's won or lost
Adjust the clip and kite so **the flyer just touches the surface: skipping and splashing, never dragging under, never flying clear of the water.** The most common mistake is flying the bait through the air like the kite itself instead of skipping it wave-to-wave — the fish are in the water, not the sky (`JiJYamo0QHk`).

### The bite and the fight
- The line **pops out of the release clip** and you come tight directly — no clip in the fighting system.
- **Lay the short leader out flat on the surface** to bring the fish into gaff range at the swivel.
- A kite-hooked 100 lb+ bluefin was fought **40–45 minutes** before landing (`zBd1mayUt_I`) — the KB flags the source's auto-captions as garbled on that figure.
- Fight it with the boat, not your arms: keep the rod in the holder and **tap in and out of gear** — out the moment line peels, back in the instant it stops. Hand-fighting in a harness at **30–40 lb of drag** is an endurance choice, not a functional advantage. **Never fish bluefin under 130 lb spectra/braid** whichever style you use (`8jC61LzQoxU`, [techniques/fighting-big-bluefin.md](techniques/fighting-big-bluefin.md)).
- **20–30 ft private-boat variant:** leave the rod in the holder the whole time rather than swapping sides across the transom; turn the wheel a little and walk the boat in **big gentle circles** (not tight donuts); keep the fish **pinned on the same side**, amidships back to the stern; **drive forward only, never reverse**, holding roughly **45°** to the fish (`Q196GVwVqro`). That's the one directly applicable to your panga.

### Common failures
Wings set too far out (a swell knocks the bait off) · leader too long (the fish hits the swivel before it's in gaff range) · letting the flyer sink or drag instead of skipping.

---

## Against your own inventory ([profiles/cameron/rods.md](profiles/cameron/rods.md), [profiles/cameron/boat.md](profiles/cameron/boat.md))

**You have the rod, and it's already designated.** Setup 7 — **Okuma PCH-C-741XXXXH, 7'4", XXXX-H, 150–200 lb** with a **Penn Fathom II 80LD2 two-speed (4.2:1 / 1.6:1, 50 lb max drag) and ~1000 yd of 100 lb braid** — is recorded as your future kite rod (keep the 100 lb braid for capacity and less wind-blow, 200 lb leader, small boat can chase). It's also the only setup of the eight that hasn't caught a bluefin.

**Gaps I have to name rather than paper over:**
- **No kite, no flyers, no harness materials** (skewers, zip ties), **no 500 lb ball-bearing swivel, no 12/0 J or 5/0 treble** appear anywhere in [profiles/cameron/tackle.md](profiles/cameron/tackle.md) or [profiles/cameron/trolling-lures.md](profiles/cameron/trolling-lures.md). This is a shopping list, not a rig-tonight plan.
- **Your 100 lb braid sits below the 130–200 lb kite spools** in every documented program, and your planned 200 lb leader is at the **bottom** of the harness note's 200–400 lb (typically 400) range. Your own profile reasoning for the 100 lb (capacity, less wind-blow) is recorded doctrine, so I'm flagging the mismatch rather than overriding you.
- **Helium is out on the panga**, so the sub-8 kt dead-boat window has no light-wind assist.
- **Sea-state tension:** the kite band (8–15 kt) runs straight into the working-captain go/no-go rule that **wind above ~12 kt raises whitecaps and is the personal cutoff for not running**, with **12–15 kt / 4–8 ft / 9-second interval** named as flatly unfishable for boats of any size (`NC3-3pJDEgo`, [conditions/sea-state.md](conditions/sea-state.md), single-source flagged). Practically that leaves you a **~8–12 kt** working window. Your boat note has **`range_nm` and `sea_state_max_ft` null**, and the protocol says to ask rather than assume — so tell me your real sea-state ceiling and I'll tighten that.

**Your flyline side is already covered:** Setup 2 (Teramar TMC90MHB2, 9'0", MH, 30–65 lb + Avet MXJ, 50 lb braid) is the named exemplar of the flyline/soft-rod class in [tackle/gear-classes.md](tackle/gear-classes.md); Setup 1 (Trinidad 40, 8'0" XH 40–80 lb, 80 lb braid) is your heavy flyline stick. If the bite goes finicky, the corpus fix is a **25 lb mono top shot to a 2–3 ft, 50 lb fluorocarbon bite guard** joined with a Seaguar knot — the 25 lb is what pulls through the water so the bait swims like it's on 25 lb, while the short heavy section rides in the mouth and along the gill plates (`48ZFXnCTTQE`). Hansen's simpler big-bait alternative: a thick-wire Mustad circle tied straight to **3–4 ft of 80 lb fluorocarbon** with a San Diego jam — **no weight, no swivel, no beads** — mackerel nose-hooked, thrown into the foamer (`RbqOKkINSCM`).

**One line-class conflict to know about:** the bluefin router puts flyline at the **40–60 lb class with 1–2/0 circles**, while the flyline note answers the same picky-bite scenario at **20–25 lb, no more than 30**, and gear-classes calls that the finesse fly-line class (12–30 lb). The KB flags this contradiction rather than resolving it. What it turns on is **bait size and how finicky the fish are**, not the fish's weight — carry both and step down when you're not getting bit.

## Bottom line for a day plan

Fly the kite when you've got **80+ grade confirmed and steady wind you can keep the flyer skipping in** — and especially when they're up and feeding on something you can't match. Keep a **flyline stick rigged and in the water the whole time** anyway; the corpus fishes both off the same drift, and on most days flyline is where the bites come from. Give me a date, launch point and the day's wind/SST and I'll run the full protocol against zones.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/kite-fishing.md`, `techniques/evidence/kite-fishing.md`, `techniques/flyline.md`, `techniques/fighting-big-bluefin.md`, `species/bluefin-tuna.md`, `species/bluefin-tuna-trolling.md`, `rigging/flying-fish-harness.md`, `tackle/gear-classes.md`, `bait/fishing-live-bait.md`, `conditions/sea-state.md`, `seasonal/may.md`, `locations/tanner-bank.md`, `locations/coronados-230-302-226.md`, `locations/474-711.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`  
*videos:* `YsiHziY_PWw`, `2y0VznL2qk8`, `Ix0gG0-l3v0`, `rsCAh-QyK60`, `JiJYamo0QHk`, `vCskOx6N-XM`, `RM7cBgCDWFA`, `fgTmUq78ofQ`, `lf3S28nh-kk`, `shZCjX2-fkI`, `zBd1mayUt_I`, `mDmbGdQAy-4`, `ouBrIdO7d4k`, `qLKLlZdiflA`, `GqcVaTIlyg0`, `2TmLaSCmfC8`, `usHl-4SfqDA`, `w5_x6kkN-xE`, `pk2blktDQ9Y`, `QHY5kmU7OTU`, `jH0q4UPjwC0`, `z1CmWHqe9uk`, `149px8WQ2Ng`, `48ZFXnCTTQE`, `icpm7gADxvU`, `RbqOKkINSCM`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `8jC61LzQoxU`, `Q196GVwVqro`, `NC3-3pJDEgo`, `S2L3KLSQ6Is`  
*gaps admitted:* The '8-15 kt' kite wind band is internally contradicted in the KB: the kite technique note carries no wind numbers at all in its wind-window section, and the trolling note flags ~8 kt as unsupported by z1CmWHqe9uk and contradicted by 2y0VznL2qk8, which flies a kite under 8 kt. | No source in the corpus compares kite and flyline head-to-head on the same fish; the 'kite beats flyline' read is assembled from the 100-300 lb kite grade statement plus the separate 40-60 lb picky-fish flyline statement. | The KB gives no kite specification at all - no brand, size, square footage, or wind rating for the kite itself, and no guidance on which kite to buy for a given wind range. | No note covers whether the kite is worth flying for sub-100 lb / schoolie-grade bluefin; every kite citation is scoped to the 100-300 lb class. | No stated distance in feet for how far to set the kite bait from the boat; the only figures are the kite run (120-150 yd out) and a ~75 ft payout knot mark whose function the source does not resolve. | The flyline line class for picky bluefin is contradicted between notes (router: 40-60 lb class, 1-2/0 circles; flyline note: 20-25 lb capped at 30; gear-classes: finesse fly-line class 12-30 lb) and the KB flags it without resolving it. | The kite hook count is unresolved doctrine - most SoCal boats run J-plus-trailing-treble, Hansen's boat runs single hook with no treble - and the KB calls it a program choice with no conditions test to pick between them. | Cameron's profile records no kite, no flying fish, no harness materials (skewers, zip ties), no 500 lb ball-bearing swivel, and no 12/0 J or 5/0 treble hooks - the kite program is unowned gear. | Cameron's boat profile has range_nm and sea_state_max_ft null, so the day-plan protocol's step-1b envelope cannot be derived and must be asked for; the kite's 8-15 kt band overlaps the 12 kt no-go rule with no note reconciling them for a 22 ft panga. | Nothing in the KB covers kite-line handling or spread geometry in a small panga cockpit, or running a kite alongside a flyline spread on a boat that size. | The question supplied no date, launch point, wind, or SST, so no zone, timing or conditions call is made here - no BightSST pull was performed. | No corpus source resolves whether the Coronado Islands Yummy Flyer bites (2020-06) came trolled or under the kite, or on which bank - the location note carries this as a flagged gap. | Whether a balloon adds lift or is only a strike marker is explicitly unsettled in the KB - one report flies a rubber flyer under a balloon without saying whether a kite was also up, another flies a balloon together with the kite in fishable wind.

</details>

### 13. [technique] How do I fish a drop-shot for calico bass along a kelp line?

**Winner:** NOW · mapping {'A': 'B2', 'B': 'B3', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three refuse to invent a calico drop-shot program and all three give the same honest negative, so the separation is in scoping and provenance. A is the weakest of the three only because it never runs the waters gate — it never tells the angler that the drop-shot note excludes `island`, so a Catalina or San Clemente trip gets an unqualified rig; B and C both catch that step-1b exclusion, and both surface the Fred Hall calico-panel weedless dropper rig (2 ft leader, 1 oz torpedo weight) that A misses entirely. C edges B by grounding the envelope call in the actual regions.md vocabulary, tracing the panel items to the evidence file, carrying source-hygiene caveats (miscited Spin Shot rationale, verbatim re-cuts, ⚠ unverifiable depth figures, a misattributed current cite), and stamping both regulations with jurisdiction, as-of, and verify — including flagging its own 2019 bag-limit figure as stale.

- *B2 reasons:* found: leads with the true negative (no drop-shot row, not even a flagged stub) and pulls the right adjacent notes. specific: dense real parameters — 12–14 in Palomar tag, 6–10 in hook-to-weight, 1/4–2 oz weights, 8–12/15–20 lb line pairing, 25/40/60–65 lb kelp leaders, 50→25 ft edge band, 70–80 ft sink, 10–15 ft rise, 6–10 oz dropper sinkers. sourced: note paths plus video ids (k4mD2d6C81k, EGKesj7V64M, KTsXdQXAnkU, 9xNhdu2aBqE, HMdrP4-i9MM) attached to the claims they carry. scoped: regulation is correct (California/CDFW, 14 in, as of 2026-08, verify-current), but it never runs the waters gate — no mention that the drop-shot note excludes `island`, so an angler heading to Catalina/Clemente is not told the technique is out of envelope. honest: no bluffing, absolute dates throughout, nine concrete gaps admitted including the fouling and boat-positioning holes. actionable: rig build, cadence, hookset, move discipline, and five documented kelp alternatives including the dropper-loop analogue.
- *B3 reasons:* found: same true negative (17-row table, no stub) and finds the one genuine bridge — the Fred Hall calico-panel weedless-slug dropper rig (RUuPNpK0x-s) — while correctly scoping it to halibut/bay sand channels. specific: 2 ft leader, 1 oz torpedo/keel weight, 6–10 in spacing, 1/4–1 and 1–2 oz, 8–12/15–20 lb, 3/8–3/4 oz keel heads, 1.5 oz tube, 8–10 in trophy baits, 65–80 lb braid, 25→50 ft edge, plus the sloped-bottom 2–3 in addendum. sourced: paths plus ids (BPxE3xn3gAc, _KldpqPPT1c, 9a-Zy_D6c3w, ZoIzpyyS9xw, fHMwcm1xRQk) and an explicit re-cut note (_rcxIWhNMSE / nZfEB7466ys). scoped: applies day-plan step 1b correctly — island kelp is out of envelope because the drop-shot note's waters lack `island`, coastal kelp clears the gate; states no regulation, so nothing bare. honest: names the conflicts as note-vs-note, flags the reverse drop shot as detail-free on camera, ten gaps listed. actionable: situation→answer table plus a recommended substitute with a leader spec that survives kelp.
- *NOW reasons:* found: true negative stated first, then the only real link — the Fred Hall panel items traced through techniques/evidence/drop-shot.md — with the weedless 2 ft / 1 oz torpedo rig correctly scoped to sand channels. specific: full rig build (2000 reel, 10–12 lb leader, 12–14 in Palomar tag, point-up, 1/4–1 vs 1–2 oz matched to 8–12/15–20 lb, VMC Spin Shot #2, #2 mosquito), plus 1 oz/25 lb pitch-and-sink, 7 in slug on 7/0 3/8 oz vs 3/4 oz, 6.2:1 reel, 8–8.5 vs 7 ft rods, 20–120 ft structure, 40–42 ft with kelp 20 ft off bottom. sourced: paths, ids, the evidence file, and unusually careful provenance hygiene — flags the Spin Shot miscite, the verbatim re-cuts, the unverifiable 70–80 ft and 25–50 ft figures, and a misattributed current-tier cite. scoped: quotes locations/regions.md to separate nearshore-coast kelp (inside the gate) from island kelp (outside), and both regs carry CDFW + as-of (14 in as of 2026-08; 5 fish as of 2019-03-13, self-labeled as stale) + verify-current. honest: calls the absence silence rather than a documented no, admits ledger-level contradictions, ten gaps including no calico zone guide. actionable: names the single best documented substitute (1 oz leadhead at the kelp base, 25 lb fluoro, bite on the sink) and gives a complete kelp-line program around it.

<details><summary>Full prompt</summary>

How do I fish a drop-shot for calico bass along a kelp line?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Straight answer first: this KB has no drop-shot doctrine for calico bass

I checked the router and the technique note directly. **`species/calico-bass.md` does not contain a drop-shot row anywhere in its Situations → techniques table** — not a real row, not even a `⚠ flagged stub` row (the KB uses those elsewhere, e.g. the Wax Wing stub in that same table and the "light troll class" stub in `tackle/gear-classes.md`). And **`techniques/drop-shot.md` never mentions calico, kelp, or islands** — it is tagged `[drop-shot, halibut, spotted-bay-bass, bays, finesse, vertical]` and its "Reach for this when" list names only [California halibut](species/california-halibut.md) buried in sand and [spotted bay bass](species/spotted-bay-bass.md) in the back bays.

So I can give you the drop-shot rig exactly as the KB documents it — but I have to be explicit that **every number in it was recorded off bay/flatfish sources, and the KB's own calico doctrine contradicts several of them for a kelp line.** I'm not going to paper over that with general knowledge.

---

## 1. The drop shot as this KB actually documents it

All of this is `techniques/drop-shot.md` (confidence: **medium**; sources `k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`), backed by `lures/bay-bass-plastics.md`.

**The rig concept.** Hook tied up the line, weight hanging below on a tag end, so the bait is suspended a fixed height just above bottom while the lead stays pinned to the deck — that lets you **shake it in place** without dragging it off the spot.

**Build (Nathan Winch, `k4mD2d6C81k`/`1enjjFVcDG0`):**
- Light spinning rod, **2000-size spinning reel**, **braid** mainline — braid because you *see* the line jump for the visual bite and can feel a bite even on slack line.
- **Leader 10–12 lb, light drag.**
- **Strong long-shanked J-hook** (O'Shaughnessy forged long shank) — the long shank keeps the plastic from sliding around.
- **Palomar knot:** leave **12–14 in** of leader, double the line, through the eye, overhand, drop the loop over the shank, cinch. Then **pass the leader tag back down through the top of the hook eye** so the knot lies flat and the **hook points upward.** The note flags this as *the* single most common rigging error — "if it isn't facing up, the rig won't work well."
- **Weight below the hook on the tag: 1/4 oz up to 1 oz**, light when it's glassy. Rod Marquez runs heavier — **1 oz to 2 oz**, with line matched to it: **8–12 lb test with 1 oz, stepping to 15–20 lb test with 2 oz.**
- **Hook-to-weight distance: 6–10 inches** (Marquez). His stated reasoning is halibut-specific — a predator won't burn energy chasing a bait 15 ft up, but at 6–10 in it only takes a little effort to commit.
- **Bait:** 4-in scented finesse fluke (ZMan), or swap to a grub or a small swimbait. Marquez feeds a **Gamakatsu size 1 straight worm hook** through the plastic to expose the point closer to the tail *because halibut chase and bite from behind* — that rationale is flatfish-specific and the KB gives no calico equivalent.

**Working it:** weight on bottom, bait suspended just above, **shake it in place**. Grub → rod tip down at **45°, constant retrieve**. Fluke → **twitch, reel the slack, twitch again.** `lures/bay-bass-plastics.md` adds Roman Castro's **drag-and-pause** cadence (`EGKesj7V64M`, 2019-06-18, medium): lift the rod tip with no reeling to drag the bait a short distance, then lower the rod while reeling the slack so the bait sits dead through the reset. He also recommends a drop of **super glue between head and plastic** so the bait can't slide down the shank on an off-center grab.

**Hookset (Roman Castro, `EGKesj7V64M`, medium):** **never set into slack** — on light line it's the slack, not the force, that pops the leader. Wind down and lower the rod to come tight first, *then* set. A missed swing costs nothing, so swing on anything that doesn't feel like bottom.

**Move discipline:** ~**20 minutes** with no bite and you move; the fish may be only 20 yards off.

**Gear class:** `tackle/gear-classes.md` puts drop shot in the **light spinning class — light spinning, 10–20 lb**, alongside the Ned rig and bay finesse.

---

## 2. Where that rig collides with the KB's calico doctrine — read this before you fish it

These aren't my objections; they're conflicts between two notes in this KB.

- **Line class is the big one.** Drop shot as documented is a **10–12 lb leader on light drag** (or 15–20 lb behind a 2 oz weight). For kelp calico, `techniques/swimbaits.md` records Landesfeind at **50–65 lb braid, 300-size reel, 60 lb fluorocarbon leader** — explicitly because "the leader gets braided up and chafed just from throwing it in the kelp" — and Todd Klein at **65 lb braid to 40 lb mono** cinched down tight (`9xNhdu2aBqE`, San Clemente Island, 2015-10-28, medium). The lightest leader in this KB for anything at a kelp base is Dave Hansen's **25 lb fluoro** pitch rig (`KTsXdQXAnkU`, 2019-06-05). 10–12 lb is a full order below the KB's floor for this structure.
- **The presentation logic points the other way.** `species/calico-bass.md` and `locations/bass-structure.md` are built on the parallel-current rule: calico **face into the current and ambush from the leading/up-current edge**, and you want a lure **swept past** that edge the way current-borne food moves (Benny Florentino, `Rwy4MqeXCIU`; Landesfeind Academy Ep. 5/Ep. 14, `kwMIgkCtFUE`/`0KQ--N5TjqE`). A drop shot is a stationary bottom-anchored shake — the opposite of a swept presentation. The KB never resolves that; it simply never puts the two together.
- **The search method conflicts.** Calico doctrine is **cover water**: 10–25 casts to the prime edge of a bed, then move 100 ft or 100 yards; "hit three or four sides of it and you know in two or three casts" (Ep. 14). The drop shot's 20-minute soak-then-move is a much slower grid.
- **Hookset doctrine conflicts.** Drop shot says swing on anything after taking up slack. Swimbait calico doctrine says **set on the pause, never on the grab** — "swing the instant you get bit and nine times out of ten you pull the bait out of the fish's mouth."
- **Fouling.** `techniques/swimbaits.md` records a fish lost boatside at Dono, Baja because **kelp slid down the hook shank and "pops it right out of the fish's mouth"** (`L3tkGVu516A`, 2014-11-13, medium). An upward-pointing exposed J-hook on a 6–10 in tag, fished at the base of a kelp line, is the rigging style that note warns about — and the KB has no weedless drop-shot variant on file.

---

## 3. What the KB *does* document for putting a plastic on the bottom at a kelp line

If what you actually want is "a plastic held low, worked slow, right on the kelp edge," these are the presentations the KB has real sources for. I'd take them over an unsourced drop-shot improvisation.

1. **Pitch-and-sink at the kelp base** — the closest documented analogue. Pitch a **1 oz black/gold leadhead** right at the base of the kelp line and **let it sink straight to the bottom; the bite typically comes on that sink.** Run **25 lb fluoro** (Dave Hansen, Your Saltwater Guide, `KTsXdQXAnkU`, 2019-06-05; registered voice, single mention — medium). `techniques/swimbaits.md`.
2. **Flip / punch a heavy head into gaps in the canopy** — when fish are holding *up under* the floating canopy rather than on the edge. Short, accurate pitches into the kelp itself, not long casts; the fish work the dropped bait before eating (Aaron Martens with Benny Florentino, San Clemente Island, Dec 2013, `P6Slg6RQiXw`). The router itself flags this as **⚠ a single-session observed data point, not established doctrine**, and no leader/hook/weight spec was given on camera.
3. **Lead-head swimbait sunk deep** — sink the same bait class **70–80 ft down for calicos** over structure; fish holding and feeding will rise to meet it. `techniques/swimbaits.md`.
4. **Dropper loop over kelp that doesn't reach the surface** — the KB's one recorded *hook-above-weight* rig that actually produced calico: hard bottom in **~40–42 ft** with kelp growing **~20 ft off the bottom**, off North County San Diego near Camp Pendleton, drop straight down and reel, no casting (`HMdrP4-i9MM`, 2022-10-11, unregistered channel — medium). `techniques/dropper-loop.md` adds the general doctrine: **drop it straight down, never cast it**; take a **half crank up off the bottom** then into gear; a steady **tap-tap-tap** is the bait swimming, a **steady pull-down that stays down** is the bite; SoCal sinkers **6–10 oz**, up the weight when current picks up; **a longer loop gives the bait more action.**
5. **Weedless slug, the default kelp presentation** — 7-in weedless/MC slug on a **keel-weighted hook (Gamakatsu 7/0, 3/8 oz, or Trokar)**, Landesfeind preferring the heavier **3/4 oz** because it keeps the bait in the water on a fast wind; upgrade the stock spring to an **Owner large / Trokar / Eagle Claw XL** and bury it so the plastic butts the hook. Short pinpoint casts to individual stringers, starting at the leading edge. `techniques/swimbaits.md` (Landesfeind, `YIABTTYXeqc`, `n6PTy8g3pb0`).

**Once you're bit, whatever you threw:** **set, then grind — never pump the rod.** Every pump gives slack the calico uses to dive back into the kelp. `techniques/swimbaits.md` records this as broadly applicable to calico on any gear (Dave Hansen, `KTsXdQXAnkU`) — high confidence, repeated doctrine.

---

## 4. Reading the kelp line itself (applies no matter what you tie on)

From `species/calico-bass.md`, `locations/bass-structure.md`, `conditions/current-diagnostics.md`:

- **Current, not tide.** Calico are current-driven and largely tide-indifferent — the opposite of spotted bay bass. Current running **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage, skip it. (Kept side by side: the late-fall San Clemente exception where bass wanted off-color water with current running *into* the island, 11/23/22.)
- **Read the current off the kelp:** kelp **pulled 20 ft under** = raging current, surface presentations dead; **laid down** = strong; **resurfacing** = slacking, switch back up. Under raging current the router says go **subsurface — sunk iron or leadhead — or wait for the slack.** That row is the one place a bottom-oriented plastic naturally fits the calico table.
- **Where to look on the meter:** calico mark **tight to kelp/structure edges and on hard bottom**, at the reef-to-sand transition. Typical working depths run the **outside kelp edge ~50 ft in to ~25 ft**, and calico will rise **10–15 ft off 80–100 ft of reef** to eat. A solid unbroken wall of bait usually has no predators on it; broken, harried bait does.
- **Which side of the head:** biting fish sit on the **up-current / leading edge**; hit three or four sides of a head and you'll know in two or three casts.
- **Water:** a green-stained, near-opaque color with roughly **5–10 ft visibility** was called out as the preferred kelp-edge read — the stain gives fish a place to hide (`9xNhdu2aBqE`, San Clemente West End, 2015-10-28, unregistered channel — medium).
- **Moon:** on clear full-moon nights calico gorge after dark and **shut down by mid-morning** — fish first light or late afternoon.
- **Birds:** **cormorants diving *in* the kelp** = actively feeding, the best calico tell inshore.

**Regulation:** California / CDFW minimum legal size for calico (kelp bass) is **14 in**, as of 2026-08 — **verify current rules before you fish** (`species/calico-bass.md`, `r6j5w40fVHI`, 2022-04-25).

---

## Bottom line

The KB will fully support you fishing a drop shot **in a bay for spotties or halibut**, and it will fully support you fishing **plastics on a kelp line** — but it has no note, row, or source connecting the two. If you want to run the experiment, the rig geometry above (hook up, 6–10 in tag, weight sized to hold bottom) is the documented starting point, but **you'd be inventing the leader class and the fouling solution yourself**, and the KB's kelp numbers (25–60 lb leader) say to go far heavier than the 10–12 lb the drop-shot note specifies. I'd log it as an open item rather than let it read as KB doctrine.

Per this KB's own rule in `CLAUDE.md` — "**Flagged stubs, never silence** ... a method popular in the real SoCal/Baja fishery but absent from the source corpus gets a flagged stub row in the router's table" — if drop-shotting calico is a real thing in the fishery, the calico router is missing a stub row it ought to have. That's worth flagging to Cameron.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/drop-shot.md`, `species/calico-bass.md`, `techniques/swimbaits.md`, `techniques/dropper-loop.md`, `lures/bay-bass-plastics.md`, `tackle/gear-classes.md`, `locations/bass-structure.md`, `sources/source-registry.md`, `sources/extraction-log.md`, `techniques/README.md`  
*videos:* `k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`, `KTsXdQXAnkU`, `P6Slg6RQiXw`, `9xNhdu2aBqE`, `L3tkGVu516A`, `HMdrP4-i9MM`, `Rwy4MqeXCIU`, `kwMIgkCtFUE`, `0KQ--N5TjqE`, `YIABTTYXeqc`, `n6PTy8g3pb0`, `r6j5w40fVHI`  
*gaps admitted:* No drop-shot doctrine for calico bass anywhere in the KB — species/calico-bass.md has no drop-shot row in its Situations → techniques table, and not even a flagged stub row, which the KB's own 'flagged stubs, never silence' rule would require if the method is real in the fishery. | techniques/drop-shot.md is sourced entirely from bay/flatfish videos (halibut, spotted bay bass) and never mentions calico, kelp, islands, or reef — no source in the corpus applies it to kelp-line structure. | No leader class is documented for a drop shot fished in kelp — the drop-shot note's 10–12 lb (or 15–20 lb behind 2 oz) is far below the 25–65 lb range the KB records for calico at a kelp line, and the conflict is never addressed by any note. | No weight sizing for a drop shot in kelp-line current — the 1/4–2 oz range is given for bay/sand conditions only, with nothing on holding bottom against the 'kelp laid down' or 'kelp pulled 20 ft under' current states. | No hook-to-weight distance is documented for calico — the 6–10 in figure is explicitly justified by the halibut strike zone, and the KB gives no calico equivalent. | No weedless or snag-resistant drop-shot variant is documented anywhere in the KB, so the KB offers no solution to fouling an upward-facing exposed J-hook in kelp (it only records that kelp sliding down a hook shank costs fish). | The KB does not say whether a drop shot should be cast to a kelp edge or dropped vertically for calico; the only vertical-drop doctrine on file (dropper loop: 'drop straight down, never cast it') is for a different rig. | No calico-specific hookset guidance for a drop shot — the drop-shot note's 'swing on anything' and the calico swimbait note's 'set on the pause, never on the grab' conflict, and no note reconciles them. | No boat-positioning or drift guidance for fishing a stationary bottom rig on a current-swept kelp edge; the calico boat-work doctrine is written for casting and covering water.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

I followed the protocol from `README.md` → `planning/day-plan-protocol.md` → the species router → the technique note. Here is what the KB actually supports.

## The short answer: this KB does not document a drop-shot program for calico bass

I have to be straight with you before giving you anything actionable.

**`techniques/drop-shot.md` is not a calico note.** Its front matter gates it to `regions: [socal-bight]`, `waters: [bay-harbor, nearshore-coast]`, and its tags are `[drop-shot, halibut, spotted-bay-bass, bays, finesse, vertical]`. Its "Reach for this when" list names exactly two fish — California halibut and spotted bay bass — plus surf casting. Its own framing is *"fish holding on or just off the bottom"* with the weight pinned to the deck.

Two consequences under `planning/day-plan-protocol.md` step 1b:

- **On an island kelp line (Catalina, Clemente, the Channel Islands), the drop shot is out of envelope entirely.** `species/calico-bass.md` carries `waters: [nearshore-coast, island, bay-harbor]`; the drop-shot note does **not** include `island`. Step 1b says a technique whose `waters` doesn't intersect the day's waters is "never offered — not ranked lower, not offered with a caveat."
- **On a coastal kelp line it clears the waters gate but has no calico content behind it.** Nothing in that note was written about kelp, kelp abrasion, or calico.

And on the other side of the router: the Situations → techniques table in `species/calico-bass.md` has **17 rows and not one of them is a drop shot** — not even a `⚠ Flagged stub` row. So this isn't a case of the KB flagging a known method it hasn't sourced yet; the mapping simply isn't there.

## The closest thing the KB has — and it came off a calico panel

There *is* one drop-shot-family rig in the KB that was described by calico anglers and is built for structure rather than open sand. From the Fred Hall calico bass panel (`RUuPNpK0x-s`), logged in `techniques/drop-shot.md`:

- **Bait:** a slug-style soft plastic with a tail fin, rigged **weedless on an Owner twist-lock** hook — the same weedless-slug family as `techniques/swimbaits.md`, put on a dropper-style leader instead of a straight cast-and-wind.
- **Rig:** roughly a **2 ft leader** from weight to bait, with a **1 oz torpedo/keel weight** below.
- **Presentation:** sight-fish it — cast down a **visible sand channel between structure** and twitch it back.

That 2 ft leader and weedless hook are the two things that would matter in kelp, and the panelists were calico guys. But read the fine print: the panel described this rig producing on **California halibut and bay species in sand channels**, not on calico on a kelp line. The KB records no calico catch on it. Same note, same panel, also logs a **"reverse drop shot"** among slow-day improvisations — rig detail was not given on camera, so there's nothing to build from.

## If you carry the bay build to a kelp line, two things in the KB will fight you

These are real conflicts between notes, not my opinion:

1. **Leader.** The documented drop-shot builds run **10–12 lb leader on a light drag** (`techniques/drop-shot.md`), and the light-finesse halibut variant runs **10 lb, 12 lb at the most** (`BPxE3xn3gAc`). The calico kelp doctrine in `species/calico-bass.md` calls for **heavy fluoro, 40–65 lb, specifically for kelp abrasion**, and the weedless-in-the-junk presentation in `techniques/swimbaits.md` runs **50–60 lb fluoro to 50 lb braid** (`RUuPNpK0x-s`). Twelve-pound leader against a calico that runs into a stringer is a break-off, and `species/calico-bass.md` records exactly that failure mode at Cat Harbor — *"consistent bites with hooked fish repeatedly running into the kelp"* (`_KldpqPPT1c`, 2019-05-23).
2. **Hook orientation vs. weedlessness.** The rig's single most emphasized rule is an **exposed point riding upward** after the Palomar — `techniques/drop-shot.md` lists "hook not facing upward" as the #1 rigging error, and the halibut version deliberately **exposes more point toward the tail**. That is the opposite of what kelp demands; every kelp-line presentation the KB documents for calico is weedless or on a keel-weighted spring hook.

Gear class also doesn't line up: `tackle/gear-classes.md` puts the drop shot in the **light spinning class, 10–20 lb**, while calico kelp work sits in the **bass class — 7–9 ft graphite-composite, 200–300 low-profile reel, 30–65 lb braid**.

## The transferable mechanics, if you want to experiment anyway

Everything below is from `techniques/drop-shot.md` and is bay/surf/halibut doctrine. Treat it as a starting point you're adapting, not a calico program:

- **Hook-to-weight distance: 6 to 10 inches** (Rod Marquez). The reasoning given is the halibut strike zone — a predator won't burn energy chasing a bait 15 ft off, but commits at 6–10 in. It is not tuned to a fish that sits on a kelp edge and eats what current sweeps past.
- **Weight:** **1/4 oz up to 1 oz**, light when it's glassy; the heavier school runs **1–2 oz** and matches line to it — **8–12 lb test with 1 oz, 15–20 lb with 2 oz**. Cylinder-style weight, plain lead is fine (`_rcxIWhNMSE`; re-cut as `nZfEB7466ys`).
- **Hook:** strong long-shanked forged J-hook (O'Shaughnessy). Alternates documented: **VMC Spin Shot #2** swivel hook for a free-swinging bait, or a **#2 mosquito hook** (`M2qZiY2lR98`, `_XfScSliRVk`).
- **Working it:** weight on bottom, bait suspended above it, **shake in place**. Grub → rod tip down at **45°**, constant retrieve. Fluke → **twitch, reel slack, twitch again**.
- **Hookset — the failure point:** **never set into slack** (`EGKesj7V64M`, Roman Castro). On light line it's the slack, not the force, that pops the leader — wind down, lower the rod, take up slack, *then* set. Swing on anything that doesn't feel like bottom; a missed swing costs nothing.
- **Mobility:** nothing in **~20 minutes, move** — fish may be 20 yards off.
- **Sloped-bottom addendum** (`fHMwcm1xRQk`): fishing off a slope, lifting the rod doesn't lift hook and weight equally — the weight sits on bottom while the bait ends up only **2–3 in** off, short of the 6–10 in spacing. Run a longer leader. Worth knowing if you try this over a sloping reef-to-sand edge.

## What the KB actually tells you to do on a kelp line

If the goal is calico on a kelp edge, `species/calico-bass.md` routes you here. The read first:

- **The edge is the spot** — biting fish sit on the **up-current / leading edge**; calico face into the current and ambush from the front. *"Hit three or four sides of it and you know in two or three casts"* (Landesfeind, Academy Ep. 14).
- **Current, not tide** — parallel current makes the edge fishable; into the beach is marginal; off the beach gets skipped. Read it off the kelp itself: **pulled 20 ft under = raging** (surface presentations dead), **laid down = strong**, **resurfacing = slacking** (`conditions/current-diagnostics.md`, `locations/bass-structure.md`).
- **Depths:** outside kelp edge **~50 ft in to ~25 ft**; calico will rise **10–15 ft off 80–100 ft of reef** to eat.
- **Cover water:** **10–25 casts** to the prime edge, then move 100 ft or 100 yards.

Then the presentations — and note that the two closest in spirit to a drop shot (bottom contact, vertical, let-it-sink) are both documented and both use a single weighted head rather than a dropper:

| What you're doing | The KB's answer |
| --- | --- |
| Fish tight to individual stringers | **Weedless swimbait** — 7" slug on a **3/8–3/4 oz** keel-weighted spring hook, short targeted casts, fast steady wind, pause on the eat (`techniques/swimbaits.md`) |
| Want bottom contact right at the kelp | **Pitch-and-sink**: a **1 oz** black/gold leadhead pitched at the base of the kelp line, let it sink **straight to the bottom** — the bite comes on the sink. **25 lb fluoro** (Dave Hansen, `KTsXdQXAnkU`, 2019-06-05) |
| Fish deep on the edge | **Lead-head swimbait sunk 70–80 ft** over structure; fish holding up will rise to it (`techniques/swimbaits.md`) |
| Tight to the beach, current ripping, no kelp | **Free-spool bounce a weighted tube** — **1.5 oz** holds bottom, current sweeps it **5–10 ft** further each bounce; "calicos every cast" (`9a-Zy_D6c3w`) |
| Bigger cruising fish, current up | **Surface iron** along the kelp line, jig-stick class |
| Trophy (7–10+ lb) rather than numbers | **8–10 in baits**, 65–80 lb braid — baits under ~5.5 in top out around 1–4 lb (`ZoIzpyyS9xw`) |

That pitch-and-sink at the kelp base is the note I'd point you at if what you like about a drop shot is the vertical, bottom-contact, bite-on-the-drop presentation. It gets you there without a tag-end weight to hang in the stringers, and it comes with a leader spec that survives kelp.

## Bottom line

Fish a drop shot for calico if you want to — plenty of people do — but understand you'd be extrapolating, and this KB gives you nothing calico-specific to extrapolate from: no hook-to-weight distance tuned to a kelp edge, no weight for kelp current, no leader spec that reconciles 10–12 lb finesse against 40–65 lb abrasion doctrine, and no recorded catch. If you go out and make it work, that's a genuine gap worth writing up.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/drop-shot.md`, `species/calico-bass.md`, `species/spotted-bay-bass.md`, `techniques/swimbaits.md`, `lures/bay-bass-plastics.md`, `locations/bass-structure.md`, `tackle/gear-classes.md`  
*videos:* `RUuPNpK0x-s`, `EGKesj7V64M`, `BPxE3xn3gAc`, `fHMwcm1xRQk`, `M2qZiY2lR98`, `_XfScSliRVk`, `_rcxIWhNMSE`, `nZfEB7466ys`, `KTsXdQXAnkU`, `9a-Zy_D6c3w`, `ZoIzpyyS9xw`, `_KldpqPPT1c`  
*gaps admitted:* No calico-bass drop-shot program exists anywhere in the KB — species/calico-bass.md's 17-row Situations → techniques table has no drop-shot row and not even a flagged stub for it. | techniques/drop-shot.md is gated waters: [bay-harbor, nearshore-coast] and excludes `island`, so it is formally out of envelope for an island kelp line (Catalina, Clemente, Channel Islands) under day-plan-protocol step 1b. | No hook-to-weight distance is documented for calico or for a kelp edge — the 6–10 in figure is explicitly reasoned from the California halibut strike zone. | No drop-shot weight sizing is documented for kelp-line current; the 1/4–1 oz and 1–2 oz figures are bay/surf/halibut numbers. | No leader spec reconciles the drop shot's 10–12 lb finesse leader with calico kelp doctrine's 40–65 lb fluoro for abrasion — the KB has no drop-shot build that survives kelp. | The weedless-slug dropper rig from the Fred Hall calico panel (RUuPNpK0x-s) is documented only for California halibut and bay sand channels; no calico catch on it is recorded. | The 'reverse drop shot' named on the same panel has no rig detail — it was not given on camera. | No drop-shot retrieve, cadence, or presentation is documented for a kelp edge, canopy, or stringer. | No hook style is documented that satisfies both the drop shot's exposed-point-up requirement and kelp weedlessness. | No sonar or depth guidance is documented for drop-shotting calico specifically (the 25–50 ft outside-edge and 10–15 ft rise-off-reef figures come from general calico finding-them doctrine, not from a drop-shot source).

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short answer: this knowledgebase does not cover drop-shotting calico bass on a kelp line

I want to lead with that, because the honest answer matters more than a plausible one.

I ran the [day-plan protocol](planning/day-plan-protocol.md) the way it says to — envelope first, then in through the species router — and the mapping you're asking for does not exist in this KB:

- **[`species/calico-bass.md`](species/calico-bass.md)** has a 17-row *Situations → techniques* table. **No row is a drop shot.** There isn't even a `⚠ Flagged stub` row for it, which is what CLAUDE.md says a real-fishery method absent from the corpus is supposed to get. So this is silence, not a documented "no."
- **[`techniques/drop-shot.md`](techniques/drop-shot.md)** never mentions calico. Its front matter is `tags: [drop-shot, halibut, spotted-bay-bass, bays, finesse, vertical]`, `waters: [bay-harbor, nearshore-coast]`, `depth_band: on bottom`. Its "Reach for this when" names exactly two fish: [California halibut](species/california-halibut.md) buried in the sand, and [spotted bay bass](species/spotted-bay-bass.md).
- The gear lexicon agrees. [`tackle/gear-classes.md`](tackle/gear-classes.md) files the drop shot under **Light spinning class (a.k.a. light bay finesse), 10–20 lb** — and files calico under **Bass class, 7–9 ft, 200–300 reel, 30–65 lb braid**. Two different classes, and the KB never bridges them.

So I can't tell you the hook-to-weight distance, the weight, or the leader for a calico kelp-line drop shot, because no note here states them. What I *can* do is give you (1) what the protocol's gating actually permits, (2) the rig exactly as the KB specifies it if you want to adapt it yourself with eyes open, and (3) the kelp-line presentations the KB *does* rank — including the two closest to what you're reaching for.

---

## 1. Where the protocol lets you even try it

Step 1b of the protocol is a **binding** filter — a note whose `waters` doesn't intersect the day's waters is "never offered, not ranked lower, not offered with a caveat."

Per the vocabulary in [`locations/regions.md`](locations/regions.md): `nearshore-coast` = "the coastal strip — kelp lines, breakwalls, jetties, riprap, coastal reef"; `island` = "island shorelines, boiler rocks, island ridges **and their kelp**."

- **Coastal kelp line** (Point Loma, La Jolla, Dana Point, North County) — `nearshore-coast`. This is *inside* the drop-shot note's `waters`. The protocol wouldn't block it; the technique note simply has no calico content.
- **Island kelp** (Catalina, San Clemente, the Channel Islands) — `island`, which is **not** in the drop-shot note's `waters`. On a strict read of step 1b, this KB would not put a drop shot in front of you at Catalina at all.

## 2. The drop-shot rig exactly as the KB states it — and why it fights kelp doctrine

Every number below is from [`techniques/drop-shot.md`](techniques/drop-shot.md), and every one is stated for bay/surf fish, not calico:

- **Outfit:** light rod, **2000-size spinning reel**, braid (you can *see* the line for the visual bite and feel it on slack line), **10–12 lb leader, light drag** (`k4mD2d6C81k`).
- **Hook:** strong long-shanked forged J-hook (O'Shaughnessy) so the plastic can't slide (`k4mD2d6C81k`). Alternates: **VMC Spin Shot #2**, or a **#2 mosquito hook** (`_XfScSliRVk`). The KB itself flags that the Spin Shot's 360°-swing rationale is miscited — that content is actually in `_rcxIWhNMSE`, with `M2qZiY2lR98` and `nZfEB7466ys` being verbatim re-cuts of it, not independent confirmation.
- **Tie:** Palomar. Measure **12–14 in** of leader, double the line, tie it, then pass the tag **back down through the top of the hook eye** so the **point rides up**. Hook not facing up is listed as the single most common rigging error (`k4mD2d6C81k`).
- **Weight:** on the tag below the hook. One build says **1/4 oz to 1 oz**, light when it's glassy (`k4mD2d6C81k`); a second says **1–2 oz**, matched to line — **8–12 lb with 1 oz, 15–20 lb with 2 oz** (`1enjjFVcDG0`). Cylinder style; lead is fine, tungsten is pricier with more sensitivity (`_rcxIWhNMSE`).
- **Bait:** 4-in scented finesse fluke (ZMan), or swap in a grub or small swimbait (`k4mD2d6C81k`). [`lures/bay-bass-plastics.md`](lures/bay-bass-plastics.md) tabulates it as "drop-shot fluke / grub / small swimbait, 4 in, long-shank J-hook (point up)."
- **Working it:** weight pinned to the bottom, bait suspended just above; **shake in place** (`1enjjFVcDG0`). Grub — rod tip down at **45°**, constant retrieve. Fluke — **twitch, reel the slack, twitch again** (`1enjjFVcDG0`).
- **Hookset:** **never set into slack.** On light line, driving a set with slack between tip and bait is what pops the leader. Wind down, drop the rod, take up the slack, *then* swing — and swing at anything that isn't bottom, because a missed swing costs nothing (`EGKesj7V64M`).

**Three places this collides with calico doctrine in this KB — none of which any note resolves:**

1. **Leader class.** The drop shot runs **10–12 lb** with a light drag. [`techniques/swimbaits.md`](techniques/swimbaits.md) says kelp calico want **50–65 lb braid to 60 lb fluorocarbon**, because "the leader gets braided up and chafed just from throwing it in the kelp" (`YIABTTYXeqc`, `n6PTy8g3pb0`); a second build runs 65 lb braid to 40 lb mono (`9xNhdu2aBqE`). That's roughly a 5x gap, on structure the KB says chafes leader passively.
2. **Fouling.** Every drop-shot hook in the KB is exposed — long-shank J, Spin Shot, mosquito. The whole kelp bass technique note is organized around **weedless** rigging so the bait "comes through cover clean." Nothing here tells you how to run a drop shot through kelp without hanging up.
3. **Camping vs. covering.** The drop shot is an in-place presentation; its own move-rule is "20 minutes with no bite, move" (`1enjjFVcDG0`). [`species/calico-bass.md`](species/calico-bass.md) states the opposite tempo: "**Covering water is the method** — a bed is graded by a handful of casts to the prime edge and then you move on" (`YIABTTYXeqc`, `0KQ--N5TjqE`).

**One genuine connection, and it's thin.** `RUuPNpK0x-s` is the **Fred Hall Calico Bass Panel (2013-03-09)** — a source on *both* [`species/calico-bass.md`](species/calico-bass.md) and [`techniques/drop-shot.md`](techniques/drop-shot.md). Two drop-shot-family items in that technique note trace to that calico panel ([`techniques/evidence/drop-shot.md`](techniques/evidence/drop-shot.md)):

- **Weedless slug on a drop-shot-style leader** — a slug-style plastic with a tail fin, rigged weedless on an **Owner twist-lock**, roughly a **2 ft leader** from weight to bait, **1 oz** torpedo/keel weight below. Cast down a visible sand channel between structure and twitch it back. This is the only weedless drop-shot-style rig in the KB — but the note scopes it to halibut, spotted bay bass and "other bay species," and to a sand channel, **not a kelp line**.
- **The "reverse drop shot"** is named as an improvisation for a dead bite — and the note explicitly says the **rig detail was not given on camera**.

## 3. What the KB actually ranks for a kelp line — including the closest vertical presentations

If your instinct is "I want a bait sitting still, down, on the kelp edge," these are the documented versions of that instinct.

**Closest thing to a drop shot — pitch-and-sink at the kelp base** ([`techniques/swimbaits.md`](techniques/swimbaits.md), `KTsXdQXAnkU`): pitch a **1 oz black/gold leadhead** right at the base of the kelp line and let it **sink straight to the bottom** — the bite typically comes on that sink. **25 lb fluoro** leader for this one, deliberately lighter than the 60 lb above; the note calls it a second workable combination, not a contradiction.

**Punching the canopy** (`P6Slg6RQiXw`): where fish sit *up under* a dense floating canopy rather than on the edge, flip a heavy leadhead on a short accurate cast into gaps in the kelp — freshwater flipping borrowed onto kelp; fish work the dropped bait from underneath before eating. Flagged single-source: one session, San Clemente Island, December 2013.

**Sunk leadhead swimbait:** sink the bait **70–80 ft** over structure for calico, and fish holding up will rise to meet it. **Caveat the note carries itself** — that depth figure is flagged `⚠ unverifiable`, with no source of its own.

**When current rips and the kelp goes under**, the calico router's row is: slow down, switch to **subsurface** (sunk iron, leadhead), or wait for the slack. Read it off the kelp — pulled under = raging, laid down = strong, resurfacing = slacking, go back on top. ([`locations/bass-structure.md`](locations/bass-structure.md) states this and flags that the three-tier version is cited in `conditions/current-diagnostics.md` to `HnqiE05vdXs`, not to `0KQ--N5TjqE`.)

**The default kelp-line program the router actually ranks first** — a **7-in weedless slug** on a keel-weighted hook, Gamakatsu **7/0 3/8 oz** or Trokar; the **3/4 oz** weight is preferred because it keeps the bait in the water while you wind fast; replace the stock spring with an **Owner large / Trokar XL** and bury it so the plastic butts the hook (roughly **10x** the fish per bait). Short pinpoint casts to individual stringers at the **leading edge**; fast steady wind; **set on the pause, never on the grab** — swing the instant you feel it and "nine times out of ten you pull the bait out of the fish's mouth" (`YIABTTYXeqc`, `n6PTy8g3pb0`). Reel **at least 6.2:1**, because calico eat and come straight back at the boat (`P6Slg6RQiXw`) — the KB flags this as an unreconciled behavioral conflict with Landesfeind's general inshore doctrine. Rod: **8–8½ ft** casts farther into structure, **7 ft** gives more leverage pulling fish out of the kelp (`IATPg9110CE`). Once bit: **set, then wind — never pump.**

**Where to put the boat, whatever you throw** ([`species/calico-bass.md`](species/calico-bass.md), [`locations/bass-structure.md`](locations/bass-structure.md)):

- **Current is the gate.** Parallel to the beach = fishable; into the beach = marginal; off the beach = skipped (`0KQ--N5TjqE`). Calico face into the current and ambush from the **front** of the structure (`Rwy4MqeXCIU`).
- **The edge is the spot** — leading/up-current edge, outside edge, isolated stringers, not the dense middle. "Hit three or four sides of it and you know in two or three casts" (`0KQ--N5TjqE`; the note flags the quote as non-verbatim, the doctrine as verbatim).
- **Light angle sets where they hold.** Bright, stable sun → calico levitate into the canopy and concentrate on the **outer canopy edge**; overcast **spreads them out** through the column and structure (`RUuPNpK0x-s`). That second case is exactly where a bottom-pinned presentation is least likely to be where the fish are.
- **Depth follows the bait, not a number** (`kwMIgkCtFUE`) — bass structure generally runs **20–120 ft**; light kelp that never reaches the surface still holds them, e.g. kelp riding ~20 ft off the bottom in **40–42 ft** off North County San Diego (`HMdrP4-i9MM`).
- **Regs — California / CDFW, verify before you fish:** **14 in** minimum (`r6j5w40fVHI`, as of 2026-08), bag limit **5** (`LqW32NSkObY`, as of 2019-03-13 — the note itself calls this the oldest regulatory figure it carries).

---

### My recommendation

If you're on a **coastal** kelp line and want a bottom-oriented calico presentation, this KB's answer is the **1 oz leadhead pitched to the kelp base on 25 lb fluoro, bit on the sink** (`KTsXdQXAnkU`) — not a drop shot. It puts a bait on the base of the edge, it's documented for calico, and it doesn't ask 10 lb leader to survive kelp.

If you want to fish an actual drop shot there anyway, treat it as an experiment and log it: the rig build above is sound and cited, but you'd be scaling leader up from 10–12 lb toward the 40–65 lb kelp-abrasion range and choosing a weedless hook on your own judgment — and **no note in this KB backs either decision.** That's exactly the kind of thing that should come back as an attributed observation and, per CLAUDE.md's "flagged stubs, never silence" rule, get a stub row added to the calico router so the next person doesn't hit silence the way I just did.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/drop-shot.md`, `techniques/evidence/drop-shot.md`, `species/calico-bass.md`, `techniques/swimbaits.md`, `locations/bass-structure.md`, `locations/regions.md`, `tackle/gear-classes.md`, `lures/bay-bass-plastics.md`, `species/spotted-bay-bass.md`, `sources/fact-check-ledger.md`, `sources/escalations.md`  
*videos:* `k4mD2d6C81k`, `1enjjFVcDG0`, `EGKesj7V64M`, `_XfScSliRVk`, `_rcxIWhNMSE`, `M2qZiY2lR98`, `nZfEB7466ys`, `9qwsg-e9ECA`, `fHMwcm1xRQk`, `BPxE3xn3gAc`, `RUuPNpK0x-s`, `YIABTTYXeqc`, `n6PTy8g3pb0`, `9xNhdu2aBqE`, `KTsXdQXAnkU`, `P6Slg6RQiXw`, `IATPg9110CE`, `9a-Zy_D6c3w`, `ZoIzpyyS9xw`, `0KQ--N5TjqE`, `Rwy4MqeXCIU`, `kwMIgkCtFUE`, `HMdrP4-i9MM`, `HnqiE05vdXs`, `r6j5w40fVHI`, `LqW32NSkObY`, `OURS05qEGcA`  
*gaps admitted:* The KB has no drop-shot presentation for calico bass anywhere - species/calico-bass.md's 17-row Situations-to-techniques table contains no drop-shot row and no flagged stub row either, so the method reads as absent rather than deliberately excluded. | No hook-to-weight (tag-end) distance is stated for calico; the only spacing guidance in techniques/drop-shot.md is halibut-scoped and deferred to species/california-halibut-surf-lures.md, and lures/bay-bass-plastics.md's '6-10 in above the weight' figure is itself flagged contradicted-by-source in sources/fact-check-ledger.md. | No drop-shot weight size is given for kelp or for the current a kelp line runs - the stated ranges (1/4-1 oz, or 1-2 oz matched to line) are bay- and surf-scoped only. | No leader or line class is given for a drop shot fished in kelp; the technique note's 10-12 lb bay leader and species/calico-bass.md's 40-65 lb kelp-abrasion doctrine are never reconciled by any note. | No weedless drop-shot hook option exists in the KB - all three documented hooks (long-shank J, VMC Spin Shot #2, #2 mosquito) are exposed, and nothing covers running the rig through kelp without fouling. | The 'reverse drop shot' is named in techniques/drop-shot.md as a dead-bite improvisation, but the note explicitly records that the rig detail was not given on camera. | No boat-positioning or drift doctrine exists for holding a vertical, in-place presentation on a kelp edge; the calico boat-work doctrine is written entirely around covering water with casts. | No calico sonar depth is documented for a bottom-pinned presentation - the 'outside kelp edge ~50 ft in to ~25 ft' band in species/calico-bass.md is flagged unverifiable with no cite, and the 70-80 ft leadhead sink depth in techniques/swimbaits.md is flagged unverifiable as well. | For island kelp (Catalina, San Clemente, Channel Islands) the KB gives no basis at all: techniques/drop-shot.md's waters field excludes 'island', so the day-plan protocol's binding step-1b filter would not offer the technique there. | No calico zone guide exists for any zone - every entry under species/calico-bass.md's Zone guides section is a flagged stub, so there is no zone-level trip story to place a kelp-line program into.

</details>
