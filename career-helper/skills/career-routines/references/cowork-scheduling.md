# Scheduling in Claude Cowork

**Purpose:** The setup steps, the rules that decide where a scheduled task runs, permissions, and troubleshooting for Career Helper routines in Claude Cowork.

**Applies to:** Claude Cowork on a paid plan (Pro, Max, Team, or Enterprise). Cowork's help centre article "Schedule recurring tasks in Claude Cowork" is the authority on current behaviour; where this guide and that article differ, the article wins.

---

## Create a Scheduled Task

1. In any Cowork task, type `/schedule` in the chat input, or click **Scheduled** in the left sidebar and create a new task there.
2. Give it a name you will recognise in the Scheduled list (for example, "Career weekly update").
3. Paste the prompt. For the weekly update, the whole prompt is `/career-helper:weekly-update`. For a narrower routine, paste the prompt from the library with its bracketed parts filled in.
4. Choose the cadence: daily, weekdays, weekly on a chosen day, or on demand.
5. Choose the folder, or leave it empty. This decides where the task runs (next section).
6. Save, then run it once straight away from the Scheduled list. Read the result, and approve anything it asks for so future runs do not stall.

**Dyslexia-friendly mode:** keep the steps above numbered, give them one at a time with a confirmation between each ("Step 2 of 6 done. Next: choosing the cadence."), ask the cloud-or-local question on its own with two short numbered options, and refer to the routine by its name ("your weekly update routine"), never by a filename or a prompt string. Troubleshooting is one likely cause per message, with the fix, not the whole table at once.

Each run is its own Cowork session with access to the same things a normal task has: connected tools, plugins, skills, and web research. Runs appear in the Scheduled list, where you can open one to see what it did.

---

## Where a Task Runs

Cowork runs a scheduled task remotely when it can, and on your computer when it must. The deciding factor is whether the task needs a folder on your computer.

| You choose | Where it runs | Your computer | What it can reach |
|:-----------|:--------------|:--------------|:------------------|
| No folder (or a workspace Cowork can reach from the cloud) | In the cloud | Can be off or asleep; Claude Desktop can be closed | Connected tools, plugins, skills, web research, files saved to your Claude account |
| A folder on your computer | On your machine | Must be on and awake, with Claude Desktop available | Everything above plus that folder |

### Desktop Cowork and cloud Cowork keep data differently

Career Helper keeps its working data in two places, and routines depend on both:

- **In your Claude account.** The application board, the market map board, the ikigai map, and the dashboards are artifacts in your account. Every session can reach them, including a scheduled run in the cloud, so a cloud-run weekly update can read and update your applications and market map with your computer closed.
- **In your workspace folder.** Per-application files (CVs, research briefs, application strategies), learnings notes, the dated reports, the snapshots, and `routines.md` are files. Desktop Cowork with a local folder reads and writes the same files every time. Cloud Cowork keeps files Claude creates in that conversation's data store, so a scheduled cloud run (a new session each time) cannot see last week's files unless the workspace lives somewhere every session can reach, such as a connected drive.

So both choices work for the weekly update, with different trade-offs:

1. **On your machine, with your workspace folder:** the fullest run (boards plus follow-ups from application strategies, learnings, and dated reports saved beside your other files). Pick a time you are normally at your desk (Monday 07:30 is a poor choice if the laptop is in a bag until nine).
2. **In the cloud, with no folder:** runs with your computer closed, reads and updates the boards and the progress dashboard, and gives you the report in the run itself. It cannot read your application strategies or learnings notes, and says so.

Do not move a folder of CVs to a shared or public location for the sake of a routine.

If a run you expected in the cloud instead waited for your machine, the task was given a local folder. That is the single most common reason a routine "did not run".

---

## Permissions and Unattended Runs

A scheduled run cannot ask you anything. Two consequences:

1. **Approve on the first run.** Run the task once by hand from the Scheduled list. If it needs permission to write files or use a tool, grant it then, so later runs do not stall waiting for an answer.
2. **Prompts must not need a decision.** Every Career Helper routine is written to record a decision rather than ask for one. The weekly update lists what it could not decide under "Decisions waiting for you" in its report. If you edit a prompt, keep that behaviour, and keep the "do not invent" line.

---

## Checking It Worked

- The weekly update writes `updates/{date}-weekly-update.md`; the market map update writes `market-watch/{date}-update.md` and updates the market map board. A dated file, or the `lastChecked` date on the market map board, is the proof a run happened.
- `/career-helper:status` reads `routines.md` and surfaces open decisions from the latest weekly update.
- Open the run in Cowork's Scheduled list to read what Claude actually did. A run that completed is not the same as a run that found anything; read the report.

---

## Troubleshooting

| Symptom | Most likely cause | Fix |
|:--------|:------------------|:----|
| No output file this week | The task has a local folder and the computer was asleep or Desktop was closed | Change the scheduled time to when you are at your desk, or move the workspace somewhere cloud-reachable |
| The run stalled or ended early | It needed a permission nobody was there to grant | Run it once by hand and approve what it asks for |
| Report says "no application board found" or "no market map found" | The board has not been built yet, or it was renamed | Build it first (`/career-navigator` Application Tracker, `/market-mapper` map); keep the fixed titles `Career Helper Applications` and `Career Helper Market Map` |
| The same news reported every week as new | The prompt lost its "report only what changed" instruction, or the map's last-checked dates are not being updated | Restore the library prompt; run the market map update by hand once so the dates roll forward |
| Cloud-run routine says it cannot read application strategies or learnings | Each cloud run is a new session and cannot see files from an earlier cloud conversation | That is expected; the boards are still updated. For the fuller run, schedule it from Desktop Cowork with your local folder |
| A routine says a board could not be reached | The run did not have access to artifacts, or the board was deleted | Open the board yourself to check it exists; run the routine once by hand and approve what it asks for |
| Nothing at all runs | The task is paused, or the plan does not include scheduled tasks | Check the Scheduled list; check the plan |
| Cannot find `/schedule` | Not in a Cowork task, or the feature is not available on this account | Open Cowork and start a task first; check the help centre for plan availability |

---

*Scheduling in Claude Cowork v2.0 | Career Helper Plugin | Prosper AI Consulting, UK*
