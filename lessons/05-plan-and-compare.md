# Lesson 05 — Plan and Compare

[← Previous: 04](04-predict-before-prompting.md) · [Journey](../JOURNEY.md) · [Next: 06 →](06-execute-smallest-step.md)

Time: 10–15 minutes

## Outcome

Compare the agent's proposed route with your Lesson 04 before snapshot, then authorize only the smallest in-scope execution boundary.

> You are evaluating a plan in this lesson. You are not permitting edits yet.

## Why this matters

An agent plan is a proposal, not authority. Compare it with the task contract and your prediction before permitting edits.

## Request the plan

Ask your agent:

> Inspect `challenges/01-blank-title.md`, `loop_lab/tasks.py`, and `tests/test_tasks.py`. Propose the smallest plan that satisfies the written requirement and boundaries. Do not edit files. For each step, name the file, reason, and verification evidence. Identify any unnecessary work you rejected.

## Compare

For each of the three predictions from Lesson 04, record:

| Before snapshot | Agent plan | Same or different? | Question or evidence needed |
|---|---|---|---|
| Likely change area | | | |
| Expected behavior | | | |
| Protected behavior | | | |

Then identify:

- one agreement,
- one surprise or correction, if any,
- any plan item outside the contract,
- the exact files and actions the agent may perform next.

## Gate

- **Explain:** Why can a technically sound plan still be wrong for the task?
- **Execute:** Complete the three-row comparison.
- **Verify:** State exactly what the agent may edit next.

---

[← Previous: 04](04-predict-before-prompting.md) · [Journey](../JOURNEY.md) · [Next: 06 →](06-execute-smallest-step.md)
