from django.contrib import admin

from task_manager.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'completed', 'created_at']
    list_filter = ['completed', 'created_at']
