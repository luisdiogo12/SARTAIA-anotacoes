#

## Notas

talvez seja util tb fazer o curso de MCP do hugging face

pesquisar a descrição de circuitos usando SPACE

## cenas de matching networks

representações de topologias
- **netlist SPICE**
  - ```
    * L-match 2.445 GHz
    Vs  src 0   AC 1
    Rs  src n2  50
    L1  n2  n1  2.35n
    C1  n1  0   1.4p
    ZL  n1  0   ...      ; carga (modelada com R, L, C)
    .ac lin 201 2G 3G
    ```
  - em principio deve ser o formato de circuitos mais presente nos dados de treino de LLMs
  - representa qualquer topologia
  - tem elementos para linhas de transmissão
  - é simulavel com **`ngspice`**
  - possiveis problemas: 
    - nomes dos nós são arbitrários e LLMs podem errar na coerência dos nós
    - equivalencia de netlistas para a mesma rede pode dificultar comparar sol
    - carga complexa tem que ser modelada com elementos, não como um numero
- grafos
  - ```
    nós:     [src, n2, n1, gnd]
    arestas: (n2, n1, L, 2.35nH), (n1, gnd, C, 1.4pF), (n1, gnd, ZL), (src, n2, Rs, 50Ω)
    ```
  - podia ser lista de arestas, matriz de adjacencia ou de incidencia
  - é o que é mais usado em ML aplicadas a topologias de circuitos (GNNs, geraçao de topologias)
  - possiveis problemas:
    - LLMs não lidarem bem com matrizes de adjacencia
    - a lista de arestas é melhor, mas para isso mais vale usar netlist SPICE
- listas em escada
  - ```
    [{"position": "shunt",  "kind": "capacitor", "value": "1.4 pF"},
     {"position": "series", "kind": "inductor",  "value": "2.35 nH"}]
    ```
  - o que já estou a usar
  - é simples, compacta, facil de validar e converte-se bem para ABCD, SPICE ou grafos
  - problemas:
    - só representa redes em escada, logo exclui muitas possibilidades
- expressão série-paralelo
  - ```
    Zin = L(2.35n) + ( C(1.4p) || ZL )
    ```
  - compacta, sem ambiguidades para redes serie-paralelo e mostra diretamento como calcular Z_in
  - possiveis problemas: muitos elementos e parenteses aninhados, propenso a erros

outras representações (indiretas) de topologia (não são representações topologicas):
- usar matrizes ABCD
  - ```
    [A B; C D] = [1  jωL; 0  1] · [1  0; jωC  1]
    ```
  - é para resolver equações, mas talvez seja util
  - podia-se conservar as matrizes para descrever a topologia, sendo depois uteis para ao resolve-las dá a matriz da network equivalente e resultados
  - seria util para integrar com tools
- usar descrição de malhas
  - ```
    Malha 1: Vs = I1·(Rs + jωL) − I2·0 + (I1 − I2)·1/(jωC)
    Malha 2: 0 = (I2 − I1)·1/(jωC) + I2·ZL
    ```
  - tipo cada malha ter uma descrição da sua equação
  - é uma forma classica de analise de circuitos
  - possiveis problems:
    - a descrição do circuito é indireta, depois tera que reconstruir a topologia
    - é muito verboso
- **código de simulação**
  - bibliotecas como scikit-rf, PySpice, Lcapy, ...
  - LLMs são bons a escrever codigo e as bibliotecas são muito usadas em RF
  - o resultado é executavel
- trajetoria na carta smith
  - é como eng. de RF raciocinam e está na literatura
  - liga cada componente a um move geometrico
  - problema: não é uma representação de saida, continua a precisar de valores
  - pode ser util como raciocinio (pode-se comparar o modelo de raciocinio, este vs livre)
-  files touchstone e parametros S,Z e Y
   -  formato padrão para dados de RF
   -  forma de dar uma carga dependente da frequenci
   -  problemas: descrevem comportamentos, nao topologia e tabelas sao extensas
   -  é bom para descrever carga em problemas avançados mas nao serve de solução


representações de comportamentos
- matriz ABCD
- parametros S
- equações de malhas

## Onde rodar modelos

**Laptops dos meus irmãos**

**Server IT**


### Groq

| model id                     | reasoning | prompt caching | struct output | Local & Remote Tool Use | Parallel Tool Use | JSON Mode | Built-In Tools |
| :--------------------------- | :-------: | :------------: | :-----------: | :---------------------: | :---------------: | :-------: | :------------: |
| openai/gpt-oss-20b           |     x     |       x        |     both      |            x            |         -         |     x     |       x        |
| openai/gpt-oss-120b          |     x     |       x        |     both      |            x            |         -         |     x     |       x        |
| openai/gpt-oss-safeguard-20b |     x     |       x        |  Best-effort  |            x            |         -         |     x     |       -        |
| qwen/qwen3.8-27b             |     x     |       -        |     both      |            x            |         x         |     x     |       -        |
| minimaxai/minimax-m2.7       |     x     |       -        |       -       |            x            |         x         |     x     |       -        |
| meta-models/muse-spark-open  |     x     |       -        |     both      |            x            |         x         |     x     |       -        |
| llama-3.3-70b-versatile      |     -     |       -        |       -       |            x            |         x         |     x     |       -        |
| llama-3.1-8b-instant         |     -     |       -        |       -       |            x            |         x         |     x     |       -        |


## Modelos LLM

### Aspetos principais

#### Capacidade

Numero de parametros

Arquitetura (dense vs MoE)

Tipo de Treino

Tokenizer

Data de fim de treino: o quao atualizado está

#### Hardware

Precisão e quatização
- FP16/BF16
- INT8/ 8 bits
- 4 bits

#### 

Context size

Limite de tokens de saida

Parametros de amostragem
- temperatura
- top-p e top-k

Chat template

##

- LLM cru
- LLM 
