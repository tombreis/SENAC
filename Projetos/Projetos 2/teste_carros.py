def infantil():
    print ("""\n
           -Hot Wheels (a coleção toda!)
           -Filmes Carros (Relâmpago Marquinhos Acelera!)
           """)

    print("""
       .-.
     __|=|__
    (_/`-`\\_)
    //\\___/\\\\
    <>/   \<>
     \|_._|/
      <_I_>
       |||
      /_|_\\
    """)  # Balão de festa 🎈

def adulto():
    print ("""\n
           -Fusca 70: A partir de R$15.000
           -Alpha Romeo: A partir de R$20.000
           -Meriva: A partir de R$38.000
           """)

    print("""
      ______
   .-'      '-.
  /            \\
 |              |
 |,  .-.  .-.  ,|
 | )(_o/  \\o_)( |
 |/     /\\     \\|
 (_     ^^     _)
  \\__|IIIIII|__/
   | \\IIIIII/ |
   \\          /
    `--------`
     _|____|_
  __|_|__|_|__
 (__)      (__)
    """)  # Caveira 💀

while True:
    entrada = input("Insira sua idade (ou digite 'sair' para encerrar): \n")
    
    if entrada.lower() == 'sair':
        print("Encerrando o programa. Até logo!")
        break

    if not entrada.isdigit():
        print("Por favor, insira um número válido.")
        continue

    idade = int(entrada)

    if idade < 18:
        infantil()
    else:
        adulto()

    print("\n")  # Espaço entre execuções
