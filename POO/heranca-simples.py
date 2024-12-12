class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} faz um som.")

class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} late.")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} mia.")

if __name__ == '__main__':
    cachorro = Cachorro("Maile")
    gato = Gato("Gatão")
    cachorro.fazer_som()
    gato.fazer_som()