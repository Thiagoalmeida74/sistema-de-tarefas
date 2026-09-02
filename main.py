from funcoes import criar_tarefa, listar_tarefas, buscar_tarefas


def mostrar_menu():
    print("1 - criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Buscar tarefa")
    print("4 - Editar tarefa")
    print("5 - Excluir tarefa")
    print("6 - Alterar status")
    print("7 - Filtrar tarefas")
    print("8 - Sair")
    opcao = input("Digite a opção desejada: ")
    return opcao

def main():
    tarefas = []
    while True:
        opcao = mostrar_menu()
        if opcao == "1":
            criar_tarefa(tarefas)
            
        elif opcao =="2":
            listar_tarefas(tarefas)
            
        elif opcao =="3":
            buscar_tarefas(tarefas)
                        
        elif opcao == "8":
            print("Até logo!")
            break
        
        else:
            print("opcao invalida")

main()

