# Escreva uma função que receba uma lista de números inteiros e 
# retorne uma nova lista contendo a diferença absoluta entre cada elemento e o número médio da lista.

def diferenca_absoluta_media(lista):
    media = sum(lista) / len(lista)
    diferencas = [abs(numero - media) for numero in lista]

    return diferencas, media

numeros = [2, 4, 6, 8, 10]
print(diferenca_absoluta_media(numeros))
