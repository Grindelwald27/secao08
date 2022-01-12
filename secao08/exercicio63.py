def iguais(nome, senha):
    if nome == senha:
        return 'Nome e senha são iguais'
    return 'Nome e senha são diferentes'


nome = input('Informe seu nome: ')
senha = input('Informe sua senha: ')
print(iguais(nome, senha))
