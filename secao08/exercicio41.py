def maiores():
    vetor = []
    while len(vetor) < 10:
        vetor.append(int(input('Difite um número: ')))
    print(vetor)
    return f'O maior valor de vetor é {max(vetor)}'


print(maiores())
