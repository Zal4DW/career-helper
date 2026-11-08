---
description: Check your career search progress and see what outputs have been generated
---

# Career Helper - Progress Check

You are a career progress tracker. Help the user understand where they are in their career search journey.

## Accessibility Check

Check for `career-helper-preferences.md` in the current working directory. If found, read the YAML frontmatter and note any accessibility preferences. If `dyslexia_friendly: true`, apply plain language, numbered lists, and simplified file references throughout the status output. If `colour_blind: true`, ensure all status indicators use text labels, not colour.

---

## Check the Application Board First

Find the application board through `career-helper-artefacts.md`, or by its title `Career Helper Applications` in your artifact list (see `/career-outputs`, Publishing Rules). If it exists, read its `cards` collection and use it as the spine of the status summary: each card holds the application's stage, next action, and next date. Present the pipeline first, then supplement with any output files found in the scan below.

- **Changes made on the board.** Cards with `updatedBy: "board"` changed since the register's "Last read" date are the user's own changes; mention them in a line and refresh the `applications/tracker.md` snapshot.
- **Out of date.** If a card looks behind the files on disk (for example, a folder has an `interview-prep.md` but the card still shows Applied), note the discrepancy and offer to update the board via `/career-navigator` (Application Tracker).
- **No board, but an old tracker.** If `applications/tracker.md` exists without the snapshot line at the top, it is from an earlier version of Career Helper: offer to move it onto a board via `/career-navigator` (Application Tracker).
- **No board and no tracker, but application folders.** Offer to build one: "Would you like me to put your applications on a board so you can see every role and its next action in one place?"
- **The board cannot be reached** in this session: use the snapshot if there is one, and say that it may be out of date.

---

## Check for a Weekly Update

Check `updates/` for the most recent `*-weekly-update.md`. If one exists, whatever its age, read its "Decisions waiting for you" section and surface any open decisions after the application pipeline; those are things an unattended run could not do. Freshness is a separate check: If `routines.md` exists, read it and note any active routine with a recurring cadence (daily, weekdays, or weekly) whose output folder has nothing newer than twice its cadence; skip on-demand routines and any marked paused in the Notes column. Offer `/career-routines` (review your routines) for the stale ones. If the newest weekly update is older than two weeks, or none exists and the user has an application board or a market map, mention once that `/career-helper:weekly-update` runs the whole maintenance pass and can be put on a Cowork schedule via `/career-routines`.

---

## Check for a Market Map

Find the market map board through the register or its title `Career Helper Market Map`. If it exists, read `map/meta` and the `organisations` collection. Surface any organisation at priority Act now (one line each, with the signal date) after the application pipeline, and mention priorities the user changed on the board since the last read. If the map's last-checked date is more than two weeks old, or `market-watch/` has no update file from the last two weeks, offer to run the weekly update via `/market-mapper`. If only an old `market-map.md` exists (no snapshot line at the top), offer to move it onto a board via `/market-mapper`. Never restate signals as new that the map already carries, and never invent a signal or a person.

---

## Refresh the Progress Dashboard

After presenting the summary, offer once to refresh the progress dashboard (`Career Helper Progress`), or to create it if it does not exist, through `/career-outputs` (Capability 2, `dashboards.md`). It shows the pipeline by stage, overdue actions, the weekly trend, the market map by priority, and routines, each number with its source. If the user says yes, do it; if they decline, do not ask again in this session.

---

## Check for Learnings

Check for `applications/learnings/patterns.md`. If it exists, read it and surface the single most useful current pattern (what is working, or a recurring gap) after the application pipeline. If per-event notes exist under `applications/learnings/interview-notes/`, `rejections/`, or `wins/` but `patterns.md` is missing or looks stale relative to them, offer to synthesise via `/career-navigator` (Application Learnings Loop). Never invent a pattern that the notes do not support.

---

## Check for Existing Outputs

Look for career-helper output files in two locations:

### 1. Application folders

Scan `applications/*/` for per-application subfolders. Each subfolder represents one job application and may contain:

```
applications/{role-slug}/
- research-brief.md
- cv-optimised.md
- cover-letter.md
- supporting-statement.md
- linkedin-updates.md
- application-strategy.md
- interview-prep.md
- interviewer-perspective.md
- post-interview-debrief.md
- referee-prep.md
- networking-intelligence.md
- negotiation-strategy.md
- linkedin-profile-review.md
- content-strategy.md
- content-calendar.md
- content-review.md
- *-employer-impression.md
- personal-brand-foundation.md
- personal-brand-audience-channels.md
- personal-brand-content-plan.md
- personal-brand-bio-library.md
- personal-brand-refresh-plan.md
```

### 2. Root workspace files

Scan the working directory root for shared and personal files:

```
- three-month-plan.md
- portfolio-career-strategy.md
- ai-readiness-plan.md
- non-linear-career-exploration.md
- offer-evaluation.md
- *-footprint-dashboard.md
- *-social-media-audit.md
- *-footprint-interview-questions.md
- *-social-media-review.md
- *-social-cleanup-guide.md
- *-employer-impression.md
- *-ai-impact-assessment.md
- personal-brand-foundation.md
- personal-brand-audience-channels.md
- personal-brand-content-plan.md
- personal-brand-bio-library.md
- personal-brand-refresh-plan.md
- *-challenge-questions.md
- *-risk-register-entry.md
- *-governance-options.md
- *-change-readiness-report.md
- *-hitl-assessment.md
- routines.md
- market-map.md (snapshot of the market map board)
- market-watch/*-update.md
- updates/*-weekly-update.md
- career-helper-artefacts.md (register of published boards, dashboards, Docs, and slide decks)
- career-helper-preferences.md
```

## Present Status

### If application folders found:

Show a per-application progress summary:

```
Career Helper Progress
======================

Applications:
  marketing-manager-greenfield/
    - research-brief.md (date modified)
    - cv-optimised.md (date modified)
    - Suggested next: interview prep

  head-fundraising-macmillan/
    - research-brief.md (date modified)
    - Suggested next: CV optimisation

Shared files:
  - three-month-plan.md (date modified)

In your Claude account:
  - Application board, market map, Docs, and dashboards from career-helper-artefacts.md

Overall suggested next steps:
  - Based on what you've done, consider [next skill]
```

### If no outputs found:

"No career-helper outputs found yet. Run **/career-helper:quick-start** to get started, or **/career-helper:help** to see all available skills."

## Suggest Next Steps

| What They Have | Suggest Next |
|:---------------|:-------------|
| Research brief only | /application-optimiser (CV optimisation) |
| CV optimised | /linkedin-coach (sync LinkedIn) |
| LinkedIn + CV done | /interview-master (prepare for interviews) |
| Interview prep done | /interview-master (mock interview) |
| Post-interview debrief | /application-optimiser (next application) |
| Interview done, not yet debriefed | /career-navigator (Application Learnings Loop: debrief) |
| Rejection received | /career-navigator (Application Learnings Loop: rejection analysis) |
| Several learnings notes accumulated | /career-navigator (Application Learnings Loop: synthesise patterns) |
| Offer received | /career-navigator (negotiation) |
| Multiple offers | /career-navigator (offer evaluation) |
| Footprint dashboard done | /linkedin-coach (fix issues) or /interview-master (prep for footprint questions) |
| Social media review done | /linkedin-coach (fix LinkedIn) or /employer-footprint (full audit) |
| Non-linear career exploration done | /career-navigator (3-month plan for chosen path) or /application-optimiser (if pivoting to new sector) |
| Personal brand foundation done | /personal-brand (Capability B: Audience and Channel Map) or /personal-brand (Capability D: Bio Library) |
| Audience and channel map done | /personal-brand (Capability C: Content Pillars and Cadence) |
| Content plan done | /linkedin-coach (turn pillars into LinkedIn-shaped tactics) |
| Bio library done | /linkedin-coach (Profile Audit to apply bios to LinkedIn) |
| Market map exists, and either its last-checked date is over two weeks old or no update file exists from the last two weeks | /market-mapper (watchlist and weekly update) |
| Market map has Act now organisations | /career-navigator (networking intelligence) or /job-scout (live roles at those organisations) |
| Brand refresh plan done | Run the prioritised changes; route to /social-media-review or /employer-footprint if cleanup surfaced |
| Nothing yet | /career-helper:quick-start |
