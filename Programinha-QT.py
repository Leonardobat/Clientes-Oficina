# Leitor de Dados
from time import *
import os, sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

#Aquisição do caminho e pasta dos arquivos finais.
if sys.platform.startswith('linux'):
        caminho = "/home/" + os.getlogin() + "/Documentos/Dados dos clientes"
elif sys.platform.startswith('win'):
        caminho = ("C:\\users\\" + os.getlogin() +
                   "\\Área de Trabalho\\Dados dos clientes")

if os.path.isdir(caminho):      #Verifica se já existe a Pasta.
        pass
else:
        os.makedirs(caminho)


class Widget(QWidget):
    def __init__(self):

              #Inicialização da Janela
        QWidget.__init__(self)
        Font = QFont()
        Font.setBold(True) # deixar os label Negrito

                #Nomes:
        l_nome = QLabel()
        l_nome.setText("Nome:")
        l_nome.setFont(Font)
        l_numero = QLabel()
        l_numero.setText("Telefone:")
        l_numero.setFont(Font)
        l_placa = QLabel()
        l_placa.setText("Placa:")
        l_placa.setFont(Font)
        l_km = QLabel()
        l_km.setText("Quilometragem:")
        l_km.setFont(Font)
        l_modelo = QLabel()
        l_modelo.setText("Modelo:")
        l_modelo.setFont(Font)
        l_servico = QLabel()
        l_servico.setText("Serviço:")
        l_servico.setFont(Font)
        l_valor = QLabel()
        l_valor.setText("Valor:")
        l_valor.setFont(Font)

                #Lista de Modelos e Combo:
        self.c_modelo = QComboBox()
        Modelos = ["Corolla", "Hilux", "SW4", "Etios", "Outro"]
        for modelo in Modelos:
                self.c_modelo.addItem(modelo)
                
                #Entradas:
        self.e_nome = QLineEdit("Nome Completo")
        self.e_numero = QLineEdit("Apenas os Números!")
        self.e_placa = QLineEdit()
        self.e_km = QLineEdit("Apenas os Números!")
        self.e_placa = QLineEdit()
        self.e_valor = QLineEdit("Total Pago e Devido")

                #Entrada de Texto:
        self.servico = QTextEdit()
        self.e_servico = self.servico.toPlainText() #buffer do texto
        self.servico.setPlainText("Comente o que foi feito")

                #Botão:
        self.botao = QPushButton("Salvar")
        self.botao.clicked.connect(self.salvar)

                #Leiaute:
        self.layout = QVBoxLayout()
        self.layout.addWidget(l_nome)
        self.layout.addWidget(self.e_nome)
        self.layout.addWidget(l_numero)
        self.layout.addWidget(self.e_numero)
        self.layout.addWidget(l_modelo)
        self.layout.addWidget(self.c_modelo)
        self.layout.addWidget(l_placa)
        self.layout.addWidget(self.e_placa)
        self.layout.addWidget(l_km)
        self.layout.addWidget(self.e_km)  
        self.layout.addWidget(l_valor)
        self.layout.addWidget(self.e_valor)
        self.layout.addWidget(l_servico)
        self.layout.addWidget(self.servico)
        self.layout.addWidget(self.botao)
        self.setLayout(self.layout)

    def salvar(self):
                #capturas
        nome = self.e_nome.text()
        numero = self.e_numero.text()
        placa = self.e_placa.text()
        mod = self.c_modelo.currentText()
        km = self.e_km.text()
        valor = self.e_valor.text()
        servico = self.servico.toPlainText()
                #formataçao de strings
        nome = nome.title()             # Primeira Maiúscula
        placa = placa.upper()           # Todas Maiúsculas
        Info = ("\n" + strftime("%d/%m/%Y") + '\nNome: ' + nome +
                '.\nTelefone: ' + numero + "\nModelo: " + mod +
                "\nPlaca: "+ placa + "\nQuilometragem: "+ km +
                "\nValor: " + valor + "\nServico: \n"+ servico)

                #Tela de Pop Up
        popup = QMessageBox(QMessageBox.Question,"Olá",
                            "Tudo Certo?")
        popup.setInformativeText(Info)
        Salvar = popup.addButton(QMessageBox.Ok)
        popup.addButton("Voltar",
                QMessageBox.ButtonRole.RejectRole)
        popup.exec()
        if popup.clickedButton() == Salvar: #salvar
            f = open((caminho + "/"+  nome + " " +
                     strftime("%d %m %Y")),"a+")
            f.write(Info)
            f.close()

class Janela(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Teste")
        self.setCentralWidget(widget)

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = Janela(widget)
    window.resize(800, 600)
    window.show()
    # Execute application
    sys.exit(app.exec_())

