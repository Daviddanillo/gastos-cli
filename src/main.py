"""Interface CLI do Gerenciador de Gastos Pessoais."""

from src.gastos import (
    adicionar_gasto,
    calcular_total,
    carregar_dados,
    listar_gastos,
    remover_gasto,
    resumo_por_categoria,
    salvar_dados,
)
from src.noticias import buscar_noticias_economicas


def exibir_menu() -> None:
    print("\n" + "=" * 40)
    print("    Gerenciador de Gastos")
    print("=" * 40)
    print("  1. Adicionar gasto")
    print("  2. Listar gastos")
    print("  3. Remover gasto")
    print("  4. Resumo por categoria")
    print("  5. Ver total gasto")
    print("  6. Resumo econômico do dia")
    print("  0. Sair")
    print("=" * 40)


def exibir_gastos(gastos: list[dict]) -> None:
    if not gastos:
        print("\n  Nenhum gasto registrado.")
        return
    print(f"\n  {'ID':<5} {'Data':<12} {'Categoria':<15} {'Descrição':<25} {'Valor':>10}")
    print("  " + "-" * 70)
    for g in gastos:
        print(
            f"  {g['id']:<5} {g['data']:<12} {g['categoria']:<15} "
            f"{g['descricao']:<25} R$ {g['valor']:>8.2f}"
        )


def fluxo_adicionar(gastos: list[dict]) -> None:
    print("\n  --- Adicionar Gasto ---")
    descricao = input("  Descrição: ").strip()
    categoria = input("  Categoria (ex: alimentação, transporte): ").strip()
    valor_str = input("  Valor (R$): ").strip().replace(",", ".")
    try:
        valor = float(valor_str)
        gasto = adicionar_gasto(gastos, descricao, valor, categoria)
        print(f"\n  Gasto adicionado! ID #{gasto['id']} — R$ {gasto['valor']:.2f}")
    except ValueError as e:
        print(f"\n  Erro: {e}")


def fluxo_listar(gastos: list[dict]) -> None:
    filtro = input("\n  Filtrar por categoria? (Enter para ver todos): ").strip()
    resultado = listar_gastos(gastos, filtro or None)
    exibir_gastos(resultado)


def fluxo_remover(gastos: list[dict]) -> None:
    print("\n  --- Remover Gasto ---")
    try:
        gasto_id = int(input("  ID do gasto a remover: "))
        if remover_gasto(gastos, gasto_id):
            print(f"  Gasto #{gasto_id} removido.")
        else:
            print(f"  Gasto #{gasto_id} não encontrado.")
    except ValueError:
        print("  ID inválido.")


def fluxo_resumo(gastos: list[dict]) -> None:
    resumo = resumo_por_categoria(gastos)
    if not resumo:
        print("\n  Nenhum gasto registrado.")
        return
    print("\n  --- Resumo por Categoria ---")
    for cat, total in sorted(resumo.items(), key=lambda x: -x[1]):
        print(f"  {cat:<20} R$ {total:>8.2f}")


def fluxo_noticias() -> None:
    """Busca e exibe as principais notícias econômicas do dia."""
    print("\n  --- Resumo Econômico do Dia ---")
    print("  Buscando notícias...")
    try:
        noticias = buscar_noticias_economicas()
        if not noticias:
            print("  Nenhuma notícia encontrada no momento.")
            return
        for i, n in enumerate(noticias, 1):
            print(f"\n  [{i}] {n['titulo']}")
            print(f"      Fonte: {n['fonte']}")
    except ValueError as e:
        print(f"\n  Configuração pendente: {e}")
        print("  Dica: defina a variável de ambiente NEWSAPI_KEY com sua chave gratuita.")
    except ConnectionError as e:
        print(f"\n  Não foi possível buscar notícias: {e}")


def main() -> None:
    gastos = carregar_dados()

    while True:
        exibir_menu()
        opcao = input("\n  Escolha uma opção: ").strip()

        if opcao == "1":
            fluxo_adicionar(gastos)
            salvar_dados(gastos)
        elif opcao == "2":
            fluxo_listar(gastos)
        elif opcao == "3":
            fluxo_remover(gastos)
            salvar_dados(gastos)
        elif opcao == "4":
            fluxo_resumo(gastos)
        elif opcao == "5":
            total = calcular_total(gastos)
            print(f"\n  Total gasto: R$ {total:.2f}")
        elif opcao == "6":
            fluxo_noticias()
        elif opcao == "0":
            print("\n  Até logo! \n")
            break
        else:
            print("\n  Opção inválida.")


if __name__ == "__main__":
    main()
