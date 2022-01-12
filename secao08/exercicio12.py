def somas(numero):
    soma = 0
    if numero > 0:
        num = list(str(numero))
        for n in range(len(num)):
            soma += int(num[n])
        return f'A soma dos números é {soma}'
    return 'Número inválido'


numero = int(input('Informe um número: '))
print(somas(numero))
