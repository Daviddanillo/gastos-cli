"""Módulo principal de gerenciamento de gastos pessoais."""

import json
import os
from datetime import date

ARQUIVO_DADOS = "dados.json"


def carregar_dados(caminho: str = ARQUIVO_DADOS) -> list[dict]:
    """Carrega os gastos salvos do arquivo JSON."""
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(gastos: list[dict], caminho: str = ARQUIVO_DADOS) -> None:
    """Salva os gastos no arquivo JSON."""
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=2)


def adicionar_gasto(
    gastos: list[dict],
    descricao: str,
    valor: float,
    categoria: str,
    data: str | None = None,
) -> dict:
    """Adiciona um novo gasto à lista.

    Raises:
        ValueError: Se descrição vazia, valor negativo ou zero, ou categoria vazia.
    """
    descricao = descricao.strip()
    categoria = categoria.strip()

    if not descricao:
        raise ValueError("A descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    if not categoria:
        raise ValueError("A categoria não pode ser vazia.")

    gasto = {
        "id": len(gastos) + 1,
        "descricao": descricao,
        "valor": round(valor, 2),
        "categoria": categoria,
        "data": data or str(date.today()),
    }
    gastos.append(gasto)
    return gasto


def listar_gastos(gastos: list[dict], categoria: str | None = None) -> list[dict]:
    """Retorna a lista de gastos, opcionalmente filtrada por categoria."""
    if categoria:
        return [g for g in gastos if g["categoria"].lower() == categoria.lower()]
    return gastos


def remover_gasto(gastos: list[dict], gasto_id: int) -> bool:
    """Remove um gasto pelo ID. Retorna True se removido, False se não encontrado."""
    for i, g in enumerate(gastos):
        if g["id"] == gasto_id:
            gastos.pop(i)
            return True
    return False


def calcular_total(gastos: list[dict]) -> float:
    """Calcula o total de gastos."""
    return round(sum(g["valor"] for g in gastos), 2)


def resumo_por_categoria(gastos: list[dict]) -> dict[str, float]:
    """Retorna um dicionário com o total gasto por categoria."""
    resumo: dict[str, float] = {}
    for g in gastos:
        cat = g["categoria"]
        resumo[cat] = round(resumo.get(cat, 0) + g["valor"], 2)
    return resumo
