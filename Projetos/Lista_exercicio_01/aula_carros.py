idade = int (input("Insira sua idade: \n"))

menu_infantil = ["-Hot Wheels (a coleção toda!)", "-Filme Carros (Relâmpago Marquinhos Acelera!)"]
menu_adulto = ["-Fusca 70: A partir de R$15.000" ,"-Alpha Romeo: A partir de R$20.000", "-Meriva: A partir de R$38.000"]

def infantil ():
    print (menu_infantil)
    
def adulto ():
    print (menu_adulto)
    
if idade < (18):
    for item in menu_infantil:
        print(item)
else:
    for item in menu_adulto:
        print (item)

input("\nPressione Enter para sair...")    