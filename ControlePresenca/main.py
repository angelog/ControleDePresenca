import PySimpleGUI as sg
from dataBaseManager import DataBase


class App:

    def __init__(self):
        self.conn = DataBase()
        self.run()

    def windowRegistrar(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Informe seu RG')],
            [sg.Input(key='Rg')],
            [sg.Button('Registrar'), sg.Button('Cadastrar')]
        ]
        return sg.Window('Registro de Preseça', layout=layout, icon='relogio.ico').finalize()

    def windowCadastro(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Nome Completo:')],
            [sg.Input(key='Nome')],
            [sg.Text('Informe o RG:')],
            [sg.Input(key='Rg')],
            [sg.Text('Telefone  para contato:')],
            [sg.Input(key='Tel')],
            [sg.Text('Nome do responsavel:')],
            [sg.Input(key='Responsavel')],
            [sg.Button('Cadastrar'), sg.Button('Registrar presença')]
        ]
        return sg.Window('Cadastro', layout=layout, icon='relogio.ico').finalize()

    def registrar(self, values):
        self.conn.insert('Presenca', values)
        sg.popup('Presença confirmada')

    def cadastrar(self, values):
        self.conn.insert('Alunos', values)
        sg.popup(f"Cadastro de {values['Nome']} realizado")

    def run(self):
        window1, window2 = self.windowRegistrar(), None

        while True:
            window, event, values = sg.read_all_windows()

            if window == window1:
                if event == sg.WINDOW_CLOSED:
                    break

                elif event == 'Registrar':
                    self.registrar(values)
                    window1['Rg'].update('')

                elif event == 'Cadastrar':
                    window1.hide()
                    window2 = self.windowCadastro()
                    window1['Rg'].update('')

            elif window == window2:
                if event == sg.WINDOW_CLOSED:
                    window2.hide()
                    window1.un_hide()

                elif event == 'Cadastrar':

                    if values['Nome'] == '' or values['Rg'] == '' or values['Responsavel'] == '':
                        print(values)
                        sg.popup('Nome, RG ou Responsavel não informado!')
                    else:
                        self.cadastrar(values)
                        for keys in values:
                            window2[keys].update('')
                elif event == 'Registrar presença':
                    window2.hide()
                    window1.un_hide()


if __name__ == '__main__':
    App()
