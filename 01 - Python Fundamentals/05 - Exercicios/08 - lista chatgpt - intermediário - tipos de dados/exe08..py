# Escreva uma função que receba uma lista de dicionários, onde cada dicionário contém informações sobre uma pessoa (nome, idade, cidade). 
# A função deve retornar um dicionário onde as chaves são os nomes das pessoas e os valores são suas respectivas idades.

def nome_para_idade(lista_pessoas):
    dicionario_pessoas = {}

    for pessoa in lista_pessoas:
            dicionario_pessoas[pessoa["Nome"]] = pessoa["Idade"]

    for nome, idade in dicionario_pessoas.items():
        print(f"{nome}: {idade}")

lista_pessoas = [
    {"Nome": "Yuri", "Idade": 25, "Cidade": "Joinville"},
    {"Nome": "Isabella", "Idade": 21, "Cidade": "Lages"},
    {"Nome": "Lulu da Pomerânia", "Idade": "Velho demais para este mundo", "Cidade": "SFS"}
    ]

nome_para_idade(lista_pessoas)