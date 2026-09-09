# Finding fish — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.5 | 11.5 | 12 |
| found | 1.5 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 2 | 2 | 2 |
| honest | 2 | 1.5 | 2 |
| actionable | 2 | 2 | 2 |
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
| Finding fish | 11.5 | 11.5 | 12 |
| Conditions & season | None | None | None |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 14. [finding] What do yellowtail look like on the sounder and at what depths, and how does that differ from bluefin?

**Winner:** NOW · mapping {'A': 'B2', 'B': 'NOW', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 1 | 2 | **11** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three nail the core answer - yellowtail as a shallow, structure-referenced mark (arcs/tight balls at ~5-10 fathoms, boomerang arcs at 90-120 ft under paddies, 150-300 ft on Baja high spots) versus bluefin as an open-water suspended mark (30-50 fathoms sounded, 198-360 ft at night, 300-480 ft at the banks) - with real video ids and note paths behind the numbers. C is the most usable document, with the fullest bluefin depth table, per-row technique and jig weight, and per-claim confidence labels, but it repeats the 'below 300 ft = traveling, not biting' rule alongside its own 240-360 ft night and 50-80 fathom bank rows without noticing the conflict, which would mislead someone planning a night jig session. B carries essentially the same depth and shape material plus the yellowtail feeding-state read (stratified = hunting, bottom-balled = not), and is the only answer that flags the headline 5-10 fathom figure as unsupported by the source it cites and names that 300 ft contradiction outright. A is a close third: strong tables and settings guidance and it does name a related range-window tension, but it lacks the feeding-state read and the metered-but-not-showing band, and its opening pointer to the species routers cites the electronics note instead.

- *B2 reasons:* found: hits both species' sonar sections plus the electronics/DSL/paddy notes; answers depth + shape + difference directly. specific: fathom conversion, 5-10 fm structure band, 90-120 ft paddy boomerangs, 150-300 ft BOLA (bit 150-180), 30-50 fm bluefin, 198-330 ft night, 0-120/0-150/0-300 range windows, Furuno TVG 55-57 / ping 15 of 20, jig weights 150-400 g. sourced: video ids on nearly every parameter plus note paths, though the opening line says signatures live in the species routers and then cites planning/electronics-and-sounder.md. scoped: SoCal vs Baja (BOLA, San Benito) and bank/island/paddy waters kept labelled; no regulatory claims made. honest: names the unreconciled 0-120/150 ft private-boat window vs 30-50 fm sounded-school tension and refuses to resolve it; long, concrete gap list (no bluefin shape vocabulary, no CHIRP, no size-from-arc). actionable: mark -> technique -> gear class chain is complete, and the settings section tells you what to change between the two fisheries. Weaker than B/C in one respect: no yellowtail feeding-state read (stratified vs bottom-balled) and no metered-but-not-showing 40-60 ft row, so the 'what the shape means' half is thinner.
- *B3 reasons:* found: widest sweep - both routers, electronics, DSL, yo-yo iron and flat-fall technique notes; the head-to-head table is the cleanest direct answer to 'how does that differ'. specific: richest numeric set (11-row bluefin depth table with dates/places, 40-60 ft 'coming up' rules out the yo-yo, 20-30 ft rock, 120-240 ft yo-yo band, 250 g floor, 100-200 ft flat-fall zone, line-out is not true depth). sourced: video ids plus channel, date and an explicit high/medium confidence label per claim, matching the registry rubric - the most transparent sourcing of the three. scoped: SoCal vs BOLA/San Benito/Cortez kept separate, sportboat vs private-boat context labelled, no regulatory claim. honest: good confidence caveats and a solid gap list, but it states the 'fish below 300 ft are traveling, not biting' rule and then, unflagged, lists 240-360 ft night marks, a 198-330 ft school and 300-480 ft bank marks - an internal contradiction handed to the angler as settled doctrine, exactly the thing B caught. actionable: highest ceiling - every depth row carries the technique and jig weight it selects, plus drop mechanics (get below the called depth, wind up through).
- *NOW reasons:* found: full coverage of both routers plus the evidence files and the Coronado zone guide; the structure-referenced vs open-water-suspended framing answers the actual question first. specific: every band carries a number and a consequence - 40-60 ft staging (not yo-yo water), 60-80 ft in 120 ft at Cortez, 30-40 fm San Benito squid, 240-360 ft night setting a 250 g jig floor, 300-480 ft bank marks, 15 ft spot -> 30 ft screen. sourced: note paths as live links, video ids per row, evidence-file citations; flags which rows are single-trip. scoped: Baja/Cortez vs Bight separated, paddy/bank/island waters distinguished, no regulation stated. honest: strongest integrity work - flags the headline 5-10 fathom figure as contradicted-by-source and KB-internal, flags the DSL mechanism as unverifiable in nRFFM8DT-og, flags the paddy row as not species-tagged, and names the flat contradiction between 'below 300 ft = traveling' and its own 240-360 ft night rows without papering over it. actionable: jig-weight floors by depth, chum-then-cast, anchor-to-drift pivot, range windows; the caveats sit beside the numbers rather than replacing them.

<details><summary>Full prompt</summary>

What do yellowtail look like on the sounder and at what depths, and how does that differ from bluefin?

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

# Yellowtail vs. bluefin on the meter

Short version: **yellowtail are a shallow, structure-anchored mark you read against the bottom; bluefin are a deep-water, mid-column mark you read against nothing but water.** The KB splits the work this way on purpose — `planning/electronics-and-sounder.md` owns the general method and settings, and the species-specific signatures live in the species routers (`planning/electronics-and-sounder.md`).

Units first, because both notes talk in fathoms: **1 fathom = 6 ft**, and the sounder is historically a "fathometer" because its original job was bouncing depth off the bottom (`planning/electronics-and-sounder.md`, `Rf1HKJG-SDg`, `9hEa3sGTh40`). Worked example from the same branch: 9 fathoms read at Catalina converted on the fly to 54 ft (`HGyL7pXy3Ts`).

---

## Yellowtail — three signatures, all shallow, all read against structure

From `species/yellowtail.md`:

- **Structure/bottom yellows — the classic read: arcs / boil-ups at ~5–10 fathoms (≈30–60 ft) near structure**, appearing as **tight balls hugging the structure** over hard bottom, pinnacles and high spots. Quoted: "We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`). That mark routes to yo-yo iron (Salas 6X class, hit bottom then a couple of cranks off it) or a dropper loop, on a 40–60 lb class stout rod with a high-ratio reel.
- **Hard bottom only, never mud.** Structure yellows sit exclusively on hard/rocky bottom — "they're not going to be [out] in the mud... they're always going to be on the hard bottom" — so grade the *bottom return* before you even look for fish sign: **thin, faint line = sand/mud; thickening and darkening = rock** (`6DzbsElGE7E`, Dave Hansen, 2021-04-13; brand-agnostic per `planning/electronics-and-sounder.md`).
- **The tell that separates fish from bait: a thin, lighter mark riding *higher* than the bait ball is the yellowtail itself**, pushing bait up off the rocks. That's the commit signal for the anchor — not the bait pile alone (`6DzbsElGE7E`). Anchoring geometry that follows: grade the mark with repeated passes over the same GPS track, then drop the hook in the **sand patch beside the rock, not on it**, and for yellowtail specifically **anchor further still** so a hooked fish has room before it reaches structure (`planning/search-and-glassing.md`, `6DzbsElGE7E`, `xI9tPJFXbUM`).
- **Deep high-spot yellows (BOLA / Baja):** marks in the **150–300 ft** band, stacked on the **up-current face** of the high spot (`vqsD0qpwcJA` / `Jtf-bU4aM-c`). Slow-pitch / vertical jigging, 130–250 g, and it bit best at **150–180 ft**.
- **Paddy yellows don't meter deep.** Under a kelp paddy with no surface activity, look for **boomerang-shaped arcs around 90–120 ft**, and give it about **a minute or two** before writing the paddy off — a look, one sounder pass, one bait (`ZFqe49jRgA0`, Dave Hansen, 2019-05-26; the paddy-check discipline is in `conditions/kelp-paddies.md`).

**Observed depth data points that stretch that picture** (kept beside the doctrine, not folded into it):
- Cortez Bank, high spot on an incoming tide: yellowtail marked at **60–80 ft in 120 ft of water**, worked with flylines, J-hooks, surface irons and yo-yo irons; fish 20–40 lb (`UfuiWFVvz2E`).
- San Benito Island, Baja: yellowtail on **squid at 30–40 fathoms (≈180–240 ft)** — called on camera as "30, 40, 50" and later "30, 35" — feeding right off the bottom because the squid had moved out of the shallows when small mackerel took over. Nearly every fish had fresh squid in its stomach. That's a **bait-migration-driven depth read, not a fixed structure depth** (`JaKSGkZ6CAc`).

**One behavioral note the meter alone won't tell you:** fish still visibly marking but not biting at anchor is a signal to **get up above the marks and drift over them** instead of staying pinned on the hook — an anchor-to-drift pivot made off a live sounder read (`97clKtVsEOs`; `planning/electronics-and-sounder.md`).

---

## Bluefin — deep, mid-column, and you grade a mark you can't anchor on

From `species/bluefin-tuna.md`:

- **The headline signature — sounded schools, wind up, no surface sign: 30–50 fathoms (≈180–300 ft).** Quoted: "god forbid there's no foamer, you're going over a lot of fish and there's a lot of wind — that's when those fish sound down, you're looking 30, 45, 50 thousands," and you need the machine's power to reach and grade them (`HWx1jDTGsng`). That is explicitly the **meter-and-jig situation, not a troll situation** — knife jigs, 100–130 lb braid jig class (PE6–8), 150–300 g by day, 300–400 g in more current or deeper.
- **Deeper bank extension:** an overnight jig session at Cortez/Tanner (mid-August 2024) read marks **360° around the boat, from 50 fathoms down to 80 fathoms (≈300–480 ft), even below** (`LsFMBCa9DOQ`) — kept side by side with the 30–50 fm range, not replacing it.
- **Night bite on the deep scattering layer:** fish rise with the DSL after dark and the read is **depth-called marks — "fish at 180, fish at 230 ft"** — that you drop a jig straight onto (`nRFFM8DT-og`). A backside San Clemente session read a school **stacked from ~198 ft down to 330 ft** under the boat (`r4J5nP5Bkl4`). To paint the DSL at all you have to **turn the machine up: gain/TVG up (Furuno ~55–57, mid-to-high on other brands) and slow the ping (~15 of 20)** so the layer builds as a distinct band; on a Garmin GPSMAP 840xs that's gain up + ping slowed (`planning/electronics-and-sounder.md`, `conditions/deep-scattering-layer.md`). The DSL itself sits **600+ ft by day** and rises at night.
- **Shallow bluefin marks are common enough to expect** — the KB carries four separate observed shallow reads beside the deep doctrine: **60–80 ft** (jig dropped, hookup after about two cranks), plus ~100 ft moving up and down all around the boat, and ~150 ft (`cLYqjT7ddl8`); **120 ft then a "really good mark... solid" at 150 ft** off Catalina's west end (`M7BtON4GZgQ`); fish sitting in **50–100 ft** on a drift rather than up top, worked with butt-hooked sardines let swim down (`8THSuqoPI_Q`); and **80–150 ft** under an anchored kelp paddy, worked with butt-hooked and sinker-rigged live bait (`IwxqgocsQTY`). A **~60 ft bait-ball mark around the boat while chumming sardines** is its own router row → yo-yo iron, 40–60 lb class, and a heavy bite on the drop reads as the rod suddenly going dead-weight, "almost like stuck on the bottom" (`ntQXxcH5sjI`).
- Related depth parameter: the low-visibility flat-fall bite comes **at night or 250–350 ft down** — dark enough that the read is profile and flash rather than detail (`scmPq63lLWM`, `techniques/knife-jigging.md`).
- **Paddy/kelp bluefin** hang under paddies with yellowtail and dorado — grade fast and move.

---

## Side by side

| | Yellowtail | Bluefin |
| --- | --- | --- |
| Core depth band | **~5–10 fathoms (30–60 ft) near structure**; deep high spots 150–300 ft (BOLA); paddies 90–120 ft | **30–50 fathoms (180–300 ft)** sounded; night on the DSL 180–330 ft; bank extension 50–80 fm+ |
| Mark shape given in the KB | **Tight balls hugging structure**; **arcs / boil-ups**; **boomerang-shaped arcs** under paddies | No bluefin-specific shape vocabulary — the KB grades bluefin by **depth call** and by bait shape (see gaps) |
| Read against what | **The bottom** — hard vs. soft return decides whether the spot is even worth working | **Open water** — mid-column marks, often over bottom far deeper than the range you're reading |
| Fish-vs-bait tell | A **thin, lighter mark riding above the bait ball** is the yellowtail pushing bait up off the rock | **Broken, harried, moving bait holds predators; a solid unbroken wall usually doesn't** |
| What the mark routes to | Yo-yo iron / dropper loop (structure), slow-pitch 130–250 g (deep high spot), surface iron (up top) | Knife-jigging 150–400 g (deep + night), yo-yo iron (~60 ft bait balls), sinker/butt-hooked bait (50–150 ft) |
| Boat handling off the mark | Grade with repeated passes, anchor in sand beside the rock, extra standoff for break-off risk; pivot anchor→drift if they mark but won't bite | Drift and stay vertical — throw up-current off the bow, walk back to the stern; track the captain's changing depth call off marked line |

---

## Settings that change between the two

This is where the practical difference bites hardest:

- **Run manual range, not auto** — repeated doctrine across three videos, high confidence (`9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`). Left on auto over deep water the machine keeps hunting for a bottom far below your fish and shallow marks never paint. The stated payoff: at manual range a tuna school paints as **a large, distinct upside-down-U-shaped mark**; on auto it shrinks to a barely visible speck (`9hEa3sGTh40`).
- **For yellowtail you're sizing the range so the bottom sits mid-screen**, which leaves room above the bottom return to read hard-vs-soft and pick fish out of the column — worked examples: a 15 ft spot gets a 30 ft screen range, a 25 ft spot gets 40 ft (`FEXgl0eQCa8`).
- **For bluefin you're sizing the range to the fish, ignoring the real bottom.** Working windows given: **0–120 ft on older machines, 0–150 ft on newer**, regardless of whether the actual bottom is 209 or 181 fathoms (`9hEa3sGTh40`); a manual **0–150 ft** for tuna schooling under dolphin pods (`SgF5hRlEGqU`); **0–300 ft** to look for tuna suspended around 150 ft down (`FEXgl0eQCa8`).
- **Practice inshore, not on the fuel run.** Dial gain in the harbor until hard bottom reads clearly different from soft and you can tell fish from kelp; then leave it alone, go offshore and open the range up (`FEXgl0eQCa8`).
- **Backing down blanks the bottom return** — that's air under the hull, not a machine fault (`HGyL7pXy3Ts`). Relevant on the yellowtail anchor set.
- **Photograph the meter during bites** so you build your own library of marks that paid off, and **stop only on marks you can grade — it's a bait budget** (`planning/electronics-and-sounder.md`).

**One tension worth naming, because the KB carries both sides without reconciling them:** the private-boat reasoning behind the 0–120/150 ft manual window is that a private boat can't chum a school up from depth the way a sportboat can — "they can look at fish at 30 fathoms and set on it long enough... the fish will come up" — so there's no point reading deeper than the top of the column (`9hEa3sGTh40`). That sits directly against the bluefin router's 30–50 fathom sounded-school read (`HWx1jDTGsng`), which is exactly a 30-fathom mark you're expected to reach with a jig. Both are in the KB; neither note reconciles them. Practical read for a private boat: the shallow-window doctrine is about *what you can raise with bait*, and the jig doctrine is about *going down to them instead* — but the KB doesn't say that, so treat it as an open call rather than settled doctrine.

---

## What the KB does not cover (don't assume from this answer)

- **No bluefin-specific mark-shape vocabulary.** Yellowtail get "tight balls," "arcs / boil-ups," "boomerang-shaped arcs"; bluefin get depths and depth calls. The only shape language that touches tuna is the generic "large, distinct upside-down-U-shaped" school mark at manual range (`9hEa3sGTh40`), stated for tuna under dolphin pods generally, not bluefin specifically.
- **No guidance on telling bluefin apart from yellowfin, skipjack or other tuna on the meter**, and none on telling yellowtail apart from white seabass or bonito on a structure mark.
- **No frequency / CHIRP / transducer-selection guidance**, and no gain or ping numbers for yellowtail or general bluefin marks — the only settings numbers in the KB are the DSL ones (Furuno TVG 55–57, ping ~15 of 20).
- **No arc-shape-to-fish-size read** (nothing on grading fish size off mark thickness or arc length) for either species.
- **No side-scan / horizontal search-sonar method for yellowtail or bluefin from a private boat.** The only search-sonar entry is a commercial long-range sportboat running 400–600 ft side to side with an audio bite cue (`nkJNzdNlm_c`) — explicitly a different machine from the down-looking fathometer.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `planning/search-and-glassing.md`, `species/yellowtail.md`, `species/bluefin-tuna.md`, `conditions/deep-scattering-layer.md`, `conditions/kelp-paddies.md`, `techniques/knife-jigging.md`  
*videos:* `D5DR7Kx42_A`, `6DzbsElGE7E`, `vqsD0qpwcJA`, `Jtf-bU4aM-c`, `ZFqe49jRgA0`, `UfuiWFVvz2E`, `JaKSGkZ6CAc`, `97clKtVsEOs`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `nRFFM8DT-og`, `r4J5nP5Bkl4`, `M7BtON4GZgQ`, `cLYqjT7ddl8`, `8THSuqoPI_Q`, `IwxqgocsQTY`, `ntQXxcH5sjI`, `scmPq63lLWM`, `9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`, `HGyL7pXy3Ts`, `Rf1HKJG-SDg`, `xI9tPJFXbUM`, `nkJNzdNlm_c`  
*gaps admitted:* No bluefin-specific mark-shape vocabulary in the KB — bluefin are graded by depth call only, while yellowtail get 'tight balls', 'arcs/boil-ups' and 'boomerang-shaped arcs'. | No guidance on distinguishing bluefin marks from yellowfin, skipjack or other tuna on the sounder. | No guidance on distinguishing yellowtail marks from white seabass, bonito or other structure species on the sounder. | No frequency / CHIRP / transducer-selection guidance for either species; the only sounder settings numbers in the KB are the DSL ones (Furuno TVG 55-57, ping ~15 of 20). | No arc-shape-to-fish-size read — nothing on grading fish size from mark thickness or arc length for either species. | No private-boat side-scan or horizontal search-sonar method for yellowtail or bluefin; the only search-sonar entry is a commercial sportboat's 400-600 ft side-to-side scan. | The KB carries the private-boat 0-120/150 ft manual-range doctrine and the bluefin 30-50 fathom sounded-school read without reconciling them; no note states how a private boat should resolve that.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

## Short version

They are different reads because they are different **problems**. Yellowtail are a *structure* mark — you read them against the bottom, mostly shallow, and the shape of the mark (balled vs. stratified, tucked vs. spread) tells you whether to fish at all. Bluefin are an *open-water suspended* mark — no bottom to read against, far deeper on average, and the depth number itself is what picks the jig weight. ([species/yellowtail.md](species/yellowtail.md), [species/bluefin-tuna.md](species/bluefin-tuna.md), [planning/electronics-and-sounder.md](planning/electronics-and-sounder.md))

Units note: the KB preserves numbers as spoken, so some bands are in fathoms and some in feet. 1 fathom = 6 ft ([planning/electronics-and-sounder.md](planning/electronics-and-sounder.md), `Rf1HKJG-SDg`, `9hEa3sGTh40`).

---

## Yellowtail on the meter

**Mark shape.** The classic yellowtail read is **arcs / boil-ups at ~5–10 fathoms (30–60 ft) near structure**, and **tight balls hugging the structure** on hard bottom, pinnacles and high spots — "we see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`). Under a kelp paddy showing no surface activity, look for **boomerang-shaped arcs around 90–120 ft**, and give the paddy about a minute or two before writing it off (`ZFqe49jRgA0`, Dave Hansen, 2019-05-26). ([species/yellowtail.md](species/yellowtail.md))

**Depth bands, and what each one means for technique:**

| What you're seeing | Depth | What it says to do |
| --- | --- | --- |
| Fish metering but not showing on top | **40–60 ft** | The "they're coming up" read — **rules out the yo-yo**. Stay on light bait and casting; go all-in on surface iron once they boil (`0DKmYId1NN4`, Strictly Irons, 2026-03-21, SoCal private boat — unregistered channel, medium) |
| Arcs / tight balls on hard structure | **~5–10 fm (30–60 ft)** | Yo-yo iron first, dropper loop second; 40–60 lb class stout rod + high-ratio reel, full-size Salas 6X-class iron, hit bottom then **a couple cranks off the bottom = reaction bite** (`D5DR7Kx42_A`) |
| Boomerang arcs under a dry-looking paddy | **~90–120 ft** | Work it briefly, then move (`ZFqe49jRgA0`) |
| Fish on squid, feeding right off the bottom (San Benito) | **30–40 fm (180–240 ft)** — spoken variously as "30, 40, 50" and "30, 35" | Dropper loop and yo-yo iron; squid had moved out of the shallows and the yellows moved with them — a bait-migration depth, not a fixed structure depth (`JaKSGkZ6CAc`, medium) |
| Marks on a high spot (BOLA / Baja) | **150–300 ft**, stacked on the **up-current face** | Slow-pitch / vertical jigging, 130–250 g; bit best **150–180 ft** (`vqsD0qpwcJA`; single-trip source, medium) |

**Shape beats depth for yellowtail.** Two reads the KB carries that have no bluefin equivalent:

- **Stratified vs. balled.** Marks running as **lines from the bottom up through mid-column, sometimes all the way to the surface** = fish actively hunting bait → put slow-trolled baits out. A **ball stuck to the bottom** = fish present but not hunting → dropper-loop water, not flyline water (`HTowqnwAMeA`, Nate Winnicki, BDOutdoors — medium).
- **High and spread = biting; tucked to the bottom = not.** Watched over a small rock roughly **20–30 ft across**, fish up in the column and spread out are the ones that eat (`HTowqnwAMeA`, second angler named only as "Marshall" — medium).

**Two bottom-reading cues that are specific to yellowtail:**

- **Hard bottom only, never mud.** Structure yellows sit exclusively on hard/rocky bottom — read bottom hardness by return thickness (thin, faint line = sand/mud; thick and dark = rock) to decide whether the spot is even worth working before you look for fish sign (`6DzbsElGE7E`, Dave Hansen, 2021-04-13). ([species/yellowtail.md](species/yellowtail.md), [planning/electronics-and-sounder.md](planning/electronics-and-sounder.md))
- **A thin, lighter mark riding higher than the bait ball can be the yellowtail itself**, pushing bait up off the rocks — that's the sign to commit the anchor, not the bait pile alone (same source).

**And the payoff for a mark that never shows:** schools located on the sounder that "don't come up and boil around" still get bit reliably once a jig reaches their metered depth — "just about every lure that makes it down to the depth that fish is, is a bite," with yo-yo iron said to have "absolutely" out-fished live bait "multiple times" in exactly that scenario (`tpmOYXYQwhU`, SearcherSportfishing, 2020-04-21 — medium). A related pivot: fish still marking but gone quiet **on the anchor** means get up above the marks and **drift through them** (`97clKtVsEOs`, San Benito, medium; also [planning/electronics-and-sounder.md](planning/electronics-and-sounder.md)). And when the sounder shows fish holding down while some anglers get bit up top, alternate surface iron and yo-yo on the same drift (`ecJPMTCi-gw`, San Clemente, 2019-06-19, medium).

---

## Bluefin on the meter

**The core read: sounded deep, no surface sign, wind up.** "God forbid there's no foamer, you're going over a lot of fish and there's a lot of wind — that's when those fish sound down, you're looking **30, 45, 50 thousands**" — i.e. **30–50 fathoms (180–300 ft)** — and you need the power on the meter to reach and grade them (`HWx1jDTGsng`, Capt. Duane Diego Mellor; carried as high-confidence doctrine in [species/bluefin-tuna.md](species/bluefin-tuna.md)). **That is a meter-and-jig situation, not a troll situation.** Technique: knife-jigging to graded marks, 100–130 lb braid jig class (PE6–8), **150–300 g by day; 300–400 g in more current or deeper** to punch down and still stay horizontal in the strike zone.

The KB then keeps a spread of **side-by-side depth data points rather than one number** — deliberately not reconciled:

| Situation | Depth on the meter | Source |
| --- | --- | --- |
| Sounded schools, wind, no surface sign | **30–50 fm (180–300 ft)** | `HWx1jDTGsng` |
| Overnight jig session, Cortez/Tanner Bank | marks **360° around the boat, 50 fm down to 80 fm (300–480 ft), even below** | `LsFMBCa9DOQ`, Aug 2024, medium |
| Night, ~20 mi off San Diego | **240–360 ft** — the stated reason a flat-fall/knife jig needs to be **250 g or greater** (120–150 g won't get there fast enough, especially drifting in wind) | `eehDVb6_GoI`, 2021-06-30, medium |
| Night bite on the DSL | depth-called marks — **"fish at 180, fish at 230 ft"** — drop straight down onto them | `nRFFM8DT-og` |
| Night, backside San Clemente | school **stacked ~198 ft down to 330 ft** | `r4J5nP5Bkl4`, June 2023, medium |
| Catalina west end, day | marks at **120 ft**, then a "really good mark… solid" at **150 ft** | `M7BtON4GZgQ`, Aug 2020, medium |
| Shallow marks, fast jig hookup | **60–80 ft** (hooked up after ~two cranks); also ~**100 ft moving up and down all around the boat**, and ~**150 ft** | `cLYqjT7ddl8`, medium |
| Drift bite, fish off the top | **50–100 ft** — butt-hook a sardine and let it swim down to them, long soak | `8THSuqoPI_Q`, 2015-09-26, offshore Catalina, medium |
| Anchored on a kelp paddy | bluefin marking **80–150 ft**, worked with butt-hooked and sinker-rigged live bait | `IwxqgocsQTY`, 2015-10-29, medium |
| Surface signs sink out after the motor spooks them | captain marks them at **120–140 ft** → switch from sinker rig to knife/vertical jigging | `gimFbgN5Jjk`, 2025 PCS Show, medium |
| Big fish marked deep, captain calling depth | bite zone **~100–200 ft**; free-spool to the mark, most bites **on the fall**, wind back about halfway and re-drop | `an_uw-5pjfw`, Capt. Art Taylor, medium — [techniques/flat-fall-jigging.md](techniques/flat-fall-jigging.md) |
| Shallow bait-ball marks while chumming sardines | **~60 ft** → yo-yo iron through/around the mark, crank fast; a heavy bite on the drop reads as the rod going dead-weight, "almost like stuck on the bottom" | `ntQXxcH5sjI`, Tanner Bank, 2024-08-29, medium |

**Bluefin mark shape.** The KB's shape cue for tuna is a **large, distinct upside-down-U-shaped mark** — but that's a *range-setting* artifact as much as a fish shape: on a properly capped manual range the school paints that way; left on auto over 2,000–3,000 ft of water, the same school (Hansen: "10 tons of bluefin sounded through") shrinks to a barely visible speck or doesn't show at all (`9hEa3sGTh40`, `8XrMkWPRxgs`, `m-M0iwX8DjA` — [planning/electronics-and-sounder.md](planning/electronics-and-sounder.md)). The other bluefin-specific screen cue is **bait shape**: broken, harried, moving bait holds predators; a solid unbroken wall usually does not ([species/bluefin-tuna.md](species/bluefin-tuna.md)).

**The night difference.** Bluefin have a mechanism yellowtail don't: the **deep scattering layer** sits **600+ ft down by day and rises toward the surface at night**, and the deep sonar-school fish that were unreachable by day come up the column after dark — that's why the night jig bite works ([conditions/deep-scattering-layer.md](conditions/deep-scattering-layer.md)). Mechanism is kept as two side-by-side reads: the corpus read is **food-following**; Cameron's read is that the night jig bite is **likely a reaction bite** (flagged *likely, not measured*).

---

## Head to head

| | Yellowtail | Bluefin |
| --- | --- | --- |
| **Where the mark sits** | On/near structure — hard bottom, pinnacles, high spots; also under paddies | Suspended in open water over 2,000–3,000 ft of bottom; also under paddies |
| **Typical mark** | Arcs / boil-ups; **tight balls hugging structure**; a thin lighter mark above the bait ball | Large **upside-down-U** school on a capped manual range; graded marks with no bottom reference |
| **Bread-and-butter depth** | **~5–10 fm (30–60 ft)** on structure; 40–60 ft = "coming up" | **30–50 fm (180–300 ft)** sounded, wind up, no surface sign |
| **Deep end** | 150–300 ft on Baja/BOLA high spots; 30–40 fm on squid | 50–80 fm (300–480 ft) at the banks; 198–360 ft at night |
| **Shallow end** | 40–60 ft "they're coming up" | 50–100 ft drift fish; 60–80 ft bait-ball marks |
| **Bottom matters?** | **Yes — decisive.** Hard bottom only, never mud; grade the bottom before you grade the fish | No bottom to read against; the called depth *is* the reference |
| **What the shape tells you** | Stratified = hunting (slow-troll); balled on bottom = dropper loop; high + spread = biting, tucked down = not | Shape mostly tells you the machine is set right; bait shape (broken vs. wall) is the predator cue |
| **Night behavior** | Not covered in this KB | Rises with the DSL — that's the whole night fishery |
| **Technique the depth picks** | 40–60 ft → light bait/surface iron (no yo-yo); 5–10 fm → yo-yo/dropper loop; 150–300 ft → slow-pitch 130–250 g | 60 ft → yo-yo; 100–200 ft → flat-fall; 30–50 fm → knife jig 150–400 g; ≥240 ft → jig **must** be 250 g+ |

---

## Set the machine differently for each

This is the part that actually changes what you see:

- **For bluefin (open water):** get off auto. A private boat's working manual range is **0–120 ft on older machines, 0–150 ft on newer ones**, regardless of the real bottom (`9hEa3sGTh40`, `8XrMkWPRxgs`) — the stated reason is bait budget: you can't chum a school up from 250 ft the way a sportboat holds fish from 30 fathoms. For bluefin specifically, **0–300 ft** is the window (`m-M0iwX8DjA`), with the stated reason to stop there being that fish **below 300 ft are traveling, not biting**, while fish in the 300-ft-to-surface band are the eager ones. Once a mark shows in that band: **hit the GPS mark button, run past, turn around, and troll back over it** with a Mad Mac. Separately, for shallow schools under dolphin in deep water, set a manual **0–150 ft** window or the machine keeps hunting a bottom that's far deeper and the shallow marks never paint (`SgF5hRlEGqU`).
- **For yellowtail (structure):** size the manual range so **the bottom sits mid-screen, not pinned at the edge** — a 15 ft spot gets a 30 ft range, a 25 ft spot (most SoCal harbors run 15–25 ft) gets a 40 ft range (`FEXgl0eQCa8`). That leaves room above the bottom return to read hard vs. soft and to pick fish and bait out of the column. Practice the hard/soft and fish-vs-kelp discrimination **in the harbor**, not on the fuel-burning offshore trip (same source).
- **For the DSL / night bluefin:** **gain/TVG up** (Furuno ~55–57, mid-to-high on other brands) and **ping speed slowed** (~15 of 20) so the layer paints as a distinct band ([planning/electronics-and-sounder.md](planning/electronics-and-sounder.md), [conditions/deep-scattering-layer.md](conditions/deep-scattering-layer.md)).
- **Two things that will fool you either way:** backing down (e.g. holding position while the anchor pays out) puts air under the hull and **blanks the bottom return** — that's aerated water, not a broken machine (`HGyL7pXy3Ts`); and **sea state limits how shallow you can read** — in chop the cone has to be shot lower, so a fish high in the column won't show until you're right on top of it (`fgTmUq78ofQ`). A searching sportboat wheelhouse runs to about **80 fathoms (480 ft)** and watches the whole band, which the KB keeps side by side with the private-boat 0–150/0–300 ft rule rather than reconciling them.

**Grading discipline, both species:** don't stop on a mark you can't grade — every stop burns bait and time. Idle on, keep running and stack the picture depth by depth, and only commit when it grades out ([planning/electronics-and-sounder.md](planning/electronics-and-sounder.md), [planning/search-and-glassing.md](planning/search-and-glassing.md)). For yellowtail specifically: grade with **repeated passes over the same track**, then drop the anchor in the **sand beside the rock**, not on it, so your lines go back to the structure (`6DzbsElGE7E`). And present to where the mark actually is — told the meter is marking 30 ft down under the boat, the reflex to cast far away puts the bait outside the zone (`bM2vUS1B-yQ`).

**On the drop:** when a depth is called with no bottom reference, **get the jig a little deeper than the called depth, then wind up through the school at full speed** (`RNRFrfepiW0`, Steve Carson — [techniques/yo-yo-iron.md](techniques/yo-yo-iron.md)). Yo-yo depth on overnight/multi-day trips commonly runs **120–240 ft**: 150–250 ft wants a full-size 6X-class iron, shallower wants a smaller iron (6X Jr / Tady 40 class); 40 lb line minimum, 50–60 lb preferred (`UP_3fBu7VPA`, medium). Note also that **line-out is not true depth** once you're drifting — the jig trails out behind, so actual depth runs shallower than the footage paid out ([techniques/flat-fall-jigging.md](techniques/flat-fall-jigging.md)).

---

## What this KB does not tell you

- **It gives no rule for telling a yellowtail mark from a bluefin mark by the mark itself.** Every discrimination above is *contextual* — depth band, hard structure vs. open water, association with a paddy or with the DSL. The only species-ID-by-screen content in the KB is a historical note that flasher-era operators learned to tell species apart by how a mark flashed (`Rf1HKJG-SDg`); the actual rules are not carried.
- No transducer **frequency** guidance (50 vs 200 kHz, CHIRP band selection) for either species.
- No **arch size / thickness → fish grade** rule (nothing on reading a 20 lb vs. a 40 lb yellowtail, or a 100 lb bluefin, off the mark).
- No numeric **gain / target-separation** settings other than the DSL numbers above.
- Nothing on **forward-facing or side-scan** (LiveScope-type) imaging for either species; the only horizontal-sonar content is a sportboat search sonar run **400–600 ft side to side** with an audio cue that changes when it hits fish (`nkJNzdNlm_c`, medium), and that is not species-specific.
- **No night/DSL sonar signature for yellowtail** — the DSL material is bluefin and swordfish only.
- **No bottom/structure sonar signature for bluefin** — every bluefin mark in the corpus is open-water suspended or paddy-associated.

Confidence caveat worth carrying: the two anchoring numbers — yellowtail arcs at ~5–10 fathoms on structure, bluefin sounded at 30–50 fathoms — are the high-confidence doctrine. Most of the individual depth data points in the tables above come from unregistered channels or single mentions and are logged at **medium** confidence, which is why the KB keeps them side by side as a spread rather than averaging them into one number.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `planning/search-and-glassing.md`, `species/yellowtail.md`, `species/bluefin-tuna.md`, `conditions/deep-scattering-layer.md`, `techniques/yo-yo-iron.md`, `techniques/flat-fall-jigging.md`  
*videos:* `D5DR7Kx42_A`, `vqsD0qpwcJA`, `ZFqe49jRgA0`, `6DzbsElGE7E`, `0DKmYId1NN4`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `JaKSGkZ6CAc`, `97clKtVsEOs`, `ecJPMTCi-gw`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `eehDVb6_GoI`, `nRFFM8DT-og`, `r4J5nP5Bkl4`, `M7BtON4GZgQ`, `cLYqjT7ddl8`, `8THSuqoPI_Q`, `IwxqgocsQTY`, `gimFbgN5Jjk`, `an_uw-5pjfw`, `ntQXxcH5sjI`, `Rf1HKJG-SDg`, `9hEa3sGTh40`, `8XrMkWPRxgs`, `m-M0iwX8DjA`, `FEXgl0eQCa8`, `SgF5hRlEGqU`, `fgTmUq78ofQ`, `HGyL7pXy3Ts`, `bM2vUS1B-yQ`, `nkJNzdNlm_c`, `RNRFrfepiW0`, `UP_3fBu7VPA`  
*gaps admitted:* No rule anywhere in the KB for distinguishing a yellowtail mark from a bluefin mark by the mark's own appearance — all discrimination carried is contextual (depth band, structure vs. open water, paddy/DSL association). | No transducer frequency guidance (50 kHz vs 200 kHz, CHIRP band selection) for either species. | No arch-size / thickness to fish-grade rule — nothing on estimating fish size (20 lb vs 40 lb yellowtail, 100 lb bluefin) from the mark. | No numeric gain or target-separation settings beyond the DSL settings (Furuno TVG/gain ~55-57, ping ~15 of 20). | No forward-facing or side-scan (LiveScope-type) imaging content for either species; the only horizontal-sonar entry is a sportboat search sonar run 400-600 ft side to side with an audio cue, not species-specific. | No night / deep-scattering-layer sonar signature for yellowtail — the DSL material covers bluefin and swordfish only. | No bottom- or structure-oriented sonar signature for bluefin — every bluefin mark in the corpus is open-water suspended or paddy-associated.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short version

They are two different *kinds* of read. Yellowtail are a **structure-referenced** mark — you read them against the bottom, and mostly shallow (30–60 ft over rock, out to 150–300 ft on deep Baja/Cortez high spots). Bluefin are an **open-water suspended** mark — you read them against a manually-set range window with no bottom in the picture at all, and the working band is far deeper (180–300 ft typical, 300–480 ft at the banks and at night).

The KB is explicit that the general meter method lives in [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md) and the species-specific signatures live in the species routers ([`species/yellowtail.md`](species/yellowtail.md), [`species/bluefin-tuna.md`](species/bluefin-tuna.md)). Fathom conversion throughout: 1 fathom = 6 ft (`HGyL7pXy3Ts`).

---

## Yellowtail on the meter

**Shape.** Tight balls hugging structure — arcs and boil-ups near pinnacles and high spots ([`species/yellowtail.md`](species/yellowtail.md), `D5DR7Kx42_A`). Under a kelp paddy the shape is different: **boomerang-shaped arcs** (`ZFqe49jRgA0`).

*Honesty flag from the KB itself:* the note carries a `⚠ Fact-check (contradicted-by-source)` on that first row — `D5DR7Kx42_A` supports only "tight balls of yellowtails sometimes hugging the structure" and carries **no depth figure, no fathoms, no "arcs" or "boil-ups"**. So take the shape language as solid and the 5–10 fathom number as KB-internal rather than sourced.

**Depth bands the KB actually logs:**

| Read | Depth | What it means |
| --- | --- | --- |
| Structure fish on hard bottom / pinnacles | **~5–10 fathoms (30–60 ft)** — flagged above | Yo-yo iron first, then dropper loop; 40–60 lb class stout rod + high-speed reel (`D5DR7Kx42_A`) |
| Fish metered but not yet showing | **40–60 ft** | They are *staging up* — surface-iron and light-bait fish, **not** yo-yo fish; when they boil, go all-in on the iron (`0DKmYId1NN4`) |
| Under a kelp paddy with no surface activity | **90–120 ft**, boomerang arcs | Paddy fish often don't meter at all — check fast (look, one bait, sonar under the kelp), but give it a minute or two before writing it off (`ZFqe49jRgA0`) |
| Cortez Bank high spot, incoming tide | **60–80 ft in 120 ft of water**, fish 20–40 lb | Flylines, J-hooks, surface iron, yo-yo all worked (`UfuiWFVvz2E`, [`species/evidence/yellowtail.md`](species/evidence/yellowtail.md)) |
| Deep Baja high spots (BOLA) | **150–300 ft**, bit best **150–180 ft** | Slow-pitch/knife jigs 130–250 g to punch current (`vqsD0qpwcJA`) — the KB flags this as a **single-trip data point**, and that 150–300 was a pre-trip expectation against a fished 150–180 ft |
| San Benito, squid pushed out of the shallows | **30–40 fathoms (180–240 ft)** — spoken on camera as "30, 40, 50 fathoms" and preserved unsmoothed | Feeding right off the bottom, not up top; nearly every fish had fresh squid in its stomach (`JaKSGkZ6CAc`) |
| Offshore tuna pens | straight down **~120 ft** | Logged but **demoted from the router table** as a single observation, not a standing situation (`Ob45hK4HSWc`) |

**The bottom itself is half the read.** Grade the bottom before hunting fish sign: **thin, faint return = sand/mud; thick, dark return = rock — and the fish hold on rock, never mud** (`6DzbsElGE7E`). That works on any brand, no discrimination mode needed. Also run the hard/soft *seam*, not just the high spot — those transitions are travel and feeding highways (`yLpDI8jnizU`, `11npFUPOJKU`).

**Shape and spread = feeding state, not just position.** This is the yellowtail-specific read the KB is proudest of ([`species/yellowtail.md`](species/yellowtail.md), `HTowqnwAMeA`):

- **Stratified lines from the bottom up through mid-column**, or fish sitting high and spread over a small rock (**~20–30 ft across**) → they are **hunting**. Slow-trolled and flylined baits.
- **Balled tight to the bottom** → present but **not feeding**. Dropper-loop water, worth a yo-yo burned past for the reaction strike — but a bottom-hugging ball is not a wide-open bite waiting for a good angler. (`tpmOYXYQwhU` is flagged here: it contains no bottom-balled school and no burned yo-yo.)

**Fish mark vs bait mark.** A thin, lighter mark riding *above* a bait ball can be yellowtail pushing bait up off the rocks (`6DzbsElGE7E`). The KB flags that the source actually inverts the anchor trigger — the bait pile is what commits the anchor, and the anchor goes into the *sand*, not onto the rock.

**Three live plays off a yellowtail mark:**
- Metered but not showing → **chum-then-cast**: meter the school, throw live chum, let them boil, cast into the boil. The long cast is load-bearing — they won't let the boat drive over the top of them (`4pT0efBD1j0`, `dS9gd9k7A7Q`, [`species/yellowtail-coronado-islands.md`](species/yellowtail-coronado-islands.md)).
- Still marking at anchor but not responding → **pull off the hook and drift over them**; the extra motion restarted a bite anchoring had killed (`97clKtVsEOs`, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)).
- Hard wind (the source's unitless "pushing 25") after a run of surface days → fish are still metered, just no longer on top; the fleet bite goes mostly yo-yo, iron still picks (`ejUTAnONf7o`).

---

## Bluefin on the meter

**Shape.** At a correct manual range a bluefin school paints as a **large, distinct upside-down-U-shaped mark**. Left on auto with the bottom set to the real (2,000–3,000 ft) depth, that same school shrinks to a barely visible speck (`8XrMkWPRxgs`, `9hEa3sGTh40`). At the banks at night, marks read **360° around the boat** (`LsFMBCa9DOQ`). That is the whole descriptive vocabulary the KB gives for bluefin mark morphology — there is no arc/boomerang shape language on the bluefin side.

**Depth bands ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)):**

| Read | Depth | What to do |
| --- | --- | --- |
| Sounded schools, wind up, no surface sign | **30–50 fathoms (180–300 ft)** (`HWx1jDTGsng`) | Meter-and-jig, not a troll — you need sounder power to reach and grade them |
| Offshore-bank night marks, 360° around the boat | **50 to 80 fathoms (300–480 ft), even below** (`LsFMBCa9DOQ`) | Bank-specific extension of the row above, not a replacement |
| Night, 20–30 mi off San Diego | **240–360 ft** (`eehDVb6_GoI`) | Sets a **250 g or greater** jig floor — 120–150 g will not reach in a wind drift |
| Night bite, depth-called marks | **180 and 230 ft** (`nRFFM8DT-og`); a school stacked **198–330 ft** (`r4J5nP5Bkl4`) | Drop straight down onto the called depth |
| Daytime open-water marks (~25 mi off, Clemente/Catalina) | **60–80 ft, ~100 ft, ~150 ft** (`cLYqjT7ddl8`); **120 ft then 150 ft** off Catalina's west end (`M7BtON4GZgQ`) | Jig straight down; a bite can come within two cranks |
| Fish off the top on an offshore drift | **50–100 ft** (`8THSuqoPI_Q`) | Butt-hooked sardine swum down, long soak |
| Shallow bait-ball marks near the boat | **~60 ft** (`ntQXxcH5sjI`) | Yo-yo through or around the mark; a heavy bite reads as the rod going dead-weight, "almost like stuck on the bottom" |
| Kelp-paddy marks | **80–150 ft** (`IwxqgocsQTY`) | Flagged: that stop was drifting, not anchored, and the marks were not species-tagged (yellowfin were landed there) |
| Fish sink out when the motor pushes them off the top | captain marks them at **120–140 ft** (`gimFbgN5Jjk`) | Switch off the sinker rig to vertical jigging |

**The 300 ft rule.** A **0–300 ft manual window is why the offshore bluefin read works at all**: on auto over 2,000–3,000 ft of water the screen reads zero at the top and the real bottom at the edge, and a sounded school compresses to nothing. Cap the range and it paints. **Fish below 300 ft are traveling, not biting; fish in the 300 ft-to-surface band are the ones eager to bite.** Once a mark shows in that band: hit the mark button, run past, turn around, and troll back over it with a Mad Mac (`m-M0iwX8DjA`, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)).

**The KB flags its own contradiction here**, and you should know about it before you plan a night: that "below 300 ft = traveling" doctrine sits against bluefin's own 240–360 ft night row and the 50–80 fathom bank row, and neither note acknowledges the other. Front-matter `sonar_depth` on the bluefin note also caps the night band at 330 ft while the table reaches 360 ft. Unreconciled in the KB — I'm not going to reconcile it for you.

**Night bluefin and the DSL.** The deep scattering layer sits **600+ ft by day and rises toward the surface at night**, lifting the bait and the deep sonar-school fish into reach ([`conditions/deep-scattering-layer.md`](conditions/deep-scattering-layer.md), `nRFFM8DT-og` — though the KB flags that this source never actually says "DSL," only captain-called depths of 180 and 230 ft). To **paint** the layer: push TVG/gain up (Furuno ~55–57, mid-to-high on other brands) and slow the ping speed to ~15 of 20 so the band builds as a distinct layer (`yMiBtZ7k8-w`).

---

## The differences that actually change how you run the boat

1. **What you read against.** Yellowtail: the bottom return — hard vs soft, and where the fish sit relative to structure. Bluefin: an artificial range ceiling you set yourself, with the bottom deliberately out of the picture.
2. **Range setting.** Yellowtail/inshore: bottom sits **mid-screen** — a 15 ft spot gets a 30 ft screen, a 25 ft spot gets 40 ft (most SoCal harbors run 15–25 ft) (`FEXgl0eQCa8`). Bluefin/offshore: **manual 0–120 ft on older machines, 0–150 ft on newer**, or **0–300 ft** for the sounded-school game (`9hEa3sGTh40`, `8XrMkWPRxgs`, `m-M0iwX8DjA`). Never auto in either case — that rule repeats across three sources (`9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`).
3. **Depth.** Yellowtail's core band is 30–120 ft; only Baja/Cortez high spots and squid-displacement situations push it to 150–300 ft. Bluefin's core band *starts* around where yellowtail's ends.
4. **What the mark tells you.** Yellowtail marks carry a **feeding-state read** (stratified/spread = hunting, balled to bottom = not feeding) that selects your presentation. Bluefin marks carry a **depth-and-reachability read** that selects your jig weight (250 g+ below 240 ft; 150–300 g by day).
5. **Practice where it's cheap.** Learn hard/soft bottom and fish-vs-kelp discrimination in the harbor with range mid-screen and gain dialed in — then leave the settings alone, go offshore, open the range to 0–300 ft, and apply the same skill to suspended tuna (`FEXgl0eQCa8`).
6. **Sea state caps both.** In flat water the cone shoots close to the surface and reads the whole column; in chop the cone tips and a fish holding high doesn't paint until you're nearly on top of it. A fixed transducer follows the roll and adds aerated-water noise; a gyro/roll-stabilized one stays aimed down (`fgTmUq78ofQ`, `ZIJAvAEW_tU`). The limit is described as still real on newer hardware.
7. **Bait budget governs the stop.** Stop only on marks you can grade — every stop on a no-name mark burns bait and time. And don't stop at the first bottom mark: keep running and stack the picture depth by depth (a worked example ran 20 ft → 40 ft → 60 ft, moving slowly) (`KjVLn4cWHbc`, `QP6c8vcslVs`).
8. **Photograph the meter during bites** to build your own library of what a paying mark looks like for each species (`yLpDI8jnizU`, `11npFUPOJKU`).

---

## What the KB does not answer

Worth saying plainly, because these are the questions you'd naturally ask next:

- **The KB gives you no way to tell a yellowtail mark from a bluefin mark on the same screen.** That's a real operational hole — at Cortez Bank the corpus has both species biting together on flylined sardines at the same stop (`nQvJnfb5jQ4`), and nothing in the KB says how to distinguish them on the meter. Depth is your only proxy, and the bands overlap at 60–150 ft.
- No target-strength, arc-thickness, or "grade the fish size from the mark" guidance for either species.
- No frequency, CHIRP, or beam-angle selection by species.
- No yellowtail night-sounder read at all, and no yellowtail relationship to the DSL.
- Nothing on what either species looks like on **side-scan/horizontal search sonar** — the 400–600 ft side-to-side scan range and the audio bite-cue are carried generically (`nkJNzdNlm_c`), never species-tagged.

And two integrity notes on the numbers above: the **yellowtail 5–10 fathom** figure is flagged in the KB as unsupported by the source it cites, and the **bluefin 300 ft "traveling not biting"** doctrine directly contradicts the KB's own 240–360 ft night rows without either note acknowledging the other.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `species/yellowtail.md`, `species/bluefin-tuna.md`, `species/evidence/yellowtail.md`, `species/evidence/bluefin-tuna.md`, `species/yellowtail-coronado-islands.md`, `conditions/deep-scattering-layer.md`  
*videos:* `D5DR7Kx42_A`, `6DzbsElGE7E`, `ZFqe49jRgA0`, `vqsD0qpwcJA`, `0DKmYId1NN4`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `JaKSGkZ6CAc`, `UfuiWFVvz2E`, `ejUTAnONf7o`, `97clKtVsEOs`, `Ob45hK4HSWc`, `4pT0efBD1j0`, `dS9gd9k7A7Q`, `nQvJnfb5jQ4`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `eehDVb6_GoI`, `nRFFM8DT-og`, `r4J5nP5Bkl4`, `cLYqjT7ddl8`, `M7BtON4GZgQ`, `8THSuqoPI_Q`, `IwxqgocsQTY`, `ntQXxcH5sjI`, `gimFbgN5Jjk`, `HGyL7pXy3Ts`, `9hEa3sGTh40`, `8XrMkWPRxgs`, `m-M0iwX8DjA`, `FEXgl0eQCa8`, `SgF5hRlEGqU`, `fgTmUq78ofQ`, `ZIJAvAEW_tU`, `yMiBtZ7k8-w`, `yLpDI8jnizU`, `11npFUPOJKU`, `KjVLn4cWHbc`, `QP6c8vcslVs`, `nkJNzdNlm_c`  
*gaps admitted:* No discriminator anywhere in the KB for telling a yellowtail mark from a bluefin mark on the same screen, despite the corpus documenting both species biting together at Cortez Bank (nQvJnfb5jQ4) and the depth bands overlapping at 60-150 ft. | No target-strength, arc-thickness, or fish-size-from-the-mark guidance for either species. | No frequency, CHIRP, or beam-angle selection guidance by species. | No yellowtail night-sounder signature, and no yellowtail relationship to the deep scattering layer. | No species-tagged read for side-scan / horizontal search sonar - the 400-600 ft side-to-side scan range and audio bite cue (nkJNzdNlm_c) are carried generically only. | No bluefin mark-shape vocabulary beyond 'large upside-down-U school at manual range' and 'marks 360 degrees around the boat' - no equivalent of the yellowtail arc/boomerang morphology. | No bluefin equivalent of the yellowtail feeding-state read (stratified vs bottom-balled); bluefin marks are graded by depth and reachability only. | The yellowtail ~5-10 fathom structure band is flagged in the KB itself as contradicted-by-source - D5DR7Kx42_A carries no depth figure, so the number is KB-internal rather than sourced. | The yellowtail 150-300 ft deep Baja high-spot band is a single-trip data point (vqsD0qpwcJA), and 150-300 was a pre-trip expectation against a fished 150-180 ft. | Unreconciled internal contradiction: planning/electronics-and-sounder.md states fish below 300 ft are traveling rather than biting, while species/bluefin-tuna.md carries 240-360 ft night marks and 50-80 fathom bank marks; neither note acknowledges the other. | Front-matter sonar_depth on species/bluefin-tuna.md caps the night band at 330 ft while its own table reaches 360 ft. | The DSL mechanism for the night bluefin bite is flagged unverifiable - nRFFM8DT-og never mentions the deep scattering layer, only captain-called depths of 180 and 230 ft. | The bluefin kelp-paddy 80-150 ft row (IwxqgocsQTY) is flagged: the stop was drifting not anchored, and the marks were not species-tagged.

</details>

### 15. [finding] What do terns, gulls and shearwaters each tell me when I see them working?

**Winner:** NOW · mapping {'A': 'B3', 'B': 'B2', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 1 | 2 | 2 | 2 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three get the core axis right (behavior, not presence) and none fabricates or states a regulation, so the split is on mechanism, caveats and gap honesty. C wins because it explains why each read works (bait under predation looks down, so a locked dive-line means nothing is pushing it; a raft is waiting for tide to lift deep bait), carries the KB's own single-source flags into the answer instead of laundering them (the 72F figure is that day's water temperature, not a threshold; the 20-30 ft hopscotch and the 4-5 mi radar envelope each rest on one transcript), and names the internal contradiction over whether terns are Coronados-scoped. A is a very close second with the widest coverage and a clean gaps list, but it repeats the 72F number without the caveat and pads with lens tint and dolphin-pod material that is off the question. B is the tightest read and adds genuinely useful paddy-qualification detail, but it drops the two best tern actionables the others keep - cast under the bird at the instant of the dive, and the mechanism that makes the locked-versus-moving call trustworthy.

- *B2 reasons:* found: all three birds answered cleanly, but it omits the two most useful tern reads the other two carry - cast under the bird the instant it dives, and the mechanism (bait under pressure looks down) that makes the locked-dive read trustworthy. specific: adds paddy qualification the others mostly skip (boomerang arcs 90-120 ft, one to two minutes), jacuzzi foamer taxonomy, 209 bank, 72F, 16-18 mph contour runs. sourced: consistent note paths plus ids; radar again attributed to yLpDI8jnizU; the notes_used list includes several notes nothing in the answer visibly draws on. scoped: Cedros marked Baja, kelp/island vs open-water break distinction kept, no regulations asserted. honest: flags Cameron's shearwater blind spot, the single 2022 source, and eight real gaps including gull 'locked in' having no duration test; no relative time. actionable: tightest of the three to act on - run, stop, cast, budget, then qualify the paddy - just missing the under-the-bird cast.
- *B3 reasons:* found: covers all three birds plus mixed piles, pelicans, cormorants, and the run-to execution; broadest sweep, though it drifts into lens tint and dolphin-pod tells that are only loosely on-question. specific: 25 kt to neutral, 2-3 casts, 20-30 ft hopscotch, 0.5-1 mi / ~2 mi / 4-5 mi ranges, 3-4 min scans, 72F, 10-15/20/25 lb grades. sourced: every claim carries a note path plus video id (Blh2BA-7Ono, JiJYamo0QHk, A6DJoXbID4c, SczdZIq3UmE, lf3S28nh-kk) and the numbers match the notes; radar is attributed to yLpDI8jnizU rather than the demo id, a minor slip. scoped: SoCal Bight material kept separate, Cedros explicitly labeled baja-pacific-north, no regulatory claims made. honest: names the shearwater doctrine as single-source, Cameron's model empty as of 2026-08, absolute dates throughout, seven concrete gaps; presents the 72F reading without the KB's 'not a threshold' caveat. actionable: full run-and-gun sequence, swing-wide variant, drive-through test, glassing protocol and detection ranges - a day is runnable from it.
- *NOW reasons:* found: hits every element of the question and adds the mechanism behind each read (bait looks down; shearwater rafts wait on tide to lift deep bait), plus the KB's own scoping contradiction on terns at the Coronados. specific: same hard numbers as the others (25 kt to neutral, 2-3 casts, 20-30 ft, 0.5-1/2/4 mi, 3-4 min, 4-5 mi radar, 100-500 ft off the beach) and correctly attributes the radar demo. sourced: note paths and ids line up with the notes verbatim, including the evidence file split; only slip is calling the Coronados tern flag 'contradicted-by-source' where the note says contradicted-internal. scoped: Cedros called out as Baja not SoCal, kelp/structure vs open-water exception preserved, no regulatory claims. honest: carries the KB's inline single-source warnings forward - 72F is that day's temp not a threshold, the 20-30 ft hopscotch and 4-5 mi radar rest on one source each - and its ten gaps are the sharpest (no timing for the drive-through circle-back, no fishing mechanics for a confirmed raft). actionable: foamer execution, drive-through probe, glassing protocol, ranges, and the up-current chum read at anchor.

<details><summary>Full prompt</summary>

What do terns, gulls and shearwaters each tell me when I see them working?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short version

Don't ask "are there birds?" — ask **"are they on bait, or on bait being pushed by fish underneath?"** Read *behavior*, not presence (`conditions/bird-reading.md`). Terns answer that question best, shearwaters answer it for fish that are deep, and gulls mostly answer a different question (is there life / floating kelp here?).

---

## Terns — the bird you run on

Both voices in the KB agree terns are the best bird — the BD corpus (`Blh2BA-7Ono`, SoCal Bight report 7/21/22) and Cameron's own model (`cameron`, stated 2026-08-03) (`conditions/bird-reading.md`).

The read is the shape of the dive pattern:

- **Locked-in repeated dives on one spot = bait only.** Skip it.
- **A moving dive-line = bait being pushed by fish underneath.** That is the one to run on. (`Blh2BA-7Ono`, via `conditions/bird-reading.md`)

Finer-grained layer on top of that, from on-camera coaching offshore of San Diego on a bluefin paddy (StokedOnFishing, `A6DJoXbID4c`, 2016-10-06 upload; unregistered channel — medium confidence): **read the individual bird, not just the flock** — "watch their head, watch how they look, watch the little reactions in the bird." And a state read the moving-vs-locked rule doesn't give you: **birds actively diving/working = the school is feeding on the surface; birds off the fish = the school is still there but "puddling"** (present, not surface-feeding) rather than gone. The KB keeps that beside the dive-line rule, not as a replacement (`conditions/bird-reading.md`).

Practical notes:
- It's the **white terns** specifically that a new-to-tuna angler should be hunting — "not pelicans and not seagulls... they do help but... it's the white terns" (StokedOnFishing, `SczdZIq3UmE`, 2019-10-02, offshore SoCal near the **209 bank**; that day's water was **72 °F** and the boat put yellowfin of **10–15 lb, ~25 lb and ~20 lb** on the deck) (`conditions/bird-reading.md`, `species/yellowfin-tuna.md`).
- **Cameron will almost always stop and cast on working terns, and offshore he'll follow terns around to find fish even with no other birds working** (`cameron`) (`conditions/bird-reading.md`, `planning/search-and-glassing.md`).
- Terns are the key bird on the **bluefin** router too — same moving-dive-line rule, paired with foamer taxonomy where a **"jacuzzi" (solid circular whitewater) ≈ a bite every cast** and spread-out directional feeders are picky (`species/bluefin-tuna.md`). Terns also mark **yellowfin** (`species/yellowfin-tuna.md`), **skipjack** (`species/skipjack-tuna.md`) and **yellowtail** (`species/yellowtail.md`).

**What to do when you find them** (`techniques/foamer-casting.md`): run at the working terns fast, set up **ahead of the school's direction of travel**, **stop hard — 25 knots straight to neutral** — and cast immediately, as close to the **middle of the foam** as you can reach. Budget **2–3 casts per school**, then move; foamers are short-lived, do not stake one out. Cameron's version is the same run-and-gun at working terns, ~2–3 casts per school, smaller presentation (Colt-Sniper class) out-fishing bigger, timed around **slack tide** (`cameron`) (`species/bluefin-tuna.md`). A stealthier variant for a school still travelling: guess the direction off the terns, **swing out and around** so you come to rest ahead of it, shut down and let them come into casting range (`A6DJoXbID4c`).

## Shearwaters — the deep-fish bird

This is corpus doctrine (`Blh2BA-7Ono`, 7/21/22). Worth flagging: **Cameron doesn't factor shearwaters in at all as of 2026-08**, and the KB carries this specifically as the gap his model wants filled (`conditions/bird-reading.md`).

- **Rafted (sitting in a group)** = sitting over **deep bait, waiting for the tide**.
- **The drive-through test** — run the boat through the raft: **circle straight back = fish under them; scatter and land elsewhere = bait only.** This is the single most useful thing on the list, because it converts an ambiguous sit into a yes/no.
- **Rafts hopscotching 20–30 ft at a time = tracking deep fish.** Follow the hopscotch.
- **Racing off low in one direction from a boil** = they are running to the **head** of the school. Follow them — **the old boil is the tail.**

Related, and it matters when nothing is flying: **birds sitting still on the water still mark the zone.** Trolling past sitting birds and hopscotching rafts produced immediate bites when nothing was in the air (`HzE4FHHcvTk`, 8/17/22 report) (`conditions/bird-reading.md`).

## Gulls — a life meter and a paddy-finder, not a fish finder

Both voices land in the same place from opposite directions (`conditions/bird-reading.md`):

- **Corpus:** unreliable — **"parking-lot birds."** Only meaningful when **locked in at islands / kelp edges** with nothing better around (`Blh2BA-7Ono`).
- **Cameron:** **"good sign but dumb"** — a general measure of life in an area, and his **paddy-finders** (`cameron`).

So: gulls tell you there's **life and floating kelp**, not that gamefish are under them. Use them as search infrastructure — on a paddy program, gulls are reliable for **locating floating kelp even when they aren't marking gamefish** (`conditions/kelp-paddies.md`). Then qualify the paddy itself: look in the water, check the fathometer for **boomerang-shaped arcs, typically 90–120 ft** down, give it **about a minute, maybe two**, and move (`ZFqe49jRgA0`, 2019-05-26) (`conditions/kelp-paddies.md`).

Inshore, a gull locked to a **kelp edge with nothing better around is worth checking** for calico — but **cormorants diving *in* the kelp** (= actively feeding = bass below) is the better inshore tell (`species/calico-bass.md`). On riprap/jetties, **birds sitting on the rocks mark the "thumb-over-hose" current deviation** — a cluster parked on one stretch of wall is sitting where the break concentrates bait; that's your spot on the rock line (`bydQzE3F9yM`/`jTXIr9O6zYk`) (`locations/breakwalls-jetties-riprap.md`).

One observed counter-data-point, so you don't write gulls off completely: at Cedros Island, Baja, a session closed with a roughly **30-minute blitz under gulls "going bonkers," including a triple hookup**, after the crew had already called the day done (StokedOnFishing, `6EDQtQHEwFE`, October 2024 trip, 2025-03-07 upload; unregistered channel — medium confidence) (`species/yellowtail.md`). That's an observation, not a rule — the doctrine above still stands.

## Three things that change how you read all three

- **Mixed piles** (gulls + pelicans + terns + cormorants) at **open-water current breaks = bait only — skip** (`Blh2BA-7Ono`). **Exception:** a mixed pile **on kelp/structure** can be a real bait event worth a look — e.g. the grunion blitz that produced every-cast bass in ugly water (`OYOda6T3f-8`, 10/20/22) (`conditions/bird-reading.md`).
- **Pelicans are the anti-signal.** Corpus: worthless as a gamefish indicator. Cameron: **"dirty birds"** — diving pelicans usually mean he's in the **wrong area**, and casting there typically produces **mackerel** (so they're a useful *bait* tell) (`conditions/bird-reading.md`).
- **Give each bird 30–40 seconds before you judge it.** Glass from a full stop or bow into the swell at **~1 kt**, scan **360° in small increments over 3–4 minutes**, and **watch a bird 30–40 seconds** — one glimpse won't tell you whether the dive-line is moving or the raft is tracking (`DnSqw4r7A1s`, 7/14/22 + `E4vKwRaRueA`) (`planning/search-and-glassing.md`).

## Detection ranges (so you know what you can even see)

From `planning/search-and-glassing.md`: from **deck level** you'll pick up a **few terns at ~0.5–1 mi** and a **big bird spot at ~2 mi**; from a **hardtop**, birds carry to **~2 mi** and dolphins to **~4 mi**. Space glass stations **3–4 mi apart**. Along a bank, run the contour at **16–18 mph** with a lookout **~30° off each bow**. Bird radar (Duane Diego Mellor, `yLpDI8jnizU`): gain near max, **range 4–5 mi**, bird schools paint as **red blotches**, sometimes boat-sized — that 4–5 mi is the working envelope to expect from a T-top bird-mode radar (`conditions/bird-reading.md`).

## The one-line quick reference (from `conditions/bird-reading.md`)

| Bird | Means *fish* | Means *bait / skip* |
|---|---|---|
| **Terns** | moving dive-line | locked dives on one spot |
| **Shearwaters** | circle back on the drive-through; hopscotching rafts; racing low off a boil | rafted and scatter-off; no movement |
| **Gulls** | locked in at island/kelp edge (weakly) | anywhere else — "parking-lot" / paddy-finder |

---

**What the KB does not give you:** no field-ID guidance for telling these birds apart at glassing range (beyond "white terns"), no month-by-month note on which of the three you should expect off SoCal when, and the whole shearwater doctrine rests on a single dated 2022 report with no second source and no user corroboration — treat it as a good working model, not repeated doctrine.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `conditions/bird-reading.md`, `planning/search-and-glassing.md`, `conditions/kelp-paddies.md`, `techniques/foamer-casting.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/skipjack-tuna.md`, `species/dorado.md`, `species/bonito.md`, `species/barracuda.md`, `species/pacific-crevalle-jack.md`, `species/white-seabass.md`, `locations/breakwalls-jetties-riprap.md`, `lures/tuna-poppers-and-stickbaits.md`, `sources/extraction-log.md`, `sources/memory-export.md`  
*videos:* `Blh2BA-7Ono`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `yLpDI8jnizU`, `SczdZIq3UmE`, `A6DJoXbID4c`, `DnSqw4r7A1s`, `E4vKwRaRueA`, `ZFqe49jRgA0`, `6EDQtQHEwFE`, `bydQzE3F9yM`, `jTXIr9O6zYk`  
*gaps admitted:* No field-identification guidance anywhere in the KB for distinguishing terns, gulls and shearwaters at glassing range - the only ID cue given is 'white terns' (SczdZIq3UmE). | No seasonal/monthly layer on bird presence: the KB never says which months terns, gulls or shearwaters are actually around off SoCal/Baja, so the seasonal/ calendar cannot be used to weight a bird read. | The entire shearwater doctrine traces to one dated BD report (Blh2BA-7Ono, 7/21/22) with no second corpus source and no user corroboration - Cameron explicitly does not factor shearwaters in as of 2026-08. | No stated detection ranges for shearwater rafts or gull piles specifically; the glassing ranges in planning/search-and-glassing.md cover only terns, a 'big bird spot' and dolphins. | No guidance on how long a gull has to stay put to count as 'locked in' at an island or kelp edge, or how to tell that from a gull merely loafing. | No content on how bird behavior changes with sea state, wind or time of day (e.g. whether flat-calm vs. windy conditions change the dive-line read). | No bird content for bays/harbors - the inshore bird material covers only cormorants in kelp and unspecified birds sitting on riprap. | Boobies are carried only as Cameron's unelaborated observation (mostly at the Coronado Islands, 'worth paying attention to') with no behavioral read attached; no doctrine exists for any other SoCal seabird.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short version

The KB's core rule is that **presence is worthless — behavior is everything**. From [`conditions/bird-reading.md`](conditions/bird-reading.md): the question for every bird is never "are there birds?" but **"are they on bait, or on bait being pushed by fish underneath?"**

| Bird | Means *fish* | Means *bait / skip* |
|---|---|---|
| **Terns** | moving dive-line | locked dives repeating on one spot |
| **Shearwaters** | circle straight back on a drive-through; rafts hopscotching; racing off low from a boil | rafted and scatter-off; no movement |
| **Gulls** | locked in at an island/kelp edge, weakly, with nothing better around | anywhere else — "parking-lot birds" / paddy-finders |

(That table is reproduced from `conditions/bird-reading.md`; the corpus half is BD's 7/21/22 Bight report, `Blh2BA-7Ono`, the other half is `cameron`.)

---

## Terns — the best bird, and the one both voices agree on

**The read** ([`conditions/bird-reading.md`](conditions/bird-reading.md), corpus 7/21/22 `Blh2BA-7Ono`):

- **Locked-in repeated dives on one spot = bait only.** The bait is pinned there by something other than gamefish; there's nothing under it to run on.
- **A moving dive-line = bait being pushed by fish underneath.** That is the one you run on. The same rule is restated as the key bird sign in [`species/bluefin-tuna.md`](species/bluefin-tuna.md) and [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md) ("working birds, terns best").

**Cameron's practice merged in** (source `cameron`, memory 8/3/26, in `conditions/bird-reading.md` and [`planning/search-and-glassing.md`](planning/search-and-glassing.md)): terns are his best bird too. He will **almost always stop and cast on working terns**, and **offshore he will follow terns around to find fish even when no other birds are working**.

**Finer reads layered on top:**

- **Watch the individual bird, not just the flock** (StokedOnFishing, `A6DJoXbID4c`, 2016-10-06, offshore San Diego, bluefin on a paddy — unregistered channel, medium confidence): on-camera coaching while glassing a single working tern — watch its head, how it looks, the little reactions. Same trip gives the state machine: **birds actively diving/working = the school is feeding at the surface; birds off the fish = the school is still there but "puddling"** (present, not surface-feeding) rather than gone. The KB keeps this beside the moving-vs-locked rule, not as a replacement.
- **Cast *under* the diving bird, not at its general position** (Capt. Dave Hansen, Fred Hall 2019 Part 2, `JiJYamo0QHk`, 2019-03-12 — registered voice, single mention, medium confidence): a hovering tern is waiting on a school to eventually push bait up underneath it. The instant it actually dives to pick, the bait just broke the surface directly below it — put your bait there, immediately, under the bird itself.
- **One or two terns still count.** Even a **single or a couple of terns picking at the water** — diving and looking rather than working a school hard — is worth running to and sweeping with sonar, because fish can sit just under the surface with no bird pile and no visible boil (SearcherSportfishing, `lf3S28nh-kk`, 2021-03-26, in [`planning/search-and-glassing.md`](planning/search-and-glassing.md)). A small group of terns marking a pocket of yellowfin is logged as an on-the-water instance in [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md) (`ilINTeknKB4`).
- **Look for the white terns specifically** — not pelicans, not seagulls ("they do help but... it's the white terns"), stated to anglers new to tuna fishing near the 209 bank over **72°F** water (StokedOnFishing, `SczdZIq3UmE`, 2019-10-02 — medium confidence; the yellowfin boated that day graded 10–15 lb, ~25 lb, ~20 lb, per [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md)).

**What you do about it** ([`techniques/foamer-casting.md`](techniques/foamer-casting.md)): run at working terns fast, set up **ahead of the school's direction of travel** (fish feed with their mouths, not their tails — a bait behind a moving school is presented to fish that already passed it, `JiJYamo0QHk`), **stop hard — 25 knots straight to neutral — and cast immediately** into the middle of the foam, and budget **2–3 casts per school** before moving on. The variant from `A6DJoXbID4c` for a school still under way: don't run straight up on them, swing wide and around so you come to rest ahead of travel, shut down, and let them swim into casting range.

## Gulls — "a good sign but dumb"

Both voices land in the same place ([`conditions/bird-reading.md`](conditions/bird-reading.md)):

- **Corpus (`Blh2BA-7Ono`):** unreliable — "parking-lot birds." Only meaningful when **locked in at islands / kelp edges**, and even then only with nothing better around.
- **Cameron:** "good sign but dumb" — a general measure of **life in an area**, and his **paddy-finders**. Repeated in [`conditions/kelp-paddies.md`](conditions/kelp-paddies.md): gulls are reliable for locating **floating kelp** even when they aren't marking gamefish.

So the practical translation: gulls tell you there is life and probably kelp — they do not tell you there are gamefish underneath. Two places they earn a look:

- **Kelp edges / island structure**, per above, and in [`species/calico-bass.md`](species/calico-bass.md): "gulls locked to a kelp edge with nothing better around are worth checking" — but inshore, **cormorants diving *in* the kelp** beat them as a calico tell.
- **Beaches on the grunion cycle** — staging fish show **100–500 ft off the beach** starting around midday before a run, marked by **gulls, pelicans and terns** working that zone (Tackle Express / Shannon Gallagher, `EuYOlsnxXko`, 2025-11-19 — unregistered, medium confidence, in [`species/california-halibut.md`](species/california-halibut.md)). Note the KB explicitly calls that a **bait signal**, worth noting *before* the halibut signal shows.

One contrary observation is on file, and the KB's rule is that observations don't overturn doctrine: a Cedros Island session (baja-pacific-north) closed with a roughly **30-minute blitz under gulls "going bonkers," including a triple hookup**, after the crew had called the day done (StokedOnFishing, October 2024 trip, `6EDQtQHEwFE` — unregistered, medium confidence, in [`species/yellowtail.md`](species/yellowtail.md)). Read that as "gulls going genuinely berserk over structure/island water is worth one look," not as a promotion of gulls generally.

## Shearwaters — the most information-dense bird, and the one you have to test

This is the piece Cameron's own model is missing — he **doesn't factor shearwaters in (as of 2026-08)** — so it is pure corpus doctrine from the 7/21/22 report, `Blh2BA-7Ono` ([`conditions/bird-reading.md`](conditions/bird-reading.md)):

- **Rafted (sitting in a group)** = sitting over **deep bait, waiting for the tide.**
- **The drive-through test.** Idle through the raft and watch what they do: **circle straight back = fish under them**; **scatter and land somewhere else = bait only.** This is the only bird read in the KB where you actively probe rather than just observe.
- **Rafts hopscotching 20–30 ft at a time = tracking deep fish.**
- **Racing off low in one direction from a boil = they are running to the *head* of the school.** Follow them — the old boil you were looking at is the tail.

That last one is the most actionable line in the whole note: it converts a dying boil into a heading.

## Cross-cutting rules that change how you read all three

- **Mixed piles** (gulls + pelicans + terns + cormorants) **at open-water current breaks = bait only, skip** (`Blh2BA-7Ono`). **Exception:** a mixed pile **on kelp or structure** can be a real bait event — e.g. the grunion blitz that produced every-cast bass in ugly water (10/20/22, `OYOda6T3f-8`).
- **Birds sitting still on the water still mark the zone.** Trolling past sitting birds and hopscotching rafts produced immediate bites when nothing was flying (8/17/22, `HzE4FHHcvTk`). The riprap version: **birds sitting on the rocks mark the thumb-over-hose current deviation** ([`locations/breakwalls-jetties-riprap.md`](locations/breakwalls-jetties-riprap.md)) — a cluster parked on one stretch of wall is sitting where the break concentrates bait.
- **Birds on structure = a repeatable decision; the same sign in no-man's-land = low value** ([`conditions/current-structure.md`](conditions/current-structure.md)).
- **Watch a bird 30–40 seconds before you judge it.** A single glimpse cannot tell you whether the dive-line is moving or the raft is tracking ([`planning/search-and-glassing.md`](planning/search-and-glassing.md), 7/14/22 `DnSqw4r7A1s` + the Landesfeind dorado video `E4vKwRaRueA`). Glass from a full stop or bow into the swell at ~1 kt, 360° in small increments, **3–4 minutes per full scan**.
- **Know your detection ranges** (same note): from deck level, **a few terns at ~0.5–1 mi**, a **big bird spot at ~2 mi**; from a **hardtop**, birds to **~2 mi** (dolphins to ~4 mi). Space glass stations **3–4 mi apart**. Bird-mode radar with gain near max paints bird schools as **red blotches at 4–5 mi** (Duane Diego Mellor, `yLpDI8jnizU`) — that's the working envelope to expect from a T-top unit.
- **Lens tint matters for picking birds out:** the contrast lens — **green or copper** — is the one called out for kelp, **birds** and dolphins; neutral gray is the bright-light default, yellow for overcast/low light (`nnrEjc-Gq2o`, 2020-01-02, in [`planning/search-and-glassing.md`](planning/search-and-glassing.md)).
- **The other birds, for completeness** (`conditions/bird-reading.md`): **pelicans** are worthless as a gamefish indicator — Cameron's "dirty birds," diving pelicans usually mean he's in the wrong area and casting there produces **mackerel** (useful as a *bait* tell). **Cormorants diving in kelp = actively feeding = a bass indicator**, better than gulls inshore. **Boobies** at the Coronado Islands are carried as Cameron's observation, worth paying attention to, with no corpus doctrine behind it.
- **Related, not species-specific:** on traveling dolphin pods offshore, **even a single bird sitting on a pod** is the tell that *that* group is holding tuna, over unmarked pods nearby (Dave Hansen, `SgF5hRlEGqU`, 2022-02-27 — registered voice, single mention, medium confidence, in [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md)). The bird species isn't named there.

## What the KB does not tell you

- It never distinguishes **shearwater species** (sooty vs. pink-footed, etc.), or gull or tern species beyond "white terns" — so all three reads are behavioral, not taxonomic.
- There is **no seasonal calendar for the birds themselves** — nothing on when shearwaters are present in the Bight, or how bird composition shifts month to month.
- **Glassing ranges are only given for terns and a generic "big bird spot."** No stated detection range for a shearwater raft or a gull pile.
- **No stated shelf life on a moving dive-line** (how long it stays workable), and no distance for how far ahead to lead a shearwater raft that's racing off a boil — "follow them" is as specific as the corpus gets.
- Cameron's shearwater model is explicitly **empty as of 2026-08**, so there is no second, independent voice on any of the shearwater doctrine above — it is single-source from one 2022-07-21 report.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/bird-reading.md`, `planning/search-and-glassing.md`, `conditions/kelp-paddies.md`, `conditions/current-structure.md`, `locations/breakwalls-jetties-riprap.md`, `techniques/foamer-casting.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/california-halibut.md`, `sources/transcripts/_manifest.csv`  
*videos:* `Blh2BA-7Ono`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `yLpDI8jnizU`, `SczdZIq3UmE`, `A6DJoXbID4c`, `JiJYamo0QHk`, `DnSqw4r7A1s`, `E4vKwRaRueA`, `lf3S28nh-kk`, `nnrEjc-Gq2o`, `EuYOlsnxXko`, `6EDQtQHEwFE`, `ilINTeknKB4`, `SgF5hRlEGqU`  
*gaps admitted:* No shearwater, gull or tern species-level identification anywhere in the KB — all three reads are behavioral only (only 'white terns' is specified). | No seasonal calendar for bird presence/abundance — nothing on when shearwaters are in the SoCal Bight or how bird composition shifts month to month. | Glassing/detection ranges are given only for terns (~0.5-1 mi deck, ~2 mi hardtop) and a generic 'big bird spot'; no stated range for spotting a shearwater raft or a gull pile. | No stated duration for how long a moving tern dive-line stays workable. | No distance or lead given for following shearwaters racing off a boil to the head of the school — 'follow them' is as specific as the corpus gets. | Shearwater doctrine is single-source (one 2022-07-21 BD Bight report) — Cameron's own bird model explicitly does not factor shearwaters as of 2026-08, so there is no second independent voice on it. | The dolphin-pod 'single bird on the pod' tell does not name which bird species.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## The one question you're actually asking

The KB's framing is that presence is worthless — **"the question is never just whether birds are present — it is whether they are on bait alone, or on bait being pushed by fish underneath"** ([conditions/bird-reading.md](conditions/bird-reading.md)). Locked-in, stationary behavior reads bait-only. Moving, pushing, racing behavior reads fish working that bait. All three of your birds get scored on that same axis; what changes is how much you should trust each one's answer.

Ranking, straight from the note: **terns and shearwaters are the reliable ones; gulls and pelicans mostly are not.**

---

## Terns — the money bird

Terns are "the single best bird: constant, high-eyesight surface hunters that are always flying and looking, so they surface anything edible fast" (`Blh2BA-7Ono` — BDOutdoors SoCal Bight report, 2022-07-21). Cameron's model agrees: he will stop and cast on working terns, and offshore he follows terns to find fish even with no other birds working (cameron).

What the behavior means:

- **Locked-in, repeated dives on one spot = bait only.** The mechanism matters here, because it's what makes the read trustworthy: bait under predation pressure looks *down*, not up, so surface bait with nothing under it sits still and lets a tern hit the same spot over and over without moving (`Blh2BA-7Ono`).
- **A moving dive-line = bait being pushed from below.** Terns come in, dive, fly ahead a few feet, dive again — because the bait itself is fleeing something underneath. "That is the one to run on" (`Blh2BA-7Ono`).
- **Cast under the bird the instant it dives**, not at its general position. A hovering tern is *waiting* on a school to push bait up beneath it; the dive is the signal that bait just broke the surface directly under it (`JiJYamo0QHk` — Dave Hansen, Fred Hall 2019).
- **Read the individual bird, not just the flock.** Birds actively diving/working a school mean it's feeding on the surface. Birds *off* the fish but still nearby mean the school hasn't left — it's holding just under the surface without feeding on top ("puddling") rather than gone (`A6DJoXbID4c` — StokedOnFishing, 2016-10-06). The same trip's on-camera coaching is to watch the bird's *head* and its small reactions, not just whether the flock is working ([conditions/evidence/bird-reading.md](conditions/evidence/bird-reading.md)).
- **Even one or two terns picking at the water** — diving and looking rather than working a school hard — is worth running to and sweeping with sonar, because near-surface fish show on side-scan/up-down sonar without ever making a boil or a bird pile (`lf3S28nh-kk` — Searcher Sportfishing, 2021-03-26; [planning/search-and-glassing.md](planning/search-and-glassing.md)).
- **The color call:** anglers new to tuna are told to key on the **white terns** over pelicans and gulls (`SczdZIq3UmE` — StokedOnFishing, 2019-10-02). That day's water was 72 °F, and the KB flags it: the 72 °F figure is that one report's water temperature that day, **not a general threshold**, and it's corroborated nowhere else ([conditions/bird-reading.md](conditions/bird-reading.md)).

**Once terns confirm, the execution note is [techniques/foamer-casting.md](techniques/foamer-casting.md):** run at the working terns fast, set up **ahead of the school's direction of travel** (fish feed with their mouths, not their tails — a bait cast behind a moving school is presented to fish that already passed it, `JiJYamo0QHk`), stop **25 knots straight to neutral**, cast immediately as close to the middle of the foam as you can reach, and budget **2 to 3 casts per school** before moving to the next one. Foamers are short-lived; do not stake one out (`e73wPONTOJU`, cameron).

---

## Shearwaters — the deep-fish tracker

This is the part of the bird model Cameron does not personally run: he **does not currently factor shearwaters into his own model (as of 2026-08)** (cameron), and the corpus doctrine below — all of it from `Blh2BA-7Ono` — is merged in to fill that gap ([conditions/bird-reading.md](conditions/bird-reading.md)).

- **Rafted, sitting in a tight group** = sitting over **deep** bait, waiting for the tide to bring it up within diving range. That's the key difference from terns: a shearwater raft is telling you about fish and bait you cannot see and may not be able to reach on the surface.
- **The drive-through test — the most actionable move in the whole bird model.** Run the boat straight through the raft. **Circling straight back = fish underneath. Scattering and landing somewhere else = bait only.** It converts a static, ambiguous raft into a yes/no answer.
- **Rafts hopscotching 20–30 ft at a time = tracking fish holding deep.** ⚠ The KB flags this one as single-source: the 20–30 ft hopscotch distance and its fish-holding-deep read rest on that one transcript alone, corroborated nowhere else in the note or the KB.
- **Racing off low in one direction from a working boil = they're running to the head of the school.** Follow them — the boil they left is the *tail*. This is the read that keeps you from parking on fading whitewater while the school moves out from under you.

Corroborating on-the-water case: trolling past sitting birds and then hopscotching rafts produced immediate bites **with nothing flying** (`HzE4FHHcvTk` — BDOutdoors, 2022-08-17 report). Birds on the water still mark the zone.

---

## Gulls — a life detector, not a fish detector

Gulls are explicitly **unreliable**: "a gull is as happy fighting over fast-food scraps as it is feeding on bait," so it will eat garbage, dead bait, or anything thrown overboard (`Blh2BA-7Ono`). They are only meaningful **locked in at an island or a kelp edge with nothing better working** (`Blh2BA-7Ono`).

What they *are* good for:

- **Paddy-finding.** For Cameron, gulls are mainly [kelp-paddy](conditions/kelp-paddies.md) finders — "good sign but dumb," a general measure of life, and reliable for locating floating kelp even when they aren't marking gamefish (cameron). On a gray, calm morning, glassing down-swell for gulls is a legitimate way to find the paddy line before you commit gear ([conditions/kelp-paddies.md](conditions/kelp-paddies.md)). [species/yellowtail.md](species/yellowtail.md) states it as the split you should carry offshore: "working terns are the run-to bird; gulls sitting on floating kelp are the paddy-finders."
- **Inshore, ranked below cormorants.** For calicos, cormorants diving *in* the kelp is the better tell; gulls locked to a kelp edge with nothing better around are worth checking, and that's the whole of it ([species/calico-bass.md](species/calico-bass.md)).
- **Birds parked on riprap mark the current deviation.** A cluster of birds sitting on one stretch of wall sits where the current break concentrates bait — you don't have to guess where the thumb-over-hose spot is (`bydQzE3F9yM`, [locations/breakwalls-jetties-riprap.md](locations/breakwalls-jetties-riprap.md)).

Two cases where gulls did produce, both worth keeping as observations rather than doctrine:

- A **mixed pile on kelp/structure** can be a real bait event: a grunion blitz in the kelp produced bass on every cast in dirty water (`OYOda6T3f-8` — BDOutdoors, 2022-10-20). The rule this bends is the general one below.
- At **Cedros Island (Baja, not SoCal)**, a session already written off as done reopened into a roughly 30-minute blitz **under gulls**, including a triple hookup (`6EDQtQHEwFE`, [locations/cedros-island.md](locations/cedros-island.md)). Observation, not a promotion of gulls.
- Inshore/beach: staging halibut show **100–500 ft off the beach** from around midday before a grunion run, "marked by gulls, pelicans and terns working that zone" (`EuYOlsnxXko`, [species/california-halibut.md](species/california-halibut.md)) — a case where an undifferentiated bird pile is the sign.

---

## Quick reference

| Bird | Means *fish* | Means *bait / skip* |
|---|---|---|
| **Terns** | moving dive-line; individual birds actively diving/working | locked dives on one spot; off the fish and puddling (school is still there, just not feeding on top) |
| **Shearwaters** | circle straight back on the drive-through; rafts hopscotching 20–30 ft; racing low off a boil (follow to the head of the school) | rafted and scattering off on the drive-through; no movement |
| **Gulls** | locked in at an island/kelp edge with nothing better working (weak) | anywhere else — treat as paddy-finder / general life |

(Table condensed from [conditions/bird-reading.md](conditions/bird-reading.md), which also covers pelicans — "worthless" as a gamefish indicator, diving pelicans usually mean wrong area and produce mackerel — and cormorants, where diving *in* kelp is a bass tell.)

**The mixed-pile rule:** gulls + pelicans + terns + cormorants together **at an open-water current break = bait only, skip it** (`Blh2BA-7Ono`). The exception is that same pile **on kelp or structure**, which can be a real bait event worth working (`OYOda6T3f-8`).

---

## How to actually put eyes on this

From [planning/search-and-glassing.md](planning/search-and-glassing.md):

- **Glass from a full stop, or bow into the swell at ~1 kt** — a rolling, drifting boat makes glassing useless (`DnSqw4r7A1s`, `E4vKwRaRueA`). Image-stabilized binoculars.
- **Watch a bird 30–40 seconds before judging it.** A single glimpse does not show you whether the dive-line is moving or the raft is tracking — which is the entire tern and shearwater read above. Work 360° in small increments, **3–4 minutes per full scan**.
- **Ranges:** from deck level expect a few terns at **~0.5–1 mi**, a big bird spot at **~2 mi**; from a hardtop, birds carry to **~2 mi** and dolphins to **~4 mi**. Glass from the highest stable spot you have. **Space glass stations 3–4 mi apart.** Along a bank, run the contour at **16–18 mph** with a lookout ~30° off each bow.
- **Bird radar:** gain near max, range capped at **4–5 mi** — a shorter range gives a clean return on bird schools instead of drowning them in clutter; schools paint as **red blotches**, sometimes boat-sized (`HWx1jDTGsng` — Capt. Duane Diego, BDOutdoors, 2020-06-08). ⚠ The KB flags the 4–5 mi range and the red-blotch description as single-source.
- **Lens tint:** a contrast lens — green or copper / amber — is the one called out for picking out kelp, birds and dolphins; neutral gray/blue mirror is the all-around bright-light default; yellow for overcast and low light (`nnrEjc-Gq2o`, `YJX-hYEIcNM`).
- **At anchor on a sportboat**, chum gets pushed *up-current toward the bow* by the fish working it — watch for birds locking on up there and put the surface iron under them (`DnSqw4r7A1s`).

One scoping correction worth knowing, since it's flagged in the KB itself: [locations/coronado-islands.md](locations/coronado-islands.md) says "terns are worth reading here specifically," and carries a ⚠ **contradicted-by-source** flag on it — the cameron source states terns as his best bird *generally*, with no Coronados scoping. The bird he does scope to the Coronados is the **booby**, and the KB has no corpus doctrine on booby behavior at all.

---

## What the KB does not tell you

Listed plainly rather than filled in from outside knowledge — see the gaps list below. The biggest one for your question: **there is no bird-identification content anywhere in this KB.** Everything above is behavior doctrine. If you can't yet separate a tern from a gull from a shearwater at half a mile, the closest thing the KB offers is "look for the **white** terns" (`SczdZIq3UmE`).


*notes:* `README.md`, `planning/day-plan-protocol.md`, `conditions/bird-reading.md`, `conditions/evidence/bird-reading.md`, `planning/search-and-glassing.md`, `planning/evidence/search-and-glassing.md`, `conditions/kelp-paddies.md`, `techniques/foamer-casting.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/california-halibut.md`, `locations/breakwalls-jetties-riprap.md`, `locations/coronado-islands.md`, `locations/cedros-island.md`, `locations/209-312.md`, `sources/transcripts/_manifest.csv`  
*videos:* `Blh2BA-7Ono`, `JiJYamo0QHk`, `A6DJoXbID4c`, `SczdZIq3UmE`, `lf3S28nh-kk`, `HzE4FHHcvTk`, `OYOda6T3f-8`, `HWx1jDTGsng`, `DnSqw4r7A1s`, `E4vKwRaRueA`, `e73wPONTOJU`, `6EDQtQHEwFE`, `EuYOlsnxXko`, `bydQzE3F9yM`, `nnrEjc-Gq2o`, `YJX-hYEIcNM`  
*gaps admitted:* No bird-identification content anywhere in the KB — no field marks, size, wingbeat, flight profile or plumage cues to separate a tern from a gull from a shearwater at range; the only ID-ish phrasing is 'look for the white terns' (SczdZIq3UmE). | No shearwater species breakdown (sooty vs. pink-footed, etc.) — the KB treats 'shearwater' as one undifferentiated bird. | The entire shearwater doctrine rests on a single source (Blh2BA-7Ono, BDOutdoors 2022-07-21), and Cameron explicitly does not factor shearwaters into his own model as of 2026-08, so there is no second voice or internal cross-check on any shearwater read. | No timing parameters for the shearwater drive-through test — the KB does not say how long to wait for a circle-back before calling it a scatter, nor over what interval the 20-30 ft raft hopscotch is measured. | No distance or time budget for the shearwater 'racing off low = run to the head of the school' move — no how-far-to-follow number, unlike the tern/foamer approach which has 25 kt to neutral and 2-3 casts per school. | No approach, lure, depth or drift mechanics for fishing a confirmed shearwater raft — nothing equivalent to techniques/foamer-casting.md exists for the deep-fish-under-a-raft case. | No positive gull read beyond 'locked in at an island or kelp edge with nothing better working' — the KB gives no depth, structure, species or conditions detail for that case, and no hit rate or corpus corroboration for gulls-as-paddy-finders (Cameron's model only). | No bird seasonality anywhere — the seasonal/ priors carry no calendar for when shearwaters raft in the Bight or when tern numbers peak. | No Baja- or Sea-of-Cortez-specific doctrine for these three birds; the Cedros gull blitz (6EDQtQHEwFE) is logged as a Baja observation, not doctrine. | The 72 F figure attached to the white-tern call is flagged single-source in the KB as that one day's water temperature, not a general threshold for tern-worthy water — so the KB gives no temperature band for bird activity.

</details>
