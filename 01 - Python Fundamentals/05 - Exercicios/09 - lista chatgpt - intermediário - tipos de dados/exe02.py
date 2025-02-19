# Crie uma função que receba uma lista de tuplas, 
# onde cada tupla contém dois números, e retorne a tupla que possui o maior produto entre os dois números.

def maior_produto(lista_tuplas):
    maior_produto = float('-inf')
    tupla_resultado = None

    for tupla in lista_tuplas:
        produto = tupla[0] * tupla[1]
        if produto > maior_produto:
            maior_produto = produto
            tupla_resultado = tupla
    
    return maior_produto, tupla_resultado

lista_tuplas = [(2, 8), (2, 6), (3, 6)]

print(maior_produto(lista_tuplas))
            