from datetime import date
import requests
import re


def calc(parcel: str, interest_rate: str, due_day: str, discharge_date: str, parcels_amount: str) -> str:
    response = requests.post('https://www.mpsc.mp.br/calculadora-de-antecipacao-atualizada', verify=False, data={
        'txfValor': parcel,
        'txfTaxaJuros': interest_rate,
        'txfDiaVencimento': due_day,
        'txfDataQuitacao': discharge_date,
        'txfQtdParcelas': parcels_amount,
    })
    regex = re.compile(r'Valor total para.* em \d{2}/\d{2}/\d{4}: (R\$.*)</b>', re.DOTALL)
    return regex.findall(str(response.content))[0].strip()
