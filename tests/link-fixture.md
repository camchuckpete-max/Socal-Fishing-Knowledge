---
type: planning
tags: [tooling, link-maintenance, fixture]
sources: [cameron]
confidence: high
---

# Link-Maintenance Fixture

Regression fixture for `scripts/link-maintenance.py` (mandated in the
2026-08-12 fix pass, item X1): link-looking text inside **fenced code blocks**
and **inline code spans** must be ignored by link validation, backlink
extraction, and the mermaid maps. If the script ever flags the fake links
below as dead, code-stripping has regressed — this file must always pass.

A fenced block containing a fake link:

```markdown
This [fake link](../does-not-exist/nowhere.md) must never be validated.
Nor this one: [also fake](missing-note.md).
```

An inline code span containing a fake link: `[inline fake](../nope/void.md)`.

A real link, which IS validated: [repo master index](../README.md).

<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
