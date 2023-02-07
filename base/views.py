from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from base.forms import NovoUsuarioForm
from livro.models import Livro


def home(request):
    livros = Livro.objects.all()[:5]

    dados = {"livros": livros}

    return render(request, "base/home.html", dados)


def sobre(request):


    return render(request, "base/sobre.html")

def registrar(request):
    form = NovoUsuarioForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Usuário registrado com sucesso.")

        return redirect("base:login")

    messages.error(request, "Falha ao registrar usuário. Informações inválidas.")

    return render(
        request=request,
        template_name="registration/registrar.html",
        context={"form": form}
    )
