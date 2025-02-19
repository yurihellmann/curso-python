# Crie um dicionário que armazene o nome de 3 frutas e seus preços por kg.
# frutas = {
#     "Banana": 3.50,
#     "Maçã": 5.20,
#     "Laranja": 2.30
# }
# Tarefa 1: Adicione uma nova fruta ao dicionário, como "Morango" com preço 6.00.
# Tarefa 2: Remova a "Laranja" do dicionário.

frutas = {
    "Banana": 3.50,
    "Maçã": 5.20,
    "Laranja": 2.30
}

frutas.update({"Morango": 6.00})
print(frutas)

frutas.pop("Laranja")
print(frutas)