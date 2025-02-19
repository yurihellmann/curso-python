# Crie uma função chamada desconto() que receba o preço de um produto e um valor de desconto percentual (com um valor padrão de 10%). 
# A função deve retornar o preço com desconto.

def desconto(preco, desconto):
    valor_desconto = (preco * desconto) / 100

    preco_final = preco - valor_desconto

    mensagem = f'O valor do desconto é de R${valor_desconto:.2f} e o total a pagar é R${preco_final:.2f}'

    return mensagem

preco = float(input("Informe o preço do produto: R$"))
porcentagem_desconto = float(input("Informe a percentual de desconto: "))

print(desconto(preco, porcentagem_desconto))

