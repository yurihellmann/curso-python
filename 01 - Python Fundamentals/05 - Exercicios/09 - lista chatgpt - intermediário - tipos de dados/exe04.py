# Escreva uma função que receba uma lista de números inteiros e retorne uma lista onde todos os números negativos foram removidos.

def remove_negativos(lista):
    lista_filtrada = []

    for numero in lista:
        if numero >= 0:
            lista_filtrada.append(numero)

    return lista_filtrada

lista = [-3, -2, -1, 0, 1, 2, 3]

print(remove_negativos(lista))