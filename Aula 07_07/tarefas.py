tarefas = []

count = 0
while count < 3  :
    nome_tarefa = input("Insira uma nova tarefa: ")
    tarefas.append(nome_tarefa)

    print (tarefas)
    count += 1
    
tarefa_delete = input("Remova uma tarefa: ")
tarefas.remove(tarefa_delete)
print (tarefas)