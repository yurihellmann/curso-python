valorAula = float(input("Informe o valor da hora/aula: "))
aulasNoMes = int(input("Informe a quantidade de aulas lecionadas no mês: "))
inss = float(input("Informe o percentual de desconto do INSS: "))

salarioBruto = valorAula * aulasNoMes
descontoINSS = (salarioBruto * inss) / 100

salarioLiquido = salarioBruto - descontoINSS
mensagem = f"O valor liquido do salário é de R${salarioLiquido:.2f}"

print(mensagem)