# Escreva uma função que receba uma lista de elementos e 
# retorne um conjunto contendo apenas os elementos únicos que aparecem mais de uma vez na lista.

def elementos_duplicados(lista):
    conjunto = set()
    contagem = {}

    for item in lista:
        contagem[item] = contagem.get(item, 0) + 1

    for elemento, quantidade in contagem.items():
        if quantidade > 1:
            conjunto.add(elemento)

    return contagem, conjunto

lista = [1, 2, 3, 5, 6, 3, 5, 6]

print(elementos_duplicados(lista))