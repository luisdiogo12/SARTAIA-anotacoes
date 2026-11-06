#

## Notas

talvez seja util tb fazer o curso de MCP do hugging face

## Onde rodar modelos

**Laptops dos meus irmãos**

**Server IT**


### Groq

| model id                     | reasoning | prompt caching | struct output |
| :--------------------------- | :-------: | :------------: | :-----------: |
| openai/gpt-oss-20b           |     x     |       x        |     both      |
| openai/gpt-oss-120b          |     x     |       x        |     both      |
| openai/gpt-oss-safeguard-20b |     x     |       x        |  Best-effort  |
| qwen/qwen3.8-27b             |     x     |       -        |     both      |
| minimaxai/minimax-m2.7       |     x     |       -        |       -       |
| meta-models/muse-spark-open  |     x     |       -        |     both      |


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

