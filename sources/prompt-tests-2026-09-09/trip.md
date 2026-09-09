# Trip planning — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.4 | 11.8 | 11.6 |
| found | 1.6 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.8 | 1.8 | 2 |
| honest | 2 | 2 | 2 |
| actionable | 2 | 2 | 1.6 |
| **wins** | 1 | 2 | 2 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 0 | 1 | 0 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | 11.4 | 11.8 | 11.6 |
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

**Winner:** B3 · mapping {'A': 'B2', 'B': 'NOW', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |

**Judge:** All three make the same correct call - outside is off, fish the Dana Point-to-Oceanside coastal strip for calico with mixed-bag bycatch - and all three are honest about the chlorophyll number and the missing swell period, so the separation is in coverage depth and how the envelope is declared. C wins on breadth plus execution: it states the regions/waters gate as binding, explains via bight-geography why water south of Newport survives a NW blow (a mechanism neither A nor B gives), ranks six programs down to gangion, slider-hook and diver-setback specifics, and still lands a harbor bail-out and a jurisdiction-stamped regs block. A is very close - its halibut water-triad, drift-control and bait-barge detail are the best of the three - but it never declares the envelope explicitly, leaves the lobster season unstamped, and its version of the KB has no inshore SST band so the 67-69 F datum goes unscored. B has the cleanest sourcing and the sharpest epistemics (it refuses a self-flagged unverifiable sonar band, surfaces the bait-barge contradiction, and won't guess how far the fishable band extends), but that discipline costs it execution detail on halibut, rockfish and the harbor fallback, leaving the angler with less to do once the kelp bite dies.

- *B2 reasons:* found: nails the go/bail call, the blown-out September offshore program, and a full inshore bass/halibut/WSB/rockfish menu; says plainly the KB has no chlorophyll scale and no inshore SST bands. specific: coordinates for nine spots, 3/8 vs 3/4 oz keel weights, 50-65 lb braid to 60 lb fluoro, 1/2 oz egg + size-2 J, 2.5-3 ft 25-30 lb fluoro trap-rig leader, 20 ft kelp-under current read. sourced: note paths plus video ids on nearly every load-bearing claim, with unregistered-channel medium-confidence calls flagged. scoped: offshore correctly excluded and calico/halibut/rockfish/lobster regs carry CDFW + as-of + verify, but there is no explicit regions/waters declaration and the lobster season line is the one reg without an as-of stamp; the Catalina Eddy 'check before writing off everything offshore' aside is a slightly loose invitation on an SCA day. honest: fifteen concrete admitted gaps including the missing period, moon and current direction, and the tackle-file gap that kills the top calico presentation. actionable: bait-barge protocol, hour-by-hour shape, ranked presentations, drift control, gear table with an honest 'nearest fit' row.
- *B3 reasons:* found: explicit envelope plus the best conditions reasoning of the three - the bight-geography note explaining why water south of Newport survives a NW blow while the northern islands roll over, which is exactly why this day is fishable. specific: six ranked programs with real numbers - 65-68 F band, 0-8/20-100 ft, ~40-42 ft hard bottom with kelp 20 ft off, 24 oz torpedo on 12-15 lb breakaway, 6/0 circles, 1/4-1/2 oz slider with No.2/No.4 bronze, Husky Magnum 25 ft at 33 yd setback at 6-8 kt, spottie 12-14 ft breaks. sourced: note paths and video ids throughout, with named sources and confidence levels attached. scoped: regions/waters declared binding, offshore species named and excluded by their own waters tags, regs block carries CDFW + as-of dates + verify plus three MPA lines. honest: admits September priors contain nothing inshore, no Dana Point location page exists, spot data comes from the personal library, boat envelope is null so it asks, and names two flagged stubs it cannot fill. actionable: the most complete day - bait plan, timeline anchored to the 09:20 pre-change arrival, ranked presentations, terminal rigs for every program, harbor bail-out, and a gear table that names the specific owned irons and divers; minor tension between the late-afternoon session and its own 'return against the build' rule.
- *NOW reasons:* found: correct envelope, correct offshore exclusion, and the only answer that actually scores the given 67-69 F against a stated 65-68 F calico band; refuses to evaluate the paddy water because the KB cannot say how far the inshore band extends. specific: 0-8 and 20-100 ft working depths, nine charted positions, Salas 7X wind step-up, third-of-a-Tady-45 downsize rule, 240 ft vs 75-fathom RCA lines. sourced: cleanest citation hygiene of the three - linked note paths plus a video id on essentially every claim, and it names which claims are single-sourced. scoped: explicit regions/waters gate stated as binding, calico 14 in as of 2026-08, and it flags the bag-of-5 as 2019-03 single-source with no jurisdiction named rather than passing it off as law; MPA latitude flagged as unverified. honest: strongest epistemics - declines to use a sonar band its own note self-flags as unverifiable, surfaces the 5 a.m./7 a.m. bait-barge contradiction side by side, and admits it only read the lobster front matter. actionable: primary program is runnable, but the secondary programs are thin on terminal detail (halibut gets 15 lb fluoro and a three-way, no weight range or drift discipline; rockfish gets regs but no gangion spec) and the harbor bail-out resolves to 'no corpus source', so an angler gets less to execute once the kelp goes quiet.

<details><summary>Full prompt</summary>

It is blowing outside. I am launching from Dana Point. What is fishable today and for what? Assume these conditions and do NOT fetch live data: late September. Outside: NW 20-25 kt, seas 6-8 ft at San Nicolas, Santa Barbara Island and the outer banks, Small Craft Advisory through Sunday. Inshore Dana Point to Oceanside: NW 8-12 kt, 3-4 ft, SST 67-69 F, chlorophyll 1.2 along the kelp. Low tide 10:20.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

## Short answer

**Outside is off. Inside is on, and it's a bass day.** Fish the Dana Point–to–San Onofre kelp and hard bottom for calico and sand bass, with barracuda and bonito as the mixed-bag bycatch, and a halibut drift as the change-up. Skip the outer-bank/island program entirely — the water that holds it in September is exactly the water that's blown out.

---

## 1. The go/bail call

The KB's sea-state layer (`conditions/sea-state.md`) doesn't just look at height:

- **Working-captain thresholds** (`NC3-3pJDEgo`, 2020-11-18 — the note holds these at *medium* confidence, single-mention): wind **above ~12 kt is what raises whitecaps**, and that captain's personal cutoff is not to run above 12 kt. **Swell interval under 10 seconds is a hard bad-sea flag** ("absolutely horrible"), independent of height. And the **named unfishable combo is 12–15 kt with 4–8 ft swell at a 9-second interval** — "you cannot be caught out there," a call he applies to big boats too, not just small ones. NW 20–25 kt over 6–8 ft at San Nic / SBI / the outer banks is well past every one of those numbers.
- **Forecast error is asymmetric** — assume it errs on the worse side, and that afternoon W at the islands **strengthens** rather than eases (Academy Ep. 6, cited by date in the note). Corollary: **if it's windier than forecast in the morning, assume it builds all day and a small boat bails early** (7/14/22 report).
- **Captain's-call framing:** a big-red-flag forecast is a "we are not going," not a "let's see" (`NC3-3pJDEgo`).

**What I'd want before I trust the inshore leg:** the **swell period** for the 3–4 ft inside. The steepness rule is the whole game — *10 ft @ 15 s is barely felt; 3–4 ft @ 4–5 s is brutal*. Flag any zone or route segment where the period in seconds approaches the height in feet. You gave me height but not period, so I can't score the inside ride. Also check **current-vs-swell opposition**: a 4 ft @ 10 s forecast fishes like **6 ft @ 7–8 s** where the current runs against the NW swell.

Two more route notes from the same file:
- **Homebound wind.** Runs *south* put the wind on your return leg — plan the return **against** the afternoon build, not on the outbound conditions. From Dana Point that means if you run south to San Onofre/Barn, go early and be heading home before the build, not after it.
- **Bathymetric slop hotspots.** Where current accelerates over a ridge or shoal the swell stands up *locally* — one rough patch doesn't condemn a whole zone (Landesfeind's example is the ridge off Catalina's east end: horrible for a few miles, lays down 3–4 mi past it).
- If you're mourning the outside: the note also carries the **Catalina Eddy** case — the eddy can shield inner banks while it blows outside, so check eddy state before writing off *everything* offshore. That's a check, not a promise.

**What you're giving up:** `seasonal/september.md` puts the bigger bluefin in the **"volume square" — SBI–San Nicolas–Clemente–Catalina** (`5to3Q5P7w90`, cameron). That block is precisely your 6–8 ft. Dorado in September run in **open-water schools below Catalina**, also out of reach. And per `conditions/water-temperature.md`, dorado concentrate at the **green-cold/blue-warm coastal boundary around ~71–72 °F** — your 67–69 °F inshore is under that boundary anyway.

---

## 2. Primary program: calico bass on the kelp and hard bottom

`species/calico-bass.md` is the router. The load-bearing rule: **calico are current-driven and largely tide-indifferent** — you read the *current across the kelp*, not the tide clock. That's why this is the right call on a day whose only tide datum is a 10:20 low.

**Where (coordinates from `sources/spot-lists.md`, Dana Point + Oceanside sections):**

| Spot | Position |
| --- | --- |
| Monarch Boilers | 33 28.970 / 117 44.020 |
| Salt Creek | 33 28.565 / 117 44.040 |
| Dana Point Kelp — Red Buoy | 33 27.320 / 117 43.380 |
| Barber Poles | 33 26.710 / 117 41.410 |
| San Clemente Kelp (mainland city) | 33 24.450 / 117 38.140 |
| San Clemente Artificial Reef | 33 23.890 / 117 37.200 |
| San Mateo Point / Trestles | 33 22.960 / 117 36.800 · 33 22.790 / 117 36.280 |
| San Onofre Kelp | 33 20.880 / 117 34.050 |
| Barn Kelp | 33 17.015 / 117 29.475 |

The spot library gives **coordinates only — no depths** for these, so verify soundings on your own plotter. If you run north instead, the library flags MPAs: **Abalone Point — stay N/W of the MPA at 33 33.233 x 117 49.200**, and **The Hospital 100 Fathom Curve — stay S of the MPA at 33 30.050**.

**A near-exact seasonal precedent for this stretch:** a Dana Point–departing trip on **2022-10-11** worked south down the coast and found calico (with sand bass mixed) over **hard bottom with light kelp that did not reach the surface — kelp riding roughly 20 ft off the bottom in ~40–42 ft of water**. Same trip's pre-fish plan also flagged barracuda and **25–30 lb yellowtail** recently seen in that stretch (`HMdrP4-i9MM`; unregistered channel — medium confidence). Don't write off unbroken-looking water just because there's no surface canopy.

**Pick the spot on current, not the chart:**
- **Parallel-current rule** (`conditions/current-structure.md`): current running **parallel** to the shoreline (uphill or downhill) makes the edge fishable; **into the beach** is marginal; **off the beach is dead — skip it.**
- **Corner selection within a bed** (Dave Hansen, `kzD0kSnnVPw`, 2019-04-07 — registered voice, single mention on this framing, medium confidence): **current running downhill → work the NW corner of the kelp; running uphill → work the SE corner.** Same logic carries to rock structure.
- **Kelp lean is your current gauge** (`conditions/current-diagnostics.md`): **pulled ~20 ft under = raging** (surface presentations dead, go weighted); **laid down = strong** (fishable, work the down-current side); **resurfacing = slacking** (switch back to surface/lighter).
- **The edge is the spot.** Biting fish sit on the **up-current / leading edge**, facing into the current — "hit three or four sides of it and you know in two or three casts." Fish edges, pinch-points and isolated stringers, never the dense middle (Ep. 14; leading-edge/ambush mechanic also `Rwy4MqeXCIU`).
- **Water color:** a green-stained, near-opaque read with roughly **5–10 ft of visibility** was called the preferred kelp-edge color — the stain gives fish a place to hide and makes them feed up in the open (`9xNhdu2aBqE`, 2015-10-28, unregistered — medium confidence).
- **Bird tell:** **cormorants diving *in* the kelp** = actively feeding, a better calico tell inshore than gulls.

**Sonar picture:** calico mark **tight to kelp/structure edges and hard bottom**. Working depths run the **outside kelp edge ~50 ft in to ~25 ft**, and they'll rise **10–15 ft off 80–100 ft of reef** to eat a crankbait or a sunk iron. A **solid unbroken wall of bait has no predators on it; broken/harried bait does** — grade the mark before you commit.

**Technique, ranked for today (from the router's Situations table):**

1. **Weedless swimbait to the stringers** — short targeted casts, fast steady wind, pause on the eat. **7" weedless/MC slug on a keel-weighted hook: Gamakatsu 7/0, 3/8 oz, or a Trokar keel-weight.** Weights come half oz / 3/4 oz / nano; Landesfeind prefers the **3/4 oz** because it keeps the bait *in the water* while you wind fast. Replace the stock spring with an **Owner large** or **Trokar/Eagle Claw XL**, buried all the way so the plastic butts the hook — worth roughly **10x more fish per bait**. Line: **50–65 lb braid on a 300-size reel to 60 lb fluoro** (kelp chafes leader just from casting). A second, side-by-side data point runs **65 lb braid to 40 lb mono**, buttoned down tight (`9xNhdu2aBqE`).
2. **Surface iron along the kelp line** — and this is the wind-adapted choice. **Wind up → heavier iron:** step up to a **Salas 7X class** to punch the cast through it (`D5DR7Kx42_A`); a second source frames the same thing as one of three jigs you should carry — small-and-erratic for reaction, a Tady 45 for finesse, and a heavy one that casts through wind/chop (`A70kK2niu2Q`, medium confidence). For reference weights, a **surface iron runs 2–3 oz** vs a **5–6 oz yo-yo iron** (Scotty, `VpW91AKOFVQ`, registered — high confidence). **Counter-case:** if the forage is small anchovy ("rice"), drop to a light iron (Tady AA-light / A1-light, about **a third the weight of a Tady 45**) — on small bait the small jig out-bites the big one **two or three to one** (`pcwcRdmWmLc`). Those two rules pull opposite directions today; let the bait you actually see decide, not the wind alone.
3. **Flyline a sardine or mackerel** — the router explicitly lists this for "live bait around, fish deeper on the edge **or in wind**," 25–40 lb flyline class. It sweeps the up-current edge naturally.
4. **Raging current / kelp pulled under** → go subsurface (sunk iron, leadhead) or wait for the slack. Resurfacing kelp = go back on top.
5. **Chum-and-anchor** if you find a live edge: chum-bucket the spot, then reposition **up-current** and back the boat down onto it as the anchor sets — fish come out of the kelp as the anchor goes down (`RXNebDr4j7s`).

**Covering water is the method:** 10–25 casts to the prime edge, then move — 100 ft or 100 yards to the next stringers. If they're not on the prime spot they're usually not in the bed. Beds re-bite, so come back later (Ep. 13).

**Bait choice, Dana Point specifically — kept side by side, not reconciled** (`M6U_FVdosr4`, 2013-07-04, Dana Point kelp bed, unregistered — medium confidence): the boat anchored on a **light current running through the kelp bed**; that morning's first trip had produced **5 sand bass and 3 calico, every one on a strip of squid**. By day's end the same crew reported the fish were "actually biting the smaller sardines." Bring both.

---

## 3. Riding along: sand bass, barracuda, bonito

- **Sand bass** (`species/sand-bass.md`) mark **slightly above or within** the reef/wreck, not pinned to the bottom — cover the column. If they're locked down, **dropper loop**. With small anchovy, the **sliding (egg) sinker**: **1/2 oz egg + size-2 J hook**, slow-sink through the column on an **8–8.5 ft, 12–30 lb finesse fly-line class** rod. A big sand bass is ~6 lb, so **20 lb leader** gets it done.
- **Barracuda** (`species/barracuda.md`, medium confidence — the corpus has no dedicated barracuda program): they mark as **scattered, higher-in-the-column fish suspended along the kelp/structure edge**, looser and more mobile than the bass. **Retrieve the iron fast** — they chase a moving target. When you start getting cut off, add a **short single-strand wire (haywire twist)** or step to heavy hard mono; wire ends the cut-offs but costs bites.
- **Bonito** (`species/bonito.md`, medium confidence): read them as the **measure of life** — where they boil outside the kelp, the water is working. Cast small chrome jigs/small iron into the foam. There's a Dana Point data point: a **5:45 am** start, slow morning fishing **south of Dana Point Harbor then working north of it**, with **small feathers rigged as a small daisy-chain trolled at ~5.5 kt** and a **small sardine-profile hard bait (Rapala-class) cast and twitched** behind the boat also drawing bites (`poqjnb1r1zk`, 2019-07-02, Your Saltwater Guide).

---

## 4. Change-up: halibut

`species/california-halibut.md` — good use of an 8–12 kt breeze, because this is a **drift** fishery.

- **You cannot mark the halibut.** You mark the conditions that put one there. What you want is **sand within 5–20 ft of a hard edge** — a rock, shale reef, channel edge, low-relief rockpile, a bubbler, an eelgrass line. Even a **15-ft-wide rock that barely paints** changes the current, traps plankton, and gives a fish a place to lie (`OpcKQPA3vAI`).
- **The water triad — all three or leave:** off-color patch **+ current + bait**. Milky water alone is not a spot. If you're in it and not marking bait or catching *anything* — leopard shark, sargo, a small calico, any feeding sign — **leave inside 20–30 minutes.** The productive version is a dirty patch with a **hard rip / dirty foam edge** inside cleaner water (`OpcKQPA3vAI`, `6TBxHnkYXI0`).
- **Sonar:** hunt the soft/hard transition, and look for **bait pinned close to the bottom** — bait 20 ft down over 80 ft of water won't fire a halibut.
- **Drift discipline:** drift **along** the structure, not across it. Start **20 ft up-current**, end **20 ft past**. If it looked right and you got nothing, drift the other side.
- **Rig:** **trap rig** off a three-way with a **breakaway sinker**; **30 lb mono class** outside (mono for stretch on the bolting run), **2.5–3 ft of 25–30 lb fluorocarbon leader** — "the mono-leader guy is the one who blanks." **Ball/cannonball 1–10 oz** to conditions; ball weights bounce and kick the fish up off the mud. Artificial alternative: **drop-shot** a plastic near the bottom to pick apart rockpiles instead of long straight drifts.
- **Drift control in breeze** (`planning/search-and-glassing.md`, Scotty via `_ZThckj2TIM`, registered — high confidence): on arrival, **stop and watch which way and how fast the boat moves before dropping lines**; angle the outboard off the keel line to use it as a **rudder** to slow/steer the drift, or deploy a **drift sock**; pull the motor out of the water to speed a slow drift.

---

## 5. The long shots, honestly graded

- **White seabass** (`species/white-seabass.md`): it's a **squid-driven, gray-light-and-night, slack-tide** fishery, and the odds concentrate at low light. Your one tide datum — **low at 10:20** — actually gives you the discipline: **be on your highest-percentage spot an hour before the change**, so in place by ~09:20 (`conditions/tide-and-slack.md`). Same water triad as halibut, plus the spot check-in shorthand: **milky water + uphill/downhill current + structure line all "going together"** (`82gEHYel-4U`). Anchor **up-current** of the spot and let bait/chum drift back — WSB is not a bottom fish. Rig: **lead-head + squid** (2–3 squid threaded up the head, 3/4–1 oz), or a **dropper loop with the hook 12–18 in above the sinker** (`ShSxNKAcUB4`). Realistically: mid-morning, no squid intel, no low-light window — this is an opportunistic add if you land in the right dirty-water edge, not a plan.
- **Rockfish** (`species/rockfish-lingcod.md`): the coast has ground for it — **Box Canyon rockfish area 33 17.290 / 117 34.150**, **Leucadia rockfish area 33 04.100 / 117 20.600** (`sources/spot-lists.md`). Workhorse rig is a **dropper-loop gangion — two loops ~1.5 ft apart, 6/0 circle hooks, 24 oz torpedo on a light 12–15 lb breakaway**, baited with a **5–8" gulp/plastic grub** (white-glow / nuclear-chicken); scent fishes as well as live bait. **~90% of bites come on the first drop.** But the KB is explicit that the **season and depth limits are CDFW regulation, checked as of 2026-08 — verify current-year dates and depth constraints before you go.** I can't tell you today's depth band from this KB.
- **Lobster: no.** `species/california-spiny-lobster.md` puts the recreational season at **roughly early October through mid-March**, set by regulation, not water state. Late September is almost certainly before the opener — **confirm the exact date with CDFW** before you even load nets.

---

## 6. Running the day

1. **Bait first.** `bait/making-bait.md` has the Dana Point barge specifically (`7WapaxdtjQg`, Dave Hansen): **hail on VHF 11** with the barge's name twice plus your boat's name, wait for a response before approaching. **Never board the barge.** Follow the side signal — **at Dana Point, a cone on the ocean side**. Tell the attendant you want it **loaded light** and you're not in a rush. **Avoid the 6:00 a.m. rush** — the 3/4-day and half-day fleet all load then; go **5:00 or 7:00 a.m.** Tip at the end. Take both sardine and squid if they have it (see the Dana Point bait reversal above).
2. **First light on the closest live edge** — Monarch Boilers / Salt Creek / the Red Buoy kelp. Grade each bed in 10–25 casts.
3. **Read the kelp lean before you pick a presentation**, and re-read it every stop.
4. **Work outward with the wind at your back**, but plan the return against the build. If the inside is windier than forecast at 08:00, take that as "it builds all day" and shorten the plan.
5. **Around 09:20–10:20**, if you've found off-color water with current and bait, that's your halibut/WSB window on the low.

---

## 7. Gear, resolved against your profile

Your profile (`profiles/cameron/`) is an offshore/tuna kit, and that matters today:

| Job | Class term | Your gear |
| --- | --- | --- |
| Surface iron on the kelp line | jig-stick / surface-iron class (8–10 ft, 2–4 oz, 25–60 lb) | **Torium 20HG on the Phenix Abyss 10'0" (PSX-C 1009, 25–60 lb), 50 lb braid** — your dedicated surface-iron setup |
| Punching a cast into wind | heavier iron | **JRI-5** (biggest JRI), **Nomad Slidekick 120g / 4.25 oz** (heavier than traditional irons, can be sunk out). **JRI-7** is your "~Tady 45 class, local/kelp all-rounder" |
| Flylined sardine/mackerel on the edge | flyline class, 25–40 lb | **Avet MXJ on the Teramar 90MHB2, 50 lb braid** |
| Dropper loop / sinker rigs | yo-yo / heavy-iron class | **Trinidad 40 on the 8'0" XH 40–80, 80 lb braid** (heavier than this fishery needs, but it's what's rigged) |
| Weedless slug / plastics | **bass class** — 7–9 ft graphite-composite, low-profile 200–300 reel, 30–65 lb braid | **Nearest fit: the Tranx 400 on the Phenix M1 Inshore SMX-82H (8'2", H, 20–45 lb)** — but its braid is logged **TBD, respool pending** |

**Real gap:** `profiles/cameron/tackle.md` is complete as of 7/23/26 for **hard baits, casting and jigging only** — it lists **no soft plastics, no weedless slugs, no keel-weighted hooks, no leadheads**. The highest-percentage calico row in the router is exactly that program, so today it resolves to **class terms, not owned gear**: 7" weedless slugs + Gamakatsu 7/0 3/8 oz or Trokar keel-weight hooks + 60 lb fluoro. Buy or borrow, or fish the iron and the flyline and accept you're leaving the best presentation on the beach.

**Boat notes** (`profiles/cameron/boat.md`): the Panga Marquesas 22 has **no trim tabs** — engine trim is your only attitude control — and your own routine is **at least one person forward on the bow bean bag** underway, with the caveat that **rough days forward are brutal**. 3–4 ft is workable; it's the period I'd want first. **30-gal tank, Rule 401 500 GPH pump**, and **drain the tank coming in** (heavy stern water) with one person shifted aft. Also worth naming: **your home port is Dana Landing, Mission Bay** — Dana Point is a trailer launch for you, not the usual departure, so budget the tow. No drift sock is listed in the profile, and the drift-control doctrine above wants one.

---

## 8. Regulations (verify before you fish)

- **Calico bass / kelp bass and sand bass: 14 in minimum** (California/CDFW, as of 2026-08 — `r6j5w40fVHI`; the 14 in figure was also called out on camera on the 2022 Dana Point trip, `HMdrP4-i9MM`). **Verify current rules.**
- **California halibut: 22 in minimum**, as stated on camera 2016-11-23 (`MUpvP-Yl2R0`) — the KB flags this explicitly as a regulatory claim to re-check with CDFW.
- **Rockfish season and depth limits:** CDFW annual regs, as-of 2026-08 in the KB — **verify current-year dates and depth constraints.**
- **Lobster:** season roughly Oct–Mar; **confirm the opener with CDFW.**
- **MPAs** on the Laguna/Crystal Cove side, per the spot library: **stay N/W of the MPA at 33 33.233 x 117 49.200** (Abalone Point) and **S of 33 30.050** (Hospital).
- Local release ethic for the bass, from the corpus: "our bass are slow to grow, so let them go" — photo-and-release is the encouraged SoCal practice (`usHl-4SfqDA`). Handle by the **lower lip**, and per one tournament dock, **grab them by the middle of the body, not the tail**, to release.

---

## 9. What this KB can't tell you today

- **It has no chlorophyll scale.** `conditions/water-color.md` gives *new cold bloom (skip) vs mature bloom edge (fish)* and Cameron's "won't fish dirty green water" rule — but **no numeric thresholds**, so I can't tell you whether **1.2 along the kelp** is good green or dead green. The test the KB *does* give: if there was an **overnight ~5 °F drop plus green water after an afternoon NW wind**, that's a **local upwelling event — short-term negative, mark it for the recovery, don't expect it to fish today.** With NW 20–25 offshore, that's a live possibility worth checking against yesterday's SST.
- **It has no SST band for any inshore species.** 67–69 °F can't be scored for calico, sand bass, barracuda, bonito, halibut or WSB. The only temperature anchor near your numbers is the dorado boundary at ~71–72 °F.
- **You didn't give me a swell period or the moon phase**, and both change the plan — see the steepness rule above, and the moon rule below.
- **Moon matters and I don't have it.** On clear full-moon nights calico gorge after dark and **shut down by mid-morning** — bite early, then dead until late day, and the same suppression applies to sand bass. If we're near a full moon, front-load the day hard and plan a late-afternoon second session.
- **Current direction and strength for today weren't given**, and the parallel-current rule — the single most load-bearing call in this plan — depends entirely on it. Read it on the water off the kelp lean and the chum-drift angle.

<sub>Sources are the KB notes named inline; video IDs are carried from those notes. Several inshore data points come from unregistered channels and are held at medium confidence in the KB — I've flagged those where I used them.</sub>


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `conditions/sea-state.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/tide-and-slack.md`, `conditions/water-color.md`, `conditions/water-temperature.md`, `conditions/kelp-paddies.md`, `seasonal/september.md`, `seasonal/october.md`, `species/calico-bass.md`, `species/sand-bass.md`, `species/barracuda.md`, `species/bonito.md`, `species/california-halibut.md`, `species/white-seabass.md`, `species/rockfish-lingcod.md`, `species/yellowtail.md`, `species/california-spiny-lobster.md`, `species/ocean-whitefish.md`, `species/spotted-bay-bass.md`, `techniques/surface-iron.md`, `techniques/swimbaits.md`, `techniques/flyline.md`, `techniques/dropper-loop.md`, `techniques/inshore-crankbaits.md`, `tackle/gear-classes.md`, `locations/bass-structure.md`, `locations/breakwalls-jetties-riprap.md`, `locations/bays-and-harbors.md`, `bait/making-bait.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`  
*videos:* `NC3-3pJDEgo`, `5to3Q5P7w90`, `HMdrP4-i9MM`, `M6U_FVdosr4`, `poqjnb1r1zk`, `r6j5w40fVHI`, `Rwy4MqeXCIU`, `9xNhdu2aBqE`, `RXNebDr4j7s`, `kzD0kSnnVPw`, `D5DR7Kx42_A`, `pcwcRdmWmLc`, `VpW91AKOFVQ`, `A70kK2niu2Q`, `7WapaxdtjQg`, `OpcKQPA3vAI`, `6TBxHnkYXI0`, `82gEHYel-4U`, `ShSxNKAcUB4`, `MUpvP-Yl2R0`, `usHl-4SfqDA`, `_ZThckj2TIM`, `P6Slg6RQiXw`  
*gaps admitted:* No numeric chlorophyll scale anywhere in the KB — it cannot say whether 1.2 along the kelp is fishable green or dead green; only the new-cold-bloom vs mature-bloom-edge distinction is given. | No SST band for any inshore species (calico, sand bass, barracuda, bonito, halibut, white seabass), so 67–69 F cannot be scored; the only nearby temperature anchor is the dorado ~71–72 F coastal boundary. | Swell period for the inshore 3–4 ft was not supplied, and the KB's steepness rule (10 ft @ 15 s vs 3–4 ft @ 4–5 s) cannot be applied without it. | Moon phase was not supplied, so the calico/sand-bass full-moon suppression rule (gorge at night, shut down by mid-morning) cannot be applied. | Current direction and strength for today were not supplied, and the parallel-current rule that governs every kelp spot choice depends entirely on it. | sources/spot-lists.md gives coordinates only for the Dana Point and Oceanside spots — no depths, no bottom descriptions, no bed extents. | The KB has no Dana Point Harbor note; bays-and-harbors covers San Diego Bay, Mission Bay, Newport and the LA/Long Beach complex only, so there is no in-harbor fallback detail for a Dana Point launch. | Current-year CDFW rockfish season dates and depth limits are not in the KB — the note explicitly defers to CDFW (as-of 2026-08). | The exact spiny lobster opener date is not in the KB (only 'roughly early October'), so whether late September is open must be confirmed with CDFW. | No live squid availability intel — squid is the driver for the white seabass program and the KB is not a conditions source. | Bounce-ball trolling for halibut on coastal flats is a flagged stub in the router — no corpus source covers it. | Barracuda has no dedicated program in the corpus; everything in that router is inferred from mixed-bag report mentions and held at medium confidence. | The KB has no small-craft-advisory or sea-state threshold specific to a 22 ft panga — the go/no-go numbers used are boat-agnostic and held at medium confidence (single-mention, dave-hansen). | profiles/cameron/tackle.md inventories hard baits, casting and jigging lures only — it lists no soft plastics, weedless slugs, keel-weighted hooks or leadheads, so the highest-percentage calico presentation cannot be resolved to owned gear. | No drift sock is listed in the profile, though the drift-control doctrine calls for one on a breezy halibut drift.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Blown out outside, wide open inside — fish the Dana Point → Oceanside coastal strip

## 1. The envelope (this is binding for everything below)

Per step 1b of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), the day's `{regions, waters}` from your launch point and today's numbers:

- **regions:** `socal-bight`
- **waters:** `nearshore-coast` (+ `bay-harbor` if you bail into the harbor)
- **NOT reachable today:** `island`, `bank`, `open-ocean`

Anything the KB tags outside that set is not offered today, not offered with a caveat — that's the protocol's rule, and it's why you won't see dorado, yellowfin or bluefin below (all gated `waters: [open-ocean]` / `[open-ocean, bank]` in `species/dorado.md`, `species/yellowfin-tuna.md`, `species/bluefin-tuna.md`).

**One thing I need from you:** your boat file [`profiles/cameron/boat.md`](profiles/cameron/boat.md) has `range_nm: null` and `sea_state_max_ft: null` — the comment in that file says the protocol must **ask** rather than assume. So: the plan below assumes you're staying inside the 3–4 ft / 8–12 kt band and not crossing anything. If your real limit is higher than I'm assuming, tell me and I'll re-run it. (The profile also lists your launch as Dana Landing, Mission Bay — I'm using Dana Point as you gave it.)

## 2. Why outside is a no, in the KB's own numbers

[`conditions/sea-state.md`](conditions/sea-state.md):

- The one explicit go/bail threshold set in the corpus (dave-hansen, `NC3-3pJDEgo`, 2020-11-18, held at medium confidence as a single-mention claim): **wind over ~12 kt is what raises whitecaps**, and his personal cutoff is not running above 12 kt. NW 20–25 is double that.
- Same source names **12–15 kt with 4–8 ft swell at a 9-second interval** as a flat "you cannot be caught out there" combo — and he holds *bigger* boats at the dock in it, not just small ones. You have more wind and the same sea height.
- **Forecast error is asymmetric** (Landesfeind Ep. 6): assume the forecast errs on the worse side and that afternoon W at the islands strengthens rather than eases.
- **Homebound wind** (8/17/22): plan the return leg against the afternoon build, not the outbound conditions. A downwind run out to San Nicolas/SBI feels fine; the beat home is the part that hurts.

The good news is geographic and it's in [`locations/bight-geography.md`](locations/bight-geography.md) (`HzE4FHHcvTk`): a big NW blow **crushes the northern Channel Islands and the LA/Ventura shelf** (5–8 °F of surface rollover), but **south of Newport is "less prone to wind-wave-driven rollovers."** You are south of Newport. Your 67–69 °F inside water is exactly the water that survives this pattern.

*One caveat I can't resolve without live data:* the same note logs the **Catalina Eddy shield** — the eddy can hold the inner banks down while it blows outside (5/26/22). If you ever want to re-open the outside question, that's the check. I'm not fetching it, and you gave me no numbers for Catalina or San Clemente, so I'm treating everything past the coastal strip as unknown, not as fishable.

## 3. The clock — low tide 10:20

From [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md):

- **Be on your highest-percentage spot by ~09:20** — an hour *before* the change, not at it (2/20/25).
- **Window compression:** when conditions are marginal, the action compresses into the tide windows; wide-open days bite all day. Today is a wind-affected day, so anchor the plan to the tide clock and be disciplined about arriving early to each stop.
- Your tide is **falling through 09:30 into a 10:20 low**, which is the note's stated **late-morning slack pop-up window** (7/14/22, 10/26/22) — though it frames that specifically as an *open-water* pop-up rule, so treat it as a reason to keep your eyes up, not as a bass rule.
- **Important nuance:** calico bass are listed in that note's table as **current-driven and tide-indifferent** — for the kelp they care about current across the structure, not the clock. The fully tide-driven fish is the **harbor spotted bay bass**.

**Suggested shape of the day:**
- Bait first (see §6), then out.
- **08:00–09:15** — work the closest kelp (Dana Point Kelp / Red Buoy) while the tide still runs.
- **09:20–11:30** — be parked on your best edge across the low and the turn.
- **Midday** — reposition down the strip (Barber Poles → San Clemente Kelp → San Onofre / Barn Kelp) working the flood, or drop onto hard bottom.
- **Late afternoon** — the dawn/dusk hour is the other high-percentage window per the n6yun panel in [`species/calico-bass.md`](species/calico-bass.md) (`RUuPNpK0x-s`, medium confidence): the hour before sunset.

## 4. What's fishable, ranked

### #1 — Calico bass on the kelp line (the day's primary)

[`species/calico-bass.md`](species/calico-bass.md), [`locations/bass-structure.md`](locations/bass-structure.md).

**Why it's #1 today:** it's a coastal kelp/reef fishery that lives inside your envelope, and your water is right in the stated band. Tommy Ponce — a kayak guide fishing **Dana Point** specifically (Fisher Newb seminar, `LqW32NSkObY`, 2019-03-13; medium confidence) — gives a personal temperature preference of **65–68 °F**, with fish getting lethargic and dropping to cooler water past about 70 °F. Your 67–69 °F straddles the top of that. His stated Dana Point working depths: **0–8 ft and 20–100 ft**, occasionally a bit past 100.

**Charted spots on your strip** (from your own library, [`sources/spot-lists.md`](sources/spot-lists.md) — public per your 2026-08-12 waiver):
- The Hospital 100 Fathom Curve — 33 29.500 / 117 47.100 (**stay S of the MPA line at 33 30.050**)
- Monarch Boilers — 33 28.970 / 117 44.020
- Salt Creek — 33 28.565 / 117 44.040
- **Dana Point Kelp — Red Buoy — 33 27.320 / 117 43.380**
- Barber Poles — 33 26.710 / 117 41.410
- San Clemente Kelp (mainland city) — 33 24.450 / 117 38.140
- San Clemente Artificial Reef — 33 23.890 / 117 37.200
- San Mateo Point — 33 22.960 / 117 36.800
- San Onofre Kelp — 33 20.880 / 117 34.050
- Barn Kelp — 33 17.015 / 117 29.475

**How to pick the edge:** the **parallel-current rule** governs (Ep. 14) — current running **parallel** to the shore/kelp makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage, skip it. Fish the **up-current / leading edge** of each kelp head; calico face into the current and ambush from the front (Benny Florentino, `Rwy4MqeXCIU`). Hit three or four sides of a head and you know in two or three casts.

**Depths / marks:** typical working depth is the **outside kelp edge ~50 ft in to ~25 ft**, and calico will rise **10–15 ft off 80–100 ft of reef** to eat a crank or a sunk iron. A solid unbroken wall of bait usually has no predators on it; broken, harried bait does.

**Cover water:** 10–25 casts to the prime edge of a bed, then move — 100 ft or 100 yards to the next patch of stringers. Beds re-bite, so come back later (Ep. 13).

**Presentations, in the order today's conditions rank them:**
1. **Weedless swimbait** — 7" slug on a **3/8–3/4 oz keel-weighted spring hook**, short targeted casts to individual stringers, fast steady wind, pause on the eat. Heavy fluoro leader (40–65 lb) for kelp abrasion. ([`techniques/swimbaits.md`](techniques/swimbaits.md))
2. **Surface iron** along the kelp line, steady grind. **In wind, step up to a heavier iron to punch the cast through it** ([`techniques/surface-iron.md`](techniques/surface-iron.md), `D5DR7Kx42_A`). At 8–12 kt this is a real factor.
3. **Flylined sardine/mackerel** on the up-current edge — the note's row for "live bait around, fish deeper on the edge **or in wind**," 25–40 lb class.
4. **If the current rages and the kelp pulls under** — surface presentations are dead; go subsurface (sunk iron, leadhead) or wait for the slack.

**A Dana-Point-specific data point worth carrying:** StokedOnFishing, 2013-07-04, Dana Point kelp bed aboard a Dana Wharf boat (`M6U_FVdosr4`) — they **anchored** rather than drifted on a light current running through the kelp, and that morning's tally was **5 sand bass and 3 calico, every one on a strip of squid**; by day's end the crew said the bass were "actually biting the smaller sardines." Both kept side by side in the note — so carry squid strips *and* small bait.

**Water color:** your chlorophyll 1.2 along the kelp — see §9 for what I can and can't say about that number. What the KB *does* give (StokedOnFishing, 2015-10-28, `9xNhdu2aBqE`, medium confidence) is that a **green-stained, near-opaque kelp edge with roughly 5–10 ft of visibility is the preferred read for kelp-edge bass** — the stain gives fish a place to hide and makes them feed up more comfortably. A colored kelp line is not a problem for this program.

### #2 — Barracuda and bonito on the same edges (free upgrades)

[`species/barracuda.md`](species/barracuda.md), [`species/bonito.md`](species/bonito.md) — both `nearshore-coast`, both in-season (barracuda are a late-spring-into-fall nearshore fishery; bonito run spring through fall).

- **Barracuda:** cast the iron and **retrieve fast** — they chase a moving target. Small chrome jigs when they're on small bait. There's one dated SoCal iron data point (`oadK6zIYyCo`, Catalina, 2016): an old Tady 45 **let sink to roughly 30 ft** before the retrieve. **Rig for the teeth** the moment you get cut off — a short single-strand wire ([`rigging/haywire-twist.md`](rigging/haywire-twist.md)) or heavier hard mono as the line-shy compromise.
- **Bonito:** cast small flashy iron/jigs into the foam outside the kelp. The KB frames them as a **measure of life** — a boil tells you the zone is working. There's a Dana Point trolling report in the note (Your Saltwater Guide, `poqjnb1r1zk`, 2019-07-02): a 5:45 am start south of Dana Point Harbor then north, **small feathers rigged as a small daisy chain trolled at ~5.5 kt**, plus a small sardine-profile diver cast and twitched behind the boat.

### #3 — Sand bass on the hard bottom / reef-to-sand transition

[`species/sand-bass.md`](species/sand-bass.md) (`nearshore-coast, bay-harbor, bank`).

Be honest about the timing: the note's headline event is the **summer spawn, peaking around late June–July** on the open flats. Late September is past that, and the winter deep-structure program hasn't started. What still applies today is the general read: they hold on hard bottom, high spots, wrecks and the **hard-to-soft transition**, and they mark **slightly above or within** the structure, not pinned to it — so cover the column.

There's a directly relevant local observation (`HMdrP4-i9MM`, 2022-10-11, off North County San Diego near Camp Pendleton, medium confidence): sand bass mixed into the calico catch on **hard bottom with kelp not reaching the surface, ~40–42 ft**. That's a good description of half the ground between San Onofre and Oceanside.

Presentations: **paddle-tail plastics on a leadhead**, cast-and-wind low and slow through the column (get bit on the sink — watch the free-spool for the speed-up/tap); **sliding egg-sinker live anchovy** (1/2 oz egg + size-2 J, slow-sink); **dropper loop** when they're pinned down. A big sand bass is ~6 lb, so 20 lb leader gets it done.

### #4 — Halibut on the sand next to structure (the wind actually helps)

[`species/california-halibut.md`](species/california-halibut.md).

**The rule that matters:** not "sandy bottom" — **sand within 5–20 ft of a hard edge** (`OpcKQPA3vAI`). A 15-ft-wide rock that barely paints changes the current, traps plankton and gives a halibut somewhere to lie. On the coast specifically: **off-color water just outside the surf line where hard bottom (shale) sits outside the beach and bait gets pushed in** — the note cites a 40–50 lb fish off a Huntington bubbler zone in **30 ft**.

**Timing is on your side:** Tackle Express / Shannon Gallagher (`ghHQe3fP9U4`, 2025-11-04, medium confidence) states halibut push into **less than 15 ft of water in spring and in fall**, and splits the fishery — bigger fish spend most of their time in **80–200 ft**, harbor fish run **17–33 in**.

**The triad, and it's a hard gate:** off-color water **+ current + bait**, all three. Milky water alone is not a spot. If you drop in and aren't marking bait or catching *anything* — a leopard shark, a sargo, a small calico — **leave inside 20–30 minutes**. The premium version is a dirty patch with a **hard rip / foam edge** inside otherwise cleaner water.

**Rigs:** **trap rig** (stout bait hook + 3–4X-strong treble stinger) off a **three-way with a breakaway clip**, ball/cannonball **1–10 oz** to conditions, **fluorocarbon leader 2.5–3 ft, 25–30 lb** — the note is blunt that the mono-leader guy is the one who blanks. **30 lb mono class** outside for the stretch on the bolting run. Artificial alternative: **drop-shot** a plastic on short drifts, or a **crankbait/jerkbait wound noticeably faster than instinct suggests** — halibut give chase.

### #5 — Coastal hard bottom: rockfish, lingcod, sheephead

[`species/rockfish-lingcod.md`](species/rockfish-lingcod.md) (`bank, island, nearshore-coast`), [`species/sheephead.md`](species/sheephead.md).

Season is **open most of the year, closing around year-end** (CDFW, as of 2026-08 — **verify current-year dates and depth limits before you go**). This is a **meter-and-chart fishery, no surface sign**: run the contour, read **where hard meets soft**, and **mark every hard-bottom hit as a waypoint** with the track line running so you can circle back (`11npFUPOJKU`). What you want is a **distinct pinnacle or hump rising 20–30 ft** off the surrounding floor, with a bait cloud up high and **arches on the hard bottom** under it. Run **low + high frequency split screen** — low paints the bait cloud, high distinguishes the gamefish arches.

Where the drift lays your bait decides the species (Capt. Scotty, Brothers Sportfishing, `_ZThckj2TIM`, high confidence): **reds/vermilion sit tight to the rock**; **bocaccio hold in the sand off it**.

Charted coastal options from your library: **Box Canyon rockfish area — 33 17.290 / 117 34.150**, **Leucadia rockfish area — 33 04.100 / 117 20.600**, **Del Mar rockfish area — 32 57.191 / 117 17.981**, plus the **Pendleton AR cluster (33 19.5 / 117 31.7)** and the **Oceanside AR 1A–2L / Carlsbad AR 1–12** clusters.

**Rig:** dropper-loop gangion, two loops ~1.5 ft apart, **6/0 circle hooks**, **24 oz torpedo on a light 12–15 lb breakaway**, 30–40 lb mono leader (rockfish aren't leader-shy), **30 lb braid** for a fast straight drop. Bait a 5–8" gulp/plastic grub — scent fishes as well as live bait and you carry no squid.

**Sheephead** ride along on the artificial reefs: **chum first**, then a **1/4–1/2 oz slider** with a **No. 2 or No. 4 thin-wire bronze hook** (never chrome), bait **suspended off the bottom, never laid on it** — a bottomed bait draws bat rays and shovelnose instead. Pismo clam is the named premium bait; squid strips are the fallback.

### #6 — The one pelagic still legal in today's envelope: yellowtail

[`species/yellowtail.md`](species/yellowtail.md) is tagged `island, bank, nearshore-coast, open-ocean`, so the nearshore version stays on the menu. Two rows are directly on point:

- **"Hard wind (20–25 kt+) after a run of good surface days — fish still there, no longer showing on top"** → **1) yo-yo iron, 2) keep casting surface iron as a picker** (Coronado Islands, 2026-04-21, `ejUTAnONf7o`, Jared Saaib; medium confidence — 25 kt gusts, the crew's read was that the wind turned the bite and the day went "mostly yo-yo," but the surface iron still produced two, so it's a re-rank, not an abandonment). Yo-yo target picture: **tight balls hugging structure, marks on hard bottom or pinnacles at ~5–10 fathoms** — heavy full-size iron (Salas 6X class), hit bottom, **a couple cranks off the bottom is the reaction bite**, 40–60 lb stout rod + high-speed reel.
- **"Prospecting an unworked zone"** → **troll diving hard baits to cover water fast** (Nate Winnicki, BDOutdoors, `HTowqnwAMeA`; registered voice, medium pending repetition). Carry variety across three axes — **colour, style/profile, dive depth**. Colour by light and it runs opposite to intuition: **overcast/low light → high-visibility; bright clear blue day → darker** (blues, purples, reds). **20–30 ft divers run fine off the flyline outfit**; only 40 ft divers need a dedicated troll rod.

**On paddies:** [`locations/bight-geography.md`](locations/bight-geography.md) and [`conditions/kelp-paddies.md`](conditions/kelp-paddies.md) both name **the coastal strip from Dana Point to Oceanside and southward** as the *best* paddy water in the Bight (paddies thin out and hold fewer fish north of Dana Point). If you cross a paddy inside your fishable band: **drive right up to it like it's the dock** — don't sneak (Dave Hansen, `ZFqe49jRgA0` + `8XrMkWPRxgs`, repeated doctrine, high confidence); look under it for visible fish, check the meter for **boomerang-shaped arcs, typically 90–120 ft** down; give it **about a minute, maybe two**, then move. **A dry paddy stays dry all day** — they only restock at night (`4xzK7YaXK5s`). Note that paddies aligned by current run roughly **N–S in open water**, so if one produces, search that line.

### Bail-out — Dana Point Harbor

If it gets uglier than forecast, [`species/spotted-bay-bass.md`](species/spotted-bay-bass.md) (`socal-bight`, `bay-harbor`) is the note's explicit fallback for "marginal weather when the outside coast is blown out." Spotties are **fully tide-driven** — set up **up-current of the structure** and re-read after the turn. Roman Castro (`EGKesj7V64M`, medium confidence): the **half hour either side of the turn is the dead window** — fish the moving water on either side of 10:20, not the turn itself; **cast up-current across the grain of the eelgrass** (blades lean like a flag); and if you snag **brown, decaying grass, move to green** — brown grass is releasing CO2 and that water runs less oxygenated. Jeremy (`lP6cg4eEU6s`, medium confidence): on the **falling/low tide they pull off the flat onto the adjacent drop-offs**, which is exactly your 10:20 situation. Working depths **12–14 ft**, on breaks as subtle as 17 ft rolling up to 12 ft.

Note: the KB's harbor structure note [`locations/bays-and-harbors.md`](locations/bays-and-harbors.md) covers San Diego Bay, Mission Bay, Newport, Huntington and the LA/Long Beach complex — **it does not have a Dana Point Harbor breakdown**. The universal read still applies: eelgrass edges, channel drop-offs, docks/pilings (**favor old weathered pilings over new** — established growth holds fish, `usHl-4SfqDA`), and riprap **deviations** — points, pockets, corners, angle changes, not the featureless straightaways ([`locations/breakwalls-jetties-riprap.md`](locations/breakwalls-jetties-riprap.md), Ep. 9). **Birds sitting on the rocks mark the deviation.** When casting a wall, **close the bail the instant the lure hits** — the face sits at ~45° and slack line buries a leadhead in the rocks.

## 5. Gear, resolved against your profile — and the gaps

From [`profiles/cameron/rods.md`](profiles/cameron/rods.md) and [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md):

| Today's job | What you own | Fit |
| --- | --- | --- |
| Surface iron on the kelp line | **Torium 20HG / Phenix Abyss 10'0" 25–60 lb, 50 lb braid** — your full surface-iron setup | Exact match to the jig-stick class |
| Iron selection | **JRI-7** (~Tady 45 class, your "local/kelp all-rounder"); **Nomad Slidekick 120g / 4.25 oz** for the wind (heavier, and can be sunk out — matches the cuda sink-to-30-ft trick); **Strictly Irons Mighty 5.5"** for the fast retrieve on cuda/bonito; **Strictly Irons Glory 7"** as the slow drawn-out change-up for picky/slack current | Good coverage. The Slidekick is the "wind up → heavier iron" answer |
| Yo-yo, if you find bait balls on hard bottom | **Salas 6X / Salas CP 105** on the **Trinidad 40 / Rainshadow 8'0" XH 40–80, 80 lb braid** | Rod is right in the 40–60 lb class. The note wants a **high-speed reel** to burn the iron off the bottom — your profile doesn't record the Trinidad's ratio, so verify |
| Flyline | **Avet MXJ / Teramar 9'0" MH 30–65 lb, 50 lb braid** | Exact match to the 25–50 lb flyline class |
| Prospect-trolling divers | **Rapala Husky Magnum 25** (= **25 ft at ~33 yd setback**, best **6–8 kt**, 40–50 lb line, low gunnel holder) and **HM15** (15 ft); **Halco Laser Pro 190 XDD** (20+ ft, 3–11 kt, optimum 6.5) | Right in the 20–30 ft diver band — which the KB says the **flyline outfit** handles, no second rod needed. Your **TLD 20 / Seeker 660H** is already earmarked for diver duty |
| Bonito daisy chain | **Williamson Tuna Catcher**, JAW dual-skirt lures, dad's feather bag | Matches the ~5.5 kt small-feather chain from the Dana Point report |

**Gaps I have to name rather than paper over** (step 4 of the protocol says never substitute something that doesn't fish the same way):

- **The day's #1 program has no bait in your box.** The calico kelp-edge program wants **7" weedless slugs on 3/8–3/4 oz keel-weighted spring hooks**, leadheads, and 40–65 lb fluoro. Your recorded inventory ([`profiles/cameron/tackle.md`](profiles/cameron/tackle.md)) is hard baits, irons and poppers only — no soft plastics, no leadheads, no weedless hardware. Buy them on the way to the ramp, or accept that you're fishing this day on **iron + flylined bait**, which will work but gives up the highest-percentage presentation.
- **No inshore bass rod.** The class is a **7–8 ft graphite-composite bass rod, 200–300 size reel, 30–65 lb braid**. Your closest is the **Tranx 400 on the Phenix M1 SMX-82H (8'2", H, 20–45 lb, 3–8 oz)** — a heavier reel than the class calls for, and the profile lists its braid as **TBD, respool pending**. Sort the line before you leave.
- **No bottom terminal recorded.** The rockfish/sheephead programs want gangions, 6/0 circles, 24 oz torpedoes, light breakaway line, and 1/4–1/2 oz sliders with No. 2/No. 4 bronze hooks. None of that is in your profile files.
- **No light spinning / drop-shot outfit** for spotties or the halibut drop-shot row.

## 6. Bait

[`bait/making-bait.md`](bait/making-bait.md) has a **Dana Point-specific** barge section (dave-hansen, `7WapaxdtjQg`, 2022-01-04):

- **Never board the barge** — ask the attendant for help rather than jumping off to fend the boat.
- **At Dana Point the side signal is a cone on the ocean side** — tie to the side they mark.
- **Hail on VHF 11** if no attendant is visible: barge name twice, then your boat's name, then wait.
- **Tell them to load it light** and that you're not in a rush.
- **Avoid the 6:00 a.m. rush** — every half-day, 3/4-day and charter boat loads then. Go at **5:00 a.m. or 7:00 a.m.**; the same presenter's own target at a later seminar (`bM2vUS1B-yQ`) is "at least five, if not four thirty."

Your own split (source `cameron`) is: **buy sardines; when you make bait, it's always mackerel** — sabiki to **~100 ft with an 8 oz sinker**, which has loaded five 12-inch macks on one drop. Twelve-inch mackerel are heartier baits than sardine. Given the day's targets, a mixed tank plus **squid strips** covers the Dana Point kelp observation above.

## 7. What you're reading once you're out there

- **Kelp lean is your current gauge** ([`conditions/current-diagnostics.md`](conditions/current-diagnostics.md), Ep. 14): **pulled ~20 ft under = raging** (surface presentations dead, go deep); **laid down = strong** (fishable, work the down-current side); **resurfacing = slacking** (switch back to the surface). Watch the kelp, not the clock.
- **Separate wind push from real current:** chum drifting straight back in line with the boat = wind-dominated; chum swinging **off at an angle** to the boat's lay = real current cutting across. On today's 8–12 kt this matters — and note the KB's warning that **a chart plotter's current-arrow layer is reading wind, not current** (`BskCsKaTiZw`, medium confidence).
- **Birds:** **cormorants diving *in* the kelp = actively feeding**, a better calico tell than gulls inshore. Birds sitting on riprap mark the current deviation.
- **Grade the bait mark before you commit:** solid unbroken wall = no predators; broken/harried bait = predators on it (Ep. 5).
- **Casting distance:** on a beach stop the fish are usually within **30–40 yards of the boat**, not way out (Doug Kearn, `r9bF3VtzDUg`, medium confidence).

## 8. Explicitly NOT today

- **Bluefin, yellowfin, dorado, marlin, swordfish** — all gated to `open-ocean`/`bank`, which is out of the envelope. September's priors ([`seasonal/september.md`](seasonal/september.md)) put the bigger bluefin in the **SBI–San Nicolas–Clemente–Catalina "volume square"** and dorado in open-water schools below Catalina; that's precisely the water that's 6–8 ft today.
- **Lobster.** [`species/california-spiny-lobster.md`](species/california-spiny-lobster.md) puts the season at roughly **early October through mid-March** — late September is before the opener. Confirm the exact date with CDFW; don't set nets on a hunch.
- **White seabass** is region- and waters-legal (`island, nearshore-coast`), but the KB's program for it is **island squid beds in 60–100+ ft, moon-driven, gray light and night**. You gave me no moon phase, the islands are out, and I have no report of squid or off-color water on your strip. If you *do* run into a dirty-water patch with a hard rip edge, current and bait all together, that's the triad and it's worth 20–30 minutes with a lead-head-and-squid or a slow-worked surface iron — but I'm not planning the day around it.

## 9. Regulations (verify before you fish)

The KB carries these as jurisdiction-stamped claims, not current law:
- **California / CDFW, as of 2022-04-25: 14 in minimum for sand bass** (and the same 14 in figure called out on camera for calico) — [`species/sand-bass.md`](species/sand-bass.md).
- **Rockfish: open most of the year, closes around year-end; depth constraints apply** (as of 2026-08) — verify current-year dates *and* depth limits.
- **Spiny lobster: roughly Oct–mid-March, 7 per person per day** (as of 2026-08).
- **MPA lines on your own spots:** The Hospital — **stay S of 33 30.050**; Abalone Point (Crystal Cove) — **stay N/W of 33 33.233 × 117 49.200**; Encinitas/Devil's Rock North — **stay N of 33 03.000**.

Verify all of it with CDFW before you leave the dock — the KB does not carry a current, complete bag/size table.

## 10. Where the KB came up short today

Listed plainly rather than filled in from anywhere else — see `gaps_admitted`. The big three: **chlorophyll 1.2 can't be graded against any numeric scale in this KB**, **your boat's sea-state and range limits are blank in your own profile**, and **the September priors page has nothing at all about the inshore coastal program** — everything below is assembled from the species routers and conditions layers, not from a seasonal prior for this exact week.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `locations/regions.md`, `locations/bight-geography.md`, `locations/bass-structure.md`, `locations/bays-and-harbors.md`, `locations/breakwalls-jetties-riprap.md`, `seasonal/september.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/water-color.md`, `conditions/water-temperature.md`, `conditions/current-diagnostics.md`, `conditions/kelp-paddies.md`, `species/README.md`, `species/calico-bass.md`, `species/barracuda.md`, `species/bonito.md`, `species/sand-bass.md`, `species/california-halibut.md`, `species/white-seabass.md`, `species/rockfish-lingcod.md`, `species/sheephead.md`, `species/spotted-bay-bass.md`, `species/yellowtail.md`, `species/california-spiny-lobster.md`, `techniques/surface-iron.md`, `techniques/trolling.md`, `techniques/wind-in-your-face-positioning.md`, `bait/making-bait.md`, `bait/fishing-live-bait.md`, `lures/rapala-husky-magnum.md`, `lures/halco-laser-pro.md`, `profiles/cameron/README.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`  
*videos:* `NC3-3pJDEgo`, `HzE4FHHcvTk`, `LqW32NSkObY`, `RUuPNpK0x-s`, `Rwy4MqeXCIU`, `9xNhdu2aBqE`, `M6U_FVdosr4`, `r9bF3VtzDUg`, `D5DR7Kx42_A`, `oadK6zIYyCo`, `poqjnb1r1zk`, `HMdrP4-i9MM`, `OpcKQPA3vAI`, `6TBxHnkYXI0`, `ghHQe3fP9U4`, `11npFUPOJKU`, `_ZThckj2TIM`, `OSbAHdB4uPs`, `EGKesj7V64M`, `lP6cg4eEU6s`, `usHl-4SfqDA`, `ejUTAnONf7o`, `HTowqnwAMeA`, `ZFqe49jRgA0`, `8XrMkWPRxgs`, `4xzK7YaXK5s`, `BskCsKaTiZw`, `7WapaxdtjQg`, `bM2vUS1B-yQ`, `5to3Q5P7w90`  
*gaps admitted:* Chlorophyll 1.2 cannot be graded — conditions/water-color.md gives no numeric chlorophyll scale or thresholds anywhere; it only gives bloom-age doctrine (new cold-green bloom vs mature bloom edge), the bait-in-the-dirty-water/fish-the-seam rule, and Cameron's warm-year clarity preference. I used those qualitatively and did not assign a value judgment to the number 1.2. | Your boat's operating envelope is blank — profiles/cameron/boat.md has home_port, range_nm and sea_state_max_ft all null, with an explicit note that the protocol must ASK rather than assume. I assumed you are staying inside the 3-4 ft band; nothing in the KB says what sea state a Panga Marquesas 22 will take. | seasonal/september.md has no inshore/coastal content at all — it covers only the offshore volume square, dorado below Catalina, yellowfin sliding north, and the Baja/BOLA bottom yellowtail program. There is no September prior for the Dana Point-to-Oceanside kelp/bass fishery. | No Dana Point location note exists — locations/ has no page for Dana Point, Dana Point Harbor, or the Orange County coastal strip. All spot names and coordinates I used came from Cameron's personal library in sources/spot-lists.md, not from universal locations knowledge, and there is no structure breakdown for any of them. | locations/bays-and-harbors.md does not cover Dana Point Harbor — it names San Diego Bay, Mission Bay, Newport, Huntington Harbour and the LA/Long Beach complex only. The harbor bail-out plan is the universal structure read applied by analogy. | No moon phase was given and I did not compute one, so the moon-gated doctrine is unused: the full-moon calico/sand-bass suppression pattern, the white seabass full/new-moon island windows, and the lobster darkest-nights rule all stayed out of the plan. | No conditions were given for Catalina or San Clemente Island, only for San Nicolas, Santa Barbara Island and the outer banks. I treated the nearer islands as unknown rather than assuming they were fishable or blown out. The KB's Catalina Eddy shielding caveat (sea-state note) cannot be checked without live data. | The KB has no sea-state guidance for a Small Craft Advisory as such, no launch-ramp or bar-crossing guidance for Dana Point, and no note on trailering/launching in wind. | The KB carries no rule for how NW wind affects an inshore drift speed for halibut or rockfish — the only wind-and-drift doctrine is techniques/wind-in-your-face-positioning.md, which is rail positioning on a crowded sportboat, not private-boat drift control. | Bounce-ball trolling for halibut is a flagged stub in species/california-halibut.md with no corpus source, so I could not give it any parameters despite it being a standard coastal-flats method. | The downsized-jig presentation for picky small-bait bonito is a flagged stub in species/bonito.md with no corpus source. | Your profile records no soft plastics, leadheads, weedless spring hooks, bay-bass plastics, dropper-loop gangion terminal, torpedo sinkers, circle hooks, or a light spinning/drop-shot outfit — so the weedless-swimbait calico program, the bottom-fishing programs and the drop-shot rows have no owned gear behind them. | The Trinidad 40's gear ratio is not recorded in profiles/cameron/rods.md, so I cannot confirm it meets the yellowtail yo-yo spec of a high-speed reel. | The Tranx 400 setup's braid weight is listed as TBD/respool pending in profiles/cameron/rods.md, so its line class for today is unknown. | The KB carries no current, complete CDFW bag/size/season table — only scattered jurisdiction-stamped claims (14 in sand bass as of 2022-04-25, rockfish closing around year-end as of 2026-08, lobster roughly Oct-mid-March, 7/day). Barracuda, bonito, halibut and white seabass limits are not stated anywhere I read. | species/barracuda.md is explicitly held at medium confidence with no dedicated technique program in the corpus — everything there is inferred from report mentions alongside bass and bonito.

</details>

<details><summary><b>NOW — review</b> · 11/12</summary>

# Dana Point, late September, blowing outside — what's fishable

## 1. The envelope call (day-plan protocol step 1b)

Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), I set `{regions, waters}` before opening a single species note, and that filter is binding for the rest of the plan.

- **regions:** `socal-bight`
- **waters:** `nearshore-coast` (+ `bay-harbor` as the bail-out)

**Islands, banks and open ocean are out today.** You gave me NW 20–25 kt / 6–8 ft at San Nicolas, Santa Barbara Island and the outer banks with an SCA through Sunday, and no conditions at all for anything else offshore. That means every note gated `island`, `bank` or `open-ocean` is **not offered** — not ranked lower, not offered with a caveat. Concretely, the whole late-September headline fishery is off the table for you today:

- The **volume square (SBI–San Nicolas–Clemente–Catalina) that holds the bigger bluefin in September** ([`seasonal/september.md`](seasonal/september.md), `5to3Q5P7w90`) sits inside the blown-out water.
- **Dorado running open-water schools below Catalina** in September (same note, `5to3Q5P7w90`) is `waters: [open-ocean]` — out.
- The **kelp-paddy program**, which is exactly what this stretch is famous for — the best paddy water in the Bight runs **from Dana Point to Oceanside and southward** ([`conditions/kelp-paddies.md`](conditions/kelp-paddies.md), `HzE4FHHcvTk`) — is open-ocean water offshore of the coastal spots, not on them ([`locations/dana-point.md`](locations/dana-point.md)). **The KB cannot tell me how far out your 8–12 kt / 3–4 ft inshore band actually extends.** If you can get me wind, swell height *and period* for the paddy water 5–15 mi off the beach, I'll re-run it; I won't guess.

## 2. Is the inshore band actually a go?

Your inshore numbers are **NW 8–12 kt, 3–4 ft**. Run them against [`conditions/sea-state.md`](conditions/sea-state.md):

- **You are sitting right on the working-captain cutoff.** Wind above ~12 kt is what raises whitecaps, and 12 kt is the stated personal don't-run line (`NC3-3pJDEgo`). 8–12 kt is fishable; 12+ is the bail number.
- **I'm missing the number that matters most.** Period drives how a sea feels far more than height: **10 ft @ 15 s from the south is barely felt; 3–4 ft @ 4–5 s is brutal** (`zKmZ4zql2ws`). And **a sub-10-second interval is a hard bad-sea flag independent of height** (`NC3-3pJDEgo`). Your 3–4 ft could be a pleasant day or a beating. **Pull the period before you launch.** The named never-go combo is 12–15 kt with 4–8 ft at a 9-second interval (`NC3-3pJDEgo`) — you're not there, but you're not far off it either.
- **Degrade the forecast where current opposes swell.** Summer uphill counter-current running against NW swell compresses the interval: a forecast 4 ft @ 10 s fishes like 6 ft @ 7–8 s, and point forecasts won't show it (`zKmZ4zql2ws`).
- **Assume it errs worse and builds.** Forecast error is asymmetric, and afternoon W strengthens rather than eases (`zKmZ4zql2ws`). If it's windier than forecast at 7 a.m., **assume it builds all day and bail early** — that rule is written for small boats (`DnSqw4r7A1s`).
- **Plan the return leg, not just the run out.** Homebound wind doctrine: plan return timing *against* the afternoon W build (`HzE4FHHcvTk`). The zone's own kayak guide picks his stretch of coast off wind direction and heads **south** on a windy day to avoid resistance coming home (`LqW32NSkObY`) — the note flags that he hedges it and never says which way the push actually runs, so treat it as a prompt to think about the return, not a rule.

**Verdict: go, inshore only, early, with a hard bail trigger at 12 kt sustained or any sign it's building.** Deep water starts close here — a mile to a mile-and-a-half off the beach from Dana Point through Newport is already **2,000–3,000 ft** (`Rf1HKJG-SDg`) — so you are never far from the harbor mouth.

## 3. Reading your water

- **SST 67–69 °F is the calico window, just.** The stated preference band is roughly **65–68 °F**; past about **70 °F** they go lethargic and drop to cooler water, though they'll still hit a top-water bait ([`species/calico-bass.md`](species/calico-bass.md), `LqW32NSkObY`). You're at the top of the band — good, and a reason to work the cooler/cleaner patches rather than the warmest.
- **Chlorophyll 1.2 — I can't grade that number.** The KB carries **no numeric chlorophyll bands anywhere** (see gaps). What it does carry is qualitative: **bait holds in the dirtier water and the clean blue sits empty** (`HzE4FHHcvTk`), predators work the **dirty/clean seam** (`HWx1jDTGsng`), and for calico specifically a **green-stained, near-opaque kelp edge with roughly 5–10 ft of visibility** was called the *preferred* read — the stain is cover they feed in (`9xNhdu2aBqE`). A chlorophyll signal along the kelp is not a reason to leave. Cameron's own warm-year rule is the counterweight: weight color at least as heavily as SST and skip dead dirty green.
- **Current, not the tide clock, picks your calico spots.** Parallel to the shoreline (uphill or downhill) = fishable edge; **into** the beach = marginal but viable when it's off-color (fish use the dirt to ambush against structure, `Z3rZqy2Pi8E`); **off** the beach = garbage, skip it (`0KQ--N5TjqE`, `Rwy4MqeXCIU`). Read it off the kelp: **pulled 20 ft under = raging** (surface presentations dead), **laid down = strong**, **resurfacing = slacking**, go back on top.
- **The 10:20 low.** Calico are current-driven and tide-indifferent, but halibut and white seabass are tide-gated, and on a marginal day the bite **compresses into the tide windows** ([`conditions/tide-and-slack.md`](conditions/tide-and-slack.md), `HzE4FHHcvTk`). **Be on your highest-percentage spot by 9:20 — an hour before the change — not looking for water at 10:20** (`6TBxHnkYXI0`).
- **You didn't give me the moon.** That matters: on a clear full moon calico gorge overnight, bite early and shut down by mid-morning, and the instruction is not to launch until noon or one if you can't make first light (`Blh2BA-7Ono`). Tell me the phase and I'll re-shape the timeline.

## 4. What to fish, ranked

### A. Primary — coastal calico + the "three B's" on the Dana Point kelp-and-boiler strip

This is the zone's actual fishery: **two kelp beds, boiler rock, three beach-break points, one artificial reef and the 100-fathom curve** ([`locations/dana-point.md`](locations/dana-point.md), 9 charted spots, cameron). September is inside the calico peak (`season_peak: apr–oct`), and the corpus records **calico, sand bass and barracuda coming off the Dana Point kelp bed together, all on strips of squid, in a single morning session** (`M6U_FVdosr4` — the note flags that the transcript places only the *afternoon* trip at that bed, so treat the pairing as the pattern, not a pinned location).

**Working depths here are the ones the corpus actually fishes: 0–8 ft and 20–100 ft, occasionally a little past 100** (`LqW32NSkObY`).

**How to run it:**
1. **Grade each bed in a handful of casts, then move.** The biting fish sit on the **up-current / leading edge** — hit three or four sides of a head and you know (`0KQ--N5TjqE`).
2. **Surface iron is your wind-day tool** — it covers a whole edge on the drift where a weedless cast covers one stringer, and **wind is a reason to step *up* in iron weight** (Salas 7X class) to punch the cast ([`techniques/surface-iron.md`](techniques/surface-iron.md), `D5DR7Kx42_A`). Retrieve slow-to-medium for calico — crank it fast and it skips out instead of swimming, and you can't out-wind them anyway (`3dVc-2rsYII`, `Ec2GaNpiOHI`). **Colour ranks last: swim → size/weight → colour.** The one calico exception is yellow up in the kelp/canopy, "bleeding soldier" out in the open (`Ec2GaNpiOHI`).
3. **If the bait is small ("rice" anchovy), downsize hard** — a Tady AA-light/A1-light class iron, roughly a **third the weight of a Tady 45**, out-bites the big jig **two or three to one** (`pcwcRdmWmLc`).
4. **Pick stringers with a weedless slug** where the iron won't reach: 7" weedless slug on a **3/8–3/4 oz keel-weighted spring hook**, 7–8 ft bass class, **40–60 lb**, heavy fluoro leader for kelp abrasion, soft glass tip so you don't pull it (`YIABTTYXeqc`).
5. **Sonar/sign:** calico mark **tight to kelp and structure edges and on hard bottom**, on the reef-to-sand transition. Watch for the sub-surface signature you'd otherwise run past — **hard bottom with light kelp riding ~20 ft off the bottom in ~40–42 ft**, documented on the Camp Pendleton stretch just south of you (`HMdrP4-i9MM`). Birds: **cormorants diving *in* the kelp = bass below**, a better inshore read than gulls (`Blh2BA-7Ono`).
6. **Regs (California/CDFW — verify current before you fish):** calico minimum **14 in** (as of 2026-08; corroborated four ways), bag stated as **5** (as of 2019-03, single-source and the speaker names no jurisdiction).

**Spots, with the coordinates the KB carries** (all `parent: dana-point.md`, cameron):

| Spot | Position |
|---|---|
| Monarch Boilers | 33°28.970'N 117°44.020'W |
| Salt Creek | 33°28.565'N 117°44.040'W |
| Dana Point Kelp — Red Buoy | 33°27.320'N 117°43.380'W |
| Barber Poles | 33°26.710'N 117°41.410'W |
| San Clemente Kelp *(mainland city)* | 33°24.450'N 117°38.140'W |
| San Clemente Artificial Reef *(mainland city)* | 33°23.890'N 117°37.200'W |
| San Mateo Point | 33°22.960'N 117°36.800'W |
| Trestles | 33°22.790'N 117°36.280'W |
| The Hospital 100 Fathom Curve | 33°29.500'N 117°47.100'W — **stay south of 33°30.050'N (MPA edge)** |

**Naming trap:** "San Clemente Kelp" and "San Clemente Artificial Reef" are off the **mainland city**, not San Clemente Island. Do not read island reports onto them.

**The MPA line at The Hospital is single-sourced to one spot-library annotation with no MPA named** — latitude alone doesn't establish a boundary. California/CDFW, as of 2026-08: verify boundaries and take rules before fishing.

### B. Bonito and barracuda — the corpus's one dated Dana Point program

The KB has an actual worked Dana Point method for this: **troll a short, soft daisy chain of small feathers ("just small booties") at 5.5 kt either side of the harbor mouth, and cast a lure the moment you get bit** — the troll locates a scattered school, the cast is what you fish it with ([`techniques/trolling.md`](techniques/trolling.md), `poqjnb1r1zk`, 2019-07-02, either side of Dana Point Harbor). Follow-up cast: a small sardine-profile diving hard bait twitched behind the boat.

- **Chrome is the colour bonito and barracuda reach first** (`YAKOv9bXKO0`, `PrdPJy26H8c`) — which is exactly why chrome backfires if a yellowtail shows.
- SoCal bonito grade runs **2–3 lb typical** (`Z3rZqy2Pi8E`).
- **Barracuda teeth cut mono leaders even in heavy sizes** (`lm7D9Tlc7Po`) — carry short single-strand wire or heavier hard mono if they turn up thick. If they're a tax, **run a single inline hook and shake them off** (about half drop without handling — the note flags the source actually ran two *barbless* singles, `kt3G72gUldM`, `28IttH7P7K0`), or upsize to a big live mackerel to screen them out (`YVHdDbkQrKk`).
- Late-September is inside both season windows (barracuda `may–oct`, bonito `may–dec`); the corpus's dated Dana Point bonito record is early July.

### C. Coastal yellowtail — the opportunistic overlay, not the plan

[`species/yellowtail.md`](species/yellowtail.md) maps **warm-stable (June–September) to coastal kelp-line fish from LA to San Diego**, and `waters` includes `nearshore-coast`, so it's in envelope. Just south of you, **25–30 lb fish were reported on this stretch of coast in October**, and mainland-coast schools are **markedly finicky on the iron** compared to island fish (`HMdrP4-i9MM`, `VpW91AKOFVQ`).

- **Sonar signature: arcs at 5–10 fathoms near structure.**
- **If it's windy and they're metered rather than showing, the rank flips: yo-yo iron first, surface iron as a picker** — a re-rank, not an abandonment (`ejUTAnONf7o`). That's a 40–60 lb class rod, hit bottom and burn it; the strike comes a couple cranks off.
- Don't build the day around this. **The KB gives no numeric SST band for yellowtail at all** — it's an explicit flagged gap in the note.

### D. Bail-out if it builds — bottom program, or the harbor

If the wind pushes past 12 kt or the chop stands up, drop off the shallow boiler work:

- **Sand bass / rockfish on the deeper hard structure.** Sand bass hover **above or within** the structure, so a column-covering presentation beats a dead-stick on the rocks (`P2OzCf2CwXI`); a big one is about **6 lb**, which sets the whole scale — 20 lb leader gets it done. Match the bait's depth, not the bottom's: sand bass and calico came off a Newport pipe in **80 ft** on crankbaits running only **15 ft** deep (`kwMIgkCtFUE`). South of you, four spots in the North County library are labelled "rockfish area" outright ([`locations/oceanside-north-county.md`](locations/oceanside-north-county.md), cameron). **Rockfish (California/CDFW, as of 2026-08 — verify):** season open most of the year, closing roughly Jan–Feb; bag stated as **10 rockfish + a separate 10-whitefish allowance** (as of 2020-03, single-source); the RCA depth line runs ~**240 ft** at the islands vs a **75-fathom (450 ft)** line closer to the mainland, so check position against the drawn boundary, not the depth reading (`iAr6sbRC384`).
- **Halibut are genuinely in season.** `season_peak` includes September, and inshore fish push under **15 ft** twice a year — spring behind the grunion and **again in fall on structure** (`ghHQe3fP9U4`, `EuYOlsnxXko`). They lie in the sand within **5–10 ft of a hard edge** (`OpcKQPA3vAI`). Discipline: you need **off-colour water + current + bait, all three** — missing one, **leave inside 20–30 minutes** (`OpcKQPA3vAI`). Live-bait drift on a trap rig off a three-way with a breakaway sinker, **15 lb fluoro inshore** on a 200-class reel; artificial version is a **3 in swimbait**, which covers about **90%** of deeper fishing (`a5u8BaYzw8c`, `OURS05qEGcA`, `fHMwcm1xRQk`). The 10:20 low means you're fishing the outgoing into the change — be set up by 9:20.
- **White seabass:** in envelope on `nearshore-coast`, but its `season_peak` is **mar–aug**. Late September is outside it. Not a target today.
- **Harbor:** I have to be straight with you — **the KB has no Dana Point Harbor page.** [`locations/bays-and-harbors.md`](locations/bays-and-harbors.md) gives universal harbor structure (eelgrass edges, channel drops, docks/pilings — older weathered pilings hold better than new, `usHl-4SfqDA`), but the bays it documents are San Diego Bay, Mission Bay, Newport, Huntington and LA/Long Beach. Spotted bay bass are `regions: socal-bight`, `waters: bay-harbor` so they're in envelope in principle, but **no corpus source puts them in Dana Point Harbor.**

## 5. Bait and the clock

The bait comes first and the clock is the whole problem at this port ([`locations/dana-point.md`](locations/dana-point.md), [`bait/making-bait.md`](bait/making-bait.md)):

- **The Dana Point sportboat fleet leaves at 6:00 a.m.**, which is exactly when the private-boat line forms — it's already building by a quarter to six (`ztpj1Xll0-U`, `bM2vUS1B-yQ`).
- **Leave the dock at 5:00, or 4:30, and there's no line** (`ztpj1Xll0-U`). A **7:00 a.m.** arrival also avoids the line (`7WapaxdtjQg`) — but the other half of that same presenter's doctrine is that by 7:00 "it's all gone" (`ztpj1Xll0-U`). Both halves are in the KB; pick your poison.
- **At the barge:** follow the side signal — **at Dana Point it's a cone on the ocean side**. Hail on **VHF 11**, barge name twice plus your boat name, wait for the response. **Never board the barge to fend off.** Tell the attendant you want it loaded light and you're not in a rush; tip at the end (`7WapaxdtjQg`).

**Suggested timeline:** dock 4:30–5:00 → bait → be on the Dana Point kelp bed or Monarch Boilers for the **gray-light window** (the hour before sunrise into early morning is credited with deciding a large share of SoCal bass tournaments, `RUuPNpK0x-s`) → work the edges south with the current read → be re-set on your best spot by **9:20** for the 10:20 change → reassess wind by late morning and run for the barn against the afternoon W build.

Note this collides with your profile: [`profiles/cameron/boat.md`](profiles/cameron/boat.md) records your normal departure as **~8 a.m.**, "earlier starts are the exception." An 8 a.m. start here costs you both the bait and the gray-light window.

## 6. Gear, resolved against your profile

Per [`tackle/gear-classes.md`](tackle/gear-classes.md), which maps your setups to classes directly:

| Job | Class | Your gear ([`profiles/cameron/rods.md`](profiles/cameron/rods.md)) |
|---|---|---|
| Kelp-line surface iron | jig-stick / surface-iron class, 8–10 ft, 2–4 oz, ~25–60 lb | **Torium 20HG on the Phenix Abyss 10'0" (25–60 lb), 50 lb braid** — your full surface-iron setup |
| Flylined bait on the edge | flyline / soft-rod class, ~9 ft MH, ~30–65 lb | **Avet MXJ on the Teramar TMC90MHB2, 50 lb braid** |
| Yo-yo iron / dropper loop / sinker rigs | yo-yo / heavy-iron class, ~8 ft XH, 40–80 lb | **Trinidad 40 on the RA96XH 8'0" 40–80 lb, 80 lb braid** |
| Utility inshore casting | utility inshore / baitcast, 8 ft H, 20–45 lb | **Tranx 400 on the Phenix M1 SMX-82H** — braid still TBD, respool pending |

**Owned irons that fit today** ([`profiles/cameron/tackle.md`](profiles/cameron/tackle.md)):
- **JRI-7** (light blue, ~Tady 45 class, medium-fast) — your local/kelp all-rounder, the default grind.
- **Nomad Slidekick 120g** (4.25 oz, heavier than traditional irons) — this is your answer to the "wind up → heavier iron" rule; it also sinks out to cover the column.
- **Strictly Irons Mighty 5.5"** (medium-to-high retrieve) — the downsized in-tight jig.
- **Strictly Irons Glory 7"** (wide drawn-out kick, slow and steady) — the change-up for a picky bite or slack current.
- **Salas 6X / Salas CP 105** for the yo-yo re-rank if yellowtail meter up.

**Gaps I have to name rather than paper over** (protocol step 4: never recommend gear you haven't said you own):
- **You have no bass-casting / swimbait class outfit.** The gear-classes table lists *no* example setup for bass class (7–9 ft graphite, low-profile **200–300** reel, 30–65 lb braid) or crank class, and your inventory has none. The Tranx is the nearest thing but it's an 8'2" H rated **3–8 oz** — a **3/8–3/4 oz** weedless slug is well under it. The weedless-slug and crankbait programs in the calico and sand bass routers are real gaps in your box, not something I'll substitute around.
- **No soft-plastic swimbaits, slugs, flukes or leadheads are recorded in your tackle file** — it's scoped to hard baits, casting and jigging. So the plastics half of the coastal bass game isn't equipped.
- **No small feathers for the bonito daisy chain.** [`profiles/cameron/trolling-lures.md`](profiles/cameron/trolling-lures.md) lists the Williamson Tuna Catcher, three JAW dual-skirt lures and your dad's unidentified skirt bag — all offshore-scale. The Dana Point program calls for a **short, soft chain of small booties**, and I can't see one.
- **No wire bite tippet recorded** for the barracuda cut-off problem.
- **Your boat's operating envelope is null.** `range_nm` and `sea_state_max_ft` are deliberately left empty in [`profiles/cameron/boat.md`](profiles/cameron/boat.md) — "Cameron has not stated these — left null rather than guessed. Until they are filled, the protocol must **ASK** for range and sea-state." So: **what's your honest sea-state limit in the 22 Panga, and how far off the beach will you take it in 3–4 ft?** That answer is what decides whether §3 (paddy water) ever comes back on the table.

One profile detail that matters in 3–4 ft: your trim routine puts **one person forward on the bow bean bag** underway, and the file notes rough days forward are brutal — rider catches air then hits the deck. Short legs and a slow bump down the coast, not a run.

## 7. What the KB does not cover here

Listed honestly rather than filled in — see `gaps_admitted`. The big ones: **no numeric chlorophyll bands anywhere in the KB**, so I cannot tell you what 1.2 means; **no swell period in your brief**, which the KB says matters more than height; and **the Dana Point zone note carries an explicit flagged gap for the launch ramps and hoists, the run time or distance from the harbour mouth to any spot, and the sea-state envelope the run demands.** All nine Dana Point spot pages are minimum pages — position and parent zone, nothing on depth, relief or bottom.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `conditions/tide-and-slack.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `seasonal/september.md`, `locations/dana-point.md`, `locations/oceanside-north-county.md`, `locations/dana-point-kelp-red-buoy.md`, `locations/monarch-boilers.md`, `locations/salt-creek.md`, `locations/barber-poles.md`, `locations/san-clemente-kelp.md`, `locations/san-clemente-artificial-reef.md`, `locations/hospital-100-fathom-curve.md`, `locations/san-mateo-point.md`, `locations/trestles.md`, `locations/bays-and-harbors.md`, `species/calico-bass.md`, `species/calico-bass-surface-iron.md`, `species/sand-bass.md`, `species/barracuda.md`, `species/bonito.md`, `species/california-halibut.md`, `species/yellowtail.md`, `species/rockfish-lingcod.md`, `species/white-seabass.md`, `species/spotted-bay-bass.md`, `species/california-spiny-lobster.md`, `techniques/trolling.md`, `techniques/surface-iron.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`  
*videos:* `zKmZ4zql2ws`, `NC3-3pJDEgo`, `DnSqw4r7A1s`, `HzE4FHHcvTk`, `Z3rZqy2Pi8E`, `LqW32NSkObY`, `0KQ--N5TjqE`, `Rwy4MqeXCIU`, `YIABTTYXeqc`, `9xNhdu2aBqE`, `M6U_FVdosr4`, `ztpj1Xll0-U`, `7WapaxdtjQg`, `bM2vUS1B-yQ`, `poqjnb1r1zk`, `HMdrP4-i9MM`, `Rf1HKJG-SDg`, `6TBxHnkYXI0`, `OpcKQPA3vAI`, `ghHQe3fP9U4`, `EuYOlsnxXko`, `OURS05qEGcA`, `fHMwcm1xRQk`, `a5u8BaYzw8c`, `D5DR7Kx42_A`, `pcwcRdmWmLc`, `Ec2GaNpiOHI`, `3dVc-2rsYII`, `ejUTAnONf7o`, `YAKOv9bXKO0`, `PrdPJy26H8c`, `lm7D9Tlc7Po`, `kt3G72gUldM`, `28IttH7P7K0`, `YVHdDbkQrKk`, `VpW91AKOFVQ`, `Blh2BA-7Ono`, `HWx1jDTGsng`, `RUuPNpK0x-s`, `P2OzCf2CwXI`, `kwMIgkCtFUE`, `iAr6sbRC384`, `usHl-4SfqDA`, `5to3Q5P7w90`, `r6j5w40fVHI`  
*gaps admitted:* The KB carries no numeric chlorophyll bands anywhere — nothing in conditions/water-color.md or elsewhere lets me classify a reading of 1.2 as clean, green or dirty; only qualitative doctrine (bait in the dirty water, fish the dirty/clean seam) applies. | No swell period was given for the inshore 3-4 ft, and conditions/sea-state.md makes period the primary variable (10 ft @ 15 s barely felt vs 3-4 ft @ 4-5 s brutal; sub-10 s a hard flag) — the steepness rule cannot be applied without it. | locations/dana-point.md carries an explicit flagged gap: no corpus source for the launch ramps and hoists in Dana Point Harbor, the run time or distance from the harbour mouth to any spot in the zone, or the sea-state envelope the run demands. | All nine Dana Point spot pages are minimum pages — coordinates and parent zone only. No charted depths, relief or bottom composition for Dana Point Kelp, Monarch Boilers, Salt Creek, Barber Poles, San Clemente Kelp, San Clemente Artificial Reef, The Hospital, San Mateo Point or Trestles; and no source says what Barber Poles actually is. | No corpus source for the extent, health or seasonality of the two Dana Point kelp beds. | locations/dana-point.md flags that no corpus source says whether yellowtail, white seabass, halibut, rockfish, lingcod or sheephead are targeted anywhere in this zone, and no month-by-month season is scoped there for any species. | species/yellowtail.md carries an explicit flagged gap for numeric SST bands — the corpus gives directional water-state reads only, so I cannot tell you whether 67-69 F favours coastal yellowtail. | No SST band exists in the KB for barracuda or bonito (sst_band_f: unknown on both). | The KB has no Dana Point Harbor zone page. locations/bays-and-harbors.md is universal structure only and documents San Diego Bay, Mission Bay, Newport, Huntington and LA/Long Beach — no corpus source records spotted bay bass, halibut or any species inside Dana Point Harbor specifically. | The moon phase was not given, and species/calico-bass.md makes a clear full moon invert the fishing day (gorge overnight, bite early, dead until late) — that rule cannot be applied. | profiles/cameron/boat.md leaves range_nm and sea_state_max_ft null by design, and instructs the protocol to ASK rather than assume — so I cannot compute how far offshore the 8-12 kt band is usable for you. | Nothing in the KB or the given conditions establishes how far offshore the inshore Dana Point-to-Oceanside band extends, so the kelp-paddy water (the region's normal late-September program, and open-ocean gated) could not be evaluated. | Cameron's profile contains no bass-casting/swimbait class rod (gear-classes.md lists no example setup for bass class or crank class at all) and no soft-plastic swimbaits, slugs, flukes or leadheads — the plastics half of the coastal bass program is unequipped. | Cameron's trolling inventory has no small-feather daisy chain of the kind the Dana Point bonito program calls for, and no wire bite tippet is recorded for barracuda cut-offs. | species/calico-bass.md self-flags its 'outside kelp edge ~50 ft in to ~25 ft' sonar band as unverifiable — no cite, in no other note, yet promoted into the infobox — so I did not rely on it. | The Hospital MPA line (stay south of 33 30.050 N) rests on a single spot-library annotation with no MPA named and no corpus source; California/CDFW boundaries must be verified independently before fishing. | Regulatory figures used (calico 14 in / bag 5; rockfish season and 10+10 bag; RCA depth lines) are stamped as of 2026-08, 2019-03 and 2020-03 in the notes, several single-sourced, and all require verification with CDFW before fishing. | I did not open species/california-spiny-lobster.md beyond its front matter; its season_peak is oct-mar, so late September falls outside it, but I make no claim about the legal opener.

</details>

### 3. [trip] I want to do two days at the Coronado Islands in October on a private boat. What is the program, and what pape…

**Winner:** NOW · mapping {'A': 'B3', 'B': 'B2', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 1 | 2 | 2 | 2 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three read the conditions the same correct way (0.9 F is a gradient not a break, neap tide means the bite compresses into current windows, 12 kt / 10 s sits exactly on the KB's go/no-go lines) and none fabricated - the shared specifics I spot-checked against the repo (sabiki 100 ft / 8 oz / five 12-inch mackerel, 6X at 5-6 oz keyed to depth, ~30 ft of sink on the surface iron, October's '100% temp chart and chlorophyll') all verify. The separator was the papers half of the question: B returned nothing at all on Mexican paperwork, A found the FMM/CONAPESCA/passport block and correctly labelled it a road-trip source from another region, and C delivered a jurisdiction page with INM/CONAPESCA + as-of 2026-08 + verify, the matching US-side CDFW licence and GO ID, and the fact that Lower 9 Mile sits 0.65 nm from US water so jurisdiction is a positional question - the single most useful thing any answer says about permits. C also has the best spot layer (per-spot pages with bearings and distances, plus an admission that nine of eleven are position-only) and the most unusual honesty, flagging that the KB's own Coronados circuit doctrine rests on a video that never mentions the islands. A's one clear edge over C is resolving the gear against the owned rod inventory and naming the gaps; B's is bait execution (mackerel filtering the catch toward yellowtail, butt-hooking against sea lions).

- *B2 reasons:* found: excellent on the fishing half (bait-choice doctrine, anchoring, birds, paddies, technique cadences) but delivers nothing at all on the papers half - 'nothing to cite' - where the other two surfaced an FMM/CONAPESCA/passport block, so half the question returns empty. specific: full spot table, sabiki 100 ft/8 oz, 3/8-3/4 oz spring hook with 7in slug, 40-65 lb fluoro, 10-25 casts then move, 130-250 g at 1.5 g/ft, 10-crank and 5-6-crank yo-yo cadences, 5-minute bleed, 2 cups salt per 7-10 lb ice. sourced: dense note paths and ids (w5_x6kkN-xE, ZFqe49jRgA0, 9tTM99InluM, kzD0kSnnVPw) with confidence tiers. scoped: region and jurisdiction handled correctly - CDFW does not travel, BCS circle-hook dated 2019-02-13 with verify flag and correctly excluded; no US-side licence mention. honest: strongest single feature is the 10-item 'could not tell you' list; no bluffing, no relative time. actionable: the day is runnable and the gear riggable, and the mackerel-filters-to-yellowtail and butt-hook-versus-sea-lions detail is the best bait execution of the three, but an angler still cannot answer 'what papers do I need'.
- *B3 reasons:* found: pulled the right layers (yellowtail router, current diagnostics, sea-state, tide/moon, bait, care) and located the KB's only paperwork block (BOLA FMM/CONAPESCA), while stating plainly that no Coronados location note exists in its version. specific: coordinates for 7 island + 4 vicinity spots, sabiki 100 ft/8 oz, iron 2-3 oz vs 5-6 oz, 40/50/60 lb line ladder, 2-4 oz egg sinker with 2/0-4/0 J hook, 6-10 oz dropper, salt slurry 2 cups per 7-10 lb ice. sourced: note paths plus video ids (D5DR7Kx42_A, 0DKmYId1NN4, HTowqnwAMeA, ejUTAnONf7o, yGXSrUauo2w) that match real KB content; flags confidence tiers per source. scoped: baja-pacific-north + socal-bight transit gate stated up front, exclusions named; FMM/licence carry INM/CONAPESCA + as-of 2026-08 + verify, and it correctly rules the 2019 BCS circle-hook row out of scope; misses the US-side California licence for the Point Loma/9 Mile leg. honest: labels the BOLA block as a road-trip source in another region, says island-structure.md is socal-bight-gated so applying it is extrapolation, no relative time, long explicit gap list. actionable: only answer that resolves the called-for classes against owned rods and names the two gaps (no SPJ outfit, unknown Trinidad gear ratio, braid TBD).
- *NOW reasons:* found: hit the exact right material on both halves - a dedicated Mexican-waters jurisdiction page, a US-waters page, a Coronados zone page and species-zone guide, and per-spot location pages - and named the gaps those pages themselves flag. specific: 11 spots with positions plus bearings/distances off Middle Grounds (2.0 nm NE, 4.7 nm NNW, 9.6 nm SSE), 190-class divers, 65 lb braid to 40-50 lb top shot, yo-yo depth ladder 60/80/100 ft to 120-150 ft at 5-6 oz, 1-4 oz egg sinker, 1.5-3 mph slow-troll, calico 65-68 F band, dorado ~71-72 F, 0.65 nm to the border. sourced: cites verified against the repo (mexican-waters.md as-of 2026-08, yo-yo 5-6 oz depth ladder, 30 ft sink, sabiki 8 oz / five 12-inch macks all match). scoped: only answer that handles both jurisdictions - Mexican block with INM/CONAPESCA + as-of 2026-08 + verify, plus the CDFW licence and GO ID for any US-side leg and the point that jurisdiction is positional; CA licence requirement itself carries no as-of stamp, the one small slip. honest: exceptional - discloses that the KB's own Coronados circuit doctrine rests on a video that never mentions the islands, surfaces contradicted-by-source flags on the FMM and licence rows, labels the two-day schedule as its own sequencing rather than KB doctrine, and lists internal conflicts it declined to resolve. actionable: circuit, conversion sequence, meter reads, gear table and pre-trip checklist are all executable; weaker than A only in not resolving gear against the owned rod inventory.

<details><summary>Full prompt</summary>

I want to do two days at the Coronado Islands in October on a private boat. What is the program, and what papers and permits do I need? Assume these conditions and do NOT fetch live data: mid-October, two days. SST: Coronado Islands 66.8 F, 9 Mile Bank 66.2 F, Point Loma 65.9 F. Chlorophyll 0.9 at the islands. Wind NW 8 kt mornings, NW 12 kt afternoons. Swell NW 3 ft at 10 s. Moon: last quarter.

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

> Built from the KB only, using exactly the conditions you gave. No live BightSST pull, no outside sources. Where the KB is silent I say so rather than filling it in.

---

# 1. Papers and permits — the KB cannot answer this, and you should not let me guess

The Coronado Islands are Mexican water. **This knowledgebase contains no entry on Mexican paperwork for a private boat** — no fishing licence, no vessel documentation, no immigration or customs procedure, no crew-manifest or border-crossing guidance. I searched every note branch; there is nothing to cite.

The only Mexico-regulatory traces in the whole KB, none of which is a procedure you can act on:

- `techniques/flyline.md` carries a single on-camera claim that a circle hook was "mandatory," read as a Mexican sportfishing requirement — **Baja California Sur, as of a 2019-02-13 video**, explicitly flagged "verify current CONAPESCA/DOF circle-hook rules before fishing," and never confirmed against regulation text (`0dIwWiOc1NY` is the Ensenada entry in the same note; the circle-hook claim is from the BCS entry). BCS is not Baja California Norte, so it does not even cover the Coronados.
- `species/rockfish-lingcod.md` states plainly that **California/CDFW rockfish regulations do not apply in Mexican waters in any case, and that current Mexican/Baja regs must be verified separately before fishing there.** That is a warning, not a rule set.
- `species/calico-bass.md` mentions in passing that one charter group's Mexican fishing permits were **obtained in Tijuana** (`xIUKmH9ccgQ`, 2012 Cedros trip via Ensenada) — an incidental historical detail about someone else's trip, not guidance.

The KB's own house rule (`CLAUDE.md`) is that any regulatory claim must carry jurisdiction + an as-of date + a verify-current flag. Nothing meeting that bar exists here for a private boat fishing Mexican water. **Get your paperwork requirements from the Mexican authorities or an official source before you leave the dock — I am not going to invent a checklist for a foreign border crossing.** Also assume any US-side bag/size limit you know is irrelevant: `species/rockfish-lingcod.md` is explicit that CDFW rules do not travel across the line, and the KB has no Mexican limits for yellowtail, bass, or rockfish.

---

# 2. Reading your conditions

**SST spread is 0.9 °F across the whole plan area** (Coronados 66.8, 9 Mile 66.2, Point Loma 65.9). Warmest and cleanest read available to you is the islands themselves.

- **October is the regime-change month.** `seasonal/october.md`: "conditions become pretty important… look 100 % at your temp chart and chlorophyll" (`XLVUhV8DW64`, `OYOda6T3f-8`) — build the plan on break structure, not spot names. `conditions/water-regimes.md` calls this **fall fragmentation**: an everything-season but **scattered — breadth of species, low density of any one**.
- **Your temperature field has essentially no break in it.** A 0.9 °F spread over ~20 nm is not the "sharp offshore edge that jumps multiple degrees in ~1 mi" that `conditions/water-temperature.md` tells you to hunt. Treat the whole area as one water mass with a mild inshore-to-island warm gradient, and go looking for the edge **on the water** — `conditions/current-diagnostics.md` documents a current break as a visible whitewater/foam line against a slicker patch.
- **Chlorophyll 0.9 — the KB gives you no numeric scale.** There is no threshold anywhere in `conditions/water-color.md` or elsewhere mapping a chlorophyll number to "clean" or "green." What the KB does give you is the **age question**: is this a new cold bloom (skip — cold, green, "bad now, productive later") or a **mature bloom edge** (fish it)? With SSTs in the mid-60s and no reported overnight ~5 °F drop, you have no evidence of a fresh upwelling event, so read it as established water and **fish the edge, not the middle of the mass**. Corollary from the same note: **bait holds in the dirtier water and predators work the dirty/clean seam** — do not default to the prettiest blue.
- **This species mix is on, this one is off.** `conditions/water-temperature.md` puts the dorado concentration at the green-cold/blue-warm boundary around **~71–72 °F** — you are ~5 °F below that, so do not build any part of the trip around dorado. Yellowfin want **SST max × chlorophyll min**; your max is 66.8 and there is no warm cell to run to. `seasonal/october.md` has the bluefin **condensing outward toward Tanner and Cortez** as the coast cools — off the map for a Coronados trip.
- **Wind geography favors you.** `locations/bight-geography.md` (`HzE4FHHcvTk`, 4/21/22 Landesfeind) names the **Coronados among the zones that held their water through a big NW blow**, while the northern Channel Islands and the LA/Ventura shelf rolled over 5–8 °F. In a NW pattern, this is the right side of the Bight to be on.

**Sea state.** NW 8 kt AM / 12 kt PM, NW 3 ft @ 10 s, per `conditions/sea-state.md`:
- Steepness rule: flag any segment where **period in seconds approaches height in feet**. 10 s against 3 ft is nowhere near that — the swell itself is a non-issue.
- Hansen's thresholds (`NC3-3pJDEgo`, registered voice, single-mention set — medium confidence): **wind over ~12 kt is what raises whitecaps**, and that is his personal no-run cutoff; **sub-10-second interval is a hard bad-sea flag**. Your afternoon sits exactly on the 12 kt line and your period sits exactly on the 10 s line. You are inside the envelope, but with zero margin in the afternoon.
- Two rules that bite specifically here: **forecast error is asymmetric** — assume the worse side, and assume afternoon W at the islands **strengthens** rather than eases; and the **homebound-wind rule** — "runs south into Mexican paddy water put a W wind on the return leg = uphill misery. Plan return timing against the afternoon W build, not just the outbound conditions" (`HzE4FHHcvTk`, 8/17/22). Your entire trip is a run south. **Plan both days to be turning for home before the afternoon build, not after it.**
- If you launch San Diego Bay: Cameron's own chart work in the same note has the entrance open to swell from **~160°–186°**, channel seaward axis **186°**, with **Point Loma blocking swell from west of the axis** — a NW swell is blocked, so the entrance is not your problem on this forecast.

**Moon — last quarter.** `conditions/tide-and-slack.md` (mechanism, `9tTM99InluM`): **quarter moons are neap tides — the smallest tidal range**, because the lunar and solar bulges partially cancel. So the moon/tide stacking described in `conditions/moon.md` is absent: you get the **weakest tidal push of the month**. Consequences you can act on:
- The moon note's elevated windows are full/new **±1 week with the leading days strongest**; last quarter sits at the outside edge of them. Hansen's dissenting view in the same note (`fri_BWI-VA0`) actually likes the 7-days-after-full window, tied to bluefin. Both are recorded side by side, neither is a gate — treat the moon as a mild probability adjustment here, not a reason to go or not go.
- One clear positive: the **full-moon daytime bass suppression** (calico gorging at night, dead by mid-morning) does not apply. Your bass segments are not moon-suppressed.
- The **post-moon relocation/coverage-illusion discipline** also does not apply — you are not chasing a stale post-moon report.
- The real consequence is **window compression** (`conditions/tide-and-slack.md`): when the bite is off-peak — and fall fragmentation is explicitly "scattered, low density" — **action compresses into the tide windows**, and the answer is to **anchor the plan's zones to tide times and arrive an hour before the change**, not at it. On weak neap swings you may also get the "treadmill is off" state (bait pointing every direction, fish metering but not biting) more often; that is a **move-or-wait signal**, not a reason to keep soaking.

**Pull a real tide table.** The KB gives timing rules but no tide data, and BightSST is not in scope here. The rules that need actual times: arrive an hour before the change; the **late-morning slack when a tide falls after ~9:30 is the prime open-water pop-up window**, and pop-ups also **cluster in the afternoon**, so re-run water you marked earlier at those times.

---

# 3. The program

## Primary target: yellowtail — with an honesty caveat

`species/yellowtail.md`: **"The Coronados are synonymous with yellowtail"** (`D5DR7Kx42_A`), ~13 mi from San Diego, and the western side of the group is exposed to colder Pacific currents and tidal swings, so **the water stays bait-rich**.

The caveat you should hear before you commit: **the KB frames the Coronados as the warming-transition (spring) classic, and carries no October-at-the-Coronados corpus entry.** What partly offsets that is Cameron's standing doctrine, kept side by side with the corpus year-anniversary prior in the same note: **"calendar date doesn't matter for yellowtail — water state (temp + bait) does."** So October is not a disqualifier, but you are fishing a zone the KB documents best in spring, in the month the KB says to trust the chart over the calendar.

The second Coronados-specific pattern to plan around, and it matters more than anything else on a neap two-day trip: **"seeing-not-biting" cycles with narrow daily windows** — you will mark and even see fish that will not eat until a short window opens (`YZtX1MiT0y8`, 4/21/22). **Anchor those days to tide and current, not to the clock.**

## The spots (coordinates from `sources/spot-lists.md`)

Seven island spots and four vicinity spots, N→S:

| Spot | Position |
|---|---|
| Pukey Point | 32 26.850 / 117 18.000 |
| East of Pukey Point (yellowtail & rockfish) | 32 27.000 / 117 14.100 |
| Middle Grounds | 32 25.810 / 117 15.950 |
| Ribbon Kelp | 32 24.800 / 117 13.880 |
| Lighthouse | 32 23.290 / 117 14.570 |
| 5-Minute Kelp | 32 22.940 / 117 13.515 |
| South Kelp Ridge | 32 22.000 / 117 13.260 |
| Rockpile | 32 17.620 / 117 10.030 |
| Coronado Canyon (rockfish) | 32 30.300 / 117 17.500 |
| North of North Island (rockfish) | 32 27.380 / 117 18.000 |
| Lower 9 Mile Bank | 32 32.500 / 117 20.500 |

Two planning points from the KB about this group specifically:
- **Conditions vary a lot across the six-spot group** — enough that Cameron's own BightSST eval set is being **split from one "Coronado Islands" entry into each of the six spots individually, because one averaged reading hides the spread** (`locations/bightsst-eval-targets.md`, `profiles/cameron/spots.md`). Do not treat "66.8 at the islands" as one number: expect the north end and the south end to differ, and **verify temp and color spot to spot as you move**.
- The KB **does not classify these spots as "complex" or "compact" search boxes.** `locations/zone-lexicon.md` gives that framework and names 302/371/west-of-Catalina as compact 20–30 minute reads and the below-Clemente group as a 50–60 sq-mi expedition — but no Coronado spot is placed in either bucket. Budget your time from your own read of the structure, not from a KB classification that doesn't exist.

## How to pick which spot to fish, hour by hour

`conditions/current-structure.md` is the decision layer here, and it does more work than temperature will on this trip:

- **Parallel-current rule.** Current running **parallel** to the shoreline (uphill or downhill) is good — it builds a definable leading edge and makes land-attached reef pinch-points work. Current **straight into the beach** is marginal (with a genuine late-fall exception: on 11/23/22 at San Clemente the bass bites *required* into-the-island current with off-color water, fish using the dirt to ambush). Current **straight off the beach is dead — leave**.
- **Spot typology** (`locations/island-structure.md`): **land-attached perpendicular ridges are two-directional** — they only produce on parallel current; **standalone banks fish any direction** but each has its own preferred directions; **coastal deep spots prefer downhill (N→S)**. Identify which one you're looking at *before* you commit.
- **Spatial coherence** — current direction is coherent across a region on a given day. **Read the current once, then pre-judge every spot on your list from it.** This is the single highest-leverage thing you can do at a seven-spot island group.
- **Up-current face.** Within any one spot, bias to the **up-current face** — that's where nutrients get forced up and the food chain stacks. Kelp-bed corner refinement (Hansen, `kzD0kSnnVPw`, medium confidence): **current downhill → work the NW corner of the kelp; current uphill → work the SE corner.**
- **Read current off observables**, not the plotter (`conditions/current-diagnostics.md`): **kelp pulled ~20 ft under = raging, surface presentations are dead, go deep**; **kelp laid flat = strong, fishable, work the down-current side**; **kelp resurfacing = slacking, switch back to the surface.** The chum bucket is an artificial "thumb over the hose" — its drift angle relative to how the boat lies separates true current from wind push.

## Finding them

`species/yellowtail.md`, Finding them:
- **Sonar, structure yellows: tight balls hugging the structure — arcs / boil-ups at ~5–10 fathoms (30–60 ft) near structure.** "We see tight balls of yellowtails hugging the structure, so you drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`).
- **Hard bottom only, never mud** (`6DzbsElGE7E`) — read bottom hardness by return thickness (thin/faint = sand or mud, thick and dark = rock) and decide whether a spot is worth working *before* hunting for fish sign on it. Works on any brand of sounder.
- **A thin, lighter mark riding higher than the bait ball can be the yellowtail itself**, pushing bait up off the rocks — that's the commit signal, not the bait pile alone.
- **Deep high-spot fish** (the KB's BOLA/Baja pattern) sit in the **150–300 ft** band on the **up-current face**, best bit 150–180 ft (`vqsD0qpwcJA` / `Jtf-bU4aM-c`) — relevant if you work Coronado Canyon or the deeper vicinity structure.
- **Sounder settings** (`planning/electronics-and-sounder.md`, Hansen, repeated doctrine — high confidence): **run manual range, not auto.** Private-boat working window **0–120 ft on older machines, 0–150 ft on newer**, regardless of true bottom depth; a school paints as a large upside-down-U at that range and shrinks to a speck on auto. When you *are* reading bottom, size the range so **the bottom sits mid-screen, not pinned at the edge** — that leaves column above it to read hardness and pick fish out. **Photograph the meter when you're getting bit** and build your own library of marks that pay.
- **Glassing** (`planning/search-and-glassing.md`): glass from a full stop or bow into the swell at ~1 kt; **3–4 minutes per full 360° scan**; **watch a bird 30–40 s** before judging it. Ranges from deck level: a few terns at **0.5–1 mi**, a big bird spot at **~2 mi**; from a hardtop, birds ~2 mi and dolphins ~4 mi. Space glass stations **3–4 mi apart**; run a contour at **16–18 mph** with a lookout ~30° off each bow.
- **Birds** (`conditions/bird-reading.md`): **terns are the best bird** — Cameron follows working terns even with nothing else flying and almost always stops and casts. **Boobies are mostly seen at the Coronado Islands and Cameron considers them worth paying attention to** (his observation, no corpus doctrine to merge). **Gulls** = life and floating kelp, paddy-finders, not gamefish. **Pelicans diving = usually the wrong area, expect mackerel** — useful as a bait tell. **Mixed piles at an open-water current break = bait only, skip**; a mixed pile **on kelp/structure** can be a real bait event.
- **The governing search rule** (`locations/island-structure.md`): **sign associated with structure is a repeatable decision; sign in no-man's-land is low value.** And when you get a popped fish near a contour, identify the structure it related to, **run the curve slowly**, do not sprint to where the fleet went, and **come back to your own marked positions at tide time.**

## Bait

`bait/making-bait.md` — the Coronados are Cameron's own mackerel spot: **drop the sabiki to ~100 ft with an 8 oz sinker**; he has loaded **5 twelve-inch mackerel on one drop** there. Twelve-inch mackerel are big, hearty baits, heartier than sardine. Buy sardine at the barge when it's available; **when he makes bait it's always mackerel.**

The reason this matters more than convenience, from `bait/fishing-live-bait.md` (`w5_x6kkN-xE`, Hansen, high confidence, and the region label names the Coronado Islands explicitly): **fishing live mackerel rather than sardine or anchovy at San Clemente, Catalina, or the Coronado Islands skews the catch toward yellowtail specifically**, screening out the calico, barracuda, and bonito bycatch a smaller bait draws. Yellowtail have been seen eating mackerel up to **1.5 lb**, sometimes five or six fish attacking one mackerel at once.

Hook position, same note:
- **Butt hook, zero weight only** — swims down and away, and **defeats sea lions at the islands that pick off nose-hooked baits**. Mechanism: pulling a butt-hooked bait reads to the bait as something biting its tail, so it bolts the other way. Applied cast: throw to the edge of a visible school, then **jerk the tail on the water** and the bait swims away from the jerk, toward the fish.
- **Nose hook becomes mandatory the moment any weight is added** (dropper loop, sliding sinker, rubber-core) — a butt-hooked bait under a sinker gets dragged backward and doesn't read as natural.
- **Back/dorsal hook is kite-only** — not part of this trip.
- Sardine specifics (`ZggReeO1nyU`): nose-hook **side to side through the clear spot at the tip of the nose**, the only way to do it; the butt hook draws blood so that bait doesn't last as long.

On a two-day trip, keep the tank honest: `bait/bait-tanks.md` — **don't overload it** (too many baits for the volume crashes the oxygen), match pump GPH to tank gallons for enough turnovers per hour, and **save culled dead bait in a 5-gallon bucket for chum**, including chumming on the anchor. The note also carries a cautionary observation of a boat on a 2-day trip whose **bait net rolled overnight and lost its bait** — if you are holding bait between days, that is the failure mode to guard against.

## Situation → technique → gear

From the `species/yellowtail.md` router, with execution from the technique notes. **Cameron's three-outfits switching doctrine** governs the day: **rig the surface-iron outfit, the heavy yo-yo/dropper outfit, and the flyline outfit simultaneously and switch as temp + bait depth change** — the three faces are states of one population, not fish types, so no row below locks you in.

**1 — Boiling / breezing fish, or fish on a paddy → surface iron, then flylined bait, then stickbait.**
Gear: **jig-stick class, 9–10 ft, 25–60 lb** (`tackle/gear-classes.md`). Irons: **Tady 45 / Tady 45 Surface, Salas 7X / 6X Jr.**, roughly **5.5″–7″, ~3 oz** (`lures/iron-jigs.md`); **go heavier (Salas 7X) when it's windy to punch the cast out** — relevant to your 12 kt afternoons. Execution (`techniques/surface-iron.md`): hang the jig about **18 in** below the tip, take the rod to **2 o'clock**, let the blank load, sweep through to 9 o'clock — **the rod does the work**; pendulum the jig **up and down, not side to side** (`VpW91AKOFVQ`), release on the **outside part of the swing** (`3dVc-2rsYII`), and **lay the reel on its side through the cast** for distance (`KLoEJInlmZo`). **Placement beats distance** — land it *on* moving fish and cut off their line of travel rather than casting into their wake. Retrieve: steady grind ("steady whine"), not too fast; **watch how the iron swims back to the boat** (`D5DR7Kx42_A`). A **wide, slow, drawn-out kick** is the change-up for picky bites and slack current — which is what a neap day is likely to hand you.

**2 — Tight balls hugging structure / marks on hard bottom at ~5–10 fathoms → yo-yo iron, then dropper loop.**
Gear: **stout 40–60 lb class rod with a high-speed reel**. Iron: **Salas 6X / Salas CP 105 class**, heavy enough to **stay vertical** in current (`lures/iron-jigs.md`). Corpus doctrine from the Coronados/BOLA roundups: **heavy full-size irons work the majority of the time on structure fish; vertical/flat-fall jigs 100–180 g depending on current are the change-up** (`D5DR7Kx42_A`).
Execution (`techniques/yo-yo-iron.md`): position **up-current** so the drop sweeps onto the structure; **free-spool straight down under light thumb pressure** so it tracks vertical instead of scoping away; then **wind as fast as you can, all the way up** — the speed is the trigger; **a couple of cranks off the bottom is where the reaction bite comes**. Kept side by side: Hansen's cadence (`wzI0lpgKT1U`) defines yo-yoing as **staying down in the zone** — cast version, **10 cranks then straight back to freespool to the bottom**, walking the iron back over as much as 150 yards; vertical version, **five or six quick cranks (~20 ft) then freespool**, cycling the same 20-ft band where fish are marked. **Strikes often come on the drop.** Both cadences stand; pick by whether your marks are suspended or pinned.

**3 — Deep marks on a high spot, fast drift → slow-pitch / vertical jigging.**
**130–250 g** wing-fall jigs, **150–300 ft** band, bit best 150–180 ft (`lures/knife-jigs.md`, `techniques/slow-pitch-jigging.md` via the router). Weight rule: **~1.5 g per foot of depth** for slow-pitch, **~1 g per foot** for a speed jig; in a fast drift go **longer and more slender**, in slack go **fatter and more fluttery**. They typically **bump it on the fall, then you wind tight.**

**4 — Fish visible but not biting (the Coronados' signature state) → flylined bait, downsize leader and hook, and wait for the window.**
Gear: **40–50 lb flyline class** per the yellowtail gear summary; the flyline/soft-rod class is ~9 ft, MH, fast, ~30–65 lb. **Drop leader size, put live bait in the water, and anchor the plan to the daily bite window rather than grinding through it.** On a neap day, the window is more likely tide-driven than clock-driven.

**5 — Bottom bait presentation on the same marks → dropper loop.**
`techniques/dropper-loop.md`: hook off a **dropper-loop knot or spider hitch**, **err long on the loop** for more bait action, **sinker 6–10 oz** at the bottom; **if the current is heavy, up the weight**; sinker weight tracks drift speed, not just depth. Nose-hook the bait (weight is on the line).

## Anchoring — get this right or the yellowtail will beat you

`planning/search-and-glassing.md`:
- **Grade first, then commit.** Idle over the high spot, mark the peak, **re-drive the same track** to confirm bait/fish sign, and only then set up.
- **Drop the anchor into the sand patch beside the rock, not on the rock** (`6DzbsElGE7E`); the same presenter frames it earlier as anchoring **in front of the structure so your lines drift back onto it** (`xI9tPJFXbUM`) — same effect, both stated.
- **Midwater/gamefish → anchor up-current, standoff scaled to current strength**, so chum and baits sweep down onto them.
- **Yellowtail specifically → anchor further still**, so a hooked fish has room before it reaches the structure. This is the break-off rule and it is called out for yellowtail by name.
- **Rode:** chain-and-rope, never all-chain (Hansen, repeated across two videos — high confidence on the structure of the rode).
- Expect the sounder to **blank the bottom while you back down** — that's aerated water under the hull, not a fault.
- If a spot is too deep to anchor, **set the drift instead** (Scotty/Brothers Sportfishing, `_ZThckj2TIM`, high confidence): stop, note the position, watch which way wind and current move you, then start up-drift; the outboard angled off the keel line works as a rudder to steer or slow the drift, and a drift sock slows a fast one.

## The rest of the card — because October is scattered

`seasonal/october.md` calls October an **everything season but scattered**, so build a variety fallback rather than a single-species day.

- **Calico bass** (`species/calico-bass.md`): fish **edges and pinch-points** — leading edge, outside edge, isolated stringers — **not the dense middle**. **Current, not calendar or tide**, governs, by the same parallel rule. Gear: **7–8 ft graphite-composite bass class, 40–60 lb**, a **7″ weedless slug on a 3/8–3/4 oz keel-weighted spring hook**, **40–65 lb fluoro leader** for kelp abrasion; **10–25 casts to the prime edge, then move** 100 ft or 100 yards. Beds re-bite — come back later. Ribbon Kelp, 5-Minute Kelp, South Kelp Ridge and Middle Grounds are the named kelp/structure spots in the library.
  - **The October wildcard worth watching for:** **grunion-in-kelp events override water quality entirely** (`OYOda6T3f-8`, 10/20/22) — every-cast bass in ugly, stagnant water you'd normally skip. The tell is a **mixed bird pile *on* kelp/structure**. If you see it, drop everything and match the bait.
- **Bonito** (`species/bonito.md`): boil **up outside the kelp**; sportboats "doing good on the bonito" is a common fall-fragmentation island line, and they **persist later into the season than many nearshore species**. Small chrome jigs / surface iron into the foam, or a flylined small bait. Also a **life indicator** — a bonito boil tells you the zone is living water.
- **Barracuda** (`species/barracuda.md`): kelp lines and boiler rocks, mixed into the bass and bonito. **Fast, flashy retrieve** — they chase a moving target. The one gear change is a **bite tippet: short single-strand wire tied with a haywire twist**, or heavier hard mono as the line-shy compromise.
- **Rockfish** on the vicinity spots (Coronado Canyon, North of North Island, Lower 9 Mile, East of Pukey Point). `species/rockfish-lingcod.md`: hard bottom, dropper loop or **200–250 g knife jigs**, squid or cut bait; **reds and lings chase bait up off the bottom — fish the column just over the rock, not only the bottom line.** Regs: California limits do not apply; **verify Mexican/Baja regs separately.**
- **Kelp paddies on the run out and back** (`conditions/kelp-paddies.md`): **drive right up to it like it's the dock** — a paddy is not spooky. **Check fast: look for visible fish, check the meter for boomerang-shaped arcs typically 90–120 ft down, give it about a minute or two, one bait, then move** (`ZFqe49jRgA0`). **A dry paddy stays dry all day** — fish only move paddy-to-paddy at night (`4xzK7YaXK5s`). If one produces, **search its line**: paddies align **N–S in open water** under the uphill current, and **along the contour near a bank edge**. Note the KB's paddy-water geography puts the best paddy water **south of Catalina/San Clemente and from Dana Point southward** — you're in that band.

---

# 4. A suggested two-day shape

**Day 1 — read the group, then commit.**
1. Bait first. Barge sardines if available; **sabiki mackerel at the islands, ~100 ft, 8 oz** — and remember mackerel is the bait that filters your catch toward yellowtail.
2. **Start in gray light if you can.** The one timing data point the KB gives for yellowtail feeding is from Ensenada (`0dIwWiOc1NY`, medium confidence, unregistered channel): **yellowtail feed hardest during gray light early in the morning** — a crew there attributed a blank stop to fishing after that window with the tide "off." That argues against the ~8 am departure norm in `profiles/cameron/boat.md` for this particular trip.
3. **Read the current once** — kelp lean, chum drift angle — and then pre-judge all seven spots from it (spatial coherence). Skip anything sitting on off-the-beach current.
4. Work the north end down (Pukey Point → Middle Grounds → Ribbon Kelp → Lighthouse → 5-Minute Kelp → South Kelp Ridge), **grading each on the meter before you commit bait** — every stop on an ungradeable mark is a bait budget you spend for nothing. Verify **temp and color spot to spot**; the group's spread is real.
5. **Be on your highest-percentage spot an hour before the tide change**, fishing when it hits.
6. **Turn for home ahead of the afternoon W build.**

**Day 2 — spend day 1's information.**
- Your own day-1 marks are the best intel you will have, and they age differently than a fleet report: `planning/report-reading-and-forecasting.md` puts open-water bluefin at **10–15 nm overnight** and low single-digit mph intraday, but **structure fish on a rockpile are not that problem** — go back to the spots that graded out, at tide time, per the fathom-curve worked example.
- If day 1 said "seeing not biting," day 2 is a **window discipline** day: pick the two best spots, arrive an hour before each change, run the flyline outfit with a downsized leader, and be patient instead of driving.
- If day 1 said dead water — no current, bait pointing every direction, marks not converting — that is the **treadmill-off** read, and the answer is **reposition to where current is running or wait for the change**, not more casts.
- Only extend offshore (Lower 9 Mile at 66.2, or the KB-named compact spots further out like 371 at 32 16.200 / 117 32.800) if you actually find an **edge**. On the numbers you gave, there is no offshore warm cell pulling you out there, and the October fish that do condense offshore are condensing toward **Tanner and Cortez**, which is not a Coronados-trip destination.
- **Fleet as a data layer, not a destination:** `planning/fleet-intelligence.md` — "**go fishing for fish, not for boats**"; a cluster of boats on a spot is usually one boat stopping and the rest following. Cameron's own verification-oriented use is **AIS stop/start tracking on Coronados sportboats** (e.g. the Grande, MMSI 366746210) as a learning layer, which is exactly the kind of thing a two-day trip is good for building.

---

# 5. Fish care (plan it before you land one)

`fish-care/tuna-care.md` carries the only yellowtail-specific bleed data point in the KB (`Klfb433I3Uk`, San Clemente, 2019-10-04, unregistered channel — medium confidence; the note flags that **no dedicated yellowtail bleed-and-chill note exists**): as soon as the fish is on deck, **cut the artery**, hold the fish **upside down in a bucket**, **~5 minutes** is enough for the blood to pump out, then **on ice**. The tuna chain in the same note is bleed → **field-dress (guts and gills out)** → **wet-towel cooldown** → chill.

`fish-care/dorado-and-general.md`, general principles for every species: **salted slurry — about 2 cups of rock salt per 7–10 lb bag of ice, plus a splash of seawater**, which is what drops the mix below freezing; **keep fish cold and out of the sun**; **never rinse in fresh water**; and **bring a car cooler for the drive home** — the cold chain has to survive past the dock, which matters more on a two-day trip than a single day.

Ice: Cameron's own panga load is **100–125 lb per trip** (`profiles/cameron/boat.md`) — a two-day trip is where that number gets tested.

---

# 6. If this is Cameron's Panga Marine Marquesas 22

Resolved against `profiles/cameron/rods.md` and `boat.md`, the three-outfits doctrine maps cleanly:

- **Surface iron** → the **Torium 20HG on the Phenix Abyss 10'0" (25–60 lb), 50 lb braid** — the full surface-iron setup.
- **Yo-yo / dropper loop** → the **Trinidad 40 on the 8'0" XH 40–80 lb blank, 80 lb braid** — the heavy setup, explicitly for yo-yo iron and sinker rigs.
- **Flyline** → the **Avet MXJ on the Teramar 9'0" MH (30–65 lb class), 50 lb braid**, with the **Lexa 400** (9'0" H, ~20–60 lb, 50 lb braid) as the workhorse backup.
- The **Talica 25 / Fathom 80** are trolling and jumbo-bluefin tools — not needed for this program on these numbers.
- Boat envelope notes that matter: **35 kt top end, 30-gal bait tank on a single starting battery with the NOCO charger holding it up so the pump can run overnight**, **10 rod holders**, normal launch **Dana Landing, Mission Bay**, home waters explicitly include the Coronado Islands. **Drain the bait tank coming in** — that's heavy stern water on a small foam-filled hull.

If it isn't Cameron's boat, everything above stands in class terms and `tackle/gear-classes.md` is the lexicon; `tackle/rod-and-reel-selection.md` notes that the full five-outfit ladder is the kit for **anything overnight to 2+ days**.

---

# 7. What this knowledgebase could not tell you

Listed so you know exactly where to go get it elsewhere:

1. **Every part of your permits/papers question** — Mexican fishing licence, vessel paperwork, immigration, customs, border-crossing procedure for a private boat. Nothing in the KB.
2. **Mexican bag, size, and gear limits** for anything you'd catch there.
3. **Any October record of the Coronados** — the KB documents this zone as the spring classic.
4. **What chlorophyll 0.9 means numerically** — no scale, no threshold anywhere.
5. **Any SST number for yellowtail** — no on/off temperature for the species.
6. **Per-spot detail for the seven Coronado spots** — depths, contour shape, kelp extent, which current direction each one fishes. The library gives coordinates; `locations/island-structure.md` gives only the generic typology.
7. **Whether these spots are quick reads or all-day search boxes.**
8. **Overnighting** — anchorages, whether to run home between days, and the whole logistics layer (fuel, float plan, safety gear, comms).
9. **Your actual tide times** — the KB has the timing rules, not the data.
10. **Mission Bay / Dana Landing entrance exposure** — the KB has San Diego Bay's swell window only.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/report-reading-and-forecasting.md`, `planning/fleet-intelligence.md`, `seasonal/october.md`, `seasonal/september.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `locations/bight-geography.md`, `locations/island-structure.md`, `locations/zone-lexicon.md`, `locations/bightsst-eval-targets.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/bonito.md`, `species/barracuda.md`, `species/rockfish-lingcod.md`, `species/yellowfin-tuna.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `bait/making-bait.md`, `bait/fishing-live-bait.md`, `bait/bait-tanks.md`, `lures/iron-jigs.md`, `lures/knife-jigs.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `fish-care/tuna-care.md`, `fish-care/dorado-and-general.md`, `sources/spot-lists.md`, `profiles/cameron/boat.md`, `profiles/cameron/spots.md`, `profiles/cameron/rods.md`  
*videos:* `D5DR7Kx42_A`, `YZtX1MiT0y8`, `XLVUhV8DW64`, `OYOda6T3f-8`, `5to3Q5P7w90`, `5p6gu14ZC4w`, `HzE4FHHcvTk`, `NC3-3pJDEgo`, `fri_BWI-VA0`, `9tTM99InluM`, `w5_x6kkN-xE`, `ZggReeO1nyU`, `6DzbsElGE7E`, `xI9tPJFXbUM`, `kzD0kSnnVPw`, `ZFqe49jRgA0`, `4xzK7YaXK5s`, `9hEa3sGTh40`, `SgF5hRlEGqU`, `vqsD0qpwcJA`, `Jtf-bU4aM-c`, `Klfb433I3Uk`, `T3p1mrqNjIo`, `8YvmROeVL-0`, `mUrihh0V59M`, `HTssdpnUGMo`, `VpW91AKOFVQ`, `3dVc-2rsYII`, `KLoEJInlmZo`, `wzI0lpgKT1U`, `_ZThckj2TIM`, `0dIwWiOc1NY`, `xIUKmH9ccgQ`, `Rf1HKJG-SDg`, `E4vKwRaRueA`, `2gHRrR3D8rY`, `xPFm_ZV2PZU`, `mscHk0qiXnk`, `Ul5FLB2dFgQ`  
*gaps admitted:* Mexican paperwork for a private boat fishing the Coronados — fishing licence, vessel documentation, immigration, customs, border-crossing procedure — is entirely absent from the KB; the only Mexico-regulatory traces are an unverified 2019 Baja California Sur circle-hook claim in techniques/flyline.md and an incidental note in species/calico-bass.md that one 2012 Cedros charter's permits were obtained in Tijuana. | No Mexican bag limits, size limits, or gear restrictions for any species; species/rockfish-lingcod.md only states that California/CDFW rules do not apply in Mexican waters and must be verified separately. | No October-at-the-Coronados entry exists — the KB frames the Coronado Islands as the warming-transition (spring) yellowtail classic, so the October program here is assembled from general fall-fragmentation doctrine plus Cameron's water-state-over-calendar rule, not from a documented October Coronados bite. | No numeric chlorophyll scale anywhere in the KB — chlorophyll 0.9 cannot be mapped to 'clean' or 'green'; only the bloom-age and fish-the-edge doctrine applies. | No SST threshold for yellowtail — the KB gives no temperature at which they turn on or off, and no Coronados-specific temperature band. | No per-spot structure detail for the seven Coronado Islands spots (depths, contour orientation, preferred current direction, kelp extent) — sources/spot-lists.md gives coordinates only, and locations/island-structure.md is generic typology. | The KB does not classify the Coronado spots as 'complex' vs 'compact' search boxes, so it gives no basis for budgeting time per spot there. | Nothing on overnighting in Mexican waters — anchorages, whether to run home between days, fuel planning, float plans, safety gear, or comms for a two-day private-boat trip. | No tide times or tide data — the KB carries the timing rules (arrive an hour before the change, late-morning slack after ~9:30) but you must pull an actual tide table. | No swell-exposure note for the Mission Bay / Dana Landing entrance; conditions/sea-state.md covers only the San Diego Bay entrance window (~160-186 degrees). | Sea-lion depredation is documented as general island doctrine (butt-hook counter, free-spool slack trick), not specifically observed at the Coronado Islands. | No October bluefin or yellowfin guidance tied to a 66-67 F, near-flat SST field near the border — the KB's fall pattern condenses bluefin toward Tanner and Cortez, well outside a Coronados trip, and gives no yellowfin temperature floor.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Two days at the Coronado Islands, mid-October — the program

## First, the thing that reframes the whole trip

**The Coronado Islands are Mexico.** The KB tags them `baja-pacific-north` and describes them as "~13 mi from San Diego, off Mexico" (`species/yellowtail.md`). That sets both the fishing envelope and the paperwork problem — and the paperwork section below is mostly a list of what this KB does **not** know, because it genuinely doesn't.

---

## 1. The envelope (day-plan protocol step 1b)

Per `planning/day-plan-protocol.md`, I set `{regions, waters}` before opening a single species note. For a San Diego-launched two-day run to the Coronados:

- **`regions`: `baja-pacific-north`** (the islands themselves) **+ `socal-bight`** (the transit lane — Point Loma, 9 Mile Bank). Vocabulary in `locations/regions.md`.
- **`waters`: `island`** (primary), **`nearshore-coast`** (the island kelp/beach edges), **`bank`** (9 Mile Bank and the Coronado Canyon rockfish ground on the way down), **`open-ocean`** only if you glass paddies on the transit.

What that gate **excludes** outright: everything `cortez-*` (cabrilla, etc.), and the `socal-bight`-only notes — `species/swordfish.md`, `species/opah.md`, `species/california-spiny-lobster.md`, `species/spotted-bay-bass.md`. No hoop-net program in Mexican water off this KB.

**Two open questions the protocol says I must ask rather than assume.** `profiles/cameron/boat.md` carries an explicit machine comment: `range_nm` and `sea_state_max_ft` are `null` — "Cameron has not stated these — left null rather than guessed. Until they are filled, the protocol must ASK." So:

1. **What's the boat's range and sea-state ceiling?** That decides whether the 9 Mile Bank / Coronado Canyon detour is in or out.
2. **Does "two days" mean two day-runs from the mainland, or an overnight on the hook down there?** The KB has nothing on overnighting a private boat in Mexican waters — no anchorage, no legal, no procedure. Two day-runs is what I've planned.

---

## 2. Reading the conditions you gave me

### SST: 66.8 islands / 66.2 nine-mile / 65.9 Point Loma

**That is a gradient, not a break, and it changes the plan.** `conditions/water-temperature.md` is explicit that the value "is usually not the absolute number but which **side of a break** a species sits on," and that sharp offshore edges "can jump multiple degrees in ~1 mi." Your three points spread **0.9 °F across the entire run** — roughly the noise floor of the read. `seasonal/october.md` says October is the regime change where you "look 100 % at your temp chart and chlorophyll" and "build the plan on the break structure, not on spot names" (`XLVUhV8DW64`, `OYOda6T3f-8`) — but there is no break in these numbers to build on. So the plan **defaults back to structure, bait and current at the islands**, which is what the rest of this document is.

Consequences for the pelagic options, so you don't waste a day chasing them:

- **Bluefin** — the break-side rule (`conditions/water-temperature.md`) is *relative*: cool side when the water is warm, warm side when it's cold. You need an edge to apply it and you don't have one. And `seasonal/october.md` says that as the coast cools and fragments, bluefin **condense outward to Tanner and Cortez** — away from you. The 76 °F ceiling being soft (`9/14/22`) doesn't help here; that softens *warm* exclusions.
- **Yellowfin** — want **SST max × chlorophyll min** (`conditions/water-temperature.md`, `seasonal/october.md`). The islands are your warmest point at 66.8 °F, but the KB's only yellowfin-sign-with-a-temperature data point is white terns working over **72 °F** near the 209 (`species/yellowfin-tuna.md`, `SczdZIq3UmE`). There *is* a documented Coronados school-yellowfin entry — a 2018-10-31 tackle tip recommending **20 or 25 lb fluorocarbon** for a bite that was "starting" (`NN5MWeRA28o`) — but the note itself caps it at **low confidence** (promotional segment). Carry a light-fluoro leader; do not build the trip on it.
- **Dorado** — `conditions/water-temperature.md` puts them on the green-cold/blue-warm boundary around **71–72 °F**. 66.8 is well under.

### Chlorophyll 0.9 — the KB gives you no number to compare it to

I have to be straight about this: **this knowledgebase contains no numeric chlorophyll scale.** `conditions/water-color.md` treats chlorophyll as an **age-and-edge** read, not a threshold, and the only numeric mention anywhere is an endpoint-hygiene rule in `config/endpoints.md` (check `chlorophyll_coverage_pct` before reporting chlorophyll at all). So "0.9" is uninterpretable against this KB. What the KB *does* give you, and what you should actually do on the water:

- **Distinguish a new cold bloom from a mature bloom edge.** New = cold + green after an afternoon NW blow (often with a ~5 °F overnight drop) — that's a fresh local upwelling event, "bad *now* but productive *later*." Mark it for the recovery, don't expect it to fish today. Mature bloom **edge** = where the chain has caught up and bait has stacked. Fish the edge.
- **Bait holds in the dirtier water; predators work the seam.** Clean-water trolling found nothing because the bait wasn't there (`8/17/22`). Do not default to the prettiest blue water — find the dirty/clean **seam** and work it.
- **Cameron's own doctrine, if this is your trip:** in warm-water years weight color at least as heavily as SST, and don't fish "dirty green" water for gamefish (`conditions/water-color.md`).

### Wind NW 8 → 12 kt, swell NW 3 ft @ 10 s

- **Steepness rule** (`conditions/sea-state.md`): period drives feel far more than height. 3 ft @ 10 s is a benign ratio — the flagged case is "period in seconds approaching the height in feet," and 3–4 ft @ 4–5 s is what's described as brutal.
- **But you are sitting exactly on two of Dave Hansen's go/no-go lines** (`NC3-3pJDEgo`, medium confidence, single-mention): **wind above ~12 kt is what raises whitecaps**, and that's his personal don't-run cutoff; and **swell interval under 10 seconds is a hard bad-sea flag**. Your afternoon is 12 kt and your interval is 10 s — at the edges, not over them. His named unfishable combo (12–15 kt with 4–8 ft @ 9 s) is worse than your forecast.
- **Forecast error is asymmetric.** Assume the forecast errs on the worse side and that afternoon W at the islands **strengthens** rather than eases (`conditions/sea-state.md`, Ep. 6). If it is windier than forecast in the morning, **assume it builds all day and a small boat bails early** (`7/14/22`).
- **Pull a 12–24 h wind hindcast, not just the forward forecast.** A calm-morning number hides overnight wind and the leftover chop it left.
- **Homebound wind.** `conditions/sea-state.md` names this exact case: runs south into Mexican water put a wind on the return leg — "uphill misery." **Plan the return against the afternoon build, not the outbound conditions.** With NW 12 in the afternoon, the beat home is the part of the day to budget for.
- **Current-vs-swell opposition:** where the current field opposes the NW swell it compresses the interval and stands the swell up — degrade the forecast on those route segments.
- One caution on a figure you may be tempted to use: Cameron's charted entrance-exposure window (open to swell **160°–186°**, channel axis **186°**, Point Loma blocking anything west of the axis) is stated in `conditions/sea-state.md` for the **San Diego Bay entrance specifically**. A NW swell is on Point Loma's blocked side of that. The KB gives **no equivalent figure for the Mission Bay / Dana Landing entrance**.

### Moon: last quarter

- **Quarter moon = neap tide** — the *smallest* tidal range of the month (`conditions/tide-and-slack.md`, mechanism from `9tTM99InluM`). Expect the weakest tide-driven current of the cycle. Current is the engine in `conditions/current-structure.md`, so this is a real headwind.
- **You are outside the elevated moon windows.** `conditions/moon.md` reconciles to full/new **±1 week** as elevated-probability, leading days strongest. Last quarter is neither. The upside: you also skip full-moon daytime bass suppression (calico/sand bass gorging at night and shutting down by mid-morning), so **your bass window is not shut mid-day** — and there's no bright-moon paddy redistribution to chase.
- **The operative consequence** comes from `conditions/tide-and-slack.md`: when the bite is off-peak, "action **compresses into the tide windows**" — wide-open days bite all day, marginal days don't. So **anchor both days' zones to tide times**, and **be on the highest-percentage spot an hour BEFORE the change, fishing when it hits** — do not arrive *at* the change (`2/20/25`). This dovetails exactly with the one Coronados-specific behavioral warning in the KB.

### The one Coronados-specific warning you need

`species/yellowtail.md`: Coronado yellows run **"seeing-not-biting" cycles with narrow daily windows** — you will mark and even *see* fish that won't eat until a short window opens (`YZtX1MiT0y8`). **Anchor those days to tide and current, not to the clock.** With a neap tide, that discipline is the difference between the trip working and not.

---

## 3. What's actually on the table (species routers, filtered to the envelope)

| Target | Gate | KB depth for this trip |
| --- | --- | --- |
| **Yellowtail** — the primary | `baja-pacific-north` + `island`/`bank` | Deep. "The Coronados are synonymous with yellowtail" (`D5DR7Kx42_A`) |
| **Calico bass** — the fill and the fallback | `baja-pacific-north` + `island`/`nearshore-coast` | Deep, and October-relevant (see grunion note below) |
| **Rockfish / lingcod + ocean whitefish** — the weather fallback | `baja-pacific-north` + `bank`/`island` | Good, with a Baja data point |
| **Bonito, barracuda, sheephead** | in-gate | Bycatch/fill; bonito matter tactically (below) |
| Bluefin / yellowfin / dorado | in-gate but conditions don't support | See §2 |

**An honest gap you should plan around: this KB's Coronados content is spring-weighted.** `species/yellowtail.md` calls the islands "the warming-transition (**spring**) classic," and the dated Coronados entries are April (`YZtX1MiT0y8`, `ejUTAnONf7o`) and November (`F9XjGMEvvag`). **There is no October-at-the-Coronados doctrine in this knowledgebase.** Everything below is built from universal structure/current/technique doctrine plus the Coronados entries that do exist — not from an October Coronados prior. Treat the seasonal layer as thinner than the tactical layer here.

**October's one wildcard, and it's a good one:** `seasonal/october.md` — **grunion-in-kelp events override water quality entirely** (`10/20/22`). When grunion pile into the kelp you get **every-cast bass in ugly, stagnant water** you'd normally skip. The tell is a **mixed bird pile *on* the kelp/structure** (`conditions/bird-reading.md`) — as opposed to a mixed pile at an open-water current break, which is bait only and gets skipped. Match the bait: a 7" split-tail slug on a sled/leadhead, every cast (`species/calico-bass.md`).

---

## 4. Spots

From your own library, `sources/spot-lists.md` (committed under the 2026-08-12 waiver — "none of these spots are secret"). Format is `deg min.mmm`, N latitude / W longitude.

**Coronado Islands (the six-plus-one that BightSST splits out individually):**

| Spot | Position |
| --- | --- |
| Pukey Point | 32 26.850 / 117 18.000 |
| Middle Grounds | 32 25.810 / 117 15.950 |
| Ribbon Kelp | 32 24.800 / 117 13.880 |
| Lighthouse | 32 23.290 / 117 14.570 |
| 5-Minute Kelp | 32 22.940 / 117 13.515 |
| South Kelp Ridge | 32 22.000 / 117 13.260 |
| Rockpile | 32 17.620 / 117 10.030 |

**Bottom / bad-weather ground nearby:** Lower 9 Mile Bank 32 32.500 / 117 20.500 · Coronado Canyon 32 30.300 / 117 17.500 · North of North Island rockfish area 32 27.380 / 117 18.000 · East of Pukey Point (yellowtail **and** rockfish) 32 27.000 / 117 14.100.

**On the transit, if range allows:** North 9 Mile Bank 32 38.000 / 117 26.000 · South 9 Mile Bank 32 32.000 / 117 21.000 (`profiles/cameron/spots.md`).

---

## 5. Day 1 — bait, read the current, let the meter pick the technique

### 5a. Bait before anything

- **Make mackerel at the islands** — the KB records this as your own program (`bait/making-bait.md`): sabiki dropped to **~100 ft** with an **8 oz** sinker; has loaded **5 twelve-inch mackerel on one drop**. Twelve-inch macks are big, hearty baits, heartier than sardine.
- **Buy sardine at the barge if they have them.** Barge discipline (`bait/making-bait.md`, `7WapaxdtjQg` / `bM2vUS1B-yQ`): **avoid the 6:00 a.m. sport-fleet rush** — be there **5:00 a.m. or earlier** (Hansen's own target is "at least five o'clock, if not four thirty"), or 7:00 a.m. Hail on **VHF ch 11** with the barge's name twice plus yours. Tell the attendant you want it **loaded light** and you're not in a rush. Never board the barge. Tip at the end.
- **Bait choice has a tactical edge here:** if the tank ends up **anchovy**, `techniques/flyline.md` (`8TO-tuYjwWk`) says a fly-lined anchovy draws bycatch as readily as the target — that's the stated cue to switch to iron.

### 5b. On arrival, read the current before you pick a spot

Do this first, every time, from `conditions/current-diagnostics.md`:

| Kelp behavior | Current | Call |
| --- | --- | --- |
| Kelp pulled **~20 ft under** | Raging | **Surface presentations are dead** — go deep / weighted |
| Kelp **laid flat** on the surface | Strong | Fishable but hard; work the **down-current side** |
| Kelp **resurfacing / standing back up** | Slacking | **Switch back to the surface / lighter** |

Also: **chum-drift angle vs. how the boat is lying** separates true current from wind push — chum swinging off at an angle to the boat's lay is real current cutting across, and that angle is your direction sensor. The chum bucket is a deliberate "thumb over the hose" you can deploy on purpose. And **do not trust the chartplotter's current-arrow layer — it's reading wind, not current** (`sIoNELGlxmk`, medium).

### 5c. Structure typology decides which of your seven spots can work today

`locations/island-structure.md` + `conditions/current-structure.md`:

- **Land-attached perpendicular ridges are two-directional** — they only produce on **parallel** current (running along the shoreline). Straight **into** the beach is marginal; straight **off** the beach is **dead**. Don't waste a tide window on a ridge that today's vector can't light up.
- **Standalone banks fish any direction** but each has its own preferred ones, learned spot by spot.
- **Coastal deep spots default-prefer downhill (N→S).**
- **Late-fall exception, kept side by side:** at San Clemente in late November the bass bites *required* current running **into** the island with off-color water present — fish used the dirt to ambush. Encode parallel as the prior, into-beach as a viable late-fall/off-color state, off-beach as dead. Mid-October sits right at the front edge of that exception, so don't reflexively reject an into-the-island day.
- **Current direction is spatially coherent across a region** — once you've read it at your first stop you can pre-judge the whole day's list without running it.
- **Kelp corner selection** (`kzD0kSnnVPw`, `sIoNELGlxmk`, dave-hansen): downhill current → work the **northwest** corner of the bed; uphill → the **southeast** corner. And **anchor the kelp, don't drift through it** — drifting gives up the edge-holding pattern entirely.

*Caveat I owe you: `locations/island-structure.md` is region-gated `socal-bight` only. Its typology is universal in framing but its worked examples are Catalina/SCI. Applying it at the Coronados is an extrapolation the KB doesn't formally authorize.*

### 5d. The meter picks the technique — this is the core of the day

From `species/yellowtail.md` § Finding them, the depth bands are decision rules, not descriptions:

- **Marks at 40–60 ft that aren't showing** → *"usually like surface iron fish and like light bait zone — so we're **not** going to be yo-yoing today"* (`0DKmYId1NN4`). Stay on light bait and casting; go all-in on surface iron once they start boiling.
- **Tight balls hugging structure / arcs at ~5–10 fathoms (30–60 ft) near structure** → **yo-yo iron**, then dropper loop. "Drop something with weight to get down there and provoke a reaction bite" (`D5DR7Kx42_A`).
- **Stratified column** — marks running as lines from the bottom up through mid-column → fish **actively hunting**; put **slow-trolled baits** out. **Ball stuck to the bottom** → fish present but not hunting: that's **dropper-loop water, not flyline water** (`HTowqnwAMeA`).
- **High and spread = biting; tucked tight to the bottom = not** (same trip, `HTowqnwAMeA`). This behavioral read overrides the depth bands — same fish, same mark, worth working or not depending on distribution.
- **Hard bottom only, never mud** — thin return = sand/mud, thick return = rock. Read bottom hardness to decide if a spot is even worth working before you look for fish on it (`6DzbsElGE7E`).
- **A thin, lighter mark riding higher than the bait ball is the yellowtail itself**, pushing bait up off the rocks — that's the sign to commit, not the bait pile alone.
- **Marked but not surfacing?** Get any lure down to their depth and it gets bit: *"just about every lure that makes it down to the depth that fish is, is a bite"* — and yo-yo iron has "absolutely" out-fished live bait "multiple times" in exactly this scenario (`tpmOYXYQwhU`, registered channel, single mention — medium).
- If you do check a paddy on the transit: look for **boomerang-shaped arcs at ~90–120 ft** under a paddy showing nothing on top; give it a minute or two before writing it off (`ZFqe49jRgA0`).

### 5e. The afternoon wind adjustment

The KB has a **dated Coronado Islands** data point for exactly this shape of day (`species/yellowtail.md`, `ejUTAnONf7o`, Jared Saaib, 2026-04-21, registered voice, single session — medium): **25 kt gusts**, fish metered and **swiping the iron without committing**; the crew read it as *the wind turning the bite*, and other boats confirmed the day had gone *"mostly yo-yo."* The surface iron still produced two, so the note is explicit that this is **a re-rank, not an abandonment**.

Your afternoon is 12 kt, not 25 — far milder — but the direction of the adjustment is the same: **as the NW builds, shift weight to the yo-yo and keep the iron going as a picker.** The complementary move from `conditions/current-diagnostics.md`: when the wind-driven current lays the kelp flat, surface is dead and you go vertical; when the kelp resurfaces, go back on top.

### 5f. Bonito interference — have the counter rigged before you need it

`species/yellowtail.md` has a specific row for this, and it's a real Coronados problem: **bonito working the surface intercept flylined baits before they reach the yellowtail.** The fix is **sliding sinker instead of flyline** — the added weight gets the bait *under* the bonito layer and in front of the yellows faster. Build: **2–4 oz egg sinker straight to a J hook, 2/0–4/0**, scaled to wind and depth, on a 30 lb live-bait class outfit (`yGXSrUauo2w`, Steve Carson, registered voice, single mention — medium). Have one tied.

---

## 6. Day 2 — spend the fresh day on what day 1 taught you

- **Your own day-1 marks are your freshest report.** The template from `locations/island-structure.md` (`8/31/22`): one popped fish appears → identify **the structure that fish related to**, treat it as signal not noise → run the contour **slowly** and wait → **do not sprint to where the fleet went** → **return to your own marked positions at tide time.** The governing line: *sign associated with structure is a repeatable decision; sign in no-man's-land is low value.*
- **Age everything else.** `planning/report-reading-and-forecasting.md`: reports have a shelf life measured in miles (advection), and absence of reports is coverage bias, not absence of fish. Hansen's chart method (`JiJYamo0QHk`): sighting dots are age-coded **red = today, yellow = yesterday, green = the day before** — read the 3-day trend and **run to where the water is heading, not where it was**; if the projected water is empty, work back down the trend line toward yesterday's position, because the fish are usually in between.
- **The fleet layer, and its dissent.** `planning/fleet-intelligence.md` records **AIS sportboat stop/start tracking at the Coronado Islands** (e.g. the Grande, MMSI 366746210) as one of the most valuable data sources for learning these islands — AIS is third-party-observed and harder to fake than radio chatter. Kept side by side, unreconciled: Hansen's stated practice is that **when he sees a cluster of boats he goes the other way**, hunting clean water with no boats on it. Both are in the KB; the choice turns on whether you're trying to *learn the islands* (AIS, follow the stops) or *find unpressured fish today* (go the other way).
- **The weather/bottom fallback if both mornings die.** Drop onto Coronado Canyon / Lower 9 Mile / North-of-North-Island with **dropper loops**: sinker **6–10 oz** at the very bottom, hooks on the loop(s) above; **longer loop = more bait action, err long**; heavier lead for rock cod and deeper water or when current is up, lighter for a seabass-style presentation kept off the bottom (`techniques/dropper-loop.md`). Single-hook rockfish version keeps the hook **no more than ~2½ ft** above the sinker. The nearest Baja analogue in the KB (`species/rockfish-lingcod.md`, Ensenada, `0dIwWiOc1NY`): the crew slid out to where the bottom drops to about **300 ft** over rock and split the boat between **slow-pitch jigging** and a dead-bait dropper — both produced steadily, on a mixed bag of reds/vermilion, bocaccio and multiple lingcod. **Note explicitly: California/CDFW rockfish regs do not apply in Mexican waters, and this KB carries no Mexican bottomfish regs at all.**

---

## 7. Gear, by class

From `species/yellowtail.md` § Gear summary and the technique notes.

**Surface iron** — jig-stick class, **9–10 ft**. A surface iron runs **2–3 oz**, distinctly lighter in the hand than a **5–6 oz** yo-yo iron (`VpW91AKOFVQ`, registered voice — high). **Wind up → heavier iron** (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`) — relevant to your 12 kt afternoons. **If the bait is small anchovy ("rice"), downsize hard:** drop to a Tady AA-light / A1-light class jig, roughly **a third the weight of a Tady 45** — on small bait the small jig out-bites the big one **two or three to one** — and the light iron drags the tackle down with it: medium-action **9 ft** graphite-composite stick, smaller narrow reel, **~50 lb braid** to a short fluorocarbon leader (`pcwcRdmWmLc`).

**The retrieve is the presentation.** Dan Wade, registered voice, stated in two videos (`yn1suHH6b1Y`, `Ec2GaNpiOHI`) → high confidence: it's a **serpentine action**, and **every third or fourth time the jig kicks out to the side — that kick-out is what triggers the bite**, because it imitates the bait that separated from the ball. If the jig is swimming flat, speed it up or slow it down to make it kick.

**Yo-yo iron** — stout **40–60 lb class** rod with a **high-speed** reel, heavy full-size iron (Salas 6X class). Position **up-current** of the mark; **free-spool to the mark thumbing the spool** so the iron falls under light tension and tracks straight down instead of scoping away. Then **wind as fast as you can, all the way up** — speed is the trigger, there is no cadence. **On the bite, don't set the hook — keep cranking through it** (`5pbA-wXoric`). Line: **40 lb works, 50 better, 60 better still, "because the fish don't care."** Carson's stated base rig for **12–30 lb yellowtail near an island or bank in 120–180 ft** (`RNRFrfepiW0`, registered channel): two-speed **Penn Fathom 30**, **65 lb braid** with a **50-yard 40–50 lb mono top shot**, **8 ft 30–60 lb** all-around rod, treble hook, **Tady 4/0**; colors **scrambled egg, blue-and-white, and red crab when there are crabs around**.

**Flyline** — **40–50 lb** class, 8–9 ft, enough backbone to turn a fish off the rocks. **Nose hook** (the clear spot in front of the eyes) is the all-purpose position. **Coronados-specific hook note:** as a Coronados bite picked up, the boat's tip was to **downsize to smaller J hooks for flylining fluorocarbon — Owner Ringed Flyliner, sizes 1, 2 and 4** (`F9XjGMEvvag`, 2018-11-20, unregistered channel — medium).

**Dropper loop** — same heavy class rod, 6–10 oz.

**Slow-pitch / knife jig** — **130–250 g**, if you find deep high-spot marks. The KB's band is **150–300 ft, bit best 150–180 ft**, fish stacked on the **up-current face** — but that's a **BOLA/Baja single-trip source at medium confidence** (`vqsD0qpwcJA`), not Coronados doctrine.

**Calico** — 7–8 ft graphite-composite bass class, 40–60 lb; **7" weedless slug on a 3/8–3/4 oz keel-weighted spring hook**; **heavy fluoro leader, 40–65 lb**, for kelp abrasion. Method: **10–25 casts to the prime edge of a bed, then move — 100 ft or 100 yards.** If they're not on the prime spot they're usually not in the bed. **Beds re-bite — come back later** (`species/calico-bass.md`).

### If this is the Panga 22 in the profile — the owned-gear pass, gaps named

`planning/day-plan-protocol.md` says never recommend gear the angler hasn't said they own, and **name the gap** when a called-for class has no match. Against `profiles/cameron/rods.md`:

| Called for | Your match | Verdict |
| --- | --- | --- |
| Jig-stick, surface iron | **#5 Torium 20HG** on Phenix Abyss 10'0" 25–60 lb, 50 lb braid | Clean fit — the profile calls it the full surface-iron setup |
| Flyline 40–50 lb | **#2 Avet MXJ** on Teramar 9'0" MH 30–65 lb, 50 lb braid; **#4 Lexa 400** on Okuma PCH 9'0" H, 50 lb braid | Two good options |
| Yo-yo, 40–60 lb + **high-speed reel** | **#1 Trinidad 40** on M&M/Rainshadow 8'0" XH 40–80 lb, 80 lb braid | **Partial.** The rod is right and the profile lists yo-yo as its role, but it also flags a **"relatively soft tip"**, and **no gear ratio is recorded for the Trinidad 40 anywhere in the profile.** The yo-yo doctrine is built on a high-speed reel. Confirm the ratio before you count on it |
| Dropper loop / sinker rigs | **#1 Trinidad 40** (role explicitly includes sinker rigs) | Fits |
| Slow-pitch / knife jig 130–250 g | **Nothing** | **Gap.** The profile's own open items list a dedicated SPJ/speed-jig setup as still being shopped. If you end up on 150–300 ft high-spot marks you have no rod that fishes that way — go dropper loop instead, don't substitute |
| Bass/calico 7–8 ft, 40–60 lb | **#3 Tranx 400** on Phenix M1 SMX-82H 8'2" H 20–45 lb | Closest fit, but the profile records **braid TBD, respool pending** — spool it before the trip |

**Boat-side facts from `profiles/cameron/boat.md` worth staging around:** 30-gal bait tank on a Rule 401 (500 GPH, 2.1 A) running off the **single starting battery** — the **NOCO GEN5X1** is what lets the bait pump run **overnight**, which is exactly the day-1-to-day-2 problem. **100–125 lb ice per trip.** Normal departure ~8 a.m. — for a tide-anchored, wind-limited October day at the islands, that is later than this plan wants; the wind builds on you. **Drain the 30-gal tank coming in** (heavy stern water on a small foam-filled hull).

---

## 8. Fish care over two days

`fish-care/dorado-and-general.md`: **the salted slurry** — roughly **2 cups of rock salt per 7–10 lb bag of ice**, plus a splash of seawater to wet it; the salt is what drops the mix below freezing. Get fish cold fast and keep them out of the sun. **Never soak or rinse the catch in fresh water** — it degrades colour and flesh. Fillets: ice-saltwater soak, rinse in salt water only, **pat dry before bagging**; water-displacement bagging gets you a near-vacuum seal with no machine. Storage windows: **~3 days refrigerated**, **1–3 months** vacuum-sealed and frozen, **1 week to 1 month** in a plain ziplock.

---

## 9. Papers and permits — and this is where I have to stop short

**The knowledgebase does not cover taking a private boat into Mexican waters.** `sources/regulatory-claims.md` carries an explicit **"Known gap"** section saying Mexican licensing and entry requirements are absent, that `FMM`, `tourist permit` and `fishing licence` return no hits outside that file, and that "the KB currently says none of it." I'm not going to fill that from general knowledge.

**What the KB does have** is one paperwork block, and it was written for a **drive-across trip to Bahía de los Ángeles** — a different region (`cortez-north`), a different mode of entry, unregistered source (`P36VGPPf120`), jurisdiction **INM for entry / CONAPESCA for fishing**, as reported **2026-08-06**, stamped verify-before-you-travel (`locations/bahia-de-los-angeles.md`):

1. **FMM** (the tourist permit) — filled out online in advance; needs **passport details, point of entry, and length of stay**; it produces a printout. **Print it.** One viewer reported being checked three times on a previous trip.
2. **Mexican fishing licence** — bought online. The source notes a **new website as of 2026**, so search fresh rather than trusting an old bookmark. Have your passport with you.
3. **Passport.**
4. Plus **vehicle insurance**, mandatory in practice, **Baja Bound** named — but that's a *car* item on a *drive* trip, not a boat item.

`locations/cedros-island.md` says the same thing from the other direction: Mexican paperwork "is not covered by this source," pointing back to the BOLA entry and telling you to **verify current rules with the Mexican authorities before travelling**, with the KB's Mexico entries stamped as of 2026-08.

**What this KB does NOT tell you, and you must resolve elsewhere before you go:**

- Anything **boat-specific**: vessel/temporary import permit, crew list, port clearance, Mexican boat liability insurance, whether you check in or out with a port captain, or how to handle a Mexican Navy boarding.
- Whether the **CONAPESCA licence is per-angler or per-vessel**, its cost, its duration, or whether every person aboard needs one.
- Whether an **FMM is required for a same-day boat trip that never lands ashore** — the FMM guidance in the KB is written for a land crossing with a point of entry and a length of stay.
- Anything about **going ashore on the islands** (they're a Mexican reserve in reality; the KB is silent, so I'm not asserting it).
- **US re-entry**: no CBP reporting/small-vessel requirement is recorded anywhere in this KB.
- **Mexican bag and size limits** for yellowtail, rockfish or anything else at the Coronados. The KB's *only* Mexico regulatory row is a **circle-hook requirement for Baja California Sur sportfishing, as of 2019-02-13** (`GptrotE0x5M`) — a different state, roughly 700 miles away, **not applicable at the Coronados**. `species/rockfish-lingcod.md` states plainly that California rockfish regs do not apply in Mexican waters and that you must verify Mexican/Baja regs separately.

The KB's own framing, from `locations/regions.md`: a Baja limit differing from a CDFW limit is **two jurisdictions, not a conflict** — don't try to reason from California rules to Mexican ones. **Verify the full private-boat set with CONAPESCA and INM (and the relevant port captain) before you leave the dock.**

---

## 10. Summary — how I'd run it

| | Day 1 | Day 2 |
| --- | --- | --- |
| **Depart** | Early enough to make bait and be on your first spot **an hour before the tide change**, not at it | Same, earlier if day 1 showed a specific window |
| **Bait** | Barge sardine before 5 a.m. if available; sabiki mackerel at the islands, 100 ft / 8 oz | Top up; the NOCO holds bait overnight |
| **First move** | Read current off the kelp lean and the chum-drift angle **before** picking which of the seven spots is even live today | Return to **your own** day-1 marks at tide time |
| **Primary** | Yellowtail; the meter picks iron vs. yo-yo (40–60 ft = iron/light bait; balls on structure at 5–10 fm = yo-yo) | Same, refined |
| **When wind builds (12 kt, afternoon)** | Re-rank toward yo-yo, keep the iron as a picker; watch the kelp for the flat/resurfacing switch | Plan the run home **against** the NW build |
| **Fill** | Calico on the kelp edges — 10–25 casts, then move; watch for a mixed bird pile **on** the kelp (grunion) | Bottom program at Coronado Canyon / Lower 9 Mile if the islands are flat |
| **Discipline** | Neap tide + off-peak = the bite compresses into the tide windows. Be early to each | Don't sprint to the fleet; structure-related sign beats no-man's-land sign |

**Biggest risks, in order:** (1) the paperwork, which this KB genuinely cannot answer for a private boat; (2) the neap tide killing the current the whole program runs on; (3) the afternoon NW sitting right on the 12 kt whitecap line with a 10-second interval, and the fact that the KB says to assume the forecast errs worse and that afternoon wind at the islands strengthens rather than eases.

Tell me the boat's range and sea-state ceiling and whether you're overnighting, and I'll tighten the transit and the fallback ladder.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `planning/search-and-glassing.md`, `planning/report-reading-and-forecasting.md`, `planning/fleet-intelligence.md`, `planning/electronics-and-sounder.md`, `config/endpoints.md`, `locations/regions.md`, `locations/island-structure.md`, `locations/bight-geography.md`, `locations/bahia-de-los-angeles.md`, `locations/cedros-island.md`, `locations/bightsst-eval-targets.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/water-regimes.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `conditions/bird-reading.md`, `conditions/upwelling-and-turnover.md`, `seasonal/october.md`, `seasonal/september.md`, `seasonal/november-december.md`, `species/README.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/rockfish-lingcod.md`, `species/yellowfin-tuna.md`, `species/bluefin-tuna.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `bait/making-bait.md`, `bait/bait-tanks.md`, `fish-care/dorado-and-general.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`, `sources/regulatory-claims.md`  
*videos:* `XLVUhV8DW64`, `OYOda6T3f-8`, `5to3Q5P7w90`, `D5DR7Kx42_A`, `YZtX1MiT0y8`, `ejUTAnONf7o`, `F9XjGMEvvag`, `HzE4FHHcvTk`, `NC3-3pJDEgo`, `0DKmYId1NN4`, `HTowqnwAMeA`, `tpmOYXYQwhU`, `6DzbsElGE7E`, `ZFqe49jRgA0`, `RNRFrfepiW0`, `5pbA-wXoric`, `UP_3fBu7VPA`, `VpW91AKOFVQ`, `pcwcRdmWmLc`, `yn1suHH6b1Y`, `Ec2GaNpiOHI`, `kzD0kSnnVPw`, `sIoNELGlxmk`, `JiJYamo0QHk`, `aFb221LUoD0`, `yGXSrUauo2w`, `8TO-tuYjwWk`, `vqsD0qpwcJA`, `0dIwWiOc1NY`, `NN5MWeRA28o`, `SczdZIq3UmE`, `GptrotE0x5M`, `P36VGPPf120`, `7WapaxdtjQg`, `bM2vUS1B-yQ`, `9tTM99InluM`, `XyKF34C5iB4`, `fri_BWI-VA0`, `cameron`  
*gaps admitted:* Private-boat entry paperwork for Mexico is entirely absent: no vessel/temporary import permit, no crew list, no port clearance or port-captain check-in, no Mexican boat liability insurance, no Navy-boarding procedure. sources/regulatory-claims.md names this as a Known gap in so many words. | No US re-entry requirement (CBP small-vessel reporting) is recorded anywhere in the KB. | The KB does not say whether the CONAPESCA fishing licence is per-angler or per-vessel, what it costs, how long it lasts, or whether every person aboard needs one. | The KB does not say whether an FMM is required for a same-day boat trip that never lands ashore — its FMM guidance is written for a land border crossing with a point of entry and a length of stay. | No Mexican bag limits, size limits, or seasons for yellowtail, rockfish, calico or anything else at the Coronado Islands. The only Mexico regulatory row in the KB is a Baja California Sur circle-hook requirement (2019-02-13), a different state and not applicable here. | Nothing on landing or going ashore at the Coronado Islands, or on any reserve/closure status there. | The KB provides no numeric chlorophyll scale, so the given value of 0.9 cannot be interpreted against it — chlorophyll is treated only as an edge-and-age read, not a threshold. | No October-specific Coronado Islands doctrine exists in the KB. The islands are documented as the spring warming-transition classic; the dated Coronados entries are April and November. | No Coronado Islands location note exists at all — the islands appear only as mentions inside species, conditions, bait and profile notes, plus coordinates in Cameron's spot library. | locations/island-structure.md is region-gated socal-bight only, so applying its structure typology at the Coronados (baja-pacific-north) is an extrapolation the KB does not formally authorize. | The boat profile leaves range_nm and sea_state_max_ft null, and the protocol explicitly requires asking rather than assuming — so the 9 Mile Bank / Coronado Canyon detour and the sea-state go/no-go cannot be resolved from the KB. | Nothing on overnighting a private boat in Mexican waters — no anchorage guidance, no legal or procedural coverage. | The KB gives a swell-exposure window (160-186 degrees) for the San Diego Bay entrance only; there is no equivalent figure for the Mission Bay / Dana Landing entrance. | profiles/cameron/rods.md records no gear ratio for the Trinidad 40, so the yo-yo doctrine's high-speed-reel requirement cannot be verified against the owned inventory. | No slow-pitch / knife-jig outfit (130-250 g class) exists in the owned inventory; the profile lists one as still being shopped.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Two days at the Coronado Islands — mid-October

Worked through [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md). I used the conditions you gave exactly and pulled nothing live.

**Before the fishing, the honest headline twice over:**

1. **The KB cannot tell you what a private boat needs to cross into Mexican water.** It says so itself, in three separate places. Everything below under "Papers" is what the KB *does* hold plus the exact shape of the hole.
2. **The KB has no October at the Coronados.** Its Coronados material is a spring fishery (Apr–Jun), and `locations/baja-pacific-north.md` carries an explicit flagged gap: *no corpus source for a month-by-month prior for the Baja Pacific north.* So this plan is built the way October says to build one — conditions-first, off the chart, not off a calendar prior for that chain.

---

## 1. The day's envelope (protocol step 1b)

- **`regions: baja-pacific-north`** — the whole chain is Mexican water ([`locations/coronado-islands.md`](locations/coronado-islands.md)).
- **`waters: island`**, plus **`bank`** if you work the Middle Grounds or the ground north of the chain.

That filter is binding. It rules out, by gate rather than by opinion: swordfish and opah (socal-bight only), cabrilla (Cortez only), and dorado (`waters: open-ocean` only — and at 66.8 °F you are ~5 °F below the ~71–72 °F green-cold/blue-warm boundary dorado concentrate on, with 71.6 °F measured on a productive paddy, `E4vKwRaRueA`). White seabass does gate into this region, but `locations/baja-pacific-north.md` flags that no corpus source says where or when they are taken on this coast — so I'm not offering it.

**The border runs through your fishing grounds.** [`locations/south-9-mile-bank-439.md`](locations/south-9-mile-bank-439.md) puts South 9 Mile Bank (US waters) **0.65 nm** from Lower 9 Mile Bank (Mexico), and 5.7 nm from Pukey Point, then states flatly: *"Which papers a day here needs is therefore a positional question, and the KB cannot answer it."* Treat your position, not your intention, as what decides which jurisdiction you're in — and know where the line is on your plotter before you start drifting.

**I need two numbers from you the protocol says not to guess.** If this is the profile boat ([`profiles/cameron/boat.md`](profiles/cameron/boat.md), Panga Marine Marquesas 22, 115 hp, 30-gal tank, 100–125 lb ice, Dana Landing), its `range_nm` and `sea_state_max_ft` are both **null** in the profile with a comment saying the protocol must *ask* rather than assume. So: what's your range, and what sea state do you actually run in? Also note that profile launches from **Mission Bay**, which is a materially longer run to the Coronados than a San Diego Bay start.

---

## 2. Papers and permits

**Regulatory — Mexico. INM for entry, CONAPESCA for fishing. Checked as of 2026-08. Verify current requirements before you travel; this is a foreign jurisdiction and these change.** ([`locations/mexican-waters.md`](locations/mexican-waters.md))

### What the KB holds (all of it sourced to a Baja *road* trip, `P36VGPPf120`)

| Paper | What the KB says |
| --- | --- |
| **FMM (tourist permit)** | Filled out online in advance; needs passport details, point of entry, length of stay. Produces a printout — **print it**. The KB records someone being checked three times (the note frames it as one angler on one trip; the flag on it says the transcript actually says "someone got checked three times last year"). |
| **Mexican fishing licence (CONAPESCA)** | Bought online. Have your passport on you when you buy it. The note adds that the licence moved to a new website "as of 2026" and to search fresh rather than trust an old bookmark — flagged, because the transcript states only "there's this new website for the licenses… purchase it there. Have your passport on you," with no year. |
| **Passport** | Yes. |
| **Vehicle insurance** | Baja Bound named; ~**$90** for a 2021 car and ~**$130** for a newer Tacoma over **4 days**. This is *vehicle* insurance — it bears on towing or driving in, not on the boat. |

### What the KB does not have — say it plainly

- **Whether a boat run from San Diego into Mexican water for the day needs an FMM at all, and what a private boat as opposed to a vehicle must carry.** Flagged as a gap in [`locations/mexican-waters.md`](locations/mexican-waters.md), [`locations/coronado-islands.md`](locations/coronado-islands.md) *and* [`species/yellowtail-coronado-islands.md`](species/yellowtail-coronado-islands.md), where it is called "the single most common Mexican-water trip in the KB" and the corpus does not answer it.
- **Boarding and inspection practice** — what the Mexican Navy asks for and how paperwork should be presented. No corpus source.
- **US declaration for bringing fish home** — customs, transport and limits at the border. No corpus source.
- **Mexican bag limits / size gauges for yellowtail, rockfish and lingcod, whitefish and sheephead** — all recorded in [`sources/regulatory-claims.md`](sources/regulatory-claims.md) as *unknown, absent from the corpus.* The register is explicit that **California rockfish regs do not apply in Mexican waters** — do not carry your CDFW season, depth lines or bag limits across the border in your head.

The only boat-specific permit datapoint in the whole KB: running a San Diego boat to **Guadalupe Island** in 2009 was done only after obtaining Mexican federal fishing permits (`Sx40JvCXFuA`; the issuing agency is garbled in the caption). That's a 2009 datapoint about a different destination — treat it as evidence that boat-level permits exist, not as your checklist.

**So: call CONAPESCA and a San Diego Mexican-permit broker before this trip. Do not treat the table above as sufficient for a vessel.**

### The US side

If any part of either day is fished on the US side of the line — Point Loma on the way out, the 9 Mile complex, anything north of the border — that's CDFW water and a **California fishing licence** applies, carried on your person and checked before you reach the water (`LsFMBCa9DOQ`). Your **GO ID** is the 10-digit number on it. Boundary compliance is **positional, not depth-based**: load the line into a chart app and check position in real time rather than trusting the sounder (`iAr6sbRC384`). ([`locations/us-waters.md`](locations/us-waters.md))

---

## 3. Reading your conditions

### Temperature — there is no break here to fish

66.8 at the islands, 66.2 at the 9 Mile, 65.9 at Point Loma: **0.9 °F across the whole inshore-to-island span.** [`conditions/water-temperature.md`](conditions/water-temperature.md) says the planning move is to find **breaks** — sharp gradients, where offshore edges can jump multiple degrees in ~1 mi — not the warmest cell. Your three points don't resolve a break at all; they show a gentle warm-toward-the-islands gradient. The islands are the warm end of what you've given me, which is consistent with going there, but **do not plan on a temperature edge you can't see in this data.** If a real edge shows up inside the chain on the day, that's your structure.

At 66.8 °F: **calico bass sit right in their stated 65–68 °F preference band** (past ~70 °F they get lethargic and drop, `LqW32NSkObY`). Yellowtail have **no numeric SST band in the corpus** — [`species/yellowtail.md`](species/yellowtail.md) flags that gap explicitly and gives directional water-state reads only.

### Chlorophyll 0.9 — the KB gives you no threshold

I searched: **the KB carries no numeric chlorophyll bands anywhere.** [`conditions/water-color.md`](conditions/water-color.md) works entirely on two ideas, neither of which a single number can serve:

- **Age.** A new cold bloom (post-NW-wind, overnight ~5 °F drop, cold and green) is *bad now, productive later*; a mature bloom edge is what fishes. You have no way to age 0.9 from one reading.
- **Edges.** The fishable water is the edge, not the middle of a mass — and you cannot see an edge with one value at one point.

October doctrine says to run "100% at your temp chart and chlorophyll" (`OYOda6T3f-8`, quoted in [`seasonal/october.md`](seasonal/october.md) with a flag that the quote splices two non-adjacent passages). That's exactly the layer your data is thinnest in. **If you can get a chlorophyll image rather than a point value before you go, that's the highest-value thing you can add to this plan.**

### Wind and swell — the day is a morning day

- **NW 3 ft @ 10 s** is not steep by the KB's steepness rule (flag a zone when the period in seconds approaches the height in feet — 10 vs 3 is fine, `zKmZ4zql2ws`). But a working-captain threshold in [`conditions/sea-state.md`](conditions/sea-state.md) calls **sub-10-second intervals "absolutely horrible"** (`NC3-3pJDEgo`) — you are sitting exactly on that line, so if the period drops at all, the sea gets worse faster than the height suggests.
- **12 kt is the same captain's personal no-run cutoff, and above ~12 kt is what raises whitecaps** (`NC3-3pJDEgo`, flagged single-source and framed as personal). Your afternoon forecast *is* 12 kt.
- **Forecast error is asymmetric** — assume it errs worse, and that afternoon wind at the islands strengthens rather than eases (`zKmZ4zql2ws`). **If it's windier than forecast in the morning, assume it builds all day and a small boat bails early** (`DnSqw4r7A1s`).
- Also unmodelled in a point forecast: **current running against the NW swell compresses the interval and stands it up** — 4 ft @ 10 s can fish like 6 ft @ 7–8 s (`zKmZ4zql2ws`).

**Consequence: both days are front-loaded.** Be on fish at first light, plan to be done or inside by early afternoon, and don't let a 12 kt afternoon become a "we'll see."

On the bright side for presentation: the Coronados wind read is that **gusts to 25 kt push fish off the top and the fleet bite goes mostly yo-yo while the surface iron still picks a fish** (`ejUTAnONf7o`). At 8–12 kt you are well under that — **the surface iron should stay live both days.**

### Moon — last quarter is the awkward one

- **Quarter moons are neap tides — the smallest tidal range**, because sun and moon sit ~90° apart and the bulges partially cancel (`9tTM99InluM`, [`conditions/tide-and-slack.md`](conditions/tide-and-slack.md)).
- The KB's elevated windows are **full/new ±1 week, with the days leading into the peak strongest** ([`conditions/moon.md`](conditions/moon.md)). Last quarter sits roughly 7 days off both peaks — the outer edge of both windows, not the middle of either.
- **This matters because yellowtail run on current, not the clock.** "Current on = bite on"; slack current keeps the bite off and the current *starting* is what starts it (`fDSd9kqwYW0`); even a puff of current can fire a lee-side bite (`_r_qKX_7080`). A neap range means **current is your scarce ingredient**, so you cannot afford to be off-station when it runs.
- The Coronados-specific version: the zone runs **seeing-not-biting cycles with one short bite window a day**, and the day is planned around tide and current rather than the clock (`YZtX1MiT0y8`). Inside a cycle there is "no shortage of fish" — presence stays high while catchability compresses.
- **Arrival discipline: be at your highest-percentage spot an hour BEFORE the tide change, not at it** (`6TBxHnkYXI0`).

I have no tide table — the KB doesn't hold one and I'm not fetching. **Pull the tide and current times for both days and hang the whole plan on them.** The KB also flags that no corpus source covers the moon-phase effect on yellowtail at all, so I'm not going to tell you last quarter is good or bad; I'm telling you it's a small tidal range and that the current windows are therefore worth more.

---

## 4. The program

### The zone circuit (from [`species/yellowtail-coronado-islands.md`](species/yellowtail-coronado-islands.md))

1. **Set the troll before you reach the islands.** Pink and purple **190-class deep divers** are the zone's fish-finder — troll while you search for working birds, boils, breezing fish and bait on top. Trolling here is prospecting that happens to hook fish, not the presentation (`HTowqnwAMeA`).
2. **Figure-8 patterns around the islands, plus a pass across the Middle Grounds** — the circuit covers island edges and mid-chain structure in one sweep.
3. **Convert on sign or a troll strike.** Cast a surface iron at any surface activity (`D5DR7Kx42_A`). Fish metered but not showing get **chum-then-cast**: meter the school, throw live chum, let them boil, cast into the boil (`4pT0efBD1j0`, `dS9gd9k7A7Q`). The long cast is load-bearing — they won't let the boat drive over the top of them (`dS9gd9k7A7Q`).
4. **Hold the stop while anyone is bent** — a hooked fish keeps the school near the boat; get a jig back in the water while someone is still hooked (`gdqI2dNd5_U`).
5. **Tight balls hugging structure → yo-yo iron:** hit bottom and the bite comes a couple of cranks off it — a reaction bite, so burn it (`D5DR7Kx42_A`).
6. **With bait aboard → slow-trolled bait** over the same zones; **flyline** when current and tide turn them onto bait; **dropper loop** to bottom marks (`D5DR7Kx42_A`).

**A caveat you should have.** The KB's own evidence file flags that the "figure-8s + Middle Grounds circuit" wording rests on `HTowqnwAMeA`, which is a mid-August day on a small rock *above the border* and never mentions the Coronados ([`locations/evidence/coronado-islands.md`](locations/evidence/coronado-islands.md)). The circuit is the KB's stated doctrine; the corpus support under it is thinner than it reads. Fish it, but don't treat it as heavily corroborated.

Two more zone reads worth having:
- **Good water here is bait volume.** The west side's exposure to colder Pacific currents and tidal swings keeps it filled with bait (`D5DR7Kx42_A`).
- **Big Coronado schools forgive the retrieve** — they eat a faster, less exacting retrieve than the finicky smaller schools on the Del Mar–Imperial Beach coast (`VpW91AKOFVQ`). Get the jig swimming and keep it moving before micro-tuning cadence.
- **Water flips fast** — Coronado droughts run in hours, not months, so re-run the circuit rather than abandoning it.

### Spots and coordinates (all `cameron`, charted; feed these to your plotter and to per-spot conditions)

| Spot | Position | Role |
| --- | --- | --- |
| [Pukey Point](locations/pukey-point.md) | 32°26.850'N 117°18.000'W | North end of chain; ~14 nm from the bay entrance |
| [East of Pukey Point](locations/east-of-pukey-point.md) | 32°27.000'N 117°14.100'W | Library names it "yellowtail & rockfish" |
| [North of North Island](locations/north-of-north-island-rockfish-area.md) | 32°27.380'N 117°18.000'W | Rockfish ground |
| [Middle Grounds](locations/middle-grounds.md) | 32°25.810'N 117°15.950'W | Mid-chain bank — the trolled leg |
| [Ribbon Kelp](locations/ribbon-kelp.md) | 32°24.800'N 117°13.880'W | Kelp edge |
| [Lighthouse](locations/lighthouse.md) | 32°23.290'N 117°14.570'W | South island landmark |
| [5-Minute Kelp](locations/5-minute-kelp.md) | 32°22.940'N 117°13.515'W | Kelp edge |
| [South Kelp Ridge](locations/south-kelp-ridge.md) | 32°22.000'N 117°13.260'W | Kelp edge |
| [Rockpile](locations/rockpile.md) | 32°17.620'N 117°10.030'W | Outlying high spot, 9.6 nm SSE of Middle Grounds |
| [Coronado Canyon](locations/coronado-canyon.md) | 32°30.300'N 117°17.500'W | Rockfish ground N of chain |
| [Lower 9 Mile Bank](locations/lower-9-mile-bank.md) | 32°32.500'N 117°20.500'W | Rockfish ground; 0.65 nm from US South 9 Mile Bank |

Useful geometry from [`locations/middle-grounds.md`](locations/middle-grounds.md): from the Middle Grounds, East of Pukey Point 2.0 nm NE, Ribbon Kelp 2.0 nm ESE, Pukey Point 2.0 nm WNW, North of North Island 2.3 nm NW, Lighthouse 2.8 nm SSE, 5-Minute Kelp 3.5 nm SE, South Kelp Ridge 4.4 nm SSE, Coronado Canyon 4.7 nm NNW, Lower 9 Mile 7.7 nm NNW, Rockpile 9.6 nm SSE. **Nine of the eleven spot pages are minimum pages** — position and parent zone only, with depth, bottom composition and approach all flagged as no-corpus-source. There is no per-spot depth data in this KB.

**Distance caveat:** the KB carries an unresolved unit conflict on the run — the zone page says ~13 **nm** from the San Diego bay entrance (cameron), the yellowtail guide says ~13 statute **mi** (`D5DR7Kx42_A`), and the charted math gives 13.3 nm to the nearest waypoint and 14.0 nm to Pukey Point. Plan fuel on ~14 nm from the bay entrance, more from Mission Bay.

### Two days — my structuring, not KB doctrine

**The KB has nothing on a two-day private-boat trip here.** [`planning/trip-length-selection.md`](planning/trip-length-selection.md) is about booking a sportboat (one-day vs 3-day vs 5-day) and doesn't apply. The anchor-vs-drift commit call at the Coronados is a flagged gap, and there is no corpus material on overnighting in Mexican water. So this schedule is me sequencing KB-sourced pieces, and I'm labelling it as such:

**Day 1 — learn the water.** Leave early enough to make bait and be trolling into the chain at gray light (yellowtail feed hardest in the gray light early, `0dIwWiOc1NY`). Run the full circuit north-to-south with divers down: Pukey Point → Middle Grounds → Ribbon Kelp → Lighthouse → 5-Minute Kelp → South Kelp Ridge. Glass hard between passes. Time your commitment so you are parked on whatever produced **an hour before the tide change**. Be honest about the afternoon wind.

**Day 2 — re-run what worked, plus the tide.** Coronado droughts run in hours, so a dead Day-1 spot is not disqualified. Repeat the productive legs and, if Day 1 was flat everywhere, extend to the Rockpile (9.6 nm SSE) or work the rockfish ground north of the chain — **subject to the Mexican limits you'll have to verify yourself.** Calibrate expectations: the corpus's local-coast yellowtail benchmark is **three or four bites for a good day**, 12–15 bites an anomaly (`HTowqnwAMeA`) — two fishless hours is not evidence the technique is wrong. That figure is scoped to the local coast, not stated for the islands.

### Search discipline ([`planning/search-and-glassing.md`](planning/search-and-glassing.md))

- Glass from a **full stop, or bow into the swell at ~1 kt** — a rolling boat makes glassing useless. Image-stabilized binoculars.
- **360° in small increments, 3–4 minutes per scan.** When a bird catches your eye, **watch it 30–40 seconds** before judging it.
- **Ranges from deck level:** a few terns at ~0.5–1 mi, a big bird spot at ~2 mi. From a hardtop: birds ~2 mi, dolphin ~4 mi. **Space glass stations 3–4 mi apart.**
- **Along a bank, run the contour at 16–18 mph** with a lookout ~30° off each bow.
- **Terns are the run-to bird** — run to working terns even when nothing else is working, and cast under the bird the moment it dives, not at its general position (`JiJYamo0QHk`). A **moving dive-line** = bait being pushed from below; a **locked-in, stationary** bird = bait only (`Blh2BA-7Ono`).
- **Boobies are mostly seen at the Coronados and are worth paying attention to (cameron)** — but [`conditions/bird-reading.md`](conditions/bird-reading.md) flags that there is **no corpus doctrine on booby behavior at all**, so you get "look at them," not "here's what they mean."
- **Mixed piles at open-water current breaks = bait only, skip.** Exception: a mixed pile *on kelp or structure* can be a real bait event (`Blh2BA-7Ono`, `OYOda6T3f-8`).

### On the meter ([`species/yellowtail.md`](species/yellowtail.md))

- **Grade the bottom before hunting fish sign:** thin return = sand/mud, thick return = rock, and the fish hold on rock (`6DzbsElGE7E`).
- **Tight balls hugging hard bottom, arcs at ~5–10 fathoms near structure** → yo-yo / dropper loop. (Flagged: `D5DR7Kx42_A` carries no depth figure; the 5–10 fathom band is note-side.)
- **Metered at 40–60 ft and not showing** = staging up — surface-iron and light-bait fish, not yo-yo fish; when they boil, go all-in on the iron (`0DKmYId1NN4`).
- **Stratified column, bottom through mid-water** = hunting → slow-trolled and flylined bait (`HTowqnwAMeA`).
- **Balled tight to the bottom** = present but not feeding → dropper loop, plus a yo-yo burned past them for the reaction strike.
- **Don't marry the technique.** Pulling the anchor and slow-trolling the same zone roughly quadrupled a bite rate over anchoring (`HTowqnwAMeA`).

---

## 5. Gear — class terms, with the zone's numbers

Rig all three faces before you leave the dock; the face can flip by the hour.

| Job | Class | Coronados numbers |
| --- | --- | --- |
| **Troll / search** | The flyline outfit tows a 20–30 ft diver — no second setup needed. For a **40 ft** diver, switch to a **6–7 ft rod, 40-class reel, 80 lb braid**, top shot short: **15–20 ft of 50–60 lb** (`HTowqnwAMeA`) | Pink and purple **190-class deep divers**. Carry variety on three axes — colour, profile, dive depth. **Colour by light, and it inverts intuition:** overcast/low light → high-vis; bright clear blue → darker, blues/purples/reds |
| **Surface iron** | **Jig-stick class** — 8–10 ft, casts 2–4 oz irons, ~25–60 lb ([`tackle/gear-classes.md`](tackle/gear-classes.md)) | ~**65 lb braid** backing to **fresh 40–50 lb mono top shot** (`D5DR7Kx42_A`); **40 lb** is the local full-day-island top-shot bracket (`LTCFjqtSI8g`). **Tady 45 / JRI Stinger class**; step up to a **Salas 7X-class** heavy iron in wind to punch the cast |
| **Yo-yo iron** | **40–60 lb stout rod + high-speed reel** | Depth ladder: **60/80/100 ft → 6X Jr class; 120–150 ft → Salas 6X, roughly 5–6 oz** ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)). Flat-fall / vertical change-up **100–180 g depending on current** (`D5DR7Kx42_A`) |
| **Dropper loop** | Same 40–60 lb outfit | Sinker **6–10 oz** at the very bottom, hooks on the loops above; **err long on the loop** for bait action |
| **Flyline** | **20–40 or 20–50 lb rated rod, 8–9 ft** — backbone to turn a fish off the rocks (`D5DR7Kx42_A`) | Hook follows bait size: **1/0–2/0 baseline**; downsize to **J hooks 1, 2, 4** when they're picky on fluorocarbon (`F9XjGMEvvag`); **2/0–4/0** on bigger baits |
| **Sliding sinker** (if bonito intercept your flylined baits before the yellowtail get them) | 30 lb live-bait class | **1–4 oz egg sinker** straight to a **J hook 2/0–4/0**, scaled to wind and depth (`yGXSrUauo2w`) |
| **Slow-trolled bait** | Same outfit as flyline — it's a change of boat behaviour, not tackle | **1.5–3 mph, chosen by the bait:** small sardine (size 1–2 hook) → as slow as you possibly can; mackerel or anything taking a 3/0–5/0 → pull it faster |

**Yo-yo execution:** position **up-current of the mark** so the drop sweeps onto the structure; free-spool the iron to the mark thumbing the spool so it tracks straight down instead of scoping away; **start winding the instant it touches** — the most common error is letting it settle; then **wind as fast as you can, all the way up**, and keep cranking on the bite rather than swinging (`5pbA-wXoric`, `hteLeDIy9Qs`, `RNRFrfepiW0`). Line: 40 lb works, 50 better, 60 better still.

**Surface iron execution for yellowtail:** **let it sink ~30 ft before you start winding** — it covers depth instead of only the top (`ntQXxcH5sjI`) — and **work it all the way to the rail**, because they eat it right at the boat after trailing it in (`VpW91AKOFVQ`).

**Two internal conflicts you should know about rather than trip over:**
- **Iron weight.** [`species/yellowtail.md`](species/yellowtail.md) says full-size 6X = 8 oz in stronger current, 6X Jr = 4 oz when light; [`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md) puts a 6X at 5–6 oz and sizes it by **depth**, not current, and says neither the 8 oz nor 4 oz figure appears in it. I've given you the depth ladder above because the technique note owns execution. Not a ranking — the KB keeps both.
- **Iron colour.** The zone guide and the router both list scrambled egg, bird shit, mint and blue/white as "the yellowtail colours," and [`species/yellowtail.md`](species/yellowtail.md) itself carries the flag that the colour note's actual doctrine is **colour is not the variable** (rank: swim → size/weight → colour, last), and that "colour doesn't matter" is itself a yellowtail saying. Carry the four; don't spend the day changing them.

---

## 6. Bait for two days ([`bait/making-bait.md`](bait/making-bait.md), [`bait/bait-tanks.md`](bait/bait-tanks.md))

- **Making bait at the Coronados is a documented program (cameron):** sabiki dropped to **~100 ft** with an **8 oz** sinker; **five 12-inch mackerel on one drop** at best. Twelve-inch mackerel are big, hearty baits — heartier than sardine.
- **Buying instead:** sardines from the barge. **Avoid the 6:00 a.m. rush** when the sportboat fleet loads — target **5:00 a.m., or 4:30** (`ztpj1Xll0-U`, `bM2vUS1B-yQ`). A 7:00 a.m. arrival avoids the line but "it's all gone." Tell the attendant you want it **loaded light** and you're not in a rush; hail on **VHF 11** if nobody's dockside; never board the barge; tip.
- **Holding bait between days:** the KB's turnover target is **the entire tank volume changing every 8 minutes** (flagged single-source, and the source itself says "why eight minutes I have no clue but that's what works"). West-coast circular flow, side drain, never a centre standpipe. On the profile boat that's a 30-gal tank on a **Rule 401, 500 GPH** pump running off a **single starting battery** with a NOCO GEN5X1 charger added specifically to hold the battery up while the bait pump runs overnight. **The KB has no doctrine on keeping bait alive across an overnight between two fishing days** — plan power and water changes yourself.

---

## 7. Fish care over two days ([`fish-care/dorado-and-general.md`](fish-care/dorado-and-general.md))

- **Salted slurry:** rock salt at roughly **2 cups per 7–10 lb bag of ice**, plus a splash of seawater to wet it — the salt is what drops the mix below freezing.
- **Never fresh-water rinse** anything; salt water for every rinse. Keep fish out of the sun and get them cold fast.
- **A deck hose-down doesn't chill a fish** — that water runs in the high 70s °F.
- **Bring a cooler for the drive home** if it's more than ~10 minutes.
- The profile boat carries **100–125 lb of ice per trip** — that number is stated for a trip, not for a two-day trip, and the KB has no guidance on holding a catch across an overnight. Budget ice accordingly and assume you need more than the single-day figure.

---

## 8. What else is realistically on the table

The Coronados zone page lists yellowtail (spring peak), rockfish & lingcod, and bonito (summer, with a flagged gap for zone-specific behaviour). Beyond that, gating in for `baja-pacific-north` + `island`:

- **Bonito** — the best-documented October fish in the KB, though every dated October record is SoCal-side (Ventura coast and the islands, Cortez Bank, San Clemente late October). The framing that matters: *"presence is not the bite, and late fall inverts the ratio"* — inside Catalina in late October the water still supports yellowtail, but "you're mostly against Bonita, bass and Rockfish this time of year" (`5p6gu14ZC4w`). And **bonito hours and yellowtail hours are not the same hours** (`Blh2BA-7Ono`). Expect bonito to fill the middle of the day.
- **Barracuda** — dated SoCal appearances run late May through October, and off Ensenada barracuda are named with bonito and yellowtail as the standing inshore mix (`0dIwWiOc1NY`).
- **Calico bass** — in their 65–68 °F band at your temperature; fish edges and pinch-points, not the dense middle of kelp. The Coronados page doesn't list them, so this is a gate-level inference from region and water type, not a zone-documented fishery.
- **Rockfish, lingcod, whitefish, sheephead** — the ground north of the chain (Coronado Canyon, Lower 9 Mile, North of North Island, East of Pukey Point). **Mexican limits and seasons for all of them are recorded as unknown in the KB, and California's rules do not apply.** Verify before you keep anything.

---

## 9. Before you go — my short list

1. **Resolve the vessel paperwork with CONAPESCA / a San Diego permit broker.** The KB cannot tell you what a boat needs; treat the FMM + CONAPESCA licence + passport list as necessary, not sufficient.
2. **Get chlorophyll imagery, not a point value**, and pull the tide/current times for both days.
3. **Tell me your range and sea-state limit**, and whether you're launching from Mission Bay or San Diego Bay — the profile leaves both null and the protocol says to ask, not assume.
4. **Load the border onto your plotter.** Lower 9 Mile is 0.65 nm from US water.
5. **Plan both days to be finished, or inside, before the 12 kt NW fills in.**

## Notes for judging this plan

Two things I did *not* do, deliberately: I didn't give you an October Coronados prior (the KB doesn't have one — its Baja Pacific north fall row is a single November 2014 calico record from San Martin Island, 200-odd miles south), and I didn't tell you what 0.9 chlorophyll means (the KB has no numeric bands). Anything you read elsewhere on those two points isn't coming from this knowledgebase.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `planning/search-and-glassing.md`, `locations/coronado-islands.md`, `locations/evidence/coronado-islands.md`, `locations/mexican-waters.md`, `locations/evidence/mexican-waters.md`, `locations/us-waters.md`, `locations/regions.md`, `locations/baja-pacific-north.md`, `locations/middle-grounds.md`, `locations/pukey-point.md`, `locations/ribbon-kelp.md`, `locations/5-minute-kelp.md`, `locations/south-kelp-ridge.md`, `locations/lighthouse.md`, `locations/rockpile.md`, `locations/north-of-north-island-rockfish-area.md`, `locations/east-of-pukey-point.md`, `locations/coronado-canyon.md`, `locations/lower-9-mile-bank.md`, `locations/south-9-mile-bank-439.md`, `locations/north-9-mile-bank-178.md`, `locations/coronados-230-302-226.md`, `species/yellowtail.md`, `species/yellowtail-coronado-islands.md`, `species/yellowtail-surface-iron.md`, `species/yellowtail-dropper-loop.md`, `species/bonito.md`, `species/barracuda.md`, `species/calico-bass.md`, `species/rockfish-lingcod.md`, `species/ocean-whitefish.md`, `species/sheephead.md`, `seasonal/october.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/water-regimes.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/tide-and-slack.md`, `conditions/current-structure.md`, `conditions/bird-reading.md`, `techniques/surface-iron.md`, `techniques/yo-yo-iron.md`, `techniques/dropper-loop.md`, `techniques/flyline.md`, `techniques/trolling.md`, `techniques/slow-trolling-bait.md`, `lures/halco-laser-pro.md`, `tackle/gear-classes.md`, `bait/making-bait.md`, `bait/bait-tanks.md`, `fish-care/dorado-and-general.md`, `sources/regulatory-claims.md`, `sources/gap-report.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`  
*videos:* `D5DR7Kx42_A`, `HTowqnwAMeA`, `YZtX1MiT0y8`, `ejUTAnONf7o`, `VpW91AKOFVQ`, `4pT0efBD1j0`, `dS9gd9k7A7Q`, `gdqI2dNd5_U`, `LTCFjqtSI8g`, `F9XjGMEvvag`, `P36VGPPf120`, `Sx40JvCXFuA`, `OYOda6T3f-8`, `5p6gu14ZC4w`, `E4vKwRaRueA`, `LqW32NSkObY`, `NC3-3pJDEgo`, `zKmZ4zql2ws`, `DnSqw4r7A1s`, `9tTM99InluM`, `6TBxHnkYXI0`, `fDSd9kqwYW0`, `_r_qKX_7080`, `0dIwWiOc1NY`, `ntQXxcH5sjI`, `0DKmYId1NN4`, `yGXSrUauo2w`, `6DzbsElGE7E`, `hteLeDIy9Qs`, `5pbA-wXoric`, `RNRFrfepiW0`, `Blh2BA-7Ono`, `JiJYamo0QHk`, `sIoNELGlxmk`, `ztpj1Xll0-U`, `bM2vUS1B-yQ`, `7WapaxdtjQg`, `iAr6sbRC384`, `LsFMBCa9DOQ`, `L3tkGVu516A`, `5to3Q5P7w90`  
*gaps admitted:* What a private BOAT run into Mexican water actually requires — whether an FMM applies to a day trip that never lands, and what a vessel (as opposed to a vehicle) must carry. The KB flags this identically in locations/mexican-waters.md, locations/coronado-islands.md and species/yellowtail-coronado-islands.md as its single most common Mexican-water trip, unanswered by the corpus. | Mexican Navy boarding and inspection practice — what is asked for and how paperwork should be presented. No corpus source. | US customs declaration for bringing fish home from Mexico, and transport/limits at the border. No corpus source. | Mexican (CONAPESCA) bag limits, size gauges and seasons for yellowtail, the rockfish/lingcod complex, ocean whitefish and sheephead — all recorded as unknown/absent in sources/regulatory-claims.md. | Whether the water at the 9 Mile complex is a US or Mexican paperwork day — locations/south-9-mile-bank-439.md states this is a positional question the KB cannot answer. | Any October or fall prior for the Coronado Islands or the wider baja-pacific-north region. locations/baja-pacific-north.md flags the absence of a month-by-month prior outright; seasonal/october.md is written for socal-bight, and the Coronados material is a spring (Apr–Jun) fishery. | Numeric chlorophyll bands — the KB carries no threshold anywhere that would let me call 0.9 good, bad or indifferent; conditions/water-color.md works only on bloom age and edges, neither derivable from one point value. | Numeric SST bands for yellowtail — species/yellowtail.md explicitly flags the absence and gives directional water-state reads only. | Moon-phase effect on yellowtail — species/yellowtail.md flags that the corpus's moon claims cover bass and offshore tuna only, so last quarter cannot be scored for this species. | Depth bands and bottom composition for every Coronados spot — nine of the eleven spot pages are minimum pages carrying position and parent zone only. | The anchor-versus-drift commit call at the Coronados — when to drop the hook on a mark versus keep working the circuit. Flagged gap in species/yellowtail-coronado-islands.md. | Mechanism for what flips Coronados fish from seeing to eating, and any zone-specific gray-light read. Flagged gap in the zone guide. | Anything on a two-day private-boat trip: overnighting or anchoring in Mexican water, how to structure day 2 against day 1, or holding bait and catch across an overnight. planning/trip-length-selection.md covers sportboat booking only. The two-day schedule I gave is my sequencing of KB pieces, not KB doctrine. | Zone-specific bonito behaviour at the Coronados — flagged in locations/coronado-islands.md; every dated October bonito and barracuda record in the KB is from the SoCal side, not this chain. | Where or when white seabass are taken on the Baja Pacific north coast, despite the species gating into the region — flagged in locations/baja-pacific-north.md, so I did not offer it. | Booby behaviour — what distinguishes bait-only from fish-underneath. conditions/bird-reading.md says there is no corpus doctrine on this bird at all, even though it is the Coronados bird. | Tide and current times for the two days — the KB holds no tide data and I made no live pull, so the timing discipline in this plan has no clock attached to it. | The boat's operating envelope: profiles/cameron/boat.md leaves range_nm and sea_state_max_ft null with an explicit instruction that the protocol must ask rather than assume. | Internal conflicts I passed through rather than resolved: yo-yo iron weight (current-keyed 8 oz/4 oz in the species router vs depth-keyed 5–6 oz in the technique note), yellowtail iron colour (four named colours vs the colour note's 'colour is not the variable' doctrine), and the Coronados run distance (13 nm vs 13 statute mi). | Gating oddities that would silently drop content under a strict protocol read: lures/halco-laser-pro.md is gated socal-bight / open-ocean+bank even though the Coronados zone guide routes to it, and species/yellowtail-dropper-loop.md is gated socal-bight only. I used the class terms rather than the gated-out model pages. | The Coronados circuit doctrine (figure-8s + Middle Grounds pass) rests on HTowqnwAMeA, which the KB's own evidence file flags as a mid-August day above the border that never mentions the Coronados — the doctrine is the KB's, but the corpus support under it is thin.

</details>

### 4. [trip] I am thinking about an overnight run to Tanner Bank / Cortez Bank for bluefin. Go or no-go? Describe the run, …

**Winner:** B2 · mapping {'A': 'B3', 'B': 'NOW', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three reach the same well-supported no-go on the same two gates — the named 12–15 kt / 4–8 ft @ 9 s unfishable combo and an unset boat envelope (range_nm / sea_state_max_ft null) — and all three refuse to invent an eclipse effect or a chlorophyll threshold, so the separation is entirely in the second half of the question: describing the run and what to expect. C delivers the most usable picture, teaching the actual bank programs (night DSL jigging with the ~1 g/ft rule, 300 g floor stepping to 500 g on a hard-drifting night, stay-vertical routes, line marked every 100 ft; daylight flyline at 25–30 lb fluoro on size 2 circles with the hook-wire caution), then converts the weekend into a timed, rigged alternative off Cameron's own rack with fish care and regs — while openly flagging that no Tanner/Cortez location page exists and that its distances are its own arithmetic. B is a close second and has the best structural trip picture (sunup-to-noon yellowtail then deep, two night windows, anchor-and-chum gated by current, fleet slotting) plus the only Cow Cod Conservation Area warning, but it names the night-jig and kite gaps and stops rather than teaching what happens out there, omits fish care, and slips statute miles into nm. A has the strongest situation→technique→owned-gear table and the most detailed alternative-day search and sounder discipline, but its bank coverage is a list of corpus data points rather than a coherent program, and it never surfaces that the fishery out there is an anchor-and-chum, current-gated one.

- *B2 reasons:* found: same correct kill criteria plus the fullest 'what to expect' — up-current face positioning, anchor depths, grade ladder, the night DSL program, daylight flyline program, foamer failure case — and stated plainly that no Tanner/Cortez location page exists (even noting Bishop Rock is never mentioned). specific: distances checked against corpus figures, 198–330 ft night stacks, 50–80 fm bank-specific marks, ~1 g per foot jig rule, 300 g floor / 500 g wind-night, mark line every 100 ft, 16 oz 'Eddie bomb', 25–30 lb fluoro on size 2 circles, 90% of daytime bites on flyline, hook-wire caution on light No. 4s. sourced: note paths plus ids throughout (NC3-3pJDEgo, LsFMBCa9DOQ, UfuiWFVvz2E, 947solNfiPw, Ul5FLB2dFgQ, nRFFM8DT-og, mDmbGdQAy-4). scoped: socal-bight/bank; bluefin limit and rockfish closure both jurisdiction + as-of + verify. honest: flags the threshold set as medium confidence, flags its distances as its own arithmetic, surfaces the counter-doctrine that full moons drive the night bite and states section order is not a ranking, admits eclipse/chlorophyll/tide/anchoring/ice gaps. actionable: the only answer that both teaches the bank programs well enough to fish them and lays out a timed, rigged alternative day off the actual rack with care and regs.
- *B3 reasons:* found: pulled the right layers — sea-state thresholds, moon (Landesfeind vs Hansen), August dispersal, water-temp/color, boat profile — and stated plainly that no small-boat account of the run exists; weaker on the banks' actual fishing program (never names the anchor-and-chum/current-gating structure of the day). specific: distances from KB coordinates (declared as arithmetic, and they check out: ~92/95/35 nm), 60 ft bait marks in 120 ft, 50–80 fm night marks, 25 lb/#2 and 40 lb/#4 circle, 250 g flat-fall floor, 2 cups rock salt per 7–10 lb bag, chill times. sourced: every claim carries a note path plus video id (NC3-3pJDEgo, ntQXxcH5sjI, 947solNfiPw, LsFMBCa9DOQ, UfuiWFVvz2E). scoped: socal-bight/bank+open-ocean set explicitly; bluefin limit and the 43 rockfish closure both carry California/CDFW + as-of + verify-current. honest: long, genuine gap list (eclipse, chlorophyll scale, null range/sea-state, bait-pump power offshore, ice capacity, bank-specific advection) and refuses to invent the envelope. actionable: best situation→technique→owned-gear table of the three, plus a fully runnable 43 alternative with sounder ranges (manual 0–150/0–300 ft), glassing cadence and return timing.
- *NOW reasons:* found: worked from dedicated bank pages and used their own flagged gaps well (no source turns the zone off on wind/swell; no small-boat port run stated) — the best structural picture of the trip day: sunup-to-noon yellowtail then deep, two night windows, anchor-and-chum gated by current, fleet slotting. specific: 15.6 nm bank separation on 179/359, 15–25 fm anchor, 50–60 fm edge, 60–80 ft marks in 120 ft, 25 lb/#2, 40 lb floor droppable to 30, 300 g floor stepping to 500 g, 43 at 34.9/31.2/21.5 nm from three named waypoints. sourced: dense video ids tied to specific notes; conflicts kept side by side with an explicit decision frame ('what they turn on is grade and bite quality — not section order'). scoped: region right; bluefin limit with CDFW + as-of 2026-08/2024-11 + verify, plus the unique Cow Cod Conservation Area flag with the boundary honestly marked unverified. honest: names kite and 300–500 g jig as gaps rather than substituting; flags the KB's lack of chlorophyll scale, eclipse content, tide tables, anchoring gear. actionable: usable flyline/yo-yo/troll numbers and a 43 search plan, but thinner on execution than C — no night-jig technique, no fish care, and the alternative is caveated rather than timed; minor unit slip treating statute-mile corpus figures as nm.

<details><summary>Full prompt</summary>

I am thinking about an overnight run to Tanner Bank / Cortez Bank for bluefin. Go or no-go? Describe the run, and what to expect out there. Assume these conditions and do NOT fetch live data: Friday night into Saturday, 2026-08-28/29. SST: Tanner Bank 69.4 F, Cortez Bank 69.9 F, 43 Fathom Spot 68.2 F. Chlorophyll 0.3 offshore. Wind: NW 15-20 kt Friday, easing to NW 8-12 kt at Saturday dawn, building to 15 kt by noon. Swell: NW 5 ft at 9 s Friday, NW 4 ft at 9 s Saturday. Moon: full on 08-28 with a partial lunar eclipse that night. No Small Craft Advisory for Saturday morning. Use the angler profile in profiles/cameron/ (boat.md, rods.md, tackle.md, trolling-lures.md, spots.md) and respect the boat envelope.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

# Tanner / Cortez overnight, Fri 2026-08-28 → Sat 08-29 — **NO-GO on the panga**

Short version: the KB kills this trip twice over — once on sea state, once on the boat envelope — and the moon timing is the weakest half of the window besides. The banks themselves are a real, well-documented mid-August bluefin fishery, so I've written up what the run and the fishing would look like, then given you the version of this weekend your boat can actually do.

---

## 1. The go/no-go call

### Sea state — this is the KB's *named* unfishable combo

`conditions/sea-state.md` carries Capt. Dave Hansen's go/bail thresholds (`NC3-3pJDEgo`, 2020-11-18). Your forecast matches one of them almost word for word:

- **"12–15 kt wind with 4–8 ft swell at a 9-second interval"** — "you can't go out there… you just cannot be caught out there," called a dire situation **even for bigger boats**; he holds the larger boats he runs at the dock in that combo, not just small ones.
  - Your Saturday: **NW 4 ft @ 9 s**, wind **8–12 kt at dawn building to 15 kt by noon**. That is inside the named combo by mid-morning.
- **Swell interval under 10 seconds is a hard bad-sea flag**, independent of height — "absolutely horrible." Both your days are 9 s.
- **Wind over ~12 kt is what raises whitecaps**; Hansen's personal cutoff is not to run over 12 kt. Your Friday transit leg is **NW 15–20 kt over 5 ft @ 9 s** — worse than the named combo, and that's the leg you'd run in the dark.

Two more layers make the paper forecast optimistic rather than pessimistic:

- **Current-vs-swell opposition** (`conditions/sea-state.md`): summer uphill (counter)current running against NW swell compresses the interval and stands the swell up — a forecast **4 ft @ 10 s fishes like 6 ft @ 7–8 s**, and point forecasts don't show it. Your 4 ft @ **9 s** starts worse than that example.
- **Forecast error is asymmetric** — assume it errs on the worse side, and that afternoon W at the islands strengthens rather than eases. Your forecast is already *building* through Saturday, not easing.

The absence of a Small Craft Advisory isn't the KB's threshold. Hansen's numbers are, and they say no.

*(Honesty flag: `conditions/sea-state.md` labels this specific threshold set **medium confidence** — registered voice, single mention, not yet repeated in the corpus. But it's the only explicit go/bail rule the KB has, and your numbers hit it dead-on rather than marginally.)*

### Boat envelope — `profiles/cameron/boat.md`

The 2004 Panga Marine Marquesas 22, single 115 hp Yamaha:

- **Foam-filled hull with slight flex/"spring" on hard wave impacts**, **very small bilge**, **no trim tabs** (engine trim is the only attitude control).
- The trim routine *requires* **at least one person forward on the bow bean bag underway** — and the note itself says **"rough days forward are brutal — rider catches air then hits the deck."** That's the profile's own description of this run in this sea.
- **No AC/shore-power inlet, no house battery.** The 30-gal tank's Rule 401 (500 GPH, 2.1 A) runs off the **single Group 24 start battery** (550 CCA, 140 min RC). The NOCO GEN5X1 that "holds the battery up while the bait pump runs overnight" is an **AC** charger on a hardwired pigtail — that's a dock solution, not an offshore-overnight one (`bait/bait-tanks.md`).
- **Home waters: Coronado Islands, La Jolla, San Diego offshore banks**; normal departure **~8 am**; launch **Dana Landing, Mission Bay**.

### The distance, from your own waypoints

`sources/spot-lists.md` gives **Tanner Bank 32°42.000′N / 119°08.000′W** and **Cortes Bank 32°26.417′N / 119°07.833′W**. Measured off the **La Jolla NW Corner** anchor in your own eval list (32°50.630′ / 117°18.460′ — the closest thing the KB gives me to Mission Bay's offing):

| Leg | Distance |
|---|---|
| La Jolla NW corner → Tanner Bank | **~93 nm** |
| La Jolla NW corner → Cortes Bank | **~95 nm** |
| Tanner ↔ Cortez (they're one complex) | **~15.6 nm** |
| La Jolla NW corner → the 43 | **~35.5 nm** |

That cross-checks cleanly against the corpus figures: Cortez called **111 mi west of Point Loma / 96 mi SW of San Pedro / 47 mi SW of San Clemente Island** (`QSvzVHW9UMk`), **~110–115 mi from San Diego** (`UfuiWFVvz2E`), Tanner **~90–100 mi west of Long Beach** (`ntQXxcH5sjI`). `species/yellowtail.md` flatly calls Cortez "a full overnight run **for a sportboat**." Every KB trip to these banks is an 80–85 ft boat on a **1.5- to 3-day** charter.

**The KB gives no fuel capacity, cruise burn, or range figure for your panga** — only top speed ~35 kt and idle ~1.5 kt. So I can't tell you it's out of range; I can tell you the KB has nothing that puts it *in* range, and that ~190 nm round trip plus a night of drifting/anchoring on a single start battery is not a call the profile supports.

### The moon is the wrong half of the window

`conditions/moon.md` + `seasonal/june-july.md`:

- **Days *leading into* the full moon are the strongest documented bluefin windows** ("if we've learned anything over the last six, seven years," 10/12/22 report). Full moon is **08-28** — the leading days were **08-21 through 08-27**. You'd be arriving on the peak, one night past the best of it.
- **Hansen's dissent, kept side by side** (`fri_BWI-VA0`, 2022-02-12): the moon peak itself is the **travel period, not a bite period** — "the full moon itself is not good," softened by "I've seen a bite in a full moon also." Best windows are 7 days before **and** 7 days after.
- **Both voices agree on your Saturday morning:** the morning *after* a full-moon night is typically slow ("it hasn't been really located, or it's been feeding all night"), with the bite **picking back up late in the day**. Hansen's explicit advice: if you must fish a full moon, **fish it late rather than push the early-morning window.**
- **Post-moon relocation:** open-water bluefin not holding structure move **10–15 nm overnight** (Landesfeind, 7/21/22); Hansen puts it at **20 miles** — kept side by side, not averaged. Any position you ran out on is stale by that much by Saturday dawn.

**The one thing that cuts the other way:** the corpus also says **"full moons drive the bluefin night bite"** (`seasonal/june-july.md`, 7/14 + 8/11/22 reports). So the internally consistent read of your window is: **the Friday/Saturday *night* jig session is the good half; the Saturday *morning* is the weak half** — exactly inverted from how you'd normally plan a run-out-Friday, fish-Saturday-dawn trip. Section order isn't a ranking here: what it turns on is whether you're a night-jig boat or a daylight boat.

**The partial lunar eclipse: the KB has nothing on eclipses.** No note in `conditions/` mentions one. I have no basis to adjust for it either direction and I'm not going to invent one.

---

## 2. The run, and what to expect out there

If a boat that belongs out there is going — this is what the KB says the trip is.

### Geography

Tanner and Cortez are **15.6 nm apart** and read as one bank complex; crews use the names loosely enough that the KB flags one annual charter series described as "Cortez" in one video and calling a fish a "Tanner Bank yellow" in another, unresolved (`c3NFkQbdDy0` vs `nQvJnfb5jQ4`). Bank naming convention: a bank is named for the fathom depth of its **shallowest** point (`locations/zone-lexicon.md`, `Rf1HKJG-SDg`) — so the **43** is a 43-fathom high spot, not a distance.

**Where on the bank:** with the **summer uphill (counter)current**, upwelling forms on the **lower / south face** — bias to the **up-current face** (`conditions/current-structure.md`, Academy Ep. 1). The corpus positioning that produced: working the **50–60 fathom edge** of the drop-off off the high spot, which put fish on the boat "right out the gate" (`nQvJnfb5jQ4`).

### Water depths and where boats sit

- **Tanner:** anchored in **~120 ft**, bluefin taken on bait marks at **~60 ft** while chumming sardines (`ntQXxcH5sjI`, mid-August 2024). Another day-one anchored on the **eastern side of the high spot** (`947solNfiPw`).
- **Cortez:** anchor in **15–25 fathoms**; high spot marks **60–80 ft in 120 ft of water**; drifting and anchoring both produced in water around **50 fathoms** (`UfuiWFVvz2E`, `zBd1mayUt_I`).

### Grade — plan for the whole ladder, not an average

Mid-August at these banks, from the corpus:

- **~30 lb opening grade, fish to 41 lb** the previous day; one fought "on 50 [lb]" (`947solNfiPw`, Tanner).
- **20–30 lb, about 25 lb average**, day's grade at Cortez on **20 lb fluorocarbon** to **No. 4 and No. 2** hooks (`QSvzVHW9UMk`).
- A landed **40 lb** fish (`c3NFkQbdDy0`); a **20–30 lb** call on a fly-line day (`eL1Qm33-Mj0`).
- But the crew's own framing of the core tackle problem: **10 lb schoolies up to 80, "maybe even 100" lb** moving through together on **one size line** — "a total game" (`947solNfiPw`).
- And **bluefin gear does not get scaled down** on a mixed trip the way skipjack/schoolie yellowfin gear does — grade is unpredictable trip to trip, so tackle stays sized for the biggest fish that could show (`PrdPJy26H8c`).

**Hook caution:** some **No. 4s run light wire** — a **stouter No. 4** was preferred, because even at 25–30 lb line test there's enough pressure on the hook to matter (`QSvzVHW9UMk`).

### The night program — this is the fishery out there

`species/bluefin-tuna.md` + `techniques/knife-jigging.md` + `conditions/deep-scattering-layer.md`:

- Fish rise with the **deep scattering layer** after dark; the read is depth-called marks — **"fish at 180, fish at 230 ft"** (`nRFFM8DT-og`). A June 2023 night school read **stacked from ~198 ft down to 330 ft** (`r4J5nP5Bkl4`). The flat-fall bite specifically comes **at night or 250–350 ft down** (`scmPq63lLWM`).
- **Bank-specific and deeper:** an overnight jig session at Tanner/Cortez read marks **360° around the boat, from 50 fathoms down to 80 fathoms, even below** (`LsFMBCa9DOQ`) — kept side by side with the 30–50 fathom sounded-school range, not replacing it.
- **Jig weight:** general range **150–400 g** by depth and current; **~1 g per foot of depth** for a speed jig. At Cortez one captain set a **hard 300 g floor** for night jigs, with **250 g** allowed only for anglers savvy enough to fish it (`UfuiWFVvz2E`). On a **windy, hard-drifting night at Tanner/Cortez, 250–350 g wouldn't hold the zone and the boat stepped up to 500 g** (`LsFMBCa9DOQ`) — that's your Friday night, with 15–20 kt on it.
- **Stay vertical.** Two attributed routes, not reconciled: throw **up-current off the bow and walk back toward the stern**; or from the stern, **cast down-swell** so the jig sits at ~200–250 ft straight under the boat by the time you drift to it (`UfuiWFVvz2E`) — that captain called keeping the jig vertical *the* key to night jigging.
- **Work it slower at night** — a slow, worked drop ("blinking") out-produces speed after dark, and pair the slow pace with a **center-weighted flip-slider** rather than a tail-weighted speed jig. **Slack the line on the drop**, don't tightline it (`Ul5FLB2dFgQ`).
- **Mark your line every 100 ft** (Ray marks every 50; pre-marked braid can be every 25) — the captain calls depths and they change fast (`Ul5FLB2dFgQ`).
- Blunt-instrument option: the **"Eddie bomb"** — a wire-through **16 oz sinker with a treble on the bottom** and a bite leader. Multiple **200 lb night bluefin** have come on it (`nRFFM8DT-og`).
- Night results at these banks: an overnight session starting **~1:00 am** put roughly **a half dozen fish, 30 lb class**, on the boat in the opening hours (`LsFMBCa9DOQ`); another two-night stretch stacked bluefin on the jig including a **"hot 90-pounder"** (`sHnqSIOjTdM`).

### The daylight program

- **Chummed sardines + flyline on a circle hook** is the bank's bread and butter. Stated tackle: **25 lb mono or fluoro leader to a #2 circle** (`nQvJnfb5jQ4`); **40 lb flyline floor** for bluefin (`UfuiWFVvz2E`); **No. 4 circle, 40 lb line/leader, short piece of fluoro** (`947solNfiPw`). One deckhand's log: **~90% of daytime bites came on flyline**, on a **25–30 lb fluorocarbon** stick, majority on **size 2 circles** (`149px8WQ2Ng`).
- **Circle hooks specifically for big bluefin** — their teeth saw through the leader, and a circle's corner-of-the-mouth set keeps the leader out of the teeth (`RbqOKkINSCM`). Physical corroboration: a 40 lb fish came aboard **still carrying another angler's hook** after chewing through that line; crews caution a hooked bluefin will hunt **any** abrasion point — another angler's line, the anchor rode, the bottom of the boat (`c3NFkQbdDy0`). One crew member on the Ranger 85 stated a personal **J-over-circle** preference — kept side by side, one crew's stated preference, not reconciled.
- **Shallow marks around the boat while chumming (~60 ft):** yo-yo iron, drop through and crank fast; a heavy bite on the drop reads as the rod going dead-weight, "almost like stuck on the bottom" (`ntQXxcH5sjI`).
- **Wind up, no surface sign:** fish **sound to 30–50 fathoms** — meter-and-jig, not troll (`HWx1jDTGsng`).
- **Foamers:** poppers first (they hold the zone longest), then surface iron, then a small lead bait; run **ahead** of the school's travel, stop hard, cast to the middle, **2–3 casts per school** then move. Wait for the **"jacuzzi"** circular form — spread-out directional feeders are picky (`seasonal/august.md`, `techniques/foamer-casting.md`). Bluefin foamers are **slack-tide biters** (`conditions/tide-and-slack.md`). Warning from `mDmbGdQAy-4`: foamers all around the boat converted on **nothing** — trolled bar and cast plugs both scoreless — because the fish were locked on **saury, anchovies, microbait**; a dead flying fish under the kite is what converted.
- **Kite:** your Saturday dawn (8–12 kt) is inside the KB's **8–15 kt kite window**, and a flying fish under a kite is called *the* most effective method for **100–300 lb** fish (`species/bluefin-trolling.md`). A kite was also flown alongside bait rods in **daytime** at Cortez (`QSvzVHW9UMk`).
- **Troll:** speed-troll a full-size Mad Mac at **13–15 kt** when it's **too light to kite (under ~8 kt) or the fish are too spread out to sit and kite over** — a coverage need, not a sea-state call (cameron). Troll **sweeping arcs around the bird/bait area**, not straight-lining away (tuna move at low single-digit mph), and don't troll the fleet's prop wash.

### Yellowtail are the co-target, and the fallback

`species/yellowtail.md`: Cortez yellowtail marked at **60–80 ft in 120 ft**, graded **20–40 lb**, on **fly lines, J hooks, surface irons, yo-yo irons and sinker rigs**, anchored **15–25 fathoms**, fished sunup to ~11:00–noon. **40 lb flyline, droppable to 30 lb if line-shy** — with the caveat that **Cortez yellows "swim straight down" into the rock** once hooked on lighter line. A full-speed yo-yo bite there had fish fighting "mean" on **60 lb and 50 lb**, with one angler rocked on **60 lb** (`zBd1mayUt_I`). **J hooks for yellowtail, circle hooks for bluefin** is the stated split (`UfuiWFVvz2E`).

### How good it can be — and how binary

Mid-August 2024 at Cortez/Tanner, captain Jake Hensley (Ranger 85, H&M San Diego): the school switched on **the week before** the trip after being scattered and sparse; distribution was unusually wide — **"not very common to just drive through 20 to 30 miles of fish"**, with a boat 15 miles away seeing the same thing instead of the more typical isolated 4–5 sq mi patch — and he cited **50 to 100 fish days**, anchor and drift both producing (`LsFMBCa9DOQ`). Against that, Capt. TJ described fish holding **outside** the bank for **several days, close to a week**, then another **10 to 14 days** before they pushed in close enough to anchor on the bank (`eL1Qm33-Mj0`). That's the honest spread: it is either wide-open or it is a long look.

And **August is the KB's peak-dispersal month** — bluefin scatter across the whole Bight, "showing up in weird places, gone the next day," yesterday's spot a weak prior; the fleet shifts offshore and the islands lose coverage, so **absence of reports is coverage bias, not absence of fish** (`seasonal/august.md`, `planning/report-reading-and-forecasting.md`).

### Your conditions, read

- **SST 69.4 / 69.9 °F** — far under the **76 °F soft ceiling**, and the KB's ceiling rule only ever runs the other way (warm SST is soft evidence *against*, never a hard exclusion). Nothing here argues against bluefin on temperature. But the actual rule is **relative, not absolute**: bluefin sit the **cool side of a break when the surrounding water is warm, the warm side when it's cold** — *read the break, not the thermometer* (`conditions/water-temperature.md`). Your three points give a **1.7 °F spread** with the banks warm and the 43 cool; the KB gives no absolute preferred band, so I can't turn 69.4 vs 69.9 into a pick.
- **Chlorophyll 0.3** — the KB has **no numeric chlorophyll scale**. What it has: chlorophyll has an **age** (new cold bloom = skip now, mature bloom edge = fish it), the fishable water is an **edge, not the middle of a mass**, and **bait holds in the dirtier water while predators work the dirty/clean seam** — clean blue water trolled up nothing because the bait wasn't there (`conditions/water-color.md`). Your own doctrine in that note: in warm-water years weight color at least as heavily as SST and don't fish dirty green. A single offshore number without a gradient doesn't resolve into a call.
- **Spring tide.** Full moon = spring tides, so the moon window and the tide window stack (`conditions/moon.md`). Bluefin foamers bite the slack; **be on the highest-percentage zone an hour before the change**, not at it. **I don't have tide times for 08-29** — the KB carries no tide tables.

---

## 3. What I'd actually run this weekend

Same water state, same moon, boat that fits it.

**Target: the 43 and the below-Clemente complex.** `sources/spot-lists.md` puts the 43 at **32°39.333′N / 117°58.417′W** — **~35.5 nm** from your La Jolla NW corner waypoint, **~27 nm** west of the North 9 Mile Bank. `locations/zone-lexicon.md` is explicit that the **43, 181, 182, 289, Clemente Ridge up to Mackerel Bank** read as **one ~50–60 square-mile search box** — you do not "check the 43," you plan **hours of looking**, glassing and running contour between features. Budget it as a commitment, not a spot-check. (Your 68.2 °F there is the cool side of the day's spread.) Bonus context: the 43 draws bluefin effort partly because it now sits inside a **closed rockfish area** (California/CDFW, as-of 2020-12, `Rf1HKJG-SDg` — verify current regs), so the boats that used to stop there for rockfish work it for tuna instead.

**Timing:**
- **Break your ~8 am norm and leave at first light.** The wind graph runs 8–12 at dawn → 15 by noon; the KB rule is that if it's windier than forecast in the morning you **assume it builds all day and a small boat bails early**. You are buying the calm hours, not saving them.
- Expect a **slow morning** (full-moon night before, both voices agree) with the bite **picking up late** — so don't read a dead 07:00 as a dead day, and plan your latest fishable window against the wind build rather than against the fish.
- Anchor your zone timing to the **tide change, arriving an hour early**; on off-peak days (post-moon is off-peak) action **compresses into the tide windows** rather than spreading across the day.

**On the way out:** run a **paddy line**, not a stakeout. August is the peak of the paddy program, best water is **south of SCI/Catalina and Dana Point to Oceanside southward**; paddies restock only in darkness, so a dry paddy stays dry — **look, sonar, one bait, move** (`seasonal/august.md`, `conditions/kelp-paddies.md`, `locations/bight-geography.md`). Also: **yellowfin show in August and are more lure-cooperative than bluefin — a surface yellowfin bite can fire the bluefin**, so treat them as a trigger and an area indicator, not a consolation.

**Search discipline** (`planning/search-and-glassing.md`): glass from a full stop or bow into the swell at ~1 kt, **360° in small increments, 3–4 minutes per scan**, watch a bird **30–40 seconds** before judging it; **stations 3–4 mi apart**; along a bank run the contour at **16–18 mph** with a lookout **~30° off each bow**. Your terns are the sign you run to.

**Gear off your own rack:**
- **Foamers / jumbo shot:** Talica 25 on the Phenix Axis 8'0" 3XH (60–130 lb, 100 lb braid) — your own stated rod for an **80–140 lb** foamer school. Clear Choice Ghost Popper 150 first (poppers hold the zone longest), Zakana 100 g or Slidekick 120 g to downsize to tiny anchovy.
- **Surface iron:** Torium 20HG on the 10' Phenix Abyss.
- **Yo-yo on ~60 ft bait marks:** Trinidad 40 (8'0" XH 40–80, 80 lb braid) with the Salas 6X or CP 105.
- **Flyline:** Avet MXJ on the Teramar 9'0" MH, 50 lb braid — **40 lb** flyline, drop to 25–30 lb fluoro if they're picky, **circle hooks** for bluefin (size 2, stout wire), **J** for yellowtail.
- **Troll to cover the box:** 2–3 lures, divers (Halco LP190 XDD, Husky Magnums) in the **15° gunnel holders**, bar or skirt out of the **5° elevated shotgun**; Madmacs 200 at **13–15 kt** only if it goes light or the fish are too spread to sit on.

**Care:** you carry **100–125 lb of ice**. Slurry is **~2 cups rock salt per 7–10 lb bag** plus a splash of seawater; chill times **30–40 lb ≈ 2 h, ~100 lb ≈ 3–5 h, >100 lb overnight, re-iced** (`fish-care/tuna-care.md`). Bleed and gill-and-gut on the water before icing. **Bag limit: 2 Pacific bluefin per person per day** (California/CDFW, as of 2024-11 — verify current regs, `usHl-4SfqDA`).

---

## 4. Two gear gaps you should close before any Tanner/Cortez attempt

1. **You have no knife-jig setup and no knife jigs.** The bank fishery out there is fundamentally a **night jig** fishery, and `profiles/cameron/rods.md` lists a dedicated SPJ/speed-jig setup as an **open item you're still shopping**. Ironically the Talica 25 setup is nearly identical to the corpus's canonical overnight/multi-day night-jig outfit — **Talica 25, 100 lb braid marked every 50 ft, 10 ft leader tied straight from braid to 130 lb fluoro, no crimp no swivel, jigs 250–400 g** (`gevNj2Y1Ep8`) — but your Axis is a rail rod, not a short parabolic jig stick, and `profiles/cameron/tackle.md` shows **no knife jigs at all** in the inventory (surface irons, two yo-yo irons, a 100 g Zakana, poppers). You'd be at Cortez with nothing that meets that captain's **300 g floor**, let alone the 500 g the wind night called for.
2. **The kite.** `species/bluefin-tuna.md` records you started kite fishing in **July 2026**, with the Fathom 80 named as the **future kite rod** (keep the 100 lb braid for capacity and less wind-blow, 200 lb leader, small boat can chase). Saturday dawn at 8–12 kt is squarely in the kite window and the KB says that's *the* big-fish method — but helium assist is ruled out on the panga (no room for a tank), so a dying wind leaves you with no light-wind fallback but the troll.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `planning/report-reading-and-forecasting.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/current-structure.md`, `conditions/tide-and-slack.md`, `conditions/deep-scattering-layer.md`, `seasonal/august.md`, `seasonal/june-july.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `species/yellowtail.md`, `techniques/knife-jigging.md`, `techniques/kite-fishing.md`, `techniques/foamer-casting.md`, `techniques/fighting-big-bluefin.md`, `tackle/rod-and-reel-selection.md`, `fish-care/tuna-care.md`, `bait/bait-tanks.md`, `locations/zone-lexicon.md`, `locations/bight-geography.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`  
*videos:* `NC3-3pJDEgo`, `fri_BWI-VA0`, `ntQXxcH5sjI`, `947solNfiPw`, `c3NFkQbdDy0`, `nQvJnfb5jQ4`, `eL1Qm33-Mj0`, `LsFMBCa9DOQ`, `QSvzVHW9UMk`, `UfuiWFVvz2E`, `zBd1mayUt_I`, `sHnqSIOjTdM`, `r4J5nP5Bkl4`, `usHl-4SfqDA`, `mDmbGdQAy-4`, `HWx1jDTGsng`, `nRFFM8DT-og`, `Ul5FLB2dFgQ`, `scmPq63lLWM`, `RbqOKkINSCM`, `gevNj2Y1Ep8`, `xPFm_ZV2PZU`, `149px8WQ2Ng`, `PrdPJy26H8c`, `Rf1HKJG-SDg`, `Blh2BA-7Ono`, `HzE4FHHcvTk`, `CMQkHQMxbXM`, `cameron`  
*gaps admitted:* No Tanner Bank or Cortez Bank location note exists in this KB — the banks appear only as coordinates in sources/spot-lists.md plus scattered trip observations inside species notes; there is no per-spot page with depths, structure, approach, or hazards (e.g. the Bishop Rock shoal is never mentioned). | No fuel capacity, cruise speed, fuel burn, or range figure for the Panga Marine Marquesas 22 anywhere in profiles/cameron/boat.md — only top speed ~35 kt and idle ~1.5 kt — so I cannot state whether ~190 nm round trip is inside or outside the boat's actual range. | No launch-point coordinate for Dana Landing / Mission Bay in the KB, so my leg distances are measured from the La Jolla NW Corner waypoint in Cameron's own list, not from the ramp. | The KB says nothing about lunar eclipses — no note in conditions/ mentions one — so I have no basis to adjust the plan for the 2026-08-28 partial eclipse in either direction. | No numeric chlorophyll scale or threshold anywhere in conditions/water-color.md — only bloom age (new cold bloom vs mature bloom edge) and edge-vs-mass doctrine — so a single 0.3 offshore reading cannot be graded good or bad. | No absolute SST preference band for bluefin — conditions/water-temperature.md gives only the relative break-side rule and the 76 F soft ceiling — so 69.4 vs 69.9 F cannot be turned into a bank pick. | No tide tables or tide times in the KB, so I cannot give slack-tide windows for 2026-08-29 despite bluefin foamers being slack-tide biters. | No battery-endurance figure for running the 500 GPH / 2.1 A bait pump overnight offshore off the single Group 24 start battery — bait/bait-tanks.md documents the NOCO AC charger as the overnight solution, which is a dock solution, not an offshore one. | No guidance anywhere on anchoring a small boat in the 15-25 fathom (90-150 ft) depths the corpus boats anchor in at Cortez, or on anchor tackle for that depth 90+ nm offshore. | No sourcing, storage, or rigging-availability guidance for flying fish (the kite bait) — techniques/kite-fishing.md and rigging/flying-fish-harness.md cover the harness but not where a private boat gets the bait. | No small-boat / private-boat overnight offshore procedure at all — no watch-standing, lighting, night-running, or safety-equipment doctrine; every Tanner/Cortez trip in the corpus is an 80-85 ft sportboat on a 1.5-3 day charter. | The KB does not reconcile whether 100-125 lb of ice is sufficient to core-chill a >100 lb bluefin that fish-care/tuna-care.md says needs an overnight, re-iced hold. | Distances between banks and from the La Jolla NW corner are my own great-circle arithmetic on the KB's coordinates, not figures stated in any note.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## Verdict: **No-go** for the overnight to Tanner/Cortez on this boat, this weekend.

Two independent things kill it — the sea state, and a boat envelope the knowledgebase says I'm not allowed to guess at. The bank itself is a legitimate late-August bluefin target; the KB has real August data for it. It's the platform and the weekend that don't fit. I've laid out the run anyway, plus what I'd actually do with Saturday.

---

## 1. The envelope, and the one question I have to ask you first

Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) step 1b I set `{regions, waters}` before opening a single species note.

- **regions:** `socal-bight` — Tanner and Cortez Bank are explicitly inside the Bight per [`locations/regions.md`](locations/regions.md).
- **waters:** `bank`, `open-ocean`.
- **Launch:** Dana Landing, Mission Bay ([`profiles/cameron/spots.md`](profiles/cameron/spots.md), [`profiles/cameron/boat.md`](profiles/cameron/boat.md)).

**But the envelope is incomplete, deliberately.** [`profiles/cameron/boat.md`](profiles/cameron/boat.md) carries `range_nm: null` and `sea_state_max_ft: null`, with the note in the file itself: *"Cameron has not stated these — left null rather than guessed. Until they are filled, the protocol must ASK for range and sea-state instead of assuming one."*

So: **what is the Marquesas 22's usable range at cruise, and what's your honest sea-state ceiling?** I'm not going to invent numbers for a 190-nm round trip. The KB records only that the boat *tops out ~35 kt and idles ~1.5 kt* — no cruise speed, no fuel burn, no range. Everything below treats the run as unproven rather than assuming it works.

## 2. The run, as the KB describes it

| Bank | Coordinates ([`sources/spot-lists.md`](sources/spot-lists.md)) | Distance |
|---|---|---|
| Tanner Bank | 32 42.000 / 119 08.000 | ~92 nm from the La Jolla NW Corner anchor (32 50.630 / 117 18.460) |
| Cortes Bank | 32 26.417 / 119 07.833 | ~95 nm from the same anchor |
| 43 | 32 39.333 / 117 58.417 | ~35 nm from that anchor |

(Distances are arithmetic on the KB's own coordinates.) The corpus figure agrees: [`species/yellowtail.md`](species/yellowtail.md) calls Cortez Bank *"a legendary SD-offshore high spot roughly **110–115 mi** from San Diego, **a full overnight run for a sportboat**"* (`UfuiWFVvz2E`). Boats fishing it in the corpus are 80–85 ft sportboats — the Constitution out of Fisherman's Landing (`UfuiWFVvz2E`), the El Dorado and Ranger 85 out of Long Beach at ~90 mi (`nQvJnfb5jQ4`, `LsFMBCa9DOQ`). The KB has **no private-boat or small-boat account of this run at all.**

## 3. Why the weather says no — this is the decisive one

[`conditions/sea-state.md`](conditions/sea-state.md) carries Capt. Dave Hansen's go/no-go thresholds (`NC3-3pJDEgo`, 2020-11-18), and your Saturday numbers land on the **named unfishable combo**:

> **12–15 kt wind with 4–8 ft swell at a 9-second interval** — *"you can't go out there… you just cannot be caught out there,"* a dire situation **even for bigger boats**; he holds the larger boats he runs at the dock in that combo too, not just as small-boat caution.

Your Saturday is NW **4 ft @ 9 s** with wind building to **15 kt** by noon. That is the combo, term for term. Supporting rules from the same note, all firing:

- **"Swell interval under 10 seconds is a hard bad-sea flag"** — *"absolutely horrible," independent of height.* Both days are 9 s.
- **Hansen's personal cutoff is not running above ~12 kt** (wind over ~12 kt is what raises whitecaps). Friday is 15–20 kt; Saturday builds through 12 to 15.
- **Forecast error is asymmetric** — assume the forecast errs on the worse side, and that afternoon W at the islands *strengthens* rather than eases. Also: if it's windier than forecast in the morning, **assume it builds all day — a small boat bails early** (7/14/22). "Builds to 15 by noon" is the forecast's *good* case.
- **Current-vs-swell opposition.** Summer uphill countercurrent running against NW swell compresses the interval and stands the swell up — *4 ft @ 10 s fishes like 6 ft @ 7–8 s*, and point forecasts don't show it. You gave me no current field, so I can't rule this out; it can only make the read worse, never better.
- **Homebound wind.** The KB's rule is to plan return timing **against** the afternoon build, not off the outbound conditions (8/17/22). Your return leg is ~95 nm starting into a wind that's still building at noon.

On **"no Small Craft Advisory"**: the KB doesn't use SCA as its go/no-go gate anywhere. It uses the numbers above, and the numbers above fire. A no-SCA morning doesn't move Hansen's 9-second flag or his 12-kt cutoff.

**Friday night's transit is worse than Saturday's fishing weather** — NW 15–20 kt over 5 ft @ 9 s, in the dark, ~95 nm, in a boat with **no trim tabs** (engine trim is the only attitude control), a **foam-filled hull with a very small bilge**, a **manual-switch bilge pump with no float switch**, and a **single 115 hp Yamaha** with no second engine ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)). Your own trim routine has a person riding the bow bean bag with the note that *"rough days forward are brutal — rider catches air then hits the deck."* That's your record of how this hull handles a steep sea.

There's also a power problem specific to overnighting offshore. The panga has **no AC/shore-power inlet and no house battery** — the 30-gal tank's Rule 401 pump (500 GPH, 2.1 A) runs off the **single starting battery** ([`bait/bait-tanks.md`](bait/bait-tanks.md), [`profiles/cameron/boat.md`](profiles/cameron/boat.md)). The NOCO GEN5X1 that "holds the battery up so the bait pump can run overnight" is a **hardwired AC pigtail** unit — that's a dock/trailer solution, not a 95-nm-offshore one. The KB does not resolve whether the pump can run all night offshore off the start battery, so I won't tell you it can.

## 4. The moon makes this a bad weekend to spend that fuel

Full moon lands **on 08-28 — your departure night.**

[`conditions/moon.md`](conditions/moon.md) keeps two views side by side and neither favors Saturday morning:

- **Landesfeind (high):** the days **leading into** the full moon are the strongest documented bluefin windows. 08-28 is the peak — you'd be arriving at the back edge of that window, not inside it.
- **Hansen (`fri_BWI-VA0`, 2022-02-12):** the full moon itself *"is not good"*; the peak is the **travel period, not a bite period**. The morning **after** a full-moon night is typically slow — the school *"has been feeding all night and doesn't have a tendency to feed real well right away"* — with the bite **picking back up late in the day**. His stated instruction: if fishing a full moon is unavoidable, **fish it late rather than push the early-morning window.**

Saturday dawn on the bank is precisely the window he tells you not to push — and a 22-ft boat 95 nm out doesn't get to stay for the late-day rebound and then run home.

The relocation figures compound it: open-water bluefin not holding structure move **10–15 nm overnight** (Landesfeind, 7/21/22); Hansen puts it at **20 miles after a night of a full moon** for albacore, bluefin and yellowfin. Both figures kept side by side, not averaged ([`planning/report-reading-and-forecasting.md`](planning/report-reading-and-forecasting.md)). Any report you're running 95 nm on is displaced by that much by the time you arrive. The honest caveat: that prior is stated for fish **not holding structure**, and a bank high spot is structure — the KB gives no bank-specific advection figure, so I can't tell you how much it discounts.

Layer on [`seasonal/august.md`](seasonal/august.md): peak dispersal, *"showing up in weird places, gone the next day"* — **yesterday's spot is a weak prior**, and the whole fleet is offshore so island reports go quiet (read as coverage bias, not dead water).

**On the partial lunar eclipse: the KB has nothing.** No note anywhere covers eclipses. I'm not going to speculate about it.

## 5. What's actually out there in late August (so this isn't just "no")

The bank is a real target this month, and the KB is specific that August Tanner/Cortez sits **beside** — not inside — the Oct–Dec "condense outward to Tanner/Cortez" pattern ([`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`conditions/water-regimes.md`](conditions/water-regimes.md)):

- **Mid-August 2024, Tanner Bank, anchored, ~120 ft of water** (`ntQXxcH5sjI`): bluefin and yellowtail both landed over two days; **bluefin taken on bait marks sitting around 60 ft** while the boat chummed sardines.
- **Tanner Bank, eastern side of the high spot, day one** (`947solNfiPw`): sardine bite from first light; **41 lb the previous day**, day-one grade opening ~**30 lb**, a fish fought "on 50 [lb]", one flylined on a **No. 4 circle hook, 40 lb** line/leader with a short fluorocarbon length. The crew's framing of the challenge: **10 lb schoolies up to 80, "maybe even 100" lb** moving through together on one size line.
- **August 2024, Cortez Bank, ~90 mi off Long Beach** (`nQvJnfb5jQ4`): bluefin and yellowtail on flylined sardines, **25 lb mono or fluoro leader to a #2 circle hook**, working a **50–60 fathom** edge off the high spot; crowded fleet on the spot.
- **Mid-August 2023, ~90 mi off, at anchor** (`c3NFkQbdDy0`): mixed bluefin/yellowtail, one bluefin at **40 lb**.
- **Night, Cortez/Tanner, mid-August 2024** (`LsFMBCa9DOQ`): an overnight jig session read marks **360° around the boat, from 50 fathoms down to 80 fathoms and below** — deeper than the general 30–50 fm sounded-school range. Capt. Jake Hensley's read on that season's night windows: roughly **9:00 pm–11:00 pm/midnight**, a lull, then **~3:30 am to sunrise**.
- **Yellowtail as the co-target:** Cortez fish marked at **60–80 ft in 120 ft of water**, graded **20–40 lb**, on flylines, J-hooks, surface irons and yo-yo irons; captain's floor **40 lb flyline**, droppable to 30 if they get line-shy, with the warning that Cortez yellows **"swim straight down" into the rocks** once hooked (`UfuiWFVvz2E`). Another Cortez trip had them fighting "mean" on **60 and 50 lb**, with an angler **rocked off on 60 lb**, in ~50 fathoms (`zBd1mayUt_I`).

**On your SSTs.** 69.4 / 69.9 / 68.2 °F is nowhere near a problem — the KB's only ceiling is the **76 °F soft ceiling**, and it's soft: bluefin were seen foaming in 76 °F ([`conditions/water-temperature.md`](conditions/water-temperature.md), 9/14/22). But the KB's actual bluefin rule is *relative, not absolute*: **cool side of a break when the water is warm, warm side when it's cold** (10/20/22). Three point readings across ~60 nm aren't a break — and the note warns that sharp offshore edges can **jump multiple degrees in ~1 mi**. Your 1.7 °F spread tells me the general zone is uniform-ish; it tells me nothing about where the edge is. That needs the gradient field per spot and along the route, which I'm not fetching here.

**On chlorophyll 0.3:** the KB has **no numeric chlorophyll scale** — nowhere does it say what a given mg/m³ value means. What it gives is qualitative and still useful ([`conditions/water-color.md`](conditions/water-color.md)): chlorophyll has an **age** (new cold bloom = skip today, mark it for the recovery; mature bloom **edge** = fish it), **bait holds in the dirtier water while predators work the dirty/clean seam**, and bluefin will swim into the dirtiest coldest water to be on bait. Also your own recorded doctrine: in warm-water years, weight color at least as heavily as SST and don't fish dirty green water. One offshore number isn't an edge — the edge is the target.

## 6. Gear resolution against your profile — and one gap that matters

If you were out there Saturday with 8–12 kt at dawn:

| Situation | Technique | Your gear |
|---|---|---|
| 8–15 kt, 100–300 lb fish up | **Kite** — *the* most effective method for that grade ([`techniques/kite-fishing.md`](techniques/kite-fishing.md)) | Fathom 80 setup: Okuma PCH-C-741XXXXH 7'4" 150–200 lb, Penn Fathom II 80LD2 2-speed, ~1000 yd of 100 lb braid — the profile's designated **future** kite rod |
| Too light to kite, or fish too spread out to sit over | **Speed-troll a Mad Mac 200 at 13–15 kt** ([`species/bluefin-trolling.md`](species/bluefin-trolling.md)) | Madmacs 200 ×2 + 130, on the Talica 25 (Phenix Axis 8'0" 3X-H 60–130 lb, 100 lb braid) or Fathom 80 |
| Light-moderate, school grade | **Spreader bar**, small presentation, out of the elevated shotgun holder | Three Half Fish bars; shotgun sits ~3 ft higher / 4 ft forward of the gunnels at 5° |
| Calm, school grade, want a swimmer | **DTX 165 / Husky Magnum divers**, 60–100 lb (action dies on heavy line) — **divers want the low gunnel holders** (15°) | DTX Minnow 165, Husky Magnum 25 ×2 + 15, Halco LP190 XDD ×2; TLD 20 entering rotation for diver duty |
| **Marks ~60 ft around the boat while chumming, no surface sign** — the Tanner August scenario | **Yo-yo iron**, 40–60 lb class stout rod + high-speed reel ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)) | Salas 6X, Salas CP 105, on the Trinidad 40 (Rainshadow 8'0" XH 40–80, 80 lb braid) — **good match** |
| Chummed up / picky on bait | **Flyline sardine, circle hook** ([`techniques/flyline.md`](techniques/flyline.md)); 4/0 thin-wire circle straight-tied for sportboat sardine (`ftEvyfwjZFU`) | Avet MXJ on the Teramar 9'0" MH 30–65 lb, 50 lb braid |
| Foamers, castable seas | **Poppers first**, then surface iron, then a small lead bait; bite comes on the **pause/fall** | Ghost Popper 150, TP 140/160, JRI-5/JRI-7, Nomad Slidekick 120g, Zakana 100g; Talica 25 is your stated jumbo-foamer (80–140 lb) rod |
| **Night bite, fish rising on the DSL** — the reason you'd overnight at all | **Knife-jigging vertical**, 100–130 lb braid jig class / PE6–8, jigs **150–400 g** | **GAP — you don't own this** |

**Name the gap plainly:** the single highest-percentage reason to make an overnight run to those banks in August is the **night jig bite** — and it's the one program you can't currently fish. [`profiles/cameron/rods.md`](profiles/cameron/rods.md) lists a *dedicated SPJ / speed-jig setup* as an **open item you're still shopping**, and [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md) lists no knife jigs at all — surface irons, yo-yo irons, casting jigs and poppers only. The depth numbers make the substitution question moot: fish sounded at **240–360 ft** are the stated reason a flat-fall/knife jig needs to be **250 g or greater** — 120–150 g "won't reach that depth quickly enough," especially drifting in wind (`eehDVb6_GoI`); and the bank-specific night read was **50 to 80 fathoms and below** (`LsFMBCa9DOQ`). Your heaviest jig is a 120 g Nomad Slidekick surface iron. I'm not going to tell you to sink it out and call that the night program — it isn't the same tool.

The kite has an unresolved gap too: [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md) is a hard-bait inventory and lists **no kite, no flying fish, no flying-fish harness, and no 200 lb-class bite leader / 300–400 lb fluoro**. The KB records that you started kite fishing July 2026 and ruled out a helium assist (no room for a tank on the panga), but it doesn't inventory the terminal end. **Do you have the kite, flyers and harness aboard?**

**Fish care, if you did land fish** ([`fish-care/tuna-care.md`](fish-care/tuna-care.md)): bleed and gill-and-gut immediately on the water, then a below-freezing slurry — **rock salt ~2 cups per 7–10 lb bag of ice**, plus a splash of seawater, fish fully submerged, re-iced as it burns down. Chill times: **30–40 lb ≈ 2 h; ~100 lb ≈ 3–5 h; >100 lb overnight, re-iced.** You carry **100–125 lb of ice per trip**. Limit is **two Pacific bluefin per person per day** (California/CDFW, as stated on camera 2024-11, `usHl-4SfqDA` — **verify current regs before you fish**). The KB gives no cooler-capacity math, so I can't tell you how many 40–80 lb fish your ice budget actually holds.

## 7. What I'd do with Saturday instead — inside the envelope

The NW blow itself points where to go. [`locations/bight-geography.md`](locations/bight-geography.md) (`HzE4FHHcvTk`, 4/21/22) maps wind rollover: the **northern Channel Islands and the LA/Ventura shelf get crushed** (a strong NW event rolls surface temp down **5–8 °F**); **south of Newport is less prone**; and the **Coronados, the tuna grounds, Catalina and San Clemente held their water through the blow.** You launch at Mission Bay — you're already on the right side of that map.

**Target the below-Clemente complex, entering at the 43** — 32 39.333 / 117 58.417, ~35 nm from your La Jolla NW anchor, and the coolest of your three given readings at **68.2 °F**.

- Treat it as a **search box, not a spot.** [`locations/zone-lexicon.md`](locations/zone-lexicon.md) is explicit: the 43 / 181 / 182 / 289 / Clemente Ridge up to Mackerel Bank read as **one ~50–60 square-mile box** — *"You do not 'check 43'; you plan hours of looking."* Budget it as a half-day commitment.
- **Why there's effort on it:** the 43 was the destination rockfish grounds for decades and now sits inside a closed rockfish area, so the effort that stopped there for rockfish targets the same high spot for bluefin instead (Capt. Dave Hansen, `Rf1HKJG-SDg`, California/CDFW as-of 2020-12 — **verify current regs**). Structure and bait draw unchanged; target species changed.
- **Bank naming, so the box makes sense:** a bank is named for the fathom depth of its shallowest point — the 43 tops out at 43 fathoms before the bottom falls away (same source). Six feet to a fathom.
- **Run the search properly** ([`planning/search-and-glassing.md`](planning/search-and-glassing.md)): along a bank, **run the contour at 16–18 mph with a lookout ~30° off each bow**; glass from a **full stop or bow into the swell at ~1 kt** — you cannot glass off a rolling drifting boat; **360° in small increments, 3–4 minutes per full scan**; watch a bird **30–40 seconds** before judging it; **space glassing stations 3–4 mi apart**. From deck level you'll pick up a few terns at **0.5–1 mi**, a big bird spot at **~2 mi**. Your own practice — follow working terns even with nothing else going — is the right instinct here; a **moving dive-line means bait being pushed from underneath**.
- **Sounder** ([`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)): put the GPSMAP 840xs on **manual range, not auto**. Hansen's private-boat rule is **0–150 ft** (bait budget won't draw fish up from 250 ft), elaborated elsewhere to **0–300 ft** for bluefin, with the bottom sitting **mid-screen**. On auto over 2,000–3,000 ft of water, *"10 tons of bluefin sounded through simply doesn't show."* Mark a shallow-band mark on the GPS, run past, turn, and troll back over it with the Mad Mac.
- **Expect the meter to under-read in the chop.** In flat conditions the cone shoots right along the surface; in choppy/rolly water it's shot lower, so **a fish high in the column won't show until you're right on top of it** (`fgTmUq78ofQ`). That's a mechanism, not a settings problem — it means glassing carries more of the load on a 4 ft day than it would on a flat one.
- **Troll sweeping arcs around the bird/bait area, never straight-lining away** — tuna move at low single-digit mph, you're not chasing a fleeing school — and **don't troll through the fleet's prop wash** ([`seasonal/august.md`](seasonal/august.md), 8/17/22).
- **Foamer discipline:** wait for the **"jacuzzi"** — solid circular whitewater ≈ a bite every cast. Spread-out directional feeders are picky. Your recorded program is **~2–3 casts per school**, smaller presentation out-fishing bigger, timed around slack tide.
- **Full-moon fallback if the tuna are sulking:** don't plan a mid-day bass segment. On clear full-moon nights calico and sand bass **gorge at night and shut down by mid-morning** — fish them **first light or late day** ([`conditions/moon.md`](conditions/moon.md)).
- And run the return **against** the build, not after it.

## 8. What would flip this to a go

1. **A stated range and sea-state ceiling** in [`profiles/cameron/boat.md`](profiles/cameron/boat.md) that actually covers a ~190 nm round trip with reserve.
2. **Swell period out past 10 s.** The 9-second interval is the hard flag; height matters far less than period — *10 ft @ 15 s from the south is barely felt; 3–4 ft @ 4–5 s is brutal.*
3. **Wind under ~12 kt** with a 12–24 h hindcast confirming it hasn't been blowing overnight (a calm morning read after a windy night is a trap).
4. **The night-jig setup bought and spooled** — PE6–8 / 100–130 lb braid class, jigs to 400 g — so the overnight actually buys you the program that justifies the distance.
5. **A moon window on the leading days**, not the peak night, or a plan that can stay for the late-day rebound.
6. **A current field** showing the countercurrent isn't standing that NW swell up along the route.

Cortez and Tanner will still be there. Per [`conditions/water-regimes.md`](conditions/water-regimes.md) and [`locations/bight-geography.md`](locations/bight-geography.md), as the coast cools and fragments in fall the fish **condense outward toward Tanner and Cortez** — the outer banks get *better* as the season closes, and the Nov–Dec prior is Tanner/Cortez, night-dominant, with 300 lb fish through November. That's the trip to build the boat and the jig quiver for, with a weather window you pick rather than one you accept.

---

### What the KB could not answer here

- **No coverage of lunar eclipses** — nothing anywhere in the KB.
- **No numeric chlorophyll scale** — "0.3" can't be interpreted against any threshold the KB states.
- **No stated range, cruise speed, fuel burn, or sea-state ceiling** for your boat — the profile leaves these null on purpose and instructs me to ask.
- **No private/small-boat account of a Tanner or Cortez run** — every corpus trip to those banks is an 80–85 ft sportboat.
- **No sea-state limit for speed-trolling** — I can't tell you whether the panga holds 13–15 kt in 4 ft @ 9 s.
- **No resolution of the overnight bait-pump power question** offshore on the single start battery with an AC-only charger.
- **No cooler/ice capacity math** for how many bluefin your 100–125 lb of ice will actually hold.
- **No bank-specific overnight advection figure** — the 10–15 nm / 20 mi relocation priors are stated for fish *not* holding structure.
- **No SST-band doctrine for bluefin** beyond the soft 76 °F ceiling and the relative break-side rule — your 68–70 °F readings can't be graded as "good" or "bad" on their own.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `planning/report-reading-and-forecasting.md`, `planning/search-and-glassing.md`, `planning/electronics-and-sounder.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/deep-scattering-layer.md`, `seasonal/august.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `species/yellowtail.md`, `techniques/kite-fishing.md`, `techniques/knife-jigging.md`, `techniques/yo-yo-iron.md`, `techniques/flyline.md`, `locations/regions.md`, `locations/zone-lexicon.md`, `locations/bight-geography.md`, `fish-care/tuna-care.md`, `bait/bait-tanks.md`, `profiles/cameron/README.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`, `sources/spot-lists.md`  
*videos:* `NC3-3pJDEgo`, `fri_BWI-VA0`, `ntQXxcH5sjI`, `nQvJnfb5jQ4`, `947solNfiPw`, `c3NFkQbdDy0`, `LsFMBCa9DOQ`, `UfuiWFVvz2E`, `zBd1mayUt_I`, `Rf1HKJG-SDg`, `HzE4FHHcvTk`, `usHl-4SfqDA`, `ftEvyfwjZFU`, `fgTmUq78ofQ`, `eehDVb6_GoI`, `m-M0iwX8DjA`, `8XrMkWPRxgs`, `9hEa3sGTh40`, `HWx1jDTGsng`, `nRFFM8DT-og`, `i3qIAHW-SJc`  
*gaps admitted:* The KB has no coverage of lunar eclipses anywhere — nothing on the partial eclipse on the night of 2026-08-28. | The KB states no numeric chlorophyll scale or thresholds, so the given 0.3 offshore value cannot be interpreted against any KB rule; chlorophyll doctrine is qualitative only (bloom age, edges vs. middle). | profiles/cameron/boat.md leaves range_nm and sea_state_max_ft null by design and instructs the protocol to ASK rather than assume — so the boat's usable range and sea-state ceiling for a ~190 nm round trip are unknown. | The KB records the panga's top speed (~35 kt) and idle (~1.5 kt) but no cruise speed, fuel capacity, or burn rate, so no passage-time or fuel-reserve calculation is possible. | Every Tanner/Cortez Bank trip in the corpus is an 80–85 ft sportboat; the KB has no private-boat or small-boat account of the run and no small-boat offshore-overnight safety doctrine. | The KB gives no sea-state limit for speed-trolling, so it cannot say whether the boat can hold the 13–15 kt Mad Mac band in NW 4 ft @ 9 s. | The bait-tank note says the NOCO charger lets the pump run overnight, but boat.md records the charger as an AC pigtail on a boat with no shore-power inlet or house battery — the KB does not resolve whether the pump can run overnight 95 nm offshore off the single starting battery. | The KB gives fish chill times and slurry parameters but no cooler/ice capacity math, so it cannot say how many bluefin the boat's 100–125 lb ice budget will hold. | The 10–15 nm overnight / 20 mi post-full-moon relocation priors are stated for open-water bluefin NOT holding structure; the KB gives no advection figure for fish holding a bank high spot. | The KB has no absolute SST preference band for bluefin — only the soft 76 °F ceiling and the relative break-side rule — so the given 68.2–69.9 °F readings cannot be graded good or bad on their own. | Three point SST values cannot locate a temperature break; the KB's break-side rule needs a gradient field per spot and along the transit route, which was not provided and was not to be fetched. | profiles/cameron/tackle.md inventories hard baits only and lists no kite, flying fish, flying-fish harness, or 200 lb-class bite leader, so kite-program readiness cannot be confirmed from the profile. | No knife-jig / SPJ setup or knife jigs appear in the profile (listed as an open shopping item), so the night DSL jig program at the banks cannot be resolved to owned gear.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

I worked this through the day-plan protocol in the repo (`planning/day-plan-protocol.md`), in order: conditions → envelope → priors/layers → species router → gear against the profile. Here's what the KB says.

## Verdict: **No-go** on Tanner/Cortez for this window, on this boat

Not because of the fish — the water you gave reads reasonable for bluefin out there. It fails at step 1b (the boat envelope) and at the sea-state gate, and those two are binding before any species note gets opened.

---

## 1. The sea state fails the KB's own go/no-go thresholds

`conditions/sea-state.md` carries an explicit captain's-rule threshold set (`NC3-3pJDEgo`):

- **"Swell interval under 10 seconds is a hard bad-sea flag"** — "absolutely horrible," independent of height. Both your days are **9 s**. That flag is on for the entire trip, outbound and back.
- **The named unfishable combo: 12–15 kt wind with 4–8 ft swell at a 9-second interval** — "you can't go out there… you just cannot be caught out there," described as dire *even for bigger boats*, with boats staying at the dock regardless of size.
  - **Friday night: NW 15–20 kt, 5 ft @ 9 s.** That is the named combo at or above its top wind band. That is your transit window.
  - **Saturday noon: 15 kt, 4 ft @ 9 s.** That is the named combo again — and it arrives while you are ~110 miles from Mission Bay.
- **~12 kt is the stated personal cutoff for not running**; above ~12 kt is whitecap water. Your Saturday dawn window (8–12 kt) sits right at that line and only goes up from there.

Two more layers from the same note make the forecast worse, not better:

- **Wind history, not just wind forecast** (`zKmZ4zql2ws`): "a calm-morning forecast can hide overnight wind that already built chop before dawn." Your Saturday-dawn 8–12 kt is sitting on top of a full night of NW 15–20 — that easing dawn number is precisely the trap the note names. The sea at dawn is the sea Friday night built.
- **Current-vs-swell opposition** (`zKmZ4zql2ws`): summer uphill counter-current running against NW swell compresses the interval — a **4 ft @ 10 s forecast fishes like 6 ft @ 7–8 s**, and point forecasts won't show it. You're already at 9 s. I have no current field (you said no live data), so this is a check to run, not an assertion — but it can only degrade the number, never improve it.
- **Forecast error is asymmetric** — assume it errs worse, and assume afternoon W strengthens rather than eases (`zKmZ4zql2ws`); on a small boat the rule is **bail early** (`DnSqw4r7A1s`). You cannot bail early from Cortez Bank.

Note that "no Small Craft Advisory Saturday morning" isn't the gate this KB uses — nothing in `conditions/sea-state.md` keys off the SCA. It keys off wind, period, and the interaction with current.

`locations/tanner-bank.md` also flags, honestly, that **no corpus source states a wind or swell number that turns that zone off** — so I'm applying the general layer, which is what it tells you to do: "Nothing out here is sheltered by land in any direction, so the upstream fetch scan belongs in front of the run."

## 2. Your boat envelope isn't established, and the KB refuses to guess it

`profiles/cameron/boat.md` has `home_port: null`, `range_nm: null`, `sea_state_max_ft: null`, with the comment: *"Cameron has not stated these — left null rather than guessed. Until they are filled, the protocol must ASK for range and sea-state instead of assuming one."* Step 1b of `planning/day-plan-protocol.md` derives reachable `waters` from exactly those two fields. Without them I can't clear `bank` + `open-ocean` at 110 nm, and I'm not going to fabricate the clearance.

**Two numbers I need from you before this run is even discussable: usable range in nm (fuel, not tank size), and your sea-state ceiling in ft.**

What the notes do give:

- **The run.** `locations/tanner-bank.md` states it in statute miles only: **111 mi west of Point Loma** and **~110–115 mi from San Diego** to Cortez (`QSvzVHW9UMk`, `UfuiWFVvz2E`); **~90–100 mi west of Long Beach** to Tanner, ~110 mi to Cortez (`ntQXxcH5sjI`, `fDSd9kqwYW0`, `nQvJnfb5jQ4`). Read it as one run to a two-bank complex: **about 90 miles to Tanner, about 110 to Cortez**, the two banks **15.6 nm apart on a 179°/359° line** (Tanner 32°42.000'N 119°08.000'W; Cortes 32°26.417'N 119°07.833'W, cameron).
- **The KB explicitly has no run stated from any Orange County or San Diego small-boat port, and no fuel figure or sea-state envelope for the crossing** — that's a flagged gap on the page, not something I can fill.
- **"Every account of this water is an overnight run or longer, from a big boat."** The single non-sportboat trip in the entire corpus is a **triple-outboard** private boat that ran 2.5–3 hours to Tanner, with the crew calling the return leg alone over 100 mi (`vCskOx6N-XM`).
- Against that: **2004 Panga Marquesas 22, single 115 hp Yamaha**, no trim tabs, foam-filled hull with slight flex on hard wave impacts, **no house battery** — the 30-gal tank's Rule 401 pump runs off the single Group 24 starting battery, with the NOCO GEN5X1 added July 2026 specifically to hold that battery up while the bait pump runs overnight (`profiles/cameron/boat.md`). Normal departure is ~8 am from Dana Landing; home waters are Coronados, La Jolla, and the San Diego offshore banks.

That's a one-engine, one-battery, 22-ft boat proposing the corpus's longest run, at night, into the combo the KB says nobody should be caught out in.

## 3. Even if you cleared 1 and 2, you can't fish the two programs that make the run worth it

Resolving `species/bluefin-tuna.md` and `locations/tanner-bank.md` against `profiles/cameron/rods.md` + `tackle.md`:

| The bank's core program | Your inventory |
| --- | --- |
| **Kite + flying fish** — the most effective method on 100–300 lb SoCal bluefin (`YsiHziY_PWw`), and the sundown/big-grade play at Cortez (`zBd1mayUt_I`, `vCskOx6N-XM`) | **Gap.** The Fathom 80 is listed as a *future* kite rod; no kite, no flying-fish harness. Kite fishing is a program in progress (started July 2026). |
| **Night jig program** — **300 g floor**, 250 g only for savvy anglers, over 80 lb braid and 130 lb mono/fluoro (`UfuiWFVvz2E`); on a windy hard-drifting night at Cortez the standard 250–350 g wouldn't hold and the boat went to **500 g** (`LsFMBCa9DOQ`) | **Gap.** Heaviest thing in your box is a Daiwa Zakana **100 g**. `rods.md` names the dedicated SPJ/speed-jig setup for night bluefin as still being shopped. Night jigging is an Aug-2026 program in progress. |

Both are named gaps, not substitutions — the protocol's rule is to name the gap rather than swap in something that doesn't fish the same way. On a windy night at 9 s, that 250→500 g step-up is exactly the situation you'd hit.

**What you *could* fish out there,** for completeness:

- **Flyline** — Avet MXJ / Teramar 9'0" MH (50 lb braid), or heavy flyline on the Trinidad 40. Bank numbers: sardine on **25 lb** mono/fluoro to a **No. 2** (`fDSd9kqwYW0`, `nQvJnfb5jQ4`); a **40 lb** daylight floor for bluefin, down to 30 only if they're line-shy, with the caveat that Cortez yellows "swim straight down" into the rocks on light line (`UfuiWFVvz2E`); **20 lb** fluoro to No. 4/No. 2 on a 20–30 lb grade day, some No. 4s running light wire (`QSvzVHW9UMk`).
- **Yo-yo iron** — your **Salas 6X** on the Trinidad 40 (80 lb braid). The Tanner data point is a Salas 6X **Jr** in blue/white, 40 lb fluoro to 65 lb braid, **dropped to ~80 ft with bait marks sitting around 60 ft** while chumming sardines, no surface sign; bite reads as the rod going dead-weight (`ntQXxcH5sjI`). Yours is the full-size 6X, not the Jr — near-match, different sink and profile.
- **Surface iron** (Torium/Phenix Abyss 10') for boils, **poppers** (Ghost Popper 150) on the Talica 25 for foamers.
- **Troll**: 2–3 lures, divers in the 15° gunnel holders, spreader bar out of the elevated shotgun — the Half Fish bars, Madmacs 200, Halco LP190 XDD, Husky Magnums (`profiles/cameron/trolling-lures.md`, `species/bluefin-tuna-trolling.md`). Speed-troll band to locate is **13–15 kt** (`z1CmWHqe9uk`) — flagged in the note as attached to the Rapalas, not the Mad Mac.

---

## What the water you gave is actually saying

For the record, since this is the part that *doesn't* argue against going:

- **69.4 / 69.9 / 68.2 °F is not a break.** 0.5 °F across the 15.6 nm between Tanner and Cortez is a flat field. `conditions/water-temperature.md` is explicit that the value is usually not the absolute number but **which side of a break** a species sits on, and bluefin read **relative, not absolute** — cool side when the water's warm, warm side when it's cold (`OYOda6T3f-8`). With no edge, you have no side to pick.
- **A flat field pushes you to structure.** "Across a big area with no temperature differentiation the fish are most likely on structure like the banks" (`OYOda6T3f-8`, in `locations/tanner-bank.md`). So the banks are the *right* read for this SST field — that's the frustrating part.
- **The temps are in a supportive range, not a warning.** The one bank-edge data point has bluefin holding the cooler **70–72 °F** while yellowtail and yellowfin sat warmer (`i3qIAHW-SJc`); the fall Tanner read was "60-something," the cooler water called the more ideal water (`OYOda6T3f-8`). Cortez's other record is 74–75 °F for a mixed yellowtail/yellowfin/skipjack bite. 69–70 sits below that and in line with the bluefin side.
- **The 43 at 68.2 °F is your coolest number** and it's ~35 nm out, not 110 (see below).

**Chlorophyll 0.3 I can't interpret against this KB.** There is no numeric chlorophyll scale anywhere in it — the layer is qualitative: chlorophyll has an *age* (new cold bloom = skip now, mature bloom edge = fish it), and the fishable water is an **edge, not the middle of a mass** (`conditions/water-color.md`, `h3PTupup17I`). One number offshore gives no edge. Also flagged in `planning/day-plan-protocol.md`: an empty layer is missing data, not a zero.

## Moon: Friday night is the peak, and that's a timing squeeze

`conditions/moon.md` keeps two reads side by side, unreconciled:

- **The days leading into the full moon are the strongest documented bluefin windows** (`XLVUhV8DW64`). Friday 8/28 is the peak itself — you'd be arriving at the end of that ramp.
- **The peak day is a relocation event, not a bite event.** Capt. Dave Hansen's doctrine: 7 days before and 7 days after, with the **peak day itself the travel period**, called "not good" for the bite; **the morning after a full-moon night runs slow**, and if a full-moon trip is unavoidable, **fish it late rather than pushing the early-morning window** (`fri_BWI-VA0`, `LEiyB9QNzHY`).
- On the moon, open-water bluefin not holding structure move **10–15 nm overnight** (`Blh2BA-7Ono`); Hansen puts schools at **20 miles** after a full-moon night (`fri_BWI-VA0`). Discount any report older than a day or two hard.
- A direct dissent is on file — no reliable moon pattern trip to trip (`shZCjX2-fkI`).

Your Saturday is the morning after the peak — the window the doctrine calls slow — and the guidance is to fish *late*, which is exactly when your wind builds to 15 kt. That's the squeeze: the moon says fish the afternoon, the wind says be pointed home by then.

**The KB has nothing at all on lunar eclipses.** No note anywhere addresses eclipse effects on a bite. I'm not filling that from outside the corpus.

## Seasonal prior: August is dispersal, and Tanner/Cortez is the October pattern

`seasonal/august.md`: **peak dispersal — Catalina to San Nicolas to Ventura**, fish "showing up in weird places" and gone the next day (`CMQkHQMxbXM`), so **yesterday's spot is a weak prior** and the fleet is offshore, so island reports thin out (coverage bias, not dead islands). `species/bluefin-tuna.md` puts the **Tanner/Cortez condensation in October–December**, as the coast cools.

That said, **August at Tanner is documented and it produced repeatedly** — mid-Aug 2023 and mid-Aug 2024, anchored bites (`ntQXxcH5sjI`, `947solNfiPw`, `LsFMBCa9DOQ`). The page's own line: "Presence is not catchability's mirror image here." So the month isn't the objection; the boat and the sea are.

---

## What the run and the fishing actually look like out there (so you have the picture)

**Shape of the day** (`locations/tanner-bank.md`): yellowtail from sunup to roughly 11:00 a.m. or noon at anchor, then deeper water for bluefin (`UfuiWFVvz2E`). Night bite runs two windows — roughly **9:00 p.m.–11:00 p.m./midnight**, a lull, then **3:30 a.m. to sunrise** (`LsFMBCa9DOQ`, single-source, one season, ledgered). One overnight started yo-yo and jig fishing at **1:00 a.m.** and put roughly half a dozen 30 lb-class fish aboard in that first session.

**Depths.** Anchor zone **15–25 fathoms**; high spot marked in **~120 ft** with yellowtail at 60–80 ft in that water; a ridge on the edge in **~150 ft**; the drop-off edge worked at **50–60 fathoms**, which produced "right out the gate" after a reposition (`nQvJnfb5jQ4`); night jig marks 360° around the boat from **50 fathoms down to 80, "even below"** (`LsFMBCa9DOQ`) — deeper than the general 30–50 fathom sounded-school band (`HWx1jDTGsng`), kept as a bank-specific extension.

**The program is anchor-and-chum, and current gates it.** Flyline with the current; when the current goes slack the exotics don't go — one morning "missing the current" was spent scratching rockfish until it moved, then a **five-hour yellowtail bite** closed the charter (`fDSd9kqwYW0`). Anchor isn't the only answer; a Cortez day produced on both a drift and an anchor job in ~50 fathoms, and when the anchor spot slowed the crew moved off to search (`zBd1mayUt_I`).

**Positioning is read off structure *and* the fleet.** Expect company — anchoring at Cortez meant picking a slot among "northern boats… southern boats… middle boats," private and commercial sportboats on the same structure (`nQvJnfb5jQ4`). One captain moved onto anchor mid-morning after hearing a nearby boat was stacking fish on an established chum line, judging his drifting boat was picking off only a piece of the school from outside the spot (`QSvzVHW9UMk`).

**Grade is the tackle problem.** At Tanner: **"10 pounders all the way up to 80 pounders, maybe even 100"** through on one size line, and matching hook/leader/weight without going under-gunned called "a total game" (`947solNfiPw`). The corpus's answers sit side by side, and what they turn on is grade and bite quality — not section order: **go down in hook size, not line class** (a 1/0 circle stepped to a No. 1; the Tanner data point is the 2020 season, 40–60 lb fish, small hook getting bit better regardless of bait size, `shZCjX2-fkI`) versus **step the line up when the grade is up** (100 lb called easier than 30 lb for the bigger fish being seen, `nQvJnfb5jQ4`) — with the cost of the light option recorded: about six hooked, one landed, on 40 lb with a tiny circle during a Sundowner bite on the better grade (`nQvJnfb5jQ4`). Briefing standard is **circles for bluefin, J hooks for yellowtail** (`UfuiWFVvz2E`), against one crew's stated J-hook preference on a finicky bluefin bite (`LsFMBCa9DOQ`).

**Distribution can be unlike anything inshore** — driving through **20 to 30 miles of fish**, a boat 15 miles away seeing the same, against the usual isolated 4–5 sq mi patch (`LsFMBCa9DOQ`). And fish take their time getting onto the bank: a school held outside for close to a week, ~10–14 days elapsed before pushing in close enough to anchor directly on the structure (`eL1Qm33-Mj0`).

**Also out there:** resident 20–40 lb "Home Guard" yellowtail at anchor over the high spot, "giant" bonito, deep hard-bottom reds/lingcod/big ocean whitefish on the bank edge when the pelagic bags fill or the current dies.

**Regs, US / California / CDFW, checked as of 2026-08 — verify current before you fish.** Bag limit **two Pacific bluefin per person per day** (`usHl-4SfqDA`, as of 2024-11). And a real one for this destination: the corpus names the **Cow Cod Conservation Area** as an offshore closure but gives no boundary, so **whether either bank falls inside it is unverified — check the CCCA boundary against your position with CDFW/NOAA before you drop**. Compliance is positional, not depth-based.

---

## The in-envelope alternative for this weekend

`planning/day-plan-protocol.md` says if nothing in the envelope fits, say so and stop rather than substitute out of region. This stays in `socal-bight` and in your stated home waters ("San Diego offshore banks"), so it's a legal offer — but I'm giving you the KB's honest coverage on it, not a sales pitch.

**The 43** (32°39.333'N 117°58.417'W) at your 68.2 °F: **34.9 nm from the Point Loma Pipe, 31.2 nm from Widow Rock off La Jolla, 21.5 nm from Pyramid Head** (`locations/43.md`, cameron). That's roughly a third of the Cortez run, with a bail-out line to the beach the whole way — which is the thing your Saturday noon wind build actually needs.

- It's the shallowest numbered bank in the Bight grid, a **43-fathom (~258 ft) crest**, the corpus's worked example of a bank as "a mountain in a desert" where bait congregates for safety and the big fish follow (`Rf1HKJG-SDg`). Since the rockfish closure, "everyone goes to the 43" for giant bluefin instead.
- **Honest caveats:** the KB's bluefin window for that box is **June–July**, and it names **no August source** at the 43. It's a **search box**, not a spot-check — the below-Clemente complex reads as one **~50–60 sq mi** area; plan hours of looking, run bank to bank for color changes, temperature changes and bird life, and if a piece of water reads fishier, be back in it on a **late-morning slack after 09:30** (`Blh2BA-7Ono`). Expect to spend the day driving around.
- **Also worth checking before you write off the inside:** the Catalina Eddy shielding rule — the islands shadow the water behind them from the prevailing north wind, and marks well south still sit in that shadow (the 425 is often shielded despite being far south of San Clemente; cameron, `S2L3KLSQ6Is`). On a NW-wind weekend that's the lee to check.
- Paddy program peaks in August, and the best paddy water is south of SCI/Catalina and Dana Point–Oceanside southward (`HzE4FHHcvTk`) — the one on-the-water trip aimed at the 43 caught its bluefin **on a paddy, not on the bank**, keyed on anchovies, glassing white terns; they fished from about **100 yards off** the kelp because the tuna sit outside the piece, watching the full 360° (`A6DJoXbID4c`).

**Two transit tools for whatever you run:** watch the boat's water-temp gauge directly while running and note when it changes — a manual backstop for a break the satellite map missed — and use the Garmin 840xs's buoy overlay for live wave height/period rather than trusting the point forecast (`planning/electronics-and-sounder.md`, cameron).

## What would flip Tanner/Cortez to a go

1. Your **range_nm** and **sea_state_max_ft**, on paper, clearing a 110 nm open-ocean run with reserve.
2. A swell **period well over 10 s**, and wind under ~12 kt across the *whole* window including the return — not a dawn lull inside a 15–20 kt night.
3. A **kite + flying-fish harness**, or the **300–500 g jig setup**, actually in the boat — otherwise you've made the corpus's longest run to fish the one program (flyline/yo-yo at anchor) you can also fish 70 miles closer.
4. Ideally not the full-moon peak night, given the "peak day is travel, morning after is slow, fish it late" doctrine — and "fish it late" doesn't work when the wind builds at noon.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/trip-length-selection.md`, `planning/electronics-and-sounder.md`, `planning/search-and-glassing.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `seasonal/august.md`, `seasonal/september.md`, `species/bluefin-tuna.md`, `species/bluefin-tuna-trolling.md`, `species/evidence/bluefin-tuna.md`, `techniques/kite-fishing.md`, `locations/tanner-bank.md`, `locations/cortes-bank.md`, `locations/evidence/tanner-bank.md`, `locations/43.md`, `locations/43-91-300.md`, `locations/regions.md`, `profiles/cameron/README.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/trolling-lures.md`, `profiles/cameron/spots.md`  
*videos:* `NC3-3pJDEgo`, `zKmZ4zql2ws`, `DnSqw4r7A1s`, `S2L3KLSQ6Is`, `QSvzVHW9UMk`, `UfuiWFVvz2E`, `fDSd9kqwYW0`, `nQvJnfb5jQ4`, `ntQXxcH5sjI`, `947solNfiPw`, `LsFMBCa9DOQ`, `vCskOx6N-XM`, `zBd1mayUt_I`, `i3qIAHW-SJc`, `OYOda6T3f-8`, `eL1Qm33-Mj0`, `Y1xeieQI3B4`, `shZCjX2-fkI`, `XLVUhV8DW64`, `fri_BWI-VA0`, `LEiyB9QNzHY`, `Blh2BA-7Ono`, `CMQkHQMxbXM`, `HzE4FHHcvTk`, `5to3Q5P7w90`, `HWx1jDTGsng`, `z1CmWHqe9uk`, `YsiHziY_PWw`, `2y0VznL2qk8`, `Rf1HKJG-SDg`, `usHl-4SfqDA`, `yMiBtZ7k8-w`, `A6DJoXbID4c`, `h3PTupup17I`, `c3NFkQbdDy0`  
*gaps admitted:* Cameron's boat envelope is unset: profiles/cameron/boat.md has range_nm, sea_state_max_ft and home_port all null, and instructs the protocol to ASK rather than assume — so a 110 nm offshore-bank run cannot be cleared at step 1b. | No fuel capacity, burn rate, or range figure for the Panga Marquesas 22 anywhere in the KB, so I cannot compute whether a Mission Bay → Cortez → Mission Bay run is possible. | locations/tanner-bank.md carries a flagged gap: no corpus source states a run from Dana Point, Oceanside or any Orange County / small-boat port to Tanner or Cortez, and no fuel figure or sea-state envelope for the crossing itself. | locations/tanner-bank.md carries a flagged gap: no corpus source states a wind or swell number that turns the Tanner/Cortez zone off — the go/no-go had to come from the general conditions/sea-state.md layer. | The KB has no content on lunar eclipses at all — no note addresses an eclipse's effect on a bite, so the partial lunar eclipse on 2026-08-28 could not be interpreted. | The KB has no numeric chlorophyll scale (no mg/m3 values anywhere), so 'chlorophyll 0.3 offshore' cannot be graded as clean/green/productive — the layer is only qualitative (bloom age, edge vs. mass). | No zone guide exists for bluefin at Cortez/Tanner — species/bluefin-tuna.md carries it as a flagged stub with material parked in the evidence file. | No corpus source names a rock, pinnacle, sub-feature, preferred direction, bottom composition or relief profile at either Tanner or Cortez, so approach and start-point detail is unavailable. | Whether Tanner or Cortez falls inside the Cow Cod Conservation Area is unverified — the corpus names the closure but gives no boundary. | No corpus source dates an August session at the 43, and no source gives run distance, bearing, run time or fuel to that bank from any port; its bluefin window in the KB is June–July only. | No anchoring gear, ground tackle or anchoring procedure for Cameron's boat exists in the profile, though the Tanner/Cortez program is an anchor-and-chum program in 15–25 fathoms. | Cameron owns no kite, no flying-fish harness, and no 250–500 g knife/flat-fall jigs or SPJ rod — the two highest-percentage programs at these banks are inventory gaps, named rather than substituted. | Tide and slack times for 2026-08-28/29 were not supplied and the KB holds no tide tables, so the current/slack gating on the bank program could not be timed. | Cameron's Tranx setup braid weight is unrecorded (respool pending), so that setup could not be resolved to a line class.

</details>

### 5. [trip] Can I fish for cabrilla out of San Diego this weekend in mid-September? Where would I go?

**Winner:** B3 · mapping {'A': 'NOW', 'B': 'B2', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |

**Judge:** All three correctly refuse the trip and none bluffs or fabricates, so the separation is on the second half of the question — 'where would I go'. C is the only answer that delivers the whole chain: the region gate with the KB's own failure case, three real access routes with drive legs, trip shape, per-person cost, FMM/CONAPESCA/insurance stamped with jurisdiction and as-of, the full through-the-day depth-and-lure ladder, and a calico fallback whose two regulatory figures each carry their own date (including a flag that the 2019 bag limit is stale). B has the best execution table and the only profile-resolved gear and bait plan, but never tells you how to get to the Cortez at all and leaves the Coronados recommendation without the Mexican paperwork it admits the KB lacks. A is the sharpest on September timing and uniquely audits its own cabrilla note for bad attributions, but hands the angler no gear or retrieve to actually fish cabrilla with.

- *B2 reasons:* found: locates the cabrilla note and the Cedros grouper mention, but answers 'where would I go' only as a place name — no route, cost, or access shape for the Cortez. specific: the best execution table in the set (30-40 ft rise, 60-80 ft by 9-10 am, 80-150 ft midday, burn 30-40 cranks, bites in 5-10), plus 69 F to 71-72 F at 7-13 nm, 100 ft sabiki on 8 oz, VHF 11. sourced: consistent note paths and ids (EmZO8QiOfik, Rwy4MqeXCIU, uyjTdgIw-1k, ldVj0BoB-kE). scoped: region call is right and calico 14 in / rockfish season carry CDFW + as-of 2026-08 + verify, but it frames cabrilla by prose header rather than region fields, repeats a sand-bass 14 in limit without its own jurisdiction/as-of/verify, and has no Mexican-waters paperwork for the Coronados it recommends (admitted as a gap). honest: explicitly says 'no' means the KB has no basis, not that fish are absent; refuses to invent conditions; frank gap list including missing swimbaits in the profile. actionable: highest — profile-resolved boat, rods and reels, bait-barge timing, per-presentation calico plan.
- *B3 reasons:* found: answers both halves — gate refusal quoting the KB's own named failure case, then three documented ways into the fishery (BOLA drive-in, San Felipe mothership, Loreto fly-in via CBX) plus the September read. specific: 4-day/2-fishing-day trip shape at $800-1,000 pp, panga $550/day + $100 tip, hotel $90-120, Baja Bound ~$90-130, 04:30 wake/05:30 depart, full depth ladder 30-40 / 60-80 / 80-150 ft, 7'10"-8 ft ~50 lb, 6.5:1-7:1, 65/50 and 80/80, 12-15 lb grade, calico 0-8 and 20-100 ft, 65-68 F. sourced: dense and plausible pairing of paths and ids (P36VGPPf120, odiIWmut6gM, 8IRONtdkceM, ts9rJgxjmSg, n4nMCLLW3tY, LqW32NSkObY, r6j5w40fVHI). scoped: cortez-north/south vs socal-bight explicit, Mexico INM/CONAPESCA stamped as-of 2026-08-06 + verify, calico 14 in as-of 2022-04-25 and 5-fish bag as-of 2019-03-13 with the age of the oldest figure flagged for re-check. honest: no conditions and no profile stated up front, says which structure notes it did not open, warns Loreto season data is thin and the paperwork detail is single-sourced. actionable: the only answer from which you could both plan/book the cabrilla trip and execute the program, with a fishable local calico fallback.
- *NOW reasons:* found: nails the region gate on cabrilla, names the Cortez access zones, and answers the mid-September timing question directly. specific: leg-by-leg drive times, 11-hour door-to-door, 1-1.5 in fall bait, 71.6 F paddy, 15-25 lb YFT grade, 18-20 ft reef drift. sourced: note paths plus video ids (P36VGPPf120, T3cEQUqiH8E, EmZO8QiOfik, 5to3Q5P7w90) throughout. scoped: cortez vs socal-bight handled correctly, Coronados flagged as Mexican water, Mexico INM/CONAPESCA and CDFW rockfish both carry as-of 2026-08 + verify. honest: best-in-set on flagging contested content in its own cabrilla note (misattributed zones, unsupported 40-60 lb rod class), states no conditions pulled, long concrete gap list. actionable: strong on when-to-go-instead and on the local calico rig, but gives almost no cabrilla execution (no depth ladder, no reel ratio/line spec, no drag doctrine), so the trip it redirects you to can't be fished from this answer.

<details><summary>Full prompt</summary>

Can I fish for cabrilla out of San Diego this weekend in mid-September? Where would I go?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short answer: not out of San Diego — cabrilla in this KB is a Baja fish

Per [`species/cabrilla.md`](species/cabrilla.md), cabrilla (leopard grouper) is documented here as a **Sea of Cortez / Bahía de los Ángeles (BOLA) panga fishery** — the whole note is framed "Region: Baja — Sea of Cortez / Bay of LA (BOLA), panga fishery," sourced to a single dedicated cabrilla breakdown (Cesar, 25+ yr Sea of Cortez cabrilla angler, via Dirty Hookers, `EmZO8QiOfik`, 2025-03-04; `confidence: medium`). There is **no cabrilla record anywhere in the KB for San Diego, the Coronados, or the SoCal Bight** — the only other Pacific-side grouper/cabrilla mention is **Cedros Island, Baja** (~188 miles down from San Diego by the crew's own transit numbers in [`species/calico-bass.md`](species/calico-bass.md)), and there local operators adopted a **voluntary 100% catch-and-release** on calico, grouper (cabrilla) and black seabass because summer spawning-aggregation pressure had collapsed the catch (Jose via StokedOnFishing, `ldVj0BoB-kE` / re-cut of the same interview in `Zo92MG459gQ` — operator agreement, not a government rule; verify current status before fishing).

So: **a Saturday/Sunday out of Mission Bay is not a cabrilla trip.** A real cabrilla day in this KB is a Sea of Cortez / BOLA panga trip — which, if you're Cameron, is already on the books: [`profiles/cameron/spots.md`](profiles/cameron/spots.md) records "next BOLA trip September 2026."

---

## If this is prep for that BOLA/Cortez trip

From [`species/cabrilla.md`](species/cabrilla.md) (all `EmZO8QiOfik`) — the day is structured by sun angle, and the fish move down the column through it:

| Time | Depth | Program |
| --- | --- | --- |
| Low light, early/late | Fish rise **30–40 ft** to eat on the surface | **170-size jerkbait** cast tight to visible shoreline rock ([`lures/jerkbaits.md`](lures/jerkbaits.md)); white, bright *or* dark all get bit |
| Sun up | Shallow-to-mid, off the tightest rock | Drop to **150-size** (or Mag Minnow class), switch to bright/metallic/flashy; work toward the **"dark spot"** — a dark patch off the visible rocks that is submerged rock, and holds the **bigger** fish once the sun is up |
| ~9–10 am on | **60–80 ft** | **Yo-yo iron** — Salas 6X, 6X Jr, 60 g jig paras or Krocodile; cast, hit bottom, **burn it straight back to the boat** (not a hop-on-bottom rockfish retrieve) ([`techniques/yo-yo-iron.md`](techniques/yo-yo-iron.md)) |
| ~11 am–3 pm | **80–150 ft** | Heavier iron — Salas 6X, Tady 40, or 7X class; burn **30–40 cranks** off the bottom, let it settle back, repeat — bites usually come **within 5–10 cranks** of picking it back up |

Structure rule: target **"snaggy," not sandy** — bull rocks, pinnacles, boulder slides; a **boiler rock** is the easiest visual target, and bottom **color changes** tell you reef vs. sand vs. submerged boiler. With two anglers, **split the cast** — one at the visible shoreline rock, one parallel to the submerged rock further out.

Two notes on timing for a September trip specifically: the **micro-bait window is fall into winter, roughly October on**, when Cortez baitfish shrink to **1–1.5 in** and you downsize both programs — mid-September is *ahead* of that, so run the standard sizes and keep the downsize as the slow-bite fallback.

Gear ([`species/cabrilla.md`](species/cabrilla.md), [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)): two jerkbait rods side by side, medium-light + medium-heavy, **7'10"–8 ft, ~50 lb class**, "a crankbait rod on steroids"; **low-profile level-wind at 6.5:1–7:1+** because the program is **2–3 casts/min** all day; light outfit **65 lb braid → 50 lb mono top shot**, heavy outfit **80 lb braid → 80 lb leader**. Bring a **spare 300 yd braid spool** — cast volume wears braid through the guides. Drag doctrine is an unresolved conflict kept side by side: **Cesar runs the star drag locked to its stop** paired with a slower-bending rod as the shock absorber; **Ray Sharifi backs the drag off** and runs a faster-action rod. Both are attributed philosophies for the same fishery — the choice turns on which component you want absorbing the strike, not on which is "right."

---

## What is actually fishable out of Mission Bay this weekend

I have **no conditions for this weekend** — you didn't give me any and I'm not allowed to invent them. Step 1 of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) is to pull **BightSST per spot and along the transit route — observed *and* forecast SST, chlorophyll, wind/swell/current** (read endpoints are open, expect 30–60 s Render cold starts), and to **distrust single-source SST extremes** and cross-check models. Everything below is the priors layer, which weights zones *before* you do that.

**The closest thing to a cabrilla day that exists here is calico bass.** That isn't a hand-wave: the KB's own Sea of Cortez source describes the wolf-pack grouper and cabrilla they caught on rocky points as behaving **"just like calicoes"** (StokedOnFishing, `A6s-A1NARuA`, Gonzaga Bay), and [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) files the cabrilla jerkbait build under the same "close-structure cabrilla/calico-style casting application." Same idea — a structure-ambush fish pulled off rock with a fast reaction retrieve.

The calico program ([`species/calico-bass.md`](species/calico-bass.md), [`locations/bass-structure.md`](locations/bass-structure.md)) — kelp beds, reef, boiler rocks, breakwalls and island structure from the coast out:

- **Current, not tide, is the switch.** Calico are current-driven and largely tide-indifferent. Current running **parallel** to the structure makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage, skip it.
- **The edge is the spot** — the biting fish sit on the **up-current / leading edge**; they face into the current and ambush from the front (Benny Florentino, `Rwy4MqeXCIU`). Hit three or four sides of a kelp head and you know in two or three casts.
- **Read the current off the kelp itself:** pulled **20 ft under** = raging, surface presentations dead, go subsurface; **laid down** = strong; **resurfacing** = slacking, go back on top.
- **Covering water is the method:** 10–25 casts to the prime edge, then move 100 ft or 100 yards. Beds re-bite — come back later.
- **On the meter:** calico mark tight to kelp/structure edges and hard bottom; working depths run the **outside kelp edge ~50 ft in to ~25 ft**, and they'll rise **10–15 ft off 80–100 ft of reef** to eat a crankbait or sunk iron. A solid unbroken bait wall usually has no predators on it; broken, harried bait does.
- **Moon caveat:** on a clear full moon they gorge at night and **shut down by mid-morning** — bite first light, then dead until late day. Check the phase before you pick a departure time.
- **Birds:** cormorants diving *in* the kelp is the calico tell, better than gulls inshore.
- **Presentations:** weedless **7" slug on a 3/8–3/4 oz keel-weighted spring hook** on short targeted casts to individual stringers, fast steady wind, pause on the eat; an **open slug** bombed and skittered with a 1-2-3 pause to call fish off the stringers; **surface iron** ground along the kelp line for bigger cruising fish with current up; **flylined** sardine/mackerel when they're deeper on the edge or it's windy; **chum-and-anchor** — chum the spot, reposition up-current, back down onto it as the anchor sets, fish come out of the kelp as it goes down (`RXNebDr4j7s`).
- **Gear class:** 7–9 ft **graphite-composite bass class**, 200–300 size reel, **30–65 lb braid**, heavy **40–65 lb fluoro** leader for kelp abrasion; **jig-stick class** for the surface iron.
- **Legal:** calico (kelp bass) minimum **14 in** — California/CDFW, as of 2026-08, `r6j5w40fVHI`. **Verify current regs before you go.**

**Sand bass** mix into the same water — one North County San Diego session near Camp Pendleton found them mixed with calico on hard bottom with kelp not reaching the surface at **~40–42 ft**, same 14 in size limit (`HMdrP4-i9MM`, 2022-10-11) — but note their event is the **early-summer spawn on the flats (late June–July)**, so mid-September is off that peak ([`species/sand-bass.md`](species/sand-bass.md)).

**Offshore, if the water's right and the boat's up for it** — mid-September is the **late warm-stable regime** ([`seasonal/september.md`](seasonal/september.md)):

- **Dorado** are the most San Diego-friendly offshore target: **~15 mi off San Diego** is the typical big-concentration zone (`E4vKwRaRueA`), though by the late warm-stable phase (September) they're described as **open-water schools below/backside Catalina** (`5to3Q5P7w90`). They ride the **cold-green-on-the-beach / warm-blue-offshore boundary**, reference band **~71–72 °F** (71.6 °F on a productive paddy). A Mission Bay run once read exactly that: **69 °F near the harbor climbing to 71–72 °F at roughly 7–13 nm** (`uyjTdgIw-1k`). Structure is **kelp paddies** — and the best paddy water is **south of Clemente/Catalina and the Dana Point–Oceanside-and-south coastal strip** ([`locations/bight-geography.md`](locations/bight-geography.md)), which is your water.
- **Yellowfin** — the September prior is **volume near the border sliding north with the warm water**; the search rule is **warmest water crossed against your chlorophyll chart for the cleanest** (SST-max × chlorophyll-min) ([`species/yellowfin-tuna.md`](species/yellowfin-tuna.md)).
- **Bluefin grade** sits in the **"volume square" — Santa Barbara Island / San Nicolas / Clemente / Catalina** in September ([`seasonal/september.md`](seasonal/september.md), [`locations/zone-lexicon.md`](locations/zone-lexicon.md)). That's a long way north of Mission Bay and is a region to work through for hours, not a spot to check.
- **Yellowtail** on **La Jolla and the SD offshore banks** is real but the KB calls it **strongest warming-transition into warm-stable (spring–summer)**, so mid-September is past that peak; **coastal kelps LA to San Diego** hold kelp-line yellows in the warm-stable regime, surface iron along the edge being the classic ([`species/yellowtail.md`](species/yellowtail.md)). The **Coronados** are the nearest island structure — **~13 mi from San Diego, off Mexico**, "synonymous with yellowtail" (`D5DR7Kx42_A`) — but they run **"seeing-not-biting" cycles with narrow daily windows** (`YZtX1MiT0y8`); anchor those days to tide and current, not the clock. If you're marking fish on the hard bottom / pinnacles at **~5–10 fathoms**, that's the **yo-yo iron** row: heavy full-size iron (Salas 6X class), hit bottom, **a couple cranks off the bottom is the reaction bite**, or a dropper loop to the same marks.
- **Rockfish** is open (the recreational season closes year-end, CDFW, as of 2026-08 — verify current dates and depth limits). Out of San Diego that's the **deep 300–900 ft** banks and coastal deep rock for reds/vermilion; the shallow **100–250 ft island variety day — blue bass, bocaccio, lings on one rock — is a Channel Islands thing you do not get in San Diego** (`6-8KfjEg0x8`) ([`species/rockfish-lingcod.md`](species/rockfish-lingcod.md)).

**Bait** ([`bait/making-bait.md`](bait/making-bait.md)): buy sardines at the barge when available, or make mackerel on a sabiki — the Coronados, or **La Jolla during shortages** — dropped to **~100 ft on an 8 oz sinker** (five 12-inch mackerel on one drop is the benchmark, `cameron`). If you're buying, **avoid the 6:00 am rush** when every 3/4- and half-day boat loads; go **5:00 or 7:00 am**, hail the barge on **VHF 11**, and ask for it loaded light (`7WapaxdtjQg`).

**Boat and gear resolution** (against [`profiles/cameron/`](profiles/cameron/), the only profile in the KB — say so if this isn't your profile and I'll drop to class terms): Panga Marine Marquesas 22, single 115 hp Yamaha, **tops ~35 kt**, launches Dana Landing, normal departure **~8 am**, no trim tabs, 30-gal bait tank, 100–125 lb ice. For the structure program you already own the pieces: the **Torium 20HG on the Phenix Abyss 10' 25–60 lb / 50 lb braid** is the surface-iron setup, and the **Trinidad 40 on the 8'0" XH 40–80 lb / 80 lb braid** with the owned **Salas 6X** is the yo-yo setup. The **Lexa 400 (Okuma PCH 9'0" H, 20–60 lb, 50 braid)** or the **Tranx (Phenix M1 Inshore 8'2" H, 20–45 lb)** is the closest thing you have to the 7–9 ft bass-class casting rod the calico program wants.

---

## Bottom line

Fish **structure out of Mission Bay this weekend** — coastal kelp and reef for calico (and mixed sand bass), with the Coronados as the island option if the water and the Mexican paperwork are sorted, and dorado on the 71–72 °F break at 7–15 mi if BightSST says the warm blue water is in reach. Save the cabrilla program for the BOLA trip, where the KB actually has doctrine for it. Pull the BightSST numbers before you commit to a zone — none of the above is today's water.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/cabrilla.md`, `species/calico-bass.md`, `species/sand-bass.md`, `species/yellowtail.md`, `species/dorado.md`, `species/yellowfin-tuna.md`, `species/rockfish-lingcod.md`, `seasonal/september.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `locations/bass-structure.md`, `techniques/yo-yo-iron.md`, `tackle/rod-and-reel-selection.md`, `lures/jerkbaits.md`, `lures/iron-jigs.md`, `bait/making-bait.md`, `profiles/cameron/boat.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`  
*videos:* `EmZO8QiOfik`, `A6s-A1NARuA`, `ldVj0BoB-kE`, `Zo92MG459gQ`, `E4vKwRaRueA`, `5to3Q5P7w90`, `uyjTdgIw-1k`, `D5DR7Kx42_A`, `YZtX1MiT0y8`, `r6j5w40fVHI`, `Rwy4MqeXCIU`, `RXNebDr4j7s`, `HMdrP4-i9MM`, `6-8KfjEg0x8`, `7WapaxdtjQg`, `kwMIgkCtFUE`, `0KQ--N5TjqE`  
*gaps admitted:* The KB never states cabrilla's northern range limit or whether leopard grouper occur off San Diego at all — it only ever documents them as a Sea of Cortez / Bay of LA (and, as 'grouper/cabrilla', Cedros Island) fishery, so 'no' here means 'the KB has no basis for it', not 'the KB says they are absent'. | No cabrilla regulations of any kind (Mexican or CDFW) are in the KB — no season, size, bag limit, or jurisdiction stamp. | The KB has no coverage of Mexican fishing licences, tourist permits, or the paperwork needed to fish the Coronado Islands or Mexican waters out of San Diego (it only mentions in passing that a Cedros charter obtained permits in Tijuana). | No conditions were supplied for this weekend and the KB holds no live data — SST, chlorophyll, wind, swell, current, tide and moon phase for 2026-09-12/13 all have to come from BightSST, which I cannot call. | The September priors note carries no coastal calico/sand-bass entry — its lineup is offshore (bluefin volume square, dorado below Catalina, yellowfin sliding north) plus BOLA bottom yellowtail, so the mid-September inshore-structure read is inferred from the calico note's year-round/warm-months framing rather than a September-specific source. | The KB names no specific calico or rockfish spots for the San Diego area — locations/ holds universal structure knowledge only, and the calico note's 'where' list does not name the Coronados or La Jolla. | Cameron's tackle profile lists only hard baits, irons and jigs — it records no soft-plastic swimbaits, weedless slugs, keel-weighted spring hooks or leadheads, which is what the calico program calls for; and no jerkbaits in the 150/170 sizes the cabrilla program uses. | Two micro-lure names in the cabrilla source's fall/winter downsizing program could not be reconstructed from the captions (logged asr-uncertain in the note), so that lineup is incomplete. | The KB gives no sonar/arc signature for cabrilla specifically — only the visual structure and 'dark spot' read. | No transit distance or run time is recorded from Mission Bay to the September bluefin 'volume square', so I cannot say whether it is inside the Marquesas 22's practical day range.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Short answer: no — not out of San Diego. Cabrilla are a Sea of Cortez fish.

Cabrilla (leopard grouper) is region-gated in this KB to `regions: [cortez-north, cortez-south]` — the Sea of Cortez, both sides of the 28°N state line (`species/cabrilla.md`, `locations/regions.md`). A weekend day out of San Diego is a `socal-bight` envelope, and under step 1b of `planning/day-plan-protocol.md` a note whose `regions` doesn't contain the day's region is **never offered** — not ranked lower, not offered with a caveat.

This is not me being pedantic. Your exact question is the named failure case the protocol was written to stop:

> "…a day plan for a Mission Bay jetty could route to cabrilla, whose situation table opens with 'low light, tight to shoreline structure → jerkbaits, cast tight to the rock.' That reads perfectly for a SoCal jetty at dawn. The fish is 400 miles away." — `locations/regions.md`, echoed in `planning/day-plan-protocol.md`

So: this weekend (Sept 12–13, 2026) out of San Diego, cabrilla is off the table. Below is (A) where cabrilla actually live and what it takes to get on them, and (B) what the KB says to do instead if you're staying home this weekend.

---

## A. Where you'd actually go for cabrilla — and why it isn't a weekend

The KB documents three ways into the Sea of Cortez cabrilla fishery (`locations/sea-of-cortez.md`), and none of them is a two-day trip out of San Diego.

**1. Bahía de los Ángeles (BOLA) — the drive-in day-panga fishery** (`locations/bahia-de-los-angeles.md`, `cortez-north`)

- **~8 hours' drive from San Diego** without stops, 9–10 h at a relaxed pace: SD → Calexico 1.5–2 h, Calexico → San Felipe 2 h, San Felipe → Gonzaga Bay 2 h, Gonzaga → BOLA 2 h. One crew's real door-to-door was 06:30 to 17:31 — an **11-hour travel day** (`T3cEQUqiH8E`). It's all paved (`wX7jUycIJ-U`).
- **The documented trip shape is 4 days** — 4 days of driving/travel, 3 nights, **2 fishing days** — at **$800–1,000 per person all in** (~$250/day) splitting shared costs across a group of 13. **Panga $550/day plus ~$100 tip.** Hotel (Costa del Sol) ~$90–120/night (`P36VGPPf120`).
- **Paperwork (Mexico — INM for entry, CONAPESCA for fishing; as reported 2026-08-06 — verify current before you travel, this is a foreign jurisdiction):** FMM tourist permit filled out online and **printed**, Mexican fishing licence bought online (new website as of 2026 — search fresh, don't trust an old bookmark), passport. Vehicle insurance is separate and mandatory in practice — **Baja Bound** named; ~$90 for a 2021 car, ~$130 for a newer Tacoma on a 4-day.
- **No cell service** through the desert, at Gonzaga or at Bahía. Travel in a group, **minimum two vehicles**. Buy all tackle and food before you cross — prices run roughly double past the border, and "there's no tackle shop to really speak of" (`odiIWmut6gM`).
- **Day shape:** wake ~04:30, depart 05:30, boat picks you up in front of the hotel. One captain's stated day-order is **cabrilla first thing, then move after roughly two hours for yellowtail and snapper** (`odiIWmut6gM`). Cabrilla and yellowtail sit in different areas — you pick a target for the day.

**2. San Felipe mothership (Tony Reyes-style)** — **a week to ten days** aboard a live-aboard carrying pangas, relocating overnight (one relocation was an 8–9 hour run, `aT-fL7vaavY`). Categorically not a weekend, and weather governs it — one crossing ran 12–15 ft rollers and the pangas stayed on deck (`locations/sea-of-cortez.md`).

**3. Loreto / Puerto Escondido** (`locations/loreto.md`, `cortez-south`) — **the only fly-in option in the KB**: one documented trip flew out of **CBX** (the San Diego–Tijuana airport bridge) rather than driving (`ikiXx9sUsoA`). Cabrilla there come **shallow, 5–10 ft, on a suspending jerkbait**, off islands like Isla Monserrat ("Monserrat north end is the best") and Six Mile Reef (`n4nMCLLW3tY`). The KB gives no flight times, frequency, or cost for CBX→Loreto, so I can't tell you whether that compresses into a weekend.

### What mid-September means for a cabrilla trip

The cabrilla note itself gives **no month-by-month location pattern** — only a bait-driven shift: **fall into winter, roughly October on**, Sea of Cortez baitfish shrink to about **1–1.5 in** and cabrilla key hard on that micro-bait, so you downsize both the jerkbait and iron programs (`species/cabrilla.md`, `EmZO8QiOfik`). Mid-September sits just ahead of that window; downsizing is still the reliable slow-bite fallback any time.

The BOLA seasonal table (`P36VGPPf120`, unregistered channel — medium confidence, and the hosts say outright they can't give "a hard fast answer") reads **July on: "everything starts to go down," water heats and fish drop out of the surface program**, with **August–October the late-season play for dorado, marlin, sailfish and occasionally tuna**. Prime is May–June. Cameron's own September BOLA program is consistent: the fish are **on the bottom**, worked with **dropper loops and yo-yo iron** (`seasonal/september.md`). Treat the table as a prior, not a forecast — the 2026 season ran against the pattern.

### The cabrilla program itself, when you do go (`species/cabrilla.md`, `lures/jerkbaits.md`, `EmZO8QiOfik`)

- **Structure is everything — target "snaggy," not sandy.** Boiler rocks (rock showing itself at the surface), pinnacles, boulder slides. Read bottom color changes. Once the sun is up, the **"dark spot"** — a dark patch a little off the visible rock — is submerged structure and holds the **bigger fish**.
- **Depth moves through the day:** fish rise **30–40 ft** to eat a surface-fished jerkbait early; by ~9–10 am they're at **60–80 ft**; by 11 am–3 pm the bigger fish are **80–150 ft**.
- **Low light, tight to shoreline rock:** jerkbait, **170 size** (Yo-Zuri Hydro Minnow LC runs 1–3 ft; Current Sniper 5–7 ft, 170 only). After ~9–10 am drop to **150** or the Mag Minnow, brighter/metallic colors.
- **Mid-morning on:** yo-yo iron — Salas 6X, 6X Jr, 60 g jig paras, Krocodile — cast, hit bottom, then **burn it straight back**, not a hop-on-bottom rockfish retrieve. Midday: heavier iron (6X, Tady 40, 7X class), **burn 30–40 cranks off the bottom, settle back, repeat — bites usually come within 5–10 cranks** of picking it up.
- **Gear class:** two jerkbait rods side by side, medium-light and medium-heavy, **7'10"–8 ft, ~50 lb class** ("a crankbait rod on steroids"); **low-profile levelwind at 6.5:1–7:1** because the program is ~2–3 casts/min; **65 lb braid to 50 lb mono top shot** on the lighter outfit, **80 braid to 80 lb leader** on the heavier. Yo-yo: stout 40–60 lb class, high-speed reel. Bring a spare 300 yd braid spool.
- **80 lb is about the rocks, not the fish** — fish get taken in **six feet of water** there: "I see now why we fish 80 — I think we would have lost a lot of them already" (`8IRONtdkceM`). Grade ran **12–15 lb** on that trip.
- **A pause placed next to the rock is the trigger:** "when I get really close to a rock with a jerkbait I'll go, and then pause for a half second… and on that pause they just launch out of the water for it" (`ts9rJgxjmSg`).
- **Doctrine kept side by side, unreconciled:** Cesar fishes the jerkbait drag **locked down** with a slower, softer rod to absorb the shock; Ray Sharifi fishes the drag **backed off** with a faster-action rod. The choice turns on which end absorbs the strike — rod or drag — not on which is "right."

---

## B. If you're fishing out of San Diego this weekend instead

The in-region equivalent is **calico bass** (`species/calico-bass.md` — `regions: [socal-bight, baja-pacific-north, baja-pacific-south]`, `waters: [nearshore-coast, island, bay-harbor]`, confidence high). The KB makes the connection itself: one angler's summary of the Sea of Cortez rock program was *"this is literally calico fishing on steroids"* (`locations/sea-of-cortez.md`, `8IRONtdkceM`). Same structure-ambush read, same cast-and-wind at boiler rock — smaller fish, lighter line, no border.

**Where:** kelp beds, reef, boiler rocks, breakwalls/jetties and island structure from the coast out to Catalina, Clemente and the Channel Islands. Fish the **edges and pinch-points** — leading edge, outside edge, isolated stringers off the main bed — not the dense middle (`locations/bass-structure.md`, `locations/breakwalls-jetties-riprap.md`, `locations/island-structure.md` are the structure notes; I did not open them beyond the router's summary).

**When, on the day:** an hour before sunrise into early morning, and the hour before sunset — cited as the window that decides a large share of SoCal bass-tournament wins (n6yun panel, `RUuPNpK0x-s`, unregistered — medium). Bright stable light pushes fish up into the **outer canopy edge**; overcast spreads them through the column.

**The governing read is current, not tide:** current running **parallel** to the shoreline makes the edge fishable; **into** the beach is marginal; **off** the beach is garbage — skip it (`conditions/current-structure.md` via the router).

**Depths and temp:** most commonly worked **0–8 ft and 20–100 ft**, occasionally past 100; a stated personal-observation preference of **65–68 °F**, with fish going lethargic past ~70 (Tommy Ponce, Dana Point, `LqW32NSkObY`, 2019-03-13 — medium). Summer evening trips connect with calico staging to spawn in **40–60 ft over hard bottom** as light fades (`RUuPNpK0x-s`).

**Technique, closest to the cabrilla program you asked about:**
- Kelp bed, parallel current, fish tight to stringers → **weedless swimbait**, short targeted casts, fast steady wind, pause on the eat. 7" weedless slug on a **3/8–3/4 oz** keel-weighted spring hook; 7–8 ft graphite-composite bass class, 40–60 lb.
- Bigger cruising fish, current up → **surface iron** on a jig-stick class, steady grind along the kelp line.
- Sparse lanes, not committing → **inshore crankbaits** through the 80–100 ft lanes.
- Hunting a **7–10 lb** fish rather than numbers → step to **8–10 in** swimbaits on 65–80 lb braid; baits under ~5.5 in top out around 1–4 lb (n6yun Fred Hall panel, `ZoIzpyyS9xw`, 2013-03-09).

**Covering water is the method:** 10–25 casts to the prime edge of a bed, then move 100 ft or 100 yards. Beds re-bite — come back later.

**Regulations (California / CDFW — verify current before you fish):** calico minimum size **14 in** (as of 2022-04-25, `r6j5w40fVHI`); bag limit **5 per day** (as of 2019-03-13 — the oldest regulatory figure in the register, explicitly flagged to re-check) — `sources/regulatory-claims.md`.

---

## What I could not do for this plan

- **No conditions pull.** You didn't give me any, and I have no BightSST access here, so steps 1 and 2 of `planning/day-plan-protocol.md` (per-spot SST/chlorophyll, wind/swell/current, observed and forecast) are unrun. Everything above is the **priors layer only**. Give me the water and wind for Saturday and I'll weight zones properly.
- **No profile loaded**, so gear is in class terms per `tackle/gear-classes.md` rather than your own rods. If you tell me your boat's range and sea-state limit and what's in your rod locker, the recommendations sharpen and I'll name the gaps instead of substituting.
- **No San Diego spot pages exist in this version of the KB.** `locations/` holds universal structure knowledge only — bass structure, bays and harbors, breakwalls/jetties, island structure, the zone lexicon — with no Point Loma, La Jolla, or Coronado Islands page. The closest thing to a San Diego-area zone read is `locations/bight-geography.md` (`HzE4FHHcvTk`), which notes the Coronados, Catalina and San Clemente **held their water** through a big NW blow that rolled the northern Channel Islands and the LA/Ventura shelf down 5–8 °F, and that the best paddy water runs **south of Clemente/Catalina and along the coast from Dana Point to Oceanside and south**. That's zone-level weighting, not a place to put the boat.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `locations/regions.md`, `species/cabrilla.md`, `lures/jerkbaits.md`, `locations/bahia-de-los-angeles.md`, `locations/sea-of-cortez.md`, `locations/loreto.md`, `seasonal/september.md`, `species/calico-bass.md`, `species/README.md`, `locations/README.md`, `locations/bight-geography.md`, `sources/regulatory-claims.md`, `techniques/yo-yo-iron.md`  
*videos:* `EmZO8QiOfik`, `P36VGPPf120`, `T3cEQUqiH8E`, `6P34jI9q1tE`, `odiIWmut6gM`, `wX7jUycIJ-U`, `ojE5H6AdGGo`, `XRIjUgpuyZ8`, `8IRONtdkceM`, `ts9rJgxjmSg`, `ZYAILGyrkRk`, `4Dn7yChmhk0`, `aT-fL7vaavY`, `BSNGeduOHYM`, `n4nMCLLW3tY`, `ikiXx9sUsoA`, `5to3Q5P7w90`, `RUuPNpK0x-s`, `LqW32NSkObY`, `ZoIzpyyS9xw`, `r6j5w40fVHI`, `HzE4FHHcvTk`  
*gaps admitted:* No conditions were supplied and I have no BightSST access, so steps 1-2 of the day-plan protocol (per-spot SST/chlorophyll, wind/swell/current, observed and forecast) were not run — the answer is priors only. | No angler profile was supplied, so gear is given in class terms only; boat range, sea-state limit and owned rods are unknown. | The KB has no San Diego-area spot or zone pages — no Point Loma, La Jolla, Coronado Islands, or kelp-bed pages; locations/ holds universal structure knowledge only. | species/cabrilla.md carries no month-by-month seasonal/location pattern, so the KB cannot say whether mid-September is a good or bad cabrilla window at BOLA specifically — only the Oct+ micro-bait shift. | species/cabrilla.md carries a flagged stub: no sonar/meter signature for cabrilla exists in the corpus. | locations/loreto.md explicitly states season data is thin and warns against borrowing BOLA's calendar — there is no month-by-month Loreto calendar in the KB. | The KB gives no flight times, frequency, or cost for CBX to Loreto, so I cannot say whether a fly-in cabrilla trip compresses into a weekend. | No cabrilla bag limit, size limit, or Mexican-waters catch regulation appears in sources/regulatory-claims.md (only a Baja California Sur circle-hook rule and the voluntary Cedros catch-and-release agreement). | sources/regulatory-claims.md still lists Mexican licensing and entry requirements as a known gap, even though locations/bahia-de-los-angeles.md now carries FMM/licence/insurance detail from a single 2026-08-06 source — treat the paperwork detail as single-sourced and unverified. | The KB has no Coronado Islands note, so I cannot give a cabrilla-analogue structure plan for the closest island structure to San Diego. | seasonal/september.md covers the SoCal offshore lineup (bluefin volume square, dorado, yellowfin) and Cameron's BOLA bottom program, but says nothing about September inshore calico fishing specifically.

</details>

<details><summary><b>NOW — review</b> · 11/12</summary>

## Short answer: no — not out of San Diego, not at any time of year.

Cabrilla is a **Sea of Cortez fish**, and the knowledgebase gates it that way explicitly. [`species/cabrilla.md`](species/cabrilla.md) carries `regions: [cortez-north, cortez-south]` and `waters: [nearshore-coast, island]` — the leopard grouper of the Cortez, fished from pangas out of Bahía de los Ángeles and Loreto (`dEPuDrhoClM`, `EmZO8QiOfik`, `n4nMCLLW3tY`). A San Diego day is `socal-bight` (or `baja-pacific-north` if you run to the Coronados), so under step 1b of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) cabrilla is **never offered** — not ranked lower, not offered with a caveat.

This is not me being pedantic about tags. Your exact question is the failure mode the protocol was written to stop. From [`locations/regions.md`](locations/regions.md) and the protocol note itself: a SoCal day plan can route to cabrilla because its situation table opens with *"low light, tight to shoreline structure → jerkbaits, cast tight to the rock"* — which reads perfectly for a San Diego jetty at dawn, **and the fish lives 400 miles away** (cameron). The Cortez and the Pacific side are treated as different oceans in this KB for precisely this reason: cabrilla and pargo are Cortez; white seabass and calico run the Pacific side ([`locations/cortez-north.md`](locations/cortez-north.md)).

## Where you'd actually go for cabrilla

Two documented zones, both a trip and not a weekend run from a San Diego ramp:

**Bahía de los Ángeles (BOLA) — the drive-in panga zone.** [`locations/bahia-de-los-angeles.md`](locations/bahia-de-los-angeles.md), [`locations/cortez-north.md`](locations/cortez-north.md). The route from San Diego is the 8 east to Calexico, cross at Mexicali, then south down the Cortez coast (`P36VGPPf120`):

| leg | time |
| --- | --- |
| San Diego → Calexico | 1.5–2 h |
| Calexico → San Felipe | 2 h |
| San Felipe → Gonzaga Bay | 2 h |
| Gonzaga → Bahía de los Ángeles | 2 h |
| **total** | **~8 h without stops; 9–10 h relaxed** |

Door-to-door runs longer than the legs suggest — one crew left 06:30 and reached the hotel 17:31, an 11-hour travel day (`T3cEQUqiH8E`). No cell service through the desert, at Gonzaga, or at the bay; travel minimum two vehicles; top off fuel before crossing and again in San Felipe; carry everything you fish with, because there is *"no tackle shop to really speak of"* (`odiIWmut6gM`, `P36VGPPf120`). You don't use the ramp — the panga is driven to your hotel room and trailered off the beach (`odiIWmut6gM`, `P36VGPPf120`). Note the KB flags a conflict on the Calexico → San Felipe leg (2 h in one source's planning summary, ~1–1.25 h on the road, 2.5 h from a second crew).

**San Felipe mothership** — a week to ten days aboard a live-aboard that carries its pangas on deck; it's an access point, not a fishing ground ([`locations/san-felipe.md`](locations/san-felipe.md), `aT-fL7vaavY`, `81YHbZQFzgk`).

**Loreto / Puerto Escondido — you fly in.** [`locations/loreto.md`](locations/loreto.md). One documented trip reached it through CBX, the Cross Border Xpress bridge into the Tijuana airport (`ikiXx9sUsoA`); Puerto Escondido Marina south of Loreto is the documented launch (`n4nMCLLW3tY`). Cabrilla there came off **5–10 ft** of water on a jerkbait (`n4nMCLLW3tY`).

**Paperwork before tackle** ([`locations/mexican-waters.md`](locations/mexican-waters.md), as of 2026-08, verify current): FMM tourist permit printed (one report of being checked three times), CONAPESCA fishing licence bought online with passport in hand, passport, and separate Mexican vehicle insurance — US policies do not carry over. **Regulatory — Mexico. INM for entry, CONAPESCA for fishing. Verify before you travel.**

## And the timing would be wrong even if you went

Mid-September is not the cabrilla window. The Cortez North season table ([`locations/cortez-north.md`](locations/cortez-north.md), `P36VGPPf120`) reads:

- **End of April → early June** is the good window, wind permitting; **May–June are the prime months**.
- **July on: "everything starts to go down."** The water heats and fish **drop out of the surface program**. The mechanism is depth, not absence — you lose the surface bite and move to dropper loop, live bait, yo-yo iron and knife jigs, "anything heavy on the bottom."
- **August–October** is the late-season play for dorado, marlin, sailfish and occasionally tuna — how hot the water gets decides it.
- **Fall into winter (Oct+)** the Cortez baitfish drop to about **1–1.5 in** and cabrilla key hard on that micro-bait, so that trip carries downsized lures (`EmZO8QiOfik`).

Cameron's own September program at BOLA is the same read: yellowtail **on the bottom**, worked with dropper loops and yo-yo iron ([`seasonal/september.md`](seasonal/september.md), cameron). So the cast-and-burn jerkbait program you'd go for cabrilla to fish — 170-size early in low light, dropping to the 150 once the sun is up, 2–3 casts a minute and 500–700 casts a day (`EmZO8QiOfik`) — is exactly what mid-September takes away. **Plan that trip for late April through June, or October+ with small lures.** Caveat: nobody in the corpus gives a month-by-month cabrilla presence or temperature pattern — the KB flags that as a gap, and this September read is the region's season shape plus cameron's yellowtail note, not a cabrilla-specific source.

## What you can actually do out of San Diego on 2026-09-12/13

I have **not pulled conditions** — no BightSST, no SST, chlorophyll, wind or swell for that weekend — so this is the priors layer only, and per [`seasonal/september.md`](seasonal/september.md) a stale prior is not today's water. Step 1 of the protocol is still owed before this becomes a plan.

If what you actually want is the *cast-at-rock* program, the local version is **calico bass** — the KB draws that comparison from the other direction: an angler on the Cortez rocks calls it *"literally calico fishing on steroids"* (`8IRONtdkceM`). [`species/calico-bass.md`](species/calico-bass.md): `regions: [socal-bight, ...]`, `waters: [nearshore-coast, island, bay-harbor]`, `season_peak` includes September, `sst_band_f: 65-68`. Fish the **edges and pinch-points** — leading edge, outside edge, isolated stringers — not the dense middle, and plan off the **current** read across the kelp rather than the tide clock (`0KQ--N5TjqE`). They don't migrate; movement is structure pile to structure pile (`LqW32NSkObY`). Weedless 7" swimbait on a 3/8–3/4 oz keel-weighted spring hook, 7–8 ft bass class 40–60 lb; or surface iron on the drift to cover a whole edge (a documented reef drift at **18–20 ft** with birds overhead, `I-QBxuV2p7M`).

Other in-envelope September priors, routing only:

- **Yellowfin tuna** — `season_peak: [aug, sep, oct, nov]`, 8–10 lb to 40–50 lb with **15–25 lb average grade** (`8M4QhL-Qb7E`); September prior is that volume near the border **slides north with the warm water** and bluefin slide with them (`5to3Q5P7w90`). Follow the temperature, not last week's spot. [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md).
- **Dorado** — `season_peak: [jul, aug, sep, oct]`, SoCal grade 8–15 lb with fish to 30 lb (`P9H-bpzT7eU`), on kelp paddies along the green/blue edge — 71.6 °F on a productive paddy (`E4vKwRaRueA`). The September prior puts them in **open-water schools below Catalina**, not on structure (`5to3Q5P7w90`). [`species/dorado.md`](species/dorado.md).
- **Rockfish & lingcod** — `season_peak` includes September, hard bottom 20–900 ft, `regions: [socal-bight, baja-pacific-north]`. **Regulatory — California / CDFW, as of 2026-08: verify current season dates, bag limits and RCA depth boundaries before you go**; the KB's own figures are single-source and self-flagged. [`species/rockfish-lingcod.md`](species/rockfish-lingcod.md).
- **Coronado Islands** — the closest island boiler rock to you, ~13 nm from the San Diego bay entrance (cameron; the linked species note says 13 *statute* miles from `D5DR7Kx42_A`, and the KB flags that mismatch). But it is **Mexican water** — paperwork first — and its species table peaks yellowtail Apr–Jun, with no September row. [`locations/coronado-islands.md`](locations/coronado-islands.md).

The bigger-bluefin September prior — the volume square, SBI–San Nicolas–Clemente–Catalina (`5to3Q5P7w90`) — is real but it is a long way up the Bight from a San Diego launch, so it only belongs in your plan if your range and the forecast support it.

## One more thing worth knowing about that cabrilla note

If you do plan the Cortez trip off this KB, read [`species/cabrilla.md`](species/cabrilla.md) with its flags open. Several zone labels on it are contested — `dEPuDrhoClM` is a November 2022 Tony Reyes mothership trip out of San Felipe, not Bahía de los Ángeles, and the 5–10 lb / 15 lb / 17 lb grade from `0dNfsle54Wo` is Gonzaga Bay footage, not BOLA. The 40–60 lb yo-yo rod class in the gear summary appears in neither cited transcript (`M8hOYQ_6rSg` actually says an 8 ft, 20–50 lb rod). And there is no cabrilla zone guide yet — both BOLA and Loreto are flagged stubs.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `locations/regions.md`, `species/cabrilla.md`, `species/README.md`, `seasonal/september.md`, `locations/cortez-north.md`, `locations/bahia-de-los-angeles.md`, `locations/loreto.md`, `locations/san-felipe.md`, `locations/mexican-waters.md`, `locations/coronado-islands.md`, `species/calico-bass.md`, `species/yellowfin-tuna.md`, `species/dorado.md`, `species/rockfish-lingcod.md`  
*videos:* `dEPuDrhoClM`, `EmZO8QiOfik`, `M8hOYQ_6rSg`, `0dNfsle54Wo`, `n4nMCLLW3tY`, `6P34jI9q1tE`, `T3cEQUqiH8E`, `P36VGPPf120`, `odiIWmut6gM`, `aT-fL7vaavY`, `81YHbZQFzgk`, `8IRONtdkceM`, `ikiXx9sUsoA`, `5to3Q5P7w90`, `0KQ--N5TjqE`, `LqW32NSkObY`, `I-QBxuV2p7M`, `8M4QhL-Qb7E`, `E4vKwRaRueA`, `P9H-bpzT7eU`, `D5DR7Kx42_A`, `iAr6sbRC384`, `lF6jQklDCrY`  
*gaps admitted:* No live conditions were pulled — no BightSST SST, chlorophyll, wind, swell or current for the weekend of 2026-09-12/13, so everything here is the priors layer only and step 1 of the day-plan protocol is still owed. | The corpus has no month-by-month presence or temperature pattern for cabrilla anywhere in the Sea of Cortez — species/cabrilla.md flags this explicitly, so the mid-September read is inferred from the Cortez North region season table plus cameron's September BOLA yellowtail note, not from a cabrilla-specific source. | No corpus source covers running your own boat to Bahía de los Ángeles — nothing on trailering down, using the ramp, fuel on the water, or the range a private boat would need (flagged gap in locations/bahia-de-los-angeles.md). | No Mexican (CONAPESCA) bag limit, size gauge or closed season for cabrilla / leopard grouper is recorded anywhere in the corpus as of 2026-08. | The corpus does not say whether the Bahía de los Ángeles season shape extends north to San Felipe and Gonzaga — the northern end of the region is undated. | The KB has no note on any grouper resident in SoCal waters, so it cannot tell you whether a cabrilla-like grouper exists off San Diego at all — only that cabrilla itself does not. | No corpus source states what a private-boat day trip to the Coronado Islands requires — permits, passports, or whether an FMM applies to a day that never lands (flagged gap in locations/coronado-islands.md). | seasonal/september.md gives no San Diego spot-level or zone-level pick; its named September zones are the SBI–San Nicolas–Clemente–Catalina volume square, open water below Catalina, and the border yellowtail/yellowfin band, so no specific mid-September San Diego destination can be resolved without live conditions. | No cabrilla zone guide exists — both Bahía de los Ángeles and Loreto/Puerto Escondido are flagged stubs in species/cabrilla.md. | Several zone attributions and the 40-60 lb yo-yo rod class on species/cabrilla.md carry open fact-check flags, so trip-planning numbers from that note should be treated as contested rather than settled.

</details>
