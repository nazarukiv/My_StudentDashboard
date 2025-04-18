from django.db import models

# Create your models here.

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('college', 'College'),
        ('study', 'Study'),
        ('fitness', 'Fitness'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='college')

    def __str__(self):
        return f"{self.title} [{self.category}]"
