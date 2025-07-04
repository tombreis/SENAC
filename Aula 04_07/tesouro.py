import random

lugares = ["NORTE", "SUL", "LESTE", "OESTE"]

def randomizar_tesouro (lugares):
    local_escondido = random.choice(lugares)
    return local_escondido

def escolha(lugares):
    numero_menu = 1
    for local in lugares:
        print(f"{numero_menu}- {local}")
        numero_menu = numero_menu + 1
    escolha_jogador = int(input("Aonde está o Tesouro ???\n"))

    return escolha_jogador

def resutado (valor_escolhido, escolha_pc):
    if valor_escolhido == escolha_pc:
        print("ACHOU O TESOURO !!!")
    else
        print(f"você não achou o Tesouro")    