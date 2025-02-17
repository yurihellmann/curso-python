from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open('meu_arquivo.py')
except FileNotFoundError as exc:
    print("Arquivo não encontrado.")
    print(exc)

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except Exception as exc:
    print("Não foi possível abrir o arquivo")
    print(exc)