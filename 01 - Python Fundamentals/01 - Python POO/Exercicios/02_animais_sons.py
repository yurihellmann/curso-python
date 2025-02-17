# Crie uma classe base Animal com um método fazer_som(), que imprime "Som genérico de animal".
# Depois, crie as subclasses Cachorro e Gato, sobrescrevendo o método fazer_som() para exibir "Latido" e "Miado", respectivamente.

# Instancie objetos de cada classe e chame o método fazer_som() para cada um.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "Som genérico de animal."
    
class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miado"

cachorro = Cachorro("Luna")

print(cachorro.fazer_som())