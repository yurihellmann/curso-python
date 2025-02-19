# Escreva um programa que receba três números e exiba o maior deles.

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))

if a > b and a > c:
    print(f'O maior número entre {a}, {b}, {c} é {a}')
elif b > a and b > c:
    print(f'O maior número entre {a}, {b}, {c} é {b}')
else:
    print(f'O maior número entre {a}, {b}, {c} é {c}')