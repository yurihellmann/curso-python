# Crie uma função que receba uma lista de strings e retorne uma nova lista contendo as 
# strings que têm comprimento maior que a média do comprimento de todas as strings da lista.

def string_maiores_que_media(lista):
    quantidade_caracteres = []
    maiores_strings = []
    
    for string in lista:
        quantidade = len(string)
        quantidade_caracteres.append(quantidade)

    media = (sum(quantidade_caracteres)) / len(quantidade_caracteres)

    for string in lista:
        if len(string) > media:
            maiores_strings.append(string)

    return maiores_strings

lista = ["batata", "banana", "uva", "pera", "maçã", "pitanga"]

print(string_maiores_que_media(lista))