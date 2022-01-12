def volume():
    raio = int(input('Informe o tamanho do raio em cm: '))
    vol = (4 / 3) * 3.14 * (raio ** 3)
    return f'O volume da esfera é {vol:.2f}cm³'


print(volume())
