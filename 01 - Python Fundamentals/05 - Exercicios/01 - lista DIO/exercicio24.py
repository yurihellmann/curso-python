distancia = float(input("Informe a distância total da viagem (Km): "))
tempoViagem = float(input("Informe o tempo total da viagem (H): "))
autonomia = 12

velocidadeMedia = distancia / tempoViagem
litrosUsados = distancia / autonomia
mensagem = f"A distância total percorrida é de {distancia:.0f}Km, com uma velocidade média de {velocidadeMedia:.0f}Km/h e um total de combustível gasto de {litrosUsados:.2f}L"

print(mensagem)

