class Plugboard:
    def __init__(self, connections=None):
        self.connections = {}
        
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
            
            if a in self.connections or b in self.connections:
                raise ValueError(f"Os caracteres '{a}' ou '{b}' já estão conectados.")
            
            self.connections[a] = b
            self.connections[b] = a
            
    
    def swap(self, letter):
        return self.connections.get(letter, letter)
    
            
    
            
            
        