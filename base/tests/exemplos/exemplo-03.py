def somar(primeiro_numero: float, segundo_numero: float) -> float:
    return primeiro_numero + segundo_numero


def teste_somar_2_e_3():
    resultado = somar(2, 3)

    assert resultado == 5


def teste_somar_3_e_5():
    resultado = somar(3, 5)

    assert resultado == 8
