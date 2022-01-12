def numero(v):
    soma = 0
    while len(v) < 10:
        v.append(float(input('Digite um número: ')))
    print(f'Impressão normal {v}')
    print(f'Impressão inversa {v[::-1]}')
    for i in v:
        soma += i
    media = soma / 10
    return f'A média aritmética dos elementos do vetor é {media}'


v = []
print(numero(v))
