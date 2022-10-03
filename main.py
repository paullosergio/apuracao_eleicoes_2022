import requests
import json
import pandas as pd
import time
import os
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR')

while True:
    os.system('cls')
    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

    json_data = json.loads(data.content)
    candidato = []
    partido = []
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:

        if informacoes['seq'] in ['1', '2', '3', '4']:
            candidato.append(informacoes['nm'])
            partido.append(informacoes['cc'][0:3])
            votos.append(
            locale.format_string(
                '%d',
                int(informacoes['vap']),
                grouping=True)
            )
            porcentagem.append(informacoes['pvap'] + ' %')

    df_eleicao = pd.DataFrame(list(zip(candidato, partido, votos, porcentagem)), columns=[
        'Candidato', 'Partido', 'Nº de Votos', 'Porcentagem'
    ])
    print(f"Porcentagem das runas apuradas: {json_data['pst']}%.\n")

    print(df_eleicao)
    time.sleep(5)

    # Emulando um do-while
    if float(json_data['pst'].replace(',', '.')) == float(100):
        break

