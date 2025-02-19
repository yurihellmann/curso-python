# Crie uma função que receba dois conjuntos e retorne True se o primeiro conjunto for um subconjunto do segundo, e False caso contrário.

def verificar_subconjunto(conjunto1, conjunto2):
    
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    
    return True
    
conjunto2 = {1, 2, 3, 4}
conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(verificar_subconjunto(conjunto1, conjunto2))