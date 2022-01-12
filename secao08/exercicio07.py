temp_c = int(input('Informe a temperatura em ºC: '))


def temperatura():
    conv_f = temp_c * (9 / 5) + 32
    return f'A temperatura {temp_c}ºC é igual a {conv_f} F'


print(temperatura())
