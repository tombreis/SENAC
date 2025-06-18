IDADE_MINIMA = 16
Idade = int(input("Insira a Idade do Usuário:"))
if Idade >= IDADE_MINIMA:
    print("AUTORIZADO")   
else:
    Pais = input("Possui autorização dos pais ?")
    if Pais == "Sim" or Pais =="SIM" or Pais =="sim" or Pais =="S" or Pais =="s":
        print("AUTORIZADO") 
    else:
        print("NÃO AUTORIZADO")