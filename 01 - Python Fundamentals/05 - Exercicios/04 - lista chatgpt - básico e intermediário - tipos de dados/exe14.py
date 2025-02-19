# Crie uma função chamada soma_quadrados() que receba dois números, calcule o quadrado de cada um e retorne a soma desses quadrados.

def soma_quadrados(n1, n2):
    quadrado1 = n1**2
    quadrado2 = n2**2
    soma = quadrado1 + quadrado2

    return soma

print(soma_quadrados(4, 5))