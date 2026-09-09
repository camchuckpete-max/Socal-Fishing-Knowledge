# Gear — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.25 | 12 | 11.75 |
| found | 1.75 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.5 | 2 | 1.75 |
| honest | 2 | 2 | 2 |
| actionable | 2 | 2 | 2 |
| **wins** | 0 | 1 | 3 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 1 | 0 | 1 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | None | None | None |
| Gear | 11.25 | 12 | 11.75 |
| Technique | None | None | None |
| Finding fish | None | None | None |
| Conditions & season | None | None | None |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 6. [gear] What rod, reel and line should I use for throwing the surface iron at yellowtail? Give it in gear-class terms …

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B3', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three land the same core answer — jig-stick class, 9–10 ft moderate/fast, 25–60 lb, narrow star-drag conventional, Setup 5 (Phenix Abyss 10'0" / Torium 20HG) as the rod, Trinidad 40 and Avet ruled out — and all three are honest about the same real gaps (no gear ratios recorded, Tranx braid TBD, null envelope fields). A separates itself on the last mile: it is the only answer that reaches a drag number (~10–13 lb off the 40 lb limiting class, matching drag-setting.md's own worked example), the only one that gives a per-destination line call for Cameron's specific spools (40 lb top shot for Coronados/La Jolla, 50 lb for Baja/overnight), and it handles the internal contradictions as flagged conflicts with a decision frame rather than a side-by-side dump. B is the cleanest on scoping — it checks the region/waters front-matter gate before recommending anything and is scrupulous about which claims lack a video cite — but stops short of a drag figure and of picking a build. C is the richest on execution (cast mechanics, retrieve, hookset, FG knot, kelp braid) and the best at using the profile's actual launch and home waters, but it leaves the Build A vs Build B line question unresolved for the angler and lets the Cortez panga rod and the 8 ft extra-heavy build sit unlabeled in its alternates table beside SoCal doctrine.

- *B2 reasons:* found: class lexicon, surface-iron, rod-and-reel-selection, line-and-leader, iron-jigs, fg-and-albright, gaffing, profile — and it is the only one to use the boat.md body facts (Dana Landing launch, ~8 am departure) rather than stopping at the null front-matter fields. specific: alternate-build table with rod ratings and cast weights, the 40–65 vs ~80 lb braid split with a decision frame, FG knot with ~20 wraps, kelp braid texture, top-shot-length failure mode, Cedros 40/50/80 vs 80–100 lb floors, iron weights, and a full cast/retrieve/hookset section (2 o'clock to 9 o'clock, tip down, wind through the strike). sourced: paths plus ids on nearly everything, and it explicitly separates KB doctrine from its own inference on the Lexa. scoped: weaker — the 8 ft / 20–50 lb panga build and the 8 ft extra-heavy build sit in the alternates table without a region label, and only the later section identifies the panga argument's provenance; no regulatory claims, so no as-of failure. honest: 12 gaps, flags gaffing.md's low confidence/sponsored status, states outright that no drag figures and no color doctrine exist in the corpus and refuses to invent one. actionable: an angler can rig and fish it end to end, but it never resolves which line build to run on the Torium and offers no drag setting.
- *B3 reasons:* found: right notes — gear-classes, surface-iron, surface-iron-casting, rod-and-reel-selection, line-and-leader, iron-jigs, plus the profile; opens with the front-matter region/waters gate check, which is the protocol step the others skip. specific: class band, 25–50 / 30–60 lb rod ratings, a five-row line table (40–65 braid, ~80 braid + 18 in leader + clip, 65 braid + 100 yd of 40, 50–60 braid + 80–100 yd of 40–50, straight 40 mono), 1.75–2.75 oz iron range, 4:1 vs 7:1 ratio conflict. sourced: note paths plus ids throughout, and it flags one figure as 'stated without a video cite' — unusually careful about which claims are cited. scoped: panga/8 ft argument explicitly marked Baja/Sea of Cortez and deliberately not applied over the Bight; no regulatory claims. honest: 11 gaps, including null envelope fields, unrecorded cast-weight rating on the Phenix blank, missing iron weights, Tranx braid TBD, and the unreconciled main-line figures; admits it quotes no drag number. actionable: rigs the day — Torium primary with a stated line call, Lexa second with a casting-style adjustment for the fast blank, Tranx situational, plus the named gap of no rice-anchovy iron; only the drag setting is missing.
- *NOW reasons:* found: pulled the class lexicon, the surface-iron technique note, rod/reel + line/leader selection, drag-setting, the yellowtail×surface-iron page and all five profile files — nothing relevant left on the table. specific: 8–10 ft / 2–4 oz / 25–60 lb class band, 9–10 ft preference, 80 lb braid + 50 lb/18 in leader + 100 lb clip vs 65 lb braid + 100 yd of 40 lb mono, 40 lb local / 50 lb overnight-and-Baja top shot, iron weights, and the only concrete drag number in the field (~10–13 lb off a 40 lb limiting class). sourced: every parameter carries a note path plus a video id (yn1suHH6b1Y, 3g82igEL8yk, Y_ElKixrhsc, LTCFjqtSI8g, VpW91AKOFVQ); spot-checks against the repo (drag-setting.md quarter-to-third with the same 10–13 lb worked example, gear-classes.md row, rods.md setups) hold up. scoped: labels the 8 ft panga counter-argument as Sea of Cortez region content rather than letting it sit beside SoCal doctrine; no regulatory claims made. honest: 12 admitted gaps including no gear ratios for his reels, unknown Torium spool capacity, Tranx braid TBD, null envelope fields, and the Phoenix Axis / Phenix Abyss profile inconsistency; carries the contradicted-internal flags rather than resolving them. actionable: gives the rod (Setup 5 Torium), the reel doctrine, a per-destination line build, a drag number, reel-clamp placement, which owned irons fit the 2–4 oz window and which is the wind jig.

<details><summary>Full prompt</summary>

What rod, reel and line should I use for throwing the surface iron at yellowtail? Give it in gear-class terms first, then tell me which of the rods in the angler profile fit. Use the angler profile in profiles/cameron/ (boat.md, rods.md, tackle.md, trolling-lures.md, spots.md) and respect the boat envelope.

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Surface iron for yellowtail — class first, then your rack

## 1. In gear-class terms

**Rod — the surface-iron / jig-stick class.** `tackle/gear-classes.md` defines it as **8–10 ft, casts 2–4 oz irons, moderate/fast action, ~25–60 lb**. `techniques/surface-iron.md` narrows that to a **9–10 ft medium-heavy** stick with a tip soft enough to load a heavy iron but with backbone behind it — the length *is* the distance, and **the rod does all the work** (the most common mistake is shoving the lure out with your arms instead of loading the blank). The application table in `tackle/rod-and-reel-selection.md` gives the same row: *Surface iron → 8–10 ft jig stick, moderate → narrow high-speed conventional → 40–65 lb braid.*

Documented alternate builds the KB keeps side by side (not reconciled — they are different anglers' philosophies for the same technique), all from `techniques/surface-iron.md`:

| Build | Spec | Job |
| --- | --- | --- |
| 10 ft, **30–60 lb** (Phoenix Axis 1009 HJ) | casting weight ~**1.8 to 2+ oz** | the general-purpose jig stick (`A70kK2niu2Q`, `LTCFjqtSI8g`, `42A8Owhc8fw`) |
| 9 ft, **30–80 lb** (Axis 909 HJ) | shorter, stouter | fired-up **7–15 lb schoolies** (fight/unhook/recast faster inside a short window) and **Baja structure/kelp**, where backbone muscles a fish off the reef (`LTCFjqtSI8g`) |
| 8 ft, extra-heavy, **30–80 lb** | shorter than class | one angler's favorite specifically for cast distance (`u0scEBby7nA`) |
| 8 ft, **20–50 lb** | explicitly chosen **because a panga is a small platform** | see the boat-envelope section — this one is about your boat (`M8hOYQ_6rSg`, in `tackle/rod-and-reel-selection.md`) |

A casting-safety cap sits alongside these: **nothing longer than 9 ft** in one framework, because a longer rod gets dangerous to cast from anywhere but the bow (`F7jLrt2j2X8`, `tackle/rod-and-reel-selection.md`). That is a real counterweight to the 10 ft standard, not a footnote.

**Reel — narrow high-speed conventional, thumb-controlled** (`techniques/surface-iron.md`). Supporting parameters:

- **Star drag is all this needs** — no lever drag, no two-speed; **20–25 size, 30 max**, because a bigger/taller reel and a lever drag's heavier spool are both harder to cast (`F7jLrt2j2X8`).
- **Speed range:** a high-gear jig-stick reel at roughly **42 in per crank** (Tranx-500-class HG) covers everything from a slow grind to the fast yellowtail speed just by changing cadence (`techniques/surface-iron.md`).
- **Counterpoint, kept side by side:** with a 6-point-something-to-1 reel you have to crank *deliberately slower* to keep the kick right; an older **4:1–5:1** conventional does that slowing-down for you and suits a picky bite. **Reeling too fast is called out as the single most common mistake** — when fish you can see won't eat, suspect retrieve speed before you change jigs (`3dVc-2rsYII`).

**Line — the KB carries two rigging philosophies and does not reconcile them.**

- **Build A — short leader and clip** (`techniques/surface-iron.md` gear-class detail): **~80 lb braid** main → **50 lb mono/fluoro leader, ~18 in** → **100 lb clip** tied straight to the iron, so you swap irons without re-tying.
- **Build B — long mono top shot** (`A70kK2niu2Q`, `LTCFjqtSI8g`): **50–60 lb (up to 80 lb) braid backing** → **80–100 yd of 40–50 lb monofilament** run straight to the jig, no leader. Top-shot size is **destination-based**: **40 lb** for full-day-accessible islands (Coronados, Channel Islands, Catalina), **50 lb** for overnight-range spots (San Clemente, Santa Barbara Island) and **anywhere in Baja**, because those carry a true trophy shot at any moment.

The braid-class doctrine pulls lighter than Build A: **downsize, don't upsize — fish the lightest braid the job allows, up to 65 lb on a jig stick** (Academy Ep16, `aXF0bxAFtU0`, in `tackle/line-and-leader.md`), matching the 40–65 lb selection-table row. So **40–65 lb and ~80 lb both stand in the KB**. The decision frame: thinner line casts farther and lets the iron swim; heavier line is insurance where a big fish can bury you in structure. Section order here is not a ranking.

Other line parameters that matter on irons specifically:

- **Run the thinner end of your top-shot range on irons.** A thick top shot dampens the swimming action in a way it doesn't on a stickbait or popper (`F7jLrt2j2X8`).
- **Kelp:** a rough, high-tooth solid/low-carrier braid **saws through stringers** when a fish buries you; smooth braid just slides and won't cut (Landesfeind, `tackle/line-and-leader.md`).
- **Knot:** the **FG** is the pick for surface iron — lowest profile, reels through the guides without slapping on the cast; ~**20** over-and-under wraps, tied dockside, not in a frenzy (`rigging/fg-and-albright.md`, `CIMTyepgonk`).
- **If you run a mono top shot, make it long enough that the braid-to-mono knot never clears the spool on a full cast.** A knot dragged through the guides hangs up and backlashes, and braid's zero stretch then snaps the leader and loses the jig **even at 40 lb** (`aXF0bxAFtU0`). The same failure at Cedros put "a pretty good slice" in an angler's thumb as the knot ran through his hand (`ILBl12Jm7-0`).
- **Baja floors, side by side:** a Cedros trip's floor is **40 lb**, with **50 lb** covering most everything including surface iron and 80 lb carried just-in-case (`WE643Fue1_A`); a different Cedros operator fielded **80–100 lb as standard** over 28–30 ft rock (`QSmE3mdEL28`). Two operators' independent choices, not a correction of each other.

**Iron class.** A surface iron generally runs **2–3 oz**, distinctly lighter in the hand than a **5–6 oz** yo-yo iron (`VpW91AKOFVQ`). Benchmarks are the **Tady 45** and **Salas 7X**; lengths roughly **5.5"–7"** (`lures/iron-jigs.md`). **Wind up → step up** to a heavier iron (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`). **Small anchovy ("rice") bait → downsize** to a Tady AA-light / A1-light class, roughly a **third** the weight of a 45 — on small bait the small jig out-bites the big one **two or three to one** — and that drags the whole setup down with it: a **medium-action 9 ft graphite-composite stick, smaller narrow reel, ~50 lb braid** to a short fluoro leader. You cannot throw an AA-light on the 80 lb jig stick (`pcwcRdmWmLc`).

## 2. Which of your rods fit

From `profiles/cameron/rods.md`:

| # | Setup | Spec | Verdict for surface iron |
| --- | --- | --- | --- |
| **5** | **Torium** — Phenix Abyss PSX1009J, **10'0", 25–60 lb, moderate/fast** + Shimano **Torium 20HG**, **50 lb braid** | — | **This is the rod.** Your profile already lists its role as "full surface iron setup," and `tackle/gear-classes.md` uses it as *the* named example of the jig-stick class. 10'0"/25–60 lb sits dead centre of the 8–10 ft, 25–60 lb window; moderate/fast is the specified action; the 20HG is a **20-size star-drag high-gear** reel, exactly the 20–25-size star-drag spec in `F7jLrt2j2X8`. Your 50 lb braid sits inside the 40–65 lb bracket — lighter than Build A's ~80 lb, and the KB does not force a choice between them. |
| **1** | **Trinidad 40** — Rainshadow RCJB96XH **8'0", XH, 40–80 lb, 4–10 oz** + Trinidad 40, **80 lb braid** | yo-yo / heavy-iron class | **Backup only, and by your own profile note: "can cast large surface irons but not well."** It is the one rod in your rack carrying the ~80 lb braid of Build A, and its 8 ft length is what the panga argument (`M8hOYQ_6rSg`) asks for — but XH/40–80 lb and a 4–10 oz casting rating are well above the 2–3 oz iron class, and the KB assigns it to `techniques/yo-yo-iron.md`. Reach for it if the Torium is down or you are throwing the heaviest iron in wind. |
| **4** | **Lexa 400** — Okuma PCH-C-901H, **9'0", H, fast, ~20–60 lb** + Lexa-HD 400HS-P, **50 lb braid** | workhorse / all-around class | **Closest spare, with a caveat.** 9'0" and 20–60 lb fall inside the jig-stick window and it is your "biggest do-everything cast rod," but the KB classes it *workhorse / all-around*, not jig stick, and its action is **fast** where the class calls for **moderate/fast**. No note in this KB assigns it to surface iron — treat that as my read of the specs, not KB doctrine. |
| **3** | **Tranx** — Phenix M1 SMX-82H, **8'2", H, extra-fast, 20–45 lb, 3–8 oz**, braid **TBD (respool pending)** | utility inshore / baitcast | **No.** Extra-fast is the wrong action for loading an iron, and the KB records no braid weight for it. Note the downsized-iron build calls for a **medium-action 9 ft** stick — the opposite of this rod. |
| **2** | **Avet** — Teramar TMC90MHB2 9'0" MH fast 30–65 lb, 50 lb braid | flyline class | **No** — this is your rod for the flyline rows in `species/yellowtail.md` (picky / seeing-not-biting fish), not the iron. |
| **6** | **Talica 25** — Axis 800X3H 8'0", 3X-H, 60–130 lb, 100 lb braid | rail-rod class | **No** — the jumbo-bluefin foamer caster. `tackle/rod-and-reel-selection.md` explicitly warns a 60–130 lb-rated stick is over-gunned even for mid-grade bluefin (`-MP2RqJC7B0`). |
| **7** | **Fathom 80** | spreader-bar trolling only — **never casts** | **No.** |
| **8** | **TLD 20** — Seeker 660H 6'0" | diver-troll | **No.** |

**One profile ambiguity to sort out:** `profiles/cameron/tackle.md` lists, under open items, "owns a **10 ft Phoenix Axis jig stick**; always brings it to BOLA but rarely uses it; **wants reps** hooking/landing yellowtail on it," while `profiles/cameron/rods.md` #5 is a **Phenix Abyss** PSX1009J. The KB never says whether that is the same 10-footer under two spellings or a second rod. Either way, `species/yellowtail.md` carries the same open item — so the wanted reps are on exactly the setup this technique calls for.

**Irons in your box that fit the class** (`profiles/cameron/tackle.md`, specs in `lures/iron-jigs.md`):

- **JRI-7**, light blue — "~Tady 45 class; medium-fast; **local / kelp all-rounder**." Your default Coronados/La Jolla iron.
- **Strictly Irons Glory**, light blue, 7" — wide, slow, drawn-out kick; the change-up for **picky bites and slack current**, which is the Coronados "seeing-not-biting" profile.
- **Strictly Irons Mighty**, tan, 5.5" — medium-to-high-speed searching retrieve.
- **Squidco Candy Bar SR Lite**, scrambled egg, **3 oz / 6.5"** — moderate steady grind, optional sink count; right on the 2–3 oz class weight.
- **JRI-5**, scrambled egg — biggest JRI; slow-to-medium on heavy line; **BOLA-proven**.
- **Nomad Slidekick 120g**, **4.25 oz**, 6" — the crossover: heavier than a traditional iron, so it is your **wind jig** (the "step up when it's windy" rule) and the one to deliberately **sink out** to cover the column.

Gap in the box against doctrine: you own **nothing in the AA-light / A1-light class** (~1 oz, a third of a Tady 45). If you hit a small-anchovy "rice" bite, the KB says the small jig out-fishes the big one 2–3:1 — and you have neither the jig nor the lighter 9 ft medium stick that goes with it (`pcwcRdmWmLc`).

## 3. Respecting the boat envelope

`profiles/cameron/boat.md`: 2004 **Panga Marine Marquesas 22**, single 115 hp Yamaha, tops ~35 kt, **10 rod holders / 6 vertical**, launches **Dana Landing (Mission Bay)**, normal departure **~8 am**, home waters **Coronado Islands, La Jolla, San Diego offshore banks**, plus the BOLA program.

- **The 10 ft stick vs the panga.** The KB carries a direct, attributed argument against your primary rod's length on your exact platform: an **8 ft, 20–50 lb** rod is preferred over the "purist" 9 ft jig-stick standard **because a panga is a small fishing platform** — a 9–10 ft rod makes it hard to work a big fish close enough to gaff with the short **4–5 ft** gaffs typically carried aboard, and it is more awkward around the boat and to travel with (`M8hOYQ_6rSg`, in `tackle/rod-and-reel-selection.md`). Kept side by side with the 9–10 ft doctrine, not reconciled. What the choice actually turns on: **cast distance vs. endgame reach on a small deck.** My read for you: keep the Torium as the primary — it is the KB's own class exemplar and your stated surface-iron setup — and solve the panga end of it at the gaff, not the rod. `fish-care/gaffing.md` sizes yellowtail (and similar fish to **40–50 lb**) at a **3-in hook on a ~6-ft gaff** — longer than the 4–5 ft the panga argument assumes — though that whole note sits at **low confidence** (sponsored Promar spot, `I84uoay_jwQ`). The KB does not record what gaff is actually on your boat.
- **Stowage is not a problem:** antenna and all rods lay flat, leaving your head at the helm as the highest point; 10 holders, 6 of them vertical.
- **Range:** the Coronados are **~13 mi from San Diego** and "synonymous with yellowtail" (`species/yellowtail.md`, `D5DR7Kx42_A`) — comfortably inside a 35 kt panga's day range off Mission Bay.
- **Wind → iron weight is your sea-state lever.** No trim tabs and noted hull flex on hard wave impacts mean chop is a real constraint; the technique's answer to wind is the **heavier iron** (Salas 7X class / your Slidekick) to punch the cast out (`D5DR7Kx42_A`).

## 4. Fishing it, once you're on fish

All from `techniques/surface-iron.md`:

- **Cast:** hang the jig about a **leader length below the tip (~18 in)**, take the rod back to **2 o'clock**, let the blank load, sweep from 2 o'clock down to **9 o'clock** and turn the wrist through. Build the swing by moving the tip **up and down** (pendulum), not side to side, and release on the **outside part of the swing** as it comes back around (`VpW91AKOFVQ`, `3dVc-2rsYII`). Laying the reel on its side through the cast is an added distance step (`KLoEJInlmZo`).
- **Placement beats distance.** A 75 yd cast at fish sitting 40 yd out overshoots for nothing; on a moving school, get **ahead of its line of travel** and cut it off.
- **Retrieve:** start winding the instant it lands, **rod tip pointed down at the water** so the iron kicks side to side — tip up and it skips and stops swimming. Steady grind as the baseline; **speed up for yellows**. Every so often let it **sink out like a yo-yo drop**, then resume the surface swim, to cover the column.
- **Your home water, specifically:** a **big school at the Coronado Islands** will often eat on a faster, less exacting retrieve; the smaller schools along the mainland from **Del Mar down to Imperial Beach** run markedly more finicky, especially on bigger grade, and need the retrieve dialed precisely (`VpW91AKOFVQ`). Layer that on the Coronados **"seeing-not-biting" cycles with narrow daily windows** — anchor those days to tide and current, not the clock (`YZtX1MiT0y8`).
- **Hookset: wind through it, never swing.** Roughly 9 of 10 strikes come as the fish grabs the iron amidships and shakes it; a swing pulls the jig out of its mouth, while continuing to wind drives the hooks in as the fish turns. Crank as fast as you can until line starts peeling the other way — that is the tell you're actually hooked (`3dVc-2rsYII`, `KLoEJInlmZo`). This contradicts the swing-to-set hookset for `techniques/knife-jigging.md`; the KB keeps both, and the reason is that a vertical jig gets **sucked in** while a surface iron gets **struck** on a moving retrieve.
- **Then pull the rod up first and start cranking before the tip comes back down** — tip-down-then-wind puts slack in right as the hook is seating (`VpW91AKOFVQ`).
- **Guide the retrieved line evenly across the spool.** Line piled on one side doesn't hurt this retrieve — it sets up the backlash on your **next** cast (`KLoEJInlmZo`).

## 5. What this KB does not cover

- **No systematic surface-iron color doctrine.** The KB says so explicitly and refuses to invent one — choose size, weight and swim first, color last. What exists is a set of unmerged single-trip reports: **mint** and **blue/white** at Cedros, **scrambled egg**, a **Tady 45 "Wounded Warrior"** as one registered voice's one-jig pick across yellowtail/calico/white seabass/yellowfin (`KLoEJInlmZo`), and a chrome-in-bright-light / white-in-low-light framework that belongs to the **tuna lead-jig** class, not the classic iron blank (`F7jLrt2j2X8`).

Everything above is drawn only from the notes listed; where two sources disagree I've kept both rather than picking for you.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/yellowtail.md`, `techniques/surface-iron.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`, `lures/iron-jigs.md`, `rigging/fg-and-albright.md`, `fish-care/gaffing.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`  
*videos:* `VpW91AKOFVQ`, `3dVc-2rsYII`, `KLoEJInlmZo`, `D5DR7Kx42_A`, `pcwcRdmWmLc`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `42A8Owhc8fw`, `F7jLrt2j2X8`, `u0scEBby7nA`, `ILBl12Jm7-0`, `M8hOYQ_6rSg`, `gevNj2Y1Ep8`, `xPFm_ZV2PZU`, `aXF0bxAFtU0`, `WE643Fue1_A`, `QSmE3mdEL28`, `YZtX1MiT0y8`, `CIMTyepgonk`, `I84uoay_jwQ`, `-MP2RqJC7B0`, `cameron`  
*gaps admitted:* No inches-per-crank / gear-ratio spec for the Shimano Torium 20HG anywhere in the KB — the ~42 in per crank figure belongs to a Tranx-500-class HG, so I could not confirm Cameron's reel covers the full slow-grind-to-fast-yellow cadence range. | The Tranx 400's braid weight is unrecorded (respool pending, profiles/cameron/rods.md), so that setup's line class cannot be resolved at all. | profiles/cameron/boat.md gives no numeric sea-state or wind limit for the Panga Marine Marquesas 22, so I cannot say what conditions the boat is cleared for — only that it has no trim tabs and shows hull flex on hard wave impacts. | The KB does not record what length gaff is actually aboard Cameron's boat, which is the pivot of the panga-vs-10-ft-rod argument. | No drag settings (lb or fraction of breaking strength) are given anywhere for surface iron or yellowtail. | The KB does not state whether Cameron's Torium is spooled straight braid or braid-to-top-shot — only 'Braid: 50 lb' — so I could not resolve his setup onto Build A vs Build B. | The 40–65 lb braid bracket (gear-classes, rod-and-reel-selection, line-and-leader) and the ~80 lb main in the surface-iron gear detail are carried side by side and never reconciled in the KB; I could not give a single number. | No systematic surface-iron color doctrine exists in the corpus — the KB says so explicitly; only unmerged single-trip color reports. | profiles/cameron/tackle.md names a '10 ft Phoenix Axis jig stick' while rods.md names a 'Phenix Abyss PSX1009J' 10-footer; the KB never says whether these are one rod or two. | Cameron's inventory contains no light/downsized iron (Tady AA-light / A1-light class) and no medium-action 9 ft downsized jig stick, so the KB's small-anchovy 'rice bait' doctrine cannot be executed from his documented gear. | Classing the Lexa 400 as a possible spare jig stick is my inference from its 9'0" / 20–60 lb specs — the KB assigns it to the workhorse/all-around class and never to surface iron. | No conditions were supplied in the question and none were pulled from BightSST, so nothing here is tuned to a specific day's wind, SST or tide.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

## First, the envelope check (day-plan protocol step 1b)

Surface iron for yellowtail is in-envelope for your water: `species/yellowtail.md` gates `regions: [socal-bight, baja-pacific-north, baja-pacific-south, cortez-north, cortez-south]`, `waters: [island, bank, nearshore-coast, open-ocean]`, and `techniques/surface-iron.md` gates the same regions plus `waters: [nearshore-coast, island, bank, open-ocean]` — so Coronados / La Jolla / the San Diego banks / BOLA all qualify (`profiles/cameron/spots.md`).

Two envelope caveats before the gear, because the protocol says respect the boat, not assume it:

- `profiles/cameron/boat.md` carries `home_port: null`, `range_nm: null`, `sea_state_max_ft: null` — the note explicitly says the protocol must **ask** for range and sea state rather than assume one. You gave me no conditions, so nothing below is a zone or day call, just the outfit.
- The one place your **panga** actually changes the rod answer is length — see the panga caveat at the end.

---

## 1. In gear-class terms

**Class: surface-iron / jig-stick class** — `tackle/gear-classes.md`: *8–10 ft, casts 2–4 oz irons, moderate/fast, ~25–60 lb.*

**Rod**
- **9–10 ft is the standard.** *"An 8-ft jig stick is a yo-yo rod — it's not a jig stick. 9-ft is okay. 10-ft is better"* (`yn1suHH6b1Y`, `techniques/surface-iron.md`). Doug Kearn's counter version: **no less than 9 ft to be "in the game," 10 ft preferred**, because the longer rod throws farther and the fish don't always come in close (`3g82igEL8yk`, `tackle/rod-and-reel-selection.md`). A second clip from the same voice includes 8 ft as an option for the lighter calico-grade irons — kept side by side, not merged (`r9bF3VtzDUg`).
- **Line rating: 25–50 lb** on Steve Carson's traditional build (9 ft), **30–60 lb** on Ray Sharifi's 10-footers (`Y_ElKixrhsc`, `LTCFjqtSI8g`/`42A8Owhc8fw`, `tackle/rod-and-reel-selection.md`).
- **Action: moderate/parabolic beats stiff.** The blank does the work — an all-fibreglass jig stick "loads up more easily" and is the stated go-to for surface iron, while a stiffer composite is the better popper/stickbait tool (`sjlL5GidM58`). Length is a stated trade-off, not free: a 9–10 ft stick is *"not the most fun to fight a fish on,"* but *"the main thing is you've got to get hooked up"* (`BLbUu_mfMJY`, `techniques/surface-iron-casting.md`).

**Reel**
- **Mid-size star-drag conventional is the class standard** — narrow, thumb-controlled, high-ish speed. Kearn names a **Torium 20**-size star drag; Carson runs a **Penn Fathom 25 narrow** star drag and states *"the star drags definitely cast better than the lever drags"* (`3g82igEL8yk`, `Y_ElKixrhsc`).
- **Don't over-gear the ratio at the handle.** The irons were designed around a **Penn Jigmaster at 4:1**; *"some of these reels that are six and a half, seven and a half to one — they're too fast"* (`Ec2GaNpiOHI`). Kept side by side, unreconciled: a counter-clip argues a **7:1** baitcaster is a torque/versatility middle ground for surface iron and yo-yo on big yellowtail (`pOFsjDTqaxY`, `tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md`). Spool diameter is the other half — a taller spool picks up more line per turn, so a nominally slower ratio can still be right (`techniques/surface-iron.md`).
- **Low-profile baitcast is a legitimate second build**, not a downgrade: 9–10 ft rod + saltwater level-wind low-profile reel, **50 lb braid + a 4–5 ft leader of 40 lb mono**, reached for with smaller/mid-size jigs (`Y_ElKixrhsc`). Its stated advantages are the level wind (no line management) and an **external brake + spool tensioner you can dial per cast when you change jig weight** — which a Torium-type conventional can't do (`hAryw1v3I68`). Its stated limit: *"if you're fishing like a Tady 45 and up, I'd probably go with a different rod"* — the light-blank baitcast route is for **sub-2 oz, 5–6 in** irons (`IhBY5RHFvuk`).

**Line — three builds the KB keeps side by side, not reconciled**
| Build | Main line | Top shot / leader | Source |
| --- | --- | --- | --- |
| Application table | **40–65 lb braid** | — | `tackle/rod-and-reel-selection.md` |
| Surface-iron note baseline (names your own Torium/Trinidad setups; stated without a video cite) | **~80 lb braid** | **50 lb mono/fluoro, ~18 in**, to a **100 lb clip** tied straight to the iron so you swap irons without re-tying | `techniques/surface-iron.md` |
| Kearn counter tip | **65 lb spectra backing** | **~100 yd of 40 lb mono** (step to 50 lb for bluefin) | `3g82igEL8yk`, `tackle/line-and-leader.md` |
| Sharifi (10 ft, 30–60 lb rod) | **50–60 lb (up to 80) braid backing** | **80–100 yd of 40–50 lb mono** — **40 lb for local full-day islands (Coronados, Channel, Catalina), 50 lb for overnight-range (San Clemente, Santa Barbara) and anywhere in Baja**, because those carry a real trophy shot | `LTCFjqtSI8g` |
| All-mono / budget | **straight 40 lb mono, no spectra** | — ; 40 lb specifically so he can run a **snugger drag** for the hookset (30 lb is a personal preference, not a correction) | `49joKHD7Umc` |

Two line rules that matter more than the exact number:
- **Run the thin end of your top-shot range on irons.** A thick top shot dampens the iron's swimming action — a penalty you don't pay on a stickbait or popper (`F7jLrt2j2X8`, `techniques/surface-iron.md`).
- **Downsize, don't upsize the braid** — 65 lb braid is about the diameter of 20 lb mono; the jig-stick ceiling is **65 lb** and lighter braid casts better (`aXF0bxAFtU0`, `tackle/line-and-leader.md`). Mono's real advantage is casting latitude, not swim: *"on straight spectra you need to make very deliberate casts… it's a backlash,"* while *"a good swimming lure is going to swim well no matter what"* (`Ec2GaNpiOHI`).

**Iron weight the class throws:** surface iron runs **2–3 oz**, distinctly lighter in hand than a **5–6 oz** yo-yo iron (`VpW91AKOFVQ`); Kearn's range is **1¾–2¾ oz, 5–7 in**, and a **treble typically out-fishes a single for yellowtail** (`3g82igEL8yk`, `lures/iron-jigs.md`). Wind up → step up to a heavier iron (Salas 7X class) to punch the cast out (`D5DR7Kx42_A`). Small "rice" anchovy → drop to a **Tady AA-light / A1-light class iron, roughly a third the weight of a Tady 45**, which out-bites the big one **two or three to one** — and that downsize drags the tackle down with it: **medium-action 9 ft graphite-composite stick, smaller narrow reel, ~50 lb braid to a short fluoro leader** (`pcwcRdmWmLc`; corroborated 2026 by `JgXMpjxRxmo`, which adds that even bigger yellowtail key on small anchovy, strongest earlier in the year).

---

## 2. Which of your rods fit (`profiles/cameron/rods.md`)

**Primary — Setup 5, the Torium.** Phenix Abyss PSX1009J, **10'0", 25–60 lb, moderate/fast**, deckhand cord-wrapped handle, clamp-on reel; **Shimano Torium 20HG, 50 lb braid**. This is a textbook fit and your profile already labels it *"full surface iron setup"*; `tackle/gear-classes.md` uses it as the worked example for the class. It hits the 10-ft preference, the moderate/fast action, and the 25–60 lb window; the 50 lb braid sits inside the 40–65 lb table and inside Sharifi's 50–60 backing. Kearn independently names a **Torium 20**-size star drag as the counter standard for this technique (`3g82igEL8yk`). Note the reel has **no fixed reel seat** on that blank — set the clamp by measuring from the **crook of your elbow to the tip of your middle finger**, within about an inch (`49joKHD7Umc`, `techniques/surface-iron-casting.md`).

*Line call on it:* leave the 50 lb braid and run the short-leader build — **50 lb mono/fluoro at ~18 in to a 100 lb clip** (`techniques/surface-iron.md`) — or, if you'd rather have stretch and casting latitude, Sharifi's **40 lb mono top shot for the Coronados/Catalina day, 50 lb for San Clemente/Santa Barbara or Baja** (`LTCFjqtSI8g`). Both are in the KB unreconciled; pick by whether you want a clip system or a long mono shot.

**Second — Setup 4, the Lexa 400.** Okuma PCH-C-901H, **9'0", 1-pc, H, fast, ~20–60 lb**; Daiwa Lexa-HD 400HS-P, **50 lb braid**. Length and line rating are in class; it maps almost exactly onto Carson's "younger set" build — **9–10 ft rod, saltwater low-profile baitcast level-wind, 50 lb braid, 4–5 ft of 40 lb mono leader** (`Y_ElKixrhsc`). Caveat: it's an **H/fast** blank, not the moderate/parabolic the class prefers, so treat it as the fast-rod casting style — **hang the jig shorter than the ~18 in baseline and use the quick whip** rather than a long parabolic load (`techniques/surface-iron-casting.md`). Your profile classes it "biggest workhorse rod," and `tackle/gear-classes.md` files it as workhorse/all-around rather than jig-stick — so: real second choice, not a co-equal.

**Third, situational — Setup 3, the Tranx.** Phenix M1 Inshore SMX-82H, **8'2", H, extra-fast, 20–45 lb, 3–8 oz**; Shimano Tranx 400. Kearn names the **Tranx specifically as a good casting reel for its adjustable brakes** — they cut backlash while still letting the jig get out (`3g82igEL8yk`), and `species/yellowtail.md` lists a Tranx-class casting reel as plenty for yellows instead of heavy tuna gear (`QEmxUIGmKbo`). But 8'2" is below the "no less than 9 ft" floor and the extra-fast action is the furthest from the moderate/parabolic ideal — and **the profile records its braid as TBD, respool pending**, so I can't give you a line class for it. This is the one to grab for a downsized/small-iron program or a tight-quarters cast, not the default.

**Not for this job:**
- **Setup 1, Trinidad 40** (M&M on RCJB96XH, 8'0", XH, 40–80 lb, 4–10 oz, 80 lb braid) — your own profile says it *"can cast large surface irons but not well."* It's the **yo-yo / heavy-iron class** rod; that's its role today.
- **Setup 2, Avet** (Teramar 90MHB2, 9'0", MH, fast, 30–65 lb, 50 lb braid) — right length, wrong job: `tackle/gear-classes.md` files it flyline/soft-rod class, a tip soft enough to cast an unweighted bait.
- **Setup 6 Talica 25** (rail rod, 60–130 lb), **Setup 7 Fathom 80** (profile: *"spreader-bar trolling only — never casts"*), **Setup 8 TLD 20** (6'0") — all out of class.

**Deck plan, your own doctrine:** rig the **surface-iron outfit (Torium), the heavy yo-yo/dropper outfit (Trinidad 40) and the flyline outfit (Avet) simultaneously** and switch as temp + bait depth change — the day moves between faces of one population (cameron, `species/yellowtail.md`).

---

## 3. The panga caveat — the one real envelope conflict

There is a stated preference in the KB for an **8 ft, 20–50 lb rod over the "purist" 9 ft jig-stick standard *specifically because a panga is a small fishing platform***: a 9–10 ft rod makes it hard to work a big fish close enough to gaff with the short **4–5 ft gaffs** typically carried aboard, and it's more awkward around the boat and to travel with — and the 8-footer doubles as the yo-yo rod (Cesar, `M8hOYQ_6rSg`, `tackle/rod-and-reel-selection.md`, region: Baja/Sea of Cortez). Your boat is a **Panga Marine Marquesas 22** (`profiles/cameron/boat.md`), and that doctrine is regionally framed for the Cortez, not the Bight, so I'm not overriding the 10-ft Torium with it. But it is the argument for why your **8'0" Trinidad 40 / 8'2" Tranx** exist in a panga quiver at all, and it's worth knowing on a BOLA trip where you're gaffing your own fish solo. It also lines up with the open item in your profile: you *bring the 10 ft Phenix Axis jig stick to BOLA and rarely use it, and want reps hooking and landing yellowtail on it* (cameron, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`).

## 4. Irons that go with it, from your box (`profiles/cameron/tackle.md`)

- **JRI-7** (light blue, ~Tady 45 class, medium-fast) — the local/kelp all-rounder; the Tady 45 / Salas 7X pairing is the historical standard iron (`lYyi_Yh3S5g`, `A70kK2niu2Q`).
- **Squidco Candy Bar SR Lite**, **3 oz / 6.5"** — right at the class weight (`VpW91AKOFVQ`), and Carson names candy-bar-type jigs on the traditional 9 ft build (`Y_ElKixrhsc`).
- **Strictly Irons Glory** (7", wide drawn-out kick, slow and steady) — the change-up for picky bites and slack current; **Mighty** (5.5") for the medium-to-high-speed searching retrieve.
- **JRI-5** — biggest JRI, slow-to-medium on heavy line, BOLA-proven.
- **Nomad Slidekick 120 g / 4.25 oz** — your wind/heavy option and the one you can sink out to cover the column (`lures/iron-jigs.md`), though at 4.25 oz it's at or above the class's 2–4 oz cast-weight description.
- **Gap, named rather than substituted:** you have **no light "rice"-anchovy iron** (Tady AA-light / A1-light class, ~⅓ the weight of a Tady 45). If the tank is small anchovy, the KB's doctrine says that iron out-bites the big one 2–3:1 (`pcwcRdmWmLc`) and I don't see one in your box.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/yellowtail.md`, `techniques/surface-iron.md`, `techniques/surface-iron-casting.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`, `tackle/jig-rod-rating-selection.md`, `lures/iron-jigs.md`, `profiles/cameron/rods.md`, `profiles/cameron/boat.md`, `profiles/cameron/tackle.md`, `profiles/cameron/spots.md`  
*videos:* `Ec2GaNpiOHI`, `yn1suHH6b1Y`, `VpW91AKOFVQ`, `D5DR7Kx42_A`, `pcwcRdmWmLc`, `JgXMpjxRxmo`, `3g82igEL8yk`, `r9bF3VtzDUg`, `Y_ElKixrhsc`, `49joKHD7Umc`, `sjlL5GidM58`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `42A8Owhc8fw`, `lYyi_Yh3S5g`, `F7jLrt2j2X8`, `pOFsjDTqaxY`, `M8hOYQ_6rSg`, `BLbUu_mfMJY`, `IhBY5RHFvuk`, `hAryw1v3I68`, `aXF0bxAFtU0`, `QEmxUIGmKbo`  
*gaps admitted:* profiles/cameron/boat.md has home_port, range_nm and sea_state_max_ft all null — the KB says the protocol must ASK for range and sea state rather than assume, so I cannot verify any zone is inside the boat's envelope. | No conditions were given (wind, SST, bait size, moon/tide), so the iron-size and rod-stiffness calls (heavier iron in wind, downsize on small anchovy) are left as rules, not a decision for a specific day. | The KB records no gear ratio for the Shimano Torium 20HG, the Daiwa Lexa-HD 400HS-P or the Shimano Tranx 400, so I cannot check any of your reels against the 'six and a half to seven and a half to one is too fast' doctrine. | Setup 3 (Tranx) has no braid weight recorded — profiles/cameron/rods.md says respool pending, do not record a weight — so no line class can be given for that rod. | The Phenix Abyss PSX1009J's cast-weight (oz) rating is not recorded, only its 25-60 lb line rating, so whether the 4.25 oz Nomad Slidekick is inside its rating is unverified. | Weights are recorded for only two of your surface irons (Candy Bar 3 oz, Slidekick 4.25 oz); the Strictly Irons Glory and Mighty and the JRI-5 and JRI-7 have no weight recorded, so I cannot confirm they sit in the 1.75-3 oz surface-iron window. | You own no light 'rice'-anchovy iron (Tady AA-light / A1-light class) — a gap named rather than substituted, per the day-plan protocol. | The gaff length carried on your boat is not recorded anywhere in the KB, so the panga 8-ft-rod rationale (gaffing close with 4-5 ft gaffs) cannot be checked against your actual setup. | The KB's three main-line figures for surface iron (40-65 lb braid in the application table, ~80 lb braid in the surface-iron note's own baseline, 50-60 lb backing in Sharifi's build) are not reconciled anywhere; I presented them side by side rather than picking one as canonical. | tackle/jig-rod-rating-selection.md's 'buy toward the top of the gram rating' rule explicitly does not apply to surface-iron gear (it is framed for slow-pitch/speed-jig rods, which are rated in grams), so there is no equivalent published rule for matching a jig stick to an iron's weight. | No drag-setting number specific to surface iron for yellowtail is quoted here; the only related statement I read was the qualitative '40 lb lets me run a snugger drag' rationale.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Surface iron for yellowtail — the outfit

## 1. In gear-class terms (what the KB says, no profile needed)

**Rod — jig-stick / surface-iron class.** [`tackle/gear-classes.md`](tackle/gear-classes.md) defines it as **8–10 ft, casts 2–4 oz irons, moderate/fast action, ~25–60 lb**. [`techniques/surface-iron.md`](techniques/surface-iron.md) tightens that to **9–10 ft, medium-heavy, a tip soft enough to cast a heavy iron but with backbone** — "an **8-ft jig stick is a yo-yo rod** — it's not a jig stick. **9-ft is okay. 10-ft is better**" (`yn1suHH6b1Y`). A tackle-counter rundown in [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) says the same: **no less than 9 ft to be "in the game," 10 ft preferred**, because the longer rod throws the jig farther and fish don't always come close enough to reach on a shorter one (`3g82igEL8yk`). [`techniques/surface-iron-casting.md`](techniques/surface-iron-casting.md) is blunt about the trade: a 9–10 ft stick is "not the most fun to fight a fish on," but casting reach outranks fight comfort — "the main thing is you've got to get hooked up" (`BLbUu_mfMJY`).

Blank material, from [`techniques/surface-iron.md`](techniques/surface-iron.md): all-fiberglass loads easily and is the classic surface-iron build (Calstar 90J example); a graphite/glass composite runs stiffer and is the better popper/stickbait tool (`sjlL5GidM58`). **S-glass does what E-glass does at ~20% less weight** — which matters at 300 casts in a 12–14 hour day (`yn1suHH6b1Y`).

**Reel — mid-sized star-drag conventional, narrow, thumb-controlled.** The named class standard is a **Torium 20**, or any equivalent mid-sized star drag (`3g82igEL8yk`, [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)). Star drag over lever drag for this job: *"the star drags definitely cast better than the lever drags"* (`Y_ElKixrhsc`), and the mechanism is in [`tackle/star-drag-vs-lever-drag.md`](tackle/star-drag-vs-lever-drag.md) — a star-drag spool disengages more cleanly from the drag system, so it spins freer for the cast; lever drag buys mid-fight adjustability instead (`tYebwLzTyf8`).

**Line — two rigging philosophies, both attributed, the KB does not pick one** ([`techniques/surface-iron.md`](techniques/surface-iron.md)):

| Build | Spec |
| --- | --- |
| Short-leader + clip (that note's class build) | ~**80 lb braid** main → **50 lb mono/fluoro leader, ~18 in** → **100 lb clip** tied straight to the iron (the clip lets you swap irons without re-tying) |
| Long mono top shot | **65 lb spectra backing** → **~100 yd of 40 lb mono** (`3g82igEL8yk`, also in [`tackle/line-and-leader.md`](tackle/line-and-leader.md)); or **50–80 lb braid → 80–100 yd of 40–50 lb mono** straight to the iron, no leader (`A70kK2niu2Q`, `LTCFjqtSI8g`) |
| Traditional star-drag build | 9 ft rod rated **25–50 lb**, Penn Fathom 25 narrow, **100-yd top shot of 40 lb mono** — effective on the **12–40 lb** yellowtail grade named on camera (`Y_ElKixrhsc`) |
| Modern low-profile baitcast build | 9–10 ft rod, **50 lb braid** to a **4–5 ft leader of 40 lb mono** (`Y_ElKixrhsc`) |

The species page [`species/yellowtail-surface-iron.md`](species/yellowtail-surface-iron.md) sets the yellowtail line band as **straight mono, 40–50 lb** — "a trophy yellowtail is possible at any moment, so the heavier end runs when the water allows it."

**Sizing the top shot by where you're fishing** (`LTCFjqtSI8g`, in [`techniques/surface-iron.md`](techniques/surface-iron.md)): **40 lb** mono for local, full-day-accessible islands (Coronados, Channel Islands, Catalina); **50 lb** for overnight-range spots (San Clemente, Santa Barbara Island) **and anywhere in Baja**, because those carry a real shot at a trophy fish at any moment. A separate Cedros data point sets a **40 lb line-class floor, 50 lb for most everything** on that trip (`WE643Fue1_A`, [`tackle/line-and-leader.md`](tackle/line-and-leader.md)).

Three line details that change how the jig swims or survives:
- **Run the thinner end of your top-shot range on irons** — a thick top shot dampens the iron's swimming action; a stickbait or popper tolerates a heavier one (`F7jLrt2j2X8`).
- **40 lb specifically buys a snugger drag**, which helps the hookset; 30 lb sacrifices that (`49joKHD7Umc`).
- **Braid vs mono is a casting-latitude trade, not a swim trade** — "on straight spectra you need to make very deliberate casts. You can't just see a spot of fish over in the other corner and make that cast — it's a backlash," but "a good swimming lure is going to swim well no matter what" (`Ec2GaNpiOHI`). Same note: carry a bulk spool and **re-spool three or four times over a day's fishing** — one nick after hundreds of casts isn't worth losing the jig.

**Terminal:** Mustad 300-series hooks, chosen **to bend** so a jig buried in rock, kelp, or a sea lion comes back (`Ec2GaNpiOHI`). A **treble typically works best for yellowtail**; a single is more a bluefin choice (`3g82igEL8yk`).

**Drag:** [`tackle/drag-setting.md`](tackle/drag-setting.md) — set strike drag to **a quarter to a third of the outfit's lowest-rated line class**, and the worked example is exactly this rig: 65 lb braid to a 40 lb mono top shot → 40 lb is the limiting class → **~10–13 lb** (`VpW91AKOFVQ`, `9JnIS8HkZlA`). Start on the light end and bump up a click at a time if a hooked fish stalemates.

## 2. Three places the KB argues with itself — decide these on purpose

- **Reel gear ratio.** [`techniques/surface-iron.md`](techniques/surface-iron.md) argues 6.5–7.5:1 is **too fast**, because the irons were designed around the ~**4:1** Penn Jigmaster (`Ec2GaNpiOHI`); spool diameter is the other half — a taller spool picks up more line per turn, so a nominally slower ratio can still be right. Against that, [`tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md`](tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md) frames **7:1** as the torque-vs-speed middle ground for big yellowtail — "instead of going with 8:1 to where I'd be getting dogged every now and then, having that little bit more torque is beneficial" (`pOFsjDTqaxY`). The KB's own decision frame ([`species/yellowtail.md`](species/yellowtail.md) gear summary): **the choice turns on whether the outfit's first job is the retrieve or the fight** — and what actually matters is line speed at the jig, set by crank discipline and spool diameter as much as ratio. Practical read: whatever the ratio, crank to keep the kick correct, not to a fixed cadence.
- **Rod length on a small boat.** Against the 9–10 ft standard, the Sea-of-Cortez quiver in [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) states a deliberate preference for an **8 ft, 20–50 lb rod that doubles as surface iron and yo-yo**, *specifically because a panga is a small fishing platform*: a 9–10 ft rod makes it hard to work a big fish close enough to gaff with the short **4–5 ft** gaffs typically carried aboard (`M8hOYQ_6rSg`). That is region-labeled Sea of Cortez, and it is the single most relevant counter-argument to your rack. (For contrast, [`fish-care/gaffing.md`](fish-care/gaffing.md) sizes a yellowtail gaff up to 40–50 lb at a **3-in hook on a ~6-ft gaff**, `I84uoay_jwQ` — so the 4–5 ft gaff in that argument is a panga-carry assumption, not a yellowtail recommendation.)
- **The 25–60 lb class band itself.** [`techniques/surface-iron.md`](techniques/surface-iron.md) carries an open `⚠ contradicted-internal` flag: [`species/white-seabass.md`](species/white-seabass.md) routes to this same class calling it **7–9 ft, 40–50 lb** — most of that band is length the surface-iron note says is not a jig stick. Unresolved in the KB.

(Not applicable, so you don't go looking for it: the "buy toward the top of the gram rating" rule in [`tackle/jig-rod-rating-selection.md`](tackle/jig-rod-rating-selection.md) explicitly scopes itself to slow-pitch/speed-jig rods, "not surface iron or trolling gear, which don't use a gram-weight rating.")

## 3. Your rack — what fits

From [`profiles/cameron/rods.md`](profiles/cameron/rods.md):

| Setup | Spec | Verdict against the class |
| --- | --- | --- |
| **5. Torium** — Phenix Abyss PSX1009J, **10'0", 25–60 lb, moderate/fast**, deckhand cord-wrapped handle, clamp-on reel; **Shimano Torium 20HG, 50 lb braid** | **This is the rod.** | Dead-center: 10 ft is the "10-ft is better" length (`yn1suHH6b1Y`), 25–60 lb is the class band exactly, moderate/fast is the class action, and the **Torium 20 is the reel model the corpus names as the class standard** (`3g82igEL8yk`). Your profile already assigns it "full surface iron setup," and [`tackle/gear-classes.md`](tackle/gear-classes.md) uses it as the worked example of the class. |
| **4. Lexa 400** — Okuma PCH-C-901H, **9'0", H, fast, ~20–60 lb**; Daiwa Lexa-HD 400HS-P, 50 lb braid | **Legitimate second jig stick / backup.** | 9 ft is "okay" (`yn1suHH6b1Y`) and 20–60 lb overlaps the class band. The **Lexa is one of the three casting reels named for yellowtail** — "leave the bluefin gear racked" (`QEmxUIGmKbo`, [`tackle/tackle-express-casting-reel-for-seabass-yellowtail.md`](tackle/tackle-express-casting-reel-for-seabass-yellowtail.md)) — and a Cedros quiver's *farthest-casting* rod was a 9 ft blank on a Lexa 500 (`_C7TJoGT0nw`). Caveat: the blank is rated **H/fast** where the class wants moderate/fast with a tip soft enough to load an iron; profile also says never troll it. |
| **3. Tranx** — Phenix M1 SMX-82H, **8'2", H, extra-fast, 20–45 lb**; Tranx 400, **braid TBD** | **Light-iron option only, and not spec'd yet.** | The **Tranx is named as a good casting reel for its adjustable brakes** (`3g82igEL8yk`) and is on the yellowtail casting-reel list (`QEmxUIGmKbo`). But 8'2" sits under the "9-ft is okay" floor, extra-fast is the opposite of the loading tip the light-blank path calls for, and that path is capped at **sub-2 oz, 5–6 in irons** anyway (`IhBY5RHFvuk`). Its braid is an unresolved open item — I can't spec a line for it. |
| **2. Avet** — Teramar TMC90MHB2, 9'0", MH, fast, 30–65 lb; Avet MXJ, 50 lb braid | **On paper only.** | The length and rating overlap the class, but [`tackle/gear-classes.md`](tackle/gear-classes.md) files it as **flyline / soft-rod class** and your profile role is "mainly flyline." The KB records no drag type or gear ratio for the MXJ, so I can't check it against the star-drag casting doctrine. |
| **1. Trinidad 40** — 8'0", XH, 40–80 lb; 80 lb braid | **No — this is your yo-yo rod.** | Your own profile says it "can cast large surface irons **but not well**," and the class lexicon lists it as the yo-yo/heavy-iron example. Keep it rigged for the wind re-rank (below). |
| **6. Talica 25 / 7. Fathom 80 / 8. TLD 20** | rail-rod, spreader-bar, diver-troll classes | **Out.** Fathom 80 "never casts"; and the router's standing advice for yellowtail is to leave the heavy tuna gear racked (`QEmxUIGmKbo`). |

### The build I'd actually run on the Torium

- **Rod/reel:** as-is. The rod has a **clamp-on reel with no fixed seat** — [`techniques/surface-iron-casting.md`](techniques/surface-iron-casting.md) gives a placement method: set the reel a **crook-of-elbow to tip-of-middle-finger** span up the blank, within about an inch. Too high and your off hand can't get in front of the reel to pull on a fish; too low and you lose the casting leverage (`49joKHD7Umc`; flagged single-source).
- **Line, Coronados / La Jolla / SD banks (your home waters, per [`profiles/cameron/spots.md`](profiles/cameron/spots.md)):** your **50 lb braid to a 40 lb mono top shot** is an exact match for the modern build (`Y_ElKixrhsc`) — run the leader **4–5 ft**, or whatever you can cast without the knot passing the tip guide. Strike drag **~10–13 lb** off the 40 lb limiting class ([`tackle/drag-setting.md`](tackle/drag-setting.md)).
- **Line, BOLA / Baja trips:** step the top shot to **50 lb** — that's the stated rule for Baja and overnight-range water (`LTCFjqtSI8g`) and it matches the Cedros 40 lb floor / 50 lb workhorse read (`WE643Fue1_A`). One Cedros operator runs **straight mono rather than fluoro specifically for surface iron** (`WE643Fue1_A`, no reason given in source).
- **Whichever you run, keep the top shot at the thin end** of that band — thick top shots dampen the kick (`F7jLrt2j2X8`).

## 4. Boat envelope

- **The panga argument applies to you directly.** Your boat is a Panga Marine Marquesas 22 ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)), and the Cortez quiver's case against 9–10 ft sticks is made *about pangas* (`M8hOYQ_6rSg`). It is a real trade — you already know the 10-footer is "not the most fun to fight a fish on" (`BLbUu_mfMJY`). **The 8 ft / 20–50 lb rod that argument recommends has no match in your rack** — your only 8-footer is the Trinidad 40 at XH, 40–80 lb, which is a different animal. Naming that gap rather than substituting is what step 4 of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) requires.
- **Stowage/geometry is fine:** 10 rod holders (6 vertical), and all rods lay flat so the 10-footer doesn't cost air draft.
- **I did not apply a range or sea-state gate.** `home_port`, `range_nm` and `sea_state_max_ft` are all **null** in [`profiles/cameron/boat.md`](profiles/cameron/boat.md), and the protocol says to **ask** rather than assume. Tell me the day's launch and forecast and I'll run step 1b properly.
- Also relevant on a small boat: [`tackle/gear-classes.md`](tackle/gear-classes.md) notes the jig-stick class **doubles as a trolling outfit**, which lines up with your open item about running ~10 ft rods in the gunwale extenders — though your profile currently assigns the Torium to surface iron only.

## 5. Which of your irons this outfit throws

Class benchmarks: a surface iron runs **2–3 oz**, distinctly lighter in hand than a 5–6 oz yo-yo iron (`VpW91AKOFVQ`); [`lures/iron-jigs.md`](lures/iron-jigs.md) puts the class at **5.5–7 in, ~3 oz** up to heavier crossovers, with a second attributed range of **1¾–2¾ oz, 5–7 in** (`3g82igEL8yk`). Your rod's class window is **2–4 oz**.

From [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md): the **Squidco Candy Bar SR Lite** (3 oz / 6.5"), **JRI-7** (~Tady 45 class), **JRI-5**, **Strictly Irons Glory** (7", wide drawn-out kick — the change-up for picky bites and slack current) and **Mighty** (5.5", medium-to-high speed) all sit inside the window. The **Nomad Slidekick 120g at 4.25 oz** is at/over the top of it — that's your wind jig (**wind up → heavier iron to punch the cast**, `D5DR7Kx42_A`), and treat the swap as a reel adjustment: **reset spool tension whenever jig weight changes** (`IhBY5RHFvuk`).

Two yellowtail-specific execution notes that bear on the outfit, from [`species/yellowtail-surface-iron.md`](species/yellowtail-surface-iron.md): **sink it ~30 ft before you wind** (`oadK6zIYyCo`, `ntQXxcH5sjI`; corroborated on a Tady 45 at Cedros, `9tIp4n7q850`), and **fish the retrieve all the way to the rail** — yellowtail eat it right at the boat, so the last five feet are a real bite zone, not the end of the cast (`VpW91AKOFVQ`). On jig size, **bait size beats fish size** — on small anchovy even bigger yellowtail can be out-produced by the smaller iron (`JgXMpjxRxmo`).

**Keep the Trinidad 40 rigged alongside.** In hard wind (**20–25 kt+**) with fish metered rather than showing, the fleet bite goes mostly yo-yo and the surface iron becomes a picker — a re-rank, not an abandonment (`ejUTAnONf7o`; flagged single-source in the KB).

On colors: [`species/yellowtail-surface-iron.md`](species/yellowtail-surface-iron.md) gives scrambled egg, bird shit, mint, blue/white (source `nate`) — but be aware the KB flags this as contradicted-internal, because [`techniques/surface-iron-color.md`](techniques/surface-iron-color.md) carries the opposite doctrine: **colour is not the variable**, ranked **swim → size/weight → colour, last**. Your Candy Bar and JRI-5 are scrambled egg, your Glory and JRI-7 light blue, so you're covered either way.

## 6. What the KB doesn't answer

- **No gear ratio is recorded for any of your reels** (Torium 20HG, Lexa-HD 400HS-P, Avet MXJ), so the 4:1-vs-7:1 argument can't be settled against your actual box.
- **No spool capacity is recorded for the Torium 20HG**, so I can't tell you whether an 80–100 yd mono top shot fits over your 50 lb braid.
- **Your Tranx 400 braid weight is an open item** (respool pending), so that setup can't be spec'd.
- **Profile inconsistency:** [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md) calls your 10 ft jig stick a "Phoenix Axis" while [`profiles/cameron/rods.md`](profiles/cameron/rods.md) records the Torium's blank as a **Phenix Abyss PSX1009J** — same rod under two names, or two rods? Worth resolving. (The tackle note also logs an attributed open item that you bring it to BOLA and want reps hooking and landing yellowtail on it — noted, not treated as doctrine.)


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/yellowtail.md`, `species/yellowtail-surface-iron.md`, `techniques/surface-iron.md`, `techniques/surface-iron-casting.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`, `tackle/drag-setting.md`, `tackle/star-drag-vs-lever-drag.md`, `tackle/jig-rod-rating-selection.md`, `tackle/rod-length-for-angler-size.md`, `tackle/tackle-express-baitcaster-gear-ratio-yellowtail.md`, `tackle/tackle-express-casting-reel-for-seabass-yellowtail.md`, `tackle/tackle-express-cedros-four-rod-quiver.md`, `lures/iron-jigs.md`, `fish-care/gaffing.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`, `profiles/cameron/boat.md`, `profiles/cameron/spots.md`, `profiles/cameron/trolling-lures.md`  
*videos:* `yn1suHH6b1Y`, `3g82igEL8yk`, `Ec2GaNpiOHI`, `pOFsjDTqaxY`, `Y_ElKixrhsc`, `LTCFjqtSI8g`, `49joKHD7Umc`, `F7jLrt2j2X8`, `VpW91AKOFVQ`, `D5DR7Kx42_A`, `M8hOYQ_6rSg`, `QEmxUIGmKbo`, `_C7TJoGT0nw`, `WE643Fue1_A`, `9tIp4n7q850`, `oadK6zIYyCo`, `JgXMpjxRxmo`, `ejUTAnONf7o`, `ntQXxcH5sjI`, `sjlL5GidM58`, `IhBY5RHFvuk`, `tYebwLzTyf8`, `BLbUu_mfMJY`, `A70kK2niu2Q`, `9JnIS8HkZlA`, `I84uoay_jwQ`  
*gaps admitted:* The KB records no gear ratio for any of Cameron's reels (Shimano Torium 20HG, Daiwa Lexa-HD 400HS-P, Avet MXJ), so the surface-iron 4:1-vs-7:1 ratio conflict cannot be resolved against his owned gear. | No line/spool capacity is recorded for the Torium 20HG, so whether an 80-100 yd mono top shot fits over his 50 lb braid is unknown. | profiles/cameron/rods.md setup 3 (Tranx 400) has braid weight TBD pending respool, so that outfit cannot be spec'd for line. | boat.md front matter has home_port, range_nm and sea_state_max_ft all null, so the day-plan-protocol step 1b range/sea-state gate could not be applied - the protocol requires asking. | The KB records no drag type (star vs lever) for Cameron's Avet MXJ, so it cannot be checked against the star-drag-casts-better doctrine. | Cameron's rack has no 8 ft / 20-50 lb rod - the panga-specific surface-iron+yo-yo rod the Sea of Cortez quiver (M8hOYQ_6rSg) recommends for a small platform. | Profile inconsistency the KB does not resolve: tackle.md calls the 10 ft jig stick a 'Phoenix Axis' while rods.md records the Torium's blank as a Phenix Abyss PSX1009J. | The KB leaves the two surface-iron rigging philosophies unreconciled (80 lb braid + 50 lb/18 in leader + 100 lb clip vs. braid backing + 80-100 yd mono top shot) - it states both side by side and picks neither. | techniques/surface-iron.md carries an open contradicted-internal flag: species/white-seabass.md calls the same jig-stick class 7-9 ft / 40-50 lb against this note's 9-10 ft; unresolved. | The yellowtail iron colour list (scrambled egg, bird shit, mint, blue/white) is flagged contradicted-internal against surface-iron-color.md's doctrine that colour is not the variable; the KB does not settle it. | The 20-25 kt+ wind threshold that re-ranks surface iron behind yo-yo is flagged single-source in the KB. | No drag-setting figure specific to surface-iron yellowtail is given; only the general quarter-to-a-third-of-line-class rule and its 40 lb worked example.

</details>

### 7. [gear] Set me up a flyline rig for 20-30 lb bluefin: hook size and style, leader material and test, main line class, …

**Winner:** NOW · mapping {'A': 'B2', 'B': 'B3', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three are well-sourced, honest, and riggable; the separation is how closely each matched the 20-30 lb grade the question named. C found the KB's purpose-built rung for exactly that grade (the '20/25 lb rig' / Rig 1 with its 25-30 lb-tuna framing and late-Aug-to-late-Sept window), stated the region/waters gate outright, gave a four-placement bait table with depth cues and bone-anchor mechanics, a drag-scale weakest-link procedure, and Rig 2/Rig 3 escalation if the grade jumps. B reached the same ladder notes and produced the cleanest up-front spec table plus the most rigorous gap list, but read the finesse rig only as a 15-40 lb school-tuna rig, so it never surfaced the grade-matched framing, and its bait rigging stops at nose/belly/butt. A is excellent on hook finish, bait handling, and the braid-floats depth math, and it honestly declares that no note pairs a grade band to a hook size — but it lacked (or never surfaced) the grade ladder, so it hands over a 30 lb top shot with 25-30 fluoro and a No. 4-to-4/0 hook spread the reader must resolve, one class heavier than the 20-25 lb cap it itself cites for a tough bite.

- *B2 reasons:* found: pulled flyline, hooks, line-and-leader, live-bait and knot notes and stated plainly that no note pairs a bluefin grade band to a hook size — but never surfaced any grade-matched rig rung, so the build is assembled one class heavier than its own cited 20-25 lb cap. specific: real numbers throughout (30 lb mono top shot 50-100 yd, 4-6 ft fluoro, braid-vs-mono depth math 10-12 ft vs 50-60 ft at 200 ft back, 4.5:1-5:1 ratio, bronze finish, 6-8 lb strike drag). sourced: dense note paths plus video ids on nearly every claim, including a seven-row hook table with per-situation ids. scoped: SoCal/Cortez Bank/San Clemente content only, no out-of-region numbers unlabeled; the only regulatory touch is the absence of a CDFW circle-hook rule, correctly stamped as a 2019 Mexican mandate flagged unverified with verify-current advice. honest: six-item thin-KB section, flags that its 'start at No. 2' is its own read of an unreconciled No. 4-to-4/0 spread and that drag figures are its arithmetic; no relative time. actionable: an angler can rig from it end to end, though the central hook answer is a spread the reader must trust the synthesis on.
- *B3 reasons:* found: reached the grade ladder and finesse-outfit notes plus flyline/hooks/leader, but framed the finesse rig only as '15 lb, school tuna 15-40 lb' and missed that same note's explicit 20/25 lb-rig framing at 25-30 lb fish. specific: front-loaded spec table (300 yd 30 lb braid, 50 yd 20-25 lb top shot, 4-5 ft matched fluoro, size 2 Gorilla Light J or size 2-4 Mutu, 4-turn surgeon's, 5-7 lb strike drag, 8 ft 12-30 lb rod). sourced: note paths and ids on essentially every parameter, including the surgeon's-knot corroboration count. scoped: SoCal offshore throughout, no region drift, no regulation asserted so no as-of needed. honest: eleven declared gaps, flags the size-2-vs-size-4 discrepancy and the number-size vs ought-size unit clash, refuses to substitute a heavier owned rod for the missing finesse class. actionable: fully riggable, but bait rigging is thinner than C — nose/belly/butt only, no depth-cue mapping or bone-anchor mechanics — and the opening/closing day-plan framing is off-target for a pure gear ask.
- *NOW reasons:* found: identified that the KB has a purpose-built rig for exactly this grade ('20/25 lb rig', Rig 1 of the grade ladder) with its stated framing (25-30 lb tuna refusing heavier line, late-Aug-to-late-Sept window), then cross-checked flyline, hooks, gear-classes, knot and bait notes. specific: the tightest build of the three — 50 yd 20 lb top shot over 300 yd 30 lb braid, 4-5 ft 20 lb fluoro with the knot-outside-the-tip length rule and a 5-6 ft rebuild floor, seven-row hook table, four-placement bait table with wishbone and shoulder mechanics, depth cues (30-40 ft under the boat, 80-100 ft down, boils 50-150 yd), drag-scale weakest-link method, plus Rig 2/Rig 3 escalation. sourced: per-row video ids and note paths, including for the internal conflict. scoped: only answer to state the region/waters gate explicitly (socal-bight, baja-pacific-north; open-ocean, bank); the 'five years running as of 2023-03' phrasing carries an as-of; no regulation asserted. honest: eleven gaps, flags the unresolved species-router vs flyline-note class conflict as an open fact-check, preserves the size 2 vs 4 and clinch-vs-jam breakpoint conflicts, names the profile gear gap rather than substituting. actionable: highest — a reader can build the rig, bait it for the specific swim they need, set drag, and step up a rung if the grade jumps.

<details><summary>Full prompt</summary>

Set me up a flyline rig for 20-30 lb bluefin: hook size and style, leader material and test, main line class, and how to rig the bait.

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

## Flyline rig for 20–30 lb bluefin

Short version of what the KB converges on for exactly this grade: **a small circle hook (No. 4 to 2/0, thin-to-medium wire, bronze/black), tied straight — no swivel, no bead, no weight — to 4–6 ft of 20–30 lb fluorocarbon, off a 30 lb mono top shot (50+ yd) over braid backing, with the hook sized to the bait in your hand rather than to the fish.** Details, numbers and the places the sources disagree, below.

---

### 1. Main line class

Two legitimate builds; the KB keeps both, and the reason to pick one is depth, not strength.

- **Preferred for flylining — long mono top shot over braid backing.** 30 lb monofilament top shot, **50+ yards, more if possible**, over braid backing, then a short fluoro leader matched to the top shot — this is the stated build for **20–50 lb grade** bluefin ([techniques/flyline.md](techniques/flyline.md), `jQW2HLkMsmY`). A later restatement of the same setup runs **80–100 yards of 30 lb mono** then 4–6 ft of fluoro (`LTCFjqtSI8g`).
- **Why mono and not straight braid:** mono comes off the reel more easily and doesn't stick to itself, so the bait swims naturally (`jQW2HLkMsmY`); and braid **floats** while mono sinks. The worked depth math: braid main line + a 10 ft fluoro top shot, 200 ft back, holds the bait only **10–12 ft** down; straight mono at the same 200 ft back puts it **50–60 ft** down (`48ZFXnCTTQE`, [techniques/flyline.md](techniques/flyline.md)). That difference is what matters when bluefin won't come up; on a wide-open corner bite either rig works.
- **Straight braid → fluoro is explicitly called "totally fine"** — it maximizes capacity, it's just less efficient for flylining specifically (`jQW2HLkMsmY`).
- **Braid class: downsize, don't upsize.** 65 lb braid is roughly 20 lb mono in diameter; fish the lightest the job allows — mostly **30 or 50 lb** ([tackle/line-and-leader.md](tackle/line-and-leader.md), `aXF0bxAFtU0`). The daytime sportboat roundup's "favorite flyline rod" is spec'd **25–40 lb rod, 30 lb braid, 25–30 lb fluoro** ([tackle/rod-and-reel-selection.md](tackle/rod-and-reel-selection.md)).
- **Working line test for a finicky bluefin bite: 25–30 lb, sometimes dropped to 20** (`LsFMBCa9DOQ`, [tackle/hooks.md](tackle/hooks.md)). The tightest stated cap is **20–25 lb fly line, no more than 30** for tough bites (`48ZFXnCTTQE`, [techniques/flyline.md](techniques/flyline.md)) — the counterintuitive part being that thinner gets bit *more*, because a bait in warm water hasn't toughened up and can't swim thick line convincingly.
- **Carry a second, heavier stick.** Bluefin gear is explicitly **not** scaled down on a mixed trip — grade is unpredictable, so tackle stays sized for the biggest fish that could show ([species/bluefin-tuna.md](species/bluefin-tuna.md), `PrdPJy26H8c`). The two-rod flyline system that covers 25–80 lb: light stick 8–8'6" rated 20–50 lb with the 30 lb mono top shot (your 20–30 lb fish); heavy stick 7 ft rated 30–80 lb running **40 lb (sometimes 50) fly line direct** (`jQW2HLkMsmY`).

**Rod/reel character matters more than class here** ([tackle/rod-and-reel-selection.md](tackle/rod-and-reel-selection.md), `48ZFXnCTTQE`): **star drag, not lever** — you need the spool to free-spool on the barest touch so a swimming bait can pull line; **4.5:1 to 5:1 gear ratio** (6:1 is a little fast); and a **glass or composite rod with a slow taper and soft tip** — a graphite tip whip-cracks the bait on the cast, so it lands stunned or comes off the hook.

### 2. Hook — size and style

**The bait sets the hook size; the target fish is secondary** ([tackle/hooks.md](tackle/hooks.md), `HIXTFWlwnM0`, `m2q22sPPkEM`). For 20–30 lb bluefin on a sardine/anchovy chum line, the corpus numbers cluster small:

| Source situation | Hook |
| --- | --- |
| Flyline outfit for the **20–50 lb grade** specifically | **Size 4** Owner Mutu circle; step to 1/0–2/0 on the heavy stick (`jQW2HLkMsmY`, [tackle/hooks.md](tackle/hooks.md)) |
| Cortez Bank trip whose grade was **20–30 lb, ~25 lb average** | **No. 4 and No. 2**, on 20 lb fluoro (`QSvzVHW9UMk`, `LsFMBCa9DOQ`, [species/bluefin-tuna.md](species/bluefin-tuna.md)) |
| Dedicated 25–30 lb fluoro flyline stick, ~90% of daytime bites | majority on **size 2 circle**; size 1 up to 1/0 also used (`149px8WQ2Ng`) |
| Daytime bluefin, 25–40 lb test | **straight No. 2**; an angler credited a **No. 2 / No. 4 circle with ~90% corner-of-the-mouth** hookups (`oB4BpIUTTl4`/`r4J5nP5Bkl4`) |
| First bluefin trip, general advice | **1/0 or 2/0 circle, not J** (`EyB98RuKfeQ`) |
| Sportboat sardine, bluefin | **4/0 thin-wire circle**, straight-tied (`ftEvyfwjZFU`) |
| Sardine ~5–7 in, sizing table | **2/0** for smaller-grade/picky tuna, 4/0–5/0 for mid-grade ([tackle/hooks.md](tackle/hooks.md)) |

**My call for your fish:** start at **No. 2 circle** on typical sportboat sardines, drop to **No. 4** if the bite is finicky or the bait is small anchovy, step to **1/0–2/0** if you're handed big "donkey" sardines or mackerel. The reason the numbers spread from No. 4 to 4/0 is bait size, not fish size.

**Wire gauge — one real caution at this size.** Thin wire lets a sardine swim naturally, but on the 20–30 lb Cortez grade a crew specifically preferred a **stouter No. 4**, because some No. 4s run light wire and even at **25–30 lb line test** there's enough pressure on the hook to matter (`QSvzVHW9UMk`, [species/bluefin-tuna.md](species/bluefin-tuna.md)). That's corroborated by the thick-shank doctrine for small baits under sustained drag — a too-thin hook can come back as "an eye of the hook and no hook, no bend" (`_PGm-TlFU2A`, [tackle/hooks.md](tackle/hooks.md)).

**Finish:** bronze or black, **never nickel/chrome** for bait fishing — chrome reflects, bronze goes invisible on entry, and a bronze hook left in a fish rusts away in about a week (`IMnoZVEYpm4`, [tackle/hooks.md](tackle/hooks.md)).

**Circle vs J — the KB keeps a real conflict here, so here's the decision frame:**
- **Circle is the doctrine for bluefin** and the default I'd run: it pins the **corner of the mouth**, which keeps the leader out of the teeth — bluefin (unlike yellowfin) have a lot of teeth and saw through leaders (`RbqOKkINSCM`, high confidence; corroborated `RfiC8sfIWTk`, and a trip-wide "circle hooks always for bluefin, J for yellowtail" briefing, `UfuiWFVvz2E` — all [tackle/hooks.md](tackle/hooks.md)). Physical corroboration: a 40 lb bluefin came aboard still carrying another angler's broken-off hook (`c3NFkQbdDy0`).
- **The dissent, on this exact grade:** the crew on the 20–30 lb Cortez bite preferred **J hooks** — faster to pin a bait than a small circle, and less handling time means a livelier bait and more bites (`LsFMBCa9DOQ`). At the smallest sizes a J's gap is genuinely bigger and easier to bait (`48ZFXnCTTQE`).
- **What the choice turns on:** whether you can feel the bite and want to set (J), versus wanting the hook to do the work and the leader kept off the teeth (circle). Order above is not a ranking of correctness — it's doctrine vs. one crew's stated preference.
- **Strike timing changes with the choice:** circle = give it a **10 count**, then engage and wind tight, never swing; small J = a **3 count** before you put it in gear (`48ZFXnCTTQE`, [tackle/hooks.md](tackle/hooks.md)).

### 3. Leader — material and test

**Fluorocarbon, and it's not optional gear on finicky SoCal pelagics** — "you won't get bit without it" on bluefin (`EyB98RuKfeQ`, [tackle/line-and-leader.md](tackle/line-and-leader.md)). One captain on a 25–40 lb-test day did call it optional ("if you don't have fluoro it's not a detrimental death sentence," `oB4BpIUTTl4`) — the minority view.

- **Test: 20–30 lb.** The 20–30 lb-grade Cortez trip ran **20 lb fluoro** (`QSvzVHW9UMk`); a dedicated flyline stick ran **25–30 lb** (`149px8WQ2Ng`); San Clemente sardine flyline standard was **30 lb fluoro** to ~3/0 (`V_ONnegk95M`, corroborated `nsUdT-zXI8s`); **25–30 lb fluoro** was called "key, it's a must have" on another trip (`_PGm-TlFU2A`, all in [techniques/flyline.md](techniques/flyline.md)). Between 25 and 30: **25 gets bit a little better, 30 gives you leverage** (`A70kK2niu2Q`).
- **Match the leader within 5 lb of the mono top shot** (`LTCFjqtSI8g`).
- **Length: 4–6 ft.** Only ~3 ft is needed for the fish; the extra is buffer, because fishing 25 lb means cutting and re-tying the hook after every fish to clear nicks, and you don't want a full leader replacement mid-trip (`LTCFjqtSI8g`). Counter-parameter to respect: keep it short enough that **the knot never sits past the tip guide**, where it hangs up on the cast (`RbqOKkINSCM`). A light-flyline alternative in the KB is 4–5 arm lengths of 25–30 lb ([tackle/line-and-leader.md](tackle/line-and-leader.md), `xPFm_ZV2PZU`).
- **Optional upgrade if you're breaking off — the bite guard.** Braid and fluoro have almost no stretch, so the shock of the bite lands entirely on the mono-to-fluoro connection; that's what parts light leaders, not the fluoro being too light. The fix: **25 lb mono top shot → 2–3 ft of 50 lb fluorocarbon**, joined with the **Seaguar knot** — the 25 lb is what pulls through the water (bait swims like it's on 25), the heavy short section rides in the mouth and along the gill plates. Applied variants on 30+ lb tuna: **30 lb main → 40 lb leader**, **25 lb main → 40 lb leader** (`48ZFXnCTTQE`, [techniques/flyline.md](techniques/flyline.md), [rigging/essential-knots.md](rigging/essential-knots.md)).
- **Kept side by side, not applicable to you:** the straight **80 lb fluoro, 3–4 ft, no top shot** flyline rig (`RbqOKkINSCM`) — that's a **mackerel** bait thrown into a boatside foamer, not a finicky sardine game for 25 lb fish. Different bait, different situation. Likewise the **200 lb bite-leader class** in [rigging/bite-leaders.md](rigging/bite-leaders.md) is for big-fish deep/kite work, not this.

### 4. How to rig the bait

**Terminal rigging — strip it to nothing:**
1. **No weight, no swivel, no beads** — hook to fluoro to main line and nothing else in line (`RbqOKkINSCM`, `ftEvyfwjZFU`, [techniques/flyline.md](techniques/flyline.md)).
2. **Tie the hook with a San Diego jam:** through the eye and back to make a doubled section, **6 wraps** down the standing line (one registered captain ties **5**, reasoning fewer wraps cross over when you're tying fast — angler preference, not a fixed number), pass through the lower loop then the upper loop, **lubricate**, slide the coils down tight to the eye before setting. Any slack left uncinched is where it breaks under shock load ([rigging/essential-knots.md](rigging/essential-knots.md), `VpW91AKOFVQ`, `1BH7nQdIg5Q`).
3. **Non-ringed hook:** use the loop knot instead — overhand 6–8 in from the tag, tag through the eye and back through the overhand the same way it exited, 4–6 wraps around the standing line (fewer on heavier line), back through the overhand, lubricate with chapstick (spit under-lubricates fluoro) (`48ZFXnCTTQE`).
4. **Straighten the fluoro before tying** — it comes off the spool twisted; rub it between your fingers to warm the kink out so the knot seats clean (`RbqOKkINSCM`).
5. **Braid-to-mono/fluoro joins:** RP knot if it runs through the guides, double uni if it stays outside (9 turns braid side, 5 turns mono side); Seaguar knot specifically for mono-to-fluoro ([tackle/line-and-leader.md](tackle/line-and-leader.md), [rigging/essential-knots.md](rigging/essential-knots.md)).

**Hooking the bait — pick the position for the swim you want** ([bait/fishing-live-bait.md](bait/fishing-live-bait.md), [techniques/flyline.md](techniques/flyline.md)):
- **Nose hook — the default.** On a sardine, through the **clear spot at the tip of the nose, side to side, right before the eyes** — not chin-to-top; that's "the only way" to nose-hook one (`ZggReeO1nyU`, `SluBXkT3cuw`). Bait swims naturally and stays up.
- **Butt hook — when they're down.** Side to side just above the vent, under the two rear fins: the bait swims **opposite the pull**, i.e. down and away from the boat, and it defeats sea lions picking off nose-hooked baits at the islands (`T3p1mrqNjIo`, `8YvmROeVL-0`, `w5_x6kkN-xE`, `ZggReeO1nyU`). Directly relevant to your grade: an angler butt-hooked specifically because the captain called the fish **80–100 ft down and not coming to the chum line**, and credited that for the hookup (`oB4BpIUTTl4`/`r4J5nP5Bkl4`). Trade-off: the butt hook draws blood, so the bait doesn't last as long. **Zero weight only** — the moment any weight goes on, switch back to the nose hook, or a butt-hooked bait dragged by a sinker swims backwards.
- **Shoulder/dorsal** keeps your line up out of the water and skates the bait high for a reaction bite; **belly** (just above the anal fin) also sends it down and away.
- **Baiting a circle hook:** hold the hook **high on the arch and press straight down** into the bait. Holding it from the bottom like a J leaves no gap and squeezes the bait into a "potato chip" (`8YvmROeVL-0`).

**Bait handling — this is most of the game:**
- **Net the bait, don't hand it.** Leave the net in the water, come up under the bait, carry it to the rod in the net. Lifting a bait out to look it over knocks its scales off and starts killing it before it's hooked. Get it back in the water immediately once hooked — don't dangle it while you sort the reel (`6ueGWJek1gI`, [bait/fishing-live-bait.md](bait/fishing-live-bait.md)).
- **Cull hard.** Fish the lively lime-green ones that are hardest to catch in the tank; scales intact, good color, slime (`V_ONnegk95M`). **If a bait isn't pulling line off the reel within ~60 seconds, wind it in, flick it off, get a fresh one** — "the guys that change baits often are the ones that are going to catch more fish" (`LsFMBCa9DOQ`).
- **Distance beats weight.** Get the bait out **beyond everybody else's**, into its own zone; fish are finickier close to the hull. Adding a split shot to help the cast is framed bluntly as a crutch, not an upgrade (`gKrYKvqHUjk`, [techniques/flyline.md](techniques/flyline.md)).
- **Keep tension the instant a butt/belly bait lands** — a little pull makes it swim away like a propeller; give it slack and it turns and swims back under the boat (`8YvmROeVL-0`).
- **Conditions exception to "no weight":** with current sweeping the line flat, crews have added a **½ oz** weight to a flyline, and a **½–¾ oz rubber-core/sliding sinker** to get sardines down to a better grade holding deeper (`Rb5I2ljAqeE`, `Ow3an9lSVh4`). Both are logged as exceptions, not the rule.

**Drag, before you fish it.** Set it before the bite, not during — the pre-trip briefings hammer this (`V_ONnegk95M`, `M7BtON4GZgQ`). The rule in [tackle/rod-and-reel-selection.md](tackle/rod-and-reel-selection.md) (`VpW91AKOFVQ`): target **a quarter to a third of your lowest line-class rating**, starting at the light end. On a 25 lb leader that's roughly **6–8 lb of strike drag**; on 30 lb, roughly **7.5–10 lb**. Bump up one click at a time if you're in a stalemate. Or the feel test: pull the line off by hand — it should come off **steadily but not easily, without cutting into your hand** (`o8vLdz7OmaE`).

### 5. On your own gear (Cameron's profile)

Your flyline stick is the **Avet MXJ 5.8 MC on the Teramar TMC90MHB2** (9'0", MH, fast, 30–65 lb class), currently carrying **50 lb braid** ([profiles/cameron/rods.md](profiles/cameron/rods.md)). That braid is heavier than the 30 lb-braid flyline spec above, which is exactly the case the mono-top-shot build solves: run **50+ yards (ideally 80–100) of 30 lb mono** over that 50 lb braid, then **4–6 ft of 25–30 lb fluoro** to a **No. 2 (to 1/0) circle**. The Trinidad 40 (80 lb braid, 8'0" XH 40–80) is listed as your **heavy flyline** setup — that's the second stick for the 40 lb-direct build if a bigger grade shows.

---

### Where the KB is thin on this question

- Every hook-size and leader number for the **20–30 lb grade specifically** comes from on-the-water trip observations on **unregistered channels (medium confidence)**, not from registered doctrine. The KB deliberately keeps them side by side rather than reconciling No. 4 vs 4/0 — so treat my "start at No. 2" as my read of the cluster, not a KB rule.
- The KB has **no doctrine-level note that pairs a bluefin grade band to a hook size** the way it does for bait size; the routing is bait-first by design.
- **Hook and fluoro brands** are either sponsor-flagged (low confidence) or ASR-garbled; the only non-sponsored brand-level entry is Owner Mutu circles (medium), and Mustad/VMC named for thick-shank durability.
- **No US/California regulation on circle-hook requirements for bluefin** appears anywhere in the KB. The only circle-hook mandate logged is a Mexican one, from a 2019 video, flagged as unverified — verify current CDFW rules yourself before fishing.
- Nothing in the KB covers **hook sharpening or replacement cadence**, or **hook brand/model for the sub-1/0 sizes** beyond what's above.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `techniques/flyline.md`, `tackle/hooks.md`, `tackle/line-and-leader.md`, `tackle/rod-and-reel-selection.md`, `tackle/gear-classes.md`, `bait/fishing-live-bait.md`, `rigging/essential-knots.md`, `rigging/bite-leaders.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `jQW2HLkMsmY`, `LTCFjqtSI8g`, `48ZFXnCTTQE`, `aXF0bxAFtU0`, `LsFMBCa9DOQ`, `QSvzVHW9UMk`, `149px8WQ2Ng`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `EyB98RuKfeQ`, `ftEvyfwjZFU`, `HIXTFWlwnM0`, `m2q22sPPkEM`, `_PGm-TlFU2A`, `IMnoZVEYpm4`, `RbqOKkINSCM`, `RfiC8sfIWTk`, `UfuiWFVvz2E`, `c3NFkQbdDy0`, `V_ONnegk95M`, `nsUdT-zXI8s`, `A70kK2niu2Q`, `xPFm_ZV2PZU`, `ZggReeO1nyU`, `SluBXkT3cuw`, `T3p1mrqNjIo`, `8YvmROeVL-0`, `w5_x6kkN-xE`, `6ueGWJek1gI`, `gKrYKvqHUjk`, `Rb5I2ljAqeE`, `Ow3an9lSVh4`, `VpW91AKOFVQ`, `1BH7nQdIg5Q`, `o8vLdz7OmaE`, `PrdPJy26H8c`, `M7BtON4GZgQ`, `cameron`  
*gaps admitted:* No doctrine-level note pairs a bluefin grade band (20-30 lb) to a hook size; hook sizing in the KB is bait-first by design, so the grade-specific numbers are trip observations rather than a rule. | All the 20-30 lb-grade hook and leader figures come from unregistered-channel on-the-water observations at medium confidence, and the KB deliberately leaves the No. 4-to-4/0 spread unreconciled. | Hook and fluorocarbon brand/model recommendations are either sponsor-flagged (low confidence) or ASR-garbled in the corpus; only Owner Mutu circles and Mustad/VMC thick-shank durability survive as usable brand data. | The KB contains no US/California (CDFW) regulation on circle-hook requirements for bluefin - the only circle-hook mandate logged is a 2019 Mexican one, flagged unverified. | Nothing in the KB covers hook sharpening or hook replacement cadence for a live-bait flyline program. | No KB note gives a numeric strike-drag figure for a 20-30 lb bluefin flyline outfit; the drag numbers above are my arithmetic on the general quarter-to-a-third-of-line-class rule.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Flyline rig for 20–30 lb bluefin

You didn't give me conditions, a date, or a zone, so this is a pure tackle answer — I'm not picking water or timing for you. Grade-wise, 20–30 lb bluefin sits squarely in the KB's **finesse / light-flyline band**, below the 40 lb line where the corpus starts stepping gear up.

Two notes before the build: (1) I resolved gear against the only profile in the KB, `profiles/cameron/rods.md`, and there's a real gap there — flagged at the bottom. (2) The KB has no single note that says "here is the 20–30 lb bluefin flyline rig." I'm assembling it from the finesse-rig ladder, the flyline technique note, and the hook/leader notes, and I'll show you where the sources disagree rather than smoothing it.

---

## Short answer

| Component | Spec |
| --- | --- |
| **Main line** | 30 lb braid backing (300 yd), 50 yd top shot of **20 or 25 lb** mono — braid one class heavier than the top shot |
| **Leader** | **4–5 ft of 20–25 lb fluorocarbon**, same test as the top shot, sized so the connecting knot never passes the tip guide on a cast |
| **Hook** | **Size 2** — either an **Owner Gorilla Light J** (Carson's finesse pick) or a **size 2 / size 4 Owner Mutu circle**; thin wire either way |
| **Knots** | 4-turn surgeon's knot mono→fluoro; **single-pass** San Diego jam at the hook |
| **Weight** | None. Zero. Straight hook to leader — no swivel, no bead, no split shot |
| **Drag** | ~25–33% of the lowest link: **5–7 lb strike drag** on a 20 lb top shot, ~6–8 lb on 25 lb |

---

## 1. Main line class

The corpus is tight on this for a finicky bluefin bite:

- **Cap the flyline at 20–25 lb test, no more than 30** — that's boat-skipper guidance for tough bites, cited by Cesar of Eric's Tackle (`48ZFXnCTTQE`, [`techniques/flyline.md`](techniques/flyline.md)). The reason is mechanical, not superstition: in warm water live bait doesn't get time to "cure" and toughen, so a bait on line that's too thick doesn't swim convincingly and won't draw the bite.
- Vince at Fisherman's Landing puts the working range at **20–25 lb test against bluefin grading 40–60 lb** (`icpm7gADxvU`, same note) — so 20–25 is not under-gunned at your grade, it's the point of the exercise.
- A Highliner deckhand's daytime numbers: ~90% of daytime bites came on flyline off a dedicated **25–30 lb fluorocarbon flyline stick** (Ray Sharifi, `149px8WQ2Ng`, [`species/bluefin-tuna.md`](species/bluefin-tuna.md)).

**Build the spool this way** (Steve Carson / Penn, `dg1sbr6GuB8` + `9JnIS8HkZlA`, [`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md), [`tackle/searcher-finesse-live-bait-outfit.md`](tackle/searcher-finesse-live-bait-outfit.md)):

- **300 yd of 30 lb braid** backing, filled about ¾ up the spool.
- **50 yd top shot** of 20 or 25 lb mono — deliberately *longer* than his other rigs. Stated reason: more stretch, because the hook is small; without stretch in the system a hooked fish pulls the small hook right out of its mouth.
- **Braid one class heavier than the top shot** — his general rule, cited independently for both this rig and the 40 lb starter rig (`QHY5kmU7OTU`).
- Carson's own preference inside that band is **20 lb, not 25** — "you get a lot more bites with 20 lb than 25, I don't know why" — which he explicitly keeps apart from what the captains publicly tell everybody (25 lb). Attributed preference, not a correction of the captains.

Capt. Matt of SD Fish and Sips runs the same class differently: **30 lb braid straight to 15–25 ft of fluorocarbon** on a 25 lb all-purpose flyline setup, no mono top shot (`G1YIlakiRqg`, same ladder note). His stated logic is a happy medium — long enough the fish doesn't see the Spectra, short enough that a flylined sardine isn't dragging thick line through the water. Both builds are in the KB; pick one, don't blend them.

## 2. Leader — two different philosophies, and what the choice turns on

**Build A — matched leader (the finesse standard).** 4–5 ft of fluorocarbon at the **same test as the top shot** (20 or 25 lb), tied with a **4-turn surgeon's knot** (`9JnIS8HkZlA`, `dg1sbr6GuB8`, `QHY5kmU7OTU`). Carson's leader-length rule is about the cast, not the fish: size the fluoro so the connecting knot **stays outside the rod tip** — roughly 3 ft on a 7 ft rod, 4 ft on an 8 ft rod, 5 ft on a 9 ft rod ([`tackle/searcher-finesse-live-bait-outfit.md`](tackle/searcher-finesse-live-bait-outfit.md)). The 4-turn count is his stated rule for 20–100 lb test (5 turns under 20 lb) — corroborated four separate times in [`rigging/surgeons-knot-mono-to-fluoro.md`](rigging/surgeons-knot-mono-to-fluoro.md).

**Build B — light main to a short heavy bite guard.** **25 lb monofilament** top shot to a **50 lb fluorocarbon section 2–3 ft long**, joined with a [Seaguar knot](rigging/seaguar-knot.md) (Cesar, `48ZFXnCTTQE`, [`techniques/flyline.md`](techniques/flyline.md)). The reasoning is worth understanding: braid has no stretch and fluoro has very little, so on the shock of a bite the strain lands entirely on the mono-to-fluoro connection — that's what parts light leaders, not the fluoro being "too light." The 25 lb mono is what's actually pulling through the water so the bait swims like it's on 25 lb, while the short 50 lb section rides inside the fish's mouth and along the gill plates and teeth. Applied variants from the same source: **30 lb main → 40 lb leader** and **25 lb main → 40 lb leader**, with the heavier-leader step "dramatically" improving landings.

**The decision frame** (section order here is not a ranking): Build A is the higher-bite-rate, lower-margin rig — it's what gets eaten when fish are genuinely picky, and it accepts that a much bigger fish will probably beat you. Build B buys abrasion insurance at the mouth without changing what the bait feels, and is the one to reach for if the school is mixed-grade and you expect a 60–80 lb fish could eat. Bluefin specifically justify the bite guard — they have "so many teeth" and will bite through anything lighter (Capt. Dave Hansen, `ftEvyfwjZFU`).

Cross-check from [`tackle/line-and-leader.md`](tackle/line-and-leader.md): for finicky daytime live bait on light flyline gear, **4–5 arm lengths of 25–30 lb** fluoro (`xPFm_ZV2PZU`) — longer than Carson's 4–5 ft, in the same family as Capt. Matt's 15–25 ft. Thin-diameter, low-memory fluoro cinches best on the tiny hooks a sardine can carry.

**Practical:** fluorocarbon comes off the spool twisted — warm it by rubbing it between your fingers before tying so the knot seats cleanly (Dave Hansen, `RbqOKkINSCM`).

## 3. Hook — size and style

**Size: 2.** That's where the corpus converges for this grade.

- Carson's 15 lb finesse rig (framed for **school-size tuna, roughly 15–40 lb**, in a big school but not biting well): a **J hook, Owner Gorilla Light, size 2** — "a nice light hook that lets your bait swim" (`9JnIS8HkZlA`, `dg1sbr6GuB8`, [`tackle/hooks.md`](tackle/hooks.md)). ⚠ Unresolved in the corpus: an earlier 2020 citation of the same rig has him naming and fishing a **size 4** (`ptoIvB2MspE`), and he later says he'd use a 4 "if it came in that size." Both sizes are kept side by side, not reconciled — either is inside the corpus.
- Circle side: **Owner Mutu size 4** on the lighter (20–50 lb grade) flyline outfit, stepping to 1/0–2/0 only for bigger fish (Ray Sharifi, `jQW2HLkMsmY`). The Highliner deckhand's day: majority on **size 2 circles**, with size 1 up to 1/0 also used (`149px8WQ2Ng`). A Cortez Bank trip on bluefin and yellowtail together ran **25 lb test mono or fluoro leader to a #2 circle** (`nQvJnfb5jQ4`).
- If your sardines are small or weak, the **Gamakatsu Nautilus** is named as a **lighter-wire** circle alternative to the Owner, sized 4 through 3/0 (`G1YIlakiRqg`).

**Wire gauge: thin.** A thin-wire hook adds almost no weight to the bait's nose so it swims naturally and draws more bites; straightening one under a normal drag is rare (`sWRSYCmt4Tw`, `m2q22sPPkEM`, [`tackle/hooks.md`](tackle/hooks.md)). ⚠ One counterpoint worth knowing: Capt. Jeff Marklin, fishing 3–4 in anchovies for fish to 40 lb on 30 lb leader against 65 lb Spectra, argues a thin-wire hook lacks the surface area to take sustained heavy drag and comes back as "an eye of the hook and no hook" (`_PGm-TlFU2A`). Kept beside the thin-wire rule, not folded into it.

**Circle vs J — the actual decision:**

- **Circle** is the offshore live-bait default and the bluefin-specific pick, because the corner-of-the-mouth hookset keeps the leader off the teeth and away from a bite-off (Ray Sharifi `RfiC8sfIWTk`; Dave Hansen `RbqOKkINSCM` — he normally prefers J hooks and switches to circle specifically for bluefin). It requires the drag to be doing the work, since there's no manual set to fall back on.
- **J** wins on **baiting speed** at this class: a small J goes on a lively bait fast, no need to scale the bait first, and gets it back in the water quicker; a circle's smaller point-to-shank gap makes it trickier to thread (Vince, `icpm7gADxvU`). That's the explicit reason behind Carson's Gorilla Light J on the finesse rig.
- **Frame:** if you're at 20–25 lb and expect only 20–30 lb fish, the J is defensible and baits faster. If a bigger fish could eat — and on SoCal bluefin one usually can — go circle for the teeth. Order above is not a ranking.

**Hook-size sanity check against the bait**, since the bait sets the size and the fish is secondary (`HIXTFWlwnM0`, `m2q22sPPkEM`): sardine ~5–7 in → **2/0** for smaller-grade or picky tuna (up to 4/0–5/0 only for mid-grade bluefin); anchovy → **No. 4 thin wire**; sizes 1/2 → "scaling way down for finicky small-grade fish." Note the unit clash — Carson's "size 2" is a number size (small), not 2/0. At 20–30 lb grade on sardine you're choosing between roughly a **No. 2–4 number size** (finesse) and a **2/0** (standard sardine flyline).

## 4. Terminal knots

- **Mono top shot → fluoro leader:** 4-turn surgeon's knot for 20–100 lb test, 5 turns under 20 lb ([`rigging/surgeons-knot-mono-to-fluoro.md`](rigging/surgeons-knot-mono-to-fluoro.md), `9JnIS8HkZlA` + three independent corroborations).
- **Leader → hook:** the **single-pass** San Diego jam, not the doubled version. Capt. Art's stated reason: the doubled knot is about **three times the size** of the single on the same hook, and asking a live bait to drag both an oversized knot and a bigger hook around is exactly what the fish sees (`6T3xZ9vufrM`, [`rigging/san-diego-jam-single-vs-double.md`](rigging/san-diego-jam-single-vs-double.md)). Wrap counts in the corpus run **5–7** depending on the tier — 5 (Pete Gray `AGaVlYu61O4`, Scotty `VpW91AKOFVQ`), 6 (base entry, `1BH7nQdIg5Q`), 7 (Capt. Armando `YeV--HarEYQ`) — kept as angler preference, not one number. Keep tension throughout, wet it, then slide the coils down to the eye.
- **Nothing else in line.** Hook tied straight to fluoro, fluoro to main line — no swivel, no beads (`ftEvyfwjZFU`, `RbqOKkINSCM`).

## 5. How to rig the bait

**Sardine (the SoCal staple for tuna, per Dave Hansen's species-bait pairing, `gKrYKvqHUjk`):**

- **Nose hook — the all-purpose flyline placement.** Through the **clear spot at the tip of the nose, right in front of the eyes**, and on a sardine specifically it goes **side to side** through that spot — not chin-to-top. Hansen: that's "the only way" to nose-hook one (`ZggReeO1nyU`, [`bait/fishing-live-bait.md`](bait/fishing-live-bait.md)). Same spot works on mackerel and anchovy (`SluBXkT3cuw`). The bait swims naturally and stays up; it also keeps drawing bites on the retrieve when you wind in to swap it (`MuC0uGKDzxg`).
- **Belly hook — just above the anal fin** — if you want the bait down and away, or want a reaction bite. A PCS Show panel's reasoning for preferring belly over butt on tuna specifically: the belly-hooked bait "shoots out" with an urgency that triggers a reaction strike, and the hook catches only a little cartilage instead of risking internal organs and bleeding the bait (`UP_3fBu7VPA`). Most deckhands belly-hook the bait they hand you nine times out of ten.
- **Butt hook — near the vent** — down and away, and it **defeats sea lions** at the islands that pick off nose-hooked baits (`T3p1mrqNjIo`, `8YvmROeVL-0`). Sardine mechanism: hooked there it swims **opposite the direction of pull**. Trade-off: it draws blood, so the bait doesn't last as long. **Zero-weight only** — the instant any weight goes on, switch back to the nose, because a butt-hooked bait dragged by a sinker swims backward (`w5_x6kkN-xE`).
- **On a circle hook, bait it correctly:** hold the hook **high on the arch and press straight down** into the bait. Holding it from the bottom leaves no gap and mangles the bait ([`techniques/flyline.md`](techniques/flyline.md)).
- **Cast underhand** on belly and butt placements — both sit in thin tissue, unlike the cartilage at the nose, and a hard overhand swing tears the bait off the hook (`SAltQjih0ms`, [`techniques/underhand-casting.md`](techniques/underhand-casting.md)). Carson prefers underhand generally on this rig: letting the bait land gently and swim away on its own matters more than casting distance (`QHY5kmU7OTU`).

**Fishing it:**

- **No weight, and get it away from the boat.** Distance beats weight — the goal is your bait **beyond everybody else's**, in its own zone. Hansen frames a split shot or slider added for casting distance as a crutch for not knowing how to cast, not a technique upgrade (`gKrYKvqHUjk`).
- **Bait selection is king.** Cull the bloody, scaly, lethargic ones into the chum bucket; fish the lively lime-green ones that are hardest to catch in the tank. **If a bait isn't pulling line off the reel within about 60 seconds, wind it in, flick it off, grab a fresh one** ([`techniques/flyline.md`](techniques/flyline.md)). On a finicky bluefin bite a crew member put it directly: "the guys that change baits often are the ones that are going to catch more fish" (`LsFMBCa9DOQ`).
- **Don't swing on the bite.** Give a solid three-count, then come tight. On a circle that alone seats it in the corner of the mouth; on a J, raise the rod to about 45° and wind tight rather than an exaggerated hookset (Billy, Fisherman's Landing, `R48YdVFfEOI`, [`tackle/hooks.md`](tackle/hooks.md)).

## 6. Drag

Set it before you fish — this is the piece the corpus repeats hardest for circle hooks, because there's no swing to fall back on.

- **Rule: a quarter to a third of your lowest line-class rating**, starting at the light end (Scotty, `VpW91AKOFVQ`, [`tackle/drag-setting.md`](tackle/drag-setting.md)). Applying it to this rig: a **20 lb** top shot → **~5–6.5 lb strike drag**; a **25 lb** top shot → **~6–8 lb**. Carson's own target is the lighter 25% end rather than the full third, so you can advance the lever once the first run is over.
- If you're in a stalemate — cranking without gaining — bump one click at a time. If the fish makes a hard run, let the drag do its job.
- Carson on this class specifically: pair it with a reel that has a very good drag, have a crewman set it if you're unsure, and **every knot has to be perfect** — "everything has to be perfect if you're going to catch a 30 or 40 lb tuna on one of these finesse rigs" (`ptoIvB2MspE`).

## 7. Rod and reel class (no models — class terms only)

- **Reel:** a small conventional live-bait reel, **star drag, single-speed** — Carson is explicit you don't need a two-speed in this line category (`dg1sbr6GuB8`, `QHY5kmU7OTU`). Counterpoint, kept side by side: Capt. Matt now runs **two-speed even at 25 lb**, because 25 lb-class SoCal bluefin trips regularly hook 40–60 and even 80 lb fish; he's landed fish to **80 lb** on that exact setup (`G1YIlakiRqg`).
- **Rod:** **8 ft, rated 12–30 lb** — "as close to the middle of the line rating as you can get"; some prefer 7 ft or occasionally 9 ft (`QHY5kmU7OTU`, `dg1sbr6GuB8`). Capt. Matt's version is **8–8.5 ft rated 15–30 or 15–40 lb** (`G1YIlakiRqg`). **A rod tip too heavy for this small a hook rips the hook out** of the bait or the fish — that's the actual failure mode, not fish strength.

**Profile gap (`profiles/cameron/rods.md`):** the lightest setups in the profile are the Avet MXJ on a 9' Teramar (30–65 lb braid class, 50 lb braid, role: "mainly flyline"), the Lexa 400 on a 9' PCH (~20–60 lb, 50 lb braid), and the Tranx 400 on an 8'2" Phenix M1 (20–45 lb, braid TBD pending respool). **Nothing in that inventory is a 12–30 lb rod with 30 lb braid.** The finesse rig this grade calls for has no match in the box — the honest options are respooling the Tranx setup light for this program, or fishing the Avet/Lexa at 50 lb braid and accepting you're at the heavy edge of the bite. I'm not going to substitute a heavier outfit and call it the same rig. There is also **no hook or leader inventory recorded in `profiles/cameron/tackle.md`** — it covers hard baits only — so I can't tell you whether you already own size 2 Gorilla Lights, Mutus, or 20–25 lb fluoro.

## 8. The conflict you should know about

The KB's bluefin router lists the general bait/flyline class as **40–60 lb with circle hooks size 1–2/0**, not the finesse band above ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)). And there's an explicit doctrine against downsizing: unlike skipjack and schoolie yellowfin, **bluefin gear doesn't get scaled down on a mixed tuna trip — grade is unpredictable trip to trip, so tackle stays sized for the biggest fish that could show up** (Ray Sharifi, `PrdPJy26H8c`). A Cortez Bank captain called exactly this the core tackle challenge: 10 lb schoolies up to 80, "maybe even 100" lb fish moving through together on one size line (`947solNfiPw`).

Against that, Carson's premise: the wide-open bite anglers hear about happens **less than 10% of the time** — most days you need a finesse rig to get bit at all (`9JnIS8HkZlA`). And the corpus's clearest ceiling on the finesse rig is blunt: **don't fish it on fish over about 40 lb**; he's hooked "really really big" tuna on it and did not land them (`dg1sbr6GuB8`).

**What the choice actually turns on** — not which section came first: *what else is in the school.* If the boat is genuinely on a clean 20–30 lb grade and they're picky, fish 20–25 lb and get bit. If the marks are mixed and a 60–100 lb fish could eat, either take Build B's bite guard or step to the 40 lb starter rig and accept fewer bites. Two people fishing the same bank on the same day can be correctly on different rigs.

For reference, the corpus does contain a 20–30 lb bluefin taken exactly this way: an opening bite at Cortez Bank explicitly called a "fly line day" on camera produced yellowtail, a bluefin graded at **20–30 lb**, and an incidental sheephead, all flylined (`eL1Qm33-Mj0`).

---

### One last thing

This whole answer is gear. If you tell me the date, the zone you're running to, and the conditions, I can run the actual day-plan protocol against it — [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) wants conditions first, then priors, then species, then gear — and it may well tell you the flyline isn't the play that day.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `techniques/flyline.md`, `species/bluefin-tuna.md`, `tackle/bluefin-rig-ladder-by-grade.md`, `tackle/searcher-finesse-live-bait-outfit.md`, `tackle/hooks.md`, `tackle/line-and-leader.md`, `tackle/drag-setting.md`, `bait/fishing-live-bait.md`, `rigging/surgeons-knot-mono-to-fluoro.md`, `rigging/san-diego-jam-knot.md`, `rigging/san-diego-jam-single-vs-double.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `48ZFXnCTTQE`, `icpm7gADxvU`, `149px8WQ2Ng`, `9JnIS8HkZlA`, `dg1sbr6GuB8`, `ptoIvB2MspE`, `QHY5kmU7OTU`, `G1YIlakiRqg`, `nQvJnfb5jQ4`, `jQW2HLkMsmY`, `riEkdu8PEds`, `fyJA3o2hVh0`, `ftEvyfwjZFU`, `RbqOKkINSCM`, `RfiC8sfIWTk`, `sWRSYCmt4Tw`, `m2q22sPPkEM`, `HIXTFWlwnM0`, `EyB98RuKfeQ`, `_PGm-TlFU2A`, `R48YdVFfEOI`, `ZggReeO1nyU`, `SluBXkT3cuw`, `T3p1mrqNjIo`, `mscHk0qiXnk`, `raUPkuaFXpw`, `8YvmROeVL-0`, `w5_x6kkN-xE`, `UP_3fBu7VPA`, `MuC0uGKDzxg`, `SAltQjih0ms`, `gKrYKvqHUjk`, `LsFMBCa9DOQ`, `VpW91AKOFVQ`, `6T3xZ9vufrM`, `AGaVlYu61O4`, `YeV--HarEYQ`, `1BH7nQdIg5Q`, `PrdPJy26H8c`, `947solNfiPw`, `eL1Qm33-Mj0`, `xPFm_ZV2PZU`, `M7BtON4GZgQ`, `V_ONnegk95M`, `cameron`  
*gaps admitted:* No conditions, date, or zone were given, so no zone selection, timing, or BightSST-driven recommendation is made — the answer is tackle only. | The KB has no single note specifying a rig calibrated to a 20-30 lb bluefin grade band as its own rung; this build is assembled from Carson's 15 lb finesse rig (framed for 15-40 lb school tuna), the 25 lb sportboat flyline data points, and the flyline technique note. | Hook size for the Owner Gorilla Light is unresolved in the corpus — size 2 in the 2023 citation, size 4 actually fished in the 2020 citation; the KB keeps both side by side rather than reconciling them. | No specific strike-drag number is stated anywhere in the KB for a 20 lb or 25 lb top shot; the 5-7 lb and 6-8 lb figures are the quarter-to-a-third rule applied arithmetically, not a figure a source gave. | Number-size vs. ought-size hooks are used inconsistently across sources (Carson's 'size 2' vs. the bait-size table's '2/0' for sardine); the KB does not resolve which convention a given source means in every case. | profiles/cameron/rods.md contains no rod in the 12-30 lb class and no reel spooled with 30 lb braid, so the finesse outfit this grade calls for has no match in the recorded inventory. | profiles/cameron/tackle.md records hard baits only — there is no hook, leader-material, or line inventory in the profile, so I cannot confirm whether the specified hooks or 20-25 lb fluorocarbon are already owned. | No fluorocarbon brand or abrasion-test doctrine exists in the KB beyond low-confidence product endorsements (a Japan-manufacture preference with no mechanism stated). | The KB gives no wrap count specific to the single-pass San Diego jam at this light a line class — the 5, 6, and 7 wrap figures are logged as unreconciled angler preference across different line classes. | No note states how many flyline outfits to rig or how to stagger line classes for a 20-30 lb bluefin bite specifically; the one multi-class data point (three rods at 30, 40 and 25 lb) is a Baja East Cape tuna trip, not SoCal bluefin. | The KB gives no bait-tank or bait-quality guidance tied to this grade band beyond the general cull-and-swap rules; whether sardine or anchovy is the better match at 20-30 lb bluefin is not addressed.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# Flyline rig for 20–30 lb bluefin

You gave me a grade, not conditions, so this is the KB's grade-matched default rig — no conditions pulled, no BightSST call. Everything below is SoCal / northern-Baja offshore water, which is the gate on [`species/bluefin-tuna.md`](species/bluefin-tuna.md) (`regions: socal-bight, baja-pacific-north`; `waters: open-ocean, bank`).

**The good news: 20–30 lb is the one grade the KB has a purpose-built rig for.** [`tackle/searcher-finesse-live-bait-outfit.md`](tackle/searcher-finesse-live-bait-outfit.md) calls it the "20/25 lb rig" and frames it exactly at your fish — reached for when **25–30 lb tuna "are just being fish"** and won't eat anything heavier, tied to a recurring **last week of August through the last week of September** window with tuna running **20, 25, 30, sometimes up to 40 lb**, refusing anything heavier than 20–25 lb test (`QHY5kmU7OTU`). The same rig is **Rig 1 — 15 lb finesse** in [`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md), framed there for **school-size tuna roughly 15–40 lb** swimming in a big school but not biting well (`dg1sbr6GuB8`, `9JnIS8HkZlA`).

---

## 1. Main line — 20 lb top shot, 25 lb if you want the cushion

Braid backing to a **monofilament top shot**, not straight braid to fluoro:

- **Top shot: ~50 yd of 20 lb mono.** Steve Carson's emphasis is on the exact number — *"not 25, 20"* (`ptoIvB2MspE`); a later citation gives a **25–50 yd** range instead (`QHY5kmU7OTU`). A second, independent citation runs **300 yd of 30 lb braid backing topped with a 50 yd top shot of 20 or 25 lb** — deliberately a little longer than other top shots in the ladder, because the hook is small and you need the stretch in the system or a hooked fish pulls the small hook straight out of its mouth (`dg1sbr6GuB8`, [`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md)).
- **The ceiling on 20 lb: don't fish this rig on fish over about 40 lb** (`9JnIS8HkZlA`); a second voice puts the stop at **over 50 lb** (`QHY5kmU7OTU`). Your 20–30 lb grade sits comfortably inside it.
- **Braid: one class heavier than the top shot** — not 20 lb braid under a 20 lb top shot (`QHY5kmU7OTU`, `9JnIS8HkZlA`). 30 lb braid backing is the stated figure (`dg1sbr6GuB8`).
- **Why mono and not straight braid for flylining specifically:** mono comes off the reel more easily and doesn't stick to itself the way braid does, which helps the bait swim naturally. Straight braid-to-fluoro maximizes capacity and is "totally fine," just less efficient for this job (`jQW2HLkMsmY`, [`techniques/flyline.md`](techniques/flyline.md)).

**The 25 lb variant, same class:** [`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md) also carries a **25 lb all-purpose flyline setup** — 8–8.5 ft rod rated 15–30 or 15–40 lb, two-speed Fathom 15-class reel, **30 lb braid to 15–25 ft of fluorocarbon**, long enough that the fish doesn't see the Spectra, short enough that a flylined sardine isn't dragging thick line through the water. Two-speed even at this light class, because 25 lb-class SoCal bluefin trips regularly hook 40–60 and even 80 lb fish on 25 lb test; fish to 80 lb have been landed on that exact setup (`G1YIlakiRqg`).

**Rod:** **8 ft, rated roughly 12–30 lb** — "as close to the middle of the line rating as you can get"; 7 ft or 9 ft also fished by preference. A rod tip too heavy for this small a hook rips the hook out of the bait or the fish (`QHY5kmU7OTU`). Rig 1's corroborating citation gives the same **12–30 lb** rating (`dg1sbr6GuB8`). [`techniques/flyline.md`](techniques/flyline.md) adds the blank material reason: a graphite tip is too stiff to load on the cast of a live bait — the whip-crack either gives the bait "whiplash" so it lands stunned, or throws it off the hook. **Glass or composite**, slow taper — glass casts a bait best, composite is the easier all-rounder once a fish is on (`48ZFXnCTTQE`).

**Reel:** small conventional live-bait reel, no level wind — **Penn Fathom 15 / Squall II 15 class, star drag, single-speed**: "you don't need a two-speed reel in this line category" (`ptoIvB2MspE`, `QHY5kmU7OTU`, `dg1sbr6GuB8`). Kept side by side with `G1YIlakiRqg`'s two-speed-even-at-25 lb call above — the split is whether you expect the grade to jump on you.

## 2. Leader — fluorocarbon, matched or one step up

Two builds in the KB, both legitimate at your grade:

**A. Straight fluoro leader, matched to the top shot (the finesse-rig standard)**
- **4–5 ft of 20 lb fluorocarbon** on the 20 lb build (`ptoIvB2MspE`); narrowed to **~4 ft** in the later citation (`QHY5kmU7OTU`).
- **Length rule, not a fixed number:** size the fluoro so the connecting knot stays *outside the rod tip* on the cast — roughly **4 ft on an 8 ft rod, 3 ft on a 7 ft rod, up to 5 ft on a 9 ft rod**, varying with casting style (`QHY5kmU7OTU`, `9JnIS8HkZlA`, `fyJA3o2hVh0`). A knot that gets up past the tip guide hangs on the cast.
- **Don't let re-tying whittle it down:** repeated cut-and-retie after each fish can take a leader to 1–2 ft, at which length bites drop off — **5–6 ft is the stated floor to rebuild back to** (`UP_3fBu7VPA`, [`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md)). Ray Sharifi runs **4–6 ft** for the same reason — buffer so a full leader replacement isn't needed mid-trip (`LTCFjqtSI8g`).
- [`tackle/line-and-leader.md`](tackle/line-and-leader.md) puts light flyline gear at **4–5 arm lengths of 25–30 lb** fluoro for finicky daytime live bait (`xPFm_ZV2PZU`). Thin-diameter, low-memory fluoro cinches best on the tiny hooks a sardine can carry.

**B. Mono top shot + short heavy fluoro "bite guard" (the finicky-bite fix)**
From [`techniques/flyline.md`](techniques/flyline.md) (`48ZFXnCTTQE`): **25 lb mono main/top shot to a 50 lb fluorocarbon section 2–3 ft long**, joined with a [Seaguar knot](rigging/seaguar-knot.md). The mechanism matters — braid has no stretch and fluoro very little, so on the shock of the bite the strain lands entirely on the mono-to-fluoro connection; that's what parts light leaders, not the fluoro being "too light." The 25 lb mono is what's actually pulling through the water so the bait swims like it's on 25 lb, while the short 50 lb section rides inside the fish's mouth against gill plates and teeth. Applied trip variants: **30 lb main → 40 lb leader** and **25 lb main → 40 lb leader**, which "dramatically helped" land fish (Ray Sharifi, `48ZFXnCTTQE`).

**Fluoro is not optional-by-default for bluefin:** Dave Hansen's stated reason is that bluefin "have so many teeth" and will bite through anything lighter (`ftEvyfwjZFU`). One boat briefing does call it optional — "if you don't have fluoro it's not a detrimental death sentence" (`oB4BpIUTTl4`/`r4J5nP5Bkl4`) — kept side by side.

## 3. Hook — size 2 / No. 2 class, thin wire

Every citation at this grade converges on the **size-2-ish, thin-wire** window. The KB's rule is stated flatly: **match the hook to the bait, not to the fish** — a bait dragging an oversized hook won't swim right and won't get bit ([`tackle/hooks.md`](tackle/hooks.md), `HIXTFWlwnM0`, `m2q22sPPkEM`).

| Source build | Hook |
| --- | --- |
| Rig 1 / 20 lb finesse (`9JnIS8HkZlA`, `dg1sbr6GuB8`) | **Owner Gorilla Light J, size 2** — "a nice light hook that lets your bait swim"; size 4 substitutes |
| Same rig, earlier citation (`ptoIvB2MspE`) | **Owner Gorilla Light, size 4** actually fished — a discrepancy the KB preserves rather than reconciles |
| Line-class J sizing rule (`y0LVT59inEA`) | **25 or 30 lb test → a No. 1 or No. 2** Owner Gorilla live-bait J |
| Light-line bluefin, 20–25 lb test, finicky (`icpm7gADxvU`, `0AtmEH6aQt0`) | **Owner Hybrid Mutu circle, size 2** — a thinner gauge than the standard Mutu, for a better-swimming bait |
| Ray Sharifi's light flyline stick, **20–50 lb grade** (`jQW2HLkMsmY`) | **Owner Mutu circle, size 4**, stepping to 1/0–2/0 only on the heavy stick |
| Deckhand's daytime flyline stick, 25–30 lb fluoro (`149px8WQ2Ng`) | **size 2 circle**, sizes **1 to 1/0** also used |
| El Dorado daytime bluefin, 25–40 lb test (`oB4BpIUTTl4`/`r4J5nP5Bkl4`) | **straight No. 2**; a **No. 2 (or No. 4) circle** credited with a ~90% corner-of-mouth hookup rate that trip |

**Wire gauge: thin.** A thin-wire hook adds little weight to the bait's nose so the sardine swims naturally and draws more bites; straightening one is rare with a normal drag ([`tackle/hooks.md`](tackle/hooks.md), `sWRSYCmt4Tw`, `m2q22sPPkEM`). **Finish: bronze or black, never nickel or chrome** — chrome reflects underwater, bronze/black goes effectively invisible wet, and pressured SoCal bluefin are named as the case where it matters most (`IMnoZVEYpm4`).

**Circle vs. J — the KB keeps both, and here's what the choice actually turns on.** This is a live doctrine conflict, not a ranking:

- **The weight cutoff says J is fine for you:** circle hooks for fish **40 lb and up; a standard J is fine under 40 lb** (`YntRJAN88fs`, `y0LVT59inEA`). Your grade is under it.
- **The bluefin-specific rule says circle regardless:** a Cortez Bank pre-trip briefing gives **"circle hooks always for bluefin, J hooks for yellowtail"** (`UfuiWFVvz2E`); the mechanism is that bluefin carry more teeth than yellowfin and can saw a leader, and a full-circle, slightly offset point seats in the corner of the mouth and keeps the leader off the teeth (`RfiC8sfIWTk`, `RbqOKkINSCM`).
- **At small sizes, J gets the practical vote:** a small J's gap is noticeably bigger and easier to pin a bait through than a small circle's tighter gap — faster baiting, less handling, livelier bait. Stated directly for **light-line bluefin bait fishing** (`icpm7gADxvU`); the 15/20 lb finesse rig is built around a J for exactly this reason (`9JnIS8HkZlA`).
- **The decision frame:** at 20–30 lb on 20–25 lb line, the teeth argument is weaker (you're not fighting a fish for an hour with a leader in its jaw) and the baiting-speed/swim argument is stronger — which is why the two purpose-built rigs at your grade both run a small J. Go circle if you're on a crowded rail, can't reliably feel the bite, or the grade might jump. **If you go circle, the drag has to be doing its job** — there's no manual hookset to fall back on ([`tackle/hooks.md`](tackle/hooks.md), [`tackle/drag-setting.md`](tackle/drag-setting.md)).

**When it goes slow: downsize the hook, never the line** (`FXWOIB0TPfE`, `shZCjX2-fkI`, `YntRJAN88fs`) — one size at a time, e.g. 1/0 down to a No. 1. Fishing line too light just to get bit wastes the trip, because a hooked fish that size can't be landed on under-gunned line.

**The heavier dissent, for the record:** Dave Hansen's sportboat sardine flyline for bluefin runs a **4/0 thin-wire circle**, straight-tied, no swivel, no bead, thin wire specifically because a sardine "has a hard time swimming" a heavier-gauge hook (`ftEvyfwjZFU`); [`tackle/hooks.md`](tackle/hooks.md)'s bait table puts sardine at **2/0 for smaller-grade / picky tuna, up to 4/0–5/0 for mid-grade bluefin**. For picky 20–30 lb fish you're at the small end of that.

## 4. Knots

- **Mono top shot → fluoro leader: a 4-turn surgeon's knot.** The pound-test-scaled rule is **4 turns for 20–100 lb test, 5 turns under 20 lb** — more than the 2–3 turns knot books show ([`rigging/surgeons-knot-mono-to-fluoro.md`](rigging/surgeons-knot-mono-to-fluoro.md), `9JnIS8HkZlA`, `dg1sbr6GuB8`, `QHY5kmU7OTU`). The Seaguar knot is the attributed alternative for the same job, and is what the bite-guard build above specifies (`48ZFXnCTTQE`).
- **Leader → hook: a single-pass tie.** Carson ties a **single San Diego jam** at the hook end on this rig (`QHY5kmU7OTU`). Note the conflict: [`rigging/san-diego-jam-knot.md`](rigging/san-diego-jam-knot.md) carries a line-class breakpoint of **improved clinch at 40 lb test or less, San Diego jam above 40 lb** (`tpmOYXYQwhU`, `J0NJhN6-Thg`) — and several presenters tie the identical single-pass mechanic under both names, a naming split the KB tracks in [`rigging/improved-clinch-knot.md`](rigging/improved-clinch-knot.md) rather than resolving. Practically: tie the **single-pass** version, not the doubled-through-the-eye one — the doubled tie's bulk works against live-bait presentation (`5J7a6UwTA90`).
- **Straighten the fluoro before tying** — it comes off the spool twisted; rub it between your fingers to warm the kink out so the knot seats cleanly (`RbqOKkINSCM`).
- **Retie the hook after nearly every fish.** Toothy SoCal species, bluefin named, fray the last few inches; cutting the hook off and re-tying beats fishing a compromised end (`VsUUBICiBzQ`). "Everything has to be perfect if you're going to catch a 30 or 40 lb tuna on one of these finesse rigs" (`ptoIvB2MspE`).

## 5. Rigging the bait

**Bait selection first — it's the deciding variable, not the hook.** Cull the bloody, scaly, lethargic baits into the chum bucket and fish the lively lime-green ones that are hardest to catch in the tank. **If a bait isn't pulling line off the reel within about 60 seconds, wind it in, flick it off, grab a fresh one** ([`techniques/flyline.md`](techniques/flyline.md)). A crew on a finicky bluefin bite put it as "the guys that change baits often are the ones that are going to catch more fish" (`LsFMBCa9DOQ`). Pick for **scales intact, good color, and slime** (`V_ONnegk95M`). Sardine is the SoCal staple named for tuna (`gKrYKvqHUjk`).

**Hook placement — pick it for the swim you want** ([`bait/fishing-live-bait.md`](bait/fishing-live-bait.md), `T3p1mrqNjIo`, `mscHk0qiXnk`):

| Placement | Exactly where | What it does | When |
| --- | --- | --- | --- |
| **Nose** | Side to side through the clear spot at the tip of the nose, right before the eyes — **not** chin-to-top; it's the only entry that works on a sardine (`ZggReeO1nyU`) | Swims naturally, stays up | The all-purpose flyline hook; **mandatory the moment any weight goes on the line** (`UP_3fBu7VPA`, `aD0Iim9C15o`) |
| **Butt** | Side to side just above the anal vent, under the two rear fins | Swims **down and away**; also defeats sea lions and harbor seals picking off nose-hooked baits | Fish holding down — an angler butt-hooked specifically because the captain called bluefin **80–100 ft** down and not coming to the chum line (`oB4BpIUTTl4`). Trade-off: it draws blood, so the bait doesn't last as long (`ZggReeO1nyU`) |
| **Shoulder / nape** | Behind the head, deep enough to hold but not into the spine (that kills the bait) | Hook **folds down** as the bait swims away — less resistance, and less visible to a tuna looking up | Bluefin boiling **50–150 (up to 200+) yards** off and not coming closer (`aD0Iim9C15o`, `QHY5kmU7OTU`) |
| **Sardine "wishbone"** | The bony chest structure near the small forward fins | Bait **dives straight down** on its own; no cast needed, just drop or flip it ~10 ft from the boat | Fish sitting **30–40 ft under the boat**; the tell is anglers around you hooking up within 5–15 seconds of a bait hitting the water. Trade-off: ~3 minutes of bait life vs 10–15 minutes hooked further back, and the hook tears out once you start reeling (`aD0Iim9C15o`, `QHY5kmU7OTU`) |

**Two mechanics specific to your finicky-bite scenario** ([`bait/fishing-live-bait.md`](bait/fishing-live-bait.md), `48ZFXnCTTQE`): if you keep any tension on the line (rolling the reel to keep the bait swimming), a **nose hook drags the bait's head back toward the boat** — exactly wrong. Fix it with the **shoulder hook** (cradle the bait, thumb and index finger over its eyes to calm it, hook through about 1/8 in below where a thumb's knuckle sits) or the **butt hook anchored on the bone behind the fin** — start from the tail side behind the fin, run through the body cavity where you'll feel the bone, out the front side of that same fin, **hooking over the top of the bone** so it won't pull free on a hard cast; a plain sideways belly hook that misses the bone pulls out. Orient the hook eye **toward the tail** so rolling the reel pulls the bait backward and it dives away.

**Circle hooks specifically: hold the hook high on the arch and press straight down into the bait.** Holding it from the bottom the way you would a J leaves no gap and squeezes the bait into a "potato chip" (`8YvmROeVL-0`, [`techniques/flyline.md`](techniques/flyline.md)).

**Then: no weight, and get it away from the boat.** Fish are finickier close to the hull and bites drop off sharply near it; the goal is the bait **beyond everybody else's, in its own zone** (`raUPkuaFXpw`, `gKrYKvqHUjk`). Adding a split shot or slider to help the cast is framed bluntly as a crutch for not knowing how to cast, not a technique upgrade (`gKrYKvqHUjk`) — see [`techniques/underhand-casting.md`](techniques/underhand-casting.md) (Carson's preference for this rig: landing the bait gently and letting it swim away matters more than distance, `QHY5kmU7OTU`) and [`techniques/live-bait-pendulum-cast.md`](techniques/live-bait-pendulum-cast.md). On a butt- or belly-hooked bait, **keep a little tension the instant it lands** — a small pull makes it swim away like a propeller; give it slack and it turns and comes back under the boat (`8YvmROeVL-0`). The three documented exceptions to no-weight are all conditions-driven: current sweeping the bait flat (a **half-ounce**, `Rb5I2ljAqeE`), fish wanting it deeper (**½–¾ oz rubber-core or sliding sinker**, `Ow3an9lSVh4`), and no visible sign at all with fish read as lower in the column (**a small sliding egg sinker**, `qh3hL2Dt3HY`). Any of those means switching back to a nose hook.

**On the bite: don't swing.** Give it a solid **three count**, then come tight without swinging. On a circle that alone seats it in the corner of the mouth; on a J, raise to about **45°** and wind tight — the same unhurried motion (`R48YdVFfEOI`, `raUPkuaFXpw`). If the bait isn't getting away from the boat fast, that's your marker it isn't lively — though **a long soak still works** (`icpm7gADxvU`).

## 6. Drag

Set it before you fish — a captain's briefing on this exact fishery stressed not ending up fighting a fish with an unset drag (`V_ONnegk95M`). Method from [`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md) (`9JnIS8HkZlA`): from free-spool, roll the lever forward by feel pulling line by hand until it's close, then **confirm with a drag scale**. **Weakest-link rule:** identify the weakest link (top shot, braid, or any knot you don't fully trust — have a crewmate re-tie it), then set strike drag at **no more than one-third of that link's test; a quarter is the more usual target**, since you can always advance the lever once the first run is over. On 20 lb that's roughly 5 lb strike. Don't underestimate what it turns: 25 lb mono properly drag-set handles far more than most anglers assume, and the KB carries a **44 lb bluefin landed on the 15 lb version of this rig** (`ptoIvB2MspE`) and a **130 lb fish landed in 45 minutes on 30 lb** after downsizing off a dead 50–60 lb bite (`48ZFXnCTTQE`).

## 7. If the grade is wrong

- **Fish come in bigger, 50–70 lb and refusing 40–50 lb line:** that's **Rig 2 — 30 lb "big fish finesse"**, two-speed Fathom 15-class, small Owner Mutu circle size 4 (2 the largest) — a pattern stated as recurring five years running as of 2023-03 ([`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md), `9JnIS8HkZlA`, `riEkdu8PEds`).
- **Fish are wide open / you want one rig to cover up to ~100 lb:** **Rig 3 — 40 lb starter**, 50 lb braid to a 50 yd 40 lb mono top shot, ~4 ft of 40 lb fluoro, Owner Mutu circle size 4 (sometimes 2) (`9JnIS8HkZlA`). Worth knowing the wide-open "chewing the paint off the boat" bite happens **less than 10% of the time** — most days need the finesse rig just to draw a bite at all.

**⚠ One internal conflict you should see:** [`species/bluefin-tuna.md`](species/bluefin-tuna.md)'s situations table routes "chummed up / picky on bait" to flyline at the **40–60 lb class**, and its gear summary says "bait / flyline: 40–60 lb class, circle hooks size 1–2/0." [`techniques/flyline.md`](techniques/flyline.md) answers the same situation the opposite way — capping fly line at **20–25 lb, no more than 30** for a tough bite, on the stated mechanism that in warm water bait doesn't have time to toughen up, so it can't swim heavy line convincingly (`48ZFXnCTTQE`), with bluefin grading 40–60 lb refusing heavier line for exactly that reason (`icpm7gADxvU`). The router carries this as a flagged fact-check, unresolved. For a **20–30 lb** target the light side is the one every grade-matched build in the KB supports; the 40–60 lb class is for a heavier grade of fish, not a heavier grade of bite.

## 8. Against your profile

Resolving this against [`profiles/cameron/rods.md`](profiles/cameron/rods.md): your dedicated flyline stick is **Setup 2 — Teramar TMC90MHB2 (9'0", MH, fast, 30–65 lb) on an Avet MXJ 5.8 with 50 lb braid**. That's [`tackle/gear-classes.md`](tackle/gear-classes.md)'s **flyline / soft-rod class (~30–65 lb)**, and it's a class heavier than this rig calls for.

**The gap, named rather than substituted:** this program wants the **finesse fly-line class — 8–8.5 ft, 12–30 lb, small star drag** — and [`tackle/gear-classes.md`](tackle/gear-classes.md) shows no owned setup against that class for you. Your lightest braid on any setup is 50 lb, which is fine as *backing* under a 20–25 lb top shot (heavier than the one-class-up rule requires), but the 30–65 lb rod is above the 12–30 lb rating both sources give, and the KB's own warning is that a rod tip too heavy for this small a hook rips the hook out of the bait or the fish (`QHY5kmU7OTU`). The Avet + a 50 yd 20–25 lb top shot will fish it; a 8 ft 12–30 lb glass/composite stick on a small star drag is what the rig is actually built around.

Your profile also carries **no hook or leader inventory** ([`profiles/cameron/tackle.md`](profiles/cameron/tackle.md) covers hard baits, casting and jigging only), so I can't tell you whether you already have size 2 Gorilla Lights, Hybrid Mutus, or 20–25 lb fluoro on the boat — that's a shopping list from the sizes above, not a confirmation.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `techniques/flyline.md`, `tackle/bluefin-rig-ladder-by-grade.md`, `tackle/searcher-finesse-live-bait-outfit.md`, `tackle/hooks.md`, `tackle/line-and-leader.md`, `tackle/gear-classes.md`, `bait/fishing-live-bait.md`, `rigging/san-diego-jam-knot.md`, `rigging/improved-clinch-knot.md`, `rigging/surgeons-knot-mono-to-fluoro.md`, `rigging/seaguar-knot.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `QHY5kmU7OTU`, `ptoIvB2MspE`, `9JnIS8HkZlA`, `dg1sbr6GuB8`, `G1YIlakiRqg`, `48ZFXnCTTQE`, `icpm7gADxvU`, `jQW2HLkMsmY`, `LTCFjqtSI8g`, `149px8WQ2Ng`, `oB4BpIUTTl4`, `r4J5nP5Bkl4`, `ftEvyfwjZFU`, `RbqOKkINSCM`, `HIXTFWlwnM0`, `m2q22sPPkEM`, `sWRSYCmt4Tw`, `YntRJAN88fs`, `y0LVT59inEA`, `UfuiWFVvz2E`, `RfiC8sfIWTk`, `FXWOIB0TPfE`, `shZCjX2-fkI`, `0AtmEH6aQt0`, `IMnoZVEYpm4`, `xPFm_ZV2PZU`, `ZggReeO1nyU`, `8YvmROeVL-0`, `raUPkuaFXpw`, `R48YdVFfEOI`, `T3p1mrqNjIo`, `mscHk0qiXnk`, `aD0Iim9C15o`, `UP_3fBu7VPA`, `fyJA3o2hVh0`, `riEkdu8PEds`, `tpmOYXYQwhU`, `J0NJhN6-Thg`, `VsUUBICiBzQ`, `5J7a6UwTA90`, `gKrYKvqHUjk`, `LsFMBCa9DOQ`, `V_ONnegk95M`, `Rb5I2ljAqeE`, `Ow3an9lSVh4`, `qh3hL2Dt3HY`  
*gaps admitted:* No note states a bait-species preference for the 20-30 lb bluefin grade specifically — sardine is named as the SoCal tuna staple, but the KB gives no sardine-vs-mackerel-vs-anchovy call tied to this grade. | No stated drag number in pounds for the 20-25 lb flyline outfit; the KB gives only the general weakest-link rule (quarter to one-third of the weakest link's test), so the ~5 lb strike figure is my arithmetic on 20 lb, not a cited number. | Hook style at this grade is an unreconciled conflict in the KB (circle-always-for-bluefin vs J-fine-under-40-lb vs J-easier-to-bait-at-small-sizes); no source resolves it for a 20-30 lb fish. | The terminal-knot line-class breakpoint conflicts: san-diego-jam-knot.md says improved clinch at 40 lb test or less, while the finesse-rig source ties a single San Diego jam at 20 lb. Unresolved in the KB. | Hook-size discrepancy on the finesse rig itself (Owner Gorilla Light size 2 vs size 4) is preserved unreconciled across citations — the KB does not say which is correct. | species/bluefin-tuna.md routes the picky-bait situation to a 40-60 lb class while techniques/flyline.md caps it at 20-25 lb; the KB carries this as an open flagged fact-check, not a resolved answer. | No brand/model guidance for fluorocarbon leader material at this class (the KB names knots and tests, not leader brands, apart from unrelated product mentions). | No substitute hooks are named if the Owner Gorilla Light or Hybrid Mutu is unavailable, beyond the size-4-for-size-2 swap. | profiles/cameron/tackle.md carries no hook or leader inventory, so terminal tackle could not be resolved against owned gear. | tackle/gear-classes.md shows no owned setup for the finesse fly-line class (8-8.5 ft, 12-30 lb, small star drag) in Cameron's profile — the rig's intended rod class is a gear gap, not something I could substitute. | No conditions were given and none were pulled (no BightSST call), so this is a grade-matched default rig rather than a conditions-resolved one.

</details>

### 8. [gear] What knife-jig weights and hook rig should I use for daytime bluefin in 200-350 ft of water, and what rod and …

**Winner:** B3 · mapping {'A': 'B2', 'B': 'NOW', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** | regulation_without_asof |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 1 | 2 | 2 | **11** | regulation_without_asof |

**Judge:** All three found the right router row and the same core doctrine (1 g/ft speed-jig rule, 200-350 g box, knife/speed-jig class, narrow two-speed, 19-20 lb strike drag), so the separation came from scoping and from which supporting notes each version could reach. C is the only answer that handles the one regulatory claim in play correctly: A and B both assert 'US waters cap you at two hooks' as settled fact with no jurisdiction, as-of date, or verify-current, while C flags it as unverified, points out the KB logs three-hook US rigs against it, and tells the angler to check. C also uniquely surfaces the jig-rod-rating rule (a jig rod fishes toward the top of its printed gram rating, so a 100-300 g blank is wrong for a 200 g jig), which is the most decision-relevant rod fact in the whole question, and pairs the braid choice with dated landings rather than a bare range. B is a close second - its Searcher depth ladder, PE activation/drag table, and boat-rule-first hook decision frame match C's substance, and its honest note that 300-350 ft sits past the documented daytime window is the sharpest single caveat any answer makes; A is the thinnest, presenting hook variants without the boat-policy override and offering a 250-400 g rod rating that fits the light end of the asked jig range poorly.

- *B2 reasons:* found: hit the right router row (sounded deep 30-50 fm -> knife jigging) and the right notes (knife-jigging, knife-jigs, assist-hooks, bite-leaders, gear-classes, rod-and-reel-selection). specific: 1 g/ft rule, 200/300/350 g, 150-400 g captain range, 500 g hard-current step-up, PE 4x8 250-400 g, 19-20 lb strike drag, 2-2.5 ft 200 lb bite leader, 1.6 crimp, 10-turn sweep cadence. sourced: nearly every claim carries a video id plus a note path (HWx1jDTGsng, 149px8WQ2Ng, Ul5FLB2dFgQ, scmPq63lLWM). scoped: SoCal-correct and the Sea-of-Cortez yellowtail data is properly labeled as a region contrast, but 'US waters cap you at two hooks' is stated bare - no jurisdiction, no as-of, no verify-current. honest: strong gap list, flags the 100-200 g vs 1 g/ft internal conflict, notes the single-bottom-assist doctrine is night-scoped, absolute dates only. actionable: gives a buildable box, a stated hook doctrine, line/drag, line marking, vertical positioning and hookset - but omits the boat hook-policy override and gives no PE-by-drag ladder, and its 250-400 g rod rating is a loose fit for 200 g jigs.
- *B3 reasons:* found: same router row and ladders, plus the one note the others miss - jig-rod-rating-selection - which is the direct answer to 'what rod for a 200-350 g jig'. specific: full Carson ladder by depth (100/170/220/280/300 g), 200/250/300 g core with 170 and 350 bookends, PE 4-8 = 150-350 g / 20-30 lb drag vs PE 6-10 = 250-500 g / 25-40 lb, 65 lb braid under 200 g vs 80 lb over 350 g with dated 2023/2024 landings, 180 lb hollow PE cord, #2 310 lb swivel, 12-18 in metered marks. sourced: every parameter carries a note path and a video id, and asr-uncertain figures are labeled as such. scoped: the only answer that treats 'two hooks in US waters' correctly - flags it as carrying no jurisdiction, no as-of, no verify-current, notes the KB itself logs three-hook US rigs, and tells the angler to verify before fishing. honest: says outright the KB will not settle hook count, labels the 280/300 g tiers as depth-only not daytime, flags sponsored model picks as low confidence, no relative time. actionable: gives a bag list, a stated pick with the boat-policy override, the buy-toward-the-top-of-the-gram-rating rule, drag split (strike 19-20 vs fighting 20-30), line marking arithmetic, and a purchase spec that also covers the BOLA yellowtail open item.
- *NOW reasons:* found: same router row plus the Searcher daypart/depth ladder and the grade ladder, and it usefully flags that 300-350 ft sits at/past the corpus's confident daytime window (150-240 ft, workable to 300). specific: 170/280/300 g depth ceilings, 200-350 g box, PE table with activation windows and 15-40 lb fighting drag, 7/0 5X (asr-uncertain), 200 lb fluoro 2.5-3 ft to 400 lb swivel, 100 lb 30-40 ft day leader, narrow = under 2 in spool, 12-18 in line marks. sourced: dense video ids and note paths throughout, including tackle ladder notes. scoped: SoCal/N-Baja gated at the end, but opens the hook section by asserting 'US waters cap a jig at two hooks' as a fixed constraint with no jurisdiction, as-of, or verify-current. honest: names the braid contradiction the note itself carries, says the KB does not settle the leader test, admits the profile owns none of this class. actionable: best-in-class decision frame (boat rule -> retrieve style -> jig profile), plus overshoot-the-call, free-spool-back-down, thumb tension, fight geometry.

<details><summary>Full prompt</summary>

What knife-jig weights and hook rig should I use for daytime bluefin in 200-350 ft of water, and what rod and reel class?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Daytime bluefin, 200–350 ft: jig weight, hook rig, rod/reel

You gave me a depth band and nothing else — no date, no wind, no current, no SST — so this is a gear answer built off the KB's standing doctrine, not a day plan. Current is the one variable that moves every number below, and I don't have it.

**Where your band sits in the KB.** 200–350 ft is roughly **33–58 fathoms**, which straddles the "fish sounded deep" row in [`species/bluefin-tuna.md`](species/bluefin-tuna.md): in wind with no surface sign, bluefin "sound to 30–50 fathoms" and you need power on the meter to reach and grade them (`HWx1jDTGsng`). That row routes to [`techniques/knife-jigging.md`](techniques/knife-jigging.md), so you're on the right technique. One thing worth knowing: Capt. Dave Hansen puts the low-visibility flat-fall bluefin bite specifically **"at night or 250–350 ft down"** — dark enough that he reasons the fish react to profile and flash, not detail (`scmPq63lLWM`, [`lures/knife-jigs.md`](lures/knife-jigs.md)). Your deep half is a documented *daytime* window, not just a night thing.

## Jig weight

**Anchor rule — ~1 g per foot of depth for a speed jig** (vs ~1.5 g/ft for a slow-pitch/wing-fall jig, which needs the extra weight to offset the flutter). [`techniques/knife-jigging.md`](techniques/knife-jigging.md), [`lures/knife-jigs.md`](lures/knife-jigs.md). That puts you at:

- **200 ft → ~200 g**
- **300 ft → ~300 g**
- **350 ft → ~350 g**

That lines up with the corroborating ranges:

| Source | Working range | Scope |
| --- | --- | --- |
| Bluefin router, sounded-deep row ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)) | **Day 150–300 g**; more current / deeper fish → **300–400 g** to punch down and still stay horizontal in the strike zone | day, 30–50 fm |
| Highliner deckhand (`149px8WQ2Ng`, [`lures/knife-jigs.md`](lures/knife-jigs.md)) | **200 g minimum, up to 300 g, occasionally 350 g**; stay below **400 g unless the current is really ripping** — the point is keeping a smaller bait profile | that week's producing pattern |
| Captain-called range, general ([`techniques/knife-jigging.md`](techniques/knife-jigging.md)) | **150–400 g**, called by depth and current; ~220 g fluttery jig for fish 150–200 ft up in the column | general |

**Practical call: build around 200–250 g at the top of your band and 300–350 g at the bottom, and carry 400 g for hard current.** If the drift is ripping, the KB's documented step-up is real but night-scoped — on a windy, hard-drifting night at Cortez/Tanner, standard **250–350 g wasn't enough and the boat went to 500 g** (`LsFMBCa9DOQ`, [`techniques/knife-jigging.md`](techniques/knife-jigging.md)).

**One internal conflict you should know about.** The sportboat day/night roundup in [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) says **100–200 g jigs by day**, 200–400 g at night (`gOAOyMNG3Ug`, `qSgIwLX2FWw`) — lighter than 1 g/ft gives you at 200–350 ft. That roundup isn't depth-scoped, and Ray Sharifi's "daytime jigging with lighter flat-fall-style jigs" figure is explicitly the **80–120 g Colt-Sniper class** (`RfiC8sfIWTk`, [`techniques/knife-jigging.md`](techniques/knife-jigging.md)) — an upper-column presentation, not a 350-ft one. The two reconcile at **200 g**, which is where the day roundup's ceiling meets the deckhand's floor. I'd fish the 1 g/ft rule for your band and treat the 100–200 g number as the shallower-marks day box.

**Profile and shape, not just grams:** in a fast drift or wind go **longer and more slender** so the jig cuts water and falls straight; in slack/light wind go **fatter and more fluttery** for hang time. Tail-weighted = speed jig (darts, fished on a fast rip); balances flat on your fingertip at the midpoint = slow-pitch/wing-fall (flutters, bite comes on the fall) — that's the tackle-counter test (`Ul5FLB2dFgQ`, [`lures/knife-jigs.md`](lures/knife-jigs.md)).

**Color, since you're fishing this in daylight:** glow paint reflects **UV** more than regular paint, which is why an all-glow jig is a strong *daytime* choice at real depth (~300 ft) — there's still light down there, just dim. Don't read glow as night-only. Baseline: off-color/dark water → whites and yellows; bright, sunny, clear water → more chrome and flash. Hansen leans **reds, silvers and blues in daylight**, with red/orange as a pelagic-red-crab match (orange specifically for the egg-bearing belly), and calls the "glow works best" claim angler-confidence marketing — while stating plainly that if everyone else on the boat is getting bit on glow, he switches to glow (`RbqOKkINSCM`, `scmPq63lLWM`, [`lures/knife-jigs.md`](lures/knife-jigs.md)).

## Hook rig

**KB doctrine for bluefin knife jigging: a single bottom assist pair, no top hook.** Two reasons given — the fish suck the jig in, so a top hook adds little; and a top hook fouls fish in the cheek or pec on the swinging jig, which moves the fight off the mouth and puts a loose hook on the rail or in a deckhand's hand at gaff ([`techniques/knife-jigging.md`](techniques/knife-jigging.md), [`lures/knife-jigs.md`](lures/knife-jigs.md)). **US waters cap you at two hooks** ([`lures/knife-jigs.md`](lures/knife-jigs.md)).

That doctrine is contested in the corpus and the KB keeps the variants side by side rather than reconciling them. What the choice actually turns on is where you're willing to take the hookup — mouth-only (fewer hooks) versus more hook points on a jig the fish may be inhaling deep:

- **Single top assist + a short double on the bottom, deliberately light-wire** — reported landing fish consistently on the bottom hook, sometimes pinned on both; framed as an increasingly common San Diego rig and standard in Japan (`Ul5FLB2dFgQ`).
- **Double 6/0 on top + single 6/0 on the bottom** (three hooks) on a 270 g jig — landed 5 fish of 50–130 lb before two of the three bent out on a rail snag and the jig was retired (`-MP2RqJC7B0`).
- **Assists up top plus one on the bottom**, on a 130 lb fluorocarbon option leader, on a ~200 g knife jig (`jQW2HLkMsmY`).
- **Factory pre-rig: two 6/0 up top + one 9/0 sliding hook on the back** on a 250 g flat-fall — Hansen's stated reason for fishing it as-is is convenience, plus the general argument that bluefin inhale a flat-fall so deep (at night or 250–350 ft) that they aren't really seeing the hooks anyway (`scmPq63lLWM`).

All of them, plus [`rigging/assist-hooks.md`](rigging/assist-hooks.md), agree on these build rules:

- **Never let two hooks cross or lock together.** Tie each hook of a double from the back of the shank forward toward the point so the points ride outward.
- **Speed-jig assists run noticeably shorter than what's on the rack** — most store assists are built for slow-pitch. Don't grab one for a speed jig.
- **Don't over-hook a jig** — too many assists kills its action (`jQW2HLkMsmY`).
- **Hook-to-jig sizing = the pass-through test:** hold the hook against the jig body; it should be just wide enough to pass all the way through. Oversized interferes with the swim (`U4zifdssSes`). A single top assist's loop should rest about **a third of the way down** the jig's total length.
- **Stiffen the cord on a speed-jig assist** with shrink tubing over the cord itself so the loop doesn't flop and tangle the main line; softer cord for slow-pitch. Gel (not thin) cyanoacrylate on the knot, 30–45 s to set, then a larger sleeve over the hook eye and knot (`U4zifdssSes`).
- Assist cord in the demo was roughly **215 lb** PE with a mono core on the speed jig, stepping to roughly **300 lb** class on the heavy tail double — both flagged asr-uncertain in the source, so treat them as mid/heavy PE, not precise specs.

**Terminal to the jig — two schools, both fished in the fleet:**

- **Crimp school:** a **~2 ft bite leader of 200 lb** fluoro/mono crimped **directly through the jig's solid wire ring, not a split ring** (`nRFFM8DT-og`). Keep it **no more than ~2–2.5 ft** — it carries a large swivel at the top that will not pass the guides, so a longer one strands you with the fish at deep color and no line to wind. Match the crimp to the leader (130 lb fluoro → size 1.6 crimp + 1.6 chafe sleeve), two presses per crimp, snug not crushed, leave a tag through. A corroborating seminar puts the bite guard at **2–3 ft, not 5–6** (`Ul5FLB2dFgQ`). [`rigging/bite-leaders.md`](rigging/bite-leaders.md).
- **Direct-tie school:** no crimp — 80–100 lb braid → FG → **15–20 ft of mono/fluoro top shot tied straight to the jig** (`j37zxs33gws`). A variant runs **100 lb braid straight to a 10 ft, 130 lb fluoro leader**, no crimp and no swivel, deliberately: the bulky knot stops running smoothly through the guides on the retrieve, which is your physical warning to slow down before you wind the connection into the tip and crack the ceramic (`gevNj2Y1Ep8`).

The KB calls the bite leader **the most critical part of a bluefin jig setup** — you're geared for anything from a 20 lb schoolie to a 300 lb fish on the same drop, and bluefin teeth saw through leader.

## Rod, reel and line class

**Class: knife / speed-jig class** ([`tackle/gear-classes.md`](tackle/gear-classes.md)) — a rod that vertically rips a **150–400 g** jig, thin braid, assist hooks.

- **Rod:** short, parabolic, high-power, commonly **PE 4x8 rated 250–400 g** ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)) — that rating window brackets your 200–350 g jigs cleanly. Often **spiral / acid-wrapped guides** to kill rod twist and stop line wrapping the tip during the jigging motion. A budget broomstick (130–150 class) covers schoolie grade; a stiffer fiberglass-tipped composite for cow fish. Power is deceptive for the size — a demoed speed-jig rod is rated **55 kg (≈110 lb) of pulling power at a 60° rod angle** despite a slow action, but only because the blank loads all the way to the butt: **fish it in hand, not racked on the rail**, which throws away roughly half its power (`Ul5FLB2dFgQ`). Caution on over-gunning: a 60–130 lb-rated jig stick ran **too stiff on 40–50 lb-class bluefin** — hard to keep a consistent bend — while the same stiffness "worked to our benefit" on 80 lb-and-up fish (`-MP2RqJC7B0`).
- **Reel: any narrow two-speed**, high-speed retrieve. A premium two-speed (Talica, Daiwa or comparable) if budget allows; a **Fathom** is called out as strong value — big, high capacity, two-speed — with the caveat that its stock handle is thin enough to snap, so budget for a thicker/longer aftermarket handle, which also speeds the low-gear retrieve (`Ul5FLB2dFgQ`). A documented working combo is a **Talica 25** on a 7 ft, 60–120 lb blank with 100 lb braid (`jQW2HLkMsmY`). *Region-labeled contrast (Baja, Sea of Cortez, for yellowtail/amberjack, not bluefin):* a shorter **5.5–6 ft rod rated 150–350 g up to 400 g** on 50–65 lb braid with a tall, narrow reel, because on vertical speed jigging you want max line gained per pump (`M8hOYQ_6rSg`).
- **Line, daytime:** the sportboat roundup's daytime build is the **same jigging rod, 100 lb braid, day size-down to a 60–80 lb fluoro top shot** (`gOAOyMNG3Ug`, `qSgIwLX2FWw`). The by-rod variant runs a **light/day outfit — 65 lb braid to a 25 ft, 80 lb top shot — for jigs 200 g and under**, and a heavy/night outfit at 100 lb braid to a 130 lb **mono** (not fluoro, for the stretch) top shot (`Ul5FLB2dFgQ`). At 200–350 g you're past that light-day outfit, so I'd run **80–100 lb braid to a 60–80 lb fluoro top shot**, plus the bite leader. **80 lb braid sinks faster than 100** and gives less line angle so the jig hangs straighter — real at this depth — but note the bluefin exception: unlike skipjack and schoolie yellowfin, **bluefin gear doesn't get scaled down**, because grade is unpredictable trip to trip (`PrdPJy26H8c`, [`species/bluefin-tuna.md`](species/bluefin-tuna.md)). The "never fish under 100 lb line" rule in the KB is stated for **night** specifically; there is no equivalent stated daytime floor.
- **Drag: set strike at 19–20 lb.** The KB explicitly flags the online advice to run **35 lb strike as dangerous** — a hookup at the get-go on 35 lb can rip a jigging outfit clean out of your hands (a witnessed loss of five outfits on one trip). Kept side by side; 19–20 lb is the documented conservative setting (`Ul5FLB2dFgQ`).

## Fishing it at 200–350 ft

- **Mark your line.** You can't put a jig on a called depth you can't measure. Sharpie or a contrasting braid wrap **every 100 ft down to ~400 ft**, or run color-metered braid; intervals in the corpus vary by angler — every **50 ft**, or commercially pre-marked every **25 ft**. Pick one and know it cold ([`techniques/knife-jigging.md`](techniques/knife-jigging.md), `Ul5FLB2dFgQ`, `gevNj2Y1Ep8`).
- **Stay vertical.** Don't run to the stern and drop with the crowd — your line scopes and on a 300 ft mark your jig is only ~80 ft down. Throw **up-current off the bow, let it sink straight, and walk back toward the stern**. Attributed alternative for stern anglers: **cast down-swell**, so by the time the boat drifts over it the jig sits at roughly **200–250 ft** hanging straight down (`UfuiWFVvz2E`). Ask the deckhand which way the boat drifts.
- **Working the 150 ft band you've got:** drop to the called depth, then instead of winding straight up, put the reel in gear, **pop the tip high and let slack line the jig flutter all the way down** — 2–3 times. Then **wind 10 full turns (≈30–40 ft)** and repeat for another 3–4 sweeps. Ten turns at a time works you through roughly 100 ft of column with the jig fluttering the whole way (`Ul5FLB2dFgQ`).
- **Slack the drop, don't tightline it** — resistance on the nose stops the jig camber/flutter/dart.
- **Hookset: do not wind on it like bait fishing.** A jig-hooked fish typically hangs just above the barb on hard jaw; wind on it and the hook can bend open under load regardless of wire. Wait until **drag is actually coming off the reel**, then **grab/palm the spool and give three or four hard sideways swings** (`Ul5FLB2dFgQ`).

## Against your profile

[`profiles/cameron/rods.md`](profiles/cameron/rods.md) lists 8 setups and **none of them is a knife/speed-jig setup** — a dedicated SPJ / speed-jig outfit is an open shopping item there (and in [`lures/knife-jigs.md`](lures/knife-jigs.md), where the goal is one setup covering night bluefin knife jigging and September BOLA bottom yellowtail). So the recommendations above stay in class terms. Your closest owned line class is the **Talica 25 setup** — Phenix Axis HAX-C 800X3H, 8'0", 3X-H, 60–130 lb, 100 lb braid — but the KB files that as **rail-rod / heavy tuna class**, not the short parabolic jig rod, and it does not endorse it for jigging; note also the flagged caution that a 60–130 lb blank runs stiff on 40–50 lb-class bluefin. If you buy the rod for this band, a **PE 4x8 / 250–400 g** blank covers 200–350 g jigs with the right load.

## What the KB does not cover here

- No note gives a **daytime** jig-weight table indexed to a specific depth band; the 200–350 g figures above are the 1 g/ft rule plus the day 150–300 g router row, not a stated "at 200–350 ft in daylight, use X."
- The single-bottom-assist doctrine is written for the **night** bluefin knife-jig bite. There is no separate daytime hook-configuration doctrine in the KB.
- The 500 g hard-current step-up and the 300 g floor are both **night**-scoped observations; there is no documented daytime hard-current ceiling.
- No stated daytime minimum line class for a heavy jig at this depth (the "never under 100 lb" rule is night-only, and the 40–50 lb daytime figure is scoped to 80–120 g flat-falls).
- No bluefin-specific assist **hook size** chart — sizing is by the pass-through test, with 6/0 (270 g jig) and 2×6/0 + 9/0 (250 g flat-fall) as the only observed points.
- Assist cord weights (~215 lb / ~300 lb) are flagged asr-uncertain in the source.
- You gave no date, wind, current or water conditions, so I have not applied any seasonal priors or conditions layers, and I made no BightSST call.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `techniques/knife-jigging.md`, `techniques/slow-pitch-jigging.md`, `lures/knife-jigs.md`, `rigging/assist-hooks.md`, `rigging/bite-leaders.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`, `tackle/hooks.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `HWx1jDTGsng`, `scmPq63lLWM`, `Ul5FLB2dFgQ`, `149px8WQ2Ng`, `RfiC8sfIWTk`, `gevNj2Y1Ep8`, `-MP2RqJC7B0`, `jQW2HLkMsmY`, `nRFFM8DT-og`, `j37zxs33gws`, `U4zifdssSes`, `oB4BpIUTTl4`, `UfuiWFVvz2E`, `LsFMBCa9DOQ`, `M8hOYQ_6rSg`, `gOAOyMNG3Ug`, `qSgIwLX2FWw`, `PrdPJy26H8c`, `RbqOKkINSCM`  
*gaps admitted:* No note states a daytime-specific knife-jig weight for a 200-350 ft band; the 200-350 g figures are derived from the ~1 g/ft speed-jig rule plus the router's day 150-300 g range. | Internal conflict left unreconciled: the sportboat roundup says 100-200 g jigs by day while the 1 g/ft rule and the deckhand's 200-350 g range apply at this depth. | The single-bottom-assist-pair, no-top-hook doctrine is written for the NIGHT bluefin knife-jig bite; the KB gives no separate daytime hook-configuration doctrine. | Hook count and placement is a live, unreconciled conflict in the KB (single bottom pair vs at least four documented top-plus-bottom / three-hook configurations), so no single rig is settled doctrine. | The 300 g night floor and the 500 g hard-current step-up are night-scoped observations; no documented daytime hard-current jig ceiling exists. | No stated daytime minimum line class for a 200-350 g jig at this depth - the 'never under 100 lb' rule is night-only and the 40-50 lb daytime figure is scoped to 80-120 g flat-falls. | No bluefin-specific assist hook size guidance beyond the pass-through sizing test and two observed data points (6/0 on a 270 g jig; 2x6/0 plus 9/0 on a 250 g flat-fall). | Assist cord weights (~215 lb speed-jig, ~300 lb tail double) are flagged asr-uncertain in the source and are not precise specs. | No conditions, date, wind or current were supplied, so no seasonal priors, conditions layers or BightSST data were applied - current is the variable that most changes the jig weight.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Daytime bluefin jigging, 200–350 ft

**Which situation this is.** 200–350 ft is 33–58 fathoms, which lands on the bluefin router's **"fish sounded deep (30–50 fm), wind up, no surface sign"** row — the knife-jigging row, not the foamer or flyline rows (`species/bluefin-tuna.md`). That row's own summary is: **day 150–300 g; more current / deeper fish → 300–400 g to punch down and still stay horizontal in the strike zone**, on the **100–130 lb-braid jig class (PE6–8)**. Everything below is that row expanded.

You gave me a depth and a daypart but no conditions — no zone, current, wind, or grade. The corpus is emphatic that this call is not a fixed lookup: jigging big bluefin is "very condition oriented," a jig that got bit yesterday is not a guaranteed bite today (`tackle/tackle-express-trophy-bluefin-jig-outfit.md`, `DuNkl8F45NE`), and Carson's closing line on his own ladder is that which jig and depth works "is probably going to change every hour" — check with the crew (`tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md`, `vVOkxHx58Eg`).

---

## 1. Jig weight

**The two arithmetic rules** (`lures/knife-jigs.md`):

- **Speed/knife jig: ~1 g per foot of depth.** 200 ft → ~200 g, 350 ft → ~350 g. Stated in the same terms at the 2025 PCS Show seminar: "fish 200 ft down, go around 200 grams, you're safe" (`gimFbgN5Jjk`).
- **Slow-pitch / wing-fall jig: ~1.5 g per foot** — the extra weight offsets the flutter and keeps it vertical. That puts a wing-fall profile at 300–525 g across your band, which is why the knife/speed profile is the more practical choice at the deep end.
- **Shape is the second factor, current decides it:** fast drift or wind → **longer and more slender** so it cuts water and falls straight; slack/light wind → **fatter and more fluttery** for hang time (`lures/knife-jigs.md`, `gimFbgN5Jjk`).

**The named ladders that bracket your band:**

| Source | Weight | Stated depth |
| --- | --- | --- |
| Carson / Searcher (`vVOkxHx58Eg`) | ~100 g | midday, full daylight, good to ~**200 ft** |
| Carson | ~170 g | dawn/dusk **or any time fish are deeper than the 100 g jig's ~200 ft ceiling** — as deep as ~**250 ft** |
| Carson | ~280 g | "good down to probably about **300 ft**, depending on the current and the wind" |
| Carson | ~300 g | same depth range as the 280 g tier |
| Carson | ~220 g | mid-depth **speed/fast-pitch** (cranking retrieve) |
| Highliner deckhand (`149px8WQ2Ng`) | **200 g minimum, up to 300 g, occasionally 350 g** | stay below 400 g unless current is really ripping — goal is keeping a smaller bait profile |
| Bluefin router | 150–300 g day; 300–400 g for more current/deeper | 30–50 fm |

**What I'd actually put in the bag:** a **200 / 250 / 300 g** core in a slender knife/speed profile, with a **170 g** bookend for the shallow end of your band on a slack day and a **350 g** for the deep end in current or breeze. Carry the spread rather than one jig — the on-the-water pattern the corpus documents is swapping *within* the box as the captain's call moves (started 250 g, dropped to 200 g when fish came higher and were swimming past faster, stepped up toward 300 g when the call went to 400 ft — `tackle/tackle-express-trophy-bluefin-jig-outfit.md`, `BsWb5BQ1Tdc`).

**The daytime tension, and how the corpus resolves it.** Carson's reasoning for going *lighter* in daylight is that bluefin "generally eat little food" and in daytime can see the lure well, so presentation has to be more careful (`vVOkxHx58Eg`). That pulls against needing 200–300 g to reach 200–350 ft. The resolution in the notes is **profile, not bulk**: get the depth from a long, slender, dense cross-section that cuts current, and keep the presentation small — which is exactly the deckhand's stated goal at 200–300 g ("a smaller bait-profile presentation") and the shape rule above.

**A separate, differently-cadenced option at your exact depth:** Capt. Dave Hansen puts the low-visibility **flat-fall** bite on bluefin at **night or 250–350 ft down**, reasoning the fish are reacting to profile and flash rather than detail that deep (`techniques/knife-jigging.md`, `scmPq63lLWM`). If you go that way it's a different cadence — free-spool, count, wind back up about halfway and re-drop rather than a continuous rip — and the weights are **250 g / 320 g by default, dropping to 120 g only when it's calm enough the boat isn't drifting much** (`techniques/flat-fall-jigging.md`, `fgTmUq78ofQ`, `shZCjX2-fkI`). The flat-fall's usual bite zone is called shallower (**100–200 ft**) in that note, and the KB keeps that side by side with Hansen's 250–350 ft rather than reconciling them.

---

## 2. Hook rig — the KB does not settle this, and says why

There is **no single reconciled hook doctrine** in this KB. It logs at least eight attributed configurations side by side and explicitly refuses to reconcile them. Here is the decision frame the notes give, because section order is not a ranking:

**What the choice actually turns on:**

1. **The boat's policy overrides everything else.** A lot of sportboats specifically require **twins on the bottom only** — not for hookup ratio but for **safety**, because a top hook has caught a deckhand's hand swinging a jig aboard; "every boat's different," and some allow both top and bottom during the day. Treat a captain's stated hook policy as overriding the general guidance (`lures/knife-jigs.md`, `gimFbgN5Jjk`). **Ask before you rig.**
2. **The jig's own weight/profile,** per that same seminar: smaller/shorter jigs (100–150 g) → single assist on the nose only; **longer-profile jigs → one assist on top and one on the bottom**; short, heavy profiles → twin assists on the bottom only.
3. **Weight tier, per Carson's ladder** (`vVOkxHx58Eg`) — this is the one that maps directly onto your 200–350 ft band:
   - **280 g and 300 g:** **heavy single hooks, one off the nose and one off the tail.** His reason: bluefin frequently bite the jig **as it's sinking**, not on a clean centered strike, so the fish "might bite it at either end" — hooking both ends covers the ambiguity. Stated trade-off: a hooked fish can snag the *other* hook and come in sideways, which takes more pulling force.
   - **220 g on a cranking speed-jig retrieve:** **two hooks off the nose end** — "usually the best" for that retrieve style.
   - **Hook size:** captioned "70 5x," read in the note as a **7/0, 5X-strong** hook — the exact number is flagged **asr-uncertain**. The nearest independent size figure is a tackle-shop **Mustad 6/0 assist, called "a good universal size"** across Rip Roller / Streaker / Jigpara, attached with a **heavy-duty split ring** (`lures/knife-jigs.md`, `6_E5JCRvazc`).
   - **Safety rule, stated flatly:** **never add extra hooks to a lure already rigged with a treble** — "a real safety issue for you and for the crew." Trebled jigs stay single-treble.
4. **The technique note's own doctrine, which points the other way:** `techniques/knife-jigging.md` carries **single bottom assist pair, no top hook** — reasons being that the fish suck the jig in so a top hook adds little, and a top hook fouls fish in the cheek or pec, moving the fight off the mouth and putting a hook near the rail or a deckhand at gaff. Its **Common failures** list names "blinged-out hooks (multiple assists top and bottom)" outright. The attributed variant kept beside it (`Ul5FLB2dFgQ`, Eric's Tackle) is **single top assist + a short double on the bottom, both deliberately light-wire** — reported landing fish consistently on the bottom hook, framed as an increasingly common San Diego rig and the standard in Japan.

**My read for a daytime 250–300 g jig at your depth**, said as a choice and not a rule: start with **one heavy single on the nose and one on the tail** (Carson's tier match, and it directly addresses the on-the-sink bite you'll be getting at that depth) — **unless** you're on a boat that mandates bottom-only, in which case run **twins on the bottom and no top hook**, which is also the technique note's own doctrine. If you're speed-jigging on a cranking retrieve rather than dropping and working, go **two off the nose**.

**Hook-count caveat, flagged not asserted:** `lures/knife-jigs.md` states "**US waters cap you at two hooks**" — but that note carries **no jurisdiction, no as-of date, and no verify-current stamp**, and it logs several three-hook configurations from US trips that exceed it. Treat it as an unverified regulatory claim and **check current rules and the boat's own policy before you fish it**.

**Building or resizing the assist itself** (`rigging/assist-hooks.md`, `U4zifdssSes` / `unARAuTgF_A`, high confidence — corroborated across two videos):

- **Hook-to-jig sizing, pass-through test:** hold the hook against the jig body; it should be **just wide enough to pass all the way through the jig's body**. Oversized interferes with the swimming action.
- **Assist position:** a single top assist on a speed jig should rest **roughly a third of the way down the jig's total length**.
- **Cord stiffness by style — this matters for a speed jig:** slide shrink tubing over the **cord itself** to stiffen it, so the loop doesn't flop and tangle the main line. Mechanism: a speed jig gets bit **on the pump/upswing**, so you want the hook **stationary**, riding exactly where the fish eats. Slow-pitch is the opposite — bit on the fall, so you want it looser and flopping.
- **Speed-jig assists run noticeably shorter** than the long assists sold on the rack, which are built for slow-pitch. Don't grab a slow-pitch assist for a speed jig.
- **Cord:** **180 lb hollow-core PE** is used for speed-jig-class hooks; heavier ratings are chosen for **abrasion resistance against teeth and scales**, not breaking strength, and a doubled loop is still only rated to the single-strand number.
- **Two hooks must never cross or lock together** — tie each hook from the back of the shank forward toward the point so the points ride outward.
- **Swivel option:** a **#2-class swivel rated 310 lb** is the smallest usable; smaller risks the thin wire cutting heavier line. Going to a swivel instead of a plain solid ring leaves working room on a dual build and puts fight load on the swivel-to-line connection instead of through a split ring.
- **Assume you're re-rigging every jig.** Stock hooks ship undersized — Carson changes "almost all" of his because Searcher-grade fish run bigger than what these lure lines are built for anywhere else; Tackle Express puts it as stock jigs being "ready to catch local island fish and smaller grade bluefin. These are not 100 lb fish ready" (`Q4sW6JRQzAY`).

---

## 3. Bite leader and terminal

- **The bite leader is the most critical part of a bluefin knife-jig setup** — a hooked tuna inhales the jig deep and you don't want braid or light mono sawing on teeth and gill rakers (`rigging/bite-leaders.md`).
- **Length: no more than about 2–2.5 ft.** It carries a large swivel at the top that will **not** wind through the guides — too long and you're stranded at your top-shot connection with the fish at deep color and nothing left to wind.
- **Test, by source, unreconciled:** Carson runs **200 lb fluorocarbon, ~2.5–3 ft, to a ~400 lb swivel** on the 280 g tier and ~3 ft of 200 lb on the 300 g (`vVOkxHx58Eg`). The bite-leader note's worked build is **130 lb** with a **size 1.6 crimp and matching 1.6 chafe sleeve**. Tackle Express runs **200–300 lb standard, up to 400 lb for heavy night work**, reasoning that a swallowed jig puts the leader against the fish's teeth for the whole fight (`DuNkl8F45NE`). Capt. Armando gives the mechanism for going heavy: past roughly **50–60 lb of fish, bluefin teeth get bigger** and a light leader risks abrasion when the lure is engulfed deep (`shZCjX2-fkI`). The bluefin router's class term for everything deep is a **200 lb bite-leader class**.
- **Crimp judgment:** don't over-crimp — snug, two presses per crimp, one top one bottom; over-crimping bites into and weakens the fluoro. Leave a small tag through the second side so the loop can't pull back (`rigging/bite-leaders.md`).
- **Ring choice:** Tackle Express goes to a **solid ring rather than a split ring** at the hook — "we've heard and seen split rings bind."

---

## 4. Rod class

**Class term: knife / speed-jig class** — a short, parabolic, high-power rod that vertically rips a 150–400 g jig, thin braid, assist hooks (`tackle/gear-classes.md`).

**The PE rating that matches your jig weights** (`tackle/bluefin-rig-ladder-by-grade.md`):

- **PE 4–8 — "the 80 lb stick," 5.5–6 ft.** Activates **150–300 g, sometimes up to 350 g**; handles **20–30 lb of drag**. Named as **the single rod to bring if you're only bringing one** (`gimFbgN5Jjk`), and independently as one captain's one-rod answer for knife jigging, fishing **150 g up**, working **150–250 g** jigs (`G1YIlakiRqg`).
- **PE 6–10 — "the 100 lb stick."** Activates jigs as light as 200 g, typically **250–500 g**; handles **25–40 lb of drag**. The bigger-fish and night pick.
- **The selection rule between them:** pick the **lightest rod that still activates the jig you're fishing**, not the heaviest one that can. Their own worked example is a 250 g jig, which both rods move, but which "does a little bit better" on the lighter PE 4–8.

**For 200–350 ft daytime that means a PE 4–8 / ~5.5–6 ft rod is the right single stick**, and you step to PE 6–10 only if you're pushing 350 g+ in heavy current.

**Two buying checks that are easy to get backwards** (`tackle/jig-rod-rating-selection.md`, `DTvXJrtytwg` / `PbiZMk4Ft6w` / `ZrcwcugaEe4` — all one source appearance, medium confidence):

- **A jig rod fishes toward the TOP of its printed gram rating, not the middle.** The worked example is literally yours: planning to fish a **200 g jig in 300–400 ft** calls for a rod rated close to 200 g at its top end. A rod rated **100–300 g does not fish a 200 g jig well** — it actually fishes best with 250–300 g. This is the **opposite** of the all-purpose-rod rule of buying a wide line rating and fishing the middle of it.
- **Power has to be soft enough to load the jig,** separate from whether the gram range covers it — a too-stiff blank won't bend enough to load and unload and can't impart the action.

**Construction:** short and parabolic, and commonly **spiral / acid-wrapped guides** — they kill rod twist and stop line grabbing the tip during the jigging motion (`techniques/knife-jigging.md`; `tackle/bluefin-rig-ladder-by-grade.md`). Trade-off noted: the transition zone is unforgiving if slack line wraps a guide right as a fish comes tight on 25 lb of drag.

**Fish it in hand, at 60° or lower.** A speed-jig rod demoed at a tackle-shop seminar rates **55 kg (≈110 lb) of pulling power at a 60° rod angle** despite a slow action — but that power only exists because the blank loads all the way through to the butt. **Fishing it flat on the rail throws away roughly half the rod's power** (`Ul5FLB2dFgQ`). Don't bounce the fish or high-stick it (`ZrcwcugaEe4`).

---

## 5. Reel class

- **Narrow two-speed.** "Narrow" is defined as **under 2 in of spool width** — wider is "trouble," because at the **15–30 lb of drag** jigging commonly runs, line on a wide spool can dig into itself under load and then won't pay out cleanly (`techniques/knife-jigging.md`, `gimFbgN5Jjk`).
- **Capacity and drag target:** a reel putting out **30 lb+ of drag** and **400–800 yd** of line (`tackle/tackle-express-trophy-bluefin-jig-outfit.md`, `DuNkl8F45NE`).
- **Two-speed is treated as a requirement, not an option,** at triple-digit grade. Expect pushback from speed-jig purists, but the trend — including Japan — is toward two-speeds (`Ul5FLB2dFgQ`).
- **Named benchmarks across the class**, as instances of it rather than the class itself: **Shimano Talica 20** on the light end, valued specifically for **free-spool getting the jig down fast**; **Penn International 50 with 130 lb** on the heavy end (`6_E5JCRvazc`). Talica 12 on a 50–60 lb jig setup, or a **Fathom 40** as the budget pick, on the daytime ladder (`G1YIlakiRqg`). A **Fathom** is called out generally as strong value with one caveat — the stock handle is thin enough to snap, so budget for an aftermarket handle, which also speeds up the low-gear retrieve. All specific model picks in this KB from sponsored/shop channels are low-confidence product endorsements; the **class** is the transferable part.

---

## 6. Line — and the part that actually decides whether you get bit

**Braid:** the class term on the router row is **100–130 lb braid / PE6–8**; the technique note's working range is **80–100 lb**, with the explicit warning **don't over-gun the braid chasing a big-fish story — 65–100 lb covers it**, and much over 100 lb is only worth it on the biggest jigs. **80 lb sinks faster than 100 lb**, and **thinner braid means less line angle** and a jig that hangs straighter under the boat (`techniques/knife-jigging.md`).

Matched to your jig weights specifically (Cesar Chang, `ZrcwcugaEe4`): **65 lb braid for 200 g or lighter** (it gets a lighter jig down without working as much drag against it), **80 lb braid for 350 g and heavier**. Top-shot pairing: **100 lb mono on the 65 lb setup**, **~15 ft of 130 lb mono on the 80 lb setup**. His dated evidence that this isn't undergunned: a **140 lb bluefin hooked in the daytime landed on 65 lb braid** with a single-speed reel in 15 minutes (2023), and a 180 lb landed at ~450 ft on 80 lb braid with a two-speed in 6 minutes (2024) — contrasted with same-trip anglers on 100–130 lb braid and 450–500 g jigs getting *less* far down for the extra weight.

**A genuine conflict to know about, with the frame:** Ray Sharifi warns that anglers confuse the **daytime** jig guidance with the **night** guidance — daytime jigging with **light Colt-Sniper-class 80–120 g** jigs fishes **40–50 lb test**, while the night knife-jig bite has a **documented minimum of 80 lb, 80–100 lb recommended**, leader up to 200 lb (`RfiC8sfIWTk`). **That 40–50 lb figure is scoped to 80–120 g casting-jig-class gear, not to a 250–300 g jig at 300 ft.** Your program is the deep-jig program even though it's daylight, so it sits on the 65–100 lb side. At the far end, one captain's briefing set a floor of **100 lb braid and 100 lb mono, 200–400 lb leader, 350 g jigs and heavier**, with the caution "try not to drop down to 30 lb with a knife jig, the results might not be in your favor" (`oB4BpIUTTl4`).

**Mark your line, or none of the above matters.** A PCS panel calls failing to mark line to depth **the single most common mistake new bluefin jig anglers make** — a fish holding at **350 ft is not going to eat a jig worked at 250 or 550 ft** (`UP_3fBu7VPA`). Options in the notes: pre-marked color-metered braid (100 ft per color, some 25 or 30 ft), or Sharpie marks at your chosen interval — **25 / 30 / 50 / 60 / 100 ft** all appear; pick one and know it cold. Make each mark **12–18 in long, not a dot** — line runs off fast enough on a drop that a short mark gets missed entirely (`fgTmUq78ofQ`). For tuna specifically, **multi-color beats a single 100 ft interval**, because there's no bottom to reference: if the jig hesitates, note the color you were on, work that area, and drop back to the same color to get back in the zone (`t0kkwlrNwHk`). Worked example of the arithmetic: captain calls 200 ft, angler drops 7 colors × 30 ft = 210 ft, "right on the fish's nose" (`q_ciF1xiDiI`) — and the general rule is to go slightly past the call, e.g. down to ~220 ft on a "marking 200 ft" call, and work that column rather than 100 ft above or below it (`Et2TUskzCSs`).

**Drag:** fighting drag **20–30 lb on PE 4–8**, 25–40 on PE 6–10. But set your **strike drag lighter — 19–20 lb is the documented setting; 35 lb+ at strike can rip the outfit out of your hands on the first hookup** (`techniques/knife-jigging.md`, `Ul5FLB2dFgQ`).

**Two execution details that cost fish at this depth:** keep **light thumb tension on the spool through the fall** — it keeps the jig vertical instead of scoping, and it stops the backlash when a bite stops the spool dead (`Et2TUskzCSs`, `6_E5JCRvazc`). And **you are fishing water too deep to ever hit bottom** — so when free-spooling line suddenly stops paying out, the deckhands' stock answer is that it isn't bottom, it's a bite.

---

## 7. Against your own profile

Resolving this against `profiles/cameron/rods.md` and `profiles/cameron/tackle.md`: **you don't own this outfit, and I'm naming the gap rather than substituting.**

- **No knife/speed-jig rod or reel.** The gear-class lexicon lists the knife/speed-jig class as "Cameron shopping (open item)," and your rods file carries it as an open item — a dedicated SPJ/speed-jig setup for night bluefin plus September BOLA bottom yellowtail, ideally one setup for both.
- **No knife jigs in the box.** Your casting-jig inventory tops out at a **Daiwa Zakana 100 g** — which by Carson's ladder is a ~200 ft daytime jig at best and won't reach 300 ft.
- **Closest thing you own is the wrong tool for this:** the **Talica 25II two-speed / Phenix Axis HAX-C 800X3H (8'0", 3X-H, 60–130 lb), 100 lb braid** — that's the **rail-rod class**, your jumbo-foamer and troll rod. It's an 8 ft 3X-H, not a 5.5–6 ft parabolic PE 4–8, so it won't load or activate a 250 g jig the way the jig-rod rules above require, and the notes say fishing power off the rail rather than in-hand is exactly the wrong geometry for this technique.
- **What to buy against this answer:** a **PE 4–8, 5.5–6 ft, spiral/acid-wrapped** blank whose gram rating tops out near the jigs you intend to fish, on a **narrow two-speed** with 30 lb+ drag and 400–800 yd, spooled **65–80 lb metered braid**. That one purchase also covers the BOLA bottom-yellowtail program you flagged — the notes put slow-pitch bottom yellowtail at 130–250 g wing-fall jigs over high spots at 150–180 ft, inside a PE 4–8's activation window.

---

## What this KB does not cover for your question

- The 280 g and 300 g tiers of the one full weight ladder are given **by depth only — they are not labeled day vs. night**. There is no daytime-specific weight tier in the corpus above ~170 g; I'm bridging from depth-based rules and the router's "day 150–300 g" line.
- **No settled hook-count/placement doctrine** — the KB logs eight-plus attributed configurations side by side and explicitly does not reconcile them. I gave you the decision frame; the KB won't give you an answer.
- **No confirmed hook size table** for 250–300 g jigs. Carson's number is captioned "70 5x," flagged asr-uncertain (read as 7/0, 5X-strong); the only clean figure is a shop's Mustad 6/0 "universal."
- The "**US waters cap you at two hooks**" claim carries **no jurisdiction, no as-of date, and no verify-current stamp**, and the KB itself logs three-hook rigs fished in US waters. Verify before relying on it.
- **No daytime-specific leader test** for this depth band — leaders come as unreconciled ranges (130 lb / 200 lb fluoro / 200–400 lb mono) drawn largely from night and mixed-daypart sources.
- **No conditions were given** — no zone, season, current, wind, or expected grade — and the corpus insists the jig call is condition-driven, captain-called, and changes hourly. Treat the box above as a spread to bring, not a jig to tie on.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `techniques/knife-jigging.md`, `lures/knife-jigs.md`, `tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md`, `tackle/tackle-express-trophy-bluefin-jig-outfit.md`, `tackle/bluefin-rig-ladder-by-grade.md`, `tackle/jig-rod-rating-selection.md`, `tackle/gear-classes.md`, `rigging/assist-hooks.md`, `rigging/bite-leaders.md`, `techniques/flat-fall-jigging.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `vVOkxHx58Eg`, `gimFbgN5Jjk`, `149px8WQ2Ng`, `Ul5FLB2dFgQ`, `ZrcwcugaEe4`, `Et2TUskzCSs`, `G1YIlakiRqg`, `DTvXJrtytwg`, `PbiZMk4Ft6w`, `6_E5JCRvazc`, `U4zifdssSes`, `unARAuTgF_A`, `scmPq63lLWM`, `DuNkl8F45NE`, `Q4sW6JRQzAY`, `RfiC8sfIWTk`, `UP_3fBu7VPA`, `t0kkwlrNwHk`, `fgTmUq78ofQ`, `shZCjX2-fkI`, `oB4BpIUTTl4`, `BsWb5BQ1Tdc`, `q_ciF1xiDiI`  
*gaps admitted:* The KB has no daytime-labeled jig-weight tier above ~170 g — the 280 g/300 g tiers in the one full ladder (vVOkxHx58Eg) are given by depth only, not split day vs. night, so the 200-350 ft daytime band is bridged from depth rules plus the router's 'day 150-300 g' line. | No reconciled hook-count/placement doctrine exists — the KB logs eight-plus attributed configurations (single bottom pair no top hook; nose+tail singles; twins on the nose; single top + double bottom; dual-top; three-hook builds) side by side and explicitly refuses to reconcile them. | No confirmed hook size for a 250-300 g bluefin jig: Carson's figure is captioned '70 5x' and flagged asr-uncertain (read as 7/0 5X-strong); the only clean number is a shop's Mustad 6/0 'good universal size' assist. | The 'US waters cap you at two hooks' claim in lures/knife-jigs.md carries no jurisdiction, no as-of date and no verify-current stamp, and the same note logs three-hook rigs fished in US waters — it is unverified as a regulation. | No daytime-specific bite-leader test for the 200-350 ft band — leader figures (130 lb fluoro, 200 lb fluoro, 200-400 lb mono) come as unreconciled ranges from night and mixed-daypart sources. | No conditions were supplied in the question (zone, season, current, wind, expected grade), and the KB states jig selection is condition-driven and captain-called, changing hourly — so no single jig can be named, only a spread. | The flat-fall bite depth is itself unreconciled in the KB: 100-200 ft (an_uw-5pjfw / techniques/flat-fall-jigging.md) vs 250-350 ft (scmPq63lLWM), with neither source stating whether the gap is day vs. night, a different mark, or a different trip. | Cameron's profile contains no knife/speed-jig rod, reel, or knife jigs — the class is an open shopping item, so this answer resolves to class terms rather than owned gear.

</details>

<details><summary><b>NOW — review</b> · 11/12</summary>

# Daytime bluefin, knife jig, 200–350 ft

200–350 ft is 33–58 fathoms — the "fish sounded deep, wind up, no surface sign" row in the bluefin router ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)), which puts sounded daytime schools at **30–50 fathoms** (`HWx1jDTGsng`) and calls it a meter-and-jig game, not a troll.

One honest caveat before the numbers: [`techniques/knife-jigging.md`](techniques/knife-jigging.md) puts the **confident daytime SoCal bluefin zone at 150–240 ft, still workable to 300 ft** (`gimFbgN5Jjk`). So the bottom half of your window is squarely inside documented doctrine; **300–350 ft is at/just past the edge** of that source's daytime range — it's where the corpus starts handing the depth off to the night program.

---

## 1. Jig weight

**Start from the rule of thumb: ~1 g per foot of depth for a speed/knife jig** — "fish 200 ft down, go around 200 grams, you're safe" (`gimFbgN5Jjk`, [`lures/knife-jigs.md`](lures/knife-jigs.md)). A slow-pitch/wing-fall jig runs heavier at **~1.5 g/ft** because the extra weight offsets the flutter and keeps it vertical.

So your window is a **200 g → 350 g** knife-jig band. The corpus supports that from three directions:

| Source | What it gives for your depth |
| --- | --- |
| Searcher daypart/depth ladder (`vVOkxHx58Eg`), [`tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md`](tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md) | **~170 g** covers fish deeper than the 100 g jig's ~200 ft ceiling, as deep as **~250 ft**. **~280 g** is good to about **300 ft**, depending on current and wind — beyond that depth, or in wind, it may not reach. **~300 g** covers the same range. |
| Highliner deckhand working range, 2023 (`149px8WQ2Ng`), [`lures/knife-jigs.md`](lures/knife-jigs.md) | **200 g minimum, up to 300 g, occasionally 350 g**; stay below 400 g unless the current is really ripping. |
| Captain-called doctrine ([`techniques/knife-jigging.md`](techniques/knife-jigging.md)) | Jig weight is called **150–400 g** by depth and current: more current or deeper → heavier (200–300 g+) to hold the zone and stay horizontal; a lighter **~220 g** fluttery jig works the upper column when fish sit 150–200 ft down. |

**Practical box for this window:** 200 g, 250 g, 300 g as the core, with a **170 g** for the top of the column and a **350 g** for wind/hard drift. Carrying a spread rather than one jig is explicit doctrine — the jig that gets bit changes day to day and can't be predicted (`DuNkl8F45NE`, [`tackle/tackle-express-trophy-bluefin-jig-outfit.md`](tackle/tackle-express-trophy-bluefin-jig-outfit.md)); one crew "found the cadence" mid-trip by adjusting light-to-heavy jigs through the day and landed 9–11 bluefin (`gimFbgN5Jjk`).

**Shape, then color — the ranked priority is depth → weight, current → shape, color last** (`gimFbgN5Jjk`):
- Fast drift or wind → **longer and more slender** so the jig cuts water and falls straight.
- Slack or light wind → **fatter and more fluttery** for hang time and action.
- Windy "hot dog style" alternative: a short, stubby, blunt **170–250 g** profile (West Coast HD, Daiwa SK, Shimano Flat-Fall class) that sinks faster and flutters on the way down, specifically for when chop makes a slim jig hard to keep vertical (`G1YIlakiRqg`).
- Calibrate off the first drop: a jig that should sink straight but starts to scope out is telling you to go **narrower/longer or heavier** (`Et2TUskzCSs`).

**Check what you actually bought.** The finger-balance test: a speed/knife jig tips **tail/butt-heavy** at the midpoint; a slow-pitch/wing-fall jig **balances flat**. The Rip Roller is popular as a "knife jig" but reads as a wing-fall jig on that test and gets bit on the fall (`ZrcwcugaEe4`, `5XWnm7ok09k`) — don't assume fall behavior from the model line.

## 2. Hook rig

Two fixed constraints first ([`lures/knife-jigs.md`](lures/knife-jigs.md)): **US waters cap a jig at two hooks**, and **a captain's stated boat policy overrides everything** — many sportboats require twin bottom hooks only, for crew safety, not action (`gimFbgN5Jjk`).

Absent a boat rule, at 200–350 g the corpus gives you three defensible builds and does not reconcile them:

- **Nose + tail singles (the weight-tier match for your jigs).** At the **280 g and 300 g** tiers the pick is heavy single hooks, one off the nose and one off the tail — captioned "70 5x", read as **7/0, 5X-strong** (exact number asr-uncertain) (`vVOkxHx58Eg`). Reason: bluefin frequently bite the jig **as it sinks**, don't get a clean aim, and can hit either end. Trade-off: a hooked fish can snag the *other* hook and come in sideways, which takes more pulling force to land.
- **Two hooks off the nose end — if you're speed/fast-pitch jigging** (mechanical cranking retrieve). That's the stated best placement for that retrieve style, sized around a 220 g jig (`vVOkxHx58Eg`). This is the one to pick if you're ripping rather than dropping-and-waiting, and it's consistent with the assist-cord logic below.
- **Single bottom assist pair, no top hook** — [`techniques/knife-jigging.md`](techniques/knife-jigging.md)'s own baseline, stated for the **night** bluefin bite: the fish suck the jig in so a top hook adds little, and a top hook fouls fish in the cheek/pec, moving the fight off the mouth and putting a hook near the rail at gaff.

**Decision frame** (the KB keeps these side by side, so here's what the choice actually turns on): boat rule first → then **retrieve style** (cranking speed-jig retrieve → nose-paired; drop-and-work with bites on the sink → nose+tail) → then **jig profile**: short heavy profiles → twin assists on the bottom only; long profiles → one top and one bottom; small 100–150 g jigs → a single nose assist (`gimFbgN5Jjk`). Section order above is not a ranking.

**Safety rule that overrides all of it:** never add extra hooks to a lure already rigged with a treble (`vVOkxHx58Eg`). If you're fishing the ~100–170 g end of the range on a treble jig (the ladder keeps trebles up through 170 g — a heavy-duty **size 20 treble** on the 100 g jig), it stays single-treble. Stock hooks are rarely worth fishing as-is on any of these.

**Building the assist** ([`rigging/assist-hooks.md`](rigging/assist-hooks.md), `U4zifdssSes`, `unARAuTgF_A`):
- **Pass-through sizing test:** hold the hook against the jig body — it should be just wide enough to pass all the way through. Oversized interferes with the swim. (Demo speed jig landed on a size 7; the test is the parameter, not the model.)
- **Position:** a single top assist rests roughly **one third of the way down** the jig's total length.
- **Cord stiffness is the day-vs-night tell:** stiffen a speed-jig assist cord with shrink tubing over the cord itself, so the hook stays **stationary** — a speed jig gets bit on the pump/upswing and you want the hook exactly where the fish eats. A slow-pitch/fall-bite jig wants a **softer, flopping** cord instead. Since daytime bites flip to mostly **on the rise** (`Et2TUskzCSs`), the stiff-cord speed build is the right one for your window.
- **Cord:** 180 lb hollow-core PE (splices back into itself), or ~215 lb mono-core for a single top assist / ~300 lb for a tail double (both asr-uncertain caption figures).
- **Double-hook orientation:** tie each hook from the back of the shank forward toward the point so the two points ride **outward** — they must never cross or lock.
- **Ring vs. swivel at the jig:** a welded/solid ring split-ringed to the jig is the default for longer bluefin jigs — a swivel accentuates flutter, and on an already-fluttery jig that makes it *less* attractive; a solid ring also keeps the jig in plane as it rises on the rip. Exception is jig-specific: a jig that flutters little on its own benefits from the swivel (`Et2TUskzCSs`).

## 3. Leader and terminal

The corpus does not settle on one daytime test — here are the builds as stated:

- **Matched to your weight tier:** **200 lb fluorocarbon, ~2.5–3 ft**, to a **~400 lb test swivel** at 280 g; 200 lb fluoro ~3 ft at 300 g (`vVOkxHx58Eg`).
- **Base bite-leader build:** **130 lb** fluoro over 80–100 lb braid, **capped at 2–2.5 ft** — because the large swivel crimped to the top end won't wind through the guides, and a longer leader strands you at the top-shot connection with the fish still at deep color (`kO_BqzUYayc`, [`rigging/bite-leaders.md`](rigging/bite-leaders.md)). Crimp: size 1.6 crimp + matching 1.6 chafe sleeve on 130 lb fluoro, two snug presses per crimp — over-crimping bites into the fluoro. For a single-jig leader, crimp direct through the jig's solid wire ring; use a split ring only for one leader swapped across several jigs.
- **Daytime jig ladder:** **100 lb mono or fluoro, 30–40 ft**, on the PE 4–8 one-rod build working 150–250 g jigs (`G1YIlakiRqg`). Jig leaders run long here deliberately — long enough to stay invisible, short enough that the lure doesn't drag excess thick line down or sink slower.
- **Triple-digit program:** **200–300 lb** standard, up to 400 lb for heavy night (`DuNkl8F45NE`).
- **Daytime TG-jig re-rig:** a standard assist hook on **80 or 100 lb** (`A7rveRBkL-g`).

The reason the leader is heavy at all: bluefin inhale the jig deep, and braid or lighter mono sawing against teeth and gill rakers cuts (`kO_BqzUYayc`). Size for the worst case — a 20 lb schoolie and a 300 lb trophy eat the same drop.

## 4. Rod and reel class

**Class: knife / speed-jig class** — a rod that vertically rips a 150–400 g jig, thin braid, assist hooks ([`tackle/gear-classes.md`](tackle/gear-classes.md)).

**Rod — PE 4–8 is the match for 200–350 g** ([`tackle/bluefin-rig-ladder-by-grade.md`](tackle/bluefin-rig-ladder-by-grade.md), `Et2TUskzCSs`, `gimFbgN5Jjk`):

| Class | Activates | Fighting drag |
| --- | --- | --- |
| PE 3–6 | 100–250 g | ~15 lb, max ~25 lb |
| **PE 4–8 ("80 lb stick")** | **150–350 g** | **20–30 lb** (30 lb the realistic ceiling) |
| PE 6–10 ("100 lb stick") | 250–500 g (activates as light as 200 g) | ~25 lb start, some push to 40 lb |

PE is a **diameter/line-class window, not a strength spec** — roughly PE × 10 ≈ lb test, 65 lb ≈ PE5 (`Ul5FLB2dFgQ`). PE 4–8 is also named as the **single rod to bring if bringing one**, and as the one-rod answer if buying only one, fishing jigs from about 150 g up (`gimFbgN5Jjk`, `G1YIlakiRqg`).

Key selection rule: **pick the lightest rod that still activates the jig, not the heaviest one that can.** A 250 g jig that both a PE 4–8 and a PE 6–10 can technically move does noticeably better on the PE 4–8 (`gimFbgN5Jjk`).

Physical spec: **short and parabolic — 5.5–6 ft** in the two-rod sportboat quiver (`gimFbgN5Jjk`); the short parabolic blank lets the jig dart and gives leverage with less fatigue than a rail rod. **Spiral / acid-wrapped guides** are standard: less side-to-side twist under load, and the geometry stops line grabbing the tip during the jigging stroke. Fish it **in hand, not racked** — laying it flat on the rail throws away roughly half the rod's power (`Ul5FLB2dFgQ`).

**Reel — any narrow two-speed, "narrow" meaning under 2 in of spool width** (`gimFbgN5Jjk`). Wider spools let line dig into itself under the 15–30 lb of drag jigging commonly runs, and once it digs it can't pay out cleanly. Named benchmarks spanning the class: a **Shimano Talica 20** at the light end (valued for a free-spool that gets a jig down fast) up to a **Penn International 50** on 130 lb at the heavy end (`6_E5JCRvazc`); a **Penn Fathom** is called out as strong value — big, high-capacity, two-speed — with the caveat that the stock handle is thin enough to snap, so budget an aftermarket handle. The daytime ladder's specific pick for this rod: **Jigging Master PE7, or the budget Fathom 40** (`G1YIlakiRqg`).

**Line — this is where the KB openly disagrees with itself.** [`techniques/knife-jigging.md`](techniques/knife-jigging.md) splits by daypart: a **light/day outfit (200 g and under jigs) runs 65 lb braid to a 25 ft, 80 lb top shot**; **80 lb braid with a ~15 ft, 130 lb mono top shot for 350 g+ jigs**; 100 lb braid to a 130 lb top shot is the heavy/night outfit. The bluefin router publishes the class as **100–130 lb braid / PE6–8** instead, and that contradiction is flagged in the note itself.

**Decision frame:** thinner braid means less line angle in the water, a jig that hangs straighter under the boat, and a faster drop — and a rod and reel can't generate enough drag to break 80 lb braid by pulling alone, while thinner braid usually cuts *through* a tangle with thicker braid rather than losing (`Ul5FLB2dFgQ`, `ZrcwcugaEe4`). For a daytime 200–350 ft drop, **80 lb braid is the defensible middle**: it's the stated pairing for the heavier end of your jig range, and 100–130 lb is the group the same source says put more scope and belly in the water. The daytime ladder independently runs **80 or 100 lb Power Pro Max Quattro** on that PE 4–8 rod (`G1YIlakiRqg`). Note the countervailing floors: 80 lb minimum (80–100 recommended) with leader to 200 lb for the night bite, since a night stop can produce anything from a 20 lb schoolie to a 200 lb+ cow (`RfiC8sfIWTk`, `UfuiWFVvz2E`).

## 5. Things that decide whether this works at 200–350 ft

- **Drag: set strike drag at 19–20 lb.** The common online 35 lb advice is dangerous — one trip lost **five jigging outfits** ripped out of anglers' hands (`Ul5FLB2dFgQ`).
- **Mark your line, in 12–18 in marks, not dots** — line runs off fast enough on a drop that a short mark gets missed. Documented intervals: 25, 30, 50, 60, 100 ft; pick one and know it cold. For tuna specifically, **multi-color beats a single 100 ft interval** because there's no bottom to read off: note the color you were on when the jig hesitated, and drop back to it (`Ul5FLB2dFgQ`, `fgTmUq78ofQ`, `t0kkwlrNwHk`). Failing to mark line at all is called the single most common beginner mistake — a fish at 350 ft won't eat a jig worked at 250 or 550 (`UP_3fBu7VPA`).
- **Position, or your 300 ft mark is an 80 ft jig.** From the bow, throw up-current, let it sink straight, walk back toward the stern as it settles. From the stern, cast down-swell/downwind so the boat drifts onto the jig. Keep light thumb tension through the fall — it keeps the jig vertical and gets it down faster than a free fall, and thumbing off completely means a bite that stops the spool backlashes you (`Ul5FLB2dFgQ`, `G1YIlakiRqg`, `Et2TUskzCSs`, `6_E5JCRvazc`).
- **Overshoot the call, then work up:** a captain's call of 240 ft becomes a drop to about 300 ft and a retrieve back up through 180–240 ft — documented independently, same figures, three years apart (`gimFbgN5Jjk`, `AyN9MBWg-XY`). Otherwise work the called depth, not 100 ft either side of it (`Et2TUskzCSs`).
- **"When you hit bottom, you're bit."** These jigs are fished over water too deep to touch bottom, so line that suddenly stops paying out is a bite (`6_E5JCRvazc`).
- **Daytime bite timing flips.** At night ~70–80% of bites come on the fall; **by day it flips to mostly bites on the rise** — the reaction-bite mechanism this technique is built on (`Et2TUskzCSs`, `G1YIlakiRqg`). Day tackle also scales down: thinner line, smaller jigs, more refined presentation, because the fish can see it. Slack the line on the drop — a tight line puts resistance on the jig's nose and kills the dart.
- **Hookset:** don't wind on it like bait. Wait until **drag is actually running** off the reel, then palm/claw the spool and give **three or four hard sideways swings** to drive the point past the barb — a jig-hooked fish sticks just above the barb on a hard point of jaw, and an unset hook bends open under load no matter how heavy the wire (`Ul5FLB2dFgQ`).
- **Missed it? Free-spool straight back down** — don't wind up first. About 8 out of 10 times you get bit again (`G1YIlakiRqg`).
- **Fight:** point the rod tip at the fish's face for roughly 90% of the fight rather than pumping; cut off its circles in the end game (`Et2TUskzCSs`).

## 6. If you'd rather fish it passively

At this depth the flat-fall alternative is real: the router's flat-fall row puts the bite zone at ~100–200 ft with the captain calling depth, on a two-speed **rail-rod class** outfit (`an_uw-5pjfw`), and [`techniques/flat-fall-jigging.md`](techniques/flat-fall-jigging.md) carries deeper data points — 250–300 ft (`shZCjX2-fkI`), 240–360 ft with a stated **250 g floor** at that depth — worked examples at 250 g and 300 g. Free-spool to the mark, count the sink, most bites come on the fall, and wind back up about halfway before re-dropping rather than cranking to the top.

## 7. Against your own box

Your profile ([`profiles/cameron/rods.md`](profiles/cameron/rods.md), [`profiles/cameron/tackle.md`](profiles/cameron/tackle.md)) has **no knife/speed-jig outfit and no knife jigs** — the gear-class lexicon literally lists this class as "Cameron shopping (open item)," and your rods note carries the open item of shopping a dedicated SPJ/speed-jig setup for night bluefin plus September BOLA bottom yellowtail. Naming the gap rather than substituting: the closest thing you own is the **Talica 25 on the Phenix Axis HAX-C 800X3H (8'0", 3X-H, 60–130 lb, 100 lb braid)** — that's rail-rod class, not knife-jig class. It will fight the fish, but an 8 ft 3X-H rail rod is not a 5.5–6 ft parabolic PE 4–8 blank and won't activate a 250 g jig the way the class calls for. The **Trinidad 40 (8'0" XH, 40–80 lb, 80 lb braid)** is yo-yo/heavy-iron class — same mismatch, lighter. If you're buying one rod for this, the corpus's own one-rod answer is a **PE 4–8 rod with a Fathom 40 (budget) or Jigging Master PE7, 80–100 lb braid**.

---

**What I did not do:** you gave no zone, month, sea state, or grade, so I ran no conditions pull, no seasonal priors, and no zone selection — this is the gear answer only, gated to the SoCal Bight / northern Baja bank-and-open-ocean water these notes apply to.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `species/bluefin-tuna.md`, `techniques/knife-jigging.md`, `techniques/flat-fall-jigging.md`, `lures/knife-jigs.md`, `rigging/assist-hooks.md`, `rigging/bite-leaders.md`, `tackle/searcher-bluefin-jig-ladder-by-daypart-and-depth.md`, `tackle/bluefin-rig-ladder-by-grade.md`, `tackle/tackle-express-trophy-bluefin-jig-outfit.md`, `tackle/tackle-express-night-bluefin-tg-jig-rig.md`, `tackle/gear-classes.md`, `profiles/cameron/rods.md`, `profiles/cameron/tackle.md`  
*videos:* `vVOkxHx58Eg`, `gimFbgN5Jjk`, `Ul5FLB2dFgQ`, `G1YIlakiRqg`, `Et2TUskzCSs`, `149px8WQ2Ng`, `ZrcwcugaEe4`, `6_E5JCRvazc`, `U4zifdssSes`, `unARAuTgF_A`, `kO_BqzUYayc`, `DuNkl8F45NE`, `UfuiWFVvz2E`, `RfiC8sfIWTk`, `A7rveRBkL-g`, `an_uw-5pjfw`, `shZCjX2-fkI`, `fgTmUq78ofQ`, `UP_3fBu7VPA`, `AyN9MBWg-XY`, `t0kkwlrNwHk`, `5XWnm7ok09k`, `HWx1jDTGsng`, `cameron`  
*gaps admitted:* No settled daytime jig weight for 200-350 ft: the KB explicitly keeps three unreconciled ranges side by side (Searcher's 100-400 g by light level, knife-jigs' 150-500 g by depth/current, the trophy outfit's ~200-500 g and a 2025 recap widening it to 160-560 g), and the bluefin router carries a flagged internal contradiction between its own 150-300 g daytime floor and Searcher's ~100 g most-used daytime jig. | No daytime-specific hook count/placement rule exists for the 200-350 g tier. The nose+tail rule at 280-300 g comes from a ladder organized by light level, and the single-bottom-assist-pair baseline is stated for the night bite; the KB says fleet hook count/placement is unresolved and no configuration is correct over another. | No vetted hook-size table by jig weight. The only figures are a captioned '7/0 5X-strong' (asr-uncertain) at 280-300 g, a Mustad 6/0 called a 'good universal size', and a size 7 Owner SJ51 on one demo speed jig - the pass-through sizing test is the transferable parameter, not a number. | Daytime leader test at this depth is not settled: 200 lb fluoro 2.5-3 ft (Searcher tier), 130 lb base bite leader capped at 2-2.5 ft, 100 lb mono/fluoro at 30-40 ft (daytime ladder), 200-300 lb (trophy program), 80-100 lb (daytime TG re-rig) - the KB states these side by side without reconciling. | Braid class for daytime jigging is internally contradicted: knife-jigging states 65-100 lb (65 lb for 200 g-and-under, 80 lb for 350 g+) while the bluefin router publishes 100-130 lb / PE6-8; the flag is carried in the note itself and no source resolves it. | 300-350 ft sits at or past the edge of the corpus's documented confident daytime window (150-240 ft, workable to 300 ft); the KB has no daytime-specific doctrine for the deeper half of the asked range. | Cameron's profile owns no knife/speed-jig rod, reel, or knife jigs - the class is logged as 'Cameron shopping (open item)', so no owned-gear resolution was possible and the gap is named rather than substituted. | The prompt gave no zone, month, sea state, grade, or launch point, so no conditions pull, seasonal priors, or zone/timing selection was performed - this is the gear answer only. | Several named products in the underlying sources are asr-uncertain and/or low-confidence sponsored picks (Williamson Gomame, 'Williamson kensaki', 'Eddie bomb', Mustad/Nomad Rip Roller naming), so model-level picks cannot be asserted from this KB - only the weight/hook/class parameters.

</details>

### 9. [gear] What is a jig stick, and what is a rail rod? How do they differ and what is each for?

**Winner:** NOW · mapping {'A': 'B3', 'B': 'B2', 'C': 'NOW'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 1 | 2 | 2 | 2 | 2 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** A and C both answer the actual question — a rail rod is defined by its long hypalon foregrip braced on the rail, a jig stick by length that loads a pendulum cast — and both carry the four-tier Searcher ladder, the fish-the-middle-of-the-rating rule, the 7 ft floor, and the gear-ratio conflict left unreconciled. C edges A by grading its own evidence (sponsored-claim caveat on the named Seeker models, confidence: medium on the ladder note, the open fact-check flag on the jig-stick length band), by giving a complete worked outfit (OSP 1x3 + Fathom 60 two-speed + 100 lb spectra + top-shot options), and by resolving both classes against the angler's actual rods so the definition becomes a pick-this-rod decision. B is the strongest of the three on the jig stick specifically — top-shot sizing by destination, release point, reel-on-its-side — but its version of the KB apparently lacks the rail-rod foregrip material, so it honestly admits it cannot say why a rail rod is called that; the honesty is exemplary, the coverage of half the question is not.

- *B2 reasons:* found: excellent on the jig stick, but the core of 'what is a rail rod' is missing — no foregrip/bracing mechanic, and it says outright the KB never connects the name to rail fighting; the answer is about a heavy tuna rod, not a rail rod. specific: strong numbers — 1.8-2+ oz casting weight, 40 lb full-day vs 50 lb overnight top shots, 150 lb wind-on at 20-25 ft, 300 lb kite leader, 100-300 lb fish. sourced: dense note paths and ids throughout, conflicts kept side by side. scoped: Baja panga vs SoCal island distinctions labeled, no bare regulations. honest: the most candid gap list of the three (2x4 undefined, four irreconcilable braid figures, no rail construction detail); no relative time. actionable: rigging and fighting are executable, but a reader still would not recognize a rail rod in a shop.
- *B3 reasons:* found: nails both classes from the lexicon plus the class-specific notes, and gets the physical distinction right (foregrip, not power rating). specific: 8-10 ft / 2-4 oz / 25-60 lb, 2-to-9-o'clock swing, 18 in hang, 42 in/crank, the full four-tier ladder with line/reel/grade ceilings, 6-8 in extra foregrip. sourced: every parameter carries a note path and a video id, ladder attributed to Steve Carson sjOJiR6_HJ4. scoped: SoCal sportboat framing stated explicitly, Cortez panga material labeled as a different-region contrast; no bare regs (the IGFA 2001 note is dated and historical). honest: flags no standalone note for either rod, the unreconciled 8 ft vs 7 ft rail length, the missing rail casting mechanics, all sportboat-framed; no relative time. actionable: an angler could buy, set up, cast and fight from this.
- *NOW reasons:* found: covers both classes fully — foregrip-on-rail definition, 7 ft floor, jig-stick length doctrine, plus the applications (flat-fall, yo-yo, trolling) each class actually serves. specific: S-glass ~20% lighter, elbow-to-middle-finger reel placement, four-tier ladder with fish-the-middle rule, OSP 1x3 / Fathom 60 / 100 lb spectra worked outfit, flat-fall 100-360 ft, top-shot sizing by destination. sourced: note paths plus video ids on essentially every claim, and it grades them — sponsored-claim caveat on named models, confidence: medium on the ladder note, evidence file cited. scoped: SoCal multi-day-boat framing named, Baja panga argument labeled as such, no regulatory claims. honest: surfaces the KB's own open fact-check flag on jig-stick length, the unreconciled foamer-casting vs lexicon conflict, Tier 4 length simply unstated, no head-to-head note exists. actionable: adds profile resolution mapping each class to the angler's actual rods, which turns definition into a pick-this-rod decision.

<details><summary>Full prompt</summary>

What is a jig stick, and what is a rail rod? How do they differ and what is each for?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

# Jig stick vs. rail rod

Short version, straight from the class lexicon in [`tackle/gear-classes.md`](tackle/gear-classes.md):

- **Jig stick** = the **surface-iron / jig-stick class**: **8–10 ft, moderate/fast action, casts 2–4 oz irons, ~25–60 lb**. It is a *casting* rod. Its whole job is distance.
- **Rail rod** = the **rail-rod / heavy tuna class**: **~8 ft, 3X-H, 60–130 lb, paired with a 2-speed reel**. It is a *leverage* rod. Its job is casting at and then beating jumbo bluefin.

They sit at opposite ends of the same offshore ladder, and the point of the ladder is line class, not brand — "the lesson isn't the exact rods — it's the **ladder of line classes** and having a dedicated tool at each rung so you're not under- or over-gunned when the grade shows up" ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md), `xPFm_ZV2PZU`).

---

## The jig stick

**What it is.** 9–10 ft, medium-heavy, with a tip soft enough to load and cast a heavy iron but real backbone underneath ([`techniques/surface-iron.md`](techniques/surface-iron.md)). Reel is a **narrow high-speed conventional** (Tranx-500 class), thumb-controlled — roughly **42 in of line per crank** on a high-gear model, which is what lets you cover everything from a slow grind up to yellowtail speed just by changing cadence (same note).

**What it's for.** The long-cast surface-iron game, and its neighbors:
- Yellowtail boiling on top or working a kelp paddy — a 9–10 ft jig stick throwing a Tady 45 / JRI Stinger class iron ([`species/yellowtail.md`](species/yellowtail.md))
- Surface-feeding calico and sand bass, barracuda, bonito ([`techniques/surface-iron.md`](techniques/surface-iron.md))
- White seabass on a color edge — jig-stick class, 7–9 ft, 40–50 lb ([`species/white-seabass.md`](species/white-seabass.md))
- Bluefin/yellowfin foamers, on a **beefed-up** version of the same class ([`techniques/foamer-casting.md`](techniques/foamer-casting.md))

**Why it's long.** "The distance IS the technique" — the long rod is what buys it, and **the rod does all the work**; the classic mistake is shoving the lure out with your arms instead of loading the blank. Hang the jig about **18 in** below the tip, take the rod back to **2 o'clock**, let the blank load, then sweep down to **9 o'clock**. Build the swing with an **up-and-down pendulum, not a side-arm sling** — a longer rod gives a longer pendulum arc, hence more distance (Scotty, Brothers Sportfishing, `VpW91AKOFVQ`). Retrieve with the **tip pointed down at the water** so the iron kicks side to side; tip-up drags it onto the surface and it stops swimming (same source, corroborated by Dave Hansen, `3dVc-2rsYII`). Two smaller distance tricks: release on the **outside of the swing**, not the top or bottom of the arc (`3dVc-2rsYII`), and **lay the reel on its side** through the cast so the spool rides one bearing (`KLoEJInlmZo`).

**Line.** The KB gives you a spread here rather than one number, and doesn't reconcile it:
- Class rating **~25–60 lb** ([`tackle/gear-classes.md`](tackle/gear-classes.md))
- **40–65 lb braid** in the application table ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md))
- "up to **65** on a jig stick" under the downsize-don't-upsize rule — 65 lb braid is about the diameter of 20 lb mono, so fishing 65 for everything is a mistake ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), Academy Ep16, `aXF0bxAFtU0`)
- **~80 lb braid main**, with a short **50 lb, ~18 in** mono/fluoro leader to a **100 lb clip** tied straight to the iron, so you can swap irons without retying ([`techniques/surface-iron.md`](techniques/surface-iron.md))

A competing rigging philosophy is kept side by side rather than merged: a **10 ft, 30–60 lb** rod (Phoenix Axis 1009 HJ) running **50–80 lb braid backing to 80–100 yards of 40–50 lb mono top shot** straight to the iron, no short leader and no clip (Ray Sharifi, `A70kK2niu2Q`, `LTCFjqtSI8g`). His top-shot sizing is location-based: **40 lb** for full-day islands (Coronados, Channel Islands, Catalina), **50 lb** for overnight range (San Clemente, Santa Barbara Island) and anywhere in Baja, because those spots carry a trophy shot at any moment. Casting weight on that rod runs **roughly 1.8 to 2+ oz**, with a **Salas 7X** among the heavier picks (`LTCFjqtSI8g`). One thing that *is* consistent: on irons specifically, run the **thinner end** of your top-shot range — a thick top shot dampens the iron's swim, a penalty stickbaits and poppers don't pay (Cesar, Eric's Tackle, `F7jLrt2j2X8`).

**Shorter jig sticks are a real, attributed position, not a compromise.** A Baja/Sea of Cortez quiver prefers **8 ft, 20–50 lb** over the "purist" 9 ft standard, specifically because a panga is a small platform — a 9–10 ft rod makes it hard to work a fish close enough for the short 4–5 ft gaffs typically carried (Cesar, `M8hOYQ_6rSg`). And one Cedros angler's favorite for the technique was an **8 ft extra-heavy rated 30–80 lb**, chosen precisely *for* casting distance (`u0scEBby7nA`). There's also a heavier tier: a **9 ft, 30–80 lb** (Axis 909 HJ) for fired-up schoolies (7–15 lb) where fast fight-unhook-recast cycles bank more fish, and for Baja structure where you need backbone to muscle a fish out of the reef (`LTCFjqtSI8g`).

---

## The rail rod

**What it is.** **~8 ft, 3X-H, 60–130 lb, 2-speed reel** ([`tackle/gear-classes.md`](tackle/gear-classes.md)). Written as **"rail rod 2x4 / 50–100 lb"** with an **HD30 / Fathom 60-size 2-speed** and **130 lb braid** in the application table ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)).

**What it's for.** One job: **casting at and fighting jumbo bluefin**. It's rung 5 — the top rung — of the five-setup San Diego offshore quiver (`xPFm_ZV2PZU`).

**How it's rigged.** 130 lb braid, then a **Bimini twist or splice to a wind-on leader, 150 lb blue label, ~20–25 ft, crimped to a snap swivel** (`xPFm_ZV2PZU`). The Bimini is the standing double-line ahead of the top shot on rail-rod big-tuna setups, and a **worm knot** is the specific connection that ties a mono top shot onto that Bimini loop — it's also the fast mid-trip field repair, because the twisted section survives when you cut the knot away ([`rigging/essential-knots.md`](rigging/essential-knots.md)). If the same outfit goes to a kite flyer rig, it steps up again to **300 lb line, a 10/0–11/0 J hook and an extra-heavy treble** (`xPFm_ZV2PZU`).

**How it gets fished.** [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md) documents the beltless, boat-leverage fighting style used on **100–300 lb** fish — three independent trips describe the same mechanic:
- Rod butt **under the left armpit**, reel hand on the handle, **no fighting belt or harness** — coached on camera as "you're off the belt." Visiting East Coast anglers used to harness fighting found it awkward on their first fish (`usHl-4SfqDA`)
- **Squat down and stand up, using the boat as leverage**: wind down as the boat travels **down the back of a swell**, hold or ease off as it **rises** (`usHl-4SfqDA`, `xzIaUEDklrE`)
- Kneel, butt under the armpit, and **even half a crank on the way down still counts as gained line** (Tanner Bank, late Oct 2021, `vCskOx6N-XM`)
- One operation names the whole locked-to-the-rail style **"railroading"** — "lock the rod to the rail and let your body in the boat do the work" (`mDmbGdQAy-4`)

Alternatively the rod stays **in the gunnel holder** entirely while the captain gear-taps the boat in and out of gear to winch the fish in; on that program, hand-fighting a big bluefin in a harness at **30–40 lb of drag** is treated as a personal-endurance choice, not a functional advantage (same note).

**A worked example of the class:** Cameron's Talica 25 setup — Phenix Axis HAX-C 800X3H, **8'0", 3X-H, 60–130 lb, cross-cut 4-slot aluminum gimbal butt**, Shimano Talica 25II 2-speed, **100 lb braid**. Role: main heavy setup, commonly **trolling** ([`profiles/cameron/rods.md`](profiles/cameron/rods.md)).

---

## Side by side

| | Jig stick | Rail rod |
| --- | --- | --- |
| Length | 8–10 ft (9–10 ft the standard) | ~8 ft |
| Power | Moderate/fast, MH — tip loads to cast | 3X-H / "2x4" |
| Line class | ~25–60 lb rating; 40–65 lb braid | 60–130 lb rating; 130 lb braid |
| Reel | Narrow high-speed conventional, star drag fine | HD30 / Fathom 60-size **2-speed** lever drag |
| Throws | 2–4 oz irons (working weight ~1.8–2+ oz) | Big metal / poppers at jumbos; also trolls |
| Design goal | **Cast distance** | **Leverage under load** |
| Target | Yellowtail, calico, sand bass, barracuda, bonito, WSB, foamer tuna | Jumbo bluefin, 100–300 lb |
| Note | [`techniques/surface-iron.md`](techniques/surface-iron.md) | [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md) |

The physical middle rung between them is the **yo-yo / heavy-iron class** — ~8 ft, XH, 40–80 lb, fast crank ([`tackle/gear-classes.md`](tackle/gear-classes.md)) — which is why a heavy jig stick often doubles as a yo-yo rod but a rail rod never doubles as a surface-iron rod.

---

## Where the line between them actually blurs

For a **bluefin foamer**, the KB does not send you to a rail rod — it calls for a **"beefed jig-stick class"** with backbone to lever a deep fish up to color, since these can be 200 lb+ ([`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`techniques/foamer-casting.md`](techniques/foamer-casting.md)). Two practical constraints push against reaching for the true rail rod to cast:

- **Rod length caps around 9 ft for casting safety** — 8 ft is fine, longer than 9 ft gets dangerous, especially for anglers not on the bow (Cesar, `F7jLrt2j2X8`)
- For the casting application, a **star drag, 20–25 size up to a 30 max** is all you need; a bigger reel and a lever drag's heavier spool are harder to cast. Spinning gear handles yellowfin **to 50 lb** fine; **100 lb-class bluefin** is where it starts to struggle (same source)

And too much rod is a real failure mode, not a theoretical one: on a **60–130 lb-rated** stick (Black Diamond Hybrid + Talica 25), the same angler found it **too stiff on 40–50 lb-class bluefin** — it wants to stay straight and won't hold a consistent bend — while on **80 lb-and-up fish** the stiffness "worked to our benefit" (`-MP2RqJC7B0`, vs. his own write-up of the setup in `gevNj2Y1Ep8`).

Cameron's own position sits right on that seam and is logged as an **attributed open item, not doctrine**: he'd cast his heaviest **jig-stick/rail-class** setup (the Talica 25) at a jumbo **80–140 lb** foamer school ([`species/bluefin-tuna.md`](species/bluefin-tuna.md), [`profiles/cameron/rods.md`](profiles/cameron/rods.md)). Separately, he owns a **10 ft jig stick** he always brings to BOLA but rarely uses, and wants reps hooking and landing yellowtail on it ([`species/yellowtail.md`](species/yellowtail.md)).

One more practical difference if you're casting a long jig stick at tuna: a popper is awkward to sweep sideways on a 9–10 ft rod, so keep the **tip high and burn 2–3 reel turns** to jump it instead ([`techniques/foamer-casting.md`](techniques/foamer-casting.md)).

---

## What this knowledgebase does *not* tell you

I want to be straight about the edges of what I could verify here:

- **Why a rail rod is called a rail rod.** No note in this KB states the etymology. The rail-fighting mechanics are documented in [`techniques/fighting-big-bluefin.md`](techniques/fighting-big-bluefin.md) and the class is named "rail-rod" in [`tackle/gear-classes.md`](tackle/gear-classes.md), but nothing here explicitly connects the two. I'm not going to assert the link from outside knowledge.
- **What "2x4" means.** It appears twice in [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) as shorthand for the rail-rod class and is never defined.
- **Rail-rod construction details** — bent vs. straight butt, roller guides, foregrip length, blank taper. The only build specific anywhere is Cameron's cross-cut 4-slot aluminum gimbal butt in his profile.
- **How to cast a rail rod.** All the cast mechanics in the KB are jig-stick mechanics.
- **The jig-stick braid number.** Four notes give four different figures (25–60 lb class / 40–65 lb / up to 65 / ~80 lb main) and none of them arbitrates.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `tackle/line-and-leader.md`, `techniques/surface-iron.md`, `techniques/fighting-big-bluefin.md`, `techniques/foamer-casting.md`, `techniques/yo-yo-iron.md`, `rigging/essential-knots.md`, `lures/iron-jigs.md`, `species/bluefin-tuna.md`, `species/yellowtail.md`, `species/white-seabass.md`, `profiles/cameron/rods.md`  
*videos:* `xPFm_ZV2PZU`, `VpW91AKOFVQ`, `F7jLrt2j2X8`, `M8hOYQ_6rSg`, `LTCFjqtSI8g`, `A70kK2niu2Q`, `42A8Owhc8fw`, `gevNj2Y1Ep8`, `-MP2RqJC7B0`, `aXF0bxAFtU0`, `3dVc-2rsYII`, `KLoEJInlmZo`, `u0scEBby7nA`, `usHl-4SfqDA`, `mDmbGdQAy-4`, `vCskOx6N-XM`, `xzIaUEDklrE`  
*gaps admitted:* The KB never states why a 'rail rod' is called that — no note connects the class name in tackle/gear-classes.md to the rail-fighting mechanics in techniques/fighting-big-bluefin.md. | '2x4' is used as rail-rod shorthand twice in tackle/rod-and-reel-selection.md and is never defined anywhere in the KB. | No rail-rod construction detail (bent vs straight butt, roller guides, foregrip length, blank taper) exists outside Cameron's 'cross-cut 4-slot aluminum gimbal butt' line in profiles/cameron/rods.md. | No note covers casting mechanics for a rail rod; all cast doctrine in the KB (pendulum swing, 2-to-9-o'clock sweep, release point, reel-on-its-side) is jig-stick/surface-iron specific. | The jig-stick braid class is given four different ways across four notes (~25–60 lb class, 40–65 lb braid, 'up to 65 on a jig stick', ~80 lb braid main) and no note reconciles them or says which governs. | No 2-speed gear ratios are given for any rail-rod-class reel; the only ratios recorded (4.2:1 / 1.6:1) belong to the heavier trolling/spreader-bar class Fathom 80. | The rail-rod class is mapped only to jumbo bluefin — the KB gives no guidance on whether or when it applies to any other species. | There is no general rail-fighting technique note; the beltless, boat-leverage 'railroading' style is documented only inside the bluefin-specific fighting note.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# Jig stick vs. rail rod

Two different jobs. **A jig stick is a casting rod — its job is reach.** **A rail rod is a fighting rod — its job is leverage against a fish that is already on.** In this KB they are two named entries in the gear-class lexicon at [`tackle/gear-classes.md`](tackle/gear-classes.md), and almost everything else about them falls out of that difference.

---

## The jig stick (surface-iron / jig-stick class)

**Class spec** — 8–10 ft, casts 2–4 oz irons, moderate/fast action, ~25–60 lb ([`tackle/gear-classes.md`](tackle/gear-classes.md)). The application table in [`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md) gives it as: *surface iron → 8–10 ft jig stick, moderate → narrow high-speed conventional → 40–65 lb braid.*

**What it's for.** Long-casting a heavy chrome/painted iron and swimming it back near the surface — [`techniques/surface-iron.md`](techniques/surface-iron.md). Reach for it on yellowtail boiling or on a kelp paddy, surface-feeding calico and sand bass, barracuda and bonito on top, and bluefin foamers when you want a bigger/faster presentation than a plug.

**Why it's long.** "The distance IS the technique" — the 9–10 ft blank is what buys the cast, and **the rod does all the work**; the commonest mistake is shoving the lure out with your arms instead of loading the blank ([`techniques/surface-iron-casting.md`](techniques/surface-iron-casting.md)). Mechanically: hang the jig about a leader length below the tip (~18 in), take the rod back to **2 o'clock**, let the blank load, and sweep through to **9 o'clock**. Build the swing **up and down, not side to side** — a longer rod gives a longer pendulum arc between tip and jig, hence more distance (Scotty, Brothers Sportfishing via Roman Castro, `VpW91AKOFVQ`).

The length is a stated trade-off, not free: a 9–10 ft stick is *"not the most fun to fight a fish on,"* but casting reach is deliberately ranked above fight comfort — *"the main thing is you've got to get hooked up"* (`BLbUu_mfMJY`).

**How long, exactly — the strongest opinion in the corpus.** Dan Wade (registered voice): *"An **8-ft jig stick is a yo-yo rod** — it's not a jig stick. **9-ft is okay. 10-ft is better**"* (`yn1suHH6b1Y`). Working alternates are logged side by side and not reconciled: a 10 ft Phoenix Axis 1009 HJ rated 30–60 lb, and a shorter/stouter 9 ft Axis 909 HJ rated 30–80 lb for fired-up schoolies and structure fish (Ray Sharifi, `LTCFjqtSI8g`); an 8 ft extra-heavy 30–80 lb stick one angler favored at Cedros specifically for casting distance (`u0scEBby7nA`).

**Blank material matters to the job.** Comparing two jig sticks side by side, an **all-fiberglass** rod loads up more easily and "can really swing into pretty far" — the go-to build for surface iron; a **composite** (graphite-blended) rod carries a **stiffer action**, better for working a popper or stick bait, since a stiffer blank gives more response out of your sweep (Billy, Fisherman's Landing Tackle Shop, `sjlL5GidM58`, 2018-11-29). Dan Wade's material note: **S-glass does what E-glass does at ~20% less weight** — which matters when you're making 300 casts over a 12–14 hour day (`yn1suHH6b1Y`).

**Reel and line.**
- **Narrow high-speed conventional**, thumb-controlled; ~42 in per crank on a Tranx-500-class HG covers slow grind up to yellowtail speed just by changing cadence ([`techniques/surface-iron.md`](techniques/surface-iron.md)).
- But there's a real conflict here, kept side by side: Dan Wade argues high ratios are wrong — the irons were designed when the **Penn Jigmaster (4:1)** was the go-to, and *"six and a half, seven and a half to one — they're too fast"* (`Ec2GaNpiOHI`); a Tackle Express counter clip frames a **7:1** baitcaster favorably as a torque/versatility middle ground (`pOFsjDTqaxY`). Spool diameter is the other half — a taller spool picks up more line per turn, so a nominally slower ratio can still be right.
- Line: ~80 lb braid main with a **50 lb, ~18 in** leader to a **100 lb clip** tied straight to the iron; or the mono school — 30–60 lb, **most often 40 lb**, because 40 lets you run a **snugger drag** which helps the hookset (`49joKHD7Umc`). A budget build in that same source: 9 ft casting rod + single-speed **star drag**, straight 40 lb mono, no spectra backing.

**A jig-stick quirk worth knowing:** many are built with **no fixed reel seat**. Set the reel by measuring from the **crook of your elbow to the tip of your middle finger**, within about an inch — too high and you can't get your off hand in front of the reel to pull on a fish, too low and the cast loses the leverage that makes it work (`49joKHD7Umc`). The deckhand-style version is clamped, not seated (`_C7TJoGT0nw`).

**It doubles as a trolling outfit.** An 8-ft jig stick with a 20-size reel and 65 lb braid (close to 400 yd, so you don't get spooled) runs as both jig stick and troller. Clicker sequence: **clicker on, drag backed off a couple of clicks** to troll; on the bite, **advance the drag two to three clicks and turn the clicker off** ([`tackle/tackle-express-jig-stick-trolling-outfit.md`](tackle/tackle-express-jig-stick-trolling-outfit.md), `BNp-gSOpWBw`). It's also worth packing offshore: one Searcher tip is specifically that anglers leave their jig sticks at home for Guadalupe when they should be casting irons at tuna there (`rziFyx7SRGI`, cited in [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md)).

---

## The rail rod (rail-rod / heavy tuna class)

**Class spec** — ~8 ft, 3X-H, 60–130 lb, **two-speed reel**, for casting/fighting jumbo bluefin ([`tackle/gear-classes.md`](tackle/gear-classes.md)). The application table gives *big bluefin cast/fight → rail rod 2x4 / 50–100 lb → HD30 / Fathom 60 / two-speed → 130 lb braid* ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)).

**What physically makes it a rail rod.** Not the blank — the **grip**. A rail rod carries a **long foregrip wrapped in hypalon**, long enough that the rod can be laid on and braced against the boat's rail instead of being held up entirely by your arms and body (`Y2XZ34-Tpa0`, 2019-06-06). One model is cited as carrying **6–8 in of extra foregrip** for exactly that purpose (`aAqKHeyBwEo`), and heavier tiers add reinforcement because you'll be rubbing that grip on the rail more (`sjOJiR6_HJ4`).

**The rule that goes with it:** put **the rubber on the rail, never the blank** — laying the blank on the rail breaks the rod (Steve Carson, `sjOJiR6_HJ4`).

**How it's fished** ([`techniques/fighting-fish-from-the-rail.md`](techniques/fighting-fish-from-the-rail.md)): tuck the butt under the **left** armpit (for a right-handed angler — there's a natural pull to tuck right, coached against), lay the rod on the rail if the fish is down below, put a hand on top of or beside the reel to counter the twisting load, keep the reel in **low gear**, and **crank down, then pump up with body weight** — not the arms (`6wVlDDno2TE`, `sjOJiR6_HJ4`). The failure mode it corrects is **high-sticking** — holding the rod up unsupported (`0xJqOtkmHqY`, "the rail is your friend"). Rail height varies around the deck, so pick where you'll stand before the fight, not during it. On triple-digit bluefin the framing is blunt: no angler is stronger than the fish; the rod-and-rail combination is what brings it in, as long as you keep the bend and keep cranking (`DuNkl8F45NE`).

**The four-tier ladder by line rating** (Steve Carson, `sjOJiR6_HJ4`, 2023-12-07 — full detail in [`tackle/searcher-rail-rod-ladder.md`](tackle/searcher-rail-rod-ladder.md)):

| Tier | Rod | Line | Reel | Grade / use |
| --- | --- | --- | --- | --- |
| 1 | **7 ft 8 in, 40–100 lb** — "the lightest you'll usually see," a little more tip action | fish **60 lb** (50 or 80 fine) | — | live sardine/mackerel; flyline, dropshot, sinker rig |
| 2 | **"Carnage 3," 7 ft, 60–100 lb** — extra foregrip reinforcement | **80 lb** | — | large live baits or medium jigs; tuna to **~225 lb** |
| 3 | **"8130," 7 ft, 80–130 lb** — "the most popular one if you're coming out on the Searcher" | **100 lb** | Penn International 16BX/16VISX | tuna to **~300 lb** |
| 4 | **80–150 model** (length not restated) | **100 or 130 lb** top shots | Penn International 20, "or even a 30" | **350–400 lb** tuna |

Two rules ride along with that ladder:
- **Fish the middle of the printed line rating** — throw out the high and low ends; that's where the rod performs best. This is high-confidence repeated doctrine on this channel (60 lb on a 40–100 rod, 80 on a 60–100, 100 on an 80–130).
- **7 ft is the floor.** The 1980s/90s-era **5 ft 2 in–6 ft stand-up trolling rods** are called out by name as the thing not to bring — "put them away, sell them on eBay." A bigger/stronger angler can size **up** to 7 ft 3 in or 7 ft 6 in instead ([`tackle/rod-length-for-angler-size.md`](tackle/rod-length-for-angler-size.md)).

A heavier model in the same family, the **OSP 2x4**, is given as **80–130 lb on a 7 ft 3 in composite blank**, fished for sinker rigs, the night knife jig, and flylining big fish on 10-, 16-, and 18-day trips (`scScYJJF95Y`). One historical note worth having: rail fishing fell out of fashion for a stretch because, around 2001, **IGFA world-record rules** disqualified a catch if the angler touched the rail — by 2021 "everybody's using the rail again" (`fgTmUq78ofQ`).

---

## Side by side

| | **Jig stick** | **Rail rod** |
| --- | --- | --- |
| **Purpose** | Deliver a 2–4 oz iron a long way and make it swim | Lift and grind a big fish you're already hooked to |
| **Length** | 9–10 ft is the doctrine (8 ft "is a yo-yo rod") | **7 ft is the floor**, ~7 ft–7 ft 8 in in the ladder; class row says ~8 ft |
| **Action** | Moderate/fast, glass or composite, loads to cast | 3X-H, stiff, built to lift |
| **Line class** | ~25–60 lb; 40–65 lb braid, or straight 40 lb mono | 40–100 lb up through 80–150 lb; 130 lb braid |
| **Reel** | Narrow high-speed **single-speed** conventional or star drag | **Two-speed** lever drag (Fathom 60 / Penn International 16–30 class), fished in **low gear** |
| **Defining hardware** | Often **no fixed reel seat** — reel positioned by hand for casting leverage | **Long hypalon foregrip** for bracing on the rail |
| **Where the load goes** | Your cast, and the iron's swim | Your armpit, the rail, and your body weight |
| **Grade** | Calico, barracuda, bonito, yellowtail (7–25 lb schoolies up to trophy) | Bluefin ~225 lb → 350–400 lb by tier |
| **Doubles as** | A trolling outfit (clicker sequence above); a yo-yo rod at the short end | Flyline, dropshot, sinker rig, flat-fall and night knife jig at the lighter tiers |

**The one-line version:** if you need to get a lure to a fish that won't come to the boat, that's the jig stick. If you're hooked to something that outweighs you and you need the boat's rail to do the lifting, that's the rail rod. They are not substitutes in either direction — a jig stick has no foregrip to brace, and a rail rod won't load and throw an iron.

---

## What the KB does not cover here

- There is **no standalone note for either rod** — the definitions are distributed across [`tackle/gear-classes.md`](tackle/gear-classes.md), [`techniques/surface-iron.md`](techniques/surface-iron.md), [`techniques/surface-iron-casting.md`](techniques/surface-iron-casting.md), [`tackle/searcher-rail-rod-ladder.md`](tackle/searcher-rail-rod-ladder.md), and [`techniques/fighting-fish-from-the-rail.md`](techniques/fighting-fish-from-the-rail.md).
- **The rail-rod length figures don't agree and the KB doesn't reconcile them:** the class row says ~8 ft, while the sourced ladder puts the floor at 7 ft and the tiers at 7 ft–7 ft 8 in. Treat the ladder's numbers as the sourced ones.
- All rail-rod content is **sportboat-framed** (Searcher / Fisherman's Landing). Nothing in the KB covers running a rail rod on a private or small boat without a proper rail. The nearest thing is a **Sea of Cortez** contrast — on a panga, an 8 ft 20–50 lb rod is preferred over the "purist" 9 ft jig-stick standard, because a 9–10 ft rod makes it hard to work a fish close enough for the short 4–5 ft gaffs carried aboard (Cesar via Dirty Hookers, `M8hOYQ_6rSg`, 2025-05-20) — different region, and about jig sticks/yo-yo rods, not rail rods.
- The gear class says a rail rod is for "casting/fighting" jumbo bluefin, but **no casting mechanics for a rail rod are anywhere in the KB** — every casting note is jig-stick/surface-iron.
- **No gram/jig-weight rating rule for jig sticks.** The "buy toward the top of the gram rating" rule in [`tackle/jig-rod-rating-selection.md`](tackle/jig-rod-rating-selection.md) explicitly scopes itself to slow-pitch and speed-jig rods and says surface-iron rods don't use a gram rating.
- No pricing, brand-shopping guidance, or "which to buy first" comparison between the two classes.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `tackle/gear-classes.md`, `tackle/rod-and-reel-selection.md`, `tackle/searcher-rail-rod-ladder.md`, `tackle/rod-length-for-angler-size.md`, `tackle/jig-rod-rating-selection.md`, `tackle/tackle-express-jig-stick-trolling-outfit.md`, `tackle/tackle-express-trophy-bluefin-jig-outfit.md`, `tackle/searcher-big-tuna-rig-ladder.md`, `tackle/rod-blank-and-component-materials.md`, `techniques/surface-iron.md`, `techniques/surface-iron-casting.md`, `techniques/fighting-fish-from-the-rail.md`, `techniques/yo-yo-iron.md`, `species/yellowfin-tuna.md`  
*videos:* `sjOJiR6_HJ4`, `Y2XZ34-Tpa0`, `aAqKHeyBwEo`, `scScYJJF95Y`, `6wVlDDno2TE`, `0xJqOtkmHqY`, `fgTmUq78ofQ`, `an_uw-5pjfw`, `MPC_OQjvO-o`, `DuNkl8F45NE`, `sjlL5GidM58`, `yn1suHH6b1Y`, `Ec2GaNpiOHI`, `VpW91AKOFVQ`, `BLbUu_mfMJY`, `49joKHD7Umc`, `BNp-gSOpWBw`, `_C7TJoGT0nw`, `LTCFjqtSI8g`, `u0scEBby7nA`, `pOFsjDTqaxY`, `rziFyx7SRGI`, `M8hOYQ_6rSg`  
*gaps admitted:* No standalone note defines either rod — 'jig stick' and 'rail rod' are only defined across gear-classes.md, surface-iron.md, surface-iron-casting.md, searcher-rail-rod-ladder.md and fighting-fish-from-the-rail.md. | The rail-rod length figures conflict and are not reconciled: the gear-class row says ~8 ft while the sourced four-tier ladder gives a 7 ft floor and 7 ft–7 ft 8 in tiers. | All rail-rod content is sportboat-framed (Searcher / Fisherman's Landing); nothing covers using a rail rod on a private or small boat without a proper rail. | The gear class lists a rail rod for 'casting/fighting' jumbo bluefin, but no casting mechanics for a rail rod exist anywhere in the KB — all casting notes are jig-stick/surface-iron. | No jig-weight (gram) rating rule for jig sticks — jig-rod-rating-selection.md explicitly scopes its rule to slow-pitch and speed-jig rods and states surface-iron rods don't carry a gram rating. | No pricing, brand-shopping guidance, or 'which to buy first' comparison between the jig-stick and rail-rod classes. | No stated blank-material doctrine for rail rods beyond scattered 'composite'/'graphite' model callouts — nothing equivalent to the glass-vs-composite reasoning documented for jig sticks.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

I read the repo's own conventions, then followed the day-plan protocol's gear path: `tackle/gear-classes.md` (the class lexicon) out to the class-specific notes.

Both of these are **class terms** in this KB's lexicon — the way notes name gear so a profile lookup can resolve them ([`tackle/gear-classes.md`](tackle/gear-classes.md)). Here's what each one is.

## Short answer

- **Jig stick** = a long casting rod. Its job is **distance** — throwing a 2–4 oz iron a long way and swimming it back. You hold it and cast it all day.
- **Rail rod** = a short, very heavy fighting rod with an extra-long padded foregrip so the rod can be **laid on the boat's rail**. Its job is **leverage on a big fish**. You barely cast it; you brace it.

They sit at opposite ends of the lexicon and are not substitutes.

## Jig stick (a.k.a. surface-iron / jig-stick class)

**The class as written:** 8–10 ft, casts 2–4 oz irons, moderate/fast action, ~25–60 lb ([`tackle/gear-classes.md`](tackle/gear-classes.md)). The technique note is tighter: *"An 8-ft jig stick is a yo-yo rod — it's not a jig stick. 9-ft is okay. 10-ft is better"* (`yn1suHH6b1Y`, [`techniques/surface-iron.md`](techniques/surface-iron.md)). Length is what buys the cast — it loads the pendulum swing; a shorter rod can't generate the arc ([`techniques/surface-iron-casting.md`](techniques/surface-iron-casting.md)).

**Build details the KB gives:**
- **Material.** S-glass does what E-glass does at ~20% less weight — *"when you're on a boat 12–14 hours making 300 casts, your back and shoulders don't hurt"* — and has more backbone, *"denim versus polyester"* (`yn1suHH6b1Y`). All-fiberglass (Cal Star 90J example) loads easily and is the go-to for iron; a composite (Terramar 90 example) is stiffer and the better popper/stick-bait tool — two jobs, not one best pick (`sjlL5GidM58`).
- **Often no fixed reel seat.** Deckhand-style sticks ship bare and take a reel clamp (`_C7TJoGT0nw`). Set reel position by measuring **crook of the elbow to tip of the middle finger**, within about an inch (`49joKHD7Umc`, flagged single-source in [`techniques/surface-iron-casting.md`](techniques/surface-iron-casting.md)).
- **Reel.** Narrow high-speed conventional in the application table ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)), but the surface-iron note holds a live conflict: irons were designed around the **4:1 Penn Jigmaster**, so 6.5–7.5:1 is *"too fast"* (`Ec2GaNpiOHI`), against a clip framing **7:1** as a torque/versatility middle ground (`pOFsjDTqaxY`). The KB's decision frame: what matters is **line speed at the jig**, set by crank discipline and spool diameter as much as ratio.
- **Line, two attributed schools, not reconciled.** Short system: ~80 lb braid, 50 lb / ~18 in leader, 100 lb clip tied straight to the iron. Long-top-shot system: 50–60 lb (up to 80 lb) braid backing to **80–100 yd of 40–50 lb mono** straight to the iron (`A70kK2niu2Q`). Classic mono build: 40 lb Izorline, 125–150 yd, on a Harnell 724 (`Ec2GaNpiOHI`). Top-shot sizing by destination: **40 lb** for full-day islands (Coronados, Channel Islands, Catalina), **50 lb** for overnight range (San Clemente, Santa Barbara Island) and anywhere in Baja, because a trophy is live at any moment there (`LTCFjqtSI8g`). Casting weight roughly **1.8 to 2+ oz**, Salas 7X among the heavier picks (`LTCFjqtSI8g`).
- **Fight character is a known compromise.** A 9–10 ft stick is *"not the most fun to fight a fish on"*; the stated priority is the cast — *"the main thing is you've got to get hooked up"* (`BLbUu_mfMJY`).

**What it's for:** [surface iron](techniques/surface-iron.md) first — yellowtail boiling or on a paddy, surface calico and sand bass, barracuda, bonito, bluefin foamers. A **heavy** jig stick is also the [yo-yo iron](techniques/yo-yo-iron.md) rod (that's the sense in which "an 8-ft jig stick is a yo-yo rod"). And an 8-ft jig stick with a 20-size reel and 65 lb braid (~400 yd) doubles as a **trolling outfit** — clicker on with drag backed off a couple clicks while trolling, then on the bite advance the drag two or three clicks and click the clicker off ([`tackle/tackle-express-jig-stick-trolling-outfit.md`](tackle/tackle-express-jig-stick-trolling-outfit.md), `BNp-gSOpWBw`).

## Rail rod (rail-rod / heavy-tuna class)

**The class as written:** ~8 ft, 3X-H, 60–130 lb, two-speed reel; application is casting/fighting jumbo bluefin ([`tackle/gear-classes.md`](tackle/gear-classes.md)).

**The defining feature is the foregrip, not the power rating.** A rail rod carries a **long hypalon-wrapped foregrip section** — long enough that the rod lays on and braces against the boat's rail instead of being held entirely by the angler's arms and body — and on some models double reinforcement. *"The rail is your friend."* It is paired with a **two-speed** reel, not a single-speed (`Y2XZ34-Tpa0`, `sjOJiR6_HJ4`). Put the **foregrip** on the rail, never the blank — blank-on-rail breaks the rod (`sjOJiR6_HJ4`).

**Length runs the other way from a jig stick: 7 ft is the floor.** Don't go shorter than 7 ft; that rules out the 1980s/90s 5'2"–6' stand-up trolling rods — *"these are great in their day, put them away, sell them on eBay"*. A bigger or stronger angler sizes **up** to 7'3" or 7'6" (`sjOJiR6_HJ4`, [`tackle/searcher-rail-rod-ladder.md`](tackle/searcher-rail-rod-ladder.md)).

**The four-tier ladder by line rating** (`sjOJiR6_HJ4`), with the governing rule — **throw out the high and low ends of the printed rating and fish the middle**:

| Tier | Rod | Fish this line | Use / grade ceiling |
| --- | --- | --- | --- |
| 1 | 7'8", 40–100 lb | 60 lb (50 or 80 also work) | Live sardine/mackerel — flyline, dropshot, sinker rig; more tip action than the tiers below |
| 2 | Penn Carnage 3, 7'0", 60–100 lb | 80 lb | Big live baits, medium jigs; tuna to ~225 lb; extra foregrip reinforcement because you rub it on the rail |
| 3 | "8130", 7'0", 80–130 lb | 100 lb | Penn International 16-class; tuna to ~300 lb. *"Make sure if you don't have anything else, have this one"* |
| 4 | 80–150 lb model | 100 or 130 lb top shots | Penn International 20 *"or even a 30"*; framed at 350–400 lb tuna |

**Named models** (product claims — the KB stamps a sponsored-claim caveat on all of these): Seeker **OSP 1x3** 7 ft composite, 60–100 lb (also cited 80–100), *"the Guadalupe special"*, the Searcher's standard heavy outfit across 1.5- to 8-day trips (`aAqKHeyBwEo`, `Y2XZ34-Tpa0`, `MPC_OQjvO-o`); Seeker **OSP 2x4** 7'3" composite, 80–130 lb (`scScYJJF95Y`); Seeker **SSR 7650** 7'6", 50 lb, a wahoo-bomb rod that doubles as a rail rod with 6–8 in of extra foregrip (`aAqKHeyBwEo`).

**A complete worked outfit** ([`tackle/searcher-spring-bluefin-yellowtail-quiver.md`](tackle/searcher-spring-bluefin-yellowtail-quiver.md), `lf3S28nh-kk`): OSP 1x3 rated 60–100 lb + **Penn Fathom 60 two-speed** (the two-speed is the one non-negotiable spec) + **100 lb spectra**, then either 100 ft of 80–100 lb mono top shot for stretch against headshakes, or the jig tied straight to spectra (works, but you feel every tailbeat). Lure example: 300 g glow flat-fall. A minimum three-outfit quiver runs the same rod with **130 lb braid** and swappable top shots — 60 lb for live bait, 80 lb for flat-fall and dropper loop (`kzpeM56Gh7o`). On a rail rod in a 15-kt breeze with the boat rolling, one stated preference is **100–150 ft of mono** ahead of the fluoro purely for stretch — *"easier on the body"* over a long fight, at the cost of one more connection ([`tackle/line-and-leader.md`](tackle/line-and-leader.md), `YntRJAN88fs`).

**How you actually fish it** ([`techniques/fighting-fish-from-the-rail.md`](techniques/fighting-fish-from-the-rail.md)): once past the initial run, brace on the rail and crank — when the tip loads up, **stop cranking** and let the rod and rail lift (`0xJqOtkmHqY`). Big-tuna variant: tuck the butt under the **left** armpit (right-handed angler), lay the rod on the rail if the fish is down, put a hand on top of or on the side of the reel to counter the twist, stay in **low gear**, and lift with body weight rather than arms (`6wVlDDno2TE`, `sjOJiR6_HJ4`). Rail height varies around the deck — work out where you'll stand before the fight. The failure this corrects is **high-sticking** — holding the rod up unsupported, which *"will hurt yourself really bad"* on bigger bluefin (`bEFhWtGBdBU`).

**What it's for:** [flat-fall jigging](techniques/flat-fall-jigging.md) (large bluefin marked deep, captain-called 100–360 ft) and night knife jigs; heavy sinker rigs and dropper loop; flylining big fish; wahoo trolling and kite on the OSP-class rods; and fighting 100–300 lb+ tuna. *"The rest of us normal humans have to use the rail"* (`sjOJiR6_HJ4`).

## Side by side

| | Jig stick | Rail rod |
| --- | --- | --- |
| Length | 9–10 ft (lexicon says 8–10) | 7–8 ft; **7 ft is the floor** |
| Power / line | Moderate/fast, ~25–60 lb | 3X-H; 40–100 through 80–150 lb |
| Defining feature | Length + a tip that loads for the cast | **Long hypalon foregrip** that lays on the rail |
| Reel | Narrow conventional/star drag; ratio contested | **Two-speed** lever drag (non-negotiable) |
| Main line | 40–80 lb braid, or straight 40 lb mono | 100–130 lb braid + heavy top shot |
| Job | Get the lure far away from the boat | Get a big fish off the bottom |
| Where the load goes | Your arms and body, hundreds of casts | The boat's rail |
| Grade | Schoolie yellowtail 7–25 lb up to trophy | 100–400 lb tuna |
| Fight comfort | Poor, and knowingly traded for casting reach | The entire point |

**The decision frame:** it's about which half of the fight you're solving. The jig stick solves **getting bit at distance** — boiling yellowtail, a paddy, a foamer, fish that spook off the boat. The rail rod solves **staying connected to something that outweighs you** — a jig fished straight down deep, or a fish that's already down and won't come up on tackle you have to hold. Neither does the other job: a rail rod won't throw an iron 80 yards, and a jig stick has nothing to brace on the rail.

**One nuance the KB leaves slightly open on casting at jumbos:** the lexicon lists "casting/fighting jumbo bluefin" as the rail-rod class's application ([`tackle/gear-classes.md`](tackle/gear-classes.md)), while the actual technique note for that scenario, [`techniques/foamer-casting.md`](techniques/foamer-casting.md), calls for a **jig-stick class outfit beefed up** from the yellowtail version, because these can be bluefin over 200 lb. Both are in the KB; nothing reconciles them.

## In your box (profile resolution)

From [`profiles/cameron/rods.md`](profiles/cameron/rods.md) (source: `cameron`):

- **Jig stick →** Setup 5, the **Torium**: Phenix Abyss PSX1009J, 10'0", 25–60 lb, moderate/fast, deckhand cord-wrapped handle with a clamp-on reel (exactly the no-fixed-seat build above) + Torium 20HG, 50 lb braid. Listed role: full surface iron.
- **Rail rod →** Setup 6, the **Talica 25**: Phenix Axis HAX-C 800X3H, 8'0", 3X-H, 60–130 lb, tagged rail-rod class, cross-cut aluminum gimbal + Talica 25II two-speed, 100 lb braid. Role: main heavy setup, commonly trolling, and the rod you'd cast at an 80–140 lb bluefin foamer school.
- The in-between rod is Setup 1, the **Trinidad 40** (8'0" XH 40–80, 80 lb braid) — the yo-yo/heavy-iron class, noted as able to cast large surface irons "but not well."

## Confidence caveats worth knowing

- **The jig-stick length band disagrees inside the KB.** [`techniques/surface-iron.md`](techniques/surface-iron.md) says 9–10 ft and "8 ft isn't a jig stick"; the lexicon says 8–10 ft; [`species/white-seabass.md`](species/white-seabass.md) routes to the same class calling it 7–9 ft, 40–50 lb. The surface-iron note carries this as an open `⚠ Fact-check (contradicted-internal)` flag. There's also a Baja panga argument for 8 ft over the 9 ft "purist" standard — a short platform and 4–5 ft gaffs make a 9–10 ft rod hard to work a fish to gaff on ([`tackle/rod-and-reel-selection.md`](tackle/rod-and-reel-selection.md)).
- **Rail-rod detail is nearly all one channel** (SearcherSportfishing / Penn / Seeker reps, San Diego multi-day boats), and the model callouts carry a sponsored-claim caveat; the KB rates the underlying mechanism normally but the named-product specs low ([`tackle/evidence/gear-classes.md`](tackle/evidence/gear-classes.md)). The rail-rod ladder note itself is `confidence: medium`.
- **The jig-stick-as-trolling-rod note is `confidence: medium`** and flags its own gap: the source gives no mechanism beyond "it was easy."

## What the KB does not cover

Three things I couldn't answer from these notes: there's no note that compares these two classes head to head (I assembled this from the lexicon plus each class's own notes), no casting mechanics for a rail rod the way `surface-iron-casting.md` exists for the jig stick, and Tier 4's rod length is simply not stated in the source.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `tackle/gear-classes.md`, `tackle/evidence/gear-classes.md`, `tackle/searcher-rail-rod-ladder.md`, `tackle/searcher-three-outfit-minimum-quiver.md`, `tackle/searcher-spring-bluefin-yellowtail-quiver.md`, `tackle/tackle-express-jig-stick-trolling-outfit.md`, `tackle/rod-and-reel-selection.md`, `tackle/rod-blank-and-component-materials.md`, `tackle/line-and-leader.md`, `techniques/surface-iron.md`, `techniques/surface-iron-casting.md`, `techniques/yo-yo-iron.md`, `techniques/fighting-fish-from-the-rail.md`, `techniques/flat-fall-jigging.md`, `techniques/foamer-casting.md`, `profiles/cameron/rods.md`  
*videos:* `yn1suHH6b1Y`, `Ec2GaNpiOHI`, `sjlL5GidM58`, `49joKHD7Umc`, `BLbUu_mfMJY`, `A70kK2niu2Q`, `LTCFjqtSI8g`, `pOFsjDTqaxY`, `BNp-gSOpWBw`, `_C7TJoGT0nw`, `Y2XZ34-Tpa0`, `sjOJiR6_HJ4`, `aAqKHeyBwEo`, `an_uw-5pjfw`, `scScYJJF95Y`, `MPC_OQjvO-o`, `kzpeM56Gh7o`, `lf3S28nh-kk`, `6wVlDDno2TE`, `0xJqOtkmHqY`, `bEFhWtGBdBU`, `YntRJAN88fs`, `cameron`  
*gaps admitted:* No note in the KB compares the jig-stick class and the rail-rod class head to head; the comparison given is assembled from tackle/gear-classes.md plus each class's own notes. | There is no casting-mechanics content for the rail-rod class equivalent to techniques/surface-iron-casting.md for the jig stick, even though tackle/gear-classes.md lists 'casting jumbo bluefin' as a rail-rod application. | Tier 4 of the Searcher rail-rod ladder (the 80-150 lb model) has no stated rod length - the source does not confirm whether it matches the 7 ft of the lighter tiers. | The jig-stick length band is internally contradicted in the KB (surface-iron 9-10 ft vs. lexicon 8-10 ft vs. white-seabass router 7-9 ft / 40-50 lb) and is carried as an open fact-check flag, not resolved. | No corpus source explains the mechanism for why a jig stick works as a trolling outfit - the note flags this gap explicitly ('it was easy' is all the source gives). | The lexicon's rail-rod application ('casting jumbo bluefin') and techniques/foamer-casting.md's jig-stick-class call for the same scenario are not reconciled anywhere in the KB. | The jig-stick trolling-conversion note gives no drag numbers, no line classes beyond 65 lb braid, and does not name the lure or species it was run for.

</details>
