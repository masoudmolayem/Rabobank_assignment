
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
import json

from .models import Task

class TaskView(View):
    model = Task
    def get(self, request):
        task = get_object_or_404(self.model, pk=request.GET["id"])
        data = {
            'id': task.pk,
            'title': task.name,
            'description': task.description,
            'status': task.status
        }
        return JsonResponse(data, safe=False)

    def post(self, request):
        data = request.POST
        # data = json.loads(request.body)
        task = self.model.objects.create(
            name=data['title'],
            description=data['description'],
            status="Pending"
        )
        return JsonResponse({'id': task.id}, status=201)

    def put(self, request):
        data = json.loads(request.body)
        task = get_object_or_404(self.model, pk=data["id"])
        task.name = data['title']
        task.description = data['description']
        task.status = data['status']
        task.save()
        return JsonResponse({'id': task.pk})

    def delete(self, request):
        data = json.loads(request.body)
        task = get_object_or_404(self.model, pk=data["id"])
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=204)

def pending_tasks(request):
    tasks = Task.objects.filter(status="Pending")
    data = [
        {
            'id': task.id,
            'title': task.name,
            'description': task.description,
            "status" : task.status
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)

def completed_tasks(request):
    tasks = Task.objects.filter(status="Completed")
    data = [
        {
            'id': task.id,
            'title': task.name,
            'description': task.description,
            "status" : task.status
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)

def deleted_tasks(request):
    tasks = Task.objects.filter(status="Deleted")
    data = [
        {
            'id': task.id,
            'title': task.name,
            'description': task.description,
            "status" : task.status
        }
        for task in tasks
    ]
    return JsonResponse(data, safe=False)