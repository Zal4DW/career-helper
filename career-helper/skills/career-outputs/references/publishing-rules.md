# Publishing Rules

**Purpose:** The rules every Career Helper output follows when it is published as an artifact, a dashboard, a Claude Doc, or a slide deck, so that each one is found, refreshed, and kept private the same way.

**Applies to:** Every capability in `career-outputs`, and every skill that hands an output to it.

---

## The Outputs and Their Fixed Titles

Each output has one fixed title. The title is how you find the output again when the register is missing (for example, in a cloud session or a scheduled run that cannot see the workspace folder), so never change it and never add the user's name or a date to it.

| Output | Title | Kind | Capabilities to declare |
|:-------|:------|:-----|:------------------------|
| Application board | `Career Helper Applications` | Page from `kanban-board-template.html` | `{"db": {}, "user": {}}` |
| Market map | `Career Helper Market Map` | Page from `market-map-board-template.html` | `{"db": {"rules": [{"path": "private", "read": "owner", "write": "owner"}]}, "user": {}}` |
| Ikigai map | `Career Helper Ikigai` | Page from `ikigai-map-template.html` | `{"db": {}, "user": {}}` |
| Progress dashboard | `Career Helper Progress` | Dashboard artifact type | From the type |
| Footprint dashboard | `Career Helper Footprint` | Dashboard artifact type | From the type |

Docs and slide decks take descriptive titles set out in `docs-and-slides.md`.

The page files carry their own `<title>`, which matches the table. Use a one-sentence description when publishing, for example "Your job applications by stage, kept current by you and Claude."

---

## One Output, One Link

1. **Look up before you publish.** Read the register (below). If it has no entry, list your artifacts and look for the fixed title. Only when neither finds it is the output new.
2. **Refresh in place.** Republish to the recorded link, or write new data to its database. Never publish a second board, map, or dashboard. A second copy splits the user's data in two.
3. **Data survives republishing.** A page's database is kept when the page is republished to the same link, so upgrading the page never loses the user's applications or organisations.
4. **Delete only when asked.** Never delete an output, its data, or a Doc unless the user asks for that one by name.

---

## Page Versions

Each page file states its version in its opening comment (for example, "Page version 2.0.0"). The register records the version each published page is on.

- **New page:** publish the file unchanged, with the capabilities in the table above.
- **Older page:** when the plugin's page version is newer than the register's, republish the new file to the same link, unchanged, with the same capabilities. Tell the user in one line that the page was updated and their data is unaffected.
- **Same version:** do not republish. Write data only.

Never edit a page file to put user data in it. The pages hold no user data; everything lives in the database.

---

## Writing Data (Seeding and Updating)

The data fields for each page are defined by its owning skill (`kanban-board.md`, `market-map-board.md`, `tim-ikigai-visual.md`). When writing:

1. **Write after publishing.** A new page has an empty database until you write to it. Write the user's data with the artifact data tools straight after the first publish.
2. **Use one batch** for more than a couple of documents, so the user approves one write, not twenty.
3. **Use stable document ids.** Lower-case letters, digits, and hyphens, built from the organisation and role (for example `example-org-operations-director`). Add `-2`, `-3` when an id is already taken.
4. **Stamp every write** with `updated` (the current date and time, ISO 8601) and `updatedBy: "claude"`. The page stamps its own writes with `updatedBy: "board"`; that is how you tell the user's changes from yours.
5. **Never invent a value.** Unknown text fields are empty strings. Dates are `YYYY-MM-DD` or empty.
6. **Merge, do not replace,** when changing an existing document: update the fields that changed and leave the rest, so you never overwrite something the user just changed on the board.
7. **Check once.** After a seed or a large update, list the collection and confirm the count. If it does not match, say so.

---

## Reading Data Back

At the start of any task that uses a board, read its database before relying on anything in the conversation or the workspace snapshot:

1. List the collection (and the meta document).
2. Find documents with `updatedBy: "board"` whose `updated` timestamp is later than `lastReadByClaude` in the board's meta document (`board/meta` or `map/meta`). These are the user's own changes. Compare full ISO 8601 timestamps, never dates alone. If `lastReadByClaude` is missing (a board from before this rule, or the first read), treat every `updatedBy: "board"` document as new once, and say so.
3. Summarise them in one or two lines ("You moved Example Org to Interviewing and set a follow-up for Friday"), then act on them as the owning skill describes (for example, a move to Interviewing suggests interview preparation).
4. Write the current time (ISO 8601, to the second) to `lastReadByClaude` in the board's meta document, and copy it to "Last read" in the register when there is one. The meta document is the baseline, so it works in sessions with no workspace folder.

The board's database is the record. If the workspace snapshot and the database disagree, the database wins; refresh the snapshot.

---

## Workspace Snapshots

When the session has a workspace folder, keep a read-only markdown snapshot of each board next to the user's other files, so the data is portable, readable outside Claude, and visible to `/career-helper:status`:

| Board | Snapshot |
|:------|:---------|
| Application board | `applications/tracker.md` |
| Market map | `market-map.md` |

- Regenerate the snapshot from the database after every change you make or read back.
- Start each snapshot with: `*Snapshot of your {{board name}} on {{YYYY-MM-DD}}. The board is the record: change it there, or ask Claude. Edits made to this file are not read back.*`
- If the user edits a snapshot by hand anyway, do not discard it: show them the differences and offer to apply them to the board.
- The market map snapshot must not include the seed organisation unless the user's posture is "Openly searching" and they ask for it.

---

## The Register

`career-helper-artefacts.md` at the workspace root lists every published output. Create it from @artefact-register-template.md the first time anything is published. It records, per output: title, kind, link, page version, date first published, date last updated, and date last read.

If the session has no workspace folder, rely on the fixed titles to find outputs, and say once that a workspace folder would let Claude keep a register.

---

## Privacy and Sharing

- **Everything starts private.** Only the user can see a new artifact, Doc, or deck.
- **Never share on the user's behalf,** and never make an output public. If the user wants to share, tell them what the other person would see and could change, then let them use the share menu:
  - A **Viewer** sees the board read-only.
  - A **Contributor** or **Editor** can change the board's data. Suggest Viewer unless they want help keeping it up to date.
  - On the market map, the seed organisation is kept in an owner-only part of the database and is never shown on the page, whoever it is shared with.
- **Keep sensitive detail off boards.** Salary figures, health matters, and personal reflections belong in the negotiation, learnings, or other private documents, not in card notes.

---

## When Publishing Is Not Available

If a session cannot publish artifacts or reach an artifact's data (for example, a scheduled run without those tools), do not pretend it did:

- Say plainly what could not be reached.
- Carry on with what can be done (research, drafting, the dated report).
- In an unattended run, record "Board not reachable in this run" in the report's "Decisions waiting for you" section, and list any changes you would have made, so the next session can apply them.

---

*Publishing Rules | Career Helper Plugin | Prosper AI Consulting, UK*
