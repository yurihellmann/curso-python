# Dado o dicionário de empregados com as respectivas horas trabalhadas por mês:
# empregados = {
#     "João": {"Janeiro": 160, "Fevereiro": 170, "Março": 155},
#     "Maria": {"Janeiro": 150, "Fevereiro": 175, "Março": 160},
#     "Ana": {"Janeiro": 165, "Fevereiro": 160, "Março": 170}
# }
# Tarefa: Calcule e adicione uma nova chave "Total" em cada subdicionário, 
# representando o total de horas trabalhadas pelo empregado nos três meses.

empregados = {
    "João": {"Janeiro": 160, "Fevereiro": 170, "Março": 155},
    "Maria": {"Janeiro": 150, "Fevereiro": 175, "Março": 160},
    "Ana": {"Janeiro": 165, "Fevereiro": 160, "Março": 170}
}

for empregado, meses in empregados.items():
    total_horas = sum(meses.values())
    meses["Total"] = total_horas

print(empregados)