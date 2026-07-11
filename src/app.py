tarefas = []

def criar_tarefa(nome):
    tarefas.append(nome)
    return "Tarefa cadastrada com sucesso!"

def listar_tarefas():
    return tarefas

def editar_tarefa(indice, novo_nome):
    if 0 <= indice < len(tarefas):
        tarefas[indice] = novo_nome
        return "Tarefa atualizada!"
    return "Tarefa não encontrada."

def excluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        return "Tarefa removida!"
    return "Tarefa não encontrada."

def menu():
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Editar tarefa")
        print("4 - Excluir tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            print(criar_tarefa(nome))

        elif opcao == "2":
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(listar_tarefas()):
                print(f"{i} - {tarefa}")

        elif opcao == "3":
            indice = int(input("Número da tarefa: "))
            novo = input("Novo nome: ")
            print(editar_tarefa(indice, novo))

        elif opcao == "4":
            indice = int(input("Número da tarefa: "))
            print(excluir_tarefa(indice))

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()