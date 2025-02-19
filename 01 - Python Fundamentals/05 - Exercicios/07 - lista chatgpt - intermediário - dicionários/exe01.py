# Dada uma lista de tuplas representando categorias e itens:
# lista = [("Frutas", "Maçã"), ("Frutas", "Banana"), ("Legumes", "Cenoura"), ("Frutas", "Laranja"), ("Legumes", "Pepino")]
# Tarefa: Crie um dicionário que agrupe os itens por categoria, ou seja, 
# as chaves serão as categorias e os valores serão listas de itens correspondentes. Exemplo de saída esperada:

lista = [("Frutas", "Maçã"), ("Frutas", "Banana"), ("Legumes", "Cenoura"), ("Frutas", "Laranja"), ("Legumes", "Pepino")]

itens_filtrados = {}

for categoria, item in lista:

    if categoria not in itens_filtrados:
        itens_filtrados[categoria] = []
    itens_filtrados[categoria].append(item)
        

print(itens_filtrados)


