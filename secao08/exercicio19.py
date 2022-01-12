def maior_primo(n):
    if n == 1:
        return 1
    fp = 2
    while n != 1:
        if n % fp == 0:
            n = n / fp
        else:
            fp += 1
    return fp


valor = int(input('Informe um número positivo: '))
print(f'O maior fator primo de {valor} é {maior_primo(valor)}')
