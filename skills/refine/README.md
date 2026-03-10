# refine

Version `2.0.0` rewrites `refine` as an AI coding agent agnostic audit skill. It is designed to work in Claude Code, OpenAI Codex, or similar agents that can inspect a repository and return structured findings.

## What It Does

`refine` runs one focused refinement pass over a repository, feature, or path and returns a prioritized set of improvements. The skill is evaluation-only by default: it audits the codebase, ranks the issues, and stops before implementation unless the user asks for changes.

## Use It For

- Whole-repo health checks
- Targeted audits of a route, feature, page, or subsystem
- Pre-release cleanup passes
- Performance, UX, accessibility, architecture, or DX reviews

## Example Prompts

Use natural language that matches your agent:

```text
Run a refine pass on this repo.
Refine the dashboard area and give me the top 10 improvements.
Audit this app for performance, accessibility, and maintainability issues.
Do one refinement pass on auth and stop at findings only.
```

## Output Shape

The skill returns one prioritized set of findings with:

- Priority
- Category
- File or location
- Current issue
- Recommended change
- Expected impact

It also includes:

- Top 3 highest-leverage improvements
- A one-sentence overall assessment
- Any assumptions or verification gaps

## Compatibility

`refine` no longer assumes slash commands, platform-specific prompt syntax, or a particular skill runtime. If other relevant skills are available in the current agent session, they can be used to sharpen the audit, but they are optional.
