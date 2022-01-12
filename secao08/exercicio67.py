vetor = []


def caracteres(vetorex, tamanho):
    while len(vetorex) < tamanho:
        palavra = input('Informe uma palavra: ')
        if palavra != 'enter':
            vetor.append(palavra)
        else:
            break
    return vetorex


tam = int(input('Informe o tamanho do vetor: '))
print(caracteres(vetor, tam))
