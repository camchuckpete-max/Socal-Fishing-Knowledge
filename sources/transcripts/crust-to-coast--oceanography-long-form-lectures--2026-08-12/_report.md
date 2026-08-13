# Run report — Oceanography - Long Form Lectures

## Header

- **Playlist URL:** https://www.youtube.com/playlist?list=PLOMMpqItRwQna8TRhb8KHjjD3zoZp-a1j
- **Playlist ID:** `PLOMMpqItRwQna8TRhb8KHjjD3zoZp-a1j`
- **Channel:** Crust to Coast (`UC4lyFLgi-ZqANz1m-zb2zrw`)
- **Run date:** 2026-08-12
- **Deliverable:** `crust-to-coast--oceanography-long-form-lectures--2026-08-12.zip`

## Counts

| Metric | Value |
|---|---|
| Entries listed | 19 |
| Unique video IDs | 19 |
| ok | 18 |
| failed | 1 |
| Manual captions | 0 |
| Auto-generated captions | 18 |

No duplicate video IDs. No videos hidden from `--flat-playlist` — the flat listing returned 19 entries and all 19 resolved to real videos with full metadata.

## Failures

| video_id | title | reason |
|---|---|---|
| `DRbl0fVgGIo` | Geology 5 - Climate Change | no English caption track (manual or auto-generated) |

`DRbl0fVgGIo` is not private or removed — it resolves with full metadata (title, channel, 38m41s duration) under `web_embedded`. Both `subtitles` and `automatic_captions` are empty objects, so the uploader has captions disabled and YouTube never generated an automatic track. The default `web` client returns nothing usable for this video (bot check), so no additional detail was available from a re-probe. Nothing to retry here — this is a permanent absence, not a transient block.

## Pipeline notes

Ran exactly as METHOD describes, with no deviations:

- `--flat-playlist -J` expanded the playlist cleanly on the first call.
- `youtube:player_client=web_embedded` with `--ignore-no-formats-error` worked for all 19 videos. No bot checks, no 429s, no backoff triggered, no TLS interception — `--no-check-certificate` was never needed.
- `youtube-transcript-api` skipped per the standing `RequestBlocked` note.
- Every successful track was auto-generated `en`. No manual English tracks and no `en-orig` fallbacks existed anywhere in this playlist.
- 2s sleep between videos held for the whole run; the batch finished in roughly three and a half minutes.

## Observation — playlist topic

This playlist does not match the fishing subject matter of the rest of this repository. It is a 19-part undergraduate oceanography lecture course ("Geology 5") from Crust to Coast, covering plate tectonics, chemical and physical oceanography, ocean circulation, tides, marine sediments, primary productivity, and marine pollution — roughly 10.5 hours of lecture. Flagging it here rather than in the CSV, per the report convention. It is adjacent background material rather than fishing technique, so it may or may not be what was intended for this repository.
