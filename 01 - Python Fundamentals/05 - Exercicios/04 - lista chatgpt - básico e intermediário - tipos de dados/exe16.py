# Crie uma função chamada maior_elemento() que receba uma lista de números e retorne o maior número da lista.

def maior_elemento(lista):
    lista.sort()
    maior = max(lista)

    return maior

lista = list(input('Informe os número da lista separados por espaço: ').split())
maior = maior_elemento(lista)

print(f'O maior elemento da lista {lista} é {maior}.')