# 🔐 Simulador Enigma e Máquina Bombe

![Python](https://img.shields.io/badge/Python_3.11.3-plastic?style=plastic&logo=python&logoColor=white&color=3776AB)

Este projeto apresenta uma simulação em Python do funcionamento da máquina de criptografia **Enigma** e de um processo de **criptoanálise inspirado na máquina Bombe**, permitindo reproduzir, de forma prática, o ciclo entre a cifragem de uma mensagem e sua posterior tentativa de quebra.

O projeto é dividido em duas frentes principais: a **criptografia**, responsável pela configuração da Enigma e geração do texto cifrado, e a **criptoanálise**, responsável por utilizar informações conhecidas da mensagem para buscar a configuração necessária para sua decifragem.

## 📜 Contextualização das Máquinas

A **Enigma** foi uma máquina eletromecânica utilizada pela Alemanha durante a Segunda Guerra Mundial para cifrar comunicações. Seu funcionamento era baseado principalmente na combinação de rotores, refletor e conexões do plugboard, produzindo uma substituição que variava a cada caractere digitado.

A **Bombe**, desenvolvida pelos britânicos durante a Segunda Guerra Mundial a partir do trabalho de Alan Turing e outros pesquisadores, foi criada para auxiliar na criptoanálise das mensagens cifradas pela Enigma. Seu funcionamento explorava configurações possíveis da máquina em busca de combinações compatíveis com informações previamente conhecidas sobre a mensagem.

Neste projeto, esses conceitos são utilizados para criar uma simulação computacional que permite acompanhar as duas etapas: **cifrar uma mensagem com a Enigma e tentar recuperar sua configuração por meio da criptoanálise**.

## 📁 Estrutura do Projeto

```text
📦 enigma-vs-bombe-simulator
├── 📂 cryptanalysis/   # Componentes relacionados à criptoanálise
├── 📂 enigma/          # Implementação da máquina Enigma
├── 📂 tests/           # Testes automatizados
├── 📄 intercept.py     # Execução do processo de interceptação
├── 📄 main.py          # Ponto de entrada da simulação da Enigma
├── 📄 README.md
└── 📄 LICENSE
```

## 🚀 Instruções de Execução

O software utiliza o terminal interativo para receber as configurações da máquina e conduzir as etapas de criptografia e criptoanálise.

### 🔒 1. Painel de Criptografia

A execução da etapa de criptografia é realizada por meio do arquivo `main.py`.

O programa solicitará progressivamente os parâmetros necessários para configurar a máquina:

- **Rotores:** I, II, III, IV ou V
- **Posição inicial:** três letras válidas do alfabeto, como `ABC`
- **Refletor:** B ou C
- **Plugboard:** pares de letras maiúsculas separados por espaço, como `GH IJ KL`
- **Mensagem:** texto claro que será cifrado

A máquina realiza a normalização da entrada, removendo espaços e caracteres especiais antes da criptografia.

Ao final da execução, será apresentado o texto cifrado em um bloco contínuo de letras maiúsculas.

### 🕵️ 2. Painel de Interceptação

A etapa de criptoanálise é executada por meio do arquivo `intercept.py`.

O processo utiliza o texto cifrado produzido na etapa anterior e informações conhecidas sobre a mensagem para procurar uma configuração compatível com a máquina utilizada na criptografia.

Para iniciar o processo, serão solicitados:

- **Rotores e refletor:** os mesmos utilizados na criptografia
- **Plugboard alvo:** as conexões utilizadas na máquina ou uma entrada vazia
- **Texto cifrado:** o texto produzido pela Enigma
- **Texto claro conhecido:** uma palavra ou fragmento que se sabe estar presente na mensagem original

A partir dessas informações, o simulador realiza a busca pelas configurações possíveis e apresenta os resultados encontrados, incluindo a posição inicial identificada, o tempo de execução e a mensagem decifrada.

## 📚 Documentação

Para manter este README focado na utilização e na visão geral do projeto, os detalhes de implementação estão documentados separadamente:

- 📖 [`enigma/README.md`](enigma/README.md) — funcionamento da implementação da Enigma e contribuição de cada arquivo do módulo.
- 🔎 [`cryptanalysis/README.md`](cryptanalysis/README.md) — funcionamento da criptoanálise, da Bombe e contribuição de cada arquivo do módulo.