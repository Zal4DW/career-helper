# Contributing to Career Helper

Thank you for considering a contribution. This guide explains what belongs in the repo, how to propose changes, and the house style we use across skills and agents.

Every contribution — pull request, issue, prompt, framework, bug fix — is welcome, and every contributor is credited in [CONTRIBUTORS.md](../CONTRIBUTORS.md).

---

## What Belongs in This Repo

Career Helper is a Claude Code plugin. The useful contributions look like:

- **New skills** — a new capability that fits alongside the existing 11 skills (e.g., a new persona, a new ceremony, a new type of research). Propose as an issue first so we can discuss scope.
- **New references inside existing skills** — most changes belong here. A new prompt, framework, or template that strengthens one of the existing skills (e.g., `verified-content-guardrails.md` inside application-optimiser).
- **Refinements to existing skills** — clearer prompts, better examples, improved routing logic, tighter coaching tone.
- **Bug fixes** — if something is broken, please file an issue with reproduction steps.
- **Documentation improvements** — README, skill docs, examples.

## What Does NOT Belong in This Repo

- **Personal CVs, cover letters, or any file containing real personal data.** If you want to contribute a template, use `{{VARIABLE}}` placeholders and name the file clearly as a template (e.g., `cv-template-senior-leader.md`).
- **Monolithic instruction dumps at the repo root.** Extracted value should be integrated into the existing skill architecture (`career-helper/skills/*/references/` or `career-helper/agents/`), not dropped as a loose file.
- **Third-party secrets or credentials** of any kind.
- **Content that is substantively the same as existing references.** Before adding a new file, check whether your idea can be merged into an existing one.

If you are unsure where something belongs, open an issue and ask.

---

## Contribution Process

1. **Open an issue first** for anything more substantial than a typo fix. This lets us discuss scope, avoid duplicate effort, and agree on where the change fits.
2. **Fork the repository** and create a branch: `feature/short-description` or `fix/short-description`.
3. **Make your changes** following the house style (below).
4. **Open a pull request** against `main`. Describe the change, link to the issue, and explain what you tested.
5. **Respond to review.** We aim to review within a week. The maintainer may suggest refactoring, splitting, or integrating your change into existing files rather than accepting it as a standalone addition — this is normal and not a rejection of the contribution.
6. **Get credited.** Once merged, you'll be added to [CONTRIBUTORS.md](../CONTRIBUTORS.md) with a summary of what you contributed.

**For larger contributions** (new skills, substantial refactors): expect a round or two of review. We care a lot about consistency across the plugin, so we may ask for changes that align your contribution with the rest of the codebase.

---

## House Style

### Language

- **UK English throughout** — organisation, colour, optimise, analyse, centre, programme. US English is acceptable only when a specific skill explicitly targets a US audience.
- **Oxford comma** — "skills, experience, and qualifications".
- **No em dashes** — use commas, semicolons, colons, or full stops instead.
- **No emojis** — this includes emoji-style markers in skill content (no ✅, ❌, ⚠️). Use plain text labels instead.
- **No hyperbole** — avoid "game-changing", "revolutionary", "supercharge". Plain, honest language only.
- **Second person** for coaching and user-facing content — "your CV", not "the user's CV".

### Content Integrity

- **Never invent user data.** Templates must use clearly-marked placeholders (`{{LIKE_THIS}}` or `[BRACKETED]`).
- **Cite sources for factual claims.** Research skills require source URLs and access dates. Coaching skills must trace advice to verified user context.
- **Prefer specificity over generics.** "Grew weekly newsletter from 40k to 180k" beats "grew newsletter significantly".

### File Organisation

- **Skills** live under `career-helper/skills/{skill-name}/` with a `SKILL.md` and a `references/` folder.
- **Agents** live under `career-helper/agents/`.
- **Commands** live under `career-helper/commands/`.
- **References** are loaded with `@references/filename.md` from within the owning skill.
- **New references should be purposeful.** Avoid creating a file that gets loaded once and never referenced again.

### Skill Content Conventions

- Every skill's `SKILL.md` starts with YAML frontmatter: `name`, `description`, `tags`.
- Each skill should have an Accessibility section that checks for `career-helper-preferences.md`.
- Each skill should have a Tone of Voice subsection within Output Standards.
- Skills that produce user-facing documents must respect the **no em dashes, no emojis, Oxford comma** rules in their output as well as in their prompts.

---

## Versioning

Career Helper follows [Semantic Versioning](https://semver.org/):

- **Patch** (1.9.0 → 1.9.1): bug fixes, typo corrections, small refinements that don't change behaviour.
- **Minor** (1.9.0 → 1.10.0): new skills, new references, new capabilities, additive behaviour changes.
- **Major** (1.x → 2.0): breaking changes to skill interfaces, file structure, or plugin behaviour.

Version is bumped in two places:
- `career-helper/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`

The maintainer handles version bumps during merge unless the contribution is a maintainer-driven release.

## Changelog

All user-facing changes are recorded in [CHANGELOG.md](../CHANGELOG.md) following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The maintainer will add your contribution to the next release entry on merge.

---

## Code of Conduct

Be kind, be direct, and assume good intent. Criticism of ideas is welcome; criticism of people is not.

If you experience or witness unacceptable behaviour, contact the maintainer directly via the email on the GitHub profile.

---

## Questions

Not sure whether something is worth contributing, where it fits, or how to structure it? Open a GitHub issue and ask. It's always better to check first than to write something that needs significant rework.

Thank you for making Career Helper better.

---

*Career Helper Plugin | Prosper AI Consulting, UK*
