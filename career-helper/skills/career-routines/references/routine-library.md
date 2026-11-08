# Routine Library

**Purpose:** Ready-made prompts for Career Helper routines. Each is safe to run unattended: it reads only what exists, records decisions instead of asking, and never invents. Copy one into Cowork's `/schedule` (see `cowork-scheduling.md`), fill the bracketed parts, and set the cadence shown.

Start with routine 0. It already contains routines 1, 4, and 6, so most people never need the others separately.

---

### 0. Weekly update (weekly, Monday morning; start here)

One command runs the whole maintenance pass and saves a dated report to `updates/`: application board standup with overdue actions first, follow-ups due, market map update, a check on whether learnings notes are ready to synthesise, the progress dashboard refreshed, and one suggested next skill. Anything it cannot decide is listed under "Decisions waiting for you".

```text
/career-helper:weekly-update
```

Cadence: Weekly, Monday, at a time your computer is normally awake if the task uses a local folder.

### 1. Monday job-search standup (weekly, Monday morning)

Reads your application board and tells you what to do this week.

```text
Read my Career Helper application board (the artifact titled "Career Helper Applications").
Give me a short Monday standup:
1. Every active application and its next action, with anything overdue flagged first.
2. Any application that has had no movement for over two weeks.
3. The three most important things for me to do this week, in order.
Keep it to one screen. Do not invent any application or status that is not on the board,
and do not change the board.
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
Read my Career Helper application board (the artifact titled "Career Helper Applications")
and any application-strategy.md files in my workspace.
Tell me which applications are due a follow-up today or are overdue, based on their
next dates. For each, remind me of the follow-up step from the application strategy.
If nothing is due, say so in one line. Do not invent dates or contacts.
```

Cadence: Weekdays.

### 5. Pre-interview prep nudge (on demand)

Set this up when an interview is booked, then trigger it the day before.

```text
I have an interview for [role] at [company] on [date]. Read the interview-prep file in
the matching applications folder. Give me a focused day-before checklist: the stories
to have ready, the questions I planned to ask, and the logistics to confirm, drawn only
from that file. If the file does not exist, or a section is missing, say which and list
only what the file supports; do not invent stories, questions, or logistics. Keep it
short and calm in tone.
```

Cadence: On demand.

### 6. Weekly market map update (weekly, Monday morning)

Keeps your ear to the ground on organisations like your employer without searching from scratch. Build the map first with `/market-mapper`; this routine only updates it.

```text
Read my Career Helper market map board (the artifact titled "Career Helper Market Map")
and the most recent file in market-watch/ if one exists. If there is no market map,
say so in one line and stop; do not ask me anything.
Run the market-mapper weekly update: re-check every organisation on the map for
hiring, growth, investment, and change signals dated after its last-checked date, and
report only what has changed. Update the board in place without overriding priorities
I set on it, save the update to market-watch/ with today's date, and refresh the
market-map.md snapshot. Keep the posture recorded in the map (if it says
employed and discreet, suggest only following, reading, or commenting). Offer, but do
not apply, removals of quiet organisations or additions of new ones. If nothing changed,
say so in one line. Do not invent a signal, a person, a title, or a URL.
```

Cadence: Weekly, Monday, 07:30 or whenever you start your week.

---

## Adapting These

- **Accessibility.** If you use dyslexia-friendly mode, the scheduled prompts will produce numbered, short-sentence output because every skill checks `career-helper-preferences.md` on each run. Keep that file in your workspace folder.
- **Keep prompts honest.** Every routine above tells Claude not to invent applications, dates, or claims. Keep that instruction in if you edit a prompt; it is what stops a scheduled task from drifting into fabrication when a file is missing.
- **Unattended runs cannot answer questions.** Any prompt you schedule should say what to do when a decision is needed: record it and move on. The weekly update does this by design.
- **Start with one.** For most people that is the weekly update. Add the narrower routines only if you want one at a different cadence.

---

*Routine Library v2.0 | Career Helper Plugin | Prosper AI Consulting, UK*
