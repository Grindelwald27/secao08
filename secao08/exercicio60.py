palavra = 'Eu sou demais'


def retornar():
    letra = input('Informe a letra: ')
    if letra == 'E':
        return palavra[0]
    else:
        return '-1'


print(retornar())
