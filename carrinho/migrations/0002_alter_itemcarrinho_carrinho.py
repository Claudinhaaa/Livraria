# Generated by Django 4.1.4 on 2023-01-12 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='carrinho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='carrinho.carrinho', verbose_name='Item do carrinho'),
        ),
    ]
