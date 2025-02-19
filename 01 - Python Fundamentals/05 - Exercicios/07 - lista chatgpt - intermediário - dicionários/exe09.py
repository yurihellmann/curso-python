# Escreva uma função que receba uma string e retorne um dicionário onde as chaves são as palavras da string e os 
# valores são a contagem de quantas vezes cada palavra aparece.

def contar_palavras(texto):
    texto = texto.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    palavras = texto.split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

texto = "Isabella é uma baita de uma grande de uma gostosa"
print(contar_palavras(texto))