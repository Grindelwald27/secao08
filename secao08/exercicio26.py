def somatorio(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return f'O resultado da soma é {soma}'


print(somatorio(int(input('Digite o número: '))))
