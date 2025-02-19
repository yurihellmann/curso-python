numero = int(input("Digite o seu número: "))

if (numero % 2 == 0):
    paridade = "par"
else:
    paridade = "impar"

if (numero > 0):
    sinal = "positivo"
else:
    sinal = "negativo"

if (paridade == "par" and sinal == "positivo"):
    mensagem = f"O número {numero:.0f} é {paridade} e {sinal}"
elif (paridade == "par" and sinal == "negativo"):
    mensagem = f"O número {numero:.0f} é {paridade} e {sinal}"
elif (paridade == "impar" and sinal == "positivo"):
    mensagem = f"O número {numero:.0f} é {paridade} e {sinal}"
elif (paridade == "impar" and sinal == "negativo"):
    mensagem = f"O número {numero:.0f} é {paridade} e {sinal}"
else:
    mensagem = "Número inválido"

print(mensagem)

