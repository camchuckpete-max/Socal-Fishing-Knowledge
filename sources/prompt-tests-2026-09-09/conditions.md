# Conditions & season — head-to-head prompt tests

21 prompts answered blind by a planning session confined to each of three pinned checkouts, then scored blind by a judge on six 0–2 criteria (max 12). Versions: **B2** = batch 2 (`540ea4a`), **B3** = batch 3 / pre-review (`1e66a92`), **NOW** = the review (branch tip). The A/B/C order the judge saw was fixed per prompt by index; the mapping below was never shown to it.

## Scoreboard

| | **B2** batch 2 | **B3** batch 3 | **NOW** review |
|---|---:|---:|---:|
| mean total /12 | 11.5 | 10.5 | 12 |
| found | 2 | 2 | 2 |
| specific | 2 | 2 | 2 |
| sourced | 2 | 2 | 2 |
| scoped | 2 | 1.5 | 2 |
| honest | 1.5 | 1.5 | 2 |
| actionable | 2 | 1.5 | 2 |
| **wins** | 0 | 0 | 2 |
| ⚑ fabricated_specifics | 0 | 0 | 0 |
| ⚑ bluffed | 0 | 0 | 0 |
| ⚑ regulation_without_asof | 0 | 1 | 0 |

### By category (mean total /12)

| category | B2 | B3 | NOW |
|---|---:|---:|---:|
| Trip planning | None | None | None |
| Gear | None | None | None |
| Technique | None | None | None |
| Finding fish | None | None | None |
| Conditions & season | 11.5 | 10.5 | 12 |
| Rigging, bait, care | None | None | None |
| Honesty | None | None | None |

[← back to the index](README.md)


## Per prompt

### 16. [conditions] What is the Catalina Eddy and when does it matter for deciding where to fish?

**Winner:** NOW · mapping {'A': 'B3', 'B': 'NOW', 'C': 'B2'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |
| B3 | 2 | 2 | 2 | 2 | 2 | 1 | **11** |  |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three correctly diagnose the eddy as a wind/sea-state shield rather than a bite driver, name the same single trigger (bad outer forecast, do not write off the inside), and admit the same real holes — no season, no mechanism, no way to actually check eddy state. B separates itself on the two things a new angler needs next: it carries the adjudicated scoping ('everything east of Catalina and San Clemente', with the north-wind lee reasoning) instead of the superseded 'inner San Diego banks' wording, and it converts that into charted marks with positions, distances and bearings plus the go/no-go numbers those marks still have to clear — and it is the only answer to flag that the 425 sits in Mexican water. C matches B's execution discipline (steepness, current-vs-swell, the 12 kt / 10-second gates) but never names the water; A is the most rigorous on provenance, catching that the bight-geography 4/21/22 cite resolves to no manifest video, and adds the useful day-by-day read that eddy state flips inside a week, but leaves the angler with a check and no thresholds or marks.

- *B2 reasons:* found: correct notes and correct framing, plus the cleanest separation of the wind eddy from the 500-fathom current eddies that aggregate bait and paddies. specific: steepness rule (10 ft @ 15 s vs 3-4 ft @ 4-5 s), current-vs-swell (4 ft @ 10 s fishes like 6 ft @ 7-8 s), Catalina east-end ridge rough then laying down 3-4 mi past, 12 kt / sub-10-sec / 12-15 kt-4-8 ft-9 sec, 5-8 degF — but no coordinates and no named sheltered marks. sourced: note paths with S2L3KLSQ6Is, NC3-3pJDEgo (dated, medium/single-mention noted), HnqiE05vdXs, HzE4FHHcvTk, 9hEa3sGTh40. scoped: region handling correct, no regulation asserted; states the eddy carries no species/technique consequence. honest: strong eight-item gap list and explicit 'one-source, two-paragraph topic'; states the 4/21/22 attribution flatly where A caught it as unresolvable. actionable: the fishable-or-not checklist plus VHF-discount doctrine makes the day decidable, though it never says which water to point at beyond 'inner zones'.
- *B3 reasons:* found: went straight to the right notes (island-structure, sea-state, day-plan-protocol) and correctly framed the eddy as a wind/sea-state feature, not a bite feature. specific: 5-8 degF rollover, 12-24h hindcast, 48-72h fetch, named per-coordinate endpoints, the /api/v1/context field-wide-wind defect verified 2026-08-18, plus dated transcript detail — but no positions and no named sheltered marks. sourced: every claim carries a note path plus S2L3KLSQ6Is / HnqiE05vdXs / aFb221LUoD0 and the transcript file itself. scoped: SoCal-bight framing correct, waters axis handled through the step-1b envelope, no regulation stated. honest: best provenance honesty of the three — caught that the 4/21/22 bight-geography cite resolves to no manifest video, and listed six real gaps. actionable: gives the check ('query inside and outside separately') but no go/no-go numbers and no named water, so the angler still cannot decide the day.
- *NOW reasons:* found: same right material plus the adjudicated scoping in sea-state.md and the superseded-wording flags on north-9-mile-bank-178 and socal-bight. specific: charted positions for North 9 Mile 32d38.000'N 117d26.000'W, the 178 at 32d42.000'N 117d29.317'W, 4.9 nm / 325 deg, South 9 Mile and the 439, the 425 at 32d15.000'N 117d23.200'W, Zuniga 10.9 nm/078 and 13.5 nm/097, ~600 ft crown, and the 12 kt / sub-10-sec / 12-15 kt-4-8 ft-9 sec limits — all verified against the notes. sourced: note paths plus S2L3KLSQ6Is, NC3-3pJDEgo, zKmZ4zql2ws, Rf1HKJG-SDg, HzE4FHHcvTk, and the fact-check ledger row. scoped: only answer to catch that the 425 is baja-pacific-north Mexican water needing papers, and it separates the north-wind lee from the opposite-geometry Santa Ana. honest: surfaces the contradicted-by-source flag on 'counter-clockwise', the internal supersession, and says the KB never operationalizes 'check eddy state'. actionable: names the exact water to query, the marks, and the thresholds it must clear — a runnable morning decision.

<details><summary>Full prompt</summary>

What is the Catalina Eddy and when does it matter for deciding where to fish?

</details>

<details><summary><b>B2 — batch 2</b> · 12/12</summary>

# The Catalina Eddy — what this KB actually says, and when it changes your zone call

Short version: in this knowledgebase the Catalina Eddy is **a sea-state / wind feature, not a water-quality or bite feature.** It matters at exactly one decision point — when the outer forecast looks blown and you're about to cancel or push offshore anyway. It is thin coverage (one dated source), so I'll mark plainly where it runs out.

You gave me no conditions for a specific day, so this is the rule, not a call on today's water.

## What it is (the KB's whole definition)

> the **Catalina Eddy** — "a counter-clockwise circulation that sets up in the bight"
> — [`locations/island-structure.md`](locations/island-structure.md), §"The Catalina Eddy as a shielding feature", from the BD SoCal Bight report of 5/26/22, Landesfeind (`S2L3KLSQ6Is`)

That one clause is the entire definition in the KB. It's filed under island structure on the logic that **islands don't only make bottom structure — they shape the wind field**, and it feeds forward into [`conditions/sea-state.md`](conditions/sea-state.md) as a planning input.

## What it does for you

- It can **shield the inner San Diego banks and the tuna grounds while it blows outside** (`S2L3KLSQ6Is`, 5/26/22) — [`locations/island-structure.md`](locations/island-structure.md), [`conditions/sea-state.md`](conditions/sea-state.md) §"Unforecast-wind heuristics".
- Mechanically for planning purposes: it **decouples inner-zone seas from the offshore forecast**. The bight-wide or offshore number stops being a valid proxy for what the inside is doing.

## When it matters — the trigger, stated as a rule

**Trigger:** the outer forecast looks bad/blown.
**Action:** check eddy state **before** writing off the inside — the inner zones may be fishable ([`conditions/sea-state.md`](conditions/sea-state.md); [`locations/island-structure.md`](locations/island-structure.md)).

It does **not** change species or technique routing. It changes **which zone you point the boat at**, and whether the day happens at all.

Where it sits in the protocol ([`planning/day-plan-protocol.md`](planning/day-plan-protocol.md)):
- **Step 1 (pull conditions)** — this is the reason the protocol insists on wind/swell **per fishing zone and along the transit route, observed and forecast**, not one number for the bight. An eddy day is precisely the day a single regional wind figure lies to you. The route can also be the disqualifier even when the destination zone is fine.
- **Step 2 (apply layers)** — weight inner-zone options up rather than defaulting to "offshore is blown, so it's blown."

## Before you commit to the inside on eddy shielding

Everything below is from [`conditions/sea-state.md`](conditions/sea-state.md) and applies on top of the eddy read — the eddy tells you to *look inside*, these tell you whether inside is actually fishable:

- **Run a 12–24 h wind hindcast, not just the forward forecast.** A calm-morning read hides overnight wind and the leftover chop it built.
- **Forecast error is asymmetric** — assume it errs on the worse side, and assume afternoon W at the islands **strengthens** rather than eases.
- **Inland heat → afternoon W wind.** 100 °F+ inland can break down into unforecast afternoon W on the water; if it's windier than forecast in the morning, assume it **builds all day** and a small boat bails early.
- **Steepness beats height.** 10 ft @ 15 s from the south is barely felt; **3–4 ft @ 4–5 s is brutal.** Flag any zone or route leg where the period in seconds approaches the height in feet.
- **Current-vs-swell opposition.** Summer uphill (counter) current against NW swell stands the swell up: a forecast **4 ft @ 10 s fishes like 6 ft @ 7–8 s.** Point forecasts won't show this.
- **Localized bathymetric slop, and don't over-read it.** The ridge off the **east end of Catalina is horrible for a few miles, then lays down 3–4 mi past it.** One rough patch on the transit does not mean the whole outer zone is blown.
- **Hard go/bail numbers** (Capt. Dave Hansen, `NC3-3pJDEgo`, 2020-11-18 — the note flags this set as **medium confidence, single mention**): won't run above **~12 kt** (that's where whitecaps come up); **sub-10-second swell interval is a hard bad-sea flag** independent of height; **12–15 kt with 4–8 ft @ 9 s** is named flatly unfishable, big boats included.

One more discipline: if your evidence that "it's fine inside" is an unsolicited VHF call, discount it. [`planning/fleet-intelligence.md`](planning/fleet-intelligence.md) documents deliberate radio misinformation and the doctrine to weight your own research and sign over a stranger's call (`9hEa3sGTh40`, medium confidence).

## Don't confuse it with the other "eddies" at Catalina

Same word, different feature, different use:

At **Catalina's ~500-fathom curve**, the uphill (summer counter) current **compresses as it climbs the slope, spins eddies, and aggregates both bait and kelp paddies** along the curve (8/31/22, `HnqiE05vdXs`) — [`locations/island-structure.md`](locations/island-structure.md), [`conditions/current-structure.md`](conditions/current-structure.md). Those are small-scale current eddies that **concentrate food — a place to fish.** The Catalina Eddy above is a **wind feature — a reason the inside is fishable at all.**

The curve version comes with its own method: the curve is **a line you hunt, not a point** — run it **slowly**, identify the structure a popped fish related to, don't sprint to where the fleet went, and come back to your own marked positions at tide time. Governing rule, near-verbatim: **sign associated with structure is a repeatable decision; sign in no-man's-land is low value.**

## Adjacent layer worth pulling the same morning (but not the eddy)

If the bad outer forecast is a **big NW blow** specifically, [`locations/bight-geography.md`](locations/bight-geography.md) (`HzE4FHHcvTk`) gives a separate, repeatable map from the 4/21/22 report: the **northern Channel Islands and the LA/Ventura coastal shelf get crushed** (surface temp rolled down **5–8 °F**), **south of Newport is less prone** to wind-wave rollover, and the **Coronados, tuna grounds, Catalina and San Clemente held their water** through that event. That's a water-survival map, not the eddy — the KB does not connect the two, so treat them as two independent weightings that happen to both push you south/inside on a NW day.

## Where the KB runs out on this (say it plainly)

The Catalina Eddy is a **one-source, two-paragraph topic** here — a single dated report (5/26/22, `S2L3KLSQ6Is`, registered voice Landesfeind per [`sources/source-registry.md`](sources/source-registry.md)) with no second corpus mention. Specifically, the KB does **not** tell you:

- **When it sets up** — no month, season, frequency or typical duration. [`seasonal/may.md`](seasonal/may.md), built from that same 5/26/22 report, carries no eddy content at all, and no other seasonal note mentions it.
- **How to check "eddy state"** — the doctrine says check it, but names no product, model, buoy or diagnostic for doing so. BightSST is the conditions source of record ([`planning/day-plan-protocol.md`](planning/day-plan-protocol.md)) but no eddy field is documented.
- **How far the shielding extends** — "inner San Diego banks and tuna grounds" is never enumerated into named banks or a zone boundary; neither [`locations/zone-lexicon.md`](locations/zone-lexicon.md) nor [`locations/bightsst-eval-targets.md`](locations/bightsst-eval-targets.md) defines that set.
- **Any effect on water or fish** — nothing on the eddy's influence on SST, chlorophyll/clarity, current, marine layer/fog, or on the bite itself. In this KB it is purely a wind/sea-state shield.
- **Any species or technique consequence** — no species router links to it.

So: use it as a *don't-cancel-yet* check, verify the inner zone with a real per-zone observed+forecast pull plus the hindcast, and don't expect the KB to predict eddy days for you.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `locations/island-structure.md`, `conditions/sea-state.md`, `conditions/current-structure.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `locations/bightsst-eval-targets.md`, `planning/fleet-intelligence.md`, `planning/report-reading-and-forecasting.md`, `seasonal/may.md`, `sources/source-registry.md`, `sources/extraction-log.md`, `sources/transcripts/_manifest.csv`  
*videos:* `S2L3KLSQ6Is`, `HnqiE05vdXs`, `NC3-3pJDEgo`, `HzE4FHHcvTk`, `9hEa3sGTh40`  
*gaps admitted:* No seasonality for the Catalina Eddy — the KB gives no month, season, frequency, or typical duration for when it sets up (seasonal/may.md, built from the same 5/26/22 report, carries no eddy content). | No formation mechanism or synoptic setup for the eddy beyond the one clause 'a counter-clockwise circulation that sets up in the bight'. | No method or tool for checking 'eddy state' — the doctrine says to check it but names no forecast product, model, buoy, or on-water diagnostic; no BightSST eddy field is documented. | No spatial extent or boundary — 'inner San Diego banks and tuna grounds' is never enumerated into named banks or a zone definition in locations/zone-lexicon.md or locations/bightsst-eval-targets.md. | No documented effect of the eddy on water temperature, chlorophyll/clarity, current, or the bite itself — it appears only as a wind/sea-state shielding input. | Nothing on marine layer, fog, or visibility associated with the eddy, which would matter for search-and-glassing. | No species or technique consequence — no species router or technique note references the Catalina Eddy. | Single-source coverage: the eddy claim rests on one dated report (5/26/22, S2L3KLSQ6Is) with no second corpus mention, so the shielding doctrine has never been repeated or bounded.

</details>

<details><summary><b>B3 — batch 3</b> · 11/12</summary>

## Short answer

In this KB the Catalina Eddy is a **wind/sea-state feature, not a bite feature**. It is defined as "a counter-clockwise circulation that sets up in the bight" that can **shield the inner San Diego banks and the tuna grounds while it blows outside** ([`locations/island-structure.md`](locations/island-structure.md), § "The Catalina Eddy as a shielding feature" — cited to the BDOutdoors Southern California Bight report of 2022-05-26, `S2L3KLSQ6Is`, Landesfeind).

It matters at exactly one decision point: **when the outer/offshore forecast looks blown and you are about to write off the day or the inside.** Check eddy state before you do — the inner zones may be fishable while the outside is not.

## The rule, as the KB states it

[`conditions/sea-state.md`](conditions/sea-state.md) files it under **unforecast-wind heuristics**, alongside "inland heat → afternoon W wind" and "forecast error is asymmetric":

> **Catalina Eddy shielding.** The Catalina Eddy can shield the inner SD banks / tuna grounds while it blows outside. Check eddy state when the outer forecast looks bad before writing off the inside (5/26/22 → `S2L3KLSQ6Is`).

[`locations/island-structure.md`](locations/island-structure.md) adds the mechanism framing: **islands do not only make bottom structure, they shape the wind field**, so the eddy is "an island-driven feature that decouples inner-zone seas from the offshore forecast." That decoupling is the whole planning value — it breaks the assumption that one blown forecast describes the whole bight.

## Where it lands in the day-plan protocol

Per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md):

- **Step 1 (pull conditions)** — pull wind/swell **per fishing zone and along the transit route, observed and forecast**. A single field-wide number cannot show you an eddy.
- **Step 1b (set the envelope)** — this is where the eddy actually changes the answer. Your reachable `waters` are derived from range and `sea_state_max_ft` against the day's forecast. An eddy day can put `island` / `bank` inside the envelope for the inner San Diego zones while the outer `open-ocean` water stays out of it. Once step 1b is set it is binding — so getting the eddy read right *before* step 1b is what keeps you from cancelling a fishable day, or from planning an outside run the eddy is not actually protecting.
- **Step 2 (priors + layers)** — sea-state is the layer that carries it.

## How to actually check eddy state

The KB names no eddy index or eddy product. What it does give you is the resolution discipline that makes the shielding visible, from [`config/endpoints.md`](config/endpoints.md):

- **Per-spot resolution is required.** "Wind and swell get queried at every candidate spot and at points along the route out and back. A single coastal station cannot describe a trip that crosses 40 miles of open water."
- **Do not use BightSST `/api/v1/context` for wind.** Its wind is **field-wide and it carries no swell** — it returns the same wind whatever lat/lon you pass (verified 2026-08-18 at two points 130 nmi apart). That is precisely the product that would hide an eddy.
- Per-coordinate wind: `api.open-meteo.com/v1/forecast` (`wind_speed_10m`, `wind_gusts_10m`, `wind_direction_10m`), fallback `api.weather.gov` marine zones. Per-coordinate swell: `marine-api.open-meteo.com/v1/marine`. Observed: NDBC realtime station text.

So operationally: query the inner SD banks/tuna-grounds spots and the outer spots **separately**, and look for the inside reading to diverge from the outside. Pair it with the note's other sea-state layers before committing — the **12–24 h wind hindcast** (a calm-morning forecast hides overnight wind) and the **48–72 h upstream fetch check** (swell arrives after the wind that made it, from far away), both in [`conditions/sea-state.md`](conditions/sea-state.md).

## Expect it to flip inside a single week

The source report this doctrine comes from ([`sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md`](sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md), BDOutdoors, 2022-05-26) walks the eddy day by day: blown out everywhere Monday ("Monday is a wash"), then it "starts to back off on Tuesday down south here in the tuna grounds" with "that Catalina eddy blocking off," creeping back Tuesday afternoon into Wednesday, "getting into that Catalina eddy again" by Thursday, and weather building and wrapping around again Friday — "hopefully that eddie holds up, keeps that pushed out."

Practical read: **eddy state is a per-day check, not a season setting.** It can turn a wash into a fishable inside day and then give it back 48 hours later.

## Do not confuse it with the other "eddies" in this KB

The word appears in a completely different, smaller-scale sense: at **Catalina's ~500-fathom curve**, the uphill (summer counter) current compresses as it climbs the slope, **spins eddies, and aggregates both bait and kelp paddies along the curve** ([`conditions/current-structure.md`](conditions/current-structure.md), [`locations/island-structure.md`](locations/island-structure.md) — 8/31/22 report, `HnqiE05vdXs`). That is a *current-over-structure* feature you hunt as a line ("the curve is a line you can hunt, not a point"), with the governing rule: **sign associated with structure is a repeatable decision; sign in no-man's-land is low value.** It is unrelated to the Catalina Eddy's wind shielding.

## The companion pattern for "where to fish when it blows"

The eddy is one of two KB reasons the bight does not blow uniformly. The other is **wind-rollover geography** ([`locations/bight-geography.md`](locations/bight-geography.md), cited to a 4/21/22 Landesfeind report): a big NW blow **crushes the northern Channel Islands and the LA/Ventura coastal shelf** (surface temp rolled down **5–8 °F**), **south of Newport is less prone**, and the **Coronados, the tuna grounds, Catalina, and San Clemente Island held their water** through that event. Different mechanism (turnover vs. wind shielding), same planning direction on a blown day: **look south and inside.**

Separately, if the day sends you to Catalina itself, side selection is driven by swell direction, not the eddy: a **south swell** tears up the **east end**; a **big west swell** is the trigger to send anglers **down to the east end** rather than front-side/backside/middle (Capt. Dave Hansen, `aFb221LUoD0`, 2020-10-20 — single mention, medium confidence, in [`locations/island-structure.md`](locations/island-structure.md)).

## What this KB does not tell you about the Catalina Eddy

Being straight about the limits — this rests on a **single 2022-05-26 report**:

- **No season or climatology.** The KB never says which months the eddy typically sets up, or how often. The one dated citation is late May; that is a data point, not a stated season. [`seasonal/may.md`](seasonal/may.md) is sourced from that very report and does not mention the eddy at all.
- **No formation mechanism.** "Counter-clockwise circulation that sets up in the bight" is the entire physical description. Nothing on what causes it or what precedes it in a forecast.
- **No boundary or extent.** "Inner San Diego banks" and "the tuna grounds" are never defined as a spot list or a zone with edges anywhere in `locations/` — so the KB cannot tell you which specific banks fall inside the shield.
- **No duration or eddy-state indicator.** No index, product, or observable is named for "check eddy state."
- **No effect on the fish.** Nothing on whether eddy conditions change SST, chlorophyll, current, or the bite itself — in this KB it is purely a wind/sea-state and zone-access call.

Fill those from a live forecast discussion and per-spot wind on the day; do not fill them from this KB.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `locations/island-structure.md`, `locations/bight-geography.md`, `conditions/current-structure.md`, `config/endpoints.md`, `seasonal/may.md`, `planning/report-reading-and-forecasting.md`, `locations/zone-lexicon.md`, `sources/transcripts/bdoutdoors--southern-california-bight-fishing-report-05-26-22--S2L3KLSQ6Is.md`, `sources/transcripts/_manifest.csv`, `sources/extraction-log.md`, `sources/bd-transcript-knowledge-proposal.md`  
*videos:* `S2L3KLSQ6Is`, `HnqiE05vdXs`, `aFb221LUoD0`  
*gaps admitted:* No season or climatology for the Catalina Eddy — the KB's only dated citation is a single 2022-05-26 report; it never states which months it typically forms or how often. | No formation mechanism — the KB describes it only as 'a counter-clockwise circulation that sets up in the bight' with no cause, no precursor signature, and no synoptic pattern. | No spatial extent or boundary — 'inner San Diego banks' and 'the tuna grounds' are never defined as a spot list or bounded zone anywhere in locations/, so the KB cannot say which specific banks the shield covers. | No duration or persistence guidance — nothing on how long an eddy typically holds once established. | No named product, index, or observable for 'check eddy state' — config/endpoints.md gives per-coordinate wind/swell endpoints but no eddy diagnostic. | No stated effect of the eddy on SST, chlorophyll, current, or fish behavior — in this KB it is purely a wind/sea-state and zone-access input, not a bite driver. | seasonal/may.md is sourced from the same 2022-05-26 report (S2L3KLSQ6Is) but carries no eddy content, so the seasonal layer offers no eddy prior. | Provenance gap: the wind-rollover geography claim in locations/bight-geography.md cites a '4/21/22' report, but no 4/21/22 video appears in sources/transcripts/_manifest.csv and the note's front matter lists only HzE4FHHcvTk (the 8/17/22 report), so that claim's video ID is not resolvable in this KB version.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

I read the repo's CLAUDE.md, the README, the day-plan protocol, and then followed the eddy through the conditions and locations branches.

Here is the answer.

## What the Catalina Eddy is, per this KB

The knowledgebase treats the Catalina Eddy as a **wind/sea-state feature, not a water-quality or bite feature**. [`locations/island-structure.md`](locations/island-structure.md) files it under "How it fishes" as the case where islands shape the wind field rather than the bottom: a circulation that sets up in the Bight and can **shield inner zones while it blows outside** (`S2L3KLSQ6Is`) — "an island-driven wind feature that decouples inner-zone seas from the offshore forecast."

Two honesty notes the KB itself carries:

- That page describes the eddy as **counter-clockwise**, and the note flags it: `⚠ Fact-check (contradicted-by-source)` — the source transcript never states a rotation direction and never names San Diego banks specifically, only "tuna grounds down south." The rotation direction is queued for external verification in [`sources/fact-check-ledger.md`](sources/fact-check-ledger.md) (row on `locations/island-structure.md`).
- The KB carries **no mechanism** for how the eddy forms and **no seasonal timing** for it. Treat it as a condition you check, not one you predict from the calendar.

## The scope of the shelter (adjudicated — use this version)

[`conditions/sea-state.md`](conditions/sea-state.md) carries the current, adjudicated scoping (⚠ adjudicated, Cameron, 2026-08-26):

> **Catalina Eddy shielding — everything east of Catalina and San Clemente.**

The reasoning is a lee, not a list of banks: the prevailing wind down the California coast outside SoCal comes from the **north**, so the islands shadow the water behind them, and **marks well to the south still sit in that shadow**. The named example is the **425**, which is "often shielded despite being far south of San Clemente" (cameron) — the 425 is charted at **32°15.000'N 117°23.200'W** ([`locations/425-bank.md`](locations/425-bank.md)), and note it is `regions: baja-pacific-north`, i.e. Mexican water, so that one needs papers ([`locations/mexican-waters.md`](locations/mexican-waters.md)).

An **older, narrower wording** still lives on [`locations/north-9-mile-bank-178.md`](locations/north-9-mile-bank-178.md) and [`locations/socal-bight.md`](locations/socal-bight.md) — "shields the inner San Diego banks and tuna grounds." That page flags itself as the superseded scoping (`⚠ Fact-check (contradicted-internal)`), and the ledger records that the conclusion for those zones is unaffected either way: they sit inside the shelter on both readings. [`locations/south-9-mile-bank-439.md`](locations/south-9-mile-bank-439.md) carries the rescoped wording.

## When it matters for deciding where to fish

**The trigger is narrow and specific: the outer/offshore forecast looks bad.** The rule in the planning checklist of [`conditions/sea-state.md`](conditions/sea-state.md) is:

> Check Catalina Eddy shielding before writing off water east of Catalina / San Clemente on a bad outer forecast.

In the sequence of [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md), this is a **step 1b / step 2 call** — it belongs to setting the day's `waters` envelope (which of `bank` / `island` / `open-ocean` is reachable given your `sea_state_max_ft` against the forecast) and to weighting zones with the conditions layers. It happens **before you open any species router**. It does not change *what* you fish or *how*; it changes **whether the inside stays on the board**. [`locations/socal-bight.md`](locations/socal-bight.md) states the consequence plainly: "an ugly offshore forecast does not automatically close the inner zones."

Concretely, on a blown-outside day the eddy is what keeps these in play (all positions cameron, via the spot library):

| Zone | Marks |
| --- | --- |
| [North 9 Mile Bank / 178](locations/north-9-mile-bank-178.md) | North 9 Mile Bank **32°38.000'N 117°26.000'W**; the 178 **32°42.000'N 117°29.317'W** (4.9 nm apart, 178 bearing 325°) |
| [South 9 Mile Bank / 439](locations/south-9-mile-bank-439.md) | South 9 Mile Bank **32°32.000'N 117°21.000'W**; the 439 **32°29.500'N 117°24.000'W** (3.6 nm apart, 439 bearing 225°) |
| [101 / 425](locations/101-425.md) | the **425** at **32°15.000'N 117°23.200'W** — Mexican water |

The Nine Mile complex is named for distance, not depth — nine statute miles off the beach, with many closely spaced high spots coming up to roughly **600 ft** in places (`Rf1HKJG-SDg`, [`locations/zone-lexicon.md`](locations/zone-lexicon.md)). North 9 Mile Bank sits **10.9 nm at 078°** from the Zuniga Jetty at the San Diego Bay entrance; the 178 is **13.5 nm at 097°** (cameron) — the same order of run as the Coronados' ~13 nm, but staying in US water.

## What it does *not* license

- **The eddy is not a Santa Ana.** [`conditions/sea-state.md`](conditions/sea-state.md) keeps those separate: a Santa Ana is an offshore-blowing **northeast** wind that flattens the **northern** islands (the Rosa / San Miguel window) while making the **Catalina return leg** dangerous — offshore wind pushing water out against the prevailing motion stacks fast-building swell, and a boat at Avalon faces a multi-hour beat home to Newport / Dana Point (`NC3-3pJDEgo`). Eddy shelter is a north-wind lee; a Santa Ana is the opposite geometry.
- **It does not override the go/no-go numbers.** Same note: hold at the dock above **~12 kt** wind, treat a **sub-10-second** interval as a hard flag, and never run the **12–15 kt / 4–8 ft / 9-second** combo (`NC3-3pJDEgo`). Shielded water still has to clear those.
- **It does not mean the whole inside is smooth.** Expect local slop where current accelerates over structure — the ridge off the **east end of Catalina** is horrible for a few miles then lays down 3–4 mi past it (`zKmZ4zql2ws`) — and assume forecast error runs to the worse side, with afternoon W at the islands strengthening rather than easing (`zKmZ4zql2ws`).
- **It is a different question from the NW-rollover map.** [`locations/bight-geography.md`](locations/bight-geography.md) says a big NW blow crushes the northern Channel Islands and the LA/Ventura shelf (surface temp down **5–8 °F**) while **south of Newport** is less prone to wind-wave rollover, and the Coronados, tuna grounds, Catalina and San Clemente held their water. That map is about **water temperature surviving**; the eddy is about **seas being runnable**. The KB flags the map as `cite-unresolved (standing)` — adjudicated by Cameron (2026-08-26) to stand and be backed by per-zone BightSST rollover statistics rather than re-sourced (`HzE4FHHcvTk`, and `YZtX1MiT0y8` on [`locations/socal-bight.md`](locations/socal-bight.md), where the 5–8 °F figure carries its own contradicted-by-source flag).

## Practical use, compressed

On a day where the offshore forecast is ugly: **do not close the inside yet.** Pull per-spot wind and swell for the water east of Catalina / San Clemente — the inner San Diego bank grid and marks south of it — instead of only the outer banks, run those numbers against the 12 kt / 10-second thresholds, and if they clear, that is your day. Per-coordinate wind and swell come from the endpoints in [`config/endpoints.md`](config/endpoints.md); note that the `/api/v1/context` payload's wind is field-wide and carries no swell, so it is never valid for a per-spot shelter read.

## What the KB does not answer

The eddy content in this KB is four sentences of doctrine plus a scoping adjudication. It does not tell you **how** to check eddy state — no product, index, or observable is named anywhere, including in `config/endpoints.md`. In practice the KB's rule reduces to "query the inside directly rather than inferring it from the outside forecast," which is what I would do. It also gives no season for the eddy, no wind threshold at which the lee breaks down, no boundary for how far the shelter extends, and nothing tying eddy days to any species or technique choice.


*notes:* `CLAUDE.md`, `README.md`, `planning/day-plan-protocol.md`, `conditions/sea-state.md`, `locations/island-structure.md`, `locations/socal-bight.md`, `locations/north-9-mile-bank-178.md`, `locations/south-9-mile-bank-439.md`, `locations/425-bank.md`, `locations/bight-geography.md`, `sources/fact-check-ledger.md`, `sources/extraction-log.md`, `locations/evidence/catalina-island-front-side.md`, `config/endpoints.md`, `seasonal/may.md`  
*videos:* `S2L3KLSQ6Is`, `NC3-3pJDEgo`, `zKmZ4zql2ws`, `YZtX1MiT0y8`, `HzE4FHHcvTk`, `Rf1HKJG-SDg`  
*gaps admitted:* No note gives the eddy's formation mechanism — only that it is a circulation that sets up in the Bight; its rotation direction is flagged contradicted-by-source on locations/island-structure.md and queued for external verification in sources/fact-check-ledger.md. | No seasonal timing or climatology for the eddy anywhere in the KB — seasonal/may.md, the month fed by the one eddy source (S2L3KLSQ6Is, dated 2022-05-26), does not mention it at all. | The KB says to 'check eddy state' but never operationalizes it — no data product, index, endpoint, or on-water observable is named, including in config/endpoints.md. | No wind-speed or wind-direction thresholds are given for when the shielding holds or breaks down. | No stated boundary or extent for the lee beyond 'east of Catalina and San Clemente' plus the single 425 example — how far south or east the shelter reaches is unstated. | No stated effect of the eddy on SST, chlorophyll, water color, bait or bite quality — the KB treats it purely as a wind/sea-state feature. | No species or technique consequence is tied to eddy days anywhere in species/ or techniques/. | locations/north-9-mile-bank-178.md flags that no corpus source gives a run time, sea-state envelope or minimum boat range for the inner San Diego bank zones, so the KB cannot say what boat the sheltered run actually suits. | The NW-rollover map that pairs with this decision (bight-geography.md) carries a standing cite-unresolved flag and its 5-8 degF figure is flagged contradicted-by-source on locations/socal-bight.md.

</details>

### 17. [conditions] What changes in the Southern California Bight from September into October, and how should my fishing change wi…

**Winner:** NOW · mapping {'A': 'NOW', 'B': 'B2', 'C': 'B3'}

| version | found | specific | sourced | scoped | honest | actionable | total | flags |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| B2 | 2 | 2 | 2 | 2 | 1 | 2 | **11** |  |
| B3 | 2 | 2 | 2 | 1 | 1 | 2 | **10** | regulation_without_asof |
| NOW | 2 | 2 | 2 | 2 | 2 | 2 | **12** |  |

**Judge:** All three get the core answer right — September's late warm-stable regime gives way to October's fall fragmentation, so the chart replaces the spot list — and all three deliver real numbers, note paths and video ids. A separates itself on provenance honesty and precision: it alone flags that the load-bearing '100 % temp chart and chlorophyll' quote is spliced and mis-co-cited, that the backside-Rosa → SBI → Catalina → 499 retreat arc and the Tanner/Cortez condensation are single-sourced with the second cited video actually contradicting them, and that the yellowtail October framing is inferred from upload dates; it also carries the only charted Tanner/Cortez coordinates and the fullest regulation handling (CDFW + as-of 2026-08 + verify, with the 7/day bag limit itself flagged). B is the best profile-aware answer — it is the only one that filters the Tanner/Cortez endgame out of a 22-ft panga's October and redirects to reachable water — but it repeats the misattributed quote and the distance figures without their caveats. C matches on execution detail (its swordfish rig chain is the most complete) yet states the Farnsworth Bank closure as a bare regulation with no jurisdiction, as-of or verify, which is exactly the failure mode the KB's own content rules forbid.

- *B2 reasons:* found: same correct regime spine, plus useful extras (box-size time budgeting, report-aging, moon doctrine, BOLA contrast labeled Baja). specific: 90–100/110–115 mi runs, DSL ≥600 ft / ~950 ft, 10–13 kt gate, drift ≤2–2.5 kt, PE6–8 150–400 g, 30 lb flyline / 2/0 circle stepping to 15–20 lb and size 1, paddy arcs 90–120 ft, 12–15 kt @ 4–8 ft/9 s unfishable combo. sourced: note paths plus video ids and confidence tags on medium/unregistered sources. scoped: socal-bight-correct, Baja BOLA labeled; lobster, rockfish and the Farnsworth closure all carry CDFW/as-of/verify. honest: good gaps list and side-by-side conflicts, but presents the '100 % temp chart' line as jointly spoken by two videos when only one says it, and states the Tanner/Cortez distances without the KB's own statute-mile/two-ends-of-a-complex caveat. actionable: strongest profile-aware section — filters the Tanner/Cortez condensation out of a 22-ft panga's October and redirects to reachable water.
- *B3 reasons:* found: correct regime flip, retreat arc, break-side table, October doors (sword, lobster, grunion) and the NW-blow differential map of the Bight. specific: best swordfish rigging chain (14/0 forged offset circle, 7–10.5 lb breakaway, 80 lb braid → 25 ft 200 lb wind-on → 10–15 ft 200–300 lb leader, LP light 10–15 ft above bait), 74–75 °F Cortez vs 70 °F Osborn edge, hoop rope 40–50 ft vs Catalina 20–30 ft, WSB 60–100+ ft. sourced: note paths and ids throughout, with confidence/unregistered-channel tags. scoped: mostly right and wahoo is region-labeled, but the Farnsworth Bank closure ('only yellowtail and bonito may be kept') is stated bare with no jurisdiction, as-of or verify, unlike its lobster and rockfish handling. honest: candid gaps list, but repeats the spliced '100 %' quote as though three sources support it and offers no fact-check flags on single-source claims. actionable: clear ordered 'what I'd change on the boat' list and executable sword/yo-yo detail.
- *NOW reasons:* found: nails the Sept warm-stable → Oct fall-fragmentation flip and pulls every relevant branch (regimes, break-side rules, geography arc, swordfish opening, lobster, inshore grunion event). specific: charted Tanner 32°42.000'N/119°08.000'W and Cortes 32°26.417'N/119°07.833'W, 15.6 nm apart, 96/111/90–110 mi runs, DSL ≥600 ft with baits 800–1,100 ft, 150–350 fm ground, PE6–8 / 150–400 g jigs, 71.6 °F paddy reading, calico 65–68 °F, hoop nets 20–55 ft. sourced: nearly every claim carries a note path plus a video id (OYOda6T3f-8, 5to3Q5P7w90, E4vKwRaRueA, HzE4FHHcvTk, yMiBtZ7k8-w). scoped: socal-bight throughout, Baja/Cortez explicitly excluded as out-of-region; lobster and rockfish both carry California/CDFW + as-of 2026-08 + verify-current, and the bag limit is flagged as single-source. honest: uniquely flags the spliced '100 %' quote and its wrong co-cite, the single-sourced retreat arc that a second source contradicts, the inferred-from-upload-date yellowtail months, and the extrapolated dorado band; long explicit gaps list, absolute dates only. actionable: per-situation rig/gear/depth for bluefin, yellowfin, paddies, swordfish, bass, plus a changed pre-trip sequence.

<details><summary>Full prompt</summary>

What changes in the Southern California Bight from September into October, and how should my fishing change with it?

</details>

<details><summary><b>B2 — batch 2</b> · 11/12</summary>

## The short version

September and October are not two months of the same fishery — the KB treats them as **two different water regimes**. September is the *late* phase of the **warm-stable** regime; October is **fall fragmentation** (`conditions/water-regimes.md`, `seasonal/september.md`, `seasonal/october.md`). Everything below follows from that one flip.

One caveat up front: **you gave me no conditions and I did not pull any** (no BightSST, no reports). So this is the *pattern layer only* — priors that weight zones before you look at live water. The KB is explicit that the regime is read off the chart, not the calendar: "in an anomalous year trust the live water, not the calendar," and in a warm year a regime can arrive weeks early or grind late (`conditions/water-regimes.md`). Don't let the date on the wall tell you which of the two below you're in.

---

## 1. The plan stops being about spots and starts being about the chart

This is the single biggest change. October is the regime change where **"conditions become pretty important… look 100 % at your temp chart and chlorophyll"** (`seasonal/october.md`, `conditions/water-temperature.md`; 10/12/22 `XLVUhV8DW64`, 10/20/22 `OYOda6T3f-8`). Build the plan on **break structure, not spot names**.

In September you can still run a spot-and-species plan — the warm band is established, conditions hold day to day, the paddy field is seeded (`conditions/water-regimes.md`). In October the coast cools, the band **fragments**, and sharp SST breaks and edges reappear. Which *side* of the break you're on starts mattering more than the absolute number.

**The break-side rules (turn these on in October)** — `conditions/water-temperature.md`, `seasonal/october.md` (10/20/22 `OYOda6T3f-8`):

- **Bluefin: relative, not absolute.** Cool side of the break when the surrounding water is warm; warm side when the water is cold. Find the edge first, then pick the side by the overall regime.
- **Yellowfin: warmest × cleanest.** SST **max** crossed with chlorophyll **min**. Find the warmest water you can, then cross it against the chlorophyll chart for the cleanest of it.
- **Dorado: the coastal boundary.** They stack where cold-green beach water butts against warm-blue offshore water — reference band **~71–72 °F** (`species/dorado.md`, `E4vKwRaRueA`; 71.6 °F measured on a productive paddy). Fish the boundary line, not the middle of either mass.

Practical: look for **sharp gradients — offshore edges can jump multiple degrees in ~1 mile** (`conditions/water-temperature.md`), and give every chlorophyll pull a **freshness read** — a new cold-green bloom (overnight ~5 °F drop + green after an afternoon NW wind) is short-term *negative*, mark it for the recovery; the **edge of a mature bloom** is what you fish (`conditions/water-color.md`, `conditions/current-structure.md`).

## 2. The geography moves — and it moves away from you

**September:** weight the **"volume square" — SBI – San Nicolas – San Clemente – Catalina** — that block holds the **bigger bluefin** (`seasonal/september.md`, `locations/zone-lexicon.md`; 9/14/22 `5to3Q5P7w90`). It's a *region to work through*, not a point. Meanwhile **yellowfin volume near the border slides north with the warm water, and the bluefin slide with them** — follow the temperature, not last week's spot. **Dorado run in open-water schools below Catalina**, off structure (`seasonal/september.md`).

**October:** the warm band follows a repeatable retreat arc — **backside Santa Cruz / Rosa → Santa Barbara Island → backside Catalina → hooking to the 499 / Clemente** — and as the coast cools and fragments, **the bluefin condense outward to Tanner and Cortez** (`seasonal/october.md`, `locations/bight-geography.md`; `XLVUhV8DW64`, `OYOda6T3f-8`). Yellowfin, once fragmentation sets in, track the warmest water on the coast: **the West End of Clemente down through Mackerel Bank to the 181/182 Ridge** (`species/yellowfin-tuna.md`; 10/20/22 `OYOda6T3f-8`).

The planning consequence is a **range problem**. The Tanner/Cortez endgame is a long-range run — the KB's own observed trips put **Tanner ~90–100 mi west of Long Beach** and **Cortez ~110–115 mi from San Diego** (`species/bluefin-tuna.md`, observed, `ntQXxcH5sjI` and `UfuiWFVvz2E`, medium confidence, unregistered channel). If that's outside your boat, October means your bluefin program degrades and your *inshore/island* program becomes the plan.

## 3. Breadth goes up, density goes down

October is an **everything season, but scattered** — marlin, first swordfish, bluefin, yellowfin and dorado are all on the table simultaneously, with **low density of any one** (`seasonal/october.md`). September is more concentrated: the volume square for grade bluefin, a defined dorado program, yellowfin volume pushing north.

So change how you spend the day. Budget time by **box size**: a *complex* (the 43/181/182/289/Clemente Ridge type of water) is a half-day commitment; a *compact spot* (302, 371, west-of-Catalina) is a **20–30 minute read** — idle up, grade the meter, commit or leave (`locations/zone-lexicon.md`). In a scattered month, don't burn half a day proving a complex empty when the species menu is wide.

## 4. New doors open in October that were shut in September

- **Swordfish.** Season is **late September – December, peak October – mid-November** (`species/swordfish.md`). Requirements before you stop: **DSL present ≥ 600 ft, preferably ~950 ft / 150 fathoms or deeper**, and **DSL *plus* chunky bait balls at 100–150+ fathoms ≈ bites near-assured** — a bare layer is not a stop. Working depths **150–350 fathoms** on contour lines, thumbs, notches, humps. Hard weather gate: **>15 kt = no-go, comfortable 10–13 kt, drift ≤ ~2–2.5 kt** (a drift sock extends marginal days). Prefer **one big powerful "highway" break** over finger rips.
- **Striped marlin.** Fall is the window, marlin leading the everything-season from ~September through October; **tournament fleets are out by mid-September** (`species/striped-marlin.md`; `5to3Q5P7w90`, `XLVUhV8DW64`). They **live in the clear blue water**, working the seam where the dirty/bait water meets clean — jigs out on the bait edge *and* in the clean water (`HzE4FHHcvTk`). They're **slack-tide biters** — be on the highest-percentage spot **an hour before the tide change**. Fleet-reading tell: **outriggers up + circling = a tournament, not tuna** (`seasonal/october.md`; 9/14/22 `5to3Q5P7w90`).
- **Lobster.** Recreational spiny lobster season runs roughly **early October through mid-March** (California/CDFW jurisdiction, KB last checked **as of 2026-08** — **verify current dates, size, bag and gear counts with CDFW before you go**; `species/california-spiny-lobster.md`, `b19_AJjYCok`). Night fishery, **darkest no-moon nights best** — the opposite lean from the pelagic/bass moon doctrine (`conditions/moon.md`, `fri_BWI-VA0`). **5 nets per angler from a boat** (verify). Rig fishes ~**40–50 ft of rope**, but Catalina drops of **20–30 ft** are documented — match rope to the actual drop, and spread nets across depths early in the season rather than committing to one band.
- **Inshore bait events override the water read.** The October signature: **grunion-in-kelp events override water quality entirely** — **every-cast bass in ugly, stagnant water** you'd normally skip (`seasonal/october.md`, `species/calico-bass.md`; 10/20/22 `OYOda6T3f-8`). Match the bait: **7" split-tail slug on a sled/leadhead**, bass class. The tell is a **mixed bird pile *on* kelp/structure** — normally a mixed pile at an open-water current break is bait-only and you skip it, but on structure it can be the real event (`conditions/bird-reading.md`).

## 5. Report discipline changes — this is where people lose October

- **After the October full moon, "the tuna are gone" was a coverage illusion** — the fleet lost them and simply stopped reporting (`conditions/moon.md`; 10/12/22 `XLVUhV8DW64`). Late-season and post-moon, **absence of reports = coverage bias, not absence of fish** (`planning/report-reading-and-forecasting.md`; 10/12, 10/26/22 `XLVUhV8DW64`, `5p6gu14ZC4w`).
- **Age every report in miles.** Open-water bluefin not holding structure move **10–15 nm overnight** (7/21/22); Dave Hansen puts it at **20 miles** after a full-moon night for albacore/bluefin/yellowfin — both figures kept side by side, not averaged (`conditions/moon.md`, `fri_BWI-VA0`). Intraday they move at **low single-digit mph** (8/17/22 `HzE4FHHcvTk`). Draw a **box sized by the report's age**, not a pin.
- **Moon timing:** days **leading into** the full moon are the strongest documented bluefin windows (10/12/22 `XLVUhV8DW64`); the dissenting view (Hansen) is **7 days before AND after**, with the peak itself a travel period — and the morning after a full-moon night typically slow, **picking back up late in the day**. Working rule in the KB: full/new **±1 week** elevated, **leading days strongest**, the peak itself a **relocation event, not a bite-death**.
- **Widen toward the year-anniversary prior in fall.** "Go back to this date last year and the year before — pretty close to where they'll be," and the KB says the repeatability is **strongest in the fall run** (`seasonal/year-anniversary-prior.md`; `XLVUhV8DW64`). Kept side by side with Cameron's counter-model: for **yellowtail**, calendar date doesn't matter — the fish follow water temperature and bait, and calendar patterns are downstream of water state (source `cameron`). Use the anniversary as a **starting box** and let live water override.

## 6. Weather changes character

September's weather note is reassuring: **hurricane remnants are usually a non-event** — they break the heat, fishing largely unaffected (`seasonal/september.md`; 9/14/22 `5to3Q5P7w90`). Don't over-plan around a tropical system tracking up the Baja coast.

October is when the **Santa Ana** pathway starts appearing in the reports: Santa Anas **flatten the NW outer islands and open Rosa / Miguel** for shallow rockfish and lingcod (`conditions/sea-state.md`, `seasonal/november-december.md`; 10/20/22 `OYOda6T3f-8`, 11/23/22 `Z3rZqy2Pi8E`). The go/no-go is **2+ consecutive days of no-wind or Santa Anas** before committing to a Rosa/Miguel crossing. The flip side is the return-leg danger: an offshore NE Santa Ana pushes water back out against the prevailing motion and **stacks fast-building swell** — a boat caught at Avalon faces a multi-hour beat home into it (`conditions/sea-state.md`, `NC3-3pJDEgo`, medium confidence).

Also still in force: **homebound wind** — runs south into Mexican paddy water put a W wind on the return leg; plan return timing **against** the afternoon W build (8/17/22 `HzE4FHHcvTk`). And the go/bail thresholds: **wind >~12 kt raises whitecaps** (Hansen's personal cutoff), **sub-10-second swell interval is a hard bad-sea flag**, and **12–15 kt with 4–8 ft @ 9 s is a named unfishable combo** (`conditions/sea-state.md`, `NC3-3pJDEgo`, medium confidence, single mention).

---

## What to actually do differently — by program

**Offshore tuna.** September: work the **volume square** for grade, and read foamer *shape* before committing — **"jacuzzi" solid circular whitewater ≈ a bite every cast**; spread-out directional feeders are picky; wait for the school to ball up (`seasonal/august.md`; `HzE4FHHcvTk`, `HnqiE05vdXs`). October: lead with the chart, pick your break side, and expect to work edges rather than a zone. Don't skip good bluefin sign on a high SST number — the **76 °F "ceiling" is soft, not hard** (bluefin observed foaming in 76 °F, 9/14/22 `5to3Q5P7w90`; `conditions/water-temperature.md`).

Technique rows from `species/bluefin-tuna.md`:
- **Surface foamers** → poppers first (hold the zone longest), then surface iron, then a small lead bait; run ahead, stop hard, cast to the middle. Beefed **jig-stick class**. The bite comes on the **pause/fall**, not the pop.
- **Sounded 30–50 fm, wind up, no surface sign** → **knife-jigging** to graded marks; **100–130 lb-braid jig class (PE6–8)**, jigs **150–300 g** by day, **300–400 g** in more current or deeper.
- **Shallow bait-ball marks ~60 ft while chumming** → **yo-yo iron** through the mark, **40–60 lb class** stout rod + high-speed reel.
- **Big fish 100–300 lb, wind 8–15 kt** → **kite with a flying fish**, **150–200 lb class**. Too light to kite or fish too spread out → **speed-troll a Mad Mac at 13–15 kt** to cover water (a coverage need, not a sea-state call — `cameron`).
- **Chummed up / picky** → **flyline a sardine on a circle hook**, **40–60 lb class**, scale the leader down.

Yellowfin (`species/yellowfin-tuna.md`): **30 lb flyline class, 2/0 circle**, scaling to **15–20 lb leader and a size 1 thin-wire circle** when they get picky, plus the **bait-net freebie trick** (pitch 3–4 freebies with your hook bait mixed in). Their school marks sit **~40–50 ft down and rise to chum** — two minutes of chumming pulls them into casting range. Troll cedar plugs and feathers at **~6–6.5 kt** as a *search* tool. And remember the routing signal: **a surface yellowfin bite fires the bluefin**.

**Paddies.** The paddy program **peaks in August**, but October paddies still produce — the KB carries October observations of a paddy holding hundreds of dorado plus incidental yellowtail (Dave Hansen, 2022-10-12) and a 2.5-day trip that ran **south into warmer water off a dead overnight bluefin push** and found **60-plus dorado** on day one (`VWClGAn2WEw`, 2022-10-13, medium confidence). Keep the discipline: **fish move paddy-to-paddy only at night, so a dry paddy stays dry all day** — look, one sounder pass (**boomerang arcs typically 90–120 ft down**), one bait, **about a minute or two**, then move (`conditions/kelp-paddies.md`, `4xzK7YaXK5s`, `ZFqe49jRgA0`). Search the **line**, not the compass: open water, paddies align roughly **N–S**; near a bank edge they align **along the contour**. Weight the program **south** — best paddy water is south of SCI/Catalina and Dana Point to Oceanside southward; paddies are scarcer and hold less **north of Dana Point**. For tuna on a paddy, **stand off ~100 yards** rather than fishing tight to the kelp (`A6DJoXbID4c`, medium confidence).

**Yellowtail.** In the Bight, October is when the **squid-driven island zone** and the **structure/yo-yo game** come back to the front — SBI/Sutil fish as a squid-driven zone in both spring and the Oct–Nov fragmentation window; **~40 yellows in a day at Catalina in late October** is on the record, and **Farnsworth Bank gives good fall yo-yo fishing** (note the closure there: **only yellowtail and bonito may be kept** — verify current) (`species/yellowtail.md`; 10/26/22 `5p6gu14ZC4w`). Situation rows: **tight balls hugging structure / marks on hard bottom ~5–10 fm → yo-yo iron** (heavy full-size iron, Salas 6X class; hit bottom, **a couple cranks off the bottom = the reaction bite**) or **dropper loop**, on a **40–60 lb class stout rod + high-ratio reel**. Surface/paddy fish → **surface iron first**, then flylined bait, then stickbait; go heavier iron (Salas 7X) when it's windy to punch the cast out. If the squid drops deep or moves, **the bite dies but the fish did not leave** — relocate the forage on the meter before writing the zone off.

If your September is a **Baja/BOLA** program instead: at Bahía de los Ángeles in September the yellowtail are **on the bottom** — **dropper loops and yo-yo iron**, drop to marks on high structure and crank (source `cameron`, `seasonal/september.md`). Slow-pitch/vertical is the alternative over the same structure, **130–250 g**, **150–300 ft zone, biting best 150–180 ft** (`species/yellowtail.md`).

**Inshore bass.** October's transitional months "can pull another degree of warmth out of stable water" (`species/calico-bass.md`). Keep the **parallel-current rule** as the prior — parallel to shore good, **into** the beach marginal, **off** the beach dead — but know the **late-fall exception**: at San Clemente Island the bass bite *required* current running **into** the island with off-color water (11/23/22 `Z3rZqy2Pi8E`; `conditions/current-structure.md`). And on clear full moons, bass **gorge at night and shut down by mid-morning** — fish first light or late afternoon, not mid-day.

**Bottom fish.** Bonito **persist later into the season than most nearshore species** and show up in the fall island reports (`species/bonito.md`). Rockfish stays open but **closes at year-end** (CDFW, as of 2026-08, verify), with the **lings-shallow window** arriving in the Nov–Dec handoff behind a Santa Ana (`species/rockfish-lingcod.md`).

---

## If this is the Cameron profile (`profiles/cameron/boat.md`)

The 22-ft Panga out of **Dana Landing (Mission Bay)**, home waters **Coronado Islands, La Jolla, San Diego offshore banks**, changes the October read in three ways:

1. **The Tanner/Cortez condensation is not your fishery.** At ~110–115 mi from San Diego, that's the sportboat endgame. Your October bluefin/yellowfin play is the **warm, clean water that's still inside your range** — and the KB's October yellowfin geography (**Clemente West End → Mackerel Bank → 181/182 Ridge**) is the more realistic target than chasing the outer-bank condensation.
2. **Paddy geography is in your favor.** Best paddy water is **south of SCI/Catalina and Dana Point to Oceanside southward** — that's your water, not a run north.
3. **Weather gates bite harder.** No trim tabs, single 115 hp, **normal ~8 am departure**. The homebound-W-wind rule and the "if it's windier than forecast in the morning, assume it builds all day — a small boat bails early" heuristic (7/14/22) matter more in October than they did in flat late-summer mornings. Also add the **12–24 h wind hindcast** to every pull, not just the forward forecast (`conditions/sea-state.md`).

---

## What I could not answer from the KB

Listed plainly so you don't read confidence into silence:

- **No live conditions.** I pulled no BightSST and you gave none, so nothing above is a plan — it's the prior layer. Step 1 of `planning/day-plan-protocol.md` (per-spot SST/chlorophyll + wind/swell/current, observed *and* forecast, along the route too) is unrun.
- **No date for the flip.** The KB deliberately refuses to say "October 1 the regime changes" — it's read off the chart.
- **No moon or tide calendar** in the KB, so I can't tell you where this October's full moon or slack windows fall.
- **Trolling to locate yellowtail** is a **flagged stub** — no corpus source yet (`species/yellowtail.md`).
- **Yellowfin troll spread geometry** (setbacks, lure positions) is flagged **thin** — the corpus gives speeds only.
- **No albacore note** exists in this KB; albacore appears only in passing in the moon note.
- **No October-specific bait-availability doctrine** (sardine/anchovy/mackerel supply through the fall) for the Bight. The one "October on" bait-size note in the KB — downsized jig paras matching **~1–1.5 in bait** — is a **Sea of Cortez cabrilla** source (`lures/iron-jigs.md`, `EmZO8QiOfik`, medium confidence), not SoCal doctrine.
- **No fall-specific content for halibut** or the bay fisheries; barracuda is only noted as running "late spring into fall."
- **Regulatory specifics** (exact lobster opener, rockfish closure dates, bag/size limits, the Farnsworth closure terms) are carried in the KB only as of **2026-08** — verify all of them with CDFW before you fish.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/report-reading-and-forecasting.md`, `seasonal/september.md`, `seasonal/october.md`, `seasonal/august.md`, `seasonal/november-december.md`, `seasonal/year-anniversary-prior.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/current-structure.md`, `conditions/kelp-paddies.md`, `conditions/moon.md`, `conditions/sea-state.md`, `conditions/bird-reading.md`, `locations/bight-geography.md`, `locations/zone-lexicon.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/dorado.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/white-seabass.md`, `species/bonito.md`, `species/striped-marlin.md`, `species/swordfish.md`, `species/rockfish-lingcod.md`, `species/california-spiny-lobster.md`, `species/california-halibut.md`, `species/barracuda.md`, `species/sand-bass.md`, `lures/iron-jigs.md`, `profiles/cameron/boat.md`, `sources/transcripts/_manifest.csv`  
*videos:* `5to3Q5P7w90`, `XLVUhV8DW64`, `OYOda6T3f-8`, `5p6gu14ZC4w`, `HzE4FHHcvTk`, `HnqiE05vdXs`, `Z3rZqy2Pi8E`, `6TBxHnkYXI0`, `DnSqw4r7A1s`, `E4vKwRaRueA`, `4xzK7YaXK5s`, `ZFqe49jRgA0`, `fri_BWI-VA0`, `NC3-3pJDEgo`, `b19_AJjYCok`, `lxFNVdDhMy4`, `VWClGAn2WEw`, `A6DJoXbID4c`, `ntQXxcH5sjI`, `UfuiWFVvz2E`, `EmZO8QiOfik`, `cameron`  
*gaps admitted:* No live conditions were supplied and none were pulled (no BightSST), so step 1 of the day-plan protocol is unrun — this is the prior layer only, not a plan. | The KB gives no calendar date for the September-to-October regime flip; it insists the regime be read off live SST/chlorophyll, not the month. | No moon calendar or tide tables in the KB, so specific October full/new-moon and slack windows cannot be stated. | Trolling hard baits/feathers to LOCATE yellowtail is a flagged stub in species/yellowtail.md — no corpus source yet. | Yellowfin trolling spread geometry (setback distances, lure positions in the pattern) is flagged as a thin area — the corpus gives troll speeds only. | No albacore note exists in this KB; albacore appears only in passing in conditions/moon.md. | No October-specific bait-availability doctrine (sardine/anchovy/mackerel supply through fall) for the Bight; the one 'October on' bait-size note is a Sea of Cortez cabrilla source, not SoCal doctrine. | No fall-specific content for California halibut or the bay/harbor fisheries; barracuda carries only a broad 'late spring into fall' presence. | Regulatory specifics (exact lobster opener/closer, rockfish closure dates, bag/size limits, the Farnsworth Bank closure terms) are carried only as of 2026-08 and must be verified with CDFW. | Sight-fishing a finning/sunning swordfish — the classic SoCal surface sword encounter — is a flagged stub with no corpus source. | The KB gives no October-specific grade expectations for Bight bluefin/yellowfin (the only dated grade doctrine is the Nov Tanner/Cortez 300 lb fish reverting to sub-30 lb by mid-December).

</details>

<details><summary><b>B3 — batch 3</b> · 10/12</summary>

## The short version

September → October is the one **regime change** in the Bight's year that actually changes *how you plan*, not just what you catch. September is the tail of the **warm-stable regime**; October is **fall fragmentation** (`conditions/water-regimes.md`). In September you can pick a block of water and go. In October the water picks the spot for you: *"conditions become pretty important… look 100 % at your temp chart and chlorophyll"* (`seasonal/october.md`, 10/12 and 10/20/22 reports; sources `XLVUhV8DW64`, `OYOda6T3f-8`, `5to3Q5P7w90`).

One caveat up front: you didn't give me conditions, a launch point, or a range, and I have no live BightSST here — so everything below is the **prior layer**, not today's water (`planning/day-plan-protocol.md`). The profile in this KB (`profiles/cameron/boat.md`) has `range_nm` and `sea_state_max_ft` **null**, so per step 1b of the protocol I have to ask rather than assume: home port, usable range, and your sea-state ceiling. That matters a lot this month, because the October pattern pushes fish *outward*.

---

## 1. The water: one warm band becomes fragments

- **September (warm-stable, late):** an established warm band of clean water over the Bight, conditions holding day to day, the paddy field seeded and holding fish; the read is warmest × cleanest (`conditions/water-regimes.md`).
- **October (fall fragmentation):** the coast cools, the band **fragments** — sharp SST breaks and edges reappear, and the warm water tracks a retreat path and **condenses offshore** (`conditions/water-regimes.md`, `seasonal/october.md`).

**What you do differently:** stop planning off spot names. Pull SST **and** chlorophyll, find the **break**, then decide the species by which side of it you sit (`conditions/water-temperature.md`). Sharp offshore edges can jump multiple degrees in about a mile. A field example of the size of the swing: 74–75 °F at Cortez Bank one day, then 70 °F right at the Osborn Bank edge (about 1.5 mi off) and 72 °F where the boat sat the next — the crew explicitly "chasing cooler water," and the gray-light bite (~4:30–5:00 a.m.) in it was bluefin (`conditions/water-temperature.md`, `i3qIAHW-SJc`, medium confidence, unregistered channel).

Chlorophyll now has to be read for **age**, not just amount (`conditions/water-color.md`): an overnight ~5 °F drop plus green water after an afternoon NW blow is a **new cold bloom** — mark it for later, don't fish it today; the **edge of a mature bloom** is the now-asset. And don't default to the prettiest blue: bait holds in the dirtier water and predators work the **dirty/clean seam** (8/17/22).

## 2. Where they go: the fall track, and the run gets longer

The warm band moves through a repeatable sequence (`seasonal/october.md`, `locations/bight-geography.md`, `HzE4FHHcvTk`):

> **backside Santa Cruz / Rosa → Santa Barbara Island → backside Catalina → hooking to the 499 / Clemente**

and as the coast cools and fragments, **bluefin condense outward to Tanner and Cortez**.

Compare that with September, where the grade sat inside the Bight: the **volume square — SBI–San Nicolas–Clemente–Catalina — holds the bigger bluefin** in September (`seasonal/september.md`, `5to3Q5P7w90`), dorado run in open-water schools below Catalina, and the yellowfin volume near the border slides north with the warm water with bluefin trailing it.

So the October version of that same fish is a **fuel-and-sea-state question**. From the corpus: Tanner Bank is roughly **90–100 mi west of Long Beach**, fished at anchor in ~120 ft (`species/bluefin-tuna.md`, `ntQXxcH5sjI`); Cortez Bank is **~110–115 mi from San Diego**, anchored in **15–25 fathoms** (`species/bluefin-tuna.md`, `UfuiWFVvz2E`). If those are outside your envelope, the honest October plan is to fish the inside track of the band (backside Catalina, SBI, toward the 499/Clemente) and accept the grade that's there.

Yellowfin, meanwhile, invert the geography: once fragmentation sets in, their biggest concentrations track **the warmest water on the coast — the West End of Clemente down through Mackerel Bank to the 181/182 Ridge** (`species/yellowfin-tuna.md`, 10/20/22).

## 3. The break-side rules — the biggest single change in stop selection

This is the doctrine that barely matters in September and runs your day in October (`conditions/water-temperature.md`, `seasonal/october.md`):

| Species | Which water | Number to work with |
|---|---|---|
| **Bluefin** | **Cool side** of the break when the surrounding water is warm; **warm side** when it's cold — relative, never absolute | 76 °F ceiling is **soft**: bluefin were seen foaming in 76 °F (9/14/22). Treat a warm SST as evidence *against*, not an exclusion — don't skip good sign on the thermometer |
| **Yellowfin** | **Warmest × cleanest** — SST **max** crossed with chlorophyll **min** | Find the warmest water, then cross it with the chlorophyll chart |
| **Dorado** | The **green-cold / blue-warm coastal boundary** — fish the line, not the middle of either mass | reference band **~71–72 °F** (71.6 °F on a productive paddy, `E4vKwRaRueA`); a Mission Bay run read 69 °F near the harbor climbing to 71–72 °F about 7–13 nm out (`uyjTdgIw-1k`) |
| **Striped marlin** | Clean blue water **off the bait/color edge** — set the spread on the seam, not the empty blue or deep in the dirt (`species/striped-marlin.md`, `HzE4FHHcvTk`) | Slack-tide biters — be on your best spot **an hour before the tide change** (`6TBxHnkYXI0`) |

## 4. "Everything season, but scattered" — how you run the day changes

October is an **everything season**: marlin, first swordfish, bluefin, yellowfin and dorado all on the table — but **scattered**. Breadth of species, **low density of any one** (`seasonal/october.md`). Practical consequences:

- **Budget search time and carry a broader spread.** With fish spread out, **speed-troll a Mad Mac at 13–15 kt** to cover water and locate — that call is a *coverage* need, not a sea-state one (cameron); **kite** when the wind gives 8–15 kt and the fish are big (`species/bluefin-tuna.md`).
- **Use the anniversary prior as your starting box.** "Go back to this date last year and the year before — pretty close to where they'll be" (10/12/22), and it is **strongest in fall** (`seasonal/year-anniversary-prior.md`, `XLVUhV8DW64`). Better still, line up the last few days of catch positions and **project the travel line** forward. Cameron's counter-model is kept side by side and is worth holding: the calendar is an artifact, water state is what recurs — so shift the prior with the regime, not the date.
- **Age every report in miles.** Open-water bluefin not holding structure move **10–15 nm overnight**, so a 3-day-old position is stale, and after the moon "the tuna are gone" is usually **coverage bias**, not absence (`planning/report-reading-and-forecasting.md`, `conditions/moon.md`).

## 5. Doors that open in October that were shut in September

- **Swordfish.** Season is late **September – December**, **peak October – mid-November** (`species/swordfish.md`, sword seminar `yMiBtZ7k8-w` / `KuVwmfF6RAo`). Requirements before you stop: **150–350 fathoms** on contour lines/thumbs/notches, **DSL present at ≥600 ft** (prefer ~950 ft / 150 fm), and **DSL plus chunky bait balls at 100–150+ fm ≈ bites near-assured**. Weather gate is tight: comfortable **10–13 kt, >15 kt is a no-go, drift ≤ ~2–2.5 kt** (drift sock extends marginal days). Rig, from `techniques/deep-drop-swordfishing.md`: baits ride 100–250 ft below the layer, **averaging 800–1,100 ft**; **14/0 heavy forged offset circle** sewn to exit the top of the squid mantle; **7–10.5 lb breakaway lead** matched to drift; **80 lb braid → 25 ft of 200 lb wind-on → 10–15 ft of 200–300 lb leader**; one **LP-class light 10–15 ft above the bait** (green/blue standard, white early and late) — fishing with no light is a rigging failure. Two baits staggered, ~7–9 min to get both down. Moon: bites rise on **new and full and the flanking weeks**.
- **Lobster.** The recreational spiny lobster season runs roughly **early October through mid-March** (California/CDFW; the KB's numbers were last checked **as of 2026-08** — **verify current CDFW rules before you go**, they change) (`species/california-spiny-lobster.md`). Hoop nets on rock, riprap, boulder, reef and kelp edge **at night**; the standard rig fishes ~**40–50 ft of rope**, but Catalina work at **20 and 30 ft** is documented (`YQsbwfQ4wzY`), and early in the season the advice is to **spread nets across depths** rather than commit to one band (`Ow3an9lSVh4`). Moon lean is the **opposite** of the pelagic rule — **darkest, no-moon nights** are best (`conditions/moon.md`, `fri_BWI-VA0`), and once rain starts falling in season, the LA/Long Beach and San Diego harbor complexes get a strong crawl.
- **Marlin fleet is already out** — tournament fleets by mid-September. Read them correctly: **outriggers up + boats circling back over themselves = a marlin tournament, not a tuna stop** (`species/striped-marlin.md`, `seasonal/october.md`, 9/14/22). Don't crash it and start Mad-Mac-ing.
- **Grunion-in-kelp — the inshore wildcard that overrides everything.** When grunion pile into the kelp you get **every-cast bass in ugly, stagnant water** you'd normally skip — a bait event on structure beats a clean-water read (`seasonal/october.md`, 10/20/22). Match the bait: a **7" split-tail slug on a sled/leadhead**, every cast (`species/calico-bass.md`); the **mixed bird pile sitting on the kelp/structure** is the tell. This is the one October situation where you should deliberately ignore your own water-quality discipline.
- **Long range (Baja grounds, region-labeled — not the Bight):** October–November is named as the best wahoo window, with the 6–8 day boats starting Alijos Rocks / "the ridge" trips (`species/wahoo.md`, `9IhmYstB8sA`, `tjBeR9tWd4s`, `4uNPLknRAQg`).

## 6. The inshore/island game shifts too

- **Yellowtail.** They stay very much on the table, but the face changes. Catalina gives fall structure fish when the water holds — **~40 yellows in a day at Catalina in late October**, and "no reason you couldn't catch a yellowtail" while temps stay good (10/26/22, `5p6gu14ZC4w`). **Farnsworth Bank is good fall yo-yo ground** — note it sits in a closure where **only yellowtail and bonito may be kept**. SBI/Sutil runs as a **squid-driven zone** in the fall fragmentation window (Oct–Nov): take squid and you have a real shot; when the squid drops deep or moves, the bite dies but **the fish did not leave** — relocate the forage on the meter before writing the zone off (`species/yellowtail.md`). Practical switch: when a hard current pulls the kelp under or lays it flat, surface presentations are dead — **go vertical (yo-yo iron, dropper loop)**, and switch back to surface iron when the kelp resurfaces (`techniques/yo-yo-iron.md`).
- **Calico bass.** The fall fragmentation months (October into December) can pull another degree of warmth out of stable water, so the kelp bite doesn't just stop (`species/calico-bass.md`). The **parallel-current rule** still governs: current parallel to the shoreline is good, straight into the beach is marginal, **straight off the beach is dead** — but hold the late-fall exception in mind, because at San Clemente Island in late fall the bass bite *required* current running **into** the island with off-color water (`conditions/current-structure.md`, `seasonal/november-december.md`, 11/23/22, `Z3rZqy2Pi8E`).
- **White seabass** stays moon- and slack-driven, on squid near island structure in **60–100+ ft**, best in **gray light and after dark**; October is one of the months the note flags (`species/white-seabass.md`).
- **Bonito** persist later than most nearshore species — "doing good on the bonito" is a common line in Oct–Nov island reports (`species/bonito.md`).

## 7. Weather and logistics change character

- **September:** hurricane remnants tracking up the Baja coast are **usually a non-event** that breaks the heat with the fishing unaffected (9/14/22) — don't over-plan around one, though post-storm water can still roll over (`seasonal/september.md`).
- **October onward:** **Santa Ana events flatten the NW outer islands** and are the trigger to run Santa Rosa / San Miguel for shallow rockfish and lings (10/20/22, 11/23/22 — `conditions/sea-state.md`, `seasonal/november-december.md`). The stated go/no-go is **2+ consecutive days of no-wind or Santa Ana** before committing to a Rosa/Miguel crossing. The flip side: a Santa Ana is a **NE offshore blow**, and the return leg is where it hurts — 25–45 kt was observed at Avalon in one, stacking a fast-building sea against a boat trying to get back to Newport/Dana (`NC3-3pJDEgo`, 2020-11-18).
- **NW blows don't hit the Bight evenly** (`locations/bight-geography.md`, `HzE4FHHcvTk`): the **northern Channel Islands and the LA/Ventura shelf get crushed** — a strong NW event can roll surface temps down **5–8 °F** there; **south of Newport is less prone**; the **Coronados, the tuna grounds, Catalina and San Clemente held their water** through one documented blow. That map is exactly how you re-pick a zone after an October wind event.

---

## What I'd actually change on the boat, in order

1. **Change the pre-trip sequence.** September: pick the zone, then check conditions. October: pull SST + chlorophyll first, find the strongest break, *then* choose the species by which side you're on.
2. **Carry a wider kit than in September** — it's an everything-season. Cast/foamer gear plus **knife jigs 150–400 g** (day 150–300 g; more current or deeper fish → 300–400 g), a **40 lb flyline** setup with circle hooks for bluefin, **yo-yo iron** for Catalina/Farnsworth and for when the current lays the kelp flat, and bass gear for a grunion event (`species/bluefin-tuna.md`, `techniques/yo-yo-iron.md`).
3. **Plan a search, not a stop.** Expect to run the band. If you can't reach the Tanner/Cortez condensation, plan the inside track and don't chase reports that are 3 days and 30 miles old.
4. **Time the day on slack and low light,** not on departure convenience: marlin and bluefin foamers on the slack (be on the spot an hour before the change), WSB in gray light and after dark, swordfish on the new/full and flanking weeks.
5. **Give me your launch point, range and sea-state ceiling** and I'll filter the above to what's actually reachable, then resolve gear against your rod/tackle list rather than class terms.

---

## What this knowledgebase does *not* answer

I want to be explicit about the edges here rather than paper over them — several are things you'd reasonably expect in a September→October answer:

- **No live conditions.** I have no BightSST here, so nothing above is current intel — it's the pattern layer only.
- **No typical SST numbers by month.** The KB never gives "September usually runs X °F, October Y" for the Bight. The break-side rules are relative on purpose.
- **No stated end-of-season for dorado or yellowfin in the Bight.** The KB says dorado build through fall and documents loaded paddies well into October, but never says when they leave.
- **No fall-specific kelp-paddy behavior.** Paddy alignment doctrine is given for the *summer* uphill current (N–S lines, or along the contour near a bank edge); there's no October statement about paddy abundance or alignment changing.
- **No grunion-run calendar.** The KB gives the override rule ("grunion-in-kelp beats water quality") but nothing about when grunion events happen or how to anticipate one.
- **No moon calendar.** Windows are stated as full/new ±1 week with the leading days strongest; you have to supply October's actual dates.
- **No fall bait-availability note** — nothing on squid/sardine/anchovy receiver availability shifting between September and October.
- **Thin on the fall transition for barracuda, sand bass and halibut.** Barracuda are logged only as "late spring into fall," and sand bass jump from the summer spawn straight to the winter deep-structure program; there's no October-specific behavior for either.
- **Rockfish/lingcod October specifics are absent.** The KB has the year-end closure (roughly Jan–Feb depending on the CDFW annual regs, as of 2026-08 — verify) and the **Nov–Dec** lings-shallow window, but nothing about October depth limits or October behavior.
- **No exact current-year regulatory dates** — lobster opener, rockfish depth constraints and bag limits all carry "verify current CDFW rules" flags rather than dates you can fish off.


*notes:* `README.md`, `planning/day-plan-protocol.md`, `planning/report-reading-and-forecasting.md`, `seasonal/september.md`, `seasonal/october.md`, `seasonal/november-december.md`, `seasonal/year-anniversary-prior.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/current-structure.md`, `conditions/sea-state.md`, `conditions/moon.md`, `conditions/kelp-paddies.md`, `locations/bight-geography.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/dorado.md`, `species/yellowtail.md`, `species/calico-bass.md`, `species/white-seabass.md`, `species/striped-marlin.md`, `species/swordfish.md`, `species/bonito.md`, `species/barracuda.md`, `species/sand-bass.md`, `species/rockfish-lingcod.md`, `species/california-spiny-lobster.md`, `species/wahoo.md`, `techniques/deep-drop-swordfishing.md`, `techniques/yo-yo-iron.md`, `profiles/cameron/boat.md`, `sources/extraction-log.md`  
*videos:* `5to3Q5P7w90`, `XLVUhV8DW64`, `OYOda6T3f-8`, `HzE4FHHcvTk`, `6TBxHnkYXI0`, `i3qIAHW-SJc`, `E4vKwRaRueA`, `uyjTdgIw-1k`, `5p6gu14ZC4w`, `Z3rZqy2Pi8E`, `NC3-3pJDEgo`, `ntQXxcH5sjI`, `UfuiWFVvz2E`, `yMiBtZ7k8-w`, `KuVwmfF6RAo`, `fri_BWI-VA0`, `YQsbwfQ4wzY`, `Ow3an9lSVh4`, `9IhmYstB8sA`, `tjBeR9tWd4s`, `4uNPLknRAQg`  
*gaps admitted:* No live BightSST conditions were pulled — the answer is the prior/pattern layer only, not current intel. | The KB gives no typical monthly SST norms for the Bight (no 'September runs X °F, October Y °F' baseline). | No stated end-of-season or departure timing for dorado or yellowfin in the Southern California Bight. | No fall-specific kelp-paddy doctrine — paddy alignment/abundance rules in the KB are written for the summer uphill current only. | No grunion-run calendar or mechanism for anticipating a grunion-in-kelp event; the KB only states the override rule. | No moon-phase calendar for October — the KB gives full/new ±1 week windows but no dates. | No note on fall live-bait availability (squid, sardine, anchovy) or how receiver bait changes September into October. | Barracuda, sand bass and California halibut have no October-specific fall-transition behavior in the KB. | Rockfish/lingcod have no October-specific behavior or depth-limit detail; only the Nov–Dec lings-shallow window and the year-end closure. | Exact current-year regulatory dates are absent — lobster opener, rockfish closure dates and depth constraints all carry 'verify current CDFW rules' flags. | The active user's boat envelope is unknown: profiles/cameron/boat.md has range_nm and sea_state_max_ft null, so reachability of the Tanner/Cortez condensation could not be filtered.

</details>

<details><summary><b>NOW — review</b> · 12/12</summary>

# September → October in the Bight: the regime flips, and the chart replaces the spot list

**Two caveats up front, per [`planning/day-plan-protocol.md`](planning/day-plan-protocol.md):** I have no live conditions (no BightSST pull in this session), so everything below is the **prior/pattern layer** — the KB is explicit that "a stale report is not today's water" ([`seasonal/october.md`](seasonal/october.md)). And you gave me no profile, so I could not run protocol step 1b (the `{regions, waters}` envelope from your launch point, `range_nm` and `sea_state_max_ft`). Gear below is therefore in **class terms**, not your gear.

---

## 1. The headline change: warm-stable → fall fragmentation

This is the single most important thing. September is the **late warm-stable regime**; October is **fall fragmentation** ([`conditions/water-regimes.md`](conditions/water-regimes.md), [`seasonal/september.md`](seasonal/september.md), [`seasonal/october.md`](seasonal/october.md)).

| | September (late warm-stable) | October (fall fragmentation) |
|---|---|---|
| Water state | Established warm band of clean water over the Bight; conditions hold day to day; paddy field seeded and holding | Coast cools, the warm band **fragments**; sharp SST breaks and edges reappear; the band tracks a retreat path and condenses offshore |
| What you plan on | The warmest × cleanest combination across a broad, stable field | **Which side of a break** you're on, and where the band condensed to |
| Fish distribution | Dispersed but concentrated in known blocks | **Everything season, but scattered** — breadth of species, low density of any one (`XLVUhV8DW64`) |
| Spot names | Usable | Weak. "Build the plan on the break structure, not on spot names" |

The operating line from the corpus: *"conditions become pretty important… look 100% at your temp chart and chlorophyll"* (`OYOda6T3f-8`). **Honesty flag:** the KB itself marks this quote as spliced from two non-adjacent passages ~4 minutes apart in one transcript, and notes the co-cited `XLVUhV8DW64` never says either half ([`seasonal/october.md`](seasonal/october.md), [`conditions/water-regimes.md`](conditions/water-regimes.md)). The *sense* is corroborated; treat the "100%" framing as one captain's emphasis, not a measured rule.

**Practical consequence:** in September you can plan a zone and go. In October, pull SST + chlorophyll first and let the break structure pick the zone. Find the **breaks** — sharp gradients, which offshore can jump multiple degrees in ~1 mi — not just the warmest cell ([`conditions/water-temperature.md`](conditions/water-temperature.md)).

---

## 2. The break-side rules become the operative read

In September the read is "warmest × cleanest, broadly." In October, **which side of the edge you sit on** matters more than the absolute number ([`conditions/water-temperature.md`](conditions/water-temperature.md), [`seasonal/october.md`](seasonal/october.md)):

- **Bluefin — relative, not absolute.** They sit the **cool side of a break when the surrounding water is warm**, and the **warm side when it's cold** (`OYOda6T3f-8`). A bank-edge trip matched this: bluefin held the cooler **70–72 °F** water at a bank edge while yellowtail and yellowfin sat in warmer water nearby (`i3qIAHW-SJc`).
- **Yellowfin — warmest × cleanest.** SST **max** × chlorophyll **min** (`OYOda6T3f-8`, `XLVUhV8DW64`). One SoCal fall bite sat over **72 °F** (`SczdZIq3UmE` — flagged in [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md) because the source says only "it's 72 degrees" without stating it's a water reading).
- **Dorado — the boundary.** Green-cold coastal water against blue-warm offshore, reference **~71–72 °F**, with **71.6 °F** measured on a productive paddy (`E4vKwRaRueA`). Fish the boundary line, not the middle of either mass. (Flagged: the ~71–72 band is extrapolated from that single reading — [`species/dorado.md`](species/dorado.md).)
- **Marlin — the clear side of the bait seam.** Target **68 °F** before dropping jigs, with fished water at **69.3–69.4 °F** (`3qSY328fFYo`).

Don't over-read a high SST against bluefin: the **76 °F ceiling is soft, not hard** — fish were logged foaming in 76 °F water (`5to3Q5P7w90`). Warm SST is *soft evidence against*, never an exclusion ([`conditions/water-temperature.md`](conditions/water-temperature.md)).

Second axis, and it gets more important, not less: **bait beats clarity**. Bait was found holding in dirtier water while clean blue sat empty (`HzE4FHHcvTk`), and bluefin transit the chalky dirty/clean transition because the dirty side holds the bait (`HWx1jDTGsng`) ([`conditions/water-color.md`](conditions/water-color.md)). Also attach an **age** question to every chlorophyll pull: a fresh cold-green bloom after a NW blow (overnight ~5 °F drop) is a *later* asset — mark it and come back; a **mature bloom edge** is the now asset (`h3PTupup17I`).

---

## 3. The geography moves — stop fishing September's block

**September's prior:** the **volume square — Santa Barbara Island – San Nicolas – San Clemente – Catalina** holds the bigger bluefin (`5to3Q5P7w90`, [`seasonal/september.md`](seasonal/september.md)). Yellowfin volume sits near the border and slides north with the warm water, bluefin sliding with them.

**October's prior:** the warm band moves along a repeatable arc and then condenses ([`locations/bight-geography.md`](locations/bight-geography.md), `OYOda6T3f-8`):

> backside Santa Cruz / Rosa → **Santa Barbara Island** → **backside Catalina** → hooks to the **499 / Clemente** → West End of Clemente through the macro bank and the **181/182 ridge** down to the corner

…and as the coast cools and fragments, **bluefin condense outward toward Tanner and Cortez**, working the zone between the **381** (east end, backside Clemente) and Tanner/Cortez, on the cooler side of the same band.

**Honesty flag, and it's load-bearing:** the KB marks this whole arc and the Tanner/Cortez condensation as **single-source** — attested only in `OYOda6T3f-8`, with `XLVUhV8DW64` explicitly *not* supporting it (it describes fish "spread all over the place") ([`locations/bight-geography.md`](locations/bight-geography.md), [`locations/tanner-bank.md`](locations/tanner-bank.md), [`conditions/water-regimes.md`](conditions/water-regimes.md)). Use the arc as a search prior, not a promise.

**Tanner/Cortez is a real commitment** ([`locations/tanner-bank.md`](locations/tanner-bank.md)): Tanner at **32°42.000'N 119°08.000'W**, Cortes at **32°26.417'N 119°07.833'W**, **15.6 nm** apart on a near-due-N/S line. The corpus states the run in statute miles: **96 mi SW of San Pedro**, **111 mi west of Point Loma**, ~110–115 mi from San Diego; from Long Beach about **90 mi to Tanner** vs **110 mi to Cortes**. That's a full overnight sportboat run — it's an envelope decision before it's a fishing decision. Working depths there: **15–25 fathoms** at anchor with the high spot in **~120 ft**, the drop-off edge worked at **50–60 fathoms**, night jig marks **50–80 fathoms and below**.

**Yellowfin geography** shifts too: once fragmentation sets in, concentrations track the warmest water — **West End of San Clemente Island → Mackerel Bank → the 181/182 Ridge**, with the bigger **50 lb** fish off the **front side of Clemente** (`OYOda6T3f-8`, [`species/yellowfin-tuna.md`](species/yellowfin-tuna.md)). (Flagged: "typically October" is the KB's generalization; the source describes one dated season.)

**One dated bridge item worth knowing:** on **backside Catalina**, "end of September into the first week of October," dolphin-associated yellowtail/yellowfin produced **60–70 lb** yellowfin off pods on a finesse-trolled lure, during the lobster opener (`ouBrIdO7d4k`, [`locations/catalina-island-backside.md`](locations/catalina-island-backside.md)). That's exactly the window you're asking about.

---

## 4. What to add: swordfish switches on

This is the biggest *new* opportunity between the two months ([`species/swordfish.md`](species/swordfish.md), `yMiBtZ7k8-w`):

- **August:** five trips without a bite.
- **September:** a couple.
- **October: a bite a trip if not more.**

January–August the fish are there and the fuel isn't justified. Late September through December is the window. (Flagged: the "October to mid-November peak" is the KB's envelope of two non-overlapping years — 2019 ran late-September into a red-hot October, 2020 peaked ~10 days before Thanksgiving.)

**The go/no-go and the setup** ([`techniques/deep-drop-swordfishing.md`](techniques/deep-drop-swordfishing.md)):

- **Ground:** deep contour structure in **150–350 fathoms** — contour lines, thumbs, notches, humps. Worked ground includes the Ridge, 9 Mile Bank, 14 Mile Bank, the 43, the 178, the 302, and the 138/182 on break days.
- **Meter gate:** DSL present at **≥600 ft** *and* chunky bait balls at **100–150+ fathoms**.
- **Baits:** **800–1,100 ft**, roughly **100–250 ft below** the layer — a DSL read at 850 ft puts the bait at about 900 ft. One worked drift at the 178 sat in about **1,090 ft**, inside the **900–1,400 ft** band the fishery covers (`KuVwmfF6RAo`).
- **Weather gate:** **above 15 kt nobody fishes**; **10–13 kt** is the working max in the traditional NW; above roughly **2–2.5 kt** of drift the presentation dies. A **drift sock** extends marginal days.
- **Tempo:** two rods staggered to different depths, ~**7–9 minutes** to get both baits down.
- Set the drift **up-current of the fathom line** so the bait sweeps the structure; west-coast model is to set up and let fish come along the fathom-curve highways.

Hooking is not landing — one San Diego program pulled on **30-plus** fish across 2019–2020 and rates boating them the hard part.

---

## 5. Species by species: keep, change, drop

**Bluefin** ([`species/bluefin-tuna.md`](species/bluefin-tuna.md)) — still on, but the search prior moves outward and the break-side rule takes over from "go to the square." Three presentations that share almost no gear, so rig for the read you expect:

- **Sounded deep, 30–50 fathoms, no surface sign** → knife-jigging, **100–130 lb braid jig class (PE6–8)**; day 150–300 g, more current or deeper → **300–400 g**. (Internal conflict flagged: the linked Searcher ladder makes ~100 g the most-used daytime jig.)
- **Deep marks at captain-called depth, ~100–200 ft** → flat-fall, free-spool to the mark, most bites **on the fall**, wind halfway and re-drop; two-speed **rail-rod class**.
- **Surface foamers, terns working** → foamer casting, beefed **jig-stick class** for 200 lb fish; the bite comes on the **pause/fall**.
- **Big fish 100–300 lb, wind ~8–15 kt** → kite with a flying fish, **150–200 lb class** (flagged: the kite note itself gives no wind numbers).
- **Too light to kite, or fish too spread out to sit on** → speed-troll a Mad Mac at **13–15 kt** to cover water (flagged: the Mad Mac note says 13–14 kt). This coverage-vs-density call matters more in October precisely *because* the fish are scattered.
- Bank marks at the outer banks run **50–80 fathoms**; night DSL marks **180–330 ft**.

**Yellowfin** ([`species/yellowfin-tuna.md`](species/yellowfin-tuna.md)) — arrives with late warm-stable and runs **through** fall fragmentation, so October is not a drop-off. Grade **8–10 up to 40–50 lb, 15–25 lb average** (`8M4QhL-Qb7E`). Flyline a sardine, **30 lb class, 2/0 circle**, stepping leader/hook down to **15 lb and size 1** when they get picky. Troll cedar plugs and feathers at **~6–6.5 kt** as a *search* tool, then stop and convert. A surface yellowfin bite is a routing signal: when yellowfin are up on lures, nearby bluefin become more cooperative (`CMQkHQMxbXM`).

**Dorado** ([`species/dorado.md`](species/dorado.md)) — September holds them in **open-water schools below and behind Catalina** (`5to3Q5P7w90`, flagged as one ASR-garbled report); through October they stay on the table but scattered. SoCal grade **8–15 lb with fish to 30 lb** (`P9H-bpzT7eU`); ~15 mi off San Diego is the typical big-concentration zone. Abundance swings hard year to year — carry the tackle rather than packing it for a known run.

**Paddy program** ([`conditions/kelp-paddies.md`](conditions/kelp-paddies.md)) — August is the peak; September/October it's still the mechanism that concentrates dorado, paddy yellows and yellowfin, but run it with discipline:
- **Geometry:** open water, paddies line up roughly **N–S** under the uphill current; near a bank edge they line up **along the contour**. Search the line, not the compass.
- **Freshness:** fish move paddy-to-paddy **only at night**, so a dry paddy stays dry all day. Drive straight up "like it's the dock," look for visible fish, then sounder for **boomerang arcs at 90–120 ft**; give it **about a minute, maybe two** — a look, a sounder pass, one bait — then move.
- **Where:** best paddy water is **south of San Clemente/Catalina** and **Dana Point to Oceanside southward**; scarcer and less holding **north of Dana Point** (`HzE4FHHcvTk`).
- A paddy showing skipjack isn't dead — better-grade tuna can push them out later (`Ow3an9lSVh4`).

**Striped marlin** ([`species/striped-marlin.md`](species/striped-marlin.md)) — mid-August through October, and it *leads* the everything season. Short tight lure spread on the clean side of a bait/color seam, live mackerel staged the whole troll for a dropback. They bite around **slack tide**, and a raised fish converts about **one in five or six** (hedged in-source, scoped to jig fish). A body of fish holds an area anywhere from **six to eight weeks down to six to eight days** — last week's area may be empty. October fleet-reading tell: **outriggers + circling = a tournament, not tuna** (`5to3Q5P7w90`).

**Yellowtail** ([`species/yellowtail.md`](species/yellowtail.md)) — island fish keep biting while the water holds, and paddy yellows still show as bycatch on dorado-dominated paddies. **Honesty flag:** the KB marks this October/November framing as *not stated* in any of its three cited sources — the months are inferred from upload dates. Rig all three faces (surface iron, yo-yo/dropper, flyline) since the face flips by the hour. Island and bank fish key on **squid presence more than the month**.

**Inshore — this is where October gives you a genuine wildcard.** **Grunion-in-kelp events override water quality entirely** (`OYOda6T3f-8`): when grunion pile into the kelp you get **every-cast bass for two hours in ugly, stagnant, no-current water** you'd normally skip ([`seasonal/october.md`](seasonal/october.md), [`species/calico-bass.md`](species/calico-bass.md)). Match the bait — **7" split-tail slug on a sled or leadhead**, every cast. The tell is a **mixed bird pile sitting *on* kelp/structure**, which is the stated exception to the usual "mixed pile at an open-water current break = bait only, skip" rule ([`conditions/bird-reading.md`](conditions/bird-reading.md), `Blh2BA-7Ono`).

Calico preference band is **65–68 °F**; past about 70 °F they get lethargic and drop to cooler water ([`species/calico-bass.md`](species/calico-bass.md), `LqW32NSkObY`) — so a cooling October actually walks the inshore water *toward* their band. Worked depths off Dana Point: **0–8 ft** and **20–100 ft**.

**Bonito become the fallback.** By late October inside Catalina "you're mostly against Bonita, bass and Rockfish this time of year" (`5p6gu14ZC4w`), and October sport boats are "doing good on the Bonita" (`OYOda6T3f-8`) ([`species/bonito.md`](species/bonito.md)). Bonito hours and yellowtail hours aren't the same hours — the yellowtail window is the morning, then it becomes a pick-o day.

---

## 6. Two calendar items that are regulation, not fishery

- **Spiny lobster opens.** The recreational season runs roughly **early October through mid-March** — this is a real September→October change ([`species/california-spiny-lobster.md`](species/california-spiny-lobster.md)). **California / CDFW, as of 2026-08 — verify with CDFW before you fish.** The KB flags that **no corpus source actually states the October opener** (only the 2024 close, March 20, `Q196GVwVqro`), so the opener date specifically needs a CDFW check. Program: baited hoop nets after dark on rock, riprap and kelp edge; nets fish **20–55 ft** (Catalina **20–30 ft**, general big-boat **25–30 ft**, Mission Bay **25–35 ft**, San Diego Bay as deep as **55 ft**); **5 nets per angler, 10 per boat**, 2 per person from shore/pier; **3.25 in** carapace minimum; fishing licence **plus** a lobster report card filled out *before* you fish (gear code 1); every buoy carries name + GO ID. Bag limit **7/day** is flagged single-source from one garbled 2019 seminar aside — verify. Lobster are only catchable **while crawling**, and the crawl runs a bounded stretch of the night then stops.
- **Rockfish/lingcod** does *not* change between September and October — it's open most of the year and closes at year-end (California / CDFW, as of 2026-08; verify) ([`species/rockfish-lingcod.md`](species/rockfish-lingcod.md)). The lings-shallow window is a **November–December** item, not yet ([`seasonal/november-december.md`](seasonal/november-december.md)).

---

## 7. How your *process* should change

1. **Invert the order of operations.** September: pick zone, check conditions. October: pull the temp/chlorophyll chart, find the break, *then* pick the zone ([`seasonal/october.md`](seasonal/october.md)).
2. **Budget for search, not for a spot.** Everything season, but scattered — expect breadth of species and low density of any one. Trolling is a search tool as much as a catch method.
3. **Lean on the year-anniversary prior.** It's a location prior *within* fall fragmentation and is strongest exactly now: "go back to this date last year and the year before — pretty close to where they'll be" (`XLVUhV8DW64`). Project the travel line forward from recent positions rather than anchoring one point ([`seasonal/year-anniversary-prior.md`](seasonal/year-anniversary-prior.md)). Single-source flagged.
4. **Handle the October full moon correctly.** After the October full moon, "the tuna are gone" was a **coverage illusion** — the fleet lost the fish and stopped reporting ([`conditions/moon.md`](conditions/moon.md), `XLVUhV8DW64`). Discipline: heavily discount report persistence, treat absence of reports as coverage bias, treat the moon peak as a *relocation event*, and widen toward same-date prior-year positions. Open-water bluefin not holding structure move **10–15 nm overnight** (`Blh2BA-7Ono`). The morning after a full-moon night runs slow — if you must fish the full moon, fish it **late** rather than pushing the early window (`fri_BWI-VA0`).
5. **Stop over-planning around tropical systems.** Hurricane remnants are usually a **non-event** that breaks the heat with the fishing unaffected (`5to3Q5P7w90`, [`seasonal/september.md`](seasonal/september.md)).
6. **Start watching for Santa Anas** — they're the November–December trigger that flattens the NW outer islands and opens Rosa/Miguel, and they carry a real return-trip risk from Avalon ([`conditions/sea-state.md`](conditions/sea-state.md), [`seasonal/november-december.md`](seasonal/november-december.md)). Not yet an October program, but it's what's next.

---

## 8. What the KB does not tell you

- **No numeric threshold for "fragmentation has arrived."** The regime is read qualitatively off the chart, so I can't pin the Sept/Oct boundary to a date or an SST value — and the KB is explicit that in an anomalous year you plan from the regime, not the month note ([`conditions/water-regimes.md`](conditions/water-regimes.md)).
- **No way to predict a grunion-in-kelp event** — only the doctrine that one overrides the water read once you find it.
- **No October moon phases or tide/slack times** are in the KB — the slack-tide marlin window and the lobster crawl both need a separate almanac pull.
- **No live conditions and no profile** in this session, so no zone recommendation, no transit plan, and no owned-gear resolution.

If you give me your launch point, range and sea-state limit, I can run protocol step 1b properly and narrow this to the zones actually inside your envelope.


*notes:* `README.md`, `CLAUDE.md`, `planning/day-plan-protocol.md`, `planning/report-reading-and-forecasting.md`, `seasonal/september.md`, `seasonal/october.md`, `seasonal/august.md`, `seasonal/november-december.md`, `seasonal/year-anniversary-prior.md`, `conditions/water-regimes.md`, `conditions/water-temperature.md`, `conditions/water-color.md`, `conditions/kelp-paddies.md`, `conditions/bird-reading.md`, `conditions/moon.md`, `conditions/sea-state.md`, `locations/bight-geography.md`, `locations/tanner-bank.md`, `locations/catalina-island-backside.md`, `species/bluefin-tuna.md`, `species/yellowfin-tuna.md`, `species/dorado.md`, `species/yellowtail.md`, `species/striped-marlin.md`, `species/swordfish.md`, `species/white-seabass.md`, `species/calico-bass.md`, `species/bonito.md`, `species/california-spiny-lobster.md`, `species/rockfish-lingcod.md`, `techniques/deep-drop-swordfishing.md`  
*videos:* `5to3Q5P7w90`, `XLVUhV8DW64`, `OYOda6T3f-8`, `yMiBtZ7k8-w`, `KuVwmfF6RAo`, `E4vKwRaRueA`, `P9H-bpzT7eU`, `i3qIAHW-SJc`, `3qSY328fFYo`, `6TBxHnkYXI0`, `HzE4FHHcvTk`, `HWx1jDTGsng`, `8M4QhL-Qb7E`, `CMQkHQMxbXM`, `SczdZIq3UmE`, `ZFqe49jRgA0`, `4xzK7YaXK5s`, `DnSqw4r7A1s`, `-JZpyWLdKlk`, `8XrMkWPRxgs`, `8THSuqoPI_Q`, `Ow3an9lSVh4`, `5p6gu14ZC4w`, `Blh2BA-7Ono`, `ouBrIdO7d4k`, `Q196GVwVqro`, `b19_AJjYCok`, `JiJYamo0QHk`, `Qs9oEsh3b_w`, `YQsbwfQ4wzY`, `cEscIy278ew`, `EiItVWqFMYc`, `Z3rZqy2Pi8E`, `fri_BWI-VA0`, `LqW32NSkObY`, `h3PTupup17I`, `HcEh5KOYTH4`, `CrLDC4O8qS8`, `VWClGAn2WEw`  
*gaps admitted:* No live BightSST conditions were pulled in this session, so the answer is the prior/pattern layer only — the KB states priors are not current intel. | No angler profile or trip envelope (boat, range_nm, sea_state_max_ft, home port, rod inventory) was supplied, so day-plan-protocol step 1b could not be run and all gear is given in class terms rather than owned gear. | The KB gives no numeric threshold or trigger declaring that the fall-fragmentation regime has arrived — the regime is read qualitatively from the temp/chlorophyll chart, so the September/October boundary cannot be pinned to a date or an SST value. | The KB gives no way to predict when an October grunion-in-kelp event will occur — only the doctrine that such an event overrides the water read once found. | No October moon phases or tide/slack times exist in the KB; the slack-tide marlin window and the lobster crawl timing both require a separate almanac pull. | The exact CDFW spiny-lobster opener date is not in the KB — the note gives only 'roughly early October' and the KB explicitly flags that no corpus source states an October opener at all. | The spiny-lobster 7-per-day bag limit rests on a single garbled 2019 seminar aside and is flagged as needing CDFW verification. | The October warm-band retreat arc (backside Santa Cruz/Rosa → SBI → backside Catalina → 499/Clemente → 181/182) and the Tanner/Cortez condensation are single-sourced to OYOda6T3f-8; the co-cited XLVUhV8DW64 explicitly does not support them. | The '100% temp chart and chlorophyll' October operating quote is flagged in the KB as spliced from two non-adjacent transcript passages and attributed to a second source that never says it. | The yellowtail 'October–November island fish keep biting / paddy bycatch' framing is flagged as not stated in any of its three cited sources — the months are inferred from upload dates. | The dorado ~71–72 °F boundary band is extrapolated from a single 71.6 °F reading; no source states a band. | The swordfish 'October to mid-November peak' is the KB's envelope of two non-overlapping years (2019 and 2020), not a stated continuous peak. | The KB gives no numeric SST bands for yellowtail migration or bite ('migrate north at X °F') — only directional water-state reads. | Nothing in the KB covers how live-bait receiver supply (sardine/mackerel availability and quality) changes from September into October. | The KB does not cover whether or how the September paddy/dorado program's decline through October can be forecast — only isolated observations that paddies still produced into October. | No corpus source gives a water-condition trigger for when to deploy marlin gear; the KB records this as an open research question. | Yellowfin has no documented night programme and no documented kite programme — both are explicit flagged stubs in the species router. | Sight-fishing a finning or sunning swordfish is a flagged stub — approach, bait and cast have no corpus source. | No Baja-side or Sea-of-Cortez season shape was covered here; the KB's October note is region-gated to socal-bight only, and the September BOLA bottom-yellowtail program is cortez-north, outside the Bight the question asked about.

</details>
