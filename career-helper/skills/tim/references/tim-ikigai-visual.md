# Ikigai Visual Map

An optional, interactive ikigai diagram Tim can offer after the four direction-finding questions (see `tim-ikigai-guide.md`). It turns the user's four answers into the classic four-circle ikigai map they can keep, open in a browser, and revisit.

This is offered, never imposed. The plain-text grid in the ikigai guide remains the default; the visual is an extra for people who find a diagram helpful.

---

## When to Offer

After you have summarised the four answers and looked for overlaps, offer the visual:

"Would you like me to turn this into the classic ikigai diagram, an interactive page you can keep and come back to?"

Offer it only when:
- The user gave real answers to at least three of the four questions, so there is something to render.
- The user is engaged with the exercise (do not offer if they were reluctant or opted out).

If `career-helper-preferences.md` has `direction_questions_declined: true`, do not offer the visual either.

---

## What Gets Rendered

The classic ikigai model has four overlapping circles and their intersections. Populate them from the user's own answers; never invent content.

| Region | Source |
|:-------|:-------|
| What you love | Answer 1 (what you enjoy) |
| What you are good at | Answer 2 (what you are good at) |
| What the world needs | Answer 3 (problems you care about) |
| What you can be paid for | Answer 4 (what pays) |
| Passion (love + good at) | Your synthesis of where answers 1 and 2 overlap |
| Mission (love + world needs) | Your synthesis of where answers 1 and 3 overlap |
| Profession (good at + paid) | Your synthesis of where answers 2 and 4 overlap |
| Vocation (world needs + paid) | Your synthesis of where answers 3 and 4 overlap |
| Ikigai (all four) | The centre, only if a genuine candidate emerged |

Synthesising overlaps from the user's own answers is allowed; this is interpretation, not fabrication. If an overlap or the centre is not clear from what the user said, leave the `{{PLACEHOLDER}}` in place rather than guessing, and tell the user it is theirs to fill in. An honest gap at the centre is useful information; it often points toward career transitions or retraining.

---

## How to Build It

1. Load the template: @references/ikigai-map-template.html
2. Replace every `{{PLACEHOLDER}}` with the user's content, HTML-escaped (or leave it if genuinely unknown). Escape at minimum `&`, `<`, `>`, `"`, and `'` so user text cannot break the markup or inject script.
3. Save the result as `ikigai-map.html` in the workspace root.
4. Tell the user the file is saved and can be opened in any browser. In Claude Cowork it can be opened directly.

The template is a single self-contained HTML file: no external scripts, fonts, or network calls, so it works offline and can be shared as one file.

---

## Accessibility (Required)

A colour-coded diagram must never depend on colour alone (house style, and the colour-blind preference). The template already does the following; preserve all of it:

- A **colour-blind-safe palette** (Okabe-Ito) for the four circles.
- A **text label on every region**, so the meaning is readable without distinguishing colours.
- Hover and keyboard focus both reveal a region's detail, so it works without a mouse.
- A **full text-equivalent table** beneath the diagram listing all four answers and the overlaps, so the page is completely usable if the diagram cannot be seen at all.

If the user has `dyslexia_friendly: true`:
- Lead with the text-equivalent table and tell the user the diagram is below it.
- Keep the content in each region short; move detail into the table.

If the user has `colour_blind: true`:
- No change needed beyond the defaults; the palette and text labels already cover it. Mention that the diagram is labelled, not colour-dependent.

---

## Output

**File:** `ikigai-map.html` (workspace root)

A markdown alternative: if the user cannot use HTML, offer the text-equivalent table on its own as `ikigai-map.md` instead.

---

*Ikigai Visual Map v1.0 | Career Helper Plugin | Prosper AI Consulting, UK*
