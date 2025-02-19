# Escreva uma função que receba uma tupla de inteiros e retorne uma nova tupla contendo apenas os números que são divisíveis por 3.

def divisiveis_por_tres(tupla):
    lista = []

    for numero in tupla:
        if numero % 3 == 0:
            lista.append(numero)

    divisiveis = tuple(lista)

    return divisiveis

tupla = (1, 3, 5, 6, 8, 9, 12)
print(divisiveis_por_tres(tupla))

# Solução Gemini:
def filtrar_divisiveis_por_tres(tupla):
    numeros_divisiveis = []

    for numero in tupla:
        if numero % 3 == 0:
            numeros_divisiveis.append(numero)

    return tuple(numeros_divisiveis)

print(filtrar_divisiveis_por_tres(tupla))