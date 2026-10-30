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

redes descritas por matrizes ABCD e outras
Neural Architecture Search (NAS)
rede neuronal feedforward (FNN)
tunable matching network (TMN)
Zeroth-Order Projected Gradient Descent (ZO-PGD)

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

...

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


## RL de ajuste sequencial

## Resumo

encontrar valores vs encontrar topologias
