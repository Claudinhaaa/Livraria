from django.urls import path

from . import views

app_name = "livro"

urlpatterns = [
    path("buscar", views.buscar, name="buscar"),
    path("todos", views.todos, name="todos"),
    path("novo", views.novo, name="novo"),
    path("excluir/<int:pk>", views.excluir, name="excluir"),
    path("atualizar/<int:pk>", views.atualizar, name="atualizar"),
    path("vermais/<int:pk>", views.vermais, name="vermais"),
]
