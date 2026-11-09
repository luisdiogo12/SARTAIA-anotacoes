# Paper: AnalogSeeker: An Open-source Foundation Language Model  for Analog Circuit Design

[@chenDatasetConstructionTraining2026]

## Resumo

Modelo [AnalogSeeker](https://huggingface.co/analogllm/analogseeker.Detailed) que tem por base o modelo Qwen2.5-32B-Instruct.
Obteve melhoras no design de circuitos.
Criaram um corpus apartir do processamento de livros
NSC-SFT (neighborhood self-constrained supervised fine-tuning) no modelo base
Experimentaram mais modelos base e variações com diferentes tecnicas pos treino
**DeepSeek-v3 saiu-se muito bem**
**Analisaram o modelo como agent** em 3 tarefas: topology design, topology modification, and circuit analysis
- topology design e modification: agent design ou modifica a topologia baseando-se nos requerimentos atuais e resultados de simulações
- circuit analysis: agent refina a topologia numa **netlist SPICE** e listas de parametros designaveis e o seu alcance
Mostram um exemplo de prompts ao agent

## Introduction

2 refs a demonstrar que de modo geral LLMs mainstream sem mods não conseguem design de circuitos basicos

refs a demonstrar LLMs com datasets conseguem design de circuitos especificos como OpAmps e passive power converters

multi-agents frameworks com CoTs e RAG ajuda em design circuitos

fala da falta de dados e de algumas entidades que fizerem o mapeamento de variabilidades e metricas de performance, mas estes dados nao sao muito bons para LLMs

**AMSBench-TQA benchmark**: analog circuit knowledge evaluation


