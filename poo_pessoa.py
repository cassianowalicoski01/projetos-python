class Pessoa:
    def __init__(self, nome, sexo, cpf, ano_nascimento, salario_bruto):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ano_nasc = ano_nascimento
        self.idade = self.calculaIdade()
        self.salario_bruto = salario_bruto
        self.salario_liquido = self.descontaIrrfInss()

    def calculaIdade(self):
        return 2024 - self.ano_nasc
    
    def calculaIrrf(self):
        salario = self.salario_bruto
        if salario < 2112:
            irrf = 0
            faixa = 0
        elif salario < 2826:
            irrf = 7.5
            faixa = 158.40
        elif salario < 3751:
            irrf = 15
            faixa = 370.40
        elif salario < 4664:
            irrf = 22.5
            faixa = 651.73
        elif salario > 4664:
            irrf = 27.5
            faixa = 884.96
        return irrf
    
    
    def calculaInss(self):
        salario = self.salario_bruto
        if salario < 1412:
            inss = 7.5
        elif salario < 2666:
            inss = 16.5 #9
        elif salario < 4000:
            inss = 28.5 #12
        elif salario < 7786:
            inss = 42.5 #14
        elif salario > 7786:
            inss = 0
        return inss
        
        
    def descontaIrrfInss(self):
        desconto_irrf = ((self.salario_bruto * (self.irrf / 100)) * (self.irrf / 100)) - self.faixa
        desconto_inss = (self.salario_bruto * (self.inss / 100)) * (self.inss / 100)
        descontos = desconto_irrf + desconto_inss
        salario_a_receber = self.salario_bruto - descontos
        return salario_a_receber
        

    def mostrarDados(self):
        dados = {"nome": self.nome, "sexo": self.sexo, "ano_nascimento": self.ano_nasc, "idade": self.idade, "salario_bruto": self.salario_bruto, "salario_liquido": self.salario_liquido}
        for c, v in dados.items():
            print(f"{c.capitalize().replace("_", " ")}: {v}")

if __name__ == '__main__':
    uma_pessoa = Pessoa("Cassiano", "Masculino", "012.225.536-15", 2004, 3000)
    uma_pessoa.mostrarDados()