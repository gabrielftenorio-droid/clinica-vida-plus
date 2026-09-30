import sqlite3


def criar_conexao():
    conexao = sqlite3.connect("clinica_vida_plus.db")
    return conexao


def criar_tabelas():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


criar_tabelas()