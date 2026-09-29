# Market Map Board View

**Purpose:** Give the user an interactive, visual view of the watchlist when a markdown table stops being enough. The board renders every organisation on the map as a card in one of four priority columns (Act now, Warm, Watch, Quiet) and lets the user drag cards between priorities, edit the summary fields, and export the result back as the map's Watchlist section. It is the same mechanism as the application kanban board in `/career-navigator`, applied to the market map.

**Applies to:** The board artefact at `market-map-board.html`, generated from `market-map.md` using `@references/market-map-board-template.html`.

---

## Principles

1. **The map file remains the source of truth.** The board is a view, not a second database. `market-map.md` holds the signals, sources, and decision-maker detail; the board shows the watchlist summary. The Watchlist is the section the board exports, and the sync steps below also carry priority changes and organisation additions or removals into the affected detail sections, so the map never disagrees with itself.
2. **Never invent a signal or a person.** The board is populated only from rows that exist in the map. Unknown fields stay blank; the edit dialog says so.
3. **One board, regenerated.** There is only ever one `market-map-board.html`. Overwrite it after each weekly update; do not accumulate dated copies. (Dated update files live in `market-watch/`; the board is not one of them.)
4. **Offline and private.** The template is fully self-contained: no external scripts, fonts, or network calls. Board edits persist in the browser's local storage only, on the user's machine. The seed employer name appears only in the map header, never on the board.

---

## When to Offer the Board

Offer the board (do not push it) when:

- The map has eight or more organisations, or the user is running weekly updates and wants to see movement at a glance.
- The user asks to "see my watchlist as a board", "show me the market map visually", or similar.
- The user already uses the application board and asks whether the map can work the same way.

Suggested wording: "Would you like your watchlist as a board? Organisations sit in four priority columns, you can drag them between priorities as your own judgement changes, and export the result back into your map."

If the map has fewer than five organisations, do not offer the board proactively; the watchlist table is enough. A direct request is always honoured, whatever the map's size.

---

## Generating the Board

1. **Read the map.** Load `market-map.md`. If none exists, build one first (Capability 1); the board has nothing to show without it.
2. **Load the template.** Read `@references/market-map-board-template.html`.
3. **Populate the data block.** Replace the JSON inside `<script id="board-data" type="application/json">`:
   - `owner`: the user's name from the map header, or `[UNKNOWN]`.
   - `posture`: the posture from the map header (Employed and discreet, or Openly searching).
   - `generated`: today's date, `YYYY-MM-DD`.
   - `cards`: one object per watchlist row, mapping `organisation`, `overview`, `priority`, `signalGroup` (Hiring, Growth, Investment, or Change; empty string when there is no signal), `latestSignal` (the signal text and source, without the group or the date), `signalDate`, `decisionMaker`, `angle`, and `lastChecked` (empty string when the map shows `[UNKNOWN]`; the weekly update then checks the whole signal window for that organisation).
   - Use empty strings for unknown fields, never invented values. Remove the placeholder example card.
   - Escape every literal `<` inside JSON string values as `\u003c` (JSON.parse restores the character). Map content includes fetched web text; an unescaped closing script tag would otherwise terminate the data block and break, or worse script-inject, the page.
4. **Do not edit the HTML text.** The header paragraph is rendered from the JSON `owner`, `posture`, and `generated` values with `textContent`, so there are no placeholders outside the data block and nothing user-supplied is ever inserted as markup. (Browser state is keyed to a fingerprint of the data block, so a regenerated board loads fresh; if the previous board had edits that were never exported, the new board shows a recovery button that copies them as watchlist markdown, and keeps offering it across reloads until a copy succeeds.)
5. **Write the file** to `market-map-board.html` in the workspace root and tell the user to open it in their browser.

Regenerate the board at the end of every weekly update so it matches the map.

---

## Syncing Changes Back

The board has two export buttons: "Copy watchlist markdown" and "Download watchlist.md". Both produce the Watchlist section in the exact `market-map.md` format, ordered by priority and renumbered.

When the user pastes exported markdown or mentions they have made board changes:

1. **Diff before overwriting.** Compare the export against the current Watchlist section. Summarise what changed ("Two organisations raised to Act now; one removed; one added as Watch") and confirm before writing.
2. **Replace the Watchlist section** of `market-map.md`, then update the Priority line in the detail section of every organisation whose priority changed, so the map never carries two different priorities for one organisation. The board carries no reason for a priority change, so do not invent one: this sync happens in conversation, so ask the user once for the reason behind each changed priority and record it marked as their judgement; if they give none, record "Changed on the board on {{date}}; reason not given" and leave the old evidence-based reason out. Themes, coverage, and next actions are untouched. For an organisation the user added on the board, create a minimal detail section with `[NOT FOUND]` fields and offer to research it at the next update; for one the user removed, remove its detail section too.
3. **Priority changes made by hand are the user's judgement.** Record them, but at the next weekly update say plainly where the evidence disagrees ("You raised Acme to Act now; no hiring signal has appeared since") rather than silently overriding either side.
4. **Regenerate the board** so the file data matches (otherwise "Reset to file data" would restore stale data).

When the board is regenerated unattended (the weekly update does this), any edits made on the previous board and never exported are not lost: the new board detects them and offers a "Copy unexported changes from the previous board" button. Say in the update report that the board was regenerated, so the user knows to look for that button if they had been editing.

If the user edited both the map file and the board since the last sync, treat the map file as authoritative, list the conflicts, and ask the user to resolve them. Never silently discard either side.

---

## Accessibility

The template is built to be usable without a mouse and without colour vision, and generated boards must keep it that way:

- Every priority is a text label on the column, with a one-line meaning under it, and in each card's accessible name; colour is decoration, never the only signal.
- Cards are keyboard operable: focus a card, use the left and right arrow keys or the labelled Raise and Lower buttons to move it, and Enter to edit.
- Moves and saves are announced through a live region for screen readers.
- An organisation not checked for more than fourteen days shows a text `STALE` tag, not just a colour change.
- The board respects the user's light or dark system preference.

If `career-helper-preferences.md` sets `dyslexia_friendly: true`, keep the overview and angle fields short when populating the board, and explain the export flow in numbered steps. If `colour_blind: true`, the template already conveys nothing by colour alone; no changes are needed.

---

## What the Board Is Not

- It is not the evidence. Signal sources, dates, and decision-maker confirmations live in the map's detail sections; the board shows one line each.
- It is not a live sync: the HTML file cannot write to disk, which is why the export step exists. Make sure the user understands this the first time you generate a board.
- It is not a place for outreach drafts. Angles are one line; anything longer belongs in `/career-navigator` networking intelligence.
