#!/usr/bin/env bash
# Batch-2 pipeline: restore a clean working tree at a video boundary.
# Discards ALL uncommitted changes and untracked files in the repo.
# Subagent scratch files must live in /tmp, never in the repo.
set -euo pipefail
cd "$(dirname "$0")/../.."
git checkout -- .
git clean -fd
