from django.contrib import admin
from .models import *


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    ...


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...


@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    ...


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    ...
