# Career Helper - Claude Code Plugin

End-to-end career support with guided coaching for job seekers at all levels, plus AI governance guidance for Non-Executive Directors and Board Governors. Twelve skills including Tim (your personal career coach who guides you through the right skills in the right order), getting started guidance, AI impact assessment, employer footprint analysis, social media review, LinkedIn optimisation, ATS CV rewriting, cover letters and supporting statements, interview preparation, reference and referee prep, job search strategy with an application tracker, career transitions (including non-linear career exploration: entrepreneurship, startups, public sector, charity, intrapreneurship, and multi-role skilling), board-level AI oversight, and personal brand building (Why You, Why Them, Why Now positioning, audience and channel map, content pillars, bio library). Ready-made Claude Cowork scheduled routines keep the search moving between sessions.

Available to all Claude users, including free subscriptions.

**Created by:** Prosper AI Consulting | [GitHub](https://github.com/Zal4DW/career-helper) | [Issues](https://github.com/Zal4DW/career-helper/issues)

---

## Installation

### From the Claude Desktop App (Recommended)

1. Click the **+** button next to the chat input
2. Select **Add plugins...**
3. In the Browse plugins dialog, open the filter dropdown and choose **Add marketplace from GitHub**
4. Enter `Zal4DW/career-helper` and click **Sync**
5. Click **Install** on the Career Helper plugin

That's it - the skills and commands are ready to use immediately. Available on all Claude plans, including free subscriptions.

### Using Claude Code CLI

```bash
claude plugin marketplace add Zal4DW/career-helper
claude plugin install career-helper@career-helper
```

### Manual Installation

Clone the repo into your Claude Code plugins directory:

```bash
git clone https://github.com/Zal4DW/career-helper.git ~/.claude/plugins/career-helper
```

---

## Getting Started

Not sure where to begin? Try one of these:

```
/career-helper:career-coach        Guided coaching with Tim - recommended for new users
/getting-started                   Full overview of everything available
/career-helper:quick-start         Guided questions to route you to the right skill
/career-helper:help                Skill navigator - describe your situation
```

Or just describe what you need:

```
"I want to apply for a Senior PM role at Google"
"Help me prepare for an interview next Tuesday"
"I got an offer - should I negotiate?"
"I want to go fractional"
"I'm thinking about starting my own business"
"What are my options besides climbing the corporate ladder?"
"Check my digital footprint before I apply"
"Review my social media - I'm a graduate about to start applying"
```

---

## Skills

| Skill | What It Does | Command |
|:------|:-------------|:--------|
| **Getting Started** | Full overview, preparation checklists, workflow planning, skill tips, power user strategies, scheduled Cowork routines | `/getting-started` |
| **Employer Footprint** | Digital footprint audit through employer's eyes, social media scan, credit-report style dashboard, interview questions from online presence | `/employer-footprint` |
| **Social Media Review** | Quick social media check through recruiter's eyes, privacy cleanup guide. Especially useful for graduates and early career. | `/social-media-review` |
| **Application Optimiser** | Company and role research, ATS-optimised CV rewriting, cover letters and supporting statements, application strategy | `/application-optimiser` |
| **LinkedIn Coach** | Profile audit, headline optimisation, content strategy, post review, video scripts | `/linkedin-coach` |
| **Interview Master** | Interview prep, mock interviews, interviewer perspective reports, post-interview coaching, reference and referee prep, ageism support (UK law, practical strategies, emotional resilience) | `/interview-master` |
| **Career Navigator** | Networking intelligence, 3-month job search plans, salary negotiation, offer evaluation, application tracker | `/career-navigator` |
| **Career Transitions** | Portfolio and fractional careers, AI readiness assessment, non-linear career exploration (entrepreneurship, startups, public sector, charity, intrapreneurship, multi-role skilling) | `/career-transitions` |
| **AI Impact Assessment** | Researches whether AI will materially disrupt your role in the next 12 months, with a 6-month mitigation plan | `/ai-impact-assessment` |
| **NED AI Helper** | AI governance for Non-Executive Directors, Board Governors, and Charity Trustees. Challenge frameworks, risk assessment, governance structures, regulatory guidance | `/ned-ai-helper` |
| **Personal Brand** | Why You, Why Them, Why Now positioning; audience and channel map; content pillars; bio library across LinkedIn, X, speaker bio, podcast bio, About page, and board bio. Persona guides for NEDs, fractional, and career returners | `/personal-brand` |
| **Career Coach (Tim)** | Guided career coaching, understands your situation, reads emotional signals, runs the right skills in the right order, checks in after difficult work, with accessibility support and persistent agent memory | `/career-helper:career-coach` |

## Commands

| Command | Purpose |
|:--------|:--------|
| `/career-helper:help` | Find the right skill for your situation |
| `/career-helper:quick-start` | Guided entry point - answers questions and routes you |
| `/career-helper:status` | Check your progress and see generated outputs |
| `/career-helper:career-coach` | Start a guided coaching session with Tim |

---

## Typical Workflow

**Prefer guided support?** Run `/career-helper:career-coach` and Tim will handle the sequencing for you, checking in between each step.

**Or run skills yourself:**

```
0. Audit your digital footprint   /employer-footprint
1. Research the company           /application-optimiser
2. Optimise your CV               /application-optimiser
3. Write your cover letter        /application-optimiser
4. Sync your LinkedIn             /linkedin-coach
5. Track every application        /career-navigator
6. Prepare for interviews         /interview-master
7. Practice with mock interview   /interview-master
8. Prepare your references        /interview-master
9. Negotiate your offer           /career-navigator
10. Evaluate competing offers     /career-navigator
```

**Tip:** Inside Claude Cowork, run `/getting-started` and ask about scheduled routines to set up a weekly job-search standup, market monitor, and follow-up check that keep the search moving.

---

## Features

- **Works on all Claude plans** including free subscriptions
- **UK English** throughout (adapts to US when the role requires)
- **Region-aware** guidance for UK, US, EU, and APAC markets
- **Research-driven** with cited sources and access dates
- **ATS-optimised** CV output with keyword coverage analysis
- **Cover letters and supporting statements** with the same anti-hallucination guardrails as CV work
- **Application tracker** a single plain-text board of every live application, owned by you and read by `/career-helper:status`
- **Reference and referee prep** choosing, asking, and briefing referees, with UK conventions and regulated-role notes
- **Scheduled routines for Claude Cowork** ready-made `/schedule` prompts for a weekly standup, market monitor, and follow-up check
- **Career stage adaptation** from graduates to late career
- **Wellbeing-aware coaching** Tim reads emotional signals, acknowledges difficulty before routing, checks in after heavy work, and carries wellbeing context across sessions
- **Ageism support** UK law, practical strategies, and emotional resilience for age-related rejection
- **Template-driven** consistent, professional outputs
- **Digital footprint audit** credit-report style employer impression dashboard
- **Non-linear career exploration** entrepreneurship, startups, public sector, charity, intrapreneurship, and multi-role skilling with honest pros/cons and decision frameworks
- **Guided coaching** Tim orchestrates skills based on your situation with structured checkpoints and persistent agent memory that improves routing over time
- **Accessibility across all skills** dyslexia-friendly enhanced mode with signposting, numbered options, and plain language; colour-blind safe output with text labels instead of colour coding. Preferences stored in `career-helper-preferences.md` and respected by every skill, command, and Tim

---

## Output Files

Skills generate markdown files you can convert to other formats:

| Output | Generated By |
|:-------|:-------------|
| `{role}-research-brief.md` | Application Optimiser |
| `{role}-cv-optimized.md` | Application Optimiser |
| `{role}-cover-letter.md` | Application Optimiser |
| `{role}-supporting-statement.md` | Application Optimiser |
| `{role}-application-strategy.md` | Application Optimiser |
| `{role}-linkedin-profile-review.md` | LinkedIn Coach |
| `{role}-content-strategy.md` | LinkedIn Coach |
| `{role}-content-calendar.md` | LinkedIn Coach |
| `{role}-interview-prep.md` | Interview Master |
| `{role}-interviewer-perspective.md` | Interview Master |
| `{role}-post-interview-debrief.md` | Interview Master |
| `{role}-referee-prep.md` | Interview Master |
| `{role}-networking-intelligence.md` | Career Navigator |
| `three-month-plan.md` | Career Navigator |
| `{role}-negotiation-strategy.md` | Career Navigator |
| `offer-evaluation.md` | Career Navigator |
| `applications/tracker.md` | Career Navigator |
| `portfolio-career-strategy.md` | Career Transitions |
| `ai-readiness-plan.md` | Career Transitions |
| `non-linear-career-exploration.md` | Career Transitions |
| `{role}-ai-impact-assessment.md` | AI Impact Assessment |
| `{topic}-challenge-questions.md` | NED AI Helper |
| `{topic}-risk-register-entry.md` | NED AI Helper |
| `{topic}-governance-options.md` | NED AI Helper |
| `{topic}-change-readiness-report.md` | NED AI Helper |
| `{topic}-hitl-assessment.md` | NED AI Helper |
| `{name}-footprint-dashboard.md` | Employer Footprint |
| `{name}-{company}-employer-impression.md` | Employer Footprint |
| `{name}-social-media-audit.md` | Employer Footprint |
| `{name}-footprint-interview-questions.md` | Employer Footprint |
| `{name}-social-media-review.md` | Social Media Review |
| `{name}-social-cleanup-guide.md` | Social Media Review |
| `personal-brand-foundation.md` | Personal Brand |
| `personal-brand-audience-channels.md` | Personal Brand |
| `personal-brand-content-plan.md` | Personal Brand |
| `personal-brand-bio-library.md` | Personal Brand |
| `personal-brand-refresh-plan.md` | Personal Brand |
| `career-helper-preferences.md` | Tim (Career Coach) |

---

## Workspace Tip

For the best experience, always use the same local folder for your career-helper sessions. This lets you build on previous analyses and track progress across sessions:

```bash
mkdir -p ~/career-helper-workspace
cd ~/career-helper-workspace
```

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full version history.

---

## Contributing

Found a bug, have a suggestion, or want to improve something? We welcome contributions and feedback.

- **Report issues** - [Open an issue](https://github.com/Zal4DW/career-helper/issues) for bugs, feature requests, or suggestions
- **Start a discussion** - [Join discussions](https://github.com/Zal4DW/career-helper/discussions) to share your experience or ask questions
- **Share your success** - Landed a role using Career Helper? We'd love to hear about it
- **Spread the word** - Tell others who might benefit from this plugin

---

## License

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

See [LICENSE](LICENSE) for full terms.

---

*Career Helper Plugin v1.12.0 | Prosper AI Consulting, UK*
