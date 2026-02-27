# Deep Research Reflection for Employer Footprint Analysis

**Pattern for research-intensive digital footprint deliverables.**

**Purpose:** Ensure rigorous, evidence-based research during digital footprint auditing, social media analysis, and employer impression assessment.

---

## When to Apply This Workflow

Apply during these capabilities:

| Capability | Research Focus |
|:-----------|:---------------|
| **Full Footprint Analysis** | Multi-channel digital presence, employer impression |
| **Social Media Audit** | Platform-specific content and tone analysis |
| **Employer Impression Report** | Company culture mapping against candidate presence |
| **Interview Questions from Footprint** | Evidence-based question generation |

---

## The Deep Research Reflection Loop

This workflow uses **multiple search cycles** to achieve depth. Single-pass research often misses critical insights - especially important when the goal is to find what an employer might find.

```
┌─────────────────────────────────────────────────────────────┐
│            FOOTPRINT DEEP RESEARCH REFLECTION LOOP          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. SCOPE                                                  │
│      └─► Define search terms, name variations, platforms    │
│                                                             │
│   2. SEARCH (Primary - Parallel Swarm)                      │
│      └─► Execute parallel searches across all channels      │
│                                                             │
│   3. VALIDATE + GAP ANALYSIS                                │
│      └─► Cross-reference findings, identify missing data    │
│                                                             │
│   4. SEARCH (Secondary) ◄─── CRITICAL ADDITION             │
│      └─► Target gaps, dig deeper on flagged content         │
│                                                             │
│   5. RED FLAG HUNT                                          │
│      └─► Actively search for concerning content             │
│                                                             │
│   6. CROSS-REFERENCE                                        │
│      └─► CV vs online presence consistency check            │
│                                                             │
│   7. SYNTHESISE + SCORE                                     │
│      └─► Consolidate, score dimensions, generate dashboard  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 1: Scope

Before searching, define the search scope:

```
SEARCH SCOPE:
Name variations to search:
- "{Full Name}" (as provided)
- "{First Last}" (simplified)
- "{Professional Name}" (if different from legal name)
- "{Maiden/Previous Name}" (if provided by user)

Platforms to check:
- Google (general search)
- LinkedIn
- Twitter/X
- GitHub
- {Other platforms provided by user}

Target context:
- Company: {If provided}
- Role: {If provided}
- Industry: {Inferred from CV/role}
```

---

## Step 2: Primary Search (Parallel Swarm)

**CRITICAL: Execute ALL channel searches in parallel for speed.**

Launch simultaneous searches:

```
Parallel Wave 1:
- WebSearch: "{name}" (bare search, first 3 pages equivalent)
- WebSearch: "{name}" linkedin
- WebSearch: "{name}" twitter OR x.com
- WebSearch: "{name}" github
- WebSearch: "{name}" "{current company}"
- WebSearch: "{name}" "{target company}" (if provided)
```

```
Parallel Wave 2 (based on handles):
- WebSearch: "from:{twitter_handle}" (recent posts)
- WebFetch: github.com/{github_username} (if provided)
- WebFetch: {personal_website} (if provided)
- WebSearch: "{name}" medium OR blog
- WebSearch: "{name}" conference OR speaker OR panel
```

---

## Step 3: Validate + Gap Analysis

After primary search, explicitly check:

```
GAP ANALYSIS:
□ Which platforms returned NO results? (Note as [NOT FOUND])
□ Which platforms were INACCESSIBLE? (Note as [PRIVATE])
□ Are there NAME CONFLICTS (other people with same name)?
□ Did we find ALL platforms the user mentioned?
□ Are there INCONSISTENCIES between platforms?
□ What would a recruiter find vs what we found? (Any gaps?)
□ Did we check the CV against EVERY platform?
```

---

## Step 4: Secondary Search

Fill gaps identified in Step 3:

```
For each gap:
1. Identify what's missing
2. Craft specific search query
3. Execute and document results
4. Update assessment
```

---

## Step 5: Red Flag Hunt

**Actively search for content that could concern an employer:**

```
RED FLAG SEARCH QUERIES:
1. "{name}" AND (controversial OR offensive OR complaint)
2. "{name}" AND (fired OR terminated OR dismissed)
3. "{name}" AND (political OR protest) [note: not inherently negative]
4. "{name}" AND (arrest OR lawsuit OR court)
5. "{name}" AND (rant OR angry OR furious)
6. "{twitter_handle}" AND (deleted OR apologised) [past controversies]

CROSS-REFERENCE FLAGS:
- CV claims vs verifiable evidence
- Job titles: inflation or deflation?
- Dates: gaps or overlaps?
- Qualifications: verifiable?
```

**Important:** Finding political content, activism, or personal opinions is NOT automatically a red flag. Note these objectively and let the user decide how to handle them in the context of their target employer.

---

## Step 6: Cross-Reference (CV Consistency)

```
CV CONSISTENCY CHECK:
For each CV entry, check against online presence:

□ Job titles match across CV, LinkedIn, other platforms?
□ Employment dates are consistent?
□ Company names are the same?
□ Education claims are verifiable?
□ Skills claimed are evidenced online?
□ Career narrative is consistent?
□ No unexplained gaps between platforms?
```

---

## Step 7: Synthesise + Score

Score all 8 dimensions and generate dashboard:

```
SCORING CHECKLIST:
□ Professional Visibility scored with evidence
□ Brand Consistency scored with evidence
□ Thought Leadership scored with evidence
□ Cultural Fit Signals scored with evidence (if company provided)
□ Red Flag Risk scored with evidence
□ Network Strength scored with evidence
□ Technical Credibility scored with evidence (if applicable)
□ Content Quality scored with evidence
□ Overall score calculated
□ Dashboard template populated
□ Recommendations generated
□ Career-helper next steps identified
```

---

## Quality Gates

Before completing the analysis:

```
FOOTPRINT ANALYSIS QUALITY CHECKLIST:

PRIMARY RESEARCH:
□ All user-provided platforms checked
□ Google search executed with name variations
□ Multiple search queries per platform
□ WebFetch used where accessible

GAP ANALYSIS:
□ Gaps explicitly identified
□ Private/inaccessible platforms noted
□ Name conflicts checked
□ User asked for screenshots where needed

RED FLAG HUNT:
□ Controversial content search executed
□ Inconsistency scan completed
□ CV cross-reference done
□ Results documented objectively

SCORING:
□ All applicable dimensions scored 1-10
□ Evidence cited for each score
□ Traffic-light indicators applied
□ Strengths and concerns listed

OUTPUT:
□ Dashboard template followed completely
□ All sections populated or marked [NOT APPLICABLE]
□ Sources listed with URLs and access dates
□ Recommendations are specific and actionable
□ Career-helper next steps included
```

---

*Created by Prosper AI Consulting*
