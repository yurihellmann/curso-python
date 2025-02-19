from contextlib import ContextDecorator
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "empresa.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def create_tables(conexao, cursor):
    cursor.execute(
        "CREATE TABLE funcionarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(150), cargo VARCHAR(150), salario FLOAT(15, 2));"
    )
    conexao.commit()


def insert_data(conexao, cursor, nome, cargo, salario):
    data = (nome, cargo, salario)
    cursor.execute(
        "INSERT INTO funcionarios (nome, cargo, salario) VALUES (?,?,?)", data
    )
    conexao.commit()


def retrieve_data(cursor):
    funcionarios = cursor.execute("SELECT * FROM funcionarios ORDER BY nome")
    for funcionario in funcionarios:
        print(dict(funcionario))


def update_data(conexao, cursor, nome, cargo, salario, id):
    data = (nome, cargo, salario, id)
    cursor.execute(
        "UPDATE funcionarios SET nome=?, cargo=?, salario=? WHERE id=?", data
    )
    conexao.commit()


def delete_data(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM funcionarios WHERE id=?", data)
    conexao.commit()


def count_registers(cursor):
    cursor.execute("SELECT id FROM funcionarios")
    funcionarios = [row for row in cursor.fetchall()]

    return len(funcionarios)


def table_join(cursor):
    cursor.execute(
        """
    SELECT funcionarios.nome, departamentos.nome 
    FROM funcionarios
    JOIN departamentos ON funcionarios.departamento_id = departamentos.id
"""
    )
    for row in cursor.fetchall():
        print(list(row))


def create_backup(conexao):
    backup = sqlite3.connect(ROOT_PATH / "empresa-backup.sqlite")
    conexao.backup(backup)
    return f"Backup criado com sucesso"
