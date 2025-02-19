import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?,?)",
        ("Teste 3", "teste3@gmail.coktm"),
    )
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?,?,?)",
        (2, "Teste 4", "teste4@gmail.com"),
    )
    cursor.execute("DELETE FROM clientes WHERE id=13")
    conexao.commit()
except Exception as erro:
    print(f"Ops! Um erro ocorreu! {erro}")
    conexao.rollback()
