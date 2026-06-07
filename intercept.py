# MÁQUINA BOMBE - SIMULADOR DE ATAQUE DE FORÇA BRUTA PARA QUEBRA DE POSIÇÕES INICIAIS

import os
import time
from cryptanalysis.bombe import Bombe

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

    # Passo 3: dados do ataque
    print("\n==================================================")
    print("               DADOS DA MENSAGEM                  ")
    print("==================================================")
    texto_cifrado = input("Digite o texto cifrado interceptado: ").strip()
    texto_claro = input("Digite o texto claro esperado (dica): ").strip()

    # Passo 4: execução da força bruta
    print("\n[+] INICIANDO ATAQUE DE FORCA BRUTA [+]")
    print("testando 17.576 combinacoes possiveis... aguarde.\n")

    bombe = Bombe(r_esq, r_meio, r_dir, ref_model)
    
    # inicia o cronômetro
    start_time = time.time()
    
    # dispara o algoritmo de quebra
    posicao_encontrada = bombe.quebrar_posicao(texto_cifrado, texto_claro)
    
    # para o cronômetro
    end_time = time.time()
    tempo_decorrido = round(end_time - start_time, 2)

    # 5. exibição do resultado
    if posicao_encontrada:
        print("==================================================")
        print(f"  [!] SUCESSO: CÓDIGO QUEBRADO EM {tempo_decorrido}s [!]")
        print(f"  POSIÇÃO INICIAL DOS ROTORES: {posicao_encontrada}")
        print("==================================================")
    else:
        print("==================================================")
        print(f"  [-] FALHA: POSIÇÃO NÃO ENCONTRADA EM {tempo_decorrido}s [-]")
        print("  Verifique o texto cifrado e a dica fornecida.")
        print("==================================================")

if __name__ == "__main__":
    main()