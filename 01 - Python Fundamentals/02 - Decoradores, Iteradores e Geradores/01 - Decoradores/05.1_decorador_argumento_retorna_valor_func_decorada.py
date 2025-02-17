def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar a função")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois...")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"olá mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("yuri")
print(resultado)
