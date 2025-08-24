import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    # Inserindo registros
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)",
        ("Teste 3", "teste3@gmail.com")
    )
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)",
        (2, "Teste 4", "teste3@gmail.com")
    )
    cursor.execute(
        "DELETE FROM clientes WHERE id = 3",
    )

    # Confirma as operações
    conexao.commit()

except Exception as exc:
    # Em caso de erro, desfaz todas as operações
    print(f"Ops! Um erro ocorreu! {exc}")
    conexao.rollback()
