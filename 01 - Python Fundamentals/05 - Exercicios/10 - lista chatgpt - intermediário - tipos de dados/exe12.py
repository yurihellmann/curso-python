# Crie uma função que receba uma lista de strings e retorne uma lista contendo apenas as palavras que aparecem mais de uma vez, sem duplicá-las.

def palavras_repetidas(lista_palavras):
    quantidade_palavras = {}

    for palavra in lista_palavras:
        if palavra in quantidade_palavras:
            quantidade_palavras[palavra] += 1
        else:
            quantidade_palavras[palavra] = 1

    palavras_filtradas = [palavra for palavra, quantidade in quantidade_palavras.items() if quantidade > 1]

    return palavras_filtradas

palavras = ['banana', 'uva', 'laranja', 'pera', 'uva', 'melão', 'banana', 'melão']

print(palavras_repetidas(palavras))
