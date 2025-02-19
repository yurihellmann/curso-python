# Crie uma função que receba uma lista de tuplas, onde cada tupla possui três elementos: um nome, um preço e uma quantidade. 
# A função deve retornar uma tupla com o nome do produto mais caro e seu valor total (preço multiplicado pela quantidade).

def produto_mais_caro(lista_tuplas):
    lista_mais_caro = []
    produto_mais_caro = ''
    valor_mais_caro = 0

    for item in lista_tuplas:
        if (item[1] * item[2]) > valor_mais_caro:
            valor_mais_caro = item[1] * item[2]
            produto_mais_caro = item[0]

    lista_mais_caro.append(produto_mais_caro)
    lista_mais_caro.append(valor_mais_caro)

    return tuple(lista_mais_caro)

produtos = [
    ('teclado gamer', 350.00, 5),
    ('monitor gamer', 2750.99, 3),
    ('mouse gamer', 250.00, 5),
    ('mousepad gamer', 150.00, 5),
]

print(produto_mais_caro(produtos))
