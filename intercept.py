# MÁQUINA BOMBE - SIMULADOR DE ATAQUE DE FORÇA BRUTA PARA QUEBRA DE POSIÇÕES INICIAIS

import os
import time
from cryptanalysis.bombe import Bombe
from enigma.enigma_machine import EnigmaMachine
from enigma.catalog import get_rotor, get_reflector
from enigma.plugboard import Plugboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("==================================================")
    print("           MÁQUINA BOMBE - INTERCEPTAÇÃO          ")
    print("==================================================")
    print("Configuração do hardware alvo:\n")

    # Passo 1: configurando os rotores
    print("Catálogo de rotores: I, II, III, IV, V")
    r_esq = input("escolha o rotor ESQUERDO (ex: I): ").strip().upper()
    r_meio = input("escolha o rotor do MEIO (ex: II): ").strip().upper()
    r_dir = input("escolha o rotor DIREITO (ex: III): ").strip().upper()

    # Passo 2: configurando o refletor
    print("\nCatálogo de refletores: B, C")
    ref_model = input("escolha o refletor (ex: B): ").strip().upper()
    
    # Passo 3: configurando o plugboard (opcional)
    print("\nConfiguração do plugboard alvo (pares separados por espaço)")
    cabos_str = input("Digite as conexões (ou pressione enter se não houver): ").strip().upper()
    
    cabos_lista = []
    if cabos_str:
        pares = cabos_str.split()
        for par in pares:
            if len(par) == 2:
                cabos_lista.append((par[0], par[1]))

    # Passo 4: dados do ataque
    print("\n==================================================")
    print("               DADOS DA MENSAGEM                  ")
    print("==================================================")
    texto_cifrado = input("Digite o texto cifrado interceptado: ").strip()
    texto_claro = input("Digite o texto claro esperado (dica): ").strip()

    # Passo 5: execução da força bruta
    print("\n[+] INICIANDO ATAQUE DE FORCA BRUTA [+]")
    print("testando 17.576 combinacoes possiveis... aguarde.\n")

    bombe = Bombe(r_esq, r_meio, r_dir, ref_model, cabos_lista)
    
    # inicia o cronômetro
    start_time = time.time()
    
    # dispara o algoritmo de quebra
    posicao_encontrada = bombe.quebrar_posicao(texto_cifrado, texto_claro)
    
    # para o cronômetro
    end_time = time.time()
    tempo_decorrido = round(end_time - start_time, 2)

    # Passo 6: exibição do resultado
    if posicao_encontrada:
        print("==================================================")
        print(f"  [!] SUCESSO: CÓDIGO QUEBRADO EM {tempo_decorrido}s [!]")
        print(f"  POSIÇÃO INICIAL DOS ROTORES: {posicao_encontrada}")
        
        # monta a máquina com a chave descoberta para ler a mensagem real
        rotores_vitoria = [
            get_rotor(r_esq, posicao_encontrada[0]),
            get_rotor(r_meio, posicao_encontrada[1]),
            get_rotor(r_dir, posicao_encontrada[2])
        ]
        maquina_vitoria = EnigmaMachine(Plugboard(cabos_lista), rotores_vitoria, get_reflector(ref_model))
        mensagem_revelada = maquina_vitoria.process_message(texto_cifrado)
        print(f"  MENSAGEM REVELADA: {mensagem_revelada}")
        print("==================================================")
        
    else:
        print("==================================================")
        print(f"  [-] FALHA: POSIÇÃO NÃO ENCONTRADA EM {tempo_decorrido}s [-]")
        print("  Verifique o texto cifrado e a dica fornecida e tente novamente.")
        print("==================================================")

if __name__ == "__main__":
    main()