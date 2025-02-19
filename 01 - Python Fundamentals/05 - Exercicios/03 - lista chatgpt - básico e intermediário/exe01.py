# Escreva um programa que receba dois números do usuário e exiba a soma, subtração, multiplicação e divisão entre eles.

def Somar (numero1, numero2):
    soma = numero1 + numero2
    return soma

def Subtrair (numero1, numero2):
    subtracao = numero1 - numero2
    return subtracao

def Multiplicar (numero1, numero2):
    multiplicacao = numero1 * numero2
    return multiplicacao

def Dividir (numero1, numero2):
    divisao = numero1 / numero2
    return divisao

def Operar (numero1, numero2):
    soma = Somar(numero1, numero2)
    subtracao = Subtrair(numero1, numero2)
    multiplicacao = Multiplicar(numero1, numero2)
    divisao = Dividir(numero1, numero2)

    print(f'{numero1} + {numero2} = {soma}')
    print(f'{numero1} - {numero2} = {subtracao}')
    print(f'{numero1} x {numero2} = {multiplicacao}')
    print(f'{numero1} / {numero2} = {divisao}')

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

Operar(numero1, numero2)


