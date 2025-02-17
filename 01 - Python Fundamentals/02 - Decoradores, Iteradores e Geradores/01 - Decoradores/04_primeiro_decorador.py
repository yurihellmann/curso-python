def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar a função")
        funcao()
        print("faz algo depois...")

    return envelope

def ola_mundo():
    print("olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

