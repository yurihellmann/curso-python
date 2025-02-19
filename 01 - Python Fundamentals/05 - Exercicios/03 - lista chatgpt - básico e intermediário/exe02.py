# Crie uma função que verifique se um número é par ou ímpar.

def VerificarParidade (numero):
    if numero % 2 == 0:
        mensagem = f'O número {numero} é par'
    else:
        mensagem = f'O número {numero} é impar'
    return mensagem

numero = int(input("Informe o número pra verificar a paridade: "))

print(VerificarParidade(numero))