vetor_a = []
vetor_b = []


def vetores(a, b):
    while len(vetor_a) < 10:
        vetor_a.append(int(input('Digite um número para A: ')))
    while len(vetor_b) < 10:
        vetor_b.append(int(input('Digite um número para B: ')))
    a = set(vetor_a)
    b = set(vetor_b)
    vetor_c = a.union(b)
    print(a)
    print(b)
    return f'A união do vetor A com o vetor B é {vetor_c}'


print(vetores(vetor_a, vetor_b))
