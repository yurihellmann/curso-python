# Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números que aparecem mais de uma vez.

def filtra_numeros(lista):
    numeros_filtrados = []

    for numero in lista:
        if numero not in numeros_filtrados:
            numeros_filtrados.append(numero)

    return numeros_filtrados

lista = [1, 2, 3, 5, 5, 1, 6]
print(filtra_numeros(lista))