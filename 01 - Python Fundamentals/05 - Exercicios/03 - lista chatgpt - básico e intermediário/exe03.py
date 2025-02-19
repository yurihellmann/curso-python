# Escreva um programa que calcule o fatorial de um número dado.

def CalcularFatorial (numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    mensagem = (f'O fatorial de {numero} é {fatorial}')

    return mensagem

numero = int(input("Informe um número para calcular o fatorial: "))

print(CalcularFatorial(numero))


