from django.forms import ModelForm
from django import forms
from .models import Priority, Category, Task, Note


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class NoteForm(ModelForm):
    class Meta:
        model =  Note
        fields = "__all__"
        