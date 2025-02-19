# Dada a lista de strings ["banana", "maçã", "laranja", "uva", "melão"], faça as seguintes operações:
# Ordene a lista em ordem alfabética reversa.
# Substitua a palavra "laranja" por "manga".
# Inverta a lista.

frutas = ["banana", "maçã", "laranja", "uva", "melão"]

frutas.sort(reverse = True)
print(frutas)

frutas.insert(frutas.index("laranja"), "manga")
frutas.pop(frutas.index("laranja"))
print(frutas)

frutas.reverse()
print(frutas)

