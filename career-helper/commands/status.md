---
description: Check your career search progress and see what outputs have been generated
---

# Career Helper - Progress Check

You are a career progress tracker. Help the user understand where they are in their career search journey.

## Plugin Version Check

Before checking career progress, read the installed plugin version and check for updates.

### Step 1: Read installed version

Read the file `career-helper/.claude-plugin/plugin.json` (relative to the repository root where this plugin is installed). Extract the `version` field.

### Step 2: Check for updates via GitHub PRs

1. Use WebFetch to retrieve the release list: `https://api.github.com/repos/Zal4DW/career-helper/releases`
   - Find the release whose tag matches the installed version and note its `published_at` date.
   - If no matching release is found, fall back to: `https://api.github.com/repos/Zal4DW/career-helper/tags` to locate the tag, then look up its commit date.

2. Use WebFetch to retrieve closed PRs merged after that date: `https://api.github.com/repos/Zal4DW/career-helper/pulls?state=closed&per_page=50`
   - Filter to PRs where `merged_at` is after the installed version's release date.

### Step 3: Report version status

Show the version status before the career progress section:

**If up to date:**
```
Plugin Version: [version] (up to date)
```

**If updates are available:**
```
Plugin Version: [installed version] — updates available

What's new since your version:
- [PR title] (#[number])
- [PR title] (#[number])

Update: https://github.com/Zal4DW/career-helper
```

**If the GitHub check fails** (no network access or API error), show:
```
Plugin Version: [version] (unable to check for updates)
```
Then proceed to career progress.

## Check for Existing Outputs

Look for career-helper output files in the current working directory and common locations:

```
*.md files matching patterns:
- *-research-brief.md
- *-cv-optimized.md
- *-linkedin-updates.md
- *-application-strategy.md
- *-interview-prep.md
- *-interviewer-perspective.md
- *-post-interview-debrief.md
- *-networking-intelligence.md
- *-negotiation-strategy.md
- *-offer-evaluation.md
- three-month-plan.md
- portfolio-career-strategy.md
- ai-readiness-plan.md
- *-challenge-questions.md
- *-risk-register-entry.md
- *-governance-options.md
- *-change-readiness-report.md
- *-hitl-assessment.md
- *-content-strategy.md
- *-content-calendar.md
- *-linkedin-profile-review.md
- *-footprint-dashboard.md
- *-employer-impression.md
- *-social-media-audit.md
- *-footprint-interview-questions.md
- *-social-media-review.md
- *-social-cleanup-guide.md
```

## Present Status

### If outputs found:

Show a progress summary:

```
Career Helper Progress
======================

Completed:
- [skill] [output file] (date modified)

Suggested next steps:
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
| Offer received | /career-navigator (negotiation) |
| Multiple offers | /career-navigator (offer evaluation) |
| Footprint dashboard done | /linkedin-coach (fix issues) or /interview-master (prep for footprint questions) |
| Social media review done | /linkedin-coach (fix LinkedIn) or /employer-footprint (full audit) |
| Nothing yet | /career-helper:quick-start |
