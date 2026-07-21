# Lesson 06 — Execute the Smallest Step

[← Previous: 05](05-plan-and-compare.md) · [Journey](../JOURNEY.md) · [Next: 07 →](07-verify-three-truths.md)

Time: 10–15 minutes

## Learn

Execution should be the smallest reversible step that can test the plan.

## Do

Authorize only this sequence:

1. Add a focused test for the blank-title contract.
2. Run it against the unchanged implementation and observe failure.
3. Implement the smallest fix.
4. Run the focused test again.

Do not refactor unrelated code.

## Gate

- **Explain:** Why must the regression test fail before the fix?
- **Execute:** Produce the bounded diff.
- **Verify:** Preserve both the pre-fix failure and post-fix pass evidence.

---

[← Previous: 05](05-plan-and-compare.md) · [Journey](../JOURNEY.md) · [Next: 07 →](07-verify-three-truths.md)
