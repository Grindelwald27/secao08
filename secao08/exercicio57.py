import numpy as np
matriz = np.zeros([7, 6], int)
n = int(input('Digite o número da coluna que deseja fazer a soma: '))


def soma_alg(mt, num):
    soma = 0
    for l in range(7):
        for c in range(6):
            mt[l][c] = int(input(f'Digite o número [{l + 1}, {c + 1}]: '))

            if c == num - 1:
                soma += mt[l][c]
    print(mt)
    return f'A soma dos elementos da coluna {num} é igual a {soma}'


print(soma_alg(matriz, n))
