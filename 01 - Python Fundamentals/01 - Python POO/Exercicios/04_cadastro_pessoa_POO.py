class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Todo: Crie um método para retornar as informações formatas com Nome e Idade:    
    def __str__(self):
        return (f"Nome: {self.nome}, Idade: {self.idade}")

# Entrada do usuário
nome = input()
idade = int(input())

# Todo: Crie uma instância da pessoa:
pessoa = Pessoa(nome, idade)

#Todo: Chame o método para retornar as informações formatadas e imprima o resultado:
print(pessoa)