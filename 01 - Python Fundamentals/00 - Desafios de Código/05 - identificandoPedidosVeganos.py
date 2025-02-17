numPedidos = int(input())

pedido = []

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()
    if ehVegano == "s":
        tipo = "Vegano"
    else:
        tipo = "Nao-vegano"

    pedido.append((prato, tipo, calorias))
    
for i, (prato, tipo, calorias) in enumerate(pedido, start=1):
    print(f"Pedido {i}: {prato} ({tipo}) - {calorias} calorias")