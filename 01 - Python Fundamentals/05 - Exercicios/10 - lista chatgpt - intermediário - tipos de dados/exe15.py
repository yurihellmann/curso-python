# Escreva uma função que receba um dicionário com chaves representando categorias e valores como listas de preços. 
# A função deve retornar um novo dicionário com a média dos preços para cada categoria.

def media_precos_por_categoria(dicionario):
    media_categorias = {}

    for categoria, valores in dicionario.items():
        media = sum(valores) / len(valores)
        media_categorias[categoria] = media
    
    for categoria, media in media_categorias.items():
        print(f'Linha {categoria}: R${media:.2f}')


categorias_valores = {
    "Gamer entrada": [500.59, 102.69, 150.99, 1250.99],
    "Gamer entusiasta": [750.59, 205.69, 250.99, 1750.99],
    "Gamer high-end": [950.59, 405.69, 350.99, 2750.99],
}

print(media_precos_por_categoria(categorias_valores))