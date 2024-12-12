from CarrinhoDeCompras import CarrinhoDeCompras
from PainelDeControle import PainelDeControle
from Cliente import Cliente
from Produto import Produto


class Menu:
    def __init__(self):
        self.produtos = {}
        self.clientes = {}
        self.painel = PainelDeControle("usuario@exemplo.com", "123456")
        self.carrinho = None
    
    def exibir_menu_principal(self):
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("( 1 ) Gerenciar Produtos")
            print("( 2 ) Gerenciar Clientes")
            print("( 3 ) Acessar Painel de Controle")
            print("( 4 ) Gerenciar Carrinho de Compras")
            print("( 0 ) Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.menu_produtos()
            elif opcao == "2":
                self.menu_clientes()
            elif opcao == "3":
                print(self.painel.acessar_painel_de_controle())
            elif opcao == "4":
                self.menu_carrinho()
            elif opcao == "0":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_produtos(self):
        while True:
            print("\n--- GERENCIAR PRODUTOS ---")
            print("( 1 ) Cadastrar Produto")
            print("( 2 ) Editar Produto")
            print("( 3 ) Remover Produto")
            print("( 4 ) Listar Produtos")
            print("( 0 ) Voltar ao Menu Principal")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                id = int(input("ID do produto: "))
                nome = input("Nome do produto: ")
                preco_venda = float(input("Preço de venda: "))
                preco_fornecedor = float(input("Preço do fornecedor: "))
                estoque = int(input("Quantidade em estoque: "))
                descricao = input("Descrição do produto: ")
                
                produto = Produto(id, nome, preco_venda, preco_fornecedor, estoque, descricao)
                self.produtos[id] = produto
                produto.cadastrar_produto()

            elif opcao == "2":
                id = input("ID do produto a ser editado: ")
                if id in self.produtos:
                    produto = self.produtos[id]
                    nome = input("Novo nome (deixe em branco para manter o atual): ")
                    preco_venda = input("Novo preço de venda (deixe em branco para manter o atual): ")
                    preco_fornecedor = input("Novo preço do fornecedor (deixe em branco para manter o atual): ")
                    estoque = input("Nova quantidade em estoque (deixe em branco para manter o atual): ")
                    descricao = input("Nova descrição (deixe em branco para manter o atual): ")
                    
                    produto.editar_produto(
                        nome=nome or None,
                        preco_venda=float(preco_venda) if preco_venda else None,
                        preco_fornecedor=float(preco_fornecedor) if preco_fornecedor else None,
                        estoque=int(estoque) if estoque else None,
                        descricao=descricao or None
                    )
                else:
                    print("Produto não encontrado.")

            elif opcao == "3":
                id = input("ID do produto a ser removido: ")
                if id in self.produtos:
                    self.produtos[id].remover_produto()
                    del self.produtos[id]
                else:
                    print("Produto não encontrado.")

            elif opcao == "4":
                if not self.produtos:
                    print("Nenhum produto cadastrado.")
                else:
                    for produto in self.produtos.values():
                        print(f"ID: {produto.id}, Nome: {produto.nome}, Preço: R${produto.preco_venda}, Estoque: {produto.estoque}")
            
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_clientes(self):
        while True:
            print("\n--- GERENCIAR CLIENTES ---")
            print("( 1 ) Cadastrar Cliente")
            print("( 2 ) Editar Cliente")
            print("( 3 ) Excluir Cliente")
            print("( 4 ) Listar Clientes")
            print("( 0 ) Voltar ao Menu Principal")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                id = input("ID do cliente: ")
                nome = input("Nome do cliente: ")
                cpf = input("CPF: ")
                endereco = input("Endereço: ")
                email = input("Email: ")
                senha = input("Senha: ")
                
                cliente = Cliente(id, nome, cpf, endereco, email, senha)
                self.clientes[id] = cliente
                print(f"Cliente '{nome}' cadastrado com sucesso.")
                
            elif opcao == "2":
                id = input("ID do cliente a ser editado: ")
                if id in self.clientes:
                    cliente = self.clientes[id]
                    nome = input("Novo nome (deixe em branco para manter o atual): ")
                    cpf = input("Novo CPF (deixe em branco para manter o atual): ")
                    endereco = input("Novo endereço (deixe em branco para manter o atual): ")
                    email = input("Novo email (deixe em branco para manter o atual): ")
                    senha = input("Nova senha (deixe em branco para manter o atual): ")
                    
                    cliente.editar_dados(
                        nome=nome or None,
                        cpf=cpf or None,
                        endereco=endereco or None,
                        email=email or None,
                        senha=senha or None
                    )
                else:
                    print("Cliente não encontrado.")
                
            elif opcao == "3":
                id = input("ID do cliente a ser excluído: ")
                if id in self.clientes:
                    self.clientes[id].excluir_conta()
                    del self.clientes[id]
                else:
                    print("Cliente não encontrado.")
                
            elif opcao == "4":
                if not self.clientes:
                    print("Nenhum cliente cadastrado.")
                else:
                    for cliente in self.clientes.values():
                        print(f"ID: {cliente.id}, Nome: {cliente.nome}, Email: {cliente.email}")
            
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_carrinho(self):
        if not self.carrinho:
            id_carrinho = input("ID do carrinho: ")
            id_pedido = input("ID do pedido: ")
            id_cliente = input("ID do cliente: ")
            self.carrinho = CarrinhoDeCompras(id_carrinho, id_pedido, id_cliente)
        
        while True:
            print("\n--- GERENCIAR CARRINHO ---")
            print("( 1 ) Calcular Frete")
            print("( 2 ) Exibir Lista de Compras")
            print("( 3 ) Inserir Cupom de Desconto")
            print("( 0 ) Voltar ao Menu Principal")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                distancia_km = float(input("Distância em km: "))
                self.carrinho.calcular_frete(distancia_km)
            elif opcao == "2":
                self.carrinho.exibe_lista_compras()
            elif opcao == "3":
                desconto = float(input("Porcentagem de desconto: "))
                self.carrinho.insere_cupom_desconto(desconto)
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    iniciar = Menu()
    iniciar.exibir_menu_principal()