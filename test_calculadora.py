
# test_calculadora.py
import unittest

from calculadora import dividir, multiplicar, potencia, somar, subtrair


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        """Testa se a função multiplicar está funcionando corretamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

        """Cenários adicionados """
        self.assertEqual(multiplicar(7, 1), 7)
        self.assertAlmostEqual(multiplicar(0.1, 0.2), 0.02, places=7)
        

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia(self):
        """Testa se a função potencia está funcionando corretamente."""
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(3, 2), 9)

    def test_lista_vazia(self):
        """Testa se a função calcular_media retorna 0 para uma lista vazia."""
        from calculadora import calcular_media
        self.assertEqual(calcular_media([]), 0)

    def test_lista_com_numeros_inteiros(self):
        """Testa se a função calcular_media retorna a média correta para uma lista de números inteiros."""
        from calculadora import calcular_media
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)

    def test_lista_com_numeros_decimais(self):
        """Testa se a função calcular_media retorna a média correta para uma lista de números decimais."""
        from calculadora import calcular_media
        self.assertEqual(calcular_media([1.5, 2.5, 3.5]), 2.5)

    def test_lista_com_um_nuero(self):
        """Testa se a função calcular_media retorna o número quando a lista contém apenas um número."""
        from calculadora import calcular_media
        self.assertEqual(calcular_media([5]), 5)
        

if __name__ == "__main__":
    unittest.main()
