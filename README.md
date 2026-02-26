# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions that extend agent capabilities with domain-specific knowledge and best practices.

Skills follow the [Agent Skills](https://agentskills.io/) format and are listed on the [Agent Skills Directory](https://skills.sh/).

## Available Skills

### refine

One-command codebase audit. Type `/refine` to run a single evaluation pass that invokes every applicable skill in the session and produces a prioritized table of performance, UI, UX, and accessibility improvements.

**Use when:**

- You want a quick health check of your application
- Before a release, to catch low-hanging fruit
- After a major feature lands, to spot regressions
- You want a prioritized backlog of improvements

**Works best with these companion skills installed:**

| Skill | Source | Install |
|-------|--------|---------|
| `next-best-practices` | [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) | `npx skills add vercel-labs/next-skills --skill next-best-practices` |
| `next-cache-components` | [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) | `npx skills add vercel-labs/next-skills --skill next-cache-components` |
| `vercel-react-best-practices` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill react-best-practices` |
| `vercel-composition-patterns` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill composition-patterns` |
| `vercel-react-native-skills` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill react-native-guidelines` |
| `web-design-guidelines` | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` |

See [`skills/refine/`](skills/refine/) for full details.

---

### agent-best-practices

Field-tested engineering principles. Contains 40+ rules across 12 categories, distilled from real project experience and hundreds of debugging sessions.

**Use when:**

- Writing any new code
- Making changes to existing code
- Debugging issues
- Reviewing code quality
- Before committing changes
- Working with AI coding assistants

**Categories covered:**

- Verification & Testing (Critical)
- Scope Discipline (Critical)
- Root Cause Analysis (High)
- Regression Prevention (High)
- Clarification Over Assumption (High)
- Staying Current (High)
- Simplicity & Performance (Medium)
- Quality Over Quantity (Medium)
- Workflow & Automation (Medium)
- Backward Compatibility (Medium)
- Security Awareness (Medium)
- AI Collaboration Principles (Medium)

**Core philosophy:** Never assume. Always verify.

---

### common-mistakes

Concrete wrong/correct examples of common AI coding agent mistakes. Derived from analysis of 500+ real chat sessions across 21 projects. Contains 25+ rules across 8 categories.

**Use when:**

- Writing code or modifying files
- Debugging issues
- Generating output
- Reviewing AI-generated code

**Categories covered:**

- File & Project Awareness (Critical)
- Multi-Target Instructions (High)
- Deprecated APIs (High)
- Output Formatting (Medium)
- Debugging Anti-Patterns (Medium)
- Wrong Optimizations (Medium)
- Content Integrity (Medium)
- Security Scope (Medium)

Complements `agent-best-practices` (principles) with specific, actionable anti-patterns.

## Installation

Install all skills from this repo:

```bash
npx skills add sceiler/skills
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
- `README.md` — Human-readable documentation (optional)

## License

MIT
