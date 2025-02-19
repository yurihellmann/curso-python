# Crie uma função que receba dois conjuntos e retorne a diferença simétrica entre eles.

#Usando função que verifica
def diferenca_simetrica(conjunto1, conjunto2):
    diferenca = conjunto1.symmetric_difference(conjunto2)

    return diferenca

conjunto1 = {"Maçã", "Banana", "Uva"}
conjunto2 = {"Laranja", "Uva", "Maçã"}

print(diferenca_simetrica(conjunto1, conjunto2))

#Sem usar função especifica
def dif_simetrica(conjunto1, conjunto2):
    conjunto_filtrado = set()

    for item in conjunto1:
        if item not in conjunto2:
            conjunto_filtrado.add(item)
    
    for item in conjunto2:
        if item not in conjunto1:
            conjunto_filtrado.add(item)

    return conjunto_filtrado

print(dif_simetrica(conjunto1, conjunto2))