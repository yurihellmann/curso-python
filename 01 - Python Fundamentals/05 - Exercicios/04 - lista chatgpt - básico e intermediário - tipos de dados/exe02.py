# Modifique a tupla para adicionar um novo elemento (como tuplas são imutáveis, pense em uma forma de fazer isso).

while True:
    tupla = tuple(input("Informe os elementos da tupla: ").split())
    opcao = str(input("Deseja adicionar mais elementos a tupla? S ou N: ").capitalize())

    if opcao == "S":
        itens_adicionais = list(input("Informe os itens para adicionar a tupla: ").split())
        lista_tupla = list(tupla)
        lista_tupla.extend(itens_adicionais)
        tupla_atualizada = tuple(lista_tupla)
        print(tupla_atualizada)
        break
    else:
        print(tupla)
        break
    