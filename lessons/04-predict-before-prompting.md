# Lesson 04 — Predict Before Prompting

[← Previous: 03](03-orient-to-truth.md) · [Journey](../JOURNEY.md) · [Next: 05 →](05-plan-and-compare.md)

Time: 10–15 minutes

## Outcome

Create a short, timestamped **before snapshot** of what you currently expect. In Lesson 05, you will compare this snapshot with the agent's plan and identify what changed in your understanding.

> You are not editing code, solving the bug, or writing the agent's plan in this lesson.

In plain language: write what you think will change, what the fixed behavior will be, and what must keep working—before the AI tells you.

## Why this matters

An agent's fluent answer can make its reasoning feel obvious after you read it. Writing your expectation first preserves your independent starting model.

The prediction does not need to be correct. A difference between your snapshot and the later plan gives you a question to investigate.

## Active challenge

The toy function `normalize_title("   ")` currently produces an empty string. The authorized behavior says blank titles must raise `ValueError`, while valid-title normalization must remain unchanged.

Relevant files:

- `loop_lab/tasks.py` contains the implementation.
- `tests/test_tasks.py` contains the tests.
- `challenges/01-blank-title.md` contains the authorized requirement and boundaries.

## Worked example — unrelated problem

Imagine a login form that accepts passwords shorter than eight characters.

Before seeing an agent plan, a learner could write:

```text
Likely change area: the password validator and its test file.
Expected behavior: a short password is rejected.
Protected behavior: valid passwords continue to work unchanged.
```

This is enough to preserve the learner's starting model. It is not yet a plan or proof.

## Your turn

Write three predictions for the blank-title challenge:

```text
Likely change area: Where do you think the work will happen? A filename is enough.
Expected behavior: What should happen after the fix?
Protected behavior: What must continue working exactly as it does now?
```

Record the timestamp before requesting an agent plan.

## Optional stretch

Only after the three core predictions are clear, optionally predict:

- the smallest implementation change,
- the pre-fix failing test,
- one tempting but unnecessary change,
- your confidence in any prediction.

## Gate

- **Explain:** In one sentence, explain why the before snapshot is useful even when it is wrong.
- **Execute:** Record the three core predictions.
- **Verify:** Show that the snapshot was timestamped before the agent plan.

---

[← Previous: 03](03-orient-to-truth.md) · [Journey](../JOURNEY.md) · [Next: 05 →](05-plan-and-compare.md)
