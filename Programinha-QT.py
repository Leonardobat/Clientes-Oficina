# Leitor de Dados
from time import *
import os, sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from pathlib import *

#Aquisição do caminho e pasta dos arquivos finais.
if sys.platform.startswith('linux'):
        caminho = "/home/" + os.getlogin() + "/Documentos/Dados dos clientes"
elif sys.platform.startswith('win'):
        caminho = ("C:\\users\\" + os.getlogin() +
                   "\\Desktop\\Dados dos clientes")

if os.path.isdir(caminho):      #Verifica se já existe a Pasta.
        pass
else:
        os.makedirs(caminho)

class Tabulador(QWidget):
    def __init__(self):  #Inicialização da Janela

        QWidget.__init__(self)
        Font = QFont()
        Font.setBold(True) # deixar os label Negrito

                #Nomes:
        l_nome = QLabel()
        l_nome.setText("Nome:")
        l_nome.setFont(Font)
        l_cpf = QLabel()
        l_cpf.setText("CPF:")
        l_cpf.setFont(Font)
        l_endereco = QLabel()
        l_endereco.setText("Endereço:")
        l_endereco.setFont(Font)
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
        Modelos = ["Corolla", "Hilux", "SW4", "Etios",
                    "Yaris", "RAV4", "Outro"]
        for modelo in Modelos:
                self.c_modelo.addItem(modelo)
                
                #Entradas:
        self.e_nome = QLineEdit("Nome Completo")
        self.e_cpf = QLineEdit("Insira o CPF")
        self.e_endereco = QLineEdit("Endereço Completo")
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
        self.botao = QPushButton("&Salvar")
        self.botao.setShortcut("Ctrl+S")
        self.botao.clicked.connect(self.salvar)

                #Leiaute:
        self.layout = QVBoxLayout()
        self.layout.addWidget(l_nome)
        self.layout.addWidget(self.e_nome)
        self.layout.addWidget(l_cpf)
        self.layout.addWidget(self.e_cpf)
        self.layout.addWidget(l_endereco)
        self.layout.addWidget(self.e_endereco)
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

    @Slot()    
    def salvar(self): #capturas
        n_os = len(os.listdir(caminho)) + 1
        dia = strftime("%d %m %Y")
        nome = self.e_nome.text()
        cpf = self.e_cpf.text()
        endereco = self.e_endereco.text()
        numero = self.e_numero.text()
        placa = self.e_placa.text()
        mod = self.c_modelo.currentText()
        km = self.e_km.text()
        valor = self.e_valor.text()
        servico = self.servico.toPlainText()

                #formataçao de strings
        nome = nome.title()             # Primeira Maiúscula
        placa = placa.upper()           # Todas Maiúsculas
        Info = ("Ordem de Serviço: " + n_os + "\n" + dia + '\nNome: ' + nome +
                '\nCPF: ' + CPF + '\Endereço: ' + endereco +
                '\nTelefone: ' + numero + "\nModelo: " + mod +
                "\nPlaca: "+ placa + "\nQuilometragem: "+ km +
                "\nValor: " + valor + "\nServiço: \n"+ servico)

                #Tela de Pop Up
        popup = QMessageBox(QMessageBox.Question,"Dados",
                            "Tudo Certo?")
        popup.setInformativeText(Info)
        Salvar = popup.addButton(QMessageBox.Ok)
        popup.addButton("Voltar",
                QMessageBox.ButtonRole.RejectRole)
        popup.exec()
        if popup.clickedButton() == Salvar: #salvar
            f = open((caminho + "\\"+  nome + " " +
                     dia+".txt"),"a+")
            f.write(Info)
            f.close()
            self.e_nome = QLineEdit("Nome Completo")
            self.e_cpf = QLineEdit("Insira o CPF")
            self.e_endereco = QLineEdit("Endereço Completo")
            self.e_numero = QLineEdit("Apenas os Números!")
            self.e_placa = QLineEdit("")
            self.e_km = QLineEdit("Apenas os Números!")
            self.e_placa = QLineEdit("")
            self.e_valor = QLineEdit("Total Pago e Devido")
        status.setText("Salvo em: " + caminho + "\\" + nome + " " + dia+".txt")
        
class Buscador(QWidget):
    def __init__(self):

              #Inicialização da Janela
        QWidget.__init__(self)
        Font = QFont()
        Font.setBold(True) # deixar o label Negrito

        #Ações:
        l_nome = QLabel()
        l_nome.setText("Nome Completo:")
        l_nome.setFont(Font)
        self.e_nome = QLineEdit()
        self.b_busca = QPushButton("&Busca")
        self.b_busca.clicked.connect(self.buscar)
        self.b_busca.setShortcut("Ctrl+B")
        self.cb = QButtonGroup()
        self.cb_dia = QCheckBox("Hoje")
        self.cb_dia.setCheckState(Qt.CheckState.Checked)
        self.cb.addButton(self.cb_dia)
        self.cb_mes = QCheckBox("Neste mês")
        self.cb_mes.setCheckState(Qt.CheckState.Checked)
        self.cb.addButton(self.cb_mes)
        self.cb_ano = QCheckBox("Neste Ano")
        self.cb_ano.setCheckState(Qt.CheckState.Unchecked)
        self.cb.addButton(self.cb_ano)
        self.cb_todos = QCheckBox("Todos")
        self.cb_todos.setCheckState(Qt.CheckState.Unchecked)
        self.cb.addButton(self.cb_todos)
        self.lista = QListWidget()
        self.lista.itemDoubleClicked.connect(self.numero)
        
                #Leiaute:
        self.layout = QVBoxLayout()
        self.layout_c = QHBoxLayout()
        self.layout_b = QHBoxLayout()
        self.layout.addWidget(l_nome)
        self.layout.addWidget(self.e_nome)
        self.layout_c.addWidget(self.cb_dia)
        self.layout_b.addWidget(self.cb_mes)
        self.layout_c.addWidget(self.cb_ano)
        self.layout_b.addWidget(self.cb_todos)
        self.layout.addWidget(self.b_busca)
        self.layout.addLayout(self.layout_c)
        self.layout.addLayout(self.layout_b)
        self.layout.addWidget(self.lista)
        self.setLayout(self.layout)

    @Slot()
    def buscar(self):
        self.lista.clear()
        nome_buscado = self.e_nome.text()
        nome_buscado = nome_buscado.title()
        lugar = list(Path(caminho).glob('**/*.txt'))
        # lista todos os txt no caminho em função do tempo
        for k in range(len(lugar)):
                aux = lugar[k].parts[5]
                if self.cb_dia.isChecked():
                    if (nome_buscado == '' and
                        aux[len(aux)-14:len(aux)-12] == strftime("%d")
                        and aux[len(aux)-11:len(aux)-9] == strftime("%m")):
                        if (self.lista.findItems(aux[0:(len(aux)-15)],
                            Qt.MatchFlag.MatchExactly) == []):
                                self.lista.addItem(aux[0:(len(aux)-15)])
                    
                    elif (aux[0:(len(nome_buscado))] == nome_buscado
                          and aux[len(aux)-14:len(aux)-12] == strftime("%d")
                          and aux[len(aux)-11:len(aux)-9] == strftime("%m")):
                        self.lista.addItem(aux[0:(len(aux)-4)])
                   
                elif self.cb_mes.isChecked():
                    if (nome_buscado == '' and
                        aux[len(aux)-11:len(aux)-9] == strftime("%m")):
                        if (self.lista.findItems(aux[0:(len(aux)-15)],
                            Qt.MatchFlag.MatchExactly)== []):
                                self.lista.addItem(aux[0:(len(aux)-15)])
                    
                    elif (aux[0:(len(nome_buscado))] == nome_buscado
                          and aux[len(aux)-11:len(aux)-9] == strftime("%m")):
                        self.lista.addItem(aux[0:(len(aux)-4)])
                        
                elif self.cb_ano.isChecked():
                    if (nome_buscado == '' and
                        aux[len(aux)-8:len(aux)-4] == strftime("%Y")):
                        if (self.lista.findItems(aux[0:(len(aux)-15)],
                            Qt.MatchFlag.MatchExactly)== []):
                                self.lista.addItem(aux[0:(len(aux)-15)])
                    
                    elif (aux[0:(len(nome_buscado))] == nome_buscado
                          and aux[len(aux)-8:len(aux)-4] == strftime("%Y")):
                        self.lista.addItem(aux[0:(len(aux)-4)])
                        
                elif self.cb_todos.isChecked():
                    if nome_buscado == '':
                        self.lista.addItem(aux[0:(len(aux)-15)])
                    
                    elif aux[0:(len(nome_buscado))] == nome_buscado:
                        self.lista.addItem(aux[0:(len(aux)-4)]) 
        del aux
        status.setText("Feito")
        
    @Slot() 
    def numero(self):
        cliente = self.lista.currentItem()
        f = open((caminho + "/" + cliente.text() + ".txt"),"r")
        Info = f.readlines(-1)
        f.close()
        popup = QMessageBox(QMessageBox.Information,"Busca",
                            "Informações:")
        texto = ''
        for k in range(len(Info)):
                texto = texto + Info[k]
        popup.setInformativeText(texto)
        popup.addButton(QMessageBox.Ok)
        popup.exec()
        status.setText("Feito")

class Janelas(QMdiArea):
    def __init__(self): #Inicialização da Janela
        QMdiArea.__init__(self)
        Tab = self.addSubWindow(Tabulador())
        Bus = self.addSubWindow(Buscador())
        Bus.setWindowTitle("Busque por Clientes")
        Tab.setWindowTitle("Insira os Dados")
        self.setViewMode(QMdiArea.TabbedView)
        self.setActiveSubWindow(Tab)
        #self.setDocumentMode(True)
        
class Principal(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tião Automecânica")
        self.setCentralWidget(widget)
        self.menu = QMenuBar()
        self.setMenuBar(self.menu)
        self.sobre = QAction("Sobre", self)
        self.sobre.setShortcut("F1")
        self.menu.addAction(self.sobre)
        self.sobre.triggered.connect(self.info)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        global status
        status = QLabel()
        status.setText("Pronto")
        self.status.addWidget(status)

    @Slot()
    def info(self):
        popup = QMessageBox(QMessageBox.Information,"Sobre",
                            "Informações")
        popup.setInformativeText("""Suite de Apoio \nVersão 0.2
        \nFeito com S2 por Zero \nMIT License""")
        popup.addButton(QMessageBox.Ok)
        popup.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Janelas()
    window = Principal(widget)
    window.resize(500, 600)
    window.show()
    sys.exit(app.exec_())
