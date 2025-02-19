# Escreva uma função que receba uma lista de dicionários representando alunos (nome, nota) e retorne o nome do aluno com a maior nota.

def aluno_com_maior_nota(lista_alunos):
    maior_nota = 0
    melhor_aluno = None
    
    for aluno in lista_alunos:
        for nome, nota in aluno.items():
            if nota > maior_nota:
                maior_nota = nota
                melhor_aluno = nome
    
    mensagem = f'O aluno com a maior nota é {melhor_aluno} com a nota de {maior_nota}'

    return mensagem

lista_alunos = [
    {"Yuri": 9},
    {"Isabella": 10}
]

print(aluno_com_maior_nota(lista_alunos))
