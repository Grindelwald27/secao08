from math import factorial


def somas(n):
    soma = 0
    mult = 0
    for i in range(1, n + 1):
        mult = factorial(n)
    num = str(mult)
    sep = list(''.join(num))
    print(sep)
    for indice, valor in enumerate(sep):
        soma += int(valor)
    return f'A soma dos algarismos é igual a {soma}'


print(somas(int(input('Digite um número: '))))
