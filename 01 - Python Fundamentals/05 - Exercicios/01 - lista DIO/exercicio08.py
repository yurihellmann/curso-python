numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

mensagem = ""

if (numero1 == numero2 or numero1 == numero3 or numero2 == numero3):
    mensagem = "Alguns números são iguais. Digite números diferentes."

if (numero1 > numero2 and numero1 > numero3):
    if(numero2 > numero3):
        mensagem = f"Ordem descrescente dos números: {numero1} - {numero2} - {numero3}"
    else:
        mensagem = f"Ordem descrescente dos números: {numero1} - {numero3} - {numero2}"

if (numero2 > numero1 and numero2 > numero3):
    if(numero1 > numero3):
        mensagem = f"Ordem descrescente dos números: {numero2} - {numero1} - {numero3}"
    else:
        mensagem = f"Ordem descrescente dos números: {numero2} - {numero3} - {numero1}"

if (numero3 > numero1 and numero3 > numero2):
    if(numero2 > numero1):
        mensagem = f"Ordem descrescente dos números: {numero3} - {numero2} - {numero1}"
    else:
        mensagem = f"Ordem descrescente dos números: {numero3} - {numero1} - {numero2}"         

print(mensagem)
