def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar a função")
        funcao(*args, **kwargs)
        print("faz algo depois...")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"olá mundo {nome}!")

ola_mundo("Yuri")

