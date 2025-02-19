# Crie uma função que receba dois conjuntos de strings e 
# retorne um conjunto com todas as strings que contêm exatamente o mesmo número de caracteres em ambos os conjuntos.

def strings_com_mesmo_tamanho(conjunto1, conjunto2):
    strings_mesmo_tamanho = set()

    for string1 in conjunto1:
        for string2 in conjunto2:
            if len(string1) == len(string2):
                strings_mesmo_tamanho.add(string1)
                strings_mesmo_tamanho.add(string2)

    return strings_mesmo_tamanho

conjunto1 = {'maçã', 'uva', 'melão'}
conjunto2 = {'ovo', 'geleia', 'leite', 'pera'}

print(strings_com_mesmo_tamanho(conjunto1, conjunto2))
