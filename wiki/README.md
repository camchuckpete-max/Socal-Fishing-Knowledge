# The wiki UI

`index.html` in this folder is the browsable front end for the knowledgebase —
one self-contained file carrying every note, its fonts, its styles and its
search. Open it from disk, host it on GitHub Pages, or publish it as an
artifact; it needs no server, no network and no build step at read time.

**It is generated. Never hand-edit `index.html`** — the next build overwrites
it. Edit the notes, or edit the sources under `scripts/wiki/`.

## Rebuilding after a content change

```
python scripts/link-maintenance.py    # the usual pre-commit habit
python scripts/build-wiki.py          # regenerates wiki/index.html
```

The build reads every note under the branch folders plus the root `README.md`
and `CLAUDE.md`, renders the Markdown, pulls last-updated dates from git, and
inlines everything. It takes a couple of seconds, needs only Python 3 (no
third-party packages), and prints the note count, word count and file size.

Raw transcripts under `sources/transcripts/` are deliberately excluded — they
are source material, not notes, and would multiply the page size.

## What lives where

| Path | What it is |
| --- | --- |
| `scripts/build-wiki.py` | The generator: Markdown engine, link resolver, page assembly |
| `scripts/wiki/shell.html` | Page skeleton with the `__DATA__` / style / script slots |
| `scripts/wiki/app.css` | Design tokens, layout and prose styles (light + dark) |
| `scripts/wiki/app.js` | Router, sidebar, table of contents, search |
| `scripts/wiki/fonts/` | Barlow Condensed, Source Serif 4, IBM Plex Mono (OFL), inlined as data URIs |
| `wiki/index.html` | The generated output — the only file a reader needs |

## Using it

- **Search** — `/` or `⌘K` anywhere. Plain words match titles, tags, headings
  and body text; `tag:paddies`, `type:technique` and `in:species` narrow the
  field, and they combine.
- **Navigate** — the left rail groups the branches the way the KB is organised;
  each note carries breadcrumbs, an on-this-page outline, and the generated
  *Linked from* list as the reverse map.
- **Read on a phone** — the rail collapses to a drawer and search goes
  full-screen. Every table scrolls inside its own frame rather than pushing the
  page sideways.
- **Themes** — follows the reader's system setting; the toggle in the top bar
  overrides it and is remembered.

Links out to GitHub point at `main`, and each note's YouTube source IDs link to
the video they came from.
