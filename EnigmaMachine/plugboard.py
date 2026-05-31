class Plugboard:
    def __init__(self, connections=None):
        self.mapping = {}
        
        if connections:
            self.add_connection(connections)

    def add_connection(self, connections):
        
        # recebe uma lista de pares, por exemplo: [('A', 'B'), ('C', 'D')]
        
        for pair in connections:
            
            # Trava 1: verifica se o par contém exatamente dois caracteres 
            if len(pair) != 2:
                raise ValueError("Cada par deve conter exatamente dois caracteres.")
            
            a, b = pair
            
            # Trava 2: impede que a mesma letra seja conectada a si mesma 
            if a == b:
                raise ValueError(f"A letra '{a}' não pode ser conectada a si mesma.")
            
            # Trava 3: garante que nenhuma das letras já esteja usando um cabo
            if a in self.mapping or b in self.mapping:
                raise ValueError(f"Os caracteres '{a}' ou '{b}' já estão conectados.")
            
            # qualquer par válido é adicionado ao mapeamento e cria a conexão bidirecional
            self.mapping[a] = b
            self.mapping[b] = a
            
        # simula a passagem de um sinal pelo plugboard, 
        # onde cada letra é substituída pela sua correspondente no mapeamento, 
        # ou permanece a mesma se não estiver conectada   
    def swap(self, char):
        return self.mapping.get(char, char)
    
            
    
            
            
        