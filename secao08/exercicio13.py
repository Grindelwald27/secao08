def op():
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
    print('Escolha uma das operações abaixo: ')
    print('+ -> adição')
    print('- -> subtração')
    print('* -> multiplicação')
    print('/ -> divisão')
    opcao = input('Opção: ')
    if opcao == '+':
        soma = num1 + num2
        return f'A soma de {num1} + {num2} é igual a {soma}'
    elif opcao == '-':
        sub = num1 - num2
        return f'A subtração de {num1} - {num2} é igual a {sub}'
    elif opcao == '*':
        multi = num1 * num2
        return f'A multiplicação de {num1} X {num2} é igual a {multi}'
    elif opcao == '/':
        div = num1 / num2
        return f'A divisão de {num1} / {num2} é igual a {div}'


print(op())
