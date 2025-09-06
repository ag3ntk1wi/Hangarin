from django.shortcuts import render
from django.views.generic.list import ListView
from weborg.models import Priority

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
