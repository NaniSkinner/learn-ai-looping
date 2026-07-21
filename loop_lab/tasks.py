"""A deliberately small task-list domain used by the boot-camp exercises."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """One immutable task."""

    title: str
    done: bool = False


def normalize_title(title: str) -> str:
    """Trim a title and collapse repeated whitespace.

    The foundation challenge intentionally exposes an unhandled edge case.
    Do not repair it until the learner reaches the execution lesson.
    """

    if not isinstance(title, str):
        raise TypeError("title must be a string")
    return " ".join(title.split())


def add_task(tasks: list[Task], title: str) -> list[Task]:
    """Return a new list containing a normalized task."""

    return [*tasks, Task(title=normalize_title(title))]


def summarize_tasks(tasks: list[Task]) -> dict[str, int]:
    """Return total, completed, and remaining task counts."""

    completed = sum(task.done for task in tasks)
    return {
        "total": len(tasks),
        "completed": completed,
        "remaining": len(tasks) - completed,
    }
