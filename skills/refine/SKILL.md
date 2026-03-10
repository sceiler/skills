---
name: refine
description: Review and finish the current branch. Use when the user wants the agent to inspect the branch diff, fix code review, lint, typecheck, test, documentation, and PR gaps, then commit, push, and create or update the PR.
license: MIT
metadata:
  author: sceiler
  version: "2.0.0"
---

# Refine

Run one branch-finishing pass on the current branch. This skill is for taking a branch from "changes exist" to "ready for review or merge": inspect the diff, do a real code review, fix what is wrong, verify the branch, update supporting docs when needed, then commit, push, and create or update the PR.

## When To Apply

- The user asks to refine, finish, polish, or ship the current branch.
- The user wants the agent to review the code changes and fix issues instead of only reporting findings.
- The user wants lint, typecheck, tests, docs, changelog, commit, push, and PR handling completed in one pass.
- The branch is already in progress and needs to be brought to a review-ready state.

## Inputs

- The current git branch
- The diff against its base branch
- The repository's verification commands and test setup
- Optional user constraints such as scope limits, commit message preferences, or PR title/body expectations

## Workflow

1. Establish branch context. Determine the current branch, its merge base or target branch, the changed files, the repo status, and whether a PR already exists.
2. Understand the changes before editing. Read the diff and the surrounding code so the review is based on intent and behavior, not just syntax.
3. Do a real code review of the branch. Look for correctness bugs, regressions, missing edge cases, weak abstractions, incomplete docs, stale files, and missing or low-value tests.
4. Fix issues that are within scope. Do not stop at review notes if the branch can be improved directly.
5. Run the repository's lint command and fix all lint errors.
6. Run the repository's TypeScript checks and fix all warnings and errors. Prefer the project's normal typecheck command; if needed, use `tsc` directly.
7. Review unit test impact. Create, update, or delete tests when the behavior change warrants it.
8. Keep unit tests high-signal:
   - Use Vitest only.
   - Never use jsdom.
   - Never use React rendering-based tests.
   - Test behavior, logic, and observable outcomes rather than implementation details.
   - Do not add vanity coverage tests that only exercise lines without protecting behavior.
   - If the code is hard to test without rendering, refactor toward testable logic instead of adding weak UI tests.
9. Run the relevant test commands and ensure the changed area is actually verified.
10. Check release completeness. Update changelog, README, or other user-facing docs when behavior, APIs, workflows, setup, or expectations changed.
11. Prepare the branch for handoff. Ensure the worktree is clean except for intended changes, write a clear commit message, commit, and push the branch.
12. Sync the pull request. If no PR exists, create one. If it already exists, update the title, body, or checklist when the branch changes make that necessary.
13. If a required step is blocked by missing tooling, missing permissions, or missing repository conventions, state the blocker clearly and complete the rest.

## Review Priorities

- Correctness and regression risk
- Lint and type safety
- Test quality and behavioral coverage
- Documentation and release completeness
- PR readiness and branch hygiene

## Output

Return a concise shipping summary that includes:

1. What issues were found in the branch and what was fixed
2. What verification was run and whether it passed
3. What test changes were made and why
4. Whether docs or changelog were updated
5. The commit hash and push status
6. The PR status or link
7. Any remaining risks or blockers

## Unit Test Examples

Use these patterns to distinguish strong unit tests from weak ones.

### 1. Do not test internals

Bad:

```ts
// math.ts
export function add(a: number, b: number) {
  const result = a + b
  return result
}

// math.test.ts
import { add } from './math'
import { describe, it, expect, vi } from 'vitest'

describe('add', () => {
  it('calls internal addition logic', () => {
    const spy = vi.spyOn(Number.prototype, 'valueOf')

    add(1, 2)

    expect(spy).toHaveBeenCalled()
  })
})
```

Good:

```ts
// math.ts
export function add(a: number, b: number) {
  return a + b
}

// math.test.ts
import { add } from './math'
import { describe, it, expect } from 'vitest'

describe('add', () => {
  it('returns the sum of two numbers', () => {
    expect(add(1, 2)).toBe(3)
  })

  it('handles negative numbers', () => {
    expect(add(-1, 2)).toBe(1)
  })
})
```

Why the bad version is wrong:

- Tests internal implementation details.
- Breaks on refactor even when behavior stays correct.
- Does not validate the actual result.

### 2. Do not over-mock collaborators

Bad:

```ts
// user-service.ts
export async function getDisplayName(api: { fetchUser(id: string): Promise<{ first: string; last: string }> }, id: string) {
  const user = await api.fetchUser(id)
  return `${user.first} ${user.last}`
}

// user-service.test.ts
import { describe, it, expect, vi } from 'vitest'
import { getDisplayName } from './user-service'

describe('getDisplayName', () => {
  it('calls fetchUser once', async () => {
    const api = {
      fetchUser: vi.fn().mockResolvedValue({ first: 'Ada', last: 'Lovelace' }),
    }

    await getDisplayName(api, '1')

    expect(api.fetchUser).toHaveBeenCalledWith('1')
    expect(api.fetchUser).toHaveBeenCalledTimes(1)
  })
})
```

Good:

```ts
// user-service.test.ts
import { describe, it, expect, vi } from 'vitest'
import { getDisplayName } from './user-service'

describe('getDisplayName', () => {
  it('returns the full display name for the fetched user', async () => {
    const api = {
      fetchUser: vi.fn().mockResolvedValue({ first: 'Ada', last: 'Lovelace' }),
    }

    await expect(getDisplayName(api, '1')).resolves.toBe('Ada Lovelace')
  })
})
```

Why the bad version is wrong:

- Verifies interaction noise instead of the unit contract.
- Fails to assert the actual user-visible result.
- Encourages brittle tests tied to call structure.

### 3. Do not use snapshots as the unit contract

Bad:

```ts
// menu.ts
export function buildMenu(role: 'admin' | 'user') {
  return {
    showBilling: role === 'admin',
    showUsers: role === 'admin',
    showProfile: true,
  }
}

// menu.test.ts
import { describe, it, expect } from 'vitest'
import { buildMenu } from './menu'

describe('buildMenu', () => {
  it('matches the admin snapshot', () => {
    expect(buildMenu('admin')).toMatchSnapshot()
  })
})
```

Good:

```ts
// menu.test.ts
import { describe, it, expect } from 'vitest'
import { buildMenu } from './menu'

describe('buildMenu', () => {
  it('enables billing and users for admins', () => {
    expect(buildMenu('admin')).toEqual({
      showBilling: true,
      showUsers: true,
      showProfile: true,
    })
  })

  it('hides admin-only items for normal users', () => {
    expect(buildMenu('user')).toEqual({
      showBilling: false,
      showUsers: false,
      showProfile: true,
    })
  })
})
```

Why the bad version is wrong:

- Snapshots hide the real contract behind a blob.
- Snapshot churn makes review noisy.
- The assertions do not explain which behavior matters.

### 4. Do not add vanity coverage tests

Bad:

```ts
// eligibility.ts
export function isEligible(age: number, hasConsent: boolean) {
  return age >= 18 || hasConsent
}

// eligibility.test.ts
import { describe, it, expect } from 'vitest'
import { isEligible } from './eligibility'

describe('isEligible', () => {
  it('returns true for an adult', () => {
    expect(isEligible(18, false)).toBe(true)
  })
})
```

Good:

```ts
// eligibility.test.ts
import { describe, it, expect } from 'vitest'
import { isEligible } from './eligibility'

describe('isEligible', () => {
  it('returns true for an adult', () => {
    expect(isEligible(18, false)).toBe(true)
  })

  it('returns true for a minor with consent', () => {
    expect(isEligible(16, true)).toBe(true)
  })

  it('returns false for a minor without consent', () => {
    expect(isEligible(16, false)).toBe(false)
  })
})
```

Why the bad version is wrong:

- Covers a line without protecting the behavior space.
- Misses the branch conditions that define correctness.
- Gives false confidence from minimal coverage.

### 5. Do not write nondeterministic time or randomness tests

Bad:

```ts
// session.ts
export function isExpired(expiresAt: number) {
  return Date.now() >= expiresAt
}

// session.test.ts
import { describe, it, expect } from 'vitest'
import { isExpired } from './session'

describe('isExpired', () => {
  it('returns false for a future timestamp', () => {
    expect(isExpired(Date.now() + 1)).toBe(false)
  })
})
```

Good:

```ts
// session.ts
export function isExpired(expiresAt: number, now: () => number = Date.now) {
  return now() >= expiresAt
}

// session.test.ts
import { describe, it, expect } from 'vitest'
import { isExpired } from './session'

describe('isExpired', () => {
  it('returns false before the expiration time', () => {
    expect(isExpired(1_000, () => 999)).toBe(false)
  })

  it('returns true at the expiration time', () => {
    expect(isExpired(1_000, () => 1_000)).toBe(true)
  })
})
```

Why the bad version is wrong:

- Depends on real clock timing.
- Can become flaky around the time boundary.
- Makes failures hard to reproduce.

### 6. Do not ignore the error or result contract

Bad:

```ts
// port.ts
export function parsePort(input: string) {
  const port = Number(input)

  if (!Number.isInteger(port) || port < 1 || port > 65535) {
    throw new Error('Invalid port')
  }

  return port
}

// port.test.ts
import { describe, it, expect } from 'vitest'
import { parsePort } from './port'

describe('parsePort', () => {
  it('throws for invalid input', () => {
    expect(() => parsePort('abc')).toThrow()
  })
})
```

Good:

```ts
// port.test.ts
import { describe, it, expect } from 'vitest'
import { parsePort } from './port'

describe('parsePort', () => {
  it('returns the parsed port for valid input', () => {
    expect(parsePort('3000')).toBe(3000)
  })

  it('throws a clear error for invalid input', () => {
    expect(() => parsePort('abc')).toThrowError('Invalid port')
  })
})
```

Why the bad version is wrong:

- Does not assert the real failure contract.
- Tells the reader almost nothing about expected behavior.
- Can pass while the error type or message regresses.

Characteristics of a good unit test:

- Tests input -> output behavior.
- Independent from internal implementation.
- Small, deterministic, and fast.
- Focused on a single unit of logic.
- Specific about success and failure contracts.

## Rules

- Review the actual branch diff, not just the working tree.
- Fix issues when feasible; do not stop at a findings-only audit unless the user asks for that mode.
- Keep changes scoped to making the branch correct, complete, and reviewable.
- Never claim success without running the relevant verification commands.
- Prefer project-native lint, typecheck, and test commands over guessed commands.
- Use Vitest for unit tests. Do not introduce jsdom, React Testing Library, or browser-style rendering tests under this skill.
- Favor testable business logic and behavior. Avoid snapshot-heavy, implementation-coupled, or vanity coverage tests.
- Update README and changelog only when the branch materially changes behavior, APIs, setup, or user-facing expectations.
- Do not create a commit or PR with known failing lint, typecheck, or required tests unless the user explicitly accepts that state.
- Do not force-push or rewrite history unless the user asks for it.
