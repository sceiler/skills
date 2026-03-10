# refine

Version `2.0.0` turns `refine` into a branch-finishing skill for AI coding agents. It is designed to take the current branch from "work in progress" to "review-ready": inspect the diff, fix issues, verify the branch, and ship the PR.

## What It Does

`refine` reviews the code changes on the current branch, fixes code review issues it finds, runs lint and TypeScript verification, makes sure unit tests are correct and useful, updates README or changelog when needed, then commits, pushes, and creates or updates the PR.

## Use It For

- Finishing an in-progress branch before review
- Cleaning up a PR before merge
- Catching and fixing branch-local issues in one pass
- Making sure tests and docs keep up with the code change

## Example Prompts

Use natural language that matches your agent:

```text
Refine the current branch and get it ready for PR.
Review these branch changes, fix any issues, and push the branch.
Finish this PR properly: lint, typecheck, tests, docs, commit, push, and update the PR.
Refine this branch, but keep the scope limited to the files already touched.
```

## Workflow Expectations

The skill should:

- Review the branch diff against its base branch
- Fix real issues instead of stopping at findings
- Ensure lint is clean
- Ensure TypeScript is clean
- Create, update, or delete tests when the behavior change requires it
- Use Vitest only for unit tests
- Avoid jsdom and React rendering tests
- Prefer behavior-focused tests over vanity coverage
- Update changelog or README when the change warrants it
- Commit and push the branch
- Create the PR if needed, or update it if it already exists

## Unit Test Guidance

Bad unit tests inspect implementation details and create fragile coverage theater. For example:

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

Prefer behavior-focused tests instead:

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

Good unit tests are:

- Focused on input -> output behavior
- Independent from implementation details
- Small, deterministic, and fast
- Targeted at one logical unit

## Output Shape

The final result should report:

- What was reviewed and fixed
- What verification ran and whether it passed
- What test changes were made
- Whether docs or changelog changed
- The commit and push status
- The PR status or link
- Any blockers that prevented full completion

## Notes

`refine` is intended to be agent-agnostic, but it assumes the agent can inspect git state, run the repository's verification commands, and interact with the git hosting workflow when credentials and tooling are available.
