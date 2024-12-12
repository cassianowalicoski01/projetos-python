class Cachorro:

    def __init__(self, nome, comida, ano_nascimento, sono):
        self._nome = nome
        self._comida = comida
        self._ano_nascimento = ano_nascimento
        self._sono = sono

    def imprimir_informacoes(self):
        print(f" Nome: {self._nome}\n Comida: {self._comida:.1f}\n Sono: {self._sono}\n Ano Nascimento: {self._ano_nascimento}")

    def comer(self):
        self.set_comida(self.get_comida() - 0.1)
        self.imprimir_informacoes()


    # Getters e Setters

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome

    def get_comida(self):
        return self._comida
    
    def set_comida(self, comida):
        self._comida = comida

    def get_ano_nascimento(self):
        return self._ano_nascimento
    
    def set_ano_nascimento(self, ano_nascimento):
        self._ano_nascimento = ano_nascimento

    def get_sono(self):
        return self._sono
    
    def set_nome(self, sono):
        self._sono = sono

    # Fim Getters e Setters
    
    
if __name__ == '__main__':
    cachorro_maile = Cachorro("Maile", 2.5, "2012", False)
    cachorro_maile.imprimir_informacoes()
    cachorro_maile.set_nome("Mingau")
    print(cachorro_maile.get_nome())
    cachorro_maile.comer()
    cachorro_maile.comer()
    cachorro_maile.comer()