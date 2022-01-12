import numpy as np
n = int(input('Digite um número: '))


def transposta():
    matriz = np.zeros([n, n], int)
    for l in range(n):
        for c in range(n):
            matriz[l][c] = int(input(f'Informe o número [{l + 1}, {c + 1}]: '))
    print(matriz)
    print()
    print('Transposta:')
    return matriz.T


print(transposta())
