# Template: evidence file (`type: evidence`)

The provenance layer created by the observation split: one file per note that
has observations, at `<folder>/evidence/<note>.md`. It holds what the main
note's prose gave up — trip reports compressed to one-liners, and the full
per-source provenance detail (channel, upload date, registration status,
sponsor disclosure, ASR caveats). Nothing is ever deleted in the split; the
review guard checks conservation.

Evidence files are NOT region-gated (the parent note gates), are skipped by
the granularity watch, are excluded from the site export, and otherwise ride
the normal backlinks/index machinery.

## Front matter

```yaml
---
type: evidence
parent: ../yellowtail.md     # relative path to the paired note; MUST resolve
tags: [yellowtail]
sources: [<the observation video_ids>]
confidence: medium
---
```

## Skeleton

```
# Evidence — <note name>

One-line orientation: what this file is, link to the parent note.

## <Mirrors a main-note section heading, e.g. "Where & when">

- `<video_id>` (channel, YYYY-MM-DD, place): <one line — what happened, with
  conditions>. <optional provenance tail: sponsor-heavy; asr-uncertain(<what>);
  unregistered channel.>
- ...

## <Next mirrored section>
...

## Linked from   (machine-generated)
```

Rules:

- **One line per observation.** The 30-line block format is retired; boat
  names, charter lengths, and disambiguation notes survive only when they
  change what the observation means.
- Group under headings that mirror the parent's sections, in the parent's
  order, so a reader lands from the parent's `## Evidence` link and finds the
  support for the section they came from.
- Observations never change doctrine (unchanged); a contradicting one is also
  traced beside the doctrine in the parent, cited.
