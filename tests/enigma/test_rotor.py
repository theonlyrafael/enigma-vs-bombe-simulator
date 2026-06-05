import unittest
from enigma.rotor import Rotor

class TestRotor(unittest.TestCase):

    # --- testes de exceções (__init__) ---

    def test_tamanho_invalido(self):
        # Trava 1: verifica se recusa fiação com menos ou mais de 26 letras
        with self.assertRaises(ValueError):
            Rotor(wiring="ABC", notch="Q")

    # --- testes do método step ---

    def test_giro_simples(self):
        # usando a fiação real do "rotor I" histórico, entalhe no Q, começando em A
        rotor = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="A")
        
        turnover = rotor.step()
        
        self.assertEqual(rotor.position, "B")
        # a letra 'A' não é o entalhe, portanto não deve empurrar o próximo rotor
        self.assertFalse(turnover)

    def test_giro_z_para_a(self):
        # colocando o rotor na última letra para testar o limite
        rotor = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="Z")
        
        rotor.step()
        
        # garante que a matemática modular funcionou e o z voltou para o a
        self.assertEqual(rotor.position, "A")

    def test_giro_no_entalhe(self):
        # colocamos o rotor exatamente em cima do entalhe (Q)
        rotor = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="Q")
        
        turnover = rotor.step()
        
        self.assertEqual(rotor.position, "R")
        # precisa retornar true para avisar a máquina de girar o rotor vizinho
        self.assertTrue(turnover)

    # --- testes dos métodos forward e backward ---

    def test_sinal_ida_e_volta_posicao_A(self):
        # rotor I na posição inicial (sem offset/deslocamento)
        rotor = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="A")
        
        # se entrar 'A' na ida (forward), deve sair a primeira letra da string de fiação ('E')
        self.assertEqual(rotor.forward('A'), 'E')
        
        # se entrar 'E' na volta (backward), o caminho reverso obrigatóriamente deve dar 'A'
        self.assertEqual(rotor.backward('E'), 'A')

    def test_sinal_ida_e_volta_posicao_B(self):
        # rotor I girado uma posição (offset = 1)
        rotor = Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="B")
        
        # matemática de entrada (forward): 'A' entra no pino 1 ('B')
        # a fiação na posição 1 é a letra 'K' (índice 10 do alfabeto)
        # saída reajustada para a máquina: 10 - 1 = 9 ('J')
        self.assertEqual(rotor.forward('A'), 'J')
        
        # se o 'A' vira 'J' na ida (forward), o 'J' deve virar 'A' na volta (backward)
        self.assertEqual(rotor.backward('J'), 'A')

if __name__ == '__main__':
    unittest.main()