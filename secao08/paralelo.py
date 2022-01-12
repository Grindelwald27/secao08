def intercala(str1, str2):
    vet1 = list(str1)
    vet2 = list(str2)
    t = len(vet1)
    x = 0
    y = 1
    for i in range(t):
        if x < len(vet2) and y < len(vet1):
            vet1.insert(y, vet2[x].upper())
            x += 1
            y += 2
    return vet1


str1 = input('Digite a primeira palavra: ')
str2 = input('Digite a segunda palavra: ')

print('Palavras intercaladas: ', intercala(str1, str2))
