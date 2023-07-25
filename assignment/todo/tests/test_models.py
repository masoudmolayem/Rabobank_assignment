from django.test import TestCase
from todo.models import Task


class TaskModelTestCase(TestCase):
    def test_task_creation(self):
        # Create a test task
        task = Task.objects.create(
            name='Test Task',
            description='This is a test task',
        )

        # Check if the task was created successfully
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.description, 'This is a test task')
        self.assertEqual(task.status, 'Pending')
        self.assertIsNotNone(task.created_at)
        self.assertIsNotNone(task.updated_at)

    def test_task_str_representation(self):
        # Create a test task
        task = Task.objects.create(
            name='Test Task',
            description='This is a test task',
        )

        # Check if the string representation of the task is correct
        self.assertEqual(str(task), 'Test Task')
