# Crie dois dicionários. Em seguida, escreva uma função que mescle esses dois dicionários. 
# Se ambos os dicionários tiverem a mesma chave, some os valores correspondentes.

def somar_estoques(estoque_1, estoque_2):
    estoque_total = {}

    for item, quantidade in estoque_1.items():
        if item in estoque_total:
            estoque_total[item] += quantidade
    for item, quantidade in estoque_2.items():
        if item in estoque_total:
            estoque_total[item] += quantidade
        else:
            estoque_total[item] = quantidade

    return estoque_total

estoque_1 = {
    "Maçã": 10,
    "Laranja": 25,
    "Uva": 15
}

estoque_2 = {
    "Maçã": 15,
    "Laranja": 40,
    "Melão": 35
}

print(somar_estoques(estoque_1, estoque_2))