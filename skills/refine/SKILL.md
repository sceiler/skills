---
name: refine
description: Run a single refinement pass on an existing codebase or feature area. Use when the user wants a prioritized audit of quality, performance, UX, accessibility, and maintainability improvements before implementation.
license: MIT
metadata:
  author: sceiler
  version: "2.0.0"
---

# Refine

Run one focused refinement pass over the current codebase or a user-specified area. This skill is agent-agnostic: it should work in Claude Code, OpenAI Codex, or any AI coding environment that can inspect files and return structured findings.

## When To Apply

- The user asks to refine, audit, polish, tighten up, or review an application or feature.
- The user wants a prioritized list of improvements instead of immediate implementation.
- The user wants a broad pass across code quality, UX, performance, architecture, accessibility, or developer experience.
- The user provides a path, flow, page, or subsystem and wants targeted findings for that scope.

## Inputs

- A repository, directory, feature area, or user-provided scope
- Optional goals such as performance, UX, accessibility, maintainability, or shipping readiness
- Optional constraints such as "top 5 only" or "frontend only"

## Workflow

1. Define the scope from the user's request. If no scope is given, inspect the whole project.
2. Detect the stack from local evidence such as config files, package manifests, framework folders, and build settings.
3. Select the evaluation lenses that apply to this stack. If other relevant skills are available in the current agent session, use them. If not, continue with direct analysis.
4. Inspect the highest-signal files first: entrypoints, routes, layouts, shared components, data-fetching code, state boundaries, tests, and config.
5. Record concrete findings with file references, current behavior, recommended change, and expected impact.
6. Deduplicate overlapping findings and rank them by severity and payoff.
7. Stop after the audit unless the user explicitly asks for implementation.

## Evaluation Lenses

- Correctness and production risk
- Performance and rendering efficiency
- Architecture and maintainability
- UI, UX, and accessibility
- Testing, observability, and developer workflow

## Output

Return one prioritized set of findings.

If the interface supports markdown tables, use this format:

| # | Priority | Category | Location | Current | Recommended | Impact |
|---|----------|----------|----------|---------|-------------|--------|

If tables are awkward in the current interface, use an equivalent numbered list with the same fields.

After the findings, include:

1. Top 3 improvements with the best effort-to-impact ratio
2. A one-sentence overall assessment of the codebase or scoped area
3. Any assumptions, blind spots, or files you could not verify

## Rules

- Evaluation only. Do not start fixing issues unless the user asks for implementation.
- Be specific. Every finding should point to real files, components, or config.
- Prefer evidence over generic advice. Do not include broad best-practice statements without a concrete trigger in the code.
- Stay stack-aware. Only raise issues that make sense for the actual framework, runtime, and project shape.
- Do not invent problems. If an area looks solid, say so.
- Merge duplicates. If multiple lenses point to the same issue, report it once.
- Keep the list actionable. Aim for roughly 5 to 15 strong findings unless the user asks for more.
- Call out missing evidence. If the audit is limited by absent tests, generated files, or inaccessible runtime behavior, state that clearly.
