class cachorro:
    def __init__(self, raca, cor, nome, sexo, peso, altura, data_nascimento, gramas_comida):
        self.raca = raca
        self.cor = cor
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.data_nascimento = data_nascimento
        self.comida = 1000
        self.gramas_comida = gramas_comida

    
    def comer(self):
        self.comida -= self.gramas_comida
        print(f"O cachorro {self.nome} ainda possui {self.comida} gramas de comida!")

    def latir(self):
        print(f"O cachorro {self.nome} está latindo!")

    def dadosCachorro(self):
        dados = {"nome": self.nome, "raça": self.raca, "cor": self.cor, "sexo": self.sexo, "peso": self.peso, "altura": self.altura, "data_nascimento": self.data_nascimento}
        
        print(f"CACHORRO {self.nome.upper()}")
        for chave, valor in dados.items():
            print(f"{chave.capitalize().replace("_", " ")}: {valor}")
        print()


if __name__ == '__main__':
    meu_primeiro_cachorro = cachorro("Viralata", "Marrom", "Maile", "Macho", 3.4, 25, "15-04-2012", 20)
    meu_primeiro_cachorro.dadosCachorro()

    segundo_cachorro = cachorro("Dalmata", "Branco e Preto", "Tobi", "Macho", 5, 30, "12/12/2008", 30)
    segundo_cachorro.dadosCachorro()

