h_atual = input('Informe a hora atual hh:mm:ss: ')
sep = h_atual.split(':')


def horas(hora, minuto, seg):
    hora_p_seg = hora * 3600
    min_p_seg = minuto * 60
    soma = hora_p_seg + min_p_seg + seg
    return f'{h_atual} convertido para segundos fica {soma} segundos'


print(horas(int(sep[0]), int(sep[1]), int(sep[2])))
