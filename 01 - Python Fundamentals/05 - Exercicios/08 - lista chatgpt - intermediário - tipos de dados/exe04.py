# Escreva uma função que receba duas listas de números e retorne uma nova 
# lista com os números que estão presentes em ambas as listas (interseção).

def intersecao_listas(lista1, lista2):
    intersecao = []
    for numero in lista1:
        if numero in lista2:
            intersecao.append(numero)

    return intersecao

lista1 = [1, 2, 3, 4,]
lista2 = [3, 4, 5, 6]

print(intersecao_listas(lista1, lista2))