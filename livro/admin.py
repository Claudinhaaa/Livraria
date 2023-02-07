from django.contrib import admin
from .models import *


@admin.register(TipoParticipacao)
class TipoParticipacaoAdmin(admin.ModelAdmin):
    ...


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    ...


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...


@admin.register(Participacao)
class ParticipacaoAdmin(admin.ModelAdmin):
    ...

