from tarefa import Tarefa

def criar_tarefa(tarefas):
    titulo = input("digite o titulo: ")
    descricao = input("digite a descrição: ")
    prioridade = input("qual é a prioridade?:")
    
    novo_id = criar_id(tarefas)
       
    tarefa = Tarefa (novo_id, titulo, descricao, prioridade)   
    
    tarefas.append(tarefa)
    
    print("tarefa criada com sucesso!")
    
    
def criar_id(tarefas):
    if not tarefas:
        return 1
    
    return max(tarefa.id for tarefa in tarefas) + 1

def mostrar_tarefa(tarefa):
    print(f"ID: {tarefa.id}")
    print(f"Título: {tarefa.titulo}")
    print(f"Descrição: {tarefa.descricao}")
    print(f"Prioridade: {tarefa.prioridade}")
    print(f"Status: {tarefa.status}")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        mostrar_tarefa(tarefa)
        print("-" * 30)
        
def buscar_tarefas(tarefas):
    buscar = input ("qual é o nome da tarefa que voce esta buscando?: ")
    
    encontrou = False
    
    if not tarefas:
        print("nenhuma tarefa encontrada")
        return
        
        
    for tarefa in tarefas:
        
        if buscar == tarefa.titulo:
             mostrar_tarefa(tarefa)
             encontrou = True
             
        if not encontrou:
            print("nenhuma tarefa encontrada.")
        