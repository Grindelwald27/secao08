import numpy as np


def matrizes():
    matriz = np.zeros([4, 4], int)
    maior_10 = []
    for l in range(4):
        for c in range(4):
            matriz[l][c] = int(input(f'Número [{l + 1}, {c + 1}]: '))

            if matriz[l][c] > 10:
                maior_10.append(matriz[l][c])
    print('Matriz:')
    print()
    print(matriz)
    return f'A quantidade de números maiores que 10 na matriz é {len(maior_10)}'


print(matrizes())
