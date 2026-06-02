# Scheduled Job-Search Routines

**Purpose:** Turn the job search from a series of one-off sessions into a living process that keeps itself moving. Claude Cowork can run a saved prompt on a schedule (daily, weekly, weekdays only, or on demand), with full access to your skills, plugins, and local files each time. This guide gives you ready-made routines to drop into a scheduled task.

**Applies to:** Users running Career Helper inside Claude Cowork on Claude Desktop, on a paid plan (Pro, Max, Team, or Enterprise).

---

## How Scheduled Tasks Work

In Claude Cowork, type `/schedule` in the chat input to create a scheduled task. You write the prompt once, choose how often it runs, and Cowork runs it at that cadence as its own session. Each run can read your workspace folder and use the Career Helper skills, so a scheduled task can update your tracker, monitor the market, or remind you what to post.

**Two honest limitations to know before you rely on this:**

1. **Your computer must be awake and Claude Desktop must be open** for a scheduled task to run. If the machine is asleep or the app is closed at the scheduled time, Cowork skips that run and catches up the next time you open Claude Desktop.
2. **Scheduled tasks are a Cowork feature, not part of the plugin itself.** The plugin supplies the skills; Cowork supplies the scheduler. If you are using Career Helper in the Claude Code CLI or the web app rather than Cowork on Desktop, these routines will not run on a timer. You can still run the same prompts manually whenever you like.

Always keep your work in one folder (see the Workspace Tip in the README) so every scheduled run reads from and writes to the same place.

---

## Ready-Made Routines

Copy a prompt below, run `/schedule`, paste it in, and set the cadence shown. Adjust the bracketed parts to your situation.

### 1. Monday job-search standup (weekly, Monday morning)

Reads your tracker and tells you what to do this week.

```text
Read applications/tracker.md in my workspace. Give me a short Monday standup:
1. Every active application and its next action, with anything overdue flagged first.
2. Any application that has had no movement for over two weeks.
3. The three most important things for me to do this week, in order.
Keep it to one screen. Do not invent any application or status that is not in the tracker.
```

Cadence: Weekly, Monday.

### 2. Weekly market and role monitor (weekly)

Watches the market for your target roles so you are not searching from scratch each time.

```text
Search for new job postings and relevant market news from the past seven days for
[your target role, e.g. "Head of Marketing"] in [your location/region]. Use the
career-navigator approach: cite sources with dates, and be honest about volume and
seniority. List up to eight roles worth a closer look, with a one-line reason each.
Save the summary to a dated file in my workspace. Do not pad the list to reach eight.
```

Cadence: Weekly.

### 3. LinkedIn posting reminder (weekly, aligned to your content calendar)

Keeps your personal-brand cadence on track without you having to remember it.

```text
Read my content calendar (personal-brand-content-plan.md or content-calendar.md) if
present in my workspace. Remind me what I planned to post this week and which content
pillar it belongs to. Suggest one specific post idea drawn only from my existing pillars
and notes. Do not invent achievements or claims about me.
```

Cadence: Weekly.

### 4. Application follow-up check (weekdays)

Catches the follow-ups that quietly slip.

```text
Read applications/tracker.md and any application-strategy.md files in my workspace.
Tell me which applications are due a follow-up today or are overdue, based on their
next dates. For each, remind me of the follow-up step from the application strategy.
If nothing is due, say so in one line. Do not invent dates or contacts.
```

Cadence: Weekdays.

### 5. Pre-interview prep nudge (on demand)

Set this up when an interview is booked, then trigger it the day before.

```text
I have an interview for [role] at [company] on [date]. Read the interview-prep file in
the matching applications folder. Give me a focused day-before checklist: the five
stories to have ready, the questions I planned to ask, and the logistics to confirm.
Keep it short and calm in tone.
```

Cadence: On demand.

---

## Adapting These

- **Accessibility.** If you use dyslexia-friendly mode, the scheduled prompts will produce numbered, short-sentence output because every skill checks `career-helper-preferences.md` on each run. Keep that file in your workspace folder.
- **Keep prompts honest.** Every routine above tells Claude not to invent applications, dates, or claims. Keep that instruction in if you edit a prompt; it is what stops a scheduled task from drifting into fabrication when a file is missing.
- **Start with one.** The Monday standup is the highest-value routine for most people. Add others once it is part of your week.

---

*Scheduled Job-Search Routines v1.0 | Career Helper Plugin | Prosper AI Consulting, UK*
