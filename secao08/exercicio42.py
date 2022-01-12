def reais():
    vetor = []
    media = 0
    soma = 0
    while len(vetor) < 10:
        vetor.append(float(input('Digite um número: ')))
    for i in vetor:
        soma += i
    media = soma / 10
    return f'A média dos números de vetor ({vetor}) é {media}'


print(reais())
