def hipotenusa():
    a = int(input('Informe o valor de a: '))
    b = int(input('Informe o valor de b: '))
    hip = (a ** 2 + b ** 2) ** 0.5
    return f'A hipotenusa do triângulo é {hip:.2f}'


print(hipotenusa())
