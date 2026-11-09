#

## Notas

talvez seja util tb fazer o curso de MCP do hugging face

pesquisar a descrição de circuitos usando SPACE

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
