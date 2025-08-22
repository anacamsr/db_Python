import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "banco.sqlite")
# Abre (ou cria, se não existir) o arquivo de banco 'banco.sqlite' na pasta do script.
# Retorna um objeto Connection que gerencia a transação.

cursor = conexao.cursor()
# Cria um cursor para enviar comandos SQL (execute/executescript) e ler resultados (fetchone/fetchall).

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR (100), email VARCHAR(150))"
    )
    conexao.commit() 
# Executa um comando DDL que cria a tabela 'clientes'

def insert_registro(conexao, cursor, nome, email): 
    data = (nome, email)
    cursor.execute(f"INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()  
    
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()
    
def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=? ;", data)
    conexao.commit()
    
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados) #Executemany serve para executar a mesma instrução várias vezes de forma eficiente
    conexao.commit()


dados = [
    ("Carolina", "carolina@gmail.com"),
    ("Bono", "bono@gmail.com"),
    ("Ana2", "ana2@gmail.com")
]
    
# atualizar_registro(conexao, cursor, 'Ana Atual', 'ana.a@gmail.com', 1)
# excluir_registro(conexao, cursor, 1)
inserir_muitos(conexao, cursor, dados)