# Escreva um programa que receba um número e imprima a tabuada desse número (de 1 a 10).

def Tabuada (numero):
    for i in range(11):
        tabuada = numero * i
        print(f'{numero} x {i} = {tabuada}')

numero = int(input("Digite um número de 1 a 10 para retornar a tabuada: "))

print(Tabuada(numero))
    