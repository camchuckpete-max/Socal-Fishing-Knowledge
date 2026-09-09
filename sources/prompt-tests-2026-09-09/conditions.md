# Conditions & season — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11 | 11.5 | 12 |
| found | 2 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 1.5 | 1.5 | 2 |
| honest | 2 | 2 | 2 |
| actionable | 1.5 | 2 | 2 |
| **wins** | 0 | 0 | 2 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 1 | 1 | 0 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | None | None | None |
| Gear | None | None | None |
| Technique | None | None | None |
| Finding fish | None | None | None |
| Conditions & season | 11 | 11.5 | 12 |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 16. [conditions] What is the Catalina Eddy and when does it matter for deciding where to fish?

**Winner:** NOW · mapping {'A': 'B3', 'B': 'NOW', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three correctly identify the eddy as a wind/sea-state feature rather than a bite feature, cite the same single 2022-05-26 report (S2L3KLSQ6Is), and are honest about how thin the coverage is. B wins because it delivers the decision the other two only gesture at: the mechanism (a northerly wind shadow, so the lee is "everything east of Catalina and San Clemente", not a list of banks), a named test case with a position (the 425 at 32-15.000N 117-23.200W, shielded despite sitting far south), explicit negative triggers for when not to reach for the rule, and the jurisdiction consequence that the 425 sits in baja-pacific-north so routing there is a border crossing — while also disclosing that "counter-clockwise" is flagged contradicted-by-source and that two scopings still coexist in the KB. A is close behind and unusually disciplined about marking its inside-vs-outside wind comparison as its own inference rather than KB procedure, but it inherits the narrow "inner San Diego banks" wording with no mechanism and spends space on off-question bank-naming trivia. C is well written and adds the useful bay all-weather fallback and profile tailoring, but leaves the operative question — how to check eddy state — with no method, which is the difference between a rule the angler can run and a rule they can only recite.

- *B2 reasons:* found: right two notes, correctly files the rule under Unforecast-wind heuristics and separates the bight-scale wind eddy from the ~500-fathom-curve current eddies. specific: full sea-state numbers (10 ft @15 s vs 3-4 ft @4-5 s, 4 ft @10 s fishing like 6 ft @7-8 s, ~12 kt, sub-10 s, 12-15 kt / 4-8 ft @9 s, 5-8 degF), plus profile facts (22 ft panga, Dana Landing, 8 a.m. departure) — but no coordinates and no named shielded marks. sourced: note paths throughout with S2L3KLSQ6Is, NC3-3pJDEgo, aFb221LUoD0, HnqiE05vdXs (that last id verifies against the repo) and an honest note on the bight-geography cite mismatch. scoped: region/waters right, correctly labels the NW-rollover map as a different mechanism, no regulation asserted. honest: opens by calling the treatment two short paragraphs from one 2022-05-26 report, lists seven concrete gaps, refuses to fill from outside knowledge, no relative time. actionable: gives the trigger, protocol placement, side-of-island swell guidance and the bay all-weather fallback, but leaves the load-bearing question — how to actually check eddy state — with no method at all, where A and B both give the per-spot inside-vs-outside wind pull; it also carries the narrower 'inner SD banks' scoping with no mechanism, so the reader cannot tell whether a mark south of San Clemente is in the lee.
- *B3 reasons:* found: goes straight to the two notes that carry the eddy (sea-state Unforecast-wind heuristics + island-structure) and adds the raw transcript's day-by-day timescale. specific: steepness rule, 4 ft @10 s fishing like 6 ft @7-8 s, ~12 kt / sub-10 s / 12-15 kt with 4-8 ft @9 s, 5-8 degF rollover, SD Bay entrance 160-186 deg — but no positions for shielded marks. sourced: every claim carries a note path plus S2L3KLSQ6Is / NC3-3pJDEgo / Rf1HKJG-SDg, and it flags where a video id could not be resolved rather than guessing. scoped: socal-bight / island-bank framing correct, no regulation asserted, no Baja detail smuggled in unlabeled. honest: labels the inner-vs-outer wind comparison explicitly as its own chaining of two KB rules, and calls the doctrine single-source despite note-level high confidence. actionable: clear trigger, protocol step 1b envelope placement, endpoint rules incl. the /api/v1/context wind warning, go/no-go thresholds — though some padding (bank-naming trivia) is off-question.
- *NOW reasons:* found: only answer that surfaces the adjudicated rescoping (lee east of Catalina/San Clemente, Cameron 2026-08-26) AND the standing fact-check flag on 'counter-clockwise', plus the two coexisting scopings still live in other notes. specific: lat/lon for South 9 Mile (32-32.000N 117-21.000W), North 9 Mile (32-38.000N 117-26.000W, 4.9 nm, Zuniga 10.9 nm at 078) and the 425 (32-15.000N 117-23.200W), plus the same sea-state thresholds. sourced: note paths for each variant wording, ledger row cited for the flag, S2L3KLSQ6Is / NC3-3pJDEgo / zKmZ4zql2ws / aFb221LUoD0 attached to the right claims. scoped: best jurisdiction handling — flags the 425 as baja-pacific-north, i.e. a border crossing routed through mexican-waters.md, not just a weather call; no regulation number stated bare. honest: states the rotation direction is contradicted-by-source, admits no plottable boundary, no strength delta, no duration doctrine, and names the unflagged stale wording on socal-bight.md. actionable: gives the wind-direction mechanism (northerly lee) so the angler knows when the rule applies, explicit negative triggers (south/east wind, swell rather than wind, water-quality rather than sea-state), and the per-spot wind check with endpoints.

<details><summary>Full prompt</summary>

What is the Catalina Eddy and when does it matter for deciding where to fish?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short answer

In this knowledgebase the **Catalina Eddy is a wind/sea-state feature, not a fish-holding feature.** It is described as *"a counter-clockwise circulation that sets up in the bight"* that can **shield the inner San Diego banks and the tuna grounds while it blows outside** ([`locations/island-structure.md`](locations/island-structure.md) § "The Catalina Eddy as a shielding feature"; Landesfeind, 5/26/22 report — `S2L3KLSQ6Is`).

The framing the KB uses is worth keeping: *islands do not only make bottom structure — they shape the wind field.* The eddy is an **island-driven feature that decouples inner-zone seas from the offshore forecast** ([`locations/island-structure.md`](locations/island-structure.md)).

## When it matters for deciding where to fish

It matters in exactly one decision, and the KB files it under **"Unforecast-wind heuristics"** in [`conditions/sea-state.md`](conditions/sea-state.md) — the block of rules for when the forecast lies to you:

> **Catalina Eddy shielding.** The Catalina Eddy can shield the inner SD banks / tuna grounds while it blows outside. **Check eddy state when the outer forecast looks bad before writing off the inside** (5/26/22). — [`conditions/sea-state.md`](conditions/sea-state.md), `S2L3KLSQ6Is`

So the trigger is: **the outer/offshore forecast reads blown, and you are about to cancel the day or write the inside off with it.** That is the moment to check eddy state. It is an *inside-vs-outside* zone-selection lever, not a "the day is saved" lever — nothing in the KB claims the eddy improves the bite, only that it can hold the inner zones fishable.

In protocol terms it lands at **step 2** of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) — "apply priors + interpretation layers ... weight zones and set timing" — *before* you resolve species and technique at step 3. Zone choice happens first; the eddy is one of the inputs to it.

## The two heuristics that sit right beside it (they lean the other way)

The eddy rule is one of three unforecast-wind rules in [`conditions/sea-state.md`](conditions/sea-state.md), and the other two are pessimistic — do not use the eddy as a general reason to trust a marginal forecast:

- **Inland heat → afternoon W wind.** Extreme inland heat (100 °F+) can break down into unforecast afternoon W wind on the water. If it is windier than forecast in the morning, **assume it builds all day — a small boat bails early** (7/14/22).
- **Forecast error is asymmetric.** Assume the forecast errs on the **worse** side, and that afternoon W at the islands **strengthens** rather than eases (Academy Ep. 6).

## The same decision, other levers in the KB

When you are making the "where do I actually go today" call under wind, these are the other notes the protocol routes you through:

- **Steepness before height** — 10 ft @ 15 s from the south is barely felt; 3–4 ft @ 4–5 s is brutal. Flag any zone or route leg where the period in seconds approaches the height in feet ([`conditions/sea-state.md`](conditions/sea-state.md)).
- **Current-vs-swell opposition** — summer uphill (counter)current against the NW swell stands it up: a forecast **4 ft @ 10 s fishes like 6 ft @ 7–8 s**, and the point forecast will not show it ([`conditions/sea-state.md`](conditions/sea-state.md)).
- **Bathymetric slop is local, not regional** — the ridge off the **east end of Catalina** is horrible for a few miles then **lays down 3–4 mi past it**. Do not let one rough patch on the transit imply the whole outer zone is blown ([`conditions/sea-state.md`](conditions/sea-state.md)). This is the mirror image of the eddy rule: both say *don't generalize a sea state across the bight*.
- **Hard go/no-go numbers** (dave-hansen, `NC3-3pJDEgo`, 2020-11-18 — the note flags these as **medium** confidence, single mention): wind **above ~12 kt** is what raises whitecaps and is his personal don't-run cutoff; **swell interval under 10 s is a hard bad-sea flag** regardless of height; **12–15 kt with 4–8 ft at a 9-second interval** is the named unfishable combo, and he holds bigger boats at the dock in it too ([`conditions/sea-state.md`](conditions/sea-state.md)).
- **Which side of Catalina, once you're going** (Capt. Dave Hansen, `aFb221LUoD0`, 2020-10-20 — medium confidence): a **south swell** tears up Catalina's **east end** and makes it hard to fish; a **big west swell** is the trigger to send anglers **down to the east end** rather than front-side/backside/middle ([`locations/island-structure.md`](locations/island-structure.md)).
- **The "look south when it blows" geography** — a distinct mechanism (temperature rollover, not wind shielding) from a different report: a big NW blow **crushes the northern Channel Islands and the LA/Ventura shelf** (surface temp down **5–8 °F**), **south of Newport is less prone**, and in that event the **Coronados, tuna grounds, Catalina and San Clemente held their water** ([`locations/bight-geography.md`](locations/bight-geography.md), 4/21/22 report; note front matter carries `HzE4FHHcvTk`). Same direction of travel as the eddy rule — look inside/south — but it is about water, not seas, so treat them as two independent checks, not one.
- **If neither saves the day** — [`species/spotted-bay-bass.md`](species/spotted-bay-bass.md) is explicit that **the bay is the all-weather fallback**: when the outside coast is blown out or rained on, spotties in the harbor stay catchable and keep the day alive.

## One ambiguity to keep straight

The KB uses "eddy" in **two unrelated senses**, and it never connects them:

1. **The Catalina Eddy** — the bight-scale counter-clockwise circulation above; a *wind* feature.
2. **Eddies at Catalina's ~500-fathom curve** — the uphill (summer counter)current **compresses as it climbs the slope, spins eddies, and aggregates both bait and kelp paddies along the curve** (8/31/22 report, `HnqiE05vdXs`; [`conditions/current-structure.md`](conditions/current-structure.md), [`locations/island-structure.md`](locations/island-structure.md)). This one *is* a fish-finding feature — the curve is "a line you can hunt, not a point," worked slowly, with the governing rule **"sign associated with structure is a repeatable decision; sign in no-man's-land is low value."**

If someone tells you "the eddy is holding fish," they mean sense 2. The sea-state doctrine is sense 1.

## For your boat specifically

Your profile ([`profiles/cameron/boat.md`](profiles/cameron/boat.md)) puts you squarely in the zone this rule is about — 22' Panga Marquesas, launching **Dana Landing (Mission Bay)**, home waters **Coronado Islands, La Jolla, San Diego offshore banks**. "Inner SD banks / tuna grounds" *is* your normal water, so for you the eddy rule is not an exotic edge case: it is the reason a blown outer forecast should not automatically cancel a Coronados or inner-banks day. Two profile-level facts to fold in on that call: your **normal ~8 a.m. departure** puts you into the afternoon W build window that the two pessimistic heuristics above warn about, and your own chart work gives the **San Diego Bay entrance as open to swell from roughly 160°–186°, channel seaward axis 186°, with Baja blocking east of ~160° and Point Loma blocking west of 186°** ([`conditions/sea-state.md`](conditions/sea-state.md), sourced `cameron`) — a separate launch/return exposure check from the eddy question.

## What the KB does not tell you about the Catalina Eddy

I want to be straight about how thin this is — the entire treatment is **two short paragraphs**, in [`conditions/sea-state.md`](conditions/sea-state.md) and [`locations/island-structure.md`](locations/island-structure.md), both tracing to **one report, 2022-05-26 (`S2L3KLSQ6Is`)**. There is no dedicated eddy note. Specifically missing:

- **No season.** The KB never says which months eddies form. The single cite lands in late May, and [`seasonal/may.md`](seasonal/may.md) draws on the same video without mentioning the eddy at all; no seasonal note names it.
- **No method for "check eddy state."** The doctrine tells you to check it but names **no data product, model, chart or on-water tell** to check it with. [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md) has you pull wind/swell/current from BightSST, and [`conditions/current-diagnostics.md`](conditions/current-diagnostics.md) gives on-water current reads (kelp lean, chum-drift angle) — but neither is presented as an eddy-state read.
- **No mechanism, duration or strength.** Nothing on why it forms, how long it typically lasts, or what wind speeds/directions live inside it.
- **No bite effect.** Nothing on whether an eddy changes water temperature, chlorophyll, current or the fishing itself — only that it shields seas.
- **No zone boundaries.** "Inner SD banks" and "the tuna grounds" are used as zone names but never defined; [`locations/zone-lexicon.md`](locations/zone-lexicon.md) has no entry for either.
- **No fog / marine-layer / visibility angle.** The only fog content in the KB is Baja-specific radar navigation at Cedros ([`planning/electronics-and-sounder.md`](planning/electronics-and-sounder.md)); nothing ties an eddy to visibility or glassing.

Everything in those bullets I would be filling in from outside the KB, so I am leaving it out.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `locations/island-structure.md`, `conditions/current-structure.md`, `conditions/current-diagnostics.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `planning/report-reading-and-forecasting.md`, `planning/electronics-and-sounder.md`, `seasonal/may.md`, `species/spotted-bay-bass.md`, `profiles/cameron/boat.md`, `sources/extraction-log.md`  
*videos:* `S2L3KLSQ6Is`, `HnqiE05vdXs`, `HzE4FHHcvTk`, `NC3-3pJDEgo`, `aFb221LUoD0`, `d0yGBQDeY_4`  
*gaps admitted:* No dedicated Catalina Eddy note - the entire treatment is two short paragraphs in conditions/sea-state.md and locations/island-structure.md, both tracing to a single 2022-05-26 report (S2L3KLSQ6Is). | The KB gives no season or months for when Catalina Eddies form; no seasonal/ note mentions the eddy, including seasonal/may.md which draws on the same source video. | The doctrine says 'check eddy state' but names no data product, model, chart, forecast tool or on-water tell for actually checking it. | No physical mechanism for why the eddy forms, how long it typically persists, or what wind speeds/directions occur inside it. | No claim anywhere that the eddy affects water temperature, chlorophyll, current or the bite - the KB treats it purely as wind/sea-state shielding. | 'Inner San Diego banks' and 'the tuna grounds' are used as zone names but never defined; locations/zone-lexicon.md has no entry for either. | No fog / marine-layer / visibility consequence is documented for the eddy; the KB's only fog content is Baja-specific radar navigation at Cedros. | The KB never states whether the bight-scale Catalina Eddy and the small local eddies spun off Catalina's ~500-fathom curve are related phenomena - they appear in separate notes with no cross-reference. | No guidance on how far the shielding extends, which specific banks fall inside vs outside it, or how to bound the shielded area on a chart. | locations/bight-geography.md attributes its wind-rollover geography to a 4/21/22 report while its front matter lists only HzE4FHHcvTk (the 8/17/22 report), so the video-ID mapping for that specific claim is not clean in the KB.

</details>

<details><summary><b>B3 — batch 3</b> · 12/12</summary>

# The Catalina Eddy — what the KB has, and when it changes your zone call

## What it is

The knowledgebase carries the Catalina Eddy in exactly one role: **a wind-field feature, not a water feature.**

> The **Catalina Eddy** is a **counter-clockwise circulation that sets up in the bight**. Islands do not only make bottom structure — they shape the wind field. ([`locations/island-structure.md`](locations/island-structure.md), "The Catalina Eddy as a shielding feature", attributed to Landesfeind's 5/26/22 Bight report → `S2L3KLSQ6Is`)

That is the whole definition the KB gives. It does **not** explain how the eddy forms, what its boundaries are, or how long it typically lasts — see the gaps at the bottom.

## What it does for you — the shielding rule

The one piece of doctrine, stated the same way in both notes that carry it:

- **The eddy can shield the inner San Diego banks and tuna grounds while it blows outside.** When the outer forecast looks blown, **check eddy state before you write off the inside** — the inner zones may be fishable. ([`conditions/sea-state.md`](conditions/sea-state.md) → "Unforecast-wind heuristics"; [`locations/island-structure.md`](locations/island-structure.md); both cite the 5/26/22 report, `S2L3KLSQ6Is`)
- The framing that matters: the eddy is **an island-driven feature that decouples inner-zone seas from the offshore forecast** ([`locations/island-structure.md`](locations/island-structure.md)). A single "it's blown out" read pulled from a broad offshore forecast can be wrong for the inside on the same day.

The raw source behind that doctrine (BD Outdoors Bight report, 2022-05-26, `S2L3KLSQ6Is` — transcript in [`sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md`](sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md)) shows it operating on a **day-to-day timescale inside a single week's forecast**: Monday "a wash," then Tuesday it backs off "down south here in the tuna grounds" because "you get that Catalina eddy blocking off," creeping back in Tuesday afternoon into Wednesday, into the eddy again by Thursday, and weather rebuilding Friday — "hopefully that eddy holds up, keeps that pushed out." That is raw transcript detail, not curated doctrine, so treat it as illustration of the timescale, not as a rule.

## When it matters for deciding where to fish

**Trigger:** the *outer* forecast (offshore banks / open ocean) looks bad, and your candidate zones include **inner San Diego water — the tuna grounds and the inner banks** ([`conditions/sea-state.md`](conditions/sea-state.md)). That is the moment to check eddy state instead of cancelling.

**Where it sits in the day-plan protocol** ([`planning/day-plan-protocol.md`](planning/day-plan-protocol.md)):

- **Step 1 (pull conditions)** and **step 2 (apply the interpretation layers)** — the eddy is a `conditions/sea-state` input, i.e. a *fishability / where-can-I-physically-go* call.
- It feeds **step 1b**, the binding `{regions, waters}` envelope: the eddy is what can keep `bank` water in `socal-bight` inside the envelope on a day the offshore forecast would have cut it. If it is not shielding, the envelope shrinks and the plan must shrink with it — the protocol is explicit that if nothing in the envelope fits the conditions you say so and stop.
- It does **not** enter step 3 (species/technique) at all. Nothing in the KB says the eddy makes fish bite better or worse.

**When it does *not* matter:** if the outer forecast is already fishable, eddy state is irrelevant to the decision — the KB gives it no upside, only a rescue of the inside when outside is blown.

## How to actually check eddy state with this KB's tooling

The KB names **no eddy index, product, or endpoint**. There is no `/api/v1/eddy`. What [`config/endpoints.md`](config/endpoints.md) does require is the thing that would reveal it:

- **Per-spot resolution is mandatory** — wind and swell get queried at *every* candidate spot and at points along the route out and back; "a single coastal station cannot describe a trip that crosses 40 miles of open water."
- **Wind forecast per coordinate:** `api.open-meteo.com/v1/forecast` — `wind_speed_10m`, `wind_gusts_10m`, `wind_direction_10m` (fallback `api.weather.gov` marine zones). **Observed wind/swell:** NDBC realtime station text.
- **Do not use BightSST `/api/v1/context` for this.** Its wind is **field-wide and it carries no swell** — it returns the same wind whatever lat/lon you pass (verified 2026-08-18 at two points 130 nmi apart).

So operationally: pull per-spot wind at inner SD spots *and* at the outer banks and compare. A shielded inside shows up as an inner/outer divergence in the wind field. **That inner-vs-outer comparison is my chaining of two KB rules, not a stated KB procedure** — the KB tells you to check eddy state and tells you to pull per-spot wind, but never spells out how to read the eddy off a wind pull.

Also apply the report-aging discipline: an eddy call from a dated report is a *forecast-week* statement. The KB's rule for weather-event volatility is "conditions rolled over — don't rely on your pre-fish"; after any significant weather event, treat pre-event intel as expired regardless of age ([`planning/report-reading-and-forecasting.md`](planning/report-reading-and-forecasting.md)).

## Don't confuse it with the *other* Catalina eddies

Two different things share the word, and only one is the Catalina Eddy:

1. **The Catalina Eddy** — a wind/weather circulation over the bight; effect is on **sea state** (above).
2. **Structural eddies at Catalina's ~500-fathom curve** — where the island rises off the plain, the uphill (summer counter) current **compresses as it climbs the slope, spins eddies, and aggregates both bait and kelp paddies along the curve** (8/31/22 report; [`locations/island-structure.md`](locations/island-structure.md), [`conditions/current-structure.md`](conditions/current-structure.md)). That is a *bite* feature — the curve is a line you hunt, and the governing rule is **"sign associated with structure is a repeatable decision; sign in no-man's-land is low value."** It has nothing to do with the wind eddy.

## Once you decide to go inside, these still apply

The eddy buys you a zone; it does not exempt the day from the rest of [`conditions/sea-state.md`](conditions/sea-state.md):

- **Steepness rule:** period beats height. **10 ft @ 15 s** from the south is barely felt; **3–4 ft @ 4–5 s** is brutal. Flag any zone or route leg where the period in seconds approaches the height in feet.
- **Current-vs-swell opposition:** summer uphill countercurrent against NW swell makes a forecast **4 ft @ 10 s** fish like **6 ft @ 7–8 s**. NWS point forecasts won't show it — degrade the forecast where current and swell oppose.
- **Bathymetric slop:** the ridge off **Catalina's east end** is horrible for a few miles, then lays down **3–4 mi past it** — one rough patch does not condemn the whole outer zone.
- **12–24 h wind hindcast, not just the forecast** — a calm-morning read hides overnight wind.
- **Forecast error is asymmetric:** assume it errs worse, and assume afternoon W at the islands **strengthens**.
- **Go/no-go thresholds** (dave-hansen, `NC3-3pJDEgo`, 2020-11-18 — single-mention, medium confidence): wind above **~12 kt** raises whitecaps and is his personal cutoff; **sub-10-second swell interval is a hard bad-sea flag**; **12–15 kt with 4–8 ft @ 9 s** is the named unfishable combo, and he holds larger boats at the dock in it too.
- **Homebound wind:** plan the return leg against the afternoon W build, not just the outbound.
- If you're launching out of San Diego Bay, Cameron's own chart work: the entrance is open to swell from roughly **160°–186°**, channel seaward axis **186°**; Baja blocks swell from east of ~160°, Point Loma blocks west of 186° ([`conditions/sea-state.md`](conditions/sea-state.md)).

## One reinforcing but *different* piece of geography

Do not merge these — the mechanism differs. In a big **NW blow**, the wind-rollover map says the **northern Channel Islands and the LA/Ventura coastal shelf get crushed** (surface temp rolled down **5–8 °F**), **south of Newport is less prone**, and the **Coronados, the tuna grounds, Catalina and San Clemente held their water** through the event ([`locations/bight-geography.md`](locations/bight-geography.md), attributed to the 4/21/22 Landesfeind report; note's declared source `HzE4FHHcvTk`). That is about **water temperature surviving**, not about wind shielding — but it points the same direction on a blown NW day: look south and inside.

Bank-name context if you're picking inner spots: a bank is named for **the fathom depth of its shallowest high spot** ("182" tops at 182 fm, "43" at 43 fm); **Nine Mile Bank** is the exception, named for sitting **9 statute miles off the coast**, with many closely spaced high spots (roughly 600 ft in places, figure uncertain in the source) rather than one peak ([`locations/zone-lexicon.md`](locations/zone-lexicon.md), `Rf1HKJG-SDg`).

## Confidence, honestly

Both notes that carry the eddy sit at `confidence: high` at note level, and Landesfeind is a registered source in [`sources/source-registry.md`](sources/source-registry.md) (repeated, dated SoCal doctrine). But **the eddy claim itself traces to a single dated report** — `S2L3KLSQ6Is`, 2022-05-26 — repeated into two notes from that one origin ([`sources/extraction-log.md`](sources/extraction-log.md) logs `S2L3KLSQ6Is → conditions/sea-state; seasonal/may`). Treat it as a real, usable planning trigger, but a thin one.

## What this KB does not tell you about the Catalina Eddy

- **No season or months.** Nothing in [`seasonal/`](seasonal/README.md) mentions the eddy — including [`seasonal/may.md`](seasonal/may.md), which is built from the very same 5/26/22 video. So the KB gives you **no month-of-year prior** for when to expect it. The only timing signal anywhere is that its one source is a late-May report.
- **No formation mechanism** — "counter-clockwise circulation that sets up in the bight" is the extent of it; nothing on what drives it or what breaks it down.
- **No geographic extent** — "inner San Diego banks and tuna grounds" is never resolved to named banks or a boundary, so you can't tell where the shielded edge sits.
- **No duration or forecast method** — nothing on how long it holds, and no named product, index, or endpoint for "eddy state."
- **No fishing-quality effect** — nothing on whether eddy conditions help or hurt the bite, water temp, chlorophyll, or visibility.
- **No interaction rules** — nothing on eddy vs. Santa Ana, or eddy effects on the northern Channel Islands.

If you want any of that, it has to come from a source outside this KB — I'm not going to fill it from general knowledge.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `locations/island-structure.md`, `conditions/current-structure.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `config/endpoints.md`, `planning/report-reading-and-forecasting.md`, `seasonal/may.md`, `sources/source-registry.md`, `sources/extraction-log.md`, `sources/bd-transcript-knowledge-proposal.md`, `sources/transcripts/_manifest.csv`, `sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md`  
*videos:* `S2L3KLSQ6Is`, `NC3-3pJDEgo`, `HzE4FHHcvTk`, `aFb221LUoD0`, `Rf1HKJG-SDg`  
*gaps admitted:* No season or months given for the Catalina Eddy anywhere in the KB — seasonal/may.md is built from the same 5/26/22 video and never mentions it, so there is no month-of-year prior. | No formation mechanism — the KB says only 'a counter-clockwise circulation that sets up in the bight' and never explains what drives it or breaks it down. | No geographic extent or boundary — 'inner San Diego banks and tuna grounds' is never resolved to named banks or a shielded-edge line. | No duration or persistence guidance — nothing on how long an eddy typically holds. | No named forecast product, index, model, or endpoint for checking 'eddy state'; the inner-vs-outer per-spot wind comparison I suggest is my chaining of two KB rules, not a stated KB procedure. | No stated effect of the eddy on fishing quality — nothing on bite, water temperature, chlorophyll, water color, or visibility/fog. | No interaction rules between the Catalina Eddy and other patterns (e.g. Santa Ana events), and nothing on eddy effects north of the bight's inner zones (Channel Islands). | Single-source claim: the eddy doctrine in both conditions/sea-state.md and locations/island-structure.md traces to one dated report (S2L3KLSQ6Is, 2022-05-26), despite the notes' high note-level confidence. | locations/bight-geography.md attributes its wind-rollover geography to a 4/21/22 Landesfeind report but its front-matter sources list only HzE4FHHcvTk (an 8/17/22 report), so the video id backing that specific claim is not cleanly resolvable from the note. | The video id behind the 8/31/22 fathom-curve eddy example in locations/island-structure.md and conditions/current-structure.md could not be resolved from the manifest, so no video id is asserted for that claim.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## The Catalina Eddy — what the KB has

**What it is.** The KB carries it as a *wind* feature, not a current or temperature feature. `locations/island-structure.md` describes it as "a counter-clockwise circulation that sets up in the bight" that can shield inside water while it blows outside (`S2L3KLSQ6Is`) — **but that same line carries a standing fact-check flag**: the source never states a rotation direction and never names San Diego banks specifically; it says only "tuna grounds down south" (`sources/fact-check-ledger.md`, row on `island-structure.md`). So treat "counter-clockwise" as unverified in this KB. What *is* solid is the operational effect, not the meteorology.

**What it does — the adjudicated scope.** Per `conditions/sea-state.md` (Unforecast-wind heuristics, marked ⚠ adjudicated, Cameron, 2026-08-26):

> The shielded water is a **lee, not a list of banks**. The prevailing wind down the California coast outside SoCal comes from the **north**, so the islands shadow the water behind them, and marks well to the south still sit in that shadow.

Scope: **everything east of Catalina and San Clemente.** The named example is the **425** — "often shielded despite being far south of San Clemente" (cameron). That mark is at **32°15.000'N 117°23.200'W** (`locations/425-bank.md`) — note it sits in `baja-pacific-north` under `locations/101-425.md`, i.e. Mexican water, so routing there is a border crossing (`locations/mexican-waters.md`), not just a weather call.

**Heads-up on two versions in the KB.** The narrower pre-adjudication wording — "shields the *inner San Diego banks* and tuna grounds" — still stands on `locations/north-9-mile-bank-178.md` (flagged there as ⚠ contradicted-internal, superseded) and unflagged on `locations/socal-bight.md`. Use the `sea-state.md` / `south-9-mile-bank-439.md` scoping; it's the adjudicated one.

## When it matters for deciding where to fish

**One trigger: the outside forecast looks blown, and you are about to write off the inside.** The rule is stated the same way in three places (`conditions/sea-state.md`, `locations/south-9-mile-bank-439.md`, `locations/socal-bight.md`): *check the eddy state before writing the inside off* — an ugly offshore forecast does not automatically close the inner zones.

In `planning/day-plan-protocol.md` terms it bites at **step 1b (set the envelope)** and **step 2 (priors + layers)**, not at gear time. It is what keeps `island` / `bank` water inside the day's envelope on a day the raw offshore numbers would have deleted it. Concretely, marks the KB places inside the shielded line:

| Zone | Positions | Note |
| --- | --- | --- |
| South 9 Mile Bank / 439 | 32°32.000'N 117°21.000'W and 32°29.500'N 117°24.000'W, 3.6 nm apart | carries the rescoped wording (`locations/south-9-mile-bank-439.md`) |
| North 9 Mile Bank / 178 | 32°38.000'N 117°26.000'W and 32°42.000'N 117°29.317'W, 4.9 nm apart; Zuniga Jetty 10.9 nm at 078° | `locations/north-9-mile-bank-178.md` |
| The 425 | 32°15.000'N 117°23.200'W | Cameron's named "far south and still shielded" case |

**It does not matter — don't reach for it — when:**
- The wind is *not* from the north. The whole mechanism is an island wind-shadow off a northerly. Nothing in the KB claims shielding from a south or east wind.
- Your inside spot's own per-spot wind pull is already bad. The eddy is a reason to *check*, never a reason to assume.
- The problem is swell rather than wind. Swell direction is a separate decision layer: a big west swell is the trigger to run **down to Catalina's east end**, a south swell tears up that same east end (`aFb221LUoD0`, `locations/island-structure.md`). And the ridge off Catalina's **east end** is locally horrible for a few miles then lays down 3–4 mi past it (`zKmZ4zql2ws`, `conditions/sea-state.md`) regardless of any eddy.
- The problem is water quality, not sea state. That is the separate NW-event rollover map (`locations/bight-geography.md`): a strong NW blow rolls SST **5–8 °F** on the northern Channel Islands and the LA/Ventura shelf, south of Newport is less prone, and the Coronados / tuna grounds / Catalina / San Clemente held their water. Useful alongside the eddy, but a different question — and that map itself carries a standing ⚠ cite-unresolved flag (adjudicated to stand, to be backed by BightSST rollover statistics rather than re-sourced).

**How to actually check "eddy state."** The KB names **no eddy product and no eddy index** — `config/endpoints.md` has breaks, fronts, upwelling, bathymetry, but nothing for this. So the check is per-spot wind, observed **and** forecast, at each candidate inside mark and along the transit route, compared against the outside numbers. Two hard rules from `config/endpoints.md`: per-spot resolution is required (a single coastal station cannot describe a 40-mile crossing), and **never use `/api/v1/context` for wind** — it returns the same field-wide wind whatever lat/lon you pass (verified 2026-08-18 at two points 130 nmi apart). Wind forecast comes from `api.open-meteo.com/v1/forecast` (`wind_speed_10m`, `wind_gusts_10m`, `wind_direction_10m`), observed from NDBC realtime.

**Shielded still has to pass go/no-go.** Being in the lee does not exempt the spot from `conditions/sea-state.md` thresholds (`NC3-3pJDEgo`): wind above ~**12 kt** raises whitecaps and is the personal not-running cutoff; swell interval under **10 seconds** is a hard bad-sea flag independent of height; **12–15 kt with 4–8 ft at a 9-second interval** is the named unfishable combo, dock-stay for any size boat. Also apply the steepness read — 10 ft @ 15 s from the south is barely felt, 3–4 ft @ 4–5 s is brutal (`zKmZ4zql2ws`) — and remember forecast error is asymmetric: assume it errs worse, and that afternoon W at the islands strengthens rather than eases (`zKmZ4zql2ws`).

**Persistence.** The one underlying source is a single weekly BD Outdoors bight report dated 2022-05-26 (`sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md`), and in it the eddy state changes day to day across one week — blocking early, creeping back in Tuesday afternoon into Wednesday, back into the eddy by Thursday, with weather wrapping around again Friday. That's the practical caution: check it **for your day**, not for your week.

## What the KB does not cover

- **No meteorology.** No explanation of what forms the eddy, no confirmed rotation direction (the "counter-clockwise" line is flagged contradicted-by-source), and nothing on the marine layer / low cloud that goes with it — a grep for "marine layer", "June gloom", "May gray" returns nothing in `conditions/`, `seasonal/`, `locations/` or `planning/`.
- **No seasonality.** No `seasonal/` note mentions the eddy at all, so the KB gives no calendar prior for when in the year to expect it. The only date attached to it anywhere is the source's own 2022-05-26 report date.
- **No plottable boundary.** "East of Catalina and San Clemente" is Cameron's lee description, not a charted line; no corpus source gives an edge you can draw on a chart.
- **No strength or duration doctrine** — no inside-vs-outside wind delta that counts as "shielded," and no rule for how long it holds.
- **No fishing effect beyond wind** — nothing on what the eddy does to current, SST, chlorophyll or bait.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `locations/island-structure.md`, `locations/socal-bight.md`, `locations/south-9-mile-bank-439.md`, `locations/north-9-mile-bank-178.md`, `locations/425-bank.md`, `locations/101-425.md`, `locations/bight-geography.md`, `config/endpoints.md`, `sources/fact-check-ledger.md`, `sources/spot-harvest.md`, `sources/extraction-log.md`, `sources/transcripts/_manifest.csv`, `sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md`  
*videos:* `S2L3KLSQ6Is`, `zKmZ4zql2ws`, `NC3-3pJDEgo`, `aFb221LUoD0`, `HzE4FHHcvTk`  
*gaps admitted:* No meteorology for the Catalina Eddy — nothing on what forms it, and the 'counter-clockwise circulation' description on locations/island-structure.md is flagged contradicted-by-source (the transcript never states a rotation direction). | No marine-layer / low-cloud coverage anywhere in conditions/, seasonal/, locations/ or planning/, so the KB does not connect the eddy to sky or light conditions. | No seasonality — no seasonal/ note mentions the eddy, so the KB gives no month-by-month prior for when it sets up; the only date attached to it is the 2022-05-26 source report date. | No plottable boundary — 'east of Catalina and San Clemente' is Cameron's adjudicated lee description (2026-08-26), not a charted line; no corpus source gives an edge position. | No eddy index, product or endpoint — config/endpoints.md carries breaks, fronts, upwelling and bathymetry but nothing that reports 'eddy state', so checking it is left to per-spot wind comparison. | No strength threshold — the KB gives no inside-vs-outside wind delta that qualifies as 'shielded'. | No persistence/duration doctrine — the single underlying source is one weekly report in which the eddy state shifts day to day, and no note generalizes how long shielding holds. | No stated effect of the eddy on current, SST, chlorophyll or bait — the KB treats it purely as a wind-shielding feature. | Two scopings of the eddy coexist in the KB: locations/north-9-mile-bank-178.md and locations/socal-bight.md still carry the superseded 'inner San Diego banks' wording (flagged only on the 178 page). | No run time, sea-state envelope or minimum boat range is given for the shielded 9 Mile Bank zones (explicitly flagged as a gap on locations/north-9-mile-bank-178.md).

</details>

### 17. [conditions] What changes in the Southern California Bight from September into October, and how should my fishing change wi…

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B2', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 1 | 2 | 2 | **11** | regulation_without_asof |
| B3 | 2 | 2 | 2 | 1 | 2 | 2 | **11** | regulation_without_asof |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three correctly identify the real change — September's warm-stable volume square giving way to October's fall fragmentation, where the chart replaces the spot list, breaks reappear and you pick a side per species — and all three deliver comparable numeric depth on bluefin bands, swordfish go/no-go and the grunion-in-kelp override. A wins on the two things that separate a knowledgebase answer from a good guess: it is the only one that stamps every regulatory claim with jurisdiction + as-of 2026-08 + verify-current (B leaves as-of off all of them; C leaves the Farnsworth take restriction bare), and it is the only one that tells the angler which load-bearing October claims are shaky — the '100% temp chart' quote spliced from non-adjacent passages, the Tanner/Cortez condensation and warm-band arc resting on a single source, the lobster bag limit from one garbled aside — instead of presenting them as settled. C is a very close second and has the most legible planning surface, a situation→technique→gear-class table with links plus search-box sizing; B has the best per-species rigging detail (hook sizes, leader step-downs, paddy read depths) but the weakest regulatory scoping and the least provenance skepticism.

- *B2 reasons:* found: same regime read, plus chlorophyll aging, moon relocation and the Sept-to-Oct species roster; good coverage of yellowtail/squid which the others thin out. specific: strongest per-species execution — 2/0 circle on 30 lb, drop to size 1 thin wire on 15–20 lb, bait-net trick, leader step-down 40→30→20→15 lb, boomerang arcs 90–120 ft, fish ~100 yd off the paddy for tuna, 6–6.5 kt troll. sourced: note paths throughout with video ids on the key observations (5to3Q5P7w90, OYOda6T3f-8, VWClGAn2WEw, mDmbGdQAy-4 labeled medium confidence). scoped: region correct, but every regulation — lobster season, year-end rockfish closure, Farnsworth take restriction — carries 'verify with CDFW' without an as-of stamp, which the KB's own content rule requires. honest: solid gap list (no moon/tide calendar, no albacore, marlin bait-and-switch stub, Baja-vs-Bight yellowtail caveat) and flags one observation as medium confidence, but presents the '100%' quote as clean verbatim and the retreat path as settled. actionable: highest per-species rigging detail of the three; an angler could tie and fish from it directly.
- *B3 reasons:* found: cleanest framing of the regime boundary (side-by-side table), the retreat arc, break-side rules, what stops mattering from September, and what is coming after October. specific: 50–60 sq-mi below-Clemente search box vs 20–30 min compact spots, 30–50 fm knife-jig band, 150–300/300–400 g, 8–15 kt kite window, 13–15 kt Mad Mac, DSL ≥600 ft (pref ~950 ft) with bait at 100–150 fm, Santa Ana 25–45 kt at Avalon. sourced: markdown links to specific notes on nearly every claim plus video ids (HzE4FHHcvTk, E4vKwRaRueA, Z3rZqy2Pi8E, NC3-3pJDEgo with medium-confidence label). scoped: lobster block is exemplary (CDFW, as-of 2026-08, verify, gear code 1, 5/10 net rule), but the Farnsworth 'only yellowtail and bonito may be kept' closure is stated bare — no jurisdiction, no as-of, no verify. honest: names flagged stubs (sword sight-fishing, yellowfin spread geometry), Cameron's open research question on marlin triggers, no numeric fragmentation threshold, no grunion predictability, no bait-receiver coverage. actionable: the situation→technique→gear-class table with technique links is the most directly usable planning surface of the three.
- *NOW reasons:* found: nails the Sept warm-stable → Oct fall-fragmentation regime flip, the retreat arc, break-side rules, swordfish switch-on, grunion override, and names what the KB lacks. specific: volume square, 70–72°F bank-edge split, 71.6°F paddy, 30–50 fm / 50–80 fm / 240–360 ft bluefin bands with a 250 g jig floor, 150–350 fm sword ground, 15 kt / 2.5 kt gates, hoop-net depths 20–55 ft. sourced: every load-bearing claim carries a note path plus video id, and it distinguishes which id actually supports which sentence. scoped: lobster and rockfish both carry California/CDFW + as-of 2026-08 + verify-current, and the 7/day bag is explicitly marked as resting on one garbled source. honest: uniquely flags the '100% temp chart' quote as spliced across non-adjacent passages, marks Tanner/Cortez condensation and the dolphin-pod window as single-source, admits null boat envelope, longest and most concrete gap list. actionable: full swordfish go/no-go, three bluefin presentations with jig weights and line classes, calico plan B, lobster program — an angler can rig from it, though it correctly stops short of naming zones without a range envelope.

<details><summary>Full prompt</summary>

What changes in the Southern California Bight from September into October, and how should my fishing change with it?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## Short version

September and October are **two different water regimes**, and that is the change that drives everything else. September is the tail of **warm stable** — an established warm band, fish dispersed, the volume square holding grade. October is **fall fragmentation** — the coast cools, the warm band breaks up into sharp edges, and the fishery goes wide but thin (`conditions/water-regimes.md`, cameron; `seasonal/september.md`, `seasonal/october.md`).

So the plan changes from *"go to the zone that's been holding fish"* to *"read the chart, find the edge, pick the correct side of it for your target."*

**Note up front:** you gave me no conditions and I have no BightSST pull, so everything below is the **prior layer only**. Step 1 of `planning/day-plan-protocol.md` — per-spot SST + chlorophyll and wind/swell/current, observed *and* forecast, per zone and along the transit route — still has to be run before any of this becomes a plan. The month notes are explicit: "these are priors, not current intel. A stale report is not today's water."

---

## 1. What actually changes in the water

**September (late warm stable)** — `seasonal/september.md` (`5to3Q5P7w90`):
- The **volume square — Santa Barbara Island – San Nicolas – Clemente – Catalina** — holds the **bigger bluefin**. That block of water is the September grade prior.
- **Dorado in open-water schools below Catalina** — not on structure.
- **Yellowfin volume near the border slides north with the warm water, and the bluefin slide with them.** Follow the temperature, not last week's spot.
- Two September-specific softeners: bluefin were observed **foaming in 76 °F** water (9/14/22) — treat warm SST as **soft evidence against bluefin, not a hard exclusion** (`conditions/water-temperature.md`); and **hurricane remnants are usually a non-event** that knocks the heat down with the fishing unaffected.

**October (fall fragmentation)** — `seasonal/october.md` (`XLVUhV8DW64`, `OYOda6T3f-8`):
- **The chart runs the plan.** Verbatim from the 10/12 and 10/20/22 reports: "conditions become pretty important… look **100 % at your temp chart and chlorophyll**." More than any other month.
- **Breaks reappear and the break-side rule decides the zone**, per species (below).
- **The warm band tracks a repeatable retreat path:** backside **Santa Cruz / Rosa → Santa Barbara Island → backside Catalina → hooking to the 499 / Clemente**. As the coast cools and fragments, **the bluefin condense outward to Tanner and Cortez** (`locations/bight-geography.md`, `HzE4FHHcvTk`).
- **"Everything season" — but scattered.** Marlin, first swordfish, bluefin, yellowfin and dorado are all on the table at once, with **low density of any one**. Breadth up, concentration down.
- Inshore gets a new override: **grunion-in-kelp events beat water quality entirely** — every-cast bass in ugly, stagnant water you'd normally skip (10/20/22).

---

## 2. How your planning routine should change

**Lead with the two-axis chart read, not the spot list.** From `conditions/water-temperature.md`: find the **breaks** (sharp SST gradients — late-fall edges can jump multiple degrees in ~1 mi; an 11/23/22 example off SCI was **63 → 61.5 °F in ~1 mi**), then pick the side per species:
- **Bluefin — relative, not absolute:** cool side of the break when the surrounding water is warm; warm side when the water is cold.
- **Yellowfin — warmest × cleanest:** SST **max** crossed with chlorophyll **min**.
- **Dorado — the boundary:** the green-cold / blue-warm coastal seam, reference band **~71–72 °F** (71.6 °F on a productive paddy, `E4vKwRaRueA`).

**Age your chlorophyll.** `conditions/water-color.md`: a new cold bloom (overnight **~5 °F drop** + green after an afternoon NW wind) is a local upwelling event — **bad now, productive later; mark it for the recovery**. Fish the **edge of a mature bloom**. And don't default to the prettiest blue: bait holds in the **dirtier** water, predators work the dirty/clean seam (8/17/22, `HzE4FHHcvTk`). Cameron's warm-year addendum: weight color at least as heavily as SST, and don't fish dirty green water for gamefish.

**Search the band's path, not last week's pin.** `planning/report-reading-and-forecasting.md`: open-water bluefin not holding structure move **10–15 nm overnight** and low single-digit mph intraday, so draw a box sized by report age, not a pin. **Absence of reports = coverage bias, not absence of fish** (10/12, 10/26/22) — this bites hardest late-season and post-moon, exactly the October condition.

**The anniversary prior is at its strongest now — with a caveat.** "Go back to this date last year and the year before — pretty close to where they'll be," **strongest in fall** (`seasonal/year-anniversary-prior.md`, `XLVUhV8DW64`). Duane's version: line up recent catch positions and **project the travel line**. Kept side by side, unreconciled: Cameron holds the calendar is an artifact — water state is what recurs; if the water is early or late this year, so are the fish. Use the anniversary as a **starting box within the regime**, then let live water override it.

**Moon discipline stays the same but matters more, because density is lower.** `conditions/moon.md`: full/new **±1 week** elevated, **leading days into the full strongest** for bluefin; Hansen's dissent (7 days before *and* after, moon peak itself being travel, not bite) is kept beside it. After a moon, **schools relocate 10–15 nm (Hansen says 20 mi)** — discount report persistence and widen the box rather than concluding the fish are gone. After the October full moon in 2022 "the tuna are gone" was explicitly a coverage illusion.

---

## 3. Species by species — what to keep, add, and change

### Bluefin — stop anchoring on the volume square, start anchoring on the edge
The September geography (SBI–Nick–Clemente–Cat for grade) gives way to the fragmentation geography: break-side selection first, then the **outward condensation toward Tanner/Cortez** as the coast cools (`species/bluefin-tuna.md`). Techniques don't change, the *selection* does:
- **Foamers, terns working, castable seas:** poppers first (they hold the zone longest), then surface iron, then a small lead bait — run ahead of the school, stop hard, cast to the middle. Beefed **jig-stick class**. Bite comes on the **pause/fall**, not the pop.
- **Sounded deep, wind up, no surface sign (30–50 fm):** knife-jig graded marks. **100–130 lb braid jig class (PE6–8)**, jigs **150–300 g** by day, **300–400 g** in more current or deeper.
- **Big fish 100–300 lb, wind 8–15 kt:** kite a flying fish — *the* most effective method in that grade. **150–200 lb class.**
- **Too light to kite, or fish too spread out to sit over** — the classic October problem: **speed-troll a Mad Mac at 13–15 kt** to cover water and locate (a coverage need, not a sea-state call — cameron). A documented late-October 2021 Tanner Bank program was exactly this: spreader bars to cover ground, then stop and set a dead flying fish under the kite once the sounder marks numbers (`species/bluefin-trolling.md`, `vCskOx6N-XM`).
- **200 lb bite-leader class** on everything deep — described as the most critical part of the setup.
- Warning worth carrying into October: on 2025-10-06 NE of Santa Barbara Island, foamers all around the boat converted on **nothing** — trolled spreader bar and cast plugs both scoreless — because the fish were locked on **tiny saury/anchovy/microbait**; a dead flying fish under the kite is what converted (`mDmbGdQAy-4`, medium confidence).

### Yellowfin — chase the warmest, cleanest cell, and it shifts south-inside
`species/yellowfin-tuna.md`: once fragmentation sets in, the biggest concentrations track the warmest water on the coast — **the West End of Clemente down through Mackerel Bank to the 181/182 Ridge** (10/20/22). Flyline a live sardine, **30 lb class, size 2/0 circle**; if they're reacting to chum but refusing the hook bait, drop to **15–20 lb leader and a size 1 thin-wire circle** and use the bait-net trick (pitch 3–4 freebies with your hook bait mixed in), then work back up to 25–30 lb. Troll **cedar plugs and feathers at ~6–6.5 kt** as a *search* tool, then convert the stop with bait. A surface yellowfin bite can fire the bluefin.

### Dorado — the paddy program keeps producing, but the geography moves
September has them in **open-water schools below/backside Catalina**; October keeps the **paddy** program alive — a paddy "as big as the boat" held hundreds of dorado plus incidental yellowtail on 2022-10-12, and a 2022-10-13 El Dorado trip produced **60-plus dorado in a day** after running *south into warmer water* when an overnight bluefin push went cold (`species/dorado.md`, `VWClGAn2WEw`). That pivot — bluefin cold, run to warmer water and fish paddies — is a documented October plan-B.
Paddy discipline is unchanged and matters more when fish are thin (`conditions/kelp-paddies.md`): fish move paddy-to-paddy **only at night**, so a **dry paddy stays dry all day**. Drive right up to it, look, check the meter for **boomerang arcs at 90–120 ft**, give it **a minute or two**, then move down the **paddy line** (N–S in open water under the uphill current; along the contour near a bank edge). Best paddy water is **south of Catalina/SCI and Dana Point to Oceanside southward**; scarcer and less holding north of Dana Point. For tuna specifically, fish **~100 yd off** the paddy rather than tight to it (`A6DJoXbID4c`).
Gear: **40–60 lb all-day class**, **J-hook not circle** (dorado charge straight ahead and won't set on a circle), 1/0 live-bait up to 2/0–3/0 on donkey sardines; step leader down **40 → 30 → 20 → 15 lb** on finicky fish, not below ~15 or you get bit off.

### Striped marlin — this is their window, and it's tide-timed
`species/striped-marlin.md`: **fall**, ~September through October, with the tournament fleets out by **mid-September**. They live in the **clear blue water working the seam** where the dirty/bait water meets clean — put the jigs **on the edge where bait meets clear water**. They are **slack-tide biters** ("bluefin come up foaming on a slack tide, marlin bite on a slack tide") — be on your best spot **an hour before the tide change**. Trolling class **60–100 lb**. Fleet tell to save you a run: **outriggers + circling = a tournament fishing marlin, not tuna** (9/14/22).

### Swordfish — a new option that isn't there in September
`species/swordfish.md`: the season is **late September – December, peak October – mid-November**; holdover fish exist year-round but are **not worth the fuel Jan–Aug**. So October is the month this goes from "no" to "prime." Conditions gate it hard: **150–350 fathoms** on contour lines/thumbs/notches/humps (the Ridge, the 9, the 43, the 178, the 302, the 138/182 on break days); you want the **DSL ≥600 ft with bait balls at 100–150 fm** — bait *in* the layer is the trigger, a bare layer means keep moving; **>15 kt = no-go**, comfortable **10–13 kt**, drift **≤ ~2–2.5 kt** (a drift sock extends marginal days). Weight toward **new/full ± flanking weeks** and one big powerful "highway" break over finger rips.

### Yellowtail — becomes a squid/structure game again
`species/yellowtail.md` (10/26/22, `5p6gu14ZC4w`): **SBI / Sutil** fish as a squid-driven zone in the fall fragmentation window — "take a squid to any of these islands you'll probably have a good chance"; when the squid drops deep or moves, **the bite dies but the fish did not leave** — relocate the forage on the meter before writing the zone off, and a **squid-colored jig with glow** is the change-up. **Catalina** held **~40 yellows in a day in late October**, and **Farnsworth Bank** gives good **fall yo-yo fishing** — note it sits in a marine closure where **only yellowtail and bonito may be kept** (regulation, verify current CDFW rules before you go).
Technique by mark: surface iron on boils/paddy fish; **yo-yo iron or dropper loop** on tight balls hugging structure (**arcs at ~5–10 fathoms** near hard bottom) — heavy full-size iron, Salas 6X class, hit bottom then **a couple cranks off the bottom = reaction bite**, on a stout **40–60 lb class** rod with a high-speed reel. Cameron's rig-three-outfits doctrine (surface iron, heavy yo-yo/dropper, flyline, all rigged at once, switch as temp + bait depth changes) is exactly right for a scattered month.

### Inshore — October's own bite, and it ignores your water read
`species/calico-bass.md` + `seasonal/october.md` (`OYOda6T3f-8`): when grunion pile into the kelp you get **every-cast bass in ugly, stagnant water**. Match the bait — a **7" split-tail slug on a sled/leadhead**, every cast. The tell is a **mixed bird pile *on* kelp/structure** — normally mixed piles at open-water current breaks are bait only and get skipped, but **on structure they're the exception worth checking** (`conditions/bird-reading.md`). Otherwise the parallel-current rule still governs: current **parallel** to shore is good, **into** the beach marginal, **off** the beach dead — with a real late-fall exception coming (11/23/22 at San Clemente Island the bass bite *required* current running **into** the island with off-color water), so from late October on, don't reject into-the-island current at SCI. **Bonito** persist later than most nearshore species and are a common line in the Oct–Nov island reports (`species/bonito.md`).

### Two calendar items that open in October
- **Spiny lobster:** the recreational season runs roughly **early October through mid-March** (regulation — confirm the exact opener with CDFW). Night fishery, **darkest no-moon nights best**, drop **on the rock, not off it in sand**; rope roughly **40–50 ft**, though Catalina work at **20–30 ft** is documented — and early in the season, spread nets across depths rather than committing to one band (`species/california-spiny-lobster.md`).
- **Rockfish/lingcod:** not October's target yet, but October is when you start watching for it. The **lings-shallow window is late fall (Nov–Dec)**, triggered by **Santa Ana events flattening Rosa/Miguel** — and the rockfish season **closes year-end** (California/CDFW, verify current dates and depth limits). The go/no-go rule: **2+ consecutive days of no-wind or Santa Anas** before committing to a Rosa/Miguel crossing (`species/rockfish-lingcod.md`, `conditions/sea-state.md`, `Z3rZqy2Pi8E`).

---

## 4. The one-paragraph operational change

In September you can plan off geography — go to the volume square for grade, work paddies, follow the warm water north with the yellowfin. In October you plan off the **chart**: pull SST and chlorophyll first, find the sharpest edge along the **Rosa/Cruz → SBI → backside Catalina → 499/Clemente** arc, put bluefin on the cool side (warm water) or warm side (cold water), put yellowfin on the warmest × cleanest cell, put dorado on the ~71–72 °F green/blue seam, time marlin and foamer shots to **slack**, and accept that you're buying **breadth instead of density** — carry more rigged outfits and plan more looking, because the fish that were stacked in one square in September are now spread along a moving, fragmenting edge and condensing outward toward Tanner and Cortez.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/report-reading-and-forecasting.md`, `seasonal/september.md`, `seasonal/october.md`, `seasonal/august.md`, `seasonal/november-december.md`, `seasonal/year-anniversary-prior.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/current-structure.md`, `conditions/kelp-paddies.md`, `conditions/moon.md`, `conditions/bird-reading.md`, `conditions/sea-state.md`, `locations/bight-geography.md`, `species/bluefin-tuna.md`, `species/bluefin-trolling.md`, `species/yellowfin-tuna.md`, `species/dorado.md`, `species/striped-marlin.md`, `species/swordfish.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/white-seabass.md`, `species/bonito.md`, `species/barracuda.md`, `species/rockfish-lingcod.md`, `species/california-spiny-lobster.md`, `species/spotted-bay-bass.md`, `species/README.md`  
*videos:* `5to3Q5P7w90`, `XLVUhV8DW64`, `OYOda6T3f-8`, `5p6gu14ZC4w`, `HzE4FHHcvTk`, `Z3rZqy2Pi8E`, `Blh2BA-7Ono`, `6TBxHnkYXI0`, `YZtX1MiT0y8`, `E4vKwRaRueA`, `ZFqe49jRgA0`, `4xzK7YaXK5s`, `VWClGAn2WEw`, `e73wPONTOJU`, `mDmbGdQAy-4`, `vCskOx6N-XM`, `A6DJoXbID4c`, `yMiBtZ7k8-w`, `KuVwmfF6RAo`, `HWx1jDTGsng`, `D5DR7Kx42_A`, `b19_AJjYCok`, `fri_BWI-VA0`, `YQsbwfQ4wzY`, `Ow3an9lSVh4`, `6-8KfjEg0x8`, `zKmZ4zql2ws`, `h3PTupup17I`  
*gaps admitted:* No live conditions were supplied and no BightSST pull was made, so step 1 of the day-plan protocol (per-spot SST/chlorophyll, wind/swell/current, observed and forecast) is undone — everything above is the prior layer only. | The KB carries no calendar: no 2026 moon phase dates and no tide/slack times, so the moon and slack-tide windows above cannot be resolved to actual dates here. | The KB gives no explicit departure timing for yellowfin or dorado from the Bight — they are carried through 'Sep–Oct' fall fragmentation, and the Nov–Dec note does not mention them at all, so when they actually thin out is not covered. | No albacore seasonal pattern exists in the KB (albacore appear only in a moon-relocation aside and one sliding-sinker trip entry), so any fall albacore question is uncovered. | No October-specific white seabass pattern: the KB links WSB to October only through the moon layer, and frames the squid driver as spring through summer. | Striped marlin bait-and-switch execution is an explicit flagged stub in the KB — no corpus source for the pitch mechanics. | Yellowfin trolling spread geometry (setback distances, lure positions in the pattern) is flagged thin in the KB — only troll speeds are sourced. | Exact CDFW dates are not in the KB: the lobster opener/closer, the year-end rockfish closure date, and depth limits all carry verify-current flags rather than dates. | There is no October-specific yellowtail program for the SoCal Bight beyond the SBI/Sutil squid zone, Catalina, and Farnsworth mentions — the October-heavy yellowtail observations in the KB are Cedros Island, Baja, a different region. | Nothing in the KB describes how bays and harbors change from September into October specifically — spotted bay bass and the bay fishery are framed as year-round with a winter/blown-out-coast fallback.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

# September → October in the Bight: the regime flips

Two caveats up front, both required by this KB's own protocol
([`planning/day-plan-protocol.md`](planning/day-plan-protocol.md)):

1. **This is the prior layer only.** Every month note in `seasonal/` opens with the
   same warning — *"These are priors — the pattern layer, not current intel… a stale
   report is not today's water."* I have no BightSST access in this session, so I
   have pulled **no live SST, chlorophyll, wind, swell or current**. Everything below
   is what the calendar *usually* means; the chart overrides it.
2. **I don't have your envelope.** Protocol step 1b says to set `{regions, waters}`
   from your launch point and boat range **before** opening any species note, and
   that filter is binding. You haven't told me your boat, range, sea-state limit or
   home port, so gear below is in **class terms** per
   [`tackle/gear-classes.md`](tackle/gear-classes.md), and I've held everything to
   `regions: socal-bight`.

---

## 1. The single biggest change: a regime boundary, not a month boundary

Per [`conditions/water-regimes.md`](conditions/water-regimes.md) (Cameron house
doctrine), the Bight's year is **four water-state regimes, not twelve months**.
September and October sit on opposite sides of a boundary:

| | September | October |
|---|---|---|
| Regime | **Warm stable (late)** ([`seasonal/september.md`](seasonal/september.md)) | **Fall fragmentation** ([`seasonal/october.md`](seasonal/october.md)) |
| Water state | An established warm band of clean water over the Bight; conditions hold day to day; the paddy field is seeded and holding | The coast cools and the warm band **fragments** — sharp SST breaks and edges reappear, and the warm water tracks a retreat path and **condenses** offshore |
| How you plan | Weight a block of water and go fish it | **The chart runs the plan** |
| Density | Volume, concentrated | **Everything season, but scattered** — breadth of species, low density of any one |

The operative quote, from the October note and repeated in
[`conditions/water-temperature.md`](conditions/water-temperature.md): *"conditions
become pretty important… look **100 % at your temp chart and chlorophyll**"*
(10/12, 10/20/22 reports — October note sources `XLVUhV8DW64`, `OYOda6T3f-8`,
`5to3Q5P7w90`).

**And the regime layer's own anomaly rule applies:** if this year's water is running
early or late, *plan from the regime you can see on the chart, not the month note.*
The calendar flipping to October does not by itself mean fragmentation has arrived.

---

## 2. What physically changes

### The geography moves, and it moves along a known path

- **September's geography is a box.** The **"volume square" — Santa Barbara Island –
  San Nicolas – San Clemente – Catalina — holds the bigger bluefin**
  ([`seasonal/september.md`](seasonal/september.md);
  [`locations/zone-lexicon.md`](locations/zone-lexicon.md) calls it a *region to work
  through, not a point*). Yellowfin volume near the border **slides north with the
  warm water, and the bluefin slide with them** — follow the temperature, not last
  week's spot.
- **October's geography is a band in motion.** Per
  [`locations/bight-geography.md`](locations/bight-geography.md) (`HzE4FHHcvTk`) and
  the October note, the warm band tracks a repeatable sequence:

  > **backside Santa Cruz / Rosa → Santa Barbara Island → backside Catalina →
  > hooking to the 499 / Clemente.**

  And as the coast cools and fragments, **the bluefin condense outward to Tanner and
  Cortez.**

So the change in method is concrete: **in September you can weight a block of water;
in October you follow an edge along an arc, and you expect the terminal condensation
onto the outer banks.**

### Breaks come back, and which side matters

In a stable warm regime the whole Bight is warm and clean. In fragmentation, **edges
reappear**, and per [`conditions/water-temperature.md`](conditions/water-temperature.md)
the value is *not the absolute number but which side of a break a species sits on*:

- **Bluefin — relative, not absolute.** Cool side of a break when surrounding water
  is warm; warm side when the water is cold (10/20/22).
- **Yellowfin — warmest × cleanest.** SST **max** × chlorophyll **min**. In October
  specifically, per [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md), the
  biggest concentrations track the warmest water on the coast — **the West End of
  Clemente down through Mackerel Bank to the 181/182 Ridge** (10/20/22).
- **Dorado — the boundary.** Green-cold / blue-warm coastal boundary, reference band
  **~71–72 °F** (71.6 °F on a productive paddy, `E4vKwRaRueA`;
  [`species/dorado.md`](species/dorado.md)). Fish the boundary line, not the middle
  of either mass.

Two chlorophyll disciplines that get more load-bearing in October, from
[`conditions/water-color.md`](conditions/water-color.md):

- **Chlorophyll has an age.** A **new cold bloom** (overnight ~5 °F drop + green
  after an afternoon NW wind) is a local upwelling event — bad *now*, productive
  later. Mark it for the recovery. Fish the **edge of a mature bloom** instead.
- **Cameron's doctrine:** in warm-water years he weights chlorophyll/color **at least
  as heavily as SST** and **will not fish "dirty green" water for gamefish**.

### The species roster broadens and thins at the same time

October is an **everything season** — marlin, first swordfish, bluefin, yellowfin,
dorado all on the table, **all scattered** ([`seasonal/october.md`](seasonal/october.md)).
Practically:

- **Swordfish switch on.** [`species/swordfish.md`](species/swordfish.md): season is
  the fall fragmentation regime, **late September – December, peak October –
  mid-November**. Holdover fish exist year-round but are *"generally not worth the
  fuel Jan–Aug."* October is the month a dedicated deep-drop day starts paying.
- **Marlin peak into it.** [`species/striped-marlin.md`](species/striped-marlin.md):
  a **fall** sight-and-troll fishery running ~September through October; tournament
  marlin fleets are out by mid-September (`5to3Q5P7w90`).
- **Bluefin grade holds, then falls off a cliff — later.**
  [`seasonal/november-december.md`](seasonal/november-december.md): Tanner/Cortez
  bluefin go **night-dominant with 300 lb fish through November**, then revert to the
  **sub-30 lb winter grade by mid-December**. October is your window before that.
- **Lobster opens.** [`species/california-spiny-lobster.md`](species/california-spiny-lobster.md):
  the recreational spiny lobster season runs roughly **early October through
  mid-March** — a genuine September→October change, and one set by **regulation, not
  water state**.

### What *stops* mattering from September

Two September-specific reads you can retire:

- **The 76 °F bluefin ceiling was already soft.** Bluefin were observed **foaming in
  76 °F water** (9/14/22) — treat warm SST as *soft* evidence against bluefin, never a
  hard exclusion. As the water cools this stops being a live question.
- **Hurricane remnants are usually a non-event** (9/14/22) — they break the heat with
  the fishing unaffected. Don't over-plan around a tropical system tracking up the
  Baja coast in September.

---

## 3. How your fishing should actually change

### A. Change how you build the plan

**September:** pick the volume square, run to it, work it.
**October:** open the temp/chlorophyll chart *first*, find the break, and let it name
the spot. [`conditions/water-temperature.md`](conditions/water-temperature.md)'s
planning steps: (1) pull SST per spot and along the route, observed and forecast;
(2) find the **breaks**, not just the warmest cell — sharp offshore edges can jump
multiple degrees in ~1 mi; (3) pick the **side** per species and cross it with
chlorophyll — never SST alone.

Budget your time to the box, per [`locations/zone-lexicon.md`](locations/zone-lexicon.md):
the **below-Clemente complex (43, 181, 182, 289, Clemente Ridge up to Mackerel Bank)
is one ~50–60 square-mile search box** — hours of looking, not a spot-check. Compact
spots (302, 371, west-of-Catalina) are a 20–30 minute read.

### B. Trust reports less, and read their absence correctly

From [`planning/report-reading-and-forecasting.md`](planning/report-reading-and-forecasting.md):

- **Open-water bluefin not holding structure move 10–15 nm overnight** (7/21/22). A
  gray-light plan on yesterday's numbers is already 10–15 nm stale. Draw a **box**
  sized by report age, not a pin.
- **Intraday they move at low single-digit mph** (8/17/22) — the pop-up you marked at
  8 a.m. isn't at that GPS point at noon.
- **Late-season, "absence of reports = coverage bias," not absence of fish**
  (10/12, 10/26/22).

And lean harder on the **year-anniversary prior**
([`seasonal/year-anniversary-prior.md`](seasonal/year-anniversary-prior.md),
`XLVUhV8DW64`): *"go back to this date last year and the year before — pretty close
to where they'll be."* It is explicitly **strongest in fall**. Duane Diego Mellor's
version: line up prior days' catch positions and **project the travel line** forward.
Kept side by side, unreconciled, is **Cameron's opposing framing** — for yellowtail
the calendar is an artifact; fish follow water temperature and bait. Treat the
anniversary prior as a *starting box* and let live water override it.

### C. Change what's on the deck

| Situation October brings | Do this | Gear class | Source note |
|---|---|---|---|
| Break found, **bluefin sounded deep (30–50 fm)**, wind up, no surface sign | [Knife-jigging](techniques/knife-jigging.md) to graded marks | 100–130 lb-braid jig class (PE6–8); **day jigs 150–300 g**, more current/deeper → **300–400 g** to punch down and stay horizontal | [`species/bluefin-tuna.md`](species/bluefin-tuna.md) |
| **Surface foamers**, terns working, castable seas | [Foamer casting](techniques/foamer-casting.md) — poppers first, then surface iron, then a small lead bait; run ahead, stop hard, cast to the middle | Beefed jig-stick class | same |
| **Big fish 100–300 lb**, wind **8–15 kt** | [Kite fishing](techniques/kite-fishing.md) a flying fish — *the* most effective method at that grade | 150–200 lb class + flying-fish harness | same |
| Too light to kite, or fish too spread out to sit over | Speed-troll a [Mad Mac](lures/mad-mac.md) at **13–15 kt** to locate | Heavy troll class | same; full table in [`species/bluefin-trolling.md`](species/bluefin-trolling.md) |
| Yellowfin on the warmest × cleanest water, chummed and eager | [Flyline](techniques/flyline.md) a live sardine, circle hook, chum a few freebies first | **30 lb class, 2/0 circle**; picky → **15–20 lb leader, size 1 thin wire** | [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md) |
| Open zone, no visual fish — need to search | Troll cedar plugs / feathers at **~6–6.5 kt**; on the jig strike, stop and convert with flylined bait | Light troll class | same |
| **Marlin** — fall, clean blue water off a bait/color edge, slack tide | Slow-troll lures/skirts on the **clean side of the bait seam**; be on the spot **an hour before the tide change**; [bait-and-switch](techniques/bait-and-switch.md) with a pitched live mackerel on a raised or tailing fish | Trolling class 60–100 lb; pitch rod rigged and ready the whole troll | [`species/striped-marlin.md`](species/striped-marlin.md) |
| **Swordfish** — deep contour break | [Daytime deep-drop](techniques/deep-drop-swordfishing.md) | Heavy stand-up 2-speed lever-drag class; **200 lb+ bite leader**, breakaway **7–10.5 lb** lead | [`species/swordfish.md`](species/swordfish.md) |
| **Grunion-in-kelp / bait blitz**, even ugly stagnant water | Match the bait — **7" split-tail slug on a sled/leadhead**, every cast | bass class | [`species/calico-bass.md`](species/calico-bass.md) |
| Fall yellowtail at Catalina | [Yo-yo iron](techniques/yo-yo-iron.md) on hard bottom | 40–60 lb class stout rod + high-speed reel | [`species/yellowtail.md`](species/yellowtail.md) |

**Swordfish go/no-go numbers** (all SoCal Bight, from
[`species/swordfish.md`](species/swordfish.md), sources `yMiBtZ7k8-w`, `KuVwmfF6RAo`,
`cameron`) — worth memorizing because October is when they start applying:

- **Depth:** 150–350 fathoms on contour lines, thumbs, notches, humps. Named working
  spots: the Ridge, the 9, the 43, the 178, the 302, the 138/182 area on break days.
- **Before you stop:** DSL present at **≥ 600 ft** — preferred **~950 ft / 150
  fathoms or deeper** — **plus chunky bait balls** (anchovy/hake/squid) at **100–150+
  fathoms** ≈ bites near-assured. **A bare layer with no bait is not a stop.**
- **Fishable day:** **>15 kt = no-go**; comfortable **10–13 kt**; drift **≤ ~2–2.5
  kt** (a drift sock extends marginal days).
- **Water:** prefer **one big powerful "highway" break** over finger rips. Structure ×
  current-edge intersection = the banger days.
- **Moon:** bites rise on **new and full and the flanking weeks**.

### D. Don't neglect the inside — October gives it back

This is the counterintuitive one. From [`seasonal/october.md`](seasonal/october.md):
**grunion-in-kelp events override water quality entirely** (10/20/22). A grunion
blitz produces **every-cast bass in ugly, stagnant water** — water you'd normally
skip. **A bait event on structure beats a clean-water read.**

The tell is in [`conditions/bird-reading.md`](conditions/bird-reading.md): a **mixed
pile** (gulls + pelicans + terns + cormorants) at an **open-water current break** is
bait only — skip it. But a mixed pile **on kelp/structure** can be a real bait event
worth a look. Same birds, opposite call, decided by what they're sitting on.

Also on the inside:

- **Calico** stay in play — [`species/calico-bass.md`](species/calico-bass.md) notes
  the fall fragmentation transitional months (October into December) *"can pull
  another degree of warmth out of stable water."*
- **Bonito persist later than most nearshore species** — *"doing good on the bonito"*
  is a common line in fall fragmentation island reports
  ([`species/bonito.md`](species/bonito.md)).
- **Yellowtail at Catalina:** ~**40 yellows in a day at Catalina in late October**,
  and *"no reason you couldn't catch a yellowtail"* while temps stay good, even
  outside prime time (10/26/22, `5p6gu14ZC4w`). **Farnsworth Bank** gives good **fall
  yo-yo fishing** — note it sits in a marine closure where **only yellowtail and
  bonito may be kept** ([`species/yellowtail.md`](species/yellowtail.md)).
- **Paddies aren't done.** The program peaked in August
  ([`conditions/kelp-paddies.md`](conditions/kelp-paddies.md)), but
  [`species/dorado.md`](species/dorado.md) logs an oversized paddy holding **hundreds
  of dorado plus incidental yellowtail well into October** (Your Saltwater Guide /
  Dave Hansen, 2022-10-12). Best paddy water remains **south of SCI/Catalina and
  Dana Point to Oceanside southward**; paddies are scarcer and hold fewer fish north
  of Dana Point.

### E. Add a boat job that didn't exist in September: hoop nets

[`species/california-spiny-lobster.md`](species/california-spiny-lobster.md)
(`b19_AJjYCok`, `JiJYamo0QHk`, `YQsbwfQ4wzY`, `fri_BWI-VA0`, `Ow3an9lSVh4`):

- **Season roughly early October – mid-March.** Set by regulation, not water state.
- **Night only** — lobster crawl and feed after dark; buoys carry LED lights.
- **Moon:** favor the **darkest, no-moon nights**, including rough/rainy dark ones.
  This is the *inverse* of the pelagic/bass moon doctrine, and it's a lean, not a
  shutout — the same source has caught them on full moons.
- **Where:** drop **on the rock, not off it in open sand** — riprap, boulder fields,
  reef, kelp edges, bays and harbors. Rope length ~40–50 ft in the general case, but
  Catalina work has been at **20 ft and 30 ft** — **spread nets across depths** early
  in the season rather than committing to one band.
- **Regulatory claim — California / CDFW, as of 2026-08, verify current rules before
  you fish:** bag **7 lobster per person per day**; **fishing license *plus* lobster
  report card**, card filled out *before* you fish (gear code **1** for hoop netting);
  **5 nets per angler from a boat, max 10 nets per boat**, 2 per person from shore.
  Confirm the exact opener with CDFW for this year.

### F. Start watching for Santa Anas

[`conditions/sea-state.md`](conditions/sea-state.md) logs the Santa Ana rule against
both 10/20/22 and 11/23/22: **Santa Ana events flatten the NW outer islands** and are
*the* trigger to run **Santa Rosa / San Miguel** for shallow rockfish and lings. The
go/no-go rule from the 11/23/22 report (`Z3rZqy2Pi8E`) is **2+ consecutive days of
no-wind or Santa Anas** before committing to that crossing.

The paired danger (dave-hansen, `NC3-3pJDEgo`, 2020-11-18 — medium confidence,
single mention): a Santa Ana is an offshore-blowing **NE** wind that pushes water
*out* against the prevailing onshore motion, stacking large fast-building swell. Wind
at Avalon during an active event ran **25–45 kt**. An outbound downwind run to
Catalina can feel fine and leave you with a multi-hour beat home into it. That
source frames Santa Anas as running from roughly mid-November through Thanksgiving in
a typical year, so this is more a November read than an October one — but the
October report is already citing the northern-islands window.

### G. One thing that changes *after* October — know it's coming

[`conditions/current-structure.md`](conditions/current-structure.md)'s parallel-current
rule (parallel = good, into the beach = marginal, off the beach = dead) picks up a
**late-fall exception**: at San Clemente Island on 11/23/22 the bass bite **required
current running *into* the island with off-color water** — fish used the dirt to
ambush against structure. Encode **parallel as the prior, into-beach as a viable
late-fall / off-color state, off-beach as dead.** In late fall, don't reject
into-the-island current at SCI.

---

## 4. If I had to compress it to five lines

1. **Stop planning by spot name and start planning by chart** — temp break plus
   chlorophyll, then pick the *side* of the edge per species.
2. **Follow the band** — backside Santa Cruz/Rosa → SBI → backside Catalina → the
   499/Clemente — and expect bluefin to **condense outward to Tanner and Cortez**.
3. **Widen your net on species and narrow your expectation on density** — marlin,
   first swords, bluefin, yellowfin, dorado all in play, all scattered.
4. **Age every report by miles** (10–15 nm overnight for open-water bluefin) and read
   report silence as coverage bias, not dead fish.
5. **Keep the inside program alive** — a grunion-in-kelp blitz beats a clean-water
   read outright, and hoop nets go on the boat once the lobster opener lands.

---

## What this KB does *not* answer

- No live conditions were pulled — everything above is the prior layer.
- No profile/envelope was set, so gear is class terms only.
- The KB gives no numeric threshold that says "fragmentation has begun" — the regime
  is read qualitatively off the chart.
- The KB gives no way to predict *when* an October grunion event will happen — only
  what to do when one is in front of you.
- No October moon/tide dates here; those need a separate pull.
- Sight-fishing a finning/sunning swordfish is a **flagged stub — no corpus source
  yet** ([`species/swordfish.md`](species/swordfish.md)).
- Yellowfin **troll spread geometry** (setback distances, lure positions) is flagged
  as a thin area — the corpus gives speeds only.
- There is **no crisp "deploy the marlin gear now" water-condition trigger** in the
  corpus — [`species/striped-marlin.md`](species/striped-marlin.md) records that as
  Cameron's open research question.
- Nothing on how bait-receiver supply (sardine/mackerel availability) shifts from
  September into October.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/report-reading-and-forecasting.md`, `seasonal/README.md`, `seasonal/september.md`, `seasonal/october.md`, `seasonal/august.md`, `seasonal/november-december.md`, `seasonal/year-anniversary-prior.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/current-structure.md`, `conditions/bird-reading.md`, `conditions/sea-state.md`, `conditions/kelp-paddies.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/dorado.md`, `species/striped-marlin.md`, `species/swordfish.md`, `species/calico-bass.md`, `species/white-seabass.md`, `species/bonito.md`, `species/yellowtail.md`, `species/california-spiny-lobster.md`, `species/rockfish-lingcod.md`  
*videos:* `5to3Q5P7w90`, `XLVUhV8DW64`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `E4vKwRaRueA`, `5p6gu14ZC4w`, `yMiBtZ7k8-w`, `KuVwmfF6RAo`, `6TBxHnkYXI0`, `Z3rZqy2Pi8E`, `5D1vx29LVpI`, `xzIaUEDklrE`, `NC3-3pJDEgo`, `b19_AJjYCok`, `JiJYamo0QHk`, `YQsbwfQ4wzY`, `fri_BWI-VA0`, `Ow3an9lSVh4`, `i3qIAHW-SJc`  
*gaps admitted:* No live BightSST conditions were pulled in this session (no network/BightSST access), so the answer is the prior/pattern layer only — the KB itself states priors are not current intel. | No angler profile or trip envelope was supplied (boat, range_nm, sea_state_max_ft, home port, rod inventory), so protocol step 1b could not be executed and all gear is given in class terms rather than owned gear. | The KB gives no numeric threshold or trigger that declares the fall-fragmentation regime has arrived — the regime is read qualitatively from the temp/chlorophyll chart, so the September/October boundary cannot be pinned to a date or an SST value. | The KB gives no way to predict when an October grunion-in-kelp event will occur — only the doctrine that such an event overrides water quality once you find one. | No October moon phases or tide/slack times are in the KB; timing windows (slack-tide marlin, new/full-moon swordfish, dark-moon lobster) need a separate almanac pull. | Sight-fishing a finning or sunning swordfish is an explicit flagged stub in species/swordfish.md — approach, bait and cast have no corpus source. | Yellowfin trolling spread geometry (setback distances, lure positions in the pattern) is flagged as a thin area — the corpus gives troll speeds only. | There is no crisp water-condition trigger in the corpus for when to deploy marlin gear; species/striped-marlin.md records this as Cameron's open research question. | Nothing in the KB covers how live-bait receiver supply (sardine/mackerel availability and quality) changes from September into October. | The exact CDFW spiny-lobster opener date for the current year is not in the KB — the note gives only 'roughly early October' and instructs verifying with CDFW. | The KB does not cover whether or how the September paddy/dorado program's decline rate through October can be forecast — only isolated observations that paddies still produced into October in 2022.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

## Short version

September and October are two different **water regimes**, not two months. September is the tail of **warm-stable**; October is **fall fragmentation** (`conditions/water-regimes.md`, `seasonal/september.md`, `seasonal/october.md`). In September you can plan on a *place* — the volume square. In October you have to plan on a *chart*: the warm band breaks up, sharp SST breaks and edges reappear, the band walks a repeatable retreat path and condenses offshore, and species sort themselves onto specific sides of those edges. Density drops, breadth goes up.

Everything below is the **prior layer only**. You gave me no conditions, so I pulled none — before any of this becomes a plan, run step 1 of `planning/day-plan-protocol.md` (BightSST SST + chlorophyll + wind/swell/current, observed and forecast, per zone and along the transit route, endpoints in `config/endpoints.md`).

---

## 1. What actually changes

**The planning input flips from location to chart.** October is called out as the regime change where "conditions become pretty important… look 100 % at your temp chart and chlorophyll," and the instruction is to build the plan on the break structure, not on spot names (`seasonal/october.md`, `conditions/water-temperature.md`, `OYOda6T3f-8`). Fair warning: the KB flags that quote — it is spliced from two non-adjacent passages in `OYOda6T3f-8` and is not in `XLVUhV8DW64` at all. The direction of the doctrine is well supported; the "100 %" phrasing is not a clean single quote.

**The geography moves along a stated arc.** September weights the **volume square — Santa Barbara Island – San Nicolas – Clemente – Catalina — which holds the bigger bluefin** (`seasonal/september.md`, `5to3Q5P7w90`). In October the warm band tracks **backside Santa Cruz/Rosa → SBI → backside Catalina → hooking to the 499/Clemente → the west end of Clemente through the macro bank and the 181/182 ridge down to the corner**, and as the coast cools and fragments the bluefin **condense outward toward Tanner and Cortez**, working the zone between the **381** (east end, backside Clemente) and Tanner/Cortez on the *cooler side* of the same band (`locations/bight-geography.md`, `seasonal/october.md`, `OYOda6T3f-8`). The KB flags this path and the Tanner/Cortez condensation as resting on `OYOda6T3f-8` alone.

**Break-side rules replace "find the warmest cell."**
- **Bluefin — relative, not absolute:** cool side of a break when the surrounding water is warm; warm side when it is cold (`conditions/water-temperature.md`, `OYOda6T3f-8`). A bank-edge trip matched it: bluefin in the cooler **70–72 °F** at a bank edge, yellowtail and yellowfin in the warmer water nearby (`i3qIAHW-SJc`).
- **Yellowfin — SST max × chlorophyll min**, the warmest *and* cleanest combination (`species/yellowfin-tuna.md`, `OYOda6T3f-8`).
- **Dorado — the boundary itself:** green-cold beach water against blue-warm offshore, reference ~**71–72 °F**, with **71.6 °F** measured on a productive paddy (`species/dorado.md`, `conditions/water-temperature.md`, `E4vKwRaRueA`). The note flags that band as extrapolated from that one reading.
- Don't over-read a warm SST against bluefin: they've been logged foaming in **76 °F**, which softens the ceiling without moving the productive band (`seasonal/september.md`, `species/bluefin-tuna.md`, `5to3Q5P7w90`).

**Density falls, species count rises.** October is an **"everything season" — marlin, first swordfish, bluefin, yellowfin, dorado all on the table, but scattered** (`seasonal/october.md`, `XLVUhV8DW64`). September still has volume: yellowfin volume near the border slides north with the warm water and the bluefin slide with them, and dorado run in open-water schools below Catalina (`seasonal/september.md`, `5to3Q5P7w90`).

**Swordfish switch on.** Same deep-drop program: **August ≈ five trips without a bite; September produces a couple; by October it's a bite a trip if not more** (`species/swordfish.md`, `yMiBtZ7k8-w`). Season is late September into December; 2019 ran hot from mid-to-late September through a red-hot October, 2020 peaked ~10 days before Thanksgiving, last fish of 2019 ~a week before Christmas.

**The inshore game gets a wildcard.** **Grunion-in-kelp events override water quality entirely** — every-cast bass in ugly, stagnant, no-current water you'd normally skip, for a documented two hours (`seasonal/october.md`, `species/calico-bass.md`, `OYOda6T3f-8`). The tell is the mixed bird pile sitting *on* kelp/structure, which is the stated exception to the usual "mixed pile at an open-water current break = bait only, skip" rule (`conditions/bird-reading.md`, `Blh2BA-7Ono`).

**What the zone gives up changes.** Inside Catalina in late October the water still supports yellowtail, but "you're mostly against Bonita, bass and Rockfish this time of year" (`species/bonito.md`, `5p6gu14ZC4w`), and in October sport boats are "doing good on the Bonita" (`OYOda6T3f-8`).

**Fleet reading changes.** Marlin runs mid-August through October, tournament fleets are out by mid-September, and **outriggers + circling = a tournament, not tuna** — don't run to it (`species/striped-marlin.md`, `seasonal/october.md`, `5to3Q5P7w90`).

**Weather posture changes.** In September, hurricane remnants are usually a non-event that breaks the heat with the fishing unaffected — don't over-plan around a tropical system tracking up Baja (`seasonal/september.md`, `5to3Q5P7w90`). In October, storms are expected to break the hot spots up further, and the rule after any significant weather event is **"conditions rolled over — don't rely on your pre-fish"**: re-scout, treat pre-storm intel as expired regardless of age (`planning/report-reading-and-forecasting.md`, `OpcKQPA3vAI`, `OYOda6T3f-8`).

**Regulatory calendar.** The recreational **spiny lobster** season runs roughly **early October through mid-March** (California/CDFW, as of 2026-08 — verify with CDFW; the KB flags that no cited transcript actually names the October opener, only the March close — 2024 closed **March 20**) (`species/california-spiny-lobster.md`, `Q196GVwVqro`, `b19_AJjYCok`). The recreational **rockfish** season is open most of the year and **closes at year-end** (California/CDFW as of 2026-08 — verify), so the bottom season is now on a clock (`species/rockfish-lingcod.md`).

---

## 2. How your fishing should change

### Change the plan order
Stop starting from a spot list. Start from the temp/chlorophyll chart, find the **breaks**, then pick the *side* per species, then pick the spot that sits on that edge (`conditions/water-temperature.md` "how to use it in planning": pull SST per spot and along the route, find the sharp gradients rather than the warmest cell, then combine with `conditions/water-color.md` — never SST alone). Sharp offshore edges can jump multiple degrees in ~1 mi; a documented late-fall example was **63 → 61.5 °F in ~1 mi, 8 mi off San Clemente Island**, with the fish deep on it and sonar-dependent (`seasonal/november-december.md`, `Z3rZqy2Pi8E`, flagged single-source).

### Widen the search box and age your intel harder
- Use the **year-anniversary prior** as the starting box — the bluefin route through fall fragmentation repeats, so "go back to this date last year and the year before" is a usable start, strongest *in this regime* and weakest outside it. Project the travel line from recent positions rather than pinning one same-date point (`seasonal/year-anniversary-prior.md`, `XLVUhV8DW64`; flagged single-source).
- **Advection:** open-water bluefin not holding structure move **10–15 nm overnight**, so a gray-light plan on yesterday's numbers is already 10–15 nm stale — draw a box sized by report age, not a pin (`planning/report-reading-and-forecasting.md`, `Blh2BA-7Ono`).
- **Persistence-null:** late in the season, "absence of reports = coverage bias, not absence of fish." When the fleet thins, you stop *hearing* about water that still holds fish — ask why the zone is quiet before writing it off (`planning/report-reading-and-forecasting.md`, `XLVUhV8DW64`, `5p6gu14ZC4w`).

### Add the swordfish program to the October rotation (if the day allows)
The go/no-go is hard and numeric (`species/swordfish.md`, `techniques/deep-drop-swordfishing.md`, `yMiBtZ7k8-w`):
- **Ground:** deep contour structure **150–350 fathoms** — contour lines, thumbs, notches, humps. Worked ground named in the corpus: the Ridge, 9 Mile, 14 Mile, the 43, the 178, the 302, and the 138/182 on break days. A worked drift at the 178 sat in ~**1,090 ft**, inside the **900–1,400 ft** band (`KuVwmfF6RAo`).
- **Trigger:** DSL ≥600 ft **plus** bait balls at **100–150 fm**. DSL with no bait and no rip = keep moving; bait *in* the layer is the trigger, not the layer.
- **Weather gate:** above **15 kt** nobody fishes; **10–13 kt** is the working max in the traditional NW; above ~**2–2.5 kt** of drift the presentation dies. **13–15 kt or drift >2.5 kt → drift sock**, which also holds the bow into the current.
- **Day selection:** weight new/full moon and the flanking weeks, on the biggest highway break you can find.
- Method is west-coast style: **set up and let the fish come along the fathom-curve highways**.

### Shift the tuna program from "find the volume" to "work the edge, and expect it deeper"
- Bluefin sonar bands to plan around: **sounded schools 30–50 fathoms** with the wind up and no surface sign (`HWx1jDTGsng`); **offshore-bank night marks 50–80 fathoms and below** (`LsFMBCa9DOQ`); night fish at **240–360 ft** set a **250 g or greater** jig floor — 120–150 g will not reach in a wind drift (`eehDVb6_GoI`) (`species/bluefin-tuna.md`).
- Keep the whole kit aboard, because October gives you all three presentations in one day: foamer casting (jig-stick class, and the bite comes on the **pause/fall**), knife/flat-fall jigging to graded marks (**100–130 lb braid jig class**, day jigs 150–300 g, 300–400 g in more current or deeper water), and kite for **100–300 lb** fish in ~**8–15 kt** — that kite wind figure is flagged in the KB as contradicted between notes, so treat it as soft (`species/bluefin-tuna.md`).
- Know where it's heading: by November the Tanner/Cortez fish go **night-dominant**, **60–80 lb with a few 100 lb+**, mostly knife jigs or sinker rigs, with daytime bites mostly stopped, then revert to the **sub-30 lb winter grade by mid-December** (`seasonal/november-december.md`, `Z3rZqy2Pi8E`, `5D1vx29LVpI` — both carry KB fact-check flags on the bank attribution and the grade).
- **Yellowfin:** chase warmest × cleanest. Once fragmentation sets in the concentrations track the **West End of San Clemente Island down through Mackerel Bank to the 181/182 Ridge, with the bigger 50 lb fish off the front side of Clemente** (`species/yellowfin-tuna.md`, `OYOda6T3f-8`) — the note flags "typically October" as the KB's generalization, not the source's words. One dated SoCal fall bite marked by white terns sat over **72 °F** (`SczdZIq3UmE`). The **dolphin-pod program has a named window: "first week of October, end of September," backside Catalina, credited with 60–70 lb fish** (`species/yellowfin-tuna-trolling.md`, `ouBrIdO7d4k`, single-source). Approach geometry: stay outside the pod, get in front of it, never drive through; take the pod carrying its own bird.
- **Dorado:** keep the tackle aboard rather than packing for a known run — abundance swings hard year to year. Fish the **color boundary**, not the middle of either mass; grade a paddy fast and move, because **paddies restock at night**, so a bare paddy at midday is still bare an hour later. SoCal grade **8–15 lb, fish to 30 lb** (`species/dorado.md`, `E4vKwRaRueA`, `P9H-bpzT7eU`).

### Carry an inshore Plan B on every October trip
This is the biggest practical change from September. Because the offshore is scattered, the highest-percentage October day can be a bait event inshore:
- **Grunion or bait blitz in the kelp, even in ugly stagnant water → match the bait: 7" split-tail slug on a sled or leadhead, every cast, bass class.** It overrides the water read entirely, and the birds stay on top of the moving bait (`species/calico-bass.md`, `OYOda6T3f-8`).
- Otherwise the standard calico read still applies: fish the **up-current / leading edge** of the kelp, preference band roughly **65–68 °F**, worked depths off Dana Point **0–8 ft** and **20–100 ft** (`species/calico-bass.md`, `LqW32NSkObY`).
- **Bonito, bass and rockfish are the honest fallback**, not a consolation — that's what the inside-Catalina zone gives up in late October (`species/bonito.md`, `5p6gu14ZC4w`).

### Put lobster and the bottom season on the calendar
If you want bugs, October is the opener (verify with CDFW). Program: baited **hoop nets** after dark on rock/riprap/kelp edge, nets fishing **20–55 ft** with rope matched to sounded depth — Catalina **20–30 ft**, general big-boat **25–30 ft**, Mission Bay **25–35 ft**, San Diego Bay to **55 ft**; **5 nets per angler, 10 per boat**, **3.25 in** carapace minimum, fishing licence **plus** a lobster report card filled out before you fish (gear code 1). Bag limit shown as **7 per person per day** but the KB flags that on one garbled source — verify (`species/california-spiny-lobster.md`, `techniques/hoop-netting.md`, `b19_AJjYCok`, `Qs9oEsh3b_w`, `YQsbwfQ4wzY`, `JiJYamo0QHk`, `Q196GVwVqro`).

---

## 3. Before I can turn this into a day plan

Step 1b of `planning/day-plan-protocol.md` says to set the day's `{regions, waters}` envelope *before* opening any species note, and to **ask** when the profile doesn't carry it. Your boat file has `home_port`, `range_nm` and `sea_state_max_ft` all explicitly **null** (`profiles/cameron/boat.md`), so I need those three from you. It matters here specifically: the terminal October condensation is onto Tanner/Cortez, and the KB puts that run at **96 mi SW of San Pedro, 111 mi west of Point Loma, ~110–115 mi from San Diego, ~90 mi to Tanner from Long Beach** — described as a full overnight sportboat run (`locations/tanner-bank.md`). On the Panga Marquesas 22 (single 115 hp, ~35 kt top, 30 gal bait tank, 100–125 lb ice) that end of the arc is a range-and-sea-state question, not a tactics question. The rest of the arc — backside Catalina, the 499/Clemente, the 181/182 ridge — is where an October plan for your boat most likely lives, but I'm not going to assert reachability on a null envelope.

---

## 4. Where the KB is thin on this question

- **No live conditions were pulled** — this is entirely the prior layer. The regime read from live water outranks the calendar, and in an anomalous year you plan from the chart, not from `seasonal/october.md`.
- **The KB does not say when the kelp-paddy field falls apart in the fall.** August is documented as the paddy peak; there is no note stating when paddies stop holding fish, so I can't tell you whether to keep running the paddy program through October beyond "dorado and paddy yellows are still on paddies in fall."
- **No numeric SST bands for yellowtail** — the yellowtail note carries an explicit flagged gap there, so I can't give you a "yellowtail leave at X °F" number for the cool-down.
- **October white seabass is a link, not a program** — the WSB note's season shape is flagged as the KB's own extension beyond its sources, and the corpus's dated records are July–August.
- **No documented yellowfin night program and no yellowfin kite program** — both are flagged stubs in the router.
- **No October wind/weather climatology.** The Santa Ana window (which flattens the NW outer islands and opens Rosa/Miguel) is documented for November–December, not October.
- **Several October load-bearing claims are single-source or internally flagged**: the "100 % temp chart" quote, the Tanner/Cortez condensation, the warm-band arc, the yellowfin "typically October" framing, and the dolphin-pod October window. I've flagged each inline rather than smoothing them.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `planning/report-reading-and-forecasting.md`, `planning/trip-length-selection.md`, `seasonal/september.md`, `seasonal/october.md`, `seasonal/august.md`, `seasonal/november-december.md`, `seasonal/year-anniversary-prior.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/current-structure.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `conditions/sea-state.md`, `conditions/upwelling-and-turnover.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/yellowfin-tuna-trolling.md`, `species/dorado.md`, `species/swordfish.md`, `species/striped-marlin.md`, `species/calico-bass.md`, `species/white-seabass.md`, `species/yellowtail.md`, `species/bonito.md`, `species/rockfish-lingcod.md`, `species/california-spiny-lobster.md`, `locations/bight-geography.md`, `locations/tanner-bank.md`, `profiles/cameron/boat.md`  
*videos:* `5to3Q5P7w90`, `XLVUhV8DW64`, `OYOda6T3f-8`, `yMiBtZ7k8-w`, `E4vKwRaRueA`, `P9H-bpzT7eU`, `i3qIAHW-SJc`, `SczdZIq3UmE`, `ouBrIdO7d4k`, `HWx1jDTGsng`, `LsFMBCa9DOQ`, `eehDVb6_GoI`, `Blh2BA-7Ono`, `Z3rZqy2Pi8E`, `5D1vx29LVpI`, `5p6gu14ZC4w`, `LqW32NSkObY`, `OpcKQPA3vAI`, `KuVwmfF6RAo`, `Q196GVwVqro`, `b19_AJjYCok`, `Qs9oEsh3b_w`, `YQsbwfQ4wzY`, `JiJYamo0QHk`, `cameron`  
*gaps admitted:* No live conditions were pulled or given — the answer is the prior/pattern layer only; BightSST SST, chlorophyll, wind/swell/current must be pulled per zone and along the route before this becomes a plan. | The KB documents August as the kelp-paddy peak but states no date, temperature or trigger for when the fall paddy field declines, so I cannot say when to stop running the paddy program. | No numeric SST bands for yellowtail migration or bite — species/yellowtail.md carries an explicit flagged gap for the numbers; the corpus gives directional water-state reads only. | October white seabass is only a cross-link; the note's season shape is flagged as the KB's own extension beyond its sources and the corpus's dated records are July–August 2022. | No yellowfin night program and no yellowfin kite program exist in the corpus — both are flagged stubs in species/yellowfin-tuna.md. | No October-specific wind or weather climatology in the KB; the Santa Ana / northern-islands window is documented only for November–December. | The October 'look 100% at your temp chart and chlorophyll' quote is flagged in the KB as spliced from two non-adjacent passages in one source and absent from its co-cite. | The Tanner/Cortez fall condensation and the warm-band retreat arc rest on a single source (OYOda6T3f-8) per the KB's own fact-check flags. | 'Typically October' for the yellowfin fragmentation geography is flagged as the KB's generalization, not a statement in the cited source. | The dolphin-pod yellowfin window ('first week of October, end of September', backside Catalina, 60–70 lb) is single-source and uncorroborated. | The lobster October opener month is not actually stated in any cited transcript (only the March close is sourced) and the 7-per-day bag limit rests on one garbled seminar aside — both need a CDFW check. | Cameron's boat profile has home_port, range_nm and sea_state_max_ft all null, so the protocol's step-1b envelope cannot be resolved and reachability of the Tanner/Cortez end of the October arc cannot be assessed. | No documented Sept-to-Oct change in bluefin grade specifically; the KB's grade-drop claim is for mid-December.

</details>
