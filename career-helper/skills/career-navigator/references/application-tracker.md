# Application Tracker

**Purpose:** Maintain a single, plain-text board of every live application so the user can see the whole search at a glance: what stage each role is at, what the next action is, and when it is due. This is the private, local alternative to a job-search spreadsheet or a paid tracking platform.

**Applies to:** The tracker artefact at `applications/tracker.md`, created and updated by career-navigator and read by the `/career-helper:status` command.

---

## Principles

1. **One file, one source of truth.** The tracker lives at `applications/tracker.md`. There is only ever one.
2. **Plain text, fully portable.** A markdown table the user owns. No external service, no account, no data leaving their machine.
3. **Never invent status.** Only record what the user has told you or what existing output files in the application folder confirm. If you do not know a stage or date, mark it `[UNKNOWN]` and ask.
4. **Action-oriented.** Every active row must have a next action and, where known, a date. A tracker without next actions is just a list.
5. **Honest about momentum.** If the user is stalled (many roles at "researching", none submitted), say so. See the Coaching Voice section in the main skill: overthinking versus applying.

---

## Building the Tracker from Scratch

When no tracker exists, offer to create one.

1. **Scan the application folders first.** Use Glob on `applications/*/` to find existing per-role work. Each subfolder is an application already in progress. Infer the likely stage from which files exist:
   - `research-brief.md` only: stage is Researching.
   - `cv-optimised.md` or `cover-letter.md` present: stage is Applying or Applied.
   - `interview-prep.md` or `interviewer-perspective.md` present: stage is Interviewing.
   - `post-interview-debrief.md` present: stage is Post-interview or Rejected (ask which).
   - `negotiation-strategy.md` or `offer-evaluation.md` present: stage is Offer.
2. **Confirm with the user.** Inferred stages are a starting point, not fact. Ask the user to correct anything and to add applications that have no folder yet.
3. **Capture the essentials per row** (see the template): role, organisation, stage, next action, next date, and a short note.
4. **Save** to `applications/tracker.md`.

---

## Stages

Use this fixed, ordered set so the board reads consistently. These are text labels, never colour-coded, so they remain accessible.

| Stage | Meaning |
|:------|:--------|
| Researching | Considering the role; research underway, not yet applied |
| Applying | Tailoring CV, cover letter, or supporting statement |
| Applied | Submitted, awaiting response |
| Interviewing | One or more interview stages in progress |
| Offer | Offer received; evaluating or negotiating |
| Closed: accepted | Offer accepted |
| Closed: rejected | Rejected, withdrawn, or no response after follow-up |

---

## Updating the Tracker

When the user reports progress ("I submitted the Acme application", "I have a first interview Tuesday"), update the relevant row:

1. Move the stage forward (or to a Closed state).
2. Rewrite the next action and next date.
3. Add a dated note if context matters (for example, "recruiter screen booked 12 June").
4. Keep closed rows in a separate section at the bottom so the active board stays readable.

Never silently overwrite history the user may want. If a role is rejected, move it to the closed section rather than deleting it; the pattern across closed roles is useful for `/interview-master` post-interview coaching.

---

## Reading the Board for Insight

After updating, offer one honest observation when the data warrants it:

- **Stalled pipeline:** several roles stuck at Researching or Applying, none Applied. "You have four roles in progress but none submitted yet. Which one is closest to ready?"
- **Thin pipeline:** only one active application. Suggest building volume via `/application-optimiser`.
- **Overdue actions:** next dates in the past. Surface them plainly.
- **Healthy momentum:** acknowledge it briefly without flattery.

Do not lecture. One useful observation beats a paragraph of coaching.

---

## Relationship to Other Outputs

- The tracker is an index, not a replacement for the per-role files. Each row points to the work in `applications/{role-slug}/`.
- The `/career-helper:status` command reads the tracker if it exists and uses it as the spine of the progress summary, falling back to a folder scan if there is no tracker.
- The Application Strategy capability in `/application-optimiser` produces a per-role plan; the tracker aggregates across all roles.
- The Kanban Board View (see `@references/kanban-board.md`) renders the tracker as an interactive HTML board at `applications/board.html`. The tracker file remains the source of truth; board exports are merged back into it, never the other way round by default.

---

## Output

**File:** `applications/tracker.md`

**Load template:** @references/application-tracker-template.md

---

*Application Tracker v1.0 | Career Helper Plugin | Prosper AI Consulting, UK*
