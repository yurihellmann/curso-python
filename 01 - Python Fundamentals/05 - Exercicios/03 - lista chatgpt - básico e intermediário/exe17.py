# Crie um programa que receba um número inteiro positivo e, utilizando um loop, conte de 1 até esse número.

number = int(input("Informe um número para contar até: "))

for i in range(number + 1):
    print(f'Contando {i}')
    i += 1