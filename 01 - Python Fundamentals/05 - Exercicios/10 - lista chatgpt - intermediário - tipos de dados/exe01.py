# Escreva uma função que receba uma tupla de strings e retorne uma nova tupla contendo apenas as strings que começam com uma vogal.

def strings_comecam_com_vogal(tupla):
    lista = []
    vogais = ("aeiouAEIOU")

    for string in tupla:
        if string[0] in vogais:
            lista.append(string)

    tupla_filtrada = tuple(lista)

    return tupla_filtrada
        
tupla = ("abacaxi", "beterraba", "caju", "espinafre", "uva")

print(strings_comecam_com_vogal(tupla))
