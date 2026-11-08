# Application Tracker

**Purpose:** Keep one record of every live application so you can see the whole search at a glance: what stage each role is at, what the next action is, and when it is due.

**Applies to:** The application board (`Career Helper Applications`), an interactive page in your Claude account whose database is the record. Created and updated by career-navigator, read by `/career-helper:status`, `/career-helper:weekly-update`, job-scout, market-mapper, and the learnings loop. When the session has a workspace folder, a read-only snapshot is kept at `applications/tracker.md`.

---

## Principles

1. **One board, one record.** Every application lives as a card in the board's database. There is only ever one board; find it through `career-helper-artefacts.md` or its fixed title (see `@../career-outputs/references/publishing-rules.md`).
2. **You and Claude both write to it.** You move and edit cards on the page; Claude adds and updates them in conversation and in scheduled runs. Each change is stamped with who made it, so nothing you change is silently overwritten.
3. **Never invent status.** Only record what you have said or what existing files in the application folder confirm. Unknown text fields stay empty and are asked about; never guess a stage or a date.
4. **Action-oriented.** Every active card should have a next action and, where known, a date. A tracker without next actions is just a list.
5. **Honest about momentum.** If the search is stalled (many roles at Researching, none submitted), say so. See the Coaching Voice section in the main skill: overthinking versus applying.

---

## Card Fields

One document per application in the `cards` collection, with a stable id built from the organisation and role (for example `example-org-operations-director`).

| Field | Meaning |
|:------|:--------|
| `role` | Role title |
| `organisation` | Organisation name |
| `stage` | One of the stages below |
| `nextAction` | What you do next |
| `nextDate` | `YYYY-MM-DD`, or empty |
| `notes` | Short context only; no salary figures or personal reflections |
| `outcome` | For Closed cards: Accepted, Rejected, Withdrawn, or No response |
| `dateClosed` | For Closed cards: `YYYY-MM-DD` |
| `learned` | For Closed cards: one line, if any |
| `folder` | The application folder, for example `applications/example-org-operations-director/`, or empty |
| `created` | `YYYY-MM-DD` the card was added |
| `updated`, `updatedBy` | Stamped on every write: `claude` or `board` |

The `board/meta` document holds `owner` (the user's name as they gave it, or empty) and `created`.

---

## Stages

A fixed, ordered set so the board reads consistently. They are text labels, never colour codes.

| Stage | Meaning |
|:------|:--------|
| Researching | Considering the role; research underway, not yet applied |
| Applying | Tailoring CV, cover letter, or supporting statement |
| Applied | Submitted, awaiting response |
| Interviewing | One or more interview stages in progress |
| Offer | Offer received; evaluating or negotiating |
| Closed | Finished, with an outcome: Accepted, Rejected, Withdrawn, or No response |

---

## Building the Board from Scratch

When no board exists, offer to create one.

1. **Scan the application folders first.** Use Glob on `applications/*/` to find existing per-role work. Each subfolder is an application already in progress. Infer the likely stage from which files exist:
   - `research-brief.md` only: Researching.
   - `cv-optimised.md` or `cover-letter.md` present: Applying or Applied (ask which).
   - `interview-prep.md` or `interviewer-perspective.md` present: Interviewing.
   - `post-interview-debrief.md` present: Interviewing, or Closed with outcome Rejected (ask which).
   - `negotiation-strategy.md` or `offer-evaluation.md` present: Offer.
2. **Import an old tracker.** If `applications/tracker.md` exists from an earlier version of Career Helper (it has no snapshot line at the top), read its rows as the starting point; it is the user's own record.
3. **Confirm with the user.** Inferred stages are a starting point, not fact. Ask the user to correct anything and to add applications that have no folder yet.
4. **Publish and fill the board** through `/career-outputs` (Capability 1): publish the page, then write one card per confirmed application in a single batch.
5. **Write the snapshot** to `applications/tracker.md` when there is a workspace folder, using @application-tracker-template.md.

---

## Updating the Board

When the user reports progress ("I submitted the Example Org application", "I have a first interview Tuesday"):

1. **Read the board first,** so you are working from its current state, including any changes the user made on the page.
2. **Update the card:** move the stage, rewrite the next action and next date, and add a short note if context matters (for example "recruiter screen booked 12 June").
3. **Close, never delete.** A rejected or withdrawn role moves to Closed with its outcome; the pattern across closed roles feeds the learnings loop and `/interview-master`.
4. **Refresh the snapshot** if there is a workspace folder.

When the user has changed cards on the page since you last read the board, summarise those changes in a line and act on them: a move to Interviewing suggests `/interview-master`; a move to Offer suggests salary negotiation or offer evaluation; a move to Closed with outcome Rejected offers the learnings loop and a rejection debrief.

---

## Reading the Board for Insight

After updating, offer one honest observation when the data warrants it:

- **Stalled pipeline:** several roles stuck at Researching or Applying, none Applied. "You have four roles in progress but none submitted yet. Which one is closest to ready?"
- **Thin pipeline:** only one active application. Suggest building volume via `/job-scout` or `/application-optimiser`.
- **Overdue actions:** next dates in the past. Surface them plainly.
- **Healthy momentum:** acknowledge it briefly without flattery.

Do not lecture. One useful observation beats a paragraph of coaching.

---

## Relationship to Other Outputs

- The board is an index, not a replacement for the per-role files. Each card points to the work in `applications/{role-slug}/` through its `folder` field.
- `/career-helper:status` and `/career-helper:weekly-update` read the board as the spine of the progress summary and the progress dashboard.
- The Application Strategy capability in `/application-optimiser` produces a per-role plan; the board aggregates across all roles.
- The page itself, sharing it, and syncing the user's changes are covered in `@references/kanban-board.md`.

---

## Output

**Record:** The application board's database (`Career Helper Applications`)
**Snapshot:** `applications/tracker.md` (read-only, regenerated), using @application-tracker-template.md

---

*Application Tracker v2.0 | Career Helper Plugin | Prosper AI Consulting, UK*
