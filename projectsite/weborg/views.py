from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from weborg.models import Priority
from weborg.forms import PriorityForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    model = Priority
    context_object_name = 'home'
    template_name = "home.html"

class PriorityList(ListView):
    model = Priority
    context_object_name = 'priority'
    template_name = 'priority_list.html'
    paginate_by = 5

class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')
