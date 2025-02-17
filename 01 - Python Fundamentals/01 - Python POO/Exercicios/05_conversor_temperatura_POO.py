# Todo: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperaturas:
    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 1.8) + 32

# Entrada do usuário

celsius = float(input())

# Todo: Crie uma instância do conversor:
conversor = ConversorTemperaturas()
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(f"{fahrenheit:.1f}")