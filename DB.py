import os, sys, sqlite3
from pathlib import Path
from getpass import getuser


class clientes_db():

    def __init__(self):
        if sys.platform.startswith('linux'):
            path = Path.home().joinpath('Documentos', 'Oficina', 'Clientes',
                                        'clientes.sqlite')
        elif sys.platform.startswith('win'):
            path = Path.home().joinpath('Documents', 'Oficina', 'Clientes',
                                        'clientes.sqlite')
        self.db = sqlite3.connect(str(path),
                                  detect_types=sqlite3.PARSE_DECLTYPES)
        self.db.row_factory = sqlite3.Row

    def novo_cliente(self, data: dict):
        self.db.execute(
            "INSERT INTO cliente (nome, numero,"
            " cpf, endereco) VALUES (?,?,?,?)",
            (
                data["nome"],
                data["numero"],
                data["cpf"],
                data["endereco"],
            ),
        )
        self.db.commit()

    def busca(self, word: str) -> dict:
        search_word = "%{0}%".format(word)
        info = self.db.execute(
            "SELECT * FROM cliente WHERE nome LIKE ?"
            "OR numero LIKE ? OR cpf LIKE ? ORDER BY id",
            (search_word, search_word, search_word),
        ).fetchall()
        return info

    def get_id(self, word: str) -> dict:
        info = self.db.execute(
            "SELECT id FROM cliente WHERE cpf = ?",
            (word),
        ).fetchone()
        return info['id']


def init_db():

    # Aquisição do caminho
    if sys.platform.startswith('linux'):
        path = Path.home().joinpath('Documentos', 'Oficina', 'Clientes')
        config = Path.home().joinpath('.oficina', 'schema_clientes.sql')
    
    elif sys.platform.startswith('win'):
        path = Path.home().joinpath('Documents', 'Oficina', 'Clientes')
        path = Path.home().joinpath('Documents', 'Oficina',
                                    'schema_clientes.sql')

    # Cria a pasta
    Path.mkdir(path, parents=True, exist_ok=True)
    path_db = path.joinpath('clientes.sqlite')
    db = sqlite3.connect(str(path_db))
    with open(str(config)) as f:
        db.executescript(f.read())
        db.execute("VACUUM")
        db.commit()
        db.close()


if __name__ == "__main__":
    init_db()