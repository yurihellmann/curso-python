# Escreva uma função que receba um dicionário com produtos e preços e um valor limite. 
# A função deve retornar um novo dicionário contendo apenas os produtos cujo preço seja inferior ao valor limite.

def filtrar_produtos_por_preco(produtos, limite):
    produtos_filtrados = {}

    for produto, preco in produtos.items():
        if preco < limite:
            produtos_filtrados[produto] = preco
    
    return produtos_filtrados

produtos = {
    "Teclado Gamer": 250.00,
    "Mouse Gamer": 150.00,
    "Monitor Gamer": 1750.00,
    "MousePad Gamer": 75.00,
    "RTX 4060": 4000.00
}

limite = 1000.00

print(filtrar_produtos_por_preco(produtos, limite))