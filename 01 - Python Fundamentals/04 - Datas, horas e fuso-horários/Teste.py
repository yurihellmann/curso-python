def countdown(n): 
    while n > 0: 
        yield n -= 1

lista = list(countdown(3))
print(lista)