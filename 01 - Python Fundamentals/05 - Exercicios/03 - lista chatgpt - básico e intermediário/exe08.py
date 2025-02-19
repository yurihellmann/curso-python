# Crie um programa que receba uma lista de números e remova os números duplicados.

def RemoveDuplicados (lista):
    lista_ajustada = list(dict.fromkeys(lista))

    return lista_ajustada

numeros = input("Digite uma lista de números separados por espaço: ")

lista_numeros = list(map(int, numeros.split()))

lista_ajustada = RemoveDuplicados(lista_numeros)

print(f'A lista ajustada é {lista_ajustada}')
