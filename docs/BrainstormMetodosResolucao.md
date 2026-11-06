# Relatório do brainstorm com LLM para métodos de resolução

##

Claude Oppus 5.5 High - [link chat](https://claude.ai/share/0404eabb-3c5f-4d86-8c86-1e580c3869d5)

## draft

### metodos que me chamaram a atenção

Uso de CNN com GA. Como é que CNN é usado? Não percebi

Agente LLM com ferramentas de simulação. LLM decide a topologia 

Agente LLM para descobrir heurísticas em runtime

Uso de transfer learning

### cenas para pesquisar

- redes descritas por matrizes ABCD e outras
- Neural Architecture Search (NAS)
- rede neuronal feedforward (FNN)
- tunable matching network (TMN)
- Zeroth-Order Projected Gradient Descent (ZO-PGD)
- replay buffer em Deep RL
- Multilayer Perceptron (MLP)
- Monte Carlo Tree Search (MCTS)
- AlphaZero
- Recurrent Neural Network (RNN)
- Graph Neural Network (GNN)
- long short-term memory (LSTM)
- transformers 


- Voltage Standing Wave Ratio (VSWR)
- Coeficiente de Refração ($\Gamma$)
- $\text{S11}$, $\text{S21}$, $\text{S22}$, $\text{S12}$, 
- SPACE
- AlphaGO e AlphaZero
- FunSearch AlphaEnvolve 

### keys para pesquisa
- impedance
- impedance matching
- network topology
- circuits
- circuit synthesis
- input impedance
- load modeling
- Electronic design automation
- large language models
- artificial neural network (ANN)
- Deep neural network (DNN)
- deep learning
- search problems
- automated heuristic design


## Métodos analíticos e semi-analíticos

### Real Frequency Technique

### Limite de Bode-Fano

Teorema que diz o quanto é possível adaptar uma carga reativa numa dada banda, com qualquer **rede passiva(não acrescenta energia) sem perdas(componentes ideais)**.

**Util:** 
- para comparar resultados com o limite teorico
- para ser uma métrica para o agent usar - em vez do agent estar a tentar otimizar para uma potencia inalcançavel, otimiza para uma potencia dentro do limite teorico
- detetar bugs

## Otimização numérica

O modelo tem que ser diferenciavel para calcular gradientes. Um exemplo são redes descritas com matrizes ABCD 

É o método usado por simuladores comerciais (ADS, AWR)

Problemas:
- minimos locais
- dependencia do ponto inicial

Tecnicas uteis:
- multistart para tentar cobrir o max de minimos possiveis
- escala logaritmica porque os valores de L e C variam por ordens de grandeza e com uma escala linear a exploração não seria muito uniforme

**Pode funcionar como baseline.** É um método muito bom para problemas pequenos, dificilmente RL consegue competir. O que se pode competir é para problemas mais complexos, dar para usar valores discretos(valores de componentes reais), escolher topologias, muitos parametros, ...

### Algoritmos:

#### L-BFGS

Gradiente descendente que aprende a forma do terreno. Uma o método de Newton para resolver com a segunda derivada (matriz Hessiana), para saber como o terreno curva e conseguir saltar quase logo para o minimo

#### Levenberg-Marquardt

Otimizador para custos do tipo soma de quadrados de vários erros

#### Minimax

Não é um algoritmo, é uma forma de definir o custo: minimizar o máximo dos erros

Problema: a função não é diferenciavel nos pontos que pior muda de frequencia e o gradiente so ve a pior frequencia causando oscilacoes no otimizador (otimiza a freq1 -> a freq2 piora, otimiza a freq2 -> a freq1 piora)
Solução:
- log-sum-exp: tipo soft max
- norma-p

## Metaheurísticas

### Algoritmos

#### Genetic Algorithm (GA)

já estudei

#### Particle Swarm Optimization (PSO)

já estudei

#### Simulated Annealing (SA)

já estudei

#### CMA-ES

Práticamente faz o mesmo que BFGS mas sem gradientes

## Otimização bayesiana (BO)

já estudei (por mim, bases fracas)

faz-se umas simulações e a otimizacao bayesiana depois faz previsões de resultados de simulações cujos parametros estão entre as simulações feitas, esses resultados teriam uma probabilidade associada

**Util:**
- para simulações caras, este metodo permite reduzir o numero de simulacoes necessarias

**Problemas**
- escala mal com dimensoes, quantas mais dimensoes mais simulacoes sao precisas para ter uma boa incerteza 
- escala mal com muitos pontos(simulacoes), o que piora o problema anteriro
- assume que pontos proximos tem valores parecidos, coisa que não pode dificultar obter resposta, por exemplo, qual é a distancia entre uma $rede \pi$ e uma $rede T$
- não é muito util para casos com restrições


## Space mapping

Usa 2 modelos, um grosseiro para obter uma aproximação à solução de forma rápida e depois um fino para afinar a solução obtida pelo grosseiro.

Os 2 modelos:
- Coarse Model: o circuito ideal; é rápido; ignora parasitas, perdas, etc.
- Fine Model: simulação EM ou medição real; é lento; é considerado como a verdade

Exemplo com Agressive Space Mapping:
1. **Otimização no Coarse Model:** modelo ideal dá L=2.7 e C=2.3 como adaptação perfeita a 2.4GHz
2. **Simulação no Fine Model:** modelo com pads e componentes reais mostra a melhor adaptação para 2.25GHz
3. **Extração de parametros:** descobre que esta resposta é igual a um circuito ideal com L=2.9 e C=2.4, ou seja, o circuito real comporta-se como se tivesse +0,2nH e +0.1pF
4. **Correção:** compensa-se o coarse model passando L=x-0.2 e C=y-0.1, onde no caso do ponto 1 x=2.7 e y=2.3
5. **Repetir** do passo 2 até ter uma boa solução

Problemas:
- O coarse model tem que estar alinhado com o fine model. o coarse model tem que ser capaz de reproduzir o comportamento do fine model
- Extração de parametros pode ser ambigua. várias combinações de valores ideais dão respostas muito semelhantes

Space Mapping vs BO:
- BO começa sem saber nada do problema e aprende tudo à custa de simulações finas
- Space Mapping começa com a fisica embutida no modelo grosseiro e só precisa de simulações para aprender a diferença entre o ideal e o real

## Multi-Fidelity Bayesian Optimization

A ideia é usar o modelo barato para que o GP(Gaussian Process) não comece do zero, e assim precisar de menos simulações caras para ter uma incerteza baixa

Problema: risco de transferencia negativa. é assumido que o coarse model ajuda, mas se estiver mal alinhado pode conduzir para a direcao errada. os algoritmos que incluem incerteza protegem-se melhor contra isto 

### Algoritmo: Coarse Model como ponto de partida do GP

A previsão passa a ser o Coarse Model enquanto o GP serve para aprender a diferença entre o Coarse Model e o Fine Model: $\text{fino}(x) \approx \text{grosseiro}(x) + \underbrace{\text{GP}(x)}_{\text{correção}}$

Assim GP não tem tanto espaço para incerteza

### Algoritmo: Space mapping + GP no que sobra

O Space Mapping corrige o erro sistemático enquanto um GP modela o erro residual que o mapeamento não apanhou e dá a incerteza

### Algoritmo: Co-kriging (modelo autorregressivo de Kennedy e O’Hagan)

Uma versão mais completa do `Coarse Model como ponto de partida do GP`. Em vez de assumir que o Coarse model está quase certo e falta apenas a correção para acertar, aprende quando confiar nele: $\text{fino}(x) = \underbrace{\rho}_{\text{fator de escala}} \cdot \text{grosseiro}(x) + \underbrace{\delta(x)}_{\text{discrepancia}}$

### Algoritmo: BO multi-fidelidade com aquisição consciente do custo

A função de aquisição já não decide só onde simular, decide tambem com que modelo, pergunta "que simulação me dá mais info por unidade de custo?"

Ex. de vários niveis:
| Nível | Modelo                             | Custo   |
| :---- | ---------------------------------- | ------- |
| 1     | circuito ideal (ABCD)              | ~1 ms   |
| 2     | circuito com ficheiros .s2p + pads | ~ms     |
| 3     | simulação EM (openEMS)             | minutos |
| 4     | medição na bancada                 | horas   |

## Sintese Topologica

Ideia geral: escolher a arquitetura, não só os pesos

### Como repesentar um topologia

Forma mais comum é a ladder: sequencia de posições entre fonte e carga onde em cada posição escolhe-se o tipo (indutor ou condensador) e a ligação (em série ou em paralelo)

### Problema das redundancias

Topologias diferentes podem ser na verdade o mesmo circuito; ex: dois indutores seguidos em serie equivales a um só

Um metodo para evitar isto é por exemplo ter a regra de que não se pode repetir o mesmo tipo com a mesma ligação na posição seguinte

### Metodo: Brute Force

1. Listar todas as topologias até um certo tamanho eliminando as redundantes
2. Para cada topologia otimizar os valores (com por exemplo L-BFGS)
3. Ficar com a melhor 

### Metodo: Genetic Programing

Semelhante a GA. Enquanto em GA o cromossoma tem tamanho fixo, na Genetic Programing o individuo é uma estrutura de tamanho variavel como uma tree ou um grafo de circuito
- mutações: acrescentar/remover elemento, trocar L por C/trocar série por paralelo, mudar um valor
- recombinação: trocar sub-circuitos inteiros entre 2 pais

Popularizada por John Koza para evoluir filtros e amplificadores

Problema - bloat: os circuitos crescem com partes inuteis (valores quase 0, elementos que se anulam, tec.) mas nao prejudicam o fitness. Soluções habituais:
- penalisar o tamanho
- podar circuitos no fim
- impor tamanho max
- tratar como problema multi-objetivo: desempenho vs nº de elementos

### Metodo: Mixed-Integer Non-Linear Programming (MINLP)

Versão mais complexa de LP. pode ter variaveis inteiras ou binarias e a função de custo e as restrições não são lineares

Uma tecnica usada é **superestrutura**: é desenhado um super-circuito com todos os elementos candidatos em todas as posições possíveis, cada um com um interruptor binário e o solver decide que interruptores ligar e com que valores

Pros: 
- com solvers globais (por exemplo SCIP, Couenne ou BARON), pode provar que a solução é ótima. **Atenção** este otimo tem uma nuance, porque dentro de cada topologia a otimização de valores continua a ser local, portanto não é ótima no sentido estrito

Contra: 
- dificil formulação
- solver sofre com não-convexidade (coisa que este projeto tem)


## Surrogates Models
#TODO: ver melhor isto


## Design inverso e modelos generativos


### Metodo: Redes tandem

1. Treina-se um modelo direto e congela-se
2. Treina-se a rede inversa, mas o erro não é calculado comparando os parametros com a resposta oficial, passa-se o que a rede inversa propos pelo modelo direto e verifica-se se a resposta resultante cumpre a especificação 

Vantagem: não precisa de solucoes otimas como rotulos, basta sortear cargas e o simulador diz à rede o quao boa foi a proposta

Limitacao: dá uma solucao por especificacao e não mostra que existem outras

### Metodo: Mixture Density Network (MDN)
...

### cVAE
...

### Difusão


## Reinforcement Learning (RL) de ajuste sequencial

É o RL tradicional

Não aprende uma solução para um problema, aprende uma estratégia para resolver qualquer problema daquele tipo

Não precisa de conhecer Z_L

**Problemas:**
- precisa de muitas amostras
- desenho do estado é delicado
- treino pode ser instável

**Hipoteses:**
- para problemas simples perde contra métodos como L-BFGS ou exhaustive search
- para problemas dinamicos é melhor
- SAC e TD3 devem ser mais eficientes que PPO com ações contínuas, devido ao **replay buffer**
- DQN fica limitado pela discretização, exceto quando o hardware já é discreto


### Algoritmo: Deep Q-Network (DQN)
### Algoritmo: Proximal Policy Optimization (PPO)
### Algoritmo: SAC
### Algoritmo: TD3

## RL ou MCTS para síntese de topologia

**A ideia geral: construir o circuito como quem joga**

Um LLM gera texto um token de cada vez: escolhe a próxima palavra com base no que já escreveu, até decidir parar. Aqui é igual, mas os “tokens” são componentes:
1. Começas com uma rede vazia entre a fonte e a carga.
2. Em cada passo, escolhes uma ação: L em série, L em paralelo, C em série, C em paralelo, ou terminar.
3. Quando terminas (ou chegas ao limite de 6 elementos), otimizam-se os valores e calcula-se a qualidade da adaptação. Essa é a pontuação final.


#TODO: Há artigos sobre isto, pesquisar: RL analog circuit topology synthesis, graph-based circuit generation

**Problemas:**
- recompensa esparsa: recompensa so no fim do episodeo, problema de atribuição de crédito, MCTS sofre menos com isto (a procura à frente propaga a pontuação final para trás pela própria árvore)
- espaço de procura enorme
- avaliações caras: para cada topologia tem que se otimizar os seus valores
  - RL vs enumeração exaustiva
  - pode-se guardar o resultado em cache, para o agent nao ter que calcular todas as vezes
  - RL/MCTS só compensa quando o espaço não se pode enumerar

**Hipotese:**

RL/MCTS escolhe topologia e otimizafor local escolhe valores (é assim que NAS em redes neurais funciona)

### Graph Neural Network (GNN)

Um circuito é naturalmente um grafo: os nós são os pontos de ligação e as arestas são os componentes. Uma Graph Neural Network lê grafos de qualquer tamanho e forma e produz uma representação que a política pode usar para decidir.

Em topologias sequenciais GNN é demasiado (um RNN é suficiente), só se torna necessária se permitires topologias arbitrárias

### Monte Carlo Tree Search (MCTS)

Algoritmo de planeamento por trás do AlphaGo e do AlphaZero

Pesquisar melhor sobre isto

## Questão dos Contextual Bandits e RL offline

#TODO: ver melhor isto
### One-Armed Bandit

### Multi-Armed Bandit

### Contextual Bandit

### Thompson Sampling

### RL Offline

## LLM como otimizador ou operador evolutivo

Ideia: LLM ser uma ferramenta para outros algoritmos

**Problemas:**
- fraca precisão numerica: LLMs são maus com números precisos
- custo e latência: maior custo que mutações gaussianas
- não determinismo: mesmo prompt com respostas diferentes, o modelo (comercial) poder ser atualizado sem aviso
- contaminação: lembrar-se de resultados de exercicios (data leakage)

**Hipotese:**
- Aproximação mais rápida nas primeira iterações: o conhecimento no dominio conduz logo para a zona certa dando um bom ponto de partida
- Refina pior que CMA-ES: para valores
- Melhor como operador do que sozinho: dentro de um GA os erros do LLM são filtrados pela seleção
- Com estes pontos, a melhor proposta seria: GA para selação, LLM para propor mutações estruturais, L-BFGS para afinar valores


### Como otimizador

LLM é o algoritmo de otimização:
1. prompt contem histórico: soluções já experimentadas e custo de cada uma ordenadas
2. pede-se ao LLM para propor uma nova solução melhor que as no historico
3. avalia-se a proposta no simulador, junta-se no historico e repete-se

#TODO: pesquisar OPRO da Google DeepMind (2023), que mostrou que um LLM consegue otimizar desta forma em vários problemas

### Como operador dentro de GA

A mutação (ou a recombinação) passa a ser uma chamada ao LLM: “eis esta rede e a sua resposta, propõe uma modificação”

#TODO: pesquiar precedentes desta ideia: FunSearch (DeepMind, publicado na Nature em 2023) e o AlphaEvolve (DeepMind, 2025) usam LLMs como operadores evolutivos para descobrir programas e algoritmos novos, e chegaram a resultados matemáticos inéditos

## Agente LLM com ferramentas

Ideia: 

LLM ter outros algoritmos como ferramentas, LLm é que conduz o trabalho

Imita o fluxo de trabalho de um engenheiro. le as especificações, percebe a carga, escolhe uma abordagem, simula, verifica, ajusta e documenta.

Uma coisa boa é dar para aceitar especificações em linguagen natural que seriam dificies de formalizar. ex: “o menor número de componentes possível”, “evita condensadores abaixo de 1 pF, que têm tolerâncias más”

Loop:
1. Pensar: Baseado no que sabe e no problema, como pode resolver ou dar um passo na resolução
2. Agir: Chama as ferramentas que precisa
3. Observar: Analisa os resultados que obteve
4. Repetir até concluir a tarefa

Exemplos de ferramentas:
- ler a impedância da antena em cada frequência
- dizer o melhor resultado teoricamente possível (limite bode fano)
- calcular solução analitica
- otimizar valores com L-BFGS com multistart
- ver os valores comerciais que existem
- simular
- analisar tolerancias


**Problemas:**
- Alucinações:
- Custo:
- Reprodutibilidade dificil:
- Dependencia de modelos proprietários:

**Hipotese:** Forte nas decisões qualitativas (topologia, restrições, interpretação). Os números finais devem vir sempre de ferramentas numéricas.

## LLM para descobrir heurísticas

Baseado em que muitas escolhas do engenheiro são “hipóteses pragmáticas baseadas em heurísticas empíricas”


Uma das formas: GA com LLM como operador (como em "LLM como otimizador ou operador evolutivo"), mas o "cromossoma" é codigo:
1. Esqueleto fixo: Um programa com uma única função a evoluir, e um avaliador que corre essa função num conjunto de testes e lhe dá uma pontuação
2. Base de dados de programas: Guarda-se todos os programas gerados e as suas pontuações
3. Pedido ao LLM: Mostra-se os melhores programas por ordem de pontuação e pede-se para escrever uma versão melhor
4. Avaliação Automática: Corre-se o programa de novo. Se der erro/demorar/pontuar mal descarta-se, se for bom entra na base de dados
5. Repete-se

Alucinações do LLM deixam de ser perigosas: Se o LLM escrever uma fórmula errada, o avaliador dá-lhe má pontuação e o programa morre. O LLM traz criatividade e o avaliador garante a correção

É interpretável. O resultado é código que podes ler e uma heurística descoberta pode ser relevante. É reutilizável, sem LLM. Depois de encontrado, o programa é uma função normal

**Problemas:**
- muitas chamadas ao LLM
- precisa de um conjunto diverso de testes: por exemplo, o LLM pode escrever para uma função que apenas retorna o resultado(reward hacking). As proteções são as do ML clássico:
  -  separar as cargas em treino, validação e teste
  -  sortear cargas novas periodicamente
  -  penalizar programas compridos
  -  ler o código dos melhores programas
- resultado é imprevisivel: pode demorar muito a encontrar nada melhor que a baseline

**Hipotese:**
- não resolve diretamente o problema principal, melhora uma peça de outro método: o ponto de partida do L-BFGS
- pode descobrir regras de inicialização claramente melhores do que inícios aleatórios

O resultado mais interessante seria um programa legível que se aproxime de Design inverso e modelos generativos

#TODO: Pesquisar: foi esta combinação que fez o **FunSearch (DeepMind, 2023)** descobrir heurísticas novas para problemas como o bin packing (arrumar objetos no menor número de caixas possível), e que o **AlphaEvolve (2025)** levou mais longe, incluindo heurísticas usadas na prática em centros de dados.

## Meta-Learning e Transfer Learning


Transfer learning: reaproveitar o que se aprendeu. Treina-se numa tarefa e reutiliza-se noutra. Tipo fine-tunning

Meta-learning: treinar explicitamente para se adaptar depressa. O treino é organizado em muitas tarefas, e o objetivo não é ser bom numa delas, mas sim ser bom depois de poucos passos de adaptação a uma tarefa nova.

#TODO: completar isto



#TODO: Pesquisar: MAML - exemplo de meta-learning


## LLM pequeno ajustado ao domínio ou RAG

#TODO: completar

### fine-tuning de um LLM pequeno

### RAG

## Otimização robusta e de rendimento (yield)
#TODO: completar

## Resumo


