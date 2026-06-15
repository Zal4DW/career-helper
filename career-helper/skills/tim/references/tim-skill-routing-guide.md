# Tim Skill Routing Guide

This file is loaded by the Tim career coach skill when making routing decisions. It describes how the 11 skills relate to each other, what output files to expect, and how to handle common scenarios.

---

## 1. Cross-Skill Dependency Map

Skills produce outputs that feed into other skills. Tim checks for existing outputs before deciding what to run next.

- application-optimiser research brief feeds into: interview-master (company knowledge for prep), linkedin-coach (CV/LinkedIn consistency), application-optimiser cover letter (what is true about the organisation)
- application-optimiser cover letter and supporting statement draw on: the research brief, the optimised CV or master facts, and the user's stated motivation; never invent motivation
- interview-master referee prep draws on: the optimised CV and interview-prep STAR stories (verified examples the referee witnessed); runs at late interview or offer stage
- career-navigator application tracker indexes: every per-application folder; it is the spine `/career-helper:status` reads, so update it when an application moves stage
- career-navigator application learnings loop draws on: completed interviews, rejections, and wins, captured as per-event notes; the synthesised `applications/learnings/patterns.md` feeds interview-master (recurring objections to drill) and application-optimiser (a gap the CV consistently undersells), and is read by `/career-helper:status` when it exists
- employer-footprint results feed into: linkedin-coach (fix issues found), interview-master (questions from online presence)
- social-media-review results feed into: linkedin-coach (cleanup recommendations), employer-footprint (if deeper audit needed)
- career-transitions outputs feed into: application-optimiser (reposition CV for sector pivot), linkedin-coach (rebrand for fractional/portfolio), career-navigator (3-month plan for new path)
- interview-master post-debrief feeds into: application-optimiser (refine CV after rejection)
- ai-impact-assessment findings feed into: career-transitions (consider non-linear pivot if role at risk)
- career-navigator networking intelligence feeds into: interview-master (who you'll meet), application-optimiser (insider context)
- linkedin-coach updates feed into: application-optimiser (keep CV/LinkedIn consistent)
- ikigai answers (captured in conversation or in `career-helper-preferences.md`) feed into: personal-brand (the four answers map onto Why You, Why Them, Why Now via the `brand-from-ikigai.md` bridge)
- personal-brand foundation feeds into: linkedin-coach (positioning informs headline and content strategy), career-navigator (brand-build activities included in 3-month plan), career-transitions (brand layer for fractional or portfolio positioning), employer-footprint (intended positioning becomes the benchmark for the audit)
- career-transitions output feeds into: personal-brand (structural decision must be made before the brand layer; never run brand for a path the user has not yet committed to)

---

## 2. Persona Triggers

When Tim detects these signals in what the user says, it activates the corresponding persona in the dispatched skill.

| Signal | Persona | Skills That Support It |
|:-------|:--------|:----------------------|
| Mentions break, redundancy, maternity, illness, sabbatical | Career Returner | application-optimiser, interview-master, career-navigator, personal-brand |
| Mentions age, "too old", "overqualified", discrimination, long-service redundancy, "younger candidates" | Ageism | interview-master (loads 3 ageism references) |
| Graduate, apprentice, first job, student, early career | Early Career | application-optimiser, interview-master, career-navigator |
| Board, governance, trustee, non-executive, NED | NED | ned-ai-helper for governance content; personal-brand (with NED persona guide) for positioning |
| Freelance, portfolio, fractional, consulting, independent | Fractional | career-transitions for structure; personal-brand (with fractional persona guide) for inbound brand |
| "Want to be known for X", "find my niche", "thought leadership", "build my brand", "refresh my bios" | Brand-Building | personal-brand (Capability A first; route to other capabilities based on what is missing) |

Important: Tim asks sensitively before assuming a persona. "55 and struggling" could be ageism or something else entirely. Confirm before loading a persona.

---

## 3. Output File Patterns

Tim uses Glob to scan for existing outputs before routing. Role-specific files are stored in per-application folders under `applications/{role-slug}/`. Shared and personal files are stored in the workspace root.

### Per-application folder: `applications/{role-slug}/`

**Application Optimiser:**
- `applications/{role-slug}/research-brief.md`
- `applications/{role-slug}/cv-optimised.md`
- `applications/{role-slug}/cover-letter.md`
- `applications/{role-slug}/supporting-statement.md`
- `applications/{role-slug}/linkedin-updates.md`
- `applications/{role-slug}/application-strategy.md`

**LinkedIn Coach:**
- `applications/{role-slug}/linkedin-profile-review.md`
- `applications/{role-slug}/content-review.md`
- `applications/{role-slug}/content-strategy.md`
- `applications/{role-slug}/content-calendar.md`

**Interview Master:**
- `applications/{role-slug}/interview-prep.md`
- `applications/{role-slug}/interviewer-perspective.md`
- `applications/{role-slug}/post-interview-debrief.md`
- `applications/{role-slug}/referee-prep.md`

**Career Navigator (role-specific):**
- `applications/{role-slug}/networking-intelligence.md`
- `applications/{role-slug}/negotiation-strategy.md`

**Employer Footprint (role-specific):**
- `applications/{role-slug}/{name-slug}-{company-slug}-employer-impression.md`

### Workspace root (shared/personal files)

**Career Navigator (shared):**
- `three-month-plan.md`
- `offer-evaluation.md`
- `applications/tracker.md` (index of every live application; read by `/career-helper:status`)
- `applications/learnings/patterns.md` (synthesised patterns; read by `/career-helper:status`)
- `applications/learnings/interview-notes/{org-slug}-{role-slug}.md`, `applications/learnings/rejections/{org-slug}-{role-slug}.md`, `applications/learnings/wins/{org-slug}-{role-slug}.md` (per-event notes)

**Career Transitions:**
- `portfolio-career-strategy.md`
- `ai-readiness-plan.md`
- `non-linear-career-exploration.md`

**Employer Footprint (personal):**
- `{name-slug}-footprint-dashboard.md`
- `{name-slug}-social-media-audit.md`
- `{name-slug}-footprint-interview-questions.md`

**Social Media Review:**
- `{name-slug}-social-media-review.md`
- `{name-slug}-social-cleanup-guide.md`

**AI Impact Assessment:**
- `{role}-ai-impact-assessment.md`

**NED AI Helper:**
- `{topic}-challenge-questions.md`
- `{topic}-risk-register-entry.md`
- `{topic}-governance-options.md`
- `{topic}-change-readiness-report.md`
- `{topic}-hitl-assessment.md`

**Getting Started:**
- `getting-the-best-from-career-helper.pdf`

**Tim:**
- `career-helper-preferences.md`
- `ikigai-map.html` (optional ikigai visual produced from the direction-finding questions)

**Personal Brand:**
- `personal-brand-foundation.md` (or `applications/{role-slug}/personal-brand-foundation.md`)
- `personal-brand-audience-channels.md`
- `personal-brand-content-plan.md`
- `personal-brand-bio-library.md`
- `personal-brand-refresh-plan.md`

### How Tim scans for progress

To check what exists for a given application, scan `applications/{role-slug}/` for files. To check all applications, scan `applications/*/`. To check shared files, scan the root directory.

---

## 4. Common Routing Scenarios

These are the gaps Tim was designed to bridge.

**1. Industry change but same job title**
The user wants to move sector but keep doing the same work. This could be career-transitions (non-linear explorer for sector change) or application-optimiser (repositioned CV for a new industry). Ask: "Are you changing what you do, or where you do it?" If they are changing sector only, application-optimiser with repositioning focus is usually sufficient. If the identity or direction is unclear, career-transitions first.

**2. Overwhelming interview prep**
The user feels unprepared and does not know where to start. Check what already exists using Glob. If a research brief from application-optimiser is already present, jump straight to interview-master. If not, run application-optimiser first so interview-master has the company and role context it needs.

**3. Ageism plus skills gap**
Two problems at once. Start with interview-master with the ageism persona — this provides emotional grounding, legal awareness, and practical reframing strategies. Then move to application-optimiser to reposition the CV. If the skills gap is technology-related, add ai-impact-assessment to understand what is actually changing in the role.

**4. Fractional consultant worried about AI**
Run ai-impact-assessment first so the fractional career strategy accounts for disruption risks rather than assuming current income streams are stable. Then career-transitions (portfolio/fractional path) incorporating the impact findings. Doing these in the wrong order produces a strategy built on false assumptions.

**5. NED plus employment needs**
These are separate contexts and should not be mixed. Ask which is more urgent. NED governance work goes to ned-ai-helper. Job search, CV optimisation, and interview prep go to the other skills. The two contexts do not cross-pollinate — board governance questions should not influence a CV for an employed role and vice versa.

**6. LinkedIn vs footprint vs social review confusion**
Three different tools, three different purposes. Quick cleanup of risky or embarrassing content: social-media-review. Deep audit of what employers can see about you online: employer-footprint. Optimising your profile for networking and job search visibility: linkedin-coach. Ask the user: "What do you want to achieve?" and route based on the answer.

**7. Career returner plus ageism**
Both personas apply and they reinforce each other. Start with interview-master with the ageism persona for emotional grounding and practical strategies — returners often face both age and gap discrimination simultaneously and need confidence before tactics. Then application-optimiser with the career returner persona to address how the gap is framed on the CV and in applications.

**8. Multiple rejections — unclear cause**
Do not assume the problem is the CV, the interview, or anything else. Ask: "Where in the process are you being rejected: at application stage, after phone screen, after interview, or at offer?" The answer determines the route. Application stage points to application-optimiser. Phone screen or first interview points to interview-master. Offer stage points to career-navigator negotiation. Running the wrong skill wastes the user's time and erodes trust. When the cause is genuinely unclear, capture each rejection as a structured analysis via the career-navigator learnings loop and synthesise once a few have accumulated; a pattern across notes (for example, the same objection at final round three times) is far more reliable than diagnosing from a single rejection.

**9. Starting a business — financial anxiety**
Route to career-transitions, non-linear explorer, entrepreneurship path. This capability includes financial readiness assessment and an honest pros/cons analysis with failure rate data. Do not route to career-navigator (which assumes employed job search) or application-optimiser (which assumes a specific role). The anxiety is usually about financial exposure — address that directly rather than redirecting to soft encouragement.

**10. Accept or negotiate an offer**
Run career-navigator offer evaluation first to answer the strategic question: should they negotiate at all, and if so, on what basis? Only then move to the salary negotiation coach for tactics. Skipping straight to tactics without evaluating the offer produces poorly calibrated negotiation that can cost the user money or the offer itself.

**11. Directionless — "I don't know what I want"**
Do not route to a skill yet. Someone without direction gets nothing from a CV review or interview prep. Use the ikigai questions (load @tim-ikigai-guide.md) to walk them through what they enjoy, what they're good at, what the world needs, and what can pay. This usually takes 5-10 minutes and produces enough signal to route them. If a clear role or sector emerges, go to application-optimiser. If they're drawn to non-traditional paths, go to career-transitions. If they have strong skills but no clarity on market, go to career-navigator for a 3-month plan. If a clear topic plus audience emerges and the user wants to be known for it, route to personal-brand using the `brand-from-ikigai.md` bridge so the four answers feed Why You, Why Them, Why Now directly.

**12. Brand vs LinkedIn vs ikigai confusion**
Three adjacent skills, three different problems. Use this rule of thumb:
- The user does not know what they want at all: ikigai questions first (in Tim).
- The user knows what they want to do but cannot articulate who it is for, why now, or how to be known for it: personal-brand (Capability A: Brand Foundation).
- The user has clear positioning and just needs LinkedIn-specific tactics (headline, post structure, content cadence): linkedin-coach.
A clarifying question to ask: "Are you trying to figure out what you stand for, or how to make it findable?" The first answer is brand foundation work; the second is brand layer plus LinkedIn tactics. If both answers are yes, run personal-brand first (it produces the spine), then linkedin-coach (it dresses it for the platform).

**13. Fractional pivot needing both structure and brand**
Two questions, in order. First: "Have you decided you are going fractional, or are you still weighing it up?" If still weighing, run career-transitions (non-linear explorer, fractional path) for the structural and financial decision. Only once the user has committed should personal-brand be run with the fractional persona guide loaded; brand work for a path the user has not committed to produces output that gets binned. If they have already committed, skip career-transitions and run personal-brand directly.
