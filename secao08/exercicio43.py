from random import randint


def numeros():
    vetor = []
    while len(vetor) < 10:
        vetor.append(randint(1, 100))
    return f'Os números selecionados são {vetor}'


print(numeros())
