def medias():
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    nota3 = float(input('Informe a terceira nota: '))
    print('Escolha uma opção')
    print('a - Média aritmética')
    print('p - Média ponderada')
    opcao = input('Opção: ')
    if opcao == 'a':
        media = (nota1 + nota2 + nota3) / 3
        return f'A média aritmética é {media}'
    elif opcao == 'p':
        media_p = (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
        return f'A média ponderada é {media_p}'


print(medias())
