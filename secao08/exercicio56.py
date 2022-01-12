import numpy as np
matriz = np.zeros([7, 6], int)
n = int(input('Informe uma linha (de 1 a 7) que deseja fazer a soma: '))


def soma_linha(mt, num):
    soma = 0
    for l in range(7):
        for c in range(6):
            mt[l][c] = int(input(f'Digite o número [{l + 1}, {c + 1}]: '))

            if l == num - 1:
                soma += matriz[l][c]
    print(matriz)
    return f'A soma dos elementos da linha {num} é {soma}'


print(soma_linha(matriz, n))
