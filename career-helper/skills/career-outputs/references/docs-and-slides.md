# Docs and Slides

**Purpose:** Which Career Helper outputs become Claude Docs, which become slide decks, and the conventions each follows, so that the user gets a document they can edit, print, and export, or a deck they can present, in the same shape every time.

**Applies to:** Every skill that hands finished writing to `career-outputs`.

---

## Which Surface

| Use a Claude Doc when | Use a slide deck when | Keep it in markdown when |
|:----------------------|:----------------------|:-------------------------|
| The user will keep editing it, annotate it, print it, or send it as Word or PDF | The user will present it to people | It is a working file other skills read (tracker snapshot, master facts, preferences, learnings), or a CV or cover letter on its way to the verified PDF |

Always offer the Doc or deck; do not create one the user has not agreed to. If they prefer markdown in the workspace, that is fine.

---

## Claude Docs

| Output | Owning skill | Doc title |
|:-------|:-------------|:----------|
| Interview prep pack | `/interview-master` | `Interview Pack: {{ROLE}} at {{ORGANISATION}}` |
| Post-interview debrief | `/interview-master` | `Interview Debrief: {{ROLE}} at {{ORGANISATION}}` |
| Referee briefing | `/interview-master` | `Referee Briefing: {{ROLE}}` |
| Board AI paper, change-readiness report, risk register entry | `/ned-ai-helper` | `{{ORGANISATION}} AI Paper: {{TOPIC}}` |
| Personal brand foundation and bio library | `/personal-brand` | `Personal Brand` and `Bio Library` |
| Three-month plan | `/career-navigator` | `Three-Month Career Plan` |
| Offer evaluation and negotiation strategy | `/career-navigator` | `Offer Evaluation: {{ORGANISATION}}` and `Negotiation Strategy: {{ORGANISATION}}` |
| Learning plan | `/skills-radar` | `Learning Plan` |
| Portfolio and fractional career strategy | `/career-transitions` | `Portfolio Career Plan` |
| Non-linear career exploration | `/career-transitions` | `Non-Linear Career Plan` |
| AI impact assessment | `/ai-impact-assessment` | `AI Impact Assessment: {{ROLE}}` |
| Getting the best from Career Helper | `/getting-started` | `Getting the Best from Career Helper` |
| CV or cover letter draft (optional) | `/application-optimiser` | `CV Draft: {{ROLE}} at {{ORGANISATION}}` |

### Conventions

1. **Keep the owning template's headings,** in the same order, so the Doc matches the markdown version and other skills can find each section.
2. **Placeholders stay visible.** Where the user's information is missing, keep the `[BRACKETED]` placeholder; never fill it with an invented value.
3. **Front matter line.** Under the title: the date and "Prepared with Career Helper".
4. **One Doc per thing.** Update the existing Doc (found through the register) when the same output is refreshed, for example the interview pack after a new round is announced.
5. **Exports.** Tell the user once that a Doc can be downloaded as Word, PDF, or Markdown from the Doc itself.
6. **CVs and cover letters are different.** A Doc is a good place to draft and discuss a CV, but the file the user submits must still be produced and checked by the verified PDF process in `/application-optimiser` (or exported to Word and checked against the markdown), because applicant tracking systems need a plain, parseable file.
7. **Legal and financial content** keeps its "not advice" line at the top of the Doc.

---

## Slide Decks

| Output | Owning skill | Deck title |
|:-------|:-------------|:-----------|
| Board AI briefing | `/ned-ai-helper` | `{{ORGANISATION}} Board AI Briefing` |
| Interview presentation (case study, first-90-days plan, or set topic) | `/interview-master` | `{{TOPIC}}: {{ORGANISATION}} Interview` |

### Conventions

1. **Start from Claude's Slides artifact type** and use the user's default design system when one is set; otherwise choose a plain, high-contrast look.
2. **One idea per slide,** with a headline that states the point ("Three risks need a named owner"), not a topic label ("Risks").
3. **Speaker notes carry the detail.** Keep slides to a few short lines; put the evidence and wording in the notes.
4. **Every figure has a source** in the notes, or on the slide for anything contested.
5. **Accessible by default:** text labels on every chart and status, no meaning carried by colour alone, at least 24-point body text, and plain sans-serif type. With `dyslexia_friendly: true`, fewer words per slide and no full-width paragraphs.
6. **Timing.** For interview presentations, ask how long the slot is and size the deck to it (roughly one slide per two minutes), with a closing slide that invites questions.
7. **Downloads.** Tell the user once that the deck can be downloaded as PowerPoint or PDF.
8. **Never invent results.** Interview presentations use only achievements and figures the user has confirmed (from `master-facts.md` where it exists).

---

*Docs and Slides | Career Helper Plugin | Prosper AI Consulting, UK*
