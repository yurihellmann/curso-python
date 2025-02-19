# Crie uma função que receba uma tupla de números inteiros e retorne uma nova tupla onde cada número 
# é substituído pela diferença entre ele e o maior número da tupla.

def diferenca_para_maior(tupla):
    lista = [max(tupla) - numero for numero in tupla if numero != max(tupla)]
    nova_tupla = tuple(lista)

    return nova_tupla

tupla = (1, 2, 3, 6, 5, 4)

print(diferenca_para_maior(tupla))
