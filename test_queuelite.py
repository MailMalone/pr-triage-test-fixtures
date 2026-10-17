import unittest

from queuelite import add_task, list_tasks


class QueueLiteTests(unittest.TestCase):
    def test_add_task_returns_queue_size(self):
        result = add_task("review PR")
        self.assertEqual(result, len(list_tasks()))

    def test_add_task_rejects_blank_titles(self):
        with self.assertRaises(ValueError):
            add_task("   ")

    def test_list_tasks_returns_a_copy(self):
        before = list_tasks()
        tasks = list_tasks()
        tasks.append("not actually queued")
        self.assertEqual(list_tasks(), before)


if __name__ == "__main__":
    unittest.main()
