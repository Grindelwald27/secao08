def concatenar(primeira, segunda, num):
    return primeira+segunda[:num]


str1 = input('Informe a 1ª palavra: ')
str2 = input('Informe a 2ª palavra: ')
n = int(input('Informe um valor para n: '))
print(concatenar(str1, str2, n))
