# Changelog

All notable changes to Career Helper are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow [Semantic Versioning](https://semver.org/).

---

## [1.15.0] - 2026-07-10

### Added
- **Job Scout skill** (`/job-scout`). Live role discovery across job boards, aggregators, ATS-hosted postings, and employer careers pages, followed by five-dimension batch ranking (skills fit, level fit, practical fit, organisation signals, and winnability) with deal-breaker vetting, deadline flagging, and text-label tiers (Apply first, Apply, Park, Discard). The skill is deliberately honest that automated job-board search is fragile: it states coverage limits after every run, recommends saved alerts as the backbone of discovery, and offers the Claude for Chrome extension for logged-in boards such as LinkedIn and Indeed rather than attempting to circumvent access blocks. Chosen roles feed `applications/tracker.md` at stage Researching. New references `role-discovery.md`, `batch-ranking.md`, and `shortlist-template.md`. Output: `applications/shortlist.md`.
- **Skills Radar skill** (`/skills-radar`). Builds an evidenced skills inventory in three layers (stated, implicit, and transferable), including consent-based mining of the user's own public work (GitHub, portfolio, publications, talks, volunteering) to surface skills the CV undersells. Gap analysis against a specific posting or a researched role type separates evidence gaps (present but unprovable) from skill gaps (genuinely missing), prioritised with a text-label matrix and cross-read against the learnings loop patterns file. Learning plans cover three gaps at most, pair every course with an evidence-building artefact, and are built around the user's honestly stated weekly hours. New references `skill-enrichment.md` and `gap-analysis.md`, plus `skills-inventory-template.md` and `learning-plan-template.md`. Outputs: `skills-inventory.md`, `skills-gap-analysis.md`, and `learning-plan.md`.
- **Kanban Board View** capability in `/career-navigator` (Capability 7). Generates a fully self-contained, interactive HTML board from `applications/tracker.md`: one card per application across the six tracker stages, drag-and-drop plus keyboard-operable moves, an edit dialog, a text `OVERDUE` tag, and light and dark theme support. Export buttons produce complete tracker markdown (copy or download) so board changes flow back into the tracker, which remains the source of truth. No external assets or network calls; board edits persist in the browser only. New reference `kanban-board.md` and template `kanban-board-template.html`. Output: `applications/board.html`.
- **CV PDF Production** capability in `/application-optimiser` (Capability 5). A generate-verify loop that renders `cv-optimised.md` (or a cover letter) to a deliberately plain, single-column, ATS-safe PDF, then proves it survived: `scripts/generate_cv_pdf.py` (three themes: standard, compact, relaxed; HTML fallback when WeasyPrint is unavailable) and `scripts/verify_cv_pdf.py` (ATS text-layer extraction with missing-content detection, page-limit flagging, and per-page PNG rendering for visual inspection of orphaned headings, overflow, and spacing). Verification applies whatever produced the PDF, including native rendering in Claude Cowork. Scripts adapted from the ODTA pdf-toolkit reference implementation. New reference `cv-pdf-production.md`. Outputs: `applications/{role-slug}/cv.pdf` and `cover-letter.pdf`.

### Changed
- Plugin and marketplace version bumped to 1.15.0, with descriptions updated for the two new skills (fourteen in total) and the new capabilities
- `/career-navigator` capabilities table, quick-start examples, frontmatter triggers, and version footer updated for the kanban board view (skill v1.6.0); the application tracker reference now documents the board as a regenerable view
- `/application-optimiser` capabilities table, quick-start examples, frontmatter triggers, and version footer updated for CV PDF production (skill v1.5.0)
- `/career-helper:status` now offers the board view once when three or more applications are active, and offers to regenerate a stale board
- `/career-helper:help` and `/career-helper:quick-start` route to the new skills and capabilities
- Tim career coach agent and skill now list 13 orchestratable skills, with routing judgements for an empty pipeline (job-scout), recurring "you lack X" feedback (skills-radar), and a pipeline the user is losing track of (kanban board)
- Tim skill routing guide updated: cross-skill dependency map, output-file patterns, and three new routing scenarios (14 to 16)
- Getting-started guides updated for thirteen skills: the shareable `getting-the-best-guide.md` (and regenerated PDF), `full-overview.md` (two new skill sections with examples), and `skill-tips.md` (tips for both new skills)
- README skills table, features, description, and output-files table updated

### House style
- All new content adheres to the house style: no em dashes, UK English throughout, Oxford comma, hyphenated compound modifiers, no emojis, no hyperbole, second-person coaching voice. Templates use `{{PLACEHOLDER}}` syntax and carry no real personal data. The kanban board and shortlist use text labels, never colour alone.

### Credits
- Feature direction informed by a gap analysis against [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search), whose scrape, rank, expand, upskill, and PDF-verification workflow highlighted the gaps this release closes, reinterpreted for Career Helper's coaching-led, evidence-first approach.

---

## [1.14.0] - 2026-06-15

### Added
- **Application Learnings Loop** capability in `/career-navigator` (Capability 6). Turns each interview, rejection, and win into a short, structured note, then periodically synthesises those notes into one patterns file so the user can see what is actually working across a long search rather than relearning the same lesson each time. Three per-event templates (interview debrief, rejection analysis, win log) and one synthesis template feed a single `applications/learnings/patterns.md`. Notes are stored per role under `applications/learnings/interview-notes/`, `rejections/`, and `wins/`. The capability records only what the user confirms or what existing files show, keeps the user's honest read on a rejection separate from what was actually said, never invents a reason, and surfaces one useful pattern at a time. It feeds `/interview-master` (recurring objections) and `/application-optimiser` (gaps the CV undersells). New references `career-helper/skills/career-navigator/references/learnings-loop.md`, `interview-debrief-template.md`, `rejection-analysis-template.md`, `win-log-template.md`, and `patterns-synthesis-template.md`.

### Changed
- Plugin and marketplace version bumped to 1.14.0
- `/career-navigator` capabilities table, quick-start examples, and version footer updated for the learnings loop (skill v1.5.0)
- `/career-helper:status` now checks for `applications/learnings/patterns.md`, surfaces the most useful current pattern after the tracker board, offers to synthesise when per-event notes have accumulated, and suggests the learnings loop as a next step after interviews and rejections
- Tim career coach agent now lists the learnings loop under Career Navigator and carries routing judgements for capturing and synthesising interviews, rejections, and wins
- Tim skill routing guide updated: the cross-skill dependency map, output-file patterns, and the multiple-rejections scenario now cover the learnings loop
- Getting-started help guides updated to document the learnings loop: the shareable `getting-the-best-guide.md` (and regenerated PDF), `full-overview.md`, and `skill-tips.md`

### House style
- All new content adheres to the house style: no em dashes, UK English throughout (including "CV" rather than "resume"), Oxford comma, hyphenated compound modifiers, no emojis, no hyperbole, second-person coaching voice. Templates use `{{PLACEHOLDER}}` syntax and carry no real personal data.

---

## [1.13.0] - 2026-06-02

### Added
- **Optional interactive ikigai map.** After Tim's four direction-finding questions (`/career-helper:career-coach`), Tim can now offer to render the classic four-circle ikigai diagram as a self-contained, interactive HTML page the user can keep and revisit. New references `career-helper/skills/tim/references/tim-ikigai-visual.md` (when to offer, how to populate from the user's own answers, accessibility rules) and `career-helper/skills/tim/references/ikigai-map-template.html` (a single-file template with no external assets). Output: `ikigai-map.html` in the workspace root. The diagram uses a colour-blind-safe palette, labels every region in text, supports hover and keyboard focus, and includes a full text-equivalent table so it is usable without seeing the diagram. Content is populated only from the user's own answers; unknown overlaps keep their `{{PLACEHOLDER}}` rather than being invented.

### Changed
- Plugin and marketplace version bumped to 1.13.0
- `tim-ikigai-guide.md` now offers the visual map as an optional step after summarising the answers
- `/career-helper:status` and Tim's routing output patterns recognise `ikigai-map.html`
- README features list and output file table updated for the ikigai map

### Documentation
- **Shareable guide refreshed and brought up to date** (`career-helper/skills/getting-started/references/getting-the-best-guide.md` and the regenerated `getting-the-best-guide.pdf`):
  - Added the missing `/personal-brand` row to the skills table and corrected the skill count from "ten" to "eleven" (the guide had not been updated when personal-brand shipped in v1.11.0)
  - Added a new "I don't know what I want to do next" scenario covering Tim's ikigai direction-finding and the optional ikigai map
  - Retrofitted the guide to the house style by replacing all em dashes with commas, colons, semicolons, full stops, or parentheses
- **Added a reproducible PDF generator** at `scripts/build-guide-pdf.py` (depends on `markdown` and `weasyprint`, which are not part of the plugin runtime) so the shareable guide PDF can be regenerated from its markdown source and does not drift out of date again

### House style
- All new content adheres to the house style codified in v1.10.1: no em dashes, UK English throughout, Oxford comma, hyphenated compound modifiers, no emojis or emoji-style markers, no hyperbole, second-person coaching voice.

---

## [1.12.0] - 2026-06-02

### Added
- **Cover Letter & Supporting Statement** capability in `/application-optimiser` (Capability 4). Drafts a full cover letter, a competency-based supporting statement (for public sector, charity, NHS, and academia), or a short application message, confirming the required format before drafting. Mirrors job-description language only where the underlying fact genuinely matches, sources motivation from the user rather than inventing it, and addresses overqualification, career change, and gaps where the CV cannot. Runs the existing anti-hallucination guardrails and reflective validation. New references `career-helper/skills/application-optimiser/references/cover-letter.md` and `cover-letter-template.md`. Outputs `applications/{role-slug}/cover-letter.md` or `supporting-statement.md`.
- **Application Tracker** capability in `/career-navigator` (Capability 5). A single, plain-text board of every live application at `applications/tracker.md`, owned by the user and stored locally, as the private alternative to a paid tracking platform. Builds from a scan of existing application folders, then confirms each stage with the user; tracks role, organisation, stage, next action, and next date; uses fixed text-label stages (never colour coding); records only confirmed status; and surfaces one honest observation when the data warrants it (stalled pipeline, overdue actions, thin volume). New references `career-helper/skills/career-navigator/references/application-tracker.md` and `application-tracker-template.md`.
- **Reference & Referee Prep** capability in `/interview-master` (Capability 5). Helps the user choose credible, relevant referees, ask permission well, brief each referee on what the role values and the verified examples they witnessed, and anticipate the questions referees face (including the more formal checks for regulated and safeguarding roles). Handles common constraints: a current employer who cannot be contacted yet, UK factual-only reference policies, a difficult last manager, and first jobs with no prior employer. Referee details come only from the user; briefs match verified shared history. New references `career-helper/skills/interview-master/references/referee-prep.md` and `referee-prep-template.md`. Outputs `applications/{role-slug}/referee-prep.md`.
- **Scheduled Job-Search Routines (Claude Cowork)** capability in `/getting-started` (Capability 7). Ready-made `/schedule` prompts that turn the job search into a living process: a Monday job-search standup that reads the tracker, a weekly market and role monitor, a LinkedIn posting reminder aligned to the content calendar, a weekday follow-up check, and an on-demand pre-interview nudge. States the two honest limitations plainly: the computer must be awake with Claude Desktop open, and scheduling is a Cowork feature rather than part of the plugin (CLI and web users can run the same prompts manually). Each prompt retains a "do not invent" instruction. New reference `career-helper/skills/getting-started/references/scheduled-routines.md`.

### Changed
- Plugin and marketplace version bumped to 1.12.0
- Plugin and marketplace descriptions updated to mention cover letters and supporting statements, the application tracker, reference and referee prep, and Cowork scheduled routines
- `/career-helper:status` now checks for `applications/tracker.md` first and uses it as the spine of the progress summary, falling back to a folder scan when no tracker exists, flagging any tracker that looks out of date against the files on disk, and offering to build a tracker when application folders exist without one. Folder scan list extended with `cover-letter.md`, `supporting-statement.md`, and `referee-prep.md`
- `/career-helper:help` and `/career-helper:quick-start` routing updated to recognise cover letter, supporting statement, application tracking, referee, and "automate my job search" phrasing
- Getting Started reference guides (`full-overview.md`, `skill-tips.md`, `power-user-strategies.md`, `getting-the-best-guide.md`) updated to cover the four new capabilities
- Tim routing (`career-helper/agents/tim.md`, `career-helper/skills/tim/SKILL.md`, and `career-helper/skills/tim/references/tim-skill-routing-guide.md`) updated so Tim can route to the new capabilities and scan for their outputs
- README skills table, output file table, typical workflow, and features list updated; per-skill SKILL.md versions bumped (Application Optimiser 1.4.0, Career Navigator 1.4.0, Interview Master 1.5.0, Getting Started 1.12.0)

### House style
- All new content adheres to the house style codified in v1.10.1: no em dashes, UK English throughout, Oxford comma, hyphenated compound modifiers, no emojis or emoji-style markers, no hyperbole, second-person coaching voice. Existing files were not retrofitted.

---

## [1.11.0] - 2026-04-26

### Added
- **New skill: `/personal-brand`** for personal brand building, structured around the Why You, Why Them, Why Now framework. Five capabilities:
  - Capability A: Brand Foundation. An eleven-question interview producing a positioning statement, one-line elevator, three-word brand summary, and a "permission slip" paragraph the user can defend.
  - Capability B: Audience and Channel Map. Sharp ideal-audience profile, three-tier engagement strategy (industry voices, peers, rising voices), channel matrix matched to where the audience actually is, and a low/medium/high investment weekly rhythm.
  - Capability C: Content Pillars and Cadence. Three to five pillars derived from the foundation, ten topic seeds per pillar, a repurposing cascade (long-form to thread to short post to talk), voice rules, and a first-90-days plan.
  - Capability D: Bio Library. A coherent set of bios at every length the user actually needs (LinkedIn About long/medium/trimmed, LinkedIn headline, X/Twitter bio, speaker bio in three sizes, podcast guest bio, conference proposal bio, About page, email signature line, and board bio).
  - Capability E: Brand Refresh. A diagnostic of current online positioning signals, drift analysis against intended positioning, and a prioritised refresh plan.
- **Personal Brand reference suite** (`career-helper/skills/personal-brand/references/`): `personal-brand-foundation.md`, `audience-channel-map.md`, `content-pillars-from-brand.md`, `bio-library-templates.md`, `brand-from-ikigai.md` (the bridge file mapping ikigai answers onto Why You, Why Them, Why Now), and `personal-brand-output-template.md`.
- **Three persona guides** for the personal-brand skill: `ned-personal-brand-guide.md` (board, NED, governor, and trustee positioning, with adjustments for confidentiality, conflict of interest, and director duties), `fractional-personal-brand-guide.md` (fractional, portfolio, and independent positioning, treating the brand as the inbound funnel), and `career-returner-personal-brand-guide.md` (returner positioning that frames the gap honestly without making it the story, with confidence and wellbeing notes).
- **Tim integration**: personal-brand added as the eleventh specialist skill in both `career-helper/agents/tim.md` and `career-helper/skills/tim/SKILL.md`. Tim now has explicit detection signals for when to route to personal-brand vs ikigai vs linkedin-coach (the "what you stand for vs how to make it findable" distinction), with two new example judgements and a clarifying question to resolve ambiguity.
- **Ikigai-to-brand bridge in Tim's ikigai guide** (`career-helper/skills/tim/references/tim-ikigai-guide.md`): the post-questions routing table now includes routes to personal-brand when a clear topic plus audience emerges, with the `brand-from-ikigai.md` bridge so the four ikigai answers feed Why You, Why Them, Why Now directly rather than starting again.
- **Routing guide additions** (`career-helper/skills/tim/references/tim-skill-routing-guide.md`): cross-skill dependency entries for ikigai-to-brand, brand-to-LinkedIn, brand-to-career-navigator, brand-to-career-transitions (structural decision must precede the brand layer), and brand-to-employer-footprint. New brand-building persona row in the persona-trigger table. Two new common routing scenarios: "Brand vs LinkedIn vs ikigai confusion" with a clarifying question, and "Fractional pivot needing both structure and brand" with the order rule.
- **Help command routing** (`career-helper/commands/help.md`): personal-brand row in the skills table and ten new routing entries covering the trigger phrases (build my brand, position myself as X, find my niche, find my voice, be known for X, thought leadership, refresh my bio, fractional inbound, NED visibility, online presence drift).
- **Output file patterns** for personal-brand added to README and to Tim's routing guide so Tim can scan for existing brand outputs before re-running capabilities.

### Changed
- Plugin and marketplace version bumped to 1.11.0
- Plugin and marketplace descriptions updated to mention personal brand building as the headline new capability (twelve skills total)
- README skills table and output file table updated with the new skill and its five output filenames
- Tim's "Skills Tim Can Run" and "Skills Tim Can Orchestrate" tables expanded from 10 rows to 11 with detection guidance for the new skill
- Tim's "Common Routing Scenarios" count updated from "10 gaps" (which had drifted to 11 in v1.9.0 without the count being updated) to a generic "gaps" framing, with two new scenarios appended

### House style
- All new content adheres to the house style codified in v1.10.1: no em dashes, UK English throughout, Oxford comma, hyphenated compound modifiers, no emojis or emoji-style markers, no hyperbole, second-person coaching voice. Existing files were not retrofitted.

---

## [1.10.4] - 2026-04-15

### Added
- **Non-commercial use clarification** added to `LICENSE`. CC BY-NC 4.0 already permitted non-profit, public sector, charitable, and personal use, but a community question from an unemployed job seeker asking whether they could build a local-model interface (Ollama, Llama, or Qwen) around Career Helper and offer it to a national public employment service made it clear that the licence text was not explicit enough. The new section leads with the spirit of the licence (open reuse, sharing, commenting, and paying it forwards with warmth and kindness, as long as the work is not used for commercial gain), then unpacks five welcomed use cases (personal use including local-model wrappers, public employment services, charities and community groups, schools and universities, and mutual aid or volunteer coaches) and four uses that still require a commercial arrangement (paid recruitment and outplacement, paid external consultancies even when the paying party is a public body, commercial repackaging, and commercial model training).
- **Commercial licensing route** in `LICENSE`. Commercial users are asked to open a GitHub issue or discussion rather than walk away. Proceeds from any commercial licensing arrangement will be donated to an appropriate charity supporting job seekers and people facing barriers to employment.
- **"Forks and derivatives" guidance** in `LICENSE` covering licence retention, upstream attribution, telling end users the upstream project exists, and contributing improvements back.

### Changed
- Plugin and marketplace version bumped to 1.10.4

---

## [1.10.3] - 2026-04-13

### Fixed
- ATS-Helper Output Format Contract now reflects the conditional flow introduced in v1.10.2. Previously the contract unconditionally required `<Step_1_Output>` through `<Step_9_Output>`, which contradicted the Step 1 gate that halts on Poor/Questionable fit. The contract now specifies two stages: a full run emits all nine tags; a halted run emits only `<Step_1_Output>` plus the `PAUSE_FOR_CONFIRMATION` marker, and the remaining tags are emitted only after explicit user confirmation (CodeRabbit flag on PR #24).
- ATS-Helper "no tables" rule on line 3 was a global prohibition that conflicted with Step 3 analysis, which explicitly requires a table. The rule is now scoped to the CV deliverable in Step 9, while analysis steps may use tables for clarity (CodeRabbit flag on PR #24).
- CHANGELOG v1.10.0 entries for "Verified content guardrails" and "Master facts template" now use the full repo-relative paths (`career-helper/skills/application-optimiser/references/...`) rather than the shortened form, so links are navigable from the repo root (CodeRabbit flag on PR #24).

### Changed
- Plugin and marketplace version bumped to 1.10.3

---

## [1.10.2] - 2026-04-13

### Fixed
- ATS-Helper Execution Plan no longer contradicts itself. Previously the plan declared nine sequential outputs with no skipping, yet the Step 1 instructions required pausing for user confirmation before Step 2 on a Poor/Questionable fit. The plan is now an explicit conditional multi-stage flow: Strong/Moderate fits run Steps 1 to 9 straight through, Poor/Questionable fits halt after Step 1, emit a literal `PAUSE_FOR_CONFIRMATION` marker, and only resume on explicit user confirmation. Chosen for user experience: a user who is told the role is a poor fit should not have to scroll past a full rewrite they never asked for (CodeRabbit flag on PR #24).

### Changed
- Plugin and marketplace version bumped to 1.10.2

---

## [1.10.1] - 2026-04-13

### Added
- **`.claude/CLAUDE.md`** project instructions file codifying the house style for AI assistants working in this repo: no em dashes, no emojis, UK English, Oxford comma, hyphenated compound modifiers, second-person coaching voice, content integrity rules, file organisation conventions, and versioning policy.

### Changed
- Plugin and marketplace version bumped to 1.10.1
- All em dashes removed from new content introduced in v1.10.0 (`verified-content-guardrails.md`, `master-facts-template.md`, ATS-Helper additions, career-navigator Coaching Voice section, Tim master-facts section, reflect-validate additions, CHANGELOG 1.10.0 entry). Replaced with colons, semicolons, commas, or full stops as appropriate to the surrounding clause.

### Fixed
- ATS-Helper heading "Content Verification" no longer uses an em dash (CodeRabbit flag on PR #24)
- ATS-Helper "3 to 5 line summary" now correctly hyphenated as "3- to 5-line summary" (CodeRabbit flag on PR #24)
- Coverage threshold conflict between ATS-Helper (90%) and reflect-validate (70%) resolved by explicitly documenting the two as distinct gates: 90% is the aspirational target, 70% is the minimum acceptance gate. Cross-referenced in both files (CodeRabbit flag on PR #24)

---

## [1.10.0] - 2026-04-13

### Added
- **Verified content guardrails** (`career-helper/skills/application-optimiser/references/verified-content-guardrails.md`): non-negotiable anti-hallucination rules for CV rewriting, including a trigger-phrase STOP list, a decision tree for source verification, safe-vs-unsafe optimisation examples, and a hallucination red-flag self-review checklist. Every substantive word in a delivered CV must now trace to a verified source.
- **Master facts template** (`career-helper/skills/application-optimiser/references/master-facts-template.md`): optional single-source-of-truth file users can maintain once and reuse across every application. Covers verified timeline, metrics bank, and bullet library organised by emphasis area. When present in cwd, application-optimiser prefers it over any other source.
- **9-step job-analysis flow in ATS-Helper**: refactored the execution plan from 3 steps (keyword extraction, CV rewrite, LinkedIn sync) to 9 steps: Career Fit Assessment, Content Strategy, Resume-Job Alignment, Keyword and Concept Extraction, Recruiter Perspective, Enhancement Recommendations, Gap Analysis, Read Between the Lines, and finally the optimised CV rewrite plus LinkedIn reconciliation.
- **Coaching Voice section in career-navigator**: direct market-reality feedback, flight-risk check, overthinking-versus-applying heuristic, optimistic-role-analysis versus strategic-career-advice distinction, and cross-session consistency rules. Codifies the balance between warmth and directness that career coaching actually needs.
- **Master facts awareness in Tim**: before dispatching application-optimiser for CV work, Tim now checks for `master-facts.md` in the current working directory and passes the path to the sub-agent as the authoritative source of truth. For first-time users, Tim mentions the master-facts template as an optional one-time setup.
- **Traceability and hallucination red-flag scan in reflect-validate**: CV validation now runs a source traceability check before keyword coverage, and a red-flag scan for unverified adjectives, team composition, geography, reporting structure, and timing details before delivery.
- **CONTRIBUTORS.md**: manual contributor acknowledgement log at repo root, crediting community contributions by name with contribution summaries.
- **CONTRIBUTING.md** (`.github/CONTRIBUTING.md`): contribution guide covering what belongs in the repo, PR process, house style (UK English, no em dashes, no emojis, Oxford comma), skill content conventions, and versioning rules.

### Changed
- Plugin version bumped to 1.10.0
- Marketplace manifest bumped to 1.10.0
- `ATS-Helper.md` operating rules now require preferring the master facts file when present and explicitly reference the verified-content-guardrails

### Community
- Thank you to **@enigmaicon-eng** for PR #22, which prompted the verified-content-guardrails, master-facts-template, 9-step flow, coaching-voice, and Tim master-facts awareness changes. The original contribution file was not a structural fit for the plugin, but the substantive value has been extracted, translated to UK English, aligned with house style, and integrated into the existing skill architecture. Full details in [CONTRIBUTORS.md](CONTRIBUTORS.md).

---

## [1.9.0] - 2026-03-21

### Added
- **Wellbeing and emotional awareness in Tim's coaching** — Tim now reads emotional signals during intake, acknowledges difficulty before routing to skills, and checks in after emotionally demanding work
  - Intake Q2 branches based on emotional context: forced change gets "how are you feeling?", steady situations get "what would help most?"
  - Wellbeing Notes in preferences file carry emotional context across sessions
  - CHECK-IN line in checkpoints after skills that touch rejection, ageism, redundancy, or difficult feelings
  - Pace line in Progress Tracker after emotionally demanding sessions
  - Skill dispatch now passes emotional context to sub-agents so they can calibrate tone
- **Agent memory for Tim** (`memory: project`) — Tim now builds persistent coaching knowledge across sessions
  - Stores routing patterns, skill sequencing insights, and coaching approaches that work
  - Separate from user data (which stays in preferences file)
- **Interview Master: peer development questions** — explicit "How have you helped your colleagues improve?" question type with STAR guidance focused on the other person's outcome
- **Interview Master: company selection criteria** — "What matters most when choosing your next company?" with values-alignment answer framework
- **Wellbeing-aware checkpoint template** (Variation D) with CHECK-IN rules and concrete example

### Changed
- **Accessibility: traffic-light terminology replaced** — all references to "traffic-light indicators" changed to "text-label ratings (GREEN/AMBER/RED)" across employer-footprint SKILL.md, dashboard template, digital-footprint-audit, deep-research-reflection, and getting-the-best guide
- Dashboard template score key now includes accessibility note: "Ratings always use text labels alongside scores — never colour alone"
- Tim's "What Tim never does" lists deduplicated — Persona section covers voice/tone, Wellbeing section covers coaching boundaries, with cross-reference
- Sequencing Logic updated to require emotional acknowledgment before routing
- Returning user instructions broken into readable sub-bullets
- Mock interview hiring manager typical questions expanded with peer development and company selection criteria
- Plugin version bumped to 1.9.0

---

## [1.8.3] - 2026-03-17

### Added
- **Accessibility support across all skills and commands** — previously only Tim checked for accessibility preferences; now every skill and command does
  - All 10 non-Tim skills check for `career-helper-preferences.md` at skill start and apply dyslexia-friendly and colour-blind safe formatting
  - Skills invoked directly (not via Tim) ask once about accessibility preferences if no preferences file exists, then save for future sessions
  - `/career-helper:quick-start` includes accessibility as part of its intake questions
  - `/career-helper:status` respects accessibility preferences in its output formatting
  - Skill-specific accessibility guidance: risk matrices, dashboards, and status indicators always use text labels, never colour alone

### Changed
- README updated to reflect accessibility coverage across all skills
- Plugin version bumped to 1.8.3

---

## [1.8.0] - 2026-03-16

### Added
- **Tim — Career Coach** (`/career-helper:career-coach`) - Guided career coaching that orchestrates skills for you
  - Semi-autonomous skill orchestration — Tim understands your situation and runs the right skills in the right order
  - Structured checkpoints between skills using labelled DONE/SAVED/FLAG/NEXT format
  - Non-deterministic sequencing — adapts based on your goals, urgency, flags, and emotional signals
  - Session persistence via `career-helper-preferences.md` with consent-gated storage
  - Accessibility support: dyslexia-friendly enhanced mode (signposting, numbered options, confirmation checks, no idioms, one decision per message)
  - Colour-blind safe communication — all status conveyed through labels and words, never colour alone
  - Returning user detection with privacy-safe identity confirmation before displaying personal data
  - Error handling for skill failures with clear reporting and user choice
  - Supportive coach persona — warm, encouraging, direct, never sycophantic
- New command: `/career-helper:career-coach` to launch Tim
- New skill: `tim` with 3 reference files (routing guide, dyslexia guide, checkpoint templates)

### Changed
- `/career-helper:help` updated with Tim in skill table and routing
- `/career-helper:quick-start` mentions Tim as guided alternative at handoff
- Plugin description updated to mention guided coaching
- Plugin version bumped to 1.8.0 (11 skills including Tim)

---

## [1.7.0] - 2026-03-03

### Added
- **Non-Linear Career Explorer** - New capability (Capability 3) in Career Transitions skill
  - Comprehensive exploration of alternatives to traditional career progression
  - **Entrepreneurship:** Business readiness assessment, honest pros/cons, legal structures by region (UK/US), funding sources, financial modelling, failure rate data
  - **Startup founding:** VC vs bootstrapping comparison, funding paths (pre-seed to Series B+), co-founder dynamics, accelerator guidance, realistic success/failure rates (90% failure rate cited), equity and dilution considerations
  - **Public sector careers:** Private-to-public transition guide, Success Profiles framework, Civil Service values, salary/benefits comparison, transferable skills mapping, application tips
  - **Charity and non-profit:** Career paths (management, fundraising, programme delivery, policy, social enterprise, impact investing, grant making), "passion tax" reality, sector resources
  - **Intrapreneurship:** Organisational readiness assessment, internal venture pitching framework, pros/cons vs external entrepreneurship
  - **Multi-role skilling:** Skill stacking strategy, unique intersection identification, deliberate career episode design, hybrid career models
  - Financial readiness assessment with regional guidance
  - Transferable skills audit with meta-skills identification
  - Weighted decision matrix with reversibility assessment
  - Career narrative development (30-second, 2-minute, LinkedIn, and interview versions)
  - Research-driven with WebSearch for current data on success rates, salary benchmarks, and sector insights
- New reference: `non-linear-careers.md` - Comprehensive prompt reference covering all non-linear paths with assessment frameworks
- New reference: `non-linear-careers-template.md` - Structured output template for exploration results
- New reference: `alternative-career-paths-research.md` - Compiled research data on non-linear career paths, entrepreneurship, startups, public sector, charity, portfolio careers, career pivots, and intrapreneurship
- Non-linear career stage guidance in career-stage-context.md (Early Career through Late Career)
- Non-linear goal examples in three-month-plan.md (business validation, Civil Service applications, charity trustee positions, consulting launch, intrapreneurship, skill stacking)
- Non-linear Plan B options in three-month-plan-template.md
- New workflow pattern (Pattern D2: Non-Linear Career Exploration) in workflow-planner.md
- New power user scenarios: Non-Linear Career Pivot and Entrepreneurship Validation in power-user-strategies.md
- Non-Linear Career Exploration preparation checklist in preparation-checklist.md
- 8 new routing entries in help command for non-linear career queries
- 5 new routing entries in quick-start command for non-linear alternatives
- Non-linear career exploration output tracking in status command
- Career Transitions examples (non-linear exploration, public sector transition) in full-overview.md

### Changed
- Career Transitions skill expanded from 2 to 3 capabilities
- Career Transitions description updated with non-linear career triggers and tags (entrepreneurship, startup, founder, business, public-sector, charity, non-profit, non-linear, intrapreneurship, career-pivot)
- Career Transitions quick-start examples expanded with 8 new example prompts
- Career Navigator three-month-plan.md updated with guidance to consider non-linear options and proactively suggest /career-transitions when users seem stuck or questioning traditional employment
- Skill tips updated with Non-Linear Career Explorer tips, common mistakes, and iteration strategy
- Plugin version bumped to 1.7.0
- Updated all commands (help, quick-start, status) with non-linear career routing
- Updated all getting-started references (full-overview, skill-tips, workflow-planner, power-user-strategies, preparation-checklist, SKILL.md)
- README updated with non-linear career features, output files, and examples
- Marketplace description updated with non-linear career exploration

---

## [1.6.0] - 2026-03-03

### Added
- **New skill: `/ai-impact-assessment`** - AI impact analysis for career planning
  - Phase 1 research reference for understanding AI disruption across industries
  - Phase 2 assessment and action plan reference for personalised AI readiness
  - Output template for structured AI impact reports
- **New reference: "Getting the Best from Career Helper"** guide in getting-started skill
  - Comprehensive guide to maximising value from all 10 skills
  - Tips, workflows, and strategies for effective use
- AI Impact Assessment integrated into help, quick-start, overview, and plugin manifest routing

### Changed
- Plugin version bumped to 1.6.0 (10 skills)
- Updated all getting-started references with AI Impact Assessment integration

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
