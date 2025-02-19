# Dado um dicionário com os nomes e as notas de alunos:
# notas = {
#     "Alice": 85,
#     "Bruno": 92,
#     "Carla": 70,
#     "Daniel": 60
# }
# Tarefa: Filtre os alunos que têm nota maior que 80 e crie um novo dicionário com esses alunos.

notas = {
    "Alice": 85,
    "Bruno": 92,
    "Carla": 70,
    "Daniel": 60
}

maiores_notas = {}

for aluno, nota in notas.items():
    if nota > 80:
        maiores_notas[aluno] = nota

print(maiores_notas)