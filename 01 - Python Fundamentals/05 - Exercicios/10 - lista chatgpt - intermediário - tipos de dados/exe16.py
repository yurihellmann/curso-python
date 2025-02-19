# Crie uma função que receba uma lista de dicionários, onde cada dicionário representa uma pessoa com chaves para "nome", "idade" e "cidade". 
# A função deve retornar um dicionário onde as chaves são os nomes das cidades e os valores são listas contendo os nomes das pessoas 
# que moram em cada cidade.

def pessoas_por_cidade(lista_pessoas):
    pessoas_por_cidade = {}

    for pessoa in lista_pessoas:
        cidade = pessoa["Cidade"]
        if cidade in pessoas_por_cidade:
            pessoas_por_cidade[cidade].append(pessoa["Nome"])
        else:
            pessoas_por_cidade[cidade] = [pessoa["Nome"]]
        
    for cidade, pessoas in pessoas_por_cidade.items():
        print(f'{cidade}: {pessoas}')


lista_pessoas = [
    {"Nome": "Yuri", "Idade": 25, "Cidade": "Joinville"},
    {"Nome": "Isabella", "Idade": 21, "Cidade": "Lages"},
    {"Nome": "Zayn", "Idade": 1, "Cidade": "Joinville"},
    {"Nome": "Débora", "Idade": 46, "Cidade": "Joinville"},
    {"Nome": "Alexander", "Idade": 49, "Cidade": "Joinville"},
    {"Nome": "Gabriel", "Idade": 19, "Cidade": "Joinville"},
    {"Nome": "Luna", "Idade": 2, "Cidade": "Joinville"},
    {"Nome": "Ademar", "Idade": 42, "Cidade": "Lages"},
    {"Nome": "Simone", "Idade":53, "Cidade": "Lages"},
    {"Nome": "Oscar", "Idade":3, "Cidade": "Lages"},
    {"Nome": "Isis", "Idade":4, "Cidade": "Florianópolis"},
]

pessoas_por_cidade(lista_pessoas)