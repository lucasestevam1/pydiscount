import PySimpleGUI as sg
class Tela():
    def __init__(self):
        sg.theme('Reddit')
        resultado = float()
        layout = [
            [sg.Text('Calcular desconto: ',size=(15, 0))],
            [sg.Text('Preço: ',size=(15, 0)), sg.Input(size=(20 , 0))],
            [sg.Text('Desconto :        %',size=(15, 0)), sg.Input(size=(20 , 0))],
            [sg.Button('Calcular')],
            [sg.Output(size=(80,30))],
            ]
        self.janela = sg.Window("Calculadora").layout(layout)
    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            valores = self.values
            # 0 = Preço
            # 1 = Porcentagem
            valor = valores[0]
            porcentagem = valores[1]
            v = True
            v1 = True
            v2 = True
            for n in valor:
                if n.isspace() == True:
                    print('Não deixe espaços vazios. ')
                    v2 = False
                elif n == ',':
                    print('Use "." ao invés de vírgula no preço. ')
                    v = False
                elif n.isalpha() == True:
                    if n != ',' or n != '.':
                        print(f'Operação inválida. Use números e "." no preço. ')
                        v1 = False
            for n in porcentagem:
                if n == '':
                    v2 = False
                elif n == ',':
                    print('Use "." ao invés de vírgula no desconto. ')
                    v = False                
                elif n.isalpha() == True:
                    if n != ',' or n != '.':
                        print(f'Operação inválida. Use números e "." na desconto. ')                            
                        v1 = False 
            if v == True and v1 == True and v2 == True:
                valor = float(valores[0])
                porcentagem = float(valores[1])
                resultado = (porcentagem/100) * valor
                desconto = valor - resultado
                print(f'{porcentagem}% de {valor} é {resultado}. O resultado é: {desconto}')
tela = Tela()
tela.iniciar()
