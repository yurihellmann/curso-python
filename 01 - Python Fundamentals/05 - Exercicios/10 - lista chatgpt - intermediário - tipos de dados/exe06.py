# Crie uma função que receba um conjunto de palavras e retorne um novo conjunto contendo apenas as palavras que possuem exatamente cinco letras.

def palavras_com_cinco_letras(conjunto_palavras):
    
    conjunto_filtrado = {palavra for palavra in conjunto_palavras if len(palavra) == 5}

    return sorted(conjunto_filtrado)

conjunto_palavras = {'janeiro', 'março', 'abril', 'maio', 'junho'}

print(palavras_com_cinco_letras(conjunto_palavras))
