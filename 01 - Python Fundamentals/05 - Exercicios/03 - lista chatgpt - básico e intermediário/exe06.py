# Verifique se uma string é um palíndromo (lida da mesma forma de trás para frente).

def VerificaPalindromo (string):
    palindromo = string[::-1]
    print(palindromo)

    if palindromo == string:
        mensagem = f'A string {string} é um palíndromo'
        return mensagem
    else:
        mensagem = f'A string {string} não é um palíndromo'
        return mensagem

string = str(input("Informe a string para verificar se é um palíndromo: "))

print(VerificaPalindromo(string))

