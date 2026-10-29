# Notes: `Deep RL Course` Hugging Face

[repo exercicios (branch dev)](https://github.com/luisdiogo12/HF-deepRL/tree/dev)

## Unit 1: Introdução a Deep Reinforcement Learning

Agent é responsável por produzir as actions, $A_t$.

Environment é responsável por produzir os states, $S_t$, e as rewards, $R_t$.

Markov Decision Process (MDP)

Markov Property implies that our agent needs only the current state to decide what action to take and not the history of all the states and actions they took before.

Observations/States é a informação dada pelo environment ao agent

State, $s$, é uma descição completa do estado do universo. Num environment completamente observado
Observation, o, é uma descrição parcial do estado. Num environment parcialmente observado

Action space é o set de todas as possiveis actions num environment. As actions podem vir de um espaço continuo ou discreto

Reward é o unico feedback que o agent tem para saber se a action foi boa ou má

Reward Function:
$$
r(s_t, a_t)
$$

Cumulative Reward Function:
$$
R({\tau}) = \sum_{k=0}^{\infty} r_{t+k+1} = r_{t+1} + r_{t+2} + r_{t+3} + ...
$$

Cumulative Reward Function with Discount (gamma):
$$
R({\tau}) = \sum_{k=0}^{\infty} {\gamma}^k r_{t+k+1} = r_{t+1} + {\gamma} r_{t+2} + {\gamma}^2 r_{t+3} + ...
$$

Task é uma instancia de um problema de RL. Podem ser de 2 tipos: episodic e continuing

Episodic Task é uma lista de states, actions e rewards, sendo que essa lista tem um start state e um terminal state

Continuing Task não têm um terminal state, continuando para sempre. Nestas tasks o agent tem que aprender e interagir com o environment simultaneamente

Exploration é a exploração do environment apartir da exprimentação de actions aleatorias com o objetivo de obter mais informação sobre o environment.

Explotation é a explotação de informação conhecida com o objetivo de maximizar a reward

Exploration vs Explotation trade-off

Policy ${\pi}$ é o "cerebro do agent", é a função que diz que actions tomar dado um estado. Portanto, define o comportamento do agent. 
Esta policy é a função que se pretende aprender e o objetivo é encontrar a policy otima, ${\pi}^{\star}$, ou seja, a policy que maximiza a reward esperada.  
${\pi}^{\star}$ é encontrada através do treino.
Existem duas abordagens de como treinar o agent para encontrar ${\pi}^{\star}$:
- Policy-Based Methods: Diretamente, ensinando o agente a aprender que action deve tomar dado o state atual
- Value-Based Methods: Indiretamente, ensinando o agente a aprender que estado é o vais valioso e depois tomar a action que leva a esse estado.

Em Policy-Based Methods a policy function é aprendida diretamente. Esta função irá definir um mapeamento de cada state para a melhor action correspondente. Alternativamente, pode definir a probabilidade distribuida sobre o set de possiveis actions naquele state
Existem 2 tipos: O Deterministic, onde a policy a um dado state retorna sempre a mesma action. E o Stochastic, que outputs uma probabilidade distribuida sobre as actions

Em Value-based Methods, em vez de aprender a policy function, aprende a value function que mapeia o state ao expected value de estar naquele state.
O valor de um state é o expected discounted return que o agente pode obter se começar naquele state, e depois age de acordo com a policy, ou seja, vai para o state com o value mais alto

Q-Learning (classic Reinforcement Learning) and then Deep Q-Learning

bibliotecas Deep RL famosas: Stable Baselines3, RL Baselines3 Zoo, CleanRL and Sample Factory 2.0.

## Unit 2: Introdução a Q-Learning

Relembrar: em value-based methods a value function mapeia states ao expected value de estar naquele state

Em value-based methods o value de um state é o expected discounted return que o agent consegue se começar naquele state e agir de acordo com a policy.

$$
\underbrace{v_{\pi}(s)}_{\text{Value function}} = \mathbb{E}_{\pi}\Big[ \underbrace{R_{t+1} + \gamma R_{t+2} + \gamma^{2} R_{t+3} + \dots}_{\text{Expected discounted return}} \;\Big|\; \underbrace{S_t = s}_{\text{Starting at state } s} \Big] = \mathbb{E}_{\pi}\left[ \sum_{k=0}^{\infty} \gamma^{k} R_{t+k+1} \;\middle|\; S_t = s \right] = \mathbb{E}_{\pi}\left[ G_t \mid S_t = s \right]
$$

Relembrar: o objetivo de um agent é ter uma optimal policy $\pi^{\star}$

Para encontrar $\pi^{\star}$ existem 2 metodos, Policy-based e Value-based.

Policy-based methods: 
- treina diretamente a policy para selecionar a action a realizar dado o state (ou a probability distribuition sobre as actions naquele state)
- é uma deterministic policy
- não usa value function
- não definimos o comportamento da policy, training é que a define

Value-based methods:
- não treina a policy
- a policy tem que ser uma função definida manualmente, por exemplo uma greedy policy para tomar sempre a ação com a maior reward
- treina-se a value-function para que a policy tenha melhor info

Encontrar a optimal value function, $Q^{\star}$, leva a ter uma optimal policy, $\pi^{\star}$:
$$
\pi^{*}(s) = \arg\max_{a} Q^{*}(s, a)
$$

Na maior parte dos casos em value-based methods a *Epsilon-Greedy Policy* é usada porque lida com exploration/exploitation trade-off

Existem 2 tipos de value-based functions, a state-valu function e a action-value function.

State-value function:
- para cada state outpus a expected return se o agent comecar naquele state e segue a policy 
- é calculado o value do state $S_t$
$$
V_{\pi}(s)= \mathbb{E}_{\pi}\left[ G_t \mid S_t = s, A_t = a \right]
$$

Action-value function:
- outputs a expected return se o agente comecar naquele estado, tomar uma action e depois segue a policy
- é calculado o value do par state-action $(S_t,A_t)$
$$
\underbrace{Q_{\pi}(s,a)}_{\text{Value do par state-action s,a}} = 

\mathbb{E}_{\pi}\left[ G_t \mid \underbrace{S_t = s}_{\text{Se agent começar no state s}},
\underbrace{A_t = a}_{\text{e escolher a action a}}
 \right]
$$

### Equação de Bellman

Problema: para calcular o valor de um state $V(S_t)$ pela definição, é preciso somar todas as rewards desde esse state até ao fim, seguindo a policy. Para obter $V(S_{t+1})$ repete-se quase todo o mesmo cálculo. Fazer isto para cada state (ou para cada par state-action) é redundante e custoso.

Solução: a equação de Bellman define o valor de um state de forma recursiva, como a soma de duas partes:
- a reward imediata $R_{t+1}$;
- o discounted valeu do state seguinte, $\gamma V(S_{t+1})$.
- 
$$
V(S_t) = R_{t+1} + \gamma V(S_{t+1})
$$
O mesmo vale para os estados seguintes:
$$
V(S_{t+1}) = R_{t+2} + \gamma V(S_{t+2})
$$
e assim sucessivamente.

Ideia-chave: em vez de calcular o retorno completo para cada estado, aproveita-se o valor já conhecido do estado seguinte. A abordagem é semelhante à de Programação Dinâmica.

Porque $R_{t+1}$ e $S_{t+1}$ são aleatórios:

$$v_\pi(s) = \mathbb{E}\pi\left[R{t+1} + \gamma, v_\pi(S_{t+1}) \mid S_t = s\right]$$

A versão sem $\mathbb{E}$ só é exata em ambientes e policies determinísticos.

### Monte Carlo vs Temporal Difference
São duas estratégias para treinar a value function (ou a policy) a partir do treino. A diferença está em quando se faz a atualização:
- Monte Carlo (MC): espera pelo fim do episode.
- Temporal Difference (TD): atualiza a cada step $(S_t, A_t, R_{t+1}, S_{t+1})$.

### Monte Carlo
1. O agent joga um episode completo segundo a policy (por exemplo, $\varepsilon$-greedy).
2. No fim, calcula o real return $G_t$ a partir da lista de transições recolhidas.
3. Usa $G_t$ como alvo para atualizar $V(S_t)$:

$$V(S_t) \leftarrow V(S_t) + \alpha\left[G_t - V(S_t)\right]$$

Exemplo ($\alpha = 0.1$, $\gamma = 1$, $V$ inicializado a 0, $G_0 = 3$):
$$V(S_0) = 0 + 0.1,[3 - 0] = 0.3$$

### Temporal Difference (TD(0) / one-step TD)
1. O agente dá um step e observa $R_{t+1}$ e $S_{t+1}$.
2. Como ainda não conhece $G_t$, estima-o com o TD target: $R_{t+1} + \gamma V(S_{t+1})$
3. Atualiza $V(S_t)$ de imediato:
$$V(S_t) \leftarrow V(S_t) + \alpha\left[R_{t+1} + \gamma V(S_{t+1}) - V(S_t)\right]$$

Chama-se bootstrapping a esta técnica de atualizar uma estimativa com base noutra estimativa, $V(S_{t+1})$, em vez de usar o real return.

Exemplo ($\alpha = 0.1$, $\gamma = 1$, $V$ inicializado a 0, $R_1 = 1$):
$$V(S_0) = 0 + 0.1,[1 + 1 \cdot 0 - 0] = 0.1$$

## resumo

