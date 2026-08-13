# Orchestrate chunk — the unattended per-run driver

You are the ORCHESTRATOR of one chunk of the batch-2 ingestion pipeline,
running inside GitHub Actions on branch `claude/batch2-ingestion-rb0v4i`.
Your context stays thin: you NEVER read transcripts or notes, and you keep
only one-line results per video. All judgment lives in your two subagents;
all git state changes go through the sanctioned wrapper.

`CHUNK_SIZE` (N) arrives in your kickoff prompt.

## Loop

1. Run `python scripts/next-video.py -n N`. Each output line is one JSON
   row: `{"video_id", "channel", "class", "depth", "path"}`. If there are
   zero rows, print "worklist empty" and stop. If a row carries an
   `"error"` field, run
   `python scripts/batch2/commit-video.py --video-id <id> --status escalated --result "escalated: path-resolution-failed" --message "path resolution failed"`
   and continue to the next row.
2. For each row, in order — a strict per-video sequence:
   a. `bash scripts/batch2/reset-tree.sh`  (clean slate; mandatory)
   b. Spawn the EXTRACTOR subagent (Task tool, fresh context) with exactly
      this prompt:
      "Read prompts/extract-unit.md and follow it exactly. Transcript:
      <path>. Triage row: <video_id> | <channel> | <class> | <depth> |
      <evidence from the worklist>. Repo root: the current working
      directory."
      Keep only its final `LOG:` line.
   c. Spawn the EVALUATOR subagent (Task tool, fresh context) with exactly
      this prompt:
      "Read prompts/evaluate-unit.md and follow it exactly. Transcript:
      <path>. Triage row: <same row>. The extractor's patch is the current
      working-tree diff. Repo root: the current working directory."
      Keep only its `VERDICT:`, `ESCALATION:` and `LOG:` lines.
   d. Map the verdict to the wrapper call (the wrapper updates the worklist
      row, runs link-maintenance, commits, guards, and pushes):
      - `apply` / `apply-with-changes` / `escalate(apply)`:
        `python scripts/batch2/commit-video.py --video-id <id> --status done --result "<evaluator LOG destinations + one-line outcome>" --message "<class>/<depth> extraction"`
      - `reject-with-reason` (evaluator already reverted the tree):
        `python scripts/batch2/commit-video.py --video-id <id> --status skipped --result "skipped: evaluator-reject: <reason, shortened>" --message "evaluator reject"`
      - `escalate(reject)`:
        `python scripts/batch2/commit-video.py --video-id <id> --status escalated --result "escalated: <reason, shortened>" --message "escalated"`
      - Any `escalate(...)` verdict: add
        `--escalation "<video_id> | <type: evaluator-escalate> | <the evaluator's ESCALATION line>"`.
   e. Interpret the wrapper's exit code:
      - 0: done — next video.
      - 2 (link-maintenance failed, video escalated) or 3 (guard reverted
        the commit): logged and handled — next video.
      - 4 (push failed after retries): STOP the loop immediately; report.
   f. If a subagent dies or returns garbage: `reset-tree.sh`, then
        `commit-video.py --video-id <id> --status escalated --result "escalated: subagent-failure" --escalation "<video_id> | subagent-failure | <one line>"`,
        then continue.
3. Hard stop after N rows regardless of outcomes.

## Final message

One line per processed video (`<video_id>: <status>`), then a one-line
tally (`done X / skipped Y / escalated Z of N`). Nothing else. Do not
summarize content, do not read the notes you didn't write, do not push or
commit outside the wrapper.


<!-- backlinks:start -->
## Linked from

_Nothing links here yet._
<!-- backlinks:end -->
