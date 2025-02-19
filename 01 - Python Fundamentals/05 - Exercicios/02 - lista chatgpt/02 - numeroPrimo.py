numero = int(input("Informe um número: "))

if numero < 2:
    mensagem = f"O número {numero} é menor que 2. Números menores que 2 não são primos."
else:
    eh_primo = True
    
if numero == 2:
    eh_primo = True
elif numero % 2 == 0:
    eh_primo = False
else:
    for i in range (3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            mensagem = f"O número {numero} é um número primo."
            break

if eh_primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")