from enigma.rotor import Rotor
from enigma.reflector import Reflector

# dicionário conhecido das fiações históricas dos rotores e refletores usados na Enigma
rotor_wirings = {
    "I": {"wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "notch": "Q"},
    "II": {"wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE", "notch": "E"},
    "III": {"wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO", "notch": "V"},
    "IV": {"wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB", "notch": "J"},
    "V": {"wiring": "VZBRGITYUPSDNHLXAWMJQOFECK", "notch": "Z"}
}

reflector_wirings = {
  # "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
  # após pesquisa, descobri que o refletor A não era usado na prática, então decidi 
  # não incluí-lo no catálogo para evitar confusão.
  # ao q tudo indica o refletor A foi quebrado antes da guerra começar, e por isso
  # não há registros de sua fiação sendo usada após 1937. 
    "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
    "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
}

def get_rotor(model: str, initial_position: str) -> Rotor:
    
    # atua como uma fábrica: busca os dados no catálogo e monta o rotor
    model = model.upper()
    if model not in rotor_wirings:
        raise ValueError(f"modelo de rotor '{model}' não existe no catálogo histórico.")
    
    data = rotor_wirings[model]
    return Rotor(wiring=data["wiring"], notch=data["notch"], initial_position=initial_position)

def get_reflector(model: str) -> Reflector:
    
    # fabrica o refletor solicitado
    model = model.upper()
    if model not in reflector_wirings:
        raise ValueError(f"modelo de refletor '{model}' não existe no catálogo histórico.")
        
    return Reflector(wiring=reflector_wirings[model])