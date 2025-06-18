idade = int (input("Insira sua idade: \n"))

def infantil ():
    print ("""\n
           -Hot Wheels (a coleção toda!)\n
           -Filmes Carros (Relâmpago Marquinhos Acelera!)\n""")
    
def adulto ():
    print ("""\n
           -Fusca 70: A partir de R$15.000\n
           -Alpha Romeo: A partir de R$20.000\n
           -Meriva: A partir de R$38.000\n
           """)
    
if idade < (18):
    infantil()
else:
    adulto()

input("\nPressione Enter para sair...")    