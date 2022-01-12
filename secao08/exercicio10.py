def maior():
    num1 = int(input('Informe o primeiro número número: '))
    num2 = int(input('Informe o segundo número: '))
    if num1 > num2:
        return f'O número {num1} é maior que o número{num2}'
    return f'O número {num2} é maior que o número {num1}'


print(maior())
