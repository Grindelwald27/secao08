def troque(a, b):
    troca_a = b
    troca_b = a
    return f'O valor de A agora é {troca_a} e o valor de B é {troca_b}'


a = int(input('Digite um valor para A: '))
b = int(input('Digite um valor para B: '))
print(troque(a, b))
