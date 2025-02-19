# Suponha que você tenha uma tupla representando temperaturas diárias de uma semana, como (25, 27, 23, 30, 28, 26, 24). 
# Crie uma função que receba essa tupla e retorne:
# A temperatura máxima e mínima da semana.
# A média de temperatura.

def temperatura_max_min_media():
    while True:
        temperaturas = input("Informe as temperaturas da semana, separadas por espaço: ")
        temperaturas = tuple(map(int, temperaturas.split()))
        if len(temperaturas) != 7:
            print("Quantidade de temperaturas maior ou menor que 7!")
        else:
            temperaturas = list(temperaturas)
            maior_temperatura = max(temperaturas)
            menor_temperatura = min(temperaturas)
            media_temperaturas = (sum(temperaturas)) / len(temperaturas)
            print(f'A maior temperatura da semana foi {maior_temperatura}° e a menor foi {menor_temperatura}°. A média da semana foi de {media_temperaturas:.2f}°.')

temperatura_max_min_media()

