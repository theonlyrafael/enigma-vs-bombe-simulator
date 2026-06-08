# Simulador Enigma e Máquina Bombe

Este repositório contém uma implementação em Python da máquina de criptografia Enigma e do simulador de criptoanálise Bombe. Dessa forma, o projeto é dividido em duas frentes de operação independentes para simular a defesa e o ataque cibernético. Sendo assim, a arquitetura estruturada garante que os testes de quebra de código sejam fidedignos e isolados na memória do sistema. Portanto, o usuário experimenta o ciclo completo da comunicação militar através de terminais de operação exclusivos.

## Contextualização das Máquinas

Nesse sentido, o simulador da Enigma baseia o seu funcionamento computacional no fluxo eletromecânico real de rotores e refletores. Ademais, a ferramenta aplica os exatos princípios matemáticos de permutação que tornavam a comunicação de guerra impenetrável. Por outro lado, a máquina Bombe utiliza a técnica de força bruta ancorada em um fragmento de texto claro conhecido. Desse modo, o sistema gera milhares de instâncias isoladas até interceptar a dica exata fornecida pelo operador. Consequentemente, a chave diária é quebrada e a mensagem verdadeira é revelada na tela.

## Instruções de Execução

Além disso, o software exige a utilização do terminal interativo para operar de forma plena. Para tanto, os módulos solicitam os dados de entrada de forma progressiva e guiam o usuário pela configuração estrutural do equipamento.

### 1. Painel de Criptografia

A princípio, a execução da defesa ocorre através do inicializador principal denominado main. Em seguida, o sistema exigirá a configuração tática das peças criptográficas do dia. Logo, siga os parâmetros de entrada esperados listados abaixo.

* Rotores (Entrada esperada: I, II, III, IV ou V)
* Posição Inicial (Entrada esperada: Três letras juntas e válidas do alfabeto, como ABC)
* Refletor (Entrada esperada: B ou C)
* Plugboard (Entrada esperada: Pares de letras maiúsculas separadas por espaço, como GH IJ KL)
* Mensagem (Entrada esperada: Frase em texto claro contendo a dica alvo do ataque)

Contudo, a máquina de defesa executará a higienização dos dados removendo espaços e caracteres especiais automaticamente. Assim, a saída correta apresentará um bloco contínuo de letras maiúsculas representando o texto completamente cifrado.

### 2. Painel de Interceptação

Na sequência, a execução do ataque é conduzida pelo controlador secundário de espionagem denominado intercept. Diante disso, o operador utilizará o bloco de texto cifrado gerado na defesa anterior como sua munição primária contra a máquina. Adicionalmente, insira os dados no terminal respeitando os requisitos listados a seguir.

* Rotores e Refletor (Entrada esperada: Idênticos aos utilizados na fase de criptografia)
* Plugboard Alvo (Entrada esperada: As exatas conexões da máquina inimiga ou simplesmente vazio)
* Texto Cifrado (Entrada esperada: O texto ilegível gerado pelo painel da Enigma)
* Texto Claro (Entrada esperada: A palavra que o usuário tem certeza absoluta estar contida na mensagem)

Por fim, o motor da Bombe iniciará o laço de repetição exaustivo. Por conseguinte, a saída final demonstrará o tempo exato de execução da engenharia reversa, a posição inicial descoberta pelos cálculos e a leitura imediata do texto decifrado.