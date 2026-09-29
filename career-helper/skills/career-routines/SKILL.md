---
name: career-routines
description: Use when the user wants parts of their job search to run on a schedule, or asks about routines they already have, such as putting the weekly update on a Cowork schedule, setting up narrower recurring tasks, or working out why a scheduled task did not run. Explains when a task runs in the cloud and when it needs their computer.
tags: routines, schedule, scheduled-tasks, cowork, automation, weekly, recurring, cron
---

# Career Routines

Put the recurring parts of your job search on a schedule, so the tracker, follow-ups, and market map keep themselves current between sessions.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Set Up a Routine | Creating a Claude Cowork scheduled task, tailored to your workspace and cadence |
| 2 | Routine Library | Choosing from the ready-made prompts, starting with the one-command weekly update |
| 3 | Review Your Routines | Seeing what is scheduled, what last ran, and fixing a routine that is not doing its job |
| 4 | Outside Cowork | Scheduling the same prompts from Claude Code Desktop, the command line, or a cloud Routine |

## Quick Start

```text
"Set up a weekly routine that keeps my job search moving"
"Schedule the weekly update for Monday mornings"
"Put my market map update on a timer"
"What routines do I have running?"
"My scheduled task did not run over the weekend. Why?"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true**: Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition ("Step 2 of 3. Next: choosing the cadence."). Refer to saved files by description, not filename. Repeat key details (routine names, days, times); do not assume the user remembers from earlier messages.
- **colour_blind: true**: Never use colour alone to convey meaning. Use labels, text, or icons for all status indicators.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once, "Do you have any accessibility preferences I should know about? For example, if you're dyslexic, I can adjust how I format things." If yes, ask whether you may save them so they do not have to repeat them next time, and save to `career-helper-preferences.md` using the format in @../tim/references/tim-preferences-format.md only if they agree. If the user has no preferences or declines to have them saved, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## How Scheduling Works Here

Career Helper is designed for Claude Cowork on Claude Desktop, and Cowork has scheduled tasks built in. You write a prompt once, choose how often it runs, and Cowork runs it as its own session with the plugin's skills available. The plugin supplies the prompts and the one command that does all the updating; Cowork supplies the scheduler.

The one thing to understand before scheduling anything is **where the task runs**, because it decides whether your computer needs to be on:

- **In the cloud** when the task does not need a folder on your computer. Your laptop can be closed. It can use connected tools, plugins, skills, web research, and files saved to your Claude account.
- **On your machine** when the task is given a folder on your computer. Then your computer and Claude Desktop must be available at the scheduled time.

Career Helper works in both Desktop Cowork and cloud Cowork, but they keep data differently, and routines depend on that. Desktop Cowork with a local folder is the most feature-rich option for persistence: every session and every scheduled run sees the same files on disk. Cloud Cowork keeps created files in the conversation's data store, so a long-running piece of work there means staying in the same conversation, and a scheduled run (a new session each time) cannot build on last week's files unless the workspace lives on something every session can reach, such as a connected drive.

So the honest default for a routine that reads the tracker or market map is Desktop Cowork with the workspace folder, running on the user's machine at a time it is awake. Say this plainly before setting anything up, and let the user choose.

**Load:** @references/cowork-scheduling.md for the setup steps, the cloud-or-local rules, permissions, and troubleshooting.

---

## 1. Set Up a Routine

**What you need:** Your workspace folder, a Cowork session, and a rough idea of cadence
**Load:** @references/cowork-scheduling.md
**Template:** @references/routines-register-template.md

Walk the user through one routine at a time:

1. **Check what exists.** Glob the workspace for `applications/tracker.md`, `market-map.md`, `applications/learnings/`, and any content calendar. A routine that reads a file which does not exist reports "not found" every week; suggest building the file first, or pick a routine whose inputs exist.
2. **Recommend the routine.** For almost everyone the first routine is the weekly update (`/career-helper:weekly-update`), because it already contains the standup, the follow-up check, and the market map update. Offer the narrower prompts only for a different cadence.
3. **Tailor the prompt.** Fill the bracketed parts (target role, location, employer where relevant). Keep the "do not invent" and "record decisions, do not ask" lines; they are what keep an unattended run honest.
4. **Decide where it runs.** Ask whether they want it on their machine (Desktop Cowork, folder chosen, computer must be awake) or in the cloud (no local folder, lid closed, but no memory of last week's files unless the workspace is on a connected drive). State the trade-off in two sentences.
5. **Give the exact steps.** Type `/schedule` in any Cowork task (or open Scheduled in the sidebar), paste the prompt, choose the cadence, choose the folder or leave it for the cloud, and save. Suggest running it once immediately to confirm it works and to approve anything it needs.
6. **Record it.** Add a row to `routines.md` (create from the template if absent): name, cadence, where it runs, prompt, date set up. `/career-helper:status` reads this file.

**Output:** `routines.md` at the workspace root, plus the copy-paste prompt and setup steps in conversation

---

## 2. Routine Library

**What you need:** Nothing; the library is ready-made
**Load:** @references/routine-library.md

Seven prompts, each safe to run unattended:

0. Weekly update (the one command; start here)
1. Monday job-search standup
2. Weekly market and role monitor
3. LinkedIn posting reminder
4. Application follow-up check
5. Pre-interview prep nudge (on demand)
6. Weekly market map update (standalone, for those who only want the map)

Present the library only when asked, or when the weekly update does not fit; do not offer all seven to a new user.

---

## 3. Review Your Routines

**What you need:** `routines.md`, and `updates/` or `market-watch/` if the routines write there
**Load:** @references/cowork-scheduling.md (Troubleshooting section)

Read `routines.md` and the output folders, then report:

- Each routine, its cadence, where it runs, and the date of its most recent output file (or "no output found")
- Anything that looks stale: a weekly routine with no output in two weeks
- Open items from the latest weekly update's "Decisions waiting for you" section
- The likely cause when a routine has not run, in order of frequency: the task was given a local folder and the computer was asleep; the task stalled on a permission it had not been granted; the input file it reads does not exist; the schedule was paused

Offer the fix for each, and update `routines.md` when something changes. Never guess at what a run did; read its output file or ask the user to open the run in Cowork's Scheduled list.

**Output:** Conversational review, updated `routines.md`

---

## 4. Outside Cowork

**What you need:** To know where the user runs Career Helper
**Load:** @references/cowork-scheduling.md (Outside Cowork section)

Some people run the plugin in Claude Code rather than Cowork. The prompts are identical; only the scheduler changes:

- **Claude Code Desktop local scheduled task:** Routines in the sidebar, New routine, Local; runs on the machine with the folder; needs the app open and the computer awake, with one catch-up run on wake
- **Command line with cron or launchd:** `claude -p "/career-helper:weekly-update" --permission-mode acceptEdits --permission-prompts none` from the workspace folder; the machine must be awake; no catch-up
- **Cloud Routine (claude.ai/code/routines):** runs without the machine but only clones a GitHub repository, so it suits a workspace kept in a private repository and nothing else

`/loop` in Claude Code repeats a prompt only while a session is open and is not a scheduler.

---

## Coaching Voice

Routines are plumbing, and plumbing should be boring:

- **One routine first.** A new user who schedules six things reads none of them. Start with the weekly update.
- **Be plain about where it runs.** "Your laptop needs to be awake on Monday morning" is a sentence the user needs to hear before they rely on it.
- **A quiet report is a good report.** If the weekly update says nothing changed, that is the routine working, not failing.
- **Do not let routines replace decisions.** The unattended run records what it could not decide; the user still decides. Say so.

---

## Output Standards

- **UK English** throughout
- **No emojis**; professional tone
- **Honest about limits**: where a task runs, what it can reach, and what it cannot do unattended
- **Copy-paste ready**: every prompt and every scheduler step is given verbatim
- **No invented state**: `routines.md` records only what the user confirms they have set up

### Tone of Voice

- Address the user as "you": "Your weekly update runs on..." not "The user's weekly update runs on..."
- Avoid hyperbole and cinema poster phrasing (not "set it and forget it" or "your job search on autopilot")
- Use the **Oxford comma** (serial comma: "tracker, follow-ups, and market map")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability names a template, load it with the @ reference before writing, and follow its structure and footer. Users and other skills rely on the same headings appearing in the same places.

---

## Related Skills

- **/career-navigator**: The application tracker the standup reads
- **/market-mapper**: The market map the weekly update refreshes
- **/linkedin-coach**: The content calendar the posting reminder reads
- **/getting-started**: Orientation; routes here for anything about scheduling

---

*Career Routines | Career Helper Plugin | Prosper AI Consulting, UK*
