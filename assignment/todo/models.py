from django.db import models


# Create your models here.

class Task(models.Model):
    """
    Model representing a task in the Todo List app.

    Attributes:
        name (str): The name of the task. Limited to a maximum of 200 characters.
        description (str, optional): A description of the task. Can be blank and nullable.
        status (str): The status of the task. Choices are 'Pending', 'Completed', or 'Deleted'.
                     Default value is 'Pending'.
        created_at (datetime): The date and time when the task was created. Automatically set to the current
                               date and time when the task is created.
        updated_at (datetime): The date and time when the task was last updated. Automatically updated to the
                               current date and time whenever the task is saved.

    Methods:
        __str__: Returns a string representation of the task (the task's name).

    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Deleted', 'Deleted'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
