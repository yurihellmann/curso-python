# Faça um programa que receba uma lista de nomes e crie um dicionário onde a chave seja o nome e o valor seja a quantidade de letras desse nome.

def CriaDicionario (nomes):
    dicionario = {}

    for nome in nomes:
        dicionario[nome] = len(nome)

    return dicionario

nomes = input("Digite uma lista de nomes separados por espaço: ").split(' ')

print(CriaDicionario(nomes))
