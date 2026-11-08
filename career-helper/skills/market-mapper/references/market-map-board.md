# Market Map Board

**Purpose:** Keep the market map as one interactive board that the user and Claude both keep current. Every organisation is a card in one of four priority columns (Act now, Warm, Watch, Quiet). The user can raise or lower priorities with a reason, edit the overview, angle, and their own notes, and see each organisation's dated signals and decision makers; Claude researches, adds signals, and reads the user's changes back in any later session, including a scheduled weekly update.

**Applies to:** The artifact titled `Career Helper Market Map`, published from the page in `@references/market-map-board-template.md`. Its database is the record of the map. When the session has a workspace folder, a read-only snapshot is kept at `market-map.md` in the shape of `@references/market-map-template.md`.

---

## Principles

1. **The board is the record.** Organisations, signals, decision makers, priorities, and themes all live in its database. `market-map.md` is a snapshot.
2. **Never invent a signal or a person.** Signals and decision makers are written only by Claude, each with a dated public source. The page shows them but does not let anyone type new ones, so every entry keeps its source.
3. **The seed employer stays private.** It is stored in an owner-only part of the database (`private/seed`) that the page never reads, so it never appears on the board, whoever the board is shared with.
4. **One board.** Find it through the register or its fixed title before doing anything (see `@../career-outputs/references/publishing-rules.md`).

---

## Data

Declare these capabilities when publishing:

```json
{"db": {"rules": [{"path": "private", "read": "owner", "write": "owner"}]}, "user": {}}
```

### `organisations/{id}`: one document per organisation

| Field | Meaning | Written by |
|:------|:--------|:-----------|
| `organisation` | Name | Claude or board |
| `overview` | One line: what they do, size band, location | Claude or board |
| `priority` | Act now, Warm, Watch, or Quiet | Claude or board |
| `priorityReason` | One line; the evidence (Claude) or the user's judgement (board) | Claude or board |
| `priorityBy` | `claude` when evidence set it, `board` when the user did | Claude or board |
| `priorityChanged` | `YYYY-MM-DD` of the last priority change | Claude or board |
| `signalGroup`, `latestSignal`, `signalDate` | The latest signal in the window: group (Hiring, Growth, Investment, Change), one line of fact, date | Claude |
| `decisionMaker` | One-line summary: name, title (source), or `[NOT FOUND]` | Claude |
| `angle` | One-line suggested action tied to a signal, respecting the posture | Claude or board |
| `notes` | The user's own notes | Board (Claude only when asked) |
| `lastChecked` | `YYYY-MM-DD`, or empty for a card the user added | Claude |
| `website`, `careersPage`, `linkedinPage` | `https://` URLs, or empty | Claude |
| `sizeBand`, `whyOnMap` | From the map's organisation detail | Claude |
| `signals` | List of `{date, group, signal, source, seen}`, every entry in the window | Claude |
| `decisionMakers` | List of `{name, title, source, linkedin, appointed}`; `[NOT FOUND]` entries carry the search to run in `title` | Claude |
| `updated`, `updatedBy` | Stamped on every write | Both |

### `map/meta`

`owner`, `posture` (Employed and discreet, or Openly searching), `direction`, `signalWindow`, `firstBuilt`, `lastChecked`, `themes` (a list of three to five one-line observations), `coverage` (the coverage statement), and `lastReadByClaude` (the ISO 8601 time Claude last read the board back).

### `private/seed`

`seedOrganisation` and `seedProfile` (the seed profile table as fields). Owner-only; never shown on the page.

---

## Publishing and Refreshing the Page

Follow `/career-outputs` Capability 1:

1. **Look it up** in `career-helper-artefacts.md`, then by the title `Career Helper Market Map`.
2. **New board:** extract the HTML from `market-map-board-template.md` into `market-map-board-template.html` and publish that file unchanged with the capabilities above, then write `map/meta`, `private/seed`, and one document per organisation in one batch. Read the `organisations` collection back once and confirm the count.
3. **Existing board on an older page version:** extract the page again and republish the `.html` file to the same link. The data is kept.
4. **Moving from an older map:** if `market-map.md` exists from an earlier version of Career Helper (no snapshot line at the top), it is the user's own record: read it and write it into the board, then turn the file into a snapshot.
5. **Record** the link and page version in the register, and refresh the `market-map.md` snapshot.

Offer to open the board when the map is built, and whenever the user asks to "see my watchlist", "show me the market map", or similar.

---

## Syncing the User's Changes

There is no export step. At the start of any task that uses the map (including the weekly update):

1. Read `map/meta` and the `organisations` collection.
2. Pick out documents with `updatedBy: "board"` whose `updated` timestamp is later than `lastReadByClaude` in the meta document (see `publishing-rules.md`, Reading Data Back).
3. **Priority changes made on the board are the user's judgement.** Keep them, with the reason they gave (`priorityReason`). If they gave none, ask once in conversation; in an unattended run, record "Changed on the board on {{date}}; reason not given" and do not invent one. At the next update, say plainly where the evidence disagrees ("You raised Example Org to Act now; no hiring signal has appeared since") rather than silently overriding either side.
4. **Organisations the user added** have an empty `lastChecked`: research them at the next update, filling the detail fields and signals.
5. **Organisations the user removed** are gone from the board; remove them from the snapshot too, and do not re-suggest them for at least one update.
6. Refresh the snapshot, and write the current time to `lastReadByClaude` (and the register's "Last read").

---

## Accessibility

The page is built to be usable without a mouse and without colour vision; keep it that way:

- Every priority is a text label on the column, with its one-line meaning under it, and in each card's accessible name.
- Cards are keyboard operable: focus a card, use the left and right arrow keys or the labelled Raise and Lower buttons to move it, and Enter to open it.
- Moves and saves are announced through a live region for screen readers.
- An organisation not checked for more than fourteen days shows a text `STALE` tag.
- The page follows the user's light or dark theme and works at phone width.

If `career-helper-preferences.md` sets `dyslexia_friendly: true`, keep the overview and angle fields short when writing them. If `colour_blind: true`, no changes are needed.

---

## What the Board Is Not

- It is not a place to type evidence. Signals and decision makers come from Claude's dated research; ask Claude to add or correct them.
- It is not a place for outreach drafts. Angles are one line; anything longer belongs in `/career-navigator` networking intelligence.

---

*Market Map Board v2.0 | Career Helper Plugin | Prosper AI Consulting, UK*
