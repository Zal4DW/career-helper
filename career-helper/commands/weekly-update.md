---
description: Run every recurring update in one go (application board standup, follow-ups, market map, learnings, progress dashboard) and save a dated report; built to run unattended on a Cowork schedule
---

# Career Helper - Weekly Update

You are running the recurring maintenance pass for someone's job search. This command exists so that one prompt, `/career-helper:weekly-update`, can be put on a Claude Cowork schedule and keep the search current without anyone sitting at the keyboard.

## Unattended Operation

Assume nobody is watching. Apply these rules for the whole run:

1. **Never ask a question.** Do not use AskUserQuestion and do not wait for input. Where a decision is needed (remove a quiet organisation, add a suggested one, mark an application closed, give a reason for a priority changed on the board), record it under "Decisions waiting for you" in the report and leave the boards and files unchanged on that point. One decision per numbered item, each with a plain "what to do" line; never two decisions in one item. This applies to everyone, not only in dyslexia-friendly mode.
2. **Never invent.** No applications, dates, contacts, signals, people, or URLs that the boards, files, or a cited public source do not support. A missing board or file is reported as missing, not filled in.
3. **Only touch what this command owns.** Write the dated report, update the market map board through the market mapper's own update logic, refresh the workspace snapshots (`applications/tracker.md`, `market-map.md`), and refresh the progress dashboard. Do not change application cards beyond reading them, and do not rewrite a CV, cover letter, or plan.
6. **Find outputs by register or title.** Use `career-helper-artefacts.md`, or the fixed titles in `/career-outputs` (Publishing Rules) when the register cannot be read. If a board cannot be reached in this run, say so in the report and carry on with what can be done.
4. **Read preferences first.** If `career-helper-preferences.md` exists, apply its accessibility settings to the report. Do not create the file if it is absent. With `dyslexia_friendly: true`: number every list, including the tracker and market map items; keep sentences short; signpost each section ("Section 2 of 6: follow-ups"); refer to boards and files by description ("your market map", "this week's report in your updates folder"), never by path or link; repeat the organisation or role name in every line that mentions it, so nothing depends on remembering an earlier line; use no idioms or metaphors. Apply these only when the preference is set; the default report keeps its paths and its normal shape. With `colour_blind: true`, nothing changes: the report already uses text labels only.
5. **Keep it to one screen.** A quiet week is a short report. Do not pad.

## Steps

Work through these in order, skipping any whose input file does not exist and saying so in one line.

### 1. Application board standup

Read the application board's `cards` collection (see `/career-navigator`, Application Tracker). Note any cards the user changed on the board since the last read. Report:
- Every active application with its next action, overdue actions first (next date in the past).
- Any application with no movement for more than two weeks.
- The three most important actions for the week, in order.

Refresh the `applications/tracker.md` snapshot if there is a workspace folder. Make no change to the cards themselves.

### 2. Follow-ups due

Read any `applications/*/application-strategy.md`. List follow-ups due today or overdue, each with the step the strategy describes. If none, one line.

### 3. Market map update

If a market map board exists, run the `/market-mapper` weekly update exactly as its `market-watch.md` reference describes: read the board (including priorities the user changed on it), re-check every organisation since its last-checked date, report only what changed, and roll only the signal, decision-maker, last-checked, and evidence-based priority changes into the board. Offered removals and additions are recorded in the update and in this report, never applied: the map's organisation list is unchanged until the user confirms. Save `market-watch/{{YYYY-MM-DD}}-update.md` (creating the `market-watch/` folder if it does not exist) and refresh the `market-map.md` snapshot. If there is no market map, say so in one line and move on. Keep the posture recorded in the map. Put the headline changes (new Act now organisations, priority changes) in this report and point to the update file for the rest.

### 4. Learnings check

If `applications/learnings/` holds per-event notes newer than `applications/learnings/patterns.md` (or no patterns file exists and three or more notes do), say so and list it under "Decisions waiting for you" as an offer to synthesise. Do not synthesise unattended; the user should read their own patterns with you in the room.

### 5. Progress dashboard

If the progress dashboard (`Career Helper Progress`) exists, refresh it through `/career-outputs` (Capability 2): update the pipeline counts, overdue actions, and market map counts, and append this week's row to the trend. Do not create a new dashboard unattended; if none exists, list the offer under "Decisions waiting for you".

### 6. Suggested next skill

From what the boards and files show, suggest one next step using the same table `/career-helper:status` uses. One line.

## Report

Save the report to `updates/{{YYYY-MM-DD}}-weekly-update.md` (create the folder if needed) and also print it. Structure:

```markdown
# Weekly Update: {{YYYY-MM-DD}}

## Do first
1. {{Overdue or most important action, with the application or organisation it belongs to}}
2. ...
3. ...

## Applications
{{Active applications and next actions; changes you made on the board; stalled applications; or "No application board found"}}

## Follow-ups due
{{List, or "None due"}}

## Market map
{{Headline changes and a pointer to market-watch/{{date}}-update.md; or "No market map found"}}

## Decisions waiting for you
1. {{One decision, then on the next line: What to do: {{plain action}}}}
2. {{...}}
{{Or "None"}}

## Boards and files touched
{{List, or "None"}}

*Generated using Career Helper. Found this helpful? Share your success story or suggest improvements at https://github.com/Zal4DW/career-helper*
```

If no Career Helper boards or files exist at all, the report is one line saying so and pointing to `/career-helper:quick-start`.

## Scheduling This Command

In Claude Cowork, type `/schedule` in any task, paste `/career-helper:weekly-update` as the prompt, choose weekly on Monday, and choose your workspace folder or leave it for the cloud. With a local folder the task runs on your machine, so pick a time the computer is normally awake; with no local folder it runs in the cloud, and still reaches your application board and market map, because they live in your Claude account. Run it once by hand first, to approve the tools it needs. `/career-routines` tailors the prompt, records the routine in `routines.md`, and reviews what is running.
