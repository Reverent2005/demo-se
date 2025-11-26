import unittest
from src.todo import TodoList

class TestTodo(unittest.TestCase):

    def setUp(self):
        self.todo = TodoList()

    def test_add_task(self):
        self.todo.add_task("Task 1")
        self.assertIn("Task 1", self.todo.tasks)

    def test_remove_task(self):
        self.todo.add_task("Task 1")
        self.todo.remove_task("Task 1")
        self.assertNotIn("Task 1", self.todo.tasks)

    def test_list_tasks(self):
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        tasks = self.todo.list_tasks()
        # Expecting the list method to return formatted strings with indices
        self.assertEqual(tasks, ["1. Task 1", "2. Task 2"])

    def test_remove_nonexistent_task(self):
        self.todo.add_task("Task 1")
        self.todo.remove_task("Task 2")  # Task 2 does not exist
        self.assertIn("Task 1", self.todo.tasks)  # Task 1 should still exist

if __name__ == '__main__':
    unittest.main()