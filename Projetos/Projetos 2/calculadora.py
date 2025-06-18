a = 0
b = 0
res = 0

print("========CALCULADORA MATEÁTICA========\n\n" \
"MENU DE OPERAÇÕES\n\n" \
"(1)Soma\n"
"(2)Subtração\n"
"(3)Multiplicação\n"
"(4)Divisão\n"
"(5)Raiz Quadrada\n\n")

opr = int (input("Selecione a operação a ser realizada: \n"))

if opr == 1:
    print ("Você selecinou Soma !\n")
    a = int (input ("Insira o Primeiro valor: \n"))
    b = int (input ("Insira o Segundo valor: \n"))
    res = int (a+b)
    print (f"O resultado da soma é: {res}")
elif opr == 2:
    print ("Você selecinou Subttração !\n")
    a = int (input ("Insira o Primeiro valor: \n"))
    b = int (input ("Insira o Segundo valor: \n"))
    res = int (a-b)
    print (f"O resultado da Subtração é: {res}")    
elif opr == 3:
    print ("Você selecinou Multiplicação !\n")
    a = int (input ("Insira o Primeiro valor: \n"))
    b = int (input ("Insira o Segundo valor: \n"))
    res = int (a*b)
    print (f"O resultado da Multiplicação é: {res}")
elif opr == 4:
    print ("Você selecinou Multiplicação !\n")
    a = int (input ("Insira o Primeiro valor: \n"))
    b = int (input ("Insira o Segundo valor: \n"))
    res = int (a/b)
    print (f"O resultado da Multiplicação é: {res}")
else:
    print ("Você selecinou Raiz Quadrada !\n")
    a = int (input ("Insira o Valor: \n"))
    res = a ** 0.5
    print (f"A Raiz Quadrade de {a} é: {res}")
input ("Aperte ENTER para sair")    