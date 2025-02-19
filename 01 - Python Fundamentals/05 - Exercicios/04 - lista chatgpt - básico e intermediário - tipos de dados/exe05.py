# Crie uma lista com os números de 1 a 10. Faça as seguintes operações:
# Adicione o número 11 no final da lista.
# Remova o número 5 da lista.
# Inverta a lista.
# Ordene a lista.

lista = []

for i in range(1, 11):    
    lista.append(i)

print(lista)

lista.append(11)
print(lista)

lista.remove(5)
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)

