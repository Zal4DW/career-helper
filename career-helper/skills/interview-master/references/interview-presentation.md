# Interview Presentation

**Purpose:** Help you build and rehearse a presentation for an interview (a case study, a first-90-days plan, or a set topic), as a slide deck in your Claude account that you can present from or download.

**Applies to:** Capability 6 of interview-master. The deck is created through `/career-outputs` following `@../career-outputs/references/docs-and-slides.md`.

---

## Principles

1. **Answer the brief they set.** Read the exact wording of the task. If it asks for "your approach in the first 90 days", the deck is a plan, not a career history.
2. **Only confirmed facts about you.** Achievements, figures, and examples come from what you have told us, your CV, or `master-facts.md`. Never invent a result to make a slide land.
3. **Only sourced facts about them.** Claims about the organisation come from the research brief or a dated public source, cited in the speaker notes.
4. **Fit the slot.** Ask how long you have. Roughly one slide per two minutes, plus a title slide and a closing slide that invites questions.
5. **It is a conversation starter.** Panels judge thinking and judgement more than polish. Show your reasoning and your assumptions openly.

---

## What to Gather

Ask for, one at a time if dyslexia-friendly mode is on:

1. The exact brief, word for word, and any format rules (slide limit, template, handouts).
2. The time allowed for presenting and for questions.
3. Who is on the panel, if known (the research brief or networking intelligence may already hold this).
4. The two or three things you most want the panel to remember about you.

Then read, where they exist: `applications/{role-slug}/research-brief.md`, `interview-prep.md` (the competency map and top risks), the optimised CV, and `master-facts.md`.

---

## Building the Deck

1. **Structure first.** Propose the slide headlines as a numbered list and agree them before writing any slide. A typical shape:
   - Title: the topic in the panel's own words, your name, the date
   - What I understood the brief to be (and any assumptions)
   - The situation as I see it (from public sources)
   - Two or three priorities, one slide each, each tied to a competency on the competency map
   - How I would measure progress
   - Risks and what I would check first
   - Close: what I would want to learn from you; questions
2. **Headlines state the point.** "Retention is the quickest win" rather than "Retention".
3. **Few words on the slide, the detail in the notes.** The notes carry what you will say and the source for every figure.
4. **Tie back to the competencies.** Each priority slide should give the panel evidence for at least one High-likelihood competency from the interview prep.
5. **Create the deck** through `/career-outputs` with the title `{{TOPIC}}: {{ORGANISATION}} Interview`, using your default design system if you have one, otherwise a plain, high-contrast look.

---

## Rehearsal

Once the deck exists, offer a rehearsal:

1. You present (typing or speaking each slide's message); I time it against the slot.
2. I ask three to five questions the panel is likely to ask, drawn from the deck's assumptions and the top risks in your interview prep.
3. Feedback in three lines: what landed, what to cut, and one question to prepare better.

---

## Accessibility

- **dyslexia_friendly: true:** agree the structure one slide at a time; keep slide text to a few short lines; give rehearsal feedback as numbered points.
- **colour_blind: true:** every chart and status on a slide carries a text label; never rely on colour alone.

---

## Output

**Deck:** `{{TOPIC}}: {{ORGANISATION}} Interview`, in your Claude account, recorded in `career-helper-artefacts.md`; downloadable as PowerPoint or PDF.

---

*Interview Presentation v1.0 | Career Helper Plugin | Prosper AI Consulting, UK*
