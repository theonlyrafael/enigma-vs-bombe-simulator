class Rotor:
    def __init__(self, wiring: str, notch: str, initial_position: str = 'A'):
        
        # inicializa um rotor da máquina Enigma
        # parametro wiring: string de 26 caracteres representando a fiação interna
        # parametro notch: a letra que, ao ser ultrapassada, fará o próximo rotor avançar/girar
        # parametro initial_position: a letra visível na janela do rotor para o operador
        
        # Trava 1: a fiação do rotor deve ser uma string de 26 caracteres, representando a substituição de cada letra do alfabeto
        if len(wiring) != 26:
            raise ValueError("A fiação do rotor deve conter exatamente 26 caracteres.")
        
        self.wiring = wiring.upper()
        self.notch = notch.upper()
        self.position = initial_position.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
    def step(self) -> bool:
        # avança o rotor para a próxima posição
        # retorna True se o rotor atingir a posição de notch, indicando que o próximo rotor deve avançar/girar
        
        # checa se está no entalhe antes de girar
        acionar_proximo = self.position == self.notch
        
        # encontra o índice da posição atual e avança para a próxima letra
        current_index = self.alphabet.index(self.position)
        
        # gira 1 posição aplicando a matemática modular para o Z voltar ao A
        next_index = (current_index + 1) % 26
        
        # atualiza a letra que está aparecendo na janela do rotor
        self.position = self.alphabet[next_index]

        return acionar_proximo
    
    def forward(self, char: str) -> str:
        # passa o sinal elétrico da direita para a esquerda
        
        # encontra o offset numérico (0 a 25) baseado na posição atual do rotor
        offset = self.alphabet.index(self.position)
        char_index = self.alphabet.index(char.upper())
        
        # calcula em qual pino interno o sinal vai entrar (ajustado pelo giro)
        enter_index = (char_index + offset) % 26
        
        # o sinal viaja pelo emaranhado de fios e sai em uma letra nova
        mapped_char = self.wiring[enter_index]
        
        # reajusta a saída de volta para o referencial absoluto da máquina
        mapped_index = self.alphabet.index(mapped_char)
        exit_index = (mapped_index - offset) % 26
        
        return self.alphabet[exit_index]

    def backward(self, char: str) -> str:
        # passa o sinal elétrico da esquerda para a direita (voltando do refletor).
        
        offset = self.alphabet.index(self.position)
        char_index = self.alphabet.index(char.upper())
        
        # o sinal entra pela esquerda, ajustado pelo giro do rotor
        enter_index = (char_index + offset) % 26
        
        # procura de trás pra frente: descobre de qual pino da direita esse fio veio
        target_char = self.alphabet[enter_index]
        mapped_index = self.wiring.index(target_char)
        
        # reajusta a saída para a máquina
        exit_index = (mapped_index - offset) % 26
        
        return self.alphabet[exit_index]