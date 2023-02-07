from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, F

from livro.models import Livro


class Endereco(models.Model):
    rua = models.CharField("Rua", max_length=200, null=True)
    numero = models.CharField("Número", max_length=10, null=True)
    complemento = models.CharField(
        "Número",
        max_length=20,
        null=True,
        blank=True
    )
    bairro = models.CharField("Bairro", max_length=100, null=True)
    cidade = models.CharField("Cidade", max_length=50, null=True)
    estado = models.CharField("Estado", max_length=100, null=True)
    cep = models.CharField("CEP", max_length=9, null=True)

    class Meta:
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.rua


class Cliente(models.Model):
    user = models.OneToOneField(
        User,
        related_name='cliente',
        null=True,
        on_delete=models.CASCADE
    )
    nome = models.CharField("Nome completo", max_length=200)
    data_nascimento = models.DateField(
        "Data nascimento",
        blank=True,
        null=True
    )
    cpf = models.CharField("CPF", max_length=18, null=True)
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name = "Endereco",
    )
    telefone = models.CharField(
        "Nº telefone celular",
        max_length=11,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name="Cliente",
    )

    class Meta:
        verbose_name_plural = "Carrinhos"

    def __str__(self):
        if self.cliente:
            return self.cliente.nome

        return self.id

    @property
    def total(self) -> float:
        return self.itens.aggregate(
            total=Sum(F('quantidade') * F('preco'))
        )['total']


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho,
        related_name='itens',
        on_delete=models.CASCADE,
        verbose_name="Item do carrinho",
    )
    livro = models.ForeignKey(
        Livro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Livro",
    )
    quantidade = models.FloatField('Quantidade', null=True)
    preco = models.FloatField('Preço', null=True)

    class Meta:
        verbose_name_plural = "Itens do carrinho"

    def __str__(self):
        if self.carrinho and self.carrinho.cliente:
            return self.carrinho.cliente.nome

        return self.id
