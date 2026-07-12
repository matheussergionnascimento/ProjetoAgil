# Projeto Ágil - Sistema de Gerenciamento de Tarefas

## Objetivo

Desenvolver um sistema de gerenciamento de tarefas utilizando metodologias ágeis e boas práticas de Engenharia de Software.

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Editar tarefas
- Excluir tarefas

## Tecnologias Utilizadas

- Python
- Git
- GitHub
- GitHub Actions
- Pytest

## Estrutura do Projeto

```
ProjetoAgil/
│
├── .github/
│   └── workflows/
│       └── python.yml
│
├── src/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── README.md
└── .gitignore
```

## Como executar

```bash
python src/app.py
```

## Executar os testes

```bash
python -m pytest
```

## Mudança de Escopo

Durante o desenvolvimento foi simulada uma mudança de escopo com a proposta de adicionar autenticação de usuários em uma versão futura do sistema.