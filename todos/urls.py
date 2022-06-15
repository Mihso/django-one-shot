from django.urls import path
from todos.views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    )

urlpatterns = [
    path("",TodoListView.as_view(), name="list_todos"),
    path("<int:pk>/", TodoDetailView.as_view(), name="show_todolist"),
    path("create/", TodoCreateView.as_view(), name="create_todolist"),
    path("<int:pk>/edit", TodoUpdateView.as_view(), name="update_todolist"),
]