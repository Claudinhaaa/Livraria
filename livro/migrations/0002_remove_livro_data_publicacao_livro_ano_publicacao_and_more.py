# Generated by Django 4.1.4 on 2023-01-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='data_publicacao',
        ),
        migrations.AddField(
            model_name='livro',
            name='ano_publicacao',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ano de publicação'),
        ),
        migrations.AddField(
            model_name='livro',
            name='qtde_paginas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade de páginas'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='livro/livro'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo_original',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título original'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Valor'),
        ),
    ]
