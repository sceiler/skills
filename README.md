# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions that extend agent capabilities with domain-specific knowledge and best practices.

Skills follow the [Agent Skills](https://agentskills.io/) format and are listed on the [Agent Skills Directory](https://skills.sh/).

## Available Skills

### vercel-brand-guidelines

Opt-in Vercel brand and visual-language guidance for application UI, product surfaces, reports, calculators, and other frontend work. It reads Vercel's live design skill for every task instead of freezing its rules in this repository.

**Use when:**

- Building, redesigning, or reviewing frontend applications with Vercel as the default visual direction
- Adapting Tailwind, shadcn, starter templates, or generic component libraries to Vercel's visual language
- Creating official Vercel-authored reports or decision surfaces that use the published report foundation
- Validating responsive behavior, themes, hierarchy, interaction, and accessibility against current Vercel guidance

The skill makes Vercel's design direction the default only when it is installed or explicitly selected. It keeps report-only classes and authorship assets out of ordinary product UI and does not add Vercel logos unless official authorship is requested.

---

### vercel-ai-stack

Documentation-first workflow for building, reviewing, configuring, deploying, and validating applications across the Vercel AI stack. It routes agents to current nested documentation and version-matched local sources instead of relying on stale model knowledge.

**Use when:**

- Working with Next.js, AI SDK, AI Gateway, Workflow SDK, Vercel Connect, Eve, Vercel Sandbox, or agent-browser
- Deploying or configuring applications through Vercel CLI or the REST API
- Testing local, preview, or production frontends
- Accessing protected Vercel deployments in automated or browser-based checks
- A task involves only one of these products as well as when several are combined

The skill prefers Eve for new AI agents, uses `agent-browser` for manual frontend validation, and discovers the exact current guides and API references needed for each task.

---

### refine

Repository-agnostic branch-finishing workflow. Use `refine` when you want an agent to review the current branch, fix gaps, run the project's own verification, and ship it through commit, push, and PR update.

**Use when:**

- A branch is in progress and needs to be brought to review-ready quality
- You want review, project-native checks, tests, docs, and PR handling done in one pass
- You want the agent to fix issues, not only report them
- You want the branch committed, pushed, and synced with a PR

**Can use these companion skills when available:**

| Skill | Source | Install |
|-------|--------|---------|
| `next-best-practices` | [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) | `npx skills add vercel-labs/next-skills --skill next-best-practices` |
| `next-cache-components` | [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) | `npx skills add vercel-labs/next-skills --skill next-cache-components` |
| `vercel-react-best-practices` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill react-best-practices` |
| `vercel-composition-patterns` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill composition-patterns` |
| `vercel-react-native-skills` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill react-native-guidelines` |
| `web-design-guidelines` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` |

See [`skills/refine/SKILL.md`](skills/refine/SKILL.md) for the full branch-finishing workflow.

---

### agent-best-practices

Evidence-based engineering principles for repository awareness, proportionate verification, scope and authorization discipline, root-cause analysis, regression prevention, current documentation, security, and safe workflows.

**Use when:**

- Writing any new code
- Making changes to existing code
- Debugging issues
- Reviewing code quality
- Before committing changes
- Working with AI coding assistants

**Categories covered:**

- Repository and runtime context
- Proportionate verification
- Scope and authorization discipline
- Root-cause analysis
- Regression prevention
- Responsible clarification
- Current, version-matched sources
- Simple and measurable quality
- Safe git and automation workflows
- Security boundaries
- Clear collaboration

**Core philosophy:** Never assume. Always verify.

---

## Installation

Install all skills from this repo:

```bash
npx skills add sceiler/skills
```

Install only the shareable Vercel AI stack skill:

```bash
npx skills add sceiler/skills --skill vercel-ai-stack
```

Install the independent Vercel brand skill:

```bash
npx skills add sceiler/skills --skill vercel-brand-guidelines
```

## Related Skill Repositories

| Repository | Description |
|------------|-------------|
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel's official skills — React best practices, web design guidelines, composition patterns, React Native, deploy |
| [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) | Next.js skills — best practices, cache components, upgrade guides |

Browse more skills at [skills.sh](https://skills.sh/).

## Skill Structure

Each skill contains:

- `SKILL.md` — Instructions for the agent (required)
- `metadata.json` — Skill metadata (required)
- `references/` — Detailed guidance loaded only when needed (optional)
- `scripts/` — Deterministic helpers for repeated or fragile work (optional)
- `assets/` — Templates or resources used in generated output (optional)

## License

[MIT](LICENSE)
