# Crie uma função que receba uma lista de dicionários onde cada dicionário representa uma venda, contendo as chaves "produto" e "quantidade". 
# A função deve retornar um dicionário onde as chaves são os nomes dos produtos e os valores são o total de vendas de cada produto.

def total_vendas_por_produto(lista_vendas):
    vendas_totais = {}

    for venda in lista_vendas:
        for item, quantidade in venda.items():
            if item not in vendas_totais:
                vendas_totais[item] = quantidade
            else:
                vendas_totais[item] += quantidade

    return vendas_totais

vendas = [
    {"Teclado Gamer": 2},
    {"Monitor Gamer": 1},
    {"Mouse Gamer": 3},
    {"Teclado Gamer": 1},
    {"Monitor Gamer": 2},
    {"Mouse Gamer": 2},
]

print(total_vendas_por_produto(vendas))
