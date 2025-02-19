# Escreva uma função que receba uma lista de números e retorne um conjunto contendo os números que são múltiplos de 5.

def multiplos_de_cinco(lista):
    conjunto_multiplos_de_cinco = set()

    for numero in lista:
        if numero % 5 == 0:
            conjunto_multiplos_de_cinco.add(numero)

    return conjunto_multiplos_de_cinco

lista = [1, 3, 5, 6, 9, 10, 12, 15, 20, 23, 30, 35]

print(multiplos_de_cinco(lista))
