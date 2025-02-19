valor1 = int(input("Digite 1 para verdadeiro ou 2 para falso: "))
valor2 = int(input("Digite 1 para verdadeiro ou 2 para falso: "))

if (valor1 == 1):
    valor1 = True
elif (valor1 == 2):
    valor1 = False

if (valor2 == 1):
    valor2 = True
elif (valor2 == 2):
    valor2 = False

if (valor1 == True and valor2 == True):
    mensagem = "Ambos os valores são VERDADEIROS."
elif (valor1 == False and valor2 == False):
    mensagem = "Ambos os valores são FALSOS."
else:
    mensagem = "Os valores são diferentes."

print(mensagem)