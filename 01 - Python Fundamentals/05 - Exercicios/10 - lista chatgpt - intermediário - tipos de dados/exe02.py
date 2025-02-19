# Crie uma função que receba uma lista de tuplas, onde cada tupla contém um nome e um número. 
# A função deve retornar uma lista com os nomes únicos, ordenados em ordem decrescente pela soma dos números associados a cada nome.

def ordenar_nomes_por_soma(lista):
    # Cria um dicionário para armazenar a soma dos números para cada nome
    soma_por_nome = {}
    
    # Itera sobre a lista de tuplas para somar os números associados a cada nome
    for nome, numero in lista:
        if nome in soma_por_nome:
            soma_por_nome[nome] += numero
        else:
            soma_por_nome[nome] = numero
    
    return [nome for nome, _ in sorted(soma_por_nome.items(), key=lambda item: item[1], reverse=True)]

lista_tuplas = [("Isabella", 21), ("Gabriel", 19), ("Yuri", 25), ("Gabriel", 1)]

print(ordenar_nomes_por_soma(lista_tuplas))