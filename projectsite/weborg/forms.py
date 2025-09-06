from django.forms import ModelForm
from django import forms
from .models import Priority


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"
