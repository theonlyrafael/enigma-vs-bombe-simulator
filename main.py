import os
from enigma.plugboard import Plugboard
from enigma.enigma_machine import EnigmaMachine
from enigma.catalog import get_rotor, get_reflector

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
    clean_screen()
    print("==================================================")
    print("           MÁQUINA ENIGMA - SIMULADOR             ")
    print("==================================================")
    print("Para começar, configure a máquina para a sessão atual:\n")
    
    # Passo 1: configurando os rotores
    print("catálogo de rotores: I, II, III, IV, V")
    r_esq = input("escolha o rotor ESQUERDO (ex: I): ").strip()
    r_meio = input("escolha o rotor do MEIO (ex: II): ").strip()
    r_dir = input("escolha o rotor DIREITO (ex: III): ").strip()
    
    # Passo 2: configurando as posições iniciais
    posicoes = input("\nDigite as 3 letras da posição inicial juntas (ex: ABC): ").strip().upper()
    while len(posicoes) != 3 or not posicoes.isalpha():
        posicoes = input("Erro. Digite exatamente 3 letras (ex: ABC): ").strip().upper()
        
    # Passo 3: configurando o refletor
    print("\nCatálogo de refletores: B, C")
    ref_model = input("Escolha o refletor (ex: B): ").strip()
    
    # passo 4: configurando o plugboard (opcional)
    print("\nConfiguração do plugboard (pares de letras juntos separados por espaço)")
    print("exemplo: AB CD EF")
    cabos_str = input("Digite as conexões (ou pressione enter para pular): ").strip().upper()
    
    # processa a string digitada pelo usuário em uma lista de tuplas [('A','B'), ('C','D')]
    cabos_lista = []
    if cabos_str:
        pares = cabos_str.split()
        for par in pares:
            if len(par) == 2:
                cabos_lista.append((par[0], par[1]))

    # montagem da máquina 
    try:
        plugboard = Plugboard(cabos_lista)
        rotores = [
            get_rotor(r_esq, posicoes[0]),
            get_rotor(r_meio, posicoes[1]),
            get_rotor(r_dir, posicoes[2])
        ]
        refletor = get_reflector(ref_model)
        
        maquina = EnigmaMachine(plugboard, rotores, refletor)
        print("\n[+] MÁQUINA MONTADA COM SUCESSO [+]\n")
        
    except ValueError as e:
        print(f"\n[!] ERRO NA MONTAGEM: {e}")
        print("Reinicie o programa e tente novamente.")
        return

    # loop de comunicação
    while True:
        mensagem = input("Digite a mensagem (ou 'SAIR' para encerrar): ").strip()
        
        if mensagem.upper() == 'SAIR':
            print("\nencerrando...")
            break
            
        cifrada = maquina.process_message(mensagem)
        print(f"-> MENSAGEM CIFRADA: {cifrada}\n")

if __name__ == "__main__":
    main()