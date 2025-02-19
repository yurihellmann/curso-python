# Recebe a entrada e armazena na variável "entrada"
entrada = "09-09-1999;17-05-2003"


# Função responsável por receber as datas e transformar cada data para o formato "YYYY/MM/DD"
def transformar_datas(datas):
    # Divide a string de entrada nas datas individuais
    datas_lista = datas.split(";")

    datas_transformadas = []

    # TODO: Implemente a lógica necessária para formatar as datas
    for data in datas_lista:
        dia, mes, ano = data.split("-")
        nova_data = f"{ano}/{mes}/{dia}"
        datas_transformadas.append(nova_data)

    return datas_transformadas


# Imprime a lista de datas formatadas
print(transformar_datas(entrada))
