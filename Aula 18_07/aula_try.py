while True:
    try:
        n1 = int(input("Insira um número: \n"))
        n2 = int(input("Insira outro número: \n"))
        break
    except ValueError:
        print("Insira um número válido !\n")
