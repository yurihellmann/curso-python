# Crie uma tupla com 5 elementos (números ou strings). Acesse e imprima o terceiro elemento.

while True:
    tupla = tuple(input("Informe 5 elementos para a tupla, separados por espaços: \n").split())

    if len(tupla) < 5:
        print("Tamanho da tupla inferior a 5. Tente novamente. \n")
    elif len(tupla) > 5:
        print("Tamanho da tupla superior a 5. Tente novamente. \n")
    else:
        print(f'O terceiro elemento da tupla é {tupla[3]}')