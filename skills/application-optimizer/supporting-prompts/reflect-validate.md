# Reflective Validation Workflow - Career Helper

**Purpose:** Ensure generated career content meets quality standards before presenting to user.

**Based on:** Anthropic's [Evaluator-Optimizer Pattern](https://www.anthropic.com/research/building-effective-agents)

---

## When to Use This Workflow

**Always validate for:**
- CV/ATS optimization (critical - affects job applications)
- Company research briefs (citations must be accurate)
- Interview preparation (answers must be evidence-backed)
- LinkedIn profile recommendations (professional reputation at stake)

**Skip validation for:**
- Quick questions about capabilities
- Clarification requests
- Brainstorming/ideation

---

## The Reflect-Validate Loop

```
Generate → Evaluate → If NEEDS_IMPROVEMENT → Refine → Re-evaluate
                    → If PASS → Present to user
                    → Max 3 iterations
```

---

## Language Compliance (UK English)

**Check BEFORE capability-specific validation:**

| Check | Pass | Fail |
|-------|------|------|
| **UK Spelling** | organisation, colour, behaviour, optimise, analyse, centre | organisation, color, behavior, optimize, analyze, center |
| **Em Dashes** | None present | — used anywhere |
| **Override** | US role explicitly requires US English | Default should be UK |

**Common UK vs US Spelling:**
| UK (Correct) | US (Incorrect) |
|--------------|----------------|
| organisation | organisation |
| colour | color |
| behaviour | behavior |
| optimise | optimize |
| analyse | analyze |
| centre | center |
| programme | program |
| favour | favor |
| honour | honor |
| labour | labor |
| recognise | recognize |
| realise | realize |
| specialise | specialize |
| summarise | summarize |
| personalise | personalize |
| customise | customize |
| prioritise | prioritize |
| maximise | maximize |
| minimise | minimize |

**Language Validation Output Format:**
```xml
<language_evaluation>PASS | NEEDS_IMPROVEMENT | FAIL</language_evaluation>
<language_feedback>
- US spellings found: [list with UK corrections]
- Em dashes found: [locations]
</language_feedback>
```

**Note:** If user explicitly targets US role or requests US English, UK spelling check is skipped.

---

## Validation Criteria by Capability

### 1. CV/ATS Optimization

**Content Requirements:**
| Criterion | Check |
|-----------|-------|
| **Keyword Coverage** | ≥70% of JD keywords integrated? |
| **Quantified Achievements** | Numbers, percentages, metrics present? |
| **ATS-Safe Formatting** | No tables, graphics, columns, fancy fonts? |
| **Role Alignment** | Summary/headline matches target role? |
| **Skills Match** | Skills section reflects JD requirements? |

**Output Format:**
```xml
<cv_evaluation>PASS | NEEDS_IMPROVEMENT | FAIL</cv_evaluation>
<cv_feedback>
- Keyword coverage: X% (target: 70%+)
- Missing key terms: [list]
- Formatting issues: [list]
- Suggested improvements: [specific changes]
</cv_feedback>
```

### 2. Company Research Briefs

**Content Requirements:**
| Criterion | Check |
|-----------|-------|
| **All Sections Present** | Overview, Leadership, Culture, Competitors, News, Red Flags? |
| **Citation Quality** | EVERY factual claim has a source? |
| **Source Recency** | News from last 6-12 months? |
| **Source Diversity** | Multiple source types used? |
| **Red Flags Assessed** | Risk section included and honest? |

**Citation Validation:**
```xml
<citation_evaluation>PASS | NEEDS_IMPROVEMENT | FAIL</citation_evaluation>
<citation_feedback>
- Claims without sources: [list]
- Outdated sources: [list]
- Missing perspectives: [list]
</citation_feedback>
```

**CRITICAL:** Citation quality is this skill's differentiator. NO uncited claims allowed.

### 3. Interview Preparation

**Content Requirements:**
| Criterion | Check |
|-----------|-------|
| **Question Coverage** | Behavioral, technical, culture, ask-interviewer? |
| **STAR Format** | Behavioral answers use Situation-Task-Action-Result? |
| **Role Specificity** | Questions tailored to specific role/level? |
| **Company Context** | Talking points reference company specifics? |
| **Evidence-Based** | Answers include specific examples? |

**Output Format:**
```xml
<interview_evaluation>PASS | NEEDS_IMPROVEMENT | FAIL</interview_evaluation>
<interview_feedback>
- Missing question types: [list]
- Generic answers (need personalization): [list]
- STAR format issues: [list]
</interview_feedback>
```

### 4. LinkedIn Profile Optimization

**Content Requirements:**
| Criterion | Check |
|-----------|-------|
| **All Sections Reviewed** | Photo, banner, headline, about, experience, skills, recommendations? |
| **Headline Optimized** | Contains role keywords, clear value proposition? |
| **About Section** | Compelling, keyword-rich, appropriate length? |
| **Skills Ordering** | RSC API top 3 considered? |
| **Discoverability** | Recruiter search optimization addressed? |

**Output Format:**
```xml
<linkedin_evaluation>PASS | NEEDS_IMPROVEMENT | FAIL</linkedin_evaluation>
<linkedin_feedback>
- Sections not reviewed: [list]
- Headline issues: [details]
- About section improvements: [details]
</linkedin_feedback>
```

### 5. Strategic Networking

**Content Requirements:**
| Criterion | Check |
|-----------|-------|
| **Prioritized List** | Connections ranked by strategic value? |
| **Rationale Provided** | Why each connection matters? |
| **Outreach Personalized** | Specific approach for each person? |
| **Mutual Paths** | Common connections identified? |

### 6. Content Strategy

**Content Requirements:**
| Criterion | Check |
|-----------|-------|
| **Content Pillars** | 3-5 clear themes defined? |
| **Posting Schedule** | Realistic frequency established? |
| **Templates Provided** | Example posts for each pillar? |
| **Engagement Tactics** | How to build engagement explained? |

---

## Implementation Workflow

### Step 1: Generate Initial Content

Create the requested career deliverable following the appropriate template and loading relevant supporting prompts.

### Step 2: Self-Evaluate

Before presenting to user, run internal validation:

```markdown
## Internal Validation Check

### Capability: [CV/Research/Interview/LinkedIn/Networking/Content]

**Content Completeness:**
- [ ] All required sections present?
- [ ] Appropriate template structure used?
- [ ] User's specific context incorporated?

**Quality Checks:**
- [ ] [Capability-specific checks from above]

**Citation Check (if applicable):**
- [ ] Every factual claim has a source?
- [ ] Sources are recent and credible?

**Status:** PASS / NEEDS_IMPROVEMENT / FAIL
```

### Step 3: Iterate if Needed

If NEEDS_IMPROVEMENT:
1. Note specific issues
2. Refine content addressing each issue
3. Re-evaluate
4. Maximum 3 iterations

### Step 4: Present with Confidence Statement

When presenting validated content:

```markdown
## [Deliverable Title]

[Content]

---

**Quality Assurance:**
- ✅ [Key validation point 1]
- ✅ [Key validation point 2]
- ✅ Citations verified (if applicable)

*This content has been validated against Career Helper quality standards.*
```

---

## Special Validation Rules

### Citation Requirements (Research & Interview)

**MANDATORY for:**
- Company research briefs
- Interview preparation (company facts)
- Any factual claims about companies, people, or market data

**Format:**
- Inline: "[Source: Publication/URL]"
- Or footnotes at section end
- Include access date for web sources

**Validation:**
```
For each factual claim:
1. Is there a source? → If no, ADD SOURCE or REMOVE CLAIM
2. Is source credible? → News, official sites, analyst reports preferred
3. Is source recent? → News <12 months, company info <6 months ideal
```

### ATS Safety (CV Optimization)

**ALWAYS validate CV outputs for:**
- No tables (will be scrambled by ATS)
- No columns (parsing issues)
- No graphics/images (ignored by ATS)
- No headers/footers (often stripped)
- No fancy fonts (may not render)
- Standard section headings (Experience, Education, Skills)
- Contact info at top (not in header)

### Career Stage Appropriateness

**Consider user's career stage when validating tone:**
- Early career: More guidance, less assumed knowledge
- Mid-career: Balance of guidance and peer-level advice
- Senior: Strategic, executive tone, assume experience

---

## Quick Reference: Validation Prompts

### CV Validation Prompt
```
Validate this CV against the job description:

**Job Description Keywords:** [extracted keywords]
**CV Content:** [generated CV]

Check:
1. Keyword coverage (target: 70%+)
2. Quantified achievements present
3. ATS-safe formatting
4. Role alignment in summary
5. Skills match

Output: <cv_evaluation>PASS|NEEDS_IMPROVEMENT|FAIL</cv_evaluation>
```

### Citation Validation Prompt
```
Validate citations in this research brief:

**Content:** [research brief]

For each factual claim:
1. Is there a source cited?
2. Is the source recent (<12 months for news)?
3. Is the source credible?

List any uncited claims or issues.

Output: <citation_evaluation>PASS|NEEDS_IMPROVEMENT|FAIL</citation_evaluation>
```

---

## Example: Full Validation Flow

**User Request:** "Optimize my CV for this Data Scientist role at Netflix"

### Iteration 1

**Generated:** CV with role-aligned summary, experience bullets...

**CV Evaluation:** NEEDS_IMPROVEMENT
- Keyword coverage: 55% (target: 70%+)
- Missing: "A/B testing", "recommendation systems", "Python"
- Quantification: Only 2 of 5 bullets have metrics

### Iteration 2

**Refined:** Added missing keywords, quantified remaining bullets...

**CV Evaluation:** PASS
- Keyword coverage: 78% ✓
- All bullets have metrics ✓
- ATS-safe formatting ✓
- Role alignment ✓

### Final Output to User

**Optimized CV for Data Scientist - Netflix**

[CV Content]

---

**Quality Assurance:**
- ✅ 78% keyword coverage from job description
- ✅ All achievements quantified with metrics
- ✅ ATS-safe formatting verified
- ✅ Summary aligned to Data Scientist role

*Validated against Career Helper ATS optimization standards.*

---

**Document Version:** 1.0
**Created:** 2025-11-22
**Pattern Source:** [Anthropic Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
