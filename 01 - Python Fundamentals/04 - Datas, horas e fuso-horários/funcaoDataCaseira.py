def data(dia, mes, ano):
    if dia > 31 or mes > 12:
        mensagem = "Dia ou mês inválidos"
    else:
        mensagem = f"{dia}/{mes}/{ano}"

    return mensagem

data = data(32, 1, 2025)
print(data)