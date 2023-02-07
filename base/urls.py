from django.urls import path, include

from . import views
from .views import home, sobre

app_name = "base"

urlpatterns = [
    path("contas/", include("django.contrib.auth.urls")),
    path("contas/registrar/", views.registrar, name="register"),
    path("", home, name="home"),
    path("sobre/", sobre, name="sobre")
]
