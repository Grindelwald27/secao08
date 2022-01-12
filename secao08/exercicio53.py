import numpy as np
n = int(input('Informe um número: '))


def verifica_ident():
    matriz = np.zeros([n, n], int)
    cont = 0
    for l in range(n):
        for c in range(n):
            matriz[l][c] = int(input(f'Digite o número [{l + 1}, {c + 1}]: '))

    for l in range(n):
        for c in range(n):
            if l == c:
                if matriz[l][c] == 1:
                    cont += 1
            elif l != c:
                if matriz[l][c] == 0:
                    cont += 1
    print(matriz)
    print()
    if cont == 2 * n:
        return 'A matriz é identidade'
    else:
        return 'A matriz não é identidade'


print(verifica_ident())
