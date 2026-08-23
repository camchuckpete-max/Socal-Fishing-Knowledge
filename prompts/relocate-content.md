# Relocate content — one relocation-queue move (fresh context)

You are the RELOCATOR for one row of `sources/relocation-queue.md` (the
HookUp-Baits/C-1 class of fix: content filed under the wrong note). Fresh
context. Your world: `CLAUDE.md`, `templates/` for both types involved, the
row (`src | dst | what | rationale | cite | status`), and the two notes.

The transform pass only FLAGGED this move; you decide it and execute it —
or escalate it to Cameron.

## Procedure

1. Read src and dst in full (create dst from its type's template when the
   row says `NEW: <path>` — front matter, regions/waters, layout: v2, linked
   from its parent/router so it is reachable).
2. Judge the row: is the content actually misplaced? If the call is genuinely
   ambiguous (a real classification question, e.g. glide bait vs tube bait
   where sources disagree), do NOT guess — verdict `escalate` below.
3. Execute the move as a PAIR edit:
   - remove the content from src (delete its `⚠ misplaced-content` flag with
     it);
   - land it in dst under the correct section, merged per the style guide,
     cites intact; append the moved cites' ids to dst's front-matter
     `sources` list (append-only);
   - move any affected evidence entries from src's evidence file to dst's;
   - the guard checks the PAIR as a unit: every cite and observation that
     leaves src must appear in dst or dst's evidence file.
4. Leave a one-line cross-reference in src where the content was, linking
   dst, when a reader of src would otherwise miss it.
5. Log the move in the judgment-calls section the endgame collects: append a
   line to `sources/relocation-queue.md` below the table is NOT needed — the
   row itself is the record; put your reasoning in the row's rationale cell
   only if it changed.

## Hard rules

- Touch ONLY src, dst, their evidence files, and the exempt logs.
- Never drop content in transit; never resolve doctrine conflicts while
  moving them; never touch a third note (stale references elsewhere are the
  cluster pass's job).
- `NEW:` note creation follows every extractor process rule (front matter,
  gating, reachable from a parent, resolves under link-maintenance).

## Output (your final message = exactly this, nothing else)

```
VERDICT: done | skipped(<why the content was NOT misplaced>) | escalate(<the classification question Cameron must decide>)
LOG: <src> -> <dst> | <what moved, one line> | flags: <none | new-note(<path>)>
```


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
