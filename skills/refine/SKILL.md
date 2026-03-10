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
