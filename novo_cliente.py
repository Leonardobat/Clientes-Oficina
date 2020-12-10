from PySide2.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)
from PySide2.QtGui import QFont
from PySide2.QtCore import Slot, Signal
from DB import clientes_db


class novo_cliente(QWidget):
    status_signal = Signal(str)

    def __init__(self):
        self.db = clientes_db()
        QWidget.__init__(self)
        Font = QFont()
        Font.setBold(True)  # Labels em Negrito

        # Labels:
        self.label_title = QLabel("Novo Cliente")
        self.label_title.setFont(Font)
        self.label_nome = QLabel("Nome Completo:")
        self.label_nome.setFont(Font)
        self.label_endereco = QLabel("Endereço:")
        self.label_endereco.setFont(Font)
        self.label_numero = QLabel("Número:")
        self.label_numero.setFont(Font)
        self.label_cpf = QLabel("CPF:")
        self.label_cpf.setFont(Font)

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