BALA = 0.50
CHOCO = 3.00
BISC = 3.50
PIRULITO = 2.00
total = 0.00
subtotal = 0.00
while True:
    print ("------DOCES BARBOSA------\n\n"
        "(1)BALA = R$ 0,50\n"
        "(2)CHOCOLATE = R$ 3,00\n"
        "(3)BISCOITO = R$ 3,50\n"
        "(4)PIRULITO = R$ 2,00\n")
    #print(f"Total da sua compra é R$: {total}")
    produto = int (input("Selecione o Produto ou digite 0 para sair: \n"))
    if produto == 0:
        break
    else:        
        qtd = int (input("Selecione a Quantidade: \n"))    
    if produto == 1:
        subtotal =  BALA * qtd
        print(f"Você comprou {qtd} Unidades. Seu Subtotal é R${subtotal: .2f}")
        total += subtotal
        opcao = input("Deseja comprar outro item ? (s/n)\n") 
        if opcao == "s":
            total += subtotal
            continue
        else:
            print(f"Total da sua compra é R$: {total}")
            break
    elif produto == 2:
        subtotal = CHOCO * qtd
        print(f"Você comprou {qtd} Unidades. Seu Subtotal é R${subtotal: .2f}")
        total += subtotal
        opcao = input("Deseja comprar outro item ? (s/n)\n") 
        if opcao == "s":
            total += subtotal
            continue
        else:
            print(f"Total da sua compra é R$: {total}")
            break
    elif produto == 3:
        subtotal = BISC * qtd
        print(f"Você comprou {qtd} Unidades. Seu Subtotal é R${subtotal: .2f}")
        total += subtotal
        opcao = input("Deseja comprar outro item ? (s/n)\n") 
        if opcao == "s":
            total += subtotal
            continue
        else:
            print(f"Total da sua compra é R$: {total}")
            break
    elif produto == 4:
        subtotal = PIRULITO * qtd
        print(f"Você comprou {qtd} Unidades. Seu Subtotal é R${subtotal: .2f}")
        total += subtotal
        opcao = input("Deseja comprar outro item ? (s/n)\n") 
        if opcao == "s":
            total += subtotal
            continue
        else:
            break
input("")        