# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions that extend agent capabilities with domain-specific knowledge and best practices.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

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

## Installation

```bash
npx add-skill sceiler/skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Key triggers:**

- Keywords like "just", "only", "simple" → scope discipline rules activate
- Repeated issues → root cause analysis rules activate
- Framework-specific code → version checking rules activate

## Skill Structure

Each skill contains:

- `SKILL.md` - Instructions for the agent
- `metadata.json` - Skill metadata

## License

MIT
