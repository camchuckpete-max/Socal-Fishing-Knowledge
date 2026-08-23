# Template: seasonal note (`type: seasonal`)

The month-by-month priors calendar — the pattern layer, not current intel.
Already the KB's cleanest folder; v2 adds only the infobox regime field and
the standing disclaimer.

## Front matter

```yaml
---
type: seasonal
tags: [august, ...]
sources: [<video_id>, ...]
confidence: high
regions: [socal-bight, ...]
waters: [open-ocean, ...]
layout: v2
regime: warm-stable        # warming | warm-stable | cooling | cold | transition
---
```

## Skeleton

```
# <Month / window>

**These are priors — the pattern layer, not current intel.** <Lead.>

<free sections: the month's patterns, one `##` per pattern, declarative and
cited.>

## Evidence
Only when observations exist.

## Linked from   (machine-generated)
```
