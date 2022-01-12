str1 = input('Informe a primeira palavra: ')
str2 = input('Informe a segunda palavra: ')


def concatenar(primeira, segunda):
    concat = primeira + segunda
    return f'A frase resultante é {concat}'


print(concatenar(str1, str2))
