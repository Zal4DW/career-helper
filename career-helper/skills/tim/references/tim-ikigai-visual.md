# Ikigai Visual Map

An optional, interactive ikigai diagram Tim can offer after the four direction-finding questions (see `tim-ikigai-guide.md`). It turns the user's four answers into the classic four-circle ikigai map, kept in their Claude account, where they can revisit and edit it.

This is offered, never imposed. The plain-text grid in the ikigai guide remains the default; the visual is an extra for people who find a diagram helpful.

---

## When to Offer

After you have summarised the four answers and looked for overlaps, offer the visual:

"Would you like me to turn this into the classic ikigai diagram, an interactive page in your Claude account that you can keep, edit, and come back to?"

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

The map is an interactive page in the user's Claude account, published through `/career-outputs` (Capability 1). The page holds no user data; the answers live in one database document, so the user can edit any region on the page and Claude reads it back later.

1. **Look it up** in `career-helper-artefacts.md`, then by the title `Career Helper Ikigai`. Refresh the existing map rather than publishing a second one.
2. **New map:** publish @references/ikigai-map-template.html unchanged, with capabilities `{"db": {}, "user": {}}`.
3. **Write the answers** to the document `ikigai/map` with these fields, each in the user's own words (or an empty string when genuinely unknown): `owner`, `date` (`YYYY-MM-DD`), `love`, `goodAt`, `needs`, `paid`, `passion`, `mission`, `profession`, `vocation`, `ikigai`, plus `updated` and `updatedBy: "claude"`.
4. **Check once:** read the document back.
5. **Tell the user** the map is in their Claude account, that any region can be edited there, and that an empty region is theirs to fill in.

**Reading it back.** When the user returns to direction-finding, read `ikigai/map` first. Fields with `updatedBy: "board"` changed since you last read it are the user's own edits: acknowledge them and work from them.

The page renders every value as plain text and needs no escaping.

---

## Accessibility (Required)

A colour-coded diagram must never depend on colour alone (house style, and the colour-blind preference). The template already does the following; preserve all of it:

- A **colour-blind-safe palette** (Okabe-Ito) for the four circles, in light and dark themes.
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

**Artifact:** `Career Helper Ikigai`, recorded in `career-helper-artefacts.md`

A markdown alternative: if the user would rather not have a page, offer the text-equivalent table on its own as `ikigai-map.md` instead.

---

*Ikigai Visual Map v2.0 | Career Helper Plugin | Prosper AI Consulting, UK*
