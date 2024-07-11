def verificaVoto(idade_voto):
    if idade_voto >= 18 and idade_voto <= 70:
        situacao = "é OBRIGATÓRIO"
    elif idade_voto >= 16 or idade_voto > 70:
        situacao = "é FACUTATIVO"
    else:
        situacao = "ainda NÃO É PERMITIDO"
    return f"Com {idade_voto} anos de idade o voto {situacao}!"


idade = int(input("Qual sua idade: "))

while idade < 0:
    idade = int(input("ATENÇÃO! Digite uma idade válida: "))

print(verificaVoto(idade))
