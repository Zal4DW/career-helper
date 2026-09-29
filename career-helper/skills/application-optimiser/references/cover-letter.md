# Cover Letter and Supporting Statement

**Purpose:** Draft a cover letter, supporting statement, or short application message that is specific, honest, and traceable to verified content. A cover letter earns its place by saying what the CV cannot: why this role, why this organisation, and why now.

**Applies to:** All cover letter, supporting statement, and application message output produced by application-optimiser.

---

## Before You Draft: Load the Guardrails

A cover letter is more prone to invention than a CV, because it invites narrative. Load the guardrails first.

**Load:** @references/verified-content-guardrails.md

The Iron Rule applies in full: never invent, extrapolate, or infer details about work history, achievements, metrics, scope, or motivation. If you cannot cite the source, do not write it. A shorter, honest letter beats a longer, embellished one.

Motivation is the one area unique to a cover letter. Do not invent reasons the user cares about the organisation. Ask them. "What specifically drew you to this role?" is a better question than guessing from the careers page.

---

## What You Need

1. **The job description.** Source for what the role values and the language to mirror.
2. **The user's current CV or master facts file.** Source for every claim about their experience.
3. **A research brief if one exists** (`applications/{role-slug}/research-brief.md`). Source for what is true about the organisation. If none exists, offer to run Company Research first, or work from what the user can tell you.
4. **The user's own words on motivation.** Ask why this role and this organisation matter to them. Do not supply the answer.

If the research brief and CV both exist in the application folder, read them before asking the user anything.

---

## Choose the Right Format

Ask which format the application requires. Do not assume a traditional letter; many applications want something else.

| Format | When to Use | Length |
|:-------|:------------|:-------|
| Full cover letter | Traditional application, attached as a separate document | One page, roughly 250 to 400 words |
| Supporting statement | Public sector, charity, NHS, academia, or any competency-based application | As specified by the application, often 500 to 1,000 words against listed criteria |
| Short application message | Email body, LinkedIn Easy Apply, or "anything else to add" boxes | 120 to 200 words |

The structures below differ. Confirm the format before drafting.

---

## Structure: Full Cover Letter

Four short paragraphs. Every claim traces to the CV, master facts, or the user's stated motivation.

1. **The opening.** State the role you are applying for and one specific, genuine reason you are drawn to this organisation. The reason must come from the user or the research brief, not from invention. Avoid generic flattery ("I have long admired your work"). Name something concrete.
2. **Evidence paragraph one.** The single most relevant qualification, told as a brief, verified example. Mirror the language of the job description where the underlying fact genuinely matches. Do not stretch a fact to fit a keyword.
3. **Evidence paragraph two.** A second relevant strength, ideally addressing a different requirement from the first. Quantify only with numbers that appear in the source.
4. **The close.** Why this organisation specifically, tied to the user's own goals or values, and a short, confident call to action. No grovelling, no presumption.

---

## Structure: Supporting Statement

Competency-based applications score each criterion. Structure the statement to make scoring easy.

1. Address each essential criterion in the order the application lists them.
2. Use a clear heading or lead sentence per criterion so the assessor can find the evidence.
3. Answer each with a verified STAR example (Situation, Task, Action, Result). Pull these from the CV, master facts, or interview-prep stories if they already exist.
4. Cover desirable criteria briefly after the essential ones.
5. Do not pad. Assessors mark against the criteria, not against length or eloquence.

---

## Structure: Short Application Message

Three to four sentences.

1. The role and one specific reason for interest.
2. The single strongest verified qualification.
3. A short, direct close.

---

## Tone

- **Match the organisation.** A charity, a bank, and a startup expect different registers. Use the research brief and the job description to calibrate. When in doubt, lean professional and warm rather than casual.
- **Second person is for your coaching to the user, not the letter.** The letter itself is written in the user's first-person voice ("I led", "I am drawn to").
- **No hyperbole.** Avoid "passionate", "world-class", "thrilled", and "perfect fit" unless the user genuinely uses that language and means it. Specific beats effusive.
- **No em dashes.** Use commas, semicolons, colons, or full stops.
- **UK English** unless the role explicitly targets a US audience.

---

## Overqualification and Career Change

The cover letter is the right place to address a concern the CV raises but cannot explain.

- **Overqualified or flight-risk framing.** If the user's experience sits above the role, name the genuine reason they want it (a deliberate step back, a sector move, a values-led choice) in their own words. Do not invent a reason. If the user has no honest answer, that is worth a frank conversation: see the Coaching Voice section in `/career-navigator`.
- **Career change or gap.** Frame the transition honestly and briefly. State the transferable evidence; do not over-explain or apologise.

---

## What Belongs in the Cover Letter, Not the CV

- Motivation and fit that a list of achievements cannot convey.
- A short, honest explanation for a gap, a pivot, or a relocation.
- Context for an achievement that needs a sentence the CV has no room for.
- Anything the research brief flagged as worth addressing directly (see the "mention in a cover letter rather than the CV" note in ATS-Helper).

Do not repeat the CV. The letter complements it.

---

## Reflective Validation Before Delivery

After drafting, run the same self-review the CV work uses.

**Load:** @references/reflect-validate.md

Then answer:

1. Can every substantive claim be traced to the CV, master facts, research brief, or a stated motivation?
2. Is the motivation the user's own, or did you supply it?
3. Have you mirrored job-description language only where the underlying fact genuinely matches?
4. Is it the right length for the format?
5. Are there any invented adjectives, metrics, or reasons? Remove or verify them.

If any answer is unsafe, fix it before presenting.

---

## Output

**File:** `applications/{role-slug}/cover-letter.md`

If the application requires a supporting statement, save as `applications/{role-slug}/supporting-statement.md`. If a short message, present it in conversation and offer to save.

**Load template:** @references/cover-letter-template.md

---

*Cover Letter and Supporting Statement v1.0 | Career Helper Plugin | Prosper AI Consulting, UK*
