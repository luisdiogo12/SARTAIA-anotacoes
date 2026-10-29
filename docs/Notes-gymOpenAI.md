# Notes: docs. OpenAI gymnasium library


Entrepertação dos resultados do treino:
- reward plot: deve mostrar uma melhora gradual 
- episode length: deve estabilizar para um numero otimo de actions por episode. episodes curtos sugerem que o agent chegou a um terminal state que não faz parte do objetivo; episodes longos sugerem que o agent está a precisar de mais passos do que é ótimo para chegar ao objetivo
- training error: deve diminuir sobre o tempo, indicando que as previsoes do agent ficam cada vez mais precisas. picos largos no inicio do treino são normais a medida que o agent encontra novas situacoes


Problemas comuns no treino e solucoes:
- Agent nunca melhora:
  - sintomas: reward mantem-se constante; erros de treino grandes
  - causas: learning rate demasiado alta ou baixa, má reward function; bugs na logica de update
  - solucoes: experimentar learning rates entre 0.001 e 0.1; revificar que as rewards recebidas são significantes; verificar se a Q-table está a ser updated
- Treino nunca termina:
  - sintomas: rewards muito volateis; nunca converge
  - causas: learning rate demasiado alta; exploration insuficiente
  - solucoes: reduzir learning rate; garantir uma exploration minima (final_epsilon ≥ 0.05); treinar por mais episodes
- Agent fica preso numa má estrategia:
  - sintomas: a melhora termina demasiado cedo; performance final sub-otima
  - causas: exploration demasiado baixa; learning rate demasiado baixa
  - solucoes: aumentar o tempo de exploracao (epsilon decay mais lento); experimentar um learning rate mais alto inicialmente; usar diferentes extrategias de exploration
- Aprender demasiado lentamente:
  - sintomas: agent melhora mas muito gradualmente
  - causas: learning rate demasiado baixa; demasiada exploracao
  - solucoes: aumentar o learning rate (tendo atencao à instabilidade); epsilon decay mais rapido (menos exploration aleatoria); treino mais focado em states dificeis

Para a construção de um environment, questionar sobre os seguintes aspetos:
- o que é que o agent deve aprender? - definir o problema
- que info o agent precisa? - definir observation set
- que actions o agent pode tomar? - definir action set
- como medir o sucesso? - definir objetive e reward function
- quando é que um episode deve terminar? - definir end state

Armadilhas comuns no design dum environment:
- problemas na reward function
  - problema: apenas dá uma reward positiva se o agent chegar ao objetivo
  - melhor: ter um feedback interno
- problemas na representacao de um state
  - problema: incluir detalhes irrelevantes ou faltar com detalhes cruciais
  - melhor: incluir exatamente o que é necessario para decisoes otimas
- provlemas com action space
  - problema: actions nao fazem sentido ou sao impossiveis de executar
- erros em boundary handling
  - problema: permitir states invalidos ou comportamentos de boundaries ambiguas
  - melhor: boundary handling clara e consistente


Real-World Environment Design Tips:
- **Comeca simples e adiciona complexidade gradualmente**
  - 1º comaça por por a funcionar os movimentos basicos e goal-reaching
  - 2º adiona obstaculos, objetivos multiplos ou pressão temporal
  - termina com a adicao de dinamicas complexas, observacao parcial ou interacoes multi-agent
- Design para aprendezagem
  - criterios de sucesso claros: agent deve saber quando está a agir corretamente
  - regras consistentes: mesma action no mesmo state deve produzir o mesmo efeito
  - observations informativas: incluir tudo o que for necessario para ser possivel tomar decisoes otimas
- pensa sobre as tuas questoes de pesquisa
  - navegacao: foco em spatial reasioning e path planning
  - control: da enfase nas dinamicas, estabilidade e continuous actions
  - strategia: inclui informacao parcial, modelacao de oponente ou long-term planning
  - otmizacao: design trade-offs claros e restricoes de recursos


