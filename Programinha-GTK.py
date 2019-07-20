# Leitor de Dados
from time import *
import gi, os, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Aquisição do caminho e pasta dos arquivos finais.
if sys.platform.startswith('linux'):
        caminho = "/home/" + os.getlogin() + "/Documentos/Dados dos clientes"
elif sys.platform.startswith('win'):
        caminho = ("C:\\users\\" + os.getlogin() +
                   "\\Área de Trabalho\\Dados dos clientes")

if os.path.isdir(caminho):
        pass
else:
        os.makedirs(caminho)


class Janela(Gtk.Window):
        def __init__(self):
                #Inicialização da Janela
                Gtk.Window.__init__(self, title="Dados")
                self.set_default_size(400, 600)
                bar_t = Gtk.HeaderBar(title="Tabelador de Dados")
                bar_t.set_show_close_button(True)
                bar_t.set_subtitle("Tião Auto Mecânica")
                self.set_titlebar(bar_t)
                grid = Gtk.Grid()
                self.add(grid)
                
                #Nomes:
                l_nome = Gtk.Label()
                l_nome.set_markup("<b>Nome:</b>")
                l_numero = Gtk.Label()
                l_numero.set_markup("<b>Telefone:</b>")
                l_placa = Gtk.Label()
                l_placa.set_markup("<b>Placa:</b>")
                l_km = Gtk.Label()
                l_km.set_markup("<b>Quilometragem:</b>")
                l_modelo = Gtk.Label()
                l_modelo.set_markup("<b>Modelo:</b>")
                l_servico = Gtk.Label()
                l_servico.set_markup("<b>Serviço:</b>")
                l_valor = Gtk.Label()
                l_valor.set_markup("<b>Valor:</b>")
                #Lista de Modelos e Combo:
                self.c_modelo = Gtk.ComboBoxText.new()
                Modelos = ["Corolla", "Hilux", "SW4", "Etios", "Outro"]
                for modelo in Modelos:
                    self.c_modelo.append_text(modelo)
                
                #Entradas:
                self.e_nome = Gtk.Entry()
                self.e_nome.set_text("Nome Completo")
                self.e_numero = Gtk.Entry()
                self.e_numero.set_text("Apenas os Números!")
                self.e_placa = Gtk.Entry()
                self.e_km = Gtk.Entry()
                self.e_km.set_text("Apenas os Números!")
                self.e_placa = Gtk.Entry()
                self.e_valor = Gtk.Entry()
                self.e_valor.set_text("Total Pago e Devido")
                #Entrada de Texto:
                self.scroll = Gtk.ScrolledWindow() # Scroll do texto
                self.scroll.set_hexpand(True)
                self.scroll.set_vexpand(True)
                self.servico = Gtk.TextView()
                self.e_servico = self.servico.get_buffer() #buffer do texto
                self.e_servico.set_text("Comente o que foi feito")
                self.scroll.add(self.servico)
                #Botão:
                self.botao = Gtk.Button(label="Salvar")
                self.botao.connect("clicked", self.salvar)
                #Leiaute:
                grid.attach(l_nome, 1, 0, 1, 1)
                grid.attach_next_to(self.e_nome, l_nome, Gtk.PositionType.BOTTOM, 1, 1)
                grid.attach(self.e_numero, 1, 3, 1,1)
                grid.attach_next_to(l_numero, self.e_numero, Gtk.PositionType.TOP, 1, 1)
                grid.attach(self.c_modelo, 1, 5, 1,1)
                grid.attach_next_to(l_modelo, self.c_modelo, Gtk.PositionType.TOP, 1, 1)
                grid.attach(self.e_placa, 1, 7, 1, 1)
                grid.attach_next_to(l_placa, self.e_placa, Gtk.PositionType.TOP, 1, 1)
                grid.attach(self.e_km, 1, 9, 1, 1)
                grid.attach_next_to(l_km, self.e_km, Gtk.PositionType.TOP, 1, 1)
                grid.attach(self.e_valor, 1, 11, 1, 1)
                grid.attach_next_to(l_valor, self.e_valor, Gtk.PositionType.TOP, 1, 1)
                grid.attach(self.scroll, 1, 13, 1, 2)
                grid.attach_next_to(l_servico, self.scroll, Gtk.PositionType.TOP, 1, 1)
                grid.attach(self.botao, 1, 15, 1, 1)
                
                


        def salvar(self, botao):
                #capturas
                nome = self.e_nome.get_text()
                numero = self.e_numero.get_text()
                placa = self.e_placa.get_text()
                mod = self.c_modelo.get_active_text()
                km = self.e_km.get_text()
                valor = self.e_valor.get_text()
                inicio = self.e_servico.get_start_iter()#inicio do texto
                fim = self.e_servico.get_end_iter()#fim do texto
                servico = self.e_servico.get_text(inicio,fim,False)
                #formataçao de strings
                nome = nome.title()
                placa = placa.upper()
                Info = ("\n" + strftime("%d/%m/%Y") + '\nNome: ' + nome +
                '.\nTelefone: ' + numero + "\nModelo: " + mod +
                "\nPlaca: "+ placa + "\nQuilometragem: "+ km +
                "\nValor: " + valor + "\nServico: \n"+ servico)
                #Tela de Pop Up
                popup = Gtk.MessageDialog(parent=self, flags=0,
                message_type=Gtk.MessageType.WARNING,
                buttons=Gtk.ButtonsType.NONE, text="Tudo Certo?")
                popup.format_secondary_text(Info)
                popup.add_buttons("Voltar", Gtk.ResponseType.CANCEL,
                Gtk.STOCK_OK, Gtk.ResponseType.OK)
                response = popup.run()
                if response == Gtk.ResponseType.OK: #salvar
                        f = open((caminho + "/"+  nome + " " +
                                  strftime("%d %m %Y")),"a+")
                        f.write(Info)
                        f.close()
                elif response == Gtk.ResponseType.CANCEL: #esquecer
                        pass
                popup.destroy()

Jan = Janela()
Jan.connect("destroy", Gtk.main_quit)
Jan.show_all()
Gtk.main()

