class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz um som.")

class Mamifero(Animal):
    def __init__(self, nome, tipo_de_pelo):
        super().__init__(nome) # Chama o construtor da classe base Animal
        self.tipo_de_pelo = tipo_de_pelo

    def amamentar(self):
        print(f"{self.nome} está amamentando seus filhotes.")

class Cachorro(Mamifero):
    def __init__(self, nome, tipo_de_pelo, raca):
        super().__init__(nome, tipo_de_pelo) # Chama o construtor da classe Mamifero
        self.raca = raca

    def latir(self):
        print(f"{self.nome} está latindo!")

if __name__ == '__main__':
    cachorro = Cachorro("Maile", "Curto", "Viralata")
    cachorro.falar()
    cachorro.amamentar()
    cachorro.latir()
