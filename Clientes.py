# Leitor de Dados
import sys
from DB import init_db
from Gui import Buscador, NovoCliente
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QStatusBar,
    QWidget,
)

class Principal(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.inicializar_db()
        self.setWindowTitle("Tião Automecânica - Clientes")
        self.widget = QWidget()

        # Janelas
        w1, w2 = Buscador(), NovoCliente()
        w1.status_signal.connect(self.atualizar_status)
        w2.status_signal.connect(self.atualizar_status)

        # Leiaute
        self.line = QFrame()
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(1)
        self.layout = QGridLayout()
        self.layout.addWidget(w1, 0, 0, 1, 1)
        self.layout.addWidget(self.line, 0, 1, 1, 1)
        self.layout.addWidget(w2, 0, 1, 1, 2)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Menu
        self.menu = QMenuBar()
        self.setMenuBar(self.menu)
        self.sobre = QAction("Sobre", self)
        self.sobre.setShortcut("F1")
        self.menu.addAction(self.sobre)
        self.sobre.triggered.connect(self.info)

        # Status
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status_label = QLabel("Pronto")
        self.status.addWidget(self.status_label)

    @Slot()
    def info(self):
        self.popup = QMessageBox(QMessageBox.Information, "Sobre",
                                 "Informações")
        self.popup.setInformativeText("""Clientes \nVersão 0.5
        \nFeito com S2 por Zero \nMIT License""")
        self.popup.addButton(QMessageBox.Ok)
        self.popup.exec()

    @Slot()
    def atualizar_status(self, msg: str):
        self.status_label.setText(msg)

    @staticmethod
    def inicializar_db():
        try:
            init_db()
        except NameError:
            popup = QMessageBox(QMessageBox.Critical, "Erro",
                                 "Erro")
            popup.setInformativeText("Arquivo de configuração não foi encontrado")
            popup.addButton(QMessageBox.Ok)
            popup.exec()
            exit(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.showMaximized()
    sys.exit(app.exec_())