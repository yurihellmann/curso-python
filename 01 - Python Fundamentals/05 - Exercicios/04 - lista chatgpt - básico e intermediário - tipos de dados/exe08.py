# Crie dois conjuntos: um com os números ímpares de 1 a 10 e outro com os números pares de 1 a 10. Faça as seguintes operações:
# União dos conjuntos.
# Interseção dos conjuntos.
# Diferença entre o conjunto de ímpares e o de pares.

pares = set()
impares = set()

for i in range(1, 11):
    if i % 2 == 0:
        pares.add(i)
    else:
        impares.add(i)

print(f'Impares: {impares}')
print(f'Pares: {pares}')

uniao = impares.union(pares)
print(f'União: {uniao}')

intersecao = impares.intersection(pares)
print(f'Interseção: {intersecao}')

diferenca = impares.difference(pares)
print(f'Diferença: {diferenca}')