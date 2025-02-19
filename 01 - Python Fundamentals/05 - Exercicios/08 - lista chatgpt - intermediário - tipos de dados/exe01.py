# Crie uma função que receba uma lista de tuplas com dois valores cada. 
# A função deve retornar uma nova tupla contendo a soma dos primeiros valores de cada tupla e a soma dos segundos valores de cada tupla.

def soma_tuplas(lista_tuplas):
    soma1 = lista_tuplas[0][0] + lista_tuplas[1][0]
    soma2 = lista_tuplas[0][1] + lista_tuplas[1][1]

    return soma1, soma2

lista_tuplas = [(3, 6), (5, 9)]

print(soma_tuplas(lista_tuplas))

# Solução Gemini:

def soma_tupla_de_tuplas(lista_tuplas):

    soma_primeiros = 0
    soma_segundos = 0

    for tupla in lista_tuplas:
        soma_primeiros += tupla[0]
        soma_segundos += tupla[1]

    return (soma_primeiros, soma_segundos)

print(soma_tupla_de_tuplas(lista_tuplas))