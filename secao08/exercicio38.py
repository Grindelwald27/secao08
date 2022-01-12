from math import factorial


def fator(n):
    fe = 1
    while n < 0:
        n = int(input('Digite um valor positivo: '))
    for c in range(2, n + 1):
        fe = n ** factorial(c - 1)
    return f'O resultado do fatorial exponencial de {n} é igual a {fe}'


print(fator(int(input('Digite um valor positivo: '))))
