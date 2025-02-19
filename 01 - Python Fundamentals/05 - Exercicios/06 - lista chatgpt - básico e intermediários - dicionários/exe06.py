# Dado o dicionário abaixo:
# paises_capitais = {
#     "Brasil": "Brasília",
#     "França": "Paris",
#     "Japão": "Tóquio"
# }
# Tarefa: Inverta as chaves e valores desse dicionário, criando um novo dicionário onde as capitais serão as chaves e os países, os valores.

paises_capitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio"
}

capitais_paises = {}

for pais, capital in paises_capitais.items():
    capitais_paises[capital] = pais

print(capitais_paises)