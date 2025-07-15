class Personagem:
    def __init__(self, nome, classe, elemento):
        self.nome = nome
        self.classe = classe
        self.elemento = elemento

    def get_info(self):
        return f"Nome: {self.nome}\nClasse: {self.classe}\nElemento: {self.elemento}"

    def atacar ():
        print("Ataque")

personagem1 = Personagem("Mateo", "Guerreiro", "Luz")
