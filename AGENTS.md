# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

## Repository Overview

A collection of skills for AI coding agents. Skills are packaged instructions that extend agent capabilities with domain-specific knowledge and best practices.

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    metadata.json         # Required: skill metadata
```

### Naming Conventions

- **Skill directory**: `kebab-case` (e.g., `software-engineering-fundamentals`, `code-review`)
- **SKILL.md**: Always uppercase, always this exact filename
- **metadata.json**: Lowercase, contains version and author info

### SKILL.md Format

```markdown
---
name: {skill-name}
description: {One sentence describing when to use this skill}
license: MIT
metadata:
  author: {author}
  version: "1.0.0"
---

# {Skill Title}

{Brief description of what the skill does.}

## When to Apply

{List of scenarios when the skill should be used}

## Rules

{The actual rules and guidelines}
```

### Best Practices for Context Efficiency

Skills are loaded on-demand. To minimize context usage:

- **Keep SKILL.md under 500 lines** - put detailed reference material in separate files
- **Write specific descriptions** - helps the agent know exactly when to activate the skill
- **Use progressive disclosure** - reference supporting files that get read only when needed

### End-User Installation

**Claude Code:**
```bash
npx add-skill {github-user}/skills
```

**Manual:**
```bash
cp -r skills/{skill-name} ~/.claude/skills/
```
