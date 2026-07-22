# AGENTS.md

This repository contains reusable skills for AI coding agents. Treat each skill as a compact operating guide that supplies specialized workflow, domain knowledge, or tool usage only when its frontmatter description triggers.

## Creating or Updating a Skill

### Package Structure

```text
skills/
  {skill-name}/
    SKILL.md                 # Required agent instructions
    metadata.json            # Required repository metadata
    references/              # Optional on-demand documentation
    scripts/                 # Optional deterministic helpers
    assets/                  # Optional output templates or resources
```

Do not add a per-skill README, changelog, installation guide, or quick-reference file. Put human-facing repository summaries in the root `README.md`; put detailed material an agent should load conditionally in `references/`.

### Naming

- Use lowercase kebab-case for the skill directory and frontmatter `name`.
- Name the instruction file exactly `SKILL.md` and metadata file exactly `metadata.json`.
- Keep names short, specific, and action-oriented when possible.

### SKILL.md Frontmatter

```markdown
---
name: {skill-name}
description: {What the skill does and the concrete tasks or contexts that should trigger it.}
license: MIT
metadata:
  author: {author}
  version: "1.0.0"
---
```

Treat `name` and `description` as the activation interface. Include all essential trigger language in `description`; the body is loaded only after activation. Keep repository-required `license` and `metadata` synchronized with `metadata.json`.

### Instruction Design

- Write concise imperative instructions for another capable agent.
- Keep `SKILL.md` below 500 lines and preferably much shorter.
- Include only non-obvious procedures, constraints, decision rules, and reusable knowledge.
- Use progressive disclosure: link every optional reference directly from `SKILL.md` and say when to read it.
- Keep references one level deep and give files over 100 lines a table of contents.
- Add scripts only for repeated or fragile deterministic work, and execute them during validation.
- Add assets only when the skill needs reusable output files or templates.
- Make reusable skills repository- and tool-agnostic unless their purpose explicitly targets one ecosystem.
- Distinguish safe inspection from state-changing actions such as commits, pushes, deployments, account configuration, and third-party communication.
- Do not duplicate the same guidance across `SKILL.md`, references, metadata, and the root README.

### Metadata

`metadata.json` must contain matching version and author values plus a concise abstract. Use semantic versions and update the date when publishing a new version.

### Validation

Before completing a skill change:

1. Parse every `metadata.json` file.
2. Check frontmatter, directory naming, required files, links, and referenced resources.
3. Run a compatible Agent Skills validator when available.
4. Run each added script with representative input.
5. Use `npx skills add . --list` to confirm the repository's skills are discoverable.
6. Forward-test substantial workflow changes with realistic requests when possible, without leaking the intended answer to the test agent.
7. Update the root README when adding, removing, renaming, or materially changing a skill.

## Installation

Use the current Skills CLI for supported coding agents:

```bash
npx skills add {github-user}/skills
```

Install globally with `-g`, select an agent with `--agent`, or select one skill with `--skill`.
