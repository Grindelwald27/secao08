def fator(n):
    conta = 1
    while n % 2 == 0:
        n = int(input('Digite um número ímpar: '))
    for i in range(1, n + 1, 2):
        conta *= i
    return f'O fatorial duplo de {n} é {conta}'


print(fator(int(input('Digite um número ímpar: '))))
