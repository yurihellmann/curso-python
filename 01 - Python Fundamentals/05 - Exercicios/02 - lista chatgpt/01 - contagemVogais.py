palavra = input("Digite a palavra para contagem das vogais: ")

vogais = "aeiouAEIOU"

contador = 0

for caractere in palavra:
    if caractere in vogais:
        contador += 1
        mensagem = f"A palavra '{palavra}' possui {contador} vogais"

print(mensagem)