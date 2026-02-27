---
name: employer-footprint
description: This skill should be used when the user asks to "check my digital footprint", "what will employers see about me online", "audit my online presence", "what does my digital profile look like to a recruiter", "check my social media for red flags", or "employer impression report". Conducts a comprehensive digital footprint analysis through the lens of a potential employer, producing a credit-report style dashboard of positive and negative signals across social media channels, public content, and online presence.
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
"Check my digital footprint before I apply to Google"
"What would a recruiter find if they Googled me?"
"Audit my LinkedIn and Twitter for red flags"
"Generate interview questions based on what's publicly visible about me"
```

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

Each dimension scored 1-10 with traffic-light indicator:

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

**Output:** `{name-slug}-{company-slug}-employer-impression.md`

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

## Parallel Execution Strategy

**CRITICAL: Use parallel Task tool calls for maximum speed and depth.**

```markdown
Wave 1 (Parallel):
- Task Agent: Google presence search (name variations)
- Task Agent: Company culture and values research
- WebSearch: LinkedIn profile analysis
- WebSearch: Twitter/X content audit
- WebSearch: GitHub profile analysis

Wave 2 (After Wave 1 results):
- Task Agent: Deep-dive on flagged content
- Task Agent: Cross-reference CV against online presence
- WebSearch: Fill identified gaps
- WebSearch: Counter-evidence and red flag hunt

Wave 3 (Synthesis):
- Score all dimensions
- Generate dashboard
- Map to employer values
- Generate recommendations
```

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
- **Traffic-light scoring** - Clear visual indicators (GREEN/AMBER/RED)
- **Evidence-based** - Every flag backed by specific findings
- **Never invent data** - Mark missing info as `[NOT FOUND]` or `[PRIVATE]`
- **Privacy-conscious** - Only analyse publicly available information

### Template Usage

When a capability specifies a template, you MUST:
1. Load the template first using @ symbol
2. Follow the template structure exactly
3. Preserve template footers

### Working with Blocked Content

When WebFetch fails (LinkedIn, Glassdoor, paywalled content):
- Ask user to screenshot the page (Read tool processes images)
- Or copy/paste text directly
- Or save as PDF and provide path
- Only request screenshots for critical content (top 3-5 items)

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

*Employer Footprint Analysis v1.0.0 | Career Helper Plugin | Prosper AI Consulting, UK*
