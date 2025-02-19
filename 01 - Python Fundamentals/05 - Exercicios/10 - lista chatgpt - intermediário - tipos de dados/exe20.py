# Crie uma função que receba uma lista de listas de números e retorne uma lista com os maiores valores de cada sublista.

def maiores_valores_sublistas(lista):
    maiores = []

    for sublista in lista:
        maiores.append(max(sublista))

    return maiores

lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(maiores_valores_sublistas(lista))
