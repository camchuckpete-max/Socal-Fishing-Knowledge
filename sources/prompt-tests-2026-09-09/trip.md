# Trip planning — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.4 | 11.6 | 12 |
| found | 1.8 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.8 | 1.8 | 2 |
| honest | 2 | 2 | 2 |
| actionable | 1.8 | 1.8 | 2 |
| **wins** | 0 | 1 | 4 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 0 | 1 | 0 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | 11.4 | 11.6 | 12 |
| Gear | None | None | None |
| Technique | None | None | None |
| Finding fish | None | None | None |
| Conditions & season | None | None | None |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 1. [trip] I am new to SoCal. I have a 22 ft center console out of Mission Bay and want to catch yellowtail on Saturday. …

**Winner:** NOW · mapping {'A': 'B2', 'B': 'B3', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 1 | 2 | 2 | 2 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 1 | 2 | 2 | **11** | regulation_without_asof |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three converge on the same correct call — Coronados, fishing by ~05:45 for the 06:42 change, three outfits rigged, off the water before the 14:00 NW build — so the separation is in what each could reach and how cleanly it handled jurisdiction. C wins because it had and used a genuine location layer: a Coronados zone page and zone guide, a La Jolla page with a real sonar read (arcs at 5-10 fathoms, holders at 90 ft), a position-only 425 page it correctly refused to plan on, and a trolling program resolved to the two Halco 190 XDDs Cameron actually owns with running specs; it also names the KB's internal contradictions (13 nm vs 13 mi, the yo-yo sizing disagreement between two notes) instead of smoothing them. B is a close second and the most navigable on the water — ranked island spots with coordinates, a seven-row meter-to-presentation table, and the mackerel-screens-for-yellowtail bait call — but it prints three La Jolla MPA boundary lines as bare positions with no jurisdiction, as-of date or verify-current, the one scoping slip in the set. A has the deepest technique execution (surface-iron cast mechanics, wind-through-the-bite) and an exemplary gap list, but it never names a single spot within a 13-mile island chain, leaving "where should I go" answered only at zone level.

- *B2 reasons:* found: right conditions/species/technique layers and honest about the absent yellowtail SST band and the 425, but answers "where" only at whole-zone granularity — never names a single Coronados spot or reads the spot library, despite listing profiles/cameron/spots.md as used. specific: dense real numbers (18 in jig hang, 2 o'clock-to-9 o'clock sweep, 5-10 fathom arcs, 25/30 lb fluoro, 1/0-2/0 hooks, 6-10 oz droppers, sabiki 100 ft/8 oz, 2 cups rock salt per 7-10 lb ice) plus the 9 Mile eval coordinates, but no island positions. sourced: note paths plus video ids throughout (NC3-3pJDEgo, D5DR7Kx42_A, VpW91AKOFVQ, 3dVc-2rsYII, 6DzbsElGE7E) and labels its Slidekick-for-7X substitution as its own inference. scoped: Mexican waters called out, Baja/SoCal options kept separate, no bare regulation stated anywhere and the absence of any yellowtail reg content is flagged. honest: long, precise gap list; flags the trolling stub, the low-confidence gaffing note, the corpus-vs-inference boundary; absolute dates only. actionable: the deepest surface-iron execution of the three (pendulum cast, reel on its side, tip down, wind through the bite, sink-outs) — a newcomer could fish it, just not choose a piece of structure.
- *B3 reasons:* found: opens with the protocol's region/waters gate, pulls the spot library, the regulatory register's admitted Mexican-licensing gap, bight geography for NW-wind durability, and says outright there is no Coronados location note. specific: eight ranked island spots with deg-min coordinates plus La Jolla/Point Loma positions, a seven-row meter/depth-band decision table (5-10 fm balls, 40-60 ft staging, stratified column, bottom balls), 25/30 lb fluoro, 12-18 in loop 3-4 ft above a 16 oz torpedo, 2-4 oz egg sinker, 15-20 ft top shot. sourced: video ids with channel plus registration/confidence status on nearly every claim (HTowqnwAMeA, wzI0lpgKT1U, w5_x6kkN-xE, 5pbA-wXoric, SAltQjih0ms). scoped: regions/waters correct, Mexican paperwork gap named with agencies, CDFW yellowtail limit flagged missing with verify — but the three La Jolla MPA boundary lines are given as bare positions with no jurisdiction, as-of date or verify-current instruction. honest: names its own blind spots (no Coronados chlorophyll given, no run distance, null boat envelope, no terminal-tackle inventory) and keeps the yo-yo cadence conflict side by side with a decision frame. actionable: clock, ladder, three rigged outfits, kelp-lean switch, and the mackerel-filters-for-yellowtail bait call make it directly runnable.
- *NOW reasons:* found: the only answer working from an actual zone layer — locations/coronado-islands.md, la-jolla.md, 425-bank.md and a species x zone guide — and it uses them to surface the real tension (Coronados peak is spring, September's Bight pattern is the coastal kelp line) with an explicit decision frame instead of a silent pick. specific: Halco 190 XDD running specs matched to two owned lures (3-11 kt, 6.5 kt optimum, 20+ ft, setback 11-55 yd default 27, 40-60 lb leader, low gunnel), La Jolla NW Corner sonar read (arcs at 5-10 fm, holders at 90 ft), yo-yo depth ladder 60/80/100 vs 120-150 vs 150-250 ft, 40-50 lb top shot, hook sizes 1/0-2/0 down to 1/2/4, paddy arcs 90-120 ft. sourced: video ids on essentially every parameter and it carries the notes' own fact-check flags forward onto numbers the angler would act on. scoped: region/waters gate stated, Coronados framed as a CONAPESCA/INM paperwork trip before tackle, MPA edges given with jurisdiction (CDFW) and verify-current, and CDFW/CONAPESCA yellowtail limits named as a flagged gap rather than guessed. honest: best of the three — flags the KB's own sst_band unknown, the yellowtail moon gap, the 13 nm vs 13 mi internal contradiction, and the yo-yo sizing contradiction between two notes rather than picking one. actionable: full circuit, timeline keyed to gray light plus the 06:42 change, trolling-to-find on gear he owns, meter setup, and a US-water Plan B with a 20-minute bail. Minor blemish: one malformed link to techniques/surface-iron-color.md and no Coronados coordinates in-line.

<details><summary>Full prompt</summary>

I am new to SoCal. I have a 22 ft center console out of Mission Bay and want to catch yellowtail on Saturday. Where should I go, when, and how should I fish it? Assume these conditions and do NOT fetch live data: Saturday 2026-09-19. SST: Point Loma kelp 66.9 F, La Jolla 67.4 F, 9 Mile Bank 67.8 F, Coronado Islands 68.5 F, the 425 bank 69.1 F. Chlorophyll: 1.1-1.4 mg/m3 along the kelp, 0.6 at the 9 Mile, 0.35 at the 425. Wind: NW 6-10 kt at dawn, building to NW 14-16 kt by 14:00. Swell: NW 3 ft at 9 s, S 2 ft at 14 s. Moon: waxing crescent (new moon 09-15). Tides at San Diego: high 06:42 (5.1 ft), low 13:05 (0.4 ft). Use the angler profile in profiles/cameron/ (boat.md, rods.md, tackle.md, trolling-lures.md, spots.md) and respect the boat envelope.

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Saturday 2026-09-19 — Yellowtail, 22 ft center console out of Mission Bay

## The call, in one line

**Coronado Islands, structure program, fishing by ~05:40, off the water by ~13:00** — with the 9 Mile Bank as the on-the-way-home fallback and the Point Loma / La Jolla kelp line as the weather-out. This is a **morning day**; the wind, not the fish, sets the end of it.

---

## 1. Why the day is short — read the sea state first

`conditions/sea-state.md` gives a working-captain go/bail set from Capt. Dave Hansen (`NC3-3pJDEgo`, 2020-11-18):

- **Wind above ~12 kt is what raises whitecaps**, and his personal cutoff is not to run above 12 kt. Your NW 14–16 kt at 14:00 is over that line.
- **Swell interval under 10 seconds is a hard bad-sea flag** — he calls sub-10-second intervals "absolutely horrible" independent of height. Your NW 3 ft **@ 9 s** is under it. (The S 2 ft @ 14 s is the benign one — the same note's steepness rule says a long-period swell is barely felt.)
- Two forecast-discipline rules from the same note: **forecast error is asymmetric** — assume it errs on the worse side and that afternoon W at the islands *strengthens* rather than eases; and **if it's windier than forecast in the morning, assume it builds all day and a small boat bails early** (7/14/22).

Add the **homebound-wind rule** (`conditions/sea-state.md`, 8/17/22): *"Runs south into Mexican paddy water put a W wind on the return leg = uphill misery. Plan return timing against the afternoon W build, not just the outbound conditions."* The Coronados are the southern run of your options, so that penalty is real and it is the reason the plan is front-loaded rather than the reason to skip the zone.

**Consequence:** everything of value happens between first light and roughly noon. Do not plan a second half of the day.

## 2. Why the Coronados

From `species/yellowtail.md` ("Where & when"):

- **"The Coronados are synonymous with yellowtail"** (`D5DR7Kx42_A`). ~13 mi from San Diego, off Mexico; the western coast is exposed to colder Pacific currents and tidal swings, **so the water stays bait-rich**.
- The honest caveat, stated in the same entry: the KB frames the Coronados as the **warming-transition (spring) classic**, and **La Jolla / the SD offshore banks** as "structure yellows on hard bottom and pinnacles, strongest warming-transition into warm-stable (spring–summer)." Mid-September is late warm-stable (`conditions/water-regimes.md`), so you are fishing this zone slightly past its documented peak.
- **Coronado yellows run "seeing-not-biting" cycles with narrow daily windows** — you will mark and even *see* fish that won't eat until a short window opens (4/21/22, `YZtX1MiT0y8`). The note's instruction: **anchor those days to tide and current, not to the clock.**

It is also your bait spot (below), it is your shortest structure run, and `profiles/cameron/spots.md` lists it as home water.

**On your SST/chlorophyll numbers — what the KB does and does not let me say.** `conditions/water-temperature.md` gives break-side rules for **bluefin** (cool side when the water's warm), **yellowfin** (warmest × cleanest, SST max × chl min) and **dorado** (~71–72 °F green-cold/blue-warm boundary). It gives **no yellowtail temperature band at all**, and `species/yellowtail.md` states no °F figures. So the 69.1 °F / 0.35 chl at the 425 is the *yellowfin* read, not a yellowtail read — I am not going to send you 40+ miles on a rule that belongs to a different fish. Yellowtail in this KB are a **structure-and-bait** fish: "hard bottom only, never mud" (`6DzbsElGE7E`). Structure is what you should be selecting on, and the Coronados and the 9 Mile are the structure inside your weather window.

The one water-quality flag: Cameron's own doctrine in `conditions/water-color.md` is that in **warm-water years** he weights chlorophyll at least as heavily as SST and **will not fish "dirty green" water for gamefish**. The kelp line is your greenest number (1.1–1.4 mg/m³) and your coldest (66.9 °F). The KB gives no chlorophyll number that defines "dirty green," so I can't tell you 1.3 crosses that line — but it is the reason the kelp is third on the list, not first.

## 3. Moon and tide — where the day's windows actually are

`conditions/moon.md`: full/new **±1 week** are elevated-probability windows. New moon was 09-15, so Saturday sits four days into the post-new window — **inside the band**. Post-moon discipline from the same note: **heavily discount report persistence** (a 3-day-old fish position is stale), and treat **absence of reports as coverage bias, not absence of fish.** A waxing crescent also means dark nights, which per `conditions/kelp-paddies.md` means *less* paddy-to-paddy redistribution than a bright moon.

`conditions/tide-and-slack.md` — the timing rules:

- **"Be at the highest-percentage zone an hour before the tide change."** Do not arrive *at* the change; **arrive before it and be fishing when it hits.** Your high is **06:42** → **be fishing by ~05:40.**
- **Window compression:** when conditions are marginal, action **compresses into the tide windows** — so anchor the plan's zones to tide times and be disciplined about arriving early. That is exactly this day.
- The **slack mechanism** (corpus, and Cameron independently): at slack the column "goes quiet," bait rises, predators hunt it better — the bite fires on the change rather than during the hard run.
- The cautionary tale in the note: a captain left sign **before slack** and regretted it — the bite was about to fire on the change (9/14/22).

Your second change is the **13:05 low** — an hour before that is 12:05, which collides head-on with the 14:00 wind build. **You are trading the low-tide window for weather.** Take the 06:42 high change, work the drop, and leave.

Note this is a **conflict with your own ops norm**: `profiles/cameron/boat.md` records normal departure **~8 am, earlier starts the exception**. An 8 am departure misses the entire morning tide window on this day. Saturday needs to be one of the exceptions.

## 4. The timeline

| Time | What |
|---|---|
| ~04:45–05:00 | Bait. `bait/making-bait.md` (`7WapaxdtjQg`): **avoid the 6:00 a.m. rush** — the 3/4-day and half-day sportboats all load then. Arrive **5:00 a.m.** or 7:00. Tell the attendant you want it **loaded light** and you're not in a rush. Hail on **VHF 11** if nobody's dockside; never board the barge; tip at the end. |
| ~05:00 | Depart Dana Landing. |
| by ~05:40 | **Fishing** — one hour before the 06:42 high change, per the arrival-discipline rule. |
| 05:40–08:00 | The A-window: slack/change on structure. Surface iron first while current is soft. |
| 08:00–11:30 | Tide dropping hard (5.1 → 0.4 ft, a 4.7 ft swing — spring-tide range, consistent with the new moon per the tide note's mechanism section). Expect the strongest push here → **yo-yo / dropper**. Read it off the kelp, not the clock (§6). |
| ~11:30–12:00 | Pull the plug and start home, ahead of the build. |
| On the run home | Glass, and check the 9 Mile if the water and your read justify a stop. |

## 5. Bait

`bait/making-bait.md` — Cameron's split: **buy sardines from the barge; when making bait, it's always mackerel.**

- **Sabiki program at the Coronados:** drop to **~100 ft** with an **8 oz** sinker. Best result on record: **5 twelve-inch mackerel on one drop.**
- Twelve-inch mackerel are big, hearty baits — **heartier than sardine**.
- Your 30-gal tank runs a **Rule 401 500 GPH pump (2.1 A, 3 A fuse)** off the single Group 24 start battery, with the NOCO GEN5X1 holding it up dockside (`profiles/cameron/boat.md`). Tank is dialed; load light per the barge rule.

Buy a scoop of sardines on the way out **and** plan on filling the tank with mackerel on arrival — that gives you both the flyline bait and the dropper-loop bait without depending on the barge having sardine.

## 6. How to fish it — the three-outfit day

`species/yellowtail.md` "Doctrine & conflicts" — **Cameron's three-outfits switching doctrine:** rig the **surface-iron** outfit, the **heavy yo-yo/dropper** outfit, and the **flyline** outfit **simultaneously**, and switch as the read (temp + bait depth) changes. The same note's framing: **the three faces are states, not fish types** — the fish roam the column and feed looking up, so no situation locks you to one presentation. You have 10 holders, 6 vertical — rig all three.

**Your on-the-water switch is the kelp**, per `conditions/current-diagnostics.md`:

| Kelp behavior | Current | Call |
|---|---|---|
| Pulled ~20 ft under | Raging | Surface presentations are **dead** — go deep/weighted |
| Laid down flat | Strong | Fishable but hard; work the down-current side |
| Resurfacing / standing up | Slacking | **Switch back** to surface / lighter |

Same note: **the chum-drift angle relative to how the boat lies separates true current from wind push** — chum straight off the stern = boat and water moving together; chum swinging off at an angle = real current cutting across. The chum bucket is your current sensor and an artificial "thumb over the hose."

### Outfit 1 — Surface iron → your **Torium 20HG** setup
Phenix Abyss PSX1009J, **10'0", 25–60 lb, moderate/fast**, 50 lb braid (`profiles/cameron/rods.md`; this is the jig-stick class in `tackle/gear-classes.md`).

Jig picks from your own box (`profiles/cameron/tackle.md`):
- **JRI-7** — ~Tady 45 class, medium-fast, "local / kelp all-rounder." Default.
- **Strictly Irons Glory** — 7", wide drawn-out kick, slow and steady; the note's explicit **change-up for picky bites / slack current** — i.e. the 05:40–06:42 slack window and any seeing-not-biting cycle.
- **Nomad Slidekick 120g** — 4.25 oz, your heaviest surface iron. `techniques/surface-iron.md` says **wind up → heavier iron** (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`); you don't own a 7X, and the Slidekick is the closest thing in your box by weight — that substitution is **my inference from the class weights, not corpus doctrine.** (Class benchmarks: a surface iron generally runs **2–3 oz** vs a **5–6 oz** yo-yo iron — `VpW91AKOFVQ`.)

Execution (`techniques/surface-iron.md`):
- Hang the jig ~**18 in** below the tip. Rod back to **2 o'clock**, **let the blank load**, sweep through to **9 o'clock** — the rod does the work; the classic mistake is shoving it out with the arms.
- **Pendulum, not side-arm** — build the swing moving the tip **up and down**, and **release on the outside of the swing** as it comes back around, not top or bottom of the arc (`VpW91AKOFVQ`, `3dVc-2rsYII`). **Lay the reel on its side through the cast** — spool rests on one bearing, farther cast (`KLoEJInlmZo`).
- **Placement beats distance.** A 75 yd cast at fish sitting 40 yd out overshoots them. On moving fish, **get ahead of the line of travel and cut it off** rather than casting into the wake.
- **Rod tip DOWN toward the water** through the whole retrieve — tip-up pulls the iron onto the surface and it stops swimming (`VpW91AKOFVQ`, `3dVc-2rsYII`).
- Steady grind the instant it lands; then **speed up for yellows**. **Reeling too fast is called out as the single most common mistake** — when fish you can see won't eat, suspect retrieve speed before changing jigs.
- **Sink it out periodically** — let it drop almost like a yo-yo, then resume the surface retrieve, to cover the column instead of only the top (`ntQXxcH5sjI`, `9tIp4n7q850`).
- **On the bite, wind through it — do not swing.** Roughly 9 of 10 strikes come as the fish grabs the iron amidships and shakes it ("dog boning"); swinging jerks the jig out of its mouth, winding drives the hooks in as it turns. **Crank as fast as you can until line starts peeling the other way** — that's the tell you're actually hooked (`3dVc-2rsYII`, `KLoEJInlmZo`).
- Relevant to your fishery specifically: **a big school at the Coronado Islands will often eat on a faster, less exacting retrieve**, while the smaller mainland-coast schools (Del Mar down to Imperial Beach) run markedly more finicky (`VpW91AKOFVQ`). That's a real argument for the Coronados over the kelp line on a day when you have limited hours.

### Outfit 2 — Yo-yo iron → your **Trinidad 40** setup
M&M on Rainshadow RCJB96XH, **8'0", XH, 40–80 lb, 4–10 oz**, **80 lb braid** — the yo-yo/heavy-iron class in `tackle/gear-classes.md`. Jigs: **Salas 6X** and **Salas CP 105**.

`species/yellowtail.md` router, structure row: **tight balls hugging structure / marks on hard bottom or pinnacles (~5–10 fathoms)** → 1) yo-yo iron, 2) dropper loop; heavy full-size iron (Salas 6X class); **hit bottom, a couple cranks off the bottom = reaction bite.** Doctrine section: heavy full-size irons **work the majority of the time on structure fish**, with vertical/flat-fall jigs **100–180 g depending on current** as the change-up (`D5DR7Kx42_A`) — you don't own knife jigs yet, so the Salas pair is the program.

Execution (`techniques/yo-yo-iron.md`):
- **Position up-current of the mark** so the drop sweeps down onto the structure.
- **Free-spool straight to the mark, thumbing the spool** so it falls under light tension and tracks straight down instead of scoping away.
- Corpus cadence: **wind as fast as you can, all the way up.** The speed is the trigger.
- Hansen's cadence, kept side by side in the note and **not reconciled** (`wzI0lpgKT1U`) — worth trying when the straight burn isn't producing: under the boat, **five or six quick cranks (~20 ft), straight back to freespool, repeat**, cycling the band where fish are marked; working water, **10 cranks then freespool to bottom**, walking the iron back. His reasoning: continuous winding pulls the iron out of the zone where suspended fish hold. **Strikes often come on the drop** — the falling iron looks like a dying baitfish.
- A heavy iron is mandatory so it **gets to the zone and stays vertical** in current.
- The **explicit trigger to go vertical**: when a hard current has pulled the kelp under or laid it flat, surface presentations are dead. When the kelp resurfaces, switch back to the iron on top.

### Outfit 3 — Flyline / dropper → your **Avet MXJ 5.8** setup
Teramar TMC90MHB2, **9'0", MH, fast, 30–65 lb**, 50 lb braid — the flyline/soft-rod class.

- **Line class:** the Cortez Bank captain's yellowtail guidance is **40 lb flyline, droppable to 30 lb if they get line-shy** (`UfuiWFVvz2E`). The detailed build in `techniques/flyline.md` (`A70kK2niu2Q`, `LTCFjqtSI8g`) runs braid → **30 lb mono top shot** → **4–6 ft of 25 or 30 lb fluorocarbon**: 25 lb gets bit better, **30 lb gives the leverage to turn a yellowtail off rocks or kelp**. On Coronados structure I'd start at 30 and drop to 25 only if you're seeing-not-biting.
- **Hooks by bait size:** **2/0** for jumbo bait and smaller mackerel, **1/0** for smaller sardines and anchovies.
- **Hook position:** nose hook (through the clear spot in front of the eyes) is the all-purpose flyline placement — bait swims naturally and stays up. **Shoulder/dorsal hook for mackerel** keeps the line up out of the way. Common failures the note names: **hook too big for the bait** (it can't swim, so it doesn't get bit), and leaving a dead bait out past the **60-second window**.
- **Dropper loop on the same heavy Trinidad rod** for the deeper marks (`techniques/dropper-loop.md`): hook tied off a **dropper loop knot or spider hitch**, **sinker 6–10 oz at the very bottom**, hook on the loop above; **a longer loop gives the bait more action — err long**; **if the current is heavy, up the weight** to hold bottom. This is the outfit that soaks in a holder while your hands are on the iron.

Spare/backup: your **Lexa 400** (Okuma PCH-C-901H, 9'0", H, ~20–60 lb, 50 lb braid) is the workhorse all-around cast rod if you break something off.

**Not recommended:** trolling to locate. `species/yellowtail.md` carries that row as an explicit **"⚠ Flagged stub — no corpus source yet"** — trolling hard baits/feathers is a standard locate method in the real fishery, but **no source in this KB covers it for yellowtail**, so nothing in your trolling box (Madmacs, Husky Magnums, Halcos, cedar plugs) is a KB-sanctioned yellowtail method. Search by glassing and metering instead.

## 7. Picking the actual piece of structure once you're there

**Structure typology first** (`locations/island-structure.md`, `conditions/current-structure.md`) — identify which of the three a spot is *before* you commit:

- **Land-attached perpendicular ridges are two-directional** — they only produce on **parallel current** (running along the shoreline, uphill or downhill). **Current straight into the beach is marginal; straight off the beach is dead.** A perpendicular ridge on an off-the-beach current is a non-starter no matter how good the water looks.
- **Standalone banks fish in any direction**, but each has its own preferred directions you learn spot by spot.
- Bias toward the **up-current face** — that's where nutrients are forced up and the food chain stacks.
- **Kelp-bed corner rule** (`kzD0kSnnVPw`, medium confidence, and La Jolla / Point Loma are among his named beds): **current running downhill → work the NW corner of the kelp; running uphill → work the SE corner.**

I can't pre-resolve any of that for you — **no current direction was given for Saturday**. Read it on arrival off the kelp lean and the chum drift, then pick the face.

**On the meter** (`species/yellowtail.md` "Finding them", `planning/electronics-and-sounder.md`) — your Garmin GPSMAP 840xs:

- **Hard bottom only, never mud.** "They're not going to be out in the mud... they're always going to be on the hard bottom." Read bottom hardness off **return thickness** — thin/faint = sand/mud, thick and dark = rock. Works on any brand, no special mode (`6DzbsElGE7E`). Grade the bottom *before* you look for fish sign on it.
- **Structure/bottom yellows = tight balls hugging the structure**, the classic read being **arcs / boil-ups at ~5–10 fathoms (30–60 ft) near structure**. "We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`).
- **A thin, lighter mark riding higher than the bait ball can be the yellowtail itself**, pushing bait up off the rocks — *that's* the sign to commit, not the bait pile alone (`6DzbsElGE7E`).
- **Photograph the meter during bites** so you build your own library of marks that paid off.

**Anchoring geometry** (`planning/search-and-glassing.md`):

- **Grade the mark with repeated passes** — idle over the high spot, mark the peak, turn around and **re-drive the same track** to confirm bait/fish sign before committing.
- **Drop the anchor in the adjacent sand, not on the rock** — set up **in front of** the structure so your **lines drift back onto it** (`6DzbsElGE7E`, `xI9tPJFXbUM`).
- **Midwater/gamefish → anchor up-current, standoff scaled to current strength.** And specifically: **break-off risk (yellowtail) → anchor further still**, so a hooked fish has room before it reaches the structure. On 25–30 lb fluoro over Coronados rock that standoff is the whole game.
- The **"treadmill is off" tell** (`conditions/current-diagnostics.md`): bait pointing in all directions and **fish metering but not biting** = no current, marks will not convert. Read it as move-or-wait, and wait for the change rather than grinding.

## 8. On the run — glassing and paddies

`planning/search-and-glassing.md`:
- **Glass from a full stop, or bow into the swell at ~1 kt.** Image-stabilized binoculars. **360° in small increments, 3–4 minutes per full scan.** When you catch a bird, **watch it 30–40 seconds** before judging it.
- **Deck-level ranges** (you have no hardtop): a few terns at **~0.5–1 mi**, a big bird spot at **~2 mi**. Space glass stations **3–4 mi apart**. Along a bank, run the **contour at 16–18 mph** with a lookout **~30° off each bow**.
- **Terns are the best bird** — both the corpus and your own model agree (`conditions/bird-reading.md`). **Moving dive-line = bait being pushed by fish underneath** (run on it); **locked repeated dives on one spot = bait only**. Your own practice on record: follow working terns even with no other birds working. Also worth knowing: **birds off the fish doesn't mean the school left** — it means the school is "puddling," present but not surface-feeding.
- **Gray-calm mornings:** scan **down-swell** a quarter-mile out and watch **kelp paddies roll over the swell crests** — the movement gives them away when nothing is flying.

**Any paddy you pass** (`conditions/kelp-paddies.md`): **drive right up to it like it's the dock** — a paddy isn't spooky (`ZFqe49jRgA0`). Look in the water, then check the meter for **boomerang-shaped arcs, typically 90–120 ft** down. Give it **about a minute, maybe two** — a look, a sounder pass, one bait. Then move: **fish move paddy-to-paddy only at night, so a dry paddy stays dry all day.** Paddies line up with the current — **N–S in open water, along the contour near a bank edge** — so once you find a good one, search its line. Fair warning from the same note: **the best paddy water is south of Catalina/San Clemente and from Dana Point to Oceanside southward**, and the more boat traffic and the closer to a dock, the less willing the fish. Paddies are a bonus on this trip, not the plan.

## 9. Fallbacks, ranked

1. **9 Mile Bank** (67.8 °F, 0.6 chl) — covered by the yellowtail note's "La Jolla and the SD offshore banks — structure yellows on hard bottom and pinnacles." `locations/zone-lexicon.md` tells you what it physically is: named for sitting **9 statute miles off the coast**, not for a fathom depth, and it carries **many closely spaced high spots of similar depth rather than one dominant peak** — in places up to roughly 600 ft (`Rf1HKJG-SDg`). Practically that means it's a **search box, not a pin**: budget it as a spot-check on the way home, not an expedition, and grade bottom hardness at each high spot before you fish it. It's also one of your BightSST eval anchors (North 9 Mile 32 38.000 / 117 26.000; South 9 Mile 32 32.000 / 117 21.000 — `profiles/cameron/spots.md`).
2. **Point Loma / La Jolla kelp line** (66.9 / 67.4 °F, 1.1–1.4 chl) — the weather-out. `species/yellowtail.md`: "**Coastal kelps** — kelp-line and coastal-structure yellows along the beach from LA to San Diego in the warm-stable regime (summer)… **Surface iron along the kelp edge is the classic approach** (cameron; corpus coverage thin)." Note that honesty flag in the KB itself — this entry is thin. Expect finickier fish than the islands per the Del Mar-to-IB read above. Its virtue is that it's five minutes from the jetty when the wind arrives.
3. **The 425** — I'm not sending you there. See gaps.

## 10. Boat and ops (from `profiles/cameron/boat.md`)

- **Trim:** at least one person forward underway, bean bag on the bow. Running out: ~100 lb ice in the cooler, one on the bow bag + one on the seat forward of the console. **No trim tabs** — engine trim is your only attitude control, which matters in a 3 ft @ 9 s NW chop.
- **Coming in:** **drain the 30-gal bait tank** (heavy stern water) and **shift one person aft** to offset. Do this before the beat home, not during it.
- **Bilge pump is manual-switch only, no float switch**, and the bilge is very small — check it yourself on a wet ride.
- **Ice: 100–125 lb per trip.**

## 11. Fish care

- **Gaff:** yellowtail up to 40–50 lb fall in the **3-in hook, ~6-ft gaff** class (`fish-care/gaffing.md` — note this whole note sits at **low confidence**, it's a sponsored segment).
- **Cold chain** (`fish-care/dorado-and-general.md`, general principles, all species): a **salted slurry** chills faster and colder than bare ice water — **rock salt ~2 cups per 7–10 lb bag of ice** plus a splash of seawater to wet it. Get fish into the cold fast and keep them there; a fish baking on a hot deck loses quality the whole time. Bring a **car cooler** for the drive home.
- One field move worth knowing before you hook a fish at the Coronados: **sea lion depredation at the boat** (`species/yellowtail.md` router, `mdhoEQPqpng`) — wind continuously, never pump; **once the sea lion grabs the fish, throw the reel into free spool** to give total slack (it reads as the line breaking, so the sea lion lets go), then wind fast to recover.

---

## What this KB could not tell me

I want to be explicit about where I stopped, because several of these bear directly on Saturday:

- **There is no Mexican fishing licence / border-crossing / permit guidance anywhere in this KB.** The Coronados are Mexican waters. Sort that out independently before you go — I have no basis in these notes to tell you what you need.
- **No yellowtail temperature band.** Nothing in the KB says which of 66.9 / 67.4 / 67.8 / 68.5 / 69.1 °F yellowtail prefer.
- **No chlorophyll threshold for "dirty green."** Your own doctrine says don't fish it; the KB never quantifies it.
- **No page for the 425 bank** — no location note, no distance from Mission Bay, no yellowtail history. I can't plan a run I can't size, and its warmest-and-cleanest signature is the *yellowfin* rule from `conditions/water-temperature.md`, not a yellowtail rule.
- **No September SoCal yellowtail prior.** `seasonal/september.md` covers yellowtail only for **BOLA, Baja** (bottom program, dropper loops + yo-yo iron); its SoCal lineup is bluefin, dorado, yellowfin. So the seasonal layer is effectively silent on your target this month.
- **No current direction** was given for Saturday, so the parallel-current rule and up-current-face selection have to be read on the water rather than planned.
- **No stated sea-state limit for the Panga 22 itself** — only top speed ~35 kt and idle ~1.5 kt. The 12 kt / sub-10 s thresholds I used are a registered captain's personal cutoffs on his own boats, not your boat's envelope. Your call.
- **No Mission Bay channel exposure figures.** The only entrance-swell geometry in the KB is your own chart work for the **San Diego Bay** entrance (open to ~160°–186°, channel axis 186°) — different inlet, don't apply it.
- **No sunrise/first-light time**, so "fishing by 05:40" is driven purely by the tide-change rule, not by light.
- **No regulations section** on the yellowtail note — no bag limit, size limit, or gear rule of any jurisdiction.
- **No corpus source for trolling to locate yellowtail** (explicitly a flagged stub), and **no yellowtail-specific 9 Mile Bank doctrine** beyond the general "SD offshore banks" line.
- **You own no Salas 7X**, the corpus's windy-day heavy surface iron; substituting your Nomad Slidekick 120g is my inference from the 2–3 oz vs 5–6 oz class weights, not something the KB says.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `species/yellowtail.md`, `seasonal/september.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/moon.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `conditions/upwelling-and-turnover.md`, `locations/island-structure.md`, `locations/zone-lexicon.md`, `locations/bightsst-eval-targets.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `tackle/gear-classes.md`, `lures/iron-jigs.md`, `bait/making-bait.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `profiles/cameron/trolling-lures.md`  
*videos:* `D5DR7Kx42_A`, `YZtX1MiT0y8`, `UfuiWFVvz2E`, `ZFqe49jRgA0`, `6DzbsElGE7E`, `NC3-3pJDEgo`, `VpW91AKOFVQ`, `3dVc-2rsYII`, `KLoEJInlmZo`, `ntQXxcH5sjI`, `9tIp4n7q850`, `wzI0lpgKT1U`, `xI9tPJFXbUM`, `7WapaxdtjQg`, `SczdZIq3UmE`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `fri_BWI-VA0`, `I84uoay_jwQ`, `4xzK7YaXK5s`, `Rf1HKJG-SDg`, `kzD0kSnnVPw`, `mdhoEQPqpng`, `HGyL7pXy3Ts`  
*gaps admitted:* No Mexican fishing licence, permit, or border-crossing guidance anywhere in the KB, despite the Coronado Islands being Mexican waters. | No yellowtail temperature band or preferred SST range — the KB's break-side SST rules cover only bluefin, yellowfin and dorado, so none of the five given SST values can be scored for yellowtail. | No chlorophyll threshold defining 'dirty green' water, so Cameron's don't-fish-dirty-green doctrine cannot be applied to the given 1.1–1.4 / 0.6 / 0.35 mg/m3 numbers. | No note of any kind on the 425 bank — no location page, no distance from Mission Bay, no yellowtail history, so it cannot be planned. | No September SoCal yellowtail prior — seasonal/september.md covers yellowtail only for BOLA, Baja (bottom program), with bluefin/dorado/yellowfin as the SoCal lineup. | No yellowtail-specific doctrine for the 9 Mile Bank beyond the general 'La Jolla and the SD offshore banks' line and the bank's naming/bathymetry description. | No current direction was supplied for Saturday, so the parallel-current rule, up-current-face bias and kelp-corner selection cannot be pre-resolved and must be read on the water. | No stated sea-state or wind limit for the Panga Marine Marquesas 22 itself; the 12 kt / sub-10 s thresholds used are a registered captain's personal cutoffs on his own boats, not this boat's envelope. | No Mission Bay entrance/channel swell-exposure figures — the only entrance geometry in the KB is Cameron's San Diego Bay entrance work (160°–186°), a different inlet. | No sunrise or first-light time for 2026-09-19, so the 05:40 on-station target is driven only by the tide-change rule. | No regulations content on species/yellowtail.md — no bag limit, size limit, season or gear rule for any jurisdiction. | No corpus source for trolling to locate yellowtail — the router carries it as an explicit flagged stub, so nothing in Cameron's trolling-lure inventory is a KB-sanctioned method for this target. | Cameron owns no Salas 7X (the corpus's windy-day heavy surface iron); substituting his Nomad Slidekick 120g is an inference from the 2–3 oz vs 5–6 oz class weights, not KB doctrine. | No knife jigs or slow-pitch setup in the profile, so the corpus's 100–180 g vertical/flat-fall change-up for structure yellows cannot be resolved to owned gear. | The gaffing note sits at low confidence (sponsored segment), so the 3-in hook / ~6-ft gaff sizing is the weakest-supported recommendation given.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

# Saturday 2026-09-19 — Yellowtail out of Mission Bay

Short version: **run the Coronado Islands, be fishing by 05:45, fish the gray-light/high-slack window hard on surface iron, switch to yo-yo iron and dropper loop as the ebb builds, and be headed home before the 14:00 wind.** La Jolla / Point Loma is your inside fallback. Do not plan on the 425.

---

## 1. The envelope first (day-plan protocol step 1b)

Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), the region/waters filter is set before any species note is opened:

- **regions:** `socal-bight` + `baja-pacific-north`. The Coronado Islands sit in `baja-pacific-north` — [`species/yellowtail.md`](species/yellowtail.md) says so explicitly ("Ensenada, Punta Banda, and the Coronados are all `baja-pacific-north`"). Yellowtail are gated to both regions, so the fish clears the filter.
- **waters:** `island`, `bank`, `nearshore-coast` ([`locations/regions.md`](locations/regions.md)). Yellowtail carry `island, bank, nearshore-coast, open-ocean`, so every option below is in-gate.

**Two things I have to flag before the plan, not after:**

1. **Your boat envelope is blank in the profile.** [`profiles/cameron/boat.md`](profiles/cameron/boat.md) has `home_port: null`, `range_nm: null`, `sea_state_max_ft: null` — deliberately, with a comment saying the protocol must **ask** rather than assume. So: *what is your comfortable one-way range, and what sea state do you turn around at?* Everything below is built conservatively (inside the Coronados band) because the KB will not authorise a longer run on my behalf. The platform facts it does give: Panga Marine Marquesas 22, single 115 hp Yamaha, tops ~35 kt, idles ~1.5 kt, **no trim tabs**, 30-gal bait tank on a **single starting battery** (Rule 401, 500 GPH, 2.1 A), 100–125 lb ice per trip, normal departure ~8 am.
2. **The Coronados are Mexican water and this KB cannot tell you what paperwork you need.** [`sources/regulatory-claims.md`](sources/regulatory-claims.md) carries an explicit **"Known gap"**: Mexican licensing and entry requirements are absent from the knowledgebase — FMM, CONAPESCA fishing permit, passport. The register names the agencies (CONAPESCA for permits, INM for the FMM) and says nothing more. Sort that out before Saturday; I am not going to guess it for you.

---

## 2. What your conditions actually say

**Regime.** September is late **warm-stable** ([`seasonal/september.md`](seasonal/september.md), `5to3Q5P7w90` + cameron; [`conditions/water-regimes.md`](conditions/water-regimes.md), cameron doctrine).

**Temperature.** Your board runs 66.9 °F at the Point Loma kelp → 67.4 La Jolla → 67.8 at the 9 Mile → 68.5 at the Coronados → 69.1 at the 425. That is a ~2.2 °F differential across the whole plan area. [`conditions/water-temperature.md`](conditions/water-temperature.md) is emphatic that **the value is usually not the absolute number but which side of a break a species sits on** — and the Mission Bay chartplotter demo in [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md) (`uyjTdgIw-1k`) shows the same habit: read the differential, work the edge, don't stop at the first warm number. **Honest limit: this KB has no yellowtail SST band.** The break-side rules cover bluefin (cool side in warm water, warm side in cold), yellowfin (warmest × cleanest) and dorado (~71–72 °F green-cold/blue-warm boundary) — yellowtail get no number. Cameron's own stated model in [`species/yellowtail.md`](species/yellowtail.md) is that **calendar date doesn't matter; water temperature and bait do**, so treat 68.5 at the islands as "the warmest structure water you can reach," not as a threshold that has been met.

**Water colour.** 1.1–1.4 mg/m³ along the kelp is the greenest water on your board; 0.6 at the 9 Mile; 0.35 at the 425. [`conditions/water-color.md`](conditions/water-color.md): *not all green water is equal* — chlorophyll has an **age**, and the fishable water is an **edge**, not the middle of a mass. Cameron's own doctrine there: in warm-water years he weights chlorophyll **at least as heavily as SST** and **will not fish dirty green water for gamefish**. Two consequences:
- The kelp-line green is not automatically bad — but the play inshore is the **seam** between it and cleaner water outside, not the middle of it.
- **The 425 (69.1 °F / 0.35) is the warmest × cleanest combination on your board — and that is the *yellowfin* read, not the yellowtail read.** It is an offshore bank deep in Mexican water with your range unstated and the wind building. It is off the plan.

**Sea state.** [`conditions/sea-state.md`](conditions/sea-state.md):
- The **steepness rule** — flag any leg where period in seconds approaches height in feet. NW 3 ft @ 9 s does not trip that; S 2 ft @ 14 s is a non-event (10 ft @ 15 s from the south "is barely felt").
- **Kept side by side, not reconciled:** Capt. Dave Hansen's working thresholds (`NC3-3pJDEgo`, 2020-11-18, registered voice but single-mention — medium) call **any sub-10-second interval "absolutely horrible"** and put his personal don't-run cutoff at **wind over ~12 kt**. Your NW 9 s and your 14–16 kt afternoon both land on the wrong side of his lines. His named unfishable combo is 12–15 kt with 4–8 ft @ 9 s — you are not there at dawn, you are drifting toward it by mid-afternoon.
- **Unforecast-wind heuristic:** if it is windier than forecast in the morning, **assume it builds all day — a small boat bails early** (7/14/22). And forecast error is asymmetric: afternoon wind at the islands **strengthens rather than eases** (Ep. 6). Treat 14–16 kt at 14:00 as the optimistic case.
- **Bathymetric slop:** where current accelerates over a ridge or shoal the swell stands up locally. Expect the island ridges and high spots to be lumpier than the open-water numbers suggest.

**Wind geography works in your favour.** [`locations/bight-geography.md`](locations/bight-geography.md) (`HzE4FHHcvTk`): in a NW event, the northern Channel Islands and the LA/Ventura shelf get crushed (5–8 °F rollover), **south of Newport is less prone**, and **the Coronados, the tuna grounds, Catalina and San Clemente held their water through the blow**. Your target zone is on the durable side of that map.

**Moon.** New moon was 09-15; Saturday is day 4 of the waxing crescent. [`conditions/moon.md`](conditions/moon.md) treats full/new **±1 week** as elevated-probability windows with the **leading** days strongest — so you are inside the window but on the trailing side. The moon peak itself is a **relocation** event, and post-moon discipline is to **heavily discount report persistence**. Practical read: don't build the day around anyone else's four-day-old spot.

**Tide — this is the timing spine of the day.** High 06:42 (5.1 ft), low 13:05 (0.4 ft): a 4.7 ft drop over 6 h 23 m, so a **hard ebb runs through the entire fishable middle of the day**. [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md):
- **Arrival discipline — be at the highest-percentage zone an hour before the change.** For the 06:42 high that means **fishing by 05:45**, not arriving at 05:45.
- **Window compression:** when conditions are marginal, action compresses into the tide windows and you anchor the plan's zones to tide times. With a building afternoon wind, this is a marginal-conditions day. Anchor to the tide.
- The Coronados have a documented behaviour that makes this worse if you ignore it: yellowtail there run **"seeing-not-biting" cycles with narrow daily windows** — you will mark and even see fish that won't eat until a short window opens (`YZtX1MiT0y8`). *"Anchor those days to tide and current, not to the clock."*
- Add the gray-light point from Ensenada (`0dIwWiOc1NY`): yellowtail **feed hardest during gray light early in the morning**; a stop fished after that window, with the tide "off," produced no yellowtail.

Your gray-light window and your 06:42 tide change **land on top of each other**. That is the whole day in one sentence.

---

## 3. Where to go

### Primary: the Coronado Islands

Why: *"The Coronados are synonymous with yellowtail"* (`D5DR7Kx42_A`, [`species/yellowtail.md`](species/yellowtail.md)). ~13 mi from San Diego, off Mexico; the western coast is exposed to colder Pacific currents and tidal swings so the water stays bait-rich. It is the warmest structure water you can reach (68.5 °F), it is on the wind-durable side of the bight map, and it is Cameron's home water ([`profiles/cameron/spots.md`](profiles/cameron/spots.md)).

Spot ladder, coordinates straight out of [`sources/spot-lists.md`](sources/spot-lists.md) (deg min.mmm, N lat / W lon):

| Order | Spot | Position | Why in this order |
|---|---|---|---|
| 1 | **East of Pukey Point** | 32 27.000 / 117 14.100 | The library tags this one explicitly **"yellowtail & rockfish."** North end (first structure you reach) and on the east/lee side of a NW wind. |
| 2 | **Pukey Point** | 32 26.850 / 117 18.000 | North Island proper; the west-side counterpart — take it early while it's still light air. |
| 3 | **Middle Grounds** | 32 25.810 / 117 15.950 | Mid-chain hard bottom. |
| 4 | **Ribbon Kelp** | 32 24.800 / 117 13.880 | Kelp = your live current gauge (below). East side. |
| 5 | **Lighthouse** | 32 23.290 / 117 14.570 | |
| 6 | **5-Minute Kelp** | 32 22.940 / 117 13.515 | Kelp, east side. |
| 7 | **South Kelp Ridge** | 32 22.000 / 117 13.260 | Furthest south of the kelp spots. |
| — | **Rockpile** | 32 17.620 / 117 10.030 | Southernmost, and a BightSST model anchor. Only if you're early and the wind is still light — it's the longest run back into a building NW. |

**Before you commit to any one of them** — [`locations/island-structure.md`](locations/island-structure.md) typology, which decides whether today's current even lets a spot work:
- **Land-attached perpendicular ridges are two-directional.** They only produce on **parallel** current (running along the shoreline). Current straight into the beach is marginal; straight off the beach is **dead**. On a 4.7 ft ebb you will have real current — check its direction against the ridge before you burn 40 minutes on it.
- **Standalone banks fish any direction**, but each has its own preferred directions you learn spot by spot.
- **Coastal deep spots default-prefer downhill (N→S) current.**

### Inside fallback: La Jolla / Point Loma

If the crossing is a no-go, or you bail off the island early:
- **La Jolla NW Corner** 32 50.630 / 117 18.460 · **La Jolla Shelf hardbottom** 32 51.300 / 117 19.250 · **The Bump** 32 51.490 / 117 16.910 · **The Half** 32 51.220 / 117 17.620 · **Marine Street** 32 50.175 / 117 17.715.
- **Watch the MPA lines the library itself annotates:** The Cove — *stay west of the MPA at 117 16.400*; Windansea — *stay north of the MPA at 32 49.573*; Crystal Pier — *stay south of the MPA at 32 47.945*.
- Point Loma hard structure: **The Dropoff** 32 39.150 / 117 15.720 · **Point Loma Pipe** 32 40.350 / 117 17.000 · **New Hope Rock** 32 41.140 / 117 15.990 · **5 Tanks** 32 40.870 / 117 16.160.
- **Be honest about the prior:** [`species/yellowtail.md`](species/yellowtail.md) files La Jolla and the SD offshore banks as *"structure yellows on hard bottom and pinnacles, **strongest warming-transition into warm-stable (spring–summer)**."* Mid-September is the late end of warm-stable — this is a weaker prior than the islands, not an equal one. It is also the greenest water on your board (1.1–1.4), so per Cameron's colour doctrine work the **edge** of it, not the middle.

### Not on the plan

- **The 425** (32 15.000 / 117 23.200): warmest × cleanest is the yellowfin read, not a yellowtail structure read; deep in Mexican water; range unstated; wind building.
- **The 9 Mile** (North 32 38.000 / 117 26.000 · South 32 32.000 / 117 21.000 · Lower 32 32.500 / 117 20.500): the KB carries **no yellowtail doctrine for the 9 Mile at all**. All it tells you is the naming ([`locations/zone-lexicon.md`](locations/zone-lexicon.md), `Rf1HKJG-SDg`): named for sitting **9 statute miles off the coast**, not for a fathom depth, carrying **many closely spaced high spots of similar depth** rather than one dominant peak, coming up to roughly 600 ft in places (the source hedges that figure). Use it as a look-on-the-way, not a destination.

---

## 4. The clock

| Time | Do this |
|---|---|
| **04:30–05:00** | Bait. [`bait/making-bait.md`](bait/making-bait.md) (`7WapaxdtjQg`, `bM2vUS1B-yQ`): the SoCal half-day/3-4-day fleet all load at **06:00** and the line forms by quarter to six — target **05:00, or 04:30**. Tell the attendant you want it **loaded light** and you're not in a rush; hail on **VHF 11** if nobody's visible; tip at the end. If the receiver is short, Cameron's fallback is sabikis (below). |
| **~05:00** | Depart Dana Landing. **This breaks your normal ~8 am departure** (boat.md) — deliberately. An 8 am start puts you on the water after both the gray-light window and the 06:42 change. |
| **by 05:45** | **Fishing** on spot #1 — an hour before the 06:42 high, per the arrival-discipline rule. Not arriving. Fishing. |
| **05:45–08:30** | The A window: gray light + the tide change. Surface iron first, bait in the water, third rod ready. |
| **08:30–12:00** | Hard ebb. This is current-driven structure fishing — the kelp tells you which presentation (below). Move down the ladder; if two spots are dead, prospect with a troll rather than grinding. |
| **~12:00** | **Go/no-go on the second window.** If the wind is already at the top of the forecast, leave — "windier than forecast in the morning → assume it builds all day, a small boat bails early." |
| **12:05–13:30** | Only if it's still light: the **13:05 low change** is your second tide window. Take it on the **east/lee side** (5-Minute Kelp / South Kelp Ridge / East of Pukey Point), then run. |
| **before 14:00** | Off the outer water. Coming in, drain the 30-gal bait tank and shift one person aft (boat.md trim routine); at least one person forward on the bean bag underway. |

**Calibrate your patience before you leave the dock.** [`species/yellowtail.md`](species/yellowtail.md) (`HTowqnwAMeA`, Nate Winnicki, BDOutdoors — registered voice, medium): a day producing **12–15 bites was called an anomaly**; **a good day of local yellowtail fishing is three or four bites.** At that rate, two fishless hours is not evidence your technique is wrong. Held side by side with the same source's opposite lesson: their crew anchored a spot they'd been told was an anchor spot, fished it 1–1.5 hours for a couple of bites, then pulled the hook and started moving and slow-trolling — and **roughly quadrupled their bite rate**. *"You can't really be glued to a certain technique or style of fishing."* The decision frame between those two: **stay put while your reads (bait, marks, current) still say fish are there; move when the reads have gone empty, not when the clock has.**

---

## 5. Rig-up — three outfits at once, from your own inventory

Cameron's stated doctrine in [`species/yellowtail.md`](species/yellowtail.md): **rig the surface-iron outfit, the heavy yo-yo/dropper outfit, and the flyline outfit simultaneously**, and switch as the read (temp + bait depth) changes — the day moves between faces of one population, not between fish types. From [`profiles/cameron/rods.md`](profiles/cameron/rods.md) and [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md):

### A. Surface iron — Torium 20HG on the Phenix Abyss 10'0" (25–60 lb), 50 lb braid
Your listed "full surface iron setup."
- **Jig:** start with the **JRI-7** (light blue, ~Tady 45 class, medium-fast — your listed "local/kelp all-rounder"). Change-up for a picky bite or slack current: **Strictly Irons Glory** (light blue, wide drawn-out kick, slow and steady). If you want to cover the column: **Nomad Slidekick 120g** (6", 4.25 oz) — [`lures/iron-jigs.md`](lures/iron-jigs.md) classes it as a crossover you can sink out.
- **Retrieve:** steady grind, tip down. The mechanism (Dan Wade, `yn1suHH6b1Y` + `Ec2GaNpiOHI`, registered voice, high confidence — stated in both videos): the jig runs a **serpentine action, and every third or fourth time it kicks out to the side — that kick-out is what triggers the bite**, because it imitates the one baitfish that separated from the ball. If the jig is swimming flat, speed it up / slow it down to make it kick.
- **Don't over-crank.** These irons were designed around the **4:1 Penn Jigmaster**; **6.5–7.5:1 is too fast** (`Ec2GaNpiOHI`). Kept side by side: a Tackle Express clip (`pOFsjDTqaxY`, unregistered, medium) argues a 7:1 is a good torque middle-ground for big yellowtail. Your Torium sits in that argument; err slow.
- **Colour rank is swim → size/weight → colour, last** ([`techniques/surface-iron.md`](techniques/surface-iron.md)). Stop agonising over it.
- **Gear gap to name:** the wind-up rule says step to a **heavier iron, Salas 7X class**, to punch the cast through wind (`D5DR7Kx42_A`). **There is no Salas 7X-class heavy surface iron in your box.** The closest you own is the Nomad Slidekick at 4.25 oz. Traditional surface irons run ~2–3 oz (or 1¾–2¾ oz on the second logged data point) against a yo-yo iron's 5–6 oz (`VpW91AKOFVQ`, capt-scotty-brothers, registered, high).

### B. Yo-yo / bottom — Trinidad 40 on the M&M RCJB96XH 8'0" XH (40–80 lb), 80 lb braid
Your listed yo-yo rod.
- **Jig:** **Salas 6X** (blue) or **Salas CP 105** — the classic heavy yo-yo benchmarks.
- **Execution** ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)): position **up-current** of the mark so the drop sweeps onto it; **free-spool straight down, thumbing the spool** so it tracks vertical instead of scoping away; then **wind as fast as you can.** Rod tucked **under the left armpit** once it's in gear — *you cannot crank it too fast, but it is easy to crank it too slow* (`RNRFrfepiW0`, Steve Carson, registered, high). **On the bite, don't set the hook — keep cranking through it** (`5pbA-wXoric`). From the Coronados roundup doctrine: hit bottom, and **a couple of cranks off the bottom is the reaction bite** (`D5DR7Kx42_A`).
- **Cadence conflict, kept side by side with a decision frame.** Capt. Dave Hansen (`wzI0lpgKT1U`, registered, high) defines yo-yoing as **10-crank bursts then straight back to free-spool**, staying down in the strike zone and walking the iron back over as much as 150 yards — his argument is that winding continuously to the top pulls the jig out of the band the fish are holding in. The continuous-wind doctrine above says the speed *is* the trigger. **What the choice turns on:** fish pinned to a bottom mark under the boat → continuous rip; fish suspended or spread through the column → burst-and-drop keeps the iron in their band. Section order here is not a ranking.
- **Jig weight tracks the water, and it's a time budget not an action argument** (`HTowqnwAMeA`): light current + nice weather → small jig; **wind or strong current → upsize**, because *"you don't want to spend the majority of your time in free spool waiting for your lure to hit bottom."* On a 4.7 ft ebb, err heavy.
- **Line class:** *40 lb works, 50 is better, 60 is better still, "because the fish don't care"* (`5pbA-wXoric`). Your 80 lb braid is well inside that.

### C. Flyline / live bait — Avet MXJ 5.8 MC on the Teramar TMC90MHB2 9'0" MH (30–65 lb), 50 lb braid
Your listed flyline setup.
- **Leader:** 4–6 ft of **25 lb or 30 lb fluorocarbon** — 25 gets bit a little better, 30 gives the leverage to turn a fish off the rocks (`A70kK2niu2Q` / `LTCFjqtSI8g`, ray-sharifi, registered, medium). **Hook to bait size: 2/0 for jumbo bait and smaller mackerel, 1/0 for small sardine/anchovy.**
- **If they're seeing-not-biting** (the documented Coronados failure mode): downsize the leader and the hook and **wait for the window**. The dated Coronados data point for exactly this is in [`tackle/hooks.md`](tackle/hooks.md) (`F9XjGMEvvag`, 2018-11-20, unregistered — medium): as a Coronados bite was picking up, the tip was to downsize to **smaller J hooks for flylining fluorocarbon — Owner Ringed Flyliner sizes 1, 2 and 4.**
- **Bait choice is a species filter, and this is the single most useful line in the KB for your day.** [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md) (`w5_x6kkN-xE`, dave-hansen, high): fishing **live mackerel** rather than the smaller sardine or anchovy at San Clemente, Catalina **or the Coronado Islands skews the catch toward yellowtail specifically**, screening out the calico, barracuda and bonito bycatch a smaller bait draws. Yellowtail have been seen eating mackerel up to **1.5 lb**, sometimes five or six fish attacking one mackerel at once.
- **Hook placement, hard rule for mackerel:** **butt hook** (back near, not through, the vent) for **zero-weight flyline only** — pulling on it reads to the bait as something biting its tail, so it bolts away from the pull; throw it to the edge of a boil and jerk the tail to send it at the fish. **Nose hook becomes mandatory the moment any weight goes on** (dropper loop, sliding sinker, rubber core) — a butt-hooked bait under a sinker gets dragged backward and stops looking like a feeding fish.
- **If bonito take over the column and intercept your baits** — a documented yellowtail-day killer in this note (a planned yo-yo/surface-iron program at the tuna pens was abandoned to bonito; dead sardines turned it) — the presentation fix is the **sliding sinker**: a **2–4 oz egg sinker straight to a 2/0–4/0 J hook**, scaled to wind and depth, on 30 lb live-bait class for 12–22 lb grade fish (`yGXSrUauo2w`, Steve Carson, registered voice, single mention — medium). The weight gets the bait *under* the bonito layer and in front of the yellowtail faster.

### D. Dropper loop — same Trinidad 40, when the marks are balled and dead
[`techniques/dropper-loop.md`](techniques/dropper-loop.md), SoCal yellowtail build (`SAltQjih0ms`, searcher-sportfishing registered, high):
- **Loop 12–18 in, minimum 12**, sitting **3–4 ft above the sinker**; if you build it out to 24 in, tie it with a **double San Diego jam**. A longer loop = more bait action; err long.
- **Sinker:** the general SoCal reference is **6–10 oz**; this build runs a **16 oz torpedo** (kept side by side, not reconciled). Heavy current → up the lead until it holds bottom.
- **Wind up 3–4 cranks once the sinker hits** so the rig isn't dragging bottom. **Fish it in gear, never free-spool near structure** — in free spool a hooked fish wraps a rock before you come tight.
- **The bite is a strong thump. Wait for the rod to load / the tip to bend before setting**, then wind down and reset the hook, up to a second or third time — don't strike repeatedly into slack.
- **The first 30–40 ft after hookset is the fight.** Get that line back under a tight drag before the fish gets back into the structure.
- **Gear gap:** your profile inventories hard baits only. **No sinkers, hooks, fluorocarbon or terminal tackle are listed anywhere in `profiles/cameron/`** — so I can't confirm you own the 16 oz torpedo, the 2–4 oz eggs, or the J hooks these builds call for. Check the box before you leave.

---

## 6. How to actually find them (this is the part that decides the day)

Run the **Garmin GPSMAP 840xs** (boat.md) with these reads. From [`species/yellowtail.md`](species/yellowtail.md) "Finding them" and [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md):

**Bottom first, fish second.**
- **Hard bottom only, never mud.** Structure yellows sit exclusively on hard/rocky bottom — *"they're not going to be out in the mud… they're always going to be on the hard bottom."* Read bottom hardness off **return thickness** — thin/faint line = sand or mud, thick and dark = rock. Works on any brand (`6DzbsElGE7E`, dave-hansen, medium on the method).
- **Stop only on marks you can grade — it's a bait budget.** Every stop on a no-name mark burns bait and time. Idle on, grade it, commit only if it grades out.
- **Run manual range, not auto** — the core rule repeats across three Dave Hansen videos (high confidence); auto keeps hunting for a bottom and the shallow marks never paint.

**Depth bands, and what each one commits you to:**

| What you see | What it means | What you do |
|---|---|---|
| Tight balls **hugging the structure**; arcs/boil-ups at **~5–10 fathoms (30–60 ft)** near structure | Classic structure yellowtail (`D5DR7Kx42_A`) | Drop something with weight to provoke the reaction bite — **yo-yo iron** |
| Fish metering at **40–60 ft**, not yet showing | *"Surface iron fish and light bait zone — so we're not going to be yo-yoing today"* (`0DKmYId1NN4`, unregistered, medium) | **Surface iron + light bait**, and go all-in on the iron when they start boiling. This band explicitly **rules the yo-yo out** |
| A **stratified column** — marks running as lines from bottom up through mid-column | Fish **actively hunting bait** (`HTowqnwAMeA`) | Get **slow-trolled baits / flyline** out |
| A **ball stuck to the bottom** | Fish present but **not hunting** | **Dropper loop** water, not flyline water |
| Fish **up in the column and spread out** vs **tucked tight to the bottom** | Spread = will eat; tucked = won't (`HTowqnwAMeA`, "Marshall", medium) | The behavioural discriminator none of the depth bands carry on their own |
| A **thin, lighter mark riding above the bait ball** | That can be the yellowtail itself, pushing bait up off the rocks (`6DzbsElGE7E`) | **That** is the commit signal — not the bait pile alone |
| Marked but **not surfacing at all** | *"Just about every lure that makes it down to the depth that fish is, is a bite"* — the same source says yo-yo has **"absolutely" out-fished live bait "multiple times"** in this exact scenario (`tpmOYXYQwhU`, searcher-sportfishing registered, single mention — medium) | Don't wait for a boil. Get metal to their depth |

**Kelp lean is your live current gauge — the single best switch on an ebb day.** [`conditions/current-diagnostics.md`](conditions/current-diagnostics.md) (8/31/22, Ep. 14) — and you have four named kelp spots to read it on:

| Kelp behaviour | Current | Call |
|---|---|---|
| Pulled **~20 ft under** | Raging | Surface presentations are **dead** — go deep/weighted |
| **Laid flat** on the surface | Strong | Fishable but hard; work the **down-current side** |
| **Resurfacing / standing back up** | Slacking | **Switch back to the surface / lighter** |

*The transition from laid-down to resurfacing is your cue to change gear before the bite window — watch the kelp, not the clock.* Cross-check with the **chum-drift angle**: chum straight back off the stern = wind-dominated lay; chum swinging off at an angle to the boat = real current cutting across, and that angle is your current-direction sensor. Note that **a chart plotter's current-arrow layer is reading wind, not current** (`BskCsKaTiZw` via dave-hansen, medium) — confirm with the kelp and the chum.

**Glassing** ([`planning/search-and-glassing.md`](planning/search-and-glassing.md), 7/14/22): glass from a **full stop** or bow into the swell at **~1 kt**; **360° in small increments, 3–4 minutes per full scan**; when you catch a bird **watch it 30–40 seconds** before judging. Along a bank, run the contour at **16–18 mph** with a lookout **~30° off each bow**. Space stations 3–4 mi apart. Your own practice merged in: follow working **terns** even with nothing else working. [`conditions/bird-reading.md`](conditions/bird-reading.md) also notes **boobies are mostly seen at the Coronado Islands** and you consider them worth paying attention to — no corpus doctrine behind that, carried as your observation.

**If two spots are blank:** prospect rather than grind. [`techniques/trolling.md`](techniques/trolling.md) (`HTowqnwAMeA`, registered, medium) names trolling diving hard baits as **the private boater's fastest way to read a zone** when you're working unfamiliar water, between bites, or have no sign and no report. It's a **search** tool. Carry variety on three axes — colour, style/profile, dive depth. **Colour by light, and it inverts the habit:** overcast/low-light morning → **high-visibility**; bright clear blue day → **darker** (blues, purples, sometimes reds). **Gear splits at the ~40 ft plug:** for **20–30 ft divers your flyline outfit is explicitly adequate**; for 40 ft divers, switch to a shorter 6–7 ft rod, heavier 40-class reel, 80 lb braid — which is exactly what your **TLD 20 / Seeker 660H 6'0" 30–80 lb, 80 lb braid** setup is entering the rotation for. Keep the **top shot short — 15–20 ft of 50–60 lb**. From your owned spread ([`profiles/cameron/trolling-lures.md`](profiles/cameron/trolling-lures.md)) the Rapala Husky Magnum 15/25 and the Halco Laser Pro 190 XDD are the diver-class options; you normally run **2–3 lures**, furthest back out of the elevated shotgun.

---

## 7. Bait

- **Buy sardines if the barge has them; when you make bait it's always mackerel** ([`bait/making-bait.md`](bait/making-bait.md)). Your sabiki program: **Coronado Islands** (or La Jolla during shortages), **sabiki down to ~100 ft, 8 oz sinker** — you've loaded 5 twelve-inch mackerel on one drop. Twelve-inch mackerel are big, hearty baits, heartier than sardine.
- **Make mackerel at the island on arrival if you can.** Per §5C, mackerel is the bait that filters the catch toward yellowtail at the Coronados.
- **Battery watch:** the 30-gal tank's Rule 401 (500 GPH, 2.1 A) runs off your **single starting battery** with no house bank. The NOCO GEN5X1 holds it up overnight at the dock — but on a 05:00-to-14:00 day with the pump running the whole time, that's the one systems risk in this plan.
- **During bait shortages** you can watch Everingham's bait boats on MarineTraffic to see when the San Diego Bay / Mission Bay receivers get refilled ([`planning/fleet-intelligence.md`](planning/fleet-intelligence.md)).
- Same note: **AIS sportboat tracking at the Coronados** (e.g. the Grande, MMSI 366746210) is called one of the most valuable data sources for learning those islands — stop/start patterns tell you where the fleet is actually fishing, and AIS is harder to fake than radio chatter.

---

## 8. Landing, and a sea lion contingency

- **Gaff:** yellowtail fall in the **3-in hook, ~6-ft gaff** class (fish to 40–50 lb) — [`fish-care/gaffing.md`](fish-care/gaffing.md) (`OIiDJu4mx44`, medium). **Call "colour" or "gaff" while the fish is still coming up**, so whoever's gaffing is standing at the rail ready. **Keep the fish horizontal just under the surface — do not lift its head out of the water**, that makes it dive and kills your shot.
- **Sea lions** are a live risk on hooked yellowtail here. The counter-move ([`species/yellowtail.md`](species/yellowtail.md), `mdhoEQPqpng`): **wind continuously, never pump.** Once the sea lion grabs the fish, **throw the reel into free spool for total slack** — it reads as the line breaking and the animal lets go — then wind fast to recover.
- **Care.** The KB has **no dedicated yellowtail bleed-and-chill note**; the one yellowtail data point is logged inside [`fish-care/tuna-care.md`](fish-care/tuna-care.md) (`Klfb433I3Uk`, unregistered, medium): as soon as it's on deck **cut the artery**, hold the fish **upside down in a bucket ~5 minutes** for the blood to pump out, then **on ice**. General chain from [`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md): **salted slurry — rock salt ~2 cups per 7–10 lb bag of ice plus a splash of seawater** (the salt is what takes it below freezing); **never rinse in fresh water**; bring a **car cooler** so the cold chain survives the drive home. You carry 100–125 lb of ice per trip, which is the budget for it.

---

## 9. What this knowledgebase could not tell me

I'd rather you hear these than have me paper over them:

1. **No yellowtail temperature band exists in the KB.** The break-side rules cover bluefin, yellowfin and dorado only. Nothing here says whether 68.5 °F is good, marginal, or irrelevant for yellowtail.
2. **You gave me no chlorophyll for the Coronado Islands** — the one zone the plan actually commits to. The colour doctrine is edge-based and needs the surrounding field; I'm flying on SST and structure there.
3. **No current data**, so two tests in the protocol can't be run: the sea-state **current-vs-swell opposition** check (a summer counter-current against NW swell compresses the interval and stands it up — "4 ft @ 10 s fishes like 6 ft @ 7–8 s"), and the island-structure question of **which current direction each ridge needs**. You'll have to run both off the water — kelp lean and chum drift.
4. **Chlorophyll age is unknowable from one snapshot.** New cold bloom (skip it now) vs mature bloom edge (fish it) needs a time series.
5. **There is no Coronado Islands location note in this KB.** You get universal island-structure typology plus a coordinate list — no per-spot depths, no ridge orientations, no "which corner fishes on which tide" for Pukey Point, Middle Grounds or South Kelp Ridge.
6. **No Mission Bay → Coronados run distance.** The only figure is "~13 mi from San Diego." From Dana Landing you're running south past Point Loma — budget more, and I'm not going to invent the number.
7. **Your boat's range and sea-state limits are null in the profile**, so the go/no-go on the crossing in a building NW is yours, not the KB's.
8. **Mexican licensing and entry requirements are an admitted gap** in the KB (FMM, CONAPESCA, passport). It names the agencies and nothing else.
9. **No CDFW yellowtail size or bag limit** appears in the regulatory register — it carries calico, sand bass, halibut, sculpin, bluefin, lobster and rockfish rows, no yellowtail. Verify with CDFW (and with Mexican rules for fish taken in Mexican water — different jurisdiction, not a conflict).
10. **No terminal-tackle inventory in your profile** — sinkers, hooks, fluoro. The sliding-sinker and dropper-loop builds can't be resolved against gear you actually own.
11. **No Salas 7X-class heavy surface iron in your box** for the wind-up rule; closest is the Nomad Slidekick 120g at 4.25 oz.
12. **No 9 Mile or 425 yellowtail doctrine anywhere in the KB** — only bank-naming trivia and coordinates.
13. **No Mission Bay bait-receiver detail** — the barge etiquette/timing note is built on a Dana Point example.
14. **Your ~8 am departure norm has no dawn-start precedent in the profile.** The 05:00 departure is derived from the tide and gray-light doctrine, not from anything you've logged doing.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/fleet-intelligence.md`, `species/yellowtail.md`, `seasonal/september.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/moon.md`, `conditions/current-diagnostics.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `locations/bight-geography.md`, `locations/island-structure.md`, `locations/zone-lexicon.md`, `locations/regions.md`, `locations/README.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `techniques/trolling.md`, `lures/iron-jigs.md`, `bait/making-bait.md`, `bait/fishing-live-bait.md`, `fish-care/gaffing.md`, `fish-care/tuna-care.md`, `fish-care/dorado-and-general.md`, `tackle/hooks.md`, `profiles/cameron/README.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `profiles/cameron/trolling-lures.md`, `sources/spot-lists.md`, `sources/regulatory-claims.md`  
*videos:* `D5DR7Kx42_A`, `YZtX1MiT0y8`, `0DKmYId1NN4`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `yGXSrUauo2w`, `F9XjGMEvvag`, `0dIwWiOc1NY`, `yn1suHH6b1Y`, `Ec2GaNpiOHI`, `VpW91AKOFVQ`, `RNRFrfepiW0`, `5pbA-wXoric`, `wzI0lpgKT1U`, `SAltQjih0ms`, `NC3-3pJDEgo`, `6DzbsElGE7E`, `w5_x6kkN-xE`, `7WapaxdtjQg`, `bM2vUS1B-yQ`, `Klfb433I3Uk`, `OIiDJu4mx44`, `Rf1HKJG-SDg`, `HzE4FHHcvTk`, `mdhoEQPqpng`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `pOFsjDTqaxY`, `uyjTdgIw-1k`, `BskCsKaTiZw`, `5to3Q5P7w90`, `ejUTAnONf7o`  
*gaps admitted:* No yellowtail SST band or temperature threshold exists anywhere in the KB — the break-side temperature rules cover bluefin, yellowfin and dorado only, so 68.5 F at the Coronados cannot be graded as good or bad from this knowledgebase. | No chlorophyll value was supplied for the Coronado Islands, the zone the plan commits to; the KB's water-colour doctrine is edge-based and needs the surrounding field to be usable there. | No current data was supplied and the KB holds none, so the sea-state current-vs-swell opposition test and the island-structure 'which current direction does this ridge need' test cannot be run before departure. | Chlorophyll age (new cold upwelling bloom vs mature bloom edge) cannot be determined from a single snapshot — the KB's freshness rule needs a time series. | There is no Coronado Islands location note in this version of the KB: no per-spot depths, ridge orientations, or preferred current/wind directions for Pukey Point, Middle Grounds, Ribbon Kelp, Lighthouse, 5-Minute Kelp, South Kelp Ridge or Rockpile — only universal island-structure typology plus coordinates. | No Mission Bay to Coronado Islands run distance in the KB; the only figure is '~13 mi from San Diego' (D5DR7Kx42_A), which is not a Dana Landing departure figure. | The angler profile's machine envelope is explicitly null — profiles/cameron/boat.md has home_port, range_nm and sea_state_max_ft set to null, and the day-plan protocol says to ASK rather than assume, so the go/no-go on the crossing in a building 14-16 kt NW cannot be decided from the KB. | Mexican licensing and entry requirements (FMM, CONAPESCA fishing permit, passport) are an explicitly admitted gap in sources/regulatory-claims.md, and the Coronado Islands are Mexican water. | No CDFW yellowtail size or bag limit appears in the regulatory register — the California table carries calico bass, sand bass, halibut, sculpin, spotted bay bass, bluefin, lobster and rockfish rows, but no yellowtail row. | No terminal-tackle inventory exists in profiles/cameron/ — sinkers, hooks, fluorocarbon and leader material are not listed, so the sliding-sinker (2-4 oz egg, 2/0-4/0 J hook) and dropper-loop (6-10 oz or 16 oz torpedo) builds cannot be resolved against owned gear. | No Salas 7X-class heavy surface iron in the owned tackle for the wind-up-means-heavier-iron rule; the closest owned item is the Nomad Slidekick 120g at 4.25 oz. | The KB carries no yellowtail doctrine for the 9 Mile Bank or the 425 — only the bank-naming convention (Rf1HKJG-SDg) and coordinates in the spot library. | No Mission Bay bait-receiver specifics — the bait-barge etiquette, hailing and timing note is built on a Dana Point example. | No dedicated yellowtail fish-care note exists; the only yellowtail bleed-and-chill data point is logged inside fish-care/tuna-care.md as a cross-species observation (Klfb433I3Uk, medium confidence). | The profile records a normal ~8 am departure and no dawn-start precedent, so the 05:00 departure recommended here is derived from tide/gray-light doctrine rather than from the angler's logged practice.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Saturday 2026-09-19 — yellowtail, 22 ft center console out of Mission Bay

Built by the five steps in [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), against the profile in `profiles/cameron/`. Everything below comes from notes in this knowledgebase; where the KB doesn't cover something I say so rather than filling it in.

---

## 0. Two things to settle before Saturday

**Your boat envelope is blank in the profile.** [`profiles/cameron/boat.md`](profiles/cameron/boat.md) carries `range_nm: null` and `sea_state_max_ft: null` — deliberately, with the comment that until they're filled "the protocol must ASK for range and sea-state instead of assuming one." So: **what's your comfortable range and your sea-state limit?** The plan below is built to be abortable on a short leash for that reason. What the profile *does* give: 2004 Panga Marine Marquesas 22, single 115 hp Yamaha, ~35 kt top / ~1.5 kt idle, no trim tabs, 30-gal bait tank on a Rule 401 (500 GPH, 2.1 A) running off a **single starting battery — no house battery**, 10 rod holders (6 vertical), 100–125 lb ice per trip, launching Dana Landing, Mission Bay.

**If you go to the Coronados, that is a foreign-waters trip.** [`locations/coronado-islands.md`](locations/coronado-islands.md): "These are Mexican waters: seasons, limits and licensing are CONAPESCA/INM, not CDFW… the day starts with paperwork rather than tackle." The KB then flags its own hole outright — ⚠ *no corpus source: exactly what a boat run to the Coronados requires — permits, passports, whether an FMM applies to a day trip that never lands.* **The KB cannot tell you what paperwork to carry.** Sort that independently before Saturday or take Plan B.

---

## 1. What your conditions say

Using your numbers exactly, no live pulls.

**Water.** September is the **warm-stable (late)** regime ([`seasonal/september.md`](seasonal/september.md), [`conditions/water-regimes.md`](conditions/water-regimes.md)) — "an established warm band of clean water over the Bight… the paddy field is seeded" (cameron). Your set splits clean:

| | SST | Chl | read |
|---|---|---|---|
| Point Loma kelp | 66.9 °F | 1.1–1.4 | coolest, greenest |
| La Jolla | 67.4 °F | 1.1–1.4 | same |
| 9 Mile | 67.8 °F | 0.6 | mid |
| **Coronado Is.** | **68.5 °F** | **not given** | warmest *structure* water |
| 425 | 69.1 °F | 0.35 | warmest, cleanest — and deep open bank |

Three honest caveats. (a) **You gave no chlorophyll for the Coronados**, and the protocol's own doctrine is "an empty layer is missing data, not a zero" — so that cell is unknown, not clean. (b) **There is no SST band for yellowtail anywhere in this KB.** [`species/yellowtail.md`](species/yellowtail.md) carries `sst_band_f: unknown` and flags it: "*⚠ Flagged gap — no corpus source: the numeric SST bands; the corpus gives directional water-state reads only.*" So don't let me or anyone rank these five numbers for yellowtail — the KB doesn't support it. (c) The warm-year color doctrine (cameron, [`conditions/water-color.md`](conditions/water-color.md)) says weight chlorophyll at least as heavily as SST and "skip 'dirty green' water for gamefish" — but **no number separates productive green from dead green**, so 1.1–1.4 on the kelp is an on-the-water read (color, bait present, kelp lean), not a disqualifier from the chart.

**Sea state — this is the number that shapes the day.** [`conditions/sea-state.md`](conditions/sea-state.md):
- **"Wind above ~12 kt is what raises whitecaps, and 12 kt is the personal cutoff for not running"** (`NC3-3pJDEgo`, flagged single-source and framed as personal). Your NW 6–10 kt at dawn is under it; **NW 14–16 kt by 14:00 is over it.**
- **"Swell interval under 10 seconds is a hard bad-sea flag"** — your NW 3 ft **@ 9 s** trips it. You are *not* in the named unfishable combo (12–15 kt with 4–8 ft at 9 s) because your height is 3 ft, but the day walks toward it as the wind builds.
- Your S 2 ft **@ 14 s** is the benign kind — the steepness rule (`zKmZ4zql2ws`) has 10 ft @ 15 s "barely felt" while 3–4 ft @ 4–5 s is "brutal."
- **"Assume the forecast errs on the worse side"** and that afternoon W at the islands **strengthens** rather than eases (`zKmZ4zql2ws`); if it's windier than forecast in the morning, "assume it builds all day — a small boat bails early" (`DnSqw4r7A1s`).
- **Homebound wind:** "A run **south** into Mexican paddy water puts a W wind on the return leg — uphill misery. Plan return timing **against** the afternoon W build" (`HzE4FHHcvTk`). That is exactly the Coronados/425 case.

**Tide.** High 06:42 (5.1) → low 13:05 (0.4): a 4.7 ft drop over 6h23m, so **the ebb runs all morning** with the strongest push mid-morning. [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md): **"Be at the highest-percentage zone an hour before the tide change"** (`6TBxHnkYXI0`). For yellowtail specifically, [`species/yellowtail.md`](species/yellowtail.md): **"Current on = bite on. Slack current keeps the bite off; the current starting is what starts it"** (`fDSd9kqwYW0`) — even "a puff of current can fire a lee-side bite to 40 lb" (`_r_qKX_7080`) — and **"Tide windows, not clock time"** (`YZtX1MiT0y8`). Plus **gray light**: "Yellowtail feed hardest in the gray light early in the morning" (`0dIwWiOc1NY`).

**Moon.** New 09-15, so Saturday is +4 days — inside the new-moon ±1 week elevated window in [`conditions/moon.md`](conditions/moon.md), and inside Capt. Dave Hansen's "7 days before AND 7 days after" version (`fri_BWI-VA0`). **But** that note's species are bluefin, white seabass and swordfish, and the yellowtail router flags it explicitly: *"⚠ Flagged gap — no corpus source: moon-phase effect"* for yellowtail. **So the moon buys you nothing you can act on here.** Don't plan around it.

---

## 2. Where to go

Region/waters envelope from Mission Bay: `socal-bight` (nearshore-coast, bank) plus `baja-pacific-north` (island, bank) if you cross the border. Yellowtail clear both gates (`regions:` all five, `waters: [island, bank, nearshore-coast, open-ocean]`).

There is a real doctrine tension here and the KB's rules say to put it in front of you rather than pick silently:

- The **September pattern for the Bight** in [`species/yellowtail.md`](species/yellowtail.md) is warm-stable = "**coastal kelp-line fish from LA to San Diego**, and the paddy program peaks (August)."
- The **Coronados' documented peak is spring** — [`locations/coronado-islands.md`](locations/coronado-islands.md) tables yellowtail as "spring peak, Apr–Jun," and the zone guide carries `season_window: spring (warming transition)`.
- But the Coronados is the **only yellowtail zone in this KB with an actual trip program written for it** ([`species/yellowtail-coronado-islands.md`](species/yellowtail-coronado-islands.md)). La Jolla, Catalina, San Clemente and the offshore banks are all "**⚠ Flagged stub — no zone guide yet**."

**The choice turns on your paperwork and on how early you can leave — not on a KB ranking.**

### Plan A — Coronado Islands (only if Mexican paperwork is squared away)
~13 nm from the San Diego bay entrance (cameron). *Note the KB contradicts itself on the unit:* the zone guide says "roughly 13 **mi**" from `D5DR7Kx42_A`, the zone page says 13 **nm**, and both flag each other. **The KB gives no run distance or time from Mission Bay** — that's a gap you fill off your own chart.

Why it's live on your numbers: 68.5 °F is the warmest **structure** water in your set, and the zone's driver is bait — "the west side's exposure to colder Pacific currents and tidal swings is what keeps it generally filled with bait" (`D5DR7Kx42_A`). Also: **"Big schools forgive the retrieve"** — a big Coronado school eats a faster, less exacting retrieve than the finicky mainland schools (`VpW91AKOFVQ`). For someone new to SoCal iron fishing, that matters.

The circuit (11 charted spots, fished as one loop, not a list of stops): **Pukey Point** at the north end → **Middle Grounds** (the mid-chain bank, trolled between the islands) → the kelp edges **Ribbon Kelp / 5-Minute Kelp / South Kelp Ridge** → **Lighthouse** → **Rockpile** standing off to the southeast. Positions are in `sources/spot-lists.md`.

### Plan B — the coastal kelp line, Point Loma → La Jolla (US water, no paperwork, short bail)
This is the KB's stated warm-stable September shape, and it's the right call if the paperwork isn't done or if you want a 20-minute run home when the wind comes up.

The one spot in this zone with real corpus detail is the **La Jolla Northwest Corner** ([`locations/la-jolla.md`](locations/la-jolla.md)): a reef with an incline running into it, where **the sounder shows yellowtail as big arcs at 5–10 fathoms with bait around them, and holding fish down at 90 ft on the incline** (`yLpDI8jnizU`).

Go in with eyes open: **"Presence is not catchability"** — some yellowtail are in La Jolla year-round and half-day boats can go months between fish (cameron), and schools on the **Del Mar to Imperial Beach** stretch are markedly finicky about jig action, "especially for these bigger grade fish" (`VpW91AKOFVQ`). The KB's only dated La Jolla yellowtail catches are January and July, and it flags that even those months are inferred from upload dates. **There is no September La Jolla read in this KB.**

**MPA edges on three La Jolla spots** (from the spot library, single-source-flagged, CDFW — verify current boundaries before you fish): The Cove — stay **west of 117°16.400'W**; Windansea — stay **north of 32°49.573'N**; Crystal Pier — stay **south of 32°47.945'N**.

### Plan C — a paddy, opportunistically, not as a program
If you cross floating kelp on the run, work it; **do not** make a 20+ nm offshore paddy hunt the day's plan on a building-wind forecast in a 22. [`conditions/kelp-paddies.md`](conditions/kelp-paddies.md): approach **directly**, "drive up to the edge of it like it's the dock" (`ZFqe49jRgA0`) — a paddy isn't spooky. Check fast: look for visible fish, then sound for **boomerang-shaped arcs, typically 90–120 ft down**; give it **about a minute, maybe two** — a look, a sounder pass, one bait — then move (`ZFqe49jRgA0`). Fish move paddy-to-paddy **only at night**, so a dry paddy stays dry all day (`4xzK7YaXK5s`, `8XrMkWPRxgs`). Paddies line up on the current: **roughly N–S in open water under the summer uphill current, along the contour near a bank edge** — search the line, not the compass (`DnSqw4r7A1s`). Expect small fish up top early in a drift and bigger fish underneath, sometimes deeper (`SAltQjih0ms`).

**On the 425 specifically:** don't. [`locations/425-bank.md`](locations/425-bank.md) is a **minimum page** — position only (32°15.000'N 117°23.200'W), with "⚠ Flagged gap — no corpus source" on the run, the structure, what's there and how it fishes. Its 69.1 °F / 0.35 chl is the prettiest water in your set and the KB has literally nothing on fishing it, it's Mexican water, and it's the longest run on the worst wind day of the three options.

---

## 3. When — the timeline

| time | what |
|---|---|
| **04:30–05:00** | Bait. If buying sardines, beat the barge rush: SoCal 3/4-day and half-day sportboats all load ~06:00, so target **05:00 — "at least five o'clock in the morning, if not four thirty"** (`7WapaxdtjQg`, `bM2vUS1B-yQ`, `ztpj1Xll0-U`; stated on the Dana Point schedule). A 07:00 arrival avoids the line but "by then it's all gone." |
| **~05:45** | **On the first zone.** That's an hour before the 06:42 high change (`6TBxHnkYXI0`). This is earlier than your profile's ops norm — [`profiles/cameron/boat.md`](profiles/cameron/boat.md) records "normal departure ~8 am (earlier starts are the exception)." Saturday is an exception. |
| **06:00–07:30** | **Gray light.** Surface iron and light bait; the meter pass in parallel. |
| **07:30–12:30** | The ebb runs off the high toward the 13:05 low — **current on = bite on.** Run the circuit; convert on sign; re-run water rather than grinding one spot. |
| **~10:00 onward** | Wind crosses ~12 kt somewhere in here: whitecaps. Sign-reading switches from breezers to **flat spots**; the presentation starts sliding down the column. |
| **12:30–13:00** | **Turn for home.** Low at 13:05, 14–16 kt by 14:00, and the return leg from Mexican water is uphill into a W/NW build (`HzE4FHHcvTk`). |

Fishless mid-morning is not a signal to change everything: **"A good SoCal local-coast yellowtail day is three or four bites; a 12–15-bite day is an anomaly. Two fishless hours is not evidence the technique is wrong"** (`HTowqnwAMeA` — local-coast scope, not an island expectation). And at the Coronados, seeing-not-biting cycles are the zone's *normal state*, with "a little weather window or a little time with bite window" each day (`YZtX1MiT0y8`).

---

## 4. How to fish it

**Rig all three outfits before you leave the dock.** The router's framing: yellowtail show three faces — boiling/breezing surface fish, paddy fish, and bottom fish stacked on structure — and "the faces are states of one population, not fish types… the technique follows the face, and the face can flip by the hour."

### 4a. Cover water: troll to find, not to catch
"Trolling is called the private boater's fastest way to cover and read a zone" when you're working an area you don't know, between bites, or you've seen no sign ([`techniques/trolling.md`](techniques/trolling.md), `HTowqnwAMeA`). At the Coronados the guide is explicit: **pink and purple Halco 190-class divers are the zone's fish-finder**, run figure-8s around the islands and troll the Middle Grounds between them.

**You own exactly that lure** — two **Halco Laser Pro 190 XDD** (6M+ "crazy deep" bib), one purple/chrome, one pink ([`profiles/cameron/trolling-lures.md`](profiles/cameron/trolling-lures.md)). Running specs from [`lures/halco-laser-pro.md`](lures/halco-laser-pro.md): **3–11 kt, optimum 6.5 kt; 20+ ft running depth; setback 11–55 yd, default 27 yd; 40–60 lb leader; low gunnel holder** (divers want the gunnels; bars and surface skirts want the elevated shotgun — `profiles/cameron/boat.md`).

Colour by light, and it inverts the common habit: **overcast/low light → high-visibility colours; bright clear blue day → darker, blues and purples** (`HTowqnwAMeA`). So: **pink in the gray light, purple once the sun is up.**

Outfit split (`HTowqnwAMeA`): 20–30 ft divers ride the flyline outfit, no second setup needed; **40 ft divers want a real troll outfit — 6–7 ft rod, heavier 40-class reel, 80 lb braid.** Your **TLD 20 on the Seeker 660H (6'0", H, 30–80 lb, 80 lb braid)** is that outfit, and the profile already lists it as "entering trolling rotation for diver duty (Halcos, Husky Magnums)." **Top shot short — 15–20 ft of 50–60 lb**: braid's zero stretch is what lets the rod tip read the lure, and a fish hooked mid-column is near kelp and rock and needs to be lifted immediately.

**When a trolled rod gets bit, cast an iron into the same water while the first fish is fought** — yellowtail school, so a troll strike means more fish are under the boat (`jo8lMdFZ1bk`; the KB flags that this source scopes the drill to a three-man panga, so with a light crew it's a judgment call).

### 4b. Read the sign
[`planning/search-and-glassing.md`](planning/search-and-glassing.md) gives three surface reads: **boils/foamers**, **breezers** (fish pushing a ripple that reads like wind), and — the one that matters after 10:00 — **flat spots**: "with wind and whitecaps around, the same near-surface fish flatten the chop directly over them… a smooth, whitecap-free patch sitting in otherwise broken water."

Birds ([`conditions/bird-reading.md`](conditions/bird-reading.md)): **terns are the run-to bird.** A **moving dive-line** — dive, fly ahead a few feet, dive again — means bait fleeing something below, and "that is the one to run on"; **locked-in repeated dives on one spot = bait only** (`Blh2BA-7Ono`). **Cast under the bird the moment it dives**, not at its general position (`JiJYamo0QHk`). Even one or two terns picking at the water are worth running to and sweeping with sonar (`lf3S28nh-kk`). **Gulls sitting on floating kelp are your paddy-finders**, not evidence of gamefish. Pelicans are a bait tell, not a fish tell. **Boobies are mostly seen at the Coronados and Cameron rates them** — but the KB flags that it has *no* doctrine on what booby behavior actually means.

### 4c. The meter (Garmin GPSMAP 840xs)
[`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md):
- **Run manual range, not auto**, and size it so **the bottom sits mid-screen** — that leaves room to read hard vs soft bottom and pick fish out of the column. A private boat's default working range is 0–120 ft on older machines, 0–150 ft on newer. Over island/reef structure in 5–10 fathoms (30–60 ft), set accordingly.
- **Bottom hardness reads off return-line thickness on any brand**: thin/faint = sand or mud, thick and dark = rock. **Structure yellowtail sit on hard bottom, never mud** (`6DzbsElGE7E`).
- **The hard/soft transition is the highway**, worth more than the top of the high spot (`yLpDI8jnizU`).
- At La Jolla's Northwest Corner: run a **split screen — chart one half, sounder the other**; when you run over fish, use **history playback to drop a waypoint on the mark you already passed**, turn back over it, cast a jig at it (`yLpDI8jnizU`).
- **Chop hurts you specifically**: a fixed transducer follows the boat's roll, so in chop the cone tips away from vertical and high-in-the-column fish "don't show until the boat is nearly on top of them" (`fgTmUq78ofQ`, `ZIJAvAEW_tU`). Another reason the good window is the calm morning.
- **Stop only on marks you can grade — it's a bait budget.**

**Shape of the mark tells you feeding state** ([`species/yellowtail.md`](species/yellowtail.md), `HTowqnwAMeA`): fish **spread up through the column** — stratified from bottom through mid-column, or sitting high over a small rock ~20–30 ft across — are **hunting** → slow-trolled and flylined baits. Fish **balled tight to the bottom** are present but not feeding → dropper-loop water, worth a yo-yo burned past them. Fish metered at **40–60 ft and not yet showing are staging up** — surface-iron and light-bait fish, not yo-yo fish; **the moment they boil, go all-in on the surface iron** (`0DKmYId1NN4`). And a school metered deep and not showing can still be caught at its depth (`tpmOYXYQwhU`).

**Read the kelp for current** ([`conditions/current-diagnostics.md`](conditions/current-diagnostics.md)): pulled ~20 ft under = raging, surface presentations dead, go deep/weighted; laid flat = strong, work the down-current side; **resurfacing = slacking, switch back to the surface** — "watch the kelp, not the clock" (`HnqiE05vdXs`). At a kelp bed, current running **downhill → work the northwest corner; uphill → the southeast corner** (`kzD0kSnnVPw`; single-source, and the KB flags that La Jolla isn't actually named in that clip).

### 4d. The three presentations, on your gear

Class terms resolve to your rack via [`tackle/gear-classes.md`](tackle/gear-classes.md) and [`profiles/cameron/rods.md`](profiles/cameron/rods.md):

**Surface iron — fish showing, or a paddy → the Torium 20HG on the 10'0" Phenix Abyss (50 lb braid).** The lexicon names this rod as your jig-stick class; "an 8-ft jig stick is a yo-yo rod — 9-ft is okay, 10-ft is better" (`yn1suHH6b1Y`).
- **Line:** the Coronados guide runs ~65 lb braid to a **fresh 40–50 lb mono top shot**, with **40 lb the local full-day-island bracket** (`D5DR7Kx42_A`, `LTCFjqtSI8g`); [`species/yellowtail-surface-iron.md`](species/yellowtail-surface-iron.md) calls it straight mono **40–50 lb**. Your 50 lb braid works as backing. **Run the thinner end of your top-shot range on irons** — a thick top shot dampens the kick (`F7jLrt2j2X8`).
- **Irons you own** ([`profiles/cameron/tackle.md`](profiles/cameron/tackle.md)): **JRI-7** (light blue, ~Tady 45 class, "local/kelp all-rounder") is your first cast; **Squidco Candy Bar SR Lite** (scrambled egg, 3 oz); **Strictly Irons Glory** (light blue, wide drawn-out kick — the note's own change-up "for picky bites / slack current"); **Nomad Slidekick 120g** (4.25 oz, sinkable, your heaviest).
- **Sink it before you wind** — about **30 ft of sink** drew a first-cast strike at Catalina (`oadK6zIYyCo`), and the same move on a Tady 45 was near a "yellowtail guarantee" at Cedros (`9tIp4n7q850`). Single-source on the 30 ft figure.
- **Work it all the way to the rail.** Yellowtail "often eat the jig right next to the boat after trailing it in — keep working the retrieve, rod tip down, all the way back" (`VpW91AKOFVQ`). The last five feet are a real bite zone.
- **Don't over-wind.** Reeling too fast is the commonest mistake; these lures were designed around a 4:1 Jigmaster, and 6.5–7.5:1 is "too fast" (`Ec2GaNpiOHI`). Against that, 7:1 is argued as the torque-vs-speed middle ground for *landing* big yellowtail (`pOFsjDTqaxY`). **The KB keeps both and gives you the frame: the choice turns on whether that outfit's first job is the retrieve or the fight** — your Torium 20HG is a high-gear reel, so wind it on cadence, not on the handle's capability. And on colour: the named yellowtail colours are scrambled egg, bird shit, mint, blue/white (nate) — while [`techniques/surface-iron-color.md`] argues colour is *not* the variable (rank: swim → size/weight → colour last). **Decide on the swim, not the species and not the paint.**
- **Chum-then-cast** on fish you can meter but can't see: meter the school, throw live chum, let them boil, cast into the boil. **The long cast is load-bearing — the fish will not let the boat drive over the top of them** (`4pT0efBD1j0`, `dS9gd9k7A7Q`).
- **Hold the stop while anyone is hooked** — a hooked fish keeps the school near the boat; get a jig back in while someone is still bent (`gdqI2dNd5_U`).

**Yo-yo iron — tight balls hugging structure → the Trinidad 40 on the 8'0" XH 40–80 lb (80 lb braid).** That's the KB's yo-yo/heavy-iron class, and the lexicon names your Trinidad 40 as the example. Hit bottom and **burn it — the strike comes a couple of cranks off the bottom** (`D5DR7Kx42_A`). You own the **Salas 6X** (blue) and a **Salas CP 105**. Depth-banded sizing from [`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md): 60/80/100 ft → a 6X Jr-class jig; **120–150 ft → a Salas 6X at roughly 5–6 oz**; 150–250 ft → full-size 6X-class. **Heads-up on a live contradiction:** the yellowtail router states the same ladder keyed to *current* at different weights ("full-size 8 oz in stronger current, 6X Jr 4 oz when it's light"), and the technique note flags it — the two notes disagree and neither is silently right. Over Coronados/La Jolla structure at 5–10 fathoms you're at the shallow end of that ladder anyway.

**Flyline — fish visible or metered but not eating → the Avet MXJ 5.8 on the 9'0" Teramar MH (50 lb braid).** The profile lists that setup as "mainly flyline." Class is **20–30 lb**, stepping to 40 lb where grade and structure punish light line. **Hook size follows bait size**: **1/0–2/0 baseline at the Coronados** (`D5DR7Kx42_A`); downsize to J hooks in sizes **1, 2 and 4** when they're picky on fluorocarbon (`F9XjGMEvvag`); **2/0–4/0** with bigger baits (`yGXSrUauo2w`). The KB flags an ASR ambiguity on a competing "No. 2 on a sardine" baseline (`fDSd9kqwYW0`) — could be No. 2 or 2/0. Bait choice: **a bigger mackerel drifted to the outside edge of a bait ball gets picked out** — the yellowtail around the ball key on the larger item (`d0yGBQDeY_4`).

**Dropper loop — bottom fish that aren't chasing → the same Trinidad 40.** [`techniques/dropper-loop.md`](techniques/dropper-loop.md): sinker at the very bottom, **6–10 oz**, hook on a loop **6 in to 4 ft above** it, "a longer loop gives the bait more action — err long." Up the weight when the current is heavy to hold bottom.

**Don't marry any of it.** "A told technique is a starting point, not a contract: pulling the anchor and slow-trolling around the same zone roughly quadrupled a bite rate over the anchor fishing the spot was supposed to be" (`HTowqnwAMeA`). *(The KB also flags one of its own gaps here: the anchor-vs-drift commit call at the Coronados — when to drop the hook on a mark versus keep working the circuit — has no corpus source.)*

### 4e. Bait
[`bait/making-bait.md`](bait/making-bait.md) — your split is buy sardines at the barge when available, **make mackerel** when not: sabiki to **~100 ft on an 8 oz sinker**, at the Coronado Islands (and La Jolla during shortages), with **five twelve-inch mackerel on one drop** logged. Twelve-inch mackerel are "big, hearty baits — heartier than sardine." Your tank is 30 gal and dialed, but it and everything else runs off the **single starting battery** — watch that on a long day.

### 4f. Landing and care
- **Sea lions:** wind continuously, never pump; when one grabs, **throw the reel into free spool** — the sudden slack reads as the line breaking and it lets go — then wind fast (`mdhoEQPqpng`). **Boatside is the depredation window**; hooked and even boated fish get grabbed at the rail (`d0yGBQDeY_4`).
- **Bleed on deck, hang it head-down, then ice:** cut the artery as soon as the fish is on deck, hold it upside down in a bucket about **5 minutes**, then ice it (`Klfb433I3Uk`). You carry 100–125 lb.
- Keep the gaff sharp and put a **tail rope** on the big ones once gaffed (`RPSRH0jwyw4`).

### 4g. Boat handling on this forecast
From [`profiles/cameron/boat.md`](profiles/cameron/boat.md): run with **at least one person forward** (bean bag on the bow), ~100 lb ice in the cooler on the way out; **coming in, drain the 30-gal bait tank** and shift one person aft. No trim tabs — engine trim is your only attitude control, which matters on a 9-second NW chop.

---

## 5. Gear gaps the plan exposes

Per the protocol, I name these rather than substituting something that doesn't fish the same way:

1. **No Salas 7X-class heavy iron.** Both the router and the Coronados guide say to **step up to a 7X-class heavy iron in wind to punch the cast** (`D5DR7Kx42_A`). Your heaviest surface iron is the Nomad Slidekick at 4.25 oz. Once it's blowing 12–14 kt, that's the gap — the Slidekick is the closest thing you have (and it can be sunk out to cover the column).
2. **No 6X Jr-class jig** for the 60/80/100 ft yo-yo band. You have the full-size 6X and CP 105 only.
3. **No slow-pitch / knife-jig setup.** It's already an open item in your profile (shopping one for night bluefin + September BOLA bottom yellowtail). Not needed for this day's shallow structure, but it's the missing tool if you end up on deep marks in current.
4. **The 10 ft Phenix Axis jig stick** is listed in your tackle note as owned-but-rarely-used, with "wants reps hooking/landing yellowtail on it." Saturday is that day.

---

## What this knowledgebase could NOT tell me

- **Your boat's range and sea-state limit** — null in the profile; the protocol says ask, so I'm asking.
- **What Mexican paperwork a day boat needs for the Coronados** — explicitly flagged as absent, and it's the most common Mexican-water trip in the KB.
- **Any run distance or time from Mission Bay** to the Coronados, La Jolla or the banks; the Coronados distance is given from the *San Diego bay entrance*, and the KB flags its own nm-vs-mi contradiction on that figure.
- **Mission Bay entrance swell exposure.** The 160°–186° exposure window and 186° channel axis are for the **San Diego Bay entrance**; there is no Mission Bay equivalent note, so your S 2 ft @ 14 s at the jetties is your own call.
- **Any SST band or chlorophyll threshold for yellowtail** — flagged gap; your five temperatures cannot be ranked for this species from the KB.
- **Any moon-phase effect for yellowtail** — flagged gap.
- **A September read for La Jolla or the coastal kelp line**, and any La Jolla program shape (start point, commit points, tide/light windows) — flagged stub and flagged gap.
- **A documented yellowtail re-rank at 14–16 kt.** The documented "wind moves the bite down, not off → go yo-yo" threshold is ~20–25 kt+ (`ejUTAnONf7o`), and the KB flags even that number as a single unitless "pushing 25." I'm reasoning from the 12 kt whitecap line instead, and saying so.
- **CDFW yellowtail bag and size limits, and any Mexican (CONAPESCA) limits** — flagged gap. Verify with the issuing agency before Saturday.
- **The Coronados anchor-vs-drift commit call** — flagged gap.
- **Anything at all about fishing the 425** — position-only page.
- **What booby behavior means** — no corpus doctrine.

One last note on how to read this: many claims above sit beside ⚠ fact-check flags in their own notes (single-source figures, or a cite that doesn't fully support the sentence). I've carried the flags where they touch a number you'd act on. Single-source is not wrong — it's just one captain, once.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `planning/search-and-glassing.md`, `locations/regions.md`, `locations/coronado-islands.md`, `locations/la-jolla.md`, `locations/point-loma.md`, `locations/425-bank.md`, `locations/101-425.md`, `locations/north-9-mile-bank-178.md`, `species/yellowtail.md`, `species/yellowtail-coronado-islands.md`, `species/yellowtail-surface-iron.md`, `seasonal/september.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/moon.md`, `conditions/kelp-paddies.md`, `conditions/current-diagnostics.md`, `conditions/bird-reading.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/flyline.md`, `techniques/dropper-loop.md`, `techniques/trolling.md`, `tackle/gear-classes.md`, `lures/halco-laser-pro.md`, `bait/making-bait.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`  
*videos:* `D5DR7Kx42_A`, `HTowqnwAMeA`, `YZtX1MiT0y8`, `VpW91AKOFVQ`, `yLpDI8jnizU`, `ejUTAnONf7o`, `4pT0efBD1j0`, `dS9gd9k7A7Q`, `gdqI2dNd5_U`, `F9XjGMEvvag`, `LTCFjqtSI8g`, `0dIwWiOc1NY`, `fDSd9kqwYW0`, `_r_qKX_7080`, `6DzbsElGE7E`, `ZFqe49jRgA0`, `8XrMkWPRxgs`, `4xzK7YaXK5s`, `DnSqw4r7A1s`, `HzE4FHHcvTk`, `NC3-3pJDEgo`, `zKmZ4zql2ws`, `6TBxHnkYXI0`, `91ZJbhAnzMg`, `lf3S28nh-kk`, `Blh2BA-7Ono`, `JiJYamo0QHk`, `0DKmYId1NN4`, `tpmOYXYQwhU`, `oadK6zIYyCo`, `9tIp4n7q850`, `Ec2GaNpiOHI`, `pOFsjDTqaxY`, `jo8lMdFZ1bk`, `yn1suHH6b1Y`, `HnqiE05vdXs`, `kzD0kSnnVPw`, `fgTmUq78ofQ`, `ZIJAvAEW_tU`, `7WapaxdtjQg`, `bM2vUS1B-yQ`, `ztpj1Xll0-U`, `Klfb433I3Uk`, `mdhoEQPqpng`, `d0yGBQDeY_4`, `RPSRH0jwyw4`, `SAltQjih0ms`, `yGXSrUauo2w`, `F7jLrt2j2X8`, `5to3Q5P7w90`, `fri_BWI-VA0`, `nate`, `cameron`  
*gaps admitted:* profiles/cameron/boat.md carries range_nm: null and sea_state_max_ft: null, so the boat envelope had to be asked for rather than assumed (the protocol's own instruction). | No corpus source for what a boat run to the Coronados requires — permits, passports, whether an FMM applies to a day trip that never lands (flagged in locations/coronado-islands.md as the KB's most common Mexican-water trip). | No run distance or time from Mission Bay to any zone; the Coronados figure is given from the San Diego bay entrance, and the KB flags its own 13 nm vs 13 mi contradiction between the zone page and the zone guide. | No Mission Bay entrance swell-exposure note — the 160°–186° exposure window and 186° channel axis are scoped to the San Diego Bay entrance only. | No numeric SST band for yellowtail anywhere in the KB (species/yellowtail.md carries sst_band_f: unknown and flags the gap), so the five given temperatures cannot be ranked for this species from the KB. | No chlorophyll threshold separating productive green from dead green water, so the 1.1–1.4 mg/m3 kelp-line reading cannot be scored against the 0.6 and 0.35 offshore readings. | No chlorophyll value was supplied for the Coronado Islands, and the protocol treats an empty layer as missing data rather than a zero. | No moon-phase effect for yellowtail — explicitly flagged in species/yellowtail.md; the KB's moon doctrine covers bluefin, white seabass and swordfish only. | seasonal/september.md carries no SoCal-Bight yellowtail prior — its yellowtail content is the BOLA bottom program in the Sea of Cortez. | La Jolla has no yellowtail zone guide (flagged stub) and no program shape — which end to start on, commit points, bait program, or the tide/slack/light windows that turn the bite on there. | No September read for La Jolla or the coastal kelp line; the corpus's dated La Jolla yellowtail catches are January and July, and even those months are inferred from upload dates. | The anchor-vs-drift commit call at the Coronados — when to drop the hook on a mark versus keep working the circuit — is a flagged gap. | California/CDFW bag and size limits for yellowtail, and any Mexican (CONAPESCA) limits, are a flagged gap; the KB says verify with the issuing agencies. | No documented yellowtail presentation re-rank at 14–16 kt — the corpus threshold is ~20–25 kt+ and the KB flags even that as a single unitless 'pushing 25' figure. | locations/425-bank.md is a position-only minimum page: no run, no structure, no species, no program, despite the 425 having the warmest and cleanest water in the given set. | No corpus doctrine on booby behavior, despite boobies being the bird Cameron rates specifically at the Coronados. | Gear gaps against the plan: no Salas 7X-class heavy iron for punching casts in wind, no 6X Jr-class yo-yo jig for the 60–100 ft band, and no slow-pitch/knife-jig setup (still an open item in profiles/cameron/rods.md). | The KB's yo-yo jig sizing is internally contradictory — techniques/yo-yo-iron.md keys 6X vs 6X Jr to depth at 5–6 oz, species/yellowtail.md keys the same pair to current at 8 oz / 4 oz — and neither note resolves it.

</details>

### 2. [trip] It is blowing outside. I am launching from Dana Point. What is fishable today and for what? Assume these condi…

**Winner:** NOW · mapping {'A': 'B2', 'B': 'NOW', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three make the same correct call — outside is a no-go, fish the Dana Point-to-Oceanside kelp and reef strip for calico/sand bass with barracuda and bonito, halibut second — and all three stamp regulations properly and admit the missing swell period, moon phase and chlorophyll scale. B separates on the "where": it is the only one working from an actual Dana Point zone page rather than a coordinate dump, so it classifies each spot (boiler rock vs kelp vs beach break), gives inter-spot distances (0.41 nm, 1.75 nm and mostly east), notes there is no shallow bank to duck behind because the bottom is 2,000-3,000 ft a mile off the beach, and warns that San Clemente Kelp and AR are off the mainland city, not the island — a real error a new angler would otherwise make; I verified those figures verbatim in locations/dana-point.md. B is also the most disciplined: it states the {socal-bight, nearshore-coast} gate as binding before opening a species note, surfaces the KB's own unreconciled conflicts (anchor vs drift, 5:00 vs 7:00 barge), flags the MPA latitude as unverifiable, and asks for the null boat envelope instead of assuming it. C is a close second with the sharpest conditions reasoning (the Ekman/upwelling test on whether 67-69 F is a drop, and the calico temperature band), but overreaches by listing Leucadia and Del Mar rock as "in reach" on a building-wind day; A is the most complete on execution (drift control in 8-12 kt, halibut fight, fish care) but never applies the given SST to a species and lacks any zone-level geography.

- *B2 reasons:* found: right material — no-go call, kelp/bass primary, halibut second, paddy/harbor fallbacks; only answer that never applies the given SST to a species preference band. specific: coordinates, 40-42 ft hard bottom, 7" slug on 7/0 3/8-3/4 oz keel hook, 50-65 lb braid/60 lb fluoro, 2.5-3 ft 25-30 lb halibut leader, 1-10 oz balls, 5.5 kt troll. sourced: note paths plus video ids (NC3-3pJDEgo, HMdrP4-i9MM, M6U_FVdosr4, poqjnb1r1zk) that cross-corroborate the other answers. scoped: island/bank/open-ocean correctly refused, Catalina explicitly not called for lack of data; regs stamped California/CDFW + on-camera dates + verify-current. honest: strong gaps block — no chlorophyll threshold, no Dana Point Harbor note, no coastal nearshore rock program, three named tackle gaps, no relative time. actionable: most complete execution — bait-barge etiquette, 09:20 arrival, motor-as-rudder and drift-sock control in 8-12 kt, halibut fight, ice/salt slurry.
- *B3 reasons:* found: applies every given number — wind, seas, SST band (65-68 F, 67-69 at the top), chlorophyll via the color doctrine, and the 10:20 low; best conditions reasoning, including whether 67-69 is a drop (Ekman/upwelling mechanism). specific: spot table, 0-8/20-100 ft, 10-25 casts then move 100 ft/100 yd, 2-3 oz surface vs 5-6 oz yo-yo iron, 4:1 Jigmaster retrieve speed, two-loop gangion 1.5 ft apart with 24 oz torpedo, 1/4-1/2 oz slider with No.2/No.4 bronze hook. sourced: paths plus ids (LqW32NSkObY, kzD0kSnnVPw, pcwcRdmWmLc, OpcKQPA3vAI) consistent with the others. scoped: explicit envelope gate, ocean whitefish correctly gated out on waters, regs carry CDFW + as-of + verify except the spotted-bay-bass no-minimum line which names no jurisdiction; listing Leucadia and Del Mar rock (~28-33 nm south) as 'in reach' on a building NW day is a judgment stretch it never range-checks. honest: solid gaps list including the null boat envelope, no Dana Point zone guide, no drift-management doctrine, no chlorophyll scale. actionable: fully runnable, three programs plus harbor bail-out, wind-specific iron and sounder adjustments, named gear gap without substitution.
- *NOW reasons:* found: only answer to open a real Dana Point zone page and a spot page; applies the given SST to the 65-68 F calico band; leaves the given chlorophyll unapplied in the body (relegated to the gaps list). specific: charted positions plus derived geometry (Salt Creek-Monarch 0.41 nm, Barber Poles 1.75 nm and mostly east), 2,000-3,000 ft a mile off the beach, 0-8/20-100 ft working depths, No.4-6 hooks on 1/16 oz shot never over 1/4 oz, 35-40 ft AR chum, 15 lb inshore halibut class. sourced: dense note links plus ids; I verified dana-point.md and its 2,000-3,000 ft, 0.41 nm and 1.75 nm figures and the mainland-vs-island warning exist verbatim in the repo. scoped: explicit {regions: socal-bight, waters: nearshore-coast} gate stated as binding before any species note; regs carry CDFW + as-of + verify, and it flags the calico bag limit as jurisdiction-unnamed rather than asserting it; no halibut size limit offered. honest: best — surfaces internal KB conflicts (anchor vs drift, flyline bait, 5:00 vs 7:00 barge), flags the MPA latitude as an unverifiable annotation, refuses gear substitution, asks for the null range_nm/sea_state_max_ft. actionable: runnable, but misses the wind-up-heavier-iron adjustment on a wind day and its primary presentation has no owned tackle.

<details><summary>Full prompt</summary>

It is blowing outside. I am launching from Dana Point. What is fishable today and for what? Assume these conditions and do NOT fetch live data: late September. Outside: NW 20-25 kt, seas 6-8 ft at San Nicolas, Santa Barbara Island and the outer banks, Small Craft Advisory through Sunday. Inshore Dana Point to Oceanside: NW 8-12 kt, 3-4 ft, SST 67-69 F, chlorophyll 1.2 along the kelp. Low tide 10:20.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

## Short answer

Outside is a **no-go**, and it's not a close call. Fish the **Dana Point → Oceanside inshore strip** — kelp-edge and hard-bottom **calico bass / sand bass**, with **barracuda and bonito** mixed in, **halibut** on the sand next to structure as the second program, and a quick look at any **inshore kelp paddy** you cross for yellowtail. Dana Point Harbor is the bail-out if the inside builds.

---

## 1. Why the outside is off

Your outside numbers (NW 20–25 kt, 6–8 ft, SCA through Sunday) blow past every go/no-go threshold the KB carries. From `conditions/sea-state.md` (dave-hansen, `NC3-3pJDEgo`, 2020-11-18 — a registered voice but this specific threshold set is single-mention, medium confidence):

- **Wind above ~12 kt is what raises whitecaps**, and his personal cutoff is not to run when it's blowing over 12 kt.
- The **named unfishable combo** is **12–15 kt with 4–8 ft at a 9-second interval** — "you just cannot be caught out there," and he holds *larger* boats at the dock in it too. You have more wind and the same seas.
- **Captain's-call framing:** a big-red-flag forecast is a "we are not going," not a "let's see."

Two more from the same note that shape today even inside:

- **Forecast error is asymmetric** — assume it errs on the worse side, and that afternoon W at the islands strengthens rather than eases (Ep. 6). And: if it is windier than forecast in the morning, **assume it builds all day — a small boat bails early** (7/14/22).
- **Homebound wind** — plan the return leg against the afternoon build, not the outbound conditions (8/17/22). If you run south toward Oceanside, you're coming back up into it.

Your boat backs this up: `profiles/cameron/boat.md` — Panga Marine Marquesas 22, single 115 hp, **no trim tabs**, and the trim routine calls for a rider forward on the bow bean bag underway, with the note's own remark that **rough days forward are brutal** (rider catches air, then hits the deck).

**What that costs you today:** the September grade-bluefin program. `seasonal/september.md` (`5to3Q5P7w90`) puts the bigger bluefin in the **"volume square" — SBI–San Nicolas–Clemente–Catalina** — which is exactly the water under the advisory. That's a wait-for-the-window target, not a today target.

I am **not** making a Catalina call: you gave me no wind/sea numbers for the channel or the island, and I'm not fetching any. For reference, `conditions/sea-state.md` flags the ridge off **Catalina's east end** as a bathymetric slop hotspot (bad for a few miles, lays down 3–4 mi past it), and `locations/bight-geography.md` (`HzE4FHHcvTk`) notes that **south of Newport is less prone to NW wind-wave rollover** and that the Coronados/Catalina/SCI **held their water** through a big NW event — but that's a *water-temperature* map, not a sea-state permission slip.

---

## 2. Today's program — the coastal strip

### Read of your inshore conditions

- **SST 67–69 °F, chl 1.2 along the kelp.** `conditions/water-color.md` warns that a green signal has an **age**: a *new cold bloom* (overnight ~5 °F drop + green after an afternoon NW wind = local upwelling) is a short-term negative to mark for later; a **mature bloom edge** is what you fish. You gave a steady inshore SST with no drop, so this doesn't read as a fresh rollover — but check for a sudden temp break as you run. Cameron's own doctrine in the same note: in warm-water years weight color at least as heavily as SST, and **don't fish dirty-green water for gamefish**.
- **For kelp bass, some stain is a plus.** `species/calico-bass.md` carries an observed read of **green-stained, near-opaque water with roughly 5–10 ft visibility** as the preferred kelp-edge bass color — the stain gives fish a place to hide and makes them feed up in the open (`9xNhdu2aBqE`, medium confidence).
- **The switch is current, not the tide clock.** `species/calico-bass.md` + `conditions/current-structure.md`: calico are **current-driven and largely tide-indifferent**. Parallel current (uphill or downhill) = good; **into the beach** = marginal; **straight off the beach** = dead, skip it.
- **Read current off the kelp** (`conditions/current-diagnostics.md`): kelp **pulled ~20 ft under** = raging, surface presentations are dead; **laid down** = strong, fishable; **resurfacing** = slacking, switch back to the surface. A second tell for the current shutting off: **bites on nearly every drop, then several drops with nothing** (dave-hansen, `aFb221LUoD0`, medium confidence).
- **Corner selection** (`conditions/current-structure.md`, dave-hansen `kzD0kSnnVPw`, medium confidence, single mention): at a named kelp bed — his examples include **San Onofre**, on your stretch — **downhill current → work the NW corner of the bed; uphill → work the SE corner.** Same source-family also keeps a **per-spot wind-direction record** (some spots fish on NW wind, others on SE — `xI9tPJFXbUM`, medium confidence); today is a NW-wind day, so log which of these beds produce on NW for next time.
- **Spot check-in shorthand** (`species/white-seabass.md`, `82gEHYel-4U`): milky water + a readable uphill/downhill current + that current lining up with the reef or kelp line = worth a shot.

### Timing

- **Bait first.** `bait/making-bait.md` (dave-hansen, `7WapaxdtjQg`, 2022-01-04, Dana Point example): **avoid the 6:00 a.m. sportboat rush** — go at **5:00 or 7:00**. Follow the barge's side signal (**at Dana Point, a cone on the ocean side**), hail on **VHF 11** with the barge name twice plus your boat name, **never board the barge**, ask for it **loaded light**, and tip the attendant.
- **Low tide 10:20.** `conditions/tide-and-slack.md`: be on your highest-percentage zone **an hour before the change** — so **fishing by ~09:20**, not arriving at 10:20. The **late-morning slack** (a tide falling after ~9:30) is the prime open-water pop-up window, and pop-ups also **cluster in the afternoon**, so re-run water you marked in the morning at the afternoon tide time. Also: **on marginal days action compresses into the tide windows** (wide-open days bite all day, 8/17/22) — today is a marginal day, so anchor your zone rotation to the tide rather than roaming freely.
- Caveat that matters: that arrival discipline is for the **slack-tide biters** (white seabass, marlin, bluefin foamers). Your primary target, calico, is tide-indifferent — for them the kelp lean is the clock. Your 8 a.m. norm departure (`profiles/cameron/boat.md`) still lands you fishing before 9:20 if you're bait-in-the-tank early.

### Where — named spots on this stretch

From your own committed library, `sources/spot-lists.md` (repo-public, waiver on file per `CLAUDE.md`):

**Dana Point section**
- Dana Point Kelp — Red Buoy — **33 27.320 / 117 43.380**
- Barber Poles — **33 26.710 / 117 41.410**
- Salt Creek — **33 28.565 / 117 44.040**
- Monarch Boilers — **33 28.970 / 117 44.020**
- San Clemente Kelp (mainland city) — **33 24.450 / 117 38.140**
- San Clemente Artificial Reef — **33 23.890 / 117 37.200**
- The Hospital 100 Fathom Curve — **33 29.500 / 117 47.100** — *the list annotates: stay S of the MPA at 33 30.050*

**Oceanside / North County**
- San Onofre Kelp — **33 20.880 / 117 34.050**
- Barn Kelp — **33 17.015 / 117 29.475**
- Box Canyon rockfish area — **33 17.290 / 117 34.150**
- Pendleton AR Center — **33 19.500 / 117 31.700**
- Oceanside AR 2-series cluster — around **33 12.2–12.9 / 117 25–26**

Two direct local precedents in the KB for exactly this run:
- `species/calico-bass.md` (`HMdrP4-i9MM`, 2022-10-11): a boat **departed Dana Point and worked south**, finding calico and sand bass over **hard bottom with light kelp that did not reach the surface — kelp riding roughly 20 ft off the bottom in ~40–42 ft of water**. Same trip's pre-trip briefing flagged **barracuda and 25–30 lb yellowtail recently seen in that stretch of coast.** Techniques that produced: dropper loop, flylined sardine, squid or sardine strip fished dropper-style, and a soft plastic.
- `species/calico-bass.md` (`M6U_FVdosr4`, 2013-07-04, **Dana Point kelp bed**): boat **anchored** on a light current running through the kelp bed; the morning's tally was **5 sand bass + 3 calico, every one on a strip of squid** — then by day's end the same crew reported bass "actually biting the smaller sardines." Kept side by side, unreconciled: **carry both squid strips and small sardines.**

### How to fish it

Ranked off the `species/calico-bass.md` situations table:

1. **Weedless swimbait / slug** — short targeted casts to individual stringers and the leading edge, fast steady wind, **pause on the eat**. Rigging from `techniques/swimbaits.md`: a **7" weedless slug on a keel-weighted hook — Gamakatsu 7/0, 3/8 oz** (Landesfeind prefers the **3/4 oz** because it keeps the bait in the water while you wind fast); replace the stock spring with an **Owner large / Trokar XL** spring and bury it to the bait. Line: **50–65 lb braid on a 300-size reel to 60 lb fluorocarbon** (a second voice runs **65 lb braid to 40 lb mono**, cinched down tight — kept side by side, `9xNhdu2aBqE`). **Set on the pause, never on the grab** — swing on the grab and nine times out of ten you pull it out of the fish's mouth.
2. **Surface iron along the kelp line** — steady grind, change kick/speed to the bite. **This is the wind adjustment:** `techniques/surface-iron.md` — **wind up → heavier iron** (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`), corroborated by the three-iron-box framework (`A70kK2niu2Q`) whose third slot is exactly "heavier, casts through wind/chop." Counter-case: if the forage is small anchovy ("rice"), **drop to a Tady AA-light / A1-light class — roughly a third the weight of a Tady 45 — and the small jig out-bites the big one two or three to one** (`pcwcRdmWmLc`), which then drags the whole setup down to a medium-action 9 ft stick and ~50 lb braid.
3. **Flyline a sardine or mackerel** on the up-current edge when live bait's aboard and fish sit deeper on the edge or in wind — 25–40 lb class.
4. **Raging current / kelp pulled under** → subsurface: sunk iron or leadhead, or wait for the slack; **resurfacing kelp = go back on top.**
5. **Chum-and-anchor** a kelp edge with parallel current: chum the spot, reposition up-current, back down onto it as the anchor sets — fish come out of the kelp as the anchor goes down (`RXNebDr4j7s`, via `techniques/chunking.md` reference in the calico table).

**Working method** (`species/calico-bass.md`, Ep. 13/14): the **up-current / leading edge is the spot** — calico face into the current and ambush from the front (Benny Florentino, `Rwy4MqeXCIU`). Hit three or four sides of a kelp head and you know in **two or three casts**. **10–25 casts to the prime edge, then move 100 ft or 100 yards.** Beds re-bite — come back later. Working depths run the **outside kelp edge ~50 ft in to ~25 ft**, and calico will rise **10–15 ft off 80–100 ft of reef** to eat a crank or a sunk iron. Bird tell: **cormorants diving *in* the kelp** = actively feeding, better than gulls inshore. Bait grade on the meter: **solid unbroken wall = no predators; broken, harried bait = predators on it.**

**Barracuda and bonito** ride along (`species/barracuda.md`, `species/bonito.md`): fast, flashy surface-iron retrieve for both; add a **short single-strand wire (haywire twist)** or heavy hard mono the moment you start getting bit off by 'cuda. There's a Dana Point-specific bonito data point in `species/bonito.md` (`poqjnb1r1zk`, 2019-07-02): a 5:45 a.m. start south of Dana Point Harbor then working north, **small feathers rigged as a small daisy-chain trolled at roughly 5.5 kt**, plus a small sardine-profile diving hard bait cast and twitched behind the boat. That's a legitimate way to cover this coast in chop between kelp stops.

**If you mark yellowtail** on the hard bottom (they were reported in this stretch at 25–30 lb): `species/yellowtail.md` — **tight balls hugging structure, classic arcs/boil-ups at ~5–10 fathoms near structure** → **yo-yo iron** (heavy Salas 6X class, hit bottom, **a couple of cranks off the bottom = the reaction bite**) or a **dropper loop** with live bait to the same marks, on a **40–60 lb class stout rod with a high-speed reel**. Structure yellows sit on **hard bottom only, never mud** — read bottom hardness before you work a spot.

### Second program — halibut

`species/california-halibut.md` (Landesfeind Ep. 15, `OpcKQPA3vAI`): the game is **sand within 5–20 ft of a hard edge** — a rock, a shale reef, a channel edge, an eelgrass line. Even a **15-ft-wide rock that barely paints** changes the current and holds a fish. The coastal version is **off-color water just outside the surf line** where shale sits outside the beach (a 40–50 lb fish came out of a Huntington bubbler zone in **30 ft**). Your chl-1.2 stained kelp-line water is the right family of water — but apply the **triad**: **off-color + current + bait, all three. Missing one → leave inside 20–30 minutes** (`conditions/tide-and-slack.md`, `conditions/water-color.md`, `6TBxHnkYXI0`).

Rig: **trap rig off a three-way with a breakaway sinker**, **30 lb mono class** outside (mono for stretch on the bolting run), **fluorocarbon leader 2.5–3 ft, 25–30 lb**, **ball/cannonball sinkers 1–10 oz** to conditions. Short controlled drifts along the edge, not long random sand drags — a two-angler private boat should **isolate the structure and pick it apart**. Fight: one long bolting run, then **high rod tip and a straight, light-drag grind, no pumping**; keep the head underwater to the gaff.

**Wind-day drift control** (`planning/search-and-glassing.md`): stop on arrival, note the stopping point, and watch which way and how fast wind/current move you **before** dropping. Angle the outboard off the keel line to use it as a **rudder** to slow/steer the drift; **drop the motor back in and/or deploy a drift sock** to slow a fast drift; pull the motor out to speed a slow one. In 8–12 kt of NW you'll be pushing, not drifting — this is the part that makes or breaks a halibut drift today.

### Third — check any paddy you cross

`locations/bight-geography.md` and `conditions/kelp-paddies.md` (8/17/22, `HzE4FHHcvTk`): the **best coastal paddy water is exactly Dana Point to Oceanside and southward**; paddies are **scarcer and hold less north of Dana Point.** Discipline (`ZFqe49jRgA0`, `4xzK7YaXK5s`): **drive right up to it like it's the dock** — a paddy isn't spooky — look for visible fish, check the meter for **boomerang-shaped arcs at typically 90–120 ft**, give it a **minute, maybe two**, one bait, then move. **A dry paddy stays dry all day** (they only restock at night). Once you find a live one, **search its line** — N–S in open water under the uphill current, along the contour near a bank edge.

Temperature reality check: `species/dorado.md` / `conditions/water-temperature.md` put dorado on the **green-cold/blue-warm boundary around ~71–72 °F** (`E4vKwRaRueA`). At **67–69 °F** inshore you're below that band, so treat inside paddies today as a **yellowtail/bonito** bet, not a dorado bet. On a live paddy: flylined bait first, then surface iron/casting jig.

### Bail-out — Dana Point Harbor

`locations/bays-and-harbors.md` + `species/spotted-bay-bass.md`: a harbor is a **tidal system first**, and spotted bay bass are **fully tide-driven** (the exact opposite of the calico outside). Work **eelgrass edges, channel drop-offs, riprap, and dock/piling fields** — and **favor old, weathered pilings over new ones**; the growth on them is what holds fish (`usHl-4SfqDA`). Set up **up-current of the structure**, cast **up-current across the grain of the eelgrass lean** (retrieving against the grain snags; a bass sits facing up-current anyway — `EGKesj7V64M`). Note the timing nuance: **roughly the half hour either side of the turn, current all but stops** — so around your 10:20 low, fish the moving water on either side rather than the turn itself. Lures: **Zoom fluke on a 1/4–3/8 oz ballhead flipped tight to pilings**, Ned rig, drop shot, small cranks — light spinning / low-profile, 10–20 lb.

---

## 3. Gear off your profile

| Job | Your setup (`profiles/cameron/rods.md`, `tackle.md`) |
|---|---|
| Surface iron on the kelp line | **Torium 20HG on the Phenix Abyss 10'0" (25–60 lb), 50 lb braid** — your full surface-iron setup |
| Wind-punching iron | **Nomad Slidekick 120g (4.25 oz)** — heavier than traditional irons and can be sunk out to cover the column; **JRI-7** (~Tady 45 class) is your local/kelp all-rounder |
| Flyline sardine/mackerel | **Avet MXJ on the Teramar 90MHB2 (9'0", MH, 30–65 lb), 50 lb braid** — step the leader down for kelp-line bass |
| Yo-yo / dropper loop if yellowtail or bottom fish show | **Trinidad 40 on the 8'0" XH 40–80 lb blank, 80 lb braid** (yo-yo iron, sinker rigs) with the **Salas 6X** |
| Closest thing you own to a bass/swimbait stick | **Tranx 400 on the Phenix M1 SMX-82H (8'2", H, 20–45 lb)** — but your own note has its **braid TBD, respool pending**, so confirm before you leave the dock |

Three honest gaps in your kit for today's primary program: your tackle note is **hard baits only** — no soft plastics, slugs, or keel-weighted weedless hooks recorded, so the #1 calico presentation is a **class-term recommendation, not an owned-gear one**. Likewise there's **no trap-rig / three-way / breakaway terminal** recorded for halibut, and **no light spinning class** for the harbor finesse fallback.

Boat: 30-gal tank, **100–125 lb of ice per trip**, and drain the bait tank before the run home per your trim routine.

---

## 4. Off the table today, and why

- **Bluefin in the volume square (SBI–Nick–Clemente–Catalina)** — that's the September grade water (`seasonal/september.md`, `5to3Q5P7w90`), and it's the water under the advisory.
- **Outer banks / offshore paddy line** — same reason.
- **White seabass** — `species/white-seabass.md` makes it a **moon-clustered, squid-driven, gray-light/night island program** on the slack. You gave me no moon phase and no squid, and the island grounds are blown out. The **off-color triad** from that note still governs any milky inshore water you fish today.
- **Lobster** — `species/california-spiny-lobster.md` puts the season at roughly **early October through mid-March**; late September is **before the opener**. Regulation, not water state — confirm the exact date with CDFW.
- **Rockfish/lingcod** — the KB's programs are **island shallow (100–250 ft)** and **offshore/coastal deep (300–900 ft)**, and it says plainly that **season, depth limits and the year-end closure change annually and are not encoded here** — verify with CDFW. Your list does carry coastal rockfish ground on this strip (**Box Canyon 33 17.290 / 117 34.150**), but the KB has no dedicated coastal-nearshore-rock program for the Dana Point–Oceanside band.
- **Sheephead** is a legitimate windy-day add: `species/sheephead.md` puts them on the **numbered Carlsbad AR / Oceanside AR clusters** and inshore rocky structure, **chum-driven** — the bite turns on once chum is in the water.

**Regulations** (California / CDFW, as stated on camera in the cited sources — **verify current before you fish**): **14 in** minimum for kelp bass and sand bass (`HMdrP4-i9MM`, 2022); **22 in** minimum for California halibut (`MUpvP-Yl2R0`, 2016). Honor the MPA annotations carried in your own spot list (stay **S of 33 30.050** at The Hospital; **N of the SMCA at 33 03.000** at Encinitas; **N/W of the MPA at 33 33.233 x 117 49.200** at Abalone Point).

**Fish care** (`fish-care/dorado-and-general.md`): ice immediately, **salted slurry — ~2 cups rock salt per 7–10 lb bag of ice plus a splash of seawater**, and **never freshwater-rinse** the catch. `species/bonito.md` carries two independent data points that **bleeding and icing a bonito immediately** is the whole difference between "trash fish" and near-yellowfin table quality — worth doing if you box one.

---

## 5. What I could not resolve from the knowledgebase

- **No swell period.** You gave heights but not intervals. `conditions/sea-state.md`'s steepness rule (**10 ft @ 15 s is barely felt; 3–4 ft @ 4–5 s is brutal**) and the **sub-10-second hard bad-sea flag** can't be applied without it — and your inshore 3–4 ft could be short-period wind chop, which would be materially worse than the number suggests. Pull the period before you commit.
- **No moon phase**, so the moon-gated doctrine is unusable: `species/calico-bass.md` warns that on clear full-moon nights calico gorge after dark and **shut down by mid-morning** (bite first light or late afternoon), and `conditions/moon.md` is what would tell you whether today is one of those days.
- **Chlorophyll 1.2 has no threshold in this KB.** The notes handle water color qualitatively (new bloom vs mature bloom edge, "don't fish dirty green") — nothing maps a numeric chlorophyll value to a go/no-go.
- **No Dana Point Harbor note.** `locations/bays-and-harbors.md` names San Diego Bay, Mission Bay, Newport, Huntington Harbour and the LA/Long Beach complex; the structure knowledge is universal, but there is no Dana Point Harbor-specific page.
- **No current direction given**, and the parallel-current rule is the single biggest lever on the calico program. You'll have to read it on the water off the kelp lean and the chum-drift angle.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/water-regimes.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/kelp-paddies.md`, `seasonal/september.md`, `seasonal/october.md`, `species/calico-bass.md`, `species/sand-bass.md`, `species/barracuda.md`, `species/bonito.md`, `species/yellowtail.md`, `species/california-halibut.md`, `species/white-seabass.md`, `species/dorado.md`, `species/rockfish-lingcod.md`, `species/ocean-whitefish.md`, `species/sheephead.md`, `species/california-spiny-lobster.md`, `species/spotted-bay-bass.md`, `techniques/surface-iron.md`, `techniques/swimbaits.md`, `techniques/flyline.md`, `locations/bight-geography.md`, `locations/bass-structure.md`, `locations/bays-and-harbors.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `fish-care/dorado-and-general.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`  
*videos:* `NC3-3pJDEgo`, `HzE4FHHcvTk`, `5to3Q5P7w90`, `HMdrP4-i9MM`, `M6U_FVdosr4`, `poqjnb1r1zk`, `9xNhdu2aBqE`, `Rwy4MqeXCIU`, `RXNebDr4j7s`, `D5DR7Kx42_A`, `A70kK2niu2Q`, `pcwcRdmWmLc`, `kzD0kSnnVPw`, `xI9tPJFXbUM`, `aFb221LUoD0`, `ZFqe49jRgA0`, `4xzK7YaXK5s`, `OpcKQPA3vAI`, `6TBxHnkYXI0`, `MUpvP-Yl2R0`, `E4vKwRaRueA`, `7WapaxdtjQg`, `EGKesj7V64M`, `usHl-4SfqDA`, `82gEHYel-4U`  
*gaps admitted:* No swell period given for either the outside or inshore seas, so the KB's steepness rule (3-4 ft @ 4-5 s is brutal; sub-10-second interval is a hard bad-sea flag, conditions/sea-state.md) cannot be applied to today's 3-4 ft inshore chop. | No moon phase given, so the moon-gated doctrine is unusable: the full-moon calico shutdown by mid-morning (species/calico-bass.md), white seabass moon clustering (species/white-seabass.md), and the lobster dark-night preference (conditions/moon.md) could not be factored in. | The KB has no numeric chlorophyll threshold — it only distinguishes a new cold bloom from a mature bloom edge qualitatively (conditions/water-color.md), so the given value of 1.2 cannot be graded good or bad from the notes. | No current direction or strength was given, and the parallel-current rule is the largest single lever on the kelp-bass program (conditions/current-structure.md); it has to be read on the water rather than planned. | There is no Dana Point Harbor note — locations/bays-and-harbors.md covers San Diego Bay, Mission Bay, Newport, Huntington Harbour and the LA/Long Beach complex only, so the harbor fallback rests on universal structure knowledge, not a local page. | No conditions were given for the Catalina channel or the island, so no Catalina call is made; the KB's wind-rollover map (locations/bight-geography.md) is about water temperature holding, not sea state. | The KB carries no coastal nearshore rockfish/lingcod program for the Dana Point-Oceanside band — its rockfish notes cover island shallow (100-250 ft) and offshore/coastal deep (300-900 ft) only — and it explicitly does not encode current-year CDFW seasons, depth limits, or the year-end closure. | Ocean whitefish is documented only as a Channel Islands hard-bottom fishery in this KB, so it is not routed as a coastal-strip option today. | Cameron's profile records no soft plastics, slugs, or keel-weighted weedless hooks, no halibut trap-rig/three-way terminal, and no light spinning class, so those recommendations degrade to class terms rather than owned gear; the Tranx setup's braid weight is still listed as pending respool. | Regulatory figures carried here (14 in kelp/sand bass, 22 in halibut, roughly early-October lobster opener) come from dated on-camera statements in the corpus, not current CDFW rules, and must be verified before fishing.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Blown out outside, fishable inside — go bass/kelp, from Dana Point south

**Short version:** everything the late-September priors would send you at is in the water that's blown out. Stay inside the 3–4 ft band, fish the Dana Point → San Onofre kelp and reef edges for the calico/barracuda/bonito complex, with coastal hard bottom (rockfish/sheephead) as the second half and Dana Point Harbor as the bail-out. Be on your best kelp edge by **09:20** for the 10:20 low.

---

## 1. The day's envelope (protocol step 1b — this is binding)

Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), I set `{regions, waters}` before opening a single species note, and anything outside it is **never offered**, not offered with a caveat.

- **regions:** `socal-bight`
- **waters:** `nearshore-coast` (plus `bay-harbor` if it deteriorates)
- **Out today:** `island`, `bank`, `open-ocean` — SCA, 6–8 ft at San Nicolas / Santa Barbara Island / the outer banks.

That single filter kills the whole late-September A-list:

| September prior | Why it's out today |
| --- | --- |
| The **"volume square" — SBI–San Nicolas–Clemente–Catalina — holds the bigger bluefin** in September ([`seasonal/september.md`](seasonal/september.md), `5to3Q5P7w90`) | That is literally the blown-out box |
| **Dorado in open-water schools below Catalina**; **yellowfin volume near the border sliding north** (same note) | `open-ocean` — outside the envelope |
| Paddy program — best paddy water is **south of SCI/Catalina and the Dana Point→Oceanside strip** ([`conditions/kelp-paddies.md`](conditions/kelp-paddies.md), [`locations/bight-geography.md`](locations/bight-geography.md), `HzE4FHHcvTk`) | The strip is your water, but the KB files paddies as `open-ocean` structure and gives no guidance on paddy fishing inside a 3–4 ft nearshore band. If you cross one *inside* the fishable band, the doctrine is: **drive right up to it like it's the dock**, look under it, check fast — **a dry paddy stays dry all day**, fish only move paddy-to-paddy at night (`4xzK7YaXK5s`) |

**Sea-state sanity check.** The one numeric go/no-go the KB carries is Dave Hansen's (medium confidence, single mention): wind **above ~12 kt is what raises whitecaps**, his personal cutoff is not to run over 12 kt, **sub-10-second swell interval is a hard bad-sea flag**, and **12–15 kt with 4–8 ft at 9 s** is his named "you cannot be caught out there" combo ([`conditions/sea-state.md`](conditions/sea-state.md), `NC3-3pJDEgo`, 2020-11-18). Your inside numbers (8–12 kt, 3–4 ft) sit right at the top of that cutoff, and **you did not give me a swell period** — the steepness rule in that same note is blunt: **3–4 ft at 4–5 s is brutal**, while 10 ft at 15 s is barely felt. Get the period before you commit; it decides whether this is a pleasant day or a beating.

Two more from that note that apply directly:
- **Forecast error is asymmetric** — assume it errs worse. If it's windier than forecast in the morning, **assume it builds all day and bail early** (small-boat rule).
- **Homebound wind:** plan the return leg against the afternoon W build, not off the outbound conditions. Work south early, be heading home before it stands up.

## 2. Why the inside band is actually the right side of this blow

This isn't just "settle for the inside." [`locations/bight-geography.md`](locations/bight-geography.md) (`HzE4FHHcvTk`, Landesfeind 4/21/22) maps NW-blow geography explicitly:

- **Gets crushed:** the northern Channel Islands and the LA/Ventura coastal shelf — a strong NW event rolls surface temp down **5–8 °F** there.
- **Less prone:** **south of Newport** — "less prone to wind-wave-driven rollovers."
- **Held through it:** Coronados, the tuna grounds, Catalina, San Clemente.

Dana Point → Oceanside is the sheltered-geometry side of that map, and your **67–69 °F** reading is consistent with water that held.

**The one thing I can't settle for you:** whether 67–69 °F is *steady* or a *drop*. The rule is that an overnight **~5 °F drop plus green water after NW wind** is a fresh local upwelling event — **cold, green, bad now, mark it for the recovery** — versus a **mature bloom edge**, which is what you fish ([`conditions/upwelling-and-turnover.md`](conditions/upwelling-and-turnover.md), [`conditions/water-color.md`](conditions/water-color.md)). The mechanism says to expect it: a NW alongshore wind deflects surface transport 90° right — offshore — which draws cold water up at the coast (Ekman transport, `32TQdFJKIlI`). With a multi-day NW event running, check your 24–48 h SST trend at the kelp before you believe the 67–69.

Your own standing doctrine also bears on the chlorophyll number: **in warm-water years you weight chlorophyll at least as heavily as SST and won't fish dirty green water for gamefish** (`cameron`, [`conditions/water-color.md`](conditions/water-color.md)). **The KB gives no numeric chlorophyll scale**, so I can't tell you what 1.2 "is" — that's a gap, flagged below. What the corpus *does* say for kelp-edge bass specifically cuts the other way: a **green-stained, near-opaque water color with roughly 5–10 ft of visibility** was called the preferred read for kelp-edge bass, because the stain gives fish a place to hide and makes them comfortable feeding up (`9xNhdu2aBqE`, San Clemente Island 2015-10-28, medium confidence). Judge it with your eyes at the kelp, not off the number.

## 3. The clock

- **Low tide 10:20.** Arrival discipline: **be on your highest-percentage spot an hour before the change** — **09:20**, fishing, not arriving ([`conditions/tide-and-slack.md`](conditions/tide-and-slack.md)). The **late-morning slack** (tide falling after ~09:30) is called the prime pop-up window, and pop-ups also cluster in the afternoon — so re-run water you marked earlier.
- **Window compression:** when conditions are marginal (this is marginal), the action **compresses into the tide windows** — anchor your zones to tide times rather than routing freely (same note, 8/17/22).
- **Bait:** if you're buying, the Dana Point barge fills the sportboat fleet at **06:00** and the line forms by a quarter to six — target **05:00, or 04:30** ([`bait/making-bait.md`](bait/making-bait.md), `7WapaxdtjQg`, `bM2vUS1B-yQ`; [`bait/bait-tanks.md`](bait/bait-tanks.md), `ztpj1Xll0-U`). Cone marks the tie-up side on the ocean side; hail on **VHF 11**; tell them to load it light. Note your own profile has departure ~08:00 as the norm ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)) — that misses the barge window entirely.

## 4. Plan A — the kelp/reef bass complex (calico, barracuda, bonito)

This is the target the envelope, the season and the water all agree on. [`species/calico-bass.md`](species/calico-bass.md) is `regions: socal-bight`, `waters: nearshore-coast, island, bay-harbor` — in envelope, and a year-round coastal fishery that peaks in the warm months.

**Spots (charted positions from [`sources/spot-lists.md`](sources/spot-lists.md), N→S from your ramp):**

| Spot | Position |
| --- | --- |
| Monarch Boilers | 33 28.970 / 117 44.020 |
| Salt Creek | 33 28.565 / 117 44.040 |
| Dana Point Kelp — Red Buoy | 33 27.320 / 117 43.380 |
| Barber Poles | 33 26.710 / 117 41.410 |
| San Clemente Kelp (mainland) | 33 24.450 / 117 38.140 |
| San Clemente Artificial Reef (mainland) | 33 23.890 / 117 37.200 |
| San Onofre Kelp | 33 20.880 / 117 34.050 |
| Barn Kelp | 33 17.015 / 117 29.475 |
| The Hospital 100-fathom curve (**stay S of the MPA line at 33 30.050**) | 33 29.500 / 117 47.100 |

**How to pick which end of which bed — this is the whole game:**

- **Calico are current-driven and tide-indifferent.** Read the current across the kelp, not the tide clock ([`species/calico-bass.md`](species/calico-bass.md)).
- **Parallel-current rule** ([`conditions/current-structure.md`](conditions/current-structure.md), [`locations/bass-structure.md`](locations/bass-structure.md), Landesfeind Ep. 14): current **parallel** to the beach = good (definable leading edge); **into** the beach = marginal; **off** the beach = **dead, skip it**.
- **Corner call** (`kzD0kSnnVPw`, Dave Hansen — San Onofre is one of his named examples; medium confidence): **downhill current → work the NW corner of the bed; uphill → the SE corner.**
- **Anchor the bed, don't drift through it** (`sIoNELGlxmk`) — drifting through gives up the edge-holding pattern. On hard, kelp-free rock with nothing to read, **drop the anchor and watch which way the line points** — that's the current read; expect to reset it repeatedly ([`conditions/current-diagnostics.md`](conditions/current-diagnostics.md)).
- **Kelp lean is your current gauge** (same note): pulled ~20 ft under = raging, surface presentations dead, go vertical; laid down = strong, fishable; **resurfacing = slacking, switch back to the surface.**
- **The biting fish sit on the up-current / leading edge** — calico face into the current and ambush from the front of the kelp (`Rwy4MqeXCIU`, Benny Florentino). Hit three or four sides of a head; you know in two or three casts.
- **Cover water:** **10–25 casts to the prime edge, then move 100 ft or 100 yards** to the next stringers. Beds re-bite — come back later. Coastal-panel version of the same rule is 10–20 casts (`XyKF34C5iB4`).
- **Depths:** work the outside kelp edge ~**50 ft in to ~25 ft**; calico will rise **10–15 ft off 80–100 ft of reef** to eat. Tommy Ponce's Dana Point water specifically: **0–8 ft and 20–100 ft** (`LqW32NSkObY`, medium confidence).
- **Temperature:** Ponce's stated preference is **65–68 °F**, with fish going lethargic past ~70 (`LqW32NSkObY`, medium, single source). **Your 67–69 sits at the top of that band** — fine, but if the shallow edge feels dead, drop to the 20–100 ft side.
- **Light:** bright/stable light pushes calico up into the **outer canopy edge**; overcast spreads them through the column and structure (`RUuPNpK0x-s`, medium).
- **Sign:** **cormorants diving *in* the kelp** = actively feeding = the calico tell, better than gulls inshore. On the meter, a **solid unbroken wall of bait has no predators on it; broken, harried bait does.** Same read visually: "happy," meandering bait = keep running; **balled-up, fast-moving bait = stop and fish it** ([`planning/search-and-glassing.md`](planning/search-and-glassing.md), `XyKF34C5iB4`).
- **Sounder caveat for a 3–4 ft day:** in chop the transducer cone has to be shot lower, so **fish high in the column won't paint until you're right on top of them** — not a gain setting to fix (`fgTmUq78ofQ`, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)). Don't write a bed off on a clean-looking screen today.

**Techniques, ranked for today's wind:**

1. **Surface iron along the kelp line** — steady grind, bigger cruising fish, and the presentation the wind actually favors: **wind up → step up to a heavier iron** (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`, [`techniques/surface-iron.md`](techniques/surface-iron.md)). A surface iron normally runs **2–3 oz** vs **5–6 oz** for a yo-yo iron (`VpW91AKOFVQ`). Don't over-wind it — these jigs were designed around a **4:1 Penn Jigmaster**; 6.5–7.5:1 is called too fast (`Ec2GaNpiOHI`). On a miss, **keep winding, never stop.**
2. **Flylined sardine/mackerel** on the up-current edge when there's bait aboard and fish are deeper on the edge or the wind's up ([`techniques/flyline.md`](techniques/flyline.md)).
3. **When the kelp goes flat/under (raging current):** go vertical — sunk iron or leadhead; switch back on top when the kelp resurfaces ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)).
4. **If they're on small anchovy ("rice"):** drop to a light iron (Tady AA-light/A1-light class, roughly a third the weight of a Tady 45) — on small bait the small jig out-bites the big one **two or three to one** (`pcwcRdmWmLc`).

**The mixed bag rides along:**
- **Barracuda** on the same kelp lines — fast, flashy retrieve, they chase a moving target; **rig for the teeth** when you start getting cut off: short single-strand wire on a haywire twist, or heavy hard mono as the line-shy compromise ([`species/barracuda.md`](species/barracuda.md)). A Catalina data point has one coming on a **Tady-45-class iron sunk to ~30 ft** before the retrieve (`oadK6zIYyCo`).
- **Bonito** — treat a boil as the **measure of life**; small chrome jigs / small irons into the foam ([`species/bonito.md`](species/bonito.md)). Dana Point local data point: a 05:45 start working south then north of the harbor, **small feathers as a mini daisy-chain trolled at ~5.5 kt**, plus a small sardine-profile diver cast and twitched (`poqjnb1r1zk`, 2019-07-02). Bleed and ice them immediately and they eat close to yellowfin (`H-vIGWPIPVc`, `0dIwWiOc1NY`).
- **Sand bass** mix in on the same hard bottom / reef-to-sand transition ([`species/sand-bass.md`](species/sand-bass.md)). Note they hover **above or within** structure, so cover the column.
- **Regs:** calico and barred sand bass minimum **14 in** (California/CDFW, as last checked 2022-04-25 — `r6j5w40fVHI`, `HMdrP4-i9MM`; calico bag limit 5/day is on record from 2019-03-13 and is the oldest figure in the register). **Verify current CDFW rules before you fish** ([`sources/regulatory-claims.md`](sources/regulatory-claims.md)).

## 5. Plan B — coastal hard bottom, second half or if the kelp is dead

[`species/rockfish-lingcod.md`](species/rockfish-lingcod.md) carries `waters: bank, island, nearshore-coast` — the coastal deep rock is in envelope. **Wind is less of a problem here than on the kelp:** it's a meter-and-chart fishery with no surface sign, and the drift does the work.

Coastal rock in reach (from [`sources/spot-lists.md`](sources/spot-lists.md)): **Box Canyon rockfish area 33 17.290 / 117 34.150**, **Leucadia rockfish area 33 04.100 / 117 20.600**, **Del Mar rockfish area 32 57.191 / 117 17.981**, **Encinitas rockfish / Devil's Rock North — stay N of the SMCA at 33 03.000 — 33 03.130 / 117 20.920**; plus the artificial reefs (**Pendleton AR center 33 19.500 / 117 31.700**, the **Oceanside AR 1A–2L** cluster around 33 10.9–33 13.0 / 117 25–26, **San Clemente AR 33 23.890 / 117 37.200**).

- **Find it:** run the contour and read **where hard meets soft** — mark every hard-bottom hit as a waypoint and keep the track line running (`11npFUPOJKU`). A good spot is a distinct pinnacle/hump rising 20–30 ft.
- **Current matters as much as bait** — a spot with no current will meter fish that won't bite (`6-8KfjEg0x8`). Tell for the shutoff: bait pointing every direction and fish metering but not biting; or bites on nearly every drop, then several dead drops in a row (`aFb221LUoD0`).
- **Rig:** dropper-loop gangion — **two loops ~1.5 ft apart, circle hooks, 24 oz torpedo sinker on a light breakaway**, 30 lb braid for a fast straight drop; bait it with a **5–8" gulp/plastic grub** (white-glow / nuclear chicken) and you carry no squid ([`species/rockfish-lingcod.md`](species/rockfish-lingcod.md)). General dropper-loop rule: sinker **6–10 oz**, heavier if the current is up, err **long** on the loop for bait action ([`techniques/dropper-loop.md`](techniques/dropper-loop.md)).
- **Or a 3 oz lead-head slug** on shallower rock: drop slack, **5–6 quick winds off the bottom**; ~**90% of bites come on the first drop** or the instant you kick back into gear.
- **Sheephead** come off the same ground and are in envelope (`nearshore-coast`): anchored on a chummed reef, chunk to draw them up then a **1/4–1/2 oz slider with a No. 2 / No. 4 bronze hook**, bait **suspended, never laid on the bottom** — a bottomed bait draws bat rays, shovelnose and leopard sharks instead (`OSbAHdB4uPs`, `eL1Qm33-Mj0`, [`species/sheephead.md`](species/sheephead.md)).
- **Regs:** rockfish is open most of the year and closes year-end, with depth limits and RCA boundaries that vary by location (the register's examples: ~240 ft near the islands vs ~75 fathoms nearer the coast, 2020-03, speaker self-hedged). **California/CDFW — verify current season, depth limits and RCA line before you drop.**

## 6. Halibut — the swing option, if you find the right dirt

In envelope and it likes exactly this kind of day: **off-color water just outside the surf line** where hard bottom sits outside the beach and bait gets pushed in. The rule is **sand within 5–20 ft of a hard edge** — a rock, shale reef, channel edge, low-relief rockpile, bubbler, eelgrass line — not open sand (`OpcKQPA3vAI`, [`species/california-halibut.md`](species/california-halibut.md)). Halibut also **push into less than 15 ft in spring and fall** (`ghHQe3fP9U4`, medium).

- **Live bait:** trap rig off a three-way with a breakaway sinker, 2.5–3 ft of **25–30 lb fluoro** leader, 30 lb mono class outside (mono for stretch on the bolting run).
- **Artificials, covering water:** drop-shot short controlled drifts, or a fast-wound hard bait — halibut **chase it down** (`46ha7J1Fc6A`). In **1–4 ft** run a shallow minnow so it doesn't dig into the sand; **by 10 ft switch to a leadhead and swimbait** (`E4CDqBFOaP8`).
- **Fight it:** light drag, steady tension, **no pumping**, head kept underwater to the gaff.
- **Regs:** minimum **22 in** (California/CDFW, as stated on camera 2016-11-23, `MUpvP-Yl2R0`) — verify current.

## 7. Bail-out — Dana Point Harbor

If it builds and you come in early: the harbor is the marginal-weather fallback ([`species/spotted-bay-bass.md`](species/spotted-bay-bass.md), `regions: socal-bight`, `waters: bay-harbor`). Fish eelgrass edges, mooring cans, piling fields, riprap and channel drops, and especially the **edges where two of those meet** ([`locations/bays-and-harbors.md`](locations/bays-and-harbors.md)).

- **Spotties are fully tide-driven** — the exact opposite of the calico outside. Your 10:20 low means ebb all morning, then flood.
- **Slack itself is the slow window** — roughly the half hour either side of 10:20; fish the moving water on either side of it (`EGKesj7V64M`, medium).
- **Read current off the eelgrass lean and cast up-current, retrieving with the grain** — against the grain drags the lure into standing blades, and the bass sits facing up-current anyway (`EGKesj7V64M`).
- On the **flood** they push shallow onto ground they can't reach at low water; on the ebb they pull off to the deeper edges (`lP6cg4eEU6s`, medium).
- **No minimum size** on spotted bay bass (2024-11 — verify; `usHl-4SfqDA`).

**Caveat:** the KB's bay notes name San Diego Bay, Mission Bay, Newport, Huntington Harbour and the LA/Long Beach complex. **Dana Point Harbor is not named anywhere in the KB** — I'm applying the universal bay-structure knowledge, not documented local spots.

## 8. What I'm deliberately not offering

- **Bluefin, yellowfin, dorado, striped marlin, paddy yellows** — `open-ocean`/`bank`/`island`, out of envelope. The gate is binding, not a ranking.
- **Ocean whitefish** — tagged `waters: bank, island` only ([`species/ocean-whitefish.md`](species/ocean-whitefish.md)), so it's gated out of a nearshore-coast day even though it'd be a natural bycatch thought.
- **Coastal yellowtail off Dana Point** — [`species/yellowtail.md`](species/yellowtail.md) does include `nearshore-coast`, but every documented SoCal program in it is islands, banks, Coronados or paddies. **The KB has no Dana Point–Oceanside mainland yellowtail program.** If a boil or a paddy shows inside the band, the iron is already in your hand — but I'm not routing the day to it.
- **Lobster** — season runs roughly **early October through mid-March**; late September is almost certainly before the opener (California/CDFW, as of 2026-08 — `b19_AJjYCok`, [`species/california-spiny-lobster.md`](species/california-spiny-lobster.md)). Verify the exact opener.
- **White seabass** — in envelope on paper, but it's moon-clustered, slack-driven and squid-dependent, and needs the full **off-color patch + current + bait** triad; **missing any one leg, leave within 20–30 min** ([`species/white-seabass.md`](species/white-seabass.md), [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md)). You didn't give me a moon phase, so I can't weight it. If you hit a dirty patch with a hard rip edge inside cleaner water, with current and bait, fish it on the 10:20 slack — that's the setup.

## 9. Gear (resolved against your profile — including a real gap)

From [`profiles/cameron/rods.md`](profiles/cameron/rods.md) and [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md), mapped through [`tackle/gear-classes.md`](tackle/gear-classes.md):

| Job | Your setup | Lure |
| --- | --- | --- |
| Surface iron on the kelp line (**primary**) | **Torium 20HG / Phenix Abyss 10'0" 25–60 lb, 50 lb braid** — the jig-stick class | **Nomad Slidekick 120g (4.25 oz)** is your wind jig — heavier than a traditional iron and can be sunk out to cover the column; **JRI-7** (~Tady 45 class) as the kelp all-rounder; **Strictly Irons Glory** (7", wide drawn-out kick) for a picky/slack-current change-up |
| Flylined bait on the up-current edge | **Avet MXJ / Teramar 90MHB2, 50 lb braid** — flyline class | — |
| Bottom / dropper loop on coastal rock, or vertical when the kelp lays flat | **Trinidad 40 / Rainshadow 8'0" XH 40–80, 80 lb braid** — yo-yo & sinker-rig class | **Salas 6X**, **Salas CP 105** |
| Small-bait / bonito & barracuda casting | **Lexa 400 / Okuma PCH 9'0" H** or the **Tranx** | **Daiwa Zakana 100g**, **Jansen Cabo Killer** |

**Named gap (protocol step 4 — I don't substitute):** the calico programs the KB ranks highest for kelp stringers — **weedless swimbaits, open slugs, leadheads, inshore crankbaits** — all call for the **bass / swimbait class** (7–9 ft graphite-composite, low-profile 200–300 reel, 30–65 lb braid, 40–65 lb fluoro leader for kelp abrasion) and there is **no bass-class rod and no soft plastics or leadheads in your inventory**. Your Tranx (8'2" H, 20–45 lb, braid TBD after respool) is the nearest thing, but it isn't the same rod — the swimbait rows specifically want a soft glass tip so you don't pull the hook. Today that costs you the "fish tight to individual stringers" and "sparse kelp lanes" rows entirely; you're an iron-and-bait boat on the kelp. Also no wire/haywire material is listed for the barracuda cut-offs.

**Boat:** [`profiles/cameron/boat.md`](profiles/cameron/boat.md) records **`range_nm: null` and `sea_state_max_ft: null`** — deliberately not guessed. The protocol says to **ask** rather than assume, so: is the Panga a 3–4 ft, 8–12 kt boat for a 20+ nm round trip today? The note does flag that **rough days forward are brutal** (the bow rider catches air), and you run with at least one person forward — that's a real cost on a 3–4 ft short-period day. It also notes no trim tabs and a single starting battery running the bait pump.

---

## What I could not answer from the knowledgebase

Listed in `gaps_admitted` — the load-bearing ones: **no chlorophyll numeric scale** (I can't tell you what 1.2 means), **no swell period given** (the steepness rule needs it), **no moon phase given** (calico full-moon shutdown and the WSB moon windows both hinge on it), **your boat's range/sea-state limits are null in the profile**, and **there's no Dana Point zone guide or spot detail** beyond the coordinates above.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `locations/regions.md`, `locations/bight-geography.md`, `locations/bass-structure.md`, `locations/bays-and-harbors.md`, `seasonal/september.md`, `conditions/sea-state.md`, `conditions/water-color.md`, `conditions/water-temperature.md`, `conditions/tide-and-slack.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/upwelling-and-turnover.md`, `conditions/kelp-paddies.md`, `species/README.md`, `species/calico-bass.md`, `species/barracuda.md`, `species/bonito.md`, `species/sand-bass.md`, `species/california-halibut.md`, `species/white-seabass.md`, `species/yellowtail.md`, `species/rockfish-lingcod.md`, `species/sheephead.md`, `species/ocean-whitefish.md`, `species/spotted-bay-bass.md`, `species/california-spiny-lobster.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/flyline.md`, `techniques/dropper-loop.md`, `techniques/wind-in-your-face-positioning.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `bait/bait-tanks.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`, `sources/regulatory-claims.md`  
*videos:* `5to3Q5P7w90`, `HzE4FHHcvTk`, `NC3-3pJDEgo`, `32TQdFJKIlI`, `LqW32NSkObY`, `RUuPNpK0x-s`, `9xNhdu2aBqE`, `Rwy4MqeXCIU`, `XyKF34C5iB4`, `kzD0kSnnVPw`, `sIoNELGlxmk`, `aFb221LUoD0`, `D5DR7Kx42_A`, `pcwcRdmWmLc`, `VpW91AKOFVQ`, `Ec2GaNpiOHI`, `oadK6zIYyCo`, `poqjnb1r1zk`, `11npFUPOJKU`, `6-8KfjEg0x8`, `OSbAHdB4uPs`, `eL1Qm33-Mj0`, `OpcKQPA3vAI`, `MUpvP-Yl2R0`, `ghHQe3fP9U4`, `E4CDqBFOaP8`, `46ha7J1Fc6A`, `EGKesj7V64M`, `lP6cg4eEU6s`, `usHl-4SfqDA`, `7WapaxdtjQg`, `ztpj1Xll0-U`, `bM2vUS1B-yQ`, `fgTmUq78ofQ`, `b19_AJjYCok`, `r6j5w40fVHI`, `HMdrP4-i9MM`, `H-vIGWPIPVc`, `0dIwWiOc1NY`, `4xzK7YaXK5s`, `r9bF3VtzDUg`  
*gaps admitted:* No chlorophyll numeric scale anywhere in the KB — it gives no mapping from a chlorophyll value (your 1.2 along the kelp) to 'clean', 'green', or 'seabass-color', so I cannot grade that number, only the visual read. | Swell period was not given, and the KB's steepness rule (10 ft @ 15 s barely felt vs 3-4 ft @ 4-5 s brutal) cannot be applied without it. | Moon phase for late September was not given; the calico full-moon-shutdown rule, the white seabass moon-window weighting, and spring/neap tide amplitude all depend on it. | Your boat profile has range_nm and sea_state_max_ft as null (profiles/cameron/boat.md) — the protocol says to ask rather than assume, so I could not verify a 3-4 ft, 8-12 kt round trip is inside your envelope. | The KB has no zone guide or spot pages for the Dana Point / Oceanside coast — only coordinates in sources/spot-lists.md, with no per-spot depth, structure, or bottom-composition detail. | Dana Point Harbor is not named anywhere in the KB; the bay/harbor knowledge I applied names San Diego Bay, Mission Bay, Newport, Huntington Harbour and LA/Long Beach only. | No mainland Dana Point-to-Oceanside yellowtail program exists in the KB — yellowtail coverage is islands, banks, Coronados, Baja and paddies. | No doctrine on managing drift speed in 8-12 kt of wind (drogue/drift sock, motor-assisted drift) for either the halibut drift or the bottom-fishing drift. | No guidance on fishing kelp paddies inside a nearshore 3-4 ft band — paddies are treated as open-ocean structure — and the conditions given do not say how far offshore the 'inshore' 3-4 ft band extends. | No SoCal-specific numeric wind/sea go-no-go for a small private boat on a nearshore day; the only threshold set in the KB (Dave Hansen's ~12 kt cutoff, sub-10-second interval flag) is single-mention, medium confidence. | Current direction relative to the shoreline was not given, and the parallel-current rule that decides which beds are alive can only be resolved on the water (kelp lean, chum-drift angle, anchor-line read). | Whether 67-69 F represents a drop from prior days is unknown, so I cannot apply the new-cold-bloom vs mature-bloom-edge test that decides whether this water fishes today. | Bait availability at the Dana Point barge on the day is not something the KB can tell you — it carries only etiquette, timing and load-judgment doctrine. | All regulatory figures cited (14 in bass, 22 in halibut, lobster season, rockfish depth/RCA limits) carry as-of dates from 2016-2026 and must be re-verified with CDFW before fishing; the KB explicitly flags them as changeable.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Blowing outside, launching Dana Point — late September

## 1. The envelope call (this is binding for the rest of the plan)

Per step 1b of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), I set the day's `{regions, waters}` before opening a single species note:

- **regions: `socal-bight`** only.
- **waters: `nearshore-coast`** — the Dana Point coastal ribbon and south toward Oceanside. `bay-harbor` is a bail-out, with a caveat below.
- **OUT: `island`, `bank`, `open-ocean`.** San Nicolas, Santa Barbara Island and the outer banks are the water your forecast blows out, and per [`conditions/sea-state.md`](conditions/sea-state.md) a **12–15 kt wind with 4–8 ft swell at a 9-second interval** is already the named unfishable combo — "you just cannot be caught out there," a dire situation even for bigger boats (`NC3-3pJDEgo`). You're describing 20–25 kt and 6–8 ft. That's not a "see how it looks" call, it's a no.

Anything gated to `island`/`bank`/`open-ocean` is therefore **not offered at all today**, not offered with a caveat: bluefin, yellowfin, dorado, marlin, swordfish, paddy yellowtail, and the island yellowtail/white-seabass programs.

**Catalina / San Clemente Island — I am not calling it either way.** [`conditions/sea-state.md`](conditions/sea-state.md) says explicitly to check **Catalina Eddy shielding** before writing off water east of Catalina and San Clemente on a bad outer forecast — the prevailing wind down the coast outside SoCal is from the north, so the islands shadow the water behind them (`S2L3KLSQ6Is`, cameron). But you gave me no numbers for the San Pedro Channel or Catalina, I'm not allowed to invent them, and [`locations/dana-point.md`](locations/dana-point.md) carries an explicit flagged gap: **no corpus source gives a run distance, run time, or the sea-state envelope for any run out of Dana Point Harbor.** Two more things from the same note argue for caution even if the eddy is in: the ridge off the **east end of Catalina** stands the swell up locally for a few miles (`zKmZ4zql2ws`), and **forecast error is asymmetric** — assume it errs on the worse side and that afternoon W at the islands strengthens rather than eases (`zKmZ4zql2ws`).

**One structural fact about your launch:** from Dana Point through Newport, the bottom **a mile to a mile-and-a-half off the beach is already 2,000–3,000 ft** (`Rf1HKJG-SDg`, [`locations/dana-point.md`](locations/dana-point.md)). There is no shallow bank to duck behind out there. The fishable structure today is the coastal ribbon against the beach — which is exactly the water your 8–12 kt / 3–4 ft band covers.

## 2. What's fishable, ranked

### PRIMARY — coastal kelp and boiler bass: calico + sand bass, with barracuda and bonito in the mix

This is the day. Your SST of **67–69 °F** sits right on the calico preference band: **roughly 65–68 °F, with fish going lethargic and dropping to cooler water past about 70 °F** (`LqW32NSkObY`, [`species/calico-bass.md`](species/calico-bass.md)). You're at the warm top of the band, not over it.

The spots, north to south, from [`locations/dana-point.md`](locations/dana-point.md) (charted positions, cameron):

| Spot | Position | What it is |
|---|---|---|
| Monarch Boilers | 33°28.970'N 117°44.020'W | boiler rock |
| Salt Creek | 33°28.565'N 117°44.040'W | beach break point, effectively same longitude as Monarch, ~0.41 nm apart |
| **Dana Point Kelp — Red Buoy** | **33°27.320'N 117°43.380'W** | the one bed the corpus has actually worked on camera |
| Barber Poles | 33°26.710'N 117°41.410'W | boiler rock (1.75 nm from the DP bed, and mostly east — not "just south") |
| San Clemente Kelp (mainland city) | 33°24.450'N 117°38.140'W | kelp |
| San Clemente Artificial Reef (mainland city) | 33°23.890'N 117°37.200'W | built structure |
| San Mateo Point / Trestles | 33°22.960'N 117°36.800'W / 33°22.790'N 117°36.280'W | beach break points |
| San Onofre Kelp (next zone south) | 33°20.880'N 117°34.050'W | kelp, top of [Oceanside/North County](locations/oceanside-north-county.md) |

**Read this before you read any report:** San Clemente Kelp and San Clemente Artificial Reef are off the **mainland city**, not San Clemente Island. Do not read island reports onto them ([`locations/dana-point.md`](locations/dana-point.md), cameron).

**Working depths.** The only depths the corpus works in this zone are **0–8 ft and 20–100 ft, occasionally a little past 100 ft** (`LqW32NSkObY`). Bass structure generally runs **20–120 ft** (`kwMIgkCtFUE`, [`locations/bass-structure.md`](locations/bass-structure.md)). Off the Camp Pendleton end, calico and sand bass came off hard bottom with sub-surface kelp in **~40–42 ft** in October (`HMdrP4-i9MM`, [`locations/oceanside-north-county.md`](locations/oceanside-north-county.md)).

**How to pick which end of the ribbon — read current, not the tide clock.** Calico are **current-driven and tide-indifferent** ([`conditions/tide-and-slack.md`](conditions/tide-and-slack.md), `6TBxHnkYXI0`). The parallel-current rule from [`conditions/current-structure.md`](conditions/current-structure.md) (`0KQ--N5TjqE`, mechanism `6TBxHnkYXI0`):

- Current running **parallel** to the beach (uphill or downhill) → **good**, it creates a definable leading edge.
- Current **straight into the beach** → marginal (the exception is off-color water, where fish use the dirt to ambush).
- Current **straight off the beach** → **dead, skip it.**

Mechanism: calico face into the current and ambush from the front of the structure, so parallel flow is what delivers food past the edge they're sitting on (`Rwy4MqeXCIU`).

Then pick your corner of the bed: **current downhill → work the northwest corner of the kelp; current uphill → work the southeast corner** — the bigger fish in the bed sit in that corner (`kzD0kSnnVPw`, flagged single-source). Fish **edges and pinch-points**, never the dense middle. Grade a bed fast: hit three or four sides of a kelp head and you know in two or three casts (`0KQ--N5TjqE`).

**Light.** Bright stable light has calico "levitating" up into the canopy out of direct sun, concentrating along the **outer canopy edge**; overcast spreads them through the column so a wider area produces (`RUuPNpK0x-s`). Fish the hour before sunrise into early morning and the hour before sunset.

**The bait read here is unsettled, so carry both.** On the one worked Dana Point kelp session, a morning produced **5 sand bass and 3 calico, every one on a strip of squid**, then by the end of the day the same crew reported bass "actually biting the smaller sardines today" and called it a surprise (`M6U_FVdosr4`). The note's own verdict: not a doctrine conflict to resolve, just have **squid strip and small sardines both aboard**. **Short barracuda** showed mid-session in that same bed (`M6U_FVdosr4`).

**On the kelp: anchor rather than drift** was the call on the one worked session there, on a light current running through the bed (`M6U_FVdosr4`) — note the KB flags that "anchor over drift" is not actually a rule any linked note states, and [`species/calico-bass.md`](species/calico-bass.md) carries a drift row of its own. Use your sounder read: fish still marking but not responding at anchor is the cue to **drift over them instead of staying pinned** (`97clKtVsEOs`, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)).

**Techniques, ranked, from the router table in [`species/calico-bass.md`](species/calico-bass.md):**

1. **Weedless swimbait** to individual stringers — 7" weedless slug on a **3/8–3/4 oz keel-weighted spring hook**, short targeted casts, fast steady wind, pause on the eat; soft glass tip so you don't pull it, heavy fluoro leader for kelp abrasion (`YIABTTYXeqc`).
2. **Surface iron** ground down the kelp line when you want to cover a whole edge instead of one stringer, or when bigger fish are cruising with the current up ([`techniques/surface-iron.md`](techniques/surface-iron.md), [`species/calico-bass-surface-iron.md`](species/calico-bass-surface-iron.md)). Standing iron sizes across yellowtail/bass/barracuda are **Tady 45, Tady 14A, Salas 7X** (`pcwcRdmWmLc`); downsize on small bait. Retrieve **tip-down** — tip-up pulls it onto the surface where it stops swimming right ([`techniques/surface-iron.md`](techniques/surface-iron.md)).
3. **Flyline a live bait** on the up-current edge when it's deeper or windy ([`techniques/flyline.md`](techniques/flyline.md)) — note the KB flags an internal conflict on which bait pairs with calico (the router says sardine/mackerel, the flyline note pairs **anchovy** with calico).
4. **Chum-and-anchor** on a kelp edge with parallel current: chum the spot, reposition up-current, back the boat down onto it as the anchor sets — fish come out of the kelp and start biting as the anchor goes down (`RXNebDr4j7s`).

**Sand bass on the same water.** They hover slightly **above or within** the structure, not pinned to the rocks, so cover the column (`P2OzCf2CwXI`, [`species/sand-bass.md`](species/sand-bass.md)). A big one is about **6 lb**, which sets the whole tackle scale — **20 lb leader gets it done**. Critical sounder point: **they don't mark while sitting on the bottom** — mark the structure and the bait, and drop regardless of whether fish show (`kwMIgkCtFUE`). When they do come up they come a long way: over a rock in **60 ft**, bass rose **40 ft** to intercept a sinking lure where the screen had shown nothing a moment before. If they're locked down, **dropper loop** to the bottom.

**Barracuda and bonito are the mixed bag, not a target.** Barracuda hold on the same kelp lines and beach edges; dated SoCal appearances run **late May through October** (`S2L3KLSQ6Is`, `DnSqw4r7A1s`, `0KQ--N5TjqE`, `Klfb433I3Uk` — [`species/barracuda.md`](species/barracuda.md)). **Chrome is the barracuda colour** (`PrdPJy26H8c`), which is also why chrome backfires when yellowtail are the target. Carry a short **single-strand wire** or heavier hard mono bite tippet — barracuda teeth cut mono even in heavy sizes (`lm7D9Tlc7Po`, [`rigging/haywire-twist.md`](rigging/haywire-twist.md)).

Bonito were on the Dana Point harbour mouth in early July, taken on the troll **both sides of it** — a skiff worked south of the harbor first, then moved north and pulled **small feathers rigged as a short daisy chain at roughly 5.5 kt**, casting a small sardine-profile diving hard bait behind the boat on the troll bite and twitching it under way (`poqjnb1r1zk`, [`species/bonito.md`](species/bonito.md), [`techniques/trolling.md`](techniques/trolling.md)). That's a good low-cost way to run between the kelp beds this morning.

### SECONDARY — halibut on the structure edges

[`species/california-halibut.md`](species/california-halibut.md): halibut **move around looking for feed** rather than holding a spot and waiting (`OpcKQPA3vAI`). **Fall beaches do not follow the grunion cycle** — in fall the inshore bait is smaller, fish sit farther off the beach, more often in a **9–11 ft** zone, keyed to structure: protected beaches with eelgrass, point breaks, and "finger rock" areas where rock has eroded into strips with sand between them (`EuYOlsnxXko`). That's a description of Salt Creek / San Mateo Point / Trestles water.

Program: **live-bait drift with a trap rig off a three-way and a breakaway sinker**, mono for stretch on the bolting run ([`species/california-halibut-live-bait-drift.md`](species/california-halibut-live-bait-drift.md), [`rigging/trap-rig.md`](rigging/trap-rig.md), `a5u8BaYzw8c`). **15 lb class inshore**, one hook size smaller than the island build. Artificial alternative: **drop-shot a plastic near the bottom** on short drifts to pick apart rockpiles rather than running long straight drifts; deeper, a **leadhead swimbait — sink to bottom, three turns, pause, watch the line fall to confirm bottom, repeat**, with a **3-in swimbait covering about 90%** of deeper fishing (`OURS05qEGcA`, `fHMwcm1xRQk`).

**Discipline before you commit:** the halibut/WSB water triad needs **all three** of off-color water, current, and bait. Missing any one → **leave within 20–30 min** (`OpcKQPA3vAI`, [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md)). The best version is a dirty patch with a hard rip/foam edge inside otherwise cleaner water.

### THIRD — the artificial reef, if the kelp is dead

San Clemente Artificial Reef (33°23.890'N 117°37.200'W) is right in the strip; the Pendleton/Oceanside/Carlsbad series are south ([`locations/north-county-artificial-reefs.md`](locations/north-county-artificial-reefs.md)). One program runs the whole zone: **anchor up, build a chum line, fish light**.

- **Build prey density, don't just feed** — periodically add another handful of cut chunks; past a certain density even non-feeding fish come over because they see the others doing it, which is what turns a slow pick into a frenzy (`f4qYtHACGyk`, [`techniques/chunking.md`](techniques/chunking.md)). A private boat that can't carry sportboat-scale bait gets help from a **chum tube** (`JK2-cpaXkI8`).
- **Don't chum off the stern** — at anchor the current runs down the *sides*, so throw as far up the side as you can (`yKaHcxX46l4`). (The KB keeps two unreconciled current models for why the stern doesn't work; the rule holds either way.)
- **Fish far lighter than instinct says.** The stated #1 mistake at artificial reefs is fishing way too heavy: a **No. 4–No. 6 hook** tied straight to mono, a **1/16 oz split shot 2–3 in above it**, **never heavier than 1/4 oz**, and a spaghetti-thin strip of bait rather than a wad (`f4qYtHACGyk`, `bM2vUS1B-yQ`). The Pendleton worked example is in **35–40 ft** with a bucket of ground sardine/mackerel/anchovy.
- This is also the **sheephead** program — chummed artificial reef, suspended strip bait on a slider, **pismo clam** the premium bait and squid strips the everyday fallback (`OSbAHdB4uPs`, [`species/sheephead.md`](species/sheephead.md), [`species/sheephead-sliding-sinker.md`](species/sheephead-sliding-sinker.md)). Year-round resident, no month prior applies.

Deep-reef alternative if the fish are spooky over the top: **stand off the structure and bomb a slug on a 1 oz head** back across the edge — set up off to the side, not on top (`-eaaWPN5Fxk`).

### NOT today

- **White seabass.** [`species/white-seabass.md`](species/white-seabass.md) is squid-driven: the corpus's season shape is early spring through summer, and its own dated moon records run **July–August 2022**. Late September is off the back of it. Not a program to build a day on.
- **Yellowtail.** [`species/yellowtail.md`](species/yellowtail.md) puts coastal kelp-line fish in warm-stable June–September, but every zone guide and every catchable window it names is island, bank or paddy — all outside today's envelope. Mainland-coast schools from **Del Mar to Imperial Beach** are recorded as **markedly finicky on the iron** (`VpW91AKOFVQ`), and that's south of your band anyway. Keep an iron rigged, don't plan around it.
- **Paddies.** The Bight's best paddy water runs **Dana Point to Oceanside and southward** (`HzE4FHHcvTk`) — but that's open water offshore of this strip, `waters: open-ocean`, and it's the water your wind is on. (The KB flags this "Dana Point is the northern paddy limit" framing as over-stated against its source.)
- **Rockfish.** The four charted "rockfish area" spots in the corpus are down at Box Canyon / Leucadia / Encinitas / Del Mar in the next zone south, with a flagged gap for depths and season (`locations/oceanside-north-county.md`). If you go, the **RCA depth line** is the thing that bites you: about **240 ft around the offshore islands versus a 75-fathom (450 ft) line closer to the mainland**, so you can be legal at one position and over the line at a similar depth a short distance away — **check position against the drawn boundary, not against the depth reading** (`iAr6sbRC384`, [`species/rockfish-lingcod.md`](species/rockfish-lingcod.md)).

### Bail-out

If it comes up more than forecast, the coastal ribbon lets you work in tight all day. Note the honest limit: [`species/spotted-bay-bass.md`](species/spotted-bay-bass.md) names San Diego Bay, Mission Bay, Newport Bay and the LA/Long Beach harbors — **the corpus has nothing on a Dana Point Harbor spotty fishery**. The general read still applies if you poke around inside: on a running tide they hold ambush stations and you cast at the station (mooring can, grass edge, channel lip) from up-current; through the roughly half hour of slack they roam and a crankbait covering water beats the station cast (`YgqXf9iICyg`).

## 3. The clock

- **Bait first, and the clock is the whole problem.** The Dana Point sportboat fleet leaves at **6:00 a.m.**, which is when the private-boat line at the barge forms — by a quarter to six it's already building. Leaving the dock at **5:00 a.m. or 4:30** beats it entirely (`ztpj1Xll0-U`, `bM2vUS1B-yQ`). The KB records a genuine conflict on the late option: the same presenter elsewhere says **arrive at 7:00 and you'll never see a line** (`7WapaxdtjQg`), while in the Dana Point telling 7:00 means "it's all gone" (`ztpj1Xll0-U`). The 7:00 slot buys a short line at the cost of the morning window.
- **At the barge:** hail on **VHF 11** with the barge's name twice plus your own if no attendant is visible; the barge marks the side it wants you on — **at Dana Point, a cone on the ocean side**; **never board the barge** to fend your boat off; tell the attendant you want it **loaded light** and you're not in a rush (`7WapaxdtjQg`, [`bait/making-bait.md`](bait/making-bait.md)).
- **Low 10:20.** Arrival discipline is **be at your highest-percentage spot an hour before the change**, i.e. fishing by ~09:20, not searching for water at 10:20 (`6TBxHnkYXI0`). This matters most for the halibut drift and any harbor work — calico don't care about the clock, they care about current.
- **First light and the last hour** are the calico windows (`RUuPNpK0x-s`).
- **Plan the day to shorten, not lengthen.** If it's windier than forecast in the morning, assume it **builds all day** — a small boat bails early (`DnSqw4r7A1s`). One kayak-scoped read from this exact coast: on a windy day the guide's choice pushes **south**, so the trip home isn't fighting resistance (`LqW32NSkObY`, hedged in the source).

## 4. Gear

**Class terms first** (per the protocol's graceful-degradation rule):

- **Bass class** — 7–9 ft graphite-composite, 200–300 size reel, 30–65 lb braid, **40–65 lb fluoro leader** for kelp abrasion. This is the primary outfit for weedless slugs and swimbaits.
- **Jig-stick class** for surface iron down the kelp line.
- **Deep-structure bass class** for the artificial reef standoff — **8 ft graphite heavy, 300-size reel, 50 lb braid / 40 lb fluoro. Do not step up to extra-heavy — the stiffer tip pulls hooks, especially on sand bass** (`-eaaWPN5Fxk`).
- **Light bait class** (light spinning or small level-wind) for the chummed-reef program — No. 4–6 hooks, 1/16 oz shot.
- **15 lb inshore bait class** for the halibut trap rig.
- Full lexicon: [`tackle/gear-classes.md`](tackle/gear-classes.md).

**Resolved against [`profiles/cameron/`](profiles/cameron/README.md)** — and this is where I have to name gaps rather than substitute:

- **Surface iron: covered.** Setup 5 — Torium 20HG on the Phenix Abyss 10'0" 25–60 lb, 50 lb braid — is the full surface-iron setup ([`profiles/cameron/rods.md`](profiles/cameron/rods.md)). Owned irons that fit: **JRI-7** (light blue, ~Tady 45 class, logged as the "local / kelp all-rounder"), **Strictly Irons Mighty** 5.5", **Squidco Candy Bar SR Lite** 3 oz / 6.5" ([`profiles/cameron/tackle.md`](profiles/cameron/tackle.md)).
- **GAP — no chrome surface iron or small chrome casting jig.** Chrome is the barracuda colour (`PrdPJy26H8c`) and what bonito reach first; the bonito boil answer in the corpus is DD100-class small divers and **small chrome jigs fished on bass gear** (`Z3rZqy2Pi8E`). The only chrome in the inventory is the **Salas CP 105**, which is a heavy yo-yo iron, not a surface or small casting jig.
- **GAP — no bass-casting / swimbait outfit and no soft plastics on file.** All eight rods are 30–130 lb class offshore builds. The closest to the 7–8 ft bass class the calico and sand bass programs call for is the **Tranx 400 on the Phenix M1 SMX-82H (8'2", H, 20–45 lb, 3–8 oz)** — and its braid is listed **TBD pending respool**. [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md) is hard baits, casting and jigging only: there are **no leadheads, weedless spring hooks or soft-plastic slugs recorded**, so the primary program of the day — a 7" weedless slug on a 3/8–3/4 oz keel-weighted spring hook — has no bait in the box. That's a tackle-shop stop, not something I'll substitute around.
- **GAP — nothing light enough for the artificial-reef program.** No. 4–6 hooks on 1/16 oz shot and a light spinning outfit have no match in the inventory.
- **GAP — nothing at the 15 lb inshore halibut scale.** The lightest recorded is 50 lb braid on the Avet MXJ / Teramar 9'0" MH.
- **Bottom work: the Trinidad 40** (M&M on a 8'0" XH 40–80 lb blank, 80 lb braid) does the yo-yo/sinker-rig job, but note it is far heavier than the scale a ~6 lb sand bass wants — the species note says **20 lb leader gets it done** (`P2OzCf2CwXI`).
- **Boat notes that matter today:** 30-gal bait tank on a Rule 401 (500 GPH), 100–125 lb of ice, **no trim tabs**, and slight hull flex on hard wave impacts ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)). **Normal departure is ~8 a.m.** — that misses both the barge window and first light. For this plan you're looking at a 4:30–5:00 departure. Also: home launch on file is **Dana Landing, Mission Bay**, so Dana Point is a trailer move, and the KB has no launch-ramp or hoist detail for Dana Point Harbor.
- **I cannot check your sea-state envelope.** `range_nm` and `sea_state_max_ft` in [`profiles/cameron/boat.md`](profiles/cameron/boat.md) are **null** — deliberately left blank rather than guessed — and the protocol says to **ask** rather than assume. The coastal ribbon is a short run against the beach, so it's very likely inside whatever your envelope is; the Catalina question is not, and I'd want those two numbers before we ever revisit it.

## 5. Sounder note for a 3–4 ft day

Sea state sets how shallow your sounder can actually read, independent of the range setting. In chop a **fixed transducer follows the boat's roll**, so the cone tips off vertical and a fish holding high in the column doesn't paint until you're nearly on top of it — the same fish would show at range on a calm day; a rolling boat also returns aerated-water noise that swamps the signal (`fgTmUq78ofQ`, `ZIJAvAEW_tU`, [`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)). **Don't write off a kelp edge today based on what marks at range.** Grade marks the way the bass notes say: hard bottom reads harder than the chart suggests, feeding game fish show **vertical movement** through the column while perch marks read as **straight lines**, and most of what paints over reef structure is perch (`kwMIgkCtFUE`).

## 6. Regulations — verify before you go

- **Calico (kelp) bass minimum: 14 in** (California / CDFW, as of 2026-08; corroborated four ways in the corpus). **Bag limit stated as 5** — single-source, no jurisdiction named on camera, oldest regulatory figure in the note (as of 2019-03) ([`species/calico-bass.md`](species/calico-bass.md)).
- **Barred sand bass minimum: 14 in** (as of 2022; the KB flags that only one source states it for sand bass specifically). **The California bag limit for barred sand bass is a flagged gap — the corpus doesn't state it** ([`species/sand-bass.md`](species/sand-bass.md)).
- **One MPA edge is charted in this zone:** at The Hospital 100 Fathom Curve, stay **south of 33°30.050'N**. The KB flags this as resting on a single spot-library annotation with **no MPA named and no boundary extent** — a latitude alone doesn't establish where a boundary runs. Verify current MPA boundaries and closures with CDFW ([`locations/dana-point.md`](locations/dana-point.md)).
- All of the above are stamped "as of" dates in the KB and move year to year. Check current CDFW regs before you leave the dock.

## 7. What I could not answer from the knowledgebase

These are real gaps, not hedging — I'd rather flag them than fill them from outside the KB:

- **You didn't give me swell period, and it decides your day.** [`conditions/sea-state.md`](conditions/sea-state.md) is emphatic that period matters more than height: **10 ft @ 15 s from the south is barely felt; 3–4 ft @ 4–5 s is brutal** (`zKmZ4zql2ws`). Your inshore 3–4 ft could be a pleasant day or a beating. Flag any segment where the period in seconds approaches the height in feet, and note that **sub-10-second intervals are called a hard bad-sea flag** on their own (`NC3-3pJDEgo`). Also worth knowing: **8–12 kt straddles the personal 12 kt "don't run" cutoff** one working captain in the corpus states (`NC3-3pJDEgo`).
- **No current direction given.** The whole spot-selection logic above (parallel vs into vs off the beach, and NW vs SE corner of the bed) has to be read on arrival. The KB records that anglers keep a per-spot log of which wind direction each spot fishes on (`xI9tPJFXbUM`) but flags the mechanism as unknown, and it gives no wind-direction → current-direction mapping I can apply to your NW 8–12.

Everything else I couldn't cover is listed below.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/electronics-and-sounder.md`, `locations/regions.md`, `locations/dana-point.md`, `locations/dana-point-kelp-red-buoy.md`, `locations/oceanside-north-county.md`, `locations/north-county-artificial-reefs.md`, `locations/bass-structure.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/water-color.md`, `conditions/current-structure.md`, `seasonal/september.md`, `species/calico-bass.md`, `species/sand-bass.md`, `species/barracuda.md`, `species/bonito.md`, `species/california-halibut.md`, `species/sheephead.md`, `species/white-seabass.md`, `species/yellowtail.md`, `species/rockfish-lingcod.md`, `species/spotted-bay-bass.md`, `species/calico-bass-surface-iron.md`, `species/california-halibut-live-bait-drift.md`, `species/sheephead-sliding-sinker.md`, `techniques/surface-iron.md`, `techniques/swimbaits.md`, `techniques/flyline.md`, `techniques/chunking.md`, `techniques/dropper-loop.md`, `techniques/trolling.md`, `techniques/drop-shot.md`, `techniques/leadhead-swimbait-retrieve.md`, `techniques/wind-in-your-face-positioning.md`, `rigging/trap-rig.md`, `rigging/haywire-twist.md`, `bait/making-bait.md`, `tackle/gear-classes.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`  
*videos:* `NC3-3pJDEgo`, `zKmZ4zql2ws`, `S2L3KLSQ6Is`, `DnSqw4r7A1s`, `HzE4FHHcvTk`, `Rf1HKJG-SDg`, `LqW32NSkObY`, `M6U_FVdosr4`, `poqjnb1r1zk`, `ztpj1Xll0-U`, `bM2vUS1B-yQ`, `7WapaxdtjQg`, `HMdrP4-i9MM`, `0KQ--N5TjqE`, `Rwy4MqeXCIU`, `kzD0kSnnVPw`, `6TBxHnkYXI0`, `OpcKQPA3vAI`, `RUuPNpK0x-s`, `YIABTTYXeqc`, `RXNebDr4j7s`, `kwMIgkCtFUE`, `P2OzCf2CwXI`, `-eaaWPN5Fxk`, `f4qYtHACGyk`, `yKaHcxX46l4`, `JK2-cpaXkI8`, `OSbAHdB4uPs`, `PrdPJy26H8c`, `YAKOv9bXKO0`, `pcwcRdmWmLc`, `Z3rZqy2Pi8E`, `lm7D9Tlc7Po`, `a5u8BaYzw8c`, `EuYOlsnxXko`, `OURS05qEGcA`, `fHMwcm1xRQk`, `ghHQe3fP9U4`, `iAr6sbRC384`, `r6j5w40fVHI`, `VpW91AKOFVQ`, `YgqXf9iICyg`, `fgTmUq78ofQ`, `ZIJAvAEW_tU`, `97clKtVsEOs`, `5to3Q5P7w90`, `Klfb433I3Uk`, `Kf5wk_TFgTc`, `xI9tPJFXbUM`  
*gaps admitted:* Swell period was not given, and conditions/sea-state.md makes period the deciding variable (10 ft @ 15 s barely felt vs 3-4 ft @ 4-5 s brutal) - I cannot grade your inshore 3-4 ft without it. | Current direction was not given, so the parallel-current rule and the NW/SE kelp-corner rule have to be applied on arrival; the KB gives no wind-direction to current-direction mapping I can apply to NW 8-12 kt. | The KB gives no numeric chlorophyll scale, so a value of 1.2 cannot be graded against any threshold in these notes - only the qualitative new-cold-bloom vs mature-bloom-edge distinction applies. | Moon phase for late September was not given, so the full-moon inversion for calico and sand bass (bite early, dead mid-day, launch at noon if you cannot make first light) cannot be applied. | Tide range/height was not given, only the 10:20 low, so the per-bay tide-swing thresholds for spotted bay bass (SD Bay 3.5-6.5 ft best, 1-2 ft do something else; Mission Bay 4-5 ft) cannot be applied. | locations/dana-point.md carries an explicit flagged gap: no corpus source states run distance, run time, or the sea-state envelope for any run out of Dana Point Harbor - including to Catalina. | No corpus source covers the launch ramps or hoists in Dana Point Harbor. | No conditions were given for Catalina, San Clemente Island or the San Pedro Channel, so I could not evaluate the Catalina Eddy shielding option that conditions/sea-state.md says to check before writing off the inside. | profiles/cameron/boat.md has range_nm and sea_state_max_ft set to null (deliberately unstated), so per the protocol I must ask for the boat's range and sea-state limits rather than assume them. | locations/dana-point.md flags that the zone has no start-and-move program in the corpus: which end to start on, how the two kelp beds fish against the boilers and the artificial reef on a given day, how tide/light/swell shape a day there, and how long to give a spot before moving. | No corpus source gives charted depths, relief or bottom composition for any named Dana Point spot; what Barber Poles actually is; or the extent, health or seasonality of the two kelp beds. | No corpus source says whether yellowtail, white seabass, halibut, rockfish, lingcod or sheephead are targeted anywhere in the Dana Point zone, and no month-by-month season is scoped there for any species. | No zone guides exist yet for barracuda, bonito or calico bass at Dana Point - all three are flagged stubs. | seasonal/september.md is offshore-weighted (volume square bluefin, dorado below Catalina, yellowfin sliding north, BOLA bottom yellowtail); it carries no September prior for the SoCal coastal kelp strip. | species/spotted-bay-bass.md names San Diego Bay, Mission Bay, Newport Bay and the LA/Long Beach harbors - the corpus has nothing on a Dana Point Harbor spotty fishery. | The California bag limit for barred sand bass is a flagged gap in the KB, and the calico bag limit of 5 rests on one 2019 source that names no jurisdiction. | The MPA note at The Hospital 100 Fathom Curve (stay south of 33 30.050N) rests on a single spot-library annotation with no MPA named and no eastern/western limit, so it cannot be checked from inside the corpus. | No corpus source gives depths, species mix or season for the four charted rockfish areas in the Oceanside/North County zone (Box Canyon, Leucadia, Encinitas/Devil's Rock North, Del Mar). | profiles/cameron/tackle.md records no soft plastics, leadheads or weedless spring hooks, and profiles/cameron/rods.md records no 7-8 ft bass-casting outfit, no light spinning outfit and nothing at the 15 lb inshore scale - so the primary swimbait program, the light artificial-reef program and the inshore halibut trap rig have no owned match, and I did not substitute.

</details>

### 3. [trip] I want to do two days at the Coronado Islands in October on a private boat. What is the program, and what pape…

**Winner:** NOW · mapping {'A': 'B3', 'B': 'B2', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three read the conditions the same way — no break in a 0.9 F spread, chlorophyll ungradeable because the KB has no numeric scale, neap tide from the last quarter meaning weak current and tide-anchored windows — and all three refused to invent Mexican vessel paperwork, so the separation is in what each could actually put behind the question. C wins because it answers both halves: a jurisdiction page (INM entry, CONAPESCA fishing, as of 2026-08, verify-current) with FMM, licence, passport and insurance, immediately followed by the named gap that no source covers what a private boat that never lands must carry, alongside charted positions, real run distances (Zuniga to Pukey Point 14.0 nm, not the 13 the other two repeat) and per-spot pages it honestly labels as position-only. C is also the only one that separates source text from KB inference — flagging the 5-10 fathom yellowtail depth as absent from D5DR7Kx42_A and surfacing the unresolved 6X-by-current versus 6X-by-depth conflict — where A and B state the same figures as settled. A is a close second: same paperwork substance, correctly labelled as drive-down scoped from a Bahia de los Angeles note, plus a strong meter-read routing table. B has the best execution detail on the water (cast mechanics, retrieve, hookset, bait hook placement, sounder ranges) but returns nothing at all on permits, which is half of what was asked.

- *B2 reasons:* found: strongest execution material of the three, and stated plainly that its KB has zero Mexican paperwork — but that means half the question returns only an absence, with four thin fragments in place of an answer. specific: the deepest mechanics — 2 o'clock to 9 o'clock cast load, jig hung ~18 in below the tip, tip-down grind, wind-through hookset, flyline 80-100 yd 30 lb top shot to 4-6 ft of 25/30 lb fluoro, 1/0-2/0 by bait, sabiki to 100 ft on 8 oz, manual sounder range 0-120/0-150 ft. sourced: dense note+id citation (VpW91AKOFVQ, 3dVc-2rsYII, NC3-3pJDEgo, gKrYKvqHUjk) that matches the claims. scoped: Mexican-water jurisdiction stated, no bare limits anywhere, and the lone BCS circle-hook datum carried with its 2019-02-13 date, its wrong-state caveat and its unverified flag. honest: section 9 is a clean refusal to guess, plus a twelve-item gap list including the spring-prior problem and the missing yellowtail break-side rule. actionable: excellent on the water, but an angler still has no idea what to carry across the border.
- *B3 reasons:* found: pulled the right program material (yellowtail router, Coronados chum-and-cast, spot library) and located the one adjacent paperwork note instead of shrugging. specific: seven spot coordinates plus 9-Mile/Canyon/North-of-North-Island, 5-10 fathom marks, 2-3 oz vs 5-6 oz iron, 12-18 in dropper loop at 3-4 ft above a 6-10 oz sinker, 40-50 lb flyline, 2 cups salt per 7-10 lb ice. sourced: note paths plus video ids throughout (D5DR7Kx42_A, 4pT0efBD1j0, ejUTAnONf7o, VpW91AKOFVQ) that fit the claims. scoped: explicit baja-pacific-north + socal-bight transit envelope, FMM/licence/passport stamped INM+CONAPESCA as of 2026-08 with verify-current, says plainly CDFW rules do not govern Mexican water, and admits island-structure.md is socal-bight-gated so applied by analogy. honest: says the four paperwork items are drive-down scoped and refuses to invent vessel permits, clearing in/out or CBP; wide gap list; no relative time. actionable: three-outfit stack, meter-read routing table, anchoring geometry, bait plan and an afternoon-wind clock all runnable.
- *NOW reasons:* found: the only answer that hits both halves — a dedicated jurisdiction page for the papers and a Coronados zone guide plus per-spot pages for the program; verified against locations/mexican-waters.md and locations/coronado-islands.md. specific: charted positions for all eleven spots, Zuniga-to-Pukey 14.0 nm and 15 nm to Middle Grounds with neighbour spacing (2.0/2.8/3.5/4.4 nm), Halco 190 pink and purple on 20-30 and 40 ft divers, sabiki 100 ft on 8 oz, 5 twelve-inch macks a drop, 65 lb braid to 40-50 lb top shot, hook sizes 1/2/4 to 2/0-4/0. sourced: best fidelity of the three — separates what a source says from what the KB inferred (flags the 5-10 fathom figure as absent from D5DR7Kx42_A, flags the terns-here-specifically line as contradicted, flags the 6X-by-current vs 6X-by-depth conflict). scoped: full region/waters envelope, correctly rules out the socal-bight-gated yellowtail dropper-loop sub-page, papers stamped INM/CONAPESCA as of 2026-08 with verify-current, CA licence noted for the US leg; only slip is quoting CDFW's 10-fish/240-ft rockfish numbers without an as-of, though jurisdiction and verify-with-CONAPESCA are both attached. honest: names the spring-scoped zone guide as the wrong season, calls the per-spot pages minimum pages, declines to apply the 10-15 nm bluefin displacement to structure fish, and lists seventeen gaps. actionable: a real circuit — troll in, convert on sign, yo-yo the tight balls, sabiki top-up, turn north early afternoon — plus the three profile questions the protocol requires.

<details><summary>Full prompt</summary>

I want to do two days at the Coronado Islands in October on a private boat. What is the program, and what papers and permits do I need? Assume these conditions and do NOT fetch live data: mid-October, two days. SST: Coronado Islands 66.8 F, 9 Mile Bank 66.2 F, Point Loma 65.9 F. Chlorophyll 0.9 at the islands. Wind NW 8 kt mornings, NW 12 kt afternoons. Swell NW 3 ft at 10 s. Moon: last quarter.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

# Two days at the Coronado Islands, mid-October — the program

I planned this off the KB only, following `planning/day-plan-protocol.md` (conditions → priors + layers → species router → gear). I used the conditions you gave exactly and pulled nothing live. **Two things up front: the KB has no Mexican permit/paperwork content at all (section 9), and it has no per-spot structure notes for the Coronados — only the coordinate library plus universal island typology.** I'm planning this as **two day-runs**, not an overnight, because the KB carries no guidance on staying out overnight in Mexican waters.

---

## 1. What your numbers actually say

**October is the regime-change month, and the chart runs the plan.** `seasonal/october.md` is blunt about it: *"conditions become pretty important… look 100 % at your temp chart and chlorophyll"* (`XLVUhV8DW64` 10/12/22, `OYOda6T3f-8` 10/20/22). It's the **fall fragmentation** regime — an "everything season, but scattered: breadth of species, low density of any one" (`seasonal/october.md`, `conditions/water-regimes.md`). Build the plan on break structure, not spot names.

**Your SST field does not contain a break.** 66.8 at the islands / 66.2 at the 9 Mile / 65.9 at Point Loma is **0.9 °F spread over ~13+ miles** — a gentle gradient. `conditions/water-temperature.md` says the thing you're hunting is a **sharp** edge, where "offshore edges can jump multiple degrees in ~1 mi," and that the value "is usually not the absolute number but which side of a break a species sits on." Three point readings can't locate that. **Practical consequence: pull the full SST field before you leave and look for a real edge; if there isn't one within range, fish structure and bait, because the break-side game isn't available to you.**

The one thing the gradient does tell you: **the islands are the warm end of your range** — which is exactly the pattern `locations/bight-geography.md` predicts under NW wind. In the 4/21/22 wind-rollover event, the northern Channel Islands and the LA/Ventura shelf rolled down **5–8 °F**, while **"the Coronados, the tuna grounds, Catalina, and San Clemente Island held their water through the blow"** (`YZtX1MiT0y8`; also `seasonal/april.md`). Your NW 8–12 kt is nowhere near that event, but the geography rule says the Coronados are the right side of the bight to be on when the north is blowing.

**Chlorophyll 0.9 — I can't grade this number.** The KB carries **no numeric chlorophyll scale** anywhere; its whole chlorophyll doctrine is about **age and edges**, not absolute values (`conditions/water-color.md`, `conditions/upwelling-and-turnover.md`). What you can actually do with it:

- **Ask the freshness question.** A **new cold bloom** — an overnight **~5 °F drop plus green water after an afternoon NW wind** — is a local upwelling event, "bad *now*, productive *later*." A **mature bloom edge** is what you fish (`conditions/upwelling-and-turnover.md`, `conditions/water-color.md`). Your islands reading is the *warmest* of the three spots, which does not look like a fresh cold crash — but the rule needs the **day-before SST at the same spot**, which you haven't given me. Pull it.
- **Fish the seam, not the mass.** Bait was found **holding in the dirtier water** while clean blue water sat empty, and predators work the **dirty/clean edge** (`conditions/water-color.md`, `HzE4FHHcvTk` 8/17/22). Don't default to the prettiest water — find the seam.
- **Cameron's own doctrine is on record here:** in warm-water years, weight chlorophyll/colour **at least as heavily as SST**, and **don't fish "dirty green" water for gamefish** (`conditions/water-color.md`, source `cameron`).
- **The Coronados are not one water cell.** Conditions "vary a lot across that group" — which is exactly why BightSST splits the Coronados entry into **each of the 6 spots individually**, taking the eval set from 8 to ~14 (`locations/bightsst-eval-targets.md`, `conditions/upwelling-and-turnover.md`, source `cameron`). **One averaged 0.9 reading for "the islands" hides the spread.** Pull per-spot.

**No tuna case in these numbers.** October's break rule has bluefin **condensing outward toward Tanner and Cortez** as the coast fragments (`seasonal/october.md`, `locations/bight-geography.md`) — out of a Coronados day's range. Dorado concentrate at the green-cold/blue-warm coastal boundary, referenced around **~71–72 °F** (`conditions/water-temperature.md`); you're 5 degrees under that. Yellowfin want **SST max × chlorophyll min** and the KB gives no absolute threshold. Treat any offshore fish as a bonus, not the program.

**Note the break-side rules exist for bluefin, yellowfin and dorado — not for yellowtail.** The yellowtail read is a different axis: **water temperature and bait depth** (`species/yellowtail.md`, source `cameron`).

---

## 2. Sea state — this is a go, with a hard afternoon clock

**Swell 3 ft @ 10 s is fine.** `conditions/sea-state.md`'s steepness rule: period drives feel far more than height, and the flag is when **the period in seconds approaches the height in feet** — 10 vs 3 is nowhere near it (for scale, the note calls 10 ft @ 15 s "barely felt" and 3–4 ft @ 4–5 s "brutal"). Capt. Dave Hansen's harder line is that **sub-10-second intervals are "absolutely horrible"** regardless of height (`NC3-3pJDEgo`) — you're sitting exactly on 10, so you have no margin if the period drops.

**Wind is your actual constraint.** Same source: **wind above ~12 kt is what raises whitecaps, and 12 kt is Hansen's personal don't-run cutoff** (`NC3-3pJDEgo`, single-mention, medium confidence). Your NW 12 kt afternoon lands right on that number. Two rules stack on top of it:

- **Forecast error is asymmetric** — assume the forecast errs worse, and that afternoon wind at the islands **strengthens rather than eases**. If it's windier than forecast in the morning, assume it builds all day and a small boat **bails early** (`conditions/sea-state.md`).
- **Homebound wind:** plan return timing **against** the afternoon build, not on the outbound conditions (`conditions/sea-state.md`, `HzE4FHHcvTk` 8/17/22). Your return from the Coronados is northbound into the NW.

**Two checks before you commit each morning:**
1. **12–24 h wind hindcast**, not just the forward forecast — a calm-morning read hides overnight wind and leftover chop (`conditions/sea-state.md`).
2. **Current-vs-swell opposition** along the route: where current runs against the NW swell it compresses the interval and stands it up — a forecast **4 ft @ 10 s fishes like 6 ft @ 7–8 s**, and no point forecast shows this (`conditions/sea-state.md`). Degrade your 3 ft @ 10 s wherever the current field opposes.

**Launch/return exposure (if you're going out of San Diego Bay):** Cameron's own chart work has the bay entrance open to swell from roughly **160°–186°**, with the measured channel seaward axis at **186°**; **Point Loma blocks swell from west of that axis** (`conditions/sea-state.md`, source `cameron`). A NW swell sits outside that window — the channel should be protected. Cameron's profile launch is **Dana Landing, Mission Bay**, normal departure ~8 am (`profiles/cameron/boat.md`) — on this wind pattern I'd move that earlier and be off the water before the 12 kt fills in.

Worth checking before you write off a bad-looking outer forecast: the **Catalina Eddy can shield the inner San Diego banks and tuna grounds while it blows outside** (`locations/island-structure.md`, `conditions/sea-state.md`, `S2L3KLSQ6Is` 5/26/22).

---

## 3. Moon and tide — last quarter is a neap, and that changes the day

**Last quarter = neap tide, the smallest tidal range** (quarter moons put sun and moon ~90° apart so the bulges partially cancel — `conditions/tide-and-slack.md`, `9tTM99InluM`; also `conditions/moon.md`). Three consequences:

- **The moon window and the tide window do NOT stack.** `conditions/moon.md` notes that springs on full/new stack a big-swing tide onto the moon window. You get the opposite: **weak swings, weak current.**
- **You're clear of the full-moon bass suppression.** The "gorge at night, shut down by mid-morning" pattern is a **clear full-moon** effect (`conditions/moon.md`, `Blh2BA-7Ono` 7/21/22, `XLVUhV8DW64` 10/12/22). Mid-day isn't automatically dead for you.
- **You're also clear of the post-moon relocation trap** — the "discount report persistence hard, schools moved 10–15 nm overnight" discipline is a moon-peak rule (`conditions/moon.md`, `planning/report-reading-and-forecasting.md`). Last quarter sits a week past the full.
- **Where last quarter falls in the windows:** the working rule is full/new **±1 week elevated, leading days strongest**, with the moon peak itself a relocation event (`conditions/moon.md`). Hansen's dissent — kept side by side, not reconciled — is that the best window is **7 days before AND 7 days after the full**, with the moon peak being travel, not bite; he says the 7-days-after window is when "that stuff really gets going" (`fri_BWI-VA0`). Last quarter is roughly that day. **Read it as neutral-to-mildly-positive, not as a gate.**

**The neap risk you must actively manage: no current.** `conditions/current-diagnostics.md` names the failure mode exactly — **"the treadmill is off"**: bait pointing in all directions rather than lined up, and **fish metering but not biting**. That's a **move-or-wait** signal, not a "grind it out" signal. Hansen's earlier tell for the same shutoff: **baits getting hit nearly every drop, then several drops in a row with nothing** (`aFb221LUoD0`, single mention).

**So anchor the day to the tide, and arrive early:**
- **Be at your highest-percentage zone an hour BEFORE the tide change** — not at it (`conditions/tide-and-slack.md`, 2/20/25 report).
- **Window compression:** on weak/off-peak conditions the action compresses into the tide windows; wide-open days bite all day. Neap + fall fragmentation = **anchor zones to tide times and be disciplined about arriving early to each** (`conditions/tide-and-slack.md`, `HzE4FHHcvTk` 8/17/22).
- **The late-morning slack** (when a tide falls after ~9:30) is the prime pop-up window; pop-ups also cluster in the afternoon, so **re-run water you marked earlier at those tide times** (`conditions/tide-and-slack.md`).
- **This is doubly true at the Coronados specifically.** Coronado yellowtail run **"seeing-not-biting" cycles with narrow daily windows** — you'll mark and even *see* fish that won't eat until a short window opens. **Anchor those days to tide and current, not to the clock** (`species/yellowtail.md`, `seasonal/april.md`, `YZtX1MiT0y8` 4/21/22). Be on the fish and ready when it comes rather than expecting an all-day grind.

I don't have the actual tide times for your dates and the KB doesn't carry a tide table — pull them and hang the two days off them.

---

## 4. Where in the island group

**The Coronados sit ~13 mi from San Diego, off Mexico; the western coast is exposed to colder Pacific currents and tidal swings, so the water stays bait-rich. "The Coronados are synonymous with yellowtail"** (`species/yellowtail.md`, `D5DR7Kx42_A`).

The KB's spot library (`sources/spot-lists.md`; committed because Cameron waived the private-only restriction — *"none of these spots are secret,"* 2026-08-12, per `CLAUDE.md` and `profiles/cameron/spots.md`):

**Coronado Islands**
| Spot | Position |
|---|---|
| Pukey Point | 32 26.850 / 117 18.000 |
| Middle Grounds | 32 25.810 / 117 15.950 |
| Ribbon Kelp | 32 24.800 / 117 13.880 |
| Lighthouse | 32 23.290 / 117 14.570 |
| 5-Minute Kelp | 32 22.940 / 117 13.515 |
| South Kelp Ridge | 32 22.000 / 117 13.260 |
| Rockpile | 32 17.620 / 117 10.030 |

**Rockfish areas, Coronados vicinity**
| Spot | Position |
|---|---|
| Lower 9 Mile Bank | 32 32.500 / 117 20.500 |
| Coronado Canyon | 32 30.300 / 117 17.500 |
| North of North Island rockfish area | 32 27.380 / 117 18.000 |
| **East of Pukey Point (yellowtail & rockfish)** | 32 27.000 / 117 14.100 |

Format is `deg min.mmm`, all lat N / long W (`profiles/cameron/spots.md`). **The KB gives no structure description, depth, or preferred-current note for any individual Coronado spot** — only the coordinates plus the one annotation on East of Pukey Point. So you pick between them with the universal typology, not with spot lore:

**Decide the day's current vector once, then pre-judge every spot on the list.** Current direction is **coherent across a region on a given day** — read it once and apply it to the whole list, then confirm with observables at each stop (`conditions/current-structure.md`, Academy Ep. 14). Then apply the typology (`locations/island-structure.md`, `conditions/current-structure.md`):

- **Land-attached perpendicular ridges are two-directional** — they only produce on **parallel** current (running along the shoreline, uphill or downhill). Current **straight into the beach is marginal**; **straight off the beach is dead — avoid**. A perpendicular ridge on an off-the-beach current is a non-starter no matter how good the water looks.
- **Standalone banks fish in any direction**, but each has its own preferred directions you learn spot by spot.
- **Coastal deep spots default-prefer downhill (N→S).**
- **Late-fall exception, kept side by side:** on 11/23/22 at San Clemente the bass bites **required current running INTO the island with off-color water present** — fish used the dirt to ambush. Parallel is the prior, into-beach is a viable late-fall/off-colour state, off-beach is dead (`conditions/current-structure.md`).

**Kelp-corner selection at the kelp spots** (Ribbon Kelp, 5-Minute Kelp, South Kelp Ridge): **downhill current → work the northwest corner of the bed; uphill current → the southeast corner** — same logic carries to rock structure (Dave Hansen, `kzD0kSnnVPw`, single mention, medium confidence, `conditions/current-structure.md`).

**Read current strength off the kelp itself** (`conditions/current-diagnostics.md`) — this is your gear-change trigger all day:

| Kelp | Current | Do |
|---|---|---|
| Pulled **~20 ft under** | Raging | Surface presentations are **dead** — go deep / weighted |
| **Laid flat** on the surface | Strong | Fishable but hard; work the down-current side |
| **Resurfacing** / standing back up | Slacking | **Switch back to the surface / lighter** |

On a neap, expect to live in the bottom two rows. **The transition from "laid down" to "resurfacing" is your cue to change gear before the window — watch the kelp, not the clock.**

**One more layer that's specific to this zone:** Cameron's own practice is watching **sportboat AIS stop/start patterns at the Coronado Islands** (e.g. the Grande, MMSI 366746210) as "one of the most valuable data sources he has for learning the islands" (`planning/fleet-intelligence.md`, source `cameron`). That's third-party-observed and hard to fake. **VHF chatter is the opposite** — Hansen states outright he has used the radio to pull competing boats off his own program with a fabricated "wide open" call, and that anglers who are actually on fish don't broadcast it (`planning/fleet-intelligence.md`, `9hEa3sGTh40`). Working channels offshore SoCal are **72 or 65**. And **"go fishing for fish, not for boats"** — a cluster of sportboats is usually one boat stopping and the rest following it over (`ZFqe49jRgA0`).

---

## 5. The program: yellowtail, three faces, three rods rigged at once

Yellowtail is the router. `species/yellowtail.md` frames them as showing three faces — **boiling/breezing surface fish, paddy yellows, and bottom/structure yellows** — and is explicit that these are **"outputs of water temperature and bait depth acting on one population — states, not fish types"** (source `cameron`). The same fish roam the column and **feed looking up**.

**The operating doctrine for your two days (Cameron, `species/yellowtail.md`): rig the surface-iron outfit, the heavy yo-yo/dropper outfit, and the flyline outfit SIMULTANEOUSLY, and switch as the read (temp + bait depth) changes.** No situation locks you to one presentation — the table below is starting ranks, not exclusive routes.

Also on record and unreconciled, which matters in October: **Cameron holds that calendar date doesn't matter for yellowtail — water state (temp + bait) does**, kept side by side with the corpus year-anniversary prior (`species/yellowtail.md`). Worth knowing because the KB's Coronado yellowtail entry is filed as **"the warming-transition (spring) classic"** — so you're fishing a zone whose corpus prior is a spring one, in a fall month. Cameron's water-state doctrine is what justifies going anyway.

### Situation → technique → gear (from `species/yellowtail.md`)

| Situation | Do this (ranked) | Gear class |
|---|---|---|
| Boiling/breezing surface fish, or fish on/around a kelp paddy | 1) **Surface iron** 2) flylined bait 3) stickbait/jerkbait | Jig-stick class; 40–50 lb flyline class; 20–50 lb heavy bass-stick for the hard bait |
| **Tight balls hugging structure** / marks on hard bottom or pinnacles (~5–10 fm) | 1) **Yo-yo iron** 2) **dropper loop** | 40–60 lb class stout rod + high-ratio reel |
| Deep marks on a high spot, fast drift | Slow-pitch / vertical jigging | Slow-pitch / knife-jig class, **130–250 g** |
| **Fish visible but not biting** (seeing-not-biting) | **Flylined bait; downsize leader/hook; wait for the window** | 40–50 lb flyline class |

Note the fourth row is the Coronados row. When they're showing and not eating: **live bait, drop leader size, anchor the plan to the daily bite window** — don't burn the day changing jigs.

### The core doctrine numbers

- **Heavy full-size irons (Salas 6X class) work the majority of the time on structure fish; vertical/flat-fall jigs 100–180 g depending on current are the change-up** (`species/yellowtail.md` Doctrine, `D5DR7Kx42_A` — the Coronados/BOLA roundup, high confidence).
- **Structure/bottom yellows:** *"We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite"* (`D5DR7Kx42_A`).
- **Slow-pitch band:** 150–300 ft, **bit best 150–180 ft** (`vqsD0qpwcJA` / `Jtf-bU4aM-c`). At the island proper you're likely shallower than that; the Coronado Canyon / Lower 9 Mile side is where that band lives.

### Surface iron (`techniques/surface-iron.md`)

- **Distance is the technique**, but **placement beats distance** — landing the jig ON moving fish beats a longer cast past them.
- **The cast:** hang the jig about a **leader length below the tip — roughly 18 in**; take the rod to **2 o'clock**, let the blank load, sweep through to **9 o'clock**, turning the wrist slowly. The rod does the work; the commonest error is shoving with the arms. Pendulum by moving the tip **up and down**, not side to side (`VpW91AKOFVQ`, Scotty/Brothers, high confidence).
- **Retrieve:** start winding the instant it lands; a **steady grind, tip pointed DOWN at the water** — tip up pulls the iron onto the surface and it stops swimming (`VpW91AKOFVQ`; `3dVc-2rsYII` Hansen, high confidence). **Speed up for yellows.**
- **Coronados-specific, and useful:** *a big school at the Coronado Islands will often eat on a **faster, less exacting retrieve**; the smaller mainland schools from **Del Mar down to Imperial Beach** run markedly more finicky and need the retrieve dialled in precisely* (`VpW91AKOFVQ`). Don't over-finesse it at the islands.
- **Wind up → heavier iron** (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`). Your afternoon NW 12 kt is the trigger.
- **Hookset: wind through it, don't swing.** Roughly 9 of 10 strikes come as the fish grabs the swimming iron amidships and shakes it ("dog boning") before turning — a swing jerks the jig out of its mouth and ends the shot; winding keeps it in the zone for a repeat bite. **Crank as fast as you can once bit until line starts peeling out the other way** — that's the tell you're actually hooked up (`3dVc-2rsYII`, `KLoEJInlmZo`, Hansen, high confidence).
- **Reeling too fast is called out as the single most common mistake** — when fish you can see, and have caught on that jig before, won't eat, **suspect retrieve speed before you change jigs** (`3dVc-2rsYII`).
- **Weight:** a surface iron generally runs **2–3 oz**, distinctly lighter in the hand than a **5–6 oz** yo-yo iron (`VpW91AKOFVQ`, high confidence).

### Yo-yo iron (`techniques/yo-yo-iron.md`)

- **Position up-current of the mark** so the drop sweeps down onto the structure. **Free-spool the iron straight to the mark**, thumbing the spool so it falls under light tension and tracks straight down instead of scoping away.
- **The retrieve is one thing: wind as fast as you can, all the way up.** The strike is a reaction to the fleeing iron; there is no finesse cadence. No hit → drop back and rip it again.
- **A heavy iron is mandatory** so it reaches the zone and stays vertical in current.
- **Conflict, kept side by side:** Hansen defines yo-yoing as a repeated **crank-then-freespool cycle that stays down in the strike zone**, not one continuous wind to the surface (`wzI0lpgKT1U`, high confidence). Both are in the KB unreconciled — on a neap with weak current I'd try the crank-and-drop cycle when the full burn isn't producing.
- **Iron:** Salas 6X / Salas CP 105 type. **Traditional yellowtail yo-yo colours: scrambled egg, and blue and white** (`A70kK2niu2Q`, medium confidence).

### Dropper loop (`techniques/dropper-loop.md`)

- **Sinker at the very bottom, 6–10 oz; hook(s) on the loop above it.** A **longer loop gives the bait more action — err long.**
- **If the current is heavy, up the weight** until it holds bottom; under-weighting drags the sinker off the structure and the bait leaves the strike zone. (On a neap, expect to be at the **light end** — a 6 oz was run on a low-drift day.)
- **Deadstick in the rod holder is the default** — one to two, even three dropper rods soaking while your hands work an iron. More lines in the water, more bites.
- **The retrieve once hooked up: slow, steady wind, all the way to the surface. No jerking, no pumping** — jerk-and-wind-fast winds the fish off the hook (`U-dGRQ0X-Mc`, Hansen, San Clemente).

### Flyline (`techniques/flyline.md`)

- This is your **seeing-not-biting** answer. Yellowtail flyline build: an **8–8'6" rod, lighter action, rated 20–40 to 20–50 lb**; braid backing to **80–100 yd of 30 lb mono top shot**, then **4–6 ft of fluorocarbon in 25 or 30 lb** — **25 lb gets bit a little better, 30 lb gives the leverage to turn a fish off rocks or kelp**. Hook to bait size: **2/0** for jumbo bait and smaller mackerel, **1/0** for smaller sardines and anchovies (`A70kK2niu2Q`, `LTCFjqtSI8g`, medium confidence).
- **Run 4–6 ft of fluoro even though ~3 ft is enough** — fishing 25 lb means cutting and re-tying after every fish to clear nicks, so the extra length is buffer.
- **Distance beats weight.** Get the bait **beyond everybody else's**, into its own zone. Adding a split shot or slider to help the cast is a crutch, not an upgrade — **no weight, hook tied direct** (`gKrYKvqHUjk`, Hansen).
- **Match line weight to the BAIT, not just the fish**: 40 lb to flyline a mackerel, but drop to a **15–20 lb** setup if you're on anchovy — a small anchovy can't swim 40 lb line through the water (`gKrYKvqHUjk`).
- **Hooks:** J hooks are the stated recommendation for yellowtail (circle hooks for bluefin) — `species/yellowtail.md` via `UfuiWFVvz2E`, corroborating `tackle/hooks.md`.

### Gear, in class terms and resolved

Class terms (`tackle/gear-classes.md`) → the profile lookup (`profiles/cameron/rods.md`, `profiles/cameron/tackle.md`). If you're not fishing Cameron's profile, use the left column:

| Job | Class | Cameron's resolution |
|---|---|---|
| Surface iron | Jig-stick class, 8–10 ft, casts 2–4 oz, ~25–60 lb | **Torium setup** — Phenix Abyss 10'0" 25–60 lb + Torium 20HG, 50 lb braid |
| Yo-yo / sinker rigs / dropper | Yo-yo heavy-iron class, ~8 ft XH 40–80 lb, fast crank | **Trinidad 40** — RCJB96XH 8'0" XH 40–80 lb, 80 lb braid |
| Flyline | Flyline/soft-rod class, ~9 ft MH ~30–65 lb | **Avet setup** — Teramar TMC90MHB2 9'0" + Avet MXJ, 50 lb braid |
| Utility / lures | Utility inshore baitcast class | Tranx or Lexa 400 |
| Slow-pitch (if you work the deep band) | SPJ class, PE1.5–2, 130–250 g | **Open item — Cameron doesn't own one yet** |

**Line/leader for the iron:** the standard build is ~**80 lb braid main, a short 50 lb / ~18 in mono-fluoro leader to a 100 lb clip** tied straight to the iron so you can swap without re-tying (`techniques/surface-iron.md`). Run the **thinner end of your top-shot range on irons specifically** — a thick top shot dampens the swimming action in a way it doesn't on a stickbait or popper (`F7jLrt2j2X8`, Cesar, medium confidence).

**A directly on-point top-shot datum:** one angler sizes his iron top shot **by location — 40 lb mono for the full-day-accessible islands (Coronado Islands, Channel Islands, Catalina), 50 lb for overnight-range destinations and anywhere in Baja**, on the reasoning that the overnight spots carry a genuine trophy shot at any moment (`LTCFjqtSI8g`, Ray Sharifi, unregistered channel — medium confidence). Attributed, not doctrine.

**Owned irons that fit (`profiles/cameron/tackle.md`):** JRI-7 (light blue, ~Tady 45 class, medium-fast — the local/kelp all-rounder), Strictly Irons Glory (light blue, wide drawn-out kick, slow and steady — **the change-up for picky bites / slack current**, which is your neap scenario), Strictly Irons Mighty (tan, medium-to-high speed), Squidco Candy Bar SR Lite (scrambled egg, 3 oz), JRI-5 (biggest, slow-to-medium on heavy line), Nomad Slidekick 120g (4.25 oz — heavier, can be **sunk out to cover the column**, which is your wind-day punch-through jig). **Yo-yo: Salas 6X (blue) and Salas CP 105.**

---

## 6. Shape of the two days

**Day 1 — grade the group, don't try to fish all of it.**

- Depart early enough to be fishing before the 8 kt fills. Cameron's normal ~8 am departure (`profiles/cameron/boat.md`) is too late for this wind pattern.
- **Bait first** (section 7), then run to the island.
- **Read the current once on arrival** and pre-judge the whole spot list off it (`conditions/current-structure.md`). Deploy the **chum bucket as a deliberate current sensor** — it's an artificial "thumb over the hose" and its drift line is a live reading (`planning/search-and-glassing.md`, `conditions/current-diagnostics.md`). **Chum drifting straight back off the stern = wind-dominated lay; chum swinging off at an angle to the boat = real current cutting across** — that angle is your direction sensor.
- Work the **kelp spots** (Ribbon Kelp, 5-Minute Kelp, South Kelp Ridge) on the appropriate corner for the current direction, and grade **East of Pukey Point** — the one spot the library flags for yellowtail.
- **Get off the water ahead of the afternoon build.** Don't push the last hour.
- Log the current direction, which spots had bait/marks, and the tide time of anything that popped. That's Day 2's plan.

**Day 2 — return to your own marks at tide time.**

The KB's template for exactly this, from the island fathom-curve worked example (`locations/island-structure.md`, `conditions/current-structure.md`, 8/31/22):

1. One popped fish appears near the structure.
2. **Identify the structure that fish related to** — treat it as a signal, not noise.
3. Run it **slowly** and wait. **Do NOT sprint to where the fleet went.**
4. **Return to your own marked positions at tide time.**

The governing rule, near-verbatim: **"sign associated with structure is a repeatable decision; sign in no-man's-land is low value."**

Two more Day-2 disciplines:
- **Pop-ups cluster at the late-morning slack and again in the afternoon — re-run the water you marked yesterday at those tide times** (`conditions/tide-and-slack.md`).
- **Beds and spots re-bite.** The calico framework generalises: **10–25 casts to the prime edge, then move**; if they're not on the prime spot they're usually not in the bed — but **come back later** (`species/calico-bass.md`, Ep. 13).

**Secondary targets if the yellowtail don't play** (all supported, all thin in the corpus for this zone):
- **Calico bass** on the kelp — weedless swimbait to the stringers, or surface iron along the kelp line; **heavy fluoro leader (40–65 lb) for kelp abrasion** (`species/calico-bass.md`). Note the October wildcard: **grunion-in-kelp events override water quality entirely** — every-cast bass in ugly, stagnant water you'd normally skip; the mixed bird pile *on* the kelp is the tell (`seasonal/october.md`, `OYOda6T3f-8` 10/20/22).
- **Bonito** — "sportboats doing good on the bonito" is a common line in the fall-fragmentation island reports; they boil **outside the kelp** where you can pull off a structure spot and cast into the foam. Small chrome jigs, downsize to the bait. Treat a bonito boil as a **measure of life** — it tells you the zone is productive (`species/bonito.md`).
- **Barracuda** — kelp lines and boiler rocks, same water as the bass, mixed-bag component; **they have real teeth, so the terminal end changes** when you target them (`species/barracuda.md`).
- **Rockfish** on the Coronado Canyon / Lower 9 Mile / North-of-North-Island marks. Meter-and-chart fishery, no surface sign; **at the islands current is as important as bait — a spot with no current will meter fish that won't bite** (`species/rockfish-lingcod.md`). **California rockfish regs do not apply in Mexican waters** — see section 9.
- **Kelp paddies on the run:** the KB puts the best paddy water **south of San Clemente/Catalina and along the coastal strip from Dana Point to Oceanside and southward** (`locations/bight-geography.md`, `HzE4FHHcvTk`). Check any paddy **fast** — a look, a sounder pass, one bait; **seconds to a minute or two, not twenty** — then move. Paddies restock **only at night**, so a paddy sat on for hours won't turn on by waiting (`conditions/kelp-paddies.md`, `ZFqe49jRgA0`). Under a paddy showing no surface activity, look for **boomerang-shaped arcs around 90–120 ft** (`species/yellowtail.md`).

---

## 7. Bait

**You have both paths at the Coronados, and the KB says do both.**

**Make your own — this is a documented Coronados program (`bait/making-bait.md`, source `cameron`):**
- **Where:** the Coronado Islands (and La Jolla during shortages).
- **Sabiki to ~100 ft.**
- **8 oz sinker** to get the string down and hold it.
- Result on record: **5 twelve-inch mackerel on one drop.**
- Twelve-inch mackerel are big, hearty baits — **heartier than sardine** (`bait/fishing-live-bait.md`).

**Buy sardines at the barge (`bait/making-bait.md`, `7WapaxdtjQg`, Hansen):**
- **Avoid the 6:00 a.m. rush** — the 3/4-day and half-day sportboats all load then. Go **5:00 a.m. or 7:00 a.m.**
- **Hail on VHF channel 11** with the barge's name twice plus your boat's name; wait for the response before approaching.
- **Never board the barge** — ask the attendant for help instead.
- **Tell the attendant you want it loaded light and you're not in a rush.** Treat him well; tip at the end.
- **Floor, not a target:** **at least three scoops every time you run offshore** — bait gets used to throw, to chum and to fish with, and there's no topping off out there (`bait/bait-tanks.md`, `9hEa3sGTh40`).

**Fishing it (`bait/fishing-live-bait.md`):**
- **Match the hatch** — sardine isn't always the best option, and when the gamefish are chewing mackerel a live mackerel out-fishes a sardine (`mscHk0qiXnk`).
- **Hook position by the swim you want:** **nose** (clear spot in front of the eyes) is the all-purpose — flyline, slow-troll, and it's what sends a bait down a **dropper loop**; **belly** sends it down and away; **collar/shoulder** keeps the line up out of the water; **butt** flylines great, swims away and a bit deeper, and **defeats sea lions at the islands that pick off nose-hooked baits** (`T3p1mrqNjIo`, `8YvmROeVL-0`). **Trade-off: the butt hook draws blood, so that bait doesn't last as long** (`ZggReeO1nyU`, Hansen).
- **Keep it active** — wind in and cast back out rather than letting a bait sit idle; keep a bait presented since the yellowtail are moving through (`species/yellowtail.md`, `D_Y2G0rBZCs`).

**Cameron's tank (`profiles/cameron/boat.md`):** 30 gal, Rule 401 Tournament 500 GPH, running off the **single starting battery** — a NOCO GEN5X1 was added July 2026 specifically to hold the battery up while the bait pump runs overnight. If you hold bait between the two days, that charger is the plan; the boat has no house battery and no shore-power inlet.

---

## 8. Search, anchoring and the meter

**Glassing (`planning/search-and-glassing.md`):**
- Glass from a **full stop**, or bow into the swell at **~1 kt** — you can't glass off a rolling boat.
- **360° in small increments, 3–4 minutes per full scan.** When you catch a bird, **watch it 30–40 seconds** before judging it.
- Ranges: a few terns at **~0.5–1 mi**, a big bird spot at **~2 mi** from deck level; from a hardtop, birds to ~2 mi and dolphins to ~4 mi. **Space glass stations 3–4 mi apart.**
- **Along a bank, run the contour at 16–18 mph with a lookout ~30° off each bow.**
- **Gray-calm mornings:** scan down-swell a quarter-mile out and watch **kelp paddies roll over the swell crests**.
- *"If you're not burning batteries every trip or two, you're not looking enough."*

**Birds (`conditions/bird-reading.md`):** **terns are the best bird**, and both voices agree. **Locked-in repeated dives on one spot = bait only; a MOVING dive-line = bait being pushed by fish underneath — that's the one to run on** (7/21/22). Cameron will follow working terns offshore even with no other birds working. Finer read: **birds actively diving = the school is surface-feeding; birds off the fish = the school is still there but "puddling,"** not gone (`A6DJoXbID4c`).

**Anchoring (`planning/search-and-glassing.md`):**
- **Bottom fish → anchor on the spot.** Grade the mark with **repeated passes** — idle over the high spot, mark the peak, turn around and re-drive the same track to confirm bait/fish sign — then **drop the anchor into the adjacent SAND, not on the rock**, so your lines drift back onto the structure (`6DzbsElGE7E`, `xI9tPJFXbUM`, Hansen — repeated doctrine, high confidence).
- **Midwater / gamefish → anchor UP-CURRENT, with the standoff scaled to current strength** so chum and baits sweep down onto the fish.
- **Break-off risk (yellowtail) → anchor further still**, so a hooked fish has room before it reaches the structure. That's your setting at the Coronados.
- **Sportboat trick worth stealing:** at anchor, **chum gets pushed UP-current toward the bow by the fish themselves** — watch for **birds locking on up there and put the surface iron under them** (7/14/22).
- **If they mark but won't bite at anchor, try drifting over them instead** — position above the marks and let the boat drift through, on the idea that the fish want more motion in the presentation. That move brought a dead bite back on (`97clKtVsEOs`). Pair this with the "treadmill is off" read from section 3.

**Sounder (`planning/electronics-and-sounder.md`):**
- **Run manual range, not auto** — repeated across three Hansen videos, high confidence. Working range **0–120 ft on older machines, 0–150 ft on newer.** On auto with the real (deep) bottom set, a school shrinks to a barely visible speck; on manual it paints as a large, distinct **upside-down-U** (`9hEa3sGTh40`).
- **Size the range so the bottom sits mid-screen, not pinned at the edge** — that leaves room to read hard vs soft bottom and to pick fish and bait out of the column above it (`FEXgl0eQCa8`).
- **Bottom hardness by return thickness, any brand:** thin faint line = sand/mud; thickening and darkening = rock (`6DzbsElGE7E`).
- **Yellowtail sit exclusively on hard bottom — "they're not going to be out in the mud"** — so read bottom hardness to decide whether a spot is worth working *before* you look for fish sign on it (`species/yellowtail.md`).
- **The yellowtail read: tight balls hugging structure, arcs / boil-ups at ~5–10 fathoms near structure.** And **a thin, lighter mark riding HIGHER than the bait ball can be the yellowtail itself**, pushing bait up off the rocks — **that's the sign to commit the anchor, not the bait pile alone** (`species/yellowtail.md`, `D5DR7Kx42_A`, `6DzbsElGE7E`).
- **Stop only on marks you can grade — it's a bait budget.** Every stop on a no-name mark burns bait and time.
- **Photograph the meter during bites** to build your own library of marks that paid off.
- Cameron's plotter is a **Garmin GPSMAP 840xs** (`profiles/cameron/boat.md`).

---

## 9. Papers and permits — **the KB does not cover this**

I have to be straight with you: **you asked the one question this knowledgebase cannot answer.**

I searched the whole KB. There is **nothing** on:
- a **Mexican sportfishing licence** (CONAPESCA) for anglers,
- a **Mexican boat/vessel permit** for a private boat fishing Mexican waters,
- **FMM / tourist permit or visa** requirements,
- **temporary import** paperwork for a boat or trailer,
- **Mexican liability insurance**,
- **US CBP reporting on return** from foreign waters,
- **Mexican bag, size or season limits** for yellowtail, calico, bonito, barracuda or rockfish,
- **customs, immigration or check-in procedure** at the border or at sea.

**Do not treat anything above as clearance to fish.** The Coronados are Mexican waters — `species/yellowtail.md` states it plainly (*"~13 mi from San Diego, off Mexico"*) — and the KB's own rule is that regulatory claims must carry jurisdiction, an as-of date, and a verify-current flag (`CLAUDE.md`). It carries none for Mexico, because the corpus has none.

**The four fragments that exist, so you know exactly how thin this is:**

1. **The KB's only Mexico sportfishing-regulation datum anywhere** is a crew member on camera at East Cape, Baja California Sur (2019-02-13) saying a **circle hook was "mandatory"** — the note itself reads this as a Mexican regulatory requirement and flags it **"as of the 2019-02-13 video date — verify current CONAPESCA/DOF circle-hook rules before fishing," not independently confirmed against the regulation text** (`techniques/flyline.md`, `GptrotE0x5M`). That is **Baja California Sur, not Baja California Norte**, it is seven years old, and it is unverified. It is not guidance for your trip.
2. The only mention of Mexican fishing permits as a *thing you obtain* is incidental logistics on a Cedros charter — a group "reached by small-plane charter out of Ensenada with **Mexican fishing permits obtained in Tijuana**" (`species/calico-bass.md`, `xIUKmH9ccgQ`). A note about how one operator did it in 2012, not a procedure.
3. **`species/rockfish-lingcod.md` explicitly warns that California rockfish regs — the year-end closure, the depth limits — do NOT apply in Mexican waters "in any case; verify current Mexican/Baja regs separately before fishing there."** So the KB's CDFW rockfish content is actively *not* applicable to your Coronados bottom-fishing.
4. The KB's only worked example of a fishing-licence requirement is **California**: `species/california-spiny-lobster.md` documents that lobster needs **two** documents — a California fishing licence **plus** a lobster report card. That's a CDFW example and irrelevant here except as a reminder that "one licence" is often not the whole answer.

**What I'd do:** get the current requirements from the Mexican authorities and from CBP directly before the trip, and if a California licence matters for any leg (e.g. anything you fish inside US waters on the run out or back), confirm that separately. I'm not going to guess at it from general knowledge — the whole point of this KB is that a claim without a source and an as-of date isn't a claim.

---

## 10. Fish care

Once the fish is aboard (`fish-care/dorado-and-general.md`, `fish-care/gaffing.md`):

- **The salted slurry:** **rock salt, ~2 cups per 7–10 lb bag of ice**, plus a splash of seawater to wet it. The salt is what drops the mix below freezing.
- **Get fish cold fast and keep them out of the sun.**
- **Never freshwater-rinse.** Salt water only, whole fish and fillets alike.
- **Bring a car cooler for the drive home** — plan the cold chain past the dock.
- **Gaffing:** yellowtail up to **40–50 lb** fall in the **3-in hook / ~6-ft gaff** class. ⚠ Note this note sits at **low confidence** — it's from a sponsored gaff spot and the registry caps those regardless of content.
- Cameron's boat carries **100–125 lb of ice per trip** (`profiles/cameron/boat.md`) — that's your slurry budget for two days.

**Fillet storage (`fish-care/dorado-and-general.md`):** ice-saltwater soak before bagging, dry before freezing, water-displacement bagging for a near-vacuum seal without a machine. Refrigerated ~3 days; vacuum-sealed frozen 1–3 months; plain ziplock frozen ~1 week to 1 month.

---

## 11. What the KB could not tell me

Listed so you know where to fill in from elsewhere: Mexican permits/licences/paperwork and Mexican bag-and-size limits (section 9); any numeric meaning for chlorophyll 0.9; per-spot structure, depth or preferred-current detail for the seven named Coronado spots; tide times for your dates; anything about overnighting at the islands; a documented October Coronados yellowtail prior (the KB's Coronado prior is a spring one); and a yellowtail break-side rule (the KB has those only for bluefin, yellowfin and dorado).


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/report-reading-and-forecasting.md`, `planning/fleet-intelligence.md`, `seasonal/october.md`, `seasonal/april.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/water-regimes.md`, `conditions/upwelling-and-turnover.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/sea-state.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `locations/bight-geography.md`, `locations/island-structure.md`, `locations/zone-lexicon.md`, `locations/bightsst-eval-targets.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/bonito.md`, `species/barracuda.md`, `species/rockfish-lingcod.md`, `species/california-spiny-lobster.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `techniques/slow-pitch-jigging.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `bait/fishing-live-bait.md`, `bait/bait-tanks.md`, `fish-care/dorado-and-general.md`, `fish-care/gaffing.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`, `skills/boat-day/SKILL.md`  
*videos:* `XLVUhV8DW64`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `YZtX1MiT0y8`, `D5DR7Kx42_A`, `VpW91AKOFVQ`, `6DzbsElGE7E`, `xI9tPJFXbUM`, `NC3-3pJDEgo`, `fri_BWI-VA0`, `9tTM99InluM`, `kzD0kSnnVPw`, `wzI0lpgKT1U`, `U-dGRQ0X-Mc`, `3dVc-2rsYII`, `KLoEJInlmZo`, `LTCFjqtSI8g`, `A70kK2niu2Q`, `F7jLrt2j2X8`, `UfuiWFVvz2E`, `vqsD0qpwcJA`, `Jtf-bU4aM-c`, `7WapaxdtjQg`, `9hEa3sGTh40`, `FEXgl0eQCa8`, `SgF5hRlEGqU`, `97clKtVsEOs`, `ZFqe49jRgA0`, `mscHk0qiXnk`, `T3p1mrqNjIo`, `8YvmROeVL-0`, `ZggReeO1nyU`, `gKrYKvqHUjk`, `D_Y2G0rBZCs`, `A6DJoXbID4c`, `Blh2BA-7Ono`, `S2L3KLSQ6Is`, `5p6gu14ZC4w`, `GptrotE0x5M`, `xIUKmH9ccgQ`, `I84uoay_jwQ`, `E4vKwRaRueA`, `2gHRrR3D8rY`, `aFb221LUoD0`, `Rf1HKJG-SDg`, `6-8KfjEg0x8`, `cameron`  
*gaps admitted:* Mexican paperwork and permits are entirely absent from the KB — no sportfishing licence (CONAPESCA), no boat/vessel permit, no FMM/tourist permit or visa, no temporary import, no Mexican liability insurance, and no US CBP return-reporting procedure. | Mexican bag limits, size limits and seasons for any species at the Coronados are absent; the KB's only regulatory content is California/CDFW, and species/rockfish-lingcod.md explicitly says CA rockfish regs do not apply in Mexican waters. | The KB's single Mexico sportfishing-regulation datum (a crew member calling circle hooks 'mandatory') is from East Cape, Baja California Sur, dated 2019-02-13, flagged unverified against the regulation text, and is not applicable guidance for Baja California Norte in 2026. | The KB carries no numeric chlorophyll scale, so a value of 0.9 cannot be graded as good or bad — its chlorophyll doctrine is entirely about bloom age and edges, not absolute values. | No per-spot structure, depth, bottom-type or preferred-current description exists for any of the seven named Coronado Islands spots — sources/spot-lists.md gives coordinates only, plus one annotation ('yellowtail & rockfish') on East of Pukey Point. | The KB has no tide tables or tide times, so the tide-window timing that the Coronados 'seeing-not-biting' doctrine depends on has to be sourced elsewhere. | No guidance anywhere on overnighting, anchoring out, or a multi-day stay at the Coronado Islands in Mexican waters — the two days are planned as two day-runs by default. | The KB's Coronado Islands yellowtail entry is filed as 'the warming-transition (spring) classic'; there is no October/fall-fragmentation Coronados prior in the corpus. | The break-side rules in conditions/water-temperature.md cover bluefin, yellowfin and dorado only — there is no yellowtail break-side rule to apply to the SST field. | No documented Coronados bait-history, squid presence, or forage-species prior for October; the squid-zone doctrine in the KB is attached to Santa Barbara Island, San Clemente Island and Catalina, not the Coronados. | Surface-iron colour has no systematic doctrine in the corpus — the note says so explicitly and declines to invent one. | No Coronados run-time, fuel or route detail; the only figure is the '~13 mi from San Diego' distance in species/yellowtail.md.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Two days at the Coronados, mid-October — the program

Worked through [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md). I used only the conditions you gave (no BightSST pull), and everything below comes from the knowledgebase — where it has nothing, I say so.

## 1. The envelope (protocol step 1b — binding on everything after it)

- **`regions`: `baja-pacific-north`** (the Coronados sit in Mexican water; `locations/regions.md` puts the US-border-to-28°N Pacific side in that region, and `species/yellowtail.md` confirms the Coronados/Ensenada/Punta Banda group is labelled `baja-pacific-north`) **plus `socal-bight`** for the transit and any 9-Mile/Point Loma stop.
- **`waters`: `island`** primarily; add **`bank`** if you work Lower 9 Mile / Coronado Canyon, **`open-ocean`** if you check paddies on the way.
- Consequence: this is an **island structure + bait program**, not a bay or beach program, and Sea-of-Cortez-only material (cabrilla etc.) is off the table by the gate.

## 2. What your numbers actually say

**The SST set doesn't give you a break.** Islands 66.8 / 9 Mile 66.2 / Point Loma 65.9 is a **0.9 °F spread across three points** — that is a gradient, not the sharp edge October doctrine wants. `seasonal/october.md` is blunt about the month: *"conditions become pretty important… look 100 % at your temp chart and chlorophyll"* (`XLVUhV8DW64`, `OYOda6T3f-8`), and `conditions/water-temperature.md` says the value is *"usually not the absolute number but which side of a break a species sits on,"* with offshore edges able to jump multiple degrees in ~1 mi. **You cannot resolve a break from three point values — pull the chart before you commit to a tuna plan.**

**What the numbers do rule in and out:**
- **Dorado — out.** `conditions/water-temperature.md` puts the dorado concentration at the green-cold/blue-warm boundary around **~71–72 °F**. You are 4–5 °F under it.
- **Yellowfin — weak.** They want **SST max × chlorophyll min** (`species/yellowfin-tuna.md`, `conditions/water-temperature.md`, `XLVUhV8DW64`/`OYOda6T3f-8`). Your warmest water (66.8) is the islands, and 9 Mile is your *coolest* offshore number — the wrong shape for a yellowfin run.
- **Bluefin — unresolvable, not excluded.** The rule is relative: cool side of a break in warm water, warm side in cold water (`conditions/water-temperature.md`). With no break in the data, there's no side to pick. Note the 76 °F ceiling is explicitly **soft, not hard** (`9/14/22`), so temperature alone never rules bluefin out — a chart does.
- **Calico — in.** 66.8 °F sits inside the stated **65–68 °F** preference (`species/calico-bass.md`, Tommy Ponce, `LqW32NSkObY`; medium confidence, past ~70 °F they get lethargic).
- **Chlorophyll 0.9 — the KB gives no numeric threshold.** `conditions/water-color.md` is all edge-and-age: distinguish a **new cold bloom** (an overnight ~5 °F drop plus green after an afternoon NW blow — skip it now, mark it for recovery) from a **mature bloom edge** (fish it). One number with no neighbours and no history can't be read either way.

**Sea state — go, with a hard afternoon discipline.** NW 3 ft @ 10 s passes the steepness rule in `conditions/sea-state.md` (flag it when period in seconds approaches height in feet; 10 vs 3 is fine). Dave Hansen's thresholds in the same note (`NC3-3pJDEgo`, medium): **wind over ~12 kt raises whitecaps and is his personal don't-go line**, and **sub-10-second intervals are a hard bad flag** — you're sitting exactly on both edges in the afternoon. Two rules bind:
- **Forecast error is asymmetric** — assume it errs worse, and that **afternoon W at the islands strengthens rather than eases** (Ep. 6, `zKmZ4zql2ws`); if it's windier than forecast in the morning, assume it builds all day and a small boat bails early (`7/14/22`).
- **Homebound wind:** runs south into Mexican water put the wind on the return leg — *"uphill misery."* **Plan the return against the afternoon build, not the outbound conditions** (`8/17/22`, `conditions/sea-state.md`).

Add the 12–24 h wind hindcast, not just the forward forecast (same note) — a calm morning read hides overnight chop.

**Last-quarter moon — this is the biggest planning lever in your set.**
- Quarter moons are **neap tides — the smallest tidal range** (`conditions/tide-and-slack.md`, mechanism from `9tTM99InluM`; `conditions/moon.md` states the same coupling). Small swings mean less water movement, and at the islands **current is as important as the bait — a spot with no current will meter fish that won't bite** (`species/rockfish-lingcod.md`, `6-8KfjEg0x8`).
- You are **not** in a moon window: the elevated windows are full/new ±1 week (`conditions/moon.md`). The upside is you're also not fighting post-moon relocation, and reports age normally rather than being heavily discounted.
- So: **anchor the day to the tide changes.** Be at your highest-percentage zone **an hour before** the change, not at it (`conditions/tide-and-slack.md`, `2/20/25`), and expect **window compression** — off-peak conditions push the action into the tide windows while wide-open days bite all day (`8/17/22`). This lines up exactly with the Coronados' own signature failure mode: **"seeing-not-biting" cycles with narrow daily windows** — you'll mark and even see fish that won't eat until a short window opens; anchor those days **to tide and current, not to the clock** (`species/yellowtail.md`, `YZtX1MiT0y8`).

**Regime:** mid-October is **fall fragmentation** — an "everything season, but scattered": breadth of species, low density of any one (`conditions/water-regimes.md`, `seasonal/october.md`). Plan for a mixed bag, not a one-species massacre. One override worth knowing: **a grunion-in-kelp event beats water quality entirely** — every-cast bass in ugly stagnant water, with a mixed bird pile on the kelp as the tell (`seasonal/october.md`, `10/20/22`).

## 3. The species call: a yellowtail-led island mixed bag

Primary router is [`species/yellowtail.md`](species/yellowtail.md) — *"The Coronados are synonymous with yellowtail"* (`D5DR7Kx42_A`), ~13 mi from San Diego, the western side exposed to colder Pacific currents and tidal swings so the water stays bait-rich. Be aware of the honest caveat: **the KB frames the Coronados as the warming-transition (spring) classic**, and Cameron's standing counter-doctrine is that **calendar date doesn't matter for yellowtail — water state (temp + bait) does** (kept side by side with the corpus year-anniversary prior). Behind them: **calico bass** on the kelp spots, **bonito** and **barracuda** as the classic "three B's" mixed bag (`species/bonito.md`, `species/barracuda.md` — both `baja-pacific-north` tagged, so both clear the gate), and **rockfish** on the Coronados-vicinity hard bottom.

**Situation → technique, straight off the router table:**

| What you see | Do this (ranked) | Gear class |
|---|---|---|
| Boiling / breezing fish, or fish on a paddy | 1) surface iron 2) flylined bait 3) stickbait 4) skip jigging | jig-stick class; 40–50 lb flyline |
| Tight balls hugging structure, marks on hard bottom ~**5–10 fathoms** | 1) yo-yo iron 2) dropper loop | 40–60 lb stout rod + high-ratio reel |
| Fish **visible but not biting** (the Coronados special) | flylined bait, downsize leader/hook, **wait for the window** | 40–50 lb flyline |
| **Metered but not showing** | chum them up, then cast — or get any jig down to their depth | as above |
| Wind up (20–25 kt+) after good surface days | 1) yo-yo iron 2) keep the surface iron as a picker | 40–60 lb + high-speed reel |

That last row is a **Coronado Islands** data point specifically: 2026-04-21, 25 kt gusts, fish metering and swiping without committing; the crew's read was the wind turned the bite and other boats confirmed it had gone *"mostly yo-yo"* — but the iron still produced two, so it's a **re-rank, not an abandonment** (`ejUTAnONf7o`, medium).

**The Coronados chum-and-cast sequence is high-confidence doctrine here** (`techniques/surface-iron.md`, Jared Saaib, `4pT0efBD1j0` 2020-08-18 at the Coronado Islands, repeated in `dS9gd9k7A7Q`): **meter the school → throw live chum → let them boil → cast the iron into the boil.** Casting to natural surface activity outranks it; this is the fallback when they're metered and not showing. Same source: the fish are **boat-shy** — *"they would not let me drive them over the top of them"* — which is the practical reason the long cast exists. And **hold the stop while someone's bent**: a hooked fish holds the school near the boat (`gdqI2dNd5_U`).

**On the meter (`species/yellowtail.md`):**
- Structure yellows = **tight balls hugging structure**, classic read **arcs/boil-ups at 5–10 fathoms** near structure (`D5DR7Kx42_A`).
- **40–60 ft marks that aren't showing = surface-iron and light-bait water — explicitly not a yo-yo day** (`0DKmYId1NN4`, medium).
- **Shape beats depth:** a **stratified column** (marks running bottom-to-mid or all the way up) = fish hunting → slow-trolled baits; a **ball stuck to the bottom** = present but not hunting → dropper-loop water, not flyline water (`HTowqnwAMeA`). **High and spread = biting; tucked tight to the bottom = not** (same trip).
- Marked-but-not-surfacing schools still get bit: *"just about every lure that makes it down to the depth that fish is, is a bite"* — named specifically for yo-yo iron (`tpmOYXYQwhU`, medium).
- **Hard bottom only, never mud** — read return thickness (thin = sand/mud, thick = rock) before you even look for fish sign (`6DzbsElGE7E`); a thin, lighter mark riding *above* the bait ball is often the yellowtail itself pushing bait up — that's your commit signal.

**Bite-rate calibration so you don't panic-switch:** a good day of local yellowtail fishing is **three or four bites**; a 12–15-bite day was called an anomaly on camera. At that rate, two fishless hours is not evidence your technique is wrong (`HTowqnwAMeA`). Balanced against the same source's *"you can't really be glued to a certain technique"* — that crew pulled anchor, started moving and slow-trolling, and **roughly quadrupled their bite rate**.

## 4. Running the two days

**Spots.** The KB has **no Coronado Islands location page** — what it has is the coordinate library in [`sources/spot-lists.md`](sources/spot-lists.md) (public; Cameron waived the private-only restriction 2026-08-12), listing the group N→S:

| Spot | Position |
|---|---|
| Pukey Point | 32 26.850 / 117 18.000 |
| Middle Grounds | 32 25.810 / 117 15.950 |
| Ribbon Kelp | 32 24.800 / 117 13.880 |
| Lighthouse | 32 23.290 / 117 14.570 |
| 5-Minute Kelp | 32 22.940 / 117 13.515 |
| South Kelp Ridge | 32 22.000 / 117 13.260 |
| Rockpile | 32 17.620 / 117 10.030 |

Plus, in the vicinity: **Lower 9 Mile Bank** 32 32.500 / 117 20.500, **Coronado Canyon** 32 30.300 / 117 17.500, **North of North Island rockfish area** 32 27.380 / 117 18.000, **East of Pukey Point (yellowtail & rockfish)** 32 27.000 / 117 14.100. Note that **conditions vary a lot across the group** — that's exactly why the BightSST eval set splits the Coronados into six individual spots rather than one average (`locations/bightsst-eval-targets.md`, `conditions/upwelling-and-turnover.md`).

**Pick spots by current direction, not by name** (`locations/island-structure.md`, `conditions/current-structure.md`):
- **Land-attached perpendicular ridges are two-directional** — they only work on **current running parallel** to the shoreline. Straight into the beach is marginal (with a real late-fall exception when off-color water lets fish ambush against structure); **straight off the beach is dead — skip it** no matter how good the water looks.
- **Standalone banks fish any direction** but each has its own preferred ones.
- Kelp corner selection: **downhill current → work the NW corner; uphill → the SE corner** (Dave Hansen, `kzD0kSnnVPw` / `sIoNELGlxmk`; the front/up-current edge is where the bigger fish stack).
- Because current is spatially coherent, once you know the day's vector you can **pre-judge every spot on the list** before you burn fuel.

**Verify the current on the water, don't trust the plotter.** Kelp pulled ~20 ft under = raging (surface presentations dead, go deep); kelp laid flat = strong; **kelp resurfacing = slacking — switch back to the surface**, and that transition is your cue to change gear *before* the window (`conditions/current-diagnostics.md`, `8/31/22`, Ep. 14). The **chum-bucket drift line is your current sensor**: chum straight off the stern = wind-dominated lay; chum swinging off at an angle to the boat = real current. A chart plotter's current-arrow layer is reading wind, not current.

**Anchoring geometry (`planning/search-and-glassing.md`):** bottom fish → sit on the spot, but **grade the mark on repeated passes and drop the anchor in the sand beside the rock, not on it**, so your lines drift back onto the structure (repeated doctrine, `6DzbsElGE7E` + `xI9tPJFXbUM`). Midwater gamefish → **anchor up-current, standoff scaled to current strength**. **Yellowtail specifically → anchor further still**, so a hooked fish has room before it reaches the structure. Too deep to hook (180–200 ft+) → set up the drift instead, reading wind vs current, and use the outboard angled off the keel as a rudder to slow/steer it (`_ZThckj2TIM`).

**Searching, if the spots are dry.** Glass from a full stop or bow into the swell at ~1 kt, 360° in small increments, **3–4 minutes per scan**, and watch a bird **30–40 seconds** before judging it; stations **3–4 mi apart**; along a bank run the contour at **16–18 mph** with a lookout 30° off each bow (`planning/search-and-glassing.md`). Sign vocabulary: **boiler/foamer, breezer** (ripple in calm water), **flat spot** (the smooth whitecap-free patch in chop — the version you'll actually see in 12 kt) (`91ZJbhAnzMg`). Birds: **terns are the best bird** — a locked-in repeated dive = bait only, a **moving dive-line = bait being pushed from underneath**, and cast **under the diving bird**, not at its general position (`conditions/bird-reading.md`, `7/21/22`, `JiJYamo0QHk`). **Boobies are mostly seen at the Coronado Islands and Cameron rates them worth paying attention to** (attributed observation, no corpus doctrine). **Diving pelicans = wrong area for gamefish, right area for mackerel** — use them as a bait tell.

**Day 2 is where the two-day format pays.** Return to **your own marked positions at tide time** rather than sprinting to where the fleet went (`locations/island-structure.md`, `8/31/22`). If the current has reversed overnight, **don't just re-anchor to the same GPS position** — fish face into the current, so reset onto the *other* side of the spot so your baits reach the new up-current face (`planning/search-and-glassing.md`, `BskCsKaTiZw`/dave-hansen, medium). Age any intel you get: intraday schools drift at **low single-digit miles per hour**, so draw a box around a reported position sized by the report's age, not a pin (`planning/report-reading-and-forecasting.md`, `8/17/22`). For fleet reading, **AIS stop/start patterns on the sportboats at the Coronados** (e.g. the Grande, MMSI 366746210) are Cameron's most valuable learning layer there — third-party-observed and harder to fake than VHF chatter (`planning/fleet-intelligence.md`).

**Bait.** Buy sardines at the barge when they're available; **when making bait it's always mackerel** on sabikis — and Cameron has sabiki'd both La Jolla and the Coronado Islands when the barge couldn't fill him (`bait/making-bait.md`, cameron). Barge etiquette: never board it, follow the side signal (cone/arrow), **hail on VHF ch 11** with the barge name twice plus your boat name, and tell the attendant you want it **loaded light** (`7WapaxdtjQg`). One bait-driven technique switch: **if the tank is anchovy rather than sardine or mackerel**, a flylined anchovy draws bycatch as readily as the target — switch to iron (`techniques/surface-iron.md`, `8TO-tuYjwWk`, medium), and if the forage is small "rice" anchovy, **drop to a light iron (Tady AA-light / A1-light class, ~a third the weight of a Tady 45)** — on small bait the small jig out-bites the big one **two or three to one**, and it drags the tackle down with it (9 ft medium-action composite, smaller narrow reel, ~50 lb braid to a short fluoro leader) (`2/27/25`, `pcwcRdmWmLc`).

**One Coronados-specific hazard:** sea lions. If one works a hooked fish boatside — **wind continuously, never pump**; once it grabs the fish, **throw the reel into free spool** to give total slack (reads as the line breaking, so it lets go), then wind fast to recover (`species/yellowtail.md` → `techniques/fighting-big-bluefin.md`, `mdhoEQPqpng`).

## 5. Gear

Class terms first (`tackle/gear-classes.md`), because I don't know what's in your boat. Cameron's doctrine is to **rig all three simultaneously and switch as the read changes** — the day moves between faces of one population, not between fish types:

1. **Surface iron / jig-stick class** — 8–10 ft (9 ft okay, **10 ft better**; *"an 8-ft jig stick is a yo-yo rod"*), throwing **2–3 oz** irons (a second attributed range: 1¾–2¾ oz, 5–7 in). Tady 45 / Salas 7X / 6X Jr. class. **Wind up → step up to the heavier 7X-class iron to punch the cast out** (`D5DR7Kx42_A`) — relevant on your 12 kt afternoons. Carry three jobs' worth: small-and-erratic for a reaction bite, a Tady-45-type all-rounder, and a heavy one that casts through chop (`A70kK2niu2Q`). **Beware high-ratio reels** — these jigs were designed around a 4:1 Jigmaster; 6.5–7.5:1 is called too fast (`Ec2GaNpiOHI`), kept side by side with a counter-view that 7:1 is a workable torque middle ground.
2. **Yo-yo / heavy-iron class** — ~8 ft, XH, 40–80 lb, fast crank; **5–6 oz** iron (Salas 6X / CP 105 class) against the surface iron's 2–3 oz (`VpW91AKOFVQ`). Free-spool to the mark under thumb tension so it tracks straight down, then **wind as fast as you can, all the way up** — *you can't crank it too fast, but it's easy to crank it too slow* (`RNRFrfepiW0`). A stated standard rig for 12–30 lb yellowtail near an island or bank in **120–180 ft**: two-speed Fathom 30 class, **65 lb braid + a 50-yard 40–50 lb mono top shot**.
3. **Flyline class** — ~9 ft MH fast, 30–65 lb; **40–50 lb** for yellowtail. If bonito start intercepting the flylined baits, switch to a **sliding sinker** (2–4 oz egg to a 2/0–4/0 J hook) to get under them (`yGXSrUauo2w`, medium).
4. **Dropper loop** for balled, inactive fish on the bottom: loop **12–18 in** (min 12; if you build it to 24 in tie it with a **double San Diego jam**), sitting **3–4 ft above the sinker**; SoCal reference weights **6–10 oz** (a heavier same-fishery data point runs a **16 oz torpedo** with a 5/0 hook, kept side by side); tie a **plain overhand knot above the sinker as a breakaway** so a snag costs the lead, not the rig; **wind up 3–4 cranks off the bottom**; fish it **in gear, never free-spool** near structure. Bite reads as a **strong thump** — wait for the rod to load, then wind down and reset. **The first 30–40 ft off the bottom is the critical window** — win that race in low gear under a tight drag before the fish gets back into the structure (`SAltQjih0ms`).

**If this is Cameron's panga:** the three-outfit stack resolves to the **Torium** (Phenix Abyss 10'0", 25–60 lb, 50 lb braid) for surface iron, the **Trinidad 40** (8'0" XH 40–80 lb, 80 lb braid) for yo-yo/dropper/sinker rigs, and the **Avet/Teramar 90MHB2** (30–65 lb class, 50 lb braid) for flyline. Owned irons cover it: **Salas 6X** and **Salas CP 105** for yo-yo; JRI-7 (~Tady 45 class), JRI-5, Strictly Irons Glory (wide drawn-out kick — the picky/slack-current change-up) and Mighty, Squidco Candy Bar 3 oz, Nomad Slidekick 120 g for the column. **Two gaps to name rather than paper over:**
- **No slow-pitch / knife-jig setup** — it's an open shopping item in `profiles/cameron/rods.md`. If the fish end up deep on a high spot, the KB's slow-pitch row (130–250 g, 150–300 ft) has nothing in your box to resolve to.
- **`profiles/cameron/boat.md` has `range_nm: null` and `sea_state_max_ft: null`** — deliberately not guessed. The protocol says **ask** rather than assume, so before I'd sign off on a 12 kt-afternoon run to Mexican water in a 22 ft panga I need your real range and sea-state limit. Relevant boat facts that are recorded: 30-gal bait tank on a **Rule 401, 500 GPH** pump running off the **single starting battery** (a NOCO GEN5X1 charger was added July 2026 to hold it up while the pump runs overnight — worth knowing for a two-day trip), **100–125 lb of ice per trip**, normal departure ~8 am, launch from **Dana Landing, Mission Bay**.

**Fish care:** yellowtail (and dorado, halibut, WSB) up to **40–50 lb** are the **3-in hook, ~6-ft gaff** class (`fish-care/gaffing.md`). Get them cold immediately in a **salted slurry — ~2 cups rock salt per 7–10 lb bag of ice plus a splash of seawater** (the salt is what drops it below freezing); **never freshwater-rinse**, and bring a **car cooler** so the cold chain survives the drive home (`fish-care/dorado-and-general.md`).

## 6. Papers and permits — read this part carefully

**The knowledgebase does not cover this, and it says so itself.** [`sources/regulatory-claims.md`](sources/regulatory-claims.md) carries an explicit *Known gap*: **"Mexican licensing and entry requirements are absent from the knowledgebase"** — noting that anyone planning a Baja trip needs an FMM, a CONAPESCA fishing permit, a passport and Mexican insurance, "and the KB currently says none of it."

The only paperwork detail anywhere in the KB is in [`locations/bahia-de-los-angeles.md`](locations/bahia-de-los-angeles.md), and it is for a **drive-down road trip to Bahía de los Ángeles**, not a boat crossing — treat it as adjacent, not as your checklist (Mexico: **INM** for entry, **CONAPESCA** for fishing; as reported **2026-08-06**; verify current requirements before you travel — foreign jurisdiction, these change):

1. **FMM (tourist permit)** — filled out online in advance; needs passport details, point of entry and length of stay; it produces a printout. **Print it** (one traveler reported being checked three times).
2. **Mexican fishing licence** — bought online; the source flags a **new website as of 2026**, so search fresh rather than trusting an old bookmark. Have your passport with you.
3. **Passport.**
4. Vehicle insurance (Baja Bound named) — **that's car insurance for a drive-down, not boat coverage**.

**What the KB has nothing on, and I will not fill in from outside knowledge:**
- Any **permit for the boat itself** in Mexican waters, or a **per-vessel fishing permit** / everyone-aboard-must-be-licensed rule.
- **Clearing in or out**, port captain / zarpe requirements, or **US CBP reporting on re-entry** from Mexican waters.
- **Baja California (northern) sportfishing regulations** — bag limits, size limits, seasons, gear rules. The KB's *entire* Mexico regulatory table is **one row**: circle hooks mandatory in **Baja California Sur** sportfishing, as of **2019-02-13** (`GptrotE0x5M`) — that's the other state, ~700 miles south, and it does not tell you what applies at the Coronados.
- One thing the KB *does* state plainly: **California/CDFW regulations do not apply in Mexican waters** — so your CA rockfish season/depth rules and the 2/person/day CA bluefin limit are not your rulebook out there; **verify current Mexican/Baja regs separately before fishing** (`species/rockfish-lingcod.md`, `sources/regulatory-claims.md`).

Everything in this section carries the KB's standing caveat: **nothing here is current by virtue of being written down — check the issuing agency (CONAPESCA for permits, INM for the FMM) before you fish.**

## 7. The short version

Two-day island program, tide-anchored because you're on a neap moon: run down early both days, make or buy bait first, work the kelp spots (Ribbon Kelp / 5-Minute Kelp / South Kelp Ridge / Lighthouse) and the north-end structure (Pukey Point, Middle Grounds, East of Pukey Point) **choosing spots by whether today's current runs parallel to the shore**, grade every mark before you stop, run the three-outfit stack and let the meter pick — 40–60 ft marks and boils = iron and light bait; balls tight to structure at 5–10 fathoms = yo-yo and dropper loop; metered-but-not-showing = chum them up and cast into the boil. Expect three or four good bites, not thirty. Be off the water ahead of the 12 kt afternoon NW so the northbound leg home isn't uphill. And sort the Mexican paperwork from CONAPESCA/INM directly — **this knowledgebase cannot tell you what a US private boat needs to fish Mexican water, and I'm not going to invent it.**


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/report-reading-and-forecasting.md`, `planning/fleet-intelligence.md`, `planning/trip-length-selection.md`, `seasonal/october.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/water-regimes.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/bird-reading.md`, `conditions/kelp-paddies.md`, `conditions/upwelling-and-turnover.md`, `locations/regions.md`, `locations/island-structure.md`, `locations/zone-lexicon.md`, `locations/bight-geography.md`, `locations/bightsst-eval-targets.md`, `locations/bahia-de-los-angeles.md`, `locations/cedros-island.md`, `locations/README.md`, `species/README.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/bonito.md`, `species/barracuda.md`, `species/rockfish-lingcod.md`, `species/white-seabass.md`, `species/yellowfin-tuna.md`, `species/bluefin-tuna.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `lures/iron-jigs.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `bait/bait-tanks.md`, `bait/fishing-live-bait.md`, `fish-care/gaffing.md`, `fish-care/dorado-and-general.md`, `profiles/cameron/boat.md`, `profiles/cameron/spots.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `sources/spot-lists.md`, `sources/regulatory-claims.md`  
*videos:* `D5DR7Kx42_A`, `YZtX1MiT0y8`, `4pT0efBD1j0`, `dS9gd9k7A7Q`, `gdqI2dNd5_U`, `ejUTAnONf7o`, `XLVUhV8DW64`, `OYOda6T3f-8`, `5to3Q5P7w90`, `5p6gu14ZC4w`, `HTowqnwAMeA`, `0DKmYId1NN4`, `tpmOYXYQwhU`, `mdhoEQPqpng`, `6DzbsElGE7E`, `xI9tPJFXbUM`, `VpW91AKOFVQ`, `RNRFrfepiW0`, `SAltQjih0ms`, `yGXSrUauo2w`, `A70kK2niu2Q`, `Ec2GaNpiOHI`, `yn1suHH6b1Y`, `pcwcRdmWmLc`, `8TO-tuYjwWk`, `91ZJbhAnzMg`, `JiJYamo0QHk`, `NC3-3pJDEgo`, `zKmZ4zql2ws`, `LqW32NSkObY`, `kzD0kSnnVPw`, `sIoNELGlxmk`, `BskCsKaTiZw`, `_ZThckj2TIM`, `6-8KfjEg0x8`, `9tTM99InluM`, `fri_BWI-VA0`, `4xzK7YaXK5s`, `ZFqe49jRgA0`, `7WapaxdtjQg`, `P36VGPPf120`, `GptrotE0x5M`, `vqsD0qpwcJA`, `cameron`  
*gaps admitted:* No Coronado Islands location note exists — the KB has coordinates for the seven named spots in sources/spot-lists.md but no per-spot structure, depth, or how-each-spot-fishes knowledge, and locations/island-structure.md is region-tagged socal-bight only, so its typology is applied here by analogy rather than by the region gate. | Mexican entry and fishing paperwork for a US private boat crossing by sea is not in the KB at all — sources/regulatory-claims.md logs it as a known gap; the only paperwork content (FMM, Mexican fishing licence, passport, vehicle insurance) is stated in locations/bahia-de-los-angeles.md for a drive-down road trip to Bahía de los Ángeles, not a boat crossing. | Nothing in the KB covers a vessel permit for a US boat in Mexican waters, per-boat fishing permits, clearing in/out or port-captain requirements, or US CBP reporting on re-entry. | The KB carries no Baja California (northern) sportfishing regulations — no bag limits, size limits, seasons or gear rules; its entire Mexico regulatory table is a single 2019 Baja California Sur circle-hook row that does not apply at the Coronados. | No tide tables or tide/slack times for mid-October — the KB's arrival-an-hour-before-the-change discipline cannot be converted into clock times from anything in the KB. | Chlorophyll 0.9 cannot be interpreted numerically — conditions/water-color.md gives only edge-and-age doctrine, no numeric thresholds or units, so a single value with no neighbouring water or history is unreadable here. | The three given SSTs (66.8 / 66.2 / 65.9 F) do not resolve a temperature break, and October doctrine is built entirely on break structure — the KB cannot substitute for a chart or a BightSST pull. | No October-specific Coronados material in the corpus: the KB frames the Coronados as the warming-transition (spring) classic; the Coronados-specific sessions cited are August 2020 (chum-and-cast) and April 2026 (wind re-rank). | No content on overnighting on a private boat at the Coronados — nowhere to lay up, anchoring or mooring overnight in Mexican water, or running two consecutive days out of one launch; planning/trip-length-selection.md covers sportboat trip formats only. | The active profile's boat envelope is unset — profiles/cameron/boat.md has range_nm and sea_state_max_ft as null, so the protocol requires asking for range and sea-state limit rather than assuming one; the KB also has no fuel-range or crossing-distance planning for a small boat. | No slow-pitch / knife-jig outfit in the profile — if the fish sit deep on a high spot, the KB's 130-250 g slow-pitch row has no owned gear to resolve to (logged as an open shopping item in profiles/cameron/rods.md). | No safety, VHF/emergency, or border-crossing procedure content for a small private boat operating in Mexican waters.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

MEXICO ISLAND, TWO DAYS, MID-OCTOBER — PRIVATE BOAT

I ran this through `planning/day-plan-protocol.md` in order, using only the conditions you gave (no live pull). Two things up front: the KB's Coronados program is written as a **spring** trip, and the KB **does not answer the paperwork question for a private boat**. Both are called out below rather than papered over.

---

## 1. The envelope (protocol step 1b — binding)

- **regions:** `baja-pacific-north` at the islands; `socal-bight` on the transit out and back (`locations/regions.md`, `locations/coronado-islands.md`).
- **waters:** `island`, `bank`, plus `nearshore-coast` on the run.
- Anything gated to `socal-bight` only is **off the table at the islands** — that includes the KB's `yellowtail — dropper loop` sub-page (`species/yellowtail-dropper-loop.md`, `regions: [socal-bight]`), even though the Coronados guide routes to the general `techniques/dropper-loop.md`, which is not region-gated. Sea-of-Cortez species (cabrilla, etc.) never surface for this trip.
- **Run:** the chain is ~13 nm off the San Diego bay entrance per `locations/coronado-islands.md` (cameron). Note the KB flags its own unit conflict here — `species/yellowtail-coronado-islands.md` says "roughly 13 **mi**" verbatim from `D5DR7Kx42_A`; the charted math on `locations/pukey-point.md` gives Zuniga Jetty → Pukey Point = **14.0 nm**, and `locations/middle-grounds.md` gives Zuniga → Middle Grounds = **~15 nm**. Plan on 14–15 nm each way, not 13.

---

## 2. Papers and permits — what the KB actually has, and what it does not

From `locations/mexican-waters.md` (authority: **INM** for entry, **CONAPESCA** for fishing; stamped **as of 2026-08**, verify current before you travel — this is a foreign jurisdiction and these change):

1. **FMM (tourist permit)** — filled out online in advance; needs passport details, point of entry, length of stay; produces a printout. **Print it.** One report of being checked three times on a trip (`P36VGPPf120`) — the KB flags that the source actually says "someone got checked three times last year," an unnamed third party, not one angler on one trip.
2. **Mexican fishing licence (CONAPESCA)** — bought online; **carry your passport when you buy** (`P36VGPPf120`). The note says the licence moved to a new website as of 2026 so search fresh rather than trusting an old bookmark — and flags that the year and the "search fresh" advice are the note's own additions, not the source's. Only "bought online" + "have your passport on you" are verbatim.
3. **Passport.**
4. **Mexican vehicle insurance** — Baja Bound named; ~$90 for a 2021 car and ~$130 for a newer Tacoma over 4 days (`P36VGPPf120`). **This is road-trip scoped.** It is relevant to you only for the tow vehicle and trailer, and the KB flags that no cited source actually states that US policies don't carry over.

**The gap you need to know about, stated plainly:** the KB carries an explicit flag on both `locations/mexican-waters.md` and `species/yellowtail-coronado-islands.md` — *no corpus source covers what a boat run from San Diego into Mexican water for the day requires: whether an FMM applies when you never land, and what a **private boat** as opposed to a vehicle must carry.* The Coronados are called out by name as "the single most common Mexican-water trip in the KB and the corpus does not answer it." Also absent: boarding/inspection practice and what the Mexican Navy asks for; and US declaration forms for bringing fish home. **Do not treat the four items above as a complete list for a boat.** Verify the vessel-side requirements with CONAPESCA/INM directly before you cross.

Limits: `sources/regulatory-claims.md` records **no** Mexican bag limit, size gauge or season for yellowtail, rockfish/lingcod, whitefish, sheephead, yellowfin or skipjack — all logged as "unknown, absent from the corpus." California/CDFW rockfish rules (10 fish, the 240 ft island RCA line, the year-end closure) are on `species/rockfish-lingcod.md` **and do not apply in Mexican water.** Verify with CONAPESCA.

Your California licence still matters on the US side of the transit (`locations/us-waters.md`, CDFW).

---

## 3. What your numbers say (protocol step 2)

**SST — you have a 0.9 °F gradient, islands warmest.** 66.8 at the islands, 66.2 at the 9 Mile, 65.9 at Point Loma. October is the month `seasonal/october.md` says the water chart runs the plan — "conditions become pretty important… look 100% at your temp chart and chlorophyll" (`OYOda6T3f-8`; the note flags that `XLVUhV8DW64` never says this line). But that doctrine is about **which side of a break** you fish, and a 0.9 °F spread across 15 nm is a gradient, not the sharp break `conditions/current-structure.md` and the October note want you to build a plan on. **Treat the islands as the warm end of a soft gradient and let structure, not the thermometer, pick the stops.**

What 66.8 °F supports and doesn't, by the numbers the KB actually states:

| Species | KB number | Your 66.8 °F |
| --- | --- | --- |
| Calico bass | preference band **65–68 °F**; past ~70 they go lethargic (`LqW32NSkObY`, `species/calico-bass.md`) | **dead centre of the band** |
| Bluefin | 70–72 °F preferred band stated against 81 °F fished the day before, 76 °F foamers, 63–65 °F January presence — "treat any single number as soft evidence" (`species/bluefin-tuna.md`) | below the stated band |
| Yellowfin | warmest × cleanest; 72 °F over a SoCal fall bite (`OYOda6T3f-8`, `SczdZIq3UmE`) | ~5 °F under it |
| Dorado | green-cold/blue-warm boundary ~71–72 °F; 71.6 °F on a productive paddy (`E4vKwRaRueA`) | ~5 °F under it |
| Yellowtail | **⚠ no SST band exists in the KB** — `species/yellowtail.md` flags the numeric bands as a gap and gives directional water-state reads only | not decidable from temperature |

**Read: this is an island/structure trip, not a tuna trip.** Don't run past the islands to the 9 Mile hoping for warm-water pelagics — the 9 Mile is 0.6 °F *colder* and nothing in the KB's stated numbers supports bluefin, yellowfin or dorado at these temperatures. The KB's own hedge applies: a single SST number is soft evidence, never a hard exclusion (`conditions/water-temperature.md`).

**Chlorophyll 0.9 — I can't grade this.** The KB contains **no numeric chlorophyll thresholds anywhere**. What `conditions/water-color.md` gives you instead is the freshness read: a chlorophyll signal has an age. New cold bloom (overnight ~5 °F drop + green after an afternoon NW blow) is short-term negative — mark it for the recovery, don't fish it today (`h3PTupup17I`). A **mature bloom edge** is where the chain has caught up and bait/predators stacked. Fish the **edge**, not the middle of a mass, and don't default to the prettiest blue — bait holds in the dirtier water and predators work the seam (`HzE4FHHcvTk`, `HWx1jDTGsng`). At the Coronados specifically, the zone's virtue is bait volume: the west side's exposure to colder Pacific currents and tidal swings is what keeps it loaded (`D5DR7Kx42_A`).

**Wind NW 8 → 12 kt: you are running right at the KB's threshold.** `conditions/sea-state.md` carries a working-captain rule that **wind above ~12 kt is what raises whitecaps**, and 12 kt is that captain's personal no-run cutoff (`NC3-3pJDEgo`; the note flags this as single-sourced and personally framed). Layered on top: **forecast error is asymmetric** — assume it errs worse, and assume afternoon W at the islands **strengthens** rather than eases (`zKmZ4zql2ws`); if it's windier than forecast in the morning, assume it builds all day and a small boat bails early (`DnSqw4r7A1s`). And the **homebound-wind rule applies directly to this trip**: a run south into Mexican water puts a W wind on the return leg — uphill misery — so **plan return timing against the afternoon build, not the outbound conditions** (`HzE4FHHcvTk`). Practical shape: be on the water at first light, take the bite window in the morning, and be turning north by early afternoon both days.

**Swell 3 ft @ 10 s: clean, but sitting on a line.** The steepness rule says flag a segment where the period in seconds approaches the height in feet — 10 vs 3 is nowhere near it, so this is a comfortable sea by that test (`zKmZ4zql2ws`). But the same note calls a **sub-10-second interval a hard bad-sea flag** (`NC3-3pJDEgo`), and you are exactly at 10 — no margin. **Channel transit:** the SD Bay entrance is open to swell from roughly **160°–186°** (measured seaward axis 186°), and **Point Loma blocks swell from west of the channel axis** (cameron) — a NW swell is on the blocked side, so the harbor transit should be the protected part of your day. One thing I can't do: `conditions/sea-state.md` wants the current vector checked against the swell (opposition compresses the interval and stands it up — a forecast 4 ft @ 10 s fishing like 6 ft @ 7–8 s). **You gave me no current, so that check is unrun.**

**Moon last quarter — this is the least helpful phase in the KB, and it changes your timing.** `conditions/moon.md` and `conditions/tide-and-slack.md`: **spring tides (biggest swings) fall on full and new; neap tides (smallest) fall on the quarters** (`9tTM99InluM`). Every elevated-probability window the KB documents is full/new ±1 week (`XLVUhV8DW64`, `fri_BWI-VA0`) — a quarter moon is the trough between them, and the KB states **no quarter-moon bite doctrine at all**. `species/yellowtail.md` separately flags moon-phase effect on yellowtail as a **no-corpus-source gap**.

The consequence is real and actionable: **neap = smallest tidal swing = least current.** For yellowtail, `species/yellowtail.md` states **current on = bite on** — slack current keeps the bite off and the current starting is what starts it (`fDSd9kqwYW0`); even a puff of current can fire a lee-side bite to 40 lb (`_r_qKX_7080`). On a neap you get less push, so:
- **Anchor the day to the tide/current changes, not the clock.** `conditions/tide-and-slack.md`: be at your highest-percentage zone **an hour before** the change (`6TBxHnkYXI0`), and when the bite is off-peak or marginal, **action compresses into the tide windows** — arrive early to each (`HzE4FHHcvTk`).
- Confirm current on the water rather than trusting the plotter: **a chart plotter's current-arrow layer reads wind, not current** (`BskCsKaTiZw`). Use kelp lean and chum-drift angle instead (`conditions/current-diagnostics.md`): kelp pulled ~20 ft under = raging, surface dead, go deep; laid flat = strong, work the down-current side; **resurfacing = slacking, switch back to the surface** — that transition is the cue to change gear *before* the window opens (`HnqiE05vdXs`). Chum swinging off at an angle to how the boat lies = real current cutting across.

---

## 4. The program (protocol step 3)

**Caveat first:** `species/yellowtail-coronado-islands.md` is the KB's only Coronados program and its `season_window` is **spring (warming transition)**. `species/yellowtail.md` maps October to **fall fragmentation** — "island fish keep biting while the water holds" — and immediately flags that half of that sentence as absent from all three cited sources. **There is no October-specific Coronados content in this KB.** What follows is the spring circuit applied to your October conditions, and you should treat it that way.

### Bait — decide this before anything else
Two paths (`bait/making-bait.md`):
- **Buy sardines at the barge.** Timing is the whole game: sportboats all load ~6:00 a.m. and the line forms by quarter to six, so target **5:00 a.m. or 4:30 a.m.** for no line (`ztpj1Xll0-U`, `bM2vUS1B-yQ`). A 7:00 a.m. arrival also avoids the line but "it's all gone" — it buys a short wait at the cost of your morning window (`7WapaxdtjQg`, `ztpj1Xll0-U`). Hail on **VHF 11**, tie to the side the cone marks, ask for it **loaded light**, tip the attendant, never board the barge.
- **Make mackerel on the sabiki at the islands** — this is cameron's documented Coronados program: sabiki down to **~100 ft** on an **8 oz** sinker; has loaded **5 twelve-inch mackerel on one drop**. Twelve-inch macks are heartier baits than sardine, and bigger bait selects bigger fish (`Zo92MG459gQ`, `d0yGBQDeY_4`).

Given a neap/low-current day and two days to fish, **do both**: buy light at 5:00 a.m. day one, and top up with macks on the sabiki when the troll goes quiet.

### The circuit — one loop, not a list of stops
`locations/coronado-islands.md` and `species/yellowtail-coronado-islands.md`:

1. **Set the troll before you reach the islands.** Pink and purple **Halco 190-class divers** are this zone's fish-finder (`lures/halco-laser-pro.md`). Trolling here is **prospecting that happens to hook fish**, not the presentation (`HTowqnwAMeA` — the KB flags that this source never mentions the Coronados; the prospecting framing is what it supports). Carry a spread of colors, styles and dive depths — fish key on presentation, depth or vibration on any given day. The flyline outfit tows a **20–30 ft diver**; a dedicated 6–7 ft troll outfit tows **40 ft divers**.
2. **Figure-8s around the islands, plus a pass across the Middle Grounds.** Charted positions (all cameron, from `sources/spot-lists.md`, carried on the per-spot pages):
   - Pukey Point (north end) **32°26.850'N 117°18.000'W** — ~14.0 nm from Zuniga Jetty
   - Middle Grounds (the mid-chain bank) **32°25.810'N 117°15.950'W** — ~15 nm
   - Ribbon Kelp **32°24.800'N 117°13.880'W**
   - Lighthouse **32°23.290'N 117°14.570'W**
   - 5-Minute Kelp **32°22.940'N 117°13.515'W**
   - South Kelp Ridge **32°22.000'N 117°13.260'W**
   - Rockpile (outlying, SE) **32°17.620'N 117°10.030'W**
   Neighbour spacing off the Middle Grounds: East of Pukey Point 2.0 nm NE, Ribbon Kelp 2.0 nm ESE, Pukey Point 2.0 nm WNW, Lighthouse 2.8 nm SSE, 5-Minute Kelp 3.5 nm SE, South Kelp Ridge 4.4 nm SSE.
   **Be honest about what these pages hold:** Rockpile, Ribbon Kelp, 5-Minute Kelp, South Kelp Ridge, Lighthouse, East of Pukey Point, North of North Island, Coronado Canyon and Lower 9 Mile Bank are all **minimum pages — position and parent zone only.** Depth, bottom composition and approach are flagged gaps on every one of them.
3. **Convert on sign or a troll strike.** Cast a **surface iron** at any surface activity (`D5DR7Kx42_A`). Fish **metered but not showing** get the chum-then-cast sequence: meter the school, throw live chum, let them boil, cast into the boil (`4pT0efBD1j0`, `dS9gd9k7A7Q`). **The long cast is load-bearing — they will not let the boat drive over the top of them** (`dS9gd9k7A7Q`).
4. **Hold the stop while anyone is bent.** A hooked fish keeps the school near the boat — get a jig back in the water while someone is still hooked up (`gdqI2dNd5_U`). A troll strike means more fish are under the boat, so keep the other trolled rod working and cast into the same water.
5. **Tight balls hugging structure → yo-yo iron.** Hit bottom, and **start winding the instant the jig touches — never let it sit** (`8XIy7hPsFkQ`); the bite comes a couple of cranks off the bottom and it's a reaction bite, so burn it (`D5DR7Kx42_A`). Wind through the bite rather than swinging — the continuous full-speed crank drives the hookset (`5pbA-wXoric`, `ETw_3AFxEcM`, `RNRFrfepiW0`). Position **up-current of the mark** so the drop sweeps onto the structure; thumb the spool so it falls straight instead of scoping away.
6. **With bait aboard**, slow-troll over the same zones, flyline when current and tide turn them onto bait, and put a **dropper loop** down to bottom marks (`D5DR7Kx42_A`).

### Reading the meter (`species/yellowtail.md`, `planning/electronics-and-sounder.md`)
- **Grade the bottom before you hunt fish:** thin/faint return = sand or mud, thick and dark = rock, and **structure fish sit on rock, never mud** (`6DzbsElGE7E`). Works on any brand, no discrimination mode needed.
- **Tight balls hugging hard bottom, arcs at ~5–10 fathoms (30–60 ft)** near pinnacles and high spots — ⚠ the KB flags this depth figure: `D5DR7Kx42_A` carries no depth at all, only "tight balls of yellowtails sometimes hugging the structure." Treat 5–10 fm as the KB's inference, not the source's number.
- **Fish at 40–60 ft not yet showing are staging up** — surface-iron and light-bait fish, not yo-yo fish; when they boil, go all-in on the iron (`0DKmYId1NN4`).
- **Shape reads feeding state:** stratified marks running bottom-to-mid-column, or fish sitting high and spread over a small rock (~20–30 ft across), are **hunting** → slow-trolled and flylined baits. **Balled tight to the bottom** = present but not feeding → dropper loop, plus a yo-yo burned past them for the reaction strike (`HTowqnwAMeA`, `tpmOYXYQwhU`).
- **Don't stop on the first bottom mark** — idle on and stack the picture depth by depth; every stop on an ungradeable mark burns bait and time (`KjVLn4cWHbc`, `QP6c8vcslVs`).

### Birds
Glass from a full stop or bow-into-swell at ~1 kt, 360° in small increments, **3–4 min per full scan**, and watch a bird **30–40 seconds** before judging it. From deck level expect a few terns at **0.5–1 mi**, a big bird spot at **~2 mi**; space glass stations **3–4 mi apart** (`planning/search-and-glassing.md`, `DnSqw4r7A1s`, `E4vKwRaRueA`). On a bank, run the contour at **16–18 mph** with a lookout ~30° off each bow.
- **Terns:** locked-in repeated dives on one spot = **bait only**; a **moving dive-line** = bait being pushed from below — that's the one to run on. Cast **under the bird the moment it dives**, not at its general position (`Blh2BA-7Ono`, `JiJYamo0QHk`).
- **Boobies:** `conditions/bird-reading.md` says boobies are **mostly seen at the Coronados** and cameron considers them worth paying attention to — but flags that there is **no corpus doctrine on this bird at all**, and no read distinguishing bait-only from fish-underneath. So: note them, don't build the day on them.
- ⚠ `locations/coronado-islands.md` claims "terns are worth reading here specifically" and the KB flags it as contradicted — the cameron source scopes terns as his best bird *generally* and scopes the **booby** to the Coronados.
- **Mixed piles** (gulls + pelicans + terns + cormorants) at open-water current breaks = bait only, skip — **exception:** a mixed pile **on kelp/structure** can be a real bait event worth working (`Blh2BA-7Ono`, `OYOda6T3f-8`).

### Expectations, and how to run two days rather than one twice
- **Seeing-not-biting is this zone's normal state, not the fish leaving.** Boats fishing the islands daily see more fish than they catch, and each day carries one short weather-or-time bite window; inside a cycle there is "no shortage of fish" (`YZtX1MiT0y8`). Presence stays high while catchability compresses.
- **Coronado droughts run in hours, not months** (`locations/coronado-islands.md`) — which is exactly why **the circuit is worth re-running rather than abandoning**, and why day two is not a wasted repeat.
- **Big Coronado schools forgive the retrieve** — they often eat a faster, less exacting retrieve than the finicky small schools on the mainland coast from Del Mar to Imperial Beach (`VpW91AKOFVQ`). Get the jig swimming and keep it moving before micro-tuning cadence. The general rule: there is no species-specific retrieve — when the lure swims right, fish bite it; the **kick-out** every third or fourth swim is the trigger, and a flat-swimming jig gets helped with speed changes and "a little perky-jerky" (`Ec2GaNpiOHI`, `yn1suHH6b1Y`).
- **Wind re-ranks the presentation; it doesn't end the day.** Gusts to 25 push fish off the top, the fleet bite goes mostly yo-yo, and the surface iron still picks a fish — a re-rank, not an abandonment. Fish swiping the jig without committing on a wind day is the wind turning the bite, not the wrong jig (`ejUTAnONf7o`). Your 12 kt afternoon is milder than that, but it's the same direction: **surface program in the morning, weight toward the yo-yo as the afternoon builds.**
- **Day two: don't re-run day one's pin.** `planning/report-reading-and-forecasting.md` — draw a box around a position sized by how old the intel is, not a pin. (The 10–15 nm overnight figure is scoped to **open-water bluefin not holding structure** (`Blh2BA-7Ono`), so I'm not applying it to island yellowtail; the KB has no overnight-displacement figure for structure fish — a gap.) Re-run the circuit, and re-read the water rather than assuming yesterday's edge is in the same place.
- **Bite-rate calibration:** a good SoCal **local-coast** yellowtail day is **three or four bites**; a 12–15-bite day is an anomaly, and two fishless hours is not evidence the technique is wrong (`HTowqnwAMeA`). The KB explicitly scopes that to the local coast, **not** to an island — so treat it as a floor for expectations, not a Coronados forecast.

### If the yellowtail won't play — the in-envelope backups
- **Calico bass** (`species/calico-bass.md`, gated `baja-pacific-north`, `island`): your **66.8 °F sits inside the stated 65–68 °F preference band**, and October–December is named as a transitional stretch that can pull another degree of warmth out of stable water (`LqW32NSkObY`). Kelp edges along the island faces — the Ribbon Kelp / 5-Minute Kelp / South Kelp Ridge line. Weedless swimbait to individual stringers on a 7–8 ft bass-class outfit, 40–60 lb, 7" slug on a 3/8–3/4 oz keel-weighted spring hook, heavy fluoro for kelp abrasion (`YIABTTYXeqc`).
- **Bonito and barracuda**: both gated in-region. Dated October appearances exist for both (`OYOda6T3f-8`, `5p6gu14ZC4w`, `Klfb433I3Uk`, `0KQ--N5TjqE`). The KB's framing is that **bonito hours and yellowtail hours are not the same hours** — the yellowtail window is the morning and the day then "becomes a pick-o day" of bass, barracuda and bonito (`Blh2BA-7Ono`). That is a good description of what your afternoons will probably be.
- **Bottom fish on the rockfish ground north of the chain** — Coronado Canyon **32°30.300'N 117°17.500'W**, Lower 9 Mile Bank **32°32.500'N 117°20.500'W**, North of North Island **32°27.380'N 117°18.000'W**, East of Pukey Point **32°27.000'N 117°14.100'W**. Rockfish, lingcod, whitefish and sheephead all sit in-envelope, and sheephead/whitefish are explicitly the cold-season resident package (`species/sheephead.md`, `species/ocean-whitefish.md`, `46ha7J1Fc6A`). **But: this is Mexican water and the KB has no CONAPESCA season, bag or gauge for any of them.** Verify before you keep one. Note also that `locations/coronado-islands.md` calls the East-of-Pukey ground "rockfish," and the KB flags that the source library actually names it "East of Pukey Point (**yellowtail** & rockfish)" — yellowtail listed first.

---

## 5. Gear (protocol step 4)

You didn't give me a profile, so these are **class terms** (`tackle/gear-classes.md`) with the Coronados-specific numbers from `species/yellowtail-coronado-islands.md`. Rig all three yellowtail outfits before the day starts — surface iron, yo-yo/dropper, flyline — because the faces flip by the hour (`species/yellowtail.md`).

| Outfit | Class build | Coronados numbers |
| --- | --- | --- |
| **Troll/search** | Flyline outfit tows a 20–30 ft diver; 6–7 ft diver-troll outfit (~6 ft, H, E-glass, 30–80 lb) for 40 ft divers (`HTowqnwAMeA`) | Halco 190-class deep divers, **pink and purple** |
| **Surface iron** | Jig-stick class: 8–10 ft, casts 2–4 oz, ~25–60 lb; ~65 lb braid backing to **fresh 40–50 lb mono top shot** (`D5DR7Kx42_A`) | **40 lb is the local full-day-island top-shot bracket** (`LTCFjqtSI8g`); Tady 45 / JRI Stinger-class swim jigs; step up to a **Salas 7X-class** heavy iron in wind to punch the cast |
| **Yo-yo iron** | 40–60 lb class stout rod (~8 ft, XH) + high-speed reel | Full-size **Salas 6X class** works the majority of the time. ⚠ The KB carries an unresolved internal conflict here: the zone guide and `species/yellowtail.md` size 6X vs 6X Jr **by current** (8 oz strong / 4 oz light) and flag that the source states neither weight; `techniques/yo-yo-iron.md` puts a 6X at **roughly 5–6 oz** and sizes **by depth** — 6X Jr at 60/80/100 ft, 6X at 120–150 ft, full-size at 150–250 ft. I'd fish the depth rule and carry both. Vertical/flat-fall change-up **100–180 g by current** is the one figure that verifies verbatim. Fish as heavy a line as you can still crank fast: **40 lb works, 50 better, 60 better still** (`5pbA-wXoric`, `UP_3fBu7VPA`) |
| **Flyline** | 20–30 lb class, **8–9 ft**, rated 20–40 or 20–50 lb — backbone to turn a fish off the rocks (`D5DR7Kx42_A`) | Hook size follows bait size: **1/0–2/0 baseline**; downsize to J hooks **sizes 1, 2 and 4** on fluoro when they're picky (`F9XjGMEvvag`); 2/0–4/0 with bigger baits |
| **Dropper loop** | Same 40–60 lb outfit as the yo-yo | Live bait to bottom marks when they hold down (`D5DR7Kx42_A`, `HTowqnwAMeA`); good rod-holder soak while your hands are on a jig |
| **Sabiki** | — | ~100 ft, **8 oz** sinker (cameron) |

**Iron colour:** the zone guide lists scrambled egg, bird shit, mint and blue/white as the yellowtail colours — and the KB flags this as contradicted-internal: `techniques/surface-iron-color.md` holds **no yellowtail colour doctrine**, ranks colour **last** (swim → size/weight → colour), and records that "colour doesn't matter" is itself a yellowtail saying. Don't burn planning energy on colour; burn it on swim and on the cast.

**Leave the heavy tuna gear home.** A casting reel (Lexa / Fathom / Tranx class) — or a spinning rod for anyone new to conventional gear — throws yellowtail lures better than heavy tuna outfits and makes a better day (`QEmxUIGmKbo`).

---

## 6. Fish care — matters more on a two-day trip

`fish-care/dorado-and-general.md`: build a **salted slurry** — roughly **2 cups rock salt per 7–10 lb bag of ice**, plus a splash of seawater to wet it; the salt is what drops the mix below freezing. Keep fish cold and out of the sun, **never rinse in fresh water** (salt water for every rinse), and if the drive home is more than ~10 minutes, bring a **car cooler** so fillets have somewhere cold to go. The KB gives no ice budget for a two-day private-boat trip; the only figure it holds is a profile one — **100–125 lb of ice per trip** on a 22 ft panga (`profiles/cameron/boat.md`).

---

## 7. Before you commit — the questions the KB says to ask you

`planning/day-plan-protocol.md` step 1b requires the boat's `range_nm` and `sea_state_max_ft` against the day's forecast, and says to **ask** when they aren't on file. The one profile in this KB (`profiles/cameron/boat.md`) has both fields explicitly **null** — "Cameron has not stated these — left null rather than guessed. Until they are filled, the protocol must ASK." So:

1. **What's your range and your sea-state limit?** 14–15 nm each way is a short run, but the 12 kt afternoon plus the homebound-wind rule is what decides whether you fish until 2 p.m. or turn at noon.
2. **Where are you launching?** The distances above are all from the **San Diego bay entrance / Zuniga Jetty (32°40.300'N 117°13.400'W)**. From Mission Bay (Dana Landing) it's a longer run and the KB doesn't measure it.
3. **What do you own?** The protocol's rule is **never recommend gear you haven't said you own**, and to **name the gap** when a class the plan calls for isn't in your box — e.g. if there's no 40–60 lb high-speed yo-yo outfit, the tight-ball-on-structure situation has no answer and you'd be casting iron at fish that are 40 ft under it.

---

## What this KB could not tell you

Listed so you can fill them elsewhere rather than assume I covered them:

- **The vessel-side Mexican paperwork** — whether an FMM applies to a boat day-run that never lands, and what a private boat as opposed to a vehicle must carry. Flagged as a known gap on two separate pages.
- **Boarding and inspection practice** — what the Mexican Navy asks for and how to present papers. No source.
- **US customs / declaration for bringing fish back across.** No source.
- **Mexican (CONAPESCA) bag limits, size gauges and seasons** for every species on this trip. All recorded as "unknown, absent from the corpus."
- **An October Coronados program.** The only zone guide is spring-scoped; there is no October-specific content for this chain.
- **Anything about a multi-day trip at the Coronados** — overnighting, anchoring in Mexican water, or how day two should differ. The KB's only trip-length note is about booking sportboat trips, not private-boat two-day plans.
- **Depths and bottom composition** for every Coronados spot — every per-spot page is a minimum page with position only.
- **Numeric chlorophyll thresholds.** None exist in the KB, so I can't tell you whether 0.9 is good or bad water.
- **A yellowtail SST band.** Flagged gap; the corpus gives directional water-state reads only.
- **Quarter-moon doctrine, and moon-phase effect on yellowtail.** Both flagged gaps.
- **The anchor-vs-drift commit call at the Coronados** — when to drop the hook on a mark versus keep working the circuit. Flagged gap.
- **What flips Coronados fish from seeing to eating**, and any zone-specific gray-light read. Flagged gap.
- **Zone-specific bonito behaviour at the Coronados.** Flagged gap.
- **The swell-vs-current opposition check** — you gave no current, and the KB requires the current vector to degrade the sea-state forecast properly.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/report-reading-and-forecasting.md`, `planning/trip-length-selection.md`, `locations/coronado-islands.md`, `locations/mexican-waters.md`, `locations/us-waters.md`, `locations/regions.md`, `locations/middle-grounds.md`, `locations/pukey-point.md`, `locations/rockpile.md`, `locations/ribbon-kelp.md`, `locations/5-minute-kelp.md`, `locations/south-kelp-ridge.md`, `locations/lighthouse.md`, `locations/east-of-pukey-point.md`, `locations/north-of-north-island-rockfish-area.md`, `locations/coronado-canyon.md`, `locations/lower-9-mile-bank.md`, `species/yellowtail.md`, `species/yellowtail-coronado-islands.md`, `species/calico-bass.md`, `species/bonito.md`, `species/barracuda.md`, `species/rockfish-lingcod.md`, `species/ocean-whitefish.md`, `species/sheephead.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `seasonal/october.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/water-regimes.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/sea-state.md`, `conditions/current-diagnostics.md`, `conditions/bird-reading.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `techniques/slow-trolling-bait.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `fish-care/dorado-and-general.md`, `sources/regulatory-claims.md`, `profiles/cameron/boat.md`, `species/README.md`  
*videos:* `D5DR7Kx42_A`, `HTowqnwAMeA`, `YZtX1MiT0y8`, `ejUTAnONf7o`, `VpW91AKOFVQ`, `4pT0efBD1j0`, `dS9gd9k7A7Q`, `gdqI2dNd5_U`, `F9XjGMEvvag`, `LTCFjqtSI8g`, `P36VGPPf120`, `OYOda6T3f-8`, `XLVUhV8DW64`, `SczdZIq3UmE`, `E4vKwRaRueA`, `zKmZ4zql2ws`, `NC3-3pJDEgo`, `HzE4FHHcvTk`, `DnSqw4r7A1s`, `Blh2BA-7Ono`, `6TBxHnkYXI0`, `9tTM99InluM`, `fri_BWI-VA0`, `LqW32NSkObY`, `5p6gu14ZC4w`, `fDSd9kqwYW0`, `_r_qKX_7080`, `tpmOYXYQwhU`, `6DzbsElGE7E`, `8XIy7hPsFkQ`, `5pbA-wXoric`, `ETw_3AFxEcM`, `RNRFrfepiW0`, `UP_3fBu7VPA`, `HnqiE05vdXs`, `BskCsKaTiZw`, `7WapaxdtjQg`, `bM2vUS1B-yQ`, `ztpj1Xll0-U`, `Zo92MG459gQ`, `d0yGBQDeY_4`, `0DKmYId1NN4`, `KjVLn4cWHbc`, `QP6c8vcslVs`, `JiJYamo0QHk`, `HWx1jDTGsng`, `h3PTupup17I`, `Ec2GaNpiOHI`, `yn1suHH6b1Y`, `QEmxUIGmKbo`, `YIABTTYXeqc`, `Klfb433I3Uk`, `0KQ--N5TjqE`, `46ha7J1Fc6A`, `HueC1KHrcVw`, `5to3Q5P7w90`, `A6DJoXbID4c`, `91ZJbhAnzMg`  
*gaps admitted:* Whether a private boat day-run into Mexican water requires an FMM when it never lands, and what a boat as opposed to a vehicle must carry — flagged as a no-corpus-source gap on both locations/mexican-waters.md and species/yellowtail-coronado-islands.md. | Mexican boarding and inspection practice — what the Mexican Navy asks for and how paperwork should be presented. No corpus source. | US customs declaration, transport and limits for bringing fish home across the border. No corpus source. | Mexican (CONAPESCA) bag limits, size gauges and seasons for yellowtail, rockfish/lingcod, ocean whitefish, sheephead and the tunas — all recorded as unknown/absent in sources/regulatory-claims.md. | No October-specific Coronado Islands program exists; the only zone guide (species/yellowtail-coronado-islands.md) is season-scoped to spring (warming transition). | No content on a multi-day or overnight Coronados trip — overnighting, anchoring in Mexican water, or how day two should differ from day one. planning/trip-length-selection.md covers booking sportboat trip lengths only. | Depth bands and bottom composition for every Coronados spot — Rockpile, Ribbon Kelp, 5-Minute Kelp, South Kelp Ridge, Lighthouse, East of Pukey Point, North of North Island, Coronado Canyon and Lower 9 Mile Bank are all minimum pages carrying position and parent zone only. | No numeric chlorophyll thresholds anywhere in the KB, so the given 0.9 reading cannot be graded good or bad — only the qualitative new-bloom-vs-mature-bloom-edge freshness read applies. | No SST band for yellowtail — species/yellowtail.md flags the numeric bands as a gap and gives directional water-state reads only. | No quarter-moon bite doctrine; the KB's only documented moon windows are full/new +/- 1 week. Moon-phase effect on yellowtail specifically is a flagged gap. | The anchor-versus-drift commit call at the Coronados — when to drop the hook on a mark versus keep working the circuit. Flagged gap. | Mechanism for what flips Coronados fish from seeing to eating, and any zone-specific gray-light read. Flagged gap. | Zone-specific bonito behaviour at the Coronados. Flagged gap on locations/coronado-islands.md. | No overnight-displacement figure for structure-holding island fish; the 10-15 nm overnight number is scoped to open-water bluefin not holding structure, so day-two search-box sizing has no KB number. | The sea-state current-vs-swell opposition check could not be run — no current vector was given, and conditions/sea-state.md requires it to degrade the swell forecast. | Distances are measured from the San Diego bay entrance / Zuniga Jetty; the KB gives no run distance to the Coronados from Mission Bay or other launch points. | The one profile in the KB (profiles/cameron/boat.md) has range_nm and sea_state_max_ft explicitly null, so the boat envelope could not be resolved and the protocol requires asking.

</details>

### 4. [trip] I am thinking about an overnight run to Tanner Bank / Cortez Bank for bluefin. Go or no-go? Describe the run, …

**Winner:** NOW · mapping {'A': 'B3', 'B': 'NOW', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three reach the same correct no-go on the same sea-state doctrine (12 kt cutoff, sub-10 s flag, the 12-15 kt / 4-8 ft / 9 s combo), the same post-full-moon slow-morning read, and the same null boat envelope, so the separation is in the second half of the question — describing the run and what is out there. B wins because it was clearly working from a real zone page: a port-by-port distance table, a shallowest-first depth-band table from the anchor shallows through 50-80 fathom night marks, the 300 g-to-500 g night jig floor over 80 lb braid and 130 lb leader, the 9pm-midnight / 3:30am clock, the fleet-positioning problem, and the hook-size-versus-line-class conflict presented with a decision frame — while also being the only answer to pass through its own KB's fact-check flags (the 'anchored bluefin bite' reading on camera as a yellowtail bite, the one-boat sourcing, the unverified Cow Cod boundary). C is a close second and is the most actionable on the run itself, since it is the only one to convert the trip to nautical miles and to notice that Saturday's 8-15 kt wind is exactly the kite window Cameron's Fathom 80 is filed for; its only blemish is calling the two banks ~19 nm apart when its own coordinates give about 15.6. A is honest and well-cited but had no location material to work from and shows it: no nautical distance, no transit or bank-day timeline, no night clock, and an alternative plan it admits it cannot rank. No answer bluffed, fabricated, or stated a bare regulation — A asserts none, B and C both stamp jurisdiction, as-of and verify-current.

- *B2 reasons:* found: same core conditions/moon/seasonal spine plus species routers, zone-lexicon search-box sizing, kite and trolling notes, and spot-lists coordinates; no dedicated bank page but it says so implicitly by deriving position from sources/spot-lists.md. specific: computes the run itself (~94 nm Tanner, ~96 nm Cortes, ~36 nm the 43 from Mission Bay) and cross-checks against corpus statute figures; carries trolling-spread geometry (5 deg shotgun, 15 deg gunnel holders, ~3 ft tip elevation = 1 ft depth), 8-15 kt kite window, 13-15 kt Mad Mac troll, night windows and 50-80 fm marks vs the 30-50 fm general figure, 20-30 lb Cortez grade, 60 lb rocked yellowtail. sourced: note paths and ids (NC3-3pJDEgo, fri_BWI-VA0, i3qIAHW-SJc, vCskOx6N-XM, LsFMBCa9DOQ, xzIaUEDklrE, Rf1HKJG-SDg) generally match the claims. scoped: region correct; both regulatory claims stamped — two Pacific bluefin per person per day, California/CDFW, as of 2024-11, verify, and the rockfish closure as of 2020-12 with verify. honest: explicit closing section on what the KB could not tell it, no relative time, no invented chlorophyll scale or eclipse effect, flags the unreconciled bar-vs-Mad-Mac conflict rather than smoothing it. actionable: gives a concrete alternative (43 / below-Clemente as one 50-60 sq mi search box, dawn to early afternoon) and an 'if you go anyway' shape — troll bars to locate, kite in the 8-15 kt window, home before the noon build. Small slip: calls Tanner-Cortez separation ~19 nm where its own coordinates give about 15.6.
- *B3 reasons:* found: hit sea-state, moon, water-temp, seasonal and profile material and stated plainly that no location note exists for Tanner/Cortez/43, sourcing bank facts second-hand from species evidence. specific: real numbers throughout (12 kt / 9 s thresholds, 111 mi, 15-25 fm and 50-60 fm anchor bands, 60 ft chum marks, 30-41 lb grade, 25/40 lb flyline, #2 and No.4 circles, 250 g jig floor, chill times with 2 cups rock salt per bag). sourced: note paths plus video ids (NC3-3pJDEgo, UfuiWFVvz2E, ntQXxcH5sjI, LsFMBCa9DOQ, nQvJnfb5jQ4, eL1Qm33-Mj0) that plausibly carry the claims. scoped: SoCal-Bight offshore-bank framing correct, no bare regulation asserted at all, region/waters context kept on parameters. honest: strongest gap list of the three, no relative time, refuses to grade chlorophyll 0.3, refuses to assume kite ownership or the null boat envelope, says the eclipse is uncovered. actionable: gates and gear gaps are usable, but it never converts the run to nautical miles or a transit estimate, gives no bank-day timeline or night clock, and explicitly cannot rank the inshore alternatives, so the 'describe the run' half is thinner.
- *NOW reasons:* found: worked from an actual zone page (locations/tanner-bank.md plus its evidence file, cortes-bank.md, 43.md) as well as sea-state, moon, bait-tank and profile notes, and named the flagged stub where a bluefin zone guide should be. specific: densest bank picture — distance table by port, depth-band table (shallows, ~120 ft high spot, 15-25 fm anchor, ~150 ft ridge, 50-60 fm edge, 50-80 fm night marks), 300 g jig floor stepping to 500 g in wind over 80 lb braid / 130 lb leader, night clock 9pm-midnight then 3:30am, 25 lb to No.2, 40 lb flyline floor, 20 lb fluoro to No.4/No.2, 20-40 lb 'Home Guard' yellowtail, 20-30 miles of fish, the 43 at 34.9 nm from the Point Loma Pipe. sourced: consistent per-claim video ids tied to the note that holds them. scoped: SoCal-Bight offshore bank correct; the two-fish bluefin limit carries California/CDFW + as of 2026-08 + verify, and it flags the Cow Cod Conservation Area boundary as unverified rather than guessing. honest: best-in-class — passes through its own KB's fact-check flags (the 'anchored bluefin bite' reads on camera as a yellowtail bite, the 100 lb-plus claim comes from a promo intro, most sources are one boat), refuses to grade chlorophyll, refuses the eclipse, notes distances are statute with nm unknown. actionable: a reader gets the trip shape (overnight run, anchor, yellowtail to ~noon, deep search at night), the current-gates-the-bite rule, the hook-vs-line-class conflict with a decision frame, four named gear gaps including the 0-300 ft sounder window versus 300-480 ft marks, and two in-envelope alternatives.

<details><summary>Full prompt</summary>

I am thinking about an overnight run to Tanner Bank / Cortez Bank for bluefin. Go or no-go? Describe the run, and what to expect out there. Assume these conditions and do NOT fetch live data: Friday night into Saturday, 2026-08-28/29. SST: Tanner Bank 69.4 F, Cortez Bank 69.9 F, 43 Fathom Spot 68.2 F. Chlorophyll 0.3 offshore. Wind: NW 15-20 kt Friday, easing to NW 8-12 kt at Saturday dawn, building to 15 kt by noon. Swell: NW 5 ft at 9 s Friday, NW 4 ft at 9 s Saturday. Moon: full on 08-28 with a partial lunar eclipse that night. No Small Craft Advisory for Saturday morning. Use the angler profile in profiles/cameron/ (boat.md, rods.md, tackle.md, trolling-lures.md, spots.md) and respect the boat envelope.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

# Tanner / Cortez overnight, Fri 2026-08-28 → Sat 08-29 — **NO-GO as scoped**

The fish argument is decent. The sea-state argument kills it, and the moon timing is the worst configuration of an otherwise good window. I'd not run a 22 ft single-outboard panga ~95 nm offshore on this forecast. Below is the full read, then what I'd do instead.

---

## 1. The sea state is the whole call

`conditions/sea-state.md` carries a working-captain go/bail threshold set (Capt. Dave Hansen, `NC3-3pJDEgo`, 2020-11-18 — registered voice, single-mention, so the note itself grades this **medium** pending repetition). Your numbers land on it almost exactly:

| KB threshold | Your forecast | Verdict |
|---|---|---|
| **Named unfishable combo: 12–15 kt wind with 4–8 ft swell at a 9-second interval** — "you can't go out there… you just cannot be caught out there," called dire **even for bigger boats**; he holds larger boats he runs at the dock in it | **Friday: NW 15–20 kt, NW 5 ft @ 9 s**. **Saturday noon: 15 kt, NW 4 ft @ 9 s** | Friday is past the wind end of the band with the swell inside it. Saturday noon *is* the combo |
| **Swell interval under 10 seconds is a hard bad-sea flag**, independent of height | **9 s both days** | Tripped, both days |
| Hansen's personal cutoff: **don't run when wind is over 12 kt**; above ~12 kt is what raises whitecaps | 15–20 Fri; 8–12 at Sat dawn, **15 by noon** | Only the Saturday dawn window sits at/under it |

Three more layers from the same note make the Saturday "window" worse than it reads:

- **Homebound wind (8/17/22).** Plan return timing **against** the afternoon build, not the outbound conditions. Your return leg is ~95 nm and the wind is building through it. That's the part that actually hurts.
- **Forecast error is asymmetric** (SoCal Bight Fishing Academy Ep. 6): assume the forecast errs on the worse side and that afternoon wind **strengthens rather than eases**. And if it's windier than forecast in the morning, assume it builds all day — **a small boat bails early** (7/14/22).
- **Current-vs-swell opposition.** Summer uphill countercurrent running *against* NW swell compresses the interval and stands the swell up: a forecast **4 ft @ 10 s fishes like 6 ft @ 7–8 s** when the current opposes. You gave me no current field and I'm not fetching one, so Saturday's 4 ft @ 9 s has unquantified downside, not upside.

**No Small Craft Advisory Saturday morning does not clear this.** The KB's threshold set is a captain's-call framing, not an NWS product — "weigher-of-risk responsibility sits with whoever is running the boat" (`NC3-3pJDEgo`).

### Your boat specifically (`profiles/cameron/boat.md`)

The Marquesas 22 is documented as: **2004 Panga Marine Marquesas 22, single 115 hp Yamaha, tops ~35 kt**; **no trim tabs — engine trim is the only attitude control**; foam-filled hull with **slight hull flex / "spring" on hard wave impacts**; **very small bilge**, bilge pump **manual-switch only, no float switch**; **no house battery** — the 30-gal bait tank and accessories run off the **single starting battery** (Group 24DC, 550 CCA / 140 min RC), with the NOCO GEN5X1 being an **AC-pigtail dock charger**. Trim routine needs **at least one person forward** on the bow bean bag underway, and the note says rough days forward are brutal — "rider catches air then hits the deck." Normal departure is **~8 am**; home waters are **Coronado Islands, La Jolla, San Diego offshore banks**.

That is a boat with no float-switch bilge, no redundant battery, and no attitude control beyond engine trim, being asked to sit overnight and then beat home ~95 nm into a building NW 15 with a 9-second interval. Every one of those is a documented fact in your own profile, not a guess.

---

## 2. The moon is working against a Friday-night/Saturday-morning trip

`conditions/moon.md` is unusually specific here, and the trip lands on the wrong side of it:

- Days **leading into** the full moon are the strongest documented bluefin windows (10/12/22 report). **08-28 is the full itself** — you're arriving as the leading days end.
- **The moon peak itself is a relocation event, not a bite-death.** Open-water bluefin not holding structure move **10–15 nm overnight** (7/21/22); Hansen puts it at **20 miles** after a full-moon night (`fri_BWI-VA0`, 2022-02-12) — the note keeps both figures side by side rather than averaging them.
- Hansen's dissent, kept side by side in the note: best window is **7 days before AND 7 days after** the full, with the **peak itself the travel period, not a bite period**; his overall take is the full moon "is not good," softened by "I've seen a bite in a full moon also."
- The killer for your specific plan: **the morning after a full-moon night is typically slow** — "it hasn't been really located, or it's been feeding all night and doesn't have a tendency to feed real well right away" — with the bite **picking back up late in the day**. Hansen's explicit advice if you must fish a full moon: **fish it late rather than push the early-morning window** (`fri_BWI-VA0`).

Your plan is: fish the relocation night, then push the morning-after window, then leave before the late-day recovery because the wind is building. That's the one shape of trip the note argues against.

Also note the stacking: **spring tides fall on the full moon**, so the moon window is simultaneously a big-swing tide window (`conditions/moon.md`), and `conditions/tide-and-slack.md` says that when a bite is off-peak — **post-moon, pressured, or marginal conditions** — action **compresses into the tide windows** and you must anchor the plan to tide times and arrive **an hour before the change**. I have no tide table for 08-29 and I'm not fetching one, so I can't set those clock times for you.

**The partial lunar eclipse: the KB has nothing on eclipses at all.** I'm not going to invent an effect for it.

---

## 3. What the water says — the genuinely encouraging half

I want to be straight that the destination and the water are not the problem.

**SST.** `conditions/water-temperature.md` is emphatic that the value is **which side of a break** a species sits on, not the absolute number — bluefin sit the **cool side of a break when the surrounding water is warm, the warm side when it's cold** (10/20/22), and the **76 °F ceiling is soft, not hard** (bluefin observed foaming in 76 °F, 9/14/22). Against that:

- One captain's stated absolute preference, kept beside (not folded into) the break rule: bluefin move north with cooling water and want to hold in **70–72 °F**, contrasted on camera with 81 °F water fished the day before (`HueC1KHrcVw`, StokedOnFishing, 2016-08-08; unregistered channel — medium). **Tanner 69.4 / Cortez 69.9 sits right at the cool edge of that band.**
- A direct field parallel: Cortez Bank at **74–75 °F** produced yellowtail/yellowfin/skipjack, and the boat moved to **70 °F at the bank edge / 72 °F at the boat** at Osborn explicitly "chasing some cooler water" — and the early-graylight bite in that cooler water **was bluefin** (`i3qIAHW-SJc`, 2016-08-08; medium).

So 69.4–69.9 offshore is good bluefin water by the KB's own numbers. **But your three point SSTs do not give me a break.** Tanner→Cortez is 0.5 °F across ~19 nm — that's not an edge. The only gradient in your data is inshore-to-offshore: **the 43 at 68.2 vs the banks at 69.4–69.9**, which makes the outer banks the warm side of that gradient. `conditions/water-temperature.md` says to find breaks on a chart because **sharp offshore edges can jump multiple degrees in ~1 mi** — three pins can't do that job.

**Chlorophyll 0.3.** I have to flag this: **the KB never gives a numeric chlorophyll scale anywhere.** `conditions/water-color.md` treats chlorophyll as an **age and edge** question — a **new cold bloom is bad now, productive later**; a **mature bloom edge is the fishable water**; **bait holds in the dirtier water and predators work the dirty/clean seam**, and clean blue-water trolling found **nothing** because the bait wasn't there (8/17/22). Your own recorded doctrine is that in warm-water years you weight color at least as heavily as SST and **won't fish dirty green water**. A single flat "0.3 offshore" tells me the water is uniformly clean and gives me **no seam to fish** — which by this note is the thing that actually matters.

**Seasonal priors.** `seasonal/august.md` — regime **warm stable (peak)**, and August is **peak dispersal**: bluefin scatter Catalina to San Nicolas to Ventura, "showing up in weird places, gone the next day," **yesterday's spot is a weak prior**, and the **whole fleet shifts offshore so the islands lose coverage** (read that as coverage bias, not dead islands). `planning/report-reading-and-forecasting.md` adds the persistence-null rule and a post-weather one that matters directly: **"conditions rolled over — don't rely on your pre-fish"** after a weather event; re-scout, treat pre-event intel as expired regardless of age. Friday's 15–20 kt NW blow is that event.

**One genuine geographic point in favor of the destination:** `locations/bight-geography.md` says a big NW blow doesn't hit the Bight evenly — it **crushes the northern Channel Islands and the LA/Ventura shelf** (5–8 °F surface rollover) while the **Coronados, the tuna grounds, Catalina and San Clemente held their water through it** (4/21/22). So on a NW event, the southern/offshore banks are exactly where you'd want to be looking. The water logic points offshore; only the sea state and the platform say no.

---

## 4. The run, as it would actually be

Distances derived by arithmetic on the KB's own coordinates in `sources/spot-lists.md`, from the Mission Bay Park waypoints (~32°46.2′N / 117°16.1′W) that stand in for your Dana Landing launch:

| Destination | KB coordinates | Distance from Mission Bay |
|---|---|---|
| **Tanner Bank** | 32°42.000′N / 119°08.000′W | **≈ 94 nm** |
| **Cortes Bank** | 32°26.417′N / 119°07.833′W | **≈ 96 nm** |
| **43** | 32°39.333′N / 117°58.417′W | **≈ 36 nm** |

That cross-checks against the figures the notes themselves carry: Cortez is **~110–115 mi from San Diego** (`UfuiWFVvz2E`), given on camera elsewhere as **111 mi west of Point Loma, 96 mi SW of San Pedro, 47 mi SW of San Clemente Island** (`QSvzVHW9UMk`), and **~90 mi off Long Beach** for the El Dorado's annual trip (`nQvJnfb5jQ4`). Tanner is logged at **roughly 90–100 mi west of Long Beach** (`ntQXxcH5sjI`). Call it **~190 nm round trip minimum, before a single mile of searching.**

**The one small-boat precedent in the corpus** — and read the platform difference carefully: Captain Andrew's own **triple-outboard** boat ran a group **2.5–3 hours** to Tanner Bank (the crew called the return leg alone **over 100 mi**) and landed multiple **100 lb+** bluefin in a day, late October 2021 (`vCskOx6N-XM`, StokedOnFishing; unregistered channel — medium). His stated program is the template for a small-boat day out there and it's a good one: **troll spreader bars to cover ground while searching, then once the sounder is marking good numbers, stop trolling and set a dead flying fish under the kite to fish the drift over the marks** — trolling as the locate step, kiting as the close-and-convert step. Every other Tanner/Cortez trip in this KB is an 80–85 ft sportboat (El Dorado, Ranger 85, Constitution, Top Gun 80) on a 2.5–3 day charter.

I can't give you a transit time. **The KB has no sea-state-to-speed model for this hull** — only "tops ~35 kt, idles ~1.5 kt," and you are not running 35 kt into 5 ft @ 9 s with no trim tabs.

---

## 5. What to expect out there (if the weather were right)

**August at these banks is real, not a fall-only pattern.** `species/bluefin-tuna.md` puts the Tanner/Cortez condensation in the **Oct–Dec** window, but explicitly logs the mid-August data points **beside** it as "not a contradiction — different months, same bank":

- **Tanner, mid-Aug 2024:** boat anchored in **~120 ft** of water, bluefin taken on **bait marks sitting around 60 ft** while chumming sardines; yellowtail and bluefin both landed over two days (`ntQXxcH5sjI`).
- **Cortez/Tanner, mid-Aug 2024, Capt. Jake Hensley, Ranger 85:** fish arrived on the banks as a sudden switch the week before; distribution unusually wide — **"not very common to just drive through 20 to 30 miles of fish"**, a boat 15 miles away seeing the same thing rather than the usual isolated 4–5 sq mi patch — with **50 to 100 fish days**, anchor and drift both producing (`LsFMBCa9DOQ`).
- **Cortez, Aug 2024, El Dorado:** anchored alongside a **crowded fleet**; the crew repositioned onto the **50–60 fathom edge** of the drop-off next to the high spot and that line produced "right out the gate" (`nQvJnfb5jQ4`).
- **Cortez, Constitution:** anchor in **15–25 fathoms**, yellowtail sunup to ~11:00–noon, then move to deeper water to search bluefin through the night (`UfuiWFVvz2E`).

**Grade — expect it mixed and unpredictable on one size line.** The Tanner crew called the bank's core tackle challenge exactly that: **10 lb schoolies up to 80, "maybe even 100" lb** moving through together, "a total game" to match hook/leader/weight without going under-gunned (`947solNfiPw`, day-one grade opening ~30 lb, fish to 41 lb the previous day). Cortez ran **20–30 lb, about 25 lb average** on 20 lb fluoro to No. 4 and No. 2 hooks (`QSvzVHW9UMk`), while the **sundown bite the same trip produced multiple bluefin over 100 lb** on the kite and flyline fished alongside it, with a **180 lb** referenced to the northwest (`zBd1mayUt_I`). And `species/bluefin-tuna.md` is explicit that **bluefin gear does not get scaled down on a mixed tuna trip** — grade is unpredictable trip to trip, so tackle stays sized for the biggest fish that could show (`PrdPJy26H8c`).

**The night is the point of an overnight.** Same captain, same August, same banks: the night bluefin bite ran **two windows — roughly 9:00 pm to 11:00 pm/midnight, a lull, then about 3:30 am to sunrise** (`LsFMBCa9DOQ`; the note keeps this as one captain's clock-time read for that season, not moon doctrine). That first-night session started yo-yo/jig fishing around **1:00 am** and put roughly a **half dozen 30 lb-class fish** on the boat. On the meter, that overnight session read marks **360° around the boat, from 50 fathoms down to 80 fathoms, even below** — deeper than the general sounded-school figure of **30–50 fathoms** in wind with no surface sign (`HWx1jDTGsng`, Capt. Duane Diego Mellor), and deeper than the classic DSL night read of depth-called marks at **"fish at 180, fish at 230 ft"** you drop straight down onto (`nRFFM8DT-og`).

**Expect it to switch off without warning.** The Ranger 85 trip saw a large flat oceanic slick with fish breaking "everywhere" shut off **"like a light switch,"** and the crew could not relocate the school (`zBd1mayUt_I`).

**Expect a mixed bag, and expect the current to gate it.** Yellowtail bite together with the bluefin on flylined sardines at both banks — **"larger grade Cortez yellowtail," 20–40 lb**, marked at **60–80 ft in 120 ft of water**, worked on yo-yo jigs, surface irons, flylines and sinker rigs (`UfuiWFVvz2E`). Cortez yellows **"swim straight down" into the rocks** as a defense once hooked — one angler was **rocked on 60 lb** (`zBd1mayUt_I`). And a slack morning on the bank scratched until the current turned on, which is what finally produced a **five-hour yellowtail bite** (`fDSd9kqwYW0`) — the current-gates-the-bite pattern.

**Hooks/line the banks actually fish** (`species/bluefin-tuna.md`, `species/yellowtail.md`): **circle hooks for bluefin, J hooks for yellowtail**; flyline floor of **40 lb** for daytime bluefin (`UfuiWFVvz2E`); Cortez anchor bite on **25 lb mono/fluoro to a #2 circle** (`nQvJnfb5jQ4`) or **20 lb fluoro to No. 4 / No. 2** (`QSvzVHW9UMk`, with a caution that some No. 4s run light wire — prefer a stouter one); night knife-jig floor of **80 lb braid to 130 lb mono or fluoro** (`UfuiWFVvz2E`), with other sources putting night setups at **80–150 lb class** and leaders to 200 lb (`149px8WQ2Ng`, `RfiC8sfIWTk`).

**Regulation:** **two Pacific bluefin per person per day** (California/CDFW, as of 2024-11, stated on camera in `usHl-4SfqDA`) — **verify current regs before you fish.**

---

## 6. Gear resolution against your profile — and two holes

If you were going, here's how the profile resolves (`profiles/cameron/rods.md`, `tackle.md`, `trolling-lures.md`, `boat.md`, class terms per `tackle/gear-classes.md`):

- **Troll to locate:** Talica 25 (Phenix Axis 8'0" 3X-H 60–130, 100 lb braid — rail-rod class) and Fathom 80 (PCH-C-741XXXXH 7'4" 150–200 lb, ~1000 yd of 100 lb braid — trolling/spreader-bar class), plus the Trinidad 40; TLD 20 (Seeker 660H, 80 lb) for diver duty. **2–3 lures, no outriggers, furthest-back lure out of the elevated 5° shotgun behind the seat; divers in the 15° gunnel holders** — every ~3 ft of rod-tip elevation costs ~1 ft of running depth. Inventory covers it: three **Half Fish spreader bars**, **Madmacs 200 ×2 + 130**, **Halco LP190 XDD ×2**, **Husky Magnum 25 ×2 + 15**, **DTX 165**, two cedar plugs, skirts.
- **Which one:** per `species/bluefin-trolling.md` — **kite when the wind gives you 8–15 kt and the fish are big**; **speed-troll a full-size Mad Mac at 13–15 kt** when it's too light to kite **or the fish are too spread out to sit and kite over** (your own framing: a coverage need, not sea state); **spreader bar = the small presentation, Mad Mac = the large**, and **let forage size override the sea-state row** when they disagree. Note the flagged conflict the KB keeps unreconciled: one crew read the **bar as pulling the bigger fish** out of a mixed 40–100 lb school while the Mad Mac produced more generally (`xzIaUEDklrE`) — opposite to the presentation-size axis, no forage size given to explain it.
- **The kite is the one thing Saturday's wind actually suits.** NW 8–12 at dawn building to 15 sits **inside the 8–15 kt kite window**, and the kite is documented as *the* most effective method for 100–300 lb fish. Your Fathom 80 is the designated kite rod (keep the 100 lb braid for capacity and less wind-blow, 200 lb leader, small boat can chase), you started kiting July 2026, and **helium is ruled out on the panga** (no room for a tank) — which per `techniques/kite-fishing.md` is a platform constraint, not a fishery rule.
- **Two real holes in the inventory for this specific trip:**
  1. **No knife jigs and no knife/speed-jig rod.** `tackle/gear-classes.md` lists the knife/speed-jig class as "Cameron shopping (open item)" and `profiles/cameron/rods.md` has the dedicated SPJ/speed-jig setup as an open item. **The night program at these banks — 50–80 fathom marks, 9 pm–midnight and 3:30 am–sunrise — is a knife-jig game you are not currently equipped for.** Your Trinidad 40 with the Salas 6X / CP 105 covers the *shallow* row (yo-yo iron on ~60 ft bait-ball marks around the boat while chumming, where a heavy bite reads as the rod going dead-weight, "almost like stuck on the bottom" — `ntQXxcH5sjI`), not 50–80 fathoms.
  2. **The kite needs a flying fish.** The KB documents the harness, the balloon-to-kite rigging from Tanner (`vCskOx6N-XM`), and the wind window — but says nothing about whether you have flyers aboard or a source for them.
- **If foamers show:** Talica 25 is the rod the profile names for a jumbo **80–140 lb** foamer school; your own program is **run-and-gun at working terns, ~2–3 casts per school, smaller presentation (Colt-Sniper class) has out-fished bigger, timed around slack tide**. Wait for the **"jacuzzi" (solid circular whitewater) ≈ a bite every cast**; spread-out directional feeders are picky (`seasonal/august.md`, `techniques/foamer-casting.md`). Ghost Popper 150, Ghost TP 140/160, Zakana 100g, Slidekick 120g cover it.
- **Bait:** 30-gal tank, Rule 401 500 GPH pump — and the electrical note above is a trip-limiting fact, not a footnote.

---

## 7. What I'd do instead

**Option A — a short-window day trip to the 43 / the below-Clemente complex, dawn to early afternoon.**

`locations/zone-lexicon.md`: the **below-Clemente complex — 43, 181, 182, 289, Clemente Ridge up to Mackerel Bank — reads as one ~50–60 sq mi search box.** You do not "check 43"; you plan **hours of looking**, glassing and running contour between features. Your 68.2 °F reading is the inshore side of the only gradient you gave me, and `species/bluefin-tuna.md` explains why the 43 draws bluefin effort at all: it was the destination rockfish grounds for decades and now sits inside a closed rockfish area, so the effort that used to stop there for rockfish targets the same high spot for bluefin (California/CDFW, as-of 2020-12, `Rf1HKJG-SDg` — verify current regs).

From Mission Bay that's **~36 nm** by the KB's coordinates — roughly a third of the Tanner run, inside your documented home waters, and it lets you be off the water before the noon 15 kt build. The honest caveats: it's a **post-full-moon morning** (Hansen: slow early, better late — and you'd be leaving before "later"), and the 43's fathom-named high spot means **structure**, so the "open-water fish move 10–15 nm overnight" relocation rule bites less hard there than on a scattered offshore body.

**Option B — don't go, and hold the Tanner/Cortez run for a better forecast.** The banks are producing in August by the KB's own record, and `species/yellowtail.md` logs the sane way to time a Cortez run: the El Dorado picked Cortez as its destination on **inside intel from a couple of boats that had fished the bank a few days prior** (`oXunQKSbc2g`), not on a fixed schedule. The KB's own build-up timeline for that bite: fish held **outside the bank for close to a week**, then another **10 to 14 days** before they pushed in close enough to anchor on and fish at anchor (`eL1Qm33-Mj0`). That is a fishery you plan into with a fresh report and a flat forecast, not one you force on a 9-second interval.

**If you go anyway** (your boat, your call — `conditions/sea-state.md` puts that squarely on whoever is running it), the KB-consistent shape is: run in the Saturday dawn lull, **not Friday night**; troll bars to search and kite over the marks in the 8–15 kt window per `vCskOx6N-XM`; and turn for home well before the noon build, accepting that you're skipping both the night jig windows (which you're not equipped for anyway) and the late-day post-moon recovery Hansen says is the better half of a full-moon day.

---

## 8. What the KB could not tell me

Listed plainly so you know where I stopped rather than guessed — in particular, **your boat's fuel capacity and range are nowhere in this knowledgebase**, and that's the one number a ~190 nm round trip turns on.

**Notes I worked from:** `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `seasonal/august.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `species/yellowtail.md`, `techniques/kite-fishing.md`, `techniques/knife-jigging.md`, `planning/search-and-glassing.md`, `planning/report-reading-and-forecasting.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `tackle/gear-classes.md`, `sources/spot-lists.md`, and your five profile files.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/report-reading-and-forecasting.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `seasonal/august.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `species/yellowtail.md`, `techniques/kite-fishing.md`, `techniques/knife-jigging.md`, `techniques/fighting-big-bluefin.md`, `techniques/foamer-casting.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `tackle/gear-classes.md`, `bait/bait-tanks.md`, `sources/spot-lists.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`  
*videos:* `NC3-3pJDEgo`, `fri_BWI-VA0`, `HzE4FHHcvTk`, `CMQkHQMxbXM`, `HWx1jDTGsng`, `nRFFM8DT-og`, `PrdPJy26H8c`, `HueC1KHrcVw`, `i3qIAHW-SJc`, `Rf1HKJG-SDg`, `ntQXxcH5sjI`, `LsFMBCa9DOQ`, `QSvzVHW9UMk`, `zBd1mayUt_I`, `nQvJnfb5jQ4`, `eL1Qm33-Mj0`, `947solNfiPw`, `c3NFkQbdDy0`, `UfuiWFVvz2E`, `vCskOx6N-XM`, `xzIaUEDklrE`, `fDSd9kqwYW0`, `oXunQKSbc2g`, `usHl-4SfqDA`, `149px8WQ2Ng`, `RfiC8sfIWTk`, `cameron`  
*gaps admitted:* No fuel capacity or range figure for the Panga Marine Marquesas 22 anywhere in the KB — the single load-bearing number for a ~190 nm round-trip run to Tanner/Cortez. | No sea-state-to-speed or transit-time model for this hull; the KB gives only 'tops ~35 kt / idles ~1.5 kt' and one non-comparable triple-outboard data point (2.5–3 h to Tanner, vCskOx6N-XM), so I could not estimate a run time in 5 ft @ 9 s. | The KB has no doctrine on lunar eclipses at all — the partial eclipse on the night of 2026-08-28 cannot be assessed from these notes. | The KB gives no numeric chlorophyll interpretation scale (no mg/m³ thresholds anywhere); conditions/water-color.md treats chlorophyll only as bloom age and edge, so 'chlorophyll 0.3 offshore' cannot be graded good or bad, only noted as showing no seam. | No tide times for 2026-08-29 were supplied and the KB contains no tide table, so tide-and-slack.md's 'arrive an hour before the change' and off-peak window-compression rules could not be turned into clock times. | No guidance on running an overnight electrical budget offshore: the KB documents a single starting battery, no house battery, and a NOCO GEN5X1 AC-pigtail dock charger, but says nothing about powering the bait pump overnight ~95 nm from the dock or about engine/alternator charging. | No multi-day or overnight small-boat trip protocol (watch-keeping, sleeping offshore, night-running, offshore safety equipment) — planning/ is built as a day-trip surface. | No swell-exposure note for the Mission Bay entrance; Cameron's charted exposure work in conditions/sea-state.md covers the San Diego Bay entrance only (open to roughly 160°–186°). | No record of whether Cameron owns or can source flying fish for the kite program, despite the kite being the method the Saturday 8–15 kt wind window suits. | No ground-tackle inventory for the panga (rode length, chain-and-rope makeup, anchor size), so the Cortez/Tanner anchor programs at 15–25 fathoms and 50–60 fathoms could not be checked against what the boat actually carries. | No current field, break map, 12–24 h wind hindcast, or 48–72 h upstream-fetch scan was supplied, all of which conditions/sea-state.md and water-temperature.md require on every conditions pull; three point SSTs cannot resolve the break-side rule.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

# Tanner / Cortez overnight, 8/28–29/26 — **No-go on the panga.**

Not a "conditions are marginal, use judgment" no-go. Two independent things in the KB block it, and only one of them is weather.

---

## 1. The weather is the KB's named unfishable combo

`conditions/sea-state.md` carries the only explicit go/bail thresholds in this knowledgebase — Capt. Dave Hansen's, from `NC3-3pJDEgo` (2020-11-18). All three of his flags trip on your numbers:

| Hansen's rule | Your forecast |
| --- | --- |
| Personal cutoff: **don't run when wind is over ~12 kt**; above ~12 kt is what raises whitecaps | NW **15–20 kt** Friday night; back to **15 kt by noon** Saturday |
| **Swell interval under 10 seconds is a hard bad-sea flag** — "absolutely horrible," independent of height | **9 s** both days |
| Named unfishable combo: **12–15 kt wind with 4–8 ft swell at a 9-second interval** — "you can't go out there… you just cannot be caught out there" | Friday **15–20 kt / 5 ft @ 9 s**; Saturday midday **15 kt / 4 ft @ 9 s** |

He states he holds *larger* boats he runs at the dock in that combo, not just small ones. Your Friday run-out is above it and your Saturday return leg lands square in it. The KB is flagged `medium` confidence on this specific threshold set (single-mention, not yet repeated in the corpus) — but it is the only stated threshold the KB has, and it names your exact numbers.

Three more layers from the same note push the same way:

- **Steepness / current-vs-swell opposition.** Summer uphill countercurrent running against NW swell compresses the interval and stands the swell up: a **4 ft @ 10 s fishes like 6 ft @ 7–8 s** when the current opposes. You are starting at 9 s, not 10, so degrade from there. NWS/point forecasts do not show this.
- **Forecast error is asymmetric** (Landesfeind, Ep. 6). Assume the forecast errs on the worse side, and that afternoon W at the islands *strengthens* rather than eases. "If it is windier than forecast in the morning, assume it builds all day — a small boat bails early" (7/14/22).
- **Homebound wind.** Plan return timing *against* the afternoon build, not off the outbound conditions (8/17/22). Your build to 15 kt by noon is exactly when you'd be 100+ miles from the barn.

No SCA for Saturday morning does not clear this. The advisory threshold and Hansen's 12 kt / sub-10 s thresholds are different bars.

## 2. Your boat's envelope is not defined in the KB — and the run is ~111 mi each way

`planning/day-plan-protocol.md` step 1b makes the envelope binding *before* any species note gets opened. `profiles/cameron/boat.md` carries this machine block:

```
home_port: null
range_nm: null
sea_state_max_ft: null
```

with an explicit comment: *"Cameron has not stated these — left null rather than guessed. Until they are filled, the protocol must ASK for range and sea-state instead of assuming one."* So I cannot clear this run against your envelope; I have to ask.

What the KB does give on distance, from the boats that actually do this trip:

- **Cortez Bank: ~110–115 mi from San Diego** (`species/yellowtail.md`, Constitution out of Fisherman's Landing, `UfuiWFVvz2E`) — and independently **111 mi west of Point Loma / San Diego, 96 mi SW of San Pedro, 47 mi SW of San Clemente Island** (`QSvzVHW9UMk`).
- **Tanner Bank: ~90–100 mi west of Long Beach**, fished in ~120 ft of water (`ntQXxcH5sjI`).
- Your own library has **Cortes Bank at 32 26.417 / 119 07.833** (`profiles/cameron/spots.md`).

That is a **~220+ mi round trip from Dana Landing** before you troll a foot, on a **2004 Panga Marine Marquesas 22 with a single 115 hp Yamaha** (`profiles/cameron/boat.md`). The notes on that platform that matter here, all stated facts:

- **Foam-filled hull, very small bilge; slight hull flex/"spring" on hard wave impacts** (noted July 2026). Bilge pump is **manual-switch only, no float switch** — nobody watches it while you sleep.
- **No trim tabs** — engine trim is your only attitude control in a 4–5 ft @ 9 s NW sea.
- **No AC / shore-power inlet, no house battery.** Bait tank runs off the **single Group 24DC starting battery** (550 CCA, 700 MCA, 140 min RC), with the NOCO GEN5X1 (12V/5A, hardwired **AC** pigtail) added to hold it up while the pump runs overnight. There is no AC 111 miles offshore, and the KB does not state an offshore overnight power budget for that pump on the start battery.
- **One engine.** The KB has no single-engine offshore doctrine at all, and no fuel-burn or range figure for this boat.

Sportboats do this run overnight *because* they are 80–85 ft boats with crew watches. Every Tanner/Cortez trip in the corpus is one: Constitution (80–85 ft), El Dorado (85 ft), Ranger 85, Top Gun 80.

## 3. The moon is working against a 220-mile bet, not for it

Full moon **on 8/28** with the trip fished 8/28–29. `conditions/moon.md`:

- The strongest documented bluefin window is the **days leading into** the full moon (10/12/22) — you'd be arriving at the peak, not inside the lead-up.
- **The moon peak itself is a relocation event.** Open-water bluefin not holding structure move **10–15 nm overnight** (7/21/22); Hansen puts it at **20 miles** after a full-moon night and names bluefin specifically (`fri_BWI-VA0`). Both figures are kept side by side, not averaged. Any position you are running 111 miles at is stale by Saturday dawn.
- **Hansen's dissent, directly on your morning:** the full moon itself "is not good"; the morning *after* a full-moon night is typically slow — the fish "has been feeding all night and doesn't have a tendency to feed real well right away" — with the bite **picking back up late in the day**. His stated rule: if you must fish a full moon, **fish it late rather than push the early-morning window.** That is the opposite of an overnight-run-fish-dawn-run-home plan.

**The honest counterweight, kept side by side:** `seasonal/june-july.md` and the bluefin router both say **full moons drive the bluefin *night* bite**, and the Tanner/Cortez pattern in the corpus is night-dominant. A full moon is a *night-jig* argument — which is the one program you're not equipped for (see §5).

**The eclipse: the KB says nothing about lunar eclipses.** No note in this repository covers them. I'm not guessing.

## 4. The water read — temperature is the one thing not arguing against you

- All three readings sit **below** the captain-stated preferred band of **70–72 °F** for bluefin (`HueC1KHrcVw`, dockside, fish moving with cooling water) and nowhere near the **76 °F soft ceiling** (9/14/22, `conditions/water-temperature.md`). Temperature is not a reason to skip the banks. For scale, a Cortez Bank trip in the corpus fished **74–75 °F** for a mixed bite (`i3qIAHW-SJc`).
- Your **1.2–1.7 °F gradient** (Cortez 69.9 / Tanner 69.4 vs. the 43 at 68.2) is the interesting part. The bluefin rule is **relative, not absolute**: they sit the **cool side of a break when the surrounding water is warm, the warm side when it's cold** (10/20/22, `OYOda6T3f-8`). You'd have to see where the break actually lies on the water to call the side — three point values don't locate an edge.
- **Chlorophyll 0.3 tells me nothing here, and I won't pretend otherwise.** The KB has **no numeric chlorophyll bands anywhere.** What it has (`conditions/water-color.md`) is: chlorophyll has an *age* (new cold bloom = skip now, mature bloom edge = fish it); **fish the edge, not the middle of a mass**; bait holds in the *dirtier* water and predators work the seam. One offshore number with no map gives you no edge. Your own doctrine on file — in a warm-water year, weight color at least as heavily as SST and don't fish dirty green — can't be applied to a scalar.

## 5. If you went anyway: what's out there, and what you'd be missing

**The August Tanner/Cortez picture from the corpus** (all mid-August trips, all sportboats, all `medium` confidence / unregistered channel):

- **Grade:** the working number is **30–40 lb**, with the tail long. Tanner sardine bite opened around **30 lb**, fish to **41 lb** the prior day (`947solNfiPw`); a **40 lb** fish at ~90 mi (`c3NFkQbdDy0`); the Ranger 85's first-night jig session put **a half dozen fish, 30 lb class** on the boat (`LsFMBCa9DOQ`). The crews' own framing of the challenge: **10 lb schoolies up to 80, "maybe even 100" lb** moving through together on one line class.
- **The programs that produce there:**
  - **Anchored, flylined sardines** — **25 lb mono or fluoro leader to a #2 circle hook** (`nQvJnfb5jQ4`); a **No. 4 circle, 40 lb** line/leader with a short piece of fluoro (`947solNfiPw`); the Constitution's floor was **40 lb flyline** for bluefin (`UfuiWFVvz2E`). Circle hooks for bluefin, J hooks for yellowtail.
  - **Boat position is the whole game on the bank:** the El Dorado repositioned onto the **50–60 fathom edge** of the drop-off off the high spot and got bit "right out the gate" (`nQvJnfb5jQ4`). The Constitution anchored in **15–25 fathoms** for the yellowtail leg (`UfuiWFVvz2E`).
  - **Night jig from ~1:00 am** — the Ranger 85 read marks **360° around the boat, 50 to 80 fathoms and even below** (`LsFMBCa9DOQ`) — deeper than the general 30–50 fathom sounded-school range (`HWx1jDTGsng`), kept side by side as a bank-specific extension.
  - **Shallow marks too:** Tanner produced bluefin on bait marks sitting around **60 ft** while the boat chummed sardines (`ntQXxcH5sjI`) — that's the yo-yo row, not the knife-jig row.
- **It's a mixed bag, not a bluefin-only bank.** Cortez/Tanner yellowtail bit **alongside** the bluefin on the same flylined sardines; the Constitution fished yellowtail sunup to ~11:00–noon, marking them **60–80 ft in 120 ft of water**, landing **20–40 lb** on flylines, surface irons and yo-yo irons. Caveat on file: **Cortez yellowtail "swim straight down" into the rock** once hooked on light line.
- **Build-up timeline, worth knowing before betting a run on a report:** on the 2024 Cortez trip the fish held **outside** the bank for "several days, close to a week," then another **10–14 days** before they pushed in close enough to anchor on and fish (`eL1Qm33-Mj0`). Banks turn on slowly and you can arrive early.
- **August priors argue against the banks being the prior at all.** `seasonal/august.md`: August is **peak dispersal** — bluefin scattered "Catalina to San Nicolas to Ventura, showing up in weird places, gone the next day," **yesterday's spot is a weak prior**. The "condense outward toward Tanner and Cortez" pattern in `locations/bight-geography.md` is a **fall** pattern (Oct–Dec). The mid-August Tanner/Cortez entries above sit *beside* that as evidence the banks can also produce outside the fall window — not as an August prior pointing there.

**Your gear gaps against that picture** (protocol step 4 — I don't recommend what you don't own, and I name the gap):

- **The single highest-percentage bank program — night knife-jigging deep marks — you have no gear for.** `profiles/cameron/tackle.md` lists no knife jigs or flat-falls, and `profiles/cameron/rods.md` carries "shopping a **dedicated SPJ / speed-jig setup**" as an open item. The class the KB calls for is a short parabolic **100–130 lb-braid jig rod (PE6–8)** with **150–400 g** jigs; a Turner's data point puts marks at **240–360 ft** and says the jig must be **250 g or greater** to get there quickly on a drifting boat (`eehDVb6_GoI`). You cannot fish the full-moon night bite with what's in the box.
- **Kite.** The KB's cow-fish doctrine is a flying fish under a kite at **8–15 kt** for **100–300 lb** fish. Your Fathom 80 is filed as the **"future kite rod"**, you started kite fishing July 2026, and helium is ruled out on the panga (no room for a tank). Whether you own a kite and a flying-fish harness today is **not stated in the profile** — I won't assume it.
- **Bait.** The KB's offshore floor is **at least three scoops** every time you run offshore, 40 miles or 100 (`9hEa3sGTh40`), with the same voice later saying he "wouldn't even go out without five" (`bM2vUS1B-yQ`). Your tank is **30 gallons**; Hansen runs **60 gallons on a 21 ft boat**. The KB gives no gallons-per-scoop conversion, so I can't tell you how short you are — only that a chum-and-flyline bank program is what the corpus fish bit, and that's the program a 30-gal tank is least able to sustain 111 miles out.
- **What you *could* fish, and it's real:** **yo-yo iron** on the ~60 ft chum marks — the Tanner row in `techniques/yo-yo-iron.md` names exactly that scenario — with the **Salas 6X** or **Salas CP 105** on the **Trinidad 40** (Rainshadow 8'0" XH 40–80 lb, 80 lb braid), which the profile already lists as your yo-yo/sinker-rig setup. A heavy bite on the drop reads as the rod going dead-weight, "almost like stuck on the bottom" (`ntQXxcH5sjI`). And **foamer casting** on the **Talica 25** (Phenix Axis 8'0" 3X-H 60–130 lb, 100 lb braid) — the rod your profile says you'd throw at an 80–140 lb school — with the **Ghost Popper 150**, **Zakana 100 g** or **Slidekick 120 g** as the small lead-bait class. One flag: your fall-2025 producers were **Colt Snipers** (`techniques/foamer-casting.md`), and none appear in the 7/23/26 inventory — check that box before any tuna trip.

## What I'd actually do with this weekend

Stay inside, and fish the water your own precedent says a panga fishes. `techniques/foamer-casting.md` has your **fall 2025 run-and-gun program — no bait, no tank** (you couldn't hold the big sardines and cutting the 30 gal saved weight on high-mileage days), **2–3 casts per school**, most fish on the smaller presentation, landed **25–40 lb**, with **80–140 lb schools seen**. That is the documented panga-scale bluefin program in this KB.

Where to point it, from the priors — **not from conditions, because you gave me three offshore SST points and nothing inshore, so I can't rank these**:

- `seasonal/august.md`: the **paddy program peaks in August**; best paddy water is **south of SCI/Catalina and from Dana Point to Oceanside southward**, scarcer and less holding north of Dana Point.
- `locations/bight-geography.md`: in a NW event, **south of Newport is "less prone to wind-wave-driven rollovers,"** and the **Coronados, the tuna grounds, Catalina and San Clemente held their water** through a big NW blow. Your NW 15–20 is exactly that geography.
- `conditions/tide-and-slack.md`: your own foamer timing is **slack** (bait rises, foamers start), and you want to be **on the zone an hour before the change** — but you gave me no tide times, so I can't put clocks on it. Note also that a full moon is a **spring tide**: big swings stacked on the moon window.
- `conditions/moon.md` + Hansen: on a full-moon day, **fish it late**, don't burn the plan on the early window.

Sounder note for a rough day, either way: in **choppy/rolly conditions the cone gets shot lower**, so fish holding high in the column **won't paint until you're right on top of them** — the same fish that would show from a distance on a calm day (`fgTmUq78ofQ`). Expect to under-read shallow fish Saturday; that's the sea, not the Garmin 840xs.

## What would flip this to a go

1. **Fill in `boat.md`'s `range_nm` and `sea_state_max_ft`.** Until those exist, the protocol says ask, and I'm asking. A 220+ mi round trip on one 115 hp outboard needs a fuel number the KB doesn't have.
2. **A window that clears Hansen's bar** — under ~12 kt and **10 s or longer** interval, on both legs, with the 12–24 h wind hindcast clean (a calm-morning forecast hides overnight wind).
3. **A jig setup and 150–400 g knife jigs**, so the night bite you'd be running 111 miles for is actually fishable — plus confirmation you have kite and harness if the 100–300 lb row is the point.
4. **Buddy-boating.** Nothing in this KB gives doctrine on it, but every Tanner/Cortez trip in the corpus is an 80 ft boat with a crew. That's the honest comparison.

---

**Fish-care footnote if you ever do land one out there:** `fish-care/tuna-care.md` — bleed and gill-and-gut on the water, wet-towel cooldown, then a below-freezing slurry (**~2 cups rock salt per 7–10 lb bag of ice** plus a splash of seawater). Chill times: **30–40 lb ≈ 2 h**, **~100 lb ≈ 3–5 h**, **>100 lb overnight, re-iced**. Your 100–125 lb ice load covers a couple of 30–40 lb bank-grade fish; it does not core-chill a triple-digit fish, and the KB is explicit that a >100 lb fish will not chill through in an afternoon.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/tide-and-slack.md`, `conditions/deep-scattering-layer.md`, `seasonal/august.md`, `seasonal/september.md`, `seasonal/june-july.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `species/yellowtail.md`, `techniques/knife-jigging.md`, `techniques/kite-fishing.md`, `techniques/yo-yo-iron.md`, `techniques/foamer-casting.md`, `bait/bait-tanks.md`, `bait/making-bait.md`, `fish-care/tuna-care.md`, `locations/regions.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`, `config/endpoints.md`  
*videos:* `NC3-3pJDEgo`, `fri_BWI-VA0`, `UfuiWFVvz2E`, `ntQXxcH5sjI`, `nQvJnfb5jQ4`, `LsFMBCa9DOQ`, `QSvzVHW9UMk`, `eL1Qm33-Mj0`, `c3NFkQbdDy0`, `947solNfiPw`, `HueC1KHrcVw`, `i3qIAHW-SJc`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `HWx1jDTGsng`, `eehDVb6_GoI`, `fgTmUq78ofQ`, `9hEa3sGTh40`, `bM2vUS1B-yQ`, `m-M0iwX8DjA`, `nRFFM8DT-og`, `Rf1HKJG-SDg`, `sHnqSIOjTdM`, `r4J5nP5Bkl4`, `cameron`  
*gaps admitted:* No location note exists for Tanner Bank, Cortez Bank or the 43 Fathom Spot — locations/ holds universal structure knowledge only, so every bank-specific fact had to be pulled second-hand out of species notes' observation entries. | The KB has no numeric chlorophyll bands or thresholds anywhere, so the given value of 0.3 offshore cannot be scored; water-color.md only supports edge/age reasoning, which needs a gradient or map, not a single scalar. | profiles/cameron/boat.md leaves range_nm and sea_state_max_ft null and explicitly instructs the protocol to ASK rather than assume — so the KB cannot clear or reject a ~220+ mi round trip against a stated boat envelope. | No fuel-burn or cruising-range figure exists anywhere for the Panga Marquesas 22 / single 115 hp Yamaha. | The KB carries no small-boat or single-engine offshore-overnight doctrine at all — no guidance on running or lying-to overnight 100+ miles out in a 22 ft boat. | Nothing in the KB covers lunar eclipses; the partial eclipse on the night of 08-28 cannot be assessed from these notes. | No gallons-per-scoop conversion is given, so the 3-scoop (and 5-scoop) offshore bait floor cannot be checked against Cameron's 30-gallon tank. | The KB does not state how the bait pump is powered overnight away from AC: boat.md says no shore-power inlet and no house battery, yet the NOCO charger is described with an AC pigtail, and no offshore overnight power budget is given. | boat.md states the bilge pump is manual-switch only with no float switch, but the KB gives no doctrine on an unattended bilge during an overnight offshore stay. | Whether Cameron currently owns a kite and flying-fish harness is not stated — rods.md files the Fathom 80 as a 'future kite rod' while species/bluefin-tuna.md says he started kite fishing July 2026. | Cameron owns no knife jigs or flat-falls and no SPJ/speed-jig rod (open item in rods.md), so the KB's highest-percentage Tanner/Cortez program — the night deep-jig bite — has no owned-gear resolution. | No anchor or ground tackle is listed in Cameron's profile, though every documented bank program (15-25 fm yellowtail, 50-60 fm bluefin edge) is an anchored program. | No tide times were supplied and the KB holds no tide tables, so Cameron's own slack-tide foamer timing and the 'arrive an hour before the change' rule cannot be put on a clock for 08-29. | profiles/cameron/tackle.md (inventory complete 7/23/26) lists no Colt Snipers, although techniques/foamer-casting.md records them as his fall-2025 foamer producer — unresolved inventory discrepancy. | The KB gives no sea-state ceiling for speed-trolling: the Mad Mac 13-15 kt band is stated without any swell/wind limit above which that troll speed stops being viable. | No conditions were supplied for any inshore or island zone, so the in-envelope alternative program (paddies, Coronados, Catalina/SCI) is offered on priors only and its zones cannot be ranked.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Tanner / Cortez, Fri 2026-08-28 → Sat 08-29 — **No-go**

Not a close call. Two independent gates fail on the numbers you gave, and a third (moon timing) is against you. I'll give you the gates, then the picture of what's actually out there so you have it for a real window.

---

## Gate 1 — sea state. This is the one that ends it.

`conditions/sea-state.md` carries exactly one explicit go/bail rule set (`NC3-3pJDEgo`):

- **Wind above ~12 kt is what raises whitecaps, and 12 kt is the stated personal cutoff for not running.**
- **Swell interval under 10 seconds is a hard bad-sea flag** — sub-10 s is called "absolutely horrible," independent of height.
- **The named unfishable combo: 12–15 kt wind with 4–8 ft swell at a 9-second interval** — "you can't go out there… you just cannot be caught out there," described as dire **even for bigger boats**, with boats staying at the dock regardless of size.

Your numbers:

| | wind | swell | verdict |
| --- | --- | --- | --- |
| **Fri night (the crossing)** | NW 15–20 kt | NW 5 ft @ **9 s** | above the combo's wind band, inside its swell and period band — at night, ~110 miles out |
| **Sat dawn** | NW 8–12 kt | NW 4 ft @ **9 s** | at the 12 kt cutoff, sub-10 s flag active |
| **Sat noon** | NW **15 kt** | NW 4 ft @ **9 s** | **exactly the named combo: 12–15 kt / 4–8 ft / 9 s** |

You would be crossing in the worst of it and fishing into the combo. Three further layers from the same note all push the same direction:

- **Forecast error is asymmetric** — assume it errs on the worse side, and that afternoon W **strengthens** rather than eases (`zKmZ4zql2ws`). Plan "15 kt by noon" as more than 15, not less.
- **Current-vs-swell opposition.** Summer uphill counter-current running against NW swell compresses the interval and stands the swell up: **4 ft @ 10 s fishes like 6 ft @ 7–8 s**, and point forecasts do not show it (`zKmZ4zql2ws`). You gave me no current field, so I can't compute the degrade — but 4 ft @ 9 s is already *below* the input to that example.
- **No shelter, in any direction.** `locations/tanner-bank.md` is explicit: nothing out there is sheltered by land on any bearing, so the upstream fetch scan belongs in front of the run. Catalina Eddy shielding covers water **east** of Catalina and San Clemente (`S2L3KLSQ6Is`, cameron) — Tanner and Cortez are the last structure in the Bight before open ocean, i.e. the wrong side of that shadow entirely.

"No Small Craft Advisory Saturday morning" does not clear this. The KB's threshold is 12 kt and a sub-10-second interval, and you are above both by mid-morning.

## Gate 2 — the run, against your boat

What the corpus actually states for this run (`locations/tanner-bank.md`):

| from | to | stated run |
| --- | --- | --- |
| San Diego (Fisherman's Landing) | Cortez | **~110–115 mi**, "it's going to take us all night to get out there" (`UfuiWFVvz2E`) |
| Point Loma / San Diego | Cortez | **111 mi west** (`QSvzVHW9UMk`) |
| San Pedro | Cortez | 96 mi SW (`QSvzVHW9UMk`) |
| Long Beach | Tanner | ~90–100 mi west (`ntQXxcH5sjI`) |
| San Clemente Island | Cortez | 47 mi SW — the one figure the charts confirm at **40.8 nm** (cameron) |

Those are **statute** miles; the KB marks the run's nautical figure `unknown as a charted figure`. Read as one run to a two-bank complex 15.6 nm apart on a 179°/359° line: about 90 miles to Tanner, about 110 to Cortes.

**Every account of this water in the corpus is an overnight run or longer, from a big boat.** The one non-sportboat trip is a captain's own **triple-outboard** boat running 2.5–3 hours out to Tanner, the crew calling the return leg alone over 100 mi (`vCskOx6N-XM`).

Against `profiles/cameron/boat.md`:

- **2004 Panga Marine Marquesas 22, single 115 hp Yamaha.** Foam-filled hull with slight flex on hard wave impacts, **no trim tabs** — engine trim is your only attitude control. Your trim routine already assumes a rider forward on a bean bag, and the note says rough days forward are brutal (rider catches air, then hits the deck). That is a 220+ statute-mile round trip in a 9-second sea.
- **`range_nm: null`, `sea_state_max_ft: null`.** The protocol (step 1b, `planning/day-plan-protocol.md`) says that when the envelope is unfilled it must **ask** rather than assume — so the KB cannot arithmetically clear or condemn this run for you. Everything above is read off hull, power and battery facts, not off a stated envelope. Fill those two fields and this call gets mechanical.
- **Overnight power.** No AC/shore-power inlet, no house battery — the bait pump runs off the **single starting battery** (Group 24DC, 550 CCA, 140 min RC). The NOCO GEN5X1 that holds it up overnight is a **hardwired AC** charger. There is no AC 110 miles offshore.
- **Bait.** The bank program is a chum bite on sardines. The offshore floor is **at least three scoops** whether the run is 40–50 or 100 miles, five as the safer floor, with no topping off out there — and even a **360-gallon** tank carrying ~20 scoops runs dry some days (`9hEa3sGTh40`, `bM2vUS1B-yQ`, `bait/bait-tanks.md`). Your tank is **30 gallons**. You cannot chum a bank through a day and a night on that.

## Gate 3 — the moon puts you in the worst window of the cycle

Full moon **on 08-28**, and you'd fish the morning of the 29th.

- The **days leading into** the full moon are the strongest documented bluefin windows (`XLVUhV8DW64`). That window is 8/21–8/27. You're arriving after it.
- Capt. Dave Hansen's read: **the peak day itself is the travel period, not the bite period**, and he calls it "not good" — tempered by having seen bites land on a full moon (`fri_BWI-VA0`, `LEiyB9QNzHY`). **The morning after a full-moon night runs slow** — the school either hasn't relocated onto bait yet or fed all night — **with the bite rebuilding late in the day**. His guidance if a full-moon trip is unavoidable: **fish it late, don't push the early-morning window.**
- Your wind builds to 15 kt by noon. So the plan would have you pushing the exact window doctrine calls slow, then leaving before the rebuild.
- **Relocation.** Open-water bluefin not holding hard to structure move **10–15 nm overnight** (`Blh2BA-7Ono`); Hansen puts schools at **20 miles** after one full-moon night (`fri_BWI-VA0`). Kept side by side, not averaged. Any report you leave the dock on is stale — though note these fish at the banks are *on structure*, which is where that 10–15 nm figure explicitly doesn't apply.
- **Counter-doctrine, kept side by side:** one registered source states flatly there is no reliable moon pattern trip to trip (`shZCjX2-fkI`). The KB's decision frame (`species/bluefin-tuna.md`): use the moon as a **location/travel** input, not a bite input.

The KB has **nothing on lunar eclipses** — I'm not going to invent an effect for it.

---

## What the water is actually telling you (the frustrating part)

Your temperature field is not the problem. The sea is.

- **Tanner 69.4 / Cortez 69.9 = 0.5 °F across a 15.6 nm complex. There is no break out there in these numbers.** The bluefin rule is relative, not absolute — cool side of a break when the water is warm, warm side when it's cold (`OYOda6T3f-8`) — and it needs an edge to operate on. Without one, absolute numbers are the fallback and the corpus's numbers don't agree.
- The only gradient you gave me is **inshore**: the 43 at 68.2 °F, **1.2–1.7 °F cooler** than the banks.
- The one match in the corpus is encouraging for the band you have: bluefin held the cooler **70–72 °F** water at a bank edge while yellowtail and yellowfin sat in warmer water nearby (`i3qIAHW-SJc`). 69.4–69.9 sits just under that.
- For scale, the corpus's **only** Cortez water-temp record is **74–75 °F** on an August day one, which fished a mixed yellowtail/yellowfin/skipjack bite (`i3qIAHW-SJc`). You'd be arriving about 5 °F cooler than that.
- And the doctrine for a field with no differentiation: **across a big area with no temperature differentiation, the fish are most likely on structure like the banks** (`OYOda6T3f-8`). Which is to say the water read points at Tanner/Cortez. The sea state is what says no.

**Chlorophyll 0.3 — I can't grade that.** The KB carries no numeric chlorophyll scale anywhere, so 0.3 can't be called clean or green against any threshold in here. What the KB does say is that the read is a **seam, not a value**: chlorophyll has an age (a new cold-green bloom is bad now, a mature bloom **edge** is what you fish, `h3PTupup17I`), bait holds in the dirtier water while the pretty blue sits empty (`HzE4FHHcvTk`), and bluefin work the chalky dirty/clean transition because the dirty side holds the bait (`HWx1jDTGsng`). One offshore number with no field around it doesn't give you an edge to work.

**August is not the Tanner/Cortez window.** The bluefin router puts August at **peak dispersal — Catalina to San Nicolas to Ventura**, fish "showing up in weird places" and gone the next day, yesterday's spot a weak prior (`CMQkHQMxbXM`, `seasonal/august.md`). **October** is when the coast cools and fish condense outward to Tanner/Cortez. That said, `locations/tanner-bank.md` records mid-August producing repeatedly out there — with a caveat worth knowing: the KB flags that the "mid-August 2024 anchored bluefin bite" at Tanner (`ntQXxcH5sjI`) was on camera a *yellowtail* bite, with bluefin appearing day two "here and there."

---

## What it looks like out there, for when you do have a window

**The trip shape.** Overnight run, anchor, **yellowtail from sunup to roughly 11:00 a.m. or noon**, then move into deeper water and search bluefin through the night (`UfuiWFVvz2E`). Day-and-a-half charters fish the bank's bottom and yellowtail in one shot; two- and three-day trips add the night program.

**The depth bands, shallowest first:**

| band | what happens there |
| --- | --- |
| the shallows at the bank's far end, near a buoy | anchor for yellowtail (`fDSd9kqwYW0`) |
| **~120 ft** over the high spot | anchored at Tanner; yellowtail marked at **60–80 ft** in this water at Cortez (`ntQXxcH5sjI`, `UfuiWFVvz2E`) |
| **15–25 fathoms** | the Cortez anchor zone for the morning yellowtail program (`UfuiWFVvz2E`) |
| **~150 ft** on a ridge on the bank's edge | drift for reds (`fDSd9kqwYW0`) |
| **50–60 fathoms**, the drop-off edge | a repositioned boat found bluefin and yellowtail "right out the gate" (`nQvJnfb5jQ4`) |
| **50 fathoms down to 80, "even below"** | night jig marks, read 360° around the boat (`LsFMBCa9DOQ`) |

**Anchor and chum is the program, and current gates it.** Flyline with the current — hooked sardine, sardines running 6–8 in. A morning "missing the current" was spent scratching rockfish until it moved, after which a **five-hour yellowtail bite** closed the charter (`fDSd9kqwYW0`). Anchor isn't the only answer: one Cortez day produced on both a drift and an anchor job in ~50 fathoms, and when the anchor spot slowed the crew moved off to search rather than sit (`zBd1mayUt_I`).

**Expect a fleet.** Anchoring at Cortez in August meant picking a slot among "northern boats… southern boats… middle boats," private and commercial sportboats on the same structure (`nQvJnfb5jQ4`). Where the other boats sit relative to the high spot is itself a positioning input.

**The mixed grade is this zone's defining tackle problem.** At Tanner: "10 pounders all the way up to 80 pounders, maybe even 100" moving through on one size line, and matching hook, leader and weight without going under-gunned was called "a total game" (`947solNfiPw`). The corpus's answers sit side by side — **what they turn on is grade and bite quality, not order:**

- **Go down in hook size, not line class** — a 1/0 circle stepped to a No. 1 when bites aren't coming, because line too light to land the fish wastes the trip. The **Tanner data point** is the 2020 season: 40–60 lb bluefin where the smaller hook got bit better regardless of bait size (`shZCjX2-fkI`, registered channel).
- **Step the line up when the grade is up** — 100 lb line called easier for hooking the bigger fish being seen than 30 lb (`nQvJnfb5jQ4`).
- **What 40 lb costs on big fish:** on an evening "Sundowner" bite on the better grade, about **six hooked, one landed** on 40 lb with a tiny circle hook — "really tough" (`nQvJnfb5jQ4`).

**The daytime numbers, all from anchored or adrift bait fishing:** flyline **25 lb** mono or fluoro to a **No. 2** hook (`fDSd9kqwYW0`, `nQvJnfb5jQ4`); a **40 lb** flyline floor for daylight bluefin, droppable to 30 lb only if they're line-shy, with the caveat that Cortez yellowtail **"swim straight down"** into the rocks on lighter line (`UfuiWFVvz2E`); **20 lb** fluoro to No. 4 and No. 2 hooks on a 20–30 lb grade day, with a caution some No. 4s run light wire (`QSvzVHW9UMk`). **Circle hooks for bluefin, J hooks for yellowtail** as the trip-wide briefing (`UfuiWFVvz2E`) — against which one crew's stated preference for J hooks on a finicky bluefin bite is kept side by side (`LsFMBCa9DOQ`).

**The night program is a jig program, heavier than the general note's middle.** A **300 g floor**, 250 g only for anglers savvy enough to fish it, over **80 lb braid** and **130 lb mono or fluoro** (`UfuiWFVvz2E`); on a windy, hard-drifting night at Cortez/Tanner the standard **250–350 g** jigs would not hold the zone and the boat stepped up to **500 g** (`LsFMBCa9DOQ`). Colour called close to irrelevant — white-with-polka-dots if pressed. One captain's night clock: roughly **9:00 p.m.–11:00 p.m./midnight**, a lull, then **3:30 a.m. to sunrise** (`LsFMBCa9DOQ`) — single-source, one season, and the corpus's only clock-time night guidance for this water.

**Grades to expect in mid-August specifically:** opening grade around **30 lb**, fish to **41 lb** (`947solNfiPw`); a mixed bluefin-and-yellowtail bite at anchor with at least one bluefin called at 40 lb (`c3NFkQbdDy0`); roughly half a dozen **30 lb-class** fish on a 1:00 a.m. jig session (`LsFMBCa9DOQ`). Yellowtail are the bank's resident fishery — a larger **20–40 lb** grade, called "Home Guard" (`UfuiWFVvz2E`, `c3NFkQbdDy0`). Bottom stop when the bags fill or the current dies: reds, lingcod and a large grade of ocean whitefish (`fDSd9kqwYW0`, `Y1xeieQI3B4`).

**Two things worth internalizing about this water.** Fish take their time coming up onto the bank — one captain described the school holding outside for close to a week, with **10–14 days** elapsed before they pushed in close enough to anchor directly on the structure (`eL1Qm33-Mj0`). And when they're established, the distribution is unlike anything inshore: driving through **20–30 miles of fish**, with a boat **15 miles away** seeing the same thing, rather than the usual isolated **4–5 sq mi** patch (`LsFMBCa9DOQ`). Also expect it to end fast — a slick with fish breaking everywhere shut off "like a light switch" and could not be relocated (`zBd1mayUt_I`).

**Regulatory — California / CDFW, checked as of 2026-08, verify before you fish.** A **two-fish-per-person daily bluefin limit** is stated on camera at these banks (`947solNfiPw`). The KB flags that **no MPA or closure boundary is stated for either bank**, and that the Cow Cod Conservation Area is named as an offshore closure with no boundary given — so whether either bank falls inside it is **unverified**. Check the CCCA boundary against your position with CDFW/NOAA before you drop.

---

## Your gear against that program — four named gaps

Per protocol step 4, I only recommend what `profiles/cameron/` says you own, and I name the gaps rather than substitute.

**What you'd have covered:**
- **Flyline** — Avet MXJ / 9'0" Teramar (50 lb braid) top-shot to the bank's 25–40 lb window; Trinidad 40 / 8'0" XH 40–80 (80 lb braid) as the heavy stick when the grade is up.
- **Yo-yo iron** — **Salas 6X** and **Salas CP 105** on the Trinidad 40. This is the exact Tanner scenario: bluefin marked shallow around the boat while chumming with no foamer showing, answered with a **Salas 6X Jr dropped to ~80 ft with the bait marks sitting at ~60 ft**, 40 lb fluoro to 65 lb braid (`ntQXxcH5sjI`). Note the source names the **Jr**; you own the full-size 6X.
- **Surface iron** — Torium 20HG / 10'0" Phenix Abyss for boils and the "giant" bonito that come with them.
- **Poppers** — Ghost Popper 150, TP 140/160 for foamers.
- **Trolling to locate** — Talica 25 and Fathom 80, three Half Fish spreader bars, two Madmacs 200 + a 130, Halcos, Husky Magnums, DTX 165, cedar plugs. The private-boat Tanner program in the corpus is exactly this: **troll spreader bars to cover ground, then stop and fish once the sounder marks good numbers** (`vCskOx6N-XM`).

**The gaps:**

1. **The entire night jig program has no rod and no jig in your box.** The bank wants a **300 g floor over 80 lb braid and 130 lb mono/fluoro, stepping to 500 g in wind.** Your heaviest metal in `tackle.md` is the Nomad Slidekick **120 g** and the Zakana **100 g**; there are no knife jigs or flat-falls, and `rods.md` still logs the dedicated SPJ/speed-jig setup as an open item you're shopping. The night program is the main reason the multi-day boats go out there, and you'd be sitting it out.
2. **No kite.** The most effective method for **100–300 lb** SoCal bluefin is a flying fish under a kite (`YsiHziY_PWw`), and it's what the one private-boat Tanner trip converted on (`vCskOx6N-XM`). `rods.md` marks the Fathom 80 as a **future** kite rod — no kite, no flying-fish harness, no flying fish. On a bank whose grade runs to 80–100 lb, your big-fish converter isn't aboard.
3. **Bait budget** — 30 gallons against a chum-line fishery, covered above.
4. **Sounder depth.** Private-boat doctrine is a **manual 0–300 ft window**, on the stated reasoning that a private boat lacks the bait budget to chum fish up from depth; **fish below 300 ft are traveling, not biting** (`m-M0iwX8DjA`, `9hEa3sGTh40`, `8XrMkWPRxgs`). The bank's night marks run **50–80 fathoms (300–480 ft) and below** (`LsFMBCa9DOQ`) — past the top of that window on your Garmin GPSMAP 840xs. Same root cause as the bait gap.

---

## What Saturday could be instead

Honestly: **the KB's own thresholds say hold at the dock for any offshore run once you're at 12–15 kt over a 9-second sea**, not just for Tanner. And "if it's windier than forecast in the morning, assume it builds all day — a small boat bails early" (`DnSqw4r7A1s`). If you go, go short and go early.

Two things the KB supports, in envelope from Dana Landing:

- **Check the eddy state before writing off the inside.** The prevailing wind outside SoCal is from the north, so the islands shadow the water behind them and marks well to the south still sit in that shadow — the **425** is often shielded despite being far south of San Clemente (`S2L3KLSQ6Is`, cameron). Your 68.2 °F reading is at **the 43** (32°39.333'N 117°58.417'W) — **34.9 nm from the Point Loma Pipe, 31.2 nm from Widow Rock** — which is real bluefin ground: the rockfish closure moved the fleet's effort there onto the same high spot for tuna instead (`Rf1HKJG-SDg`), and it's the first-named member of the June–July below-Clemente search box. It's also the cool side of the only gradient in your data. But 35 nm out of Mission Bay in a building NW is still a long exposed leg, and the KB gives **no run figure from Mission Bay to anywhere out there**.
- **August is the paddy peak**, and the best paddy water is **south of San Clemente/Catalina and from Dana Point to Oceanside southward** (`HzE4FHHcvTk`, `seasonal/august.md`) — in your envelope, close to home. Expect a bigger overnight reshuffle after a moon-bright night: yesterday's dry paddy doesn't stay dry and yesterday's loaded one doesn't stay loaded (`conditions/moon.md`). Check each paddy fast — look, one sounder pass, one bait — and move rather than stake out. Plan the return leg against the afternoon W build (`HzE4FHHcvTk`).

And when you do point at Tanner: the doctrine window is **October–December**, the moon play is the **days leading into** the full, and the two things to fix first are a **300 g-capable jig outfit** and either a **kite** or a stated boat envelope that makes the run arguable at all.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `locations/tanner-bank.md`, `locations/evidence/tanner-bank.md`, `locations/cortes-bank.md`, `locations/43.md`, `locations/43-91-300.md`, `locations/north-9-mile-bank-178.md`, `locations/regions.md`, `species/bluefin-tuna.md`, `species/bluefin-tuna-trolling.md`, `seasonal/august.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/tide-and-slack.md`, `bait/bait-tanks.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`  
*videos:* `NC3-3pJDEgo`, `zKmZ4zql2ws`, `DnSqw4r7A1s`, `S2L3KLSQ6Is`, `UfuiWFVvz2E`, `QSvzVHW9UMk`, `nQvJnfb5jQ4`, `fDSd9kqwYW0`, `LsFMBCa9DOQ`, `ntQXxcH5sjI`, `947solNfiPw`, `c3NFkQbdDy0`, `zBd1mayUt_I`, `eL1Qm33-Mj0`, `Y1xeieQI3B4`, `i3qIAHW-SJc`, `OYOda6T3f-8`, `vCskOx6N-XM`, `shZCjX2-fkI`, `XLVUhV8DW64`, `fri_BWI-VA0`, `LEiyB9QNzHY`, `Blh2BA-7Ono`, `CMQkHQMxbXM`, `HzE4FHHcvTk`, `HWx1jDTGsng`, `5to3Q5P7w90`, `9hEa3sGTh40`, `bM2vUS1B-yQ`, `m-M0iwX8DjA`, `8XrMkWPRxgs`, `YsiHziY_PWw`, `z1CmWHqe9uk`, `Rf1HKJG-SDg`, `h3PTupup17I`, `oXunQKSbc2g`, `A6DJoXbID4c`  
*gaps admitted:* profiles/cameron/boat.md has range_nm: null and sea_state_max_ft: null — the KB cannot compute whether the panga can make this run; the protocol's step 1b says to ASK for those, so my read is inferred from hull/power/battery/bait facts, not from a stated envelope. | locations/tanner-bank.md flags no fuel figure and no sea-state envelope anywhere in the corpus for the Tanner/Cortez crossing itself. | locations/tanner-bank.md flags outright: no corpus source states a wind or swell number that turns this zone off. The go/no-go numbers I used come from the general conditions/sea-state.md note, and the KB itself flags them as single-source (one working captain, NC3-3pJDEgo). | No run is stated from Mission Bay / Dana Landing — or any Orange County port — to Tanner or Cortez. The corpus gives San Pedro, Point Loma/San Diego, Long Beach and San Clemente Island only. | The run is carried in statute miles only; locations/tanner-bank.md records distance_nm as 'unknown as a charted figure', so I have no nautical-mile or run-time figure for your boat. | The KB carries no numeric chlorophyll scale anywhere — 0.3 cannot be graded clean vs. green against any threshold in the knowledgebase. | The KB contains nothing on lunar eclipses; I have no basis to attribute any effect to the 08-28 partial eclipse. | No zone guide exists for bluefin at Cortez/Tanner — it is a flagged stub in both species/bluefin-tuna.md and locations/tanner-bank.md, with the material parked in the evidence file. | No MPA or closure boundary is stated for either bank, and whether the Cow Cod Conservation Area covers them is unverified in the KB. | locations/cortes-bank.md is a minimum page — position and parent zone only, with flagged gaps for structure, depth, species and how it fishes; everything I gave for Cortez comes from the zone page and its evidence file. | No swell or wind exposure data exists for the Mission Bay entrance — the KB carries the San Diego Bay entrance window (160 deg to 186 deg) only, and that is a different harbor from your launch. | No guidance anywhere in the KB on overnight house power at sea for a single-battery boat; the NOCO GEN5X1 in the profile is an AC-hardwired dock charger. | I have no tide table or slack times for 2026-08-28/29 and did not invent any — the KB is the pattern layer, and you supplied no tide data. | No corpus source places bluefin on the 9 Mile Bank (flagged stub in locations/north-9-mile-bank-178.md), so the nearest in-envelope bluefin ground with an actual corpus record is the 43. | Several claims on locations/tanner-bank.md that I relied on carry the KB's own fact-check flags — notably that the 'mid-August anchored bluefin bite' at Tanner (ntQXxcH5sjI) reads on camera as a yellowtail bite, that the sundown '100 lb-plus' window comes from a promo intro at an unnamed position, and that most of the zone's sources are one boat (the El Dorado out of Long Beach) rather than independent corroboration.

</details>

### 5. [trip] Can I fish for cabrilla out of San Diego this weekend in mid-September? Where would I go?

**Winner:** B3 · mapping {'A': 'NOW', 'B': 'B2', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 1 | **10** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three correctly refuse the premise — cabrilla is a Cortez fish and no version invented a San Diego spot — so the separation is in what they hand back instead. C wins narrowly because it answers 'where would I go' on both sides: three distinct cabrilla access modes with leg-by-leg drive times, per-person cost, panga rate and dated FMM/CONAPESCA paperwork, plus the BOLA season table showing mid-September is past prime even there, and then a SoCal program whose two regulatory figures each carry their own as-of date. A is essentially its equal and is the strongest on the San Diego side (named Point Loma/La Jolla pages with spot counts and working depths) and the most self-critical, flagging that its own cabrilla note mislabels San Felipe footage as BOLA. B is excellent on execution detail and unusually careful about the difference between 'no note places it here' and 'documented absence', but its KB version has no travel logistics at all, so its cabrilla answer resolves to 'see your profile's planned trip' rather than a fishery, and it recommends a Coronados run with Mexican licensing left in the gap list.

- *B2 reasons:* found: correctly reports zero SoCal cabrilla coverage and makes the sharp distinction that the KB never documents absence either (contrasting pacific-crevalle-jack) — but leans on front-matter-free prose rather than a region gate, and answers 'where' by pointing at the reader's own profile trip rather than the fishery. specific: strong on execution — 170/150 jerkbait sizes, 30–40 ft rise, 60–80 then 80–150 ft, Salas 6X/Tady 40, 30–40 cranks, 7'10"–8 ft 50 lb class, 6.5:1–7:1, 1/0 XS trebles, 71.6°F paddy. sourced: paths plus ids throughout (EmZO8QiOfik, dEPuDrhoClM, _Wb4z4ammoM, A6s-A1NARuA, E4vKwRaRueA). scoped: calico 14 in CDFW as of 2026-08 with verify and Cedros C&R correctly labeled an operator agreement with a report date, but the Coronados recommendation is made with Mexican licensing only deferred to a gap line, and the sand-bass '14 in called out on camera' rides on the calico stamp. honest: explicitly separates 'no note places it' from 'documented absence', flags September calico guidance as inferred from a regime label, clean gap list. actionable: excellent for the BOLA program and a kelp day, but the cabrilla half is unusable as a trip — it admits no drive time, no crossing procedure, no panga charter detail.
- *B3 reasons:* found: region gate plus the [Baja only] index badge, the protocol's worked example, then three genuinely different cabrilla access modes (BOLA, San Felipe mothership, Loreto) and the SoCal substitute. specific: leg-by-leg drive (1.5–2 h, 2 h, 2 h, 2 h), $800–1,000/person for 3 nights/2 days, panga $550 + ~$100 tip, hotel $90–120, BOLA season table May–June prime and 'July on everything goes down', Loreto jerkbait fish at 5–10 ft, calico kelp edge 50→25 ft, rise 10–15 ft off 80–100 ft reef, 40–60 ft pre-spawn staging, Ned rig 10 lb braid / 8 lb leader. sourced: note paths plus ids (T3cEQUqiH8E, P36VGPPf120, ikiXx9sUsoA, 8IRONtdkceM, EGKesj7V64M) and channel-registry confidence caveats. scoped: cortez gating explicit, Coronados labeled Mexican water with FMM/CONAPESCA flagged as a KB gap, Mexico paperwork stamped as-of 2026-08-06 with verify, calico 14 in (as of 2022-04-25) and 5/day (as of 2019-03-13) both CDFW with verify, SBB no minimum as of 2024-11. honest: says up front it pulled no live water, warns against borrowing BOLA's calendar for Loreto, names unregistered-channel medium confidence, admits no landing/charter list. actionable: answers both halves — a bookable trip decision and a runnable weekend program including an inside-the-bay fallback.
- *NOW reasons:* found: names the region gate on species/cabrilla.md, cites the protocol's own Mission Bay→cabrilla worked example, then routes to the real Cortez fishery and a SoCal substitute. specific: BOLA drive 8h/11h door-to-door, $90–120/night, 30–40 ft rise then 60–80 ft by 09:00–10:00 then 80–150 ft, 65/50 and 80/80 line, 6–8 ft leader, calico 65–68°F, Point Loma 12 spots / La Jolla 14 spots, 180–210 ft rockfish drift, 3/8–3/4 oz keel hook, 1.5 oz tube. sourced: note paths plus video ids on nearly every parameter (EmZO8QiOfik, 0dNfsle54Wo, 0KQ--N5TjqE, YIABTTYXeqc). scoped: cortez vs socal-bight gating explicit, Coronados flagged baja-pacific-north/Mexican paperwork, calico 14 in California/CDFW as of 2026-08 with verify-current and the bag-limit-of-5 flagged single-source and dated. honest: absolute dates only, flags its own note's mislabeled BOLA footage and unsupported 40–60 lb rod class, long and concrete gap list, no conditions bluff. actionable: an angler can run either a Cortez trip decision or a Saturday kelp day off it.

<details><summary>Full prompt</summary>

Can I fish for cabrilla out of San Diego this weekend in mid-September? Where would I go?

</details>

<details><summary><b>B2 — batch 2</b> · 10/12</summary>

## Short answer: no — not out of San Diego

Cabrilla, in this knowledgebase, is a **Baja / Sea of Cortez fishery, not a Southern California one**. [`species/cabrilla.md`](species/cabrilla.md) opens by stating its region flatly: *"Baja — Sea of Cortez / Bay of LA (BOLA), panga fishery"* (`EmZO8QiOfik`). Every cabrilla source in the corpus is on the other side of the peninsula or well down it:

- **Bay of LA / Sea of Cortez** — the core doctrine, fished from pangas off Tony Reyes-style multi-day trips (`EmZO8QiOfik`, `dEPuDrhoClM`, `M8hOYQ_6rSg`).
- **Gonzaga Bay** — wire leader on 65 lb spectra for cabrilla and barred pargo tight to the rocks; grouper dropped on big baits starting in **80–90 ft** ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), `_Wb4z4ammoM`, `A6s-A1NARuA`).
- **La Paz / Isla Espíritu Santo** — cabrilla in the mixed bag on a mackerel flyline ([`techniques/flyline.md`](techniques/flyline.md)).
- **Cedros Island** (the Baja *Pacific* side, and the closest cabrilla ever gets to San Diego in this KB) — and there, local operators adopted **100% voluntary catch-and-release for calico, grouper (cabrilla), and black seabass** as reported 2023-10-16, on the grounds that summer spawning-aggregation pressure had collapsed the catch from "by the hundred" to "none or very few" ([`species/calico-bass.md`](species/calico-bass.md), `ldVj0BoB-kE` / `Zo92MG459gQ`). That's an operator agreement, not a government rule — verify current status before fishing.

There is **no note anywhere in this KB that puts cabrilla in San Diego, the Coronados, or anywhere in the Bight.** I want to be precise about what that means: the KB never explicitly says "cabrilla do not occur off San Diego" either. Compare [`species/pacific-crevalle-jack.md`](species/pacific-crevalle-jack.md), which *does* flag its species as "a rare warm-water visitor to SoCal in strong warm-water years." Cabrilla gets no such SoCal-stray entry, and no SoCal source mentions one. So: **the KB gives you nothing to plan a San Diego cabrilla trip on**, and I'm not going to invent a spot for you.

Getting to real cabrilla water from Dana Landing is not a weekend of Sept 12–13. Your boat per [`profiles/cameron/boat.md`](profiles/cameron/boat.md) is a Panga Marine Marquesas 22 on a single 115 hp Yamaha, ~35 kt top end, home waters listed as **Coronado Islands, La Jolla, San Diego offshore banks** — that's a Bight envelope, and BOLA is a trailer trip. Your profile already has the right answer to the cabrilla question sitting in it: [`profiles/cameron/spots.md`](profiles/cameron/spots.md) records a **next BOLA trip in September 2026**. That's your cabrilla trip.

---

## What to load for that BOLA trip (since September is the pre-micro-bait window)

Worth knowing now, because the calendar matters here: the cabrilla note's only seasonal hinge is a **bait-driven shift from roughly October on**, when Sea of Cortez baitfish shrink to about **1–1.5 in** and cabrilla key hard on that micro-bait. A September trip is *ahead* of that window — run the full-size program, and treat downsizing as the slow-bite fallback rather than the default (`EmZO8QiOfik`).

The day ladder from [`species/cabrilla.md`](species/cabrilla.md) and [`lures/jerkbaits.md`](lures/jerkbaits.md):

| Time | Where the fish are | Program |
| --- | --- | --- |
| Low light, early/late | Tight to visible shoreline rock; will rise **30–40 ft** to eat a surface-fished jerkbait | **170-size jerkbait** cast tight to the rock (Yo-Zuri Hydro Minnow LC runs 1–3 ft, occasionally 4 ft; Current Sniper 5–7 ft, 170 only). White, bright, or dark all get bit |
| Sun up | Off the tightest rock, toward the "dark spot" — a dark patch a little further off the visible rocks is submerged rock, and it holds the **bigger** fish | Drop to **150-size** or Mag Minnow; bright / metallic / flashy |
| ~9–10 am on | **60–80 ft** | **Yo-yo iron**: Salas 6X, 6X Jr, 60 g jig paras, Krocodile. Cast, hit bottom, then **burn it straight back to the boat** — not a rockfish hop |
| ~11 am–3 pm | Bigger fish at **80–150 ft** | Heavier iron — Salas 6X, Tady 40, 7X-class. Burn **30–40 cranks** off bottom, settle back, repeat; bites usually come within **5–10 cranks** of picking it up |

Gear: two jerkbait rods side by side, medium-light and medium-heavy, both **7'10"–8 ft, ~50 lb class**, "a crankbait rod on steroids"; low-profile level-wind at **6.5:1–7:1+** (you're making ~2–3 casts/min all day and a non-level-wind will fatigue you into backlashes). Light outfit **65 lb braid → 50 lb mono top shot**; heavy outfit **80 lb braid → 80 lb leader**. Bring a **spare 300 yd one-shot of braid** — the cast volume wears braid through the guides. Trebles: **1/0 extra-strong wire** ([`tackle/hooks.md`](tackle/hooks.md), `dEPuDrhoClM`). Note the unreconciled drag split in the note: Cesar runs the star **locked to its stop** paired with a slower-bending rod as the shock absorber; Ray Sharifi backs the drag off and runs a faster-action rod. Both are on the table; pick by which rod you're holding.

And the other half of a September BOLA day, from your own attributed doctrine: **yellowtail are on the bottom** that time of year at BOLA — dropper loops and yo-yo iron to marks on the high spots, with slow-pitch/knife jigs **130–250 g** in the **150–300 ft** band (bit best **150–180 ft**) ([`seasonal/september.md`](seasonal/september.md), [`species/yellowtail.md`](species/yellowtail.md), `vqsD0qpwcJA` / `Jtf-bU4aM-c`).

---

## This weekend out of San Diego: fish calicos, which is the same game

The closest thing the Bight has to the cabrilla program isn't a substitute I'm inventing — the sources make the link themselves. The Gonzaga Bay crew described their cabrilla/pargo program as **"real similar to Calico fishing"** (`_Wb4z4ammoM`), and said the wolf-pack grouper and cabrilla on that structure behaved **"just like calicoes"** (`A6s-A1NARuA`). Same close-structure casting, same reaction retrieve, same rock. Out of Dana Landing on Sept 12–13 that's **La Jolla and Point Loma kelp, and the Coronados** (~13 mi from San Diego, in Mexican waters — see gaps).

Timing per [`species/calico-bass.md`](species/calico-bass.md): calico are a year-round coastal fishery that peaks in the warm months, and **the warm-stable regime is the core kelp season**. [`seasonal/september.md`](seasonal/september.md) puts mid-September in **warm stable (late)**, so you are still inside it.

**Read the water, not the tide clock.** Calico are current-driven and largely tide-indifferent — the opposite of harbor spotted bay bass. The parallel-current rule governs: current running **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage — skip it. Diagnose it off the kelp itself: pulled **20 ft under** = raging, surface presentations dead; **laid down** = strong; **resurfacing** = slacking, go back on top ([`conditions/current-diagnostics.md`](conditions/current-diagnostics.md), [`conditions/current-structure.md`](conditions/current-structure.md)).

**Where on the head.** The biting fish sit on the **up-current / leading edge** — calico face into the current and ambush from the front (`Rwy4MqeXCIU`). "Hit three or four sides of it and you know in two or three casts." Working depths: the **outside kelp edge ~50 ft in to ~25 ft**, and they'll rise **10–15 ft off 80–100 ft of reef** to eat a crank or a sunk iron. A green-stained, near-opaque color with **5–10 ft of visibility** is the preferred read — the stain gives them a place to hide and they feed up more freely (`9xNhdu2aBqE`). Cormorants diving *in* the kelp is your best bird tell ([`conditions/bird-reading.md`](conditions/bird-reading.md)).

**Rotation for the weekend:**

- **Weedless swimbait** — 7" slug on a **3/8–3/4 oz keel-weighted spring hook**, short targeted casts to individual stringers, fast steady wind, pause on the eat. **7–8 ft graphite-composite bass class, 40–60 lb**, soft glass tip, **40–65 lb fluoro** leader for kelp abrasion.
- **Open slug on top** when you need to call fish off the stringers from a distance — bomb cast, skitter with a 1-2-3 pause, 8–9 ft bass class.
- **Surface iron on a jig stick** for the bigger cruising fish when the current is up — steady grind along the kelp line, change kick and speed to the bite.
- **Chum-and-anchor** if you want to sit one edge: chum the spot, reposition up-current, back down onto it as the anchor sets — fish come out of the kelp as the hook goes down (`RXNebDr4j7s`).
- **Covering water is the method:** 10–25 casts to the prime edge, then move 100 ft or 100 yards. If they're not on the prime spot they're usually not in the bed. Beds re-bite — come back later.

**Legal size: 14 in, California / CDFW, as of 2026-08 — verify current rules before you go** ([`species/calico-bass.md`](species/calico-bass.md), `r6j5w40fVHI`). Expect **barred sand bass mixed in** on the same hard bottom; a North County San Diego trip logged them together over hard bottom with kelp not reaching the surface at **~40–42 ft**, same 14 in size called out on camera ([`species/sand-bass.md`](species/sand-bass.md), `HMdrP4-i9MM`).

**If you'd rather run offshore instead**, [`seasonal/september.md`](seasonal/september.md) says what the month holds: dorado in **open-water schools below Catalina** (not on structure), yellowfin volume near the border sliding north with the warm water and bluefin sliding with them, and the "volume square" (SBI–San Nicolas–Clemente–Catalina) holding the bigger bluefin — that last one is well outside a panga day from Mission Bay. The realistic one for you is dorado: **~15 mi off San Diego** is the typical big-concentration zone, on **kelp paddies**, where cold green beach water butts against warm blue, reference band **~71–72 °F** (71.6 °F on a productive paddy, `E4vKwRaRueA`). And paddy water is not evenly spread — best **south of San Clemente/Catalina and along the Dana Point → Oceanside strip and southward**; thin north of Dana Point (`HzE4FHHcvTk`).

---

## Before you commit: pull conditions

I have no live water for Sept 12–13, 2026 — no BightSST access in this session and you didn't give me any, so nothing above is weighted to actual conditions. Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), step 1 is per-spot SST + chlorophyll and wind/swell/current, observed **and** forecast, for each zone and along the transit route. Distrust single-source SST extremes and cross-check models — there's a known `goes_west_composite` window discrepancy and a cloud-contaminated 96.6 °F NRT max on record. One boat-specific note from [`conditions/sea-state.md`](conditions/sea-state.md): the **San Diego Bay entrance is open to swell** on your own chart work — worth a look before a Coronados run in a 22 ft panga.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/cabrilla.md`, `species/calico-bass.md`, `species/sand-bass.md`, `species/yellowtail.md`, `species/dorado.md`, `species/pacific-crevalle-jack.md`, `seasonal/september.md`, `lures/jerkbaits.md`, `lures/iron-jigs.md`, `techniques/yo-yo-iron.md`, `techniques/flyline.md`, `techniques/dropper-loop.md`, `techniques/sliding-sinker.md`, `techniques/trolling.md`, `techniques/slow-pitch-jigging.md`, `tackle/hooks.md`, `tackle/line-and-leader.md`, `tackle/rod-and-reel-selection.md`, `tackle/gear-classes.md`, `rigging/trap-rig.md`, `bait/making-bait.md`, `locations/zone-lexicon.md`, `locations/bight-geography.md`, `locations/bightsst-eval-targets.md`, `conditions/sea-state.md`, `profiles/cameron/boat.md`, `profiles/cameron/spots.md`, `species/README.md`, `lures/README.md`, `locations/README.md`  
*videos:* `EmZO8QiOfik`, `dEPuDrhoClM`, `M8hOYQ_6rSg`, `_Wb4z4ammoM`, `A6s-A1NARuA`, `ldVj0BoB-kE`, `Zo92MG459gQ`, `5to3Q5P7w90`, `E4vKwRaRueA`, `HzE4FHHcvTk`, `r6j5w40fVHI`, `Rwy4MqeXCIU`, `9xNhdu2aBqE`, `RXNebDr4j7s`, `HMdrP4-i9MM`, `vqsD0qpwcJA`, `Jtf-bU4aM-c`  
*gaps admitted:* The KB contains no note placing cabrilla anywhere in SoCal / San Diego waters — and it also never explicitly states that cabrilla are absent north of the border, so I can only report zero SoCal coverage, not a documented absence. | No cabrilla month-by-month seasonal or location pattern exists beyond the single 'roughly October on, bait shrinks to 1–1.5 in' micro-bait shift; there is no September-specific cabrilla entry. | No cabrilla sonar signature is documented anywhere in the corpus — species/cabrilla.md says so explicitly; only the visual boiler-rock / bottom-color / 'dark spot' read is covered. | No travel logistics for reaching cabrilla water: the KB gives no drive time, run distance, border-crossing procedure, or launch/panga-charter detail for BOLA or Gonzaga Bay. | No Mexican fishing license, permit, or FMM requirements are covered — the only permit mention in the whole corpus is an incidental note that a Cedros charter's permits were obtained in Tijuana. This matters for the Coronado Islands option, which is in Mexican waters. | No live conditions for Sept 12–13, 2026 — no BightSST access in this session and none supplied in the prompt, so no SST, chlorophyll, wind, swell, or current weighting was applied to any zone. | No tide tables or moon phase for the weekend of Sept 12–13, 2026, so the moon-driven calico bite-window rule (full-moon nights = bite early, dead by mid-morning) could not be applied. | seasonal/september.md carries no inshore-bass priors at all — the September calico guidance here is inferred from the regime label ('warm stable, late') plus the year-round/warm-months statement in species/calico-bass.md, not from a September-specific source. | No note gives boat-range or sea-state limits for a Coronados or 15-mile-offshore run in a Panga Marquesas 22; profiles/cameron/boat.md lists platform facts and home waters but no stated range figure or sea-state ceiling.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Short answer: no — not out of San Diego, and not on a weekend

Cabrilla (leopard grouper) is a **Sea of Cortez fish**. In this KB it is gated `regions: [cortez-north, cortez-south]`, `waters: [nearshore-coast, island]` (`species/cabrilla.md`) — it carries no `socal-bight` label, and the generated species index badges it **[Baja only]** (`species/README.md`).

This is not a technicality. It's the KB's own worked example of the mistake: the day-plan protocol says a Mission Bay plan can route to cabrilla, "whose situation table opens with 'low light, tight to shoreline structure → jerkbaits, cast tight to the rock.' That reads perfectly for a SoCal jetty at dawn, and the fish lives 400 miles away in the Sea of Cortez" (`planning/day-plan-protocol.md`, step 1b; same passage in `locations/regions.md`). The region gate is binding — a note outside the day's envelope is never offered, not offered with a caveat.

**Before anything else:** I have no live water. Step 1 of the protocol is to pull BightSST per-spot SST/chlorophyll plus wind/swell/current, observed and forecast (`planning/day-plan-protocol.md`, `config/endpoints.md`), and I can't reach it here and you didn't give me conditions. Everything below is the **priors layer**, not intel for Sept 12–13. Step 1b also needs your boat's `range_nm` and `sea_state_max_ft` to decide whether island/bank water is even in the envelope — with no profile I'm limited to gear-class terms.

---

## If you actually want cabrilla, here is where it lives

Three genuinely different trips (`locations/sea-of-cortez.md`), none of them a San Diego weekend:

| Access | What it is |
| --- | --- |
| **Bahía de los Ángeles (BOLA)** | Drive down, hotel, day-boat pangas |
| **San Felipe mothership** | Week-to-ten-day live-aboard carrying its own pangas (Tony Reyes-style) |
| **Loreto / Puerto Escondido** | Fly in; island fishery, different species mix |

**BOLA is ~8 hours' drive from San Diego** — 9–10 at a relaxed pace, and one documented crew left 06:30 and reached the hotel at 17:31, an 11-hour travel day (`locations/bahia-de-los-angeles.md`, `T3cEQUqiH8E`). Leg by leg: San Diego → Calexico 1.5–2 h, Calexico → San Felipe 2 h, San Felipe → Gonzaga 2 h, Gonzaga → BOLA 2 h. Budget from that note: **$800–1,000 per person all-in for a 4-day trip (3 nights, 2 fishing days)**, panga **$550/day plus ~$100 tip**, hotel **$90–120/night**. Paperwork (Mexico — INM for entry, CONAPESCA for fishing; as reported 2026-08-06, **verify current before you travel**): FMM tourist permit printed, Mexican fishing licence, passport, plus Mexican vehicle insurance in practice — Baja Bound named, ~$90 for a 2021 car, ~$130 for a newer Tacoma. No cell service through the desert or at the bay. Buy all tackle before you cross; prices past the border run roughly double and there is no real tackle shop (`odiIWmut6gM`).

**And mid-September is not the cabrilla window even there.** BOLA's season table (`locations/bahia-de-los-angeles.md`, `P36VGPPf120`, unregistered channel — medium confidence): prime is **May–June**, with end-April → early June called the good window; **"July on — everything starts to go down,"** water heats and **fish drop out of the surface program**; **August–October is the late-season play for dorado, marlin, sailfish and occasionally tuna**, not the shallow cast-and-wind game. The mechanism is that the fish sound — you move to dropper loop, live bait, yo-yo iron and knife jigs, "anything heavy on the bottom." That independently matches Cameron's own September BOLA read: the yellowtail are **on the bottom**, fished with dropper loops and yo-yo iron (`seasonal/september.md`, source `cameron`).

**Loreto** is the one you can fly to — out of **CBX (Cross Border Xpress)** rather than driving (`locations/loreto.md`, `ikiXx9sUsoA`). Cabrilla there come shallow, **5–10 ft, on a suspending jerkbait**. But that note is explicit that **season data is thin — no month-by-month Loreto calendar exists in this corpus, and you must not borrow BOLA's table for it** (different latitude, different species mix). There is one September shoreline session on record (`0b0PDLVh-T4`) and that's it.

One timing note if you do book a Cortez trip: from roughly **October on**, Sea of Cortez baitfish shrink to about **1–1.5 in** and cabrilla key hard on that micro-bait — carry downsized jig paras and small-profile jerkbaits for that window (`species/cabrilla.md`, `EmZO8QiOfik`).

---

## What fishes like cabrilla out of San Diego this weekend

The Cortez program *is* SoCal bass fishing scaled up — an angler on the rocks there summed it up as "this is literally calico fishing on steroids" (`locations/sea-of-cortez.md`, `8IRONtdkceM`). So the honest substitute is **calico bass**, which is gated `regions: [socal-bight, baja-pacific-north, baja-pacific-south]`, `waters: [nearshore-coast, island, bay-harbor]` (`species/calico-bass.md`).

**Where:** kelp beds, reef, boiler rocks, breakwalls/jetties and island structure from the coast out to Catalina, Clemente and the Channel Islands. Fish the **edges and pinch-points** — leading edge, outside edge, isolated stringers off the main bed — not the dense middle (`species/calico-bass.md`, `locations/bass-structure.md`, `locations/breakwalls-jetties-riprap.md`).

**When:** year-round, peaking in the warm months; `seasonal/september.md` maps September to the **warm-stable (late) regime**, which is the core kelp season. Timing rules of thumb from the n6yun panel (`RUuPNpK0x-s`, unregistered — medium): fish the **hour before sunrise into early morning**, and the **hour before sunset**. On a bright, stable-light day calico "levitate" up into the **outer canopy edge**; overcast spreads them through the column. On a clear full moon they gorge at night and **shut down by mid-morning** (`conditions/moon.md`).

**The read that decides the day is current, not tide.** Calico are current-driven and largely tide-indifferent: current running **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage — skip it (`conditions/current-structure.md`). Read it off the kelp: pulled 20 ft under = raging, surface presentations dead; laid down = strong; resurfacing = slacking, go back on top (`conditions/current-diagnostics.md`).

**Depths to work:** outside kelp edge **~50 ft in to ~25 ft**; calico will rise **10–15 ft off 80–100 ft of reef** to eat a crankbait or sunk iron; summer twilight pre-spawn staging sits in **40–60 ft over hard bottom**. Solid unbroken bait usually has no predators on it — broken, harried bait does (`planning/electronics-and-sounder.md`).

**Technique per situation** (from the router table in `species/calico-bass.md`):

- Parallel current, fish tight to stringers → **weedless swimbait**, short targeted casts, fast steady wind, pause on the eat. 7" slug on a **3/8–3/4 oz keel-weighted spring hook**, 7–8 ft graphite-composite bass class, **40–60 lb**, heavy fluoro leader (40–65 lb) for kelp abrasion.
- Need to draw fish from distance → **open slug**, bomb cast, skitter with a 1-2-3 pause, 8–9 ft bass class.
- Current up, bigger cruising fish → **surface iron** on a jig-stick class, steady grind along the kelp line (`techniques/surface-iron.md`).
- Sparse lanes, not committing → **crank the 80–100 ft lanes** (`techniques/inshore-crankbaits.md`), 7–10 ft crank class.
- Live bait around → **flyline** a sardine or mackerel, 25–40 lb (`techniques/flyline.md`).
- Hunting a 7–10 lb fish rather than numbers → size up to **8–10 in swimbaits on 65–80 lb braid**; baits under ~5.5 in top out around 1–4 lb (n6yun Fred Hall panel 2013-03-09, `ZoIzpyyS9xw`).

**Method:** 10–25 casts to the prime edge, then move 100 ft or 100 yards. If they're not on the prime spot they're usually not in the bed; beds re-bite, so come back later (Landesfeind, Academy Ep. 13).

**Regulations (California / CDFW):** calico minimum **14 in** (as of 2022-04-25) and a bag limit of **5 per day** (as of 2019-03-13 — the oldest regulatory figure in the register). Verify both with CDFW before you fish (`sources/regulatory-claims.md`).

### If the wind or your boat keeps you inside

**Spotted bay bass** in San Diego Bay or Mission Bay — `regions: [socal-bight]`, `waters: [bay-harbor]` (`species/spotted-bay-bass.md`). These are the opposite read from calico: **fully tide-driven**. Fish eelgrass edges, mooring cans, dock pilings, riprap and channel drops; set up **up-current of the structure** and re-read every spot when the tide turns. Skip the roughly **half hour either side of the high/low turn** — current all but stops — and fish the moving-water stretch instead (Roman Castro, `EGKesj7V64M`). Cast up-current across the grain of the leaning eelgrass. Programs: **Ned rig** (mushroom head + buoyant TRD on 10 lb braid / 8 lb leader), **drop shot**, a **Zoom fluke on a 1/4–3/8 oz ballhead** flipped into pilings, or crank the flats with an 8–10 ft crank class. No minimum size as of 2024-11 (`usHl-4SfqDA`) — verify with CDFW.

### One thing to be careful about

The **Coronado Islands** are ~13 mi from San Diego and are the closest thing to shallow-rock island bass work, but they are **Mexican water** (`species/yellowtail.md`; `species/yellowfin-tuna.md` labels them `baja-pacific-north`), so the FMM/CONAPESCA paperwork applies there too — and the KB flags Mexican licensing and entry requirements as a **known gap** outside the BOLA note (`sources/regulatory-claims.md`). The KB's Coronados material is the **spring/warming-transition** yellowtail classic with "seeing-not-biting" narrow daily windows; it gives me no September prior for that island group. And there is no cabrilla there regardless.

### September priors for the offshore option, since you're launching from San Diego

From `seasonal/september.md`: the **"volume square" — Santa Barbara Island / San Nicolas / Clemente / Catalina — holds the bigger bluefin** (that's well north of you); **dorado run in open-water schools below Catalina**; and **yellowfin volume near the border slides north with the warm water, with the bluefin sliding with them — follow the temperature, not last week's spot.** Paddy water is best **south of San Clemente Island / Catalina and along the coastal strip from Dana Point to Oceanside and southward** (`locations/bight-geography.md`), which is the water off your bow. Hurricane remnants are usually a non-event that breaks the heat with the fishing unaffected (9/14/22).

**Tell me your boat (range, sea-state max, rod inventory) and I'll set the actual `{regions, waters}` envelope and put real gear against it instead of class terms.** And if you have live conditions for Saturday — SST, chlorophyll, wind, swell — hand them to me and I'll weight the zones properly.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `locations/regions.md`, `locations/sea-of-cortez.md`, `locations/bahia-de-los-angeles.md`, `locations/loreto.md`, `locations/bight-geography.md`, `species/cabrilla.md`, `species/README.md`, `species/calico-bass.md`, `species/spotted-bay-bass.md`, `species/yellowtail.md`, `species/yellowfin-tuna.md`, `species/snook.md`, `seasonal/september.md`, `sources/regulatory-claims.md`  
*videos:* `EmZO8QiOfik`, `8IRONtdkceM`, `T3cEQUqiH8E`, `P36VGPPf120`, `odiIWmut6gM`, `ikiXx9sUsoA`, `0b0PDLVh-T4`, `n4nMCLLW3tY`, `RUuPNpK0x-s`, `ZoIzpyyS9xw`, `EGKesj7V64M`, `usHl-4SfqDA`, `r6j5w40fVHI`, `LqW32NSkObY`, `ts9rJgxjmSg`, `ZYAILGyrkRk`, `4Dn7yChmhk0`, `0dNfsle54Wo`, `aT-fL7vaavY`, `BSNGeduOHYM`, `K22a8Ui8tWg`, `6P34jI9q1tE`, `XRIjUgpuyZ8`, `ojE5H6AdGGo`, `wX7jUycIJ-U`, `9a-Zy_D6c3w`, `lP6cg4eEU6s`, `s5PaKJX3VDo`  
*gaps admitted:* The KB has no SoCal cabrilla fishery at all — cabrilla is gated cortez-north/cortez-south only, so the premise of the question (cabrilla out of San Diego) has no note behind it. | No live conditions: I could not pull BightSST SST/chlorophyll/wind/swell/current for Sept 12-13 2026, and none were supplied, so nothing here is current intel — only the priors layer. | No angler profile was given (boat range_nm, sea_state_max_ft, rod/reel inventory), so the day's {regions, waters} envelope could not be set and gear stays in class terms rather than owned gear. | The cabrilla note carries a flagged stub for sonar signature — the corpus has no sonar-arc or depth meter signature for cabrilla specifically, only the visual/structure read. | The KB has no month-by-month cabrilla location calendar; the only seasonal detail in species/cabrilla.md is the fall/winter (roughly October on) shift to 1-1.5 in micro-bait. | No month-by-month Loreto calendar exists in the corpus, and locations/loreto.md explicitly forbids borrowing BOLA's season table for it — so I cannot say whether mid-September is a good Loreto cabrilla window. | No September prior exists for the Coronado Islands specifically — the KB's Coronados material is the spring/warming-transition yellowtail pattern. | Mexican licensing and entry requirements are flagged in sources/regulatory-claims.md as a known KB gap outside the BOLA note, so the FMM/CONAPESCA detail I gave comes only from that one 2026-08-06 source and must be re-verified. | The KB has no list of San Diego landings, day-boat operators or charter bookings; planning/trip-length-selection.md covers only the one-day vs multi-day long-range format decision. | Several supporting figures come from unregistered channels and cap at medium confidence (the BOLA season table, the n6yun dawn/dusk and light-angle reads, the Dirty Hookers Sea of Cortez on-the-water material).

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short answer: no — not out of San Diego, not this weekend, not in any season

Cabrilla is a **Sea of Cortez fish**. The KB gates it explicitly: `species/cabrilla.md` carries `regions: [cortez-north, cortez-south]`, `waters: [nearshore-coast, island]`. San Diego is `socal-bight`. Under step 1b of `planning/day-plan-protocol.md`, a species note whose `regions` doesn't contain the day's region is **"never offered — not ranked lower, not offered with a caveat."**

Your question is, almost word for word, the failure this KB was built to stop. Both `planning/day-plan-protocol.md` and `locations/regions.md` use it as the worked example: a Mission Bay day plan can route to cabrilla because that note's situation table opens with *"low light, tight to shoreline structure → jerkbaits, cast tight to the rock"* — which reads perfectly for a SoCal jetty at dawn — **and the fish lives 400 miles away** (cameron).

`locations/cortez-north.md` puts the boundary plainly: *"Cabrilla and pargo are Cortez fish; white seabass and calico run the Baja Pacific, which is why the vocabulary splits the two rather than lumping them as 'Baja.'"* The Bight's own species mix in `locations/socal-bight.md` — bay bass to billfish across all five water types — contains no cabrilla and no grouper of any kind.

---

## If you actually want cabrilla, here's the real trip

It is a **road trip to a panga fishery**, not a boat day. From `locations/cortez-north.md` and `locations/bahia-de-los-angeles.md`:

- **~8 hours' drive from San Diego** to the northern Cortez (`P36VGPPf120`). One crew's real door-to-door was **11 hours** — left 06:30, at the hotel 17:31, with a lunch stop in San Felipe (`T3cEQUqiH8E`).
- **Bahía de los Ángeles (BOLA)** is the one ground the corpus documents in depth. You don't use the ramp — the panga is driven to your hotel room, loaded there, and trailered off the beach at day's end (`odiIWmut6gM`, `P36VGPPf120`). Costa del Sol runs **$90–120/night** (`P36VGPPf120`).
- **Everything you fish with crosses the border with you.** *"There's no tackle shop to really speak of… everything is really limited, so you pack up extra. Not the trip you want to pack light for"* (`odiIWmut6gM`). No cell service through the desert, at Gonzaga, or at the bay.
- **Timing.** `locations/cortez-north.md` carries `season_peak: [apr, may, jun]` — mid-September is not it. The one thing the corpus does peg seasonally for cabrilla is bait size: **from roughly October into winter, Cortez baitfish drop to ~1–1.5 in** and cabrilla key hard on that micro-bait, so a fall trip carries downsized lures (`EmZO8QiOfik`). Mid-September sits just ahead of that. Cortez North's `open-ocean` window — dorado, striped marlin, sailfish, occasional tuna — is given as **August–October** (`P36VGPPf120`), so a September Cortez trip is arguably better aimed at that than at the rock.
- **The program itself** (for when you do go): jerkbaits cast tight to boiler rock at first light with fish rising **30–40 ft** to eat on top; by **~09:00–10:00** they've dropped to **60–80 ft**; under high sun **11:00–15:00** the bigger fish push to **80–150 ft** and it becomes a yo-yo iron game (`EmZO8QiOfik`). Grade runs **5–10 lb with 15s in the same schools, 17 lb best on a spring scale** (`0dNfsle54Wo`). Line: 65 lb braid to a 50 lb mono topshot on the light stick, 80 lb braid to 80 lb leader on the heavy, with **6–8 ft of leader** so a fish that reaches the rocks is pulling against leader, not braid (`EmZO8QiOfik`, `dEPuDrhoClM`).

**Read that note with its flags open.** `species/cabrilla.md` is heavily fact-check-flagged: the 40–60 lb yo-yo rod class appears in neither cited transcript, and two of its headline trips (`0dNfsle54Wo`, `dEPuDrhoClM`) are San Felipe mothership footage mislabeled as BOLA. Its `confidence` is `medium`.

---

## What to fish instead this weekend (Sat 12 / Sun 13 Sept)

The KB draws the analogy in both directions, so if what you want is *the cast-at-the-rock structure-ambush program*, the SoCal fish is the **calico bass**:

- `species/cabrilla.md`: cabrilla *"sit behind a boulder or against a vertical wall and ambush what passes, **the way a calico bass works structure**"* (`6P34jI9q1tE`).
- `locations/cortez-north.md`, from the other side: an angler's summary of the cabrilla rocks is *"this is literally **calico fishing on steroids**"* (`8IRONtdkceM`).

### Calico bass — `species/calico-bass.md`
`regions: [socal-bight, …]`, `waters: [nearshore-coast, island, bay-harbor]`, `season_peak` includes **sep**. Year-round fishery that peaks in the warm months; **warm-stable (June–September) is the core kelp season**.

**Temperature:** preference band **65–68 °F**; past about **70 °F** they get lethargic and drop to cooler water, though they'll still hit a top-water bait (`LqW32NSkObY`). Mid-September in San Diego can sit above that — pull the actual per-spot SST before committing (see caveat below).

**Where, out of San Diego:**
- **Point Loma** (`locations/point-loma.md`) — coastal kelp and hard bottom down the Sunset Cliffs face, **12 charted spots**, plus the Point Loma Pipe, the Zuniga Jetty riprap and the Hotel Del hard bottom around the corner at the bay entrance. It's one of the corpus's named SoCal kelp beds (`xI9tPJFXbUM`, `kzD0kSnnVPw` — both cites carry a flag that they only name it in passing). The peninsula is also the swell block for the bay entrance: the entrance is open to swell from roughly **160°–186°**, channel seaward axis **186°**, with Point Loma blocking anything west of the axis (cameron).
- **La Jolla** (`locations/la-jolla.md`) — **14 charted spots** at the canyon head, **inside morning-half-day range for a San Diego boat** (`VpW91AKOFVQ`). North-end reef and high spots hold yellowtail in **5–10 fathoms** with marks down to 90 ft on the incline (`yLpDI8jnizU`); the south shelf hard bottom drifts at **180–210 ft (35 fathoms)** for rockfish (`_ZThckj2TIM`). Note: *"presence is not catchability here"* — some yellowtail are in La Jolla year-round and half-day boats go months between fish (cameron).

**Current is the gate, not the tide clock.** Parallel to the shoreline (uphill or downhill) = fishable; **into** the beach = marginal; **off** the beach = garbage, skip the spot (`0KQ--N5TjqE`). Mechanism: calico face into the current and ambush from the *front* of the structure, so parallel flow is what delivers food past the edge they're sitting on (`Rwy4MqeXCIU`). Read it off the kelp — **pulled 20 ft under** = raging (surface presentations dead); **laid down** = strong; **resurfacing** = slacking, go back on top.

**Timing:** hour before sunrise into early morning, and the hour before sunset (`RUuPNpK0x-s`). **Check the moon before you set the alarm** — on a clear full moon they gorge overnight and shut down by mid-morning, and the instruction is *don't launch until noon or one o'clock* if you can't make first light (`Blh2BA-7Ono`).

**Gear, in class terms** (you haven't given me a profile, so I can't resolve to owned tackle):

| Situation | Do this | Class |
| --- | --- | --- |
| Kelp bed, parallel current, fish tight to stringers | Weedless swimbait — short targeted casts, fast steady wind, pause on the eat. 7" weedless slug on a **3/8–3/4 oz** keel-weighted spring hook (`YIABTTYXeqc`) | 7–8 ft graphite-composite bass class, **40–60 lb** |
| Cruising fish, current up, cover the whole edge on top | Surface iron, grind the kelp line | Jig-stick class |
| Shallow reef, birds working over it | Surface iron on the drift — reef bottom **18–20 ft**, wide-open with birds overhead (`I-QBxuV2p7M`) | Jig-stick class |
| Tight to the beach, current ripping, no kelp | Free-spool bounce a weighted tube off the bottom — **1.5 oz** held bottom, current pulled the bait 5–10 ft further each bounce, "calicos every cast" (`9a-Zy_D6c3w`) | Bass class |
| Hunting a **7–10 lb** trophy, not numbers | Size up to **8–10 in** baits (sub-5.5 in baits top out around 1–4 lb) (`ZoIzpyyS9xw`) | Heavy bass casting, **65–80 lb braid** |

**Regs — California / CDFW.** Calico minimum **14 in**, as of 2026-08 (`r6j5w40fVHI`, `HMdrP4-i9MM`). Bag limit of **5** is stated (`LqW32NSkObY`) but the KB flags it single-source, dated **2019-03-13**, with no jurisdiction named by the speaker. **Verify current CDFW rules before you fish.**

### Two other in-envelope options
- **Spotted bay bass** — `species/spotted-bay-bass.md`, `regions: [socal-bight]`, `waters: [bay-harbor]`, `season_peak` includes sep. San Diego Bay and Mission Bay, on the tide clock rather than the current read: fish hold ambush stations keyed to which way the water is moving, so a spot on the up-current side of a channel edge on the flood is on the wrong side after the change (`YgqXf9iICyg`). The **Coronado Bridge narrows** is a popular tournament stretch precisely because the pinch point speeds the current up. Working depths **20–30 ft in the San Diego Bay channels**. A PB fish is ~**2.8–3.5 lb** (`XyKF34C5iB4`), which sets the light-line scale.
- **Coronado Islands** — `locations/coronado-islands.md`, **~13 nm from the San Diego bay entrance** (cameron), the closest island structure to a major US port. Two cautions: it is `regions: [baja-pacific-north]` and **Mexican water** — CONAPESCA/INM paperwork, not CDFW, so the day starts with paperwork rather than tackle; and the KB bills it as *the springtime yellowtail trip*, not a September program. (The note also flags an internal conflict: 13 **nm** here vs 13 **mi** in the linked yellowtail zone guide, `D5DR7Kx42_A`.)

If you'd rather chase what mid-September actually favors in the Bight, `seasonal/september.md` weights the **volume square** — Santa Barbara Island / San Nicolas / San Clemente / Catalina — for the bigger bluefin, and puts dorado in open-water schools below Catalina (`5to3Q5P7w90`). That's well north of a San Diego day for most boats, and the note's bluefin reading of that cite carries a fact-check flag.

---

## What this is not yet — the honest caveat

**This is priors, not a plan.** I have pulled **no conditions**: no BightSST per-spot SST or chlorophyll, no wind/swell/current, observed or forecast, for 12–13 September 2026. Step 1 of `planning/day-plan-protocol.md` requires that before any of the above becomes a day plan, and the KB's own doctrine is that *a stale report is not today's water* and *in an anomalous year trust the live water, not the calendar*. Everything above is the pattern layer.

I also have **no profile from you** — no boat, range, sea-state ceiling, or rod inventory — so step 1b's `waters` envelope is unresolved (I don't know whether you're on a private boat, a kayak, or booking a landing) and all gear stays in class terms. Give me those and the recommendations sharpen to owned tackle inside your boat's envelope.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `locations/regions.md`, `species/cabrilla.md`, `locations/cortez-north.md`, `locations/bahia-de-los-angeles.md`, `locations/socal-bight.md`, `seasonal/september.md`, `species/calico-bass.md`, `species/spotted-bay-bass.md`, `species/sand-bass.md`, `locations/point-loma.md`, `locations/la-jolla.md`, `locations/coronado-islands.md`  
*videos:* `EmZO8QiOfik`, `dEPuDrhoClM`, `0dNfsle54Wo`, `6P34jI9q1tE`, `T3cEQUqiH8E`, `P36VGPPf120`, `odiIWmut6gM`, `8IRONtdkceM`, `0KQ--N5TjqE`, `Rwy4MqeXCIU`, `LqW32NSkObY`, `YIABTTYXeqc`, `RUuPNpK0x-s`, `Blh2BA-7Ono`, `r6j5w40fVHI`, `HMdrP4-i9MM`, `9a-Zy_D6c3w`, `ZoIzpyyS9xw`, `I-QBxuV2p7M`, `yLpDI8jnizU`, `_ZThckj2TIM`, `VpW91AKOFVQ`, `xI9tPJFXbUM`, `kzD0kSnnVPw`, `YgqXf9iICyg`, `XyKF34C5iB4`, `D5DR7Kx42_A`, `5to3Q5P7w90`  
*gaps admitted:* No live conditions were pulled — no BightSST SST, chlorophyll, wind, swell or current, observed or forecast, for 12-13 September 2026; the KB is the knowledge layer only and holds no current intel. | No moon phase or tide table for the weekend of 12-13 September 2026 exists anywhere in the KB, so the full-moon inversion rule for calico could not be applied to the actual dates. | No angler profile was supplied (boat, range_nm, sea_state_max_ft, rod/reel inventory), so the day's `waters` envelope is unresolved and all gear stays in class terms rather than owned tackle. | species/cabrilla.md carries a flagged gap: no corpus source gives a month-by-month presence or temperature pattern for cabrilla anywhere in the Sea of Cortez, so the KB cannot say how a mid-September cabrilla trip fishes specifically. | species/cabrilla.md carries a flagged gap: no sonar signature or arc depth for cabrilla anywhere in the corpus — only the visual and structure read. | locations/cortez-north.md and locations/bahia-de-los-angeles.md carry a flagged gap: nothing in the corpus covers running your own boat to the northern Cortez — no trailering, ramp use, on-water fuel or required range. Every documented trip fishes a local panga. | No Mexican (CONAPESCA) bag limit, size gauge or closed season for cabrilla / leopard grouper is recorded anywhere in the corpus as of 2026-08. | species/calico-bass.md carries a flagged gap: no Mexican (CONAPESCA) size or bag limits for calico in Baja waters, and no confirmation of whether any SoCal seasonal closure applies. | The calico bass bag limit of 5 is single-source, dated 2019-03-13, with the jurisdiction (California / CDFW) being the note's own inference rather than stated by the speaker. | No calico zone guide exists for the SoCal coast including North County San Diego — it is a flagged stub in species/calico-bass.md, so zone-level trip detail for a San Diego calico day is not in the KB. | locations/point-loma.md gives no charted or working depth for any of its 12 spots, and no port, ramp or run distance for the zone. | The KB says nothing about whether 'cabrilla' is used in Southern California as a local name for any local species, so I could not check whether the question meant a differently-named SoCal fish. | species/cabrilla.md is confidence: medium and heavily fact-check-flagged — the 40-60 lb yo-yo rod class appears in neither cited transcript, and two headline trips (0dNfsle54Wo, dEPuDrhoClM) are San Felipe mothership footage mislabeled as Bahia de los Angeles. | seasonal/september.md's volume-square bluefin reading carries a contradicted-by-source flag: the transcript's antecedent for 'the bigger ones' is unspecified fish across dorado, bluefin and marlin, not bluefin specifically.

</details>
