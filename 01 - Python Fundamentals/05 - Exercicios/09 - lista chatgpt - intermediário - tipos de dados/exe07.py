# Crie uma função que receba um dicionário com chaves representando produtos e valores representando quantidades. 
# A função deve retornar um novo dicionário onde os produtos que têm quantidade menor que 10 foram removidos.

def filtrar_produtos(dicionario):
    dicionario_filtrado = {}

    for item, quantidade in dicionario.items():
        if quantidade >= 10:
            dicionario_filtrado[item] = quantidade

    return dicionario_filtrado

dicionario = {
    "Maçã": 10,
    "Pera": 9,
    "Uva": 15,
    "Melão": 11,
    "Laranja": 5
}

print(filtrar_produtos(dicionario))
