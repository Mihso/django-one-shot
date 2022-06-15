from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from todos.models import TodoList

# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    

class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"
