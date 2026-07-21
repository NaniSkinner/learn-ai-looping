import unittest

from loop_lab import Task, add_task, normalize_title, summarize_tasks


class TaskTests(unittest.TestCase):
    def test_normalize_title_collapses_whitespace(self) -> None:
        self.assertEqual(normalize_title("  learn   the loop  "), "learn the loop")

    def test_add_task_does_not_mutate_original_list(self) -> None:
        original = [Task("existing")]

        result = add_task(original, "  new task ")

        self.assertEqual(original, [Task("existing")])
        self.assertEqual(result, [Task("existing"), Task("new task")])

    def test_summarize_tasks_reconciles_counts(self) -> None:
        tasks = [Task("one", done=True), Task("two"), Task("three")]

        summary = summarize_tasks(tasks)

        self.assertEqual(summary, {"total": 3, "completed": 1, "remaining": 2})
        self.assertEqual(summary["completed"] + summary["remaining"], summary["total"])


if __name__ == "__main__":
    unittest.main()
