class EnigmaMachine:
    def __init__(self, plugboard, rotors: list, reflector):
        # Trava 1: a máquina enigma histórica exige exatamente 3 rotores
        if len(rotors) != 3:
            raise ValueError("a máquina deve conter exatamente 3 rotores.")
            
        self.plugboard = plugboard
        self.reflector = reflector
        # a lista de rotores seguirá a ordem física da máquina: [esquerdo, meio, direito]
        self.rotors = rotors

    def process_char(self, char: str) -> str:
        # ignora espaços ou caracteres que não são letras, mantendo o original
        if not char.isalpha():
            return char
        
        char = char.upper()
        
        # o rotor da direita sempre avança a cada tecla pressionada
        gira_meio = self.rotors[2].step()
        
        # se o rotor da direita (índece 2) atingir seu notch, o rotor do meio (índice 1) avança
        if gira_meio:
            gira_esquerdo = self.rotors[1].step()
            
            # se o rotor do meio atingir seu notch, o rotor da esquerda (índice 0) avança
            if gira_esquerdo:
                self.rotors[0].step()
        
        # Passo 2: o operador digita uma letra, que primeiro passa pelo plugboard
        signal = self.plugboard.swap(char)
        
        # Passo 3: o sinal passa pelos rotores da direita para a esquerda
        for rotor in reversed(self.rotors):
            signal = rotor.forward(signal)
        
        # Passo 4: o sinal atinge o refletor e é refletido de volta
        signal = self.reflector.reflect(signal)
        
        # Passo 5: o sinal passa pelos rotores da esquerda para a direita
        for rotor in self.rotors:
            signal = rotor.backward(signal)
        
        # Passo 6: o sinal passa pelo plugboard novamente
        signal = self.plugboard.swap(signal)
        
        return signal
    
    def process_message(self, message: str) -> str:
        # processa cada caractere da mensagem, mantendo espaços e pontuação
        return ''.join(self.process_char(char) for char in message)