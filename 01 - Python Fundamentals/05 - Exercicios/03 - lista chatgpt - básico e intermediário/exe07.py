# Escreva um programa que receba uma lista de números e exiba o maior e o menor número.

def EncontraMaiorMenor (lista):
    maior = max(lista)
    menor = min(lista)

    return maior, menor

numeros = input("Digite uma lista de números separados por espaço: ")

lista_numeros = list(map(int, numeros.split()))

maior, menor = EncontraMaiorMenor(lista_numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

