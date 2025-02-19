a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if (a == b):
    c = a + b
    mensagem = f"A soma dos números {a} + {b} = {c}"
else:
    c = a * b
    mensagem = f"A multiplicação dos números {a} * {b} = {c}"

print(mensagem)