import PySimpleGUI as sg


sg.theme('Reddit')


if __name__ == '__main__':
    layout = [
        [sg.Text('Valor das parcelas:'), sg.InputText(key='parcel')],
        [sg.Text('Número de parcelas:'), sg.Input(key='number_of_installments', enable_events=True)],
        [sg.Text('Taxa:'), sg.Input(key='interest_rate', enable_events=True)],
        [sg.Button('Calcular')],
    ]
    window = sg.Window('Simulação empréstimo', layout, resizable=False, size=(250, 116), element_justification='c')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event in ['number_of_installments', 'interest_rate'] and not values[event].isdigit():
            window[event].update(values[event][:-1])
    window.close()
