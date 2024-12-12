posicao = int(input("Digite a posição que deseja retornar: "))

anterior = 0
atual = 1

print("1 | ", end="")

for _ in range(0, posicao - 1):
    atual = anterior + atual
    anterior = atual - anterior

    print(atual, "| ", end="")
    

print(f"\n\nA posição {posicao} corresponde ao número {atual} na sequência de Fibonacci.")
