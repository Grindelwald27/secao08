lado1 = int(input('Informe o comprimento do lado 1: '))
lado2 = int(input('Informe o comprimento do lado 2: '))
lado3 = int(input('Informe o comprimento do lado 3: '))


def se_tri():
    if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
        return f'Os lados {lado1}, {lado2}, {lado3} formam um triângulo'
    return 'Não é um triângulo'


def tipo_tri():
    if lado1 == lado3 == lado2:
        return 'O triângulo é equilátero'
    elif lado1 != lado2 == lado3 or lado2 != lado1 == lado3 or lado3 != lado1 == lado2:
        return 'O triângulo é isósceles'
    elif lado1 != lado2 != lado3:
        return 'O triângulo é escaleno'


print(se_tri())
print(tipo_tri())
