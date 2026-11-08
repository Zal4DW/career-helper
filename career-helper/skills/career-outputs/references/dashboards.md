# Dashboards

**Purpose:** What goes on each Career Helper dashboard, where every number comes from, and how a dashboard is refreshed rather than duplicated.

**Applies to:** The progress dashboard (`Career Helper Progress`), refreshed by `/career-helper:status` and `/career-helper:weekly-update`, and the footprint dashboard (`Career Helper Footprint`), produced by `/employer-footprint`.

---

## How Dashboards Are Built

1. **Look it up** in the register, or by its fixed title (see `publishing-rules.md`).
2. **New dashboard:** start it from Claude's Dashboard artifact type with the fixed title, and follow the type's own instructions for its data files and layout.
3. **Existing dashboard:** update its data files at the same link. Do not create another dashboard for a new week or a new score.
4. **Every number shows its source.** Name the board, file, or search it came from, and the date it was read. A number with no source is left out.
5. **Every status has a text label.** "Ready", "Overdue", "Act now", "Strong", "Concern". Colour may support a label, never replace it.
6. **The markdown report stays.** Dashboards sit beside the dated markdown reports (`updates/`, `{name-slug}-footprint-dashboard.md`), which remain the full written record.

---

## Progress Dashboard

**Title:** `Career Helper Progress`
**Refreshed by:** `/career-helper:status` (on request) and `/career-helper:weekly-update` (every run)

### Sections

| Section | Contents | Source |
|:--------|:---------|:-------|
| Pipeline now | Count of applications in each stage: Researching, Applying, Applied, Interviewing, Offer, Closed | Application board database |
| Needs attention | Overdue next actions (role, organisation, date), shown as a list with an `OVERDUE` label | Application board database |
| This week | Applications added, moved, and closed since the last update | Application board, `updated` dates |
| Trend | One row per weekly update: date, active, applied, interviewing, offers, closed | The dashboard's own weekly history data |
| Response rate | Applications that reached Interviewing or beyond, divided by applications that reached Applied or beyond, with both counts shown | Application board database |
| Market map | Count of organisations by priority (Act now, Warm, Watch, Quiet), and new signals since the last update | Market map database |
| Learnings | The top recurring patterns, one line each | `applications/learnings/patterns.md` if it exists |
| Routines | Each routine, its cadence, and the date of its last output | `routines.md` and the output folders |

### Rules

- **Append, do not rewrite, the trend.** Each weekly update adds one row with that day's date. Never back-fill a week that was not recorded.
- **Small numbers stay honest.** With fewer than five applications past Applied, show the counts and say "too few to call a rate" instead of a percentage.
- **No targets the user did not set.** Show what happened; do not grade it against invented benchmarks.
- **Leave out empty sections** (for example, no market map yet) rather than showing zeros that look like failure.

---

## Footprint Dashboard

**Title:** `Career Helper Footprint`
**Produced by:** `/employer-footprint`, after the markdown report is written using `footprint-dashboard-template.md`

### Sections

| Section | Contents | Source |
|:--------|:---------|:-------|
| Overall score | The overall score out of 10 with its text rating as the report gives it (GREEN: Strong, AMBER: Adequate, or RED: Concern) and the one-line summary | The written report |
| Dimension scores | All eight dimensions, each with its score, text rating, and one line of evidence | The written report's dimension sections |
| What employers see first | The first-page search results, each with its impression label (Positive, Neutral, Concerning) | The searches recorded in the report |
| Top actions | The prioritised recommendations, each with its effort and the dimension it improves | The report's recommendations |
| Target fit | When a target company was given: how the footprint lines up with its stated values | The report's employer impression section |

### Rules

- **Scores come only from the written report.** The dashboard never rescores anything.
- **Every finding links to its source** (the profile, post, or search result), as recorded in the report.
- **Re-running the analysis updates the same dashboard,** keeping the previous overall score as a "Last time" figure with its date, so progress is visible.
- **The dashboard covers only the user.** It never shows another person's details.

---

*Dashboards | Career Helper Plugin | Prosper AI Consulting, UK*
