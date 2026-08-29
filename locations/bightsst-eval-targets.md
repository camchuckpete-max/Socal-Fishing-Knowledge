---
type: location
tags: [bightsst, eval-spots, upwelling, turnover, modeling]
sources: [cameron]
confidence: high
regions: [socal-bight]
waters: [bay-harbor, nearshore-coast, island, bank, open-ocean]
layout: v2
parent: unknown
structure_type: unknown — a named reference list spanning every structure type in the eval set (island, bank, nearshore); not one physical spot, see each named spot's own page for its structure
depth_band: unknown — not a single depth-banded spot
distance_nm: unknown — not measured from one launch point; a fixed reference list, not a trip
---

# BightSST Eval Targets

[BightSST](https://bightai-api.onrender.com) scores its upwelling/turnover
detection model against a fixed, small set of **named evaluation spots**
(cameron). This note holds the eval set's names only — no coordinates — so the
KB can reference the set without duplicating BightSST's live output, which
stays that platform's job. The mechanism under test — upwelling, the sharp
SST drop plus chlorophyll spike, and the approach to turnover — is
[upwelling and turnover](../conditions/upwelling-and-turnover.md)'s doctrine,
not repeated here.

## Getting there

This is a universal reference list, not a single spot — it carries no launch
point or transit leg of its own. Getting-there detail for a named eval spot
lives on that spot's own gazetteer page where one exists.

⚠ Flagged gap — no corpus source: transit/launch detail (not applicable —
this note indexes a modeling target list, not a spot to fish).

## Structure & bathymetry

This entry is the list itself, not one structure — each member spot's own
bank/island/reef makeup lives on its own page.

### The original 8 eval spots

The upwelling/turnover model started on 8 named eval spots (cameron):

1. La Jolla NW Corner
2. 302 Bank
3. Coronado Islands
4. Mexican Rockpile
5. Pyramid Cove
6. 9 Mile Bank (San Diego)
7. 14 Mile Bank (LA)
8. Cortes Bank

### Expanding to ~14

The Coronado Islands entry is split into each of the **6 Coronado Islands
spots individually**, because conditions vary enough across that group that
one averaged reading hides the spread (cameron). That expansion takes the set
from 8 to **~14** eval locations: 14 Mile Bank, North + South 9 Mile Bank,
Cortes Bank, 302, La Jolla NW Corner, Rockpile, Pyramid Cove, and each of the
6 Coronado Islands spots (cameron).

⚠ Flagged gap — no corpus source: per-spot depth/bathymetry detail for each
eval location; see the individual spot pages where charted.

## What's there

⚠ Flagged gap — no corpus source: not applicable — this note tracks modeling
targets, not species presence. See each named spot's own page and the
relevant species router for what's there.

## How it fishes

### The training universe

Behind the eval set sits a **~125-bank list** — the training universe of
SoCal banks and structures the model draws on; the eval spots are the scored
subset, the 125-bank list is the full population (cameron). The model draws on
roughly 13 years of local SST, chlorophyll, tide, wind, swell, and historical
fish-count data (cameron).

### What the evals are built to serve

The eval set is built to serve one piece of doctrine: fishing is best right
before turnover — the sharp SST drop plus chlorophyll spike — so the model's
key output is time-to-turnover / the approach, not the turnover event itself
(cameron). Full doctrine and how to use it in planning:
[upwelling and turnover](../conditions/upwelling-and-turnover.md).


<!-- backlinks:start -->
## Linked from

- [12 Mile Reef](12-mile-reef.md)
- [14 Mile Bank](14-mile-bank.md)
- [172 / 125](172-125.md)
- [179 / 220](179-220.md)
- [209 / 312](209-312.md)
- [279 / 267 / 14 Mile Bank](279-267-14-mile-bank.md)
- [289 / 284](289-284.md)
- [311 (Trask Knoll)](311.md)
- [380](380.md)
- [43 / 91 / 300](43-91-300.md)
- [474 / 711](474-711.md)
- [51 / 181 / 138](51-181-138.md)
- [81 / 381](81-381.md)
- [Anacapa Island](anacapa-island.md)
- [Cameron's Spots](../profiles/cameron/spots.md)
- [Channel Islands](channel-islands.md)
- [Coronados - 230 / 302 (Kidney Bank) / 226](coronados-230-302-226.md)
- [Deep Scattering Layer](../conditions/deep-scattering-layer.md)
- [E. Butterfly / San Salvador Knoll](e-butterfly-san-salvador-knoll.md)
- [Hancock Bank](hancock-bank.md)
- [Hidden Reef / 170](hidden-reef-170.md)
- [Kidney Bank (63) / 175](kidney-bank-63-175.md)
- [LA - 270 / 286](la-270-286.md)
- [La Jolla](la-jolla.md)
- [Lower Cross](lower-cross.md)
- [North 9 Mile Bank / 178](north-9-mile-bank-178.md)
- [Pyramid Head](pyramid-head.md)
- [San Clemente Island — Front Side](san-clemente-island-front-side.md)
- [San Juan Seamount](san-juan-seamount.md)
- [South 9 Mile Bank / 439](south-9-mile-bank-439.md)
- [Southern California Bight](socal-bight.md)
- [Sverdrup Bank (126)](sverdrup-bank-126.md)
- [Tanner Bank](tanner-bank.md)
- [The 43](43.md)
- [The Boot (504) / 307](boot-504-307.md)
- [The Bumps](bumps.md)
- [The Corner / 140 / 182](corner-140-182.md)
- [Upwelling and Turnover](../conditions/upwelling-and-turnover.md)
- [W. Butterfly / 157](w-butterfly-157.md)
- [Zone Lexicon](zone-lexicon.md)
<!-- backlinks:end -->
