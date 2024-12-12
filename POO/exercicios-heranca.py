class Veiculo:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def visualizar_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")

class Combustivel:
    def usa_combustivel(self):
        print("Este veículo utiliza combustível!")

class Caminhao(Veiculo, Combustivel):
    def __init__(self, marca, modelo, cor, num_eixos):
        super().__init__(marca, modelo, cor)
        self.num_eixos = num_eixos

    def carregar(self, tipo_carga):
        print(f"O veículo da marca {self.marca}, modelo {self.modelo} está carregado com uma carga de {tipo_carga}. Ele possuí um total de {self.num_eixos} eixos.")

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, cor, num_aro):
        super().__init__(marca, modelo, cor)
        self.num_aro = num_aro

    def vender(self):
        print(f"Vende-se bicicleta {self.marca}, modelo {self.modelo}, aro {self.num_aro} com cor {self.cor}")

if __name__ == '__main__':
    scania = Caminhao("Scania", "113", "Azul", 9)
    scania.visualizar_detalhes()
    scania.carregar("Soja")
    scania.usa_combustivel()
    viking = Bicicleta("Viking", "Tuf 6", "Preto/Amarelo", 26)
    viking.visualizar_detalhes()
    viking.vender()
