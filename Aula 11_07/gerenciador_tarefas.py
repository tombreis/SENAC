import leitor_de_tarefas

caminho = 'tarefas.txt'

while True :
    escolha = input("Escolha uma opção: 1 - Nova Tarefa / 2 - Ler Tarefa / 3 - Sair")

    if escolha == "1":
        #Adicona uma tarefa
        texto = input("Escreva o Texto")
        leitor_de_tarefas.atualizar_arquivo(caminho, texto)
        pass
    elif escolha == "2":
        #Lê uma tarefa
        leitor_de_tarefas.ler_arquivo(caminho)
        pass
    elif escolha == "3":
        #Sair do programa
        break
    else:
        print("Opção Inválida ! Digite uma opção válida.")
