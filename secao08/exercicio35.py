from math import factorial


def fator(n):
    while n < 0:
        n = int(input('Digite um valor positivo: '))
    fatorial = factorial(2 * n) / factorial(n)
    return f'O fatorial quádruplo de {n} é {fatorial}'


print(fator(int(input('Digite um valor positivo: '))))
