# refine

One-command codebase audit. Type `/refine` to run a single evaluation pass that invokes every applicable skill in the current session and produces a prioritized table of improvements.

## What It Does

`/refine` scans your application and evaluates it against all installed skills that are relevant to your stack. It detects your framework and tooling automatically, then applies each skill's rules to produce a deduplicated, impact-sorted list of findings.

**This is evaluation only** — it will not make any changes to your code.

## Usage

Audit the full application:

```
/refine
```

Audit a specific path or area:

```
/refine app/dashboard
/refine components/
/refine authentication flow
```

## Output

A prioritized table sorted by impact:

| # | Priority | Category | File(s) | Current | Suggested | Impact |
|---|----------|----------|---------|---------|-----------|--------|
| 1 | Critical | Perf | `app/page.tsx` | Client component fetches data on mount | Convert to server component with async data | Eliminates client waterfall, improves LCP |
| 2 | High | A11y | `components/Button.tsx` | No focus indicator on custom button | Add `focus-visible` ring style | Keyboard users can't see focus |
| 3 | Medium | UI | `app/layout.tsx` | Fixed max-width doesn't scale | Use responsive container with fluid padding | Better experience on ultrawide displays |

Followed by:
- **Top 3 wins** — highest impact, lowest effort changes
- **Stack health** — one sentence overall assessment

### Priority Levels

| Level | Meaning |
|-------|---------|
| Critical | Major performance, accessibility, or correctness issue |
| High | Meaningful UX or performance win with low effort |
| Medium | Noticeable improvement, moderate effort |
| Low | Polish or minor optimization |

### Categories

| Category | Covers |
|----------|--------|
| Perf | Bundle size, rendering, caching, data fetching |
| UI | Visual design, layout, responsiveness |
| UX | Interaction design, navigation, feedback, loading states |
| A11y | WCAG compliance, keyboard navigation, screen readers |
| Arch | Architecture, component structure, code organization |
| DX | Developer experience, types, conventions, maintainability |

## Companion Skills

`/refine` works on its own using `agent-best-practices` from this repo, but it gets significantly more useful with domain-specific skills installed. Install the ones relevant to your stack:

### Next.js / React projects

From [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills):

```bash
npx skills add vercel-labs/next-skills
```

Adds `next-best-practices` (file conventions, RSC boundaries, data patterns, metadata, error handling) and `next-cache-components` (PPR, `use cache`, cacheLife/cacheTag).

From [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills):

```bash
npx skills add vercel-labs/agent-skills
```

Adds `react-best-practices` (40+ React & Next.js performance rules), `composition-patterns` (compound components, render props, context), and `web-design-guidelines` (100+ UI/UX/accessibility rules).

### React Native / Expo projects

From [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills):

```bash
npx skills add vercel-labs/agent-skills --skill react-native-guidelines
```

Adds 16 rules covering mobile performance, architecture, and platform-specific patterns.

### All projects

From this repo:

```bash
npx skills add sceiler/skills
```

Adds `agent-best-practices` (40+ engineering rules) and `common-mistakes` (25+ anti-patterns from 500+ real sessions).

## How It Selects Skills

1. Reads config files (`package.json`, `next.config.*`, `app.json`, `tsconfig.json`, etc.)
2. Identifies the framework, language, and rendering strategy
3. Picks every installed skill that applies to the detected stack
4. Skips skills that don't apply (e.g., React Native skills for a Next.js project)

## Links

- [Agent Skills Directory](https://skills.sh/) — browse and discover more skills
- [Agent Skills format](https://agentskills.io/) — the open standard these skills follow
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) — Vercel's official skill collection
- [vercel-labs/next-skills](https://github.com/vercel-labs/next-skills) — Next.js specific skills
