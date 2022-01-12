def volume():
    altura = int(input('Informe a altura do cilindro: '))
    raio = int(input('Informe o raio do cilindro: '))
    vol = 3.141592 * (raio ** 2) * altura
    return f'O volume do cilindro é {vol}'


print(volume())
