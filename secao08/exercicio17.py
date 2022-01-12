def soma_todos_numeros(num1, num2):
    soma = 0
    for n in range(num1 + 1, num2):
        soma += n
    return f'A soma dos números é {soma}'


numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
print(soma_todos_numeros(numero1, numero2))
