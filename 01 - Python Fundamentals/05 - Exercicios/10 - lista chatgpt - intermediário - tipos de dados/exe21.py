# Escreva uma função que receba uma lista de conjuntos e 
# retorne um conjunto com a união de todos os conjuntos que contêm ao menos um número primo.

def uniao_conjuntos_com_primos(lista_conjuntos):
    
    def eh_primo(numero):
        if numero <= 1:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
    
    uniao = set()
    for conjunto in lista_conjuntos:
        for numero in conjunto:
            if eh_primo(numero):
                uniao.update(conjunto)
                break
    return uniao

conjuntos = [[2, 4, 6], [3, 5, 7], [8, 9, 10], [11, 13]]
print(uniao_conjuntos_com_primos(conjuntos))