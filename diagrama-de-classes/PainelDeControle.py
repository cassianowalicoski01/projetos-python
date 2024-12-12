class PainelDeControle:
    def __init__(self, email, senha):
        self._email = email
        self._senha = senha
    
    def acessar_painel_de_controle(self):
        if self._email == "usuario@exemplo.com" and self._senha == "123456":
            return "Acesso concedido ao Painel de Controle!"
        else:
            return "Falha no acesso. Verifique o email e/ou a senha."                        