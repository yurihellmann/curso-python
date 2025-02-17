valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

precoFinal = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)
troco = valorPago - precoFinal

mensagem = f'O preço final do pedido é de R$ {precoFinal:.2f}. Seu troco é de R$ {troco:.2f}'
print(mensagem)