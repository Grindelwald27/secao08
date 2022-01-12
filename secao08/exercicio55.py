import numpy as np


def soma_alg():
    matriz = np.zeros([3, 3], int)
    soma = 0

    for l in range(3):
        for c in range(3):
            matriz[l][c] = int(input(f'Digite o número [{l + 1}, {c + 1}]: '))

            if l == c:
                soma += matriz[l][c]

    soma += matriz[0][2] + matriz[1][1] + matriz[2][0]
    print(matriz)
    return f'A soma dos algarismos das diagonais primária e secundária é {soma}'


print(soma_alg())
