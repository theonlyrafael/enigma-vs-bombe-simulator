import unittest
from enigma.reflector import Reflector

class TestReflector(unittest.TestCase):

    # --- testes de exceções (__init__) ---

    def test_tamanho_invalido(self):
        # Trava 1: verifica se recusa fiação com menos ou mais de 26 letras
        with self.assertRaises(ValueError):
            Reflector(wiring="ABC")

    def test_letra_refletindo_nela_mesma(self):
        # Trava 2: garante que uma letra nunca reflete nela mesma
        with self.assertRaises(ValueError):
            Reflector(wiring="ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # cada letra reflete ela mesma

    # --- teste do método reflect ---
    
    def test_reflexao_basica(self):
        # usando a fiação do refletor "B" histórico
        reflector = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        
        # se entrar 'A' (índice 0), deve sair a primeira letra da string ('Y')
        self.assertEqual(reflector.reflect('A'), 'Y')
        
        # se entrar 'Y', deve sair 'A'
        self.assertEqual(reflector.reflect('Y'), 'A')

if __name__ == '__main__':
    unittest.main()