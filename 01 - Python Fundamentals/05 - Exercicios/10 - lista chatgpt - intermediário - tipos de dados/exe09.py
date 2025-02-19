# Escreva uma função que receba uma tupla de inteiros e retorne uma nova tupla com os 
# elementos multiplicados por sua posição (índice) original na tupla.

def multiplicar_por_indice(tupla):
    
    lista_multiplicados = [numero * tupla.index(numero) for numero in tupla]

    tupla_multiplicados = tuple(lista_multiplicados)

    return tupla_multiplicados

numeros = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(multiplicar_por_indice(numeros))
