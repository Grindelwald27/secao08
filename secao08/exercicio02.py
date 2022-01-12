def data(dia, mes, ano):
    if mes == 1:
        mes = 'Janeiro'
    elif mes == 2:
        mes = 'Fevereiro'
    elif mes == 3:
        mes = 'março'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'maio'
    elif mes == 6:
        mes = 'junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'setembro'
    elif mes == 10:
        mes = 'outubro'
    elif mes == 11:
        mes = 'novembro'
    elif mes == 12:
        mes = 'dezembro'
    return f'Hoje é dia {dia} de {mes} de {ano}'


datinha = input('Informe a data dd/mm/aaaa: ')
separador = datinha.split('/')

print(data(int(separador[0]), int(separador[1]), int(separador[2])))
