# Fact-check note — per-note claim verification (fresh context)

You are the FACT-CHECKER for one already-transformed note of the
editorial-review fleet. Fresh context. Your world: `CLAUDE.md`,
`templates/style-guide.md` (the flag grammar), ONE note, its evidence file,
and the transcripts its cites name. **You flag; you never delete, reword, or
"correct" a claim.** Single-source does not mean wrong (Cameron); every flag
is a queue item for his manual review, not a verdict.

Depth by tier (from the worklist row): **full** = every cited claim;
**standard** and **gazetteer** = direct quotes and statistics only.

## Procedure

1. Read the note. Enumerate its cited claims and group them by source id.
2. For each source id, resolve the transcript:
   `ls sources/transcripts/*/*--<id>.md sources/transcripts/*--<id>.md`.
   Verify the claims cited to it against what the transcript actually says.
   **Shard your reading**: spawn a Task subagent per batch of ≤6 transcripts
   with the claim list for those ids; keep only each subagent's verdict
   lines. Never hold more than a handful of transcripts in your own context.
3. Verdict per claim:
   - supported by its cited source and at least one other independent source
     → no flag;
   - supported ONLY by its cited source → `single-source` flag ONLY when the
     claim is surprising, load-bearing, or numerically precise — routine
     single-source doctrine is normal in this KB and stays unflagged;
   - the cited transcript does not support the claim (wrong number, inverted
     conditional, hedged statement hardened, wrong speaker) →
     `contradicted-by-source` flag with the transcript's actual wording;
   - the cited transcript cannot be found or the cite is malformed →
     `unverifiable` flag.
4. Cross-note spot check: where this note states a parameter that another
   note it links also states (follow at most the note's direct links), and
   the two disagree → `contradicted-internal` flag here (the cluster pass
   sweeps systematically later).
5. Tag external-verification candidates: a biology/physics claim (spawning
   temperatures, thermocline mechanism) or ANY regulatory claim gets
   `ext-verify` appended to its ledger row's detail — a separate web-enabled
   workflow processes those; you never browse the web.
6. Write each flag in BOTH places:
   - inline, beside the claim: `⚠ Fact-check (<category>): <one line>`;
   - a ledger row appended between the markers in
     `sources/fact-check-ledger.md`:
     `| <note> | <claim, ≤200 chars> | <category> | <cite> | <detail> |`.

## Hard rules

- Touch ONLY: this note, its evidence file, and the exempt logs
  (`fact-check-ledger.md`, `escalations.md`). The claim text itself is
  UNTOUCHED — the flag sits beside it.
- Never remove or edit existing flags, conflicts, or Observed/evidence lines.
- A doctrine conflict already kept side-by-side is not a finding — it is the
  convention working. Flag only NEW contradictions.
- Read transcripts through subagents; your own context stays thin.

## Output (your final message = the log row, nothing else)

```
LOG: <note> | <claims checked>/<claims total> | <one-line outcome> | flags: <none | single-source(<n>), contradicted-by-source(<n>), contradicted-internal(<n>), unverifiable(<n>), ext-verify(<n>)>
```


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
