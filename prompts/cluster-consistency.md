# Cluster consistency — cross-note contradiction sweep (fresh context)

You are the CONSISTENCY CHECKER for one cluster row of the review worklist
(`cluster:<species> | cluster | pending`, members listed in the row's result
cell): one species router plus the techniques/ and lures/ notes its
`## Situations → techniques` section links. Fresh context. **You flag; you
never reword, delete, or reconcile.**

## Procedure

1. Read the router, then each member note.
2. Hunt for CONTRADICTIONS between what the router claims about a
   technique/lure and what that note's own doctrine says: a parameter that
   disagrees (depth, speed, line class, season), a "reach for this when"
   that conflicts with the router's situation row, stale naming left behind
   by a relocation (the router calling something by its old class), a router
   row ranking that the technique note's own text argues against.
3. NOT findings: an attributed side-by-side doctrine conflict (that is the
   convention working); a region-labeled difference; a router summarizing
   what the technique note details.
4. For each real contradiction, flag it in BOTH notes:
   `⚠ Fact-check (contradicted-internal): <one line naming the other note
   and the disagreement>`, and append one ledger row per finding to
   `sources/fact-check-ledger.md`
   (`| <router>+<member> | <claim> | contradicted-internal | <cites> |
   <the two positions> |`).

## Hard rules

- Touch ONLY the cluster's member notes (as listed in the worklist row),
  their evidence files, and the exempt logs.
- Claims stay untouched; the flag sits beside them.

## Output (your final message = the log row, nothing else)

```
LOG: cluster:<species> | <members read> | <one-line outcome> | flags: <none | contradicted-internal(<n>)>
```


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->

## Species-technique staleness sweep (amendment v2.2)

A `## Differs from the general method` section was true against the technique
note as it stood when the sub-article was written. When that technique note is
later rewritten, the delta can quietly stop being a delta — a creation-time
check cannot catch this, which is why it lives here.

For each `type: species-technique` note in the cluster: read the parent
technique named in its `technique:` field, and confirm every bullet in
`## Differs from the general method` still states something the general note
does not. Any bullet that now merely restates the general method gets a
`⚠ Fact-check (contradicted-internal)` flag and a ledger row — **flag, never
silently rewrite**. If ALL of a page's deltas have collapsed, escalate: the
page may no longer earn its existence.

