# Career Helper Preferences File Format

The shared format for `career-helper-preferences.md`, saved in the user's current working directory. Tim, or any skill invoked directly, may create it only after the user agrees to have their preferences saved.

Before creating the file, ask: "I'll save your preferences so you don't have to repeat yourself next time. Is that okay?" If the user declines, no file is created and everything still works.

## File Format

```yaml
---
name: [name]
career_stage: [stage]
version: 2
accessibility:
  dyslexia_friendly: false
  colour_blind: false
consent_to_store: true
created: [date]
last_session: [date]
---

## Target Roles
- [role, company]

## Completed
- [date]: [skill] ([context]) -> applications/ops-manager-tesco/research-brief.md
- [date]: [skill] ([context]) -> applications/ops-manager-tesco/cv-optimised.md
- [date]: [skill] ([context]) -> three-month-plan.md

## Flags
- [flag description]
- direction_questions_declined: true/false (if user opted out of or didn't gel with the direction-finding questions)

## Wellbeing Notes
- [date]: [brief note, e.g., "Processing redundancy, needs gentle pace" or "Confident, ready to push hard"]
```

## Maintenance

These rules apply only when the file exists because the user agreed to it. If they declined, never create or update it.

- Update after each skill completion (Completed section, last_session date)
- Wellbeing Notes section records emotional context that should carry across sessions, which keeps Tim from asking "how are you?" when he already knows
- Flags section records things that affect future decisions
- Version field (version: 2) tracks preferences file schema version
- If user asks to "forget me", delete the file and confirm deletion
- If YAML is corrupt on load, treat as new user and offer to start fresh
