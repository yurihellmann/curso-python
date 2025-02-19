# Dado o dicionário de notas dos alunos:
# notas = {
#     "João": 78,
#     "Mariana": 92,
#     "Carlos": 85,
#     "Aline": 88
# }
# Tarefa: Ordene o dicionário pelo valor das notas em ordem decrescente e imprima o resultado.

notas = {
    "João": 78,
    "Mariana": 92,
    "Carlos": 85,
    "Aline": 88
}

notas_ordenadas = dict(sorted(notas.items(), key=lambda item: item[1], reverse=True))

print(notas_ordenadas)