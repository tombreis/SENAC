nota1 = int(input("Insira a Nota 1: \n" ))
nota2 = int(input("Insira a Nota 2: \n" ))
nota3 = int(input("Insira a Nota 3: \n" ))
nota4 = int(input("Insira a Nota 4: \n" ))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 6:
    print (f"Média do aluno: {media}")
    print ("ALUNO REPORVADO")
else:
    print (f"Média do aluno: {media}")
    print ("ALUNO APROVADO")
