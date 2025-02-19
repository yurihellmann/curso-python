# Escreva uma função que receba duas listas e retorne um conjunto contendo os elementos que estão apenas na primeira lista, mas não na segunda.

def elementos_unicos_primeira_lista(lista1, lista2):
    conjunto = set()

    for elemento in lista1:
        if elemento not in lista2:
            conjunto.add(elemento)

    return conjunto

lista1 = ['maçã', 'uva', 'pera', 'laranja', 'banana']
lista2 = ['pera', 'laranja', 'banana']

print(elementos_unicos_primeira_lista(lista1, lista2))
