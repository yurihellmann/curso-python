def main():
    print("executando a função principal")

    def funcao_interna():
        print("executando a função interna 1")

    def funcao_2():
        print("executando a função interna 2")

    funcao_interna()
    funcao_2()

main()