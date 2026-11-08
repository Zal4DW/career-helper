# Application Board

**Purpose:** Give the user an interactive view of their whole application pipeline that they and Claude keep up to date together. Every application is a card in one of six stage columns (Researching, Applying, Applied, Interviewing, Offer, Closed); the user can drag cards between stages, edit next actions, and add or remove applications, and Claude reads those changes back in any later session.

**Applies to:** The artifact titled `Career Helper Applications`, published from the page in `@references/kanban-board-template.md`. Its database is the application record described in `@references/application-tracker.md`.

---

## Principles

1. **The board is the record.** Its database holds every application. The workspace file `applications/tracker.md` is a read-only snapshot for portability.
2. **Never invent status.** Cards are written only from what the user has said or what their files confirm. Unknown fields stay empty.
3. **One board.** Find it through the register or its fixed title before doing anything; never publish a second copy (see `@../career-outputs/references/publishing-rules.md`).
4. **Private by default.** The board is visible only to the user unless they share it themselves.

---

## When to Offer the Board

The board is the tracker, so it is created the first time the user wants to track applications (see `application-tracker.md`). Offer to open it when:

- The user asks to "see my pipeline", "show me a board", "visualise my applications", or similar.
- A status review shows several applications moving at once.

Suggested wording the first time: "Your applications are on a board in your Claude account. You can drag them between stages and edit next steps there; I will see your changes next time we talk."

---

## Publishing and Refreshing the Page

Follow `/career-outputs` Capability 1:

1. **Look it up** in `career-helper-artefacts.md`, then by the title `Career Helper Applications`.
2. **New board:** publish the page in `kanban-board-template.md` unchanged, with capabilities `{"db": {}, "user": {}}`, then write the cards and the `board/meta` document (fields in `application-tracker.md`) in one batch. Read the collection back once and confirm the count.
3. **Existing board on an older page version:** republish the new page file to the same link. The cards are kept.
4. **Record** the link and page version in the register.

The page holds no user data, so there is nothing to fill in or escape in the file. It renders every value as plain text.

---

## Syncing the User's Changes

There is no export step. When any task uses the board:

1. Read the `cards` collection.
2. Pick out cards with `updatedBy: "board"` whose `updated` timestamp is later than `lastReadByClaude` in the meta document (see `publishing-rules.md`, Reading Data Back).
3. Summarise them in a line ("You moved Example Org to Interviewing and set a follow-up for Friday"), confirm anything that looks accidental (a card removed from Interviewing, for example), and trigger follow-ups as `application-tracker.md` describes.
4. Refresh the `applications/tracker.md` snapshot, and write the current time to `lastReadByClaude` (and the register's "Last read").

If the user has edited the snapshot file by hand, show the differences against the board and offer to apply them. Never silently discard either side.

---

## Accessibility

The page is built to be usable without a mouse and without colour vision; keep it that way:

- Every stage is a text label on the column and in each card's accessible name; colour is decoration, never the only signal.
- Cards are keyboard operable: focus a card, use the left and right arrow keys or the labelled Back and Advance buttons to move it, and Enter to edit.
- Saves and errors are announced through a live region for screen readers.
- Overdue actions show a text `OVERDUE` tag.
- The page follows the user's light or dark theme and works at phone width.

If `career-helper-preferences.md` sets `dyslexia_friendly: true`, keep card notes short when writing cards, and explain the board in numbered steps the first time. If `colour_blind: true`, no changes are needed.

---

## Sharing

If the user wants a mentor, partner, or coach to see the board, explain the options and let them share it from the artifact's share menu: Viewer (read-only, recommended) or Contributor (can move and edit cards). Never share it for them, and remind them that anyone they share with sees every card's notes.

---

## What the Board Is Not

- It is not a replacement for the tracker principles: next actions and honest momentum still matter more than a tidy view.
- It is not a place for sensitive detail. Notes are short context; salary figures and personal reflections belong in the negotiation and learnings documents.

---

*Application Board v2.0 | Career Helper Plugin | Prosper AI Consulting, UK*
