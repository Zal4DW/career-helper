# Application Learnings Loop

**Purpose:** Turn each interview, rejection, and win into a short, structured note, then periodically synthesise those notes into a single patterns file. Over a search of dozens of applications, this is how the user spots what is actually working and what keeps costing them, rather than relearning the same lesson each time.

**Applies to:** The learnings artefacts under `applications/learnings/`, created and updated by career-navigator. The synthesis file is read by the `/career-helper:status` command when it exists.

---

## Principles

1. **Capture close to the event.** A debrief written the same day is honest; one written a week later is fiction. Offer to run a debrief as soon as the user reports an interview or a decision.
2. **Never invent.** Record only what the user tells you or what existing files confirm. Mark anything uncertain as a guess, and leave `{{PLACEHOLDER}}` or `[UNKNOWN]` where you do not know. The user's honest read on a rejection is useful; a fabricated reason is harmful.
3. **Separate notes from synthesis.** Individual debriefs, rejections, and wins are raw input. The patterns file is the considered output. Do not rewrite history in the raw notes when synthesising.
4. **Synthesise periodically, not constantly.** Update the patterns file when enough new notes have accumulated to show a trend (a rough guide: every three to five new notes, or after any final-round outcome), not after every application.
5. **One observation beats a lecture.** When you surface a pattern, give the user the single most useful one and stop. See the Coaching Voice section in the main skill.

---

## File Layout

```
applications/
  learnings/
    patterns.md                                  one synthesis file, the considered output
    interview-notes/{org-slug}-{role-slug}.md    one debrief per interview round
    rejections/{org-slug}-{role-slug}.md         one analysis per rejection
    wins/{org-slug}-{role-slug}.md               one log per callback, strong interview, or offer
```

Use the same `{org-slug}-{role-slug}` naming as the rest of the application folder so notes line up with the work in `applications/{role-slug}/`.

---

## Running a Debrief

When the user reports a completed interview:

1. Load @references/interview-debrief-template.md.
2. Walk the user through it conversationally. Do not interrogate; ask for what they remember and capture it in their words.
3. Save to `applications/learnings/interview-notes/{org-slug}-{role-slug}.md`.
4. If this is a later round, do not overwrite the earlier round's note; create a new file or append a clearly dated section.

## Running a Rejection Analysis

When the user reports a rejection:

1. Load @references/rejection-analysis-template.md.
2. Separate what was actually said from the user's honest assessment of the likely real reason. Keep the two apart in the note.
3. Cross-reference the job description if the application folder has it, to identify any genuine gap the CV undersold.
4. Save to `applications/learnings/rejections/{org-slug}-{role-slug}.md`.
5. Move the role to the Closed section of `applications/tracker.md` (see the Application Tracker capability); do not delete it.

## Running a Win Log

When the user reports a callback, a strong interview, or an offer:

1. Load @references/win-log-template.md.
2. Capture which CV version and which framings worked, so the success is repeatable.
3. Save to `applications/learnings/wins/{org-slug}-{role-slug}.md`.

## Synthesising Patterns

When enough notes have accumulated:

1. Load @references/patterns-synthesis-template.md (create `applications/learnings/patterns.md` from it if it does not exist).
2. Read across the debriefs, rejections, and wins. Look for the same point appearing in three or more notes before calling it a pattern; a single data point is an anecdote.
3. Update each section with what the evidence supports, and add a dated row to the Synthesis Log explaining what changed and what prompted it.
4. Surface the single most useful pattern to the user, then stop.

---

## Relationship to Other Outputs

- The learnings loop feeds `/interview-master`: recurring objections and weak answers identified here are the raw material for sharper interview prep.
- Rejection analyses feed `/application-optimiser`: a gap the CV consistently undersells is a CV problem to fix, not just an interview problem.
- The tracker indexes applications; the learnings loop explains why they ended the way they did.

---

## Output

**Files:** `applications/learnings/patterns.md`, plus per-event notes under `applications/learnings/interview-notes/`, `rejections/`, and `wins/`.

**Load templates:**
- @references/interview-debrief-template.md
- @references/rejection-analysis-template.md
- @references/win-log-template.md
- @references/patterns-synthesis-template.md

---

*Application Learnings Loop v1.0 | Career Helper Plugin | Prosper AI Consulting, UK*
