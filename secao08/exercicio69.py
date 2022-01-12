def fracoes(a, b, c, d):
    p = a / b
    q = c / d
    for i in range(a + 1):
        if i % a == 0 and i % b == 0:
            simp_a = i / a
            simp_b = i / b
            print(f'A fração simplificada é {simp_a}/{simp_b}')
    for i in range(c + 1):
        if i % c == 0 and i % d == 0:
            simp_c = i / c
            simp_d = i / d
            print(f'A fração simplificada é {simp_c}/{simp_d}')


a = int(input('Informe A: '))
b = int(input('Informe B:'))
c = int(input('Informe C: '))
d = int(input('Informe D: '))
print(fracoes(a, b, c, d))
