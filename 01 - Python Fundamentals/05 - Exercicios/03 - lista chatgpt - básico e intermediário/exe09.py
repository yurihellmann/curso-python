# Faça um programa que receba duas listas e exiba a interseção (elementos comuns) entre elas.

def IntersecaoListas (lista1, lista2):
    intersecao = set(lista1).intersection(lista2)
    return intersecao

lista1 = input("Digite uma lista de números separados por espaço: ")
lista2 = input("Digite uma segunda lista de números separados por espaço: ")

lista1 = list(map(int, lista1.split()))
lista2 = list(map(int, lista2.split()))

print(IntersecaoListas(lista1, lista2))