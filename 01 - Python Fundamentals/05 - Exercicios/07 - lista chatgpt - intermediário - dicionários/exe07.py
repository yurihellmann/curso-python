# Dado o dicionário de pontuações a seguir:
# pontuacoes = {
#     "Equipe A": 85,
#     "Equipe B": 92,
#     "Equipe C": 78,
#     "Equipe D": 90
# }
# Tarefa: Encontre a equipe com a pontuação máxima e imprima o nome da equipe e sua pontuação.

pontuacoes = {
    "Equipe A": 85,
    "Equipe B": 92,
    "Equipe C": 78,
    "Equipe D": 90
}

maior_pontuacao = max(pontuacoes.values())

for equipe, pontos in pontuacoes.items():
    if pontos == maior_pontuacao:
        equipe_vencedora = equipe

print(f'A equipe com a maior pontuação é a {equipe_vencedora} com {maior_pontuacao} pontos.')