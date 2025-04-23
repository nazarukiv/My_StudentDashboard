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