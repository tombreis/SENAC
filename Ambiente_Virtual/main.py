idade = int(input("Insira sua idade: \n"))
clube = input("Club de Descontos (S) ou (N): \n").upper()

if idade >= 60 and clube == "S":
    print("Ganhou Desconto VIP !")
elif idade >= 60 or clube == "S":
    print("Ganhou Desconto Básico !")
else:
    print ("Sem Desconto !")