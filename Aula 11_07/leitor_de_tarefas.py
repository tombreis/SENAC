import os

caminho = 'tarefas.txt'

#Função para abrir arquivo e ler como lista
def ler_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        print(arquivo.read())

#Função para adicionar conteúdo ao existente
def atualizar_arquivo(caminho, texto):
    with open (caminho, 'a', encoding= 'utf-8') as arquivo:
        arquivo.write("\n"+texto) 

#Função para sobrescrever o conteúdo do arquivo
def escrever_arquivo(caminho):
    texto = input("Digite uma nova tarefa:\n")
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)               

#Função para deletar arquivo
def deletar_arquivo(caminho):
    os.remove(caminho)

