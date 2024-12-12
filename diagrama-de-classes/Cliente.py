class Cliente:
    def __init__(self, id, nome, cpf, endereco, email, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        self.senha = senha

    def acessar_conta(self):
        if self.email == 1 and self.senha == 1:
            print(f"{self.nome} acessou a conta.")
        else:
            print("E-mail e/ou senha incorretos.")

    def editar_dados(self, nome=None, cpf=None, endereco=None, email=None, senha=None):
        if nome:
            self.nome = nome
        if cpf:
            self.cpf = cpf
        if endereco:
            self.endereco = endereco
        if email:
            self.email = email
        if senha:
            self.senha = senha
        print(f"Dados do cliente {self.nome} foram atualizados.")

    def excluir_conta(self):
        confirmacao = input(f"Tem certeza que deseja excluir a conta de {self.nome}? (s/n): ")
        if confirmacao.lower() == 's':
            print(f"Conta de {self.nome} foi excluída!")
        else:
            print("Exclusão de conta cancelada!")