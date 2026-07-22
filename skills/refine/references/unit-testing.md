# High-Signal Unit Testing

Read this reference when creating or substantially revising tests during Refine. Apply the repository's existing framework and conventions; the examples are conceptual and do not mandate a language or library.

## Choose the Correct Test Layer

- Use a unit test for deterministic logic with a small input and output surface.
- Use an integration test when correctness depends on collaboration between modules, a database boundary, serialization, or framework behavior.
- Use a component or browser test when the behavior depends on rendering, focus, events, accessibility, navigation, hydration, or layout.
- Use an end-to-end test for a critical user journey across real application boundaries.
- Do not extract logic or add indirection merely to avoid the appropriate test layer.

## Test Contracts, Not Internals

Prefer:

```text
expect(add(1, 2)).toEqual(3)
```

Avoid assertions about an internal helper, temporary variable, or call count when the observable result is the real contract.

Interaction assertions are appropriate when the interaction itself is contractual, such as preventing a duplicate charge, publishing exactly one event, or forwarding a required idempotency key.

## Mock Only Real Boundaries

Mock network, clock, randomness, filesystem, or expensive external dependencies when isolation requires it. Keep domain logic real.

Prefer:

```text
expect(await getDisplayName(fakeUserApi, "1")).toEqual("Ada Lovelace")
```

over a test that only proves `fakeUserApi.fetchUser` was called. Assert both an interaction and the result only when both are part of the contract.

## Cover the Behavior Space

Select cases from the decision boundaries rather than adding one happy-path test for coverage:

```text
adult                         -> eligible
minor with consent           -> eligible
minor without consent        -> ineligible
invalid or missing age       -> documented error behavior
```

Include success, meaningful boundary values, expected failures, and the regression that motivated the branch. Avoid exhaustive combinations that add cost without protecting distinct behavior.

## Make Time and Randomness Deterministic

Inject or freeze clocks, random generators, and generated identifiers. Do not depend on `Date.now() + 1`, real sleeps, wall-clock timezones, or uncontrolled random output.

Prefer:

```text
isExpired(expiresAt=1000, now=999)  -> false
isExpired(expiresAt=1000, now=1000) -> true
```

## Assert Error Contracts Precisely

Verify the documented failure behavior, not merely that "something throws."

Check the relevant error type, code, message, HTTP status, retryability, or returned result. Avoid overspecifying incidental stack traces or formatting.

## Use Snapshots Selectively

Snapshots are useful for stable, reviewable serialized output where the entire shape is the contract. They are weak substitutes for assertions about a few meaningful fields and can hide accidental changes in large blobs.

When using a snapshot:

- Keep it small enough to review.
- Explain why snapshot comparison is the right contract.
- Review updates rather than accepting churn automatically.

## Keep Tests Independent and Reproducible

- Avoid order dependence and shared mutable state.
- Use isolated fixtures with explicit setup and cleanup.
- Avoid real external services in unit tests.
- Bound retries and asynchronous waits.
- Make failures explain which behavior regressed.

## Decide Whether a Test Change Is Needed

Add or revise a test when the branch changes behavior, fixes a regression, adds a boundary, or alters a public contract.

Do not add a test solely to increase a percentage, duplicate stronger coverage, or lock down an implementation detail. If the repository has no suitable test setup, weigh the risk and scope before introducing one; document the alternative verification used.
