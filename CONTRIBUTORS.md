# Contributors

Thank you to everyone who has contributed ideas, code, or feedback to Career Helper.

This file recognises community contributions that have shaped the plugin. Contributions may be direct (pull requests, issues, fixes) or indirect (ideas, prompts, frameworks that were adapted into skills). We credit both.

---

## Plugin Maintainer

**Paul Bratcher** ([@Zal4DW](https://github.com/Zal4DW)) — Prosper AI Consulting, UK
Plugin design, skill architecture, and ongoing maintenance.

---

## Community Contributors

### @sal-avelar-01

- **Contribution:** PR #29 — Job-search learnings loop (interview debriefs, rejection analyses, win logs, and synthesised patterns)
- **Date:** June 2026
- **What was adapted:** The structure of the learnings loop (per-event debrief, rejection, and win notes feeding a single synthesised patterns file) was adapted into `career-navigator` as a new capability, with templates rebuilt to the house style (UK English, "CV" rather than "resume", `{{PLACEHOLDER}}` syntax, no em dashes, template footers) and wired into `/career-helper:status`. The submitted master CV and the parallel `job-search/` directory were not adopted: personal data does not belong in the repo, and reusable value lives inside the plugin architecture.
- **Released in:** v1.14.0

Thank you for the learnings-loop idea. Treating each rejection and win as structured input to a synthesised view is a useful addition to how the plugin supports a long search.

---

### @enigmaicon-eng

- **Contribution:** PR #22 — Career coaching instructions and CV content verification framework
- **Date:** March 2026
- **What was adapted:** The verified-content-only guardrails, trigger-phrase STOP list, decision tree for source verification, and the 9-step job-analysis flow were extracted from this contribution and integrated into `application-optimiser` (new `verified-content-guardrails.md` and `master-facts-template.md` references, refactored `ATS-Helper.md` execution plan). The coaching-voice guidance (direct market feedback, flight-risk check, overthinking-versus-applying heuristic) was integrated into `career-navigator`. Tim gained master-facts awareness for dispatching CV work.
- **Released in:** v1.10.0

Thank you for raising the bar on content verification discipline. The hallucination guardrails in particular are a meaningful upgrade to how the plugin handles CV rewrites.

---

## How to Contribute

See [CONTRIBUTING.md](.github/CONTRIBUTING.md) for how to propose changes, what belongs in the repo, and the house style.

Every contribution — ideas, pull requests, bug reports, documentation fixes — is welcome, and every contributor will be credited here.

---

*Career Helper Plugin | Prosper AI Consulting, UK*
