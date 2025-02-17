arquivo = open(
    r"C:\Users\yuri\Documents\Cursos\05 - Python\03 - Manipulação de arquivos\dados.txt", "w"
)

numeros = input().split(" ")

for numero in numeros:
    arquivo.writelines(numero)