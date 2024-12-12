class Produto:
    def __init__(self, id, nome, preco_venda, preco_fornecedor, estoque, descricao):
        self.id = id
        self.nome = nome
        self.preco_venda = preco_venda
        self.preco_fornecedor = preco_fornecedor
        self.estoque = estoque
        self.descricao = descricao

    def cadastrar_produto(self):
        print(f"Produto '{self.nome}' cadastrado com sucesso.")
        print(f"ID: {self.id}, Preço de Venda: R${self.preco_venda}, Preço Fornecedor: R${self.preco_fornecedor}, Estoque: {self.estoque}, Descrição: {self.descricao}")

    def editar_produto(self, nome=None, preco_venda=None, preco_fornecedor=None, estoque=None, descricao=None):
        if nome:
            self.nome = nome
        if preco_venda:
            self.preco_venda = preco_venda
        if preco_fornecedor:
            self.preco_fornecedor = preco_fornecedor
        if estoque:
            self.estoque = estoque
        if descricao:
            self.descricao = descricao
        print(f"Produto {self.nome} atualizado com sucesso.")

    def remover_produto(self):
        confirmacao = input(f"Tem certeza que deseja remover o produto '{self.nome}'? (s/n): ")
        if confirmacao.lower() == 's':
            print(f"Produto '{self.nome}' removido com sucesso.")
        else:
            print("Remoção de produto cancelada.")