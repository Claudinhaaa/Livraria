# Generated by Django 4.1.4 on 2023-01-07 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Editoras',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('titulo_original', models.CharField(max_length=200, verbose_name='Título original')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('isbn', models.CharField(help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>", max_length=13, unique=True, verbose_name='ISBN')),
                ('data_publicacao', models.DateField(blank=True, null=True, verbose_name='Data de publicação')),
                ('edicao', models.CharField(blank=True, max_length=200, null=True, verbose_name='Edição')),
                ('genero', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gênero textual')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor')),
                ('imagem', models.ImageField(blank=True, upload_to='livro/livro')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livros', to='livro.categoria', verbose_name='Categoria')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='livro.editora', verbose_name='Editora')),
            ],
            options={
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='TipoParticipacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
            ],
            options={
                'verbose_name_plural': 'Tipos de participação',
            },
        ),
        migrations.CreateModel(
            name='Participacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacoes', to='livro.livro', verbose_name='Livro')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacoes', to='livro.pessoa', verbose_name='Pessoa')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='livro.tipoparticipacao', verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'Participações',
            },
        ),
    ]
