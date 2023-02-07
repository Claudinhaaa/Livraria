import re

import pytest
from django.urls import reverse


@pytest.fixture
def resp(client, db):
    return client.get(reverse('base:home'))


def teste_o_status_code(resp):
    assert resp.status_code == 200


def teste_se_existe_livraria_no_titulo(resp):
    result = re.search("<title>(.*)</title>", resp.content.decode("utf-8"))

    assert "Livraria" in result.group(1)


def teste_se_existe_inicio_no_titulo(resp):
    result = re.search("<title>(.*)</title>", resp.content.decode("utf-8"))

    assert "Início" in result.group(1)
