import os, sys, sqlite3
from pathlib import Path
from getpass import getuser


class ClientesDB():

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
        path = Path.home().joinpath('Documentos', 'Oficina', 'Clientes',
                                    'clientes.sqlite')
        configPath = Path.home().joinpath('.config', 'oficina',
                                          'schema_clientes.sql')

    elif sys.platform.startswith('win'):
        path = Path.home().joinpath('Documents', 'Oficina', 'Clientes',
                                    'clientes.sqlite')
        configPath = Path.home().joinpath('Documents', 'Oficina',
                                          'schema_clientes.sql')

    # Cria a pasta
    if not Path.is_file(configPath):
        raise NameError('No Config was Found')

    if not Path.is_file(path):
        Path.mkdir(path, parents=True, exist_ok=True)
        db = sqlite3.connect(path)
        with Path.open(configPath) as f:
            db.executescript(f.read())
            db.execute("VACUUM")
            db.commit()
            db.close()


if __name__ == "__main__":
    init_db()