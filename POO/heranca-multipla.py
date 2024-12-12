class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz um som.")

class Voar:
    def pode_voar(self):
        print("Este animal pode voar.")

class Botar:
    def botar_ovo(self):
        print(f"Pode botar ovos.")

class Pato(Animal, Voar, Botar):
    def __init__(self, nome):
        Animal.__init__(self, nome)

    def nadar(self):
        print(f"{self.nome} está nadando!")

class Galinha(Animal, Botar):
    def __init__(self, nome):
        Animal.__init__(self, nome)

    def comer_milho(self):
        print(f"{self.nome} come milho.")

class Ornitorinco(Animal, Botar, Voar):

    def roer_madeira(self):
        print("Roe madeira!")

if __name__ == '__main__':
    pato = Pato("Patozo")
    pato.falar()
    pato.pode_voar()
    pato.nadar()
    pato.botar_ovo()
    galinha = Galinha("Dhuni")
    galinha.botar_ovo()
    galinha.comer_milho()
    ornitorinco = Ornitorinco("Ornito")
    ornitorinco.botar_ovo()
    ornitorinco.falar()
    ornitorinco.roer_madeira()
