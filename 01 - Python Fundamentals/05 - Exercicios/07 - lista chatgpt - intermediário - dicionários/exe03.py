# Dado o dicionário a seguir, onde alguns valores são None:
# clientes = {
#     "Alice": 25,
#     "Bruno": None,
#     "Carla": 33,
#     "Daniel": None,
#     "Elaine": 42
# }
# Tarefa: Remova todas as chaves que possuem valores None e retorne o dicionário resultante.

clientes = {
    "Alice": 25,
    "Bruno": None,
    "Carla": 33,
    "Daniel": None,
    "Elaine": 42
}

clientes_filtrados = {}

for cliente, idade in clientes.items():
    if idade != None:
        clientes_filtrados[cliente] = idade

print(clientes_filtrados)