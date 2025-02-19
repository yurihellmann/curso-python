# Dado o dicionário de um inventário abaixo:
# inventario = {
#     "Pão": 50,
#     "Leite": 30,
#     "Ovos": 200
# }
# Tarefa: Verifique se "Leite" está no inventário e imprima uma mensagem apropriada.

inventario = {
    "Pão": 50,
    "Leite": 30,
    "Ovos": 200
}

for item, quantidade in inventario.items():
    if item == "Leite":
        print(f'Temos o item leite no estoque com a quantidade {quantidade}')