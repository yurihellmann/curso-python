def mensagem(nome):
    print(f'executando nome')
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, 'Yuri'))
print(executar(mensagem_longa, 'Yuri'))