nome_aluno = str(input("Digite seu nome: ")).capitalize()
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media_aluno = (n1 + n2 + n3 + n4) / 4
print(f"A média do aluno {nome_aluno} foi de {media_aluno}")

# -----------------------------------------------------------------
# MELHORADO

nome = str(input("Digite seu nome: ")).capitalize()

notas = []

for i in range(0, 4):
    nota_aluno = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota_aluno)

media = sum(notas) / len(notas)

print(f"A média do aluno {nome} foi de {media}")


# ------------------------------------------------------------------
# OUTRA FORMA -> UTILIZANDO O FOR VALOR IN VALORES:

contador = 0
soma = 0
aluno = str(input("Digite seu nome: ")).capitalize()
notas_aluno = []
for c in range(0, 4):
    n = float(input(f"Digite o valor da {c+1} nota: "))
    notas_aluno.append(n)

for nota in notas_aluno:
    soma += nota
    contador += 1

media_a = soma / contador

print(f"A média do aluno {aluno} foi de {media_a}")
