from math import factorial


def somas(n):
    soma = 0
    for c in range(0, n + 1):
        soma += (1 / factorial(c))
    return f'O resultado do número neperiano é {soma}'


print(somas(int(input('Digite um número: '))))
