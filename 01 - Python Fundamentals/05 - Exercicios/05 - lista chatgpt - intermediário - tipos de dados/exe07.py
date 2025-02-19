# Dada a lista numeros = [10, 20, 30, 20, 10, 40, 50, 30], crie uma função que remova todos os elementos duplicados, utilizando conjuntos.

def remove_duplicados(lista):
    conjunto = set(lista)

    return sorted(conjunto)

lista = [10, 20, 30, 20, 10, 40, 50, 30]

print(remove_duplicados(lista))