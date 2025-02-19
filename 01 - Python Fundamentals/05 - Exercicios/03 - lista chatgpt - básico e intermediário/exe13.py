# Escreva um programa que simule um sistema de notas de alunos, onde o usuário pode cadastrar os nomes e as notas, 
# e depois consultar a média de um aluno específico.

menu = """
Bem vindo ao sistema de alunos!

O que deseja fazer hoje?

[1] - Cadastrar aluno
[2] - Cadastrar notas
[3] - Exibir média
[0] - Sair

=> """

alunos = []
alunos_notas = {}
alunos_medias = {}

soma = 0

while True:
    opcao = int(input(menu))

    if opcao == 1:
        nome_aluno = str(input("Informe o nome do aluno: ")).capitalize()
        alunos.append(nome_aluno)
        print(f'Aluno {nome_aluno} cadastrado com sucesso!')
    # Verifica se aluno existe na lista de alunos e deve cadastrar as notas ao respectivo aluno informado.
    elif opcao == 2:
        while True:
            aluno = input("Informe o aluno que deseja atribuir as notas (deixe em branco para sair): ").capitalize()
            if aluno == "":
                break
            elif aluno not in alunos:
                print(f'O aluno {aluno} não está cadastrado no sistema!\n')
            elif aluno in alunos:
                notas = input(f"Informe as notas (separadas por espaço) para o aluno {aluno}: ").split()
                notas = list(map(float, notas))
                indice_alunos = alunos.index(aluno)
                alunos_notas[alunos[indice_alunos]] = notas

    elif opcao == 3:
        while True:
            aluno = input("Informe o aluno que deseja verificar a média (deixe em branco para sair): ").capitalize()
            if aluno == "":
                break
            elif aluno not in alunos:
                print(f'O aluno {aluno} não está cadastrado no sistema!\n')
            elif aluno not in alunos_notas:
                print(f'Não há notas cadastradas para o aluno {aluno}.\n')
            else:
                notas = alunos_notas[aluno]
                media = sum(notas) / len(notas)
                print(f'A média do aluno {aluno} é {media:.2f}')

    elif opcao == 0:
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente")