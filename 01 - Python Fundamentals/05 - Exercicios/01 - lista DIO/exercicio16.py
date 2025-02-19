a = float(input("Digite o valor do primeiro lado do triângulo: "))
b = float(input("Digite o valor do segundo lado do triângulo: "))
c = float(input("Digite o valor do terceiro lado do triângulo: "))

if ((a + b) > c and (a + c) > b and (b + c) > a):
    if (a == b and b == c):
        tipoTriangulo = "Equilátero"
        mensagem = f"O tipo do triângulo é {tipoTriangulo}"
    elif (a == b and b != c):
        tipoTriangulo = "Isósceles"
        mensagem = f"O tipo do triângulo é {tipoTriangulo}"
    elif (a == c and b != c):
        tipoTriangulo = "Isósceles"
        mensagem = f"O tipo do triângulo é {tipoTriangulo}"
    elif (b == c and a != c):
        tipoTriangulo = "Isósceles"
        mensagem = f"O tipo do triângulo é {tipoTriangulo}"
    else:
        tipoTriangulo = "Escaleno"
        mensagem = f"O tipo do triângulo é {tipoTriangulo}"

print(mensagem)