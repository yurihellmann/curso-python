# Dada a matriz (lista de listas):
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Crie uma função que receba essa matriz e retorne uma nova matriz com os elementos das linhas invertidos. 
# Exemplo: a linha [1, 2, 3] se tornaria [3, 2, 1].

def inverter_linhas(matriz):
    return [linha[::-1] for linha in matriz]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nova_matriz = inverter_linhas(matriz)
print(nova_matriz)
