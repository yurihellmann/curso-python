# Escreva uma função que receba uma lista de listas de inteiros e retorne uma lista contendo a soma dos elementos de cada sublista.

def soma_sublistas(lista):
    somas = [sum(numeros) for numeros in lista]

    return somas

numeros_inteiros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(soma_sublistas(numeros_inteiros))