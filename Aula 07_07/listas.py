lista_de_compras = ["tomate","cebola"]
item = input("Anote: \n")
lista_de_compras.append(item)
lista_de_compras.pop(0)
for item in lista_de_compras:
    print(item)