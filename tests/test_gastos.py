
from src.gastos import (
    adicionar_gasto,
    calcular_total,
    listar_gastos,
    remover_gasto,
    resumo_por_categoria,
)

import pytest

@pytest.fixture
def gastos_exemplo():
    gastos = []
    adicionar_gasto(gastos, "Almoço", 35.50, "Alimentação", "2024-01-10")
    adicionar_gasto(gastos, "Ônibus", 5.00, "Transporte", "2024-01-10")
    adicionar_gasto(gastos, "Mercado", 120.00, "Alimentação", "2024-01-11")
    return gastos

def test_adicionar_gasto_valido():
    gastos = []
    gasto = adicionar_gasto(gastos, "Café", 8.50, "Alimentação")
    assert len(gastos) == 1
    assert gasto["descricao"] == "Café"
    assert gasto["valor"] == 8.50
    assert gasto["categoria"] == "Alimentação"


def test_listar_todos_os_gastos(gastos_exemplo):
    resultado = listar_gastos(gastos_exemplo)
    assert len(resultado) == 3


def test_listar_gastos_por_categoria(gastos_exemplo):
    resultado = listar_gastos(gastos_exemplo, "Alimentação")
    assert len(resultado) == 2
    assert all(g["categoria"] == "Alimentação" for g in resultado)


def test_remover_gasto_existente(gastos_exemplo):
    removido = remover_gasto(gastos_exemplo, 1)
    assert removido is True
    assert len(gastos_exemplo) == 2


def test_calcular_total(gastos_exemplo):
    total = calcular_total(gastos_exemplo)
    assert total == pytest.approx(160.50)


def test_resumo_por_categoria(gastos_exemplo):
    resumo = resumo_por_categoria(gastos_exemplo)
    assert resumo["Alimentação"] == pytest.approx(155.50)
    assert resumo["Transporte"] == pytest.approx(5.00)

def test_adicionar_gasto_valor_negativo():
    gastos = []
    with pytest.raises(ValueError, match="maior que zero"):
        adicionar_gasto(gastos, "Teste", -10.0, "Outros")


def test_adicionar_gasto_valor_zero():
    gastos = []
    with pytest.raises(ValueError, match="maior que zero"):
        adicionar_gasto(gastos, "Teste", 0, "Outros")


def test_adicionar_gasto_descricao_vazia():
    gastos = []
    with pytest.raises(ValueError, match="descrição"):
        adicionar_gasto(gastos, "   ", 10.0, "Outros")


def test_adicionar_gasto_categoria_vazia():
    gastos = []
    with pytest.raises(ValueError, match="categoria"):
        adicionar_gasto(gastos, "Teste", 10.0, "   ")

def test_remover_gasto_inexistente(gastos_exemplo):
    removido = remover_gasto(gastos_exemplo, 999)
    assert removido is False
    assert len(gastos_exemplo) == 3


def test_calcular_total_lista_vazia():
    assert calcular_total([]) == 0.0


def test_listar_categoria_inexistente(gastos_exemplo):
    resultado = listar_gastos(gastos_exemplo, "Lazer")
    assert resultado == []


def test_resumo_lista_vazia():
    assert resumo_por_categoria([]) == {}
