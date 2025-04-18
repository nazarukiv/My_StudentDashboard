from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'is_completed']
    list_filter = ['is_completed']
    search_fields = ['title']

