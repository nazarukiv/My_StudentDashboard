from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    CATEGORY_CHOICES = [
        ('college', 'College'),
        ('study', 'Study'),
        ('fitness', 'Fitness'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to the user
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='college')

    def __str__(self):
        return f"{self.title} [{self.category}]"


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    assignment = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.subject} - {self.assignment}: {self.grade}"

from django.db import models
from django.contrib.auth.models import User


class Pomodoro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    duration_minutes = models.PositiveIntegerField(default=25)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_name} ({self.duration_minutes} mins)"