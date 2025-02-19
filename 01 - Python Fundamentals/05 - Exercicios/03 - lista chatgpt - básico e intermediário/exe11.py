# Crie um programa que receba duas listas e exiba a união e a diferença entre elas usando conjuntos.

def ConverteSet (lista):
    conjunto = set(lista)
    
    return conjunto

def UniaoConjuntos (lista1, lista2):
    set1 = ConverteSet(lista1)
    set2 = ConverteSet(lista2)
    uniao_set = set1 | set2

    return uniao_set

def DiferencaConjuntos (lista1, lista2):
    set1 = ConverteSet(lista1)
    set2 = ConverteSet(lista2)
    diferenca_set = set1 - set2
    
    return diferenca_set

lista1 = input("Digite uma lista de números separados por espaço: ")
lista2 = input("Digite uma segunda lista de números separados por espaço: ")

lista1 = list(map(int, lista1.split()))
lista2 = list(map(int, lista2.split()))

uniao = UniaoConjuntos(lista1, lista2)
diferenca = DiferencaConjuntos(lista1, lista2)

print(f'O conjunto união é {uniao} e o conjunto diferença é {diferenca}')

