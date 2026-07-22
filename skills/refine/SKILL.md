---
name: refine
description: Review, fix, verify, and ship the current branch. Use when the user asks to refine, finish, polish, or prepare an in-progress branch or pull request and wants branch-local issues fixed, repository-native checks run, documentation reviewed, changes committed and pushed, and a pull request created or updated.
license: MIT
metadata:
  author: sceiler
  version: "3.0.0"
---

# Refine

Take an in-progress branch from existing changes to a verified, review-ready pull request. Review the actual branch, fix real issues within its intent, run the repository's own checks, then commit, push, and synchronize the pull request.

## Authorization Boundary

Invoking this skill authorizes branch-local review and fixes, relevant verification, cohesive commits, pushing the current feature branch, and creating or updating its pull request.

It does not authorize:

- Unrelated refactors or feature work
- Discarding or absorbing unrelated user changes
- Force-pushing or rewriting history
- Merging the pull request
- Deploying to production
- Changing external project, team, billing, domain, or integration configuration

Obtain explicit direction before crossing those boundaries.

## Workflow

1. Establish repository rules and branch context.
   - Read the canonical agent instructions and contributor documentation.
   - Inspect the current branch, status, full diff, untracked files, merge base, target branch, remote, and existing pull request.
   - Distinguish intended branch changes from unrelated worktree changes. Preserve the latter.
   - If work is on a default or protected branch, create an appropriate feature branch without discarding current changes.

2. Understand the branch before editing.
   - Read the diff and relevant surrounding code.
   - Infer the branch's intended outcome from code, commits, issue or PR context, and documentation.
   - Identify correctness bugs, regressions, incomplete behavior, stale files, weak abstractions, missing error paths, and documentation gaps.
   - Keep findings tied to the branch's intent. Do not turn Refine into a repository-wide refactor.

3. Fix confirmed issues.
   - Address root causes rather than surface symptoms.
   - Follow repository-native patterns and installed dependency versions.
   - Preserve public contracts and compatibility unless the branch intentionally changes them.
   - Avoid modifying files outside the branch's logical scope unless required for correctness or verification.

4. Review test impact.
   - Detect the project's existing test frameworks, layers, conventions, and commands.
   - Add, update, or delete tests only when the behavior change warrants it.
   - Prefer behavior, contracts, edge cases, and regressions over implementation details or coverage theater.
   - Use the right layer: unit tests for isolated logic, integration tests for component boundaries, and browser or end-to-end tests for behavior that requires a rendered application.
   - Do not introduce or migrate a test framework solely to satisfy this skill.
   - Read [references/unit-testing.md](references/unit-testing.md) when creating or substantially revising tests.

5. Run repository-native verification.
   - Discover commands from project instructions, manifests, CI, and existing scripts.
   - Run relevant formatting or lint, static analysis or typecheck, tests, and build commands.
   - Use targeted checks while iterating, then run the broader required checks before shipping when practical.
   - Exercise user-visible or runtime-sensitive behavior manually when automated checks cannot prove it.
   - Separate branch-caused failures from pre-existing failures and report both accurately.

6. Check release completeness.
   - Update README, changelog, migration notes, generated artifacts, or examples only when the branch materially changes behavior, APIs, setup, or user expectations.
   - Remove stale branch-local artifacts that should not ship.
   - Confirm no credentials, debug output, temporary files, or unrelated changes are included.

7. Commit and push safely.
   - Review the final diff and verification results before committing.
   - Create cohesive commits that match the repository's conventions.
   - Push the feature branch without force unless explicitly authorized.
   - Do not create a knowingly failing commit or PR unless the user explicitly accepts the documented failure.

8. Create or update the pull request.
   - Create a PR against the verified target branch when none exists.
   - Update an existing PR's title, body, checklist, or verification summary when the refined branch makes them stale.
   - Describe the outcome, important implementation decisions, verification, test changes, documentation changes, and remaining risks.
   - Do not merge unless the user asks.

9. Handle blockers without abandoning useful work.
   - If credentials, permissions, tooling, CI, or repository conventions block a step, complete every safe local step that remains.
   - Report the exact blocker, attempted command or operation, and required next action.

## Review Priorities

Review in this order:

1. Correctness, data integrity, and security
2. Regression and compatibility risk
3. Error paths and boundary conditions
4. Repository-native static checks and build health
5. Test value and behavior coverage
6. Documentation and release completeness
7. Branch hygiene and pull-request accuracy

## Completion Report

Return a concise shipping summary containing:

- Issues found and fixes made
- Verification commands and results
- Test changes and why they were appropriate
- Documentation or release-note changes
- Commit hash and push status
- Pull-request URL and status
- Preview or test URL when one exists
- Remaining risks, pre-existing failures, or blockers

Never claim the branch is ready when required verification is still failing without explicit user acceptance.
