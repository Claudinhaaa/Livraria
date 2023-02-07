from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from carrinho.models import Carrinho, ItemCarrinho, Cliente
from livro.models import Livro


@login_required(login_url="base:login")
def ver(request):
    if not request.user.is_authenticated:
        return redirect("base:login")

    carrinho = Carrinho.objects.filter(cliente__user=request.user).last()

    dados = {
        "carrinho": carrinho,
        "itens": carrinho.itens.all if carrinho else []
    }

    return render(request, "carrinho/ver.html", dados)


@login_required(login_url="base:login")
def adicionar(request, pk):
    cliente, _ = Cliente.objects.get_or_create(user=request.user)

    carrinho = Carrinho.objects.filter(cliente=cliente).last()

    if not carrinho:
        carrinho = Carrinho.objects.create(cliente=cliente)

    livro = Livro.objects.get(pk=pk)

    item_no_carrinho = carrinho.itens.filter(livro=livro).first()

    if item_no_carrinho:
        item_no_carrinho.quantidade += 1
        item_no_carrinho.save()
    else:
        ItemCarrinho.objects.create(
            carrinho=carrinho,
            livro=livro,
            quantidade=1,
            preco=livro.valor,
        )

    return redirect("carrinho:ver")


@login_required(login_url="base:login")
def remover(request, pk):
    carrinho = Carrinho.objects.filter(cliente__user=request.user).last()

    if not carrinho:
        carrinho = Carrinho.objects.create(cliente__user=request.user)

    livro = Livro.objects.get(pk=pk)

    item_no_carrinho = carrinho.itens.filter(livro=livro).first()

    if item_no_carrinho:
        item_no_carrinho.delete()

    return redirect("carrinho:ver")
