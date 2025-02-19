# Faça um programa que receba uma string e exiba a string invertida.

def InverterString (string):
    string_invertida = string[::-1]
    return string_invertida

string = str(input("Informe a string a ser invertida: "))

print(InverterString(string))