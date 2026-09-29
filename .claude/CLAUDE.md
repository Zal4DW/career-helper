# Career Helper — Project Instructions for Claude Code

This file gives Claude (and any other AI assistant working in this repo) the house style and conventions to follow when editing skills, agents, references, and documentation.

## House Style — Strict

### Punctuation

- **Never use em dashes (`—`).** Use commas, semicolons, colons, parentheses, or full stops instead. This applies to headings, body text, prompts, and any user-facing output the skills produce.
- **Use the Oxford comma** in lists of three or more (e.g., "skills, experience, and qualifications").
- **Hyphenate compound modifiers** (e.g., "3- to 5-line summary", "high-impact bullet", "ATS-safe formatting").

### Language

- **UK English throughout.** Organisation, colour, behaviour, optimise, analyse, centre, programme, favour, recognise, realise, prioritise, maximise. US English is acceptable only when a specific skill explicitly targets a US audience.
- **No emojis or emoji-style markers.** This includes `✅`, `❌`, `⚠️`, `🔧`, `🤖` and similar. Use plain text labels (PASS / FAIL / WARNING) instead.
- **No hyperbole or marketing fluff.** Avoid "game-changing", "revolutionary", "supercharge", "world-class", "industry-leading", "robust", "comprehensive" unless the source material genuinely warrants them.
- **Second person** for user-facing coaching content. "Your CV" not "the user's CV".

## Content Integrity

- **Never invent user data** in templates or examples. Use clearly-marked placeholders (`{{LIKE_THIS}}` or `[BRACKETED]`).
- **Cite sources** for factual claims in research output. Coaching skills must trace advice to verified user context.
- **Templates must be obviously templates.** Filename should signal it (e.g., `cv-template-senior-leader.md`). Variables use `{{PLACEHOLDER}}` syntax. Never commit real personal data even as an "example".

## File Organisation

- **Skills** live under `career-helper/skills/{skill-name}/` with a `SKILL.md` and a `references/` folder.
- **Agents** live under `career-helper/agents/`.
- **Commands** live under `career-helper/commands/`.
- **References** are loaded with `@references/filename.md` from within the owning skill.
- **Personal data, sample CVs, and one-off documents do not belong in this repo.** If a contributor submits one, the value should be extracted into the existing skill architecture and the original file removed.

## Skill Conventions

- Every `SKILL.md` starts with YAML frontmatter: `name`, `description`, `tags`.
- Each skill should have an Accessibility section that checks for `career-helper-preferences.md`.
- Each skill should have a Tone of Voice subsection within Output Standards.
- Skills must respect the no-em-dash, no-emoji, Oxford comma rules in both their prompts and their output.

## Versioning

Career Helper follows [Semantic Versioning](https://semver.org/):

- **Patch** (1.x.0 → 1.x.1): bug fixes, typos, small refinements.
- **Minor** (1.9 → 1.10): new skills, new references, additive behaviour.
- **Major** (1.x → 2.0): breaking changes.

Version is bumped in **two places**, both must match:
- `career-helper/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`

Every release adds an entry to `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Contributors

Community contributions are credited in `CONTRIBUTORS.md` at the repo root. When merging a substantive contribution, add the contributor's GitHub handle, a one-paragraph summary of what was integrated, and the release version.

## Pull Request Process

See `.github/CONTRIBUTING.md` for the full process. Key points:

- Open an issue first for anything more substantial than a typo fix.
- Branch naming: `feature/short-description`, `fix/short-description`, `refactor/short-description`, `chore/short-description`.
- PRs go against `main`.
- Co-author trailers (`Co-Authored-By:`) on commits to give credit when integrating someone else's work.

## When Editing This File

If you find yourself wanting to add an exception to any of the above rules, that's a signal to stop and check whether the change is really necessary. The point of a strict house style is that future-you (and future contributors) don't have to think about formatting — the rules are the rules. Add new rules here when patterns emerge; do not weaken existing ones casually.
