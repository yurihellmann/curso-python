# Crie uma classe Pessoa com os atributos nome e idade. Depois, crie uma subclasse Funcionario, que herda de Pessoa e adiciona os atributos cargo e salario.

# Implemente um método mostrar_detalhes() que exiba todas as informações do funcionário.
# Instancie um objeto da classe Funcionario e exiba seus detalhes.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_detalhes(self):
        return f"Nome: {self.nome} - Idade: {self.idade}"
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        self.cargo = cargo
        self.salario = salario
        super().__init__(nome, idade)

    def mostrar_detalhes(self):
        detalhes_pessoa = super().mostrar_detalhes()
        return f"{detalhes_pessoa} - Cargo: {self.cargo} - Salário: R${self.salario:.2f}"

novo_funcionario = Funcionario("Yuri", 25, "Analista de TI", 3200)
print(novo_funcionario.mostrar_detalhes())