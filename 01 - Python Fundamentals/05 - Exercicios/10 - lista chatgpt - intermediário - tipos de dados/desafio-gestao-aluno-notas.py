import textwrap

alunos = {}

def cadastrar_aluno(nome):
    if nome not in alunos:
        alunos[nome] = list()
        print(f"Aluno {nome} cadastrado com sucesso!")
    else:
        print(f"Aluno {nome} já cadastrado!")

def adicionar_nota(nome, notas):
    if nome not in alunos.keys():
        print("Aluno não cadastrado no sistema.")
    elif nome in alunos.keys() and len(alunos[nome]) < 0:
        alunos[nome] = notas
        print("Nota(s) cadastrada com sucesso!")
    else:
        alunos[nome] += notas
        print("Nota(s) cadastrada com sucesso!")

def remover_aluno(nome):
    if nome not in alunos.keys():
        print("Aluno não cadastrado!")
    else:
        alunos.pop(nome)
        print(f"Aluno {nome} removido com sucesso!")

def listar_alunos():
    for aluno, notas in alunos.items():
        print(f"{aluno}: {notas}")

def calcular_media(nome):
    notas = sum(alunos.get(nome))
    media = notas / len(alunos.get(nome))
    print(f"A média do aluno {nome} é {media:.2f}")

def relatorio_geral():
    for aluno, notas in alunos.items():
        media = sum(notas) / len(notas)
        if media >= 7:
            situacao = "Aprovado"
            print(f"Aluno: {aluno}, média {media:.1f}, situação: {situacao}")
        else:
            situacao = "Reprovado"
            print(f"Aluno: {aluno}, média {media:.1f}, situação: {situacao}")

def menu():
    menu = """\n
    ================ MENU ================
    [1] Cadastrar aluno
    [2] Adicionar nota
    [3] Remover aluno
    [4] Listar alunos
    [5] Calcular média
    [6] Relatório geral
    [0] Sair
    => """
    return input(textwrap.dedent(menu))

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            nome = input(str("Informe o nome do aluno para cadastrar: ")).capitalize()
            cadastrar_aluno(nome)

        elif opcao == "2":
            nome = input(str("Informe o nome do aluno para adicionar notas: ")).capitalize()
            notas_str = input("Informe as notas separadas por espaço: ").split()
            notas = [float(nota) for nota in notas_str]
            adicionar_nota(nome, notas)

        elif opcao == "3":
            nome = input(str("Informe o nome do aluno para remover: ")).capitalize()
            remover_aluno(nome)

        elif opcao == "4":
            listar_alunos()

        elif opcao == "5":
            nome = input(str("Informe o nome do aluno para ver a média: ")).capitalize()
            calcular_media(nome)

        elif opcao == "6":
            relatorio_geral()
            
        elif opcao == "0":
            print("Finalizando execução!")
            break

main()
