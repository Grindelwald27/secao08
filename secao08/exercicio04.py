numero = int(input('Informe um número: '))


def quad_perf(num):
    if num == 0:
        return f'O número {numero} é um quadrado perfeito'
    elif num < 0:
        return 'Valor inválido'
    v = num / (num ** 0.5)
    if num % v == 0:
        return f'O número {numero} é um quadrado perfeito'
    return f'O número {numero} não é um quadrado perfeito'


print(quad_perf(numero))
