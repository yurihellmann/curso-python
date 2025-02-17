arquivo = open(
    r"C:\Users\yuri\Documents\Cursos\05 - Python\03 - Manipulação de arquivos\lorem.txt", "r"
)
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# tip
# while len(linha := arquivo.readline()):
#     print(linha)

arquivo.close()