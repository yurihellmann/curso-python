# Escreva uma função que receba um dicionário onde as chaves são nomes de pessoas e os valores são suas idades. 
# A função deve retornar um novo dicionário apenas com as pessoas que têm idade entre 20 e 30 anos.

def pessoas_entre_20_30(pessoas):
    pessoas_entre_20_30_anos = dict()

    for nome, idade in pessoas.items():
        if idade >= 20 and idade <= 30:
            pessoas_entre_20_30_anos[nome] = idade

    return pessoas_entre_20_30_anos

pessoas = {
    "Yuri": 25,
    "Isabella": 21,
    "Gabriel": 19
}

print(pessoas_entre_20_30(pessoas))

