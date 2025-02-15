"""
Pruebas de la clse de ArbolRojinegro
"""
import pytest

from ArbolesRojinegros import ArbolRojinegro
from data.RojinegroGenerator import RojinegroGenerador


@pytest.fixture
def gen_arboles():
    gen = RojinegroGenerador()
    return gen.ejemplo1(), gen.ejemplo2(), gen.ejemplo3(), gen.ejemplo4()


def test_recorridos(gen_arboles):
    arb1, arb2, arb3, arb4 = gen_arboles
    assert arb1.bfs() == "2 1 4 3 5"
    assert arb1.inorden() == "1 2 3 4 5"

    assert arb2.bfs() == "5 1 8 6 9"
    assert arb2.inorden() == "1 5 6 8 9"

    assert arb3.bfs() == "4 2 5 1 3"
    assert arb3.inorden() == "1 2 3 4 5"

    assert arb4.bfs() == "8 5 9 1 6"
    assert arb4.inorden() == "1 5 6 8 9"


def test_insertar():
    num = [8, 7, 6, 12, 10, 9, 11, 14, 15, 13]
    instancia = ArbolRojinegro(None, None, None, None)

    for n in num:
        instancia.insertar(n)

    assert instancia.bfs(), "10 7 12 6 8 11 14 9 13 15"
    assert instancia.inorden(), "6 7 8 9 10 11 12 13 14 15"

    numB = [20, 22, 1, 2, 3, 9, 14, 17, 0, 33, 7, 13, 19]
    instanciaB = ArbolRojinegro(None, None, None, None)

    for n in numB:
        instanciaB.insertar(n)

    assert instanciaB.bfs(), "9 2 20 1 3 14 22 0 7 13 17 33 19"
    assert instanciaB.inorden(), "0 1 2 3 7 9 13 14 17 19 20 22 33"


def test_maximo(gen_arboles):
    arb1, arb2, arb3, arb4 = gen_arboles
    assert arb1.maximo() == 5
    assert arb2.maximo() == 9
    assert arb3.maximo() == 5
    assert arb4.maximo() == 9


def test_minimo(gen_arboles):
    arb1, arb2, arb3, arb4 = gen_arboles

    assert arb1.minimo() == 1
    assert arb2.minimo() == 1
    assert arb3.minimo() == 1
    assert arb4.minimo() == 1


def test_search(gen_arboles):
    arb1, arb2, arb3, arb4 = gen_arboles

    assert arb1.search(5).getValor() == 1
    assert arb2.search(6).getValor() == 6
    assert arb3.search(3).getValor() == 1
    assert arb4.search(9).getValor() == 1


def test_rotacionIzquierda(gen_arboles):
    arb1, arb2, _, _ = gen_arboles

    # Execute
    arb1.rotacionIzquierda(4)

    # Assert
    assert arb1.bfs() == "4 2 5 1 3"

    # Execute
    arb2.rotacionIzquierda(8)

    # Assert
    assert arb2.bfs() == "8 5 9 1 6"


def test_rotacionDerecha(gen_arboles):
    _, _, arb3, arb4 = gen_arboles

    # Execute
    arb3.rotacionDerecha(4)

    #  Assert
    assert arb3.bfs() == "2 1 4 3 5"

    # Execute
    arb4.rotacionIzquierda(8)

    # Assert
    assert arb4.bfs() == "5 1 8 6 9"
