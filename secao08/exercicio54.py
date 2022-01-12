import numpy as np


def soma_alg():
    matriz = np.zeros([4, 4], int)
    soma = 0

    for l in range(4):
        for c in range(4):
            matriz[l][c] = int(input(f'Digite o número [{l + 1}, {c + 1}]: '))

            soma += matriz[l][c]
    print(matriz)
    return f'A soma dos elementos da matriz é {soma}'


print(soma_alg())
