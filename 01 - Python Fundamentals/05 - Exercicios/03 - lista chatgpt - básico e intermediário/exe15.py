# Crie uma função que receba um número e retorne a sequência de Fibonacci até esse número.

def Fibonacci (numero):
    sequencia = []
    a, b = 0, 1

    while a <= numero:
        sequencia.append(a)
        a,b = b, a + b

    return sequencia

numero = int(input("Informe um número para retornar a sequência de Fibonacci: "))

print(Fibonacci(numero))

        

