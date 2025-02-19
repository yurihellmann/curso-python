# # Escreva uma função que receba uma lista de números e um número alvo. 
# # A função deve retornar uma lista com todos os pares de números que somam o valor alvo.

def encontrar_pares(nums, alvo):
    pares = []
    visitados = set()
    
    for num in nums:
        complemento = alvo - num
        if complemento in visitados:
            pares.append((complemento, num))
        visitados.add(num)
    
    return pares

lista = [2, 7, 11, 15]
alvo = 9

print(encontrar_pares(lista, alvo))

