import PySimpleGUI as sg

class Tela():
    def __init__(self):
        sg.theme('Reddit')
        resultado = float()
        layout = [
            [sg.Text('Calcular desconto: ',size=(15, 0))],
            [sg.Text('Valor: ',size=(15, 0)), sg.Input(size=(20 , 0))],
            [sg.Text('Desconto :        %',size=(15, 0)), sg.Input(size=(20 , 0))],
            [sg.Button('Calcular')],
            [sg.Output(size=(30,20))],
            ]
        self.janela = sg.Window("Calculadora").layout(layout)
                    
    def iniciar(self):
        while True:
            
            self.button, self.values = self.janela.Read()
            valores = self.values
            # 0 = Valor
            # 1 = Porcentagem
            valor = float(valores[0])
            porcentagem = float(valores[1])
            self.resultado = valor - (porcentagem/100) * valor
            print(f'O resultado é {self.resultado}')
tela = Tela()
tela.iniciar()
