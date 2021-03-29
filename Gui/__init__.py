from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QAbstractItemView,
    QButtonGroup,
    QCheckBox,
    QFrame,
    QLabel,
    QHBoxLayout,
    QHeaderView,
    QLineEdit,
    QListWidget,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from DB import ClientesDB


class Buscador(QWidget):
    status_signal = Signal(str)

    def __init__(self):
        self.db = ClientesDB()
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


class NovoCliente(QWidget):
    status_signal = Signal(str)

    def __init__(self):
        self.db = ClientesDB()
        QWidget.__init__(self)
        font = QFont()
        font.setBold(True)  # Labels em Negrito

        # Labels:
        self.label_title = QLabel("Novo Cliente")
        self.label_title.setFont(font)
        self.label_nome = QLabel("Nome Completo:")
        self.label_nome.setFont(font)
        self.label_endereco = QLabel("Endereço:")
        self.label_endereco.setFont(font)
        self.label_numero = QLabel("Número:")
        self.label_numero.setFont(font)
        self.label_cpf = QLabel("CPF:")
        self.label_cpf.setFont(font)

        # Entries:
        self.entry_nome = QLineEdit()
        self.entry_endereco = QTextEdit()
        self.entry_numero = QLineEdit()
        self.entry_cpf = QLineEdit()

        # Botões;
        self.button_salvar = QPushButton("&Salvar")
        self.button_salvar.clicked.connect(self.salvar_cliente)
        self.button_salvar.setShortcut("Ctrl+S")
        self.button_cancelar = QPushButton("Cancelar")
        self.button_cancelar.clicked.connect(self.cancelar)
        self.button_cancelar.setShortcut("ESC")

        # Linha
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(1)

        # Leiaute:
        self.layout = QVBoxLayout()
        self.layout_buttons = QHBoxLayout()
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.entry_nome)
        self.layout.addWidget(self.label_numero)
        self.layout.addWidget(self.entry_numero)
        self.layout.addWidget(self.label_cpf)
        self.layout.addWidget(self.entry_cpf)
        self.layout.addWidget(self.label_endereco)
        self.layout.addWidget(self.entry_endereco)
        self.layout_buttons.addWidget(self.button_salvar)
        self.layout_buttons.addWidget(self.button_cancelar)
        self.layout.addStretch(2)
        self.layout.addLayout(self.layout_buttons)
        self.setLayout(self.layout)

    @Slot()
    def salvar_cliente(self):
        nome = self.entry_nome.text()
        cpf = self.entry_cpf.text()
        numero = self.entry_numero.text()
        endereco = self.entry_endereco.toPlainText()
        data = {
            'nome': nome,
            'cpf': cpf,
            'numero': numero,
            'endereco': endereco
        }
        self.db.novo_cliente(data)
        self.status_signal.emit("Salvo")
        self.cancelar()

    @Slot()
    def cancelar(self):
        self.entry_nome.setText('')
        self.entry_endereco.setText('')
        self.entry_numero.setText('')
        self.entry_cpf.setText('')