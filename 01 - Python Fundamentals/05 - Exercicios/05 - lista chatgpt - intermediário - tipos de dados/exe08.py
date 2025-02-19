# Suponha que você tenha dois conjuntos representando pessoas que gostam de diferentes frutas:
# frutas_A = {"maçã", "banana", "laranja"}
# frutas_B = {"laranja", "uva", "morango"}
# Crie uma função que retorne:
# A união de ambos os conjuntos (todas as frutas).
# A interseção de ambos os conjuntos (frutas comuns).

def uniao(frutas_A, frutas_B):
    uniao = frutas_A.union(frutas_B)

    return set(sorted(uniao))

def intersecao(frutas_A, frutas_B):
    intersecao = frutas_A.intersection(frutas_B)

    return intersecao

frutas_A = {"maçã", "banana", "laranja"}
frutas_B = {"laranja", "uva", "morango"}

print(f'União: {uniao(frutas_A, frutas_B)} \nInterseção: {intersecao(frutas_A, frutas_B)}')