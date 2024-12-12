class CarrinhoDeCompras:
    def __init__(self, id_carrinho, id_pedido, id_cliente):
        self.id_carrinho = id_carrinho
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.num_total_produtos = 0
        self.valor_total_produtos = 0.0
        self.lista_de_produtos = []

    def calcular_frete(self, distancia_km):
        frete = distancia_km * 1.50  # Exemplo: R$1,50 por km
        print(f"Frete calculado: R${frete:.2f}")
        return frete

    def exibe_lista_compras(self):
        if not self.lista_de_produtos:
            print("O carrinho está vazio.")
            return
        print(f"Carrinho de compras (ID: {self.id_carrinho}):")
        for produto in self.lista_de_produtos:
            print(f"- {produto['nome']}: R${produto['preco_venda']} (Quantidade: {produto['quantidade']})")
        print(f"Total de produtos: {self.num_total_produtos}")
        print(f"Valor total dos produtos: R${self.valor_total_produtos:.2f}")

    def insere_cupom_desconto(self, porcentagem_desconto):
        desconto = (self.valor_total_produtos * porcentagem_desconto) / 100
        valor_com_desconto = self.valor_total_produtos - desconto
        print(f"Desconto de {porcentagem_desconto}% aplicado. Valor com desconto: R${valor_com_desconto:.2f}")
        return valor_com_desconto