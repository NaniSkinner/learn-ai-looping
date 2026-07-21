# Completed Lesson Summaries

This page contains summaries only for lessons that have been completed in the guided journey. A new summary is added after its mastery gate is ready.

## How to use this page

1. Try to retrieve the lesson from memory first.
2. Write or say what you remember.
3. Read the summary and compare it with your answer.
4. Record the one idea you missed or confused.

The summary is a reference after retrieval, not a replacement for retrieval.

## Lesson 00 — Start Here

### Core idea

Progress is based on demonstrated understanding, not time spent reading. Every lesson requires three kinds of evidence:

- **Explain:** State the idea in your own words.
- **Execute:** Apply the idea in practice.
- **Verify:** Show observable evidence that the result is real.

### Why the environment is safe

- `learner/` is ignored by Git so personal answers, questions, and mistakes remain private.
- The toy repository makes experimentation inexpensive and prevents practice from changing production software.
- Public examples must not contain employer code, credentials, customer data, or private context.

### Durable takeaway

Reading or accepting an agent's answer is not mastery. You advance when you can explain, perform, and verify the work.

## Lesson 01 — Name the Loop

### Core idea

The foundational AI work loop is:

> Frame → Orient → Predict → Plan → Execute → Verify → Explain → Preserve

Each stage answers a different question:

| Stage | Question it answers |
|---|---|
| **Frame** | What outcome do we want, what are the boundaries, and what counts as success? |
| **Orient** | What does the relevant evidence say about the current state? |
| **Predict** | What do I expect to happen before the agent acts or answers? |
| **Plan** | What ordered route will move the task from its current state to the goal? |
| **Execute** | What bounded action will we perform now? |
| **Verify** | What independent evidence proves or disproves the result? |
| **Explain** | Can I account for what changed, why it worked, and what the outcome means? |
| **Preserve** | What validated lesson should become reusable context for future work? |

### Important distinctions

- **Frame is the destination; Plan is the route.**
- **Predict happens before the answer; Explain happens after the evidence.**
- **Agent confidence is not verification.** Tests, commands, diffs, and observable behavior provide verification evidence.
- **Preserve does not mean saving everything.** Preserve validated, reusable learning that would otherwise need to be reconstructed.

### Durable takeaway

A polished code change can still fail the loop when nobody independently verifies it.

## Lesson 02 — Contract the Task

### Core idea

Before an agent plans or changes anything, convert the request into a four-part contract:

- **Goal:** The outcome to create.
- **Context:** The specific source material and current behavior that matter.
- **Constraints:** The boundaries, risks, protected behavior, and limits of the agent's authority.
- **Done when:** Observable evidence that distinguishes completion from a plausible claim.

### Important distinctions

- A vague request such as “fix the bug” forces the agent to invent missing requirements.
- Context is not every available document. It is the evidence relevant to this task.
- Constraints state what must remain unchanged as well as what may change.
- Review, opening a pull request, and running unspecified tests are workflow activities. They do not prove the desired behavior.
- Strong done-when statements name observable behavior and how it will be checked with a test, command, or diff.

### Durable takeaway

Define the evidence before execution. Otherwise, the finish line can move to match whatever the agent produced.

## Lesson 03 — Orient to Truth

### Core idea

Before proposing a change, orient to three different states:

- **Code truth:** What the implementation currently says to do.
- **Data truth:** What values or state the implementation actually produces.
- **Decision truth:** What behavior the authorized requirement says should exist.

### Evidence boundary

- **Observed:** Directly supported by an inspected file, command output, test result, runtime state, or written decision.
- **Inferred:** Reasoned, predicted, or proposed beyond what the inspected evidence directly establishes.

A paraphrase can still be observed when the source directly supports it. A plausible fix remains inferred until execution and verification produce evidence.

### Durable takeaway

Do not let a likely explanation silently become a fact. Keep observations and inferences labeled until evidence closes the gap.

---

Next summary: Lesson 04, after its mastery gate is ready.
