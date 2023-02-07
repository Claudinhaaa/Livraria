from django.urls import path
from carrinho import views

app_name = "carrinho"

urlpatterns = [
    path("ver/", views.ver, name="ver"),
    path("adicionar/<int:pk>", views.adicionar, name="adicionar"),
    path("remover/<int:pk>", views.remover, name="remover"),
]
