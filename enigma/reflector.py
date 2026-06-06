class Reflector:
    def __init__(self, wiring: str): 
        # Trava 1:
        # inicializa um refletor da máquina Enigma
        # parametro wiring: string de 26 caracteres representando a fiação interna do refletor
        if len(wiring) != 26:
            raise ValueError("A fiação do refletor deve conter exatamente 26 caracteres.")
        
        self.wiring = wiring.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # Trava 2: garante qe uma letra nunca reflete nela mesma, o que é uma propriedade fundamental dos refletores da Enigma
        for i in range(26):
            if self.wiring[i] == self.alphabet[i]:
                raise ValueError(f"Refletor inválido: a letra '{self.alphabet[i]}' reflete nela mesma.")
            
    def reflect(self, char: str) -> str:
       # encontra o índice da letra que está entrando e devolve a letra correspondente na fiação  
        char_index = self.alphabet.index(char.upper())
        return self.wiring[char_index]