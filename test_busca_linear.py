import unittest

from busca_linear import busca_linear


class BuscaLinearTestes(unittest.TestCase):
    def test_encontra_alvo_e_conta_comparacoes(self) -> None:
        resultado = busca_linear([4, 8, 15, 16, 23, 42], 15)

        self.assertEqual(resultado.indice, 2)
        self.assertEqual(resultado.comparacoes, 3)

    def test_caso_de_alvo_ausente_verifica_toda_a_lista(self) -> None:
        resultado = busca_linear([10, 20, 30], 99)

        self.assertEqual(resultado.indice, -1)
        self.assertEqual(resultado.comparacoes, 3)


if __name__ == "__main__":
    unittest.main()
