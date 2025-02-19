# Escreva uma função que receba uma lista de números e retorne a média deles.

def CalculaMediaLista (lista):
    media = sum(lista) / len(lista)

    return media

lista = [1, 2, 3, 4]

media = CalculaMediaLista(lista)
print(media)