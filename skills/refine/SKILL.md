---
name: refine
description: Run one refinement pass over the current application using all applicable skills to find performance, UI, and UX improvements.
disable-model-invocation: true
argument-hint: "[path or area to focus on]"
license: MIT
metadata:
  author: sceiler
  version: "1.0.0"
---

# Refine

Run a single refinement pass over the current application. Evaluate the codebase using every applicable skill available in this session, then produce a prioritized list of improvements.

## How It Works

1. **Detect the stack** — Identify the framework, language, and rendering strategy from config files (`package.json`, `next.config.*`, `app.json`, `tsconfig.json`, etc.)
2. **Select applicable skills** — From the skills available in this session, pick every one that is relevant to the detected stack. Typical candidates:
   - `next-best-practices` — file conventions, RSC boundaries, data patterns, metadata
   - `next-cache-components` — PPR, `use cache`, cacheLife/cacheTag
   - `vercel-react-best-practices` — React & Next.js performance optimization
   - `vercel-composition-patterns` — component API design, compound components
   - `vercel-react-native-skills` — React Native / Expo performance (only if applicable)
   - `web-design-guidelines` — accessibility, UI/UX audit
   - `agent-best-practices` — general engineering quality
3. **Invoke each selected skill** against the codebase to gather findings
4. **Deduplicate and rank** — Merge overlapping findings, then sort by impact

## Scope

If arguments are provided (`$ARGUMENTS`), limit the analysis to that path or area. Otherwise evaluate the full application.

## Output Format

Present findings as a single table sorted by impact (highest first):

| # | Priority | Category | File(s) | Current | Suggested | Impact |
|---|----------|----------|---------|---------|-----------|--------|
| 1 | Critical | Perf | `app/page.tsx` | Client component fetches data on mount | Convert to server component with async data | Eliminates client waterfall, improves LCP |

### Priority levels

- **Critical** — Major performance, accessibility, or correctness issue
- **High** — Meaningful UX or performance win with low effort
- **Medium** — Noticeable improvement, moderate effort
- **Low** — Polish or minor optimization

### Categories

- **Perf** — Performance (bundle size, rendering, caching, data fetching)
- **UI** — Visual design, layout, responsiveness
- **UX** — Interaction design, navigation, feedback, loading states
- **A11y** — Accessibility (WCAG compliance, keyboard nav, screen readers)
- **Arch** — Architecture, component structure, code organization
- **DX** — Developer experience (types, conventions, maintainability)

## Rules

- **One pass only** — Do not start implementing fixes. This is an evaluation.
- **Be specific** — Reference actual files, components, and line ranges. No vague advice.
- **Show before and after** — The "Current" and "Suggested" columns should contain concrete descriptions or brief code snippets, not abstract statements.
- **No duplicates** — If multiple skills flag the same issue, list it once under the most relevant category.
- **Stay honest** — If the codebase is already well-optimized in an area, say so. Don't manufacture findings.
- **Cap the list** — Aim for 10–20 actionable findings. Quality over quantity.

## After the Table

Provide a brief summary:
1. **Top 3 wins** — The three changes that would deliver the most impact for the least effort
2. **Stack health** — One sentence overall assessment (e.g., "Solid foundation with room for caching improvements")
