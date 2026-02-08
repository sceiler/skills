---
name: common-mistakes
description: Concrete wrong/correct examples of common AI coding agent mistakes. Apply when writing code, modifying files, debugging issues, or generating output. Derived from real corrections across 500+ chat sessions.
license: MIT
metadata:
  author: sceiler
  version: "1.0.0"
---

# Common AI Coding Agent Mistakes

Concrete examples of mistakes AI coding agents make repeatedly, derived from analysis of 500+ real chat sessions across 21 projects. Each rule follows a "what went wrong / what is correct" pattern.

Complements `agent-best-practices` (principles) with specific, actionable anti-patterns.

## When to Apply

Apply these rules in every coding session. They address the most frequent real-world corrections users make to AI agent output.

---

## 1. File & Project Awareness (CRITICAL)

### `files-check-symlinks`
**Always check for symlinks before modifying files.**

| | Example |
|---|---|
| Wrong | Overwriting `CLAUDE.md` content without checking that it's a symlink to `AGENTS.md`, destroying the shared file |
| Correct | Run `ls -la` to check for symlinks before editing. If symlinked, understand the relationship and edit the target appropriately |

### `files-prefer-symlinks`
**Use symlinks instead of file copying for dev workflows.**

| | Example |
|---|---|
| Wrong | `cp ~/Projects/plugin/{main.js,manifest.json} ~/.obsidian/plugins/plugin/` and telling user to run this after every change |
| Correct | `ln -s ~/Projects/plugin/main.js ~/.obsidian/plugins/plugin/main.js` — changes propagate automatically |

### `files-read-project-config`
**Read CLAUDE.md / project config before making any changes.**

| | Example |
|---|---|
| Wrong | Starting work without reading CLAUDE.md, then violating branch naming conventions, commit rules, or package manager requirements |
| Correct | Read CLAUDE.md first. Follow its workflow rules exactly. If it says "create a branch before any code changes," do that before writing a single line |

### `files-respect-project-modes`
**Understand project-specific design decisions before changing them.**

| | Example |
|---|---|
| Wrong | Adding `dark:text-white` and `light:text-gray-900` classes to a website that only has dark mode |
| Correct | Check if the project uses light mode, dark mode, or both before adding theme-conditional styles. If only dark mode exists, use direct color values |

---

## 2. Multi-Target Instructions (CRITICAL)

### `multi-target-all-projects`
**When told to run something in multiple projects, do ALL of them.**

| | Example |
|---|---|
| Wrong | User says "run this in my-website-dashboard, skills, and toolcall" — agent only runs it in my-website-dashboard |
| Correct | Execute in every listed project. Track completion per project. Report results for each one separately |

### `multi-target-exact-scope`
**Apply changes to exactly the scope specified — no more, no less.**

| | Example |
|---|---|
| Wrong | User says "disable auth only for preview" — agent disables auth for both production AND preview |
| Correct | Apply the change to exactly the specified target. If unsure whether adjacent targets should also change, ask |

---

## 3. Deprecated & Outdated APIs (HIGH)

### `api-check-deprecations`
**Verify APIs are not deprecated for the installed framework version.**

| | Example |
|---|---|
| Wrong | Using `priority` prop on Next.js `<Image>` component (deprecated) |
| Correct | Use `loading="eager"` or `fetchPriority="high"` instead. Always check `package.json` for the installed version and reference current docs |

### `api-verify-knowledge`
**When your knowledge might be outdated, say so and verify.**

| | Example |
|---|---|
| Wrong | Confidently stating "Vercel AI Gateway does not support these models" based on stale training data, then making config changes based on wrong information |
| Correct | State "my information may be outdated for this" and verify via docs, web search, or user confirmation before making changes. When wrong, immediately revert |

### `api-field-names`
**Verify exact field names from API responses — don't assume.**

| | Example |
|---|---|
| Wrong | Filtering on `status` field when the API response uses `state`, causing deployments to silently disappear |
| Correct | Log or inspect actual API responses to confirm field names before writing filter logic. Never assume field names match across different APIs |

---

## 4. Output Formatting (HIGH)

### `format-consistency`
**Use consistent formatting throughout the entire output.**

| | Example |
|---|---|
| Wrong | Writing the first half of a document in markdown with tables and headers, then switching to plain text for the second half |
| Correct | Choose one format and stick with it for the entire output. If the user requests markdown, EVERY section must be markdown |

### `format-match-project`
**Match the project's existing formatting conventions.**

| | Example |
|---|---|
| Wrong | Setting `tabWidth: 2` for markdown files when the project uses `tabWidth: 4` everywhere |
| Correct | Check existing `.prettierrc`, `.editorconfig`, or formatting config before adding or changing format rules. Match what exists |

### `format-dont-overconfigure`
**Don't add formatting rules for file types that don't need them.**

| | Example |
|---|---|
| Wrong | Adding tabWidth overrides for `.yml` files when there's no reason to change them |
| Correct | Only add formatting rules when explicitly requested or when there's a clear problem to solve |

### `format-user-preferences`
**Respect stated writing style preferences.**

| | Example |
|---|---|
| Wrong | Using contractions ("I'm", "don't") when user said they prefer "I am"; using bold formatting when user said "don't use bold" |
| Correct | When a user states a style preference, apply it consistently across all output. Record preferences and follow them |

---

## 5. Debugging Anti-Patterns (HIGH)

### `debug-dont-make-it-worse`
**Verify that your fix doesn't make the problem worse before declaring it done.**

| | Example |
|---|---|
| Wrong | Suggesting "purge cache" to fix a dashboard not showing deployments — purging actually made it show FEWER deployments |
| Correct | After applying a fix, verify the state is better than before, not just different. If the fix makes things worse, immediately revert and investigate deeper |

### `debug-change-code-not-config`
**When config changes don't fix the problem, change the code.**

| | Example |
|---|---|
| Wrong | Repeatedly updating env vars and redeploying when the actual bug is in the code's data fetching logic |
| Correct | After one config attempt fails, shift to investigating the code path. Read the actual code that processes the config values |

### `debug-right-layer`
**Fix bugs at the layer where they actually exist.**

| | Example |
|---|---|
| Wrong | Modifying SVG icon files to fix a build error that actually comes from the GitHub Actions workflow |
| Correct | Trace the error to its actual source. If it works locally and on Vercel but fails in CI, the problem is in the CI config, not the code |

### `debug-cumulative-vs-incremental`
**Explicitly clarify whether metrics are cumulative or incremental before aggregating.**

| | Example |
|---|---|
| Wrong | Summing `daily_pageviews` table rows directly, not realizing they store cumulative totals — inflating view counts by orders of magnitude |
| Correct | Inspect actual data samples. If rows show `[100, 150, 200]`, determine whether these are daily counts (sum = 450) or cumulative snapshots (daily = 50, 50). State the assumption before writing aggregation code |

### `debug-stop-repeating-failures`
**After two failed fix attempts, change strategy entirely.**

| | Example |
|---|---|
| Wrong | Trying 4 different CSS tweaks to fix Safari E2E test failures, each one failing |
| Correct | After 2 failed attempts at the same approach, step back. In this case: remove Safari from the test matrix entirely since the value doesn't justify the cost |

---

## 6. Wrong Optimizations (HIGH)

### `optimize-know-server-vs-client`
**Understand Server Components vs Client Components before optimizing.**

| | Example |
|---|---|
| Wrong | Wrapping a Server Component with `React.memo()` (memo does nothing for RSC). Adding `Suspense` boundary around a statically generated component that has no async operations |
| Correct | Check if the component is a Server Component (no `"use client"` directive) before applying client-side optimizations. `memo`, `useMemo`, `useCallback` are meaningless in Server Components |

### `optimize-measure-first`
**Don't add caching/optimization to trivial operations.**

| | Example |
|---|---|
| Wrong | Adding `cache()` wrapper to a `structuredData` function that constructs a small JSON object — cache overhead exceeds the benefit |
| Correct | Only optimize operations that are measurably slow. A function that runs once during build and takes <1ms does not need caching |

---

## 7. Content & Data Integrity (MEDIUM)

### `content-preserve-special-chars`
**Don't strip special characters from content unless required for file safety.**

| | Example |
|---|---|
| Wrong | Stripping `<>` and `/` from a heading, turning `# Supercell <> Vercel / AI Overview` into `# Supercell  Vercel  AI Overview` |
| Correct | Only strip characters that are invalid for the specific context. Filenames need stripping (no `/`), but heading content inside the file should preserve all characters |

### `content-titles-dont-repeat`
**Avoid repeating the same identifier in compound titles.**

| | Example |
|---|---|
| Wrong | `About Yi Min Yang | Yi Min Yang` — the name appears twice |
| Correct | `About | Yi Min Yang` — the section identifier is distinct from the site name |

### `content-slug-to-title`
**Never trust automatic slug-to-title conversion for display.**

| | Example |
|---|---|
| Wrong | Converting `my-blog-post` to `My Blog Post` and assuming it matches the actual title |
| Correct | Read the actual title from the data source (frontmatter, database, CMS). Slugs are lossy — they lose casing, punctuation, and special characters |

### `content-respect-intentional-design`
**Don't "fix" behavior that is intentional.**

| | Example |
|---|---|
| Wrong | "Optimizing" a pageview counter to not increment on refresh, when the user explicitly designed it to increment on every page load including refreshes |
| Correct | Before optimizing existing behavior, ask if it's intentional. If the user says "this is by design," respect that constraint in all subsequent changes |

### `content-sitemap-hygiene`
**Generated routes like OG images should not appear in sitemaps.**

| | Example |
|---|---|
| Wrong | Sitemap contains `/blog/my-post/opengraph-image` URLs that Google shouldn't index |
| Correct | Exclude generated asset routes from sitemap generation. Only include pages meant for human visitors |

---

## 8. Security Scope (MEDIUM)

### `security-exact-target`
**Security changes must target exactly what was specified.**

| | Example |
|---|---|
| Wrong | Disabling Vercel Authentication for the entire project (production + preview) when asked to disable it "only for preview" |
| Correct | Apply security changes to exactly the specified scope. If the tool doesn't support granular control, inform the user before making a broader change |

### `security-revert-failed-bypasses`
**If a security bypass doesn't work, revert it — don't leave it in.**

| | Example |
|---|---|
| Wrong | Adding a bypass header mechanism that doesn't actually work, leaving dead bypass code in production |
| Correct | If an approach fails, fully revert it. Dead security bypass code is both confusing and a potential vulnerability |

---

## Quick Reference: Most Common Mistakes

| Frequency | Mistake | Rule |
|-----------|---------|------|
| Very High | Not following all instructions (skipping projects, over/under-scoping) | `multi-target-all-projects`, `multi-target-exact-scope` |
| Very High | Using deprecated or wrong API for the framework version | `api-check-deprecations`, `api-verify-knowledge` |
| High | Inconsistent output formatting | `format-consistency`, `format-match-project` |
| High | Repeated failed fix attempts without changing strategy | `debug-stop-repeating-failures` |
| High | Applying client-side optimizations to server components | `optimize-know-server-vs-client` |
| Medium | Modifying symlinked files without checking | `files-check-symlinks` |
| Medium | Making debugging worse (cache purge, wrong layer) | `debug-dont-make-it-worse`, `debug-right-layer` |
| Medium | Stripping characters or data that should be preserved | `content-preserve-special-chars` |
