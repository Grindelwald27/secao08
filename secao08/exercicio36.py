from math import factorial


def fator(n):
    sf = 1
    while n < 0:
        n = int(input('Digite um valor positivo: '))
    for c in range(1, n + 1):
        sf *= factorial(c)
    return f'O superfatorial de {n} é {sf}'


print(fator(int(input('Digite um valor positivo: '))))
