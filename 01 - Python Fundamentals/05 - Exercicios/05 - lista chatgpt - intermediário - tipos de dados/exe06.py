# Dado dois conjuntos:
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# Crie uma função que retorne a diferença simétrica entre os conjuntos A e B (elementos que estão em um dos conjuntos, mas não em ambos).

def diferenca_conjuntos(A, B):
    diferenca_simetrica = A.symmetric_difference(B)
    
    return diferenca_simetrica

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(diferenca_conjuntos(A, B))