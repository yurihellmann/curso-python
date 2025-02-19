numero = int(input("Informe um número para exibir a tabuada: "))

print(f"Exibindo a tabuada de {numero}")
for i in range(11):
    multiplicacao = numero * i
    print(f"{numero} x {i} = {multiplicacao}")