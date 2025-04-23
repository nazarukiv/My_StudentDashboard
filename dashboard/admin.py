from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "due_date", "is_completed")
    list_filter = ("category", "is_completed", "due_date")
    search_fields = ("title", "description", "user__username")