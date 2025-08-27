from django.contrib import admin

# Register your models here.
from .models import Priority, Category, Task, Note, SubTask

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("priority_name",)
    search_fields = ("priority_name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_title", "task_status", "task_deadline", "task_priority", "task_category")
    list_filter = ("task_status", "task_priority", "task_category")
    search_fields = ("task_title", "task_description")

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("note_task", "note_content", "created_at",)
    list_filter = ("created_at",)
    search_fields = ("note_content",)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("sub_title", "sub_status", "get_parent_task_name",)
    list_filter = ("sub_status",)
    search_fields = ("sub_title",)

    def get_parent_task_name(self, obj):
        try:
            sub_parent_task = Task.objects.get(id=obj.sub_parent_task_id)
            return sub_parent_task.task_title
        except Task.DoesNotExist:
            return None