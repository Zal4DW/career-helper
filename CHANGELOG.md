# Changelog

All notable changes to Career Helper are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow [Semantic Versioning](https://semver.org/).

---

## [1.5.1] - 2026-02-28

### Added
- **Ageism in employment support** for Interview Master skill (post-interview coaching & all capabilities)
  - New reference: `ageism-in-employment.md` — comprehensive UK law (Equality Act 2010), Employment Tribunal process, burden of proof, time limits, compensation, whistleblowing routes, EHRC role, recent case law (2024-2025), and honest assessment of practical reality vs. letter of the law
  - New reference: `age-discrimination-strategies.md` — practical CV strategies to reduce age bias, interview tactics for "overqualified" concerns, digital presence optimisation, skills to update (with free/affordable UK training resources), age-friendly employers and job boards, networking strategies for older workers
  - New reference: `emotional-support-resilience.md` — psychological impact of age-related rejection, long-service identity crisis (20-30 years at one company), NHS and charity support services with helpline numbers, cognitive reframing techniques (3 C's Framework), daily routine templates, confidence rebuilding, crisis contacts, and when to seek professional help
- New ageism persona in Interview Master — triggered when user mentions age discrimination, being "too old", "overqualified" as age proxy, long-service redundancy, or age-related rejection patterns. Loads all three ageism references alongside standard capability references
- Ageism routing in help command (5 new routing entries)
- Ageism routing in quick-start command (new situation option + follow-up question + 3 routing entries)
- Quick start examples for ageism in Interview Master skill

### Changed
- Plugin version bumped to 1.5.1
- Interview Master skill description updated to include ageism and age discrimination triggers
- Interview Master tags updated to include ageism, age-discrimination, overqualified
- Interview Master career stage adaptation updated with ageism support references
- Updated all commands (help, quick-start) with ageism routing

---

## [1.5.0] - 2026-02-27

### Added
- **New skill: `/social-media-review`** - Lightweight social media check through a recruiter's eyes
  - 3 capabilities: Quick Social Scan, Platform Deep-Dive, Privacy & Cleanup Guide
  - Designed for graduates, early career, and anyone wanting a fast health check
  - GREEN/AMBER/RED flagging system with "3-second recruiter test"
  - Graduate-specific guidance that normalises having a social life
  - Quick wins list (5 things fixable in 10 minutes)
  - Platform-specific privacy settings walkthrough
  - Clear upgrade path to `/employer-footprint` for full scored dashboard
- Cross-linking between `/employer-footprint` and `/social-media-review` with comparison table
- Social Media Review tips in getting-started skill-tips reference
- Routing for `/social-media-review` in help, quick-start, and status commands
- Output file patterns `*-social-media-review.md` and `*-social-cleanup-guide.md` in status tracking

### Changed
- Plugin version bumped to 1.5.0 (9 skills)
- Updated all commands (help, quick-start, status) with social-media-review routing
- Updated getting-started references (full-overview, skill-tips, SKILL.md)
- Updated README with new skill in skills table, output files, and description

---

## [1.4.0] - 2026-02-27

### Added
- **New skill: `/employer-footprint`** - Digital footprint analysis through an employer's eyes
  - 4 capabilities: Full Footprint Analysis, Social Media Audit, Employer Impression Report, Interview Questions from Footprint
  - Agentic deep-research swarm architecture with 8 parallel research agents
  - Credit-report style dashboard with 8 scored dimensions (1-10 scale, traffic-light indicators)
  - Channels audited: Google, LinkedIn, Twitter/X, GitHub, Facebook, Instagram, Medium, YouTube, Stack Overflow, personal websites, news/media
  - CV-to-online-presence consistency checking
  - Company culture alignment mapping when target employer provided
  - Generates likely interview questions from publicly visible content
  - Recommends next career-helper skills based on findings
  - 5 reference files: digital-footprint-audit, footprint-dashboard-template, social-media-audit, employer-impression-analysis, interview-questions-from-footprint, deep-research-reflection
- Workspace persistence tip added across getting-started overview and README
- Footprint-first workflow pattern added to workflow-planner (Pattern A Step 0, Pattern C Step 0)
- Employer Footprint tips section added to skill-tips reference
- Footprint-First Approach added as Strategy 7 in power-user-strategies
- Digital footprint preparation checklist added to preparation-checklist reference
- Output file patterns for footprint dashboard, employer impression, social media audit, footprint interview questions in status tracking

### Changed
- Plugin version bumped to 1.4.0 (8 skills)
- Updated all commands (help, quick-start, status) with employer-footprint routing
- Updated all getting-started references with new skill examples and integration
- Updated skills workflow diagram to show footprint audit as entry point
- Renumbered power-user strategies (Output Maintenance became Strategy 8)

---

## [1.3.0] - 2026-02-14

### Added
- **New skill: `/ned-ai-helper`** - AI governance for Non-Executive Directors, Board Governors, and Charity Trustees
  - 5 capabilities: Challenge an AI Proposal, Risk Assessment, Governance Structure Design, Change Readiness Assessment, Human-in-the-Loop Assessment
  - 14 persona templates covering different board and trustee roles
  - Deep research methodology for AI governance topics
  - UK regulatory focus (AI Safety Institute, ICO, FCA) with international awareness
- Getting-started skill with 5 capabilities: Full Overview, Preparation Checklist, Workflow Planner, Skill-by-Skill Tips, Power User Strategies
  - Career-level awareness across all stages (graduate to late career)
  - 6 workflow patterns for different situations
  - 7 power user strategies

### Changed
- Plugin version bumped to 1.3.0 (7 skills)
- All skill names renamed to UK spelling (optimiser, not optimizer)
- Updated all commands and routing for new skills

---

## [1.2.0] - 2026-01-20

### Changed
- Updated install instructions for Claude co-worker format
- Plugin version bumped to 1.2.0

---

## [1.1.0] - 2025-12-15

### Added
- LinkedIn Coach: copy/paste and screenshot alternatives for profile access (LinkedIn blocks WebFetch)

### Fixed
- Replaced direct LinkedIn URL fetch requests with human-in-the-loop fallbacks

---

## [1.0.0] - 2025-12-01

### Added
- **Initial marketplace release** with 5 focused skills:
  - `/application-optimiser` - Company research, ATS CV rewriting, application strategy
  - `/linkedin-coach` - Profile audit, headline optimisation, content strategy, post review, video scripts
  - `/interview-master` - Interview prep, mock interviews, interviewer perspective reports, post-interview coaching
  - `/career-navigator` - Networking intelligence, 3-month plans, salary negotiation, offer evaluation
  - `/career-transitions` - Portfolio and fractional careers, AI readiness assessment
- 3 commands: `/career-helper:help`, `/career-helper:quick-start`, `/career-helper:status`
- Region-aware guidance (UK, US, EU, APAC)
- Career stage adaptation (graduate to late career)
- Deep research validation workflow
- Template-driven outputs with citation requirements

---

## Pre-1.0 History

| Version | Date | Summary |
|:--------|:-----|:--------|
| 0.4.0 | 2025-11 | LinkedIn headline optimisation |
| 0.3.0 | 2025-11 | Post-interview coaching capability |
| 0.2.0 | 2025-10 | Interviewer's perspective reports, deep research validation |
| 0.1.0 | 2025-10 | Initial commit - Career Helper skill |

---

*Career Helper Plugin | Prosper AI Consulting, UK*
