from django import forms
from django.forms import ModelForm

from livro.models import Livro


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = [
            "titulo",
        ]


class BuscarForm(forms.Form):
    isbn = forms.CharField(
        label="ISBN",
        required=True,
        min_length=13,
        max_length=13,
    )
