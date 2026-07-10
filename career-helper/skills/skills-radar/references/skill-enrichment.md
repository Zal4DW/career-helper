# Skills Inventory Enrichment

**Purpose:** Build a complete, evidenced picture of what the user can do, including the skills their CV never mentions. Most CVs undersell; the enrichment pass finds the difference between what the user claims and what their work demonstrates.

---

## Consent First

Before examining any public source:

1. Ask the user which sources are theirs and which they want included. Suggested prompts: GitHub or GitLab profile, portfolio site, personal blog, publications or conference talks, Kaggle or similar competition profiles, Google Scholar, course certificates, App Store or marketplace listings, open-source contributions.
2. Only examine what the user confirms. Do not search for accounts that might be theirs; if the user wants to know what an employer could find uninvited, that is `/employer-footprint`.
3. Everything examined must be public. Never ask for credentials to access private work; ask the user to describe private work instead, and record it as user-described evidence.

---

## Layer 1: Stated Skills

Parse the CV and LinkedIn profile:

1. List every skill claimed, explicitly (skills section) or implicitly (verbs in experience bullets).
2. For each, find the supporting evidence within the CV itself: a bullet with a concrete outcome counts; a bare word in a skills list does not.
3. Mark bare claims as `claimed, unevidenced` for now; later layers may evidence them.

---

## Layer 2: Implicit Skills from Public Work

Work through each confirmed source. For every source, extract concrete, checkable evidence; quote or link it.

**Code repositories (GitHub, GitLab):**
- Languages and frameworks actually used, weighted by recency and depth (a maintained project beats a fork; tests, CI configuration, and documentation are themselves evidence of engineering practice).
- README quality evidences written communication. Issue and PR history evidences collaboration and review. Release history evidences shipping.
- Do not credit starred or forked repositories with no user commits.

**Portfolio sites and case studies:**
- Named tools, methods, and outcomes per project.
- Design, writing, and presentation quality as evidence in their own right.

**Publications, talks, and teaching:**
- Domain expertise, research methods, and public speaking.
- Peer-reviewed work, invited talks, and course syllabi the user has taught from are strong evidence.

**Competitions, certifications, and courses:**
- A certificate alone is weak evidence; a certificate plus produced work (a capstone, a notebook, a project) is solid. Record which it is.

**Volunteering, community, and side roles:**
- Treasurer, trustee, organiser, moderator: these evidence budgeting, governance, event delivery, and community management. Users forget these constantly; ask.

**Cross-reference with Layer 1:** every implicit skill found is either new (the CV never mentions it) or corroborating (it evidences a bare claim). Both matter; label which.

---

## Layer 3: Transferable Skills

Take evidenced skills from one context and name their value in the target market's language:

- Ran incident response rotas: operational leadership under pressure.
- Taught a course: structured communication and curriculum design.
- Managed a community project's contributors: distributed team leadership without authority.

Rules: the underlying evidence must already exist in Layer 1 or 2; the translation must be defensible in an interview follow-up ("tell me more about that"), or it does not go in.

---

## Grading

Every inventory entry gets an Evidenced level with its evidence named:

| Level | Meaning |
|:------|:--------|
| Strong | Multiple recent, substantial pieces of evidence; could discuss in depth without preparation |
| Solid | Clear evidence, but dated, narrow, or secondhand (one project, one context) |
| Working | Genuine but limited exposure; honest to claim as developing, dishonest to claim as expertise |
| Claimed, unevidenced | Asserted but not demonstrated anywhere available; the user must evidence it or drop it |

Grade against the evidence, not against the user's self-assessment in either direction. Users under-grade as often as they over-grade.

---

## Output

Load `@references/skills-inventory-template.md` and save to `skills-inventory.md`.

Present the findings in this order:

1. **The undersold skills**: implicit skills the CV never mentions, with evidence. This is the headline; lead with it.
2. **Corroborated claims**: bare CV claims now backed by found evidence.
3. **The full inventory** by category.
4. **Unevidenced claims**: what the user asserts but nothing shows, with the choice stated plainly: evidence it (there may be a quick way) or stop claiming it.

Then offer the natural next steps: a CV rewrite via `/application-optimiser` to surface the undersold skills, or a gap analysis against a target role.
