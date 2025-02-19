# Crie uma função que receba um conjunto de números e retorne um conjunto com todos os fatores primos de cada número presente.

def fatores_primos(conjunto):
    fatores_primos = set()

    for numero in conjunto:
        divisor = 2
        while numero > 1:
            while numero % divisor == 0:
                fatores_primos.add(divisor)
                numero //= divisor
            divisor += 1
    return fatores_primos 

conjunto = {24, 36, 48}

print(fatores_primos(conjunto))
