# Use list comprehension para criar uma lista que contenha o quadrado dos números de 1 a 10.

lista = []

for i in range(1, 11):
    lista.append(i)

lista_quadrado = [x**2 for x in lista]

print(lista_quadrado)