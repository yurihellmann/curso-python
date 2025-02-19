# Escreva uma função que receba uma tupla de strings e retorne uma tupla 
# onde cada string foi convertida para maiúsculas e ordenada em ordem alfabética.

def strings_ordenadas_maiusculas(tupla):
    lista = [string.upper() for string in tupla]
    lista.sort()
    nova_tupla = tuple(lista)

    return nova_tupla

tupla = ('banana', 'maçã', 'abacate', 'uva', 'laranja')
print(strings_ordenadas_maiusculas(tupla))
