# Escreva uma função que receba um dicionário cujos valores são números e retorne o dicionário ordenado pelos valores, de forma decrescente.

def ordernar_dicionario(dicionario):
    lista_ordenada = sorted(dicionario.items(), key=lambda item: item[1])
    dicionario_ordenado = dict(lista_ordenada)

    return dicionario_ordenado

dicionario = {
    "c": 3,
    "d": 4,
    "a": 1,
    "b": 2,
    "e": 5
}

print(ordernar_dicionario(dicionario))