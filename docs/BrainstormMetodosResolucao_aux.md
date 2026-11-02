#

## draft

o que procurar?: encontrar valores vs encontrar topologias

como procurar?

é um problema estático, sequencial ou bandit? e como identificar e usar essa identificação (para talvez solução adaptativa)?

world models: simulador (leis fisicas) vs surrugate (dados) vs real-word (a verdade)

métricas: taxa de sucesso, qualiadade do resultado, taxa de alucinação, numero avaliações necessárias, custo temporal real, ...


Métodos: 
- Sintese Tradicionar
- Otimização Numerica - L-BFGS
- Metaheuristicas 
- Space mapping, Multi-Fidelity Bayesian Optimization
- Machine Learning Supervised learning
- Reinforcement learning
- LLMs

##

## Projetar vs Sintonizar

## Problema

Devo explorar e definir o que procurar, a natureza do problema e os objetivos?

O que procurar:
- Procurar **valores contínuos** numa topologia fixa
- Procurar **valores discretos** numa topologia fixa
- Procurar **topologia + valores**

Natureza do problema:
- Ação muda situação seguinte?
  - Não -> bandit
  - Sim -> sequencial
- Que info precisa para decidir?
  - Nada -> sem contexto
  - Tudo -> obs completa
  - Parte -> obs parcial
- Environment muda sozinho?
  - Não -> estacionário
  - Sim -> dinamico

Objetivo:
- Que métrica?
- Como agregar na banda?
- Um objetivo ou vários?
- Restrições
- Nominal ou robusto?

O que se produz:
- Produzir **solução** para um problema
- Produzir **modelo ou política** para uma familia de problemas, de imediato
- Produzir **conhecimento prévio** para arrancar mais depressa num problema novo
- Produzir **programa que soluciona** para uma familia de problemas, de forma interpretável


Dificuldade intrinseca:


## Objetivo

## Environment Model

## Search