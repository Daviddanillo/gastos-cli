# Gastos CLI

[![CI](https://github.com/Daviddanillo/gastos-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/Daviddanillo/gastos-cli/actions/workflows/ci.yml)
![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-yellow)
![Licença](https://img.shields.io/badge/licença-MIT-green)

---

## Descrição do Problema

O descontrole financeiro pessoal vem sendo uma das principais causas de endividamento no Brasil. Segundo o Banco Central, mais de 70%(aproximadamente 77%) dos brasileiros não acompanham seus gastos de forma regular. A ausência de um controle simples e acessível faz com que muitas pessoas percam a noção de onde vai o dinheiro gasto, levando-a dívidas e dificuldades em economizar dinheiro.

## Proposta da Solução

O Gastos CLI é uma aplicação de linha de comando(CLI) que permite registrar, consultar e analisar gastos pessoais de forma simples e rápida. Sem necessidade de internet, cadastro ou aplicativos complexos — basta Python instalado. Os dados são salvos localmente em arquivo JSON.

## Público-Alvo

Qualquer pessoa que deseje ter um controle básico de suas finanças pessoais sem depender de aplicativos pagos ou conexão com internet.

---

## Funcionalidades

- Adicionar gasto com descrição, valor, categoria e data
- Listar todos os gastos ou filtrar por categoria
- Remover gasto por ID
- Ver resumo de gastos agrupados por categoria
- Calcular o total gasto
- Persistência automática em arquivo JSON
- Resumo econômico do dia (Integração com NewsAPI)

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3.11+ | Linguagem principal |
| JSON (stdlib) | Armazenamento de dados |
| pytest | Testes automatizados |
| ruff | Análise estática / linting |
| GitHub Actions | Pipeline de CI |

---

## Estrutura do Projeto

```
gastos-cli/
├── src/
│   ├── __init__.py
│   ├── gastos.py     
│   └── main.py         
├── tests/
│   ├── __init__.py
│   └── test_gastos.py 
├── .github/
│   └── workflows/
│       └── ci.yml     
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── pyproject.toml     
├── requirements.txt
└── README.md
```

---

## Instalação

Pré-requisitos: Python 3.11 ou superior.

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/gastos-cli.git
cd gastos-cli

# 2. (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# 3. Instale as dependências de desenvolvimento
pip install -r requirements.txt
```

---

## Execução

```bash
python -m src.main
```

Você verá o menu interativo:

```
╔══════════════════════════════════╗
║   Gerenciador de Gastos          ║
╠══════════════════════════════════╣
║  1. Adicionar gasto              ║
║  2. Listar gastos                ║
║  3. Remover gasto                ║
║  4. Resumo por categoria         ║
║  5. Ver total gasto              ║
║  0. Sair                         ║
╚══════════════════════════════════╝
```

**Exemplo de uso:**
```
  Escolha uma opção: 1
  Descrição: Almoço no trabalho
  Categoria: Alimentação
  Valor (R$): 32,50
  Gasto adicionado! ID #1 — R$ 32.50
```

---

## Rodando os Testes

```bash
pytest --tb=short -v
```

Saída esperada: **13 testes passando**, cobrindo caminho feliz, entradas inválidas e casos limite.

---

## Rodando o Lint

```bash
ruff check src/ tests/
```

Sem erros significa que o código está dentro do padrão de qualidade definido.

---

## CI com GitHub Actions

A cada `push` ou `pull request` na branch `main`, o pipeline executa automaticamente:

1. Checkout do código
2. Configuração do Python 3.11
3. Instalação das dependências
4. Lint com **ruff**
5. Testes com **pytest**

Veja o status do build no badge no topo deste README.

---

## Versão

**1.0.0** — veja [CHANGELOG.md](CHANGELOG.md) para o histórico de mudanças.
**2.0.0** — integração com NewsAPI para resumo econômico do dia.

---

## Deploy : https://replit.com/@daviddanillo07/gastos-cli

---
## Autor
David Danillo Gomes Braga  
