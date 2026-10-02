# Anotações relativas à Dissertação: Síntese Automática de Redes de Transformação usando Algoritmos de Inteligência Artificial (SARTAIA)

## 1. Introdução

Este repositório destina-se a hospedar as anotações relativas à dissertação, estando estas localizadas em `./docs/`.

O registo das tarefas realizadas e a realizar é efetuado no relatório de progesso, localizado em `./RelatorioDeProgresso.md`. Complementar a este documento, existe ainda o registo do `git log` que permite também a expor as datas de criação e edição dos anotamentos neles mesmo.

## 2. Setup

Requisitos:
- uv
- git

```bash
cd SARTAIA-anotacoes
uv sync
```

## 3. Comandos

```bash
uv run mkdocs serve     # servidor local em http://127.0.0.1:8000
uv run mkdocs build     # gerar o site estático na pasta site/
```

## 4. Escrita

Links uteis:

- [mkdocs - User Guide](https://www.mkdocs.org/user-guide/)
- [Material for MkDocs - Reference](https://squidfunk.github.io/mkdocs-material/reference/)
- [PyMdown - Extension](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/)
- [Python Markdown - Extensions](https://python-markdown.github.io/extensions/)
