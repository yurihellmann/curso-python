# Dado dois dicionários com notas de alunos:

# notas_1 = {"Ana": 85, "Bruno": 78, "Carla": 92}
# notas_2 = {"Bruno": 88, "Carla": 94, "Daniel": 80}
# Tarefa: Crie um novo dicionário que contenha apenas as chaves que estão presentes em 
# ambos os dicionários, mantendo os valores do segundo dicionário.

notas_1 = {"Ana": 85, "Bruno": 78, "Carla": 92}
notas_2 = {"Bruno": 88, "Carla": 94, "Daniel": 80}

notas_final = {}

for aluno, nota in notas_1.items():
    if aluno in notas_2.keys():
        notas_final[aluno] = notas_2[aluno]

print(notas_final)

