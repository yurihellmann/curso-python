# Faça um programa que leia um arquivo e crie um novo arquivo com o conteúdo invertido (linhas de baixo para cima).

file = open("demofile.txt", "r")
s = file.readlines()
file.close()

file = open("newtext.txt", "wb")
s.reverse()

for line in s:
    print(line)
file.close()