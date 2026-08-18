# socal-boat-day — the distributed skill

The skill people install. It is deliberately **thin**: a packaged skill can't be
edited once it's been sent to someone, so it carries only what can never change.

| Lives in the packaged skill (immutable) | Lives here in the repo (editable) |
| --- | --- |
| The repo URL and the entry path | The planning procedure |
| Tackle/rod intake and the memory format | The endpoint table and fallback ladder |
| The rule that recommendations come from the user's own inventory | All fishing doctrine |
| Network-setup and offline-fallback guidance | Everything else |

[`ENTRY.md`](ENTRY.md) is what an installed copy fetches first. **Its path is a
contract** — every distributed copy hardcodes it. If it has to move, leave a
stub behind.

## The packaged skill, committed here

[`SKILL.md`](SKILL.md) and [`references/`](references/setup.md) are the source
of record for what actually gets packaged and sent. They live here so a copy in
someone's hands can be diffed against what it was supposed to be — otherwise
there is no way to tell which version a person is running when they report odd
behaviour. `link-maintenance.py` validates their links but treats them as
packaged files, not KB notes: no backlinks block, not indexed.

Repackaging: zip the `socal-boat-day/` directory containing `SKILL.md` and
`references/`, excluding `ENTRY.md` and this README, which are repo-side.

## Relationship to `skills/boat-day/`

[`boat-day/`](../boat-day/README.md) is the earlier design, which **bundled** a
snapshot of the decision layer into the skill via
[`scripts/build-skill-resources.py`](../../scripts/build-skill-resources.py).
That works for a skill you rebuild yourself; it does not work for copies sent to
other people, because the bundle freezes at packaging time and the KB does not.

`socal-boat-day` replaces the bundle with live fetches. Decide whether
`boat-day` stays as a self-use variant or is retired — running both means two
definitions of the procedure, and they will drift.

## Multi-user

The KB is universal; angler-specific data lives in
[`profiles/`](../../profiles/README.md). The installed skill resolves each
user's own inventory from their chat memory and never reads another angler's
profile as if it were theirs. With no inventory it recommends in class terms,
which is a working output, not a failure.


<!-- index:start -->
## Index

- [ENTRY — SoCal Boat-Day Skill](ENTRY.md) — The live entry point every distributed socal-boat-day skill copy fetches first.
<!-- index:end -->


<!-- mermaid:start -->
## Map

_No intra-folder links yet._
<!-- mermaid:end -->
