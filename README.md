# Learn AI Looping

A mastery-gated boot camp for learning how to work *with* an AI agent without outsourcing your understanding to it.

This repository teaches one foundational loop:

> Frame → Orient → Predict → Plan → Execute → Verify → Explain → Preserve

It is designed for short 10–15 minute learning windows. There is no calendar and no requirement to complete only one lesson per day. You advance when you can explain the idea, execute it, and verify the result.

## Who this is for

- People who already use ChatGPT, Codex, Claude, or another agent but feel they are mostly prompting and reviewing.
- Builders who want agents to work more independently without losing human understanding or control.
- Teams that want a safe path from one-off prompting to reusable workflows and automations.

You do not need advanced programming knowledge. The practice project uses only Python's standard library.

## Start here

Open **[START HERE](START_HERE.md)**. It gives you the setup commands and points to the first lesson.

After that, [JOURNEY.md](JOURNEY.md) is the single course map. Every lesson also ends with **Previous · Journey · Next** navigation, so you never have to infer where to go.

## Repository map

```text
START_HERE.md       setup and first action
JOURNEY.md          ordered lesson checklist
LESSON_SUMMARIES.md retrieval-first summaries of completed lessons
lessons/            the 10–15 minute learning units
challenges/         safe problems used during the lessons
curriculum-notes/   evidence-backed improvements to the learning design
loop_lab/           dependency-free toy application
tests/              verification suite
templates/          private progress and session-card templates
INSTRUCTOR_GUIDE.md guidance for an AI or human instructor
```

## The mastery gate

Every lesson ends with three forms of evidence:

1. **Explain:** Describe the idea in your own words.
2. **Execute:** Use it on the current challenge.
3. **Verify:** Show evidence that distinguishes success from appearance.

Your instructor can mark a lesson:

- **Ready:** continue.
- **Revisit:** correct one missing piece, then continue.
- **Stretch:** the core is ready; an optional harder exercise is available.

There are no percentages and no ceremonial scores.

## Public-safety rules

This repository is intended to be shareable. Never add:

- employer or client source code,
- private prompts or transcripts,
- credentials, tokens, or `.env` files,
- customer or student data,
- proprietary metrics, roadmaps, or issue descriptions,
- private Nessie context copied verbatim.

Translate real work into generic examples. Keep personal progress in `learner/`, which Git ignores.

## What comes later

Only after the foundational loop is mastered will the boot camp add:

- context systems such as Nessie,
- external research with Exa,
- `AGENTS.md`, skills, and tools,
- subagents and reviewer roles,
- scheduled and asynchronous work,
- post-mortems and learning memory,
- controlled autonomy and merge gates.

Those mechanisms are leverage. The manual loop comes first.

## Current status

Foundation release: the manual AI loop. Later releases will add research, reusable workflows, agents, and controlled automation after the foundation is mastered.
