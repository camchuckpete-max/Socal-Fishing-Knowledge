---
type: planning
tags: [electronics, sounder, sonar, radar, dsl, garmin, furuno]
sources: [yLpDI8jnizU, 11npFUPOJKU, yMiBtZ7k8-w, SgF5hRlEGqU, FEXgl0eQCa8, 6DzbsElGE7E, 9hEa3sGTh40, Rf1HKJG-SDg, HGyL7pXy3Ts, cameron, d0yGBQDeY_4, SczdZIq3UmE, uyjTdgIw-1k, nkJNzdNlm_c, -bw1KDfDjv4, 97clKtVsEOs, MUpvP-Yl2R0, i4OB4G6_adI, 8XrMkWPRxgs, bM2vUS1B-yQ, m-M0iwX8DjA, fgTmUq78ofQ, lf3S28nh-kk, ZIJAvAEW_tU, KjVLn4cWHbc, QP6c8vcslVs, iAr6sbRC384]
confidence: high
layout: v2
---

# Electronics and Sounder

How to use the sounder and radar to find fish and decide whether to stop.
This note owns the *general* method and settings; the **species-specific
sonar signatures** (yellowtail arcs, bluefin sounded deep, sword in the DSL)
live in the species notes, and the deep scattering layer itself is in
[deep scattering layer](../conditions/deep-scattering-layer.md).

**The doctrine below is unit-agnostic; the worked example is one boat's
unit.** Furuno-based settings (`yLpDI8jnizU`, `11npFUPOJKU`, `yMiBtZ7k8-w`)
are translated onto a **Garmin GPSMAP 840xs** —
[Cameron's sounder](../profiles/cameron/boat.md) (cameron) — a worked example
rather than the reader's hardware. On a different unit, read the translated
setting as "the control that does this job on mine" and find its equivalent
on yours; the depths, frequencies, and what you are looking for do not
change with the brand.

## Terminology: fathoms and the fathometer

Ocean depth is measured in **fathoms** (1 fathom = 6 ft), which is why the
sounder is historically called a **fathometer** rather than a "fish finder"
— early units were built to bounce a signal off the bottom and report depth.
Flasher-era units incidentally showed fish on that same bottom-return
signal, and operators learned to grade marks by how they flashed on screen;
the name never changed because finding depth remained the machine's core job
(`Rf1HKJG-SDg`, `9hEa3sGTh40`).

A fathometer reading converts to feet directly (fathoms × 6): 9 fathoms is
54 ft (`HGyL7pXy3Ts`).

Fish don't mark uniformly across a passing sounder track — they concentrate
on the **high spots** (banks, rocks, seamounts) described in
[zone lexicon](../locations/zone-lexicon.md), not open flat bottom.

## Reading the bottom and grading marks

- **Bottom-discrimination shows where hard bottom meets soft bottom** —
  those seams are travel and feeding highways. Run structure looking for the
  hard/soft transition, not just the high spot (`yLpDI8jnizU`,
  `11npFUPOJKU`).
- **Photograph the meter during bites** to build a personal library of what
  a productive mark looks like (`yLpDI8jnizU`, `11npFUPOJKU`).
- **Bottom hardness reads by return-line thickness, on any brand** — no
  special discrimination mode needed: a thin, faint bottom return is soft
  bottom (sand/mud); as it thickens and darkens, that's harder, rockier
  bottom. "I don't care if you have a Hummingbird fish finder, they're all
  going to show that" (`6DzbsElGE7E`).
- **Backing the boat down blanks the bottom return — that's aerated water,
  not a machine fault.** Holding position while an anchor pays out puts air
  under the hull, and the sounder can lose the bottom entirely while that's
  happening (`HGyL7pXy3Ts`).
- **Stop only on marks you can grade — it's a bait budget.** Every stop on a
  no-name mark burns bait and time; idle on, grade the mark against what
  pays off, and only commit when it grades out. (The bait-shape rule — a
  solid unbroken wall of bait usually has no predators, broken/harried bait
  does — supports the grade; see
  [bass structure](../locations/bass-structure.md).)
- **Don't stop at the first bottom mark — keep running and stack the
  picture depth by depth.** A worked example: a mark near the boat starting
  around 20 ft, more marks found working out to 40 ft, and more again
  working out to 60 ft — move the boat slowly while doing this rather than
  committing to the first mark (`KjVLn4cWHbc`, `QP6c8vcslVs`). This is the
  search phase that precedes the bait-budget grading call above.
- **Present to where the mark actually is, not away from it.** A meter
  marking well directly under the boat at a known depth (e.g. 30 ft) calls
  for the bait dropped or under-hand flicked straight down/near the boat to
  that depth — not cast at distance (`bM2vUS1B-yQ`).
- **Set range manually for shallow schools in deep open water.** Working
  tuna schooling under dolphin pods well offshore, set a manual range window
  (e.g. 0–150 ft) rather than auto — on auto the sounder keeps hunting for a
  bottom that's far deeper and the shallow marks never paint (`SgF5hRlEGqU`).
  See [yellowfin tuna](../species/yellowfin-tuna.md) for the dolphin-pod
  sign this pairs with. The core run-manual-not-auto rule repeats across
  three sources (`9hEa3sGTh40`, `SgF5hRlEGqU`, `FEXgl0eQCa8`).
- **A private boat's default working range is 0–120 ft on older machines,
  0–150 ft on newer ones, regardless of the actual bottom depth** (e.g. 209
  or 181 fathoms at the offshore banks; see
  [zone lexicon](../locations/zone-lexicon.md)). The reasoning: a private
  boat lacks a sportboat's bait budget to hold and chum fish up from depth,
  so there's no benefit reading deeper than the top of the water column
  (`9hEa3sGTh40`, `8XrMkWPRxgs`). At that manual range a tuna school paints
  as a large, distinct upside-down-U-shaped mark; left on auto with the
  bottom set to the real (much deeper) depth, the same school shrinks to a
  barely visible speck. Most anglers never leave auto in the first place —
  fear of the machine's buttons, plus units commonly arriving pre-set to
  auto from the dealer/installer (`8XrMkWPRxgs`).
- **A 0–300 ft manual window is why the offshore bluefin read works.**
  Fished on auto over a typical bluefin bottom (2,000–3,000 ft), the screen
  reads zero at the top and the real bottom at the edge, and a sounded
  school compresses to nothing against that scale; capping the range at
  0–300 ft paints it instead. Fish below 300 ft are traveling, not biting;
  fish holding in the 300 ft-to-surface band are the ones eager to bite
  (`m-M0iwX8DjA`). Once a mark shows in that shallow band: hit the GPS
  unit's mark button, run past it, turn around, and troll back over the
  mark with a [Mad Mac](../lures/mad-mac.md) (`m-M0iwX8DjA`).
- **Size manual range so the bottom sits mid-screen, not at the edge** —
  that leaves room above the bottom return to read hard bottom vs. soft
  bottom and to pick fish marks and bait out of the water column. Worked
  examples: a 15 ft spot gets a 30 ft screen range; a 25 ft spot (most SoCal
  harbors run roughly 15–25 ft) gets 40 ft. Offshore, the same mid-screen
  principle scales up — e.g. a manual 0–300 ft range to look for tuna
  suspended around 150 ft down (`FEXgl0eQCa8`).
- **Learn hard/soft-bottom and fish-vs-kelp discrimination in the harbor,
  not on the fuel-burning offshore trip.** Drive the harbor (or a spot just
  outside it) with the range set mid-screen, dial the gain in until hard
  bottom clearly reads differently from soft bottom, and practice telling
  fish marks apart from kelp. Once that reading is solid inshore, leave the
  settings alone, go offshore, open the manual range up (e.g. 0–300 ft), and
  apply the same skill to find suspended fish like tuna (`FEXgl0eQCa8`).

## Searching range while running, and how sea state limits shallow reads

A sportboat wheelhouse sounder searching for bluefin schools while running
commonly stays open to about 80 fathoms (480 ft), watching the whole band
from the surface down rather than a narrower window — deeper than the
0–150/0–300 ft private-boat manual-range doctrine above, reflecting a bigger
bait budget than a private boat carries (`fgTmUq78ofQ`).

Sea state sets how shallow the sounder can actually read, distinct from the
range setting itself: in **flat conditions** the cone can be shot close to
the surface, reading the full water column from the top down. In
**choppy/rolly conditions** the cone tips lower, so a fish holding high in
the column doesn't show until the boat is nearly on top of it — the same
fish that would paint from a distance on a calm day is invisible at range
once the sea comes up (`fgTmUq78ofQ`).

The mechanism traces to the transducer: a **fixed transducer** follows the
boat's roll, so in chop the cone tips away from vertical and shallow,
close-to-surface fish go unmarked; a rolling boat in rough weather also
returns aerated-water noise that swamps the signal. A **gyro/roll-stabilized
transducer** stays aimed down regardless of how much the boat rolls or
pitches, reducing both effects (`ZIJAvAEW_tU`). Carried here as the
equipment-generation reasoning behind the sea-state limitation above, not a
claim that stabilization eliminates it — the sea-state limit is still
described as real on the more recent hardware above (`fgTmUq78ofQ`).

## Anchor vs. drift call off a live sounder read

Fish still marking on the sounder but not responding at anchor is a cue to
**drift over them instead of staying pinned to the hook** — position the
boat above the marks and let it drift through; the extra motion in the
presentation can restart a bite anchoring killed (`97clKtVsEOs`). This is a
sounder-driven pivot, not a fixed rule to always drift or always anchor —
read the mark and the response, not just the mark. See
[yellowtail](../species/yellowtail.md#where--when) for the session this came
from.

## SST and wind overlay for finding the break, and reading calmer water

A chartplotter's weather-overlay screen displays sea-surface temperature as
a color chart and true wind speed as color-coded, feathered barbs (flag
tips show direction-from and speed by feather count — roughly one feather
≈5 kt, two feathers ≈10–15 kt) directly on the chart (`uyjTdgIw-1k`). Read
the **temperature differential** across the run rather than stopping at the
first warm reading, and work the edge of the break — consistent with the
general break-not-absolute-number doctrine in
[water temperature](../conditions/water-temperature.md).

Worked examples: running from Mission Bay, SST broke from **69°F** near the
harbor to **71°F** at roughly **7 nm** out and **72°F** by roughly
**12–13 nm** out — a **3–4°F** differential worked toward open water
(`uyjTdgIw-1k`). The 14 Mile Bank / 209 / 267 bank complex (see
[zone lexicon](../locations/zone-lexicon.md)) read **66–67°F** on the bank
itself, climbing to **68°F** just off it — one pocket of comparatively warm
water worth working (`-bw1KDfDjv4`).

The same overlay carries a wind-speed layer: one Mission Bay run found
**~11 kt** near the boat easing to calmer conditions roughly **7 mi**
further out, useful for routing toward passenger comfort as well as toward
the fish (`uyjTdgIw-1k`).

## Manually tracking a temperature break without satellite SST

A fallback/supplement to the chartplotter SST overlays above, for running at
night or on a cloudy day when a usable satellite SST map isn't available
(`lf3S28nh-kk`):

- **Download an SST map before leaving the dock, and pull a fresh one during
  the trip when conditions allow.**
- **Tuna associate with temperature breaks** — the reason SST/temperature
  reading matters at all.
- **While running at night, watch the boat's water-temperature gauge
  directly and note when it changes**, rather than relying only on a
  downloaded map — a manual, visual backstop for a break that either isn't
  on the satellite map, or that a cloudy day left no map to download in the
  first place.

## Buoy overlay for wave height/period, plus AIS and structure-scan

A chartplotter's on-chart buoy overlay (refreshing roughly every two hours)
reads wave data directly off the plotter: one run read **wave height 3 ft
at 17 seconds** ("below average steepness") plus a separate **wind-wave
reading of 2 ft at 7 seconds** — a swell/wind-wave split without a separate
buoy-website lookup (`MUpvP-Yl2R0`). The same screen carries the SST
color-shading described above, used to help pick the day's zone, plus an
**AIS layer** (other AIS-equipped vessels) and a **structure-scan sonar**
channel run alongside the main sounder (`MUpvP-Yl2R0`).

## Closure boundaries as a chart layer

A depth-based closure line is a **charted boundary, not a depth reading** —
the same closure can run at different depths along one stretch of coast, so
the sounder cannot tell you which side of it the boat is on. Load the
boundary into a chart app — **Navionics, about $10–15** — and check position
against the drawn line rather than judging by depth; private boats have been
boarded and cited for getting that call wrong (`iAr6sbRC384`). The workflow
is boundary-agnostic: it applies to any closed area that can be carried as a
chart layer, not only to the depth closure it was described for.

Regulatory context (California / CDFW, as of 2020-03 — verify the current
boundary and depth limits before fishing): the Rockfish Conservation Area
depths behind this example are in
[rockfish and lingcod — regulations](../species/rockfish-lingcod.md#regulations).

## Bird radar

Radar isn't just for boats and weather — run it in **bird mode**: gain near
max, range 4–5 mi; bird schools paint as red blotches, sometimes boat-sized
(`yLpDI8jnizU`). That **4–5 mi detection envelope** extends glassing reach
well past the ~2 mi available from a hardtop (see
[search and glassing](search-and-glassing.md)) — radar finds the pile,
glassing confirms what the birds are doing.

A bird-mode radar zoomed to 1/2 mile tracked a working bird school in real
time as small moving dots; the unit's spec'd detection range is up to 5 mi,
consistent with the working envelope above (`MUpvP-Yl2R0`). A separate unit
could zoom in to about **200 ft**, versus roughly **1/8 mile** for older
"traditional magnetron" radar, and mark **dolphin schools before they were
spotted visually** — relevant to closing on the traveling dolphin/porpoise
pods that hold suspended [yellowfin tuna](../species/yellowfin-tuna.md)
(`SczdZIq3UmE`).

## Search sonar side-to-side scan range and audio bite cue

A horizontal search sonar (distinct from the down-looking bottom sounder) is
commonly run **400–600 ft side to side**; it can be opened out further, but
the return sweeps too slowly at longer range and marks get missed in the
meantime (`nkJNzdNlm_c`). Leaning on the unit's **audio** cuts down
screen-watching: the normal side-to-side sweep makes one sound, and that
sound **changes distinctly when it hits fish**, freeing the eyes for surface
sign (birds, paddies) instead (`nkJNzdNlm_c`).

## Radar for fog navigation (Baja)

In zero-visibility fog, which can run **5–6 months of the year** on Baja's
Cedros Island yellowtail grounds, radar alone navigates the run out to the
grounds and back; the sounder/sonar does the separate job of locating fish
once there (`d0yGBQDeY_4`).

## Speed of sound in water and the deep sound channel (mechanism, generic — not SoCal-measured)

Background mechanism for why sonar/fathometer gear works at all: sound
travels roughly **1,500 m/s in water** versus roughly **330 m/s in air** —
close to five times faster underwater. Sound speed in the ocean is not
constant; it is set by **temperature, pressure, and salinity**. Roughly
**500–1,000 m (1,640–3,281 ft)** down sits the **SOFAR channel** (sound
fixing and ranging), also called the **deep sound channel** — a band where
temperature and pressure are both relatively low, so sound speed is at a
minimum there. Sound entering this band gets trapped, bouncing between the
warmer/less-dense water above and the cooler/denser water below, and can
travel extremely long distances within the channel — the mechanism used to
track marine-life sounds and vessels (submarines, naval ships) over long
range (`i4OB4G6_adI`).

This ~500–1,000 m sound-channel band (`i4OB4G6_adI`) sits **deeper** than the
DSL's daytime working band (600+ ft/~183 m, preferred to ~950 ft/~290 m per
[deep scattering layer](../conditions/deep-scattering-layer.md)) — a
different depth feature, not the same layer; carried here as background
only, it does not change the DSL or sounder-settings doctrine in this note.

## Sounder settings for the DSL

To paint the **deep scattering layer** (600+ ft by day) for night bluefin
and daytime swordfish: push **TVG/gain up** (Furuno ~**55–57**; mid-to-high
on other brands) and slow the **ping speed** (~**15 of 20**) so the layer
paints as a distinct band (`yMiBtZ7k8-w`). Translated to the Garmin GPSMAP
840xs: turn the gain up and slow the ping, then watch for the band
(cameron). The DSL, its depth behavior, and why it matters are in
[deep scattering layer](../conditions/deep-scattering-layer.md); the species
that ride it — [swordfish](../species/swordfish.md) (in and below the DSL)
and [bluefin tuna](../species/bluefin-tuna.md) (sounded deep at night) —
carry the depth-specific signatures. For daytime rockfish marks over hard
bottom, see [rockfish and lingcod](../species/rockfish-lingcod.md).

## Evidence

Trip reports and per-source provenance:
[evidence file](evidence/electronics-and-sounder.md).

<!-- backlinks:start -->
## Linked from

- [12 Mile Reef](../locations/12-mile-reef.md)
- [14 Mile Bank](../locations/14-mile-bank.md)
- [179 / 220](../locations/179-220.md)
- [209 / 312](../locations/209-312.md)
- [279 / 267 / 14 Mile Bank](../locations/279-267-14-mile-bank.md)
- [289 / 284](../locations/289-284.md)
- [311 (Trask Knoll)](../locations/311.md)
- [380](../locations/380.md)
- [43 / 91 / 300](../locations/43-91-300.md)
- [474 / 711](../locations/474-711.md)
- [81 / 381](../locations/81-381.md)
- [Alijos Rocks](../locations/alijos-rocks.md)
- [Barred Sand Bass](../species/sand-bass.md)
- [Bass Structure](../locations/bass-structure.md)
- [Bluefin Tuna](../species/bluefin-tuna.md)
- [Bluefin Tuna — trolling](../species/bluefin-tuna-trolling.md)
- [Cabo San Lucas](../locations/cabo-san-lucas.md)
- [Cabrilla (Leopard Grouper)](../species/cabrilla.md)
- [Calico Bass (Kelp Bass)](../species/calico-bass.md)
- [California Barracuda](../species/barracuda.md)
- [California Halibut](../species/california-halibut.md)
- [California Sheephead](../species/sheephead.md)
- [California Spiny Lobster](../species/california-spiny-lobster.md)
- [Cameron's Boat — Panga Marine Marquesas 22](../profiles/cameron/boat.md)
- [Catalina Island — Front Side](../locations/catalina-island-front-side.md)
- [Cedros / San Benitos](../locations/cedros-island.md)
- [Chunking](../techniques/chunking.md)
- [Current Diagnostics](../conditions/current-diagnostics.md)
- [Day-Plan Protocol](day-plan-protocol.md)
- [Deep Scattering Layer](../conditions/deep-scattering-layer.md)
- [Desperation Reef](../locations/desperation-reef.md)
- [Dorado (Mahi-Mahi)](../species/dorado.md)
- [E. Butterfly / San Salvador Knoll](../locations/e-butterfly-san-salvador-knoll.md)
- [Ensenada](../locations/ensenada.md)
- [Evidence — 14 Mile Bank](../locations/evidence/14-mile-bank.md)
- [Evidence — 209 / 312](../locations/evidence/209-312.md)
- [Evidence — 279 / 267 / 14 Mile Bank](../locations/evidence/279-267-14-mile-bank.md)
- [Evidence — Bluefin Tuna](../species/evidence/bluefin-tuna.md)
- [Evidence — Dorado (Mahi-Mahi)](../species/evidence/dorado.md)
- [Evidence — Electronics and Sounder](evidence/electronics-and-sounder.md)
- [Evidence — La Jolla](../locations/evidence/la-jolla.md)
- [Evidence — Swordfish (Broadbill)](../species/evidence/swordfish.md)
- [Evidence — Yellowtail](../species/evidence/yellowtail.md)
- [February–March](../seasonal/february-march.md)
- [Fleet Intelligence](fleet-intelligence.md)
- [Foamer Casting](../techniques/foamer-casting.md)
- [Guadalupe](../locations/guadalupe.md)
- [Hancock Bank](../locations/hancock-bank.md)
- [Hidden Reef / 170](../locations/hidden-reef-170.md)
- [Hoop Netting](../techniques/hoop-netting.md)
- [Imperial Beach](../locations/imperial-beach.md)
- [Kidney Bank (63) / 175](../locations/kidney-bank-63-175.md)
- [LA - 270 / 286](../locations/la-270-286.md)
- [La Jolla](../locations/la-jolla.md)
- [Lower Cross](../locations/lower-cross.md)
- [Magdalena Bay (Mag Bay / Lopez Mateos)](../locations/bahia-magdalena-lopez-mateos.md)
- [Middle Grounds](../locations/middle-grounds.md)
- [North 9 Mile Bank / 178](../locations/north-9-mile-bank-178.md)
- [November–December](../seasonal/november-december.md)
- [Ocean Whitefish](../species/ocean-whitefish.md)
- [Opah (Moonfish)](../species/opah.md)
- [Pacific Bonito](../species/bonito.md)
- [Pacific Crevalle Jack (Toro)](../species/pacific-crevalle-jack.md)
- [Rockfish & Lingcod](../species/rockfish-lingcod.md)
- [Rockfish Deep-Dropping](../techniques/rockfish-deep-dropping.md)
- [San Clemente Island — Back Side](../locations/san-clemente-island-back-side.md)
- [San Juan Seamount](../locations/san-juan-seamount.md)
- [Santa Barbara Island](../locations/santa-barbara-island.md)
- [Search and Glassing](search-and-glassing.md)
- [Skipjack Tuna](../species/skipjack-tuna.md)
- [Snook (Robalo)](../species/snook.md)
- [South 9 Mile Bank / 439](../locations/south-9-mile-bank-439.md)
- [South Orange County — Crystal Cove](../locations/south-orange-county-crystal-cove.md)
- [Spotted Bay Bass (Spotties)](../species/spotted-bay-bass.md)
- [Striped Marlin](../species/striped-marlin.md)
- [Striped Marlin — trolling](../species/striped-marlin-trolling.md)
- [Sverdrup Bank (126)](../locations/sverdrup-bank-126.md)
- [Swordfish (Broadbill)](../species/swordfish.md)
- [Tanner Bank](../locations/tanner-bank.md)
- [Targeting yellowtail — Coronado Islands](../species/yellowtail-coronado-islands.md)
- [The 43](../locations/43.md)
- [The Bumps](../locations/bumps.md)
- [The Slide / 152 / 277](../locations/slide-152-277.md)
- [W. Butterfly / 157](../locations/w-butterfly-157.md)
- [Wahoo](../species/wahoo.md)
- [White Seabass](../species/white-seabass.md)
- [Yellowfin Tuna](../species/yellowfin-tuna.md)
- [Yellowtail](../species/yellowtail.md)
- [Zone Lexicon](../locations/zone-lexicon.md)
<!-- backlinks:end -->
