# Dado o dicionário de vendas abaixo, onde cada chave é um vendedor e o valor é uma lista de quantidades vendidas por mês:
# vendas = {
#     "Carlos": [120, 150, 100],
#     "Fernanda": [80, 90, 95],
#     "Bruno": [100, 110, 105]
# }
# Tarefa: Adicione as vendas do mês de outubro para cada vendedor no dicionário. As vendas são: Carlos (130), Fernanda (85), Bruno (115).

vendas = {
    "Carlos": [120, 150, 100],
    "Fernanda": [80, 90, 95],
    "Bruno": [100, 110, 105]
}

for vendedor, venda in vendas.items():
    if vendedor == "Carlos":
        venda.append(130)
    elif vendedor == "Fernanda":
        venda.append(85)
    elif vendedor == "Bruno":
        venda.append(115)

print(vendas)

