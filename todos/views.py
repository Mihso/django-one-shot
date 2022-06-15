from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from todos.models import TodoList
from django.urls import reverse_lazy

# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
    

class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"

class TodoCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = ["name"]
    def get_success_url(self):
        return reverse_lazy("show_todolist",args = [self.object.id])

class TodoUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/update.html"
    fields = ["name"]
    def get_success_url(self):
        return reverse_lazy("show_todolist",args = [self.object.id])