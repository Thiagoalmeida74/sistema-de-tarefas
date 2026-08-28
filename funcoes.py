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