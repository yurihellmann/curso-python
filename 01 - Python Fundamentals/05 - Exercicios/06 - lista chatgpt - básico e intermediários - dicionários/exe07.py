# Mesclar dois dicionários:
# estoque_1 = {"Maçã": 100, "Banana": 200}
# estoque_2 = {"Laranja": 150, "Banana": 50}
# Tarefa: Combine os dois dicionários em um só. Se a fruta existir em ambos os dicionários, some as quantidades.

estoque_1 = {"Maçã": 100, "Banana": 200}
estoque_2 = {"Laranja": 150, "Banana": 50}

estoque_total = estoque_1.copy()

for item, quantidade in estoque_2.items():
    if item in estoque_total:
        estoque_total[item] += quantidade
    else:
        estoque_total[item] = quantidade

print(estoque_total)