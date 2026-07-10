# Kanban Board View

**Purpose:** Give the user an interactive, visual view of their application pipeline when a markdown table stops being enough. The board renders every application as a card in one of six stage columns (Researching, Applying, Applied, Interviewing, Offer, Closed) and lets the user drag cards between stages, edit next actions, and export the result back to tracker markdown.

**Applies to:** The board artefact at `applications/board.html`, generated from `applications/tracker.md` using `@references/kanban-board-template.html`.

---

## Principles

1. **The tracker file remains the source of truth.** The board is a view, not a second database. `applications/tracker.md` is the record; the board is regenerated from it and changes flow back into it.
2. **Never invent status.** The board is populated only from rows that exist in the tracker. If a field is unknown, leave it blank or `[UNKNOWN]`; do not guess.
3. **One board, regenerated.** There is only ever one `applications/board.html`. Overwrite it on each regeneration; do not accumulate dated copies.
4. **Offline and private.** The template is fully self-contained: no external scripts, fonts, or network calls. Board edits persist in the browser's local storage only, on the user's machine.

---

## When to Offer the Board

Offer the board (do not push it) when:

- The user has three or more active applications in the tracker.
- The user asks to "see my pipeline", "show me a board", "visualise my applications", or similar.
- A status review (`/career-helper:status`) shows several applications moving at once.

Suggested wording: "You have several applications in flight. Would you like an interactive board view? You can drag applications between stages and export the changes back to your tracker."

If the user has zero or one active application, the tracker table is enough; do not offer the board.

---

## Generating the Board

1. **Read the tracker.** Load `applications/tracker.md`. If none exists, build one first (see `@references/application-tracker.md`); the board has nothing to show without it.
2. **Load the template.** Read `@references/kanban-board-template.html`.
3. **Populate the data block.** Replace the JSON inside `<script id="board-data" type="application/json">`:
   - `owner`: the user's name from the tracker header, or `[UNKNOWN]`.
   - `generated`: today's date, `YYYY-MM-DD`.
   - `cards`: one object per tracker row. Active rows map `role`, `organisation`, `stage`, `nextAction`, `nextDate`, and `notes`. Closed rows set `stage` to `Closed` and map `outcome`, `dateClosed`, and `learned`.
   - Use empty strings for unknown fields, never invented values. Remove the placeholder example card.
4. **Replace the header placeholders.** `{{NAME}}` and `{{DATE}}` appear in the header paragraph and in the local storage key; fill both.
5. **Write the file** to `applications/board.html` and tell the user to open it in their browser.

---

## Syncing Changes Back

The board has two export buttons: "Copy tracker markdown" and "Download tracker.md". Both produce a complete tracker file in the exact `applications/tracker.md` format, including the At a Glance counts.

When the user pastes exported markdown or mentions they have made board changes:

1. **Diff before overwriting.** Compare the exported markdown against the current `applications/tracker.md`. Summarise what changed ("Acme moved from Applied to Interviewing; next action updated on the TechCorp role") and confirm before writing.
2. **Update the tracker**, then regenerate the board so the file data matches (otherwise the board's "Reset to file data" button would restore stale data).
3. **Trigger follow-ups** exactly as the tracker guidance describes: a move to Interviewing suggests `/interview-master`; a move to Offer suggests salary negotiation or offer evaluation; a move to Closed with outcome Rejected offers the learnings loop and a rejection debrief.

If the user edited both the tracker file and the board since the last sync, treat the tracker file as authoritative, list the conflicts, and ask the user to resolve them. Never silently discard either side.

---

## Accessibility

The template is built to be usable without a mouse and without colour vision, and generated boards must keep it that way:

- Every stage is a text label on the column and on each card's accessible name; colour is decoration, never the only signal.
- Cards are keyboard operable: focus a card, use the left and right arrow keys or the labelled buttons to move it, and Enter to edit.
- Moves and saves are announced through a live region for screen readers.
- Overdue actions show a text `OVERDUE` tag, not just a colour change.
- The board respects the user's light or dark system preference.

If `career-helper-preferences.md` sets `dyslexia_friendly: true`, keep card notes short when populating the board, and explain the export flow in numbered steps. If `colour_blind: true`, the template already conveys nothing by colour alone; no changes are needed.

---

## What the Board Is Not

- It is not a replacement for the tracker principles: next actions and honest momentum still matter more than a pretty view.
- It is not a live sync: the HTML file cannot write to disk, which is why the export step exists. Make sure the user understands this the first time you generate a board.
- It is not a place for sensitive detail. Keep notes to short context; salary figures and personal reflections belong in the negotiation and learnings files.
