import unittest
from enigma.plugboard import Plugboard
from enigma.rotor import Rotor
from enigma.reflector import Reflector
from enigma.enigma_machine import EnigmaMachine

class TestEnigmaMachine(unittest.TestCase):

    def setUp(self):
        # o método setup é executado automaticamente antes de cada teste.
        # ele limpa a bancada e cria uma máquina nova, evitando repetição de código.
        self.plugboard = Plugboard([('A', 'B'), ('C', 'D')])
        
        self.rotors = [
            Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="A"),
            Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E", initial_position="A"),
            Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V", initial_position="A")
        ]
        
        self.reflector = Reflector(wiring="YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.machine = EnigmaMachine(self.plugboard, self.rotors, self.reflector)

    def test_criptografia_simetrica(self):
        # testa a simetria militar: a mensagem cifrada passada na mesma máquina deve revelar o original
        mensagem_original = "PROJETOPLUGBOARD"
        mensagem_cifrada = self.machine.process_message(mensagem_original)
        
        # recriamos os rotores do zero para simular a máquina receptora na posição inicial ('A')
        rotors_receptores = [
            Rotor(wiring="EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch="Q", initial_position="A"),
            Rotor(wiring="AJDKSIRUXBLHWTMCQGZNPYFVOE", notch="E", initial_position="A"),
            Rotor(wiring="BDFHJLCPRTXVZNYEIWGAKMUSQO", notch="V", initial_position="A")
        ]
        maquina_receptora = EnigmaMachine(self.plugboard, rotors_receptores, self.reflector)
        
        mensagem_revelada = maquina_receptora.process_message(mensagem_cifrada)
        
        self.assertNotEqual(mensagem_cifrada, mensagem_original)
        self.assertEqual(mensagem_revelada, mensagem_original)

    def test_giro_dos_rotores_durante_digitacao(self):
        # garante que a máquina não é estática (apertar a mesma tecla repetidamente gera resultados diferentes)
        # usamos a máquina limpa que foi instanciada automaticamente pelo setUp
        letra_1 = self.machine.process_char('X')
        letra_2 = self.machine.process_char('X')
        letra_3 = self.machine.process_char('X')
        
        self.assertNotEqual(letra_1, letra_2)
        self.assertNotEqual(letra_2, letra_3)

if __name__ == '__main__':
    unittest.main()