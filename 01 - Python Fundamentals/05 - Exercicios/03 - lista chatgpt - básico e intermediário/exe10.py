# Escreva um programa que receba uma lista de elementos e converta para uma tupla.

def ConverteTupla (lista):
    tupla = tuple(lista)

    return tupla

lista = input("Digite uma lista de números separados por espaço: ")
lista = list(map(int, lista.split()))

print(type(ConverteTupla(lista)))