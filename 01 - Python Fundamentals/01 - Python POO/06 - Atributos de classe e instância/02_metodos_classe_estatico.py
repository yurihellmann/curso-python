class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return Pessoa(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

# p = Pessoa("Yuri", 25)
# print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1999, 9, 9, "Yuri")
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))