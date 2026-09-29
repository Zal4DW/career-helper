---
name: employer-footprint
description: Use when the user wants a full, scored audit of what an employer would find about them online, matched to a specific target company or role. Runs parallel research across social media, public content, and search presence, then produces a credit-report style dashboard of positive and negative signals with recommendations. For a quick, informal social media check, use social-media-review instead.
tags: footprint, digital, social-media, audit, employer, impression, online-presence, reputation
---

# Employer Footprint Analysis

See yourself through an employer's eyes. A deep-research swarm audit of your digital footprint, synthesised into a credit-report style dashboard with actionable recommendations.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Full Footprint Analysis | Complete audit: social media, public content, employer impression dashboard |
| 2 | Social Media Audit | Focused audit of specific social channels |
| 3 | Employer Impression Report | How a specific company/role would interpret your online presence |
| 4 | Interview Prep from Footprint | Generate likely interview questions based on your digital presence |

## Quick Start

```
"Check my digital footprint before I apply to the NHS"
"What would a recruiter find if they searched for me online?"
"Audit my LinkedIn and Twitter for red flags"
"Generate interview questions based on what's publicly visible about me"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true** → Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition ("Step 2 of 4. Next: employer impression report."). Refer to saved files by description, not filename. Repeat key details (company names, role titles, dates); do not assume the user remembers from earlier messages.
- **colour_blind: true** → Never use colour alone to convey meaning. Use labels, text, or icons for all status indicators. Dashboard scores must use text labels, not colour coding.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim): ask once, "Do you have any accessibility preferences I should know about? For example, if you're dyslexic I can adjust how I format things." If yes, save to `career-helper-preferences.md` using the format in @../tim/references/tim-preferences-format.md before continuing. If the user declines or says no, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of output documents**.

---

## How It Works

This skill uses an **agentic deep-research swarm** approach:

1. **You provide** your name, CV, social media handles, and target company/role
2. **Parallel research agents** scan publicly available data across multiple channels simultaneously
3. **Employer lens analysis** interprets findings through the target company's values and culture
4. **Dashboard synthesis** produces a credit-report style output with positive/negative indicators
5. **Recommendations** suggest next actions across career-helper skills

---

## Input Gathering

Before starting any analysis, collect the following via AskUserQuestion:

### Required Information

**Question 1: Basic Details**
"To analyse your digital footprint, I need some details. Let's start with the basics - what is your full name (as it appears professionally)?"

**Question 2: Social Media Handles**
"Which social media platforms do you use? Please share your usernames/URLs for any that apply:"
- LinkedIn profile URL
- GitHub username
- Twitter/X handle
- Personal website or blog URL
- Any other professional platforms (Medium, Stack Overflow, Behance, Dribbble, YouTube, etc.)

**Question 3: Target Context**
"Are you targeting a specific company and role? If so, please share:"
- Company name
- Role title
- Job description (if available)

**Question 4: CV**
"Please share your CV - either paste the text, provide a file path, or upload it."

**Question 5: Concerns**
"Is there anything specific you're worried an employer might find? (This helps me focus the analysis - everything stays private.)"

---

## 1. Full Footprint Analysis

**What you need:** Name + social handles + CV + target company/role (optional)
**Load:** @references/digital-footprint-audit.md
**Template:** @references/footprint-dashboard-template.md

Agentic parallel research covering:

### Research Swarm Architecture

Launch parallel research agents for each channel simultaneously:

```
┌─────────────────────────────────────────────────────────────┐
│              EMPLOYER FOOTPRINT RESEARCH SWARM              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│   │ Agent 1  │  │ Agent 2  │  │ Agent 3  │  │ Agent 4  │  │
│   │ Google   │  │ LinkedIn │  │ Twitter/ │  │ GitHub   │  │
│   │ Presence │  │ Analysis │  │ X Audit  │  │ Profile  │  │
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│        │             │             │             │          │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│   │ Agent 5  │  │ Agent 6  │  │ Agent 7  │  │ Agent 8  │  │
│   │ Other    │  │ News &   │  │ Company  │  │ Red Flag │  │
│   │ Socials  │  │ Media    │  │ Culture  │  │ Scanner  │  │
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│        │             │             │             │          │
│        └──────┬──────┴──────┬──────┴──────┬──────┘          │
│               │             │             │                 │
│         ┌─────▼─────────────▼─────────────▼─────┐          │
│         │       SYNTHESIS & DASHBOARD ENGINE      │          │
│         │                                         │          │
│         │  • Score each dimension (1-10)           │          │
│         │  • Flag positives and negatives          │          │
│         │  • Map to employer values                │          │
│         │  • Generate recommendations              │          │
│         └─────────────────────────────────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Channels Audited

| Channel | What We Check | Agent |
|:--------|:-------------|:------|
| **Google Search** | First 3 pages of results for your name, name + company, name + role | Agent 1 |
| **LinkedIn** | Profile completeness, headline, activity, recommendations, endorsements | Agent 2 |
| **Twitter/X** | Recent posts, tone, controversial content, professional vs personal mix | Agent 3 |
| **GitHub** | Repos, contributions, commit history, profile completeness, README quality | Agent 4 |
| **Facebook/Instagram** | Public-facing content, privacy settings effectiveness | Agent 5 |
| **Medium/Blog** | Published articles, thought leadership signals | Agent 5 |
| **YouTube** | Public videos, comments, channel content | Agent 5 |
| **Stack Overflow** | Reputation, quality of contributions | Agent 5 |
| **News/Media** | Press mentions, quotes, conference talks | Agent 6 |
| **Company Culture** | Target company values, culture, what they look for | Agent 7 |
| **Red Flags** | Controversial content, inconsistencies, negative mentions | Agent 8 |

### Scoring Dimensions

Each dimension scored 1-10 with text-label rating (GREEN/AMBER/RED):

| Dimension | What It Measures |
|:----------|:----------------|
| **Professional Visibility** | How easily found, how professional the first impression |
| **Brand Consistency** | Alignment across platforms (titles, dates, narrative) |
| **Thought Leadership** | Evidence of expertise, content creation, industry engagement |
| **Cultural Fit Signals** | Alignment with target company values and culture |
| **Red Flag Risk** | Potentially controversial or concerning content |
| **Network Strength** | Connections, endorsements, recommendations quality |
| **Technical Credibility** | Code contributions, technical writing, certifications |
| **Content Quality** | Quality and professionalism of public posts and content |

**Output:** `{name-slug}-footprint-dashboard.md`

---

## 2. Social Media Audit

**What you need:** Social media handles for specific platforms
**Load:** @references/social-media-audit.md

Focused deep-dive into specific social channels:
- Platform-by-platform analysis
- Content tone assessment
- Privacy settings check (what's publicly visible)
- Recruiter-eye-view of each profile
- Specific recommendations per platform

**Output:** `{name-slug}-social-media-audit.md`

---

## 3. Employer Impression Report

**What you need:** Name + CV + target company name + role
**Load:** @references/employer-impression-analysis.md
**Template:** @references/footprint-dashboard-template.md
**Also Load:** @references/digital-footprint-audit.md

The full footprint analysis interpreted specifically through the lens of the target employer:
- Company values and culture research (parallel with footprint analysis)
- Map your digital presence against their stated values
- Identify aspects of your experience to prioritise based on company needs
- Flag any misalignments between your online presence and their culture
- Generate talking points that leverage your digital presence positively

**Output:** `applications/{role-slug}/{name-slug}-{company-slug}-employer-impression.md` if an application folder exists for this company; otherwise `{name-slug}-{company-slug}-employer-impression.md` in the workspace root

---

## 4. Interview Questions from Footprint

**What you need:** Completed footprint analysis or employer impression report
**Load:** @references/interview-questions-from-footprint.md

Generate likely interview questions based on what's publicly visible:
- Questions about specific projects or roles mentioned online
- Questions probing gaps or inconsistencies found
- Questions about controversial or interesting content discovered
- Questions that leverage your strongest public signals
- Preparation strategies for each question category

**Output:** `{name-slug}-footprint-interview-questions.md`

---

## Deep Research Validation

All research uses a rigorous multi-cycle validation workflow:
**Load:** @references/deep-research-reflection.md

- **Gap Analysis** - After initial search, identify what's missing
- **Counter-Evidence Search** - Actively search for contradicting information
- **Source Credibility Scoring** - Primary sources weighted over secondary
- **Red Flag Hunting** - Proactively search for negative/controversial content
- **Citation Requirements** - All findings include source URLs and access dates

---

## Research Approach

The audit covers several independent sources (search-engine presence, LinkedIn, X/Twitter, GitHub, and the target company's culture and values), so run that research in parallel with Task sub-agents and parallel WebSearch calls rather than one source at a time. Use Sonnet for these research sub-agents; it searches and extracts well at a lower cost, and the scoring and recommendations stay with the main model.

Once the first pass is back, look for what is missing: flagged content that needs a closer look, claims on the CV that the online presence does not support, and counter-evidence or red flags the first searches did not surface. Search for those next. Then score every dimension, generate the dashboard, map the findings to the employer's values, and write the recommendations.

---

## Persona Adaptation

When the user's context matches a specific persona, adapt the analysis focus:

| Persona | Adaptation | Trigger |
|:--------|:----------|:--------|
| Career Returner | Focus on explaining gaps positively; check if old profiles are outdated | User mentions career break |
| Early Career | Emphasise building presence rather than auditing; check student social media | Graduate or limited experience |
| Senior/Executive | Focus on thought leadership, board-level presence, media mentions | VP+ or C-suite level |
| NED/Board | Governance signals, independence markers, conflicts of interest | Board or trustee roles |
| Fractional | Multi-company narrative consistency, expertise positioning | Portfolio or fractional career |

---

## Output Standards

- **UK English** throughout (unless US role explicitly requires US English)
- **No emojis** - Professional tone
- **Cited sources** - All findings include URLs and access dates
- **Text-label ratings:** GREEN/AMBER/RED as text, never colour alone
- **Evidence-based** - Every flag backed by specific findings
- **Never invent data** - Mark missing info as `[NOT FOUND]` or `[PRIVATE]`
- **Privacy-conscious** - Only analyse publicly available information

### Tone of Voice
- Address the user as "you", not by name: "Your digital presence shows..." not "Bethan's digital presence shows..."; default to second person for warmth and engagement; occasional name use is fine for emphasis
- Avoid hyperbole and cinema poster phrasing (not "game-changing", "revolutionary", or "supercharge your career")
- Use the **Oxford comma** (serial comma: "skills, experience, and qualifications")
- Never use em dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

When a capability names a template, load it with the @ reference before writing, and follow its structure and footer. Users and other skills rely on the same headings appearing in the same places.

### Working with Blocked Content

When WebFetch fails (LinkedIn, Glassdoor, paywalled content):
- Ask user to screenshot the page (Read tool processes images)
- Or copy/paste text directly
- Or save as PDF and provide path
- Screenshots are read accurately, including dense pages, so a full-page capture is fine; ask only for the pages that matter to the task, to save the user effort

---

## Workspace Recommendation

**IMPORTANT:** For the best experience, always use the same local folder for your career-helper sessions. This allows you to:
- Build on previous analyses across sessions
- Keep all career-helper outputs in one place
- Reference earlier reports when running new skills
- Track your progress over time

**Recommended setup:**
```
mkdir -p ~/career-helper-workspace
cd ~/career-helper-workspace
```

Then run all career-helper skills from this folder. Use `/career-helper:status` to see all your generated outputs.

---

## Recommended Next Actions

After completing a footprint analysis, career-helper can help you act on the findings:

| Finding | Recommended Skill | Action |
|:--------|:-----------------|:-------|
| LinkedIn needs improvement | **/linkedin-coach** | Profile audit and optimisation |
| Content gaps identified | **/linkedin-coach** | Content strategy and calendar |
| CV doesn't match online presence | **/application-optimiser** | CV optimisation with consistency |
| Interview questions generated | **/interview-master** | Full interview prep and mock |
| Company culture concerns found | **/application-optimiser** | Deeper company research |
| Career narrative inconsistent | **/career-navigator** | Networking intelligence and strategy |
| Considering career change | **/career-transitions** | Portfolio career or AI readiness |

---

## Relationship to /social-media-review

`/social-media-review` is the **lightweight version** of the social media audit within this skill:

| Feature | /social-media-review | /employer-footprint |
|:--------|:--------------------|:-------------------|
| Social media check | Quick scan | Deep audit |
| Google presence search | Basic | Comprehensive |
| CV cross-reference | No | Yes |
| Company culture mapping | No | Yes |
| Scored dashboard (1-10) | No | Yes |
| Interview questions | No | Yes |
| Parallel research agents | No | Yes (8 agents) |
| Best for | Quick check, graduates | Full pre-application audit |

**When to recommend /social-media-review instead:**
- User is a graduate or early career and just wants a quick check
- User asks to "review my social media" or "check my Instagram"
- User wants privacy settings advice and cleanup guidance
- User doesn't have a target company and isn't doing a formal job search yet

---

## Related Skills

- **/social-media-review** - Quick social media health check (lighter alternative)
- **/application-optimiser** - Research the company and optimise your CV
- **/linkedin-coach** - Fix LinkedIn issues identified in the audit
- **/interview-master** - Prepare for questions based on your footprint
- **/career-navigator** - Build networking strategy leveraging your strengths

---

*Employer Footprint Analysis | Career Helper Plugin | Prosper AI Consulting, UK*
