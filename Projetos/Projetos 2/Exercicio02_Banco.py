SALDO_INICIAL=1000
Saldo = SALDO_INICIAL
while True :
    print("""\n===== CAIXA ELETRÔNICO SIMPLES =====
        1 - Consultar Saldo
        2 - Depositar Valor
        3 - Sacar Valor
        4 - Sair
====================================
        """)
    select = input("\nInsira a opção desejada (1 - 4): ")
    if select == ("1"):
        print ("\nSaldo Atual: ",Saldo)
    elif select == ("2"):
        deposito = float (input("\nDigite o valor a ser Depositado: "))
        Saldo = float (Saldo + deposito)
        print ("\nVALOR DEPOSITADO COM SUCESSO !")
    elif select == ("3"):
        saque = float (input("\nDigite o valor a ser Sacado: ")) 
        Saldo = float (Saldo - saque)
        print ("\nVALOR SACADO COM SUCESSO !")
    elif select == ("4"):
        break    