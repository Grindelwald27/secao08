def fatorial(n):
    multi = 1
    for i in range(n, 0, -1):
        multi *= i
    return f'O resultado de {n}! é {multi}'


print(fatorial(int(input('Informe um número: '))))
