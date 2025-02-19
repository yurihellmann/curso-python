# Crie uma função que receba uma lista de palavras e retorne uma nova lista 
# onde cada palavra foi invertida, mas a ordem das palavras permanece a mesma.

def inverter_palavras(lista):
    vogais = "aeiouAEIOU"
    
    palavras_invertidas = [string[::-1] for string in lista] # if string[0] in vogais]

    return palavras_invertidas

palavras = ['banana', 'uva', 'maçã']

print(inverter_palavras(palavras))