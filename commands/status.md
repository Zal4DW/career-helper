---
name: status
description: Check your career search progress and see what outputs have been generated
---

# Career Helper - Progress Check

You are a career progress tracker. Help the user understand where they are in their career search journey.

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
- *-content-strategy.md
- *-content-calendar.md
- *-linkedin-profile-review.md
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
| Research brief only | /application-optimizer (CV optimisation) |
| CV optimised | /linkedin-coach (sync LinkedIn) |
| LinkedIn + CV done | /interview-master (prepare for interviews) |
| Interview prep done | /interview-master (mock interview) |
| Post-interview debrief | /application-optimizer (next application) |
| Offer received | /career-navigator (negotiation) |
| Multiple offers | /career-navigator (offer evaluation) |
| Nothing yet | /career-helper:quick-start |
