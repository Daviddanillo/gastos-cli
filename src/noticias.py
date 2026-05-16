"""Integração com a NewsAPI para exibir resumo econômico do dia."""

import os

import requests

NEWSAPI_URL = "https://newsapi.org/v2/everything"
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "0315b6055a57461bb41004994dd2abe8")
TIMEOUT = 5


def buscar_noticias_economicas(api_key: str = NEWSAPI_KEY, quantidade: int = 3) -> list[dict]:
    """Busca as principais notícias econômicas do dia via NewsAPI.

    Args:
        api_key: Chave da NewsAPI.
        quantidade: Número de notícias a retornar.

    Returns:
        Lista de dicionários com 'titulo' e 'fonte'.

    Raises:
        ValueError: Se a API key estiver vazia.
        ConnectionError: Se a requisição falhar.
    """
    if not api_key:
        raise ValueError("NEWSAPI_KEY não configurada. Defina a variável de ambiente.")

    params = {
        "q": "economia brasil finanças",
        "language": "pt",
        "sortBy": "publishedAt",
        "pageSize": quantidade,
        "apiKey": api_key,
    }

    try:
        response = requests.get(NEWSAPI_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()
        dados = response.json()

        if dados.get("status") != "ok":
            raise ConnectionError(f"Erro da API: {dados.get('message', 'desconhecido')}")

        artigos = dados.get("articles", [])
        return [
            {
                "titulo": a.get("title", "Sem título"),
                "fonte": a.get("source", {}).get("name", "Desconhecida"),
            }
            for a in artigos
        ]

    except requests.exceptions.Timeout:
        raise ConnectionError("Tempo de conexão esgotado ao acessar a NewsAPI.")
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Sem conexão com a internet.")
    except requests.exceptions.HTTPError as e:
        raise ConnectionError(f"Erro HTTP: {e}")
