def pares():
    vetor = []
    par = []
    while len(vetor) < 10:
        vetor.append(int(input('Digite um número: ')))
    for i in vetor:
        if i % 2 == 0:
            par.append(i)
    print(par)
    return f'A quantidade de valores pares em vetor é igual a {len(par)}'


print(pares())
