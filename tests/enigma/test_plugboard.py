import unittest
from enigma.plugboard import Plugboard

class TestPlugboard(unittest.TestCase):
    
    # --- Testes do caminho feliz (HAPPY PATH) ---

    def test_nenhuma_conexao(self):
        # se não há cabos, 'A' deve retornar 'A'
        plugboard = Plugboard()
        self.assertEqual(plugboard.swap('A'), 'A')

    def test_conexoes_validas(self):
        # conectando A com B, e C com D
        plugboard = Plugboard(["AB", "CD"])
        
        self.assertEqual(plugboard.swap('A'), 'B')
        self.assertEqual(plugboard.swap('B'), 'A')
        self.assertEqual(plugboard.swap('C'), 'D')
        
        # 'Z' não está conectado, deve retornar 'Z'
        self.assertEqual(plugboard.swap('Z'), 'Z')

    # --- Testes do caminho triste(SAD PATH / EXCEÇÕES) ---

    def test_tamanho_invalido(self):
        # Trava 1: testando se recusa mais ou menos de 2 letras
        plugboard = Plugboard()
        
        with self.assertRaises(ValueError):
            plugboard.add_connection(["ABC"]) # 3 letras - DEVE DAR ERRO
            
        with self.assertRaises(ValueError):
            plugboard.add_connection(["A"])   # 1 letra - DEVE DAR ERRO

    def test_letra_conectada_a_ela_mesma(self):
        # Trava 2: testando se recusa conectar a letra a ela mesma
        plugboard = Plugboard()
        
        with self.assertRaises(ValueError):
            plugboard.add_connection(["AA"])  # mesma letra - DEVE DAR ERRO

    def test_letra_ja_conectada(self):
        # Trava 3: testando se recusa conectar uma letra que já tem cabo
        plugboard = Plugboard(["AB"]) # conectamos A e B com sucesso
        
        with self.assertRaises(ValueError):
            # tentar conectar A com C deve falhar, pois A já está ligado no B
            plugboard.add_connection(["AC"]) 
            
        with self.assertRaises(ValueError):
            # tentar conectar D com B deve falhar, pois B já está ligado no A
            plugboard.add_connection(["DB"])

if __name__ == '__main__':
    unittest.main()