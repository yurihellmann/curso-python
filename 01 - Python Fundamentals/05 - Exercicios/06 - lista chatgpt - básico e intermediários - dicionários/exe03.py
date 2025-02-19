# Dado o dicionário abaixo, imprima cada chave e seu valor.
# carros = {
#     "Ford": "Mustang",
#     "Chevrolet": "Camaro",
#     "Ferrari": "488 Spider"
# }
# Tarefa: Utilize um loop for para imprimir cada par de chave e valor.

carros = {
    "Ford": "Mustang",
    "Chevrolet": "Camaro",
    "Ferrari": "488 Spider"
}

for marca, modelo in carros.items():
    print(f'{marca}: {modelo}')