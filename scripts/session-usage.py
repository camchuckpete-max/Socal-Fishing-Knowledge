#!/usr/bin/env python3
"""Report token usage for Claude Code sessions on this machine.

WHAT THIS DOES AND DOES NOT MEASURE. It sums the per-turn usage records the
CLI writes into its session transcripts. That covers interactive sessions in
THIS container only. It does NOT see:
  - sessions on other machines,
  - GitHub Actions ingestion runs (each runs in its own runner container),
  - the account-level weekly plan limit itself.
So treat the total as a floor for local interactive burn, not an account
balance. `/usage` inside a session remains the only view of the real limit.

Usage: session-usage.py [--all]
"""
import json, sys, glob, os

def summarize(path):
    t = {"output": 0, "cache_creation": 0, "cache_read": 0, "input": 0}
    turns = 0
    with open(path) as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            u = (d.get("message") or {}).get("usage") or d.get("usage")
            if not u:
                continue
            turns += 1
            t["output"] += u.get("output_tokens", 0)
            t["input"] += u.get("input_tokens", 0)
            t["cache_creation"] += u.get("cache_creation_input_tokens", 0)
            t["cache_read"] += u.get("cache_read_input_tokens", 0)
    return turns, t

def main():
    files = sorted(glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl")),
                   key=os.path.getmtime, reverse=True)
    if not files:
        print("no session transcripts found"); return 1
    if "--all" not in sys.argv:
        files = files[:1]
    grand = {"output": 0, "cache_creation": 0, "cache_read": 0, "input": 0}
    for f in files:
        turns, t = summarize(f)
        for k in grand:
            grand[k] += t[k]
        print(f"{os.path.basename(f)[:20]:<22} turns={turns:<5} "
              f"output={t['output']:>10,}  cache_new={t['cache_creation']:>11,}")
    if len(files) > 1:
        print("-" * 68)
        print(f"{'TOTAL':<22} output={grand['output']:>10,}  "
              f"cache_new={grand['cache_creation']:>11,}")
    print("\nOutput tokens are the figure to watch; cached reads are cheap.")
    print("Actions ingestion runs are NOT counted here — separate containers.")
    return 0

sys.exit(main())
