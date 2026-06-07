import unittest
from enigma.catalog import get_rotor, get_reflector
from enigma.plugboard import Plugboard
from enigma.enigma_machine import EnigmaMachine
from cryptanalysis.bombe import Bombe

class TestBombe(unittest.TestCase):
    def test_quebrar_posicao_com_sucesso(self):
        # Passo 1: configura uma maquina alvo com uma posicao inicial especifica (ex: 'FAC')
        rotores = [
            get_rotor("I", "F"),
            get_rotor("II", "A"),
            get_rotor("III", "C")
        ]
        refletor = get_reflector("B")
        maquina_alvo = EnigmaMachine(Plugboard([]), rotores, refletor)

        # Passo 2: gera o texto cifrado a partir de uma mensagem original conhecida
        mensagem_original = "WETTERBERICHT"
        texto_cifrado = maquina_alvo.process_message(mensagem_original)

        # Passo 3: instancia a classe bombe e inicia a forca bruta buscando por uma parte conhecida do texto claro
        bombe = Bombe("I", "II", "III", "B")
        posicao_encontrada = bombe.quebrar_posicao(texto_cifrado, "WETTER")

        # Passo 4: valida se o algoritmo encontrou a exata posicao inicial configurada na maquina alvo
        self.assertEqual(posicao_encontrada, "FAC")

    def test_falha_ao_quebrar(self):
        # Passo 1: executa a forca bruta buscando por um texto claro que nao esta presente na cifra
        bombe = Bombe("I", "II", "III", "B")
        posicao_encontrada = bombe.quebrar_posicao("QWERTYUIOP", "FACULDADE")

        # Passo 2: valida se o retorno e None, confirmando que a quebra falhou corretamente
        self.assertIsNone(posicao_encontrada)

if __name__ == '__main__':
    unittest.main()