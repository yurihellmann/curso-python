# Escreva uma função que receba dois conjuntos de números inteiros e retorne True se todos os elementos do 
# primeiro conjunto forem múltiplos de pelo menos um elemento do segundo conjunto.

def multiplos_no_conjunto(conjunto1, conjunto2):
    for numero1 in conjunto1:
        for numero2 in conjunto2:
            if numero1 % numero2 == 0:
                return True
            else:
                return False

conjunto1 = {2, 4, 6, 8}
conjunto2 = {2, 3}

print(multiplos_no_conjunto(conjunto1, conjunto2))