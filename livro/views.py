from django.shortcuts import render, redirect

from livro.facade import buscar_no_google_books, criar_livro_do_google_books
from livro.forms import BuscarForm, LivroForm
from livro.models import Livro


def buscar(request):
    form = BuscarForm(request.POST or None)

    resultado = None
    resultado_titulo = None

    if form.is_valid():
        isbn = form.cleaned_data["isbn"]

        if isbn:
            r_json = buscar_no_google_books(isbn)
            livros = r_json.get("items")
            if livros:
                novo_livro = criar_livro_do_google_books(isbn=isbn, json=livros[0])
                resultado = novo_livro.__dict__
                resultado_titulo = novo_livro.titulo

    contexto = {
        "form": form,
        "resultado": resultado,
        "resultado_titulo": resultado_titulo,
    }

    return render(request, "livro/buscar.html", contexto)


def todos(request):
    livros = Livro.objects.all()

    busca = request.POST.get('busca')
    if busca:
        livros = livros.filter(titulo__icontains=busca)

    dados = {
        "livros": livros,
        "busca": busca
    }

    return render(request, "livro/listagem.html", dados)


def novo(request):
    dados = {}

    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form

    return render(request, "livro/form.html", dados)


def excluir(request, pk):
    livro = Livro.objects.get(pk=pk)
    livro.delete()

    return redirect("livro/todos")


def atualizar(request, pk):
    dados = {}
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("url_listagem")

    dados["form"] = form
    dados["livro"] = livro
    return render(request, "livro/form.html", dados)


def vermais(request, pk):
    dados = {}
    livro = Livro.objects.get(pk=pk)
    dados["livro"] = livro
    return render(request, "livro/vermais.html", dados)

