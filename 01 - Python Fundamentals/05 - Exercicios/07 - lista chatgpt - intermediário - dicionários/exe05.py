# Dada uma frase:
# frase = "o gato e o cachorro correram pelo jardim e o gato ganhou"
# Tarefa: Conte a frequência de cada palavra na frase e armazene os resultados em um dicionário, 
# onde as chaves são as palavras e os valores, suas frequências. Ignore a diferença entre maiúsculas e minúsculas.

frase = "o gato e o cachorro correram pelo jardim e o gato ganhou"
palavras = frase.lower().split()

ocorrencias = {}

for palavra in palavras:
        if palavra in ocorrencias:
            ocorrencias[palavra] += 1
        else:
            ocorrencias[palavra] = 1
print(ocorrencias)