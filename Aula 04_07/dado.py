import random


def lancar_dados (faces):
    resultado = random.randint(1,faces)
    return resultado



while True:
    faces = int(input("Quantos lados ? \n"))
    resultado = lancar_dados(faces)
    print (resultado)