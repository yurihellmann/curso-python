# Desafio: Crie um programa que simule um cadastro de clientes para uma loja. 
# Cada cliente deve ter um nome, idade e uma lista de compras (cada compra será uma tupla com o nome do produto e o preço). 
# Armazene esses clientes em um dicionário, onde a chave será o nome do cliente.
# Crie funções para:
# Adicionar um novo cliente.
# Adicionar compras para um cliente.
# Exibir o total gasto por um cliente.

import textwrap

clientes = {}

def menu():
    menu = """\n
================ MENU ================

[1] Cadastrar novo cliente
[2] Cadastrar compras
[3] Exibir clientes e seus gastos

======================================
=> """
    return input(textwrap.dedent(menu))

def cadastrar_clientes():
    while True:
        nome = str(input("Informe o nome do cliente: ")).capitalize()
        if nome == "":
            mensagem = "Retornando ao menu inicial..."
            break
        elif nome in clientes:
            mensagem = "Cliente já cadastrado!"
            break
        elif nome not in clientes:
            idade = int(input("Informe a idade do cliente: "))
            if idade < 18:
                mensagem = f"O cadastro não é possível pois o cliente {nome} é menor de idade."
                break
            else:
                clientes[nome] = {'Idade': idade, 'Compras' : []}
                print("")
                mensagem = f"Cliente {nome} cadastrado com sucesso!"
                break
    return mensagem

def cadastrar_compras():
    while True:
        nome = str(input("Informe o nome do cliente: ")).capitalize()
        if nome == "":
            mensagem = "Retornando ao menu inicial..."
            break
        elif nome not in clientes:
            mensagem = f"Cliente {nome} não cadastrado! É necessário cadastrar o cliente para atribuir as compras."
            break
        elif nome in clientes:
            produto = str(input("Informe o nome do produto: ")).capitalize()
            preco = float(input(f"Informe o preço de {produto}: R$"))
            compra = (produto, preco)
            clientes[nome]['Compras'].append(compra)
            mensagem = f"{produto} - R${preco:.2f} adicionado ao cliente {nome}."
            break

    return mensagem

def exibir_clientes():
    if not clientes:
        return "Nenhum cliente cadastrado."
    
    for nome, dados in clientes.items():
        total_gasto = sum(preco for _, preco in dados['Compras'])
        print(f"\nCliente: {nome}, Idade: {dados['Idade']} anos")
        print("Compras realizadas:")
        for produto, preco in dados['Compras']:
            print(f"- {produto}: R${preco:.2f}")
        print(f"Total gasto: R${total_gasto:.2f}")
    return ""

def main():
    while True: 
        opcao = menu()

        if opcao == "1":
            print(cadastrar_clientes())
        elif opcao == "2":
            print(cadastrar_compras())
        elif opcao == "3":
            print(exibir_clientes())
        else:
            print("Opção inválida. Tente novamente!")

main()
