def numero(x, a, b):
    while len(x) < 10:
        x.append(int(input('Digite um número: ')))
    for i in x:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    return f'Os valores pares de x são {a} \nOs valores ímpares de x são {b}'


x = []
a = []
b = []
print(numero(x, a, b))
