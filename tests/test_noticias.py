"""Testes de integração para o módulo de notícias econômicas."""

from unittest.mock import MagicMock, patch

import pytest

from src.noticias import buscar_noticias_economicas

# ---------------------------------------------------------------------------
# Dados simulados (mock) — não dependem de internet nem de API key real
# ---------------------------------------------------------------------------

RESPOSTA_MOCK = {
    "status": "ok",
    "totalResults": 2,
    "articles": [
        {
            "title": "Dólar cai frente ao real após dados do IPCA",
            "source": {"name": "Valor Econômico"},
        },
        {
            "title": "Bolsa fecha em alta puxada por commodities",
            "source": {"name": "InfoMoney"},
        },
    ],
}


# ---------------------------------------------------------------------------
# Testes
# ---------------------------------------------------------------------------


def test_buscar_noticias_retorna_lista(monkeypatch):
    """Verifica que a função retorna uma lista com os campos corretos."""
    mock_response = MagicMock()
    mock_response.json.return_value = RESPOSTA_MOCK
    mock_response.raise_for_status = MagicMock()

    with patch("src.noticias.requests.get", return_value=mock_response):
        resultado = buscar_noticias_economicas(api_key="fake-key-teste")

    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[0]["titulo"] == "Dólar cai frente ao real após dados do IPCA"
    assert resultado[0]["fonte"] == "Valor Econômico"


def test_buscar_noticias_campos_presentes(monkeypatch):
    """Verifica que cada notícia possui os campos 'titulo' e 'fonte'."""
    mock_response = MagicMock()
    mock_response.json.return_value = RESPOSTA_MOCK
    mock_response.raise_for_status = MagicMock()

    with patch("src.noticias.requests.get", return_value=mock_response):
        resultado = buscar_noticias_economicas(api_key="fake-key-teste")

    for noticia in resultado:
        assert "titulo" in noticia
        assert "fonte" in noticia


def test_buscar_noticias_sem_api_key():
    """Verifica que ValueError é levantado quando a API key está vazia."""
    with pytest.raises(ValueError, match="NEWSAPI_KEY"):
        buscar_noticias_economicas(api_key="")


def test_buscar_noticias_timeout():
    """Verifica que ConnectionError é levantado em caso de timeout."""
    import requests as req

    with patch("src.noticias.requests.get", side_effect=req.exceptions.Timeout):
        with pytest.raises(ConnectionError, match="Tempo de conexão"):
            buscar_noticias_economicas(api_key="fake-key-teste")


def test_buscar_noticias_sem_internet():
    """Verifica que ConnectionError é levantado quando não há conexão."""
    import requests as req

    with patch("src.noticias.requests.get", side_effect=req.exceptions.ConnectionError):
        with pytest.raises(ConnectionError, match="internet"):
            buscar_noticias_economicas(api_key="fake-key-teste")


def test_buscar_noticias_status_erro():
    """Verifica que ConnectionError é levantado quando a API retorna status de erro."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "error", "message": "apiKey inválida"}
    mock_response.raise_for_status = MagicMock()

    with patch("src.noticias.requests.get", return_value=mock_response):
        with pytest.raises(ConnectionError, match="Erro da API"):
            buscar_noticias_economicas(api_key="fake-key-errada")
