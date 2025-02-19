nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

maiorIdade = 18

if (idade > maiorIdade):
    mensagem = f"{nome} - Maior de idade"
else:
    mensagem = f"{nome} - Menor de idade"

print(mensagem)