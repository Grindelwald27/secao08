def exponencial(x, z):
    conta = x ** z
    return f'{x} elevado a {z} é igual a {conta}'


xis = int(input('Informe X: '))
ze = int(input('Informe Z: '))
print(exponencial(xis, ze))
