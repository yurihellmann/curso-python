A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma = A + B
mensagem = f"A soma de A e B é {soma}. "

if soma < C:
    mensagem = mensagem + "A soma é menor que C."
else:
    mensagem = mensagem + "A soma é maior que C."

print(mensagem)

