# 🔐 Módulo Enigma

Este diretório contém a implementação da máquina de criptografia **Enigma** utilizada pelo simulador.

A implementação foi dividida em componentes que representam as principais partes da máquina e em uma classe responsável por coordenar o fluxo completo de criptografia. Dessa forma, cada componente possui uma responsabilidade específica, enquanto `EnigmaMachine` integra todos eles para reproduzir o comportamento da máquina.

## 🧩 Componentes

A implementação é composta pelos seguintes arquivos:

```text
enigma/
├── __init__.py
├── catalog.py
├── enigma_machine.py
├── plugboard.py
├── reflector.py
└── rotor.py
```

### 🔄 `rotor.py`

Implementa a classe `Rotor`, responsável pelo comportamento individual de um rotor da Enigma.

Cada rotor possui:

* uma **fiação interna** (`wiring`), responsável pelo mapeamento das 26 letras;
* uma **posição atual**, que representa a letra exibida na janela do rotor;
* um **notch**, utilizado para determinar quando o próximo rotor deve avançar.

A classe possui três responsabilidades principais:

* `step()` avança o rotor em uma posição e informa se o notch foi atingido;
* `forward()` processa o sinal no sentido da direita para a esquerda;
* `backward()` processa o sinal no sentido inverso, da esquerda para a direita.

A transformação realizada por `forward()` e `backward()` leva em consideração a posição atual do rotor, aplicando os deslocamentos necessários antes e depois do mapeamento da fiação.

### 🔁 `reflector.py`

Implementa a classe `Reflector`, responsável pelo refletor da Enigma.

O refletor possui uma fiação fixa de 26 caracteres e realiza um único mapeamento por meio do método `reflect()`.

Durante sua inicialização, a classe também valida uma propriedade fundamental do refletor utilizado na implementação: nenhuma letra pode refletir para si mesma.

### 🔌 `plugboard.py`

Implementa a classe `Plugboard`, responsável pelas conexões configuradas pelo operador antes do início da criptografia.

As conexões são armazenadas em um dicionário e são sempre bidirecionais. Por exemplo:

```text
A ↔ B
C ↔ D
```

A classe valida:

* se cada conexão possui exatamente duas letras;
* se uma letra não está conectada a ela mesma;
* se uma letra não está sendo utilizada em mais de uma conexão.

O método `swap()` realiza a substituição de uma letra de acordo com as conexões configuradas. Letras sem conexão permanecem inalteradas.

### 🗂️ `catalog.py`

Concentra as configurações dos rotores e refletores utilizados pelo simulador.

O arquivo mantém as fiações históricas dos rotores I, II, III, IV e V, juntamente com seus respectivos notches, além das fiações dos refletores B e C.

Também fornece duas funções utilizadas como fábrica de componentes:

* `get_rotor()` cria um rotor a partir do modelo e da posição inicial informados;
* `get_reflector()` cria um refletor a partir do modelo informado.

Assim, as demais partes do projeto não precisam armazenar diretamente as fiações de cada componente.

### ⚙️ `enigma_machine.py`

Implementa a classe `EnigmaMachine`, responsável por integrar todos os componentes anteriores e reproduzir o fluxo da máquina.

Na inicialização, a classe exige exatamente três rotores e armazena:

* o `Plugboard`;
* os três `Rotor`;
* o `Reflector`.

O método `process_char()` executa o processamento de um caractere em etapas:

```text
Caractere
    ↓
Plugboard
    ↓
Rotor direito
    ↓
Rotor do meio
    ↓
Rotor esquerdo
    ↓
Reflector
    ↓
Rotor esquerdo
    ↓
Rotor do meio
    ↓
Rotor direito
    ↓
Plugboard
    ↓
Caractere resultante
```

Antes de processar o caractere, o rotor da direita avança. Quando ele atinge seu notch, o rotor do meio também avança; caso o rotor do meio atinja seu notch, o rotor da esquerda avança.

O método `process_message()` aplica esse processo a todos os caracteres da mensagem, preservando espaços e pontuação.

## 🔗 Relação entre os componentes

A organização do módulo segue uma divisão de responsabilidades:

```text
                  ┌──────────────┐
                  │   Catalog    │
                  └──────┬───────┘
                         │
              cria componentes
                         ↓
┌────────────┐     ┌───────────────┐     ┌────────────┐
│ Plugboard  │     │    Rotors     │     │ Reflector  │
└──────┬─────┘     └───────┬───────┘     └─────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ↓
                  ┌─────────────────┐
                  │ EnigmaMachine   │
                  └─────────────────┘
                           │
                           ↓
                     Texto cifrado
```

`catalog.py` fornece as configurações dos componentes, enquanto `EnigmaMachine` coordena seu funcionamento. Os demais arquivos representam partes independentes da máquina.

## 📌 Papel do módulo no projeto

O módulo `enigma` é a base de todo o simulador.

A aplicação principal utiliza `EnigmaMachine` para realizar a criptografia, enquanto o módulo de criptoanálise também cria instâncias da mesma máquina para testar diferentes configurações durante a tentativa de quebra.

Isso significa que a implementação da Enigma não é utilizada apenas para produzir o texto cifrado: ela também é reutilizada durante o processo de criptoanálise para reproduzir exatamente o comportamento da máquina em cada configuração testada.
