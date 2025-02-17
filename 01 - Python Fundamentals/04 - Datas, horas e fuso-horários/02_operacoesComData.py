from datetime import datetime, timedelta, date, time

tipo_carro = 'P'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(data_estimada)
elif tipo_carro == 'M':
    print(data_atual)
else:
    print(data_atual)

print(date.today() - timedelta(days=1))
resultado = datetime(2024, 1, 23, 11, 56, 30)  - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())