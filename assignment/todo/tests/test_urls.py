from django.test import SimpleTestCase
from django.urls import resolve, reverse
from todo.views import *


class TestUrls(SimpleTestCase):
    def test_task(self):
        url = reverse("task")
        self.assertEqual(resolve(url).func.view_class, TaskView)

    def test_pending_tasks(self):
        url = reverse("pending_tasks")
        self.assertEqual(resolve(url).func, pending_tasks)

    def test_completed_tasks(self):
        url = reverse("completed_tasks")
        self.assertEqual(resolve(url).func, completed_tasks)

    def test_deleted_tasks(self):
        url = reverse("deleted_tasks")
        self.assertEqual(resolve(url).func, deleted_tasks)
