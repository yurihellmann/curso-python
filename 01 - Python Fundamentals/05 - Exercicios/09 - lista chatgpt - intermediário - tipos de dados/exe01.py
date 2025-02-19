# Escreva uma função que receba uma tupla de números inteiros e retorne a soma dos elementos nas posições pares.

def soma_posicoes_pares(tupla):
    soma = 0

    for numero in tupla:
        if numero % 2 == 0:
            soma += numero

    return soma

tupla = (1, 2, 3, 4)
print(f'A soma das posições pares é: {soma_posicoes_pares(tupla)}')
