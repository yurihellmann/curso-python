# Dada uma lista de números [10, 15, 20, 25, 30, 35, 40, 45, 50], 
# crie uma função que retorne uma nova lista contendo apenas os números que são divisíveis por 5, usando filter ou list comprehension.

lista_filtrada = []

def filtra_numeros():
    lista = list(map(int, input("Informe os números separados por espaço: ").split()))
    lista_filtrada = [n for n in lista if n % 5 == 0]
    print(f'A lista com todos os números divisíveis por 5 é: {lista_filtrada}')

filtra_numeros()