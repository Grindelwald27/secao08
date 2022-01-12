def intercalar(primeira, segunda):
    vet1 = list(primeira)
    vet2 = list(segunda)
    while len(vet1) != len(vet2):
        if len(vet1) < len(vet2):
            segunda = input('Informe outra palavra: ')
        elif len(vet1) > len(vet2):
            primeira = input('Informe outra palavra: ')
    for c in range(len(vet1)):
        vet1.insert(c, vet2[c])
    return vet1


str1 = input('Digite a 1ª palavra: ')
str2 = input('Digite a 2ª palavra: ')
print(intercalar(str1, str2))
