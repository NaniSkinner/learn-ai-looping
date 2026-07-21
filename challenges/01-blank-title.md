# Challenge 01 — Reject Blank Task Titles

## User problem

A task with no visible title cannot be acted on or reviewed.

## Current behavior

`normalize_title` removes whitespace but allows the resulting title to be empty.

## Desired behavior

- A blank or whitespace-only title raises `ValueError`.
- A non-string title continues to raise `TypeError`.
- Valid-title normalization remains byte-for-byte unchanged.
- `add_task` continues to return a new list rather than mutating its input.

## Boundaries

- No new dependency.
- No unrelated refactor.
- No change to the `Task` data model.

## Evidence

- A focused regression test fails before the fix and passes after it.
- The existing full suite continues to pass.
