# Curriculum Improvement 001 — Prediction Scaffolding

Status: implemented and learner-validated

## Learner-reported problem

Lesson 04 was confusing, and its intended outcome was difficult to identify.

## Observed evidence

During the guided lesson, the learner:

- returned confidence ratings without prediction statements,
- asked which files the exercise referred to and what action was expected,
- needed repeated clarification that the task was prediction rather than code editing,
- completed the mechanics but later reported that the lesson outcome remained unclear.

These observations show an instructional-design failure rather than a lack of learner effort.

## Root cause

The original lesson:

1. buried the outcome inside explanatory prose,
2. did not restate the active toy challenge,
3. required five different predictions and five confidence ratings at once,
4. provided no worked example before the learner attempt,
5. made completing the template more visible than the before/after comparison it was meant to enable.

## Accepted correction

- Put one measurable outcome at the top of the lesson.
- State explicitly that the learner is not editing code or creating the agent plan yet.
- Restate the toy challenge and relevant files.
- Show one unrelated worked example.
- Reduce the core prediction to three statements: likely change area, expected behavior, and protected behavior.
- Move implementation detail, test prediction, scope-creep prediction, and confidence to an optional stretch.
- Make Lesson 05 perform the comparison that gives the prediction its value.

## Verification criteria

The revision is acceptable only if a learner can answer these questions from the lesson itself:

1. What am I doing? Writing a short before-snapshot of my current expectation.
2. What am I not doing? Editing code or accepting an agent plan.
3. Why am I doing it? To compare my model with the later plan and identify what changed.
4. What must I produce? Three concrete predictions recorded before the plan.

## Privacy boundary

This note preserves generalized learning evidence. It does not include private production context or identify the learner.

## Outcome verification

After the revision, the learner correctly explained that Lesson 04 records expected changes and protected behavior before agent influence. One timing correction was needed: Lesson 05 compares that snapshot with the proposed plan; execution and behavioral verification occur in later lessons. The learner then correctly taught back the plan-comparison boundary.
