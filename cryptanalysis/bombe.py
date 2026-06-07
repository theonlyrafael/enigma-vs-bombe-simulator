from enigma.catalog import get_rotor, get_reflector
from enigma.plugboard import Plugboard
from enigma.enigma_machine import EnigmaMachine

class Bombe:
    def __init__(self, r_esq_model: str, r_meio_model: str, r_dir_model: str, reflector_model: str, plugboard_connections: list = None):
        # a Bombe precisa saber qual modo a Enigma está usando
        # o código abaixo irá quebrar a posição inicial dos rotores       
        self.r_esq_model = r_esq_model
        self.r_meio_model = r_meio_model
        self.r_dir_model = r_dir_model
        self.reflector_model = reflector_model
        self.plugboard_connections = plugboard_connections if plugboard_connections else []
        
    def _criar_maquina_teste(self, posicao: str) -> EnigmaMachine:
        # cria uma instância da Enigma para uma única tentativa de quebra
        plugboard = Plugboard(self.plugboard_connections)
        rotores = [get_rotor(self.r_esq_model, posicao[0]),
                     get_rotor(self.r_meio_model, posicao[1]),
                     get_rotor(self.r_dir_model, posicao[2])]
        reflector = get_reflector(self.reflector_model)
        return EnigmaMachine(plugboard, rotores, reflector)
    
    def quebrar_posicao(self, texto_cifrado: str, texto_claro: str) -> str:
        # higieniza as entradas
        texto_claro = texto_claro.upper().replace(" ", "")
        texto_cifrado = texto_cifrado.upper()
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # força bruta será usada agora com loops aninhados
        # isso irá gerar 26^3 = 17576 combinações possíveis de posições iniciais dos rotores
        for esq in alfabeto:
            for meio in alfabeto:
                for dir in alfabeto:
                    posicao = esq + meio + dir
                    
                    # cria uma maquina zerada para testar essa posicao exata
                    maquina_teste = self._criar_maquina_teste(posicao)
                    
                    # descriptografa o texto cifrado usando a máquina de teste
                    texto_quebrado = maquina_teste.process_message(texto_cifrado)
                    
                    # verifica se o texto claro esperado está presente no resultado da quebra
                    if texto_claro in texto_quebrado:
                        return posicao
        
        # se o loop inteiro terminar sem achar a palavra após os passos anteriores retorna None para indicar que a quebra falhou            
        return None