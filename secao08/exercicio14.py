def consumo(distancia, qnt_litros):
    cons = distancia / qnt_litros
    if cons < 8:
        return 'Venda o carro!'
    elif 8 < cons < 14:
        return 'Econômico!'
    elif cons > 12:
        return 'Super econômico!'


dist = int(input('Quanto o carro percorreu: '))
gasto = int(input('Quanto o carro gastou de gasolina: '))
print(consumo(dist, gasto))
