import requests

from config.settings import GOOGLE_API_KEY, GOOGLE_BOOKS_URL
from livro.models import Livro, Editora


def buscar_no_google_books(search: str) -> dict:
    params = {
        "key": GOOGLE_API_KEY,
        "q": f"isbn:{search}"
    }

    r = requests.get(f"{GOOGLE_BOOKS_URL}/volumes/", params=params)

    return r.json()


def criar_livro_do_google_books(isbn: str, json: dict):
    novo_livro = {"isbn": isbn}
    info = json.get("volumeInfo")

    if info:
        novo_livro["titulo"] = info.get("title")
        novo_livro["descricao"] = info.get("description")
        novo_livro["ano_publicacao"] = info.get("publishedDate", "")[-4:]
        novo_livro["qtde_paginas"] = info.get("pageCount")

    if novo_livro["titulo"]:
        editora, _ = Editora.objects.get_or_create(nome="Genérica")

        return Livro.objects.create(
            editora=editora,
            **novo_livro,
        )

    return None
