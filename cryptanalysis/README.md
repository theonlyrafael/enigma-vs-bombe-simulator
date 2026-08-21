# 🕵️ Módulo de Criptoanálise

Este diretório contém a implementação do processo de **criptoanálise** utilizado pelo simulador para tentar descobrir a posição inicial dos rotores da máquina Enigma.

A implementação é concentrada atualmente no arquivo `bombe.py`, que utiliza os componentes do módulo `enigma` para reproduzir diferentes configurações da máquina e verificar quais delas são compatíveis com informações conhecidas sobre a mensagem original.

## 🧩 Estrutura

```text
cryptanalysis/
├── __init__.py
└── bombe.py
```

### 🧠 `bombe.py`

Implementa a classe `Bombe`, responsável pelo processo de busca da configuração da Enigma.

Apesar do nome fazer referência à **Bombe histórica**, a implementação deste projeto utiliza uma abordagem computacional simplificada baseada em **força bruta sobre as posições iniciais dos três rotores**.

A classe recebe, em sua configuração:

* modelo do rotor esquerdo;
* modelo do rotor central;
* modelo do rotor direito;
* modelo do refletor;
* conexões conhecidas do plugboard.

Essas informações permanecem fixas durante a busca, enquanto as posições iniciais dos rotores são testadas.

### 🏭 `_criar_maquina_teste()`

O método `_criar_maquina_teste()` constrói uma nova `EnigmaMachine` para uma posição inicial específica.

Para isso, ele:

1. cria um novo `Plugboard`;
2. cria os três rotores usando `get_rotor()`;
3. cria o refletor usando `get_reflector()`;
4. monta uma nova `EnigmaMachine` com esses componentes.

Criar uma nova máquina para cada tentativa é importante porque o processamento de uma mensagem altera as posições dos rotores. Dessa maneira, cada combinação começa com uma configuração limpa e independente.

### 🔎 `quebrar_posicao()`

Este método executa a busca pela posição inicial correta dos rotores.

Primeiro, o texto claro conhecido e o texto cifrado são normalizados. Em seguida, são geradas todas as combinações possíveis das três posições iniciais:

```text
26 × 26 × 26 = 17.576 posições
```

A busca é realizada por três laços aninhados:

```text
Rotor esquerdo
    ↓
Rotor do meio
    ↓
Rotor direito
```

Para cada combinação:

1. uma nova `EnigmaMachine` é criada;
2. o texto cifrado é processado;
3. o resultado é comparado com o texto claro conhecido;
4. caso o trecho conhecido seja encontrado, a posição atual é retornada.

A primeira posição compatível encontrada encerra a busca.

Caso nenhuma das 17.576 combinações produza um resultado contendo o texto claro conhecido, o método retorna `None`.

## 🔗 Relação com o módulo Enigma

O módulo de criptoanálise não possui uma implementação independente dos componentes da Enigma.

Em vez disso, `bombe.py` reutiliza diretamente:

```text
cryptanalysis/bombe.py
        │
        ├── EnigmaMachine
        ├── Plugboard
        ├── get_rotor()
        └── get_reflector()
                │
                ↓
          módulo enigma/
```

Essa abordagem faz com que a criptoanálise utilize o mesmo comportamento da máquina empregado na criptografia original.

O fluxo pode ser representado da seguinte forma:

```text
Texto cifrado
      ↓
Informação conhecida
      ↓
Geração de uma posição inicial
      ↓
Criação de uma Enigma de teste
      ↓
Descriptografia
      ↓
Texto compatível?
   ↙          ↘
 Não           Sim
  ↓             ↓
Próxima      Retorna a
posição      configuração
```

## ⚠️ Diferença em relação à Bombe histórica

O nome `Bombe` é utilizado como referência ao equipamento histórico empregado na criptoanálise da Enigma, mas esta implementação **não reproduz integralmente o funcionamento da Bombe histórica**.

Aqui, o processo é uma simulação computacional simplificada que testa sistematicamente as 17.576 posições iniciais possíveis dos três rotores e verifica se o resultado contém um trecho de texto claro previamente conhecido.

Isso permite demonstrar, de maneira prática, a ideia de utilizar informações conhecidas sobre a mensagem para reduzir uma busca de configurações possíveis.

## 📌 Papel do módulo no projeto

O módulo `cryptanalysis` representa a etapa de ataque do simulador.

Enquanto o módulo `enigma` é responsável por criar e executar a máquina utilizada para cifrar ou decifrar mensagens, este módulo reutiliza essa mesma implementação para testar configurações até encontrar uma que seja compatível com as informações conhecidas.

Dessa forma, a relação entre os dois módulos é intencional:

```text
             ENIGMA
                │
                │ produz
                ↓
         Texto cifrado
                │
                ↓
        CRIPTOANÁLISE
                │
          testa posições
                ↓
        Configuração provável
                │
                ↓
        Mensagem decifrada
```
