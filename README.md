# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions that extend agent capabilities with domain-specific knowledge and best practices.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### software-engineering-fundamentals

Core software engineering principles that every coding agent should follow. Contains essential rules covering testing, verification, error handling, code quality, and professional development practices.

**Use when:**
- Writing any new code
- Making changes to existing code
- Debugging issues
- Reviewing code quality
- Before committing changes

**Categories covered:**
- Testing & Verification (Critical)
- Error Handling (High)
- Code Quality (High)
- Change Management (Medium)
- Security Awareness (Medium)

## Installation

```bash
npx add-skill sceiler/skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `metadata.json` - Skill metadata

## License

MIT
