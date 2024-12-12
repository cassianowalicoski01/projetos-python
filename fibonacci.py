# PRIMEIRO EXEMPLO
def fibo1(valor):
    anterior = 0
    atual =  1

    for i in range(0, valor):
        print(atual, end=" ")
        auxiliar = atual
        atual = anterior + atual
        anterior = auxiliar

# SEGUNDO EXEMPLO
def fibo2(valor):
    anterior = 0
    atual = 1
    contador = 1

    while contador <= valor:
        print(atual, end=" ")
        atual, anterior = anterior + atual, atual
        contador += 1

# TERCEIRO EXEMPLO COM RECURSIVIDADE
def fiboRecursivo(valor):
    if valor <= 2:
        return 1
    else:
        return fiboRecursivo(valor - 1) + fiboRecursivo(valor - 2)

if __name__ == "__main__":
    fibo1(8)
    print()
    fibo1(8)
    print()
    print(fiboRecursivo(8))