nome_aluno = str(input("Digite seu nome: ")).capitalize()
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media_aluno = (n1 + n2 + n3 + n4) / 4
print(f"A média do aluno {nome_aluno} foi de {media_aluno}")

if media_aluno >= 7:
    print(f"O aluno {nome_aluno} está APROVADO!")
elif media_aluno > 4:
    print(f"O aluno {nome_aluno} está em RECUPERAÇÃO!")
else:
    print(f"O aluno {nome_aluno} está REPROVADO!")
