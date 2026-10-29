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

redes descritas por matrizes ABCD

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

#### Genetic Algorithm

já estudei

#### Particle Swarm Optimization

já estudei

#### Simulated Annealing

já estudei

#### CMA-ES

Práticamente faz o mesmo que BFGS mas sem gradientes
