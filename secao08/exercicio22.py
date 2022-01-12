def func(num):
    result = ''
    lista = [n * '!' for n in range(num + 1)]
    for i in lista:
        result += i + '\n'
    return result


print(func(int(input('Digite um número: '))))
