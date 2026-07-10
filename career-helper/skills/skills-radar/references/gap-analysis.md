# Gap Analysis and Learning Plan

**Purpose:** Compare the user's evidenced inventory against what a target role actually demands, prioritise the differences honestly, and turn the top gaps into a plan that fits the user's real capacity.

---

## Step 1: Establish Demand

The target can be a specific posting, a role type, or a direction. Extract demand accordingly:

- **Specific posting:** parse must-have and nice-to-have requirements from the text. Treat "essential" and "desirable" sections literally where they exist; otherwise infer from emphasis and repetition, and say that you inferred.
- **Role type or direction:** research live demand rather than relying on memory. Sample five to eight current postings for the target role and level via WebSearch, extract the recurring requirements, and cite the postings sampled. Requirements that appear in most postings are must-haves; occasional ones are nice-to-haves.
- Record demand with its source. A requirements list with no provenance is opinion.

---

## Step 2: Map Supply Against Demand

For every requirement, look it up in the inventory (`skills-inventory.md`; build one first via Skills Inventory Enrichment if none exists) and classify:

| Status | Meaning | Typical fix |
|:-------|:--------|:------------|
| Evidenced | Inventory shows Solid or Strong | None; make sure the CV says it |
| Partially evidenced | Working level, or evidenced in a different context | Small project or reframing |
| Evidence gap | The user has it but nothing demonstrates it | Create proof, not competence: a portfolio artefact, a written case study, a CV rewrite |
| Skill gap | Not present in the inventory | Learning plan material |

The evidence gap versus skill gap distinction is the most useful thing this analysis produces. Announcing a six-month course for something the user already does weekly at work is a failure of diagnosis.

If `applications/learnings/patterns.md` exists, cross-read it: an objection that has come up in two interviews ("lacks commercial ownership") is live market feedback and outranks inference from postings.

---

## Step 3: Prioritise with a Text-Label Matrix

Priority combines how much the role depends on the requirement with how far the user is from it:

| | Must-have for the role | Nice-to-have for the role |
|:--|:--|:--|
| **Skill gap** | Critical | Worth planning |
| **Evidence gap or partial** | Important, usually quick | Nice to have |

Present the full mapping as a table (the "heatmap", rendered as text labels, never colour): requirement, demand level, supply status, priority, and the one-line fix. Sort by priority.

Then say the honest headline out loud:

- Mostly Evidenced and evidence gaps: "You are closer than your CV suggests; this is mainly a proof problem."
- One or two Criticals: "Closable; here is what it takes and how long."
- Several Criticals: "This target is a stretch from where the evidence stands today. The options are a longer runway, an intermediate role, or a different target." Do not soften this into a shopping list of courses.

**Output:** save as `skills-gap-analysis.md`, or `applications/{role-slug}/skills-gap-analysis.md` when the target is one specific application.

---

## Learning Plan

Only after the gap analysis, and only for the gaps that matter. Rules:

1. **Three gaps maximum.** A plan addressing six gaps addresses none. Criticals first, then Importants; quick evidence fixes can ride alongside because they cost little.
2. **Capacity honesty.** Ask for realistic weekly hours and build to that number. State the completion horizon that capacity implies; if it is nine months and the user's search cannot wait nine months, surface the conflict now, not at the first checkpoint.
3. **Research resources live.** WebSearch for current courses, books, documentation, and communities per gap. Every resource carries a URL, price or "free", and a time estimate. Favour reputable free or low-cost first (official documentation, university-backed MOOCs, recognised industry bodies); name a paid option only when it is clearly stronger.
4. **Every gap pairs learning with evidence-building.** A course closes a gap privately; a project, a written piece, a talk, or a volunteering role closes it publicly. Specify both halves per gap: the learning and the artefact that will prove it.
5. **Checkpoints connect to the search.** At each checkpoint (fortnightly or monthly): what was completed, what artefact exists now, and the loop actions: update the CV via `/application-optimiser`, refresh the inventory entry, and re-rank open roles via `/job-scout` if Winnability has changed.

Load `@references/learning-plan-template.md` and save to `learning-plan.md`.

For AI-specific readiness (prompting, AI tooling, AI governance), route to `/career-transitions` (AI Readiness Assessment) instead of building a general plan; it holds the specialised roadmaps.
