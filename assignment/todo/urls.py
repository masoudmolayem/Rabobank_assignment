from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.TaskView.as_view(), name="task"),
    path("pending_tasks/", views.pending_tasks, name="pending_tasks"),
    path("completed_tasks/", views.completed_tasks, name="completed_tasks"),
    path("deleted_tasks/", views.deleted_tasks, name="deleted_tasks"),

]
