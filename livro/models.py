from django.db import models


class TipoParticipacao(models.Model):
    nome = models.CharField("Nome", max_length=200)

    class Meta:
        verbose_name_plural = "Tipos de participação"

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=200)

    class Meta:
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=200)
    descricao = models.TextField("Descrição", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Editora(models.Model):
    nome = models.CharField("Nome", max_length=200)

    class Meta:
        verbose_name_plural = "Editoras"

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=200)
    titulo_original = models.CharField(
        "Título original",
        max_length=200,
        blank=True,
        null=True,
    )
    descricao = models.TextField("Descrição", blank=True, null=True)
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>",
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Categoria",
        related_name="livros",
    )
    ano_publicacao = models.CharField(
        "Ano de publicação",
        max_length=200,
        blank=True,
        null=True,
    )
    qtde_paginas = models.IntegerField(
        "Quantidade de páginas",
        blank=True,
        null=True,
    )
    edicao = models.CharField("Edição", max_length=200, blank=True, null=True)
    genero = models.CharField("Gênero textual", max_length=200, blank=True, null=True)
    editora = models.ForeignKey(
        Editora,
        on_delete=models.CASCADE,
        verbose_name="Editora",
        related_name="livros",
    )
    valor = models.DecimalField("Valor", max_digits=7, decimal_places=2, default=0)
    imagem = models.ImageField(upload_to='livro/livro/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo


class Participacao(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        verbose_name="Livro",
        related_name="participacoes",
    )
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa",
        related_name="participacoes",
    )
    tipo = models.ForeignKey(
        TipoParticipacao,
        on_delete=models.SET_NULL,
        verbose_name="Tipo",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "Participações"

    def __str__(self):
        result = self.pessoa.nome

        if self.tipo:
            result += f" ({self.tipo.nome})"

        return result
