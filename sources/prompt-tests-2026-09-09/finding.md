# Finding fish — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11 | 12 | 11.5 |
| found | 2 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 1.5 | 2 | 2 |
| scoped | 1.5 | 2 | 1.5 |
| honest | 2 | 2 | 2 |
| actionable | 2 | 2 | 2 |
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
| Finding fish | 11 | 12 | 11.5 |
| Conditions & season | None | None | None |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 14. [finding] What do yellowtail look like on the sounder and at what depths, and how does that differ from bluefin?

**Winner:** B3 · mapping {'A': 'B2', 'B': 'NOW', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 1 | 2 | 2 | **11** |  |

**Judge:** All three found the right material and quoted real depths with plausible ids, so the separation came from scoping, mechanism and noise. C alone stated the notes' regions/waters gating — telling the angler the bluefin sonar reading does not apply to an inshore or Sea-of-Cortez day — and paired every depth band with both a range setting and a lure while flagging its own discrimination rule as inference rather than doctrine. B was the most honest about provenance (it surfaced that the headline 5-10 fathom figure is absent from its cited source, plus two unresolved internal contradictions and an unverifiable DSL tie) and matched C on the feeding-state shape read, but gave no region gating and left its headline yellowtail number destabilized. A was the longest and fully sourced but missed the shape-reads-feeding-state material and the 40-60 ft staging band entirely, and buried its usable contrast under repeated observation lists.

- *B2 reasons:* found: went straight to species/yellowtail.md + species/bluefin-tuna.md 'Finding them' plus electronics note; covers both species' sonar reads, though it misses the mark-shape-reads-feeding-state material (stratified vs bottom-balled) and the 40-60 ft staging band the other two carry. specific: dense real numbers — 5-10 fm/30-60 ft structure arcs, 90-120 ft paddy boomerangs, 150-300 ft (best 150-180) BOLA, 30-50 fm sounded, 198-330 ft stacked, Furuno gain 55-57, ping 15 of 20, 0-120/0-150 ft manual range. sourced: every claim carries a note path and a plausible video id (D5DR7Kx42_A, 6DzbsElGE7E, HWx1jDTGsng, nRFFM8DT-og, 9hEa3sGTh40), with confidence tiers named. scoped: Baja/BOLA/Cortez/Catalina labeled by place, but never states the notes' regions/waters gating, so an angler isn't told the bluefin material doesn't apply to a Cortez or inshore day; no regulatory claims. honest: strong — long explicit gap list, separates doctrine from medium-confidence unregistered-channel observations, refuses to invent arch discrimination, all dates absolute. actionable: yes — each depth read routes to a jig weight/technique (yo-yo, dropper, 130-250 g slow pitch, 150-300/300-400 g knife jig) plus anchor and range settings.
- *B3 reasons:* found: covered both species' sonar sections completely — shape, depth-band tables, feeding-state reads, the DSL/wind mechanism for why bluefin depth moves, and the bait-driven mechanism for yellowtail (squid pushed out to 30-40 fm). specific: full depth tables per species with ids on every row, plus 60-80 ft in 120 ft, 240-360 ft/250 g floor, 100-180 g flat-fall by current, 150-300 g to 300-400 g, 0-120/0-150/0-300 ft ranges, 15 ft spot to 30 ft screen. sourced: each table row carries its video id and the two anchor notes are named; the Searcher counter-practice and the sea-state cone mechanism are both attributed (fgTmUq78ofQ). scoped: the only answer that states front-matter gating explicitly — yellowtail all five regions/island-bank-nearshore-open, bluefin socal-bight + baja-pacific-north, open-ocean + bank only, and spells out that none of the bluefin reading applies inshore or in the Sea of Cortez; no regulations stated. honest: labels the single-trip BOLA figure medium confidence, keeps the 300 ft-travelling vs Searcher 80 fm practice side by side unreconciled, and explicitly marks its own depth/hard-bottom discriminator as inference rather than KB doctrine; absolute dates. actionable: highest signal-to-noise — the contrast table converts each read into a range setting and a lure, including where 40-60 ft rules the yo-yo out.
- *NOW reasons:* found: hit the right sections and pulled the evidence files too, adding the feeding-state shape read (spread/stratified = hunting vs bottom-balled = not feeding) and the 40-60 ft staging band that A lacks. specific: strong numbers throughout — 5-10 fm, 40-60 ft, 90-120 ft, 150-300/150-180 ft, 30-50 fm, 50-80 fm, 240-360 ft with a 250 g jig floor, 0-300 ft range cap, Furuno 55-57. sourced: note paths plus ids, and uniquely reports what a cited source does and does not actually contain (D5DR7Kx42_A carries no depth figure; tpmOYXYQwhU has no bottom-balled school). scoped: region context is geographic only; no statement of the notes' regions/waters gating; no regulation claims. honest: the strongest — surfaces the KB's own fact-check flags, two unresolved internal contradictions (300 ft travelling vs 240-360 ft night marks; 330/360/400 ft night ceiling), the unverifiable DSL tie, and the demoted BOLA figure; absolute dates only. actionable: yes — depth-to-jig-weight ladder, range settings, anchor/bait presentation, though undermining the headline 5-10 fm number leaves that one band shakier to act on.

<details><summary>Full prompt</summary>

What do yellowtail look like on the sounder and at what depths, and how does that differ from bluefin?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short version

The KB separates them mainly by **where the mark sits relative to structure and how deep**, not by the shape of an individual fish arch:

- **Yellowtail** = **tight balls hugging structure**, on **hard bottom only**, classically **arcs / boil-ups at ~5–10 fathoms (30–60 ft)** near the rock — plus a deep high-spot face at **150–300 ft** and a paddy face at **90–120 ft**.
- **Bluefin** = **open-water school marks**, either **sounded deep at 30–50 fathoms (180–300 ft)** in wind with no surface sign, or **rising on the DSL at night (~180–330 ft)** — with a well-documented set of shallower mid-column reads (**50–150 ft**) that the KB keeps side by side with the deep number rather than folding together.

Detail, with the numbers as the notes state them.

---

## Yellowtail on the meter

From `species/yellowtail.md` → **Finding them (sign & sonar)**:

**1. Structure / bottom fish — the classic read**
- **Tight balls of yellowtail hugging the structure**, marked on **hard bottom, pinnacles and high spots**; the classic read is **arcs / boil-ups at ~5–10 fathoms near structure** — i.e. **30–60 ft**, at the 1 fathom = 6 ft conversion given in `planning/electronics-and-sounder.md` (`Rf1HKJG-SDg`, `HGyL7pXy3Ts`). Quote carried in the note: "We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`).
- **Hard bottom only, never mud.** Structure yellows sit exclusively on hard/rocky bottom — "they're not going to be [out] in the mud... they're always going to be on the hard bottom" (`6DzbsElGE7E`). So read bottom hardness *first*: thin/faint bottom return = sand/mud, thick and dark = rock (`planning/electronics-and-sounder.md`, `6DzbsElGE7E`) — brand-agnostic, no discrimination mode needed. A soft-bottom spot isn't worth looking for fish sign on at all.
- **The tell that the fish (not just the bait) are there:** a **thin, lighter mark riding higher than the bait ball** is the yellowtail itself, pushing bait up off the rocks — that's the sign to commit the anchor over a hard-bottom mark, not the bait pile alone (`6DzbsElGE7E`).

**2. Deep high-spot fish (BOLA / Baja)**
- Marks on high spots in the **150–300 ft** band, with the fish **stacked on the up-current face** of the high spot (`vqsD0qpwcJA` / `Jtf-bU4aM-c`). The Situations→techniques table adds that within that band it **bit best at 150–180 ft**, on slow-pitch / knife jigs **130–250 g**.

**3. Paddy fish**
- Paddy yellows **don't meter deep**. Under a paddy showing no surface activity, look for **boomerang-shaped arcs around 90–120 ft**, and give it about **a minute or two** before writing the paddy off (Dave Hansen / Your Saltwater Guide, `ZFqe49jRgA0`, 2019-05-26).

**Observed depth data points** (these are on-the-water observations, mostly medium confidence / unregistered channel, kept beside the doctrine above, not folded into it — `species/yellowtail.md` **Where & when**):
- **Cortez Bank, June trip:** anchored in **15–25 fathoms**; later, working the bank's high spot on the incoming tide, the crew **marked yellowtail at 60–80 ft in 120 ft of water** and landed 20–40 lb fish on flylines, J-hooks, surface irons and yo-yo irons (`UfuiWFVvz2E`).
- **Cortez Bank, August 2024:** boat positioning worked along a **50–60 fathom edge / drop-off** off the high spot (`nQvJnfb5jQ4`).
- **Cortez Bank, Ranger 85:** anchor and drift both producing in water around **50 fathoms** (`zBd1mayUt_I`).
- **San Benito Island, Baja:** yellowtail out on **squid at 30–40 fathoms** — also called "**30, 40, 50** fathoms" and later "**30, 35**" in the same segment, preserved as spoken — feeding **right off the bottom**, because the squid had moved out of the shallows when small mackerel took over; nearly every fish had fresh squid in it. Worked with dropper loop and yo-yo iron (`JaKSGkZ6CAc`). That is a **bait-migration-driven depth**, not a fixed structure depth.
- **San Clemente Island:** sounder showing fish **holding down in the column while some anglers got bit up top** — the crew alternated surface iron above and yo-yo iron below on the same drift (`ecJPMTCi-gw`).

**A yellowtail-specific sounder pivot:** fish still visibly marking but the anchored surface-iron bite gone quiet → **get up above the marks and drift over them instead of staying on the hook**; that brought the bite back (`97clKtVsEOs`, San Benito Island; also in `planning/electronics-and-sounder.md` under "Anchor vs. drift call off a live sounder read"). Read the mark *and* the response, not just the mark.

---

## Bluefin on the meter

From `species/bluefin-tuna.md` → **Finding them (sign & sonar)**:

**1. Sounded schools — the headline number**
- Wind up, no surface sign: "god forbid there's no foamer, you're going over a lot of fish and there's a lot of wind — that's when those fish sound down, you're looking **30, 45, 50 thousands**" — i.e. **30–50 fathoms (180–300 ft)** — "and you need the power to reach and grade them" (`HWx1jDTGsng`). The note is explicit that this is the **meter-and-jig situation, not a troll situation**. Same figure is restated as Capt. Duane Diego Mellor doctrine (high confidence) in **Doctrine & conflicts**: in wind with no surface sign the fish **sound to 30–50 fathoms** and you need power on the meter to reach them.
- **Bank extension:** an overnight jig session at Cortez/Tanner (mid-August 2024) read marks **360° around the boat, from 50 fathoms down to 80 fathoms, even below** (`LsFMBCa9DOQ`) — deeper than the 30–50 fm band, kept side by side as a bank-specific extension.

**2. Night bite on the DSL**
- After dark the fish rise with the **deep scattering layer** (600+ ft by day, rising at night — `conditions/deep-scattering-layer.md`). The read is **depth-called marks you drop a jig straight down onto: "fish at 180, fish at 230 ft"** (`nRFFM8DT-og`).
- Backside San Clemente Island, June 2023: the meter read a school **stacked from about 198 ft down to 330 ft** under the boat (`r4J5nP5Bkl4`) — wider-banded than the 180/230 example, carried beside it.
- Mechanism is kept as **two reads side by side**: corpus = food-following (feeding on the risen layer); Cameron = the jig bite is **likely a reaction bite** (flagged *likely, not measured*).

**3. The shallow / mid-column reads the KB refuses to smooth away**
- **60–80 ft** mark, jig dropped straight down, hooked up after about **two cranks**; same session also marks at roughly **100 ft moving up and down all around the boat**, and at **~150 ft** (`cLYqjT7ddl8`).
- **120 ft**, then a "really good mark... solid" at **150 ft**, west end of Catalina, August 2020 (`M7BtON4GZgQ`).
- **50–100 ft** on a Catalina offshore drift — fish sitting off the top, worked with **butt-hooked sardines** let to swim down to the marks (`8THSuqoPI_Q`).
- **80–150 ft** anchored on a kelp paddy, worked with butt-hooked and sinker-rigged live bait rather than a jig (`IwxqgocsQTY`).
- The Situations→techniques table also carries a **~60 ft shallow bait-ball** row (chumming sardines, no surface sign yet) → yo-yo iron dropped through the mark and cranked fast.

**4. School shape in open water**
- At a manual shallow range, **a school of tuna paints as a large, distinct upside-down-U-shaped mark**; left on auto with the bottom set to the real (much deeper) depth, the same school shrinks to a barely visible speck (`planning/electronics-and-sounder.md`, `9hEa3sGTh40`). Note the KB states this for **tuna schools generally** (the worked example is schooling tuna under dolphin pods), not as a bluefin-specific signature.
- **Bait shape is the grading cue:** broken, harried, moving bait holds predators; a solid unbroken wall usually does not (`species/bluefin-tuna.md`; also `planning/electronics-and-sounder.md`).

---

## Side by side

| | Yellowtail | Bluefin |
| --- | --- | --- |
| **What the mark looks like** | Tight balls hugging structure; arcs / boil-ups; boomerang-shaped arcs under paddies; a thin lighter mark riding *above* the bait ball = the yellows themselves (`D5DR7Kx42_A`, `ZFqe49jRgA0`, `6DzbsElGE7E`) | Open-water school marks; at manual range a large distinct upside-down-U (tuna generally, `9hEa3sGTh40`); depth-called individual marks at night (`nRFFM8DT-og`) |
| **Where it sits** | Locked to **hard bottom / pinnacles / high spots**, up-current face of the high spot; never mud | Off structure — open water, over banks and island fathom curves, under paddies, or on the DSL |
| **Classic depth** | **~5–10 fathoms (30–60 ft)** near structure | **30–50 fathoms (180–300 ft)** sounded in wind |
| **Deep face** | **150–300 ft** high spots, best 150–180 ft (BOLA/Baja) | **50–80 fm and below** at Cortez/Tanner (`LsFMBCa9DOQ`); night DSL **180–330 ft** |
| **Shallow face** | Paddy fish **90–120 ft**; observed **60–80 ft in 120 ft of water** at Cortez Bank | Observed **50–100 ft**, **60–80 ft**, **80–150 ft**, **120–150 ft** — repeatedly, all kept beside the deep number |
| **What the read routes to** | Yo-yo iron / dropper loop on the 5–10 fm structure balls; slow-pitch 130–250 g on the 150–300 ft high spots; surface iron / flyline on the top face | Knife jig 150–300 g (300–400 g in more current/depth) on 30–50 fm marks; night knife-jig or rubber-band deep rig on DSL marks; yo-yo iron on ~60 ft bait balls |

**The interpretive difference that matters more than the numbers:** for yellowtail, the KB's own framing is that the three faces are **states of one population driven by water temperature and bait depth, not fish types** (cameron) — the fish roam the column and feed looking up, so a depth read tells you *which face is on today*, and the doctrine is to rig the surface-iron, heavy yo-yo/dropper, and flyline outfits **simultaneously** and switch as the read changes (`species/yellowtail.md`, Doctrine & conflicts). For bluefin the depth read is closer to a **hard gate on method**: sounded at 30–50 fm means meter-and-jig, explicitly *not* a troll situation, and no surface sign at all means trolling/kite is the locate play (`species/bluefin-tuna.md`, `species/bluefin-trolling.md`).

---

## Machine settings that make each read possible

All from `planning/electronics-and-sounder.md`:

- **Run manual range, not auto** — repeated doctrine across three Dave Hansen videos (`9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`), high confidence on the core rule. Working range **0–120 ft on older machines, 0–150 ft on newer ones**, regardless of actual bottom depth. Reasoning: a private boat doesn't have the bait budget to chum a deep school up the way a sportboat can ("they can look at fish at 30 fathoms and set on it long enough... the fish will come up"), so there's little point reading below the top of the column. Scenario-specific example: **0–150 ft** manual for tuna schooling under dolphin pods offshore (`SgF5hRlEGqU`).
- **Size the range so the bottom sits mid-screen**, not pinned at the edge — leaves room to read hard vs soft bottom and pick fish out of the column above it. Worked examples: 15 ft spot → 30 ft screen range; 25 ft spot → 40 ft; offshore **0–300 ft** to look for tuna suspended around 150 ft (`FEXgl0eQCa8`, medium confidence on the sizing method itself).
- **For the DSL / night bluefin:** gain and TVG **up** (Furuno ~**55–57**), **ping speed slowed** (~**15 of 20**) so the layer paints as a distinct band; on a Garmin GPSMAP 840xs that translates to gain up + slow ping, then watch for the band (`conditions/deep-scattering-layer.md`, `planning/electronics-and-sounder.md`).
- **Stop only on marks you can grade — it's a bait budget.** Idle on, grade against what you know pays off, commit only when it grades out; **photograph the screen during bites** to build your own library of productive marks.
- **Anchoring on a yellowtail mark:** grade the high spot with **repeated passes** on the same GPS track, then release the anchor **into the adjacent sand patch, not on the rock** (`planning/search-and-glassing.md`, `6DzbsElGE7E`, high confidence — repeated in the same presenter's own words in `xI9tPJFXbUM`). For yellowtail specifically, because of break-off risk, **anchor further off still** so a hooked fish has room before it reaches structure.
- **Backing down blanks the bottom return** — that's air under the hull, not a machine fault (`HGyL7pXy3Ts`).

---

## What the KB does not tell you

- It gives **no side-by-side description of an individual yellowtail arch vs an individual bluefin arch** — no shape, thickness, or color-intensity discrimination between the two species' marks. The separation in these notes is by **depth, position relative to hard structure, and school shape**, and I won't invent the rest.
- **No transducer frequency / CHIRP guidance for either species.** The dual-frequency split-screen doctrine (low frequency gainy and paints everything, high frequency for detail) is documented only for `species/rockfish-lingcod.md` and `species/ocean-whitefish.md` — the notes never extend it to yellowtail or bluefin.
- **No mark-size-to-fish-grade calibration** — nothing lets you call a 40 lb vs a 100 lb fish off the screen.
- **No way to tell bluefin from yellowtail under the same paddy on the meter** — both are documented hanging under kelp paddies, and the only stated instruction is to grade the paddy fast and move.
- **No numeric gain/sensitivity/color-palette values for the Garmin 840xs** beyond "gain up, ping slowed"; the actual numbers in the corpus are Furuno's.
- **No horizontal/search-sonar doctrine for yellowtail.** The one search-sonar entry (**400–600 ft side to side**, plus the audio cue that changes distinctly when the sweep hits fish) is a sportboat tuna account from `nkJNzdNlm_c`, not applied to yellowtail anywhere in these notes.
- Most of the specific depth observations above (Cortez Bank, San Benito, Catalina, San Clemente) come from an **unregistered, often sponsor-heavy channel and are logged at medium confidence** as observations, not rules. The high-confidence spine is: yellowtail = tight balls on hard structure at ~5–10 fm; bluefin = sounded to 30–50 fm in wind, rising on the DSL at night.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `planning/search-and-glassing.md`, `species/yellowtail.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `conditions/deep-scattering-layer.md`, `species/rockfish-lingcod.md`, `species/ocean-whitefish.md`  
*videos:* `D5DR7Kx42_A`, `vqsD0qpwcJA`, `Jtf-bU4aM-c`, `ZFqe49jRgA0`, `6DzbsElGE7E`, `UfuiWFVvz2E`, `JaKSGkZ6CAc`, `zBd1mayUt_I`, `nQvJnfb5jQ4`, `97clKtVsEOs`, `ecJPMTCi-gw`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `nRFFM8DT-og`, `r4J5nP5Bkl4`, `M7BtON4GZgQ`, `cLYqjT7ddl8`, `8THSuqoPI_Q`, `IwxqgocsQTY`, `9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`, `Rf1HKJG-SDg`, `HGyL7pXy3Ts`, `yLpDI8jnizU`, `yMiBtZ7k8-w`, `nkJNzdNlm_c`, `xI9tPJFXbUM`  
*gaps admitted:* No side-by-side description of an individual yellowtail arch vs an individual bluefin arch (shape, thickness, color intensity) — the KB separates the species by depth, structure relationship and school shape only. | No transducer frequency / CHIRP guidance for yellowtail or bluefin; the dual-frequency split-screen doctrine exists only in species/rockfish-lingcod.md and species/ocean-whitefish.md and is never extended to these two species. | No mark-size-to-fish-grade calibration — nothing in the KB lets you estimate fish weight from the size of a mark. | No documented way to distinguish bluefin from yellowtail marking under the same kelp paddy; both are logged as paddy fish with only 'grade it fast and move' as guidance. | No numeric gain/sensitivity/color-palette settings for the Garmin GPSMAP 840xs beyond 'gain up, slow the ping'; the only numeric settings in the corpus are Furuno's (TVG/gain 55–57, ping speed ~15 of 20). | No horizontal / search-sonar doctrine for yellowtail — the 400–600 ft side-to-side scan envelope and audio bite cue are a sportboat tuna account (nkJNzdNlm_c) and are not applied to yellowtail anywhere. | The 'large upside-down-U' school-mark shape is stated for tuna schools generally (a dolphin-pod worked example), not specifically verified as a bluefin signature. | Most specific depth observations cited (Cortez Bank, San Benito Island, Catalina, San Clemente) are medium-confidence observations from an unregistered, sponsor-heavy channel rather than doctrine.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short version

**Yellowtail are a hard-bottom, structure-locked mark. Bluefin are an open-water, suspended mark.** That difference drives everything else — the depth bands, the shape you're looking for, and even how you set the machine's range before you leave the dock.

---

## Yellowtail on the meter

Source: `species/yellowtail.md` ("Finding them (sign & sonar)"), with general method in `planning/electronics-and-sounder.md`.

**Shape.** The classic yellowtail read is **arcs / boil-ups at roughly 5–10 fathoms (30–60 ft) near structure**, and **tight balls of fish hugging the structure** — "we see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`).

**Hard bottom only, never mud.** Structure yellows sit exclusively on hard/rocky bottom — "they're not going to be [out] in the mud... they're always going to be on the hard bottom." Read bottom hardness off the return thickness: **thin, faint line = sand/mud; thick and dark = rock** (`6DzbsElGE7E`). Grade the *bottom* before you go looking for fish sign on it.

**The depth bands, as the KB has them:**

| Situation | Depth on the meter | Source |
| --- | --- | --- |
| Structure / bottom yellows, classic read | **~5–10 fathoms (30–60 ft)** near structure | `D5DR7Kx42_A` |
| "They're coming up" band | **40–60 ft**, fish not yet showing | `0DKmYId1NN4` |
| Cortez Bank high spot, incoming tide | **60–80 ft in 120 ft of water** | `UfuiWFVvz2E` |
| Under a paddy with no surface activity | **boomerang-shaped arcs, ~90–120 ft** | `ZFqe49jRgA0` |
| San Benito Island, fish on squid off the bottom | **30–40 fathoms** (also spoken as "30, 40, 50" and "30, 35" — preserved as said) | `JaKSGkZ6CAc` |
| BOLA / Baja high spots (single-trip, medium confidence) | **150–300 ft**, stacked on the **up-current face** | `vqsD0qpwcJA` |

**Two shape reads that beat depth alone** (both `HTowqnwAMeA`):
- **Stratified column** — marks running as lines from the bottom up through mid-column, sometimes to the surface — reads as **fish actively hunting bait**; that's the cue to put slow-trolled baits out.
- **Ball stuck to the bottom** — fish present but not hunting — is **dropper-loop water, not flyline water**.
- Layered on that: **up in the column and spread out = they'll eat; tucked down tight on the bottom = they won't**, watched over a rock roughly **20–30 ft across**.

**Two more yellowtail-specific tells:**
- A **thin, lighter mark riding higher than the bait ball can be the yellowtail itself**, pushing bait up off the rocks — that's the sign to commit, not the bait pile alone (`6DzbsElGE7E`).
- **Marked but not surfacing still gets bit**: schools that "don't come up and boil around" still eat once a jig reaches their metered depth — "just about every lure that makes it down to the depth that fish is, is a bite," with yo-yo iron stated to have out-fished live bait "multiple times" in that scenario (`tpmOYXYQwhU`, medium confidence).

**What the depth tells you to tie on.** The **40–60 ft** read explicitly *rules out* the yo-yo: *"usually like surface iron fish and like light bait zone — so we're not going to be yo-yoing today... once they start boiling, then we're going to go all in on the surface iron"* (`0DKmYId1NN4`, medium — unregistered channel). Deeper, on-structure balls get weight dropped on them: heavy full-size irons (Salas 6X class) most of the time, vertical/flat-fall **100–180 g depending on current** as the change-up (`D5DR7Kx42_A`).

---

## Bluefin on the meter

Source: `species/bluefin-tuna.md` ("Finding them (sign & sonar)"), plus `planning/electronics-and-sounder.md` and `conditions/deep-scattering-layer.md`.

**Shape.** The KB's stated bluefin school shape is scale-dependent, not structure-dependent: on a **manual 0–150 ft range**, a school of tuna paints as a **large, distinct upside-down-U-shaped mark**; left on auto with the bottom set to the real (far deeper) depth, the same school **shrinks to a barely visible speck** (`9hEa3sGTh40`, `8XrMkWPRxgs` — repeated doctrine, high confidence on the core rule). The same point stated for bluefin specifically: over a typical bluefin bottom of **2,000–3,000 ft** on auto, **"10 tons of bluefin sounded through simply doesn't show"** (`m-M0iwX8DjA`).

**The depth bands, as the KB has them:**

| Situation | Depth on the meter | Source |
| --- | --- | --- |
| **Core doctrine** — wind up, no surface sign, fish sound | **30–50 fathoms (180–300 ft)** — "30, 45, 50 thousands" | `HWx1jDTGsng` (Duane Diego Mellor, high) |
| Overnight jig, Cortez/Tanner banks | **50 fathoms down to 80 fathoms, even below**, reading **360° around the boat** | `LsFMBCa9DOQ` |
| Night, ~20 mi off San Diego | **240–360 ft** — the stated reason a flat-fall/knife jig must be **250 g or greater** (120–150 g won't get there) | `eehDVb6_GoI` |
| Night bite on the DSL | depth-called marks — **"fish at 180, fish at 230 ft"** | `nRFFM8DT-og` |
| Night, backside San Clemente Island | school **stacked ~198 ft down to 330 ft** | `r4J5nP5Bkl4` |
| West end of Catalina, daytime jig | marks at **120 ft**, then a "really good mark... solid" at **150 ft** | `M7BtON4GZgQ` |
| Shallow marks, fast jig hookup | **60–80 ft** (bit after ~two cranks); also ~**100 ft moving up and down all around the boat**, and ~**150 ft** | `cLYqjT7ddl8` |
| Drift, fish off the top | **50–100 ft** — butt-hook a sardine and let it swim down | `8THSuqoPI_Q` |
| Anchored on a kelp paddy | **80–150 ft** | `IwxqgocsQTY` |
| Tanner Bank, chumming sardines in ~120 ft | bait marks around **60 ft** | `ntQXxcH5sjI` |

The KB deliberately keeps these **side by side rather than reconciled into one number** — the 30–50 fm figure is the high-confidence doctrine; everything shallower and deeper is logged as an additional same-region data point.

**Why the depth moves.** Bluefin depth in this KB tracks **wind, light and the deep scattering layer**, not structure. The DSL sits **600+ ft down by day** and lifts after dark, so the deep sonar-school fish that were unreachable by day come into reach at night (`conditions/deep-scattering-layer.md`). Wind with no surface sign is what sends them to 30–50 fm in the first place (`HWx1jDTGsng`).

**What the depth tells you to tie on** (from the Situations → techniques table in `species/bluefin-tuna.md`): 30–50 fm → knife jig, **150–300 g by day, 300–400 g in more current or deeper**; **~60 ft** bait balls while chumming → yo-yo iron dropped through the mark and cranked fast; captain calling a **~100–200 ft** bite zone → flat-fall, free-spool to the mark, most bites **on the fall**, wind back up about halfway and re-drop; **240–360 ft** → 250 g minimum.

---

## The differences that actually matter on the water

| | **Yellowtail** | **Bluefin** |
| --- | --- | --- |
| What the mark is tied to | **Hard bottom, pinnacles, high spots** — exclusively; never mud (`6DzbsElGE7E`) | **Open water / suspended.** Read 360° around the boat at the banks (`LsFMBCa9DOQ`); bottom is 2,000–3,000 ft and irrelevant (`m-M0iwX8DjA`) |
| Signature shape | **Arcs / boil-ups**, **tight balls hugging structure**, **boomerang arcs** under paddies | **Large upside-down-U** school mark — but only if the range is capped manually |
| Headline depth | **5–10 fathoms (30–60 ft)** near structure | **30–50 fathoms (180–300 ft)** sounded |
| Full observed range in the KB | ~30 ft to 300 ft (BOLA outlier) | ~50 ft to 80 fathoms and below |
| What moves the fish up and down | **Bait and structure** — e.g. squid pushed out of the shallows by mackerel took the yellowtail with them to 30–40 fm (`JaKSGkZ6CAc`) | **Wind and light/DSL** — wind sinks them to 30–50 fm; the DSL lifts them after dark |
| The behavioural read | Stratified & spread = biting; balled tight on the bottom = not (`HTowqnwAMeA`) | Not stated as a shape rule; the analogue is **bait shape** — broken, harried bait holds predators, a solid unbroken wall usually doesn't |
| How you set the range | Size so **the bottom sits mid-screen** — you need to read hardness. 15 ft spot → 30 ft range; 25 ft spot → 40 ft range (`FEXgl0eQCa8`) | **Manual, bottom out of the picture entirely** — 0–120 ft on older machines, 0–150 ft on newer (`9hEa3sGTh40`, `8XrMkWPRxgs`); 0–300 ft for bluefin (`m-M0iwX8DjA`) |
| Depth → technique switch | **40–60 ft rules the yo-yo out** and puts you on surface iron + light bait | **Deeper = heavier jig**, on a stated ladder: 150–300 g → 300–400 g → 250 g minimum below 240 ft |

**One more contrast worth knowing before you touch the range knob.** The 0–150 / 0–300 ft private-boat rule has a stated *reason* that is about bait budget, not fish: a private boat can't hold and chum a school up from depth the way a sportboat can ("they can look at fish at 30 fathoms and set on it long enough... the fish will come up"), so there's no point reading deeper than the top of the column (`9hEa3sGTh40`). Hansen's stop-at-300-ft reasoning is that fish **below 300 ft are traveling, not biting**; fish in the **300 ft-to-surface band** are the eager ones (`m-M0iwX8DjA`, medium — single mention). The KB keeps a **sportboat counter-practice side by side and does not reconcile it**: the *Searcher*'s wheelhouse sounder is run to about **80 fathoms (480 ft)**, watching the whole band while searching for bluefin schools (`fgTmUq78ofQ`).

**And a sea-state caveat that applies to both.** In flat water the cone can be shot right along the surface and you read the full column. In chop the cone has to be shot lower, so **a fish holding high in the column won't show until the boat is right on top of it** — the same fish that would have painted from a distance on a calm day (`fgTmUq78ofQ`). That's a mechanism, not a gain setting to fix — expect to under-read shallow fish when it's rough. (`planning/electronics-and-sounder.md`)

**Sounder settings for the deep/night bluefin work:** gain/TVG pushed up (Furuno ~55–57, mid-to-high on other brands), **ping speed slowed (~15 of 20)** so the DSL paints as a distinct band (`planning/electronics-and-sounder.md`).

---

## What this KB does *not* answer

- **It gives you no way to tell a yellowtail mark from a bluefin mark on the same screen.** That matters, because the KB documents them biting together at Cortez Bank on the same flylined sardines (`nQvJnfb5jQ4`). In practice you'd separate them by depth band and by whether the mark is welded to hard bottom — but the notes never state that as a discrimination rule, so treat it as my inference, not KB doctrine.
- No arch-size / return-strength → fish-weight grading for either species.
- No transducer-frequency, CHIRP, or forward-facing/live sonar guidance for either species (the only settings given are manual range, gain, and ping speed).

*Region/waters applicability, per the front matter: yellowtail covers all five regions and island / bank / nearshore-coast / open-ocean; bluefin covers `socal-bight` + `baja-pacific-north` only, and only `open-ocean` + `bank` waters — so none of the bluefin reading above applies to an inshore or Sea-of-Cortez day.*


*notes:* `README.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `species/yellowtail.md`, `species/bluefin-tuna.md`, `conditions/deep-scattering-layer.md`  
*videos:* `D5DR7Kx42_A`, `6DzbsElGE7E`, `0DKmYId1NN4`, `UfuiWFVvz2E`, `ZFqe49jRgA0`, `JaKSGkZ6CAc`, `vqsD0qpwcJA`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `eehDVb6_GoI`, `nRFFM8DT-og`, `r4J5nP5Bkl4`, `M7BtON4GZgQ`, `cLYqjT7ddl8`, `8THSuqoPI_Q`, `IwxqgocsQTY`, `ntQXxcH5sjI`, `9hEa3sGTh40`, `8XrMkWPRxgs`, `m-M0iwX8DjA`, `FEXgl0eQCa8`, `fgTmUq78ofQ`, `nQvJnfb5jQ4`  
*gaps admitted:* The KB never states a rule for telling a yellowtail mark apart from a bluefin mark when both species are on the same screen (it documents them biting together at Cortez Bank but gives no discrimination method). | No guidance anywhere on grading fish size/weight from arch size or return strength, for either species. | No transducer-frequency, CHIRP, or frequency-selection guidance per species — the only sounder settings in the KB are manual range, gain/TVG, and ping speed. | No forward-facing / live-imaging / side-scan sonar content for yellowtail or bluefin (the only side-scan mention is a search-sonar scan range on a sportboat, not a mark signature). | No yellowtail equivalent of the bluefin 'upside-down-U' school-shape description — yellowtail shape is only described qualitatively (arcs, boomerangs, tight balls). | Yellowtail sonar signatures for the Sea of Cortez rest on a single BOLA trip (150-300 ft), explicitly demoted to medium confidence; no second source.

</details>

<details><summary><b>NOW — review</b> · 11/12</summary>

## Short version

The two fish read differently in **three** ways, and the KB is explicit about all three: the **depth band** they sit in, the **shape** of the mark, and — critically — **the machine setting you need to see them at all**. Yellowtail are a structure read in the top ~60 ft to a few hundred feet, graded against the bottom return. Bluefin are a mid-water/deep read, 30–80 fathoms, that your sounder will not paint if it's on auto.

One conversion the KB states outright and I'll use throughout: **1 fathom = 6 ft**, and the sounder is properly a *fathometer* (`planning/electronics-and-sounder.md`, `HGyL7pXy3Ts`, `Rf1HKJG-SDg`, `9hEa3sGTh40`).

---

## Yellowtail on the meter

Front-matter summary in `species/yellowtail.md`: *arcs 5–10 fathoms near structure; paddy arcs 90–120 ft; Baja high spots 150–300 ft.*

**Structure fish — the classic read.** Tight balls hugging hard bottom; arcs and boil-ups at **~5–10 fathoms (30–60 ft)** near pinnacles and high spots (`species/yellowtail.md`, `D5DR7Kx42_A`). Grade the *bottom* before you hunt fish sign: thin return = sand/mud, thick return = rock, and the fish hold on the rock (`6DzbsElGE7E`). That 5–10 fm band drives the router row — tight balls on structure → **yo-yo iron** first, then **dropper loop**, on a 40–60 lb stout rod + high-speed reel.

⚠ **Honesty flag, and it's a big one:** the KB itself flags that `D5DR7Kx42_A` **carries no depth figure at all** — no fathoms, no feet, and none of the words "arcs," "boil-ups," "pinnacles" or "high spots." The source supports only "tight balls of yellowtails sometimes hugging the structure." The 5–10 fathom number appears in the front matter and the situations table, but it is not in its cited source. Treat the *shape* (tight ball on hard bottom) as sourced and the *number* as unverified.

**The other yellowtail depth bands** (`species/yellowtail.md`):
- **40–60 ft** — fish metered here and not yet showing are **staging up**. These are surface-iron and light-bait fish, *not* yo-yo fish; when they boil, go all-in on the iron (`0DKmYId1NN4`).
- **90–120 ft under a paddy** — paddy fish often **don't meter at all**. A paddy with no surface activity can still carry **boomerang-shaped arcs at 90–120 ft**; give it a minute or two before writing it off (`ZFqe49jRgA0`; `conditions/kelp-paddies.md`).
- **150–300 ft, deep Baja high spots** (`vqsD0qpwcJA`) → slow-pitch/knife jigs, **130–250 g**. ⚠ Flagged: this is a **single BOLA trip**, the 150–300 ft figure was a *pre-trip expectation* while the trip actually fished **150–180 ft**, and the "stacked on the up-current face" language is not in the source (`species/evidence/yellowtail.md` — demoted 2026-08-17).

**Mark shape reads feeding state, not just position** — this is the part most people miss (`species/yellowtail.md`, `HTowqnwAMeA`):
- **Spread up through the column** — stratified lines from the bottom through mid-column, or sitting high and spread over a small rock (~20–30 ft across) → **hunting**. Slow-trolled and flylined baits work.
- **Balled tight to the bottom** → present but **not feeding**. Dropper-loop water, worth a yo-yo burned past for the reaction strike. A bottom-hugging ball is *not* a wide-open bite waiting for a good angler. (⚠ the KB flags that the second cite, `tpmOYXYQwhU`, contains no bottom-balled school.)

**Fish mark vs bait mark.** A thin, lighter mark riding *above* a bait ball can be yellowtail pushing bait up off the rocks (`6DzbsElGE7E`). ⚠ Flagged: the source actually inverts the anchor trigger — the *bait pile* is what commits the anchor, and the anchor goes into **sand**, not onto the rock.

---

## Bluefin on the meter

Front-matter summary in `species/bluefin-tuna.md`: *30–50 fathoms sounded in wind; 50–80 fathoms at the offshore banks; 180–330 ft night DSL marks.* Depth band: **surface to 80 fathoms.**

| Read | Depth | What to do |
| --- | --- | --- |
| **Sounded schools** — wind up, no surface sign | **30–50 fathoms (180–300 ft)** (`HWx1jDTGsng`) | meter-and-jig, **not a troll**; you need sounder power to reach and grade them |
| **Offshore-bank night marks**, 360° around the boat | **50–80 fathoms (300–480 ft), even below** (`LsFMBCa9DOQ`) | bank-specific extension, not a replacement |
| **Night, ~20 mi off San Diego** | **240–360 ft** (`eehDVb6_GoI`) | sets a **250 g or greater** jig floor — 120–150 g will not reach in a wind drift |
| **Night depth-called marks** | **180 and 230 ft** (`nRFFM8DT-og`); a school stacked **198–330 ft** (`r4J5nP5Bkl4`) | drop straight down onto the called depth |
| **Daytime marks** | **60–80 ft, ~100 ft, ~150 ft** (`cLYqjT7ddl8`); **120 ft then 150 ft** off Catalina's west end (`M7BtON4GZgQ`) | jig straight down; a bite can come **within two cranks** |
| **Fish off the top on an offshore drift** | **50–100 ft** (`8THSuqoPI_Q`) | butt-hooked sardine swum down to them, long soak |
| **Kelp paddy** | **80–150 ft** (`IwxqgocsQTY`) | live bait rather than a jig |

The KB is careful to say the shallow reads are **same-region data points beside** the 30–50 fathom range, not corrections to it — the band a school sits in is set by the day, so read it rather than assume it.

⚠ Two internal contradictions the KB flags on itself: (1) front-matter caps the night band at 330 ft while its own night row reaches 360 ft and `tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md` goes to ~400 ft; (2) `planning/electronics-and-sounder.md` says fish **below 300 ft are travelling, not biting**, while the 50–80 fathom bank row and the 240–360 ft night row both sit at or under that cutoff — neither note acknowledges the other. Also flagged: the tie between the night marks and the **deep scattering layer** is *unverifiable* — `nRFFM8DT-og` gives captain-called depths only and never mentions the layer, and `conditions/deep-scattering-layer.md` carries no night bluefin depths of its own (the DSL itself sits **600+ ft by day**, preferred down to ~950 ft / 150 fm, `yMiBtZ7k8-w`).

---

## The difference, side by side

| | **Yellowtail** | **Bluefin** |
| --- | --- | --- |
| **Core band** | 5–10 fm (30–60 ft) on structure; 40–60 ft staging | 30–50 fm (180–300 ft) sounded; 50–80 fm at the banks |
| **Reference point** | The **bottom** — marks are graded against a hard/soft return | **Mid-water** — bottom may be 2,000–3,000 ft and irrelevant |
| **Mark shape** | Tight balls hugging bottom; arcs; boomerang arcs under paddies; stratified lines when hunting | Large, distinct **upside-down-U** school mark when the range is set right (`planning/electronics-and-sounder.md`, `9hEa3sGTh40`, `8XrMkWPRxgs`) |
| **What the mark tells you** | **Feeding state** — spread = hunting (bait), balled = not feeding (dropper loop / yo-yo) | **Reachability** — depth picks the jig weight (250 g+ below ~240 ft) |
| **Deep outliers** | 90–120 ft under paddies; 150–300 ft Baja high spots | 240–360 ft night; 198–330 ft stacked schools |
| **Daytime shallow overlap** | 40–60 ft staging fish | 50–100 ft off the top on a drift; 60–80 ft marks |

---

## The setting difference — this is what actually separates them

You will not see bluefin at all with a yellowtail setup (`planning/electronics-and-sounder.md`):

- **Run manual range, never auto** — repeated across three sources (`9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`). Most anglers never leave auto, partly from fear of the buttons and partly because units arrive pre-set to auto from the dealer (`8XrMkWPRxgs`).
- **Yellowtail / structure work:** size the range so **the bottom sits mid-screen, not at the edge** — a 15 ft spot gets a 30 ft screen, a 25 ft spot gets 40 ft (`FEXgl0eQCa8`). That leaves room above the bottom return to separate hard from soft bottom and pick fish out of the column.
- **Bluefin:** cap the range at **0–300 ft** over a 2,000–3,000 ft bottom. On auto, a sounded school **compresses to nothing** against that scale; at 0–300 ft it paints. Fish below 300 ft are travelling; **fish in the 300 ft-to-surface band are the ones eager to bite** (`m-M0iwX8DjA`). Once a mark shows in that band: hit the mark button, run past, turn around, and troll back over it with a Mad Mac.
- Private-boat default working range is **0–120 ft on older machines, 0–150 ft on newer** regardless of actual bottom — a private boat lacks a sportboat's bait budget to chum fish up from depth, so there's no benefit reading deeper (`9hEa3sGTh40`, `8XrMkWPRxgs`). A sportboat wheelhouse searching for bluefin while running stays open to about **80 fathoms / 480 ft** (`fgTmUq78ofQ`).
- **Sea state limits the shallow read, independent of the setting.** Flat: the cone shoots close to the surface and you read the whole column. Choppy: the cone tips, and a fish holding high doesn't show until you're nearly on top of it — the same fish that paints at range on a calm day is invisible once the sea comes up (`fgTmUq78ofQ`). Mechanism is the transducer: a fixed one follows the roll, a gyro/roll-stabilized one stays aimed down (`ZIJAvAEW_tU`).
- **For the DSL** (night bluefin, daytime swordfish): push gain/TVG up (Furuno ~55–57, mid-to-high on other brands) and slow the ping to ~15 of 20 so the band builds on screen (`yMiBtZ7k8-w`).

**Two habits that apply to both:** don't stop at the first bottom mark — keep running and stack the picture depth by depth (a worked example ran marks at ~20 ft, then out to 40 ft, then 60 ft) (`KjVLn4cWHbc`, `QP6c8vcslVs`); and **stop only on marks you can grade — it's a bait budget**. Present to where the mark actually *is*: a solid mark at 30 ft under the boat calls for a bait dropped or flicked straight down, not a cast at distance (`bM2vUS1B-yQ`).

---

## What the KB does not cover

The honest limit here: **the KB has no doctrine for telling a yellowtail mark from a bluefin mark when both are possible on the same spot.** That matters, because the KB documents zones where they bite together — Cortez Bank, where boats anchor in 15–25 fathoms for yellowtail sunup to ~noon then move deep for bluefin, and where both ate flylined sardines on the same stop (`species/evidence/bluefin-tuna.md`, `UfuiWFVvz2E`, `nQvJnfb5jQ4`). There is also a demoted single observation of **yellowtail** stacked on offshore tuna pens metered straight down at **~120 ft with bluefin alongside them** (`species/evidence/yellowtail.md`, `Ob45hK4HSWc`) — squarely in the overlap band. In that situation the KB gives you depth and shape, but no discriminator. Use depth-band probability plus surface sign, and be prepared to be wrong.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `species/yellowtail.md`, `species/bluefin-tuna.md`, `species/evidence/yellowtail.md`, `species/evidence/bluefin-tuna.md`, `conditions/deep-scattering-layer.md`, `species/yellowtail-coronado-islands.md`, `tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md`  
*videos:* `D5DR7Kx42_A`, `6DzbsElGE7E`, `0DKmYId1NN4`, `ZFqe49jRgA0`, `vqsD0qpwcJA`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `Ob45hK4HSWc`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `eehDVb6_GoI`, `nRFFM8DT-og`, `r4J5nP5Bkl4`, `cLYqjT7ddl8`, `M7BtON4GZgQ`, `8THSuqoPI_Q`, `IwxqgocsQTY`, `UfuiWFVvz2E`, `nQvJnfb5jQ4`, `9hEa3sGTh40`, `8XrMkWPRxgs`, `SgF5hRlEGqU`, `FEXgl0eQCa8`, `m-M0iwX8DjA`, `fgTmUq78ofQ`, `ZIJAvAEW_tU`, `yMiBtZ7k8-w`, `HGyL7pXy3Ts`, `Rf1HKJG-SDg`, `KjVLn4cWHbc`, `QP6c8vcslVs`, `bM2vUS1B-yQ`  
*gaps admitted:* No doctrine anywhere in the KB for discriminating a yellowtail mark from a bluefin mark when both species are possible at the same depth on the same spot (e.g. Cortez Bank, or the ~120 ft tuna-pen observation where yellowtail and bluefin were stacked together). | The headline yellowtail figure — arcs at 5-10 fathoms near structure — is carried in front matter and the situations table but the KB's own fact-check flag states the cited source D5DR7Kx42_A contains no depth figure at all; only the 'tight balls hugging structure' shape is actually sourced. | No coverage of sonar frequency, CHIRP, cone angle, target strength, or arch size as a way to read fish size or species — the planning/ and conditions/ branches contain none of these terms. | No coverage of forward-facing / live-imaging sonar (LiveScope-class) or side-imaging for either species; only down-looking sounder plus a horizontal search sonar run 400-600 ft side to side. | No method for estimating fish grade (weight/size) from the mark for either species. | Yellowtail deep-band data outside SoCal is thin: the 150-300 ft Baja high-spot band rests on a single BOLA trip that the KB itself demoted, where 150-300 ft was a pre-trip expectation and the fished depth was 150-180 ft. | Unresolved internal contradiction the KB flags but does not settle: planning/electronics-and-sounder.md says fish below 300 ft are travelling rather than biting, while species/bluefin-tuna.md carries productive night marks at 240-360 ft and bank marks at 50-80 fathoms. | Unresolved internal contradiction on the bluefin night depth ceiling: front matter caps it at 330 ft, the situations table reaches 360 ft, and the Searcher jig ladder goes to ~400 ft. | The link between the bluefin night marks and the deep scattering layer is flagged unverifiable — no corpus source ties them together, and the DSL note carries no night bluefin depths of its own. | No sonar signature given for yellowtail in the Sea of Cortez beyond the single BOLA trip, and no bait-species discrimination on the meter (telling anchovy from sardine from squid marks).

</details>

### 15. [finding] What do terns, gulls and shearwaters each tell me when I see them working?

**Winner:** NOW · mapping {'A': 'B3', 'B': 'B2', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 1 | 2 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three deliver the same core doctrine - behavior not presence, moving dive-line vs locked dives, the shearwater drive-through test, gulls as life/paddy detectors - so the separation is in sourcing granularity and calibration. C wins because it gives the mechanism behind each read (bait under predation looks down, so undisturbed bait lets a tern hit one spot repeatedly; a gull will eat garbage), attaches a video id to nearly every load-bearing line, and propagates the KB's own uncertainty flags rather than laundering them: it says the 72F is that day's water temperature and not a threshold, that the 20-30 ft hopscotch and the 4-5 mi radar range are single-source, that "terns are especially good at the Coronados" is contradicted by the source, and that boobies are a flagged gap. A is a very close second and is the most executable answer - it alone carries popper-then-stickbait-then-Colt-Sniper order, the jacuzzi-vs-directional bluefin read and the stealth swing-around - but it states the 4-5 mi radar and 20-30 ft figures flat and hangs one rule on a bare date with no video id. B is solid and honest but is the thinnest on attribution, conceding outright that the central tern/shearwater/gull lines map only to dates like 7/21/22 rather than to videos.

- *B2 reasons:* found: all three birds, the core bait-vs-pushed question, mixed piles, sitting rafts, glassing and radar. specific: 72F, 209 bank, yellowfin weights, 20-30 ft hopscotch, 25 kt to neutral, 2-3 casts, 4-5 mi radar, 1/2 mi zoom demo, 30-40 s, 3-4 mi stations. sourced: note links throughout, but the core tern/shearwater/gull doctrine is carried by bare dates (7/21/22, 8/17/22, 10/20/22) with the answer itself conceding no per-claim video id mapping - weaker than A and C on the load-bearing lines. scoped: SoCal framing correct, Cedros observation labeled Baja and explicitly demoted to observation. honest: clear gap list, flags gulls-as-paddy-finder as Cameron-only with no hit rate, notes the shearwater model has no second voice; no relative time; the dating caveat at the end is a genuine refusal to invent attribution. actionable: full foamer loop, match-the-hatch, radar-finds-pile/glassing-confirms division, anchored-chum bow tell; slightly less lure detail than A.
- *B3 reasons:* found: covers all three birds plus mixed piles, sitting birds, glassing method, and the Cameron/corpus merge. specific: 72F, yellowfin 10-15/~25/~20 lb, 0.5-1 mi / ~2 mi / ~4 mi, 3-4 mi stations, 30-40 s, 25 kt to neutral, 2-3 casts, 100-500 ft grunion, 4-5 mi radar. sourced: per-claim video ids with dates/channels (Blh2BA-7Ono, A6DJoXbID4c, JiJYamo0QHk, lf3S28nh-kk, SczdZIq3UmE, 6EDQtQHEwFE, EuYOlsnxXko) plus note paths; admits one dated BD report carries no video id and attributes radar to a person name only. scoped: SoCal doctrine kept separate; Cedros/Baja observation labeled as Baja; explicitly notes no Baja/Cortez bird doctrine. honest: long, concrete gap list (no field ID, shearwater single-source, no shearwater mechanics, no bird seasonality, no drive-through timing); no relative time; declines to invent a day plan. actionable: strongest downstream execution - foamer approach, stealth swing-around, popper-then-stickbait-then-Colt-Sniper order, jacuzzi-vs-directional bluefin read, lens tint, radar settings.
- *NOW reasons:* found: all three birds plus the mechanisms behind each read (bait under pressure looks down; gulls eat garbage), mixed piles, sitting rafts, bay footnote, glassing method - matches the note's own structure. specific: 20-30 ft hopscotch, 4-5 mi radar with red blotches, 72F, ~50 yd terns ahead of a dolphin pod, 0.5-1/2/4 mi, 3-4 mi stations, 30-40 s, 25 kt to neutral, 2-3 casts, 100-500 ft. sourced: tightest per-claim ids (Blh2BA-7Ono, JiJYamo0QHk, A6DJoXbID4c, lf3S28nh-kk, ouBrIdO7d4k, OYOda6T3f-8, HzE4FHHcvTk, HWx1jDTGsng, 6EDQtQHEwFE, YgqXf9iICyg, DnSqw4r7A1s) plus evidence files and the source registry; verified against the live note and they line up. scoped: SoCal doctrine, Cedros labeled Baja, Coronados scoping claim explicitly flagged as unsupported, bay content labeled as inshore. honest: best calibrated - carries the KB's own single-source flags (72F is one day's temp not a threshold; 20-30 ft; 4-5 mi radar), surfaces the boobies gap, states shearwaters are one source with no Cameron voice, and reports a contradicted-by-source flag; no relative time. actionable: mechanism plus foamer execution, cast-under-the-diving-bird timing, drive-through test, follow-the-head repositioning, glassing protocol; slightly less lure-selection detail than A.

<details><summary>Full prompt</summary>

What do terns, gulls and shearwaters each tell me when I see them working?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short version

The KB's core rule is that the question is never "are there birds?" but **"are they on bait, or on bait being pushed by fish underneath?"** — you read *behavior*, not presence ([conditions/bird-reading.md](conditions/bird-reading.md)). Each of your three birds sits at a different point on that scale: terns are the money bird, shearwaters are the deep-fish tracker, gulls are a life-and-kelp detector.

---

## Terns — the best bird, and the one you run on

Both voices in the KB (the BD/Landesfeind corpus and Cameron) agree terns are the best bird ([conditions/bird-reading.md](conditions/bird-reading.md)).

- **Moving dive-line = bait being pushed by fish underneath.** That is the one to run on.
- **Locked-in repeated dives on one spot = bait only.** Same birds, opposite answer — the difference is whether the dive line is travelling.
- **Cameron's practice:** he will almost always stop and cast on working terns, and **offshore he will follow terns around to find fish even with no other birds working** ([conditions/bird-reading.md](conditions/bird-reading.md), [planning/search-and-glassing.md](planning/search-and-glassing.md), source `cameron`).
- **Look for the white terns specifically** — not pelicans, not seagulls ("they do help but... it's the white terns"). That call was made offshore SoCal near the **209 bank**, water **72 °F**, on a day that produced yellowfin at **10–15 lb, ~25 lb and ~20 lb** (`SczdZIq3UmE`, 2019-10-02 — unregistered channel, medium confidence; [conditions/bird-reading.md](conditions/bird-reading.md), [species/yellowfin-tuna.md](species/yellowfin-tuna.md)).
- **A finer read — watch the individual bird, not just the flock.** "Watch their head, watch how they look, watch the little reactions in the bird." Birds **actively diving/working = the school is feeding at the surface**; **birds off the fish = the school is still there but "puddling"** — present, not surface-feeding, and *not* gone. That distinction is what stops you writing off a school that just went quiet (`A6DJoXbID4c`, 2016-10-06, offshore San Diego, bluefin on a paddy — medium confidence; [conditions/bird-reading.md](conditions/bird-reading.md)). The KB keeps this beside the moving-vs-locked dive-line rule rather than replacing it.
- **Even a few terns count.** A small group of terns marked a pocket of yellowfin that a crew worked for "one last shot" (`ilINTeknKB4`, 2015-10-29 upload — medium confidence; [species/yellowfin-tuna.md](species/yellowfin-tuna.md)).
- Terns are also the stated visual sign for **bluefin** and **yellowfin** ([species/bluefin-tuna.md](species/bluefin-tuna.md), [species/yellowfin-tuna.md](species/yellowfin-tuna.md)) and appear in the yellowtail sign list ([species/yellowtail.md](species/yellowtail.md)).

**What to do when the tern read says go** ([techniques/foamer-casting.md](techniques/foamer-casting.md)): run at them fast, set up **ahead of the school's direction of travel**, stop hard — 25 knots straight to neutral — and cast immediately as close to the **middle of the foam** as you can reach. Budget **2–3 casts per school**, then move; foamers are short-lived, don't stake one out. A stealthier variant for a school still under way: guess the travel direction off the white terns, **swing out and around** rather than running straight up on them, shut down, and let the fish come into casting range, then **match the hatch** (anchovies, that day) (`A6DJoXbID4c`). Cameron's own foamer program is the same loop: run-and-gun at working terns, ~2–3 casts per school, smaller presentation (Colt-Sniper class) has out-fished bigger, timed around **slack tide** ([species/bluefin-tuna.md](species/bluefin-tuna.md), source `cameron`).

---

## Shearwaters — the deep-fish tracker (and the drive-through test)

This is the part of the model Cameron himself doesn't use — he **doesn't factor shearwaters in as of 2026-08** — so the KB merges the corpus doctrine in as the missing piece ([conditions/bird-reading.md](conditions/bird-reading.md)):

- **Rafted (sitting in a group)** = sitting over **deep bait, waiting for the tide**.
- **The drive-through test** — idle through the raft and watch what they do: **circle straight back = fish under them**; **scatter and land elsewhere = bait only**.
- **Rafts hopscotching 20–30 ft at a time** = they are **tracking deep fish**. Follow them.
- **Racing off low in one direction from a boil** = they are running to the **head** of the school. Follow them — the old boil is the **tail**, not the target.

That last one is the highest-value read of the three birds: it tells you the school's *heading*, which is exactly what the foamer approach above needs.

Related, and worth knowing: **birds sitting still on the water still mark the zone.** Trolling past sitting birds and hopscotching rafts produced immediate bites when nothing was flying (corpus, 8/17/22) ([conditions/bird-reading.md](conditions/bird-reading.md)). Do not skip a raft just because nobody is airborne.

---

## Gulls — "good sign but dumb"

Both voices land in the same place ([conditions/bird-reading.md](conditions/bird-reading.md)):

- **Corpus:** unreliable — **"parking-lot birds."** Only meaningful when **locked in at islands / kelp edges** with nothing better around.
- **Cameron:** "good sign but dumb" — a general **measure of life** in an area, and his **paddy-finders**. Gulls are reliable for locating **floating kelp** even when they aren't marking gamefish ([conditions/kelp-paddies.md](conditions/kelp-paddies.md), source `cameron`).
- Net read: gulls tell you **there is life and there is kelp**, not that gamefish are underneath.
- **Inshore, gulls are outranked.** **Cormorants diving *in* the kelp = actively feeding = a bass tell, better than gulls inshore**; gulls locked to a kelp edge with nothing better around are worth a check, no more ([species/calico-bass.md](species/calico-bass.md), [conditions/bird-reading.md](conditions/bird-reading.md)).
- Gulls can still be on a genuine blitz: a Cedros Island session closed with a roughly **30-minute** yellowtail blitz under gulls "going bonkers," including a triple hookup, after the crew had already called the day done (`6EDQtQHEwFE`, October 2024 trip, 2025-03-07 upload, Cedros Island, Baja — unregistered channel, medium confidence; [species/yellowtail.md](species/yellowtail.md)). Treat that as an observation, not a promotion of gulls — the KB's rule is that observations never change stated doctrine.

---

## Quick reference

| Bird | Behavior that means *fish* | Behavior that means *bait / skip* |
|---|---|---|
| **Terns** | moving dive-line; actively diving/working = school feeding on top | locked dives on one spot = bait only. Birds *off* the fish ≠ gone — school may be "puddling" |
| **Shearwaters** | circle straight back on the drive-through; rafts hopscotching 20–30 ft; racing low off a boil (run to the head of the school) | rafted and scatter-off; no movement |
| **Gulls** | locked in at island / kelp edge (weakly) | anywhere else — "parking-lot" bird / paddy-finder |

Source: the merged quick-reference table in [conditions/bird-reading.md](conditions/bird-reading.md).

**One more filter that applies to all three:** **mixed piles** (gulls + pelicans + terns + cormorants) **at open-water current breaks = bait only, skip.** The exception is a mixed pile **on kelp or structure**, which can be a real bait event worth a look — e.g. the grunion blitz that produced every-cast bass in ugly water (corpus, 10/20/22) ([conditions/bird-reading.md](conditions/bird-reading.md)).

---

## How to actually get these reads (ranges and discipline)

From [planning/search-and-glassing.md](planning/search-and-glassing.md) — the note owns the *method*; bird-reading owns the *meaning*:

- **Glass from a full stop, or bow into the swell at ~1 kt.** Image-stabilized binoculars. You cannot judge a dive-line off a rolling, drifting boat.
- **Scan 360° in small increments, 3–4 minutes per full scan.** When you catch a bird, **watch it 30–40 seconds before judging it** — a single glimpse will not tell you whether the dive-line is moving or the raft is tracking. That 30–40 seconds is the whole difference between the "fish" and "bait" columns above.
- **Ranges:** from deck level, a **few terns at ~0.5–1 mi**, a **big bird spot at ~2 mi**; from a **hardtop**, birds to **~2 mi** and dolphins to **~4 mi**. Space glass stations **3–4 mi apart**.
- **Discipline:** "if you're not burning batteries every trip or two, you're not looking enough."
- **Radar extends the reach:** bird mode, **gain near max, range 4–5 mi**, bird schools painting as **red blotches, sometimes boat-sized** (Duane) — **radar finds the pile, glassing confirms what the birds are doing** ([planning/electronics-and-sounder.md](planning/electronics-and-sounder.md)). A sponsor-heavy Catalina demo showed the same bird mode painting a close-in school as small moving dots at a **1/2 mile** zoom, with a spec'd range up to 5 mi (`MUpvP-Yl2R0`, 2016-11-23, front side of Catalina — medium confidence on the mechanism, low on the product claim).
- **Bonus tell at anchor:** on a sportboat anchored at San Clemente Island, chum gets pushed **up-current toward the bow** by the fish themselves — watch for **birds locking on up there** and put the **surface iron under them** ([planning/search-and-glassing.md](planning/search-and-glassing.md)).

## What the KB does not tell you

- No bird-**identification** content: nothing on field marks, size, or flight style to separate a tern from a gull from a shearwater at a distance, beyond "look for the **white** terns." If you can't tell them apart yet, the KB won't teach you that.
- No shearwater species breakdown (sooty vs. pink-footed, etc.) and no seasonal presence calendar for any of the three birds.
- No shearwater doctrine from Cameron at all — he explicitly doesn't factor them in as of 2026-08, so everything above on shearwaters is corpus-only, with no second voice against it.
- No stated distance/time budget for the shearwater "follow them to the head of the school" move — no how-far-to-run number the way the tern/foamer approach has one.
- Gulls-as-paddy-finders is Cameron's model with no corpus hit-rate behind it — no number on how often a gull-marked paddy actually holds fish.

*(Notes on the corpus dates above — 7/21/22, 8/17/22, 10/20/22, 7/14/22 — are the KB's own dated-report references in [conditions/bird-reading.md](conditions/bird-reading.md) and [planning/search-and-glassing.md](planning/search-and-glassing.md); those notes do not tie individual video IDs to each of those dated lines, so I've carried the notes' full source lists rather than inventing a per-claim mapping.)*


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/bird-reading.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `conditions/kelp-paddies.md`, `techniques/foamer-casting.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/yellowtail.md`, `species/calico-bass.md`  
*videos:* `SczdZIq3UmE`, `A6DJoXbID4c`, `ilINTeknKB4`, `6EDQtQHEwFE`, `MUpvP-Yl2R0`, `Blh2BA-7Ono`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `yLpDI8jnizU`  
*gaps admitted:* No bird-identification content: nothing on field marks, size, or flight style to tell terns, gulls and shearwaters apart at range, beyond 'look for the white terns'. | No shearwater species breakdown (sooty vs. pink-footed, etc.) anywhere in the KB. | No seasonal presence calendar for any of the three birds — the seasonal/ notes are not tied to bird availability. | No Cameron-side shearwater doctrine at all (he explicitly does not factor shearwaters in as of 2026-08), so the shearwater reads are corpus-only with no second voice. | No distance or time budget for the shearwater 'race off low = run to the head of the school' move — no how-far-to-follow number, unlike the tern/foamer approach. | No hit-rate or corroboration for gulls-as-paddy-finders — it is Cameron's model with no corpus number behind it. | The KB's dated corpus lines (7/21/22, 8/17/22, 10/20/22, 7/14/22) are not mapped to individual video IDs in the notes, so per-claim video attribution for the core tern/shearwater/gull doctrine is not available.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short version

The KB's framing (`conditions/bird-reading.md`) is that the question is never "are there birds?" but **"are they on bait, or on bait being pushed by fish underneath?"** Read behavior, not presence. Terns answer that question best, shearwaters answer it second-best (and about *deep* fish), gulls mostly answer a different question — "is there life and floating kelp here?"

That note is a deliberate **merge**: the BD corpus doctrine (Erik Landesfeind's dated Bight reports) and Cameron's own bird model, kept side by side and attributed.

---

## Terns — the best bird (both voices agree)

**The core read (corpus, BD SoCal Bight report 2022-07-21, `Blh2BA-7Ono`):**

- **Locked-in repeated dives on one spot = bait only.** Don't burn the run.
- **A moving dive-line = bait being pushed by fish underneath.** That is the one to run on.

**Cameron (source `cameron`):** terns are his best bird too. He will almost always stop and cast on working terns, and **offshore he will follow terns around to find fish even with no other birds working** — no other sign required.

**Finer reads that sit alongside that rule (`conditions/bird-reading.md`):**

- **Watch the individual bird, not just the flock** (StokedOnFishing, `A6DJoXbID4c`, 2016-10-06 upload, offshore San Diego, bluefin on a kelp paddy; unregistered channel — medium confidence): "watch their head, watch how they look, watch the little reactions in the bird." Same trip gives the mechanism for *when* — **birds actively diving/working = the school is feeding at the surface; birds off the fish = the school is still there but "puddling"** (present, not surface-feeding) rather than gone. So terns going quiet is not the same as fish leaving.
- **Cast under the diving bird** (Capt. Dave Hansen, Fred Hall Show 2019 seminar, `JiJYamo0QHk`, 2019-03-12; registered voice — medium confidence, single mention): a **hovering** tern is waiting on a school to eventually push bait to the surface underneath it. The instant it actually dives to pick, that's the signal the bait just broke the surface **directly below it** — put your bait there, under the bird itself, not at the bird's general position.
- **Even one or two terns are worth a look** (SearcherSportfishing, `lf3S28nh-kk`, 2021-03-26; registered channel — medium confidence, single mention): a single or a couple of terns picking at the water — diving and looking rather than working a school hard — is treated as worth running to and **sweeping with sonar**, because fish can be just under the surface with no bird pile and no visible boil.
- **It's the white terns you want** (StokedOnFishing, `SczdZIq3UmE`, 2019-10-02, offshore SoCal near the 209 bank; unregistered channel — medium confidence): tip to anglers new to tuna — look for the white terns, "not pelicans and not seagulls" ("they do help but… it's the white terns"). Water was **72 °F** that day; that trip boated yellowfin at **10–15 lb, ~25 lb and ~20 lb** (`species/yellowfin-tuna.md`).

**What you do about it** — terns over breaking fish are the entry to foamer casting (`techniques/foamer-casting.md`, sourced `cameron` + corpus):

- Run at working terns **fast**, and set up **ahead of the school's direction of travel** — "fish feed with their mouths, not their tails" (`JiJYamo0QHk`), so a cast behind a moving school is presented to fish that already passed it.
- **Stop hard — 25 knots straight to neutral — and cast immediately**, as close to the middle of the foam as you can reach.
- Budget **~2–3 casts per school**, then move to the next one. Foamers are short-lived; don't stake one out. (Cameron's program summary in `species/bluefin-tuna.md`: run-and-gun at working terns, ~2–3 casts, smaller presentation — Colt-Sniper class — has out-fished bigger, timed around slack tide.)
- Stealth variant for a school still under way (`A6DJoXbID4c`): read the terns for travel direction, then **swing out and around** so you come to rest ahead of it, shut down, and let the fish come into casting range — rather than closing the last distance under power.
- Lure order once you're on it (`lures/tuna-poppers-and-stickbaits.md`): **poppers first** (they hold the zone, bite comes on the pause), switch to a stickbait/darter when fish are keyed on smaller bait, and to a small lead bait (Colt-Sniper class) when the bait is finger-size.
- Bluefin refinement (`species/bluefin-tuna.md`): a **"jacuzzi" — solid circular whitewater — ≈ a bite every cast**; spread-out directional feeders are picky. Wait for the circular form.

---

## Gulls — "good sign but dumb"

Both voices land in the same place (`conditions/bird-reading.md`):

- **Corpus:** unreliable — **"parking-lot birds."** Only meaningful when **locked in at islands / kelp edges** with nothing better around.
- **Cameron:** "good sign but dumb" — a general measure of **life** in an area, and his **paddy-finders**.

Net: gulls tell you there's life and floating kelp, **not** that gamefish are under them.

Where that is actually useful:

- **Paddy hunting** (`conditions/kelp-paddies.md`, source `cameron`): gulls are reliable for **locating floating kelp even when they aren't marking gamefish** — treat them as a kelp detector, then check the paddy on the meter / with a pass.
- **Inshore kelp** (`species/calico-bass.md`): gulls locked to a kelp edge with nothing better around are worth checking — but **cormorants diving *in* the kelp** (= actively feeding) is the better inshore tell, better than gulls.
- **Beach/grunion bait signal** (`species/california-halibut.md`; Tackle Express / Shannon Gallagher, `EuYOlsnxXko`, 2025-11-19; unregistered channel — medium confidence): staging grunion show **100–500 ft off the beach** from around midday before a run, marked by **gulls, pelicans and terns** working that zone. That's a *bait* signal that precedes the halibut signal — exactly the "gulls = life" read, used deliberately.
- **Observed, Baja** (StokedOnFishing, October 2024 trip, 2025-03-07 upload, Cedros Island — `6EDQtQHEwFE`; unregistered channel — medium confidence, in `species/yellowtail.md`): the session closed with a roughly **30-minute blitz under gulls "going bonkers,"** including a triple hookup, after the crew had already called the day done. An observation, not a promotion of gulls to a gamefish bird.

---

## Shearwaters — the deep-fish bird (and the KB's own flagged gap)

`conditions/bird-reading.md` is explicit that **Cameron doesn't factor shearwaters in (as of 2026-08)** — the corpus doctrine (BD 2022-07-21, `Blh2BA-7Ono`) is merged in specifically to fill that gap. Four reads:

- **Rafted (sitting in a group) = sitting over deep bait, waiting for the tide.** They're marking bait you can't see, and they're waiting on a tide change to make it available.
- **The drive-through test:** run the boat through the raft. **Circle straight back = fish under them.** **Scatter and land somewhere else = bait only.** This is the single most actionable shearwater move in the KB — it converts a static raft into a yes/no answer.
- **Rafts hopscotching 20–30 ft at a time = tracking deep fish.** Movement in short hops is the tell, not flight.
- **Racing off low in one direction from a boil = they're running to the *head* of the school.** Follow them — **the old boil is the tail.** This is the one that repositions you correctly on a school you already found.

---

## Two cross-cutting rules that change how you read all three

- **Mixed piles** — gulls + pelicans + terns + cormorants together **at open-water current breaks = bait only, skip** (corpus). **Exception:** a mixed pile **on kelp/structure** can be a real bait event worth a look — the cited case is the grunion blitz that produced every-cast bass in ugly water (BD 2022-10-20, `OYOda6T3f-8`).
- **Birds sitting still on the water still mark the zone.** Trolling past sitting birds and hopscotching rafts produced immediate bites when nothing was flying (BD report dated 2022-08-17). The riprap version (`locations/breakwalls-jetties-riprap.md`): birds sitting on the rocks mark the thumb-over-hose current deviation.

---

## Quick reference (from `conditions/bird-reading.md`)

| Bird | Behavior that means *fish* | Behavior that means *bait / skip* |
|---|---|---|
| **Terns** | moving dive-line | locked dives on one spot |
| **Shearwaters** | circle back on drive-through; hopscotching rafts; racing low off a boil | rafted and scatter-off; no movement |
| **Gulls** | locked in at island/kelp edge (weakly) | anywhere else — "parking-lot" / paddy-finder |
| **Mixed piles** | on kelp/structure = possible bait event | open-water break = bait only, skip |

---

## Actually seeing them — the glassing numbers (`planning/search-and-glassing.md`, from the 2022-07-14 report + the dorado video, Landesfeind)

- **Glass from a full stop**, or bow into the swell at **~1 kt**, with image-stabilized binoculars. You cannot read a dive-line off a rolling, drifting boat.
- **360° in small increments, 3–4 minutes per full scan.** When you catch a bird, **watch it 30–40 seconds before judging it** — a single glimpse won't tell you whether the dive-line is moving or the raft is tracking. That 30–40 seconds is the whole difference between the tern and shearwater reads above being usable or noise.
- **Ranges:** from deck level, a few terns at **~0.5–1 mi**, a big bird spot at **~2 mi**; from a **hardtop**, birds **~2 mi** and dolphins **~4 mi**. Space glass stations **3–4 mi apart**.
- **Bird radar** (Duane, in `conditions/bird-reading.md`): gain near max, **range 4–5 mi**; bird schools paint as **red blotches**, sometimes boat-sized. That 4–5 mi is the working envelope to expect from a T-top bird-mode radar.
- **Lens tint helps** (`planning/search-and-glassing.md`): green/copper/amber is the contrast tint called out for picking out **kelp, birds and dolphins** (`nnrEjc-Gq2o`, 2020-01-02; `YJX-hYEIcNM`, 2022-06-30); neutral gray/blue mirror is the all-around bright-light default; yellow/sunrise for overcast and early/late.
- Discipline line worth keeping: *"if you're not burning batteries every trip or two, you're not looking enough."*

---

## What this KB does **not** tell you

- **How to identify these birds in the field.** Everything above is a *behavior* doctrine; there is no ID guidance — no size, wingbeat, flight-profile or plumage cues for separating a tern from a shearwater from a gull at half a mile. The closest thing is the "look for the **white** terns" phrasing in `SczdZIq3UmE`.
- **The shearwater doctrine has no second source.** It all traces to one dated BD report (2022-07-21, `Blh2BA-7Ono`), and Cameron doesn't use shearwaters at all, so there's no cross-check inside the KB.
- **No approach/cast mechanics for shearwaters** the way terns have `techniques/foamer-casting.md` — the KB tells you the raft is over deep fish, but nothing about what to drop, how deep, or how to set the drift once you've confirmed it.
- **No bird seasonality.** Nothing on when shearwaters raft in the Bight, or when tern numbers peak — the `seasonal/` priors don't carry a bird calendar.
- **No Baja/Cortez-specific bird doctrine.** `locations/loreto.md` and `locations/bahia-de-los-angeles.md` just say "run to working birds, same read as the SoCal program"; the species-level detail above is SoCal corpus.
- **Timing parameters on the drive-through test** — how long to wait for a raft to circle back, or over what interval the 20–30 ft hopscotch is measured — aren't given.

(You didn't give me a date, zone or conditions, so I haven't pulled or assumed any — this is the standing bird doctrine, not a plan for a specific day. If you want it applied to a real trip, give me the launch point, date and forecast and I'll run `planning/day-plan-protocol.md` properly.)


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/bird-reading.md`, `planning/search-and-glassing.md`, `conditions/kelp-paddies.md`, `techniques/foamer-casting.md`, `lures/tuna-poppers-and-stickbaits.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/california-halibut.md`, `locations/breakwalls-jetties-riprap.md`, `locations/loreto.md`, `locations/bahia-de-los-angeles.md`, `species/bonito.md`, `species/barracuda.md`  
*videos:* `Blh2BA-7Ono`, `OYOda6T3f-8`, `SczdZIq3UmE`, `A6DJoXbID4c`, `JiJYamo0QHk`, `lf3S28nh-kk`, `6EDQtQHEwFE`, `EuYOlsnxXko`, `nnrEjc-Gq2o`, `YJX-hYEIcNM`  
*gaps admitted:* No field-identification guidance for any seabird — the KB gives behavior doctrine only, no size/flight-profile/plumage cues to separate terns, gulls and shearwaters at range (only the 'white terns' phrasing in SczdZIq3UmE). | The entire shearwater doctrine rests on a single dated BD report (2022-07-21, Blh2BA-7Ono) with no corroborating source, and Cameron explicitly does not factor shearwaters in (as of 2026-08), so there is no internal cross-check. | No approach, lure or depth mechanics for fishing a confirmed shearwater raft — nothing equivalent to techniques/foamer-casting.md for terns. | No bird seasonality anywhere in the KB — the seasonal/ priors carry no calendar for when shearwaters raft or tern numbers peak in the Bight. | No Baja / Sea-of-Cortez-specific bird doctrine — locations/loreto.md and locations/bahia-de-los-angeles.md only say 'run to working birds, same read as the SoCal program'. | No timing parameters for the shearwater drive-through test (how long to wait for a circle-back) or the interval over which the 20-30 ft raft hopscotch is measured. | No positive gamefish read for gulls beyond 'locked in at an island/kelp edge with nothing better around' — the KB gives no depth, structure or conditions detail for that case. | The 2022-08-17 BD report cited for the 'sitting birds still mark the zone' rule is referenced by date only in conditions/bird-reading.md; the note does not carry a video_id for it.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## The one question that governs all three

Presence is not the signal. Per [`conditions/bird-reading.md`](conditions/bird-reading.md), the question is never whether birds are there — it's **whether they're on bait alone, or on bait being pushed by fish underneath**. Locked-in / stationary behavior reads as bait only; moving, pushing, or racing behavior reads as fish working that bait. Every bird below is a variation on that same test.

The KB's ranking is blunt: **terns and shearwaters are the reliable ones; gulls (and pelicans) mostly are not** ([`conditions/bird-reading.md`](conditions/bird-reading.md)).

---

## Terns — the best bird, and the one you run to

**Why they're trustworthy:** constant, high-eyesight surface hunters that are always flying and looking, so they surface anything edible fast (`Blh2BA-7Ono`, [`conditions/bird-reading.md`](conditions/bird-reading.md)).

**The read, in order of what you actually see through the glass:**

- **Locked-in, repeated dives on one spot = bait only.** The mechanism matters: bait under predation pressure looks *down*, not up. Surface bait that nothing is pushing from below sits still and lets a tern hit the same spot over and over without moving (`Blh2BA-7Ono`).
- **A moving dive-line = bait being pushed by fish underneath.** Terns come in, dive, fly ahead a few feet, dive again — because the bait itself is fleeing something below it. **That is the one to run on** (`Blh2BA-7Ono`). This is the exact read the bluefin router keys on ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)), and working terns are the run-to bird for yellowtail too ([`species/yellowtail.md`](species/yellowtail.md)).
- **Cast under the bird the moment it dives** — not at its general position. A *hovering* tern is waiting on a school to push bait to the surface beneath it; the dive is the signal that bait just broke the surface directly under it (`JiJYamo0QHk`, [`conditions/bird-reading.md`](conditions/bird-reading.md)).
- **Read the individual bird, not just the flock.** Birds actively diving/working a school mean it's feeding on the surface. Birds **off** the fish but still nearby mean the school **hasn't left** — it's holding just under the surface without feeding on top ("puddling") rather than gone (`A6DJoXbID4c`). The on-camera coaching behind that read is to watch the bird's *head and its small reactions*, not just whether the flock is working ([`conditions/evidence/bird-reading.md`](conditions/evidence/bird-reading.md)).
- **A single tern or two picking at the water is still worth the run.** Diving and looking rather than working a school hard — run to it and sweep it with sonar, because side-scan/up-down finds the same near-surface fish without a boil or a bird pile (`lf3S28nh-kk`, [`planning/search-and-glassing.md`](planning/search-and-glassing.md)).
- **On a dolphin pod (yellowfin):** terns work roughly **50 yd out in front of the pod**, and the yellowfin show on the **flanks and out in front** once the pod breaks a bait ball up (`ouBrIdO7d4k`, [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md), [`locations/catalina-island-backside.md`](locations/catalina-island-backside.md)). Note the KB's own flag there: the **50 yd figure belongs to the birds, not the tuna** — the tuna passage gives no distance.
- **Cameron's practice:** terns are his best bird too — he'll stop and cast on working terns, and offshore he'll follow terns to find fish **even with no other birds working** (cameron, [`conditions/bird-reading.md`](conditions/bird-reading.md), [`planning/evidence/search-and-glassing.md`](planning/evidence/search-and-glassing.md)).

**What to do once you're on them** — [`techniques/foamer-casting.md`](techniques/foamer-casting.md): run at working terns **fast**, set up **ahead of the school's direction of travel** (you cast where the fish are *going*), stop hard — 25 knots straight to neutral — and cast immediately. Budget **about 2–3 casts per school**, then move to the next one. Foamers are short-lived; do not stake one out.

**One caution on a number:** an on-the-water report coaching new tuna anglers to key on the **white terns** over pelicans and gulls did so in **72 °F** water (`SczdZIq3UmE`). The KB flags this explicitly — 72 °F is that one day's stated water temperature, **not a general threshold**, and it's corroborated nowhere else.

**Zone note:** [`locations/coronado-islands.md`](locations/coronado-islands.md) says the Coronados are where tern sign is most often seen and worth acting on — but carries its own fact-check flag that the cameron source states terns as his best bird *generally*, with no Coronados scoping. Treat "terns are especially good at the Coronados" as unsupported; "terns are the best bird everywhere" is the supported claim.

---

## Gulls — mostly noise, with two narrow uses

**Why they're unreliable:** a gull is as happy fighting over fast-food scraps as it is feeding on bait — it'll eat garbage, dead bait, or anything thrown overboard (`Blh2BA-7Ono`, [`conditions/bird-reading.md`](conditions/bird-reading.md)). There is no behavioral distinction for gulls in this KB the way there is for terns and shearwaters.

**The two things a gull is actually good for:**

1. **Locked in at an island or a kelp edge, with nothing better working** — the only case where the KB says a gull is meaningful, and it says it weakly (`Blh2BA-7Ono`). Inshore for calicos, the KB ranks **cormorants diving *in* the kelp** above gulls as a tell, and only sends you to gulls locked to a kelp edge when there's nothing better around ([`species/calico-bass.md`](species/calico-bass.md)).
2. **Paddy-finders.** For Cameron, gulls mark [kelp paddies](conditions/kelp-paddies.md) — "good sign but dumb," a general measure of life, reliable for locating floating kelp **even when they aren't marking gamefish** (cameron, [`conditions/kelp-paddies.md`](conditions/kelp-paddies.md)). Practical version: glass down-swell on gray, calm mornings and watch for gulls to find paddies before you commit gear.

**Mixed piles that include gulls:** gulls + pelicans + terns + cormorants **at an open-water current break = bait only — skip** (`Blh2BA-7Ono`). The **exception is on kelp/structure**, where a mixed pile can be a real bait event: a grunion blitz in the kelp produced bass on every cast in dirty water (`OYOda6T3f-8`). Same pile, different ground, opposite call.

Two more places gulls do carry weight, both event-specific rather than gull-specific:
- **Spring beach halibut / grunion:** staging fish show **100–500 ft off the beach** from around midday before a run, marked by **gulls, pelicans and terns working that zone** (`EuYOlsnxXko`, [`species/california-halibut.md`](species/california-halibut.md)).
- **At anchor** (San Clemente Island): chum gets pushed *up-current toward the bow* by the fish working it — watch for **birds locking on up there** and put the surface iron under them (`DnSqw4r7A1s`, [`planning/search-and-glassing.md`](planning/search-and-glassing.md)).

**Honest counter-evidence, kept as an observation and not a rule** (per the KB's doctrine-vs-observation convention): a Cedros session already written off as done reopened into a roughly 30-minute blitz **under gulls "going bonkers,"** including a triple hookup (`6EDQtQHEwFE`, [`locations/cedros-island.md`](locations/cedros-island.md)). That doesn't move the doctrine — it's one trip report — but it's why "gulls, therefore nothing" is a lean, not a law.

---

## Shearwaters — the deep-bait bird, read by the raft

Shearwaters are the reliable *other* bird, and they tell you about bait **below** diving range rather than bait on top. Four reads, all from one source (`Blh2BA-7Ono`, [`conditions/bird-reading.md`](conditions/bird-reading.md)):

- **Rafted — sitting in a tight group = sitting over deep bait,** waiting for the tide to bring it up within diving range. Not a fish call by itself.
- **The drive-through test.** Run the boat **straight through the raft**. Circling **straight back** = fish underneath. **Scattering and landing elsewhere** = bait only. This is the single most actionable shearwater move in the KB — it converts an ambiguous raft into a yes/no in one pass.
- **Rafts hopscotching 20–30 ft at a time = tracking fish holding deep.** The KB flags this one: the 20–30 ft distance and its fish-holding-deep meaning rest on that one transcript, corroborated nowhere else.
- **Racing off low in one direction from a working boil = the birds are running to the head of the school.** Follow them — **the boil they left is the tail.** That's a direction call, not just a presence call, and it's how you get ahead of a travelling school.

**Related, and worth remembering:** birds sitting still on the water still mark the zone. Trolling past sitting birds and then hopscotching rafts produced immediate bites **with nothing flying** (`HzE4FHHcvTk`, [`conditions/bird-reading.md`](conditions/bird-reading.md)).

**Trust caveat, stated plainly:** the entire shearwater model above comes from a single BDOutdoors SoCal Bight fishing report (`Blh2BA-7Ono`, 2022-07-21 — a registered source, per [`sources/source-registry.md`](sources/source-registry.md)), and **Cameron does not currently factor shearwaters into his own bird model at all** (as of 2026-08). So it's corpus doctrine with no second voice behind it.

---

## Quick reference

| Bird | Means **fish** | Means **bait / skip** |
|---|---|---|
| **Terns** | moving dive-line (dive, jump ahead, dive again); flock actively diving/working | locked repeated dives on one spot; birds off the fish but nearby = school "puddling" under the surface, not gone |
| **Shearwaters** | circles straight back after you drive through the raft; rafts hopscotching 20–30 ft; racing off low from a boil = head of the school | rafted and scatters off on the drive-through; no movement |
| **Gulls** | locked in at an island or kelp edge, nothing better working (weak) | anywhere else — treat as paddy-finder / general life only |
| **Mixed pile incl. gulls** | on kelp or structure = possible real bait event | at an open-water current break = bait only, skip |

*(Table condensed from [`conditions/bird-reading.md`](conditions/bird-reading.md).)*

---

## Seeing them in the first place

From [`planning/search-and-glassing.md`](planning/search-and-glassing.md) — this note owns the method, `bird-reading` owns the meaning:

- **Glass from a full stop, or bow into the swell at ~1 kt.** A rolling, drifting boat makes glassing useless (`DnSqw4r7A1s`, `E4vKwRaRueA`). Use image-stabilized binoculars.
- **Scan 360° in small increments, 3–4 minutes per full scan.** When a bird catches your eye, **watch it 30–40 seconds before judging it** — a single glimpse doesn't show whether the dive-line is moving or the raft is tracking. That 30–40 seconds is the whole difference between the two columns of the table above.
- **Ranges:** from deck level, expect a few terns at **~0.5–1 mi** and a big bird spot at **~2 mi**. From a hardtop, birds carry to **~2 mi** (dolphins to ~4 mi). Glass from the highest stable spot you have.
- **Space glass stations 3–4 mi apart** to tile the water at those ranges.
- **Bird radar:** gain near max, range capped at **4–5 mi** — a shorter range gives a clean return on bird schools instead of drowning them in clutter. Schools paint as **red blotches, sometimes boat-sized** (`HWx1jDTGsng`). The KB flags the 4–5 mi and red-blotch description as single-source.
- **Lens tint:** the contrast lens — **green or copper / amber**, including amber-mirror — is the one called out for picking out kelp, **birds** and dolphins (`nnrEjc-Gq2o`, `YJX-hYEIcNM`).

**Inshore/bay footnote:** in a bay, diving birds are the bay's version of a meter mark — diving ducks, western grebes, **terns** and cormorants are on bait fish, and the bait is in their reach *because* a spotty or something like it is pushing it up; stop and make a few casts every time (`YgqXf9iICyg`, [`species/spotted-bay-bass.md`](species/spotted-bay-bass.md)).

---

## What this KB does **not** tell you

- No **species-level ID guidance** at glassing range beyond "white terns" — nothing on distinguishing a tern from a gull, or one shearwater species from another (sooty, black-vented, etc.), through the binoculars.
- No **seasonality or migration timing** for any of these three birds in SoCal — the KB never says which months you should expect shearwater rafts or which terns are present when.
- **No behavioral read for gulls** the way there is for terns and shearwaters — the KB writes gulls off wholesale rather than offering a "gulls doing X = fish" test.
- **No flock-size or duration numbers** — nothing on how many terns constitutes a stop worth running to, or how long a working school typically stays up.
- **Boobies** are a flagged gap in the KB itself: Cameron considers them worth paying attention to (mostly at the Coronados), but there is **no corpus source at all** on what booby behavior distinguishes bait-only from fish-underneath ([`conditions/bird-reading.md`](conditions/bird-reading.md), [`sources/gap-report.md`](sources/gap-report.md)).
- The **shearwater model has one source and no corroboration**, and Cameron doesn't use shearwaters — weight it accordingly against the tern doctrine, which has multiple sources plus Cameron behind it.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/bird-reading.md`, `conditions/evidence/bird-reading.md`, `planning/search-and-glassing.md`, `planning/evidence/search-and-glassing.md`, `conditions/kelp-paddies.md`, `conditions/evidence/kelp-paddies.md`, `techniques/foamer-casting.md`, `species/bluefin-tuna.md`, `species/yellowtail.md`, `species/yellowfin-tuna.md`, `species/calico-bass.md`, `species/california-halibut.md`, `species/spotted-bay-bass.md`, `locations/coronado-islands.md`, `locations/catalina-island-backside.md`, `locations/cedros-island.md`, `locations/209-312.md`, `sources/source-registry.md`, `sources/gap-report.md`, `sources/transcripts/_manifest.csv`  
*videos:* `Blh2BA-7Ono`, `JiJYamo0QHk`, `A6DJoXbID4c`, `SczdZIq3UmE`, `HWx1jDTGsng`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `lf3S28nh-kk`, `ouBrIdO7d4k`, `EuYOlsnxXko`, `6EDQtQHEwFE`, `DnSqw4r7A1s`, `E4vKwRaRueA`, `YgqXf9iICyg`, `nnrEjc-Gq2o`, `YJX-hYEIcNM`  
*gaps admitted:* No field-ID guidance for telling terns, gulls and shearwaters apart at glassing range beyond the cue 'white terns'. | No shearwater species distinction (sooty, black-vented, etc.) anywhere in the KB. | No seasonality or migration timing for terns, gulls or shearwaters in SoCal — the KB never says which months to expect shearwater rafts or which terns are present when. | No behavioral read for gulls comparable to the tern dive-line or the shearwater drive-through test — gulls are written off wholesale rather than given a 'gulls doing X = fish' test. | No flock-size threshold or duration numbers — nothing on how many terns make a stop worth running to, or how long a working tern school typically stays up. | Booby behavior is a KB-flagged gap: no corpus source on what distinguishes bait-only from fish-underneath for boobies, despite Cameron rating them worth watching at the Coronados. | The entire shearwater model rests on one transcript (Blh2BA-7Ono) with no second voice, and Cameron does not factor shearwaters into his own bird model as of 2026-08. | The 20-30 ft shearwater hopscotch figure and the 4-5 mi bird-radar range / red-blotch description carry the KB's own single-source fact-check flags. | The 72 degF figure attached to the white-tern coaching is that one day's stated water temperature, not a general threshold, and is flagged as such. | The claim that terns are especially worth reading at the Coronados carries a contradicted-by-source flag in the KB — the cameron source scopes terns generally, not to that zone.

</details>
