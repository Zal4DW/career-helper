---
name: career-outputs
description: Use when another Career Helper skill hands over an output to show as an interactive page, dashboard, Claude Doc, or slide deck, or when the user asks to open, find, refresh, or share one of those, such as "show my application board", "open my market map", "where is my ikigai map", or "turn my interview pack into a doc". Publishes the boards, the ikigai map, the progress and footprint dashboards, Docs, and Slides the same way every time, and keeps a register of their links.
tags: artifacts, dashboards, docs, slides, boards, publishing, outputs, cowork
---

# Career Outputs

One place that decides how Career Helper shows its work in Claude: which outputs become interactive pages, which become dashboards, which become Claude Docs or slide decks, how each is published, where its data lives, and how you find it again. Other skills call on this one rather than describing rendering themselves, so every board and document behaves the same.

## Capabilities

| # | Capability | When to Use |
|:--|:-----------|:------------|
| 1 | Publish or Refresh an Interactive Page | The application board, the market map board, or the ikigai map |
| 2 | Publish or Refresh a Dashboard | The progress dashboard (status and weekly update) and the employer footprint dashboard |
| 3 | Create a Claude Doc or Slide Deck | Interview packs, board papers, plans, brand work, the getting-the-best guide, and presentations |
| 4 | Find, Open, or Share an Output | "Where is my board?", "send my market map to my mentor", "my board link is broken" |

## Quick Start

```text
"Show me my application board"
"Open my market map"
"Turn my interview pack into a doc I can print"
"Make slides for my board AI briefing"
"Where did my ikigai map go?"
```

---

## Accessibility

**At skill start**, check for `career-helper-preferences.md` in the current working directory using the Glob tool. If found, read the YAML frontmatter and apply:

- **dyslexia_friendly: true**: Use short sentences. Number all lists and options (never unnumbered). One decision per message. No idioms or metaphors; use plain replacements. Explicit signposting at every transition. Refer to outputs by what they are ("your application board"), not by link or file name. In Docs and Slides, use short paragraphs, numbered lists, and generous headings.
- **colour_blind: true**: Never use colour alone to convey meaning. Every status, priority, and score carries a text label. The page templates already do this; keep it so in dashboards and slides.

If **no preferences file exists** and this skill was invoked directly (not dispatched by Tim or another skill): ask once, "Do you have any accessibility preferences I should know about? For example, if you're dyslexic, I can adjust how I format things." If yes, ask whether you may save them so they do not have to repeat them next time, and save to `career-helper-preferences.md` using the format in @../tim/references/tim-preferences-format.md only if they agree. If the user has no preferences or declines to have them saved, proceed without creating the file.

These rules apply to **all communication with the user** and to the **formatting of every output**.

---

## How Outputs Work Here

Career Helper runs in Claude Cowork, which can publish artifacts: private pages in your Claude account. Some pages keep their own data in a small database that both you (on the page) and Claude (in any later session, including a scheduled one) can read and change. That is what lets the application board and the market map stay current without copying anything back and forth.

**Load:** @references/publishing-rules.md before publishing anything. It holds the rules every output follows: titles, privacy, one link per output, page versions, seeding and reading data, and the register.

| Output | Surface | Owning skill | Record lives in |
|:-------|:--------|:-------------|:----------------|
| Application board | Interactive page with database | `/career-navigator` | The board's database (the record) |
| Market map | Interactive page with database | `/market-mapper` | The board's database (the record) |
| Ikigai map | Interactive page with database | `/tim` | The page's database |
| Progress dashboard | Dashboard artifact | `/career-helper:status`, `/career-helper:weekly-update` | Read from the boards and workspace files |
| Employer footprint dashboard | Dashboard artifact | `/employer-footprint` | The dashboard's data file |
| Interview prep pack, board papers, plans, brand work, guides | Claude Doc | The skill that wrote it | The Doc |
| Board AI briefing, interview presentations | Slide deck | `/ned-ai-helper`, `/interview-master` | The deck |
| CV and cover letter | Markdown, then verified PDF | `/application-optimiser` | Workspace files (unchanged; ATS parsing comes first) |

---

## 1. Publish or Refresh an Interactive Page

**What you need:** The owning skill's data, already gathered and checked
**Load:** @references/publishing-rules.md, then the owning skill's board reference for its data fields:
- Application board: @../career-navigator/references/kanban-board.md and the page @../career-navigator/references/kanban-board-template.html
- Market map: @../market-mapper/references/market-map-board.md and the page @../market-mapper/references/market-map-board-template.html
- Ikigai map: @../tim/references/tim-ikigai-visual.md and the page @../tim/references/ikigai-map-template.html

1. **Look it up first.** Check the register, then your artifact list for the fixed title. If the page exists, you are refreshing it; never publish a second copy.
2. **Publish the page file unchanged** when it is new, or when its page version is older than the one in the plugin. The page files hold no user data, so there is nothing to fill in or escape.
3. **Write the data** to the page's database with the artifact data tools, as a batch, using the fields the owning skill's reference defines. Never invent a value; leave unknown fields as empty strings.
4. **Check once.** Read the collection back and confirm the count matches what you wrote.
5. **Record it** in the register and give the user one line: what the page shows, and that changes they make there are saved and read back by Claude.

**Output:** One private artifact per page, and an updated register

---

## 2. Publish or Refresh a Dashboard

**What you need:** The numbers or scores, each with a source
**Load:** @references/dashboards.md

Start a new dashboard from Claude's Dashboard artifact type, then follow that type's own instructions for its data files. On later runs, update the same dashboard's data files rather than creating another. Every number shows where it came from, and every status carries a text label.

**Output:** One private dashboard per purpose (progress, footprint), and an updated register

---

## 3. Create a Claude Doc or Slide Deck

**What you need:** The finished content from the owning skill
**Load:** @references/docs-and-slides.md

Docs are for writing you will keep editing, print, or export to Word or PDF. Slides are for something you will present. The owning skill supplies the content and structure (its template's headings); this skill decides the surface and the conventions. Each Doc or deck is recorded in the register so it is updated, not duplicated, next time.

**Output:** A Claude Doc or slide deck in your Claude account, and an updated register

---

## 4. Find, Open, or Share an Output

**What you need:** Nothing
**Load:** @references/publishing-rules.md (Finding and Sharing sections)

1. Check the register, then the artifact list for the fixed titles.
2. Open the one the user wants.
3. If they want to share it, explain what the other person will see and whether they could change anything, then let the user share it from the artifact's share menu themselves. Never share an output on the user's behalf, and never make one public.

---

## Output Standards

- **UK English** throughout, in pages, dashboards, Docs, and slides
- **No emojis**; plain text labels for every status
- **Never invent data**: unknown fields stay empty or `[UNKNOWN]`; every dashboard number has a source
- **Private by default**: nothing is shared or made public unless the user does it
- **One output, one link**: refresh in place; never leave stray copies

### Tone of Voice

- Address the user as "you": "Your board is updated" not "The user's board is updated"
- Avoid hyperbole and cinema poster phrasing (not "stunning dashboard" or "supercharge your search")
- Use the **Oxford comma** (serial comma: "boards, dashboards, and documents")
- Never use em dashes or en dashes. Use commas, semicolons, colons, or full stops instead

### Template Usage

Page files are published exactly as they are in the plugin. Doc and slide content follows the owning skill's template headings so the same sections appear in the same places every time.

---

## Related Skills

- **/career-navigator**: Owns the application board's data
- **/market-mapper**: Owns the market map's data
- **/tim**: Owns the ikigai map
- **/employer-footprint**: Owns the footprint dashboard's scores
- **/interview-master**, **/ned-ai-helper**, **/personal-brand**: Hand over Docs and Slides content
- **/career-routines**: Scheduled runs refresh the boards and the progress dashboard

---

*Career Outputs | Career Helper Plugin | Prosper AI Consulting, UK*
