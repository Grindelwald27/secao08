import numpy as np
matriz = np.zeros([5, 4], str)


def matrix():
    for l in range(5):
        for c in range(4):
            matriz[l][3] = int
            matriz[l][c] = input('Informação: ')
    return matriz


print(matrix())


def medias():
    soma_idade = 0
    cont = 0
    for l in range(0, 5):
        if matriz[l][1] == 'C' and matriz[l][2] == 'P':
            soma_idade += int(matriz[l][3])
            cont += 1
    media = soma_idade / cont
    return f'A média das idades das pessoas de cabelo preto e olhos castanhos é {media}'


print()
print(medias())


def maior_idade():
    maior = 0
    for l in range(5):
        if matriz[l][3] > maior:
            maior = maior[l][3]
    return f'A maior idade é {maior}'


print()
print(maior_idade())


def complicada():
    cont = 0
    for l in range(5):
        if matriz[l][0] == 'f' and 18 < matriz[l][3] <= 35 and matriz[l][1] == 'A' and matriz[l][2] == 'L':
            cont += 1
    return f'Existem {cont} mulheres com cabelos loiros, olhos azuis e idade entre 18 e 35 anos'


print()
print(complicada())
