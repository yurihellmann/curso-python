class Ave:
    def voar(self):
        print("Voando...")

class Pardal(Ave):
    def voar(self):
        super().voar()

class Avestruz(Ave):
    def voar(self):
        print("Avestruz não voa!")

class Aviao(Ave):
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar()

a1 = Pardal()
a2 = Avestruz()

plano_voo(a1)
plano_voo(a2)
plano_voo(Aviao())