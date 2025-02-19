# Crie uma função que receba um dicionário onde as chaves são nomes de pessoas e os valores são listas de notas. 
# A função deve retornar um novo dicionário onde as chaves são os nomes e os valores são as médias das notas de cada pessoa.

def media_notas(notas_alunos):
    media_alunos = {}

    for aluno, notas in notas_alunos.items():
        media_alunos[aluno] = sum(notas) / len(notas)

    return media_alunos

notas_alunos = {
    "Isabella": [8, 9, 10],
    "Yuri": [4, 3, 8]
}

resultado = media_notas(notas_alunos)
print(resultado)
    
