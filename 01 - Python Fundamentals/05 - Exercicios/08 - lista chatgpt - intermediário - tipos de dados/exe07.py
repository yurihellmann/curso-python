# Crie uma função que receba um dicionário onde as chaves são nomes de produtos e os valores são os preços. 
# A função deve retornar o produto mais caro.

def produto_mais_caro(produtos):
    preco = list(produtos.values())
    produto = list(produtos.keys())

    return f'O produto mais caro é {produto[preco.index(max(preco))]}, custando R${preco[produto.index(produto[preco.index(max(preco))])]}'

produtos = {
    "Teclado": 150.00,
    "Monitor": 250.99,
    "Processador": 1569.00
}

print(produto_mais_caro(produtos))