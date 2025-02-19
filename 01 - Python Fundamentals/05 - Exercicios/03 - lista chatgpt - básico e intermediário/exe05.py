# Escreva uma função que conte o número de vogais em uma string.

def ContaVogais (string):
    vogais = "aeiouAEIOU"
    contador = 0

    for char in string:
        if char in vogais:
            contador += 1

    return contador

string = str(input("Informe a string a ser verificada a quantidade de vogais: "))
quantidade_vogais = ContaVogais(string)

print(f'A quantidade de vogais da string {string} é de {quantidade_vogais}')