from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Task
import json


#
class TestTask(TestCase):
    """
   Test cases for views in the app.
   """

    def setUp(self) -> None:
        """
        Set up the test environment.
        """
        self.client = Client()
        self.url_task = reverse("task")
        self.task = Task.objects.create(
            name="task1",
            description="description of task1",
            status="Pending"
        )

    def test_task_get(self):
        get_url = self.url_task + "?id={}".format(self.task.id)
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {'id': self.task.pk,
                          'title': self.task.name,
                          'description': self.task.description,
                          'status': self.task.status}
                         )

    def test_task_post(self):
        new_task = {
            "title": "task_test",
            "description": "new task description",
        }
        response = self.client.post(self.url_task, data=new_task)
        self.assertEqual(response.status_code, 201)
        inserted_task = Task.objects.get(id=response.json()["id"])
        self.assertEqual(inserted_task.id, response.json()["id"])
        self.assertEqual(inserted_task.name, new_task["title"])
        self.assertEqual(inserted_task.description, new_task["description"])
        self.assertEqual(inserted_task.status, "Pending")

    def test_task_put(self):
        new_task = {
            "id": self.task.id,
            "title": "task_test_put",
            "description": "new task description put",
            "status": "Completed"
        }
        data_json = json.dumps(new_task)
        response = self.client.put(self.url_task, data_json)
        self.assertEqual(response.status_code, 200)
        updated_task = Task.objects.get(id=response.json()["id"])
        self.assertEqual(updated_task.id, new_task["id"])
        self.assertEqual(updated_task.name, new_task["title"])
        self.assertEqual(updated_task.description, new_task["description"])
        self.assertEqual(updated_task.status, new_task["status"])

    def test_task_delete(self):
        task_id = self.task.id
        data = {
            "id": task_id
        }
        json_data = json.dumps(data)
        response = self.client.delete(self.url_task, json_data)
        self.assertEqual(response.status_code, 200)
        t = Task.objects.get(pk=task_id)
        self.assertEqual(t.status, "Deleted")

    # (other) test cases for edges
    def test_get_task_with_non_existent_id(self):
        get_url = self.url_task + "?id={}".format(9999)
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, 404)

    def test_get_task_without_sending_id(self):
        response = self.client.get(self.url_task)
        self.assertEqual(response.status_code, 400)

    def test_task_post_wrong_data(self):
        new_task = {
            "description": "new task description",
        }
        response = self.client.post(self.url_task, data=new_task)
        self.assertEqual(response.status_code, 400)

    def test_task_post_wrong_data2(self):
        new_task = {
            "title": "new task",
        }
        response = self.client.post(self.url_task, data=new_task)
        self.assertEqual(response.status_code, 400)

    def test_update_task_with_non_existent_id(self):
        data = {
            'id': 9999,  # A non-existent ID
            'title': 'Updated Task',
            'description': 'Updated task description',
            'status': 'Completed'
        }
        response = self.client.put(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_update_task_missing_data(self):
        data = {
            'title': 'Updated Task',
            'description': 'Updated task description',
            'status': 'Completed'
        }
        response = self.client.put(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_task_missing_data1(self):
        data = {
            "id": self.task.id,
            'description': 'Updated task description',
            'status': 'Completed'
        }
        response = self.client.put(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_task_missing_data2(self):
        data = {
            "id": self.task.id,
            'title': 'Updated task',
            'status': 'Completed'
        }
        response = self.client.put(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_task_missing_data3(self):
        data = {
            "id": self.task.id,
            'title': 'Updated task',
            'description': 'Updated task description'
        }
        response = self.client.put(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_update_task_with_bad_status(self):
        data = {
            'id': self.task.id,  # A non-existent ID
            'title': 'Updated Task',
            'description': 'Updated task description',
            'status': 'badstatus'
        }
        response = self.client.put(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_task_with_non_existent_id(self):
        data = {
            'id': 9999,  # A non-existent ID
        }
        response = self.client.delete(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_task_without_sending_id(self):
        data = {}
        response = self.client.delete(self.url_task, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)


class TestTasksList(TestCase):
    """
        Test cases for views in the app.
   """

    def setUp(self) -> None:
        """
        Set up the test environment.
        """
        self.client = Client()
        Task.objects.create(
            name="task_completed",
            description="description",
            status="Completed"
        )
        Task.objects.create(
            name="task_deleted",
            description="description",
            status="Deleted"
        )
        Task.objects.create(
            name="task_pending",
            description="description",
            status="Pending"
        )

    def test_pending_tasks(self):
        res = self.client.get(reverse("pending_tasks"))
        json_result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(json_result), 1)
        for i in json_result:
            self.assertEqual(i["status"], "Pending")

    def test_completed_tasks(self):
        res = self.client.get(reverse("completed_tasks"))
        json_result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(json_result), 1)
        for i in json_result:
            self.assertEqual(i["status"], "Completed")

    def test_deleted_tasks(self):
        res = self.client.get(reverse("deleted_tasks"))
        json_result = res.json()
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(json_result), 1)
        for i in json_result:
            self.assertEqual(i["status"], "Deleted")
