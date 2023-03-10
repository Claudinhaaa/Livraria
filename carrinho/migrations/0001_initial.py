# Generated by Django 4.1.4 on 2023-01-11 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livro', '0003_alter_livro_imagem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Carrinhos',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200, null=True, verbose_name='Rua')),
                ('numero', models.CharField(max_length=10, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=50, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=100, null=True, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9, null=True, verbose_name='CEP')),
            ],
            options={
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField(null=True, verbose_name='Quantidade')),
                ('preco', models.FloatField(null=True, verbose_name='Preço')),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrinho.carrinho', verbose_name='Item do carrinho')),
                ('livro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='livro.livro', verbose_name='Livro')),
            ],
            options={
                'verbose_name_plural': 'Itens do carrinho',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome completo')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data nascimento')),
                ('cpf', models.CharField(max_length=18, null=True, verbose_name='CPF')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carrinho.endereco', verbose_name='Endereco')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.AddField(
            model_name='carrinho',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrinho.cliente', verbose_name='Cliente'),
        ),
    ]
