from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
import json

from .models import Task


class TaskView(View):
    """
        View for handling individual tasks in the Todo List app.

        Methods:
            get(request): Retrieve details of a specific task.
            post(request): Create a new task.
            put(request): Update an existing task.
            delete(request): Delete an existing task.

        Usage:
            # Example of using TaskView to handle task CRUD operations:
            # URL: /tasks/
            # URL with task ID: /tasks/?id=1

            # To retrieve the details of a specific task with ID 1:
            GET /tasks/?id=1

            # To create a new task:
            POST /tasks/
            Request Body: {"title": "Buy groceries", "description": "Remember to buy eggs and milk."}

            # To update the details of an existing task with ID 1:
            PUT /tasks/
            Request Body: {"id": 1, "title": "Buy groceries", "description": "Remember to buy eggs and milk.", "status": "Pending"}

            # To delete an existing task with ID 1:
            DELETE /tasks/
            Request Body: {"id": 1}
        """
    model = Task

    def get(self, request):
        """
             Retrieve details of a specific task.
        """
        if "id" not in request.GET:
            return JsonResponse({"message": "there is not id in variables"}, status=400)

        task = get_object_or_404(self.model, pk=request.GET["id"])
        data = {
            'id': task.pk,
            'title': task.name,
            'description': task.description,
            'status': task.status
        }
        return JsonResponse(data, safe=False)

    def post(self, request):
        """
            Create a new task.
        """
        data = request.POST
        if "title" not in data or "description" not in data:
            return JsonResponse({"message": "some information did not sent"}, status=400)
        task = self.model.objects.create(
            name=data['title'],
            description=data['description'],
            status="Pending"
        )
        return JsonResponse({'id': task.id}, status=201)

    def put(self, request):
        """
           Update an existing task.
       """
        data = json.loads(request.body)
        if "title" not in data or "description" not in data or "id" not in data or "status" not in data:
            return JsonResponse({"message": "some information did not sent"}, status=400)
        task = get_object_or_404(self.model, pk=data["id"])
        if data['status'] not in list(list(zip(*Task.STATUS_CHOICES))[0]):
            return JsonResponse({"error": "Invalid status provided for task update."}, status=400)

        task.name = data['title']
        task.description = data['description']
        task.status = data['status']
        task.save()
        return JsonResponse({'id': task.pk})

    def delete(self, request):
        """
            Delete an existing task.
        """
        data = json.loads(request.body)
        if "id" not in data:
            return JsonResponse({"message": "there is not id in variables"}, status=400)
        task = get_object_or_404(self.model, pk=data["id"])
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)


def pending_tasks(request):
    """
        View to retrieve a list of tasks with 'Pending' status.
    """
    tasks = Task.objects.filter(status="Pending")
    data = [
        {
            'id': task.id,
            'title': task.name,
            'description': task.description,
            "status": task.status
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)


def completed_tasks(request):
    """
        View to retrieve a list of tasks with 'Completed' status.
    """
    tasks = Task.objects.filter(status="Completed")
    data = [
        {
            'id': task.id,
            'title': task.name,
            'description': task.description,
            "status": task.status
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)


def deleted_tasks(request):
    """
        View to retrieve a list of tasks with 'Deleted' status.
    """
    tasks = Task.objects.filter(status="Deleted")
    data = [
        {
            'id': task.id,
            'title': task.name,
            'description': task.description,
            "status": task.status
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)
