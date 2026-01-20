---
name: software-engineering-fundamentals
description: Core software engineering principles for AI coding agents. Apply when writing, modifying, or reviewing any code. Ensures code changes are verified, tested, and production-ready. Never assume code works without verification.
license: MIT
metadata:
  author: sceiler
  version: "1.0.0"
---

# Software Engineering Fundamentals

Essential software engineering principles that every coding agent must follow. These rules ensure code changes are reliable, maintainable, and production-ready.

## Core Philosophy

**Never assume code will work. Always verify.**

Code that hasn't been tested is broken code you haven't discovered yet. Every change, no matter how small, can have unintended consequences.

## When to Apply

Reference these guidelines when:
- Writing any new code
- Modifying existing code
- Fixing bugs
- Refactoring
- Before considering any task "complete"

## Rule Categories by Priority

| Priority | Category | Impact |
|----------|----------|--------|
| 1 | Testing & Verification | CRITICAL |
| 2 | Error Handling | HIGH |
| 3 | Code Quality | HIGH |
| 4 | Change Management | MEDIUM |
| 5 | Security Awareness | MEDIUM |

---

## 1. Testing & Verification (CRITICAL)

### `test-always-run`
**Always run tests after making changes.**

Never assume your change works. Run the existing test suite to catch regressions. If tests don't exist, this is a signal to write them.

```bash
# After ANY code change
npm test        # or pytest, go test, cargo test, etc.
```

### `test-verify-manually`
**Manually verify the change works as expected.**

Automated tests catch regressions, but you must also verify the actual behavior matches intent. Run the code, check the output, confirm it does what was requested.

### `test-write-tests`
**Write tests for new functionality.**

New code without tests is incomplete code. Write tests that:
- Cover the happy path
- Cover edge cases
- Cover error conditions

```python
# Bad: Function without tests
def calculate_total(items):
    return sum(item.price for item in items)

# Good: Function with corresponding tests
def test_calculate_total_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_single_item():
    assert calculate_total([Item(price=10)]) == 10

def test_calculate_total_multiple_items():
    assert calculate_total([Item(price=10), Item(price=20)]) == 30
```

### `test-check-build`
**Verify the project builds/compiles successfully.**

A passing test suite means nothing if the project doesn't build. Always run the build command before considering work complete.

```bash
npm run build   # or cargo build, go build, etc.
```

### `test-no-assumptions`
**Never assume a "simple" change is safe.**

The most dangerous changes are the ones that seem trivial:
- "Just a rename" can break imports
- "Just a type change" can cause runtime errors
- "Just moving code" can change execution order

Always verify.

---

## 2. Error Handling (HIGH)

### `error-handle-all`
**Handle all error cases explicitly.**

Don't let errors fail silently. Every operation that can fail should have explicit error handling.

```javascript
// Bad: Ignoring potential errors
const data = JSON.parse(response);

// Good: Handling errors explicitly
let data;
try {
    data = JSON.parse(response);
} catch (error) {
    console.error('Failed to parse response:', error);
    throw new Error('Invalid response format');
}
```

### `error-meaningful-messages`
**Provide meaningful error messages.**

Error messages should help diagnose the problem. Include:
- What operation failed
- Why it failed (if known)
- What the user/developer can do about it

```python
# Bad
raise Exception("Error")

# Good
raise ValueError(f"Invalid user ID '{user_id}': must be a positive integer")
```

### `error-dont-swallow`
**Never swallow errors silently.**

Empty catch blocks hide bugs. If you catch an error, do something with it.

```javascript
// Bad: Swallowing errors
try {
    riskyOperation();
} catch (e) {
    // silent failure
}

// Good: At minimum, log the error
try {
    riskyOperation();
} catch (e) {
    console.error('riskyOperation failed:', e);
    // Then decide: rethrow, return default, or handle
}
```

---

## 3. Code Quality (HIGH)

### `quality-readable-code`
**Write code that is easy to read and understand.**

Code is read far more often than it is written. Optimize for readability:
- Use descriptive variable and function names
- Keep functions small and focused
- Avoid clever tricks that obscure intent

```python
# Bad: Clever but unclear
def p(d): return {k:v for k,v in d.items() if v}

# Good: Clear and readable
def remove_empty_values(data):
    return {key: value for key, value in data.items() if value}
```

### `quality-single-responsibility`
**Each function/class should do one thing well.**

If a function does multiple things, split it up. This makes code easier to test, understand, and modify.

### `quality-avoid-duplication`
**Don't repeat yourself, but don't over-abstract.**

Duplicate code is a maintenance burden. But premature abstraction is worse. The rule of three: abstract when you see the same pattern three times.

### `quality-consistent-style`
**Follow the existing code style.**

Consistency matters more than personal preference. Match:
- Naming conventions
- Indentation
- File organization
- Patterns used elsewhere in the codebase

---

## 4. Change Management (MEDIUM)

### `change-small-commits`
**Keep changes small and focused.**

Large changes are hard to review, hard to test, and hard to revert. Each change should do one thing.

### `change-review-diff`
**Review your own changes before committing.**

Look at the diff. Check for:
- Unintended changes
- Debug code left in
- Commented-out code
- Files that shouldn't be included

```bash
git diff --staged   # Review before committing
```

### `change-meaningful-commits`
**Write meaningful commit messages.**

Commit messages should explain WHY, not just WHAT. Future developers (including yourself) will thank you.

```bash
# Bad
git commit -m "fix bug"

# Good
git commit -m "Fix null pointer when user has no email address

The getUserEmail() function assumed all users have an email,
but guest users don't. Now returns empty string for guests."
```

### `change-dont-break-main`
**Never commit code that breaks the main branch.**

Before pushing:
1. Run all tests
2. Verify the build passes
3. Test the actual functionality

---

## 5. Security Awareness (MEDIUM)

### `security-no-secrets`
**Never commit secrets or credentials.**

API keys, passwords, tokens - none of these belong in code. Use environment variables or secret management systems.

```python
# Bad: Hardcoded secret
API_KEY = "sk-1234567890abcdef"

# Good: From environment
API_KEY = os.environ.get("API_KEY")
```

### `security-validate-input`
**Validate all external input.**

Never trust data from:
- User input
- API responses
- File contents
- Environment variables

Validate before using.

### `security-sanitize-output`
**Sanitize data before displaying or storing.**

Prevent injection attacks by escaping or sanitizing:
- HTML content (prevent XSS)
- SQL queries (prevent SQL injection)
- Shell commands (prevent command injection)

---

## Quick Checklist

Before considering any code change complete:

- [ ] Tests pass
- [ ] Build succeeds
- [ ] New code has tests
- [ ] Errors are handled
- [ ] Code is readable
- [ ] Change is focused
- [ ] No secrets committed
- [ ] Manually verified it works

## Summary

The most important principle: **Verify, don't assume.**

Every line of code you write could have a bug. Every change could break something. The only way to know your code works is to test it - automatically and manually. Never skip this step.
