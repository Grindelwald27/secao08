def serie(n):
    soma = 0
    for c in range(1, n + 1):
        soma += (((c ** 2) + 1) / (c + 3))
    return f'O resultado da série é {soma}'


print(serie(int(input('Digite um número: '))))
