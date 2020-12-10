from PySide2.QtCore import Qt, Slot, Signal
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (
    QAbstractItemView,
    QButtonGroup,
    QCheckBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
from DB import clientes_db


class buscador_clientes(QWidget):
    status_signal = Signal(str)

    def __init__(self):
        self.db = clientes_db()
        QWidget.__init__(self)
        Font = QFont()
        Font.setBold(True)  # Labels em Negrito

        # Entry:
        self.entry_nome = QLineEdit()
        self.entry_nome.setText("Nome para Busca")

        # Botões
        self.button_busca = QPushButton("&Busca")
        self.button_busca.clicked.connect(self.buscar)
        self.button_busca.setShortcut("Ctrl+B")
        self.button_limpar = QPushButton("Limpar")
        self.button_limpar.clicked.connect(self.limpar)
        self.button_limpar.setShortcut("ESC")

        # Tabela
        self.clientes = 0
        self.tabela_clientes = QTableWidget()
        self.tabela_clientes.setColumnCount(4)
        self.tabela_clientes.setHorizontalHeaderLabels([
            "Nome",
            "Número",
            "CPF",
            "Endereço",
        ])
        self.tabela_clientes.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tabela_clientes.horizontalHeader().setStretchLastSection(True)
        self.tabela_clientes.resizeColumnsToContents()
        self.tabela_clientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabela_clientes.itemDoubleClicked.connect(self.info_cliente)

        #Leiaute:
        self.layout = QVBoxLayout()
        self.layout_busca = QHBoxLayout()
        self.layout_busca.addWidget(self.entry_nome)
        self.layout_busca.addWidget(self.button_busca)
        self.layout.addLayout(self.layout_busca)
        self.layout.addWidget(self.tabela_clientes)
        self.setLayout(self.layout)

    @Slot()
    def buscar(self):
        nome_buscado = self.entry_nome.text()
        data = self.db.busca(nome_buscado)
        self.limpar()
        self.status_signal.emit("Feito")
        for cliente in data:
            nome = QTableWidgetItem(cliente['nome'])
            numero = QTableWidgetItem(cliente['numero'])
            cpf = QTableWidgetItem(cliente['cpf'])
            endereco = QTableWidgetItem(cliente['endereco'])
            nome.setTextAlignment(Qt.AlignCenter)
            numero.setTextAlignment(Qt.AlignCenter)
            cpf.setTextAlignment(Qt.AlignCenter)
            endereco.setTextAlignment(Qt.AlignCenter)
            self.tabela_clientes.insertRow(self.clientes)
            self.tabela_clientes.setItem(self.clientes, 0, nome)
            self.tabela_clientes.setItem(self.clientes, 1, numero)
            self.tabela_clientes.setItem(self.clientes, 2, cpf)
            self.tabela_clientes.setItem(self.clientes, 3, endereco)
            self.clientes += 1
        

    @Slot()
    def limpar(self):
        self.tabela_clientes.clearContents()
        self.tabela_clientes.setRowCount(0)
        self.clientes = 0

    @Slot()
    def info_cliente(self):
        pass
