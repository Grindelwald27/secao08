import numpy as np
n = int(input('Digite um número: '))
matriz_a = np.zeros([n, n], int)
matriz_b = np.zeros([n, n], int)
matriz_c = np.zeros([n, n], int)


def produto(a, b, c, num):
    for l in range(num):
        for c in range(num):
            a[l][c] = int(input(f'Matriz A - número [{l + 1}, {c + 1}]: '))

    for l in range(num):
        for c in range(num):
            b[l][c] = int(input(f'Matriz B - número [{l + 1}, {c + 1}]: '))

    for l in range(num):
        for c in range(num):
            matriz_c[l][c] = a[l][c] * b[l][c]
    print('Matriz A:')
    print(a)
    print()
    print('Matriz B:')
    print(b)
    print()
    print('Matriz C:')
    return matriz_c


print(produto(matriz_a, matriz_b, matriz_c, n))
