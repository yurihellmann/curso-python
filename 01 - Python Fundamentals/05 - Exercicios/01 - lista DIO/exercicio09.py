peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** altura)

if (imc < 18.5):
    mensagem = f"Seu IMC é de {imc:.2f} e você está abaixo do peso ideal."
elif (imc >= 18.6 and imc <= 24.9):
    mensagem = f"Seu IMC é de {imc:.2f} e você está no seu peso ideal. Parabéns!"
elif (imc >= 25 and imc <= 29.9):
    mensagem = f"Seu IMC é de {imc:.2f} e você está levemente acima do peso."
elif (imc >= 30 and imc <= 34.9):
    mensagem = f"Seu IMC é de {imc:.2f} e você está com obesidade grau I."
elif (imc >= 35 and imc <= 39.9):
    mensagem = f"Seu IMC é de {imc:.2f} e você está com obesidade grau II(severa)."
elif (imc >= 40):
    mensagem = f"Seu IMC é de {imc:.2f} e você está com obesidade grau III (mórbida)."

print(mensagem)