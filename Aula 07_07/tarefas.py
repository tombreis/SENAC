tarefas = []

count = 1
while count < 4  :
    nome_tarefa = input("Insira uma nova tarefa: ")
    tarefas.append(nome_tarefa)

    print (f"{count} - {tarefas[count-1]}")
    count += 1
    
tarefa_delete = input("Remova uma tarefa: ")
tarefas.remove(tarefa_delete)
print (tarefas)