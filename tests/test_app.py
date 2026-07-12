# Sistema de gerenciamento de tarefas desenvolvido para a disciplina de Engenharia de Software

from src.app import criar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa, tarefas

def setup_function():
    tarefas.clear()

def test_criar_tarefa():
    criar_tarefa("Estudar Python")
    assert len(tarefas) == 1
    assert tarefas[0] == "Estudar Python"

def test_editar_tarefa():
    criar_tarefa("Tarefa antiga")
    editar_tarefa(0, "Tarefa nova")
    assert tarefas[0] == "Tarefa nova"

def test_excluir_tarefa():
    criar_tarefa("Excluir")
    excluir_tarefa(0)
    assert len(tarefas) == 0

def test_listar_tarefas():
    criar_tarefa("Projeto")
    assert listar_tarefas() == ["Projeto"]
