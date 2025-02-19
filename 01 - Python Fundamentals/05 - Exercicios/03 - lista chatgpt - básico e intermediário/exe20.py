# Crie um programa que leia um arquivo texto e conte o número de palavras.

f = open("demofile.txt", "r")

num_words = 0

for line in f:
    words = line.split()
    num_words += len(words)

print(f'Número de palavras: {num_words}')