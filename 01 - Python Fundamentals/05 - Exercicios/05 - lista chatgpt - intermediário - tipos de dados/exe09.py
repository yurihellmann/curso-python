# Dado o dicionário:
# notas = {"Ana": 8.5, "João": 7.0, "Pedro": 9.0, "Maria": 6.5}
# Crie uma função que retorne uma lista de tuplas com os nomes e suas respectivas notas, ordenada pela nota (do menor para o maior).

def ordenar_notas(dicionario):
    return sorted(dicionario.items(), key=lambda x: x[1])

notas = {"Ana": 8.5, "João": 7.0, "Pedro": 9.0, "Maria": 6.5}
resultado = ordenar_notas(notas)
print(resultado)
