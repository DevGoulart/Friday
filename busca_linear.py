"""Demonstração prática de um algoritmo O(N): busca linear."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

@dataclass(frozen=True)
class ResultadoBusca:

    indice: int
    comparacoes: int

def busca_linear(valores: list[int], alvo: int, mostrar_passos: bool = False) -> ResultadoBusca:
    """Procura o valor da esquerda para a direita."""
    for indice, valor in enumerate(valores, start=1):
        if mostrar_passos:
            print(f"Comparação {indice}: {valor} == {alvo}?")
        if valor == alvo:
            if mostrar_passos:
                print("Encontrado!")
            return ResultadoBusca(indice=indice - 1, comparacoes=indice)

    if mostrar_passos:
        print("O valor não está na lista.")
    return ResultadoBusca(indice=-1, comparacoes=len(valores))


def executar(valores: list[int], alvo: int, mostrar_passos: bool = False) -> None:
    """Executa um caso de teste e mostra o custo observado."""
    resultado = busca_linear(valores, alvo, mostrar_passos)

    print(f"Lista: {valores}")
    local = f"índice {resultado.indice}" if resultado.indice >= 0 else "não encontrado"
    print(f"Tamanho da lista (N): {len(valores)}")
    print(f"Alvo: {alvo} ({local})")
    print(f"Comparações realizadas: {resultado.comparacoes}")
    print("Conclusão: no pior caso, o número de comparações cresce na mesma proporção de N (O(N)).")


def main() -> None:
    parser = argparse.ArgumentParser(description="Demonstração de busca linear O(N).")
    parser.add_argument(
        "--lista",
        help="Números separados por vírgula, por exemplo: 8,3,12,5,20.",
    )
    parser.add_argument("--alvo", type=int, help="Número que será procurado.")
    parser.add_argument("--tamanho", type=int, default=10, help="Quantidade de elementos da lista.")
    parser.add_argument("--passos", action="store_true", help="Mostra cada comparação realizada.")
    parser.add_argument(
        "--ausente",
        action="store_true",
        help="Procura um valor ausente, exibindo o pior caso da busca.",
    )
    args = parser.parse_args()

    if args.lista:
        try:
            valores = [int(valor.strip()) for valor in args.lista.split(",") if valor.strip()]
        except ValueError:
            parser.error("--lista deve conter apenas números separados por vírgula")
    else:
        valores = list(range(args.tamanho))

    if not valores:
        parser.error("a lista deve conter pelo menos um número")

    if args.tamanho < 1:
        parser.error("--tamanho deve ser maior que zero")

    alvo = args.alvo
    if alvo is None:
        alvo = valores[-1] if not args.ausente else max(valores) + 1

    executar(valores, alvo, args.passos)


if __name__ == "__main__":
    main()
