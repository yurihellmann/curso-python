# Crie um programa que conte a ocorrência de cada caractere em uma string.
# string = "banana"
# Tarefa: Crie um dicionário onde as chaves são os caracteres e os valores são o número de vezes que eles aparecem na string.

ocorrencias = {}

def contar_caracteres(string):
    for caractere in string:
        if caractere in ocorrencias:
            ocorrencias[caractere] += 1
        else:
            ocorrencias[caractere] = 1

    return ocorrencias

string = "banana"

print(contar_caracteres(string))