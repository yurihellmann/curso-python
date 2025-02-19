# Dada a tupla nums = (1, 2, 3, 4, 5), escreva uma função que receba essa tupla e retorne:
# A soma de todos os seus elementos.
# O produto de todos os seus elementos.

def soma(tupla):
    lista = list(tupla)
    soma = (sum(lista))

    return soma

def produto(tupla):
    lista = list(tupla)
    produto = 1

    for n in lista:
        produto = produto * n

    return produto

tupla = (1, 2, 3, 4, 5)

print(soma(tupla))
print(produto(tupla))