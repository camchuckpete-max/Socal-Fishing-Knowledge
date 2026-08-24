# Template: jurisdiction page (`type: jurisdiction`)

Top rung of the geographic ladder: jurisdiction -> region -> area -> zone ->
spot. Two pages only (US waters, Mexican waters). Deliberately NOT region-gated
— it applies to every region on its side of the border.

This rung holds paperwork and border rules ONLY. A closure or restriction that
is a fact about one island or bank belongs on that ZONE page: the San Clemente
Navy zones are a San Clemente fact, not a "fishing in US waters" fact.

## Front matter

```yaml
---
type: jurisdiction
tags: [paperwork, regulations, <us|mexico>]
sources: [<video_id>, cameron]
confidence: high|medium|low
layout: v2
authority: <e.g. INM + CONAPESCA (Mexico) | CDFW + USCG (California)>
as_of: <YYYY-MM>
---
```

## Skeleton (canonical order — extras allowed between)

```


# <US | Mexican> waters

**The paperwork rung.** Not a fishing page — this is what you must carry, buy
or declare to fish legally on this side of the line, and what happens when you
are checked. Fishing knowledge lives in the regions and zones below it.

Note this rung is deliberately NOT region-gated: it applies to every region on
its side of the border by definition.

## Papers you need

Each item names the issuing authority, what it costs if the corpus says, where
it is obtained, and an as-of date. Regulatory claims carry
jurisdiction + as-of + verify-current, per the content rules — rules change and
this page ages.

## On the water

Checks and boardings, what to have to hand and how, distance rules, closures
that apply jurisdiction-wide. **Facts about one island or bank belong to that
zone page, not here** — Navy closure zones at San Clemente are a San Clemente
fact.

## Bringing fish home

Declarations, transport and border rules for fish caught on this side.

## Evidence

One line linking `locations/evidence/<note>.md`.

## Linked from   (machine-generated)
```
