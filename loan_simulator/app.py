import PySimpleGUI as sg
from domain import calc


sg.theme('Reddit')


if __name__ == '__main__':
    layout = [
        [sg.Text('Valor da parcela:'), sg.Input(key='parcel', enable_events=True)],
        [sg.Text('Taxa de juros (ao mês):'), sg.Input(key='interest_rate', enable_events=True)],
        [sg.Text('Dia de vencimento:'), sg.Input(key='due_day', enable_events=True)],
        [sg.Text('Data de quitação:'), sg.Input(key='payday', enable_events=True)],
        [sg.Text('Quantidade de parcelas:'), sg.Input(key='number_of_parcels', enable_events=True)],
        [sg.Text('Resultado: ', size=(20,1), key='-OUTPUT-')],
        [sg.Button('Calcular')],
    ]
    window = sg.Window('Simulação empréstimo', layout, finalize=True, resizable=False, element_justification='c')
    window.size = (250, window.size[1])
    FLOAT_VALIDATOR = '0123456789,'
    INTEGER_VALIDATOR = '0123456789'
    DATE_VALIDATOR = '0123456789/'
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event in ['interest_rate', 'parcel'] and values[event] and values[event][-1] not in FLOAT_VALIDATOR:
            window[event].update(values[event][:-1])
        elif event in ['due_day', 'number_of_parcels'] and values[event] and values[event][-1] not in INTEGER_VALIDATOR:
            window[event].update(values[event][:-1])
        elif event in ['payday'] and values[event] and values[event][-1] not in DATE_VALIDATOR:
            window[event].update(values[event][:-1])
        elif event == 'Calcular':
            result = calc(values['parcel'], values['interest_rate'], values['due_day'], values['payday'], values['number_of_parcels'])
            window['-OUTPUT-'].update('Resultado: ' + result)
    window.close()
