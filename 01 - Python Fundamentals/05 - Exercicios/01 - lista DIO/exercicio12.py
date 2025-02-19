valorProduto = float(input("Digite o valor do produto: "))
formaDePagamento = int(input("Selecione a forma de pagemento - (1) Dinheiro ou Pix (2) Cartão de Crédito: "))

if(formaDePagamento == 1):
    valorDesconto = (valorProduto * 15) / 100
    valorFinal = valorProduto - valorDesconto
    mensagem = f"O total a pagar é R${valorFinal}"
elif (formaDePagamento == 2):
    quantidadeParcelas = int(input("Informe a quantidade de parcelas para a sua compra: "))
    if (quantidadeParcelas == 1):
        valorDesconto = (valorProduto * 10) / 100
        valorFinal = valorProduto - valorDesconto
        mensagem = f"O total a pagar é R${valorFinal}"
    elif (quantidadeParcelas == 2):
        mensagem = f"O total a pagar é R${valorProduto}"
    else:
        valorJuros = (valorProduto * 10) / 100
        valorFinal = valorProduto + valorJuros
        mensagem = f"O total a pagar é R${valorFinal}"
else:
    mensagem = "Valor ou forma de pagamento é inválido. Tente novamente!"

print(mensagem)



