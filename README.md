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

### common-mistakes

Concrete wrong/correct examples of common AI coding agent mistakes. Derived from analysis of 500+ real chat sessions across 21 projects.

**Use when:**

- Writing or modifying any code
- Debugging issues
- Generating formatted output
- Working with file systems (symlinks, project configs)
- Applying optimizations
- Making security-related changes

**Categories covered:**

- File & Project Awareness (Critical)
- Multi-Target Instructions (Critical)
- Deprecated & Outdated APIs (High)
- Output Formatting (High)
- Debugging Anti-Patterns (High)
- Wrong Optimizations (High)
- Content & Data Integrity (Medium)
- Security Scope (Medium)

**Core format:** Each rule provides a concrete wrong example and the correct alternative.

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
- File modifications → symlink and project awareness rules activate
- Debugging sessions → anti-pattern detection rules activate

## Skill Structure

Each skill contains:

- `SKILL.md` - Instructions for the agent
- `metadata.json` - Skill metadata

## License

MIT
